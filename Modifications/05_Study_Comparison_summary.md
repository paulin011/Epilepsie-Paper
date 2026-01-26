# Study Comparison Tables - Detailed Summary

**Source:** Tables in `/home/paulin/Documents/Epilepsie/Tables(tex)/`
- Table 1A: Detection Studies Overview
- Table 1B: Forecasting Studies Overview
- Table 2A: Detection Studies Architecture Deep-Dive
- Table 2B: Forecasting Studies Architecture Deep-Dive
- Table 3: Metrics Summary Across All Studies

---

## Overview: The 13 Studies

### Detection Studies (9 total)
1. **Spahr et al. 2025** - Ensemble 1D CNN (Empatica E4)
2. **Reintjes et al. 2025** - Anomaly detection via ECG
3. **Fine 2025** - Phase 1 study with 6-axis band
4. **Dong et al. 2026** - Two-stage CNN-LSTM + Attention (NightWatch)
5. **Wang et al. 2025** - LSTM with Biovital-P1 multi-sensor
6. **Singh Rathore 2024** - Case study with MLP
7. **Elemam et al. 2025** - CNN + rule-based fusion (camera PPG)
8. **Borujeny 2013** - KNN/ANN with MICAz accelerometer (earliest study)
9. **Ode et al. 2023** - Self-Attentive Autoencoder with ECG

### Forecasting Studies (4 total)
1. **Vieluf et al. 2025** - DNN + harmonic features (Embrace)
2. **Meisel et al. 2020** - LSTM with LOSO validation
3. **Stirling 2021** - Ensemble LSTM+RF+LR (Fitbit)
4. **Nasseri 2021** - 4-layer LSTM with temporal split

---

## Table 1A: Detection Studies - Overview Matrix

| Study | Design | Sample | Device | Location | Paradigm | Modality | Personalization | Algorithm | Sens | Spec | FPR |
|-------|--------|--------|--------|----------|----------|----------|-----------------|-----------|------|------|-----|
| **Spahr 2025** | Prospective | n=384, 49 CSs | Empatica E4 (ACC) | Wrist | Ensemble | 1 | Global | Ensemble 1D CNN (30 models) | 96% | -- | 0.0054/h |
| **Reintjes 2025** | Retro | n=120, 856 szs | Single-lead ECG | Chest | Anomaly | 1 | Subject split | Matrix Profile, MADRID, TimeVQVAE | 2.44-82.79% | -- | 0.11-65.62/h |
| **Fine 2025** | Phase 1 | n=15/3 | 6-axis band (ACC+Gyro) | Wrist | Feature-based | M | Global | ANN (594 features) | 100% Test, 96% complete | -- | 0.023/h |
| **Dong 2026** | Prospective | n=68, 1846 szs | NightWatch | Arm | Two-stage | M | Global | CNN-LSTM + Attention | 71.6% | -- | 0.165/h |
| **Wang 2025** | -- | n=28, 62 szs | Biovital-P1 | Wrist | Feature-based | M | Global | LSTM (40 hidden) | 56.40-95.3% | -- | 0.364/h |
| **Singh 2024** | Case study | 1 pt, 6 hrs | Wearable (EDA+ACC+HR) | -- | Feature-based | M | Case study | MLP | 96.8% | 94.8%* | -- |
| **Elemam 2025** | Cross-sect | Q:198, HRV:30 | Camera PPG | Thumbs | Hybrid | M | Global | CNN + Rule-based fusion | 95.1% Q, 93% HRV | 97.06% | -- |
| **Borujeny 2013** | 3-pt | 3 pts, 20 szs | MICAz ACC | Arm/thigh | Feature-based | 1 | Global | ANN (time-domain) | 85% | -- | 3 FA |

*Note: Singh Rathore reports precision, not specificity

---

## Table 1B: Forecasting Studies - Overview Matrix

