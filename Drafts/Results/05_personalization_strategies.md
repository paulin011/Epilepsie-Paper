# Personalization Strategies

**Date:** 2026-01-22
**Topic:** Global vs Patient-Specific Model Approaches

---

## Overview

Personalization strategy is a critical design choice in wearable seizure detection and forecasting systems. This report analyzes how **13 studies** approach model personalization and its impact on performance and generalizability.

---

## Personalization Strategy Distribution

| Strategy | Detection (n=8) | Forecasting (n=5) | Total | Definition |
|----------|-----------------|-------------------|-------|------------|
| **Global** | 4 | 1 | 5 | Population model, same for all patients |
| **Patient-specific** | 2 | 2 | 4 | Individual model trained per patient |
| **Mixed** | 0 | 1 | 1 | Combination of global and patient-specific |
| **Subject-split** | 1 | 0 | 1 | Train on one patient set, test on another |
| **Temporal** | 0 | 1 | 1 | Time-based split (early train, later test) |
| **Not specified / Case study** | 1 | 0 | 1 | Single patient or unclear |

---

## Global Models (n=5)

### Detection Studies

| Study | Sample | Validation | Performance | Notes |
|-------|--------|------------|-------------|-------|
| **Spahr 2025** | n=384 | Tunable, 10-fold | 96% sens, 0.005/h FPR | Largest global study |
| **Fine 2025** | n=15 training | Hold-out | 100% sens, 0.023/h FPR | Phase 1, small test |
| **Dong 2026** | n=68 | 10-fold CV | 71.6% sens, 0.165/h FPR | Global, tunable |
| **Elemam 2025** | Q:198 | Not specified | 95.1% sens, 97.06% spec | Cross-sectional |

### Forecasting Studies

| Study | Sample | Validation | Performance | Notes |
|-------|--------|------------|-------------|-------|
| **Meisel 2020** | n=69 | LOSO | 51.2% sens, IoC 14.1% | LOSO = global generalization test |

**Key Findings:**
- **Spahr 2025** demonstrates global model can achieve excellent FPR (0.005/h)
- **Meisel 2020** uses LOSO to test global generalization, achieving 62% patient success
- Global models benefit from larger training datasets

---

## Patient-Specific Models (n=4)

### Detection Studies

| Study | Approach | Sample | Performance | Notes |
|-------|----------|--------|-------------|-------|
| **Ode 2023** | 99% confidence level | n=66 | 74% sens, 0.85/h FPR | Anomaly detection per patient |
| **Singh 2024** | Single patient | 1 pt | 96.8% sens | Case study, limited generalizability |

### Forecasting Studies

| Study | Approach | Sample | Performance | Notes |
|-------|----------|--------|-------------|-------|
| **Stirling 2021** | Weekly retraining | n=11 | AUC 0.74, 100% success | HR cycles + diary |
| **Nasseri 2021** | Individual models | n=6 | AUC 0.75 (SD 0.15) | 5/6 above chance |

**Key Findings:**
- **Stirling 2021** achieves 100% patient success with weekly retraining
- Patient-specific models show higher individual success rates
- Requires sufficient data per patient for training

---

## Mixed / Hybrid Approaches (n=1)

| Study | Approach | Sample | Performance | Notes |
|-------|----------|--------|-------------|-------|
| **Vieluf 2025** | 5-fold + LOO | n=70 | 82% sens, 67% spec | DNN + harmonic features + diary |

**Key Finding:** Vieluf combines population patterns (24-h harmonic modeling) with individual diary data for forecasting.

---

## Subject-Split Validation (n=1)

| Study | Approach | Sample | Performance | Notes |
|-------|----------|--------|-------------|-------|
| **Reintjes 2025** | Train/test on different patients | n=120 | 38-98% sens, 1.91-39.75/h FPR | Tests generalization to new patients |

**Key Finding:** Subject-split validation reveals poor generalization for ECG anomaly detection methods.

---

## Temporal Split Validation (n=1)

| Study | Approach | Sample | Performance | Notes |
|-------|----------|--------|-------------|-------|
| **Nasseri 2021** | Early data train, later data test | n=6 | AUC 0.75 (SD 0.15) | Tests temporal stability |

**Key Finding:** Temporal split validation shows moderate AUC with high variability (SD 0.15).

---

## Performance by Personalization Strategy

### Detection Performance

