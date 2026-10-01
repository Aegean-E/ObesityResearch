# interventions.md — agents with human evidence against the surviving mechanisms

**What this is.** A register of agents evaluated by **evidence quality against a named
mechanism**, built under [guide.md](guide.md) rules: primary sources, absolute numbers,
non-empty counter-evidence, causal codes. **What it is not:** a protocol, a selection for
anyone, or a dose recommendation. The project produces mechanism; clinical decisions sit
outside it ([guide.md §0](guide.md)).

Evidence read 2026-10-03. Mechanism targets M1–M7 defined in
[session 3](sessions/2026-10-03-intervention-register.md).

---

## ⚠ The finding that governs every row below

> **Not one agent here has been tested against adiposity.** Every trial in this register
> used **limb volume, skin thickness, bioimpedance, symptom scores, or a biomarker** as its
> outcome. None measured fat mass, adipocyte number, or lipid flux.

So this register answers **"can the mechanism be moved in humans?"** It does **not** answer
"does moving it change fat." Prediction P23, written before searching, and confirmed. Any row
read as a weight-loss agent is being read wrong.

A second structural finding, also predicted (P21): **availability and mechanistic relevance
run inversely.** The agent that best fits the live mechanism is a prescription NSAID tested in
34 people; the agents that are freely available target a different mechanism or rest on weak
evidence.

---

## A — Mechanism M2 (cytokine/adipokine retention → local inflammation)

### A1. Ketoprofen — ✅ the best human evidence in the register

