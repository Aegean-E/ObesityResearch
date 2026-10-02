# VA-01 — Calculated plasma osmolarity vs DXA body fat: a replicated null

**Script:** [`va01_tonicity_vs_dxa_fat.py`](va01_tonicity_vs_dxa_fat.py) (plan in docstring,
written before the data were touched, guide R13)
**Outputs:** [`output/va01_results.csv`](output/va01_results.csv) ·
[`output/va01_notes.csv`](output/va01_notes.csv)
**Data:** NHANES 2017–2018 (cycle J) and 2013–2014 (cycle H), adults 20–59 with DXA.
**Run:** 2026-10-02 · **This is the project's first computed result.**

---

## 0. Answer

**[guide.md](../guide.md) Q5 — "is there any human evidence that plasma tonicity, as opposed to
total osmolality, tracks adiposity?" — is answered: NO, in these data.**

Pre-specified interpretation rule **(c)** applies: both coefficients' confidence intervals
include zero, in **both independent cycles**. Not the "urea carries it" outcome (rule b) that
would have killed the cell-volume premise outright — the weaker and plainer result that
**neither component is associated with body fat at all.**

**n = 2,119 (J) + 2,988 (H) = 5,107 adults**, with **DXA total body fat** as the outcome — the
endpoint this project has repeatedly complained is missing from the literature.

---

## 1. Primary result

Weighted linear regression of **DXA total body fat %** on calculated osmolarity decomposed into
its effective and ineffective parts, adjusted for age, sex, race/ethnicity, eGFR (CKD-EPI 2021)
and HbA1c. Cluster-robust SEs by stratum/PSU, 30 clusters per cycle.

| Cycle | Term | β (fat % per mOsm/L) | 95% CI | p |
|---|---|---|---|---|
| **J** 2017–18 | **effective_osm** (2Na + glu/18) | **−0.048** | [−0.127, +0.030] | 0.23 |
| **J** | **urea_osm** (BUN/2.8) | **−0.183** | [−0.399, +0.034] | 0.098 |
| **H** 2013–14 | **effective_osm** | **−0.010** | [−0.075, +0.055] | 0.76 |
| **H** | **urea_osm** | **−0.078** | [−0.350, +0.194] | 0.57 |

### Expressed per 1 SD of exposure, so the null is interpretable rather than merely negative

| Cycle | Term | β per SD (fat % points) | 95% CI |
|---|---|---|---|
| J | effective_osm (SD 5.21 mOsm/L) | **−0.25** | [−0.66, +0.16] |
| J | urea_osm (SD 1.52) | −0.28 | [−0.61, +0.05] |
| H | effective_osm (SD 4.25) | **−0.04** | [−0.32, +0.23] |
| H | urea_osm (SD 1.49) | −0.12 | [−0.52, +0.29] |

**Fat % SD is ~8.4 points.** So the data bound the association at roughly **0.08 SD of body fat
per SD of tonicity**, in either direction. This is not an underpowered null — it is a reasonably
tight one, and it excludes any effect of a size that would matter.

**Direction, where there is any hint of one, is negative** — higher calculated osmolarity with
*less* body fat. That is opposite to the hypothesis the measurement was meant to test.

---

## 2. Secondary and sensitivity: nothing rescues it

| Model | Result |
|---|---|
| Fat mass index instead of fat % | null, both cycles |
| **BMI** instead of DXA fat | **null, both cycles** |
| Total calculated osmolarity undecomposed | null, both cycles |
| Sodium and glucose entered separately | null (glucose in H: p=0.054, direction positive, does not replicate in J) |
| Exclude triglycerides > 400 mg/dL (pseudohyponatremia guard) | null |
| Exclude eGFR < 60 | see §3 |
| Women only / men only | null in both cycles, **no sex asymmetry** |

**Two of these matter beyond being null.**

**(i) DXA did not rescue it.** The project has argued repeatedly — correctly, for the
intervention literature — that limb volume and bioimpedance conflate fat with fluid. Here the
proper endpoint was available and used, and **it gave the same answer as BMI**. So the
endpoint critique, valid as it is elsewhere, does **not** explain the absence of an
osmolarity–adiposity association. That had to be checked and it was.

**(ii) No sex asymmetry.** Sessions on the vasopressin axis repeatedly anticipated one
(oestrogen lowers the AVP osmotic threshold). Women and men are both null, and the sign flips
between cycles. **Expectation not met.**

