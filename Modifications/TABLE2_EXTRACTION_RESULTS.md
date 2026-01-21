# Table 2 Extraction Results: Architecture and Modality Deep-Dive

**For Review:** Verify all extracted data before implementing Table 2.

---

## Summary of Columns Extracted

| Column | Status | Notes |
|--------|--------|-------|
| Paradigm | ✅ Extracted | Conflicts marked in TABLE1_EXTRACTION_RESULTS.md |
| Arch. Details | ✅ Extracted | Anomaly detection, attention, ensemble details |
| Modality Details | ✅ Extracted | Signals, sampling frequency, processing, window |
| Fusion Type | ✅ Extracted | Stage and method for multi-modal studies |
| Personalization | ✅ Existing | From DL_COMPARISON_EXTRACTION_RESULTS.md |
| Trade-off Config | ✅ Extracted | Operating points, optimization target, threshold |
| Deployment | ✅ Extracted | Real-time, on-device, power, setting |

---

## Complete Extraction Table

| Study | Paradigm | Arch. Details | Modality Details | Fusion | Personalization | Trade-off Config | Deployment |
|-------|----------|---------------|------------------|--------|-----------------|------------------|------------|
| **Spahr 2025** | E2E | Ensemble: 30 1D CNN models, 14 conv layers | ACC 32 Hz, Euclidean norm, 30s window | -- | Global, patient-independent (347 test) | Tunable: 86-100% @ 0.01-0.5/day | Real-time (112ms), on-device (TicWatch), EMU |
| **Reintjes 2025** | E2E | Anomaly: Matrix Profile, MADRID, TimeVQVAE-AD | ECG 256→8 Hz, bandpass, 96s window | -- | Global, LOSO validation | Multi: 38-98% @ 1.9-40/h (sens/FAR/HMS opt) | Offline, prototype, hospital |
| **Fine 2025** | Feat | ANN, 594 handcrafted features | ACC+gyro, 10s intervals, 1s overlap | -- | Global, hold-out (3 test) | Single: 100% @ 0.023/h | Offline PC, prototype, EMU |
| **Dong 2026** | Hyb | CNN-LSTM + Attention | ACM 11-12→20 Hz, PPG 100→20 Hz, 5min window | Early (feature-level) | Global, 10-fold CV | Single: 71.6% @ 0.165/h (sens-opt) | Real-time, on-device (NightWatch), home |
| **Wang 2025** | Feat | LSTM + SVM/LDA (2-stage) | ACC/GYR 50 Hz, SEMG 200 Hz, EDA 4 Hz, 4s window | Early (feature concat) | Global, hold-out | Multiple: F1-opt @ 0.5 threshold | Real-time, hybrid (phone), hospital |
| **Singh 2024** | Feat | MLP, 594 extracted features | EDA, ACC (x,y,z,mag), raw, 25k points | Early (feature-level) | Global, single-pt train/test | Single: 96.8% sens, 94.8% prec | Real-time (designed), cloud?, research |
| **Elemam 2025** | Hyb | CNN + Rule-based fusion | PPG 250 Hz, Audio 10s, bandpass 0.5-40 Hz | Decision (parallel models) | Global, unclear split | Single: 95.1% sens @ 97.1% spec | Real-time, hybrid (PC/mobile), hospital |
| **Borujeny 2013** | Feat | KNN k=5, time-domain features | ACC 2D 3 Hz, 9s window | -- | Global, same-patient (3 pt) | Multi (K=1,3,5): 57-100% @ 0-15% | Real-time alarm, server (316 mW), lab |
| **Vieluf 2025** | Feat | DNN, harmonic modeling, 24-h patterns | EDA 4 Hz, ACC 32 Hz, Temp 1 Hz, 10min windows | Early (neural network) | Mixed, 5-fold + leave-one-out | Single: 82% sens, 67% spec @ F1 0.81 | Offline, MATLAB, home, Embrace |
| **Meisel 2020** | E2E | LSTM + 1D Conv (10 units) | EDA/ACC/BVP/Temp →4 Hz, raw, 30s window | Early (multi-channel) | Global, LOSO (68 train, 1 test) | Single: 51.2% @ IoC 14.1% | Offline, research, hospital |
| **Stirling 2021** | Feat | LSTM+RF+LR ensemble | HR 5s res, steps/sleep 1min, hourly/daily | Decision (ensemble averaging) | Patient-specific, temporal split | Multiple: AUC 0.74, adaptive thresholds | Home (Fitbit), phone app, research |
| **Nasseri 2021** | Hyb | LSTM 4-layer, 128 hidden, +FFT channels | ACC/BVP/EDA/Temp/HR →128 Hz, 60s window | Early (17-channel input) | Patient-specific, temporal split | Single: AUC 0.75 @ TiW 0.9-7.2h/d | Offline, cloud upload, home |
| **Ode 2023** | E2E | Self-Attentive AE (anomaly + attention) | ECG RRI only, raw, 45s window | -- | Global, hold-out (interictal train) | Single: 74% sens @ 0.85/h (99% CL) | Real-time (Alg 2), cloud, hospital |

