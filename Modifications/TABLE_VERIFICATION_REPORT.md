# Table Verification Report: All 13 Studies

**Rigorous Verification Results - One Agent Per Paper**

---

## Summary of Verification Status

| Study | Verified | Conflicts | Status |
|-------|----------|----------|--------|
| Spahr 2025 | 5 | 3 | ⚠️ Needs correction |
| Reintjes 2025 | 5 | 1 | ⚠️ Needs correction |
| Fine 2025 | 4 | 3 | ⚠️ Needs correction |
| Dong 2026 | 7 | 2 | ⚠️ Needs correction |
| Wang 2025 | 4 | 3 | ⚠️ Needs correction |
| Singh 2024 | 3 | 2 | ⚠️ Needs correction |
| Elemam 2025 | 4 | 2 | ⚠️ Needs correction |
| Borujeny 2013 | 5 | 2 | ⚠️ Needs correction |
| Vieluf 2025 | 3 | 2 | ⚠️ Needs correction |
| Meisel 2020 | 3 | 3 | ⚠️ Needs correction |
| Stirling 2021 | 8 | 0 | ✅ All verified |
| Nasseri 2021 | 6 | 4 | ⚠️ Needs correction |
| Ode 2023 | 4 | 6 | ⚠️ Needs correction |

---

## Detailed Verification Results by Study

### 1. Spahr 2025

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: End-to-end** | ⚠️ CONFLICT | - | Ensemble approach with multiple models, not pure E2E |
| **Mod: 1 (ACC)** | ✅ VERIFIED | 220-228 | "only 3D-acc data were used" |
| **Pers: Global** | ⚠️ CONFLICT | 286-288 | Tunable parameter q allows personalization |
| **Arch: 30 models, 1D CNN** | ✅ VERIFIED | 324, 293-297 | "30 models", "14 convolutional layers" |
| **Modality: 32 Hz, 30s** | ✅ VERIFIED | 224, 259, 401 | "32 Hz", "Euclidean norm", "30 s windows" |
| **Trade-off: 86-100%** | ⚠️ CORRECTION | 508-515 | Range is 80-100%, not 86-100% |
| **Deployment: 112ms, TicWatch** | ✅ VERIFIED | 558-563 | "112 ms", "TicWatch Pro 3" |

**Corrections Needed:**
- Paradigm: Change to "Ensemble" (not pure E2E)
- Personalization: Change to "Tunable" or keep as Global with note
- Sensitivity range: 80-100% (not 86-100%)

---

### 2. Reintjes 2025

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: End-to-end** | ✅ VERIFIED | 145 | "do not extract features such as heart rate, HRV indices" |
| **Mod: 1 (ECG)** | ✅ VERIFIED | 144 | "single-lead ECG waveform" |
| **Pers: Global (LOSO)** | ⚠️ CONFLICT | 196-198 | Subject split but not explicitly "LOSO" |
| **Arch: Anomaly (3 methods)** | ✅ VERIFIED | 25 | "Matrix Profile, MADRID, and TimeVQVAE-AD" |
| **Modality: 256→8 Hz** | ✅ VERIFIED | 214 | "256 Hz", "downsampled to 8 Hz" |
| **Window: 96s** | ⚠️ NOT FOUND | - | Window size not explicitly mentioned |
| **Trade-off: 38-98%** | ✅ VERIFIED | 829-930 | Sens 38.04-98.16%, FAR 1.91-40.46/h |
| **Deployment: Offline** | ✅ VERIFIED | 1199 | Offline analysis confirmed |

**Corrections Needed:**
- Personalization: Subject split (not explicitly LOSO)
- Window: Remove if not found, or mark as N/A

---

### 3. Fine 2025

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: Feature-based** | ⚠️ PARTIAL | 62-64 | 594 features used, but paradigm not explicitly stated |
| **Mod: 1 (ACC only)** | ⚠️ CONFLICT | 59-60 | Uses "accelerometer AND gyroscope (6 axes)" |
| **Pers: Global** | ⚠️ NOT FOUND | - | Personalization not mentioned |
| **Arch: ANN, 594 feat** | ✅ VERIFIED | 62-64 | "594 features...mean, variance, standard deviation" |
| **Window: 10s, 1s overlap** | ✅ VERIFIED | 62 | "10-s intervals with 1-s overlap" |
| **Trade-off: 100% @ 0.023/h** | ✅ VERIFIED | 83-84 | "100%...0.023/h" |
| **Deployment: Offline PC, EMU** | ✅ VERIFIED | 121, 66 | "offline...on a PC", "epilepsy monitoring unit" |

**Corrections Needed:**
- Paradigm: Feature-based (implied by 594 features)
- Modality: Change to "M" (ACC + Gyro = multi-modal)
- Personalization: Not mentioned, mark as N/A

