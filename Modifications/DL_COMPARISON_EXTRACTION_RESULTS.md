# Deep Learning Architecture & Biosignal Modality Comparison - Extraction Results

**Research Goal:** "How do different deep learning architectures and biosignal modalities excluding EEG compare in their ability to achieve an optimal trade-off between sensitivity and false alarm rate for ambulatory seizure monitoring?"

---

## Part 1: Architecture Paradigm (Feature-based vs End-to-end)

| Study | Paradigm | Evidence | Line |
|-------|----------|----------|------|
| **Spahr 2025** | End-to-end | "Each model...takes the 3D-acc amplitude as input and consists of a 1D CNN" | 106-108, 292-294 |
| **Reintjes 2025** | End-to-end | "Our methods operate directly on the preprocessed ECG time series...We do not extract features such as heart rate, HRV indices" | 145-148 |
| **Fine 2025** | Feature-based | "Features were extracted in 10-s intervals...with 594 features, such as mean, variance, and standard deviation" | 61-64 |
| **Dong 2026** | Hybrid | "Raw ACM and PPG signals are first transformed into a set of statistical and physiological features, which are then processed by a DL model" | 206-208, 544-548 |
| **Wang 2025** | Feature-based | "Time, frequency, and nonlinear domain features are extracted from each signal" | 363-364 |
| **Singh Rathore 2024** | Feature-based | "Features including heart rate variability (BVP), electrodermal activity (EDA), and accelerometery (ACC)" | 452-454, 576-580 |
| **Elemam 2025** | End-to-end | "The convolutional layers of the CNN are responsible for learning these features" | 560-562 |
| **Borujeny 2013** | Feature-based | "We used three features: Variance, Correlation, Energy (sum of squared FFT component magnitudes)" | 428-434 |
| **Vieluf 2025** | Feature-based | "Best-ranking wearable markers and seizure diary variables were fed into a fully connected neural network" | 66-69 |
| **Meisel 2020** | End-to-end | "Deep learning uses multiple layers of connections to perform classification tasks without the need of feature designing" | 167-194 |
| **Stirling 2021** | Feature-based | "Heart rate features included rate of change in heart rate (RCH)...Physical activity features included steps...Sleep features included total time asleep" | 284-301 |
| **Nasseri 2021** | Hybrid | "The physiological time-series signals, their Fourier transforms, the SQI values and time of day were formed 17 channels" | 172-175 |
| **Ode 2023** | End-to-end | "The input values of SA-AE are the original RRI data, and the output values are the RRI data reconstructed by SA-AE" | 400-410 |

**Summary:**
- **End-to-end:** 5 studies (Spahr 2025, Reintjes 2025, Elemam 2025, Meisel 2020, Ode 2023)
- **Feature-based:** 5 studies (Fine 2025, Wang 2025, Singh Rathore 2024, Borujeny 2013, Vieluf 2025, Stirling 2021)
- **Hybrid:** 2 studies (Dong 2026, Nasseri 2021)

---

## Part 2: Architecture Details (Anomaly Detection, Attention, Ensemble)

| Study | Anomaly Detection | Attention | Ensemble | Secondary Architecture |
|-------|-------------------|-----------|----------|------------------------|
| **Spahr 2025** | No | No | No | CNN (1D) |
| **Reintjes 2025** | Yes (Matrix Profile, MADRID, TimeVQVAE-AD) | No | No | Multiple anomaly methods |
| **Fine 2025** | No | No | No | CNN |
| **Dong 2026** | No | No | Yes (2-layer) | CNN + LSTM |
| **Wang 2025** | No | No | No | CNN + SVM |
| **Singh Rathore 2024** | No | No | No | Random Forest |
| **Elemam 2025** | No | No | No | CNN |
| **Borujeny 2013** | No | No | No | ANN + KNN |
| **Vieluf 2025** | No | No | No | FCNN |
| **Meisel 2020** | No | No | No | LSTM |
| **Stirling 2021** | No | No | Yes (LSTM+RF+LR) | LSTM + RF + LR |
| **Nasseri 2021** | No | No | No | LSTM (4-layer, 128 hidden) |
| **Ode 2023** | Yes (Autoencoder) | Yes (Self-attention) | No | Self-Attentive AE |

