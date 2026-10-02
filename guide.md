# guide.md

**A working guide for the agent on this project.**
Version 0.1 · 2026-10-01 · Scope: **osmolality · osmolarity · adipogenesis · lipogenesis**

Read this file before the first search, the first calculation, and the first claim of
every session. It is written for me, not for a reader who already knows the project:
everything needed to start is here, and nothing is assumed from earlier work.

---

## 0. What this project is

**The question.** Does the osmotic state of body water — systemically, and inside the
cell — act **causally** on how much fat the body builds and keeps? If it does, through
which molecular step, at what dose, and with what effect size?

**The central hypothesis** this is organised around — see
[hypotheses/H1-water-retention-lipogenesis.md](hypotheses/H1-water-retention-lipogenesis.md):

> When the body holds water, net lipid flux shifts toward storage — lipogenesis up,
> lipolysis down.

Two things about H1 shape everything below. First, it only becomes testable once
"holds water" is resolved into a **compartment** (§1.5), because intracellular and
extracellular water gain imply opposite mechanisms. Second, its serious rival is not
"no effect" but **common cause**: insulin alone retains water *and* drives storage, so
every correlation between the two is pre-explained and only interventions that move water
without moving insulin can discriminate.

Note also that H1 runs **opposite in sign** to the dehydration-survival logic in §2.2–2.3,
where water *scarcity* drives fat storage because fat banks metabolic water. That conflict
is live and recorded as C-01 in the H1 file; §1.5 and H1 §2.2 sketch how the two might be
sequential rather than contradictory, but that reconciliation is unverified construction,
not a finding.

The four title terms split cleanly into two layers, and keeping them apart is most of
the discipline this file exists to enforce:

| Layer | Terms | What it is |
|---|---|---|
| **Input / state** | osmolality, osmolarity | The thermodynamic and *measurement* layer. How much dissolved particle load there is, how it was quantified, and how much of it the cell membrane actually feels. |
| **Output / response** | adipogenesis, lipogenesis | The biological layer. Fat cell *number* (adipogenesis) and fat *synthesis* (lipogenesis) — two different things with two different literatures. |

**The shape of a finished answer.** Not "high osmolality is associated with obesity."
A finished answer names: a solute, a measured concentration inside the human
physiological range, a receptor or transcription factor, a target gene, a flux in
absolute units, and a number saying how much of the observed adiposity it accounts for.

**Out of scope.** Whether obesity is bad. Comparing weight-loss diets. Clinical
recommendations, dosing, or anything patient-specific — the project produces mechanism;
clinical decisions sit outside it. (This is a division of labour, not a judgement about
competence.)

---

## 1. Definitions I am not allowed to blur

These four terms are routinely conflated in the literature — including by authors who
know better — and each conflation destroys a quantitative claim. This section is the
reference I check against before recording anything.

### 1.1 Osmolarity vs osmolality

| | **Osmolarity** | **Osmolality** |
|---|---|---|
| Unit | mOsm / **L of solution** | mOsm / **kg of solvent (water)** |
| Basis | volume | mass |
| Temperature | **dependent** (solution volume expands) | **independent** |
| Measured or computed? | normally **computed** from concentrations | **measured** by osmometer |
| Affected by plasma solids? | **yes** | no |

Plasma is roughly **93 % water by volume**, so for the same sample the numbers are not
interchangeable: osmolarity ≈ 0.93 × osmolality. For a plasma osmolality of 290 mOsm/kg,
osmolarity is near 270 mOsm/L. **Osmolarity is the numerically smaller one.**

Consequences I must carry:

- **An osmometer measures osmolality**, by freezing-point depression (the standard) or
  vapour-pressure depression. Vapour-pressure instruments under-read volatile solutes —
  they will miss ethanol and methanol entirely. Record *which* method a paper used.
- Anything derived from a formula is **osmolarity**, even when the paper calls it
  osmolality. The common formula, in mg/dL units, is
  `2[Na⁺] + [glucose]/18 + [BUN]/2.8`. Other formulas in circulation (Bhagat, Dorwart,
  Worthley) give values differing by several mOsm, which matters when the whole effect
  being chased is a few mOsm wide. **Record the formula.**
- The **osmolal gap** (measured osmolality − calculated osmolarity) is normally under
  ~10 mOsm/kg. A larger gap means unmeasured solutes.
- **Plasma solids trap.** When triglycerides or protein are very high, the water
  fraction of plasma falls. Indirect ion-selective electrodes and flame photometry, which
  dilute the sample, then report falsely low sodium — *pseudohyponatremia* — while
  directly measured osmolality is normal. In an obesity project with hypertriglyceridemic
  subjects this is a live artefact, not a footnote. Direct ISE on undiluted sample is
  immune.

