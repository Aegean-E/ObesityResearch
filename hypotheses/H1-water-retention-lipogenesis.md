# H1 — Water retention shifts net lipid flux toward storage

**Status:** open, unverified · opened 2026-10-01 · the project's central hypothesis
**Governed by** [guide.md](../guide.md). Where this file and the guide conflict, the guide wins.

---

## 1. The claim

**Loose form (as posed):** when the body holds water, it increases lipogenesis and
inhibits lipolysis.

That sentence is not yet testable, because "holds water" names three physiologically
distinct states with **opposite** implications for the mechanism, and because "the body
tries to" could mean either a causal or a correlational relationship. Both have to be
pinned down before a single search is worth running.

### 1.1 Which water?

| Form | Compartment | Does the cell swell? | Plasma osmolality |
|---|---|---|---|
| **H1a — cellular** | intracellular water ↑ | **yes** | ↓ if dilutional; unchanged if osmolyte-driven |
| **H1b — systemic extracellular** | plasma volume / generalised ECF ↑ | **no** | normal |
| **H1b′ — local interstitial** | **interstitial fluid ↑ within subcutaneous adipose tissue itself** | **no — and it does not need to** | normal |
| **H1c — program** | either; water is a *marker* | irrelevant | either |

Isotonic sodium-plus-water retention expands the extracellular space **without changing
cell volume at all** — water follows sodium and stays outside the cell. This is the exact
mirror of the tonicity rule in [guide.md §1.2](../guide.md): there, a rise in osmolality
carried by urea does not shrink cells; here, water retained with sodium does not swell them.

~~So if the mechanism runs through cell volume, then ordinary edema is *not* the exposure,
and a patient with swollen ankles is not an instance of the hypothesis.~~

**Correction, 2026-10-01 (guide R17) — this was wrong, and wrong in a way that nearly cost
the project its best evidence.** The inference above smuggles in an assumption: that the
*only* route by which extracellular water could matter is by changing cell volume. That
assumption fails for one compartment specifically — **subcutaneous adipose tissue**, where
the interstitium *is the adipocyte's immediate microenvironment*. Fluid accumulating there
does not need to enter the adipocyte to act on it. It changes the tissue's mechanics, its
diffusion distances, and the clearance of lipolysis products — each a route to lipid flux
that bypasses cell volume entirely (§3A).

So **H1b′ is a distinct hypothesis, not a weaker version of H1a**, and it has an enormous
methodological advantage over everything else in this file: **it can be localised.** Which
means it can beat the insulin null (§1.2) that no systemic observation can beat. See §3A.4.

**The error pattern, recorded for reuse:** I had one correct mechanism (cell volume) and
used it as a *filter* on which exposures could count, rather than asking what *else* the
exposure could do. Having a good mechanism made me stop enumerating. Watch for this.

### 1.2 Causal or coincident?

- **H1a/H1b (causal):** water itself — cell volume, or the water load — is the *proximate
  signal* that raises synthesis and suppresses breakdown.
- **H1c (common cause):** an upstream signal (insulin, vasopressin, aldosterone,
  glucocorticoid, PPARγ) independently produces both water retention and lipid storage.
  The water is then a **marker with no causal role**, and intervening on it does nothing.

H1c is the serious rival, not a technicality. Insulin alone produces both halves:
it is directly antinatriuretic (proximal NHE3, distal ENaC → sodium and water retention)
*and* lipogenic *and* antilipolytic. Any observed pairing of water retention with fat gain
is explained by insulin without any causal role for the water whatsoever. **H1c is the
null hypothesis this project has to beat.**

### 1.3 Stated to be falsifiable

> **H1a:** An increase in *intracellular* water in hepatocytes and adipocytes shifts net
> lipid flux toward storage — de novo lipogenesis and esterification up, lipolysis down —
> and does so **through cell volume itself**, such that swelling the cell by a means with
> no hormonal arm reproduces the effect.

