# Evidence ledger

Every protocol parameter in `index.html` — reps, seconds, cycles per day — traces to a study below.
All abstracts were retrieved from PubMed via the NCBI E-utilities API on 2026-09-10 and read in full
before being summarised; nothing here is quoted from memory.

Evidence grades used in the app:

| Badge | Meaning |
|---|---|
| **Strong RCT** | Randomised controlled trial evidence, with the protocol parameters taken from the trial itself |
| **Mixed evidence** | Trials disagree, or the popular version of the advice failed and a modified version succeeded |
| **Limited evidence** | Plausible and low-risk, but not isolated and tested in the population using this app |

---

## 1. Blink training — close · squeeze · open · **Strong RCT**

**Protocol in the app:** 15 repetitions of close (1 s) → squeeze (2 s) → open (2 s). The app states the
trial dose of 3× a day.

- **Wolffsohn JS, Travé-Huarte S, Bahra I, Finch C, Anyaegbu U, Garcia-Porta N, Kingsnorth A.**
  *Optimisation of blinking exercises for dry eye disease.* Cont Lens Anterior Eye 2025;48(5):102453.
  PMID [40467388](https://pubmed.ncbi.nlm.nih.gov/40467388/) · doi:10.1016/j.clae.2025.102453

  Dose-finding study. 98 participants with dry eye randomised across technique (squeeze-and-blink vs
  blink-only), 2–4 repeats/day, and 5–25 repetitions each time; a second efficacy study of 28
  participants followed. Blinking exercises reduced symptomatology overall (p<0.01). Including a
  squeeze step significantly reduced symptom frequency (p<0.01). 40 reps over 2×/day beat 10 reps
  4×/day (SANDE frequency p=0.015); 15 reps beat 5 reps 3×/day (p=0.008). **Optimum routine: 15
  close–squeeze–open cycles, 3×/day.** At that dose over 2 weeks: symptom severity p=0.001, frequency
  p=0.027, incomplete blinks p<0.001, conjunctival staining p=0.041. No significant effect on blink
  rate, NIBUT, tear meniscus height or corneal staining. **Readings mostly returned to baseline two
  weeks after stopping (p>0.05)** — the app surfaces this on the done screen.

- **Arita R, Fukuoka S, Matsumoto R, Kaido M.** *Effects of blinking exercises on palpebral fissure
  height and tear film parameters.* Ocul Surf 2025;36:237-243.
  PMID [39920919](https://pubmed.ncbi.nlm.nih.gov/39920919/) · doi:10.1016/j.jtos.2025.02.003

  RCT, n=100 (mean age 38.4). Blinking exercises after artificial tears, 5×/day for 3 days, vs drops
  alone. Exercise group improved on SPEED (p<0.001), VAS for eye strain (p=0.003) and discomfort
  (p=0.007), palpebral fissure height (p<0.001), NIBUT and FBUT (p<0.001), and incomplete blink rate
  (p<0.001).

- **Sadhwani P, Cs L, Dash S, Mohanty S.** *The impact of optimized blinking on vision and related
  parameters in individuals with computer vision syndrome: a single-blind randomized controlled
  trial.* Cureus 2024;16(8):e67653.
  PMID [39185289](https://pubmed.ncbi.nlm.nih.gov/39185289/) · doi:10.7759/cureus.67653

  6-month follow-up. Tear break-up time improved significantly in the blinking group (p<0.001 both
  eyes) and **deteriorated significantly in controls**. Asthenopia grades improved in cases.

---

## 2. Distance-focus breaks — the corrected 20-20-20 · **Mixed evidence**

**Protocol in the app:** a 30 s active far-fixation phase (extendable by the user), a short blink
reset, then return; the standalone break reminder defaults to every 10 minutes.

- **Johnson S, Rosenfield M.** *20-20-20 Rule: Are These Numbers Justified?* Optom Vis Sci
  2023;100(1):52-56. PMID [36473088](https://pubmed.ncbi.nlm.nih.gov/36473088/) ·
  doi:10.1097/OPX.0000000000001971

  30 subjects, 40-minute cognitively demanding tablet reading task, repeated on four occasions with
  20-second breaks every 5, 10, 20 or 40 minutes (the last = no break). Symptoms rose in all four
  conditions (p<0.001), but **scheduled 20-second breaks had no significant effect** on symptoms
  (p=0.70), reading speed (p=0.93) or accuracy (p=0.55). The authors conclude the results do not
  support 20-second breaks as a therapeutic intervention.

- **Redondo B, Jiménez R, Vera J, Rosenfield M.** *The impact of break schedules on digital eye
  strain symptoms and ocular accommodation during prolonged near work.* Exp Eye Res
  2025;258:110463. PMID [40466853](https://pubmed.ncbi.nlm.nih.gov/40466853/) ·
  doi:10.1016/j.exer.2025.110463

  24 young adults, 40-minute reading task, four conditions in random order: no break, one break at
  20 min, one break every 10 min, and self-paced breaks. Accommodation measured with a binocular
  open-field autorefractor (Grand Seiko WAM-5500). Eye irritation/burning was worse with no break
  than with 3 breaks (p<0.001) or self-paced breaks (p=0.008); eye strain likewise (p=0.04 both).
  Near-work-induced transient myopia was higher in the no-break condition than the 3-break (p=0.02)
  and self-paced (p=0.02) conditions. Accommodative lag did not differ. Conclusion: **individualised
  and frequent breaks help.**

**Why the app departs from the folk rule:** the interval and the duration in "20-20-20" are the two
numbers that failed testing. Breaking roughly every 10 minutes, for longer than 20 seconds, with the
user free to take one early, is what the evidence actually supports.

---

## 3. Convergence push-ups · **Strong RCT** (for diagnosed convergence insufficiency)

**Protocol in the app:** 20 pacer-guided repetitions (~3 min); the card states the trial dose of
15 min/day for 6 weeks. The on-screen dot paces a *physical* target the user holds — this is the
pencil push-up protocol, and the app says so.

- **Convergence Insufficiency Treatment Trial (CITT) Study Group.** *Randomized clinical trial of
  treatments for symptomatic convergence insufficiency in children.* Arch Ophthalmol
  2008;126(10):1336-49. PMID [18852411](https://pubmed.ncbi.nlm.nih.gov/18852411/) ·
  doi:10.1001/archopht.126.10.1336 · NCT00338611

  221 children aged 9–17, four arms, 12 weeks. CISS score: office-based vergence/accommodative
  therapy 15.1 vs 21.3 (home computer + push-ups), 24.7 (home pencil push-ups) and 21.9 (office
  placebo), p<0.001. Success or improvement: **73% OBVAT, 43% HBPP, 33% HBCVAT+, 35% placebo.**
  Home push-ups alone were not better than placebo on symptoms.

- **Singh A, Saxena V, Yadav S, Agrawal A, Ramawat A, Samanta R, Panyala R, Kumar B.** *Comparison of
  home-based pencil push-up therapy and office-based orthoptic therapy in symptomatic patients of
  convergence insufficiency: a randomized controlled trial.* Int Ophthalmol 2021;41(4):1327-1336.
  PMID [33392946](https://pubmed.ncbi.nlm.nih.gov/33392946/) · doi:10.1007/s10792-020-01689-7 ·
  CTRI REF/2016/11/012732

  176 symptomatic patients aged 9–30. **Home pencil push-ups, 15 minutes per day, daily for 6
  weeks**, vs synoptophore-based office therapy 20 min/day, 3 days/week for 6 weeks. Both groups
  improved significantly on near point of convergence, CISS, positive fusional vergence and near
  phoria (p<0.001), **with no statistically significant difference between groups** on the primary
  outcome; office therapy was better on final PFV (p<0.001). The authors credit compliance logging.

- **CITT-ART Investigator Group.** *Treatment of symptomatic convergence insufficiency in children
  enrolled in the CITT–Attention & Reading Trial.* Optom Vis Sci 2019;96(11):825-835.
  PMID [31651593](https://pubmed.ncbi.nlm.nih.gov/31651593/) · doi:10.1097/OPX.0000000000001443

  311 children aged 9–14, 16 weeks. NPC improved 10.4 cm with vergence/accommodative therapy vs
  6.2 cm placebo (difference −4.2 cm, 95% CI −5.2 to −3.2, p<0.001). PFV +23.2Δ vs +8.8Δ (difference
  14.4Δ, 95% CI 12.1–16.8, p<0.001). CISS improved similarly in *both* arms (p=0.21) — the authors
  warn against using self-reported symptoms alone as the success measure.

**Worth knowing (not in the app's exercise cards, but it shapes the framing):** CITT-ART also found
vergence/accommodative therapy **no better than placebo for attention** (Cohen d ≈ 0 on the SWAN
scale), with large improvements in both arms attributable to non-specific effects of intensive
therapy — *Optom Vis Sci* 2021;98(3):222-233, PMID
[33771952](https://pubmed.ncbi.nlm.nih.gov/33771952/). Vision therapy treats vision, not attention.

---

## 4. Near–far focus shifts (accommodative facility) · **Strong RCT** (for accommodative dysfunction)

**Protocol in the app:** 12 cycles of 5 s near / 5 s far ≈ 6 cycles per minute, with a live
cycles-per-minute readout (the clinical metric).

- **Scheiman M, Cotter S, Kulp MT, Mitchell GL, Cooper J, Gallaway M, Hopkins KB, Bartuccio M,
  Chung I; CITT Study Group.** *Treatment of accommodative dysfunction in children: results from a
  randomized clinical trial.* Optom Vis Sci 2011;88(11):1343-52.
  PMID [21873922](https://pubmed.ncbi.nlm.nih.gov/21873922/) · doi:10.1097/OPX.0b013e31822f4d7c

  Of 221 children with symptomatic CI, 164 (74%) also had accommodative dysfunction. After 12 weeks,
  amplitude of accommodation increased **9.9 D (office therapy), 6.7 D (home computer therapy),
  5.8 D (home push-ups) vs 2.2 D (office placebo)**, all p≤0.010. Accommodative facility improved in
  all groups (9, 7, 5 and 5.5 cpm respectively); only the office-therapy gain beat placebo
  significantly (p=0.016). **One year after treatment ended, only 12.5% had a recurrence of decreased
  amplitude and 11% of decreased facility.**

That durability is the sharpest contrast in this app: accommodative gains largely held for a year,
while blink-training benefits washed out in two weeks.

---

## 5. Saccades & smooth pursuit · **Limited evidence**

**Protocol in the app:** horizontal saccades 30 s, vertical 30 s, diagonal 20 s, linear pursuit 40 s,
figure-eight pursuit 40 s (≈2.5 min).

- **Caldani S, Gerard CL, Peyre H, Bucci MP.** *Visual attentional training improves reading
  capabilities in children with dyslexia: an eye tracker study during a reading task.* Brain Sci
  2020;10(8):558. PMID [32824168](https://pubmed.ncbi.nlm.nih.gov/32824168/) ·
  doi:10.3390/brainsci10080558

  50 children with reading disabilities, matched on IQ, sex and age, allocated in an unpredictable
  random sequence to a training group or a matched-interval control. **Ten minutes** of oculomotor
  (saccade and pursuit) plus visual-search training produced significantly faster reading and shorter
  fixation times; the control group, re-tested after an equal 10-minute gap, did not improve.

**The honest limits.** This is a short-term finding in children with a reading disorder, not in
healthy adults doing screen work. Saccade and pursuit drills are a routine component of office-based
vision therapy (they appear inside the CITT protocols above), but they have not been isolated and
shown to relieve digital eye strain. The app grades this **Limited** and describes it as controlled
movement practice rather than a treatment.

---

## What the app says does not work

- **Singh S, McGuinness MB, Anderson AJ, Downie LE.** *Interventions for the management of computer
  vision syndrome: a systematic review and meta-analysis.* Ophthalmology 2022;129(10):1192-1215.
  PMID [35597519](https://pubmed.ncbi.nlm.nih.gov/35597519/) · doi:10.1016/j.ophtha.2022.05.009

  **45 RCTs, 4,497 participants**, GRADE-assessed. No high-certainty evidence supporting *any* of the
  therapies analysed. Multifocal lenses did not improve visual fatigue vs single-vision (3 RCTs, SMD
  0.11, 95% CI −0.14 to 0.37, p=0.38). Blue-blocking spectacles did not reduce visual fatigue
  (3 RCTs, low certainty). Oral berry extract did nothing for visual fatigue (7 RCTs, SMD −0.27,
  p=0.22) or dry eye (4 RCTs, SMD −0.10, p=0.65). Oral omega-3 improved dry eye symptoms (2 RCTs, MD
  −3.36 on an 18-unit scale, p<0.00001) — the one positive, at low certainty.

- **Wang H, Qian Y, Congdon N, Boswell M, Rozelle S, Ma X.** *Effect of Chinese eye exercises on
  change in visual acuity and eyeglasses wear among school-aged children in rural China.* BMC
  Complement Med Ther 2020;20(1):82. PMID [32164649](https://pubmed.ncbi.nlm.nih.gov/32164649/) ·
  ISRCTN03252665

  252 schools; 19,934 children screened; 1,652 propensity-score-matched. Periocular acupoint
  "eye exercises", national policy in Chinese schools for ~50 years, showed **no association with
  change in uncorrected visual acuity or eyeglasses wear** at 9 or 21 months.

- **Tiwari KK, Shaik R, Aparna B, Brundavanam R.** *A comparative study on the effects of vintage
  nonpharmacological techniques in reducing myopia (Bates eye exercise therapy vs. Trataka Yoga
  Kriya).* Int J Yoga 2018;11(1):72-76. PMID
  [29343934](https://pubmed.ncbi.nlm.nih.gov/29343934/)

  24 participants (48 eyes), randomised, 8 weeks. **Neither reduced refractive error nor improved
  visual acuity** (all p>0.42). No eye exercise changes the optical length of the eye.

---

## Deliberately excluded

- **Supplements, lenses and filters.** Not exercises, and covered by the meta-analysis above.
- **Palming, sunning and other Bates-derived relaxation.** No supporting trial evidence.
- **Outdoor time for myopia control in children.** Genuinely evidence-backed, but it is an exposure
  recommendation for a paediatric population, not an exercise a screen worker performs — outside this
  app's scope.
- **Office-based vergence therapy with a clinician.** The strongest intervention in the whole
  literature, and precisely the thing a web app cannot deliver. The convergence card says so.
