# H4 — Intracellular osmolarity: what it actually is, what sets it, and whether it can be measured

**Status:** open · opened 2026-10-02 · **Governed by** [guide.md](../guide.md)

---

## 1. Why this needs its own card

Three results have narrowed the project to this point and nowhere else:

- [VA-01](../analysis/VA01-REPORT.md): **plasma** osmolarity has no association with DXA body
  fat (n=5,107, two cycles). Its own conclusion: what survives is *intracellular and local-tissue
  water, which plasma does not index.*
- [H3](H3-polyol-osmolyte-mtor.md): the **osmolyte-loading** route to intracellular water loading
  fails three ways — substitution, dormancy at normal glucose, and mTOR expelling rather than
  reading.
- [H1](H1-water-retention-lipogenesis.md) §1.5: oedema is extracellular and does not swell cells.

So every route the project has tried has pointed *inward*, and none has reached the inside. This
card asks the prior question the project has been skipping: **what is intracellular osmolarity,
physically, and is it even a variable?**

## 2. The suspicion I want to test first

I think **the project has been using the phrase loosely, and I have been the one doing it.**
Water crosses almost all cell membranes freely, through aquaporins and the bilayer itself. If
that is right, then intracellular osmolality cannot differ from extracellular for more than
seconds — water simply moves until they match.

**If so, "elevated intracellular osmolarity" is not a sustainable state at all**, and the real
variables are different ones:

| Candidate real variable | What it means |
|---|---|
| **Cell volume** | Set by the *quantity* of impermeant intracellular solute at the ambient osmolality. Water is the follower, never the driver |
| **Composition** | K⁺ ~140 mM inside vs Na⁺ ~140 mM outside, at the *same* total osmolality. Inverted composition, identical osmolality |
| **Macromolecular crowding** | The volume fraction occupied by macromolecules — what actually changes enzyme kinetics, binding constants and phase separation |

If the clamp holds, then every sentence in this project of the form "the cell becomes hyperosmolar"
should be rewritten as "the cell holds more impermeant solute and therefore sits at a larger
volume." That is not pedantry: it changes what would have to be measured.

## 3. Predictions, before searching (guide R11)

- **P57 — the one I most expect to land, against my own prior writing.** Intracellular osmolality
  will be documented as **essentially equal to extracellular** at steady state, clamped by water
  permeability. "High intracellular osmolarity" will turn out to be a category error, sustainable
  only as a transient.
- **P58** — Cell volume will be shown to be **actively and continuously defended at ATP cost**
  via the **pump-leak** mechanism: impermeant intracellular polyanions (protein, nucleic acid,
  organic phosphate) would cause Donnan swelling, and the Na/K-ATPase prevents it by keeping Na⁺
  effectively impermeant. **Therefore ATP depletion → Na⁺ influx → swelling.**
- **P59 — the novel link, and my own inference.** If P58 holds, then **fructose via KHK-C, which
  depletes ATP**, should cause cell swelling by pump failure — a route to swelling that needs
  **none** of the machinery H3 just demolished. I expect the ATP depletion to be well documented
  and **the swelling consequence not to be connected to it.** *(My inference, not shown.)*
- **P60** — **WNK1** will be confirmed as a genuine intracellular sensor, reading **chloride** and
  **macromolecular crowding** rather than osmolality as such.
- **P61** — There will be **no practical way to measure adipocyte intracellular water in vivo in
  humans.** Available proxies will be whole-body ICW/ECW by multifrequency bioimpedance or
  isotope dilution (deuterium for total, bromide for extracellular), and **erythrocyte MCV** as
  the only routinely measured single-cell volume in clinical medicine. If so, the project's
  surviving mechanism is the one it cannot measure — which must be stated as the central
  limitation rather than worked around.

**If P57 and P61 both land, the honest conclusion is uncomfortable: the project has narrowed to a
variable that is not a variable in the way it was imagined, and is unmeasurable in the tissue of
interest.** Writing that down now so it cannot be softened later.

---

## 4. Findings