---

## Detailed Extraction by Column

### Column 1: Paradigm (Learning Approach)

| Study | Paradigm | Evidence Summary |
|-------|----------|------------------|
| Spahr 2025 | End-to-end | 1D CNN learns from amplitude time series |
| Reintjes 2025 | End-to-end | Anomaly methods operate directly on ECG, no handcrafted features |
| Fine 2025 | Feature-based | 594 handcrafted features (mean, variance, SD) |
| Dong 2026 | Hybrid | Raw signals → features → DL model |
| Wang 2025 | Feature-based | Time/freq/nonlinear features extracted |
| Singh 2024 | Feature-based | 594 extracted features from multimodal data |
| Elemam 2025 | Hybrid | CNN + rule-based fusion |
| Borujeny 2013 | Feature-based | Time-domain features (variance, correlation, energy) |
| Vieluf 2025 | Feature-based | Harmonic modeling + diary features |
| Meisel 2020 | End-to-end | No feature engineering, LSTM learns from raw |
| Stirling 2021 | Feature-based | HRV features (RCH, RHR, steps, sleep) |
| Nasseri 2021 | Hybrid | Signals + FFT channels + SQI |
| Ode 2023 | End-to-end | Self-attentive AE on raw RRI |

**Legend:** Feat = Feature-based (handcrafted features), E2E = End-to-end (learns from raw), Hyb = Hybrid

---

### Column 2: Architecture Details

| Study | Anomaly Detection | Attention | Ensemble | Secondary Architecture |
|-------|-------------------|-----------|----------|------------------------|
| Spahr 2025 | No | No | Yes (30 models, 10 best used) | 1D CNN, 14 conv layers |
| Reintjes 2025 | Yes (3 methods) | No | No | Matrix Profile, MADRID, TimeVQVAE |
| Fine 2025 | No | No | No | ANN with 6-axis motion input |
| Dong 2026 | No | Yes (dynamic weights) | No | CNN-LSTM hybrid |
| Wang 2025 | No | No | No | LSTM + SVM/LDA (2-stage) |
| Singh 2024 | No | No | No | MLP, multi-layer neural network |
| Elemam 2025 | No | No | No | CNN + rules |
| Borujeny 2013 | No | No | No | ANN + KNN k=5 |
| Vieluf 2025 | No | No | No | FCNN with several hidden layers |
| Meisel 2020 | No | No | No | LSTM (10 units) + 1D Conv |
| Stirling 2021 | No | No | Yes (LSTM+RF+LR) | LSTM, Random Forest, Logistic Regression |
| Nasseri 2021 | No | No | No | 4 LSTM layers, 128 hidden nodes |
| Ode 2023 | Yes (autoencoder) | Yes (self-attention) | No | Self-Attentive AE (SA-AE) |

---

### Column 3: Modality Details

