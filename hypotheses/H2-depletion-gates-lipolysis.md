# H2 — Net lipolysis requires depletion of something intracellular

**Status:** open · opened 2026-10-02 · **Governed by** [guide.md](../guide.md)

---

## 1. The claim

As posed:

> "Something intracellular needs to be depleted in order to start lipolysis."

**Why this is a strong move rather than a rephrasing.** The standard account of lipolysis is
*signal-driven*: catecholamines raise cAMP, PKA phosphorylates HSL and perilipin, ATGL is
engaged by CGI-58. In that account lipolysis is **switched on**. H2 says it is instead
**gated** — that the signal is permissive only once some intracellular pool has run down, and
that the pool, not the signal, is the real variable.

That is a different and testable architecture, and it changes what counts as the control point.

### 1.1 The distinction that makes it precise

**Gross lipolysis ≠ net lipolysis.** Triglyceride hydrolysis and re-esterification run
*simultaneously* in the adipocyte — triglyceride–fatty-acid futile cycling. So:

> **net lipolysis = hydrolysis − re-esterification**

H2 then has a natural reading that does not require any new sensor: **hydrolysis may run
continuously, and net fat release begins only when the substrate for re-esterification is
exhausted.** On that reading the gate is a *substrate*, not a signal, and the "depletion" the
subject is describing is a metabolite pool.

**This also makes H2 compatible with a fact that otherwise looks odd:** lipolysis does not
need to be "started" at all, because it is always running. What needs to change is whether the
products can be put back.

---

## 2. Candidate depleted pools

Ranked by how well each fits "must be depleted for net lipolysis to begin."

| # | Pool | Why depletion would permit net lipolysis |
|---|---|---|
| **D-a** | **Glycerol-3-phosphate (G3P)** | The obligatory backbone for re-esterification. Adipocytes have little glycerol kinase, so G3P comes from glucose via glycolysis, or from pyruvate/lactate via **glyceroneogenesis (PEPCK-C)**. **No G3P → no re-esterification → net release.** ★★ the leading candidate |
| **D-b** | **G0S2 protein** | An endogenous **ATGL inhibitor**. If it is degraded during fasting, then a literal intracellular *protein* must disappear before the lipase works — the most literal form of H2 |
| **D-c** | **Malonyl-CoA** | Inhibits CPT-1, so its depletion permits fatty-acid **oxidation**. Gates burning rather than releasing — relevant but a different step |
| **D-d** | **Adipocyte glycogen** | Small pool, but if its breakdown feeds G3P it would sit upstream of D-a, and it connects to the project's earlier glycogen thread |
| **D-e** | **Cell water / volume** | H1's territory: shrinkage as catabolic. Depletion of intracellular water rather than a metabolite |

**D-a is the one to test first**, because it is quantitative, has a defending pathway that can
be manipulated, and makes a prediction about a number this project has already met (§4).

---

## 3. Predictions, before searching (guide R11)

- **P35** — **G3P will be the limiting substrate for re-esterification**, and **adipose PEPCK-C
  / glyceroneogenesis** will be documented as the pathway that *defends* G3P during fasting,
  when glucose is scarce. If so, glyceroneogenesis is the mechanism that **opposes** H2's gate.
- **P36** — **Thiazolidinediones will induce adipose PEPCK**, increasing re-esterification and
  fat retention. That would make the field's best-known fat-gaining drug act *by closing H2's
  gate* — a strong, independent argument for the hypothesis.
- **P37** — **G0S2 will be an endogenous ATGL inhibitor whose level falls with fasting**, making
  D-b literally true.
- **P38** — Adipocytes will be confirmed to contain **glycogen**, with turnover linked to the
  lipogenesis/lipolysis switch.
- **P39 — the one I expect to be instructive.** There will be **no single dedicated "depletion
  sensor"** for lipolysis analogous to a glucose sensor. Control will turn out to be
  **substrate-level (D-a) plus inhibitor-removal (D-b)**, with no unified account in the
  literature. If so, H2 is *correct in substance* while being **absent as a stated framework** —
  which is the most useful possible outcome, because it means the framing is the contribution.

### 3.1 ★ The re-reading this forces on my own session-1 work

Session 1 recorded, as evidence *against* my clearance mechanism, that lymphoedematous adipose
tissue showed a **"dramatically elevated basal FFA:glycerol ratio"**, which the authors read as
**impaired re-esterification** ([claims.md B2](../claims.md)).

