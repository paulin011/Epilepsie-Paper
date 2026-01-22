# Final Table Values Report
## All Corrected Values for Literature Review Tables

**Date:** 2026-01-22
**Status:** All corrections applied

---

## Table 1A: Detection Studies Matrix (Final Values)

| Study | Design | Sample | Device | Loc. | Para. | Mod. | Pers. | Algorithm | Sens | Spec | FPR |
|-------|--------|--------|--------|------|-------|------|-------|-----------|------|------|-----|
| **Spahr 2025** | Prospective | n=384, 49 CSs (test) | Empatica E4 (ACC) | Wrist | Ens | 1 | Glb | Ensemble 1D CNN (30 models) | 96% | -- | 0.005/h |
| **Reintjes 2025** | Retro | n=120, 856 szs | Single-lead ECG | Chest | Anom | 1 | Subj | Anomaly: Matrix Profile, MADRID, TimeVQVAE | 38.0%/98.16% | -- | 1.91--39.75/h |
| **Fine 2025** | Phase 1 | n=15/3 | 6-axis band (ACC+Gyro) | Wrist | Feat | M | Glb | ANN (594 handcrafted feat) | 100%Test, 96% complete | -- | 0.023/h |
| **Dong 2026** | Prospective | n=68, 1846 szs | NightWatch | Arm | 2-stg | M | Glb | CNN-LSTM + Attention | 71.6% | -- | 0.165/h |
| **Wang 2025** | Retrospective | n=28, 62 szs | Biovital-P1 | Wrist | Feat | M | Glb | LSTM (40 hidden) | 56.40% to 95.3% | -- | 0.354/h |
| **Singh 2024** | Case study | 1 pt, 6 hrs | Wearable (EDA+ACC+HR) | -- | Feat | M | CS | MLP (multi-modal features) | 96.8% | 94.8%prec | -- |
| **Elemam 2025** | Cross-sect | Q:198, HRV:30 | Camera PPG | Thumbs | Hyb | M | Glb | CNN + Rule-based fusion | 95.1% Q, 93% HRV | 97.06% Q | -- |
| **Borujeny 2013** | 3-pt | 3 pts, 20 szs | MICAz ACC | Arm/thigh | Feat | 1 | Glb | **ANN** (time-domain feat) | **85%** | -- | **3 FA** |

### Legend
- **Ens** = Ensemble
- **Anom** = Anomaly detection
- **Feat** = Feature-based
- **Hyb** = Hybrid
- **2-stg** = Two-stage
- **CS** = Case study
- **prec** = Precision (not specificity)
- **FA** = False alarms

---

## Table 1B: Forecasting Studies Matrix (Final Values)

| Study | Design | Sample | Device | Loc. | Para. | Mod. | Pers. | Algorithm | Sens | Spec | FPR |
|-------|--------|--------|--------|------|-------|------|-------|-----------|------|------|-----|
| **Vieluf 2025** | Retro | n=70, 5437 d | Embrace | Wrist | **Hyb** | M | Mix | DNN + harmonic features + diary | 82% | 67% | -- |
| **Meisel 2020** | LOSO CV | n=69, 452 szs | Empatica E4 | Wrist/Ankle | E2E | M | Glb | LSTM **(10 units)** | 51.2% | -- | TiW 43.7% |
| **Stirling 2021** | Retro+pseudo | n=11, 136 szs | Fitbit | Wrist | Feat | M | Pat | LSTM+RF+LR ensemble (RCH feat) | -- | -- | AUC 0.74 |
| **Nasseri 2021** | Retro | n=6 | Empatica E4 | Wrist | E2E | M | Tmp | LSTM 4-layer (128 hidden) | **AUC 0.75 (SD 0.15)** | -- | TiW 0.9--7.2h/d |
| **Ode 2023** | Retro | n=66, 85 szs | ECG | -- | Anom | 1 | Pat | Self-Attentive AE | 74% | -- | 0.85/h |

### Critical Corrections Applied
1. **Vieluf 2025**: Paradigm changed from `Feat` to `Hyb` (combines DNN with handcrafted harmonic features)
2. **Meisel 2020**: Algorithm changed from `LSTM + 1D Conv` to `LSTM (10 units)` (1D Conv was comparison only)
3. **Nasseri 2021**: AUC changed from `0.80` to `0.75 (SD 0.15)` (0.80 was only 5 successful patients, 0.75 is all 6)

---

## Table 2A: Detection Studies Architecture (Final Values)