**Summary:**
- **Anomaly Detection:** 2 studies (Reintjes 2025, Ode 2023)
- **Attention Mechanisms:** 1 study (Ode 2023)
- **Ensemble Methods:** 2 studies (Dong 2026, Stirling 2021)

---

## Part 3: Modality Count (Single vs Multi-modal)

| Study | Modality | Signals | Line |
|-------|----------|---------|------|
| **Spahr 2025** | Single | ACC (accelerometer) | 13-14, 106-108 |
| **Reintjes 2025** | Single | ECG | 4, 22-25 |
| **Fine 2025** | Single | ACC + Gyroscope (motion only) | 17-18, 22-24 |
| **Dong 2026** | Multi | ACC, PPG, HR (derived) | 11-13, 226, 241-248 |
| **Wang 2025** | Multi | ACC, GYR, PITCH, ROLL, SEMG, EDA | 35-43, 88-90 |
| **Singh Rathore 2024** | Multi | EDA, ACC, BVP (PPG), HR, HRV | 225-230, 242-250 |
| **Elemam 2025** | Multi | HRV (from ECG/PPG), Audio | 17-18, 56-57 |
| **Borujeny 2013** | Single | ACC (2D accelerometer) | 22-23, 56 |
| **Vieluf 2025** | Multi | EDA, ACC, Temp | 260-264 |
| **Meisel 2020** | Multi | EDA, ACC, BVP, Temp | 246-248 |
| **Stirling 2021** | Multi | HR (from PPG), Step count, Sleep | 29-30, 251-254 |
| **Nasseri 2021** | Multi | ACC, BVP, EDA, Temp, HR | 116-118, 167-168 |
| **Ode 2023** | Single | ECG (RRI only) | 21-23, 71-73 |

**Summary:**
- **Single-modal:** 4 studies (Spahr 2025, Reintjes 2025, Fine 2025, Borujeny 2013, Ode 2023)
- **Multi-modal:** 8 studies (Dong 2026, Wang 2025, Singh Rathore 2024, Elemam 2025, Vieluf 2025, Meisel 2020, Stirling 2021, Nasseri 2021)

---

## Part 4: Modality Details (Sampling Frequency, Signal Processing)

| Study | Primary Signal | Sampling Freq | Signal Processing | Window Size |
|-------|----------------|---------------|-------------------|-------------|
| **Spahr 2025** | ACC | 32 Hz | Raw (3D-acc amplitude via Euclidean norm) | 30 s, stride 5 s |
| **Reintjes 2025** | ECG | 256 Hz → 8 Hz | Bandpass (0.5-40 Hz), normalized, downsampled | Various (25-100 s) |
| **Fine 2025** | ACC | N/A | Features (594) in 10-s intervals | 10 s, 1-s overlap |
| **Dong 2026** | ACC + PPG | ACM: 11-12 Hz → 20 Hz; PPG: 100 Hz → 20 Hz | Butterworth filters, 9 features @ 1 Hz | Pre-screening: 10-20 s; Detection: 5 min |
| **Wang 2025** | Multi | ACC/GYR: 50 Hz; SEMG: 200 Hz; EDA: 4 Hz | Median/bandpass filters, features extracted | 4 s, 50% overlap |
| **Singh Rathore 2024** | EDA + ACC | N/A | Raw | 25,000 data points |
| **Elemam 2025** | PPG + Audio | 250 Hz (PPG) | Bandpass (0.5-40 Hz), features | 10 s (audio), 15 s (PPG) |
| **Borujeny 2013** | ACC | 3 Hz | Moving average filter, FFT features | 50 samples (~16.67 s) |
| **Vieluf 2025** | EDA + ACC + Temp | EDA: 4 Hz; ACC: 32 Hz; Temp: 1 Hz | 24-h harmonic modeling, Lomb-Scargle | 10-min windows |
| **Meisel 2020** | EDA + ACC + BVP + Temp | All → 4 Hz | Raw with Chebyshev antialiasing | 30-s nonoverlapping |
| **Stirling 2021** | HR + Steps + Sleep | N/A | Features (RCH, RHR, steps, sleep) | Hourly/Daily |
| **Nasseri 2021** | Multi | Varies by signal | FFT + time series | 5-min segments |
| **Ode 2023** | ECG (RRI) | Varies | Raw RRI | Real-time (8 s threshold) |

