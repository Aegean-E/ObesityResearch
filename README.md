# Obesity mechanism project — state of the work

Started 2026-10-01. **4 hypothesis cards · 2 computed analyses · ~50 source-read claims ·
25 binding rules · 1 subject observation.** Scope: **osmolality, osmolarity, adipogenesis,
lipogenesis**, and what grew out of them.

**Entry point for a reader.** [guide.md](guide.md) is the constitution — rules, definitions,
mechanism map. This file is the **verdict so far**. They are different documents and the guide
wins any conflict.

---

## The honest verdict

> **The project's founding premise has largely failed, and that is its main result.**
>
> It began from the idea that body water — osmolality, tonicity, cell volume — acts causally on
> fat storage. Four hypotheses and two of our own analyses later: **plasma osmolarity does not
> track body fat; there is no intracellular/extracellular compartment shift with adiposity;
> osmolyte loading is cancelled by substitution; "intracellular osmolarity" is not even a
> variable; and the lymphatic agent is a lipid, not water.**
>
> What survives are **three molecular targets that never depended on water as a signal** — and
> each has something the water hypotheses never got: a causal animal result with an **obesity
> endpoint**.

This was reached by elimination rather than assumption, which is why I trust it more than the
map I started with.

---

## What our own data says

Two analyses, plan written into the script docstring before the data were touched (R13).

| | Question | Answer | n |
|---|---|---|---|
| **[VA-01](analysis/VA01-REPORT.md)** | Does calculated plasma osmolarity — decomposed into **effective** (2Na+glu/18) and **urea** parts — track **DXA body fat**? | **No.** Both null, both cycles, bounded at ~0.08 SD of fat per SD of tonicity. Not rescued by DXA-over-BMI, sex, renal function, or excluding hypertriglyceridemic samples | **5,107** |
| **[VA-02](analysis/VA02-REPORT.md)** | Is the extra water in obesity **intracellular or extracellular**? | **Both, proportionally.** ICW/FFM and ECW/FFM rise at near-identical relative rates, so the **ECW/ICW ratio is null** (p=0.28, 0.50). The published ratio-to-fat association does not survive adjustment | **3,518** |

**VA-02 also reproduced a methodological fact that undercuts its own instrument:** fat-free mass
is **more hydrated** in obesity (0.75–0.78 vs the 0.73 assumed constant, p=10⁻⁹ and 10⁻²⁰) — and
bioimpedance partitioning assumes the constant it violates. **Deuterium + bromide dilution** is
what that question actually needs.

**A null here is worth more than usual** (VA-01 §4): reverse causality would *create* an
association, since adiposity alters hydration and plasma water fraction. None is present, so the
usual cross-sectional escape hatch is unavailable.

---

## What survives — and why these three

| | Mechanism | Causal evidence | Available agent |
|---|---|---|---|
| **M8** | **The re-esterification gate** ([H2](hypotheses/H2-depletion-gates-lipolysis.md)) — ~75% of hydrolysed fatty acid is recycled; net lipolysis is a *margin*, not a switch. Gated by G3P, G0S2, adipose glycogen, glycerol kinase | **Adipose PEPCK-C overexpression alone → obesity** ("without insulin resistance"). Leptin opens the gate (PEPCK nitration); thiazolidinediones close it | ✗ PEPCK is shared with gluconeogenesis — hypoglycaemia is the same enzyme doing its job. **G0S2 destabilisation is the untried node** |
| **M9** | **Aldose reductase → adipose senescence** ([H3](hypotheses/H3-polyol-osmolyte-mtor.md)) — the polyol pathway matters in adipose, but via **senescence**, not osmosis | AR raised in obese human and mouse adipose; **deletion or blockade reduces diet-induced obesity, attenuates senescence, increases lipolysis** | ✅ **epalrestat** — approved in Japan, China, India. The register's most interesting entry |
| **M10** | **WNK1/SPAK volume sensing** ([H4](hypotheses/H4-intracellular-osmolarity.md)) — the cell senses **water in an enzyme's catalytic core**, not osmolarity; also the central osmosensor for vasopressin | **SPAK inactivation → resistant to diet-induced obesity**, ↑ energy expenditure, ↑ BAT thermogenesis, ↓ WAT hypertrophy. **WNK4 deletion → reduced DIO** | ✗ same shared-pathway barrier — WNK/SPAK is renal salt handling |

**The common shape, and it is the project's most transferable finding:** all three are about
**what the cell does with lipid it already has**, not about a signal telling it to store more. And
in two of three, the target is pharmacologically **closable but not openable**, because the enzyme
has a second job the organism needs.

---

## What was refuted

Including, repeatedly, my own prior claims. Full strike-throughs are preserved in the cards (R17).