### 4.0 Headline — intracellular osmolarity is not a variable, but the machinery that *keeps* it from being one is, and that machinery has causal obesity results

**P57 confirmed. The project's language has been wrong, mine included.** Intracellular osmolality
cannot differ from extracellular for more than seconds, so "elevated intracellular osmolarity" is
a **category error** as a sustained state.

**But the question was productive anyway**, because what replaces it is better:

> The cell does not sense osmolarity. It senses **water occupancy of an enzyme's catalytic core**
> — via **WNK1** — and responds by moving **ions** to restore **volume**. And the WNK–SPAK axis
> that does this has **two independent causal obesity results** in mice.

So the surviving mechanism is not a solute concentration but a **sensor**, and it is named,
molecular, and already implicated in adiposity. **M10.**

### 4.1 ✅ P57 — the clamp is real, and someone has explicitly tested the escape route

- "All animal cells are permeable to water because **phospholipid bilayers are very water
  permeable**."
- "Water tends to equilibrate its chemical potential gradient between the intra- and extracellular
  compartments. **Because of this, changes in osmolality of the extracellular fluid are
  accompanied by changes in the cell volume.**"
- When the two osmolalities are equal, water does not move — so **cells cannot sustain an osmotic
  gradient**.
- **The obvious escape route has been tested and rejected:** a paper titled *"Macromolecular
  condensation is unlikely to buffer intracellular osmolality"* makes the argument explicitly —
  reversible macromolecular water binding could stabilise intracellular osmolality **only if the
  membrane were water-impermeant**, and it is not.

> **Rewriting rule for this project.** Every sentence of the form "the cell becomes hyperosmolar"
> must become **"the cell holds more impermeant solute and therefore sits at a larger volume."**
> Water is always the follower. This is not pedantry — it changes what would have to be measured
> from a concentration to a **quantity of solute**, and concentrations are what the project kept
> reaching for.

### 4.2 ✅ P58 — volume is defended continuously, at ATP cost, and failure is catastrophic not graded

The **pump-leak** mechanism (Tosteson & Hoffman, 1960):

- Impermeant intracellular molecules — protein, nucleic acid, organic phosphate — create a
  **Gibbs–Donnan** imbalance which, unchecked, draws water in **until the cell lyses**.
- The **Na⁺/K⁺-ATPase** prevents this by energy-dependent Na⁺ extrusion, making Na⁺ effectively
  impermeant and balancing the Donnan term.
- Modelling: turning the pump off produces **progressive collapse of ion gradients, progressive
  depolarisation, and continuous unstable cell swelling — reversed by reactivating the pump.**

> **So the resting cell is not at osmotic equilibrium; it is at a pumped steady state.** Volume is
> a continuously purchased quantity. That makes **ATP supply a volume variable**, which is the
> opening for §4.3.

### 4.3 ⚠ P59 — my inference: the ATP depletion is spectacular, the volume link is unmade, and the dose is unreal

**Fructose via KHK-C depletes ATP dramatically:**

| Measure | Value |
|---|---|
| ATP depletion, primary murine hepatocytes, **50 mM fructose** | **70–80% within 5 minutes** |
| ATP remaining | **15–20% of control for at least 20 hours** |

With Pi falling and AMP rising as F1P accumulates. In aldolase B deficiency the same sequestration
causes fatty liver, hyperuricaemia and hypoglycaemia.

**If pump-leak needs ATP (§4.2) and ATP sits at 15–20% for 20 hours, the pump should be badly
compromised and the cell should swell.** The searches state plainly that the link from ATP
depletion to sodium-pump failure and hepatocyte volume **was not detailed** — so this is
**unconnected in the literature**, as predicted.

**But I must apply the project's own dose rule to my own favourite idea (guide R6).** **50 mM
fructose is roughly two orders of magnitude above physiological portal fructose.** On the guide's
exposure scale this is **E3/E4** — hypothesis-generating only. So:

> **P59 stands as an unresolved, exposure-unrealistic inference.** The interesting version is
> narrower: *does ATP fall enough at physiological fructose to matter for pump-leak?* That is
> unknown, and it is the question worth asking rather than the one I posed. Hereditary fructose
> intolerance is the one setting where the supraphysiological intracellular state occurs naturally
> — which links this to [G01](../observations/G01-fructose-specific-craving.md) and is the
> natural place to look.

### 4.4 ★★ P60 — WNK1, and the mechanism is better than anything else in this project

**The sensing mechanism, which is a genuine molecular answer to "how is intracellular water
sensed":**

1. WNK kinases sit in equilibrium between a **chloride-bound inactive dimer** and a
   **chloride-unbound, activation-competent monomer**.
2. **Hyperosmolality extracts water from the cell *and from WNK1's own catalytic core*.**
3. That facilitates **chloride unbinding** → **autophosphorylation at S382** → activation.
4. Activated WNK1 **phase-separates** via its C-terminal domain into **condensates**, recruiting
   effectors.
5. **SPAK** and **OSR1** are activated in the condensates, exported to cytosol, and phosphorylate
   **NKCC1** and the **KCCs** → ion influx → **regulatory volume increase**.

> **The cell's water sensor is water sitting in an enzyme active site.** Not a concentration, not a
> membrane stretch, not an osmolyte level — the hydration state of a catalytic pocket, read out as
> a chloride-binding equilibrium. That is the mechanistic answer the question asked for, and
> **molecular crowding, not osmolarity, is the quantity being sensed.**

**And WNK1 is also the central osmosensor for vasopressin release**, via a
**WNK1–OSR1/SPAK–Kv3.1** cascade. So the guide's §2.3 AVP axis and the cell-volume machinery are
**the same molecule in two places** — which is the kind of convergence the project has been
looking for, arrived at from the inside rather than assembled by me.