Under H2 that same number reads differently. Glycerol escapes quantitatively (adipocytes lack
glycerol kinase), so glycerol indexes **total hydrolysis**; FFA release is hydrolysis **minus**
re-esterification. An elevated FFA:glycerol ratio therefore means **re-esterification is
failing** — which under H2 is exactly the state in which **net lipolysis is permitted**, and
the most likely proximate cause is **G3P limitation**.

> **P40** — The elevated FFA:glycerol ratio and the raised total lipolysis in that dataset are
> **one finding, not two**: a tissue in which the re-esterification gate is open. If so, I
> recorded B1 and B2 as separate contradictions when they are a single coherent observation
> **supporting** a G3P-depletion account.

**This matters for how I read my own ledger.** I filed those rows under "evidence against H1"
and did not ask what they were evidence *for*. H2 supplies the frame in which they are positive
data. **Recorded as my error to check, not as a conclusion** — the alternative explanations
(impaired FFA export, altered albumin binding, assay artefact, the liposuction sampling problem
of R19) are not excluded, and the dataset was never designed to measure G3P.

---

## 4. Findings

### 4.0 Headline — H2 is right, three pools qualify, and closing the gate alone causes obesity

**The hypothesis is correct in substance.** At least **three** distinct intracellular pools must
run down for net lipolysis, and the field has the biochemistry — though it frames it as
"re-esterification opposes release" rather than "depletion gates lipolysis."

And the keystone result, which I did not anticipate:

> **Transgenic overexpression of PEPCK-C in adipose tissue → increased glyceroneogenesis →
> increased fatty-acid re-esterification → increased adipocyte size, increased fat mass, higher
> body weight. Titled "obesity without insulin resistance."**

Nothing about the lipolytic machinery was changed. **Closing H2's gate is, on its own,
sufficient to produce obesity** — guide R15's **"sufficient"**, which almost nothing in this
project has earned. That makes the re-esterification gate a mechanism target in its own right,
and it was **absent from my M1–M7 list**. It is now **M8**.

### 4.1 ★★ D-a confirmed — G3P is the gate, and glyceroneogenesis defends it

- **Adipocytes lack glycerol kinase**, so the glycerol released by hydrolysis **cannot be
  reused**. Glycerol escapes quantitatively, which is why it indexes *total* hydrolysis.
- G3P for re-esterification therefore comes from only two places: **glucose via glycolysis**, or
  **pyruvate/lactate via glyceroneogenesis**, with **PEPCK-C rate-limiting**.
- **The defence is fasting-induced.** Pyruvate incorporation into glyceride-glycerol **rises on
  fasting and falls on refeeding** (Hanson, Ballard and Reshef), with PEPCK-C induced in adipose
  tissue. So precisely when glucose is scarce — when G3P *would* deplete and the gate *would*
  open — the cell switches on an alternative route to keep making it.

> **This is the real structure of H2.** The gate is not simply "does G3P run out." It is a
> **contest**: hydrolysis continuously liberates fatty acids, and glyceroneogenesis
> continuously regenerates the backbone to put them back. **Net lipolysis is the margin by
> which the first outruns the second.** That is a more interesting claim than the one posed, and
> it is the posed claim's own logic followed through.