| Study | Design | Sample | Device | Location | Paradigm | Modality | Personalization | Algorithm | Sens | Spec | FPR |
|-------|--------|--------|--------|----------|----------|----------|-----------------|-----------|------|------|-----|
| **Vieluf 2025** | Retro | n=70, 5437 d | Embrace | Wrist | Hybrid | M | Mixed | DNN + harmonic features + diary | 82% | 67% | -- |
| **Meisel 2020** | LOSO CV | n=69, 452 szs | Empatica E4 | Wrist/Ankle | E2E | M | Global | LSTM (10 units) | 51.2% | -- | TiW 43.7% |
| **Stirling 2021** | Retro+pseudo | n=11, 136 szs | Fitbit | Wrist | Feature-based | M | Patient-specific | LSTM+RF+LR ensemble | -- | -- | AUC 0.74 |
| **Nasseri 2021** | Retro | n=6 | Empatica E4 | Wrist | E2E | M | Temporal | LSTM 4-layer (128 hidden) | AUC 0.75 (SD 0.15) | -- | TiW 0.9-7.2h/d |
| **Ode 2023** | Retro | n=66, 85 szs | ECG | -- | Anomaly | 1 | Patient-specific | Self-Attentive AE | 74% | -- | 0.85/h |

---

## Table 2A: Detection Studies - Architecture Deep-Dive

| Study | Paradigm | Architecture Details | Modality Details | Fusion | Personalization | Trade-off Config | Deployment |
|-------|----------|---------------------|------------------|--------|-----------------|------------------|------------|
| **Spahr 2025** | Ensemble | 30 1D CNN models, 14 conv layers, quantile aggregation | ACC 32 Hz, Euclidean norm, 30 s windows | -- (single) | Global, tunable | 86-100% sens @ 0.0054/h | Real-time (112 ms), on-device |
| **Reintjes 2025** | Anomaly | Matrix-Profile, MADRID, TimeVQVAE-AD | ECG 256 to 8 Hz, bandpass filtered | -- (single) | Subject split | 2.44-82.79% @ 0.11-65.62/h | Offline, hospital |
| **Fine 2025** | Feature-based | ANN, 594 handcrafted features | ACC+Gyro 6-axis, 10 s intervals | Early fusion | Global, hold-out | 100% @ 0.023/h | Offline PC, EMU |
| **Dong 2026** | Two-stage | Pre-screening + CNN-LSTM + Attention | ACM 11-12 to 20 Hz, PPG 100 to 20 Hz, 5 min | Early fusion | Global, 10-fold CV | 71.6% @ 0.165/h | Real-time, NightWatch, home |
| **Wang 2025** | Feature-based | LSTM (40 hidden) + ReLU + FC | ACC/GYR 50 Hz, SEMG 200 Hz, EDA 4 Hz, 4 s | Early fusion | Global, hold-out | 56.4-95.3% @ 0.364/h | Real-time, hospital |
| **Singh 2024** | Feature-based | MLP, multi-modal features | EDA, ACC, HR/HRV, 25k points | Early fusion | Single pt (CS) | 96.8% sens @ 94.8% prec | Real-time, cloud? |
| **Elemam 2025** | CNN-based | CNN for HRV, CNN for Audio (separate) | PPG 250 Hz, Audio 10 s | No fusion (parallel) | Global, unclear | 95.1% @ 97.06% spec | Real-time, hospital |
| **Borujeny 2013** | Feature-based | ANN, time-domain features | ACC 2D 3 Hz, 9 s | -- (single) | Global, 3 pts | 85% @ 3 FA | Real-time, server (316 mW) |

---

## Table 2B: Forecasting Studies - Architecture Deep-Dive

| Study | Paradigm | Architecture Details | Modality Details | Fusion | Personalization | Trade-off Config | Deployment |
|-------|----------|---------------------|------------------|--------|-----------------|------------------|------------|
| **Vieluf 2025** | Hybrid | DNN + harmonic modeling (24-h) | EDA 4 Hz, ACC 32 Hz, Temp 1 Hz, 10 min | Early fusion | Mixed, 5-fold + LOO | 82% sens, 67% spec @ F1 0.81 | Offline MATLAB, home |
| **Meisel 2020** | End-to-end | LSTM only (10 units) | EDA/ACC/BVP/Temp to 4 Hz, 30 s | Early fusion | Global, LOSO | 51.2% @ IoC 14.1% | Offline, hospital |
| **Stirling 2021** | Feature-based | LSTM+RF+LR ensemble, LR combines | HR 5 s, steps/sleep 1 min, hourly/daily | Decision fusion | Patient-specific, weekly | AUC 0.74, 100% pts | Home (Fitbit), app |
| **Nasseri 2021** | End-to-end | LSTM 4-layer, 128 hidden + FFT channels | ACC/BVP/EDA/Temp/HR to 128 Hz, 60 s | Early fusion (17-ch) | Temporal split | AUC 0.75 (SD 0.15) @ TiW 0.9-7.2h/d | Offline, cloud, home |
| **Ode 2023** | Anomaly | Self-Attentive AE (attention mechanism) | ECG (RRI only), 45 s | -- (single) | Patient-specific (99% CL) | 74% @ 0.85/h (99% CL) | Real-time, cloud, hospital |