[WNK kinases sense molecular crowding (Cell 2022)](https://www.sciencedirect.com/science/article/pii/S0092867422012612) ·
[crowding sensor and phase separation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10024530/) ·
[WNK1 as central osmolality sensor for AVP (JCI)](https://www.jci.org/articles/view/164222) ·
[chloride-sensitive WNK-SPAK/OSR1 review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7606576/)

### 4.5 ★★ M10 — the WNK–SPAK axis has causal obesity results, in the right tissue

| Finding | Source |
|---|---|
| **SPAK inactivation** → resistant to high-fat-diet obesity and hepatic steatosis; ↑ energy expenditure; ↑ BAT thermogenesis; ↑ muscle mitochondrial activity; **↓ white adipose hypertrophy**; ↑ whole-body insulin sensitivity. Authors propose SPAK as **a drug target for obesity** | [Am J Physiol 2017](https://journals.physiology.org/doi/full/10.1152/ajpendo.00108.2017) |
| **WNK4 deletion → reduced diet-induced obesity**; WNK4 is an **adipogenic factor** | [WNK4 adipogenic](https://www.researchgate.net/publication/314715399_WNK4_is_an_Adipogenic_Factor_and_Its_Deletion_Reduces_Diet-Induced_Obesity_in_Mice) |
| Loss of **Akt3** → ↑ WNK1 → ↑ SGK1 → ↓ FOXO1 (a negative regulator of adipogenesis) → **adipogenesis**; Akt3 protects from diet-induced obesity **via WNK1/SGK1** | [JCI Insight](https://insight.jci.org/articles/view/95687) |
| **WNK1 is the most upregulated phosphoprotein in the obesity-associated adipocyte secretome**; hyperinsulinaemic mice show increased WNK1 phosphorylation | review |

> **This is the cell-volume mechanism the project wanted, with the causal evidence H1 never had.**
> Two independent genetic manipulations of the volume-sensing kinase cascade reduce diet-induced
> obesity, in adipose and with an **obesity endpoint** — the same box [H3 §4.0](H3-polyol-osmolyte-mtor.md)
> found epalrestat's target ticking, and almost nothing else in this project does.

**Caution, stated plainly:** WNK/SPAK is also the renal salt-handling pathway (NCC, NKCC2) behind
pseudohypoaldosteronism II and a blood-pressure target. Any metabolic effect of inhibiting it
arrives with **systemic electrolyte and blood-pressure consequences**, which is exactly the
shared-pathway problem that killed PEPCK as a target in [H2 §7.2](H2-depletion-gates-lipolysis.md).
**Same structural barrier, different enzyme.**

### 4.6 ✗ P61 refuted — intracellular water IS measurable, and the measurement points away from swelling

| Method | Validity |
|---|---|
| **Deuterium** dilution → TBW; **bromide** dilution → ECW; **ICW = TBW − ECW** | reference method |
| **Multifrequency bioimpedance spectroscopy** (low frequency = ECW, high = TBW) | explains **96% / 77% / 94%** of reference variance for TBW / ECW / ICW; overestimates by **2.3% / 1.6% / 2.7%** |

**And the directional result:** *"There was a significant positive relation between the **ECW/ICW
ratio** and the **percent body fat**."*

> **Higher adiposity goes with relatively MORE extracellular and LESS intracellular water.** That
> is the opposite sign to the cell-swelling premise, and the **same** sign as
> [H1b′](H1-water-retention-lipogenesis.md)'s interstitial route. A third independent line now
> points extracellular rather than intracellular.

**Confound that must be stated and is serious:** adipose tissue has low water content and a high
extracellular fraction, so **adding fat mass raises whole-body ECW/ICW mechanically, with no
cell-level change at all.** The comparison only means something **normalised to fat-free mass**.
As reported, the association may be pure tissue composition. **Recorded as suggestive and
confounded, not as evidence.**

---

## 5. Where this leaves the project

**The question "intracellular osmolarity and its mechanisms" has a clean answer:**

| Asked about | Reality |
|---|---|
| Intracellular osmolarity | **Not a variable** — clamped to extracellular by water permeability (§4.1) |
| What is variable | **Cell volume**, set by the *quantity* of impermeant solute, defended continuously at ATP cost (§4.2) |
| What senses it | **WNK1**, reading water in its own catalytic core via chloride binding, then phase-separating to drive SPAK/OSR1 → NKCC1/KCC (§4.4) |
| What the cell actually "feels" | **Macromolecular crowding**, not osmolarity (§4.4) |
| Adaptive solute route | Organic osmolytes via NFAT5 — but regulated as a *total*, so it does not accumulate ([H3 §4.1](H3-polyol-osmolyte-mtor.md)) |
| Measurable in humans? | **Whole-body ICW yes**; adipocyte ICW in vivo, no (§4.6) |

**Two things are now true at once, and they pull in opposite directions:**

1. **The volume-sensing machinery is the best-supported mechanism this project has found** — named
   sensor, solved mechanism, two causal obesity results, and a convergence with the AVP axis
   through one molecule (§4.4, §4.5).
2. **Every measurement that bears on direction says adiposity goes with *less* relative
   intracellular water, not more** (§4.6), joining VA-01's plasma null and H1's oedema finding.

> **So the machinery matters, but probably not by swelling adipocytes.** The honest reading is that
> WNK–SPAK affects adiposity through **adipogenesis (WNK4/SGK1/FOXO1), thermogenesis and energy
> expenditure** — all of which the mouse data actually show — rather than through cell volume per
> se. Volume sensing is the *input* the kinase evolved to read; adiposity may be a downstream
> consequence that has nothing to do with the adipocyte's own water.

**Next:**
1. Read the SPAK-inactivation paper at figure level: effect size on fat mass, whether the
   phenotype is energy expenditure or storage, and whether electrolyte/BP effects were measured.
2. Is WNK1/SPAK expression in human adipose associated with adiposity, beyond the secretome claim?
3. Does any WNK/SPAK inhibitor exist with tolerable systemic effects? (The §4.5 caution predicts
   not, by the H2 §7.2 shared-pathway argument.)
4. **ICW/ECW normalised to fat-free mass** against adiposity — the confound in §4.6 is removable,
   and multifrequency BIA datasets exist.
