# Literature Review Comparison Table: Wearable Seizure Detection/Forecasting

**Webster & Watson (2002) Approach:** Structured comparison of key metrics across 13 studies on wearable devices for epileptic seizure detection and forecasting.

**Last Updated:** 2026-01-08 (verified against original papers)

---

## Summary Table

| Study | Objective | Design | Sample | Seizure Type | Device | Location | Algorithm | Sens | Spec | FPR | Key Limitations | Conclusion |
|-------|-----------|--------|--------|--------------|--------|----------|-----------|------|------|-----|-----------------|-----------|
| **Vieluf et al. 2025** | Combine diary + wearable to discriminate seizure days | Retrospective observational cohort | n=70; 5437 days; 557 seizure days | Focal seizures | Embrace (Empatica) | Wrist | Fully connected DNN + harmonic 24-h modeling | Det: 82%/78%/57%; Pred: 81%/80% | Det: 67%/66%/44%; Pred: 67%/66% | NR (uses AUC_PR) | Daily resolution only; diary recall bias; no cardiac activity; wearable alone poor | Diary + wearable + clinical data differentiates seizure conditions |
| **Meisel et al. 2020** | Forecast seizures without patient-specific training | Retrospective, LOSO CV | n=69; 452 seizures | Focal, Generalized | Empatica E4 | Wrist/Ankle | LSTM + 1DConv | 51.2% mean; 75.6%* | NR (reports IoC) | TiW 43.7% | Short recordings; pediatric only; 43.5% significant | 43.5% showed better-than-chance forecasting |
| **Stirling et al. 2021** | Develop wearable seizure forecaster using HR cycles | Retrospective + pseudo-prospective | n=11; mean 136 seizures | Focal (8), Generalized (1), Both (2) | Fitbit smartwatch | Wrist | LSTM + RF + LR ensemble | NR (uses AUC) | NR (uses AUC) | AUC 0.74 hourly | Self-reported diaries; limited sample | 100% above chance hourly; HR cycles strongest predictor |
| **Wang et al. 2025** | Test attitude angle (PITCH/ROLL) for seizure detection | Retrospective 10-fold CV | n=28; 62 seizures | Motor seizures | Biovital-P1 (EMP+watch) | Wrist | LSTM + Tree/SVM/LDA | Acc: up to 97.8% | NR | 8.5-8.7/24h | Hospital setting; only 7 seizures tested; 6/28 no seizures | PITCH/ROLL outperform ACC for motor seizure detection |
| **Reintjes et al. 2025** | Evaluate ECG-based seizure detection via anomaly detection | Retrospective train/test split | n=120; 856 seizures | Focal (all types) | Single-lead ECG (Sensor Dot) | Left chest | Matrix Profile, MADRID, TimeVQVAE-AD | 98.16% SDW (MP) | NR | 13.9 FA/h SDW; 1.91 FA/h opt | FAR too high for clinical; no real-time eval | >90% sensitivity but FAR unacceptable for standalone |
| **Ode et al. 2023** | Predict focal seizures using RRI with real-time processing | Retrospective validation | n=66; 264 interictal + 85 preictal | Focal (TLE, FLE, PLE) | ECG (R-R intervals) | NR | Self-Attentive Autoencoder | 74%; 100% in 29/66 pts | NR (precision 0.35) | 0.85/hour | FPs in specific patients; motion artifacts; poor in bitemporal | SA-AE reduces FPs vs AE; needs individual tuning |
| **Singh Rathore 2024** | Multimodal ML for seizure detection (EDA+ACC) | Retrospective single-patient | 1 patient; 6 hours | Not specified | EDA + ACC + HR + BVP | NR | MLP, SVM, KNN, NB, LR | 96.8% (MLP) | NR (precision 94.8%) | NR | Single patient; no real-world validation | MLP best: 97.4% accuracy; needs larger datasets |
| **Borujeny et al. 2013** | Wireless accelerometry for motor seizure detection | Retrospective 3-patient | 3 patients; 20 seizures | Motor seizures | 3× 2D accelerometers (MICAz) | Arms, thigh | ANN, KNN | 100% (KNN k=5) | NR | ANN: 3 FAs; KNN k=5: 0 FAs | Very small; 2D accelerometers; 3Hz sampling | KNN k=5: perfect detection, no false alarms |
| **Fine 2025** | Evaluate tonic seizure detection with ANN | Phase 1 development/validation | n=15 training; 3 test | Tonic with motor manifestations | Wristband (6-axis) | Wrist | ANN (594 features) | 100% (95% CI 69-100) | NR | 0.23/night; 0.023/h (test) | Small test set; offline analysis; EMU only | Promising Phase 1; multicenter trials needed |
| **Spahr et al. 2025** | Tunable deep learning for convulsive seizure detection | Prospective multi-center | n=384; 49 CSs (test) | Generalized/bilateral convulsive | Empatica E4 (ACC only) | Wrist | Ensemble 1D CNN (10 of 30 models) | 96% (90-100) | NR | <1/8 days; 1/61 nights | EMU setting; offline; single sensor | Phase 2 validated; ready for smartwatch integration |
| **Elemam et al. 2025** | Automated tool using questionnaire, HRV, audio | Cross-sectional observational | Q: 198; HRV: 30; Audio: 20 | General epilepsy + PNES | Smartphone camera (PPG) + audio | Finger/thumb; ambient | CNN (HRV/audio), rule-based (Q) | 95.1% (Q); 93% (HRV) | 97.06% (Q); 90% (HRV) | NR | Small HRV/audio samples; PPG only 15s sitting; single hospital | Multi-modal shows promise; needs real-world validation |
| **Nasseri et al. 2021** | Ambulatory seizure forecasting with RNS validation | Retrospective analysis of prospective data | n=6 | Focal onset, FBTC | Empatica E4 (multi-sensor) | Wrist | LSTM RNN (4 layers) | AUC 0.75 (0.50-0.92) | NR | TiW 0.9-7.2h/d | Very small; needs RNS implant; no video; 15-min setback | First successful ambulatory forecasting; 33-min advance warning |
| **Dong et al. 2026** | Two-step ACM+PPG for severe nocturnal seizures | Prospective 10-fold CV | n=68; 788 nights; 1846 seizures | TC, major hypermotor, tonic>30s | NightWatch armband | Upper arm | Two-stage: threshold + CNN-LSTM | 71.6% overall | NR (PPV 33.4%) | 0.165/hour | Imbalanced seizures; single-center; offline | First long-term home study; HR precedes movement by ~100s |