| Claim | How it died |
|---|---|
| Water retention → lipogenesis ↑, lipolysis ↓ (**H1** as posed) | Lipolysis is **higher** in lymphoedematous tissue, re-esterification **impaired** — opposite on both counts |
| Lymphatic clearance failure traps lipolysis products | **Dead on anatomy**: transport is size-gated, 14% lymphatic at 1.18 nm → 100% at 3.24 nm. NEFA and glycerol are far below the gate and leave by capillary |
| The adipogenic agent in lymph is water | It is **free fatty acid** — and my supporting "~3× FFA" figure was **method-confounded** (centrifuged, freeze-thawed liposuction aspirate) |
| Sorbitol loading swells cells | **Osmolyte substitution**: taurine −31%, myo-inositol −37% as sorbitol rises. The cell defends a *total* |
| mTORC1 reads swelling as "grow" | It drives **taurine efflux** — part of regulatory volume *decrease*. I had it backwards |
| Fructose → mTORC1 → SREBP-1c | Fructose goes via **ChREBP**; the mTORC1 axis is the *glucose* route |
| Aldose reductase and FASN compete for NADPH | NADPH status **co-gates** both |
| The gate differs between obese and lean humans | **Refuted** — identical re-esterification fraction. And the weight-*reduced* have a **more open** gate while regaining most |
| ECW/ICW rising with fat = extracellular shift | The confound I myself flagged was doing the work ([VA-02](analysis/VA02-REPORT.md)) |
| "Elevated intracellular osmolarity" | **Category error** — water permeability clamps it within seconds |

**And the interventions.** [interventions.md §K](interventions.md): every mechanistically
motivated agent that received a properly controlled trial with a hard endpoint **failed or shrank
on replication** — ubenimex null, coumarin negative (NEJM), pentoxifylline+E null, doxycycline
43.9% in one trial → "limited role" across twelve, metformin's own paper reporting null volume
endpoints under the title *"Metformin Eliminates Lymphedema in Mice."* **Biomarkers move
reliably; hard endpoints do not.** Nothing in the register has been tested against adiposity.

---

## Reading order

1. **[guide.md](guide.md)** — rules R1–R22, the definitions that most claims die on (§1), mechanism
   map (§2), quarantined unverified numbers (§4)
2. **This file** — verdict
3. **[claims.md](claims.md)** — source-read claims with design/exposure codes, a **non-empty
   counter-evidence column on every row**, open contradictions C-01…C-05
4. **[hypotheses/](hypotheses/)** — H1 (water→storage), H2 (depletion gates lipolysis), H3
   (polyol/osmolyte/mTOR), H4 (intracellular osmolarity)
5. **[analysis/](analysis/)** — VA-01, VA-02: scripts with pre-written plans, CSV outputs, reports
6. **[interventions.md](interventions.md)** — agents by evidence quality. **Evaluation only, never a
   protocol**
7. **[observations/](observations/)** — G01, the subject's fructose-craving observation (D8/E1)
8. **[sessions/](sessions/)** — chronological logs with prediction scorecards

---

## The error record

Nine of the 25 rules were written from specific mistakes made here. That record is an asset, so it
is kept explicit rather than tidied away:

| Rule | The mistake that produced it |
|---|---|
| **R19** | Recorded "~3× FFA" without reading how the fluid was prepared — liposuction aspirate, freeze-thawed |
| **R19b** | Filtered on a variable whose coding I guessed; **n fell 5,949 → 99** and produced a confident result contradicting the replication cycle. The statistics looked excellent; the tell was the sample size |
| **R21** | Claimed a pathway without checking the tissue has its enzymes — **twice** (lymphatic clearance, then PFK-1 bypass). Correct biochemistry, wrong location |
| **R22** | Filed two findings as "evidence against H1" and never asked what they were evidence *for* — they were one coherent finding supporting H2 |
| **R18c** | Called an unverified number "the most important in this project" from one search snippet, then had to demote it |

**The habit that worked best:** writing predictions *before* searching, including predictions that
**I would be wrong**. P11 ("I will be wrong about the lymphoedema evidence") and P47 ("the 0–100%
range is probably assay spread") both fired, and both caught errors that confident reading would
have missed.

---

## Open, ranked

1. **Read [Thiagarajan 2022](https://onlinelibrary.wiley.com/doi/abs/10.1002/oby.23496) at figure
   level** — M9's keystone. Effect size on fat mass, which inhibitor, whether the human data is
   expression-only. The register's best entry rests on a search summary.
2. **Has epalrestat ever been looked at for weight or fat mass** in Japan, China or India, where it
   has been in wide diabetic use for years? A side observation may exist.
3. **G0S2 destabilisation** — M8's only node without the shared-pathway problem. Unexamined.
4. **P41:** G0S2 and PEPCK-C in lymphoedematous vs control adipose. Banked-tissue question that
   would also explain the ATGL paradox in that dataset.
5. **Does an individual's re-esterification setting predict response to an energy deficit?**
   Cross-sectional equality does not exclude predictive value, and nobody has asked.
6. **Deuterium + bromide dilution vs adiposity** — the only way past VA-02's instrument problem.
7. **Measured osmolality**, not calculated. The one form in which VA-01's question survives, and
   NHANES has no osmometry.

---

## Standing boundary

This project produces **mechanism**. It evaluates interventions by evidence quality; it does not
select agents, recommend doses, or build protocols for anyone. That line is in
[guide.md §0](guide.md) and it is a division of labour, not a comment on anyone's competence.