[Glyceroneogenesis and the TG/FA cycle (JBC)](https://www.jbc.org/article/S0021-9258(20)84065-4/pdf) ·
[Hanson's discovery of the pathway](https://www.jbc.org/article/S0021-9258(20)68892-5/fulltext) ·
[fatty acid recycling in adipocytes](https://pubmed.ncbi.nlm.nih.gov/14641009/)

### 4.2 ★★ P36 confirmed, and it rewrites two things

**The fat-gaining drug works by closing the gate.** A JBC paper is titled, literally,
*"Thiazolidinediones Block Fatty Acid Release by Inducing Glyceroneogenesis in Fat Cells."*

| Finding | Value |
|---|---|
| Rosiglitazone → adipose PEPCK-C mRNA and activity | ↑, rapid and potent, PPARγ-mediated transcription |
| Resulting glyceroneogenesis, rat | **2.5-fold increase** |
| Human adipose tissue | PEPCK induction confirmed with rosiglitazone |
| **Adipose PEPCK overexpression, transgenic** | ↑ glyceroneogenesis, ↑ FFA re-esterification, ↑ adipocyte size, ↑ fat mass, ↑ body weight — **"obesity without insulin resistance"** |

**And leptin works by opening it.** *"Rapid Nitration of Adipocyte Phosphoenolpyruvate
Carboxykinase by Leptin Reduces Glyceroneogenesis and Induces Fatty Acid Release."* Leptin
post-translationally disables PEPCK → less G3P → net release. **The principal adiposity hormone
acts on H2's gate**, in the opening direction, while the principal fat-gaining drug acts on it
in the closing direction. Two independent pharmacological confirmations, in opposite directions,
of the same control point.

> **Correction to H1 (guide R17).** H1 §3A proposed thiazolidinediones as a test case for
> "oedema → fat," on the grounds that PPARγ agonism causes both fluid retention and
> adipogenesis. **That rationale is now dead:** TZD fat gain has a documented mechanism —
> induced glyceroneogenesis blocking fatty-acid release — that has **nothing to do with fluid**.
> H1's test T3 loses its sharpest arm.

[TZDs block FA release (JBC)](https://www.jbc.org/article/S0021-9258(20)80094-5/pdf) ·
[human adipose PEPCK induction](https://pubmed.ncbi.nlm.nih.gov/14739078) ·
[PEPCK overexpression → obesity](https://pubmed.ncbi.nlm.nih.gov/11872659/) ·
[leptin nitrates PEPCK](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0040650)

### 4.3 ★ D-b confirmed — a protein that must literally be destroyed

**G0S2** inhibits ATGL directly: the **hydrophobic domain of G0S2** binds the **patatin-like
domain of ATGL**, suppressing TAG hydrolase activity.

- **"Upon fasting, G0S2 protein expression exhibits an increase in liver and a decrease in
  adipose tissue."** Adipose G0S2 falls with fasting → ATGL is released → lipolysis proceeds.
- **Feeding raises** adipose G0S2, channelling dietary fatty acids into storage.
- G0S2 increases fat storage and **reduces fatty-acid oxidation** by suppressing ATGL.
- Its stability is regulated by **ubiquitination**, and by triglyceride accumulation and ATGL
  interaction itself.

**This is H2 in its most literal form:** an intracellular protein whose **degradation** is the
permissive step. Note the **tissue divergence** — fasting moves G0S2 in *opposite* directions in
liver and adipose. Exactly the trap R21 was written for; "G0S2 rises on fasting" is true and
useless without naming the tissue.

[Cell Metab 2010](https://www.cell.com/cell-metabolism/fulltext/S1550-4131(10)00030-6) ·
[ubiquitination and stability](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4889065/) ·
[Diabetes review](https://diabetesjournals.org/diabetes/article/63/3/847/16462/Adipose-Triglyceride-Lipase-and-G0-G1-Switch-Gene)

### 4.4 ★ D-d confirmed — adipose glycogen has a *set point*, and it gates lipid mobilisation

The strongest vindication of the project's earlier glycogen thread, and it is old:

- Observed in the **1940s**: refeeding rats after a prolonged partial fast produces a **marked
  transient spike in adipose glycogen**, which **dissipates in coordination with the initiation
  of lipid resynthesis**.
- The interpretation drawn: **the adipocyte possesses a set point for glycogen** that
  coordinates glycogen turnover with lipid metabolism.
- Direct, and titled as such: **"Enhanced glycogen metabolism in adipose tissue decreases
  triglyceride mobilization."** Glycogen up → mobilisation down.
- Glycogen is now understood as **regulatory** for lipogenesis, lipolysis, glucose uptake and
  thermogenesis, **not** merely an overflow store; refeeding raises it via AKT → GSK3
  inactivation.
- And adipocytes **synthesise and secrete glycerol from glucose** via glycerogenesis to dispose
  of excess glucose — so the glucose→G3P→glycerol route is bidirectional and active.

**Glycogen plausibly sits upstream of D-a:** glycogenolysis feeds glycolysis feeds G3P. If so,
the three "pools" are one pathway sampled at three depths — glycogen → G3P → (and separately)
the G0S2 brake. *(My inference, not shown.)*

[Am J Physiol 2010](https://journals.physiology.org/doi/full/10.1152/ajpendo.00741.2009) ·
[Nature 2021, glycogen and thermogenesis](https://www.nature.com/articles/s41586-021-04019-8) ·
[2025 review](https://www.nature.com/articles/s41574-025-01152-6) ·
[adipocyte glycerol secretion](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5567128/)

### 4.5 ✗ P39 was wrong — the framework exists

I predicted there would be **no unified account**. There is: the **triglyceride/fatty-acid
cycle** literature, with Reshef and Hanson's review carrying almost that title. The field has
had this for decades.

What is *less* common is the emphasis — the literature says "re-esterification opposes release,"
the subject said "something must be depleted to start lipolysis." **Same content, and the second
framing makes the depleted pool the variable to measure and to target.** That is worth keeping,
but I should not pretend the biochemistry is new. **P39 wrong; recorded.**

### 4.6 ★ P40 — session 1's "contradiction" was one coherent finding, and I misfiled it

[claims.md B1 and B2](../claims.md) recorded, as two separate pieces of evidence *against* H1:
higher total lipolysis in lymphoedematous tissue, and a "dramatically elevated basal
FFA:glycerol ratio" read by the authors as **impaired re-esterification**.

Under H2 these are **one finding**. Glycerol indexes total hydrolysis (no glycerol kinase, §4.1);
FFA release is hydrolysis minus re-esterification. **Both numbers describe a tissue in which the
re-esterification gate is open** — and the mechanistic candidates for that are now named: G3P
limitation, reduced glyceroneogenesis, or both.

**It also dissolves the paradox the authors themselves flagged.** They reported **lower ATGL
mRNA** alongside **higher measured lipolysis** and called it paradoxical. Under H2 there is no
paradox: net release can rise with *less* lipase if the gate is open — and **lower G0S2 would
raise ATGL activity with no change in ATGL protein at all.**

> **New testable prediction, from combining H2 with session 1's dataset — P41:** lymphoedematous
> adipose tissue will show **reduced G0S2** and/or **reduced PEPCK-C / glyceroneogenic capacity**
> relative to control. Both are measurable in banked tissue. If so, the "paradox" is explained
> and H2 gains human support in the setting this project already studies.

**My error, recorded:** I filed B1 and B2 as contradictions and never asked what they were
evidence *for*. A finding that refutes one hypothesis is not thereby inert — **"against H1" is
not a complete description of a datum.** Guide needs this: a counter-evidence entry should also
record what the finding would support.

---

## 5. What this adds to the project

**M8 — the re-esterification gate** joins the mechanism list, and it is better supported than
most of M1–M7:

| Criterion | Status |
|---|---|
| Named molecular control points | **PEPCK-C** (G3P supply), **G0S2** (ATGL brake), adipose **glycogen** |
| Sufficiency | ✅ **adipose PEPCK overexpression alone → obesity** |
| Hormonal regulation | ✅ **leptin** opens it (PEPCK nitration) |
| Pharmacological closure in humans | ✅ **thiazolidinediones** (PEPCK induction confirmed in human adipose) |
| Quantitative human flux data | ◐ TG/FA cycling measurable by tracer; not done in this project's settings |
| Tested against adiposity | ✅ **in the transgenic** — the only mechanism in this project where that box is ticked |

**Why it matters more than it looks.** Every other mechanism this project has chased tried to
change how much *hydrolysis* happens. M8 says hydrolysis may be beside the point: the organism
can hold fat perfectly well while hydrolysing continuously, simply by putting the products back.
**A therapy that increased lipolysis without closing re-esterification would do nothing** — and
that may be part of why §K of the register found every hard endpoint null.

**Open, in order:**
1. **P41** — G0S2 and PEPCK-C in lymphoedematous vs control adipose tissue. Banked-tissue
   question, directly testable.
2. Is the human TG/FA cycling rate measured anywhere as a function of adiposity? Tracer methods
   exist (§4.1's literature uses them).
3. Does adipose glycogen depletion **precede** net lipolysis in humans, as the 1940s rat data
   implies? Timing study.
4. Glyceroneogenesis inhibition as an intervention class — unexamined in the register, and the
   first M8 entry.

---

# 6. Session 2026-10-02b — can the gate be opened, and does it defend itself?

Two questions, in order of importance:

**Q-i — Does the gate close itself as you fast?** §4.1 found glyceroneogenesis is *induced by
fasting*. If that induction is quantitatively meaningful, then **fasting opens the hydrolysis
side and the cell compensates on the re-esterification side** — a biochemical
defended-set-point, at exactly the level this project's premise requires. That would be the
most important thing in H2.

**Q-ii — What opens the gate pharmacologically?** M8 has no intervention entry.

## Predictions, before searching (guide R11)

- **P42 — the one that matters.** Fasting-induced glyceroneogenesis will be **quantitatively
  substantial**, not a trace pathway, and will be describable as *opposing* fat loss. If so, the
  re-esterification gate is a **self-closing** gate and part of the defence of adipose mass.
- **P43** — **PEPCK inhibition** will exist only as research tools (3-mercaptopicolinate,
  hydrazine sulfate) with **no viable clinical agent**, because PEPCK is required for hepatic
  gluconeogenesis and systemic inhibition would be intolerable. The gate will turn out to be
  **pharmacologically closable but not openable** — the same availability asymmetry as P21.
- **P44** — **Leptin (metreleptin)** will be the one approved agent whose mechanism includes
  opening the gate, and its fat-loss effect will be real but confined to leptin-deficient states
  (lipodystrophy, congenital deficiency), **not** common obesity, where leptin is already high.
- **P45 — my sharp inference, flagged as such and to be tested.** Metformin inhibits
  **mitochondrial glycerophosphate dehydrogenase**, which oxidises G3P to DHAP. Inhibiting it
  should **raise cytosolic G3P**. In adipose tissue that would mean **more substrate for
  re-esterification — i.e. metformin would CLOSE the gate** and favour fat retention. This runs
  against metformin's reputation and against its entry in
  [interventions.md §G2](../interventions.md). *(My inference, not shown — I expect the
  literature to have established the mGPD mechanism in liver and to be silent on adipose.)*
- **P46** — Human **TG/FA cycling rates** will have been measured by tracer, and the recycled
  fraction will be **large** — tens of percent of hydrolysed fatty acids re-esterified rather
  than released. A small fraction would make H2 a curiosity; a large one makes it the control
  point.

**P42 and P46 together decide whether M8 is the project's main line or a footnote.**

## 7. Findings

### 7.0 Headline — the gate is enormous, and its setting varies 0–100% between people

**P46 confirmed, and larger than I predicted.** Re-esterification is not a trim on lipolysis; it
is most of it.

| Measure | Value |
|---|---|
| **Fraction of released FFA recycled back to triglyceride** | **~75%**, and "relatively constant" across metabolic states despite large changes in cycling *rate* |
| Adipose **intracellular** recycling, share of total | **20–30%** |
| Non-adipose (mainly hepatic) share of re-esterification, overnight fast | **~50%** |
| Adipose recycling during fasting | estimated **up to 40%** |
| **Human adipocytes in vitro**, no hormone, 5 mM glucose | **40 ± 4%** cycled back — **range 0–100% across 51 subjects** |
| Effect of fasting + β-adrenergic stimulation on adipose re-esterified fraction | falls from **30–40% → 8–21%** |

> **★ The most important number in this project so far: 0–100% across 51 people.**
>
> Two individuals with **identical** rates of hydrolysis can differ severalfold in **net** fat
> release, purely from where their re-esterification gate sits. That is **measured, human,
> inter-individual heterogeneity in a mechanism that controls fat retention** — and it is
> exactly the kind of heterogeneous susceptibility the project's framing requires, since a
> uniform exposure cannot explain a widening distribution.
>
> *(That this fits the project's needs is a reason to scrutinise it harder, not to celebrate.
> The 0–100% range comes from one in vitro series and could be assay variance as much as
> biology. **Finding the original and reading its figures is the single highest-value next
> read.**)*

### 7.1 ◐ P42 — the gate is braked, not self-closing, and the brake moves to the liver

I predicted fasting-induced glyceroneogenesis would **oppose** fat loss strongly enough to make
the gate self-closing. The picture is more interesting than that:

- **Glyceroneogenic capacity rises with fasting** — PEPCK-C induced, pyruvate→glyceride-glycerol
  up (§4.1, confirmed).
- **Yet the adipose re-esterified fraction falls** with fasting and β-stimulation, 30–40% → 8–21%.

**Resolution: hydrolysis rises faster than glyceroneogenesis can compensate.** So
glyceroneogenesis is a **partial brake**, not a defence that holds. **P42 partly wrong.**

**But the systemic picture restores most of the concern, by a different route.** Total recycling
stays near **75%** while *adipose* recycling falls — because the **liver takes over** (~50% of
re-esterification). The fatty acids leave the adipocyte and are re-esterified elsewhere, to
return as VLDL.

> **So "more lipolysis" need not mean "less fat," even with the adipose gate wide open** — the
> recycling simply relocates. This is a second, systemic reason why the interventions in
> [§K of the register](../interventions.md) may have moved markers without moving mass, and it
> is independent of the measurement critique offered there.

[TG/FA cycle review (JBC)](https://www.jbc.org/article/S0021-9258(20)84065-4/fulltext) ·
[substrate cycling in human adipocytes](https://pubmed.ncbi.nlm.nih.gov/3550370/) ·
[energy cost of recycling, overnight fast vs 4-day starvation](https://www.sciencedirect.com/science/article/abs/pii/0026049587901843) ·
[lipid metabolism during fasting](https://journals.physiology.org/doi/full/10.1152/ajpendo.2001.281.4.e789)

### 7.2 ✅ P43 — the gate is pharmacologically closable but not openable, for a structural reason

**PEPCK inhibitors exist and are orally active:**

- **3-mercaptopicolinic acid (SKF-34288)**: orally active, **Ki 2–9 µM**, two binding sites — one
  competitive with PEP/OAA (~10 µM), one allosteric (Ki ~150 µM). Historically noted as a
  **potent hypoglycaemic agent** *because* it inhibits PEPCK.
- **Hydrazine sulfate**: orally active PEPCK inhibitor, also inhibits low-Km ALDH, **hepatotoxic**
  (exacerbates ethanol liver damage).

**And here is the structural barrier, which is better than a mere drug-development gap:**

> **PEPCK serves four pathways — gluconeogenesis, glyceroneogenesis, serine synthesis, and the
> conversion of amino-acid carbon skeletons.** So you cannot inhibit glyceroneogenesis without
> inhibiting gluconeogenesis. The hypoglycaemia is not a side effect; it is the **same
> enzyme doing its main job.**

That is why M8 has no opening agent and is unlikely to get one by this route. **P43 confirmed,
with a mechanism for why.** Any real M8 intervention would need adipose-selective delivery, or a
different node — G0S2 destabilisation being the obvious untried candidate.
[3-MPA pharmacology](https://pmc.ncbi.nlm.nih.gov/articles/PMC4938538/) ·
[allosteric site](https://pubs.acs.org/doi/abs/10.1021/acs.biochem.5b00822)

### 7.3 ✅ P44 — leptin opens the gate, and is useless where it would be wanted

| | |
|---|---|
| **Lipodystrophy** (leptin-**deficient**), n=48 generalised | HbA1c **8.4% → 6.4%**; triglycerides **467 → 180 mg/dL** at 12 months; sustained over 3 years |
| **Common obesity** (leptin-**resistant**) | "minimal weight loss at best" |
| Anti-leptin antibodies | **96–100%** of metreleptin-treated obese patients; 86–92% in lipodystrophy |

So the one approved agent whose mechanism includes opening H2's gate (PEPCK nitration, §4.2)
works **only** in the states where leptin is absent — and in common obesity, where the gate
would be the target, leptin is already high and adding more does nothing. **P44 confirmed.**
This is [guide R21](../guide.md)'s lesson in hormonal form: the right mechanism in the wrong
context.
[long-term metreleptin](https://pmc.ncbi.nlm.nih.gov/articles/PMC3498767/) ·
[immunogenicity](https://pmc.ncbi.nlm.nih.gov/articles/PMC4875885/)

### 7.4 ⚠ P45 — my inference is untested AND rests on a contested premise. Not a finding.

I inferred that metformin, by inhibiting mitochondrial glycerophosphate dehydrogenase (mGPD),
would **raise cytosolic G3P** and therefore **close** the gate — making metformin fat-sparing,
against its reputation and against its own entry in the register.

**What is established:** Madiraju et al., *Nature* 2014 — metformin at physiologically relevant
doses non-competitively inhibits mGPD, altering hepatocellular redox, reducing conversion of
**lactate and glycerol** to glucose, and suppressing hepatic gluconeogenesis; antisense knockdown
of hepatic mGPD reproduces the phenotype.

**Three reasons to hold my inference at arm's length:**

1. **The premise is contested.** A bioRxiv paper titled *"If Metformin Inhibited the
   Mitochondrial Glycerol Phosphate Dehydrogenase…"* challenges it, and a PNAS paper offers a
   **different** mechanism — metformin, phenformin and galegine inhibiting **complex IV** and
   reducing glycerol-derived gluconeogenesis. The mGPD account is not settled.
2. **It is a liver result.** Nothing retrieved measures adipose G3P under metformin. **R21
   applies to me again** — I was about to assert a pathway without checking the tissue.
3. **It predicts the wrong clinical outcome.** Metformin lowers liver fat in practice. If raised
   cytosolic G3P drove re-esterification, the opposite would be expected — so either the
   inference is wrong, or something else dominates.

**Recorded as a speculation with a stated test, not as a result.** The test: adipose G3P and
re-esterification fraction under metformin, which a 2025 adipose-metformin review may already
address and which I have not read.
[Nature 2014](https://www.nature.com/articles/nature13270) ·
[challenge](https://www.biorxiv.org/content/10.1101/2020.03.28.013334v1.full.pdf) ·
[complex IV alternative](https://www.pnas.org/doi/10.1073/pnas.2122287119) ·
[adipose review, unread](https://pmc.ncbi.nlm.nih.gov/articles/PMC12409170)

---

## 8. Where H2 now stands

**Confirmed and quantified.** Net lipolysis is gated by re-esterification; **~75% of hydrolysed
fatty acids are recycled**; three depletable pools control it (G3P, G0S2, adipose glycogen);
closing the gate genetically **causes obesity**; leptin opens it; thiazolidinediones close it.

**The two hardest facts for any intervention built on it:**

1. **Opening the adipose gate relocates recycling to the liver** rather than abolishing it
   (§7.1). Net oxidation, not net release, is what would have to change.
2. **The gate cannot be opened selectively**, because PEPCK is shared with gluconeogenesis
   (§7.2), and the one hormone that opens it fails exactly where it is needed (§7.3).

**The most promising thing H2 produced is not a target but a variable:** the
**0–100% inter-individual range** in re-esterified fraction (§7.0). If that is real, it is a
measurable trait that would predict who retains fat from a given lipolytic drive — and it has
never been used that way.

**Next, in order:**
1. **Read the 51-subject source at figure level.** Is the 0–100% range biology or assay spread?
   Everything above rests on it.
2. **P41** — G0S2 and PEPCK-C in lymphoedematous vs control adipose (banked tissue).
3. Has re-esterified fraction ever been correlated with **adiposity or weight trajectory** in
   humans? If not, that is the study.
4. **G0S2 destabilisation** as the untried M8 node — no shared-pathway problem, unlike PEPCK.

---

# 9. Session 2026-10-02c — attacking my own best number

§7.0 called the **0–100% inter-individual range** in re-esterified fraction the most important
number in the project. That makes it the thing most worth trying to destroy.

## Predictions, before searching (guide R11)

- **P47 — the sceptical one, and I half expect to be right.** The 0–100% range will prove to be
  substantially **technical**, not a stable trait: a 1987 isolated-adipocyte method, n=51, with
  large preparation variance. **The strongest argument against it being a real trait is that
  nobody has used it as one in ~40 years.** A robust, severalfold, measurable determinant of net
  fat release would not have been left alone.
- **P48** — Re-esterification fraction **has** been compared between obese and lean humans, and
  will be **higher in obesity** (gate more closed). I hold this loosely; the literature may
  disagree with itself.
- **P49** — **Nobody will have measured re-esterified fraction prospectively against weight
  trajectory.** The trait-prediction study will not exist. If so, that is the study H2 implies
  and the project's clearest unexploited opening.
- **P50** — The "~75%, relatively constant" figure will trace to a **small number of tracer
  studies, plausibly one group**, and the constancy claim will be weaker than the phrasing
  implies.

**If P47 lands, §7.0 must be demoted and the headline rewritten.** Writing that down now so the
demotion cannot be quietly skipped later.

## 10. Findings — and §7.0 is demoted as promised

### 10.0 Headline — H2's mechanism survives; H2 as an *explanation of human obesity* does not

Three results, and together they are sobering:

1. **The 0–100% range is UNVERIFIED.** I could not reach the 1987 source. **P47 untested.**
2. **Obesity itself shows NO difference in re-esterification fraction from lean.** **P48 refuted.**
3. **The weight-reduced state has LESS re-esterification** — gate *more* open — and those are
   precisely the people who regain. **So gate setting does not determine fat trajectory.**

The causal core of H2 stands: closing the gate genetically **causes** obesity (§4.2). But the
human cross-sectional data says the gate is **not** where lean and obese people differ.

### 10.1 ⚠ P47 untested — §7.0 demoted, as I committed to doing

PubMed would not serve the abstract; the 1987 isolated-adipocyte paper remains **unread**.

> **Demotion, executed.** §7.0 called the 0–100% inter-individual range "the most important
> number in this project." **That status is withdrawn.** It is now an **unverified claim pending
> its primary source**, and nothing should be built on it. I wrote the demotion condition into
> §9 before searching precisely so this could not be skipped once the number had become
> attractive. *(I am also no closer to knowing whether it is biology or assay spread — the
> sceptical case in P47 is untested, not refuted.)*

What I did find is the methodological lineage — a **dual-isotopic technique** for measuring
lipolysis, acylglycerol synthesis and re-esterification in human adipose tissue and isolated
adipocytes, plus a 1985 radioisotopic method paper. So the measurement is real and established;
its between-subject spread is what I cannot yet vouch for.
[1985 method](https://journals.physiology.org/doi/abs/10.1152/ajpendo.1985.248.1.E140) ·
[mechanism of re-esterification in human adipocytes](https://www.sciencedirect.com/science/article/pii/S0022227520426136)

### 10.2 ✗✗ P48 REFUTED — the gate is not where obesity differs

From *"Alterations in adipocyte free fatty acid re-esterification associated with obesity and
weight reduction in man"*:

| Group | FFA:glycerol molar ratio | Implied re-esterification |
|---|---|---|
| Never-obese, weight-stable | **1.4 : 1** | ~**53%** of FFA retained (max possible ratio is 3:1) |
| **Weight-stable obese** | **not significantly different from control** | **same** |
| Weight-stable **reduced-obese** | **significantly higher** than control *or* obese | **lower** re-esterification |

> **I predicted obesity would show a more closed gate. It does not.** Established obesity and
> leanness have the **same** re-esterification fraction. So whatever sets fat mass, **the gate's
> steady-state setting is not the difference between an obese and a lean person.**

### 10.3 ★ The reduced-obese result runs the wrong way for H2, and that is the real finding

People who have lost weight re-esterify **less** — their gate is **more open** — and they are the
group that regains most aggressively.

If an open gate straightforwardly produced fat loss, the weight-reduced would be protected. They
are not. Two readings, neither comfortable for a simple version of H2:

- **The gate is downstream of the decision.** It reports energy state rather than setting fat
  mass — opening when glucose and G3P are scarce, which is a *consequence* of restriction.
- **Compensation elsewhere dominates** — appetite, energy expenditure, and the hepatic recycling
  of §7.1, which keeps total recycling near 75% whatever adipose does.

**Either way: opening the adipose gate is not sufficient for fat loss in humans**, and H2's value
is as a description of *how* storage is defended, not as a lever. That is a real narrowing and it
should temper the enthusiasm of §4.0.

[Am J Clin Nutr](https://pubmed.ncbi.nlm.nih.gov/4025192/)

### 10.4 ✅ P49 confirmed — the prospective study does not exist

No study located correlating re-esterification fraction with **subsequent** weight trajectory.
Given §10.2, the interesting version has also changed: not "do obese people re-esterify more"
(answered, no) but **"does an individual's gate setting predict their response to a given
energy deficit?"** That remains unasked, and §10.3 makes it more interesting rather than less,
because cross-sectional equality does not exclude predictive value.

### 10.5 Counter-evidence found, recorded at equal weight (R5/R22)

- **More re-esterification can be metabolically *good*.** *Adss1* deficiency upregulates glycerol
  kinase, **promoting** glycerol-dependent adipose re-esterification — and the paper's framing is
  that this **improves** energy metabolism. A direct counter-example to "open gate good, closed
  gate bad." It also matters mechanistically: **glycerol kinase upregulation lets adipocytes
  reuse glycerol, bypassing the G3P limitation entirely** — a fourth route into the gate that
  §2's table missed.
- **Systematic between-group variation does exist:** *"Ethnic differences in in vitro glyceride
  synthesis in subcutaneous and omental adipose tissue."* Weak support for the §7.0 idea that the
  gate's setting varies systematically — but between *groups*, which is not the same as a stable
  individual trait.

[Adss1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12767003/) ·
[ethnic differences in glyceride synthesis](https://journals.physiology.org/doi/full/10.1152/ajpendo.00225.2002)

---

## 11. H2's standing, revised

| Claim | Status |
|---|---|
| Net lipolysis is gated by re-esterification | ✅ established, ~75% recycled |
| Three (now four) depletable control points | ✅ G3P, G0S2, adipose glycogen, **+ glycerol kinase** (§10.5) |
| Closing the gate **causes** obesity | ✅ sufficiency, PEPCK transgenic |
| Leptin opens it; TZDs close it | ✅ both directions, pharmacologically |
| **The gate differs between obese and lean humans** | ❌ **refuted** (§10.2) |
| **Opening the gate produces fat loss in humans** | ❌ **not supported** — weight-reduced have a more open gate and regain (§10.3) |
| The gate can be opened selectively | ❌ PEPCK shared across four pathways (§7.2) |
| Individual gate setting predicts response to deficit | ⬜ **unasked** — the one live question |

**Honest summary.** The subject's hypothesis is **mechanistically correct and causally
demonstrated in animals**, and it reframes lipolysis usefully — net release is a margin, not a
switch. But as an account of *why some humans carry more fat*, it is now **contradicted at the
steady state** and **unsupported as a lever**. What survives is narrower and still worth having:
a description of how adipose defends its mass, a reason why lipolysis-raising interventions can
do nothing, and one unasked predictive question.

**My error pattern this session:** I elevated an unverified number to "most important in the
project" on a single search snippet, then spent the next session trying to demote it. **The rule
should have caught it earlier** — guide R18 quarantines *recalled* numbers but says nothing about
numbers read once from a search summary and not from the source. That gap is worth closing.