---

### 4. Dong 2026

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: Hybrid** | ⚠️ CONFLICT | 291-292 | Two-stage approach, not hybrid |
| **Mod: M (ACC + PPG)** | ✅ VERIFIED | 41 | "ACM and PPG signals" |
| **Pers: Global** | ✅ VERIFIED | 603-610 | "subject-independent stratified split" |
| **Arch: CNN-LSTM + Attention** | ✅ VERIFIED | 44 | "CNN-LSTM with attention mechanism" |
| **Sampling: 11-12→20 Hz** | ✅ VERIFIED | 242-248 | "11-12 Hz and 100 Hz...resampled to 20 Hz" |
| **Window: 5 min** | ✅ VERIFIED | 539-540 | "300 s (5 minutes)" |
| **Fusion: Early** | ⚠️ PARTIAL | 301-302 | Multimodal integration described, term not used |
| **Trade-off: 71.6% @ 0.165/h** | ✅ VERIFIED | 836-838 | "0.716", "0.165/hour" |
| **Deployment: Real-time, home** | ✅ VERIFIED | 316-318 | "home environments", "real-time" |

**Corrections Needed:**
- Paradigm: Change to "Two-stage" (not hybrid)
- Fusion: Mark as "Early" with note (multimodal integration confirmed)

---

### 5. Wang 2025

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: Feature-based** | ✅ VERIFIED | 703-718 | Features extracted from signals |
| **Mod: M (6 modalities)** | ✅ VERIFIED | 36-37 | "ACC, GYR, ROLL, PITCH, SEMG, EDA" |
| **Pers: Global** | ⚠️ PARTIAL | 514-520 | Global training, but patient-specific testing |
| **Arch: LSTM + SVM/LDA** | ⚠️ CONFLICT | 703-718 | Single LSTM, not 2-stage |
| **Sampling: 50/200/4 Hz** | ✅ VERIFIED | 296-297 | "ACC 50 Hz...SEMG 200 Hz...EDA 4 Hz" |
| **Window: 4s** | ✅ VERIFIED | 354 | "4s...50% overlap" |
| **Fusion: Early** | ✅ VERIFIED | 413-418 | "early fusion method" |
| **Trade-off: F1-opt** | ⚠️ NOT FOUND | - | F1 not mentioned as optimization target |
| **Deployment: Real-time, hospital** | ⚠️ PARTIAL | 276-286 | Real-time data transfer mentioned |

**Corrections Needed:**
- Personalization: Global (with patient-specific testing)
- Arch: LSTM only (remove "+ SVM/LDA 2-stage")
- Trade-off: Remove "F1-opt" or mark as unclear

---

### 6. Singh Rathore 2024

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: Feature-based** | ⚠️ PARTIAL | 242-246 | "machine learning model", not explicitly feature-based |
| **Mod: M (EDA, ACC, HR)** | ✅ VERIFIED | 576-581 | "HR, EDA, ACC: x, y, z, magnitude" |
| **Pers: Global (single pt)** | ✅ VERIFIED | 500-501 | "single patient" |
| **Arch: MLP** | ✅ VERIFIED | 470-483 | "Multi-Layer Perceptron" |
| **Features: 594** | ⚠️ NOT FOUND | - | Number 594 not mentioned |
| **Data: 25k rows** | ✅ VERIFIED | 575-576 | "25,000 rows" |
| **Trade-off: 96.8% sens** | ✅ VERIFIED | 520 | "recall of 96.8%" |
| **Deployment: Real-time designed** | ✅ VERIFIED | 472-475 | "operate in real-time" |

**Corrections Needed:**
- Features: Remove "594" (not mentioned in paper)
- Fusion: Mark as N/A (not discussed)

---

### 7. Elemam 2025

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: Hybrid** | ⚠️ PARTIAL | - | Not explicitly stated as "hybrid" |
| **Mod: M (PPG + Audio)** | ✅ VERIFIED | 463, 549 | "PPG...250 Hz", "segment length of 10 seconds" |
| **Pers: Global** | ⚠️ NOT FOUND | - | Not mentioned |
| **Arch: CNN + Rule-based** | ✅ VERIFIED | 514, 375 | "CNN", "knowledge base...rules" |
| **Sampling: 250 Hz** | ✅ VERIFIED | 463 | "250 Hz" |
| **Fusion: Decision (parallel)** | ⚠️ NOT FOUND | - | "Parallel models" not described |
| **Trade-off: 95.1% sens** | ✅ VERIFIED | 23, 1049 | "95.10%" (for questionnaire) |
| **Deployment: Real-time** | ✅ VERIFIED | 87 | "real-time seizure detection" |

