# Eye Exercise Coach

A single-file, offline web app with five eye exercises, each one taken from a published clinical
trial along with the trial's own dosing. Where the evidence is weak — or where the popular version of
the advice failed when it was tested — the app says so on the card.

## Run it

Double-click **`index.html`**. That's the whole thing: no build step, no install, no server, no
network. It works with the machine offline and nothing leaves the device.

## The five exercises

| # | Exercise | Dose in the app | Evidence |
|---|---|---|---|
| 1 | **Blink training** — close · squeeze · open | 15 reps, 3×/day | **Strong RCT** — Wolffsohn 2025 dose-finding study (n=98); Arita 2025 RCT (n=100) |
| 2 | **Distance-focus break** | ≥30 s active far fixation, ~every 10 min | **Mixed** — the 20-second version failed testing (Johnson & Rosenfield 2023); frequent and self-paced breaks worked (Redondo 2025) |
| 3 | **Convergence push-ups** | 20 paced reps; trial dose 15 min/day × 6 weeks | **Strong RCT** — CITT 2008 (n=221); Singh 2021 (n=176); CITT-ART 2019 (n=311) |
| 4 | **Near–far focus shifts** | 12 cycles ≈ 6 cycles/min | **Strong RCT** — Scheiman 2011, CITT accommodative cohort (n=221) |
| 5 | **Saccades & smooth pursuit** | one ~2.5 min block | **Limited** — Caldani 2020 (n=50, children with dyslexia); labelled honestly |

Full citations, sample sizes, p-values and PMIDs are in **[RESEARCH.md](RESEARCH.md)** and inside the
app under each card's *Evidence* drawer.

### Evidence grades

- **Strong RCT** — randomised trial evidence, and the reps/seconds in the app come from the trial itself.
- **Mixed evidence** — trials disagree, or the popular form of the advice failed and a modified form succeeded.
- **Limited evidence** — plausible and low-risk, but never isolated and tested in the people using this app.

The home screen also carries a **What does not work** section: blue-light glasses, multifocals and
berry supplements (45 RCTs, 4,497 participants, no high-certainty benefit), acupoint eye exercises
(19,934 children screened, no effect), and Bates/Trataka for myopia (no effect on refractive error).

## What's in it

- Guided animated pacers for all five exercises, with rep counters and a progress bar
- Four routines: Quick reset (~2 min), Dry-eye focus (~3 min), Near-work focus (~6 min), Full session (~10 min)
- A break reminder that counts down and offers a distance break when it fires
- Synthesised beeps and optional spoken phase cues — no audio files, off by default
- Streak, session history and an estimated convergence break point, kept in `localStorage`
- English / ไทย toggle, dark and light themes, both remembered
- Keyboard: **Space** pause/resume · **→** skip exercise · **Enter** context action · **Esc** exit
- Respects `prefers-reduced-motion` and `prefers-color-scheme`

## Safety

**This is not a medical device.** It reproduces exercise protocols from published trials for general
visual comfort. It diagnoses nothing, and **no eye exercise corrects refractive error** — exercises
can make eyes more comfortable, they do not change your prescription.

Exercises 3 and 4 are therapies for diagnosed convergence insufficiency and accommodative
dysfunction. If your binocular vision has not been assessed, treat them as optional and ask an
optometrist first. Note also that in the CITT trial, office-based therapy with a clinician clearly
outperformed home exercise — a web app is the cheap substitute, not the best option.

Stop and see an eye care professional for persistent double vision, eye pain, headache, new flashes
or floaters, or any sudden change in vision.

## Privacy

Everything runs in the browser. No accounts, no analytics, no network requests. The only outbound
links are the PubMed citations, and they open only when you click one. Progress lives in
`localStorage` on that one device; **Clear saved progress** removes it. The app is built to work
normally when storage is blocked or unavailable.

## Files

```
index.html     the entire app — HTML, CSS and JS in one file
RESEARCH.md    citation ledger: every protocol parameter traced to its trial
README.md      this file
```
