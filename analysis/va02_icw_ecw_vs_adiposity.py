#!/usr/bin/env python3
"""
VA-02 — Does the reported ECW/ICW-vs-adiposity association survive normalisation to
fat-free mass? Is the extra water in obesity INTRACELLULAR or EXTRACELLULAR?

================================================================================
ANALYSIS PLAN — written before the data were touched (guide R13). Do not revise.
================================================================================

WHY
  H4 §4.6 found a reported positive association between whole-body ECW/ICW ratio and
  percent body fat, and flagged a confound that makes it potentially meaningless:
  adipose tissue itself has low water content and a high extracellular fraction, so
  ADDING FAT MASS RAISES ECW/ICW MECHANICALLY with no cell-level change at all.
  H4 §5 named the fix: normalise to fat-free mass. NHANES 2001-2004 carries
  multifrequency bioimpedance (5 kHz - 1 MHz) with derived ICW and ECW, plus DXA, so
  the fix is computable.

  This matters because three independent lines now point extracellular rather than
  intracellular (VA-01's plasma null, H1 §1.5's oedema finding, H4 §4.6), against the
  cell-swelling premise that H1 was built on.

AVOIDING A CIRCULARITY THAT WOULD INVALIDATE THE WHOLE THING
  The outcome (ICW, ECW) is BIA-derived. So the exposure and the normaliser must NOT
  be BIA-derived, or the analysis is impedance regressed on impedance.
      Exposure   = DXA total body fat %        (DXDTOPF)
      Normaliser = DXA fat-free mass           (lean soft tissue + bone mineral content)
      Outcome    = BIA ICW, ECW                (BIDICF, BIDECF)
  BIDPFAT and BIDFFM are deliberately NOT used for anything.

WHAT THIS CAN AND CANNOT ESTABLISH — stated before seeing results
  CAN: whether the published ECW/ICW-vs-fat association survives compositional
       normalisation. That is a question about the published claim, and it is
       answerable.
  CANNOT: whether cells genuinely hold more or less water in obesity. BIA-derived
       compartment estimates rest on Cole modelling and Hanai mixture theory whose
       geometric assumptions are violated by obese body shape, and the validity of
       ICW/ECW partitioning in obesity is contested. A positive result could be an
       equation artefact. This limit is not a caveat added afterwards; it bounds the
       claim from the outset.

SINGLE PRIMARY OUTCOME
  Coefficient on DXA fat % in a weighted regression of  ICW / DXA-FFM  (kg/kg),
  adjusted for age, sex, race/ethnicity and height.
  If lean tissue holds more intracellular water as adiposity rises, this is positive.

PRE-SPECIFIED INTERPRETATION RULE
  Let b_icw and b_ecw be coefficients for ICW/FFM and ECW/FFM respectively.
  (a) b_icw > 0 (CI excludes 0)
        -> intracellular water per unit lean mass RISES with adiposity. Consistent
           with the cell-swelling premise. Would be the first measurement in this
           project to support it.
  (b) b_icw ~ 0 and b_ecw > 0
        -> the extra water is EXTRACELLULAR. Supports H1b' interstitial route and is
           evidence AGAINST cell swelling. Also explains the raw ECW/ICW association
           as compositional.
  (c) b_icw < 0
        -> intracellular water per lean mass FALLS with adiposity. Strongest possible
           result against the swelling premise; H1's cellular form should then be
           declared dead rather than merely unsupported.
  (d) both > 0 and similar
        -> generalised water expansion with no compartment specificity; uninformative
           for the mechanism.

SECONDARY
  - Raw ECW/ICW ratio on fat %, to check we reproduce the published association at all
    before claiming anything about normalising it away.
  - TBW/FFM, to see whether total hydration of lean mass moves.
  - Men and women separately.
  - Replication across the two cycles (2001-2002, 2003-2004) independently. A result
    that does not reproduce is not a finding.

LIMITATIONS, stated in advance
  1. BIA compartment validity in obesity (above). This is the dominant limitation.
  2. Cross-sectional; no direction (guide R9).
  3. NHANES DXA 1999-2004 is released as FIVE MULTIPLE IMPUTATIONS per person. This
     script averages the five per SEQN. Rubin's rules would propagate imputation
     variance properly; averaging slightly UNDERSTATES standard errors. Acceptable for
     a direction question, not for a borderline p-value, and flagged as such.
  4. Survey design handled as weighted least squares with cluster-robust SEs by
     stratum/PSU — approximate, not a full Taylor-series survey estimator.
  5. BIA was restricted by age in these cycles; the analytic sample is whatever
     overlaps DXA, so generalisability is limited to that band.
  6. BIAEXSTS/BIDFIT quality flags are used to exclude non-complete or poor-fit exams.

OUTPUT
  All headline numbers to CSV.
"""