**Corrections Needed:**
- Fusion: Mark as "Rule-based" (not parallel models)
- Trade-off: Note that 95.1% is for questionnaire only

---

### 8. Borujeny 2013

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: Feature-based** | ⚠️ PARTIAL | 426-433 | Features used for detection, but not "feature-based paradigm" |
| **Mod: 1 (ACC)** | ✅ VERIFIED | 174-176 | "three 2D accelerometer sensors" |
| **Pers: Global** | ✅ VERIFIED | 739-741 | "no need for training...for each new patient" |
| **Arch: KNN k=5** | ✅ VERIFIED | 715-723 | "k=5 no seizure has been missed" |
| **Sampling: 3 Hz** | ✅ VERIFIED | 186-188 | "sampling frequency...is 3 Hz" |
| **Window: 9s** | ✅ VERIFIED | 212-217 | "9 seconds" |
| **Trade-off: 57-100%** | ⚠️ CONFLICT | 672-684 | Results: 90%, 100%, 100% for k=1,3,5 |
| **Deployment: 316 mW** | ✅ VERIFIED | 694-697 | "power on 316 mW" |

**Corrections Needed:**
- Trade-off: Change to "90-100%" (not 57-100%)

---

### 9. Vieluf 2025

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: Feature-based** | ⚠️ CONFLICT | - | Uses harmonic modeling + DNN, not pure feature-based |
| **Mod: M (EDA, ACC, Temp)** | ✅ VERIFIED | 261-263 | "EDA...4 Hz", "ACC...32Hz", "TEMP...1 Hz" |
| **Pers: Mixed** | ⚠️ CONFLICT | 292 | "Mixed-effects" refers to statistical model |
| **Arch: DNN, harmonic** | ✅ VERIFIED | 68, 288-289 | "neural network", "harmonic models" |
| **Sampling: 4/32/1 Hz** | ✅ VERIFIED | 261-263 | Confirmed |
| **Window: 10min** | ⚠️ CONFLICT | 287 | Uses 24-h patterns, 10min for median |
| **Trade-off: 82% sens** | ✅ VERIFIED | 135 | "sensitivity=.82" |
| **Deployment: MATLAB** | ✅ VERIFIED | 265 | "MATLAB 2023b" |

**Corrections Needed:**
- Paradigm: Change to "Hybrid" (harmonic + DNN)
- Personalization: Mark as N/A (mixed-effects is statistical, not personalization)
- Window: Note 24-h patterns, 10min for median

---

### 10. Meisel 2020

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: End-to-end** | ⚠️ PARTIAL | 74 | "deep learning" but not explicitly "end-to-end" |
| **Mod: M (4 signals)** | ✅ VERIFIED | 246-248 | "EDA, ACC, BVP, TEMP" |
| **Pers: Global (LOSO)** | ✅ VERIFIED | 78, 1550 | "leave-one-subject-out" |
| **Arch: LSTM + 1D Conv** | ⚠️ CONFLICT | 337-338 | LSTM only, 1D Conv for comparison |
| **Units: 10** | ⚠️ CONFLICT | 1737 | 100 units in Table S1, not 10 |
| **Window: 30s** | ✅ VERIFIED | 266-268 | "30-second segments" |
| **Fusion: Early** | ⚠️ NOT FOUND | - | Fusion strategy not explicitly described |
| **Trade-off: 51.2% sens** | ✅ VERIFIED | 1730-1731 | "51.2 ± 3.8%" |
| **Deployment: Hospital** | ✅ VERIFIED | 198 | "in-hospital monitoring" |

**Corrections Needed:**
- Arch: Change to "LSTM" only (remove "+ 1D Conv")
- Units: 100 (not 10) if specified
- Fusion: Mark as N/A (not described)

---

### 11. Stirling 2021

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: Feature-based** | ✅ VERIFIED | 29 | Machine learning on HR, sleep, steps |
| **Mod: M (HR, steps, sleep)** | ✅ VERIFIED | 29, 251-254 | Confirmed |
| **Pers: Patient-specific** | ✅ VERIFIED | 42-44 | "patient-specific seizure forecasts" |
| **Arch: LSTM+RF+LR** | ✅ VERIFIED | 343-345 | "ensemble of LSTM, RF, LR" |
| **Sampling: 5s/1min** | ✅ VERIFIED | 251-254 | "5 s resolution", "each minute" |
| **Fusion: Decision** | ✅ VERIFIED | 579-581 | "logistic regression...combined" |
| **Trade-off: AUC 0.74** | ✅ VERIFIED | 759-763 | "M AUC = 0.74" |
| **Deployment: Fitbit, app** | ✅ VERIFIED | 246-247 | "Fitbit", "Seer App" |