| Strategy | Studies | Sensitivity Range | FPR Range | Best Performer |
|----------|---------|-------------------|-----------|----------------|
| **Global** | 4 | 71.6-100% | 0.005-0.354/h | Spahr 2025 |
| **Patient-specific** | 2 | 74-96.8% | 0.85/h, N/A | Singh 2024 (case study) |
| **Subject-split** | 1 | 38-98% | 1.91-39.75/h | Reintjes 2025 |

### Forecasting Performance

| Strategy | Studies | AUC Range | Patient Success | Best Performer |
|----------|---------|-----------|-----------------|----------------|
| **Global (LOSO)** | 1 | - | 43/69 (62%) | Meisel 2020 |
| **Patient-specific** | 2 | 0.74 | 91-100% | Stirling 2021 |
| **Mixed** | 1 | - | Not specified | Vieluf 2025 |
| **Temporal** | 1 | 0.75 (SD 0.15) | 5/6 (83%) | Nasseri 2021 |

**Key Finding:** Patient-specific models achieve higher individual success rates but require per-patient training data.

---

## Generalizability Analysis

### Leave-One-Subject-Out (LOSO) Results

| Study | Patient Success Rate | Performance |
|-------|---------------------|-------------|
| **Meisel 2020** | 43/69 (62%) | IoC 14.1%, TiW 43.7% |

**Interpretation:** LOSO validation reveals the real-world generalizability challenge. Only 62% of patients achieve better-than-chance forecasting with a global model.

### Patient Success Rates by Strategy

| Strategy | Success Rate | Studies |
|----------|--------------|---------|
| **Patient-specific** | 91-100% | Stirling 2021, Nasseri 2021 |
| **Temporal split** | 83% (5/6) | Nasseri 2021 |
| **LOSO (global)** | 62% (43/69) | Meisel 2020 |

**Key Finding:** Patient-specific approaches achieve substantially higher individual success than global models.

---

## Training Data Requirements

### Global Models

| Study | Training Data | Notes |
|-------|---------------|-------|
| **Spahr 2025** | 384 patients, 49 CSs (test) | Largest dataset |
| **Dong 2026** | 68 patients, 1846 seizures | High seizure count |
| **Meisel 2020** | 69 patients, 452 seizures | Multimodal wrist data |

### Patient-Specific Models

| Study | Data per Patient | Notes |
|-------|------------------|-------|
| **Stirling 2021** | Mean 14.6 months | Weekly retraining required |
| **Nasseri 2021** | 60+ days | Concurrent iEEG validation |
| **Ode 2023** | 85 seizures total | ~1-2 seizures per patient |

**Key Finding:** Patient-specific models require longer individual monitoring periods (weeks to months) to accumulate sufficient training data.

---

## Computational Considerations

### Global Models

| Study | Deployment | Inference Time |
|-------|------------|----------------|
| **Spahr 2025** | On-device | 112 ms |
| **Dong 2026** | Real-time armband | Not specified |
| **Fine 2025** | Offline PC | Not specified |

### Patient-Specific Models

| Study | Deployment | Retraining |
|-------|------------|------------|
| **Stirling 2021** | Smartphone app | Weekly |
| **Nasseri 2021** | Cloud processing | Not specified |

**Key Finding:** Global models enable on-device deployment, while patient-specific models often require cloud processing for frequent retraining.

---

## Personalization Trade-offs

| Aspect | Global | Patient-Specific |
|--------|--------|------------------|
| **Initial performance** | Moderate | Variable (needs data) |
| **Long-term performance** | Stable | Improves with more data |
| **Generalizability** | Better to new patients | Poor to new patients |
| **Deployment** | On-device possible | Often requires cloud |
| **Training data** | Large dataset | Individual longitudinal data |
| **Patient success rate** | 62% (LOSO) | 83-100% |

---

## Key Personalization Findings

1. **Success rate advantage:** Patient-specific models achieve 83-100% individual success vs 62% for global (LOSO)
2. **Data requirement:** Patient-specific models need weeks-months of individual data
3. **Deployment complexity:** Global models enable on-device inference; patient-specific often requires cloud
4. **Mixed approach potential:** Vieluf 2025 combines population patterns with individual data
5. **Weekly retraining:** Stirling 2021 demonstrates effective periodic personalization strategy
6. **Validation mismatch:** Most detection studies use global models with k-fold validation, not assessing individual patient performance

---

## Recommendations from Findings

1. **For detection:** Global models (Spahr 2025) can achieve excellent FPR for population deployment
2. **For forecasting:** Patient-specific or hybrid approaches show higher individual success
3. **Validation gap:** More detection studies should report patient-level success rates
4. **Personalization strategy:** Should be chosen based on clinical use case and deployment constraints

---

**End of Personalization Strategies Report**