### 1.2 Osmolality vs tonicity — the distinction that decides the project

**Tonicity is *effective* osmolality:** the part contributed by solutes that cannot
freely cross the membrane. Only tonicity moves water and changes cell volume.

| Solute | Status | Why |
|---|---|---|
| Na⁺ and its anions | **effective** | excluded by the Na/K-ATPase |
| Mannitol, sucrose, raffinose | **effective** | impermeant, non-metabolised |
| **Urea** | **ineffective** | equilibrates across membranes via urea transporters |
| Glucose | **effective in aggregate**, ineffective where GLUT1 is constitutive (erythrocyte, brain endothelium) | insulin-dependent uptake limits equilibration in muscle and fat |

`Effective osmolality ≈ 2[Na⁺] + [glucose]/18` — **urea omitted.**

So: **if the mechanism under test runs through cell volume, then a rise in osmolality
caused by urea is a negative control, not an exposure.** Any claim of the form "higher
plasma osmolality → more fat storage" must say which solute carried the rise. A urea-driven
rise and a sodium-driven rise are different experiments pointing at different conclusions.

This also hands me the single best discriminating design in the whole area: compare
**mannitol** (pure tonicity, impermeant, inert) against **urea** (osmolality without
tonicity) at matched mOsm. If the effect follows mannitol, it is volume. If it follows both,
it is not volume — it is something else responding to particle load.

### 1.3 Adipogenesis vs hypertrophy

**Adipogenesis = making new adipocytes.** Mesenchymal progenitor → commitment →
preadipocyte → terminal differentiation. It changes **cell number** (hyperplasia).
Core transcriptional cascade: C/EBPβ and C/EBPδ early → **PPARγ** (necessary *and*
sufficient; the master regulator) → C/EBPα, with PPARγ and C/EBPα mutually reinforcing.
Commitment-stage factors include ZFP423 and EBF2.

**Hypertrophy = existing adipocytes getting bigger.** Changes **cell size**, not number.

These are measured differently and a paper that reports "increased fat mass," "increased
lipid accumulation," or an Oil Red O absorbance has measured **neither one cleanly**.
Legitimate readouts for adipogenesis: adipocyte number by counting or ¹⁴C birth-dating,
progenitor lineage tracing, cell-size *distribution* shifts, differentiation-marker
time courses. Lipid dye in a dish measures lipid per well, which is cell number ×
differentiation fraction × lipid per cell, all three confounded unless normalised to DNA
or counted nuclei.

### 1.4 Lipogenesis — two meanings, routinely swapped

| | **De novo lipogenesis (DNL)** | **Esterification / TAG storage** |
|---|---|---|
| What | fatty acids built from **non-lipid** precursors (glucose, fructose, acetate) | **preformed** fatty acids re-esterified into triglyceride |
| Enzymes | ACLY → ACC → FASN (→ SCD1, ELOVL6) | GPAT → AGPAT → PAP/lipin → **DGAT1/2** |
| Regulators | **ChREBP** (carbohydrate), **SREBP-1c** (insulin, LXR) | substrate supply, insulin, acylation capacity |
| Human flux | **small** | **large** |

In humans — unlike rodents — DNL is a minor route to stored fat under ordinary mixed
diets, and **adipose** DNL is especially low. So a paper reporting "lipogenesis increased
three-fold" has said very little until the baseline is known: tripling a 2 % contributor
yields 6 %. A fold change on an unreported baseline is not a quantitative result.

Also note the stoichiometry, because it links straight back to §2.2: **synthesising one
palmitate consumes 14 NADPH** (plus 8 acetyl-CoA and 7 ATP through ACC). NADPH is a
contested currency, and anything else that drains it competes with DNL.

**Measurement hierarchy** — tracer flux beats proxy, always:

1. **²H₂O (deuterated water) incorporation** — the human standard for fractional DNL.
2. **¹³C-acetate** with mass isotopomer distribution analysis (MIDA).
3. **Enzyme expression** (FASN, ACC mRNA/protein) — *not* flux. Expression can move
   without flux moving.
4. **The "DNL index"**, 16:1n-7 / 16:0 (palmitoleate/palmitate) — a **proxy only**,
   confounded by SCD1 activity and by dietary palmitate intake. Useful for ranking, not
   for absolute flux.

### 1.5 "Holding water" — which compartment

The complement of §1.2, and just as load-bearing. §1.2 said a rise in osmolality carried by
**urea does not shrink cells**. The mirror statement: **water retained with sodium does not
swell them.**