import pathlib
import numpy as np
import pandas as pd
import statsmodels.api as sm

NH = pathlib.Path("/tmp/claude-0/-home-user-ObesityResearch/"
                  "adff2785-3368-5e53-b009-ff689b2a4ae8/scratchpad/nh")
OUT = pathlib.Path(__file__).resolve().parent / "output"
OUT.mkdir(exist_ok=True)

rows, notes = [], []


def read(n):
    return pd.read_sas(NH / f"{n}.xpt", format="xport")


def build(cycle):
    """cycle: 'B' = 2001-2002, 'C' = 2003-2004."""
    demo = read(f"DEMO_{cycle}")[["SEQN", "RIAGENDR", "RIDAGEYR", "RIDRETH1",
                                  "WTMEC2YR", "SDMVPSU", "SDMVSTRA"]]
    bmx = read(f"BMX_{cycle}")[["SEQN", "BMXHT", "BMXBMI"]]

    bia = read(f"BIX_{cycle}")
    bia = bia[["SEQN", "BIDECF", "BIDICF", "BIDTBW", "BIAEXSTS", "BIDFIT"]]
    notes.append((cycle, "bia_rows", len(bia)))
    # QUALITY FILTER — CORRECTED 2026-10-02 after an error worth recording (guide R19).
    # My first version used (BIAEXSTS==1) & (BIDFIT==1) on the assumption that BIDFIT
    # was a good-fit flag with 1=good. Inspecting the distributions showed otherwise:
    #   BIAEXSTS: 1 in 4709/4298 cases, and BIAEXSTS==1 exactly coincides with having
    #             non-null derived ICF/ECF -> 1 = complete exam. Correct filter.
    #   BIDFIT:   modal value 0 (4380/3988 cases), then 7, then small counts at 1-5.
    #             That is the shape of a COUNT OF FIT PROBLEMS, not a 1=good flag, so
    #             BIDFIT==1 selected a tiny unrepresentative subgroup and collapsed n
    #             from 5949 to 99. The original filter was wrong and its results were
    #             discarded unreported.
    # Primary filter is BIAEXSTS==1 only (certain). BIDFIT==0 is carried as a
    # sensitivity, on the INFERENCE that 0 means no fit flag raised - inference,
    # because the codebook page could not be retrieved.
    bia = bia[bia.BIAEXSTS == 1]
    notes.append((cycle, "bia_after_quality", len(bia)))

    dxa = read(f"DXX_{cycle}")
    keep = [c for c in ["SEQN", "DXDTOPF", "DXDTOLE", "DXDTOBMC", "DXAEXSTS"]
            if c in dxa.columns]
    dxa = dxa[keep]
    notes.append((cycle, "dxa_rows_with_imputations", len(dxa)))
    # average the five multiple imputations per person (limitation 3)
    dxa = dxa.groupby("SEQN", as_index=False).mean(numeric_only=True)
    notes.append((cycle, "dxa_persons", len(dxa)))

    df = demo.merge(bmx, on="SEQN").merge(bia, on="SEQN").merge(dxa, on="SEQN")

    df["female"] = (df.RIAGENDR == 2).astype(int)
    df["age"] = df.RIDAGEYR
    # DXA fat-free mass: lean soft tissue + bone mineral content, g -> kg
    df["ffm_dxa"] = (df.DXDTOLE + df.DXDTOBMC) / 1000.0
    df["fat_pct"] = df.DXDTOPF

    df["icw_ffm"] = df.BIDICF / df.ffm_dxa
    df["ecw_ffm"] = df.BIDECF / df.ffm_dxa
    df["tbw_ffm"] = df.BIDTBW / df.ffm_dxa
    df["ecw_icw"] = df.BIDECF / df.BIDICF

    need = ["icw_ffm", "ecw_ffm", "tbw_ffm", "ecw_icw", "fat_pct", "ffm_dxa",
            "BMXHT", "WTMEC2YR", "age", "female", "RIDRETH1"]
    df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=need)
    df = df[(df.WTMEC2YR > 0) & (df.ffm_dxa > 10) & (df.fat_pct > 0)]
    df = df[df.age >= 20]            # adults, consistent with VA-01
    notes.append((cycle, "analytic_n", len(df)))
    notes.append((cycle, "age_min", int(df.age.min())))
    notes.append((cycle, "age_max", int(df.age.max())))
    return df