---

## Table 3: Metrics Summary - Reporting Frequency

| Metric | Detection (n=9) | Forecasting (n=4) | Reported By |
|--------|-----------------|-------------------|-------------|
| **Sensitivity/Recall** | 8/9 | 1/4 | Spahr, Reintjes, Fine, Dong, Wang, Singh Rathore, Elemam, Borujeny, Ode |
| **Specificity** | 3/9 | 0/4 | Elemam, Vieluf, Wang |
| **FPR/FA rate** | 8/9 | 0/4 | Spahr, Reintjes, Fine, Dong, Wang, Singh Rathore, Elemam, Borujeny, Nasseri, Ode |
| **AUC-ROC** | 3/9 | 3/4 | Dong, Reintjes, Ode, Nasseri, Stirling |
| **Detection Latency** | 4/9 | 1/4 | Spahr, Fine, Elemam, Borujeny, Nasseri |
| **Patient Success Rate** | 2/9 | 3/4 | Reintjes, Meisel, Stirling, Nasseri, Ode |
| **Precision/PPV** | 4/9 | 1/4 | Dong, Singh Rathore, Elemam, Ode |
| **IoC / Time in Warning** | 0/9 | 3/4 | Meisel, Stirling, Nasseri |

---

## Key Patterns Across Studies

### 1. Modality Distribution

**Detection Studies:**
- Single-modal (1): 4/9 (Spahr, Reintjes, Borujeny, Ode)
- Multi-modal (M): 5/9 (Fine, Dong, Wang, Singh Rathore, Elemam)

**Forecasting Studies:**
- Single-modal (1): 1/4 (Ode - ECG only)
- Multi-modal (M): 3/4 (Vieluf, Meisel, Stirling, Nasseri)

**Most common modalities:**
- ACC (accelerometer) - present in 8/13 studies
- ECG - present in 3/13 studies (Reintjes, Ode detection; Ode forecasting)
- EDA - present in 4/13 studies
- HR/HRV - present in 5/13 studies

### 2. Learning Paradigm Distribution

**Detection Studies:**
- Feature-based: 4/9 (Fine, Wang, Singh Rathore, Borujeny)
- Ensemble: 1/9 (Spahr)
- Two-stage: 1/9 (Dong)
- Anomaly: 2/9 (Reintjes, Ode)
- Hybrid: 1/9 (Elemam)
- CNN-based: 1/9 (Elemam - classified as both)

**Forecasting Studies:**
- End-to-end: 2/4 (Meisel, Nasseri)
- Feature-based: 1/4 (Stirling)
- Hybrid: 1/4 (Vieluf)
- Anomaly: 1/4 (Ode)

### 3. Personalization Approaches

**Detection Studies:**
- Global: 6/9 (Spahr, Fine, Dong, Wang, Elemam, Borujeny)
- Subject split: 1/9 (Reintjes)
- Case study: 1/9 (Singh Rathore)

**Forecasting Studies:**
- Patient-specific: 2/4 (Stirling, Ode)
- Global: 1/4 (Meisel)
- Temporal split: 1/4 (Nasseri)
- Mixed: 1/4 (Vieluf)

### 4. Device/Body Location Distribution

| Location | Detection | Forecasting | Total |
|----------|-----------|-------------|-------|
| Wrist | 4 | 3 | 7 |
| Arm | 2 | 0 | 2 |
| Chest | 1 | 0 | 1 |
| Thumbs | 1 | 0 | 1 |
| Ankle | 0 | 1 | 1 |
| Unspecified | 1 | 0 | 1 |

**Most common devices:**
- Empatica E4: 4 studies (Spahr, Meisel, Nasseri)
- NightWatch: 1 study (Dong)
- Fitbit: 1 study (Stirling)
- Embrace: 1 study (Vieluf)
- Custom/research devices: 6 studies

### 5. Performance Highlights

**Best Sensitivity (Detection):**
- Fine 2025: 100% (Test), 96% (complete) @ 0.023/h
- Spahr 2025: 96% @ 0.0054/h
- Singh Rathore 2024: 96.8% @ 94.8% precision