---

## Part 5: Personalization Strategy (Model Scope, Validation)

| Study | Model Scope | Validation | Test Patient in Training | Adaptation | Line |
|-------|-------------|------------|-------------------------|------------|------|
| **Spahr 2025** | Global | Patient-independent (347 test separate from 37 train) | No | None | 270-275 |
| **Reintjes 2025** | Global | LOSO (sub-001 to sub-096 train, sub-097 to sub-125 test) | No | None | 196-200 |
| **Fine 2025** | Global | Hold-out (3 test separate from 15 train) | No | None | 24-28 |
| **Dong 2026** | Global | 10-fold CV with subject-independent split | No | None | 603-617 |
| **Wang 2025** | Global | Hold-out (IDs 1-18 train, 19-28 test) | No | None | 512-527 |
| **Singh Rathore 2024** | Global (single pt) | Train/test split from same patient | **Yes** | None | 499-503 |
| **Elemam 2025** | Global | Unclear | Unclear | None | 1081-1083 |
| **Borujeny 2013** | Global | Same-patient (3 pts) | **Yes** | None | 728-740 |
| **Vieluf 2025** | Mixed | 5-fold CV + leave-one-out | Mixed | None | 454-456, 474-491 |
| **Meisel 2020** | Global | LOSO (68 train, 1 test) | No | None | 78-80, 299-302 |
| **Stirling 2021** | **Patient-specific** | Temporal hold-out + pseudo-prospective | **Yes** | Weekly retraining | 265-281 |
| **Nasseri 2021** | **Patient-specific** | Temporal split (1/3 train, 2/3 test) | **Yes** | None | 179-182 |
| **Ode 2023** | Global | Hold-out (interictal train, preictal test) | **Yes** | None | 286-288 |

**Summary:**
- **Global models:** 9 studies
- **Patient-specific:** 2 studies (Stirling 2021, Nasseri 2021)
- **LOSO validation:** 2 studies (Reintjes 2025, Meisel 2020)
- **Training includes test patient:** 5 studies (Singh Rathore 2024, Borujeny 2013, Vieluf 2025, Stirling 2021, Nasseri 2021, Ode 2023)

---

## Part 6: Fusion Type (Multi-modal studies only)

| Study | Fusion Stage | Fusion Method | Cross-modal Attention |
|-------|--------------|---------------|----------------------|
| **Dong 2026** | Late | Ensemble averaging | No |
| **Wang 2025** | Feature | Feature concatenation | No |
| **Singh Rathore 2024** | Feature | Feature concatenation | No |
| **Elemam 2025** | Late | Rule-based combination (Q + HRV + Audio) | No |
| **Vieluf 2025** | Feature | Neural network input | No |
| **Meisel 2020** | Feature | Multi-channel input to LSTM | No |
| **Stirling 2021** | Late | Ensemble averaging | No |
| **Nasseri 2021** | Feature | 17-channel input (time + FFT) | No |

**Note:** No study uses cross-modal attention mechanisms.

---

## Part 7: Performance Trade-off Configuration

| Study | Operating Points | Optimization Target | Threshold Strategy | Sens Range | FAR Range |
|-------|------------------|---------------------|-------------------|------------|-----------|
| **Spahr 2025** | Tunable (quantile-based) | Balanced (HMS) | Adaptive (quantile parameter q) | 86-100% | 0.01-0.5/day |
| **Reintjes 2025** | Multiple | FAR-opt / Sens-opt / HMS-opt | ROC-based | 7.14-100% | 0.05-40.46/h |
| **Fine 2025** | Single | Sens-opt (100%) | Fixed (0.1g feature) | 96-100% | 0.16-0.23/night |
| **Dong 2026** | Single | AUC-opt | Fixed (ROC-based) | 70.4-82.1% | 0.097-0.234/h |
| **Wang 2025** | Single | Balanced | Fixed (0.5 softmax) | 56.40-95.3% | 8.46-8.73/24h |
| **Singh 2024** | Multiple | AUC-opt | Fixed (0.5) | 92.3-97.9% | N/A |
| **Elemam 2025** | Multiple | Sens-opt | Fixed/Adaptive (HR >120 or 20% increase) | 91.5-95.1% | 2.9-7% |
| **Borujeny 2013** | Multiple (K=1,3,5) | Balanced | Fixed | 57-100% | 0-15% |
| **Vieluf 2025** | Multiple | AUC-opt | ROC-based | 57-82% | 33-44% |
| **Meisel 2020** | Tunable (3 params) | Balanced (IoC) | Adaptive/Patient-specific (0.5-0.6) | 51.2-75.6% | TiW 43.7-47.2% |
| **Stirling 2021** | Multiple (3 risk states) | Balanced (4 criteria) | Adaptive/Patient-specific | N/A (forecast: 83-86%) | N/A |
| **Nasseri 2021** | Multiple | AUC-opt | ROC-based/Patient-specific | 27-88% | TiW 0.9-7.2 h/d |
| **Ode 2023** | Single | Sens-opt/FAR-opt | Fixed (99% CL, 8 s threshold) | 74-100% | 0.85-2.6/h |

