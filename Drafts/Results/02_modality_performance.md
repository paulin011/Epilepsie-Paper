# Modality Performance Analysis

**Date:** 2026-01-22
**Topic:** Biosignal Modality Usage and Performance Comparison

---

## Overview

This report analyzes the **13 epilepsy seizure detection and forecasting studies** to compare biosignal modality usage and performance. The analysis reveals clear trends in modality selection, sampling strategies, and effectiveness.

---

## Modality Usage Frequency

| Modality | Detection (n=8) | Forecasting (n=5) | Total | % of Studies |
|----------|-----------------|-------------------|-------|--------------|
| **ACC (Accelerometer)** | 6 | 3 | 9 | 69% |
| **EDA (Electrodermal)** | 2 | 3 | 5 | 38% |
| **ECG/HRV** | 2 | 3 | 5 | 38% |
| **PPG** | 2 | 2 | 4 | 31% |
| **Gyro** | 3 | 0 | 3 | 23% |
| **HR/Heart Rate** | 1 | 2 | 3 | 23% |
| **SEMG** | 2 | 0 | 2 | 15% |
| **Temperature** | 0 | 2 | 2 | 15% |
| **Audio** | 1 | 0 | 1 | 8% |

---

## Single vs Multi-modal Distribution

| Classification | Detection | Forecasting | Total | % |
|----------------|-----------|-------------|-------|---|
| **Multi-modal (M)** | 6 | 3 | 9 | 69% |
| **Single-modal (1)** | 2 | 2 | 4 | 31% |

**Key Finding:** 69% of studies use multiple modalities, suggesting that combining biosignals improves performance.

### Single-Modal Studies
| Study | Modality | Type | Performance |
|-------|----------|------|-------------|
| **Spahr 2025** | ACC only | Detection | 96% sens, 0.005/h FPR |
| **Reintjes 2025** | ECG only | Detection | 38-98% sens, 1.91-39.75/h FPR |
| **Borujeny 2013** | ACC only | Detection | 85% sens, 3 FA |
| **Ode 2023** | ECG (RRI) | Forecasting | 74% sens, 0.85/h FPR |

### Multi-Modal Studies
| Study | Modalities | Type | Performance |
|-------|------------|------|-------------|
| **Fine 2025** | ACC+Gyro | Detection | 100% sens, 0.023/h FPR |
| **Dong 2026** | ACC+PPG | Detection | 71.6% sens, 0.165/h FPR |
| **Wang 2025** | ACC+Gyro+SEMG+EDA | Detection | 56-95% sens, 0.354/h FPR |
| **Singh 2024** | EDA+ACC+HR | Detection | 96.8% sens |
| **Elemam 2025** | PPG (HRV)+Audio | Detection | 95.1% sens, 97.06% spec |
| **Vieluf 2025** | EDA+ACC+Temp | Forecasting | 82% sens, 67% spec |
| **Meisel 2020** | EDA+PPG+Temp+ACC | Forecasting | 51.2% sens, IoC 14.1% |
| **Stirling 2021** | HR+Sleep+Steps | Forecasting | AUC 0.74 |
| **Nasseri 2021** | ACC+PPG+EDA+Temp+HR | Forecasting | AUC 0.75 |

---

## Sampling Frequencies by Modality

### Accelerometer (ACC)
| Study | Frequency | Notes |
|-------|-----------|-------|
| **Spahr 2025** | 32 Hz | Euclidean norm, 30s windows |
| **Wang 2025** | 50 Hz | 3-axis, 4s windows |
| **Dong 2026** | 11-12 Hz → 20 Hz | Downsampled |
| **Fine 2025** | 6-axis (ACC+Gyro) | 10s intervals, 1s overlap |
| **Borujeny 2013** | 3 Hz | 2D accelerometer |

### ECG/HRV
| Study | Frequency | Notes |
|-------|-----------|-------|
| **Reintjes 2025** | 256 Hz → 8 Hz | Bandpass filtered |
| **Elemam 2025** | 250 Hz (PPG for HRV) | Camera-based |

### EDA
| Study | Frequency | Notes |
|-------|-----------|-------|
| **Wang 2025** | 4 Hz | Standard for EDA |
| **Meisel 2020** | 4 Hz | Resampled |
| **Nasseri 2021** | 4 Hz | Resampled |
| **Vieluf 2025** | 1 Hz | 24-h patterns |

**Key Finding:** Movement detection (ACC) uses higher frequencies (32-50 Hz), while physiological signals (ECG, EDA) work well at lower frequencies (1-4 Hz).

---

## Sensor Location Trends

| Location | Detection | Forecasting | Total | % |
|----------|-----------|-------------|-------|---|
| **Wrist** | 5 | 3 | 8 | 62% |
| **Arm** | 2 | 1 | 3 | 23% |
| **Chest** | 1 | 0 | 1 | 8% |
| **Thigh** | 1 | 0 | 1 | 8% |