| Study | Paradigm | Arch. Details | Modality Details | Fusion | Personalization | Trade-off Config | Deployment |
|-------|----------|---------------|------------------|--------|-----------------|------------------|------------|
| **Spahr 2025** | Ensemble | 30 1D CNN, 14 conv layers, quantile | ACC 32 Hz, Euclidean norm, 30 s | -- | Global, tunable | 86--100% @ 0.005/h | Real-time (112 ms), on-device |
| **Reintjes 2025** | Anomaly | Matrix-Profile, MADRID, TimeVQVAE-AD | ECG 256->8 Hz, bandpass | -- | Subject split | 38.0--98.2% @ 1.91--39.75/h | Offline, hospital |
| **Fine 2025** | Feature-based | ANN, 594 handcrafted features | ACC+Gyro 6-axis, 10 s intervals | Early | Global, hold-out | 100% @ 0.023/h | Offline PC, EMU |
| **Dong 2026** | Two-stage | Pre-screening + CNN-LSTM + Attention | ACM 11-12->20 Hz, PPG 100->20 Hz, 5 min | Early | Global, 10-fold CV | 71.6% @ 0.165/h | Real-time, NightWatch, home |
| **Wang 2025** | Feature-based | LSTM (40 hidden) + ReLU + FC | ACC/GYR 50 Hz, SEMG 200 Hz, EDA 4 Hz, 4 s | Early | Global, hold-out | 56.4--95.3% @ 0.354/h | Real-time, hospital |
| **Singh 2024** | Feature-based | MLP, multi-modal features | EDA, ACC, HR/HRV, 25k points | Early | Single pt (CS) | 96.8% @ 94.8% prec | Real-time, cloud? |
| **Elemam 2025** | CNN-based | CNN for HRV, CNN for Audio (separate) | PPG 250 Hz, Audio 10 s | No fusion | Global, unclear | 95.1% @ 97.06% spec | Real-time, hospital |
| **Borujeny 2013** | Feature-based | **ANN**, time-domain features | ACC 2D 3 Hz, 9 s | -- | Global, 3 pts | **85% @ 3 FA** | Real-time, server (316 mW) |

---

## Table 2B: Forecasting Studies Architecture (Final Values)

| Study | Paradigm | Arch. Details | Modality Details | Fusion | Personalization | Trade-off Config | Deployment |
|-------|----------|---------------|------------------|--------|-----------------|------------------|------------|
| **Vieluf 2025** | Hybrid | DNN + harmonic modeling (24-h) | EDA 4 Hz, ACC 32 Hz, Temp 1 Hz, 10 min | Early | Mixed, 5-fold + LOO | 82% sens, 67% spec @ F1 0.81 | Offline MATLAB, home |
| **Meisel 2020** | End-to-end | LSTM only (10 units) | EDA/ACC/BVP/Temp ->4 Hz, 30 s | Early | Global, LOSO | 51.2% @ IoC 14.1% | Offline, hospital |
| **Stirling 2021** | Feature-based | LSTM+RF+LR ensemble, LR combines | HR 5 s, steps/sleep 1 min, hourly/daily | Decision | Patient-specific, weekly | AUC 0.74, 100% pts | Home (Fitbit), app |
| **Nasseri 2021** | End-to-end | LSTM 4-layer, 128 hidden + FFT channels | ACC/BVP/EDA/Temp/HR ->128 Hz, 60 s | Early (17-ch) | Temporal split | **AUC 0.75 (SD 0.15)** @ TiW 0.9--7.2h/d | Offline, cloud, home |
| **Ode 2023** | Anomaly | Self-Attentive AE (attention) | ECG (RRI only), 45 s | -- | Patient-specific (99% CL) | 74% @ 0.85/h (99% CL) | Real-time, cloud, hospital |

---

## Table 3: Metrics Summary (Final Values)

| Metric | Detection (n=8) | Forecasting (n=5) | Reported By |
|--------|-----------------|------------------|-------------|
| **Sensitivity/Recall** | 8/8 | 1/5 | Spahr, Reintjes, Fine, Dong, Wang, Singh, Elemam, Borujeny, Ode |
| **Specificity** | 3/8 | 1/5 | Elemam, Vieluf, Wang, Ode |
| **FPR/FA rate** | 8/8 | 0/5 | Spahr, Reintjes, Fine, Dong, Wang, Singh, Elemam, Borujeny, Nasseri, Ode |
| **AUC-ROC** | 3/8 | 3/5 | Dong, Reintjes, Ode, Nasseri, Stirling |
| **Detection Latency** | 4/8 | 1/5 | Spahr, Fine, Elemam, Borujeny, Nasseri |
| **Patient Success Rate** | 2/8 | 4/5 | Reintjes, Meisel, Stirling, Nasseri, Ode |
| **Precision/PPV** | 4/8 | 1/5 | Dong, Singh, Elemam, Ode |
| **IoC / Time in Warning** | 0/8 | 3/5 | Meisel, Stirling, Nasseri |