**Summary:**
- **Single operating point:** 4 studies (Fine 2025, Dong 2026, Wang 2025, Ode 2023)
- **Multiple operating points:** 7 studies (Reintjes 2025, Singh 2024, Elemam 2025, Borujeny 2013, Vieluf 2025, Meisel 2020, Stirling 2021, Nasseri 2021)
- **Tunable/Adaptive:** 3 studies (Spahr 2025, Meisel 2020, Stirling 2021)

---

## Part 8: Deployment Factors (Real-time, On-device, Power)

| Study | Real-time | On-device | Power Reported | Device Type | Deployment |
|-------|-----------|-----------|----------------|-------------|------------|
| **Spahr 2025** | Yes (112 ms inference) | Yes (TicWatch Pro 3, TFLite) | Yes (24-h continuous) | Commercial | EMU |
| **Reintjes 2025** | No (offline) | No/Cloud | No | Research prototype | Real-world |
| **Fine 2025** | No (offline PC) | No | No | Research prototype | EMU |
| **Dong 2026** | Yes | Hybrid (base station) | No | Commercial (NightWatch) | Home |
| **Wang 2025** | Yes | Hybrid (phone) | No | Research prototype | Hospital |
| **Singh 2024** | Yes (designed for) | Unknown/Cloud | No | Research prototype | Unknown |
| **Elemam 2025** | Yes | Cloud (PC/mobile) | No | Research prototype | Hospital |
| **Borujeny 2013** | Yes (alarm immediate) | No (server) | Yes (316 mW) | Research prototype | Home |
| **Vieluf 2025** | No (retrospective) | No/Cloud | No | Commercial (Embrace) | Home |
| **Meisel 2020** | Unknown | Unknown | No | Commercial (E4) | EMU |
| **Stirling 2021** | Yes (hourly/daily) | Unknown (phone) | No | Commercial (Fitbit) | Home |
| **Nasseri 2021** | No (retrospective) | No/Cloud | No | Commercial (E4) | Home |
| **Ode 2023** | Yes (Algorithm 2) | Unknown | No | Unknown | Hospital/EMU |

**Summary:**
- **Real-time capable:** 7 studies (Spahr 2025, Dong 2026, Wang 2025, Singh 2024, Elemam 2025, Borujeny 2013, Stirling 2021, Ode 2023)
- **On-device processing:** 2 studies (Spahr 2025, possibly Borujeny 2013 with base station)
- **Power reported:** 2 studies (Spahr 2025, Borujeny 2013)
- **Commercial devices:** 6 studies (Spahr 2025, Dong 2026, Vieluf 2025, Meisel 2020, Stirling 2021, Nasseri 2021)

---

## Part 9: Summary Matrix A - Paradigm × Modality × Performance