| Form | Where the water goes | Cell volume | Plasma osmolality |
|---|---|---|---|
| **Dilutional** (water without solute; SIADH, polydipsia) | everywhere, including intracellular | **swells** | ↓ |
| **Isotonic, systemic** (sodium + water; generalised oedema, saline, mineralocorticoid) | extracellular only | **unchanged** | normal |
| **Local interstitial** (lymphoedema, venous stasis — **inside adipose tissue itself**) | the adipocyte's own microenvironment | **unchanged** | normal |
| **Osmolyte-driven** (sorbitol, inositol, taurine, betaine accumulate inside) | intracellular | **swells** | unchanged or ↑ |

Four consequences I must carry:

- **Oedema is not cell swelling.** A patient with swollen ankles from isotonic sodium
  retention has no swollen adipocytes. Any mechanism running through cell volume must
  exclude this form.
- ~~which means most clinically visible "water retention" is the wrong exposure.~~
  **Corrected 2026-10-01 (R17): this does not follow, and the error nearly cost the project
  its best evidence.** "Not cell swelling" does not mean "not an exposure" — it means *a
  different exposure with different mechanisms.* In **subcutaneous adipose tissue the
  interstitium is the adipocyte's immediate microenvironment**, so fluid there acts on the
  cell without entering it: through tissue mechanics, diffusion distance and hypoxia, and
  through failure to clear the glycerol and NEFA that lipolysis releases — which can make
  lipolysis **futile while its machinery runs normally**. Full treatment in
  [H1 §3A](hypotheses/H1-water-retention-lipogenesis.md). **The error pattern: I used a
  correct mechanism as a filter on which exposures could count, instead of asking what else
  the exposure could do. A good mechanism made me stop enumerating.**
- **Local beats systemic for testing, because it localises the confound away.** Insulin
  retains water and stores fat systemically, so no whole-body observation can separate them.
  Unilateral oedema can: same person, same hormones, one limb affected, the other its own
  control. Prefer designs where the exposure is local — but **verify the "unaffected" side is
  unaffected.** In breast-cancer-related lymphoedema the contralateral arm also shows
  lymphatic dysfunction, and limbs are often sampled by different methods; I asserted this
  control was unarguable and it is not (H1 §3A.4).
- **Lymph is isosmotic to plasma, even on a high-salt diet.** It differs from plasma in
  protein (~50% in skin and muscle) and lipid, **not in tonicity**. So the lymphatic route
  and the osmolality route are **separate channels** — lymph carries lipid signals, not
  osmotic ones. Do not build circuits that join them without new evidence (H1 §3A.6).
- **A cell can hold water at normal extracellular tonicity** by accumulating organic
  osmolytes — the NFAT5 programme of §2.1. So "holding water" intracellularly does **not**
  require hypotonicity, and this is the route by which systemic hyperosmolality and
  cellular water gain could coexist rather than conflict.
- **Total body water, bioimpedance, weight, and limb volume do not distinguish any of
  these.** A measurement that cannot separate intracellular from extracellular water, or
  **adipose mass from fluid**, cannot test these hypotheses — and in oedematous tissue that
  conflation is the single commonest way a question looks answered when it is not. Name the
  compartment and the method, or the finding is uncoded.

---

## 2. The mechanistic map — where the two layers could actually meet

Candidate links, with what I think is established separated from what is not. Every
numbered item needs its primary source read at figure level before it is treated as
load-bearing.

### 2.1 Tonicity-responsive transcription — NFAT5 / TonEBP

The dedicated osmotic transcription factor (Rel family). Hypertonicity activates it;
it drives the organic-osmolyte machinery: **AKR1B1** (aldose reductase → sorbitol),
**SLC5A3** (SMIT, myo-inositol), **SLC6A12** (BGT1, betaine), and heat-shock proteins.

This is the most direct **tonicity → named target gene** pathway available, which makes
it the strongest candidate for a specific mechanistic step rather than a vague
"osmotic stress" story. NFAT5 also has reported roles in adipose tissue inflammation
and insulin resistance — a second entry point into the output layer, and one worth
checking carefully for reverse causality.

The cell's osmolyte repertoire (sorbitol, myo-inositol, betaine, taurine,
glycerophosphocholine) matters for a reason that is easy to miss: **the cell's response
to tonicity is to accumulate solutes, not just to move water.** Chronic hypertonic
adaptation is a changed metabolic state, not merely a shrunken cell.

### 2.2 The polyol pathway — tonicity, NADPH, and endogenous fructose

Glucose → **sorbitol** (aldose reductase/AKR1B1, **consumes NADPH**) → **fructose**
(sorbitol dehydrogenase, generates NADH).

