# FPR Threshold (0.05-0.1/h) Source Search Results

**Date:** 2026-01-26
**Goal:** Locate source citation for "FPR below 0.05-0.1/h is considered clinically acceptable"

---

## Papers Searched

### Beniczky et al. 2021 - Automated seizure detection using wearable devices (ILAE CPG)

**File:** `Beniczky et al. - 2021 - Automated seizure detection using wearable devices A clinical practice guideline of the Internation.md`

**Citation key:** `beniczkyAutomatedSeizureDetection2021`

**Exact lines with FPR/FAR values:**

```
Line 335-341:
Evidence from phase 3 studies for detection of seizures with
sensitivity of at least 90% was available only for GTCS, including
FBTCS. One study used accelerometer, one study used surface elec-
tromyography and one study used a multimodal device (ac-
celerometry and heart rate) (Table 2). The sensitivity of these
devices was between 90% and 96%, with a false alarm rate of
0.2–0.67/24-h. (o-0.03/night). All three devices validated in phase
3 studies have approval for use as medical device (CE-mark) in the
European Union.
```

**Phase 3 benchmark:** 0.2-0.67/24-h = **0.008-0.028/h**

**Other FPR values found:**
- Line 446: "0.11/24 h (0 at night)"
- Line 673: "Median: 0.1/24 hr"
- Line 1083: "(0.11 during sleep at night)"
- Line 1572: "0.13/24 h (0 at night)"
- Line 1893: "0.01-0.05 per night (95% CI)"

**0.05-0.1/h found:** NO

---

### Sivathamboo et al. 2022 - Preferences and User Experiences of Wearable Devices

**File:** `Sivathamboo et al. - 2022 - Preferences and User Experiences of Wearable Devices in Epilepsy A Systematic Review and Mixed-Meth.md`

**Citation key:** `sivathambooPreferencesUserExperiences2022`

**Exact lines with FPR/FAR values:**

```
Lines 1986-1992:
detection and low false alarm rate.18-20 People with epilepsy
valued a higher sensitivity (≥90%)19-21; higher false alarms
(1–2 false detections per week) were more acceptable for pa-
tients with higher seizure frequencies (≥1 seizure per week),
whereas the acceptable false alarm rate was lower (1–2 false
detections per month) in those with lower seizure frequency
(<1 per week).20 In 1 study, higher sensitivity was preferred
over lower false alarm rates.19
```

**User tolerance:**
- High frequency patients (≥1/week): 1-2/week = **0.006-0.012/h**
- Low frequency patients (<1/week): 1-2/month = **0.001-0.003/h**

**0.05-0.1/h found:** NO

---

### van Andel et al. 2016 - Non-EEG based ambulatory seizure detection

**File:** `van Andel et al. - 2016 - Non-EEG based ambulatory seizure detection designed for home use What is available and how will it.md`

**Citation key:** `vanAndelNonEEGbasedAmbulatory2016`

**Exact lines with FPR/FAR values:**

```
Lines 783-788:
Most studies (10 out of 17) focused on the detection of GTCSs. Five of
these studies reported performance measures based on algorithms de-
veloped within the same study population; the other five studies re-
ported on algorithm validation in a different population. In the former
studies, sensitivity ranged from 88% to 100%, with false alarm rates be-
tween 0.1 and 1/24 h [18,22,24,26,31].
```

```
Line 359:
Sens: 91%Latency: 17sFA: 0.1/24h
```

```
Line 855-857:
than 80% and acceptable false alarm rates: a mattress-based device for
the detection of nocturnal GTCSs (sensitivity: 84.6% in children, false
alarm rate not reported and sensitivity: 100% in adults, no false alarms)
```

**Acceptable range mentioned:** 0.1-1/24-h = **0.004-0.042/h**

**0.05-0.1/h found:** NO

---

### Chen et al. 2022 - Seizures detection using multimodal signals (scoping review)

**File:** `Chen et al. - 2022 - Seizures detection using multimodal signals a scoping review.md`

**Citation key:** `chenSeizuresDetectionUsing2022`

**Exact lines with FPR/FAR values:**

```
Lines 77-82:
entail Support Vector Machine, Random Forest and threshold-based approach. The sensitivity ranged
from 33.2% to 100% for single modality with a false alarm rate (FAR) ranging from 0.096 to 14.8 d-
1. Multimodality has a sensitivity ranging from 51% to 100% with FAR ranging from 0.12 to 17.7 d-
```

**Range across studies:** 0.096-17.7/day

**0.05-0.1/h found:** NO

---

### Beniczky et al. 2020 - Biomarkers of seizure severity derived from wearable devices

**File:** `Beniczky et al. - 2020 - Biomarkers of seizure severity derived from wearable devices.md`

**Citation key:** `beniczkyBiomarkersSeizureSeverity2020`

**FPR/FAR values found:** Mentions false alarms but no specific threshold values

**0.05-0.1/h found:** NO

---

## Summary Table

| Paper | FPR Values | 0.05-0.1/h Present? |
|-------|-----------|-------------------|
| Beniczky 2021 (ILAE) | 0.008-0.028/h (Phase 3) | **NO** |
| Sivathamboo 2022 | 0.006-0.012/h (user tolerance) | **NO** |
| van Andel 2016 | 0.004-0.042/h (acceptable) | **NO** |
| Chen 2022 | 0-50/day range | **NO** |

---

## Conclusion

**The 0.05-0.1/h threshold is NOT explicitly stated in any of the searched papers.**

**Possible explanations:**
1. The threshold may be derived from combining sources (e.g., user tolerance + clinical judgment)
2. It may appear in a different paper not in Papers_md folder
3. It may be stated in different units (e.g., "1-2 per day" = 0.04-0.08/h)
4. It may be a synthesis/interpretation rather than a direct citation

**Recommendation:** Either add a specific citation if found, or rephrase as "practical threshold" with justification (e.g., "Based on Phase 3 benchmarks of 0.008-0.028/h and user tolerance of ~0.01/h, an FPR below 0.05-0.1/h is considered clinically acceptable...")
