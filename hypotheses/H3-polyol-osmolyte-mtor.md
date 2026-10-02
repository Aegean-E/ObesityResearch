# H3 — The osmolyte route: polyol flux loads the cell with water, mTORC1 reads it

**Status:** open · opened 2026-10-02 · **Governed by** [guide.md](../guide.md)

---

## 1. Why this circuit, now

[VA-01](../analysis/VA01-REPORT.md) just closed the plasma route: calculated plasma osmolarity
has **no association** with DXA body fat in 5,107 adults, in either component, across two
cycles. Its own conclusion named what survives:

> "What survives on the input side is intracellular and local-tissue water, **which plasma does
> not index.**"

**The osmolyte route is that surviving path**, and it is the only way the cell-volume premise
lives through VA-01. The chain the subject has named:

```
glucose ──AKR1B1 (aldose reductase, −NADPH)──▶ SORBITOL ──SORD (+NADH)──▶ FRUCTOSE ──KHK-C──▶ F1P
             ▲                                    │                           │
          NFAT5/TonEBP                            │ osmotically active        └──▶ lipogenesis
          (tonicity-driven)                       ▼
                                    cell holds water at NORMAL external tonicity
                                                  │
                                                  ▼
                                          cell volume ↑ ──▶ mTORC1 ──▶ SREBP-1c (DNL ↑)
                                                                   └──▶ ATGL ↓ (lipolysis ↓)
```

**What makes this worth a hypothesis card rather than a diagram:** it is the one route by which
a cell can **hold water without extracellular hypotonicity**. Plasma stays at 290 mOsm/L — as
VA-01 measured — while the cell is loaded. That reconciles VA-01's null with H1's premise
instead of discarding one of them, and it was flagged in
[H1 §2.2](H1-water-retention-lipogenesis.md) as "my construction, not a finding." The subject
has now named it independently, which is a reason to test it, not to believe it.

**It also hits both halves of H1 through one node** — mTORC1 raises SREBP-1c and suppresses ATGL
([guide §2.7](../guide.md)) — and it connects to **H2**, since mTORC1-suppressed ATGL is a
lipolysis brake of exactly the kind H2 describes.

---

## 2. The three places this can break

| # | Step | How it fails |
|---|---|---|
| **B1** | Is intracellular sorbitol ever **osmotically meaningful**? | If sorbitol only reaches osmotically relevant concentrations in hyperglycaemia, and in tissues with high aldose reductase and insulin-independent glucose uptake (lens, nerve, renal medulla, erythrocyte), then this is a **diabetic** mechanism, not a general one — and adipose is the wrong tissue (R21!) |
| **B2** | Is polyol flux **osmotically neutral**? | Sorbitol accumulation is known to **deplete myo-inositol and taurine**. If the cell *substitutes* one osmolyte for another, net osmolyte load — and therefore net water — may not change at all. **This would kill the swelling step outright.** |
| **B3** | Does mTORC1 actually read **swelling**? | [guide §2.7](../guide.md) already warns that mTORC1's documented volume-sensitivity may be hyperosmotic **inhibition**, with hypo-osmotic *activation* assumed by symmetry. If only the inhibition arm is real, cell loading does not activate mTORC1 and the output step fails |

**B2 is the one I most expect to be fatal**, and it is the cheapest to check.

---

## 3. Predictions, before searching (guide R11)

- **P51** — Intracellular sorbitol at **normoglycaemia** will be too low to matter osmotically,
  becoming significant only in hyperglycaemia and in high-aldose-reductase,
  insulin-independent tissues. **If so, B1 fires and H3 is a diabetes mechanism, not an obesity
  one.**
- **P52** — mTORC1's osmotic literature will be **asymmetric**: hyperosmotic inhibition well
  documented, hypo-osmotic/swelling activation weak or assumed. This also closes
  [guide Q-on-mTORC1](../guide.md) which has been open since the guide was written.
- **P53** — **Fructose will activate mTORC1 and drive SREBP-1c lipogenesis directly**, which
  would mean the fructose arm **reaches lipogenesis without needing the swelling step at all**.
  That is bad news for H3 as drawn but good news for the project: a shorter path.
- **P54 — the sharp one.** Sorbitol accumulation will be documented to **deplete myo-inositol
  and taurine**, i.e. **osmolyte substitution**, making polyol flux approximately
  osmotically neutral. **If confirmed, the swelling step is dead and H3 must be redrawn without
  it.**
- **P55** — Adipose-tissue sorbitol or polyol content will **essentially never** have been
  measured against human adiposity. The compartment VA-01 identified as the one that matters
  will turn out to be unmeasured — which would make it the project's clearest open experiment.
- **P56** — The NADPH competition in [guide §2.2](../guide.md) (aldose reductase consumes NADPH;
  FASN needs 14 per palmitate) will be **stated as plausible in reviews and never measured as a
  flux competition**. Open since the guide was written as Q9.