Three things converge here, which is why this is probably the richest node on the map:

1. **Sorbitol is itself an osmolyte** — polyol accumulation is osmotically active (the
   classical explanation for diabetic cataract). So high glucose generates an
   *intracellular* osmotic load, and AKR1B1 is NFAT5-driven. Tonicity and the polyol
   pathway are mutually reinforcing, not merely adjacent.
2. **NADPH competition.** Aldose reductase drains the same NADPH that FASN needs 14 of
   per palmitate. This predicts polyol flux and DNL *compete* — a sharp, testable,
   non-obvious consequence that I should look for and should also look for refutation of.
3. **Endogenous fructose.** The pathway generates fructose from glucose without any
   dietary fructose. Fructose then goes to **ketohexokinase-C (KHK-C)**, whose high
   affinity and lack of negative feedback causes ATP depletion → AMP → IMP → **uric
   acid**, alongside lipogenic signalling. This is the substance of the "fructose survival"
   line of argument, and a KHK inhibitor has reached human Phase 2 trials — meaning a
   genuine interventional test of this limb exists in humans, not just in mice.

### 2.3 The vasopressin axis — osmolality's own hormone

Rising plasma osmolality is the primary stimulus for AVP. Threshold is near
**280–285 mOsm/kg**, with thirst set slightly higher; the response is steep.
**Copeptin** is the stable, assayable surrogate for AVP.

Receptor separation is mandatory here and is frequently botched:

| Receptor | Site | Effect |
|---|---|---|
| **V1a** | liver, vasculature | glycogenolysis, vasoconstriction |
| **V1b** | anterior pituitary | **ACTH → cortisol** |
| **V2** | renal collecting duct | water reabsorption |

A paper or a drug that does not distinguish V1a from V1b cannot support a claim about
either. Treat "vasopressin receptor" without a subscript as uncoded.

The V1b branch gives a complete, fully-named chain from the input layer to the output
layer: **osmolality ↑ → AVP ↑ → V1b → ACTH → cortisol → adipose 11β-HSD1 (amplifying
local cortisol, with H6PDH supplying luminal NADPH) → PPARγ-dependent adipogenesis.**
Every individual step here is documented somewhere. **The chain as a whole is not**, and
its quantitative sufficiency is entirely untested. I must keep saying so: a chain of
individually-true steps is a hypothesis, not a mechanism, until the flux through it is
measured.

**Sex asymmetry worth tracking:** oestrogen lowers the osmotic threshold for AVP release
and for thirst — in pregnancy the whole set point shifts down by roughly 10 mOsm/kg. If
this project keeps finding sex differences, this axis is a candidate explanation rather
than a nuisance.

### 2.4 Cell-volume sensing in the adipocyte — SWELL1 / LRRC8A

LRRC8A is the obligatory subunit of the volume-regulated anion channel (VRAC). Reported
to be required for insulin → PI3K → AKT signalling **in adipocytes**, with
adipocyte-specific loss producing insulin resistance.

If that holds up at figure level, it is the strongest Z-type mechanistic link available:
a **molecularly defined volume sensor sitting directly on the insulin pathway in the
target cell type.** It deserves to be checked before anything else on this map, because
it would turn "cell volume affects fat storage" from an analogy into a pathway.

### 2.5 Cell swelling as an anabolic signal

The hepatocyte literature holds that swelling is anabolic (glycogen synthesis, protein
synthesis, lipogenesis up) and shrinkage catabolic (proteolysis, glycogenolysis up), partly
through integrin and MAPK signalling and through Na-dependent amino-acid uptake, which
itself swells the cell.

**Flagged tension, to resolve rather than repeat:** this rule does not obviously transfer
between cell types. Hepatocyte swelling reads as anabolic, whereas a lipid-engorged,
enlarged adipocyte is associated with insulin resistance and elevated lipolysis — the
opposite sign. Either the rule is liver-specific, or "swelling" means something different
in a cell whose volume is mostly a lipid droplet rather than cytosol. **I should not use
"swelling = anabolic" as a general premise until this is settled.** My current best guess
is that the lipid droplet makes adipocyte volume a poor proxy for cytosolic water, which
would mean the two literatures are not in conflict but are not about the same variable
either. That is a guess, and labelled as one.

### 2.6 Dietary sodium

Sodium intake shows associations with adiposity that survive some adjustment for energy
intake. At least three mechanisms compete, and they are not mutually exclusive:

1. Osmotic stress → aldose reductase / fructokinase induction → endogenous fructose
   (the §2.2 route);