| Study | Signals | Sampling Freq | Processing | Window |
|-------|---------|--------------|------------|--------|
| Spahr 2025 | ACC (3D→amplitude) | 32 Hz | Euclidean norm, raw | 30 s |
| Reintjes 2025 | ECG single-lead | 256→8 Hz | Bandpass 0.5-40 Hz | 96 s |
| Fine 2025 | ACC + gyroscope | N/A | 594 features, 10s intervals | 10 s (1s overlap) |
| Dong 2026 | ACM + PPG | ACM: 11-12→20 Hz, PPG: 100→20 Hz | Butterworth filters | 5 min |
| Wang 2025 | ACC, GYR, PITCH, ROLL, SEMG, EDA | ACC/GYR: 50 Hz, SEMG: 200 Hz, EDA: 4 Hz | Median/bandpass filters | 4 s (50% overlap) |
| Singh 2024 | EDA, ACC (x,y,z,mag) | N/A | Raw | 25,000 points |
| Elemam 2025 | PPG, Audio | 250 Hz | Bandpass 0.5-40 Hz | 10 s (audio) |
| Borujeny 2013 | ACC 2D | 3 Hz | Moving average, FFT features | 9 s (50 samples) |
| Vieluf 2025 | EDA, ACC, Temp | EDA: 4 Hz, ACC: 32 Hz, Temp: 1 Hz | 24-h harmonic modeling | 10 min windows |
| Meisel 2020 | EDA, ACC, BVP, Temp | All →4 Hz | Raw (Chebyshev antialiasing) | 30 s (nonoverlapping) |
| Stirling 2021 | HR, steps, sleep | HR: 5s res, steps/sleep: 1min | Features (RCH, RHR, cyclic) | Hourly/Daily |
| Nasseri 2021 | ACC, BVP, EDA, Temp, HR | →128 Hz upsampled | FFT + time series | 60 s |
| Ode 2023 | ECG (RRI only) | N/A | Raw | 45 s |

---

### Column 4: Fusion Type

| Study | Modality Count | Fusion Stage | Fusion Method |
|-------|---------------|--------------|---------------|
| Spahr 2025 | Single | -- | N/A |
| Reintjes 2025 | Single | -- | N/A |
| Fine 2025 | Single | -- | N/A |
| Dong 2026 | Multi | Early | Feature extraction + concatenation |
| Wang 2025 | Multi | Early | Feature concatenation |
| Singh 2024 | Multi | Early | Feature-level fusion |
| Elemam 2025 | Multi | Decision | Parallel independent models |
| Borujeny 2013 | Single | -- | N/A |
| Vieluf 2025 | Multi | Early | Neural network input |
| Meisel 2020 | Multi | Early | Multi-channel input (120 points) |
| Stirling 2021 | Multi | Decision | Ensemble averaging (LR combines LSTM+RF) |
| Nasseri 2021 | Multi | Early | 17-channel input (signals + FFT) |
| Ode 2023 | Single | -- | N/A |

**Legend:** Early = signals combined before/at feature level, Decision = classifier outputs combined

---

### Column 5: Personalization

| Study | Model Scope | Validation | Test Patient in Training |
|-------|-------------|------------|-------------------------|
| Spahr 2025 | Global | Patient-independent (347 test separate) | No |
| Reintjes 2025 | Global | LOSO | No |
| Fine 2025 | Global | Hold-out (3 test separate) | No |
| Dong 2026 | Global | 10-fold CV, subject-independent | No |
| Wang 2025 | Global | Hold-out (IDs 1-18 train, 19-28 test) | No |
| Singh 2024 | Global (single pt) | Train/test split same patient | Yes |
| Elemam 2025 | Global | Unclear | Unclear |
| Borujeny 2013 | Global | Same-patient (3 pts) | Yes |
| Vieluf 2025 | Mixed | 5-fold + leave-one-out | Mixed |
| Meisel 2020 | Global | LOSO (68 train, 1 test) | No |
| Stirling 2021 | Patient-specific | Temporal hold-out | Yes |
| Nasseri 2021 | Patient-specific | Temporal split (1/3 train, 2/3 test) | Yes |
| Ode 2023 | Global | Hold-out (interictal train, preictal test) | Yes |

**Legend:** Global = population model, Patient-specific = individualized, Mixed = combination

---

### Column 6: Trade-off Configuration