**If P54 and P52 both land, H3 survives only as "polyol flux → fructose → lipogenesis," with
osmolytes and cell volume deleted.** Writing that down now so the deletion is not resisted later.

---

## 4. Findings

### 4.0 Headline — the osmolyte/volume/mTOR arm is dead; the polyol pathway in adipose is alive and *causal*

**Both halves of this were surprises, in opposite directions.**

**Dead:** every one of the three break points fired. Sorbitol is not an accumulating osmolyte —
the cell substitutes it for others; the pathway is dormant at normal glucose; and mTOR's actual
response to swelling is to **expel** osmolytes, not to signal growth. The circuit as drawn in §1
does not hold.

**Alive, and better supported than anything else in the project:**

> **Aldose reductase is increased in the adipose tissue of humans and mice with obesity, and
> genetic deletion or pharmacological blockade of it REDUCES diet-induced obesity, attenuates
> adipose senescence, and INCREASES LIPOLYSIS.**

Mechanism: **cellular senescence**, not osmosis. So the subject's cluster pointed at the right
pathway and the wrong reason. **P55 refuted** — I predicted adipose polyol content would be
unmeasured; instead it has a causal intervention study with an **obesity endpoint**, which is
the box nothing else in [interventions.md](../interventions.md) ticks.

[Thiagarajan et al., *Obesity* 2022](https://onlinelibrary.wiley.com/doi/abs/10.1002/oby.23496) ·
[AKR1B review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3410611/) ·
[aldose reductase, fructose and hepatic fat (Biochem J)](https://portlandpress.com/biochemj/article/482/05/295/235710/Aldose-reductase-fructose-and-fat-production-in)

### 4.1 ✅ P54 confirmed — B2 fires: osmolyte **substitution**, so polyol flux is near osmotically neutral

The "compatible osmolyte hypothesis": sorbitol, taurine and myo-inositol respond **coordinately**,
and rising sorbitol produces **compensatory depletion** of the others.

| Measure | Value |
|---|---|
| Taurine in diabetic nerve as sorbitol accumulated | **−31%** |
| Myo-inositol | **−37%** |
| Nerve taurine after sorbinil (aldose reductase inhibitor) | **+22%** vs untreated diabetic |

> **The cell defends an osmolyte *total*, it does not accumulate one.** Sorbitol in, taurine and
> inositol out. So the step in §1 where sorbitol loading makes the cell "hold water at normal
> external tonicity" is **largely cancelled by design** — the regulation exists precisely to
> prevent it. The swelling premise does not survive this.

*(Caveat kept: −31% and −37% are proportions, not absolute amounts, so exact osmotic cancellation
is not established. But the direction of regulation is the point, and it opposes accumulation.)*
[Taurine depletion and the compatible osmolyte hypothesis](https://pubmed.ncbi.nlm.nih.gov/8359577/) ·
[sorbitol/myo-inositol in human sural nerve](https://www.researchgate.net/publication/12497305_Sorbitol_and_myo-inositol_levels_and_morphology_of_sural_nerve_in_relation_to_peripheral_nerve_function_and_clinical_neuropathy_in_men_with_diabetic_impaired_and_normal_glucose_tolerance)

### 4.2 ✅ P51 confirmed — B1 fires: the pathway is a hyperglycaemia pathway, in other tissues

| Condition | Share of glucose entering the polyol pathway |
|---|---|
| **Normoglycaemia** | **< 3%** |
| **Hyperglycaemia** | **~30%** |

Aldose reductase has a **high Km for glucose**, so the pathway is "relatively dormant at normal
glucose levels." Its osmotically dominant tissues are **lens, peripheral nerve, renal medulla** —
and the renal medulla numbers show what real osmolyte loading looks like: sorbitol **5 mmol/kg**
in outer medulla rising to **~60 mmol/kg** at the papilla tip in water-deprived rats, higher still
in cell water.

**So the mechanism is real — in a tissue purpose-built for it.** R21 again: the osmotic version of
H3 is renal-medullary and lenticular physiology, not adipose physiology. **But see §4.0** — the
*non*-osmotic version is adipose, and that is where the pathway earns its place here.

### 4.3 ✅ P52 confirmed, and B3 fires harder than predicted — mTOR's role is **inverted**

**The inhibition arm is solid:** hyperosmotic stress causes rapid, reversible **inactivation** of
mTORC1 via TSC2 recruitment to lysosomes acting on Rheb.

**The activation arm is contested, and one report is flatly negative:**

> **C-05 — mTORC1 under hypo-osmotic conditions.** One source: *"mTORC1 activity remained
> constant under hypoosmotic conditions"* (while mTORC2 was inhibited by hypertonic shock).
> Another: *"mTOR activity is transiently increased within minutes following osmotic cell
> swelling."* Transient-vs-sustained, mTOR-vs-mTORC1, and cell type are all unresolved. **Logged,
> not adjudicated.**

**And the directional finding that breaks §1's logic:** in the swelling study, mTOR's function is
to **promote taurine efflux** — potentiating release via VSOAC and reducing uptake via TauT.

> **mTOR does not read swelling as "grow." It reads swelling as "dump osmolytes."** It is part of
> the **regulatory volume decrease**, i.e. the machinery that *undoes* swelling. I had assigned it
> the opposite role. The §1 diagram has mTOR pointing the wrong way.

[TSC2 mediates hyperosmotic inactivation of mTORC1](https://www.nature.com/articles/srep13828) ·
[mTOR and taurine under hypo-osmotic conditions](https://journals.physiology.org/doi/full/10.1152/ajpcell.00005.2014)

### 4.4 ◐ P53 — fructose reaches lipogenesis by a different transcription factor entirely

| Sugar | Lipogenic route |
|---|---|
| **Glucose** | HBP → **mTORC1 → SREBP-1c** |
| **Fructose** | **ChREBP**, with "little effect on SREBP-1c maturation" |

*"SREBP-1c mediates glucose-induced lipogenesis and ChREBP orchestrates the lipogenic response to
fructose."* And on mTORC1 directly, the literature conflicts: one report finds high fructose does
**not** activate mTORC1 and drives lipogenesis **mTORC1-independently**; another finds liver ex
vivo mTORC1 **can** be activated by fructose.

> **So the mTOR→SREBP-1c arm I drew is the GLUCOSE route, not the fructose route.** Fructose gets
> to lipogenesis via ChREBP, needing neither swelling nor mTOR. **P53 confirmed in substance:**
> the fructose arm is a shorter path, and §1's middle section is unnecessary.

*(Note for G01: this is the cleanest biochemical statement yet of fructose being handled
differently from glucose — different transcription factor, not merely different entry point.)*

### 4.5 ✗ P56 — the NADPH story is co-dependence, not competition, and my own stoichiometry is in doubt

[guide §2.2](../guide.md) predicted that aldose reductase and FASN **compete** for NADPH. The
literature frames it the other way: NADPH status **gates both**, "ensuring the polyol pathway and
DNL only operate when NADPH is high." Co-regulated, not competing. **My framing was wrong**, and
guide Q9 should be rewritten rather than left open as posed.

**And a discrepancy in my own numbers:** [guide §4](../guide.md) records **14 NADPH per
palmitate**; this source says **12**. Standard stoichiometry is 7 elongation cycles × 2 = **14**.
I cannot resolve it from a search summary, and under **R18c** neither figure may be built on.
**Flagged, not quietly corrected.**

---

## 5. H3 redrawn

```
              ✗ DEAD: osmolyte loading → swelling → mTOR → lipogenesis
                (substitution cancels it; pathway dormant at normal glucose;
                 mTOR expels osmolytes rather than reading them)

   ✓ ALIVE:  glucose ──AKR1B1──▶ sorbitol ──SORD──▶ fructose ──▶ ChREBP ──▶ DNL
                 │
                 └──▶ adipose SENESCENCE ──▶ obesity, reduced lipolysis
                      (AR deletion/blockade: ↓ diet-induced obesity, ↑ lipolysis)
```

| Claim | Status |
|---|---|
| Sorbitol is an accumulating osmolyte that swells cells | ❌ substitution (§4.1) |
| Polyol flux is quantitatively relevant at normal glucose | ❌ <3% (§4.2) |
| mTORC1 is activated by cell swelling | ❌/⚠ contested, and mTOR drives osmolyte **efflux** (§4.3) |
| Fructose → mTORC1 → SREBP-1c | ❌ fructose → **ChREBP** (§4.4) |
| AR and FASN compete for NADPH | ❌ co-gated by NADPH status (§4.5) |
| **Aldose reductase is raised in obese human and mouse adipose** | ✅ |
| **AR deletion/blockade reduces diet-induced obesity and raises lipolysis** | ✅ **causal, obesity endpoint** |

**What the subject's cluster got right:** the polyol pathway belongs in this project, and it
belongs in **adipose tissue**. **What it got wrong — and what I got wrong with it:** the route is
not osmotic. Every osmotic step failed independently, which is unusual and makes the negative
robust rather than merely unsupported.

**What this upgrades:** [interventions.md §D1, epalrestat](../interventions.md) — the approved
aldose reductase inhibitor, marketed in Japan, China and India. It entered the register on
neuropathy evidence with the note that it had no adiposity endpoint. **It now has a mechanistic
rationale in adipose tissue with a causal animal obesity result behind it**, which moves it from
a curiosity to the register's most interesting entry.

**Next:**
1. Read Thiagarajan 2022 at figure level — effect size on fat mass, which AR inhibitor, dose,
   whether the human data is expression-only.
2. Has **epalrestat** ever been looked at for weight or fat mass in its three markets? It has been
   in use for years in large diabetic populations, so the data may exist as a side observation.
3. Senescence is a new mechanism for this project (**M9**) and is not in the guide's map.