**Key Finding:** Wrist-worn devices dominate (62%), likely due to patient acceptance and consumer wearable integration.

### Wrist-Worn Studies
| Study | Device | Modalities |
|-------|--------|------------|
| **Spahr 2025** | Empatica E4 | ACC |
| **Fine 2025** | 6-axis band | ACC+Gyro |
| **Wang 2025** | Biovital-P1 | ACC+Gyro+SEMG+EDA |
| **Vieluf 2025** | Embrace | EDA+ACC+Temp |
| **Meisel 2020** | Empatica E4 | EDA+PPG+Temp+ACC |
| **Nasseri 2021** | Empatica E4 | ACC+PPG+EDA+Temp+HR |
| **Stirling 2021** | Fitbit | HR+Sleep+Steps |
| **Ode 2023** | ECG patch | ECG |

---

## Performance by Modality Type

### Detection Studies Performance Comparison

| Modality Approach | Studies | Sensitivity Range | FPR Range | Best Performing |
|-------------------|---------|-------------------|-----------|-----------------|
| **ACC only** | 3 | 85-96% | 0.005-3 FA | Spahr 2025 |
| **ACC+Gyro** | 2 | 56-100% | 0.023-0.354/h | Fine 2025 |
| **ACC+PPG** | 1 | 71.6% | 0.165/h | Dong 2026 |
| **Multi-modal (3+)** | 2 | 56-96.8% | Variable | Singh 2024 |
| **ECG only** | 1 | 38-98% | 1.91-39.75/h | Reintjes 2025 |
| **PPG+Audio** | 1 | 95.1% | Not reported | Elemam 2025 |

**Key Finding:** Single-modality ACC (Spahr 2025) achieves excellent sensitivity (96%) with very low FPR (0.005/h), challenging the assumption that multi-modal is always superior.

### Forecasting Studies Performance Comparison

| Modality Approach | Studies | AUC Range | Sensitivity Range | Best Performing |
|-------------------|---------|-----------|-------------------|-----------------|
| **EDA+ACC+Temp** | 1 | - | 82% sens, 67% spec | Vieluf 2025 |
| **Full wrist (4+)** | 2 | 0.75 | 51.2% sens | Nasseri 2021 |
| **HR+Diary** | 1 | 0.74 | - | Stirling 2021 |
| **ECG (RRI) only** | 1 | - | 74% sens | Ode 2023 |

**Key Finding:** Forecasting performance shows narrower range (AUC 0.74-0.75) compared to detection, suggesting a performance ceiling for current approaches.

---

## Most Effective Modality Combinations

### 1. ACC + EDA + PPG (Nasseri 2021, Meisel 2020)
- **Advantages:** Captures both movement and autonomic nervous system activity
- **Performance:** AUC 0.75 (Nasseri), IoC 14.1% (Meisel)
- **Use case:** Forecasting with long-term patterns

### 2. ACC + Gyro (Fine 2025, Wang 2025)
- **Advantages:** Superior movement detection with orientation stability
- **Performance:** Up to 100% sensitivity in controlled settings
- **Use case:** Motor seizure detection

### 3. ACC only (Spahr 2025)
- **Advantages:** Simpler hardware, lower power, excellent FPR
- **Performance:** 96% sensitivity, 0.005/h FPR (best in review)
- **Use case:** Generalized convulsive seizures

---

## Novel Modality Approaches

| Modality | Study | Innovation | Performance |
|----------|-------|------------|-------------|
| **Camera PPG** | Elemam 2025 | Non-contact HRV from thumbs | 95.1% sens, 97.06% spec |
| **Attitude Angles** | Wang 2025 | PITCH/ROLL > raw ACC | Better than raw signals |
| **Audio Analysis** | Elemam 2025 | Seizure vocalization detection | 92.5% accuracy |
| **RRI only** | Ode 2023 | Self-attentive autoencoder | 74% sens, 0.85/h FPR |

---

## Clinical Implications

### For Detection
- **Multi-modal systems** (ACC+EDA+PPG) show best balance for general use
- **Single-modality ACC** achieves excellent results for convulsive seizures
- **Wrist-worn devices** are preferred for patient compliance

### For Forecasting
- **Heart rate cycles** and 24-hour patterns show predictive value
- **Patient-specific models** improve accuracy
- **Longer recording periods** enhance performance

### Practical Considerations
- Trade-off between modality count and system complexity
- Battery life considerations for multi-modal devices
- Data processing requirements for real-time detection

---

## Key Findings Summary

1. **Multi-modal advantage:** 69% of studies use multiple modalities
2. **Wrist dominance:** 62% use wrist location for patient acceptance
3. **ACC ubiquity:** 69% include accelerometer data
4. **ECG promise:** ECG/HRV shows strong forecasting potential
5. **Sampling trade-offs:** Higher frequencies (32-50 Hz) for movement, lower (1-4 Hz) for physiology
6. **Performance ceiling:** Forecasting AUC consistently 0.74-0.75

---

**End of Modality Performance Report**
