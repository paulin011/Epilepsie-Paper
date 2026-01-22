# Architecture and Algorithm Patterns

**Date:** 2026-01-22
**Topic:** Deep Learning Approaches for Seizure Detection and Forecasting

---

## Overview

This report analyzes the **deep learning architectures** and algorithmic paradigms used across **13 studies** on wearable seizure detection and forecasting. The analysis reveals distinct approaches between detection and forecasting tasks, with varying levels of model complexity and validation rigor.

---

## Learning Paradigm Distribution

| Paradigm | Detection (n=8) | Forecasting (n=5) | Total | Definition |
|----------|-----------------|-------------------|-------|------------|
| **Feature-based** | 3 | 1 | 4 | Handcrafted features + classifier |
| **End-to-end (E2E)** | 0 | 2 | 2 | Raw data → DL directly |
| **Hybrid** | 1 | 1 | 2 | Combines DL + handcrafted features |
| **Ensemble** | 1 | 0 | 1 | Multiple models aggregated |
| **Two-stage** | 1 | 0 | 1 | Pre-processing + DL |
| **Anomaly detection** | 1 | 1 | 2 | Unsupervised anomaly detection |
| **Not specified (traditional)** | 1 | 0 | 1 | ANN/KNN on time-domain features |

---

## Detection Study Architectures

### Feature-based Approaches (n=3)

| Study | Features | Classifier | Performance | Notes |
|-------|----------|------------|-------------|-------|
| **Fine 2025** | 594 handcrafted from 6-axis ACC+Gyro | ANN | 100% sens, 0.023/h FPR | Phase 1, small test set |
| **Wang 2025** | Attitude angles (PITCH/ROLL) | LSTM (40 hidden) | 56-95% sens, 0.354/h FPR | Angles outperform raw ACC |
| **Singh 2024** | EDA+ACC+HR features | MLP | 96.8% sens, 94.8% prec | Single-patient case study |

### End-to-end / Deep Approaches (n=4)

| Study | Architecture | Details | Performance | Notes |
|-------|--------------|---------|-------------|-------|
| **Spahr 2025** | Ensemble 1D CNN | 30 models, 14 conv layers, quantile aggregation | 96% sens, 0.005/h FPR | Best FPR in review |
| **Dong 2026** | CNN-LSTM + Attention | Two-stage: pre-screening + DL | 71.6% sens, 0.165/h FPR | 81% data reduction |
| **Elemam 2025** | Dual CNN | Separate CNNs for HRV and audio | 95.1% sens, 97.06% spec | No fusion between CNNs |
| **Reintjes 2025** | Anomaly (3 methods) | Matrix Profile, MADRID, TimeVQVAE-AD | 38-98% sens, 1.91-39.75/h FPR | Wide performance range |

### Traditional / Early DL (n=1)

| Study | Architecture | Details | Performance | Notes |
|-------|--------------|---------|-------------|-------|
| **Borujeny 2013** | ANN | Time-domain features from 2D ACC | 85% sens, 3 FA | Earliest study, 3 patients |

---

## Forecasting Study Architectures

### End-to-end Approaches (n=2)

| Study | Architecture | Details | Performance | Notes |
|-------|--------------|---------|-------------|-------|
| **Meisel 2020** | LSTM | 10 units only | 51.2% sens, IoC 14.1% | LOSO validation |
| **Nasseri 2021** | LSTM | 4-layer, 128 hidden + FFT channels | AUC 0.75, TiW 0.9-7.2h/d | Temporal split validation |

### Feature-based / Hybrid (n=3)

| Study | Architecture | Details | Performance | Notes |
|-------|--------------|---------|-------------|-------|
| **Vieluf 2025** | DNN + harmonic features | 24-h harmonic modeling | 82% sens, 67% spec | Diary integration |
| **Stirling 2021** | LSTM+RF+LR ensemble | RCH (Rate of Change in HR) features | AUC 0.74, 100% patient success | Weekly retraining |
| **Ode 2023** | Self-Attentive AE | RRI only, 45s windows | 74% sens, 0.85/h FPR | Patient-specific (99% CL) |

---

## Architecture Complexity Trends

### Model Size Comparison

| Study | Parameters/Complexity | Paradigm | Performance |
|-------|----------------------|----------|-------------|
| **Spahr 2025** | 30 CNN models × 14 layers | Ensemble | 96% sens, 0.005/h FPR |
| **Nasseri 2021** | 4-layer LSTM, 128 hidden | E2E | AUC 0.75 |
| **Meisel 2020** | LSTM, 10 units | E2E | 51.2% sens |
| **Wang 2025** | LSTM, 40 hidden | Feature-based | 56-95% sens |
| **Fine 2025** | ANN + 594 features | Feature-based | 100% sens |
| **Ode 2023** | Self-attentive AE | Anomaly | 74% sens |

