#!/usr/bin/env python3
"""
VA-01 — Does CALCULATED PLASMA OSMOLARITY associate with DXA fat mass, and does the
association live in the EFFECTIVE (tonicity) component or in the UREA component?

================================================================================
ANALYSIS PLAN — written before the data were touched (guide R13). Do not revise.
================================================================================

WHY THIS QUESTION
  guide.md Q5 asks whether plasma tonicity, as opposed to total osmolality, tracks
  adiposity. guide.md §1.2 makes the decomposition that matters: urea is an
  INEFFECTIVE osmole (equilibrates across membranes, does not move water), while
  Na+ and glucose are EFFECTIVE. So if any cell-volume account is to survive, the
  association must sit in the effective component. If it sits in urea, guide Q5
  states the consequence plainly: the cell-volume premise is dead and should be
  declared dead.

  Every intervention trial in interventions.md used limb volume, skin thickness,
  bioimpedance or a biomarker (§F). This script uses DXA total body fat — the
  endpoint the project has repeatedly said is missing.

NAMING, per guide R1 (non-negotiable)
  What is computed here is CALCULATED OSMOLARITY (mOsm/L), NOT measured osmolality.
  It is a formula applied to concentrations, so it is volume-based and carries the
  plasma-solids problem. The formula is stated below. It must never be labelled
  "osmolality" anywhere in the output.

      effective_osm = 2*[Na+] + [glucose]/18          <- tonicity, mOsm/L
      urea_osm      = [BUN]/2.8                        <- ineffective osmole
      calc_osm      = effective_osm + urea_osm         <- the usual formula

  Units: Na mmol/L, glucose mg/dL, BUN mg/dL.

SINGLE PRIMARY OUTCOME
  The coefficient on effective_osm in a weighted linear regression of
  DXA total body fat percent (DXDTOPF) on effective_osm + urea_osm, adjusted for
  age, sex, race/ethnicity, eGFR and HbA1c.
  ONE primary outcome. Everything else below is secondary or sensitivity.

PRE-SPECIFIED INTERPRETATION RULE (written now so it cannot drift)
  Let b_eff and b_urea be the coefficients, with cluster-robust 95% CIs.
  (a) b_eff > 0, CI excludes 0, AND b_urea CI includes 0
          -> consistent with a tonicity-adiposity association. Does NOT establish
             direction (see LIMITATIONS). Records as hypothesis-supporting only.
  (b) b_urea CI excludes 0 and |b_urea| comparable to or larger than |b_eff|
          -> the association is carried by an INEFFECTIVE osmole. Under guide Q5
             this KILLS the cell-volume premise. Record it as such, do not soften.
  (c) Both CIs include 0
          -> no detectable association in this dataset. Report as null, with the
             achieved precision, so the null is interpretable rather than merely
             negative.
  (d) Both CIs exclude 0 in the same direction
          -> the decomposition does not discriminate; most likely both are tracking
             a third variable (renal function, hydration, or adiposity itself).
             Report as uninformative for the mechanism, not as support.

SECONDARY (reported, never promoted to primary)
  - Same model with DXA fat mass index (total fat kg / height m^2) as outcome.
  - Same model with BMI, to see whether DXA changes the answer versus BMI. This is
    the project's own complaint about endpoints, tested directly.
  - Sodium alone and glucose alone, to see which half of the effective term carries
    anything.
  - Replication in an independent cycle (2013-2014) with the identical model. A
    result that does not reproduce across cycles is not recorded as a finding.

SENSITIVITY
  - Exclude triglycerides > 400 mg/dL. Rationale (guide §1.1): high TG lowers the
    plasma water fraction, and indirect ion-selective electrodes then under-read
    sodium (pseudohyponatremia). That artefact would act directly on the exposure.
  - Exclude eGFR < 60.
  - Men and women separately (the project has repeatedly met sex asymmetry).

LIMITATIONS, stated in advance
  1. CROSS-SECTIONAL. Direction is not identified. guide R9 applies with force:
     adiposity itself alters hydration, plasma volume, plasma water fraction and
     AVP tone. A positive result cannot be read as "tonicity causes fat."
  2. CALCULATED, not measured (R1). No osmometry in NHANES, so the osmolal gap
     cannot be checked and unmeasured solutes are invisible.
  3. Serum glucose in BIOPRO is not reliably fasting, which adds noise to the
     effective term. HbA1c is carried as a fasting-independent glycaemia control.
  4. DXA is limited to ages 8-59; adults 20-59 are used, so this says nothing
     about older adults.
  5. Survey design is handled as weighted least squares with cluster-robust
     standard errors by stratum/PSU. This approximates, and does not exactly
     reproduce, a full Taylor-series survey variance. Treat CIs as approximate.
  6. Effect sizes on a few-mOsm exposure will be small by construction. The
     question is direction and which component, not magnitude.

OUTPUT
  Every headline number is written to CSV (guide: a result that exists only in
  console output has to be recomputed to be verified).
"""