2. Salt-driven thirst and beverage choice;
3. **Palatability → passive overconsumption** — the plainest explanation, with human
   randomised support, and therefore the one that must be excluded before any osmotic
   interpretation is credible.

Mechanism 3 is the control condition for mechanisms 1 and 2. An osmolality–adiposity
association that has not been tested against taste and energy intake is not yet evidence
of an osmotic mechanism.

### 2.8 The re-esterification gate (M8) — the best-supported mechanism in the project

Added 2026-10-02 from [H2](hypotheses/H2-depletion-gates-lipolysis.md). **Hydrolysis and
re-esterification run simultaneously, so net lipolysis is a margin, not a switch.** Adipocytes
lack glycerol kinase, so re-esterification needs **glycerol-3-phosphate** from glucose or from
**glyceroneogenesis** (PEPCK-C rate-limiting, and *induced by fasting*, defending the pool
exactly when it would run down).

Three depletable control points: **G3P** (substrate), **G0S2** (an ATGL-inhibiting protein that
adipose tissue degrades on fasting), and **adipose glycogen** (which has a set point, and whose
enhancement *decreases* triglyceride mobilisation).

**Why it outranks M1–M7:** adipose **PEPCK-C overexpression alone produces obesity** without
insulin resistance — the only **sufficiency** result in this project. **Leptin** opens the gate
(PEPCK nitration); **thiazolidinediones** close it (PEPCK induction, confirmed in human adipose)
and that, not fluid, is why they cause fat gain.

**The consequence for everything else here:** a therapy that raises hydrolysis without closing
re-esterification changes nothing. The organism can hold fat while hydrolysing continuously, just
by putting the products back.

### 2.7 The storage direction — nodes that do both halves of H1

Two candidates belong on the map because, unlike everything above, each produces **both**
halves of H1 — synthesis up *and* breakdown down — from a single node. Full treatment in
[the H1 file §3](hypotheses/H1-water-retention-lipogenesis.md); the map entries:

- **mTORC1.** → SREBP-1c → FASN/ACC (lipogenesis up), and suppresses ATGL (lipolysis down).
  Reported volume-sensitive: inhibited by hyperosmotic shrinkage, activated by swelling and
  by the Na-dependent amino-acid uptake that itself swells the cell. If H1 is true, this is
  the most likely transducer. Check whether the hypo-osmotic *activation* arm is actually
  evidenced or merely assumed by symmetry from the inhibition arm.
- **AQP7.** The adipocyte **aquaglyceroporin** — one protein channelling both water and
  the glycerol that lipolysis releases. The most literal water/lipid coupling available:
  impaired glycerol export traps glycerol, feeds glycerol kinase → glycerol-3-phosphate →
  re-esterification, making lipolysis **futile** and raising net storage without touching
  the lipolytic machinery. Knockout obesity phenotype is **contested** — resolve before use.

Counter-entry, recorded so it is not mistaken for support: **AMPK.** Shrinkage activates it
and it inhibits ACC, which fits. But it is also reported antilipolytic in adipocytes
(HSL Ser565), so shrinkage would suppress lipolysis too — breaking H1's second half.
AMPK is a tension in this map, not a pillar.

---

## 3. Rules (binding)

Each of these exists because of a specific way this subject matter goes wrong. They are
not general research hygiene.

**R1 — Never record "osmolality" when the source gave osmolarity, or vice versa.**
Record unit, method (measured vs computed), and the formula if computed. §1.1.

**R2 — Any claim about cell volume uses tonicity, never total osmolality.**
Name the solute that carried the change. State whether it is effective or ineffective.
§1.2.

**R3 — Separate cell number from cell size.** "More fat," "more lipid," and an Oil Red O
reading are none of: adipogenesis, hypertrophy, or flux. Name the readout and what it
normalises to. §1.3.

**R4 — Separate DNL from esterification, and name the tracer.** Enzyme expression is not
flux. The 16:1n-7/16:0 index is a proxy and is labelled as one. §1.4.

**R5 — Absolute values and baselines, always.** A fold change without a baseline is not
recorded as a result. Record n, the dispersion measure *and which one it is* (SD vs SEM vs
IQR), and the confidence interval.

**R6 — Osmotic dose realism, against this scale.** Every in vitro or in vivo exposure gets
positioned on it:

| Plasma osmolality | State |
|---|---|
| 275–295 mOsm/kg | normal human range |
| ~300–310 | dehydration |
| 320–380 | DKA / hyperosmolar hyperglycaemic state |
| >350 | approaching lethal |

Human plasma essentially never sustains 400 mOsm/kg. A culture experiment at
400–500 mOsm/kg is not modelling human physiology; it generates hypotheses only, and is
recorded as such.

