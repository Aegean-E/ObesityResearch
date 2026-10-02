# VA-02 — Lean tissue is more hydrated in obesity, in both compartments equally

**Script:** [`va02_icw_ecw_vs_adiposity.py`](va02_icw_ecw_vs_adiposity.py) (plan in docstring,
written before the data were touched, guide R13)
**Outputs:** [`output/va02_results.csv`](output/va02_results.csv) ·
[`output/va02_notes.csv`](output/va02_notes.csv)
**Data:** NHANES 2001–2002 (B) and 2003–2004 (C) — multifrequency bioimpedance (5 kHz–1 MHz,
Cole/Hanai-derived ICW and ECW) **plus** DXA. Adults ≥20. **n = 1,850 + 1,668 = 3,518.**
**Run:** 2026-10-02

---

## 0. Answer — pre-specified interpretation rule (d)

**Both compartments rise, proportionally. There is no compartment specificity.**

| Outcome | Cycle B β per 10 pp body fat | Cycle C | Direction |
|---|---|---|---|
| **ICW / DXA fat-free mass** (primary) | **+0.0098** [0.0056, 0.0141], p=6×10⁻⁶ | **+0.0078** [0.0052, 0.0105], p=4×10⁻⁹ | ↑ |
| **ECW / DXA fat-free mass** | **+0.0055** [0.0042, 0.0068], p=5×10⁻¹⁶ | **+0.0056** [0.0042, 0.0071], p=1×10⁻¹⁴ | ↑ |
| **TBW / DXA fat-free mass** | +0.0153, p=1×10⁻⁹ | +0.0135, p=7×10⁻²⁰ | ↑ |
| **Raw ECW/ICW ratio** | −0.0038, **p = 0.28** | −0.0020, **p = 0.50** | **null** |

In relative terms the two compartments move almost identically — ICW +2.1% / +1.8% and ECW
+1.8% / +1.8% per 10 percentage points of body fat, against baselines of 0.47 / 0.43 and
0.31 / 0.32 kg·kg⁻¹. Hence the ratio is flat.

**Two conclusions, and they point in different directions from each other:**

1. **The published ECW/ICW-vs-fat association does not survive adjustment.** H4 §4.6 recorded it
   and flagged a compositional confound. **The confound was doing the work.** Adjusted for age,
   sex, ethnicity and height and normalised to DXA fat-free mass, the ratio is null in both
   cycles.
2. **What does replicate is that fat-free mass itself is more hydrated in people with more body
   fat** — TBW/FFM rises robustly, p=10⁻⁹ and 10⁻²⁰. Mean hydration here is **0.75–0.78**, above
   the 0.73 that classical two-compartment body-composition models assume to be constant. This
   reproduces a known methodological problem: **the hydration of fat-free mass is not a
   constant, and is elevated in obesity.**

---

## 1. What this does to H4 §4.6 — my earlier reading was wrong

H4 §4.6 reported, from the literature, a positive ECW/ICW-to-body-fat association and read it as
a **third independent line pointing extracellular rather than intracellular**, alongside VA-01's
plasma null and H1's oedema finding.

> **That reading is withdrawn.** The association does not survive adjustment and normalisation,
> and in absolute per-lean-mass terms **intracellular water rises slightly *more* than
> extracellular**, not less. H4 §4.6's "third line" was the confound I had myself flagged. I
> should have weighted my own caveat more heavily than the finding it qualified.

**But this is not support for cell swelling either.** Rule (d) was written in advance for exactly
this outcome: both compartments rising together is **uninformative for the mechanism**. Nothing
here says adipocytes are swollen; it says the whole fat-free compartment carries proportionally
more water.

---

## 2. The limitation that could *be* the finding

Stated in the plan before the data were touched, and it now interacts with the result in a way
that matters:

**BIA compartment estimates rest on Cole modelling and Hanai mixture theory, whose assumptions
include tissue resistivity and hydration constants.** If those constants are violated in obesity
— and §0 conclusion 2 says FFM hydration *is* elevated in obesity — then **the apparent ICW/ECW
split in obese subjects may be partly an artefact of the model that assumed it constant.**

> So the two findings are entangled: the elevated FFM hydration I detect is also a reason to
> distrust how the instrument partitioned that water. **I cannot separate them with these data.**
> A dilution study (deuterium for TBW, bromide for ECW) would, and that is what the question
> needs.

This is why the plan stated up front that VA-02 **can** test the published association's
robustness and **cannot** settle whether cells hold more water. It did the first; the second
remains out of reach.

---

## 3. An error I made, caught, and did not report as a result

**My first run used the filter `(BIAEXSTS == 1) & (BIDFIT == 1)`, on the assumption that `BIDFIT`
was a good-fit flag with 1 = good. It is not.** The sample collapsed from 5,949 to **99**, and
those 99 produced a confident-looking primary result (β=+0.0064, p=0.0003) that **contradicted
the other cycle** and flipped the sign of the secondary.

Inspecting the distributions settled it:

| Variable | Distribution | Meaning |
|---|---|---|
| `BIAEXSTS` | 1 in 4,709 / 4,298 cases; `==1` coincides **exactly** with having non-null derived ICF/ECF | **1 = complete exam.** Correct filter |
| `BIDFIT` | modal value **0** (4,380 / 3,988), then 7, then small counts at 1–5 | shape of a **count of fit problems**, not a 1=good flag |

So `BIDFIT==1` selected a tiny unrepresentative subgroup. **The original numbers were discarded
unreported.** The corrected filter (`BIAEXSTS==1`) gives n≈1,850 and 1,668 adults.

> **This is guide R19 — read the preparation, not just the result — applied to variable codings,
> and it is the second time the rule has earned its place.** The tell was not the statistics,
> which looked excellent; it was **n collapsing by 98%**. A filter that discards 98% of a sample
> is a bug until proven otherwise. Worth adding to the operational rules.

*(`BIDFIT==0` is carried as a sensitivity on the inference that 0 = no flag raised. That is an
inference: the NHANES codebook page could not be retrieved, and it is labelled as unverified.)*

---

## 4. Secondary and sex

| Model | B | C |
|---|---|---|
| ICW/FFM, **women** | +0.0114 per 10 pp, p=3×10⁻⁴ | +0.0091, p=1×10⁻⁵ |
| ICW/FFM, **men** | +0.0066, **p=0.052** | +0.0050, **p=0.11** |

Same direction in both sexes, reaching significance only in women — most plausibly range and
power (women have a wider body-fat distribution) rather than a mechanism. **Not read as a sex
asymmetry**, especially since VA-01 found none.

---

## 5. Consequence for the project

**The compartment question is now answered as far as these data can answer it, and the answer is
"neither, proportionally."** Combined with VA-01:

| Question | Answer from our own data |
|---|---|
| Does plasma osmolarity track body fat? | **No** (VA-01, n=5,107, two cycles) |
| Is the extra water in obesity intracellular or extracellular? | **Both, proportionally** (VA-02, n=3,518, two cycles). The ratio is flat |
| Is fat-free mass more hydrated in obesity? | **Yes, robustly** — and it undermines the constant-hydration assumption those very estimates rely on |

**What this leaves.** The project's osmotic thread has now been tested three ways with its own
computation and found nothing specific: no plasma association, no compartment shift. The
mechanisms still standing are the ones that never depended on water as a signal —
**M8** (the re-esterification gate), **M9** (aldose reductase → adipose senescence), and
**M10** (WNK1/SPAK volume *sensing*, whose obesity phenotype runs through adipogenesis and
thermogenesis rather than cell volume). That is a coherent place to have arrived, and it was
reached by eliminating rather than by assuming.