import pathlib
import numpy as np
import pandas as pd
import statsmodels.api as sm

NH = pathlib.Path("/tmp/claude-0/-home-user-ObesityResearch/"
                  "adff2785-3368-5e53-b009-ff689b2a4ae8/scratchpad/nh")
OUT = pathlib.Path(__file__).resolve().parent / "output"
OUT.mkdir(exist_ok=True)

rows = []          # tidy results, one row per model term
notes = []         # provenance / n-tracking


def read(name):
    return pd.read_sas(NH / f"{name}.xpt", format="xport")


def egfr_ckdepi2021(scr, age, female):
    """CKD-EPI 2021 creatinine equation (race-free)."""
    kappa = np.where(female, 0.7, 0.9)
    alpha = np.where(female, -0.241, -0.302)
    r = scr / kappa
    return (142.0 * np.minimum(r, 1.0) ** alpha * np.maximum(r, 1.0) ** -1.200
            * 0.9938 ** age * np.where(female, 1.012, 1.0))


def build(cycle):
    """cycle: 'J' = 2017-2018, 'H' = 2013-2014."""
    demo = read(f"DEMO_{cycle}")[["SEQN", "RIAGENDR", "RIDAGEYR", "RIDRETH3",
                                  "WTMEC2YR", "SDMVPSU", "SDMVSTRA"]]
    bio = read(f"BIOPRO_{cycle}")[["SEQN", "LBXSNASI", "LBXSGL", "LBXSBU",
                                   "LBXSCR", "LBXSTR"]]
    bmx = read(f"BMX_{cycle}")[["SEQN", "BMXBMI", "BMXHT"]]
    ghb = read(f"GHB_{cycle}")[["SEQN", "LBXGH"]]
    dxx = read(f"DXX_{cycle}")[["SEQN", "DXDTOPF", "DXDTOFAT"]]

    df = demo.merge(bio, on="SEQN").merge(bmx, on="SEQN") \
             .merge(ghb, on="SEQN").merge(dxx, on="SEQN")
    notes.append((cycle, "merged_rows", len(df)))

    df["female"] = (df.RIAGENDR == 2).astype(int)
    df["age"] = df.RIDAGEYR
    df["eGFR"] = egfr_ckdepi2021(df.LBXSCR, df.age, df.female == 1)

    # --- the decomposition this whole analysis exists for (guide §1.2) ---
    df["effective_osm"] = 2.0 * df.LBXSNASI + df.LBXSGL / 18.0
    df["urea_osm"] = df.LBXSBU / 2.8
    df["calc_osm"] = df.effective_osm + df.urea_osm

    df["fat_pct"] = df.DXDTOPF
    df["fmi"] = (df.DXDTOFAT / 1000.0) / (df.BMXHT / 100.0) ** 2   # fat mass index

    df = df[(df.age >= 20) & (df.age <= 59)]
    notes.append((cycle, "age_20_59", len(df)))

    need = ["effective_osm", "urea_osm", "fat_pct", "fmi", "BMXBMI",
            "eGFR", "LBXGH", "WTMEC2YR", "age", "female", "RIDRETH3"]
    df = df.dropna(subset=need)
    df = df[df.WTMEC2YR > 0]
    notes.append((cycle, "complete_case", len(df)))
    return df