**R7 — Report the absolute final osmolality of culture medium, measured.** Baseline DMEM
already sits well above plasma (commonly ~320–350 mOsm/kg). "+50 mOsm" from that baseline
is **not** 290 → 340. Most papers state the increment and never the absolute value, which
makes the increment uninterpretable. If the absolute value is unavailable, the finding is
uncoded on the exposure axis.

**R8 — Species and model limits are stated, not assumed away.**
Rodent DNL ≫ human DNL, so rodent lipogenesis data does not transfer quantitatively.
Mice housed at ~22 °C are chronically cold-stressed, which distorts energy expenditure and
brown-fat data. **3T3-L1 cells are already-committed preadipocytes** — they model terminal
differentiation, not commitment; commitment needs primary progenitors or stromal-vascular
fraction. And the standard differentiation cocktail (IBMX + micromolar dexamethasone +
insulin far above physiological, often plus a thiazolidinedione) is supraphysiological **by
construction** — so every 3T3-L1 result starts out exposure-unrealistic, before any
osmotic manipulation is added on top.

**R9 — Reverse causality is addressed explicitly for every cross-sectional finding.**
Adiposity itself alters hydration status, plasma volume, the water fraction of plasma,
renal function, and AVP tone. For any osmolality–adiposity association the question
"could the adiposity have produced this?" is answered — with longitudinal ordering,
genetic instruments, or a reversal experiment — before a mechanistic record is opened.

**R10 — Confounders named before the model is fitted.** For this subject, at minimum:
renal function (eGFR), glycaemia, diuretics and other medications, assay era and
analyser change, and total energy intake. A secular trend in any laboratory marker is
assumed to be an assay artefact until that is ruled out.

**R11 — Write the prediction before looking.** Numbered, in the session file, before the
first search or query. Afterwards, mark explicitly which predictions were **wrong**. A
prediction recorded after the result is worthless and recording one that way is
prohibited.

**R12 — Search against the hypothesis as a separate, deliberate pass.** Finding
supporting evidence does not end the question. Run explicit null/failed-replication
searches. A session does not close without this pass. If nothing was found, record the
queries and the date — "searched, found nothing" is a result.

**R13 — Compute rather than cite, where the data allow it.** If open data (NHANES, WHO,
FAO, World Bank) can answer it, calculate it instead of quoting someone. Write the
analysis plan — single primary outcome, pre-specified interpretation rule, stated
limitations — into the script's docstring **before touching the data**. Changing the
outcome afterwards is prohibited. Persist every headline number to CSV; a result that
exists only in console output has to be recomputed to be verified.

**R14 — Primary sources, at figure level.** Abstracts, discussions, and conclusions are
*claims*. Data are figures, tables, and supplements. Reviews are for mining citations,
never for sourcing a claim. If a claim's citation chain dead-ends without original data,
record that — those gaps are findings about the field.

**R15 — Causal language is coded, not implied.** Every claim gets one of: **necessary**
(absence prevents it), **sufficient** (alone produces it), **contributory** (measured
effect, not alone sufficient), **permissive** (enables another factor), **correlational**
(direction unknown — and this one may never be used to support a mechanism).

**R16 — Mark my own inferences.** When I connect two findings in a way no source does,
the sentence says so: *(my inference, not shown)*. Non-negotiable — it is the only thing
that makes my reasoning auditable later.

**R17 — When I am wrong, strike through, don't delete.** Keep the original text with
`~~strikethrough~~`, add the refutation and its source next to it. The record of being
wrong is the most reusable thing in the project.

**R18 — Numbers in this file are from memory until verified.** See §4.

**R18c — A number from a search summary is not a number from a source.** R18 quarantines what
I recall; this quarantines what I have read *once, second-hand*. A figure seen only in a search
result or an abstract snippet is provisional: it may be cited as provisional, never built on, and
never promoted to a headline until its primary source has been read at figure level. The instance:
I called an unverified 0–100% range "the most important number in this project" on one snippet,
and had to demote it the next session (H2 §10.1). **The attractiveness of a number is not evidence
for it — and it is a reason to check harder, because it is exactly when I will not want to.**

**R18b — An n-of-1 observation is D8/E1: it starts searches, it never supports claims.** The
subject's own observations go in `observations/` **quoted unaltered**, with the separable claims
inside them numbered so each can be tested on its own. They may direct the literature and they
may be the reason a mechanism gets looked at — they may **never** appear beside a measured
finding as though the two weighed the same. And the load-bearing claim in an observation is
usually the one that feels most obvious to the observer: name it and design its test first.