**Best FPR (Detection - lowest):**
- Spahr 2025: 0.0054/h (excellent)
- Fine 2025: 0.023/h (very good)
- Dong 2026: 0.165/h (clinically acceptable)
- ILAE Phase 3 benchmark: <0.05-0.1/h

**Widest Performance Range:**
- Reintjes 2025: 2.44-82.79% sensitivity @ 0.11-65.62/h FPR

**Forecasting AUC:**
- Stirling 2021: AUC 0.74
- Nasseri 2021: AUC 0.75 (SD 0.15)
- Ode 2023: 74% sensitivity @ 0.85/h

### 6. Deployment Settings

**Real-time capable:**
- Detection: Spahr (112 ms on-device), Dong (NightWatch home), Wang, Singh Rathore, Elemam, Borujeny
- Forecasting: Ode (real-time cloud)

**Offline only:**
- Reintjes, Fine (offline PC), Meisel (hospital), Nasseri (cloud), Stirling (home app), Vieluf (MATLAB)

### 7. Study Design Quality Indicators

**Sample sizes:**
- Large: Spahr (n=384), Reintjes (n=120), Vieluf (n=70, 5437 days), Meisel (n=69)
- Medium: Dong (n=68), Wang (n=28), Fine (n=15/3), Ode (n=66)
- Small: Singh Rathore (1 pt case study), Borujeny (3 pts), Nasseri (n=6), Stirling (n=11)

**Seizure counts:**
- Largest: Dong (1846 szs), Reintjes (856 szs), Meisel (452 szs)
- Smallest: Borujeny (20 szs), Wang (62 szs)

**Validation rigor:**
- LOSO: Meisel (forecasting), Reintjes (detection - subject split)
- Prospective: Spahr, Dong
- Temporal split: Nasseri

---

## Notable Contrasts and Comparisons

### Detection vs Forecasting

1. **Sensitivity vs Prediction Horizon**
   - Detection: Focus on high sensitivity (70-100%)
   - Forecasting: Lower sensitivity typical (51-82%) but predicts in advance

2. **Metrics Used**
   - Detection: Sensitivity, FPR, latency
   - Forecasting: AUC, Time in Warning, Improvement over Chance

3. **Real-time Requirements**
   - Detection: More critical for timely intervention
   - Forecasting: Can be offline but requires advance warning

4. **Modality Preferences**
   - Detection: More single-modal approaches (4/9)
   - Forecasting: Predominantly multi-modal (3/4)

### Algorithm Evolution (2013-2026)

- **2013 (Borujeny):** Simple ANN with time-domain features
- **2020-2021:** LSTM dominance for forecasting (Meisel, Nasseri, Stirling)
- **2023:** Attention mechanisms emerge (Ode)
- **2025-2026:** Ensemble and hybrid approaches (Spahr, Vieluf, Elemam, Dong)

### Global vs Patient-Specific

- Global models: More common (7/13), larger samples needed
- Patient-specific: Better individual performance but less scalable
- Mixed approaches: Emerging compromise (Vieluf, Stirling)

### Clinical Readiness (FPR <0.1/h)

**Meets threshold:**
- Spahr 2025: 0.0054/h
- Fine 2025: 0.023/h

**Borderline:**
- Dong 2026: 0.165/h

**Above threshold:**
- Wang 2025: 0.364/h
- Reintjes 2025: 0.11-65.62/h (wide range)
- Ode 2023: 0.85/h (forecasting context)

---

## Summary Observations

1. **Wrist-worn devices dominate** (7/13 studies), likely due to patient acceptance

2. **Multi-modal approaches are prevalent** (8/13), suggesting complementary information from different biosignals

3. **Feature-based learning remains common** (5/13), not fully supplanted by end-to-end deep learning

4. **Validation rigor varies widely**, from LOSO cross-validation to simple case studies

5. **FPR reporting is inconsistent** across studies, making direct comparisons challenging

6. **Only two detection studies achieve clinically acceptable FPR** (<0.1/h) while maintaining high sensitivity

7. **Forecasting studies report different metrics** (AUC, TiW, IoC) than detection studies, requiring separate evaluation frameworks

8. **Real-world deployment is limited** - most studies are hospital-based or offline analysis

9. **Sample sizes vary dramatically** (n=1 to n=384), affecting generalizability claims

10. **Algorithm diversity is high**, with no single dominant approach across all studies