def fit(df, outcome, exposures, label, cycle):
    """Weighted LS, cluster-robust by stratum+PSU. Returns nothing; appends rows."""
    d = df.dropna(subset=[outcome] + exposures).copy()
    X = pd.DataFrame(index=d.index)
    for e in exposures:
        X[e] = d[e]
    X["age"] = d.age
    X["female"] = d.female
    X["eGFR"] = d.eGFR
    X["hba1c"] = d.LBXGH
    for lev in sorted(d.RIDRETH3.unique())[1:]:          # dummy, first as reference
        X[f"eth_{int(lev)}"] = (d.RIDRETH3 == lev).astype(float)
    X = sm.add_constant(X)
    groups = d.SDMVSTRA.astype(int).astype(str) + "_" + d.SDMVPSU.astype(int).astype(str)

    m = sm.WLS(d[outcome], X, weights=d.WTMEC2YR).fit(
        cov_type="cluster", cov_kwds={"groups": groups})
    ci = m.conf_int()
    for e in exposures:
        rows.append(dict(cycle=cycle, model=label, outcome=outcome, term=e,
                         beta=m.params[e], se=m.bse[e], p=m.pvalues[e],
                         ci_low=ci.loc[e, 0], ci_high=ci.loc[e, 1],
                         n=int(m.nobs), n_clusters=groups.nunique()))


def run(cycle):
    df = build(cycle)

    # ---------------- PRIMARY ----------------
    fit(df, "fat_pct", ["effective_osm", "urea_osm"], "PRIMARY_decomposed", cycle)

    # ---------------- SECONDARY ----------------
    fit(df, "fmi", ["effective_osm", "urea_osm"], "sec_fmi", cycle)
    fit(df, "BMXBMI", ["effective_osm", "urea_osm"], "sec_bmi", cycle)
    fit(df, "fat_pct", ["calc_osm"], "sec_total_osm_only", cycle)
    fit(df, "fat_pct", ["LBXSNASI", "LBXSGL", "urea_osm"], "sec_split_na_glu", cycle)

    # ---------------- SENSITIVITY ----------------
    fit(df[df.LBXSTR <= 400], "fat_pct", ["effective_osm", "urea_osm"],
        "sens_TG_le_400", cycle)
    fit(df[df.eGFR >= 60], "fat_pct", ["effective_osm", "urea_osm"],
        "sens_eGFR_ge_60", cycle)
    fit(df[df.female == 1], "fat_pct", ["effective_osm", "urea_osm"],
        "sens_women", cycle)
    fit(df[df.female == 0], "fat_pct", ["effective_osm", "urea_osm"],
        "sens_men", cycle)

    # descriptive, for interpretability of a few-mOsm exposure
    w = df.WTMEC2YR
    for v in ["effective_osm", "urea_osm", "calc_osm", "fat_pct", "fmi", "BMXBMI", "eGFR"]:
        mu = np.average(df[v], weights=w)
        sd = np.sqrt(np.average((df[v] - mu) ** 2, weights=w))
        notes.append((cycle, f"wmean_{v}", round(float(mu), 3)))
        notes.append((cycle, f"wsd_{v}", round(float(sd), 3)))


if __name__ == "__main__":
    for cyc in ["J", "H"]:
        run(cyc)

    res = pd.DataFrame(rows)
    res.to_csv(OUT / "va01_results.csv", index=False)
    pd.DataFrame(notes, columns=["cycle", "item", "value"]).to_csv(
        OUT / "va01_notes.csv", index=False)

    pd.set_option("display.width", 200, "display.max_columns", 50)
    print("\n=== PRIMARY: DXA total body fat %, osmolarity decomposed ===")
    print(res[res.model == "PRIMARY_decomposed"].to_string(index=False))
    print("\n=== ALL MODELS ===")
    print(res.to_string(index=False))
    print(f"\nwrote {OUT/'va01_results.csv'}")
