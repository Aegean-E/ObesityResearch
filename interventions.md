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

> ### ★ UPGRADED 2026-10-02 — epalrestat now has an adipose rationale with a causal obesity result
>
> From [H3 §4.0](hypotheses/H3-polyol-osmolyte-mtor.md): **aldose reductase is increased in the
> adipose tissue of humans and mice with obesity**, and **genetic deletion or pharmacological
> blockade reduces diet-induced obesity, attenuates adipose senescence, and increases lipolysis.**
> Mechanism is **cellular senescence**, not the osmotic route — every osmotic step failed
> independently.
>
> **This makes D1 the most interesting entry in the register**, and the only one where the target
> has a causal animal result with an **obesity endpoint** rather than a surrogate. It remains a
> neuropathy drug with no human adiposity data, and the §K pattern (hard endpoints fail where
> biomarkers move) applies to it as much as to anything else. But the gap it has to cross is now
> one step, not three.
>
> **Open:** whether weight or fat mass has ever been reported for epalrestat in its three markets,
> where it has been used for years in large diabetic populations. A side observation may exist.
> [Thiagarajan et al., Obesity 2022](https://onlinelibrary.wiley.com/doi/abs/10.1002/oby.23496)

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

## G — Mechanism M3 (interstitial fibrosis) — added 2026-10-02

Session 2 found **fibrosis precedes adipocyte hypertrophy** (present at lipoedema stage I with
normal adipocyte size), which makes M3 the earliest targetable step rather than a late
complication. The register had no M3 entry. It does now, and the news is bad.

### G1. Pentoxifylline + vitamin E — ❌ NEGATIVE in lymphoedema (closes my open item)

The standard antifibrotic combination for radiation injury, and the unclosed item from §A3.

**Double-blind placebo-controlled RCT, n=68**, chronic arm lymphoedema with fibrosis after
breast-cancer surgery and radiotherapy, entry requiring **≥20% arm volume increase**:
**at 12 months no significant difference in arm volume, and no benefit in radiation-induced
induration (fibrosis) either.** Both endpoints null.

Wider context: a phase II trial reported fibrotic lesion surface area falling **80 → 27 cm²
(p<0.001)** in 21 lesions — but **meta-analysis found no benefit of pentoxifylline + vitamin E
versus placebo or no intervention** for radiation-induced fibrosis in breast cancer. The
uncontrolled result is impressive and the controlled result is null.

→ **§A3 is downgraded accordingly.** Pentoxifylline's cytokine effect is real; its effect on
this disease is not demonstrated.
[RCT, Radiother Oncol 2004](https://pubmed.ncbi.nlm.nih.gov/15542159/) ·
[meta-analysis](https://www.advancesradonc.org/article/S2452-1094(22)00019-7/fulltext)

### G2. Metformin — ★ the best mechanistic fit in the register, and its own data contradict its title

Mechanistically this is the most attractive agent encountered: in mouse lymphoedema it
**alleviates inflammation and fibrosis and increases lymphangiogenesis via AMPK** — hitting
**M1, M2 and M3 simultaneously** — and it is the most widely available prescription drug in the
world, cheap, and extensively characterised in humans. AMPK activation in **human** adipose
tissue in vivo is confirmed by a randomised glycaemia-controlled crossover study.

**But read the data, not the title** (guide R19). The paper is titled *"Metformin Eliminates
Lymphedema in Mice."* Its own results report that **metformin had no significant effect on
hindlimb circumference or tail volume** — the volume endpoints were **null**. What improved
were inflammation and fibrosis markers.

> **This is the cleanest example in the project of why guide K-type rules exist: the title is a
> claim, the figures are the data, and here they disagree.** An agent whose mechanism moves and
> whose volume endpoint does not is exactly the pattern §H identifies as the field's signature.

No human trial of metformin in lymphoedema or lipoedema with a volume endpoint was located.
It **is** recommended in American lipoedema guidance — but for the **insulin-resistance**
indication, not on lipoedema-specific trial evidence. That is a guideline recommendation
standing on absent disease-specific data, and should be recorded as such rather than cited as
support.
[Plast Reconstr Surg 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11584190/) ·
[human adipose AMPK](https://link.springer.com/article/10.1007/s00125-011-2126-4)

### G3. Spironolactone / MR antagonism — ◐ antifibrotic signal, no disease data

HOMAGE (n=527, 25–50 mg/day, up to 9 months) found lower follow-up serum **PICP** and
NT-proBNP, suggesting altered type-I collagen metabolism. In adipose, spironolactone reduced
basal **IL-6** secretion by cultured stromal-vascular cells, and MR controls adipocyte
function; MR antagonism browns white adipose in high-fat-fed mice.

**No human lymphoedema or lipoedema data.** P28 confirmed.
[HOMAGE/PRIORITY proteomics](https://www.medrxiv.org/content/10.1101/2023.04.05.23288107.full.pdf) ·
[adipose IL-6](https://pubmed.ncbi.nlm.nih.gov/18075971/)

### G4. GLP-1 receptor agonists / tirzepatide — ◐ case series and narrative review only

Exenatide in lipoedema exists as an **Italian case series**; tirzepatide appears as a
**narrative review** arguing antifibrotic and immunometabolic relevance. **No controlled
trial.** Note that these agents reduce fat by appetite suppression, so attributing any fat
change to an antifibrotic mechanism would need the energy term subtracted first (guide R5) —
the same error §E1 flags for SGLT2 inhibitors.

**Standing fact for the register:** *there is currently no drug treatment approved for
lipoedema.*
[Case series](https://www.mdpi.com/2039-7283/15/7/128) ·
[tirzepatide review](https://www.mdpi.com/1422-0067/26/21/10741)

---

## H — Mechanism M1 revisited: doxycycline, and why single trials mislead

### H1. Doxycycline — ◐ a large single-trial effect that did not survive meta-analysis

This looked, on first pass, like the best "easily achievable" candidate in the register: oral,
cheap, globally available, and with a striking randomised result.

**Mand et al. 2012** — n=162, three arms of 54 (doxycycline 200 mg/day × 6 weeks vs amoxicillin
vs placebo): **improvement in 43.9% of doxycycline patients vs 3.2% amoxicillin and 5.6%
placebo**, with reductions in lymphoedema severity at 12 **and** 24 months, **independent of
circulating filarial antigen status** — i.e. not explained by killing the parasite. It also
**reduces plasma VEGF-C / sVEGFR-3**, which is a direct mechanistic link to the M1 axis and to
session 2's **C-03**.

**Then it was replicated properly.** A 2026 systematic review and meta-analysis of **12 RCTs**
(including multi-site trials in Sri Lanka, Mali, Tanzania and southern India): *Wolbachia*
burden per microfilaria fell significantly, but doxycycline shows **"a limited role in
clinically significant lymphedema reduction,"** with microfilarial evidence not robust and
**vomiting significantly more common** in the doxycycline arm.

> **43.9% vs 5.6% in one trial became "limited role" across twelve.** This is the single best
> cautionary datum in the register, and it applies directly to §A1 (ketoprofen, n=16 per arm,
> unreplicated). Record the effect size *and* the replication status, or the register misleads.

[Mand 2012, Clin Infect Dis](https://academic.oup.com/cid/article/55/5/621/350498) ·
[2026 meta-analysis](https://pubmed.ncbi.nlm.nih.gov/42492504/) ·
[VEGF-C mechanism](https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.0020092)

---

## I — Mechanism M6 (fructose → KHK → uric acid)

### I1. PF-06835919 — ✅ the mechanism moves, measurably, and it is not body fat

| | |
|---|---|
| **Design** | Phase 2, randomised, double-blind, placebo-controlled, 3 arms. 158 screened, **53 randomised, 48 completed** (placebo 17, 75 mg 17, **300 mg 14**) |
| **Primary result** | Whole liver fat by MRI-PDFF, 300 mg vs placebo: **difference −18.73%, p=0.04**. From baseline to week 6: **−26.5% vs −7.78%** placebo. **75 mg not significant** — a dose-response |
| **Secondary** | Reduced insulin resistance, ALT, AST, GGT, inflammatory markers |
| **Safety** | Well tolerated; adverse-event frequency similar to control |
| **D/E** | **D1/E1** |
| **Counter-evidence** | **n=14 in the effective arm.** 6 weeks. **Liver fat is not adiposity** — no body-fat or weight endpoint reported. Investigational only: not available. A second phase 2a in NAFLD + T2D exists |
| Source | [Med 2021](https://www.cell.com/med/fulltext/S2666-6340(21)00156-2) · [Diabetes Obes Metab 2023](https://dom-pubs.onlinelibrary.wiley.com/doi/10.1111/dom.14946) |

**P27 confirmed exactly as written:** liver fat moves, body fat unmeasured. This is the
best-executed trial in the register and it still cannot answer the project's question.

---

## J — Mechanism M4 (tissue mechanics / YAP-TAZ)

**Empty.** No agent with human evidence located. YAP/TAZ-directed pharmacology does not exist
clinically, and the mechanics route is addressed — if at all — by **compression**, which is
physical rather than pharmacological and is the best-evidenced lymphoedema intervention
overall. Recorded as a genuine blank rather than padded.

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

---

## K — The pattern across the whole register ★ added 2026-10-02

Assembling every hard-endpoint result in one place produces something none of the individual
rows shows, and it is the most important output of this register:

| Agent | Mechanism target | Biomarker / surrogate | **Hard endpoint (volume, fat, tissue)** |
|---|---|---|---|
| Ubenimex | M2 (LTA4H→LTB4) | — | ❌ **failed**: skin thickness, limb volume, bioimpedance all null |
| Coumarin | M1 | — | ❌ **negative** (NEJM) |
| Pentoxifylline + vit E | M3 | ✅ TNF-α, IL-6, CRP ↓ | ❌ **null** at 12 months: arm volume *and* fibrosis (n=68) |
| Doxycycline | M1 (VEGF-C ↓) | ✅ *Wolbachia* burden ↓ | ◐ large in **one** trial → **"limited role"** across **12** |
| Metformin | M1+M2+M3 | ✅ inflammation, fibrosis, lymphangiogenesis ↑ | ❌ **null**: hindlimb circumference, tail volume (mouse) |
| Ketoprofen | M2 | ✅ G-CSF ↓ | ◐ skin thickness ↓ — **n=16/arm, unreplicated** |
| PF-06835919 | M6 | ✅ liver fat −18.73%, p=0.04 | ⬜ **body fat never measured** |
| Water | M7 | ✅ copeptin −39% | ⬜ **never measured** |
| Epalrestat | M5 | ✅ nerve conduction | ⬜ **never measured** |

**The pattern: biomarkers move reliably; hard endpoints do not.** Every agent with a
mechanistically motivated rationale that received a properly controlled trial with a hard
endpoint either failed outright or shrank to "limited" on replication. The one apparent
exception is the smallest and least replicated study in the register.

Two readings, and they are not equally comfortable:

1. **The mechanisms are wrong**, or too downstream, or too small to matter at the tissue level.
2. **The endpoints are wrong.** And the project has independent reason to suspect this:
   **limb volume conflates fat with fluid** (guide §1.5, session 1 §2.4 — the measurement
   critique that resolved C-02). An agent that removed adipose tissue while fluid rose, or
   vice versa, would read as null on every trial in this table. **Bioimpedance has the same
   defect.** Skin thickness measures neither.

> So the field may have been testing plausible mechanisms with instruments that cannot see the
> thing in question. That is not a defence of the mechanisms — it is a reason the negative
> record is **less informative than it looks**, and a reason the single missing study (fat
> segmented from fluid by imaging) would be worth more than any new agent.

**What this means for the register's practical answer.** The honest ranking by *evidence that
something happens in a human*:

- **Water intake** — reliable, free, risk-free, biomarker-level, mechanism M7.
- **Ketoprofen** — the only positive controlled tissue-level result; small, unreplicated, and
  its own pathway's more specific agent failed.
- **Epalrestat** — approved and in use for a different indication in three countries; M5.
- **Metformin** — best mechanistic breadth, human AMPK activation confirmed, **zero human
  disease-endpoint evidence and null volume endpoints in its own mouse model.**
- Everything else — negative, unreplicated, unavailable, or confounded by energy balance.

**Nothing in that list has been shown to reduce adiposity.** The register's value is that it
now says exactly where each candidate fails, and names the one measurement that would change
the picture.