\*LOSO = Leave-One-Subject-Out; SDW = Seizure Detection Window; ACC = Accelerometer; EDA = Electrodermal Activity; BVP = Blood Volume Pressure; PPG = Photoplethysmography; LSTM = Long Short-Term Memory; CNN = Convolutional Neural Network; ANN = Artificial Neural Network; SA-AE = Self-Attentive Autoencoder; TiW = Time in Warning; FA = False Alarm; FPR = False Positive Rate; EMU = Epilepsy Monitoring Unit; IoC = Improvement over Chance; FBTC = Focal to Bilateral Tonic-Clonic; TC = Tonic-Clonic; CS = Convulsive Seizure; Acc = Accuracy; NR = Not Reported; PNES = Psychogenic Non-Epileptic Seizures

---

## Key Metrics Legend

| Metric | Description |
|--------|-------------|
| **Design** | Study methodology (R=Retrospective, P=Prospective, CV=Cross-Validation) |
| **Sample** | Number of patients/participants; seizure/events count |
| **Sens** | Sensitivity/Recall (True Positive Rate) - labeled "Acc" when only accuracy reported |
| **Spec** | Specificity (True Negative Rate) - labeled as "NR" when precision reported instead |
| **FPR** | False Positive Rate (per hour/day/night) |
| **NR** | Not Reported |

---

## Detection vs Forecasting