| | |
|---|---|
| **Mechanism fit** | Direct: M2. Anti-inflammatory, with an LTB4-pathway rationale |
| **Design** | Open-label n=21 (2010–11) **plus** placebo-controlled RCT n=34 (**16 ketoprofen / 18 placebo**), 2011–2015 |
| **Result** | Reduced **skin thickness**; improved composite histopathology; decreased plasma **G-CSF**. Open-label arm: histopathology and skin thickness improved at 4 months vs baseline |
| **Safety** | No serious adverse events in trial |
| **D/E** | **D1/E1** — randomised, placebo-controlled, objective histopathology |
| **Causal** | contributory |
| **Counter-evidence** | **n=16 per arm** — a pilot, author-described as such. Skin thickness ≠ adipose mass. Single centre, single group (Rockson). Not replicated independently. Systemic NSAID exposure carries the standard GI, renal and cardiovascular profile, which a trial of 34 cannot characterise |
| Source | [JCI Insight 2018;3(20)](https://insight.jci.org/articles/view/123775) |

**Why it leads:** it is the only agent here with a placebo-controlled human trial showing
change in **tissue structure**, not just symptoms or volume — and M2 is the live mechanism
after session 2. **Why it is not a conclusion:** 34 people, one group, and the outcome is skin.

### A2. Ubenimex (bestatin) — ❌ FAILED, recorded at equal weight (R5)

Oral LTA4H inhibitor, blocking LTB4 formation — mechanistically the *more* targeted version of
A1's rationale, and strongly supported in mice.

**Phase 2 ULTRA, n=46, 150 mg three times daily × 24 weeks: no improvement over placebo on the
primary endpoint (skin thickness) or on secondary endpoints (limb volume, bioimpedance).** The
sponsor discontinued development.

> **This is the most informative single result in the register.** The cleanest mechanistic
> hypothesis in the field — LTB4 drives lymphatic dysfunction, so block LTA4H — was tested
> properly in humans and **failed**. It should discipline how much weight A1 carries, since the
> two share a pathway rationale and only the less specific agent worked. P19 confirmed: the
> failure is markedly less publicised than the positive result.

[Protocol](https://cdn.clinicaltrials.gov/large-docs/29/NCT02700529/Prot_SAP_000.pdf) ·
[Preclinical rationale](https://www.prnewswire.com/news-releases/eiger-announces-results-demonstrating-benefit-of-ubenimex-and-leukotriene-b4-ltb4-modulation-in-experimental-lymphedema-300459051.html)

### A3. Pentoxifylline — ◐ real cytokine effect, wrong disease

| | |
|---|---|
| **Mechanism fit** | M2 partial — non-selective PDE inhibitor, decreases TNF-α transcription |
| **Evidence** | RCT in haemodialysis: **significantly decreased serum TNF-α, IL-6 and CRP vs placebo**. Venous leg ulcers: healing **80% vs 50% (p<0.05)**, ulcer size reduction **65% vs 45% (p<0.01)** |
| **D/E** | D1/E1 for the cytokine endpoint; D2/E1 for ulcers |
| **Counter-evidence** | **No lymphoedema or adiposity endpoint.** The cytokine effect is systemic, whereas M2 predicts a *local, size-filtered* retention problem — lowering circulating TNF-α may not address interstitial retention. Trialled with vitamin E for post-radiation arm lymphoedema (NCT00022204); result not retrieved this session — **open item** |
| Source | [Nephrol Dial Transplant 2012](https://academic.oup.com/ndt/article/27/5/2023/1841439) · [meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC11869512/) |

---

## B — Mechanism M1 (lymphatic transport capacity)

### B1. Sodium selenite — ◐ positive but small, and I could not verify the disconfirming trial

| | |
|---|---|
| **Evidence** | Volume reduction with decongestive therapy **−52.0 ± 18.0% vs −43.0 ± 16.0%** (p<0.01). **Erysipelas incidence 0% vs 50%** in supplemented vs placebo |
| **Design** | Zimmermann et al., prospective randomised placebo-controlled double-blind, **n=20**; several further small trials |
| **D/E** | D2/E1 |
| **Counter-evidence** | **n=20.** Effect on volume is an *increment* on decongestive therapy, not standalone. Selenium has a narrow therapeutic window and a U-shaped risk curve, with supplementation trials in other fields showing harm at the top end. **Honest gap: a search result referenced a 90-woman Royal Marsden lymphoedema trial, and I could not verify its intervention or result in either direction. Recorded as unresolved rather than omitted** |
| Source | [Int J Radiat Oncol 2003](https://www.redjournal.org/article/S0360-3016(02)04390-0/abstract) · [J Trace Elem Med Biol 2016](https://www.sciencedirect.com/science/article/pii/S0946672X1630075X) · [randomised placebo-controlled secondary analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC8470409/) |

The erysipelas result is the more interesting one: infection is a known driver of lymphatic
destruction, so this could be **mechanism-preserving** rather than mechanism-reversing. Worth
separating those two claims — the register currently conflates them.

### B2. Flavonoids — MPFF / diosmin, rutosides — ◐ large base, weak and off-target

| | |
|---|---|
| **Evidence** | Meta-analysis of **15 RCTs** in chronic venous insufficiency: significant reductions in leg pain, heaviness and oedema vs placebo at 2–6 months |
| **D/E** | D2/E1 |
| **Counter-evidence** | Evidence is in **CVI, not lymphoedema**. Cochrane rates phlebotonics **moderate** quality and flags **heterogeneity in study design**. Outcome is symptoms and oedema, not tissue or fat. A bradycardia case report exists for MPFF |
| Source | [Cochrane CD003229](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD003229.pub4/references) · [comparative review](https://www.tandfonline.com/doi/full/10.2147/VHRM.S324112) |

### B3. Coumarin / benzopyrones — ❌ negative trial plus a safety signal

**[NEJM 1999: "Lack of Effect of Coumarin in Women with Lymphedema after Treatment for Breast
Cancer."](https://www.nejm.org/doi/full/10.1056/NEJM199902043400503)** Negative.

Hepatotoxicity reported at **0.3–6%** incidence, mostly transaminase elevation, attributed to
CYP450-dependent alternative metabolism in susceptible individuals; clinical use restricted in
several countries. P20 confirmed: large historical literature, weak design, safety signal, and
a definitive negative trial at the top of the evidence pyramid.
[Hepatotoxicity review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9783661/)

### B4. VEGF-C / lymphangiogenic therapy — preclinical only

No human trial located. P18 confirmed — the field's best human result is anti-inflammatory,
not pro-lymphangiogenic. Note also session 2's **C-03**: more lymphangiogenesis is not
self-evidently desirable, since high salt already increases lymph flow 26% and that arrow
points away from adipose accumulation.

---

## C — Mechanism M7 (AVP / osmolality axis)

### C1. Water intake — ✅ the only zero-cost, zero-risk entry, and the evidence is real

| Protocol | Effect on copeptin |
|---|---|
| Acute 1 L | **−39%** on average, significant by 30 min, maximal by 90 min |
| 1 week increased intake | **−15%** vs control week |
| 6 weeks, +1.5 L/day, low-intake high-copeptin adults | **12.9 → 7.8 pmol/L** |
| CKD pilot RCT | **15.0 → 10.8 pmol/L** (median −3.6) |

The H2O Metabolism pilot also found **reduced plasma glucose**; a separate hydration study
found reduced glucagon in water-responders, with glucose and insulin generally unaffected
short-term.

**D/E:** D1–D2/E1 · **Causal:** sufficient (for lowering copeptin) · **Counter-evidence:**
copeptin is a **biomarker, not an outcome** — no adiposity endpoint; effects are largest in
those starting with low intake and high copeptin, so this is plausibly **correction of a
deficit rather than a treatment**; the metabolic readouts are pilot-scale and partly null.

Sources: [J Clin Endocrinol Metab 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6541888/) ·
[CKD pilot RCT](https://pmc.ncbi.nlm.nih.gov/articles/PMC4663439/) ·
[healthy adults](https://pmc.ncbi.nlm.nih.gov/articles/PMC6060834/) ·
[Eur J Nutr 2017](https://link.springer.com/article/10.1007/s00394-017-1595-8)

**This is the clearest honest answer to "easily achievable":** the mechanism moves, reliably,
measurably, at no cost and no risk — and nobody has shown that moving it changes fat.

---

## D — Mechanism M5 (polyol pathway / aldose reductase)

### D1. Epalrestat — ✅ approved and in use, but not where most readers are

| | |
|---|---|
| **Mechanism fit** | Direct: the only clinically approved aldose reductase inhibitor |
| **Evidence** | 3-year multicentre comparative trial (ARI-DCT), **150 mg/day**: suppressed deterioration of nerve conduction velocity in tibial and sural nerves vs control at 2 years |
| **Availability** | **Marketed in Japan, China and India.** Not approved in the US; no ARI has been, cited reasons being trial design, absent controls, limited efficacy or adverse events |
| **D/E** | D2/E1 |
| **Counter-evidence** | Endpoint is **neuropathy**, not adiposity or lipid flux. Comparative rather than placebo-controlled. The entire ARI class has a history of regulatory failure elsewhere, which is itself evidence about effect size |
| Source | [ARI-DCT, Diabetes Care 2006](https://pubmed.ncbi.nlm.nih.gov/16801576) · [long-term analysis](https://onlinelibrary.wiley.com/doi/10.1111/j.1464-5491.2012.03684.x) |

**Benfotiamine** is listed within this class; no randomised polyol-pathway trial retrieved this
session. **Open item.**

---

## E — Agents that move fat but not these mechanisms

### E1. SGLT2 inhibitors — fat does move, but the mechanism is not ours, and the data are mixed

Included because session 1 flagged them as a water-losing, fat-losing intervention worth
checking, and the check matters:

- Some trials: **two-thirds of weight loss attributable to fat mass** by DXA in obese
  non-diabetic subjects.
- **But** at least one DXA study found **lean mass significantly reduced (−0.67 kg vs placebo)
  with whole-body fat mass not significantly affected** — the opposite pattern.
- Mechanism is **glycosuria**, i.e. an energy deficit, plus osmotic diuresis — it does not
  bear on M1–M7. [Guide R5](guide.md) requires subtracting the energy term before crediting
  anything else, and once subtracted there is little left to attribute.

**Do not read SGLT2i as support for the water hypothesis.** It is a calorie-loss agent that
also causes diuresis.
[Meta-analysis](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0279889) ·
[network meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC13461395/)

### E2. Weight reduction itself — the arrow runs backwards

A randomised controlled trial tested **weight reduction as a treatment for breast
cancer-related lymphoedema**. Worth noting because it inverts this project's question: the
field treats adiposity as a *cause* of lymphatic dysfunction, consistent with claim B8
(obesity impairs lymphatic function, near-universal above BMI ~60).
[Cancer 2007](https://acsjournals.onlinelibrary.wiley.com/doi/10.1002/cncr.22994)

---

## F — Scorecard and the honest summary

| Prediction | Outcome |
|---|---|
| P18 — best-evidenced agent is anti-inflammatory, not lymphangiogenic | ✅ confirmed (ketoprofen; VEGF-C preclinical only) |
| P19 — a promising agent failed phase 2, less publicised | ✅ confirmed (ubenimex / ULTRA) |
| P20 — benzopyrones: large weak base, CVI not lymphoedema, safety signal | ✅ confirmed, plus a definitive negative NEJM trial |
| P21 — availability and mechanistic relevance inversely related | ✅ confirmed |
| P22 — water has genuine randomised evidence on copeptin | ✅ confirmed, with numbers |
| **P23 — nothing tested against adiposity** | ✅ **confirmed, without exception** |

**The summary the user asked for, stated plainly:**

1. **Agents that reliably move these mechanisms in humans exist.** Ketoprofen (M2, RCT),
   water (M7, RCT, free), epalrestat (M5, approved in three countries), selenite and
   flavonoids (M1, weak).
2. **None of them has been shown to change fat mass**, because none has been tested for it.
   The register is a list of **mechanism probes**, not treatments for what this project is
   about.
3. **The most mechanistically targeted agent in the field failed its trial** (ubenimex), which
   is the strongest single reason for caution about the rest.
4. The gap between "this moves the mechanism" and "this reduces adiposity" is **the entire
   remaining question**, and it is unbridged by every row above.

**Next actionable step for the project, not for a person:** the missing study is small and
obvious — any of these agents, with **fat mass segmented from fluid by imaging** as the
outcome instead of limb volume. That is the trial nobody has run, and session 1's measurement
critique explains why the existing literature cannot substitute for it.
