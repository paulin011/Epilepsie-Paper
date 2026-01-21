# Table 1 Extraction Results: 3 New Columns

**For Review:** Compare with existing `DL_COMPARISON_EXTRACTION_RESULTS.md` and resolve conflicts.

---

## New Table 1 Columns Summary

| Study | Paradigm | Modality | Personalization |
|-------|----------|----------|-----------------|
| **Spahr 2025** | ⚠️ CONFLICT | Single (ACC) | Global |
| **Reintjes 2025** | End-to-end | Single (ECG) | Global (LOSO) |
| **Fine 2025** | Feature-based | Single (ACC) | Global |
| **Dong 2026** | Hybrid | Multi (ACC, PPG, HR) | Global |
| **Wang 2025** | Feature-based | Multi (ACC, GYR, PITCH, ROLL, SEMG, EDA) | Global |
| **Singh 2024** | Feature-based | Multi (EDA, ACC, BVP, HR, HRV) | Global (single pt) |
| **Elemam 2025** | ⚠️ CONFLICT | Multi (HRV, Audio) | Global |
| **Borujeny 2013** | Feature-based | Single (ACC) | Global |
| **Vieluf 2025** | Feature-based | Multi (EDA, ACC, Temp) | Mixed |
| **Meisel 2020** | End-to-end | Multi (EDA, ACC, BVP, Temp) | Global (LOSO) |
| **Stirling 2021** | Feature-based | Multi (HR, Steps, Sleep) | Patient-specific |
| **Nasseri 2021** | ⚠️ CONFLICT | Multi (ACC, BVP, EDA, Temp, HR) | Patient-specific |
| **Ode 2023** | End-to-end | Single (ECG/RRI) | Global |

---

## Conflict Details

### Conflict 1: Spahr 2025 - Paradigm

| Source | Paradigm | Evidence | Line |
|--------|----------|----------|------|
| **Existing file** | End-to-end | "Each model...takes the 3D-acc amplitude as input and consists of a 1D CNN" | 106-108, 292-294 |
| **New agent** | Feature-based | "transformed the 3D-acc signals into a single amplitude time series by computing their Euclidean norm. No further processing..." | 259-260 |

**Resolution needed:** Does Euclidean norm pre-processing count as feature extraction?

**Recommendation:** End-to-end - the CNN learns features from the amplitude time series, not from handcrafted features.

---

### Conflict 2: Elemam 2025 - Paradigm

| Source | Paradigm | Evidence | Line |
|--------|----------|----------|------|
| **Existing file** | End-to-end | "The convolutional layers of the CNN are responsible for learning these features" | 560-562 |
| **New agent** | Hybrid | "Based on recent studies, most feature extraction algorithms are manually crafted...Deep Learning (DL) can enhance the accuracy...we leverage deep learning to create a deep model" | 179-181 |

**Resolution needed:** Is CNN + rule-based fusion (Q + HRV + Audio) considered hybrid?

**Recommendation:** Hybrid - the paper uses CNN for feature learning BUT combines with rule-based logic for final detection.

---

### Conflict 3: Nasseri 2021 - Paradigm

| Source | Paradigm | Evidence | Line |
|--------|----------|----------|------|
| **Existing file** | Hybrid | "The physiological time-series signals, their Fourier transforms, the SQI values and time of day were formed 17 channels" | 172-175 |
| **New agent** | End-to-end | "4-layer LSTM...physiological time-series signals, their Fourier transforms, the SQI values...were formed 17 channels" | 120-174 |

**Resolution needed:** Does FFT transformation + time-of-day features count as feature-based preprocessing?

**Recommendation:** Hybrid - including FFT and time-of-day as engineered features makes this hybrid, not pure end-to-end.

---

## Verified (No Conflicts)

### Part 1: Paradigm ✅

| Study | Paradigm | Evidence | Line |
|-------|----------|----------|------|
| Reintjes 2025 | End-to-end | "All three anomaly-detection methods operate directly on the preprocessed ECG time series...We do not extract features such as heart rate, HRV indices" | 320-322 |
| Fine 2025 | Feature-based | "Features were extracted in 10-s intervals...with 594 features, such as mean, variance, and standard deviation" | 62-65 |
| Dong 2026 | Hybrid | "Raw ACM and PPG signals are first transformed into a set of statistical and physiological features, which are then processed by a DL model" | 206-207 |
| Wang 2025 | Feature-based | "Time, frequency, and nonlinear domain features are extracted from each signal" | 357-364 |
| Singh 2024 | Feature-based | "Features including heart rate variability (HR), blood volume pressure (BVP), electrodermal activity (EDA), and accelerometery (ACC)" | 576-580 |
| Borujeny 2013 | Feature-based | "We used three features: Variance, Correlation, Energy (sum of squared FFT component magnitudes)" | 160-162, 432-413 |
| Vieluf 2025 | Feature-based | "We included wearable markers that were significant on a group level combined with demographics, clinical data, and the diary-based days since the last seizure variable" | 345-348 |
| Meisel 2020 | End-to-end | "Deep learning uses multiple layers of connections to perform classification tasks without the need of feature designing" | 168 |
| Stirling 2021 | Feature-based | "Heart rate features included rate of change in heart rate (RCH)...Physical activity features included steps...Sleep features included total time asleep" | 285-289 |
| Ode 2023 | End-to-end | "The input values of SA-AE are the original RRI data" | 215 |