The final clause is what makes it a hypothesis rather than a restatement of insulin action.

---

## 2. Why this is mechanistically principled, not arbitrary

The strongest argument for H1a is not any single paper. It is that **a cell cannot
increase its mass without increasing its volume.** Volume and content are not separable:
growth *is* simultaneous water and macromolecule accumulation. A controller that reads
volume is therefore reading a quantity physically welded to anabolism, which makes
volume-sensing a natural place for the cell to put its synthesis/breakdown switch.

Under that reading, swelling is not a *signal to grow* sitting arbitrarily upstream of
growth. It is **part of growing**, and the cell exploits it as a controller because it is
already there and cannot be faked.

*(My inference, not shown — this is a rationale for taking H1a seriously, not evidence
for it.)*

### 2.1 The teleological problem — and it cuts against us

If "water is plentiful" were a signal to store fat, the adaptive logic would be
backwards. Oxidising fat **yields metabolic water** — roughly 1.07 g water per g of fat,
more than carbohydrate yields per gram. Fat is, among other things, a **water store**
(the camel's hump argument). The adaptive pressure therefore runs the *other* way:
**dehydration** should drive fat synthesis, because fat is how you bank water.

That is precisely the vasopressin/fructose "survival" logic in
[guide.md §2.2–2.3](../guide.md), and it is **opposite in sign to H1a.**

| | Signal | Response | Logic |
|---|---|---|---|
| **H1a** | water abundance / swelling | store fat | growth requires volume |
| **Survival logic** | water scarcity / AVP | store fat | fat banks water |

**Both cannot be the dominant route.** Recorded as the project's first real conflict:

> **C-01 — Sign conflict.** Cell-volume anabolism predicts water *gain* drives storage.
> Dehydration-survival logic predicts water *loss* drives storage. Either one dominates,
> or they operate in different compartments or on different timescales, or one is wrong.

### 2.2 A possible reconciliation — and it is testable

The two may be **sequential rather than contradictory**:

> hypertonic signal → NFAT5/TonEBP → organic osmolyte accumulation (sorbitol via aldose
> reductase, myo-inositol, taurine, betaine) → **the cell now holds more water at
> unchanged extracellular tonicity** → swelling → anabolic

On this reading the *systemic* signal is dehydration and high osmolality, while the
*cellular* state downstream is a swollen, osmolyte-loaded, anabolic cell. The organism is
dehydrated; the adipocyte is waterlogged. Both literatures are then right about different
compartments.

This is attractive, so it needs guarding: it is currently **my construction, not a
finding** *(my inference, not shown)*. It predicts something sharp and checkable — that
intracellular osmolyte content and cell water rise in adipose tissue under systemic
hyperosmolality — and that prediction is where it should be attacked.

---

## 3A. The subcutaneous route (H1b′) — mechanisms that bypass cell volume

Added 2026-10-01 after the §1.1 correction. These act on the adipocyte **from the
interstitium**, with no change in cell volume required. Three are clearance/transport
arguments and one is mechanical; together they make H1b′ the strongest-supported form of
the hypothesis, mostly because of §3A.4.

### 3A.1 Clearance failure makes lipolysis futile ★ the tissue-level AQP7

This is the same logic as [§3.4](#34-aqp7--water-and-glycerol-through-the-same-protein) one
scale up, and it may be the cleanest answer to the "inhibits lipolysis" half of the
hypothesis.

Lipolysis releases **glycerol** and **non-esterified fatty acids** into the interstitium.
Both must then *leave the tissue* — NEFA albumin-bound into capillary blood, with lymph
carrying its share. If the interstitium is stagnant, both products accumulate locally and
are available for **re-esterification** (glycerol → glycerol kinase → glycerol-3-phosphate;
NEFA → re-acylation).

The consequence is sharp: **gross lipolysis can run at a completely normal rate while net
lipolysis falls to zero.** Nothing in the lipolytic machinery changes — no HSL, no ATGL, no
perilipin. The hypothesis's second half is satisfied by a *transport* failure rather than a
*signalling* one. Triglyceride–fatty-acid futile cycling is the mechanism, and it is
thermodynamically wasteful but metabolically silent from outside.

**This is measurable in humans with existing technique.** Adipose tissue **microdialysis**
recovers interstitial glycerol and NEFA directly. A paired measurement in affected vs
unaffected limb in unilateral lymphoedema would test it, with each patient as their own
control. No new method required. *(My inference that this has not been done — verify.)*

### 3A.2 Diffusion distance → local hypoxia → HIF-1α

Interstitial fluid accumulation increases the distance from capillary to adipocyte. Oxygen
delivery is diffusion-limited in adipose tissue, so expanded interstitium means **local
hypoxia**, independent of any systemic change.

HIF-1α then: suppresses fatty-acid oxidation (CPT1), upregulates lipid-droplet proteins
(PLIN2), promotes lipid storage, and drives local fibrosis and inflammation. Adipose tissue
hypoxia is a well-documented feature of obese adipose tissue — but normally framed as a
*consequence* of adipocyte hypertrophy outgrowing its blood supply. H1b′ proposes the
**reverse arrow**: interstitial expansion causes the hypoxia, which causes the storage.
Same two variables, opposite causality — so this is a reverse-causality problem
(guide R9) before it is evidence, and must be argued on timing, not association.

**Contested on the lipolysis half:** hypoxia is variously reported to raise basal lipolysis
and to blunt catecholamine-stimulated lipolysis. Do not present this as settled.

### 3A.3 Tissue mechanics → YAP/TAZ → adipogenesis

Adipogenesis is mechanosensitive, and the direction favours H1b′: **stiff/high-tension
substrates keep YAP/TAZ active and suppress PPARγ-driven differentiation, while soft,
compliant, low-tension conditions permit it.**

Interstitial fluid loosens and hydrates the matrix, reducing mechanical restraint on
resident progenitors. This connects to the **adipose expandability** literature: tissue
that cannot expand (fibrotic, stiff) drives ectopic fat and metabolic disease, while
compliant tissue stores safely. On that reading, interstitial fluid is **permissive** —
guide R15's category — rather than instructive. It does not tell progenitors to
differentiate; it removes the mechanical reason they were not.

Note the tension with §3A.2: fluid cannot straightforwardly both loosen the matrix *and*
drive the fibrosis that stiffens it. Either they act on different timescales — acute
loosening, chronic fibrosis — or one is wrong. **Unresolved; do not use both at once
without saying which phase.**

### 3A.4 Lymphoedema — the natural experiment, and it defeats the insulin null ★★

**This is the most important item in the file, and I missed it entirely in v0.1.**

Chronic lymphoedema is sustained, localised accumulation of subcutaneous interstitial
fluid. And the affected limb does not merely hold fluid — **it accumulates adipose
tissue.** The clinical signature is well known: long-standing lymphoedematous limbs show
genuine adipose hypertrophy, and liposuction is used therapeutically *precisely because* a
large share of the excess limb volume turns out to be fat rather than water.

Why this outranks every test in §4:

> **Lymphoedema is usually unilateral. Insulin is systemic.**

The insulin common-cause null (§1.2, §3.5) explains any *systemic* pairing of water
retention with fat gain, and no observational systemic design can escape it. But it
**cannot explain why one limb gains fat and the other does not in the same person at the
same insulin concentration.** The contralateral limb is a within-subject control that
removes insulin, cortisol, aldosterone, PPARγ, diet, activity, genotype, and age at a
stroke.

That makes unilateral lymphoedema the one available setting where H1b′ is testable against
its hardest rival using humans who already exist. Everything else in this file is either
in vitro or confounded.

**Animal support:** lymphatic insufficiency models — *Prox1* haploinsufficiency most
notably — have been reported to produce **adult-onset obesity**, with adipose accumulating
around leaky lymphatic vessels. If that holds, it is lymph-driven adipogenesis in vivo,
with the leak as the cause rather than the consequence.

### 3A.5 Is it the water, or the lymph? — the discriminating test

The §3A.4 observation has an alternative reading that must be separated out, because it
changes the whole hypothesis: perhaps it is not interstitial **fluid volume** at all, but
the **composition** of stagnant lymph, or the lymphatic failure itself.

Lymph carries albumin, lipoproteins, fatty acids, cytokines and immune cells. The *Prox1*
work reportedly showed **lymph fluid itself promotes preadipocyte differentiation** in
culture — which would make the adipogenic agent a solute in the lymph, not the water
carrying it.

**The test writes itself, and it is the best one in the project:**

> **Venous oedema versus lymphatic oedema.**
> Chronic venous insufficiency and chronic lymphoedema both produce subcutaneous
> interstitial fluid accumulation in a limb. Only the second involves lymphatic failure
> and lymph stasis.
> → If **both** cause local fat gain, the agent is interstitial fluid volume (H1b′ proper).
> → If **only lymphoedema** does, the agent is lymph composition or lymphatic transport,
> and "holding water" is the wrong description of the mechanism.

A supporting observation points toward the second answer and should be taken seriously:
ordinary dependent oedema is maximal at the ankles, yet **ankle fat deposition is not a
recognised phenomenon**, while typical fat distribution (hip, thigh, abdomen) does not
follow gravity at all. If fluid volume per se were sufficient, chronic dependent oedema
should fatten ankles. As far as I know it does not — which already argues that fluid alone
is insufficient and the lymphatic limb is doing the work. **Check this before relying on
it; it is an argument from my own absence of knowledge, which is weak evidence
(guide R12).**

### 3A.6 Local sodium storage, NFAT5, and lymphatics — the convergence

The subcutaneous interstitium is where several threads already on the map physically meet,
which is either a sign the map is right or a sign I am pattern-matching. Recorded so it can
be checked rather than admired:

Skin and subcutaneous tissue store **sodium bound to glycosaminoglycans, without
commensurate water** — non-osmotic sodium storage, with ²³Na-MRI reporting elevated tissue
sodium in obesity, diabetes and hypertension. That stored sodium creates **local
hypertonicity**, which activates **NFAT5** ([guide.md §2.1](../guide.md)) in resident
macrophages, which drives **VEGF-C** and **lymphangiogenesis** as a clearance response.

So in one tissue: local tonicity → NFAT5 → lymphatic capacity → interstitial fluid
clearance → (§3A.1) lipolysis-product removal and (§3A.4) adipose accumulation. The input
layer and output layer of this project meet in the subcutaneous interstitium, with NFAT5
as the hinge.

**This is the most attractive idea in the file and therefore the most dangerous.** Every
arrow is individually reported; the circuit is my assembly *(my inference, not shown)*. Its
value is that it is falsifiable at the hinge: if tissue sodium does not predict local
adiposity independently of BMI, the convergence is decorative.

---

## 3. Candidate mechanisms, ranked by how much they would explain

### 3.1 mTORC1 — one node, both halves ★ strongest

mTORC1 is the only candidate I can identify that produces **both** halves of the
hypothesis from a single node:

- **Lipogenesis up:** mTORC1 → SREBP-1c → FASN, ACC, SCD1.
- **Lipolysis down:** mTORC1 suppresses ATGL; mTOR inhibition *raises* lipolysis.
- **Volume-sensitive:** hypo-osmotic swelling reported to activate mTORC1, hyperosmotic
  shrinkage to inhibit it; Na-dependent amino-acid uptake both swells the cell and feeds
  mTORC1, so the two inputs are hard to separate — which is itself a clue that they are
  the same input.

**If H1a is true, mTORC1 is the most likely transducer.** Every arrow here is
independently documented; the *chain* is not. Verify each at figure level before relying
on it (guide R14).

### 3.2 Cell-volume anabolism — the hypothesis as literature

The hepatocyte work (Häussinger, Lang) *is* H1a, stated thirty years ago: swelling →
glycogen synthesis, protein synthesis, lipogenesis up, proteolysis and autophagy down;
shrinkage → the reverse. Transduction via integrin α5β1 → FAK → MAPK, and via
macromolecular crowding.

The sharp claim in that literature, and the one most worth checking: **insulin itself
swells cells** (NHE1, NKCC1, Na/K-ATPase), and part of insulin's anabolic effect was
argued to be *mediated by* the swelling it causes. If that holds, swelling is
insulin-mimetic by construction, and H1a stops being separable from insulin action — which
would make H1a and H1c the same claim rather than rivals. **That possibility has to be
confronted directly, not left implicit.**

**Unresolved tension (from [guide.md §2.5](../guide.md)):** hepatocyte swelling reads
anabolic, but an enlarged lipid-laden adipocyte reads insulin-resistant and lipolytic —
opposite sign. My working resolution is that adipocyte volume is mostly lipid droplet, so
whole-cell volume is a poor proxy for cytosolic water, and the two literatures are not
measuring the same variable *(my inference, not shown)*. **Until this is settled,
"swelling = anabolic" may not be carried over to adipocytes.**

### 3.3 SWELL1 / LRRC8A — a volume sensor on the insulin pathway

The obligatory VRAC subunit, reported to be required for insulin → PI3K → AKT2 signalling
in adipocytes, with adipocyte-specific loss causing insulin resistance, and reported
upregulation in obese adipose tissue.

Why it matters here: it would make cell volume an *input to insulin signalling itself*,
giving swelling → better insulin signalling → more storage → more swelling — a **positive
feedback loop** rather than a one-way effect. Note the apparent paradox to resolve: VRAC's
canonical job is to *export* anions and shrink the cell back, so a swelling-activated
channel that *promotes* storage needs its directionality checked carefully at figure
level.

### 3.4 AQP7 — water and glycerol through the same protein ★ most direct coupling

AQP7 is an **aquaglyceroporin**: the adipocyte channel for both water and the glycerol
released by lipolysis. This is the most literal coupling of water handling to lipid flux
available — not an analogy, the same molecule.

Reported: AQP7 loss → glycerol trapped intracellularly → glycerol kinase →
glycerol-3-phosphate → **re-esterification** → net storage and adipocyte hypertrophy.
Mechanistically this is *exactly* the hypothesis: impaired water/glycerol export makes
lipolysis **futile** (triglyceride–fatty acid cycling) and raises net storage without
changing the lipolytic machinery at all.

**Contested** — the knockout obesity phenotype was not reproduced by all groups. Resolve
the discrepancy before building on it.

### 3.5 Insulin's antinatriuretic action — the H1c engine

Solid and uncontroversial: insulin promotes renal sodium and water retention. It explains
insulin oedema, the rapid water gain of carbohydrate refeeding, and the brisk natriuresis
of carbohydrate restriction.

This is **the mechanism of the null hypothesis.** It produces the observed pairing with no
causal role for water. Its presence means that *every* correlational observation of
"holding water alongside gaining fat" is pre-explained, so correlational evidence cannot
discriminate. Only interventions that move water *without* moving insulin can.

### 3.6 WNK1 and macromolecular crowding — the actual osmosensor

WNK1 senses intracellular chloride and macromolecular crowding directly, signalling
through SPAK/OSR1 to the volume-regulating cotransporters. Crowding is the deeper variable:
cell water content sets cytosolic crowding, which sets enzyme kinetics, protein
association constants, and condensate formation.

Underexplored in lipid metabolism as far as I know — which makes it either a genuine gap
worth opening or a sign that the link does not exist. Worth one scoping pass to find out
which.

### 3.7 AMPK — a tension, not a support

Shrinkage activates AMPK, and AMPK inhibits ACC, so shrinkage → less DNL. Consistent with
H1a so far.

**But** AMPK is reported to be *antilipolytic* in adipocytes (HSL Ser565). So shrinkage
would reduce lipolysis too — breaking the clean "shrinkage = catabolic" picture and
violating the hypothesis's second half. **Do not present AMPK as supporting H1a.** Either
the adipocyte AMPK-lipolysis literature is wrong, or volume control of lipolysis does not
run through AMPK.

---

## 4. Discriminating tests

Designed so that each separates H1a from H1c, or the compartments from each other. This
is the part that matters; the mechanism list above is only worth reading if one of these
can be run.

**T0 — Unilateral lymphoedema, affected versus contralateral limb. ★ now the primary test**
*(added 2026-10-01; supersedes T3 as the project's lead design)*
Paired within-subject comparison in unilateral lymphoedema:
1. **Fat mass** of affected vs unaffected limb by DXA or MRI — adipose tissue specifically,
   segmented from fluid, not limb volume or circumference, which conflate the two and are
   the reason this may look answered when it is not.
2. **Interstitial glycerol and NEFA** by adipose microdialysis in both limbs (§3A.1),
   testing whether clearance failure makes lipolysis futile.
3. **Venous-oedema comparison arm** (§3A.5) to separate fluid volume from lymph.
→ Beats the insulin null outright: same person, same hormones, one limb affected (§3A.4).
→ **Why it leads:** every other test here either uses cultured cells or carries a systemic
confound. This one uses patients who already exist, techniques that already exist, and a
control that cannot be argued with.

**T1 — Swell without hormones.** *(H1a vs H1c, in vitro)*
Swell hepatocytes and adipocytes by a route with no hormonal arm — mild hypotonicity, or
osmolyte loading at constant extracellular tonicity — and measure DNL by ²H₂O or
¹³C-acetate (not enzyme expression) plus lipolysis as glycerol *and* NEFA release.
→ H1a predicts the shift; H1c predicts nothing happens.
**Controls, per [guide.md §1.2](../guide.md):** mannitol (pure tonicity) vs urea
(osmolality without tonicity), matched mOsm. Report **absolute measured final
osmolality**, not the increment (guide R7) — and note that baseline DMEM already sits
above plasma, so "mild hypotonicity" may be plasma-normal.

**T2 — Compartment separation.** *(H1a vs H1b)*
Isotonic ECF expansion (saline load, mineralocorticoid) versus hypotonic water loading
(desmopressin plus water; primary polydipsia as a natural analogue).
→ H1a predicts only the **hypotonic** arm moves lipid flux. If both move it, the mechanism
is not cell volume.

**T3 — Oedema with and without fat gain.** *(cheap; human data already exist)*
Drugs causing fluid retention **with** weight gain — thiazolidinediones, insulin,
gabapentinoids, glucocorticoids — versus fluid retention **without** fat gain —
dihydropyridine calcium-channel blockers (amlodipine oedema is local capillary
hydrostatics), venous insufficiency.
→ If extracellular oedema alone were sufficient, amlodipine should cause fat gain.
It does not, as far as I know — which if confirmed **kills H1b outright** and forces the
hypothesis onto the cellular compartment.
Thiazolidinediones are the sharpest single case: PPARγ agonism causes fluid retention
(ENaC) **and** adipogenesis. Are these parallel outputs of PPARγ, or is the fluid
retention part of the causal path? A dissociation study here tests H1a against H1c in
humans using drugs already in use.

**T4 — Chronic water retention as a natural experiment.** *(the main falsifier)*
Chronic SIADH and primary polydipsia are sustained states of water retention with
dilutional hyponatremia — H1b and arguably H1a, running for years.
→ **Do these patients gain fat mass?** If sustained dilutional water retention does not
raise adiposity, H1b is dead and H1a survives only via a compartment argument explaining
why plasma hypotonicity fails to swell adipocytes. Needs body composition, not weight:
weight change in hyponatremia is mostly water and uninterpretable here.

**T5 — Reversal, with the calories subtracted.**
Water-losing interventions: loop diuretics (water out, fat presumably unchanged — a
dissociation) versus SGLT2 inhibitors (osmotic diuresis **and** genuine fat loss).
→ SGLT2 inhibitors look superficially like strong support, but glycosuria of roughly
60–80 g/day is about 240–320 kcal/day thrown away, which may account for most or all of
the fat loss. **Subtract the energy term before counting this as evidence**, or the
hypothesis gets credit for a calorie deficit (guide R5).

---

## 5. What would kill this

Stated now, before searching, so the standard cannot drift later (guide R11):

1. Chronic SIADH or primary polydipsia with **no** increase in fat mass on body
   composition → H1b dead, H1a wounded.
2. ~~Amlodipine-type oedema with no fat gain → extracellular water insufficient.~~
   **Revised 2026-10-01:** this kills only the *systemic* extracellular form (H1b). It does
   **not** touch H1b′, since generalised oedema and sustained local interstitial expansion
   in adipose tissue are different exposures. I had conflated them.
3. Hypotonic or osmolyte-driven swelling **failing** to move tracer-measured DNL or
   lipolysis in T1 → the causal core of H1a is gone; only H1c survives.
4. Loop diuretic water loss with no fat loss → water removal insufficient.
5. Every reported effect dissolving once insulin is controlled for → H1c wins; water is a
   marker. **Note what §3A.4 does to this:** unilateral lymphoedema is the one setting where
   this condition can actually be *tested* rather than merely feared.
6. **For H1b′ specifically:** affected and contralateral limbs showing **equal adipose
   mass** in long-standing unilateral lymphoedema, once fat is segmented from fluid → H1b′
   dead. This is the cleanest death condition in the file, which is a point in H1b′'s favour
   as a hypothesis regardless of how it resolves.
7. **For H1b′:** fat gain occurring in lymphatic but **not** venous oedema → H1b′ survives
   only in a reformulated version where the agent is lymph or lymphatic transport, and
   "holding water" is a misdescription (§3A.5).

A hypothesis without a stated death condition is not one. These are the conditions.

---

## 6. Honest statement of current evidential standing

~~There is, as far as I currently recall, no direct human evidence that water retention
causes lipogenesis.~~

**Revised 2026-10-01.** That was a consequence of the §1.1 error, not an independent
assessment: having excluded extracellular water, I then found no evidence in the compartment
I had left myself. **Unilateral lymphoedema (§3A.4) is human evidence that sustained local
subcutaneous interstitial fluid accumulation is accompanied by local adipose accumulation**,
with a within-subject control. Its weaknesses are real — direction of causation, whether the
agent is water or lymph (§3A.5), and the measurement problem of separating fat from fluid
(P8) — but it is not absent evidence, and I should not have said it was.

For the **cellular** form (H1a), the original statement stands: the hypothesis is assembled
from individually-supported steps — volume-sensitive mTORC1, hepatocyte volume anabolism,
SWELL1, AQP7, insulin antinatriuresis — none measured as a chain, several contested or in
the wrong cell type.

That is **exactly the failure pattern [guide.md §2.3](../guide.md) warns about**: a
sequence of true steps is a hypothesis, not a mechanism, until flux through the whole
sequence is measured. I am flagging it against myself here so that later sessions cannot
quietly promote this to established.

Everything in §3 is recalled from training and **unverified** (guide R18, §4). Nothing in
this file may be cited until its primary source has been read at figure level.

---

## 7. Predictions, written before searching (guide R11)

Numbered so they can be marked wrong later. **No searches have been run yet.**

- **P1** — The hepatocyte cell-volume/anabolism literature will be substantial and
  consistent; the adipocyte equivalent will be thin, scattered, and contradictory on
  direction.
- **P2** — No human study will exist that manipulates water compartments and measures DNL
  by tracer. The hypothesis's central human test will be **unperformed**, not refuted.
- **P3** — Chronic SIADH patients will **not** show increased adiposity, and the question
  will mostly not have been asked with body composition at all.
- **P4** — Thiazolidinedione fluid retention and adipogenesis will be treated throughout
  as parallel consequences of PPARγ, with their possible causal relation never tested.
- **P5** — mTORC1's volume-sensitivity will turn out to be reported mainly for
  hyper-osmotic *inhibition*, with much weaker evidence for hypo-osmotic *activation* —
  i.e. the arm H1a needs will be the weaker one.
- **P6** — The AQP7 knockout discrepancy will trace to background strain, diet, or age at
  phenotyping rather than to a real biological disagreement.
- **P7** — Searching against the hypothesis will surface the opposite claim — that
  hyperosmotic stress *promotes* lipid accumulation — and the apparent contradiction will
  resolve into a dose and solute artefact once absolute medium osmolality is extracted
  (guide R7).

**P2 and P3 are the ones I most expect to be right, and if they are, the project's job is
to design the missing test rather than to keep reading.**

### Added 2026-10-01, before searching the subcutaneous literature

- **P8** — Local adipose excess in long-standing lymphoedema will be **well established
  clinically** (and assumed by surgeons doing liposuction for it) while being **poorly
  quantified mechanistically**: limb volume and circumference will be everywhere, adipose
  mass segmented from fluid will be scarce, and tracer or microdialysis flux data close to
  absent.
- **P9** — The venous-versus-lymphatic comparison (§3A.5) will **not have been done** as a
  fat-mass study, despite both patient populations being large and easy to find. If so, it
  is the single most answerable open question the project has.
- **P10** — Adipose tissue hypoxia (§3A.2) will be framed throughout the literature as a
  *consequence* of adipocyte hypertrophy, with the interstitial-expansion-as-cause
  direction unexamined.
- **P11** — I expect to be **wrong** somewhere in §3A.4: the lymphoedema–adipose claim is
  the kind of thing that is clinically "well known" and, when the primary sources are
  actually read, rests on small series and surgical impression rather than controlled
  measurement. I am flagging this *in advance* because the finding currently suits the
  hypothesis too well, and §3A.4 is where I will be most tempted not to look hard.

---

## 8. First actions

Reordered 2026-10-01: the subcutaneous route now leads, because it is the only branch with
a confound-free human design available.

1. **§3A.4 / T0 — lymphoedema adipose mass.** Does the affected limb carry more *fat*, as
   distinct from more fluid, measured by segmented imaging rather than volume? Tests P8 and
   P11. Read the primary sources with the P11 warning in hand.
2. **§3A.5 — venous versus lymphatic oedema.** Tests P9. If it is genuinely unasked, stop
   reading and design it.
3. **§3A.1 — adipose microdialysis** in oedematous tissue: interstitial glycerol and NEFA.
   Does clearance failure make lipolysis futile? Technique exists; question may not have
   been put.
4. **T3 on existing data** — amlodipine versus thiazolidinedione fat mass. Now demoted:
   it tests only systemic H1b, which §1.1's correction shows was never the interesting form.
5. **T4 literature scan** — chronic hyponatremia with body-composition outcomes. Tests P3.
6. **§3.1 mTORC1 verification** — whether hypo-osmotic *activation* is evidenced or assumed
   by symmetry from hyper-osmotic inhibition. Tests P5.
7. **§3.4 AQP7** — resolve the knockout discrepancy. Tests P6.
8. Counter-evidence pass (guide R12), run separately and recorded: search *against* the
   hypothesis, including P7's opposite-direction claim and the §3A.5 possibility that the
   agent is lymph rather than water.