def fit(df, outcome, label, cycle):
    d = df.dropna(subset=[outcome]).copy()
    X = pd.DataFrame(index=d.index)
    X["fat_pct"] = d.fat_pct
    X["age"] = d.age
    X["female"] = d.female
    X["height"] = d.BMXHT
    for lev in sorted(d.RIDRETH1.unique())[1:]:
        X[f"eth_{int(lev)}"] = (d.RIDRETH1 == lev).astype(float)
    X = sm.add_constant(X)
    g = d.SDMVSTRA.astype(int).astype(str) + "_" + d.SDMVPSU.astype(int).astype(str)
    m = sm.WLS(d[outcome], X, weights=d.WTMEC2YR).fit(
        cov_type="cluster", cov_kwds={"groups": g})
    ci = m.conf_int()
    sd_out = np.sqrt(np.average((d[outcome] - np.average(d[outcome], weights=d.WTMEC2YR))**2,
                               weights=d.WTMEC2YR))
    rows.append(dict(cycle=cycle, model=label, outcome=outcome, term="fat_pct",
                     beta=m.params["fat_pct"], se=m.bse["fat_pct"],
                     p=m.pvalues["fat_pct"],
                     ci_low=ci.loc["fat_pct", 0], ci_high=ci.loc["fat_pct", 1],
                     outcome_wsd=sd_out,
                     beta_per_10pct_fat=m.params["fat_pct"] * 10,
                     n=int(m.nobs), n_clusters=g.nunique()))


def run(cycle):
    df = build(cycle)
    fit(df, "icw_ffm", "PRIMARY_icw_per_ffm", cycle)      # the primary
    fit(df, "ecw_ffm", "sec_ecw_per_ffm", cycle)
    fit(df, "ecw_icw", "sec_raw_ecw_icw_ratio", cycle)    # replicate published assoc
    fit(df, "tbw_ffm", "sec_tbw_per_ffm", cycle)
    fit(df[df.female == 1], "icw_ffm", "sens_women_icw_ffm", cycle)
    fit(df[df.female == 0], "icw_ffm", "sens_men_icw_ffm", cycle)
    d0 = df[df.BIDFIT == 0]
    if len(d0) > 200:
        fit(d0, "icw_ffm", "sens_bidfit0_icw_ffm", cycle)
        fit(d0, "ecw_ffm", "sens_bidfit0_ecw_ffm", cycle)
    w = df.WTMEC2YR
    for v in ["fat_pct", "ffm_dxa", "BIDICF", "BIDECF", "BIDTBW",
              "icw_ffm", "ecw_ffm", "ecw_icw"]:
        mu = np.average(df[v], weights=w)
        notes.append((cycle, f"wmean_{v}", round(float(mu), 4)))


if __name__ == "__main__":
    for cyc in ["B", "C"]:
        run(cyc)
    res = pd.DataFrame(rows)
    res.to_csv(OUT / "va02_results.csv", index=False)
    pd.DataFrame(notes, columns=["cycle", "item", "value"]).to_csv(
        OUT / "va02_notes.csv", index=False)
    pd.set_option("display.width", 220, "display.max_columns", 50)
    print("\n=== PRIMARY: ICW per kg DXA fat-free mass, on DXA fat % ===")
    print(res[res.model == "PRIMARY_icw_per_ffm"].to_string(index=False))
    print("\n=== ALL ===")
    print(res.to_string(index=False))
