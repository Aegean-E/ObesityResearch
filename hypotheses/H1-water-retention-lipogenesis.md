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
| **H1b — extracellular** | interstitial / plasma volume ↑ (edema) | **no** | normal |
| **H1c — program** | either; water is a *marker* | irrelevant | either |

**This is the decisive fork.** Isotonic sodium-plus-water retention expands the
extracellular space **without changing cell volume at all** — water follows sodium and
stays outside the cell. So if the mechanism runs through cell volume, then ordinary edema
is *not* the exposure, and a patient with swollen ankles is not an instance of the
hypothesis.

This is the exact mirror of the tonicity rule in [guide.md §1.2](../guide.md): there, a
rise in osmolality carried by urea does not shrink cells. Here, water retained with sodium
does not swell them. Both failures come from the same error — treating a whole-body number
as if it were a cell-level force.

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
2. Amlodipine-type oedema with no fat gain → extracellular water insufficient.
3. Hypotonic or osmolyte-driven swelling **failing** to move tracer-measured DNL or
   lipolysis in T1 → the causal core is gone; only H1c survives.
4. Loop diuretic water loss with no fat loss → water removal insufficient.
5. Every reported effect dissolving once insulin is controlled for → H1c wins; water is a
   marker.

A hypothesis without a stated death condition is not one. These are the conditions.

---

## 6. Honest statement of current evidential standing

**There is, as far as I currently recall, no direct human evidence that water retention
causes lipogenesis.** The hypothesis is presently assembled from individually-supported
steps — volume-sensitive mTORC1, hepatocyte volume anabolism, SWELL1, AQP7, insulin
antinatriuresis — none of which was measured as a chain, and several of which are
contested or in the wrong cell type.

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

---

## 8. First actions

1. **T3 on existing data** — cheapest decisive step. Amlodipine versus thiazolidinedione
   weight/fat-mass data already exist in trial literature. Could kill H1b this week.
2. **T4 literature scan** — chronic hyponatremia with body-composition outcomes.
   Tests P3; likely to find the gap rather than the answer.
3. **§3.1 mTORC1 verification** — read the volume-sensitivity primary sources at figure
   level, specifically whether hypo-osmotic *activation* is real or assumed by symmetry
   from hyper-osmotic inhibition. Tests P5.
4. **§3.4 AQP7** — resolve the knockout discrepancy. Tests P6.
5. Counter-evidence pass (guide R12), run separately and recorded: search *against* the
   hypothesis, including the opposite-direction claim in P7.