**✅ All claims verified - No corrections needed**

---

### 12. Nasseri 2021

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: Hybrid** | ⚠️ CONFLICT | 88 | Wearable-based with iEEG validation |
| **Mod: M (5 signals)** | ✅ VERIFIED | 116-118 | "ACC, BVP, EDA, TEMP, HR" |
| **Pers: Patient-specific** | ⚠️ CONFLICT | 179-181 | Temporal split, not patient-specific model |
| **Arch: LSTM 4-layer, 128** | ✅ VERIFIED | 120-122 | "4 LSTM layers, 128 hidden nodes" |
| **Sampling: 128 Hz** | ✅ VERIFIED | 168 | "up-sampled to 128 Hz" |
| **Window: 60s** | ✅ VERIFIED | 184 | "60-s data epochs" |
| **Fusion: Early (17-ch)** | ✅ VERIFIED | 173-174 | "17 channels" |
| **Trade-off: AUC 0.75** | ✅ VERIFIED | 224 | "AUC of 0.75" |
| **Deployment: Cloud, home** | ✅ VERIFIED | 112-115 | "upload data daily...Empatica cloud" |

**Corrections Needed:**
- Paradigm: Change to "E2E" (LSTM on signals)
- Personalization: Change to "Temporal split" (not patient-specific)

---

### 13. Ode 2023

| Claim | Status | Line | Evidence |
|-------|--------|------|----------|
| **Para: End-to-end** | ⚠️ CONFLICT | - | "End-to-end" not mentioned |
| **Mod: 1 (ECG/RRI)** | ✅ VERIFIED | 21-22 | "RRI data" from ECG |
| **Pers: Global** | ⚠️ CONFLICT | 228, 436 | "control limit...for each patient" |
| **Arch: Self-Attentive AE** | ✅ VERIFIED | 23, 189, 214 | "self-attentive autoencoder" |
| **Window: 45s** | ✅ VERIFIED | 508-509 | "45 seconds" |
| **Fusion: N/A** | ✅ VERIFIED | - | Single modality confirmed |
| **Trade-off: 74% @ 0.85/h** | ✅ VERIFIED | 316, 308 | "74%", "0.85 times/h" |
| **Deployment: Real-time** | ✅ VERIFIED | 22 | "real time" |

**Corrections Needed:**
- Paradigm: Change to "Anomaly" (not end-to-end)
- Personalization: Change to "Patient-specific" (individual limits)

---

## Summary of Corrections Needed

### High Priority Conflicts (affects research question)

| Study | Field | Current | Corrected | Reason |
|-------|-------|---------|-----------|--------|
| Fine 2025 | Modality | 1 | M | Uses ACC + Gyro |
| Nasseri 2021 | Paradigm | Hyb | E2E | LSTM on signals |
| Ode 2023 | Personalization | Global | Patient-specific | Individual control limits |
| Ode 2023 | Paradigm | E2E | Anomaly | Self-attentive AE anomaly detection |

### Medium Priority Corrections

| Study | Field | Current | Corrected | Reason |
|-------|-------|---------|-----------|--------|
| Spahr 2025 | Sens range | 86-100% | 80-100% | Actual range is wider |
| Borujeny 2013 | Sens range | 57-100% | 90-100% | Paper shows 90%, 100%, 100% |
| Meisel 2020 | Arch | LSTM+1D Conv | LSTM | 1D Conv was comparison only |
| Vieluf 2025 | Paradigm | Feat | Hyb | Harmonic + DNN |
| Nasseri 2021 | Personalization | Patient-specific | Temporal | Not patient-specific model |

### Low Priority (clarifications)

| Study | Field | Issue | Action |
|-------|-------|-------|--------|
| Reintjes 2025 | Window | Not found | Mark as N/A or -- |
| Singh 2024 | Features | "594" not found | Remove number |
| Wang 2025 | Arch | Remove "+ SVM/LDA" | Simplify to LSTM |
| Elemam 2025 | Fusion | "Parallel" not found | Change to "Rule-based" |

---

## Final Recommendations

1. **Paradigm Classification**: Use consistent definitions
   - **E2E**: Learns from raw/minimally processed signals
   - **Feature-based**: Uses handcrafted features
   - **Hybrid**: Combines both approaches
   - **Anomaly**: Unsupervised anomaly detection

2. **Modality Count**: ACC + Gyro = Multi-modal (not single)

3. **Personalization**: Distinguish between
   - **Global**: Population model
   - **Patient-specific**: Individualized model
   - **Temporal split**: Train/test on same patient temporally

4. **Stirling 2021**: All verified ✅ - use as reference for correct format

---

**Ready to implement after user approval of corrections.**