### Detection Studies (real-time identification)
| Study | Detection Window | Best Sensitivity | Best FPR | Notes |
|-------|------------------|------------------|----------|-------|
| Reintjes 2025 | Real-time | 98.16% | 1.91 FA/h (optimized) | FAR too high for clinical use |
| Fine 2025 | 10s intervals | 100% (test) | 0.16/night | Offline analysis; small test set |
| Spahr 2025 | Real-time | 96% (90-100) | 1/61 nights | Phase 2 validated |
| Dong 2026 | 5-min windows | 71.6% | 0.165/hour | Two-stage approach |
| Wang 2025 | Windowed | Acc: 97.8% | 8.5/24h | Accuracy, NOT sensitivity |
| Singh Rathore 2024 | Windowed | 96.8% | NR | Single patient only |
| Borujeny 2013 | Real-time | 100% (KNN k=5) | 0 (k=5) | Very small sample |
| Elemam 2025 | HR>120 or +20%; 10s audio | 93% (HRV) | NR | PPG measured sitting, 15s only |
| Vieluf 2025 | Daily resolution | 82% (combined) | NR | Wearable alone: 57% |

### Forecasting Studies (prediction before onset)
| Study | Forecast Horizon | Performance | Time in Warning | Notes |
|-------|------------------|-------------|-----------------|-------|
| Nasseri 2021 | Mean 33 min advance | AUC 0.75 (0.50-0.92) | 0.9-7.2 h/day | Retrospective analysis of prospective data |
| Stirling 2021 | 37 min (hourly); 3 days (daily) | AUC 0.74 hourly | 14-18% | 100% above chance hourly |
| Meisel 2020 | Preictal period | 51.2% mean; 75.6%* | 43.7% | *Significant patients only (43.5%) |
| Ode 2023 | Preictal detection | 74% | NR | 100% in 29/66 patients |
| Vieluf 2025 | Daily prediction | 81% (combined) | NR | Diary-based: 82% |

---

## Device Types Summary

| Device Type | Studies | Sensors Used |
|-------------|---------|--------------|
| **Wrist-worn** | Meisel 2020, Stirling 2021, Wang 2025, Spahr 2025, Fine 2025, Nasseri 2021, Vieluf 2025 | ACC, GYR, EDA, BVP/PPG, TEMP |
| **Cross-body ECG** | Reintjes 2025, Ode 2023 | Single-lead ECG |
| **Armband** | Dong 2026 | ACM + PPG |
| **Multi-location WSN** | Borujeny 2013 | 2D accelerometers |
| **Smartphone** | Elemam 2025 | Camera (PPG), audio |

---

## Algorithm Categories

| Algorithm Type | Studies |
|----------------|---------|
| **Deep Learning (LSTM/CNN)** | Meisel 2020, Nasseri 2021, Stirling 2021, Wang 2025, Dong 2026, Spahr 2025, Elemam 2025, Vieluf 2025 |
| **Anomaly Detection** | Reintjes 2025, Ode 2023 |
| **Traditional ML** | Singh Rathore 2024 (MLP, SVM, KNN, NB, LR), Stirling 2021 (RF, LR) |
| **Neural Networks** | Fine 2025 (ANN), Borujeny 2013 (ANN) |

---

## Quality Assessment Notes

| Study | Strengths | Weaknesses |
|-------|-----------|------------|
| Vieluf 2025 | Largest dataset (5437 days); multi-center; longitudinal outpatient | Diary-based labels; daily resolution only; wearable alone poor (AUC .49) |
| Meisel 2020 | Large sample; LOSO CV | Short recordings; pediatric only; only 43.5% significant |
| Stirling 2021 | Cyclic features novel; 100% above chance hourly | Self-reported diaries; limited sample |
| Wang 2025 | Novel attitude angle approach | Hospital setting; only 7 seizures tested; 97.8% is accuracy NOT sensitivity |
| Reintjes 2025 | Largest ECG dataset; open benchmark | FAR too high for clinical use |
| Ode 2023 | Multi-center; attention mechanism | Retrospective validation; high FPs in some patients |
| Singh Rathore 2024 | Comprehensive ML comparison | Single patient; 94.8% is precision NOT specificity |
| Borujeny 2013 | Early WSN work | Very small; 2D accelerometers; 3Hz sampling |
| Fine 2025 | Phase 1 validation protocol | Small test set; offline analysis; EMU only |
| Spahr 2025 | Multi-center; tunable sensitivity | EMU setting; offline analysis |
| Elemam 2025 | Multi-modal (Q+HRV+audio) | Cross-sectional; PPG only 15s sitting; small samples |
| Nasseri 2021 | First ambulatory forecasting; long-term | Very small n=6; AUC 0.75 NOT sensitivity 75%; requires RNS |
| Dong 2026 | Long-term home monitoring (months) | Single-center; offline analysis |