| Study | Operating Points | Optimization Target | Threshold Strategy | Best Config |
|-------|------------------|---------------------|-------------------|-------------|
| Spahr 2025 | Tunable (quantile) | Balanced (HMS) | Adaptive (q=60) | 96% @ <1/8 days |
| Reintjes 2025 | Multiple | Sens/FAR/HMS | ROC-based | 98% @ 14/h (sens-opt) to 38% @ 2/h (FAR-opt) |
| Fine 2025 | Single | Sensitivity (100%) | Fixed (0.1g threshold) | 100% @ 0.023/h |
| Dong 2026 | Single | Sensitivity | Fixed (ROC-based) | 71.6% @ 0.165/h |
| Wang 2025 | Multiple | F1/Balanced | Adaptive (confidence) | M3-0.6 @ 28.9-35.7% speedup |
| Singh 2024 | Single | Accuracy/Precision/Recall | Fixed (0.5 threshold) | 96.8% sens @ 94.8% prec |
| Elemam 2025 | Single | Balanced | Fixed (0.65 threshold) | 95.1% sens @ 97.1% spec |
| Borujeny 2013 | Multiple (K=1,3,5) | Sens @ FAR | Fixed (K parameter) | 100% sens @ 0% FAR (K=5) |
| Vieluf 2025 | Single | Balanced (F1) | Fixed | 82% sens, 67% spec @ F1 0.81 |
| Meisel 2020 | Single | IoC | Fixed | 51.2% sens @ IoC 14.1% |
| Stirling 2021 | Multiple | Balanced (4 criteria) | Adaptive (weekly retraining) | AUC 0.74 (hourly) |
| Nasseri 2021 | Single | AUC | Fixed | AUC 0.75 @ TiW 0.9-7.2h/d |
| Ode 2023 | Single | Balanced | Fixed (99% CL, 8s threshold) | 74% sens @ 0.85/h |

**Legend:** HMS = Harmonic Mean Score, IoC = Improvement over Chance, TiW = Time in Warning, CL = Confidence Limit

---

### Column 7: Deployment

| Study | Real-time | On-device | Power Reported | Device Type | Setting |
|-------|-----------|-----------|----------------|-------------|---------|
| Spahr 2025 | Yes (112ms) | Yes (TicWatch) | No | Research | EMU |
| Reintjes 2025 | Unknown | Hybrid (Sensor Dot) | No | Prototype | Hospital |
| Fine 2025 | No (offline PC) | No | Unknown | Prototype | EMU |
| Dong 2026 | Yes | Yes (NightWatch armband) | No | Commercial | Home |
| Wang 2025 | Yes | Hybrid (watch + phone) | No | Research | Hospital |
| Singh 2024 | Yes (designed for) | Unknown | No | Research | Unknown |
| Elemam 2025 | Yes | Hybrid (PC/mobile/phone) | No | Research | Hospital |
| Borujeny 2013 | Yes (alarm) | Server (base station) | Yes (316 mW) | Prototype | Lab |
| Vieluf 2025 | No (MATLAB offline) | On-device (Embrace) | No | Research | Home |
| Meisel 2020 | Unknown | Cloud | Yes | Research | Hospital |
| Stirling 2021 | Unknown | Phone (Seer App) | No | Research | Home |
| Nasseri 2021 | Unknown | Cloud (tablet upload) | No | Research | Home |
| Ode 2023 | Yes (designed for) | Cloud | No | Research | Hospital |

---

## Summary Statistics

### Paradigm Distribution
- Feature-based: 5 studies (38%)
- End-to-end: 4 studies (31%)
- Hybrid: 4 studies (31%)

### Modality Count
- Single-modal: 5 studies (38%)
- Multi-modal: 8 studies (62%)

### Personalization
- Global: 9 studies (69%)
- Patient-specific: 2 studies (15%)
- Mixed: 2 studies (15%)

### Real-time Capability
- Yes: 7 studies (54%)
- No/Unknown: 6 studies (46%)

### On-device Processing
- Yes (on wearable): 3 studies (23%)
- Hybrid: 4 studies (31%)
- Cloud/Server: 6 studies (46%)

---

## Conflicts to Resolve

1. **Spahr 2025 Paradigm**: E2E vs Feature-based (Euclidean norm preprocessing)
   - **Recommendation**: E2E (CNN learns from amplitude, not handcrafted features)

2. **Elemam 2025 Paradigm**: E2E vs Hybrid (CNN + rules)
   - **Recommendation**: Hybrid (rule-based fusion confirms hybrid)

3. **Nasseri 2021 Paradigm**: E2E vs Hybrid (signals + FFT)
   - **Recommendation**: Hybrid (FFT channels are engineered features)

---

**Ready for implementation after review.**