**Key Finding:** More complex models (30 CNN ensemble) do not necessarily outperform simpler approaches (single-modality ACC with moderate CNN).

---

## Input Representations

| Input Type | Detection | Forecasting | Total |
|------------|-----------|-------------|-------|
| **Handcrafted features** | 3 | 2 | 5 |
| **Raw time-series** | 3 | 2 | 5 |
| **Hybrid (features + raw)** | 1 | 1 | 2 |
| **Spectrograms/FFT** | 0 | 1 | 1 |

### Window Sizes
| Study | Window Size | Overlap | Purpose |
|-------|-------------|---------|---------|
| **Spahr 2025** | 30 s | Not specified | Detection |
| **Dong 2026** | 5 min | Not specified | Detection |
| **Wang 2025** | 4 s | Not specified | Detection |
| **Fine 2025** | 10 s | 1 s | Detection |
| **Nasseri 2021** | 60 s | Not specified | Forecasting |
| **Ode 2023** | 45 s | Not specified | Forecasting |
| **Meisel 2020** | 30 s | Not specified | Forecasting |

---

## Detection vs Forecasting Architecture Differences

| Aspect | Detection | Forecasting |
|--------|-----------|-------------|
| **Paradigm preference** | Feature-based, Ensemble | E2E, Hybrid |
| **Model complexity** | Higher (ensemble, two-stage) | Moderate (LSTM variants) |
| **Input window** | Shorter (4s-5min) | Longer (30s-60s) |
| **Real-time requirement** | Critical (latency matters) | Less critical |
| **Output** | Binary (seizure/no seizure) | Probability/risk level |

---

## Ensemble Methods

| Study | Ensemble Type | Size | Aggregation | Performance |
|-------|---------------|------|-------------|-------------|
| **Spahr 2025** | 1D CNN | 30 models | Quantile | 96% sens, 0.005/h FPR |
| **Stirling 2021** | LSTM+RF+LR | 3 models | LR combines | AUC 0.74 |
| **Dong 2026** | Two-stage | Pre-screen + DL | Sequential | 71.6% sens, 0.165/h FPR |
| **Reintjes 2025** | Anomaly methods | 3 methods | Compared | 38-98% sens |

**Key Finding:** Spahr's 30-model ensemble achieves the best FPR (0.005/h) but requires substantial computational resources for training.

---

## Anomaly Detection Approaches

| Study | Method | Signal | Performance |
|-------|--------|--------|-------------|
| **Reintjes 2025** | TimeVQVAE-AD | ECG | Highest sensitivity (98.16%) |
| **Reintjes 2025** | MADRID | ECG | Lowest FPR (1.91/h) |
| **Reintjes 2025** | Matrix Profile | ECG | Intermediate |
| **Ode 2023** | Self-Attentive AE | ECG (RRI) | 74% sens, 0.85/h FPR |

**Key Finding:** Anomaly detection on ECG shows wide performance range, with significant sensitivity-FPR trade-offs.

---

## Temporal Evolution (2013-2026)

| Period | Dominant Paradigm | Example Studies |
|--------|-------------------|-----------------|
| **2013-2015** | Traditional ML (ANN, KNN) | Borujeny 2013 |
| **2020-2022** | LSTM-based forecasting | Meisel 2020, Nasseri 2021, Stirling 2021 |
| **2023-2026** | Advanced ensembles and hybrids | Spahr 2025, Dong 2026, Reintjes 2025 |

**Trend:** Evolution from simple ANN/KNN approaches to sophisticated ensemble methods and hybrid architectures.

---

## Key Architectural Findings

1. **Feature-based remains competitive:** 3/8 detection studies use handcrafted features with strong results
2. **Ensemble advantage:** Spahr's 30-model CNN ensemble achieves best FPR but high complexity
3. **LSTM dominance in forecasting:** All E2E forecasting studies use LSTM variants
4. **Anomaly detection niche:** ECG-based anomaly detection shows promise but high FPR variability
5. **Two-stage efficiency:** Dong's pre-screening reduces data by 81% without sacrificing performance
6. **Hybrid emerging:** Combining DL with handcrafted features (Vieluf, Stirling) shows promise

---

## Validation by Architecture Type

| Paradigm | LOSO Validation | Temporal Split | K-fold | Hold-out |
|----------|-----------------|----------------|--------|----------|
| **Feature-based** | 0 | 0 | 1 | 2 |
| **E2E** | 1 | 1 | 1 | 0 |
| **Hybrid** | 1 | 0 | 1 | 0 |
| **Ensemble** | 0 | 0 | 1 | 0 |
| **Anomaly** | 0 | 0 | 0 | 2 |

**Key Finding:** Only Meisel 2020 uses LOSO validation, the most rigorous for generalizability assessment.

---

**End of Architecture Patterns Report**