---

## Corrections Applied (2026-01-08)

| Study | Field | Original | Corrected | Reason |
|-------|-------|----------|-----------|--------|
| Wang 2025 | Seizure Type | "Not specified" | "Motor seizures" | Paper specifies focal onset motor seizures and GTCS |
| Wang 2025 | Sensitivity | "Up to 97.8%" | "Acc: up to 97.8%" | 97.8% is accuracy, NOT sensitivity |
| Singh Rathore 2024 | Specificity | "94.8% (MLP)" | "NR (precision 94.8%)" | 94.8% is precision (TP/(TP+FP)), NOT specificity |
| Ode 2023 | Design | "Prospective" | "Retrospective validation" | Data analysis was retrospective using existing databases |
| Ode 2023 | Sample | Added 264 interictal validation episodes | | Complete sample description |
| Borujeny 2013 | FPR | "3 FAs (ANN k=1)" | "ANN: 3 FAs; KNN k=5: 0 FAs" | ANN doesn't have "k" parameter |
| Nasseri 2021 | Design | "Prospective" | "Retrospective analysis of prospective data" | Paper states "Phase 2 retrospective evidence" |
| Nasseri 2021 | Sensitivity | "75% mean (50-92)" | "AUC 0.75 (0.50-0.92)" | Primary metric is AUC-ROC, NOT sensitivity |
| Nasseri 2021 | TiW | "0.62-7.2h/d" | "0.9-7.2h/d" | Minimum is 0.9, not 0.62 |
| Elemam 2025 | Design | "Prospective validation" | "Cross-sectional observational" | Paper describes "transversal observational study" |
| Elemam 2025 | Seizure Type | Added "+ PNES" | | Includes psychogenic non-epileptic seizures |

---

## References (BibTeX-style)

1. Borujeny et al. (2013) - Detection of Epileptic Seizure Using Wireless Sensor Networks
2. Meisel et al. (2020) - Machine learning from wristband sensor data for wearable, noninvasive seizure forecasting
3. Nasseri et al. (2021) - Ambulatory seizure forecasting with a wrist-worn device using long-short term memory deep learning
4. Ode et al. (2023) - Development of an epileptic seizure prediction algorithm using R-R intervals with self-attentive autoencoder
5. Singh Rathore et al. (2024) - Development of a Multimodal Machine Learning Model for Seizure Detection Using Wearable Devices
6. Stirling et al. (2021) - Forecasting Seizure Likelihood With Wearable Technology
7. Reintjes et al. (2025) - ECG-Based Detection of Epileptic Seizures in Real-World Wearable Settings Insights from the SeizeIT
8. Wang et al. (2025) - Epileptic Seizure Detection Based on Attitude Angle Signal of Wearable Device
9. Fine (2025) - Detection is Key Automated Tonic Seizure Detection With a Wearable Device
10. Spahr et al. (2025) - Deep learning-based detection of generalized convulsive seizures using a wrist-worn accelerometer
11. Elemam et al. (2025) - Automated validated tool for epileptic seizure detection using deep learning
12. Dong et al. (2026) - Detection of nocturnal epileptic seizures using a wearable armband A deep learning approach combining...
13. Vieluf et al. (2025) - Seizure monitoring by combined diary and wearable data: A multicenter, longitudinal, observational study

---

## Emerging Trends (2013-2026)

| Trend | Evidence |
|-------|----------|
| **Shift to deep learning** | Earlier studies used ANN/KNN (2013); recent use LSTM/CNN/transformers |
| **Multi-modal approaches** | Combining ACC + EDA + PPG improves accuracy |
| **Ambulatory focus** | Moving from EMU to real-world home monitoring |
| **Daily-resolution monitoring** | Vieluf 2025 introduces day-based seizure risk classification using wearable + diary integration |
| **Diary + wearable integration** | Vieluf 2025 shows clinical data + wearables enhances detection; hybrid approaches emerging |
| **Forecasting advancement** | From detection to prediction (minutes to days ahead) |
| **Algorithm tuning** | Spahr 2025 introduces tunable sensitivity for clinical needs |
| **Open benchmarks** | Reintjes 2025 establishes first open ECG dataset |