**R19 — Read the preparation, not just the result.** How the sample was obtained can
manufacture the finding. The instance that produced this rule: I recorded "lymphoedema fluid
has ~3× the FFA of serum" without noting the fluid was **centrifuged liposuction aspirate,
freeze–thawed** — a process that ruptures adipocytes and releases fatty acid regardless of
interstitial concentration. Careful groups in the same field biopsy *before* tumescent
infiltration precisely to avoid this. **R14's "figure level" includes the methods section.**
For this project specifically, always ask: liposuction aspirate or surgical biopsy? Cannulated
lymph or tissue homogenate? Freeze–thawed? Ex vivo incubation that washes away the very
gradient under study?

**R22 — A counter-evidence entry must also record what the finding supports.** "Evidence
against H1" is not a complete description of a datum. The instance: I filed higher lipolysis and
an elevated FFA:glycerol ratio in lymphoedema as two separate contradictions, and never asked
what they were evidence *for* — they are one coherent finding about an open re-esterification
gate (H2 §4.6). A refuted hypothesis does not make its data inert. Every row in
[claims.md](claims.md) marked as counter-evidence gets a second question: **if not this, then
what?**

**R21 — Name the tissue before claiming the pathway.** A correct mechanism applied in the
wrong compartment is the error this project makes most. Twice now: the lymphatic clearance
mechanism (dead — NEFA leave by capillary, session 2) and the PFK-1 bypass (hepatic only —
muscle hexokinase puts fructose *above* the block, G01 §3.5). Before asserting that a pathway
operates, check that the tissue in question **has the enzymes and transporters that pathway
needs**. Correct biochemistry, wrong location, is still wrong.

**R20 — Transport out of a tissue is size-gated; state the molecular radius.** Lymph-vs-
capillary partitioning from human adipose tissue runs from **14% lymphatic at 1.18 nm to 100%
at 3.24 nm**. So "impaired clearance" is never a claim about a tissue — it is a claim about a
**molecule**. Small lipophilic species (NEFA ~0.4 nm, glycerol 92 Da) leave by capillary and
are untouched by lymphatic obstruction; proteins above ~3 nm are entirely lymph-dependent.
Any clearance argument must name the species and its radius, or it is not an argument
([claims.md §D](claims.md)).

---

## 4. Quantitative anchors — ⚠ UNVERIFIED

**Every number below is recalled from training, not read from a source in this session.**
They are here so I can orient and sanity-check magnitudes quickly. **None may be cited,
quoted, or used in a calculation until I have read its primary source and moved it into a
verified record with full provenance.** Treating this table as sourced would be exactly
the failure mode R14 exists to prevent.

| Quantity | Approximate value | Status |
|---|---|---|
| Normal plasma osmolality | 275–295 mOsm/kg | ⚠ verify |
| Plasma water fraction | ~93 % by volume | ⚠ verify |
| Normal osmolal gap | < ~10 mOsm/kg | ⚠ verify |
| AVP osmotic threshold | ~280–285 mOsm/kg | ⚠ verify |
| Pregnancy set-point shift | ~−10 mOsm/kg | ⚠ verify |
| NADPH per palmitate (FASN) | 14 | ⚠ verify (stoichiometric, but check) |
| Hepatic DNL share of liver TG in fatty liver | ~25 %, with NEFA ~60 %, diet ~15 % | ⚠ verify — widely cited, check the original |
| Fasting hepatic DNL, lean | low single-digit % of VLDL-TG | ⚠ verify |
| Adult adipocyte turnover | ~10 % / year | ⚠ verify |
| Adipocyte number, lean adult | ~4–6 × 10¹⁰ | ⚠ verify |
| Typical DMEM osmolality | ~320–350 mOsm/kg | ⚠ verify — and measure, don't assume |

---

## 5. How a session runs

1. **Read this file.** Especially §1 (definitions), §3 (rules), §4 (nothing here is
   sourced yet).
2. **Pick one question** from §6 or a successor list. One primary question per session.
3. **Write numbered predictions** before any search or query (R11).
4. **Work:** search, or compute (R13). Primary sources at figure level (R14).
5. **Counter-evidence pass** (R12) — separate, deliberate, recorded.
6. **Close the session by auditing it:** which predictions were wrong, which claims
   weakened, what counter-evidence appeared, what was unexpected. Wrong predictions get
   written down permanently — they are the error-pattern record that stops me repeating
   myself.
7. **Update this file in the same session** if a definition sharpened, a rule earned its
   place, or an operational fact was learned the hard way (a URL, a column name, a trap).
   A guide updated "later" is a guide that goes stale.

---

## 6. Opening questions