---

### Part 2: Modality Count ✅

| Study | Count | Signals | Line |
|-------|-------|---------|------|
| Spahr 2025 | Single | ACC | 13-14, 106-108 |
| Reintjes 2025 | Single | ECG | 4, 22-25 |
| Fine 2025 | Single | ACC + Gyroscope (motion only) | 17-18, 22-24 |
| Dong 2026 | Multi | ACC, PPG, HR (derived) | 11-13, 226, 241-248 |
| Wang 2025 | Multi | ACC, GYR, PITCH, ROLL, SEMG, EDA | 35-43, 88-90 |
| Singh 2024 | Multi | EDA, ACC, BVP (PPG), HR, HRV | 225-230, 242-250 |
| Elemam 2025 | Multi | HRV (from ECG/PPG), Audio | 17-18, 56-57 |
| Borujeny 2013 | Single | ACC (2D accelerometer) | 22-23, 56 |
| Vieluf 2025 | Multi | EDA, ACC, Temp | 260-264 |
| Meisel 2020 | Multi | EDA, ACC, BVP, Temp | 246-248 |
| Stirling 2021 | Multi | HR (from PPG), Step count, Sleep | 29-30, 251-254 |
| Nasseri 2021 | Multi | ACC, BVP, EDA, Temp, HR | 116-118, 167-168 |
| Ode 2023 | Single | ECG (RRI only) | 21-23, 71-73 |

---

### Part 3: Personalization ✅

| Study | Scope | Validation | Line |
|-------|-------|------------|------|
| Spahr 2025 | Global | Patient-independent (347 test separate from 37 train) | 270-275 |
| Reintjes 2025 | Global | LOSO (sub-001 to sub-096 train, sub-097 to sub-125 test) | 196-200 |
| Fine 2025 | Global | Hold-out (3 test separate from 15 train) | 24-28 |
| Dong 2026 | Global | 10-fold CV with subject-independent split | 603-617 |
| Wang 2025 | Global | Hold-out (IDs 1-18 train, 19-28 test) | 512-527 |
| Singh 2024 | Global (single pt) | Train/test split from same patient | 499-503 |
| Elemam 2025 | Global | Unclear | 1081-1083 |
| Borujeny 2013 | Global | Same-patient (3 pts) | 728-740 |
| Vieluf 2025 | Mixed | 5-fold CV + leave-one-out | 454-456, 474-491 |
| Meisel 2020 | Global | LOSO (68 train, 1 test) | 78-80, 299-302 |
| Stirling 2021 | Patient-specific | Temporal hold-out + pseudo-prospective | 265-281 |
| Nasseri 2021 | Patient-specific | Temporal split (1/3 train, 2/3 test) | 179-182 |
| Ode 2023 | Global | Hold-out (interictal train, preictal test) | 286-288 |

---

## Recommendations for Table 1

### Column Values

| Study | Para. | Mod. | Pers. |
|-------|-------|------|-------|
| Spahr 2025 | E2E | 1 | Glb |
| Reintjes 2025 | E2E | 1 | Glb (LOSO) |
| Fine 2025 | Feat | 1 | Glb |
| Dong 2026 | Hyb | M | Glb |
| Wang 2025 | Feat | M | Glb |
| Singh 2024 | Feat | M | Glb |
| Elemam 2025 | Hyb | M | Glb |
| Borujeny 2013 | Feat | 1 | Glb |
| Vieluf 2025 | Feat | M | Mix |
| Meisel 2020 | E2E | M | Glb (LOSO) |
| Stirling 2021 | Feat | M | Pat |
| Nasseri 2021 | Hyb | M | Pat |
| Ode 2023 | E2E | 1 | Glb |

**Legend:**
- Para.: Feat = Feature-based, E2E = End-to-end, Hyb = Hybrid
- Mod.: 1 = Single-modal, M = Multi-modal
- Pers.: Glb = Global, Pat = Patient-specific, Mix = Mixed

---

## Summary Statistics

- **Paradigm:** 5 Feature-based, 4 End-to-end, 3 Hybrid (after conflict resolution)
- **Modality:** 5 Single-modal, 8 Multi-modal
- **Personalization:** 10 Global, 2 Patient-specific, 1 Mixed
- **LOSO validation:** 2 studies (Reintjes, Meisel)

---

**Please review conflicts and confirm before implementation.**