---

## 3. The one nominally significant term, and why it is not promoted

`sens_eGFR_ge_60`, cycle J, **urea_osm: β = −0.266 [−0.523, −0.010], p = 0.042.**

**It stays where it is, for five independent reasons:**

1. **1 of 36 terms** reached p < 0.05. At α = 0.05 the expectation is 1.8. This is exactly what
   multiplicity predicts and nothing more.
2. **It does not replicate** — cycle H gives −0.175, p = 0.28.
3. It is a **sensitivity analysis**, not the pre-specified primary (plan, §SINGLE PRIMARY OUTCOME).
4. It is the **ineffective** osmole. Under guide §1.2 urea does not move water, so even if real it
   would not support a cell-volume mechanism — it would point at renal handling or protein intake.
5. Its direction is **negative**, i.e. opposite to the hypothesis.

Recording this explicitly because a single p < 0.05 in a table of 36 is precisely the thing a
motivated reader lifts out, and the plan's interpretation rule was written to prevent it.

---

## 4. What this does and does not establish

**Does:**
- The osmolarity–adiposity association that much of [guide §2](../guide.md)'s input layer
  presupposes is **not detectable** in 5,107 US adults with gold-standard body composition,
  across two independent cycles, with renal function and glycaemia controlled.
- It is not hidden by the endpoint, by sex, by renal function, or by hypertriglyceridemic
  sodium artefact.
- **A reverse-causality argument makes the null stronger, not weaker.** If adiposity alters
  hydration, plasma volume and plasma water fraction (guide R9), that would tend to *create* an
  association. None is present. So the usual cross-sectional escape hatch is unavailable here.

**Does not:**
- **This is CALCULATED OSMOLARITY, not measured osmolality** (guide R1, stated in the plan in
  advance). A three-solute formula is blind to the osmolal gap and to unmeasured solutes.
  **An osmometer might see what this formula cannot**, and NHANES has no osmometry — so the
  measured-osmolality version of Q5 remains formally open, and is now the only version left.
- Say anything about ages outside 20–59 (DXA restriction), nor about longitudinal change.
- Address tonicity *inside* cells, which guide §1.5 makes the quantity that would actually
  matter. Plasma tonicity is a poor proxy for the adipocyte's own water, and this null is
  consistent with the mechanism being real but invisible at the plasma level.

---

## 5. Consequence for the project

**The sodium–adiposity thread ([guide §2.6](../guide.md)) is now in tension with the project's
own data.** §2.6 lists sodium intake associations with adiposity and offers three candidate
mechanisms, the first two osmotic. Here the sodium-bearing term of plasma tonicity shows no
association with measured body fat. That does not refute the dietary-sodium literature — intake
is not plasma concentration — but it removes the simplest osmotic bridge between them, and it
strengthens the case that **palatability-driven passive overconsumption** is the live
explanation, which §2.6 already named as the control condition.

**Combined with C-03** (high salt *increases* lymph flow, pointing away from adipose
accumulation) and with this null, the osmotic half of this project is substantially weaker than
when the guide was written.

**What survives on the input side:** the intracellular and local-tissue mechanisms —
osmolyte-driven cell water (guide §1.5), the polyol pathway, and the lymphatic route — none of
which plasma osmolarity indexes. **What does not survive is the idea that systemic plasma
osmolarity is itself the exposure.**

---

## 6. Honest notes on the analysis

- **Survey variance is approximated**, not exact: WLS with cluster-robust SEs by stratum/PSU
  rather than a full Taylor-series survey estimator. CIs should be read as approximate. Stated in
  the plan in advance, not after seeing the result.
- **Serum glucose in BIOPRO is not reliably fasting**, adding noise to the effective term; HbA1c
  carried as a fasting-independent glycaemia control. A fasting-subsample replication would
  tighten the effective term and is the obvious next refinement.
- **Complete-case analysis**: 3,247 → 2,119 (J) and 3,803 → 2,988 (H) after requiring DXA,
  biochemistry, HbA1c and valid exam weights. Differential missingness in DXA is not modelled.
- Weighted means are plausible and act as a sanity check on the pipeline: calculated osmolarity
  **290.2 (J) / 289.1 (H) mOsm/L**, body fat **33.1% / 33.1%**, BMI **29.0 / 28.7**,
  eGFR **103 / 102**. These are the right values for US adults 20–59, which is weak evidence the
  merge and unit handling are correct.