Unanswered, ordered by how much they would change the map. The live queue is
**[H1 §4 (discriminating tests) and §8 (first actions)](hypotheses/H1-water-retention-lipogenesis.md)**;
what follows are the standing questions that outlive any one hypothesis.

**Q1 — In long-standing unilateral lymphoedema, does the affected limb carry more *fat*
than the contralateral limb?** The project's lead question. Requires adipose mass segmented
from fluid by imaging — limb volume and circumference conflate the two and are why this may
look settled when it is not (§1.5). Its power is the within-subject control: one person, one
insulin concentration, one affected limb (H1 §3A.4).

**Q2 — Is it the water or the lymph?** Chronic venous insufficiency and chronic lymphoedema
both expand subcutaneous interstitium; only the second involves lymph stasis. If both cause
local fat gain, the agent is fluid volume; if only lymphoedema does, "holding water" is a
misdescription of the mechanism (H1 §3A.5). Likely unasked, and highly answerable.

**Q3 — Does oedema without fat gain exist?** Dihydropyridine-induced oedema versus
thiazolidinedione-induced oedema, in trial data that already exists. Note this tests only
the *systemic* extracellular form, which §1.5's correction shows was never the interesting
one.

**Q4 — Does chronic dilutional water retention raise fat mass?** SIADH and primary
polydipsia are years-long natural experiments. Needs **body composition**, not weight —
weight change in hyponatremia is mostly water and tells us nothing. I expect this to be
unasked rather than answered.

**Q5 — Is there any human evidence that plasma tonicity, as opposed to total osmolality,
tracks adiposity?** Requires solute decomposition (§1.2), eGFR and glycaemia control
(R10), and a reverse-causality answer (R9). If the association lives entirely in urea, the
cell-volume premise is dead and should be declared dead.

**Q6 — Does LRRC8A/SWELL1 in adipocytes hold up at figure level?** (§2.4) Verify the
insulin-signalling dependence, the knockout phenotype, and the direction — including the
apparent paradox that VRAC's canonical role is to shrink the cell back.

**Q7 — Has the mannitol-vs-urea discrimination (§1.2) ever actually been run on
adipogenesis or DNL?** If yes, it may settle the mechanism directly. If no, it is the
experiment this project should be designing.

**Q8 — Does osmotic stress change adipogenesis in vitro, and in which direction?** I
believe the literature is genuinely contradictory here. Resolve it by **stratifying on
absolute final medium osmolality (R7) and on solute identity**, rather than by pooling —
my working suspicion is that the apparent contradiction is a dose and solute artefact.
*(My inference, not shown.)*

**Q9 — Do polyol flux and DNL actually compete for NADPH?** (§2.2) Sharp prediction,
clear refutation condition. Look for both.

**Q10 — Where is the osmolality → adipogenesis chain in §2.3 quantitatively broken?**
Every step has support; the chain has none. Identify the weakest link and the flux
measurement that would test it.

**Q11 — Is the sodium–adiposity association separable from palatability?** (§2.6) Until
taste and energy intake are controlled, no osmotic reading of it is admissible.

**Q12 — Does the swelling-anabolism rule apply to adipocytes at all?** (§2.5) Resolve
the liver/adipocyte sign conflict, or establish that cytosolic water and cell volume
come apart in a lipid-laden cell.

---

## 7. Record-keeping

Kept deliberately thin at version 0.1 — structure should follow the work rather than be
guessed in advance. Current convention:

| What | Where |
|---|---|
| This guide | `guide.md` |
| Hypothesis cards | `hypotheses/` — one file per hypothesis: claim stated falsifiably, mechanism candidates, discriminating tests, **death conditions**, predictions written before searching |
| Subject observations | `observations/Gxx-*.md` — n-of-1 self-observations, **quoted unaltered**, coded **D8/E1** |
| Interventions | `interventions.md` — agents evaluated by evidence quality against a named mechanism. Evaluation only, never a protocol |
| Session logs | `sessions/` — one file per session: predictions → work → counter-evidence pass → audit |
| Verified quantitative claims | `claims.md` — one row per claim: value, units, model system, design and exposure coding, causal code (R15), counter-evidence column (never left empty) |
| Analysis scripts and outputs | `analysis/` — plan in the docstring before data (R13), results to CSV |
| Known gaps | `gaps.md` — what is missing, why it matters, where it could come from |

Conventions: units on every number. Confidence intervals as `[low, high]`. Relative links
between files. Dispersion measures named, never left ambiguous.

---

*v0.1 — written at the start of the osmolality/adipogenesis line of work. Expected to be
wrong in places; §3 R17 says how to record that.*