### Notes
- **Detection studies (n=8)**: Spahr, Reintjes, Fine, Dong, Wang, Singh, Elemam, Borujeny
- **Forecasting studies (n=5)**: Vieluf, Meisel, Stirling, Nasseri, Ode
- **Ode** is classified as forecasting in Table 1B but reports detection-like metrics (sensitivity 74%)

---

## Summary of All Corrections Applied

### Critical Corrections (Value Changes)
| Study | Field | Before | After | Reason |
|--------|-------|--------|-------|--------|
| **Spahr 2025** | FPR | <0.0125/h | 0.005/h | 1/8 days = 0.005/h, not 0.0125/h |
| **Nasseri 2021** | AUC | 0.80 (SD 0.15) | 0.75 (SD 0.15) | 0.75 is mean of all 6 patients; 0.80 is only 5 successful |
| **Singh 2024** | Spec | 94.8% | 94.8%prec | This is precision, not specificity |
| **Singh 2024** | Pers | Glb | CS | Single-patient case study |
| **Elemam 2025** | Sens (HRV) | 93--90% | 93% | Not a range, single value |
| **Borujeny 2013** | Algorithm | KNN k=5 | ANN | Literature review focuses on DL models, not KNN |
| **Borujeny 2013** | Sens | 100% | 85% | ANN result (17/20 detected), not KNN |
| **Borujeny 2013** | FPR | 0 | 3 FA | ANN has 3 false alarms |

### Algorithm Description Corrections
| Study | Before | After | Reason |
|--------|--------|-------|--------|
| **Vieluf 2025** | Feat | Hyb | Combines DNN with handcrafted harmonic features |
| **Meisel 2020** | LSTM + 1D Conv | LSTM (10 units) | 1D Conv was comparison only |
| **Stirling 2021** | HRV feat | RCH feat | Uses Rate of Change in HR, more precise |

### Format/Consistency Corrections
| Study | Field | Correction |
|--------|-------|------------|
| **Reintjes 2025** | FPR range | 39.75/h (not 40.5/h) |
| **Elemam 2025** | Spec | 97.06% (not 97.1%) |

---

## KNN Results for Borujeny 2013 (Reference Only)

**Not included in tables** (tables focus on DL/ANN models only)

| K Value | Sensitivity | False Alarms |
|---------|-------------|--------------|
| k=1 | 90% (18/20) | 3 |
| k=3 | 100% (20/20) | 2 |
| **k=5** | **100% (20/20)** | **0** |

**Source:** Borujeny et al. 2013, Table 2 (lines 656-684), lines 721-722

---

## Detection Studies Count Clarification

**Total Detection Studies: 8** (not 9 as originally stated)

1. Spahr et al. 2025
2. Reintjes et al. 2025
3. Fine 2025
4. Dong et al. 2026
5. Wang et al. 2025
6. Singh Rathore et al. 2024
7. Elemam et al. 2025
8. Borujeny et al. 2013

**Total Forecasting Studies: 5** (not 4 as originally stated)

1. Vieluf et al. 2025
2. Meisel et al. 2020
3. Stirling et al. 2021
4. Nasseri et al. 2021
5. Ode et al. 2023

---

## Verification Methodology

Each study was verified by:
1. Reading the full source paper from `/all_papers_md/`
2. Cross-referencing with existing verification reports in `/Modifications/`
3. Checking line-by-line evidence for each claimed value
4. One agent per study for independent verification
5. Conflicts resolved with source paper evidence

---

**Report Generated:** 2026-01-22
**All Corrections Applied:** Yes
**Files Updated:**
- `/Tables(tex)/table1a_detection_matrix.tex`
- `/Tables(tex)/table1b_forecasting_matrix.tex`
- `/Tables(tex)/table2a_detection_studies.tex`
- `/Tables(tex)/table2b_forecasting_studies.tex`
- `/Tables(tex)/table3_metrics_summary.tex`