| Study | Paradigm | Modality | Personalization | Sens | FAR |
|-------|----------|----------|-----------------|------|-----|
| Spahr 2025 | End-to-end | Single | Global | 96% | <1/8d |
| Reintjes 2025 | End-to-end | Single | Global (LOSO) | 38-98% | 1.91-39.8/h |
| Fine 2025 | Feature-based | Single | Global | 100% | 0.023/h |
| Dong 2026 | Hybrid | Multi | Global | 71.6% | 0.165/h |
| Wang 2025 | Feature-based | Multi | Global | 56-95% | 8.5/24h |
| Singh 2024 | Feature-based | Multi | Global | 96.8% | -- |
| Elemam 2025 | End-to-end | Multi | Global | 95.1% | -- |
| Borujeny 2013 | Feature-based | Single | Global | 100% | 0 |
| Vieluf 2025 | Feature-based | Multi | Mixed | 82% | -- |
| Meisel 2020 | End-to-end | Multi | Global (LOSO) | 51.2% | TiW 43.7% |
| Stirling 2021 | Feature-based | Multi | Patient-specific | -- | AUC 0.74 |
| Nasseri 2021 | Hybrid | Multi | Patient-specific | AUC 0.75 | TiW 0.9-7.2h/d |
| Ode 2023 | End-to-end | Single | Global | 74% | 0.85/h |

**Key Observations:**
1. End-to-end approaches: 5/13 studies - mixed performance (51-96%)
2. Feature-based approaches: 5/13 studies - generally higher sensitivity (56-100%)
3. Hybrid approaches: 2/13 studies - moderate performance (AUC 0.75-0.82)
4. Multi-modal: 8/13 studies - no clear advantage over single-modal
5. LOSO validation: Only 2 studies (Reintjes, Meisel) - lower but more realistic performance

---

## Part 10: Architecture vs Performance Analysis

| Architecture | Count | Mean Sens | Best Sens | Mean FAR | Best FAR |
|--------------|-------|-----------|-----------|----------|----------|
| CNN | 5 | 84.3% | 100% | Variable | 0.023/h |
| LSTM | 3 | 68.7% | 82% | Variable | TiW 43.7% |
| Ensemble | 2 | -- | -- | -- | -- |
| Anomaly Detection | 2 | 56% | 74% | 0.85-39.8/h | 0.85/h |
| Attention | 1 | 74% | 74% | 0.85/h | 0.85/h |

**Note:** Sample sizes too small for statistical significance. LSTM shows lower performance in LOSO setting (Meisel).

---

## Part 11: Research Question Analysis

**Q: How do different deep learning architectures and biosignal modalities excluding EEG compare in their ability to achieve an optimal trade-off between sensitivity and false alarm rate for ambulatory seizure monitoring?**

### Preliminary Findings:

1. **Architecture-Performance Relationship:**
   - CNN-based approaches achieve highest sensitivities (96-100%) but with varying FAR
   - LSTM-based approaches show lower sensitivity in LOSO validation (51.2%)
   - Ensemble methods (Dong, Stirling) show good generalization
   - Anomaly detection approaches show promise (Ode: 74% sens, 0.85/h FAR)
   - No study uses transformer architecture or cross-modal attention

2. **Modality-Performance Relationship:**
   - Single-modal ACC: 96-100% sensitivity (Spahr, Fine)
   - Single-modal ECG: 38-98% (Reintjes) - wide range, responder-dependent
   - Multi-modal: 56-95% sensitivity - no clear advantage over single-modal
   - Cardiac modalities (ECG/PPG/HRV): useful for preictal detection

3. **Personalization Impact:**
   - LOSO validation: 51.2% sensitivity (Meisel) vs 96% in patient-inclusive (Spahr)
   - Patient-specific models: higher AUC (0.75-0.82) but limited generalizability
   - Only 2/13 studies use true LOSO validation

4. **Clinical Deployment Readiness:**
   - Real-time capable: 7/13 studies
   - On-device: Only 2/13 studies (Spahr, Borujeny partial)
   - Home validated: 5/13 studies (Dong, Vieluf, Stirling, Nasseri, Singh)
   - Power consumption: Only 2/13 studies report

5. **Performance Trade-off Configuration:**
   - Single operating point: 4/13 studies
   - Multiple operating points: 7/13 studies
   - Tunable/adaptive: Only 3/13 studies

---

## Gaps Identified for Future Research:

1. **No transformer-based architectures** for seizure detection/forecasting
2. **No cross-modal attention** mechanisms for multi-modal fusion
3. **Limited LOSO validation** - only 2 studies
4. **Power consumption rarely reported** - only 2 studies
5. **On-device processing rare** - only 1-2 studies
6. **Inconsistent metrics** - FAR units vary (per-hour, per-day, per-night)
