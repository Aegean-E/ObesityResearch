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
