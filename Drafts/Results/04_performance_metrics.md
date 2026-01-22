# Performance Metrics Synthesis

**Date:** 2026-01-22
**Topic:** Quantitative Performance Analysis Across Detection and Forecasting Studies

---

## Overview

This report synthesizes **performance metrics** reported across **13 studies** on wearable seizure detection and forecasting. Detection and forecasting studies use different evaluation metrics, reflecting their distinct clinical objectives.

---

## Detection Studies Metrics (n=8)

### Sensitivity Summary

| Study | Sensitivity | Seizure Type | Sample Size |
|-------|-------------|--------------|-------------|
| **Fine 2025** | 100% (test) | Tonic | 10 szs, 3 pts |
| **Spahr 2025** | 96% | Generalized convulsive | 49 CSs, 384 pts |
| **Singh 2024** | 96.8% | Not specified | 1 pt case study |
| **Elemam 2025** | 95.1% (HRV model) | Not specified | 30 pts |
| **Borujeny 2013** | 85% | Motor | 20 szs, 3 pts |
| **Dong 2026** | 71.6% | Nocturnal major | 1846 szs, 68 pts |
| **Wang 2025** | 56.4--95.3% | Not specified | 62 szs, 28 pts |
| **Reintjes 2025** | 38.0--98.16% | Focal to bilateral tonic-clonic | 856 szs, 120 pts |

**Sensitivity Statistics:**
- **Range:** 38.0% to 100%
- **Median:** ~92%
- **Top 3 performers:** Fine 100%, Spahr 96%, Singh 96.8%
- **Lowest performer:** Reintjes 38% (TimeVQVAE-AD method)

### False Positive Rate (FPR) Summary

| Study | FPR | Clinical Acceptability* |
|-------|-----|------------------------|
| **Spahr 2025** | 0.005/h | Excellent (well below benchmark) |
| **Fine 2025** | 0.023/h | Excellent (below benchmark) |
| **Dong 2026** | 0.165/h | Acceptable (above Phase 3) |
| **Wang 2025** | 0.354/h | Borderline (3.5× benchmark) |
| **Ode 2023*** | 0.85/h | Unacceptable |
| **Borujeny 2013** | 3 FA total | Not rate-based |
| **Reintjes 2025** | 1.91--39.75/h | Unacceptable |
| **Singh 2024** | Not reported | - |
| **Elemam 2025** | Not reported | - |

*ILAE Phase 3 benchmark: FPR < 0.05-0.1/h for home use

**FPR Statistics:**
- **Range:** 0.005/h to 39.75/h
- **Studies meeting benchmark:** 2/8 (Spahr, Fine)
- **Studies above benchmark:** 3/8 (Dong borderline acceptable)
- **Studies not reporting FPR:** 3/8 (Singh, Elemam, partial Reintjes)

### AUC-ROC (Detection)

| Study | AUC | Notes |
|-------|-----|-------|
| **Dong 2026** | Not specified in table | Reported in text as mean AUC |
| **Reintjes 2025** | Variable by method | Anomaly detection comparison |

### Detection Latency

| Study | Latency | Notes |
|-------|---------|-------|
| **Fine 2025** | 14.1 s mean (median 10 s, max 47 s) | Nocturnal tonic seizures |
| **Spahr 2025** | Not specified in table | Real-time capable (112 ms inference) |
| **Borujeny 2013** | Not specified | Real-time server (316 mW) |

---

## Forecasting Studies Metrics (n=5)

### Sensitivity / AUC Summary

| Study | AUC | Sensitivity | Patient Success Rate |
|-------|-----|-------------|---------------------|
| **Nasseri 2021** | 0.75 (SD 0.15) | Not specified | 5/6 (83%) above chance |
| **Stirling 2021** | 0.74 | Not specified | 11/11 (100%) hourly, 10/11 (91%) daily |
| **Vieluf 2025** | Not specified | 82% | Not specified |
| **Meisel 2020** | Not specified | 51.2% | 43/69 (62%) above chance |
| **Ode 2023*** | Not specified | 74% | Not specified |

**Forecasting Statistics:**
- **AUC Range:** 0.74 to 0.75 (consistent across studies)
- **Sensitivity Range:** 51.2% to 82%
- **Patient Success:** 62% to 100% (varies by validation approach)

### Forecasting-Specific Metrics

| Study | IoC | TiW | Notes |
|-------|-----|-----|-------|
| **Meisel 2020** | 14.1% | 43.7% | Time in Warning |
| **Stirling 2021** | Not specified | 37 min (hourly), 3 days (daily) | Prediction time |
| **Nasseri 2021** | Not specified | 0.9--7.2 h/d | Time in Warning per day |
| **Vieluf 2025** | Not specified | Not specified | F1 score: 0.81 |

**IoC = Improvement over Chance**

### False Positive Rate (Forecasting)

| Study | FPR | Notes |
|-------|-----|-------|
| **Ode 2023** | 0.85/h | 99% confidence level |
| **Nasseri 2021** | Not in table | Reported in text |
| **Others** | Not reported | Forecasting uses different metrics |

---

## Clinical Benchmark Achievement

### ILAE Phase 3 Benchmark (FPR < 0.05-0.1/h)

| Study | FPR | Status | Notes |
|-------|-----|--------|-------|
| **Spahr 2025** | 0.005/h | Pass | 10× below benchmark |
| **Fine 2025** | 0.023/h | Pass | ~2× below benchmark |
| **Dong 2026** | 0.165/h | Near miss | 1.65× above benchmark |
| **Wang 2025** | 0.354/h | Fail | 3.5× above benchmark |
| **Ode 2023** | 0.85/h | Fail | 8.5× above benchmark |
| **Reintjes 2025** | 1.91--39.75/h | Fail | Up to 400× above benchmark |

**Benchmark Achievement:** 2/8 studies (25%) meet clinical FPR benchmark

---

## Performance by Validation Method

### LOSO (Leave-One-Subject-Out)

| Study | Performance | Notes |
|-------|-------------|-------|
| **Meisel 2020** | 51.2% sens, IoC 14.1% | 43/69 patients above chance |
| **Reintjes 2025** | 38-98% sens, 1.91-39.75/h FPR | Subject-split validation |

**Key Finding:** LOSO validation shows lower performance, reflecting real-world generalizability challenges.

### Temporal Split

| Study | Performance | Notes |
|-------|-------------|-------|
| **Nasseri 2021** | AUC 0.75 (SD 0.15) | 5/6 patients above chance |

### K-fold Cross-Validation

| Study | Performance | Notes |
|-------|-------------|-------|
| **Dong 2026** | 71.6% sens, 0.165/h FPR | 10-fold CV |
| **Spahr 2025** | 96% sens, 0.005/h FPR | Tunable algorithm |
| **Vieluf 2025** | 82% sens, 67% spec | 5-fold + LOO |

### Hold-out Validation

| Study | Performance | Notes |
|-------|-------------|-------|
| **Fine 2025** | 100% sens, 0.023/h FPR | Independent test dataset |
| **Wang 2025** | 56.4-95.3% sens | Hold-out split |

---

## Sensitivity-FPR Trade-off Analysis

### High Sensitivity, Low FPR (Ideal)

| Study | Sensitivity | FPR | Characteristics |
|-------|-------------|-----|-----------------|
| **Spahr 2025** | 96% | 0.005/h | Single-modality ACC, ensemble CNN |
| **Fine 2025** | 100% | 0.023/h | Phase 1, small test set (10 szs) |

### High Sensitivity, High FPR (Problematic)

| Study | Sensitivity | FPR | Issue |
|-------|-------------|-----|-------|
| **Reintjes 2025** | 98.16% | 39.75/h | Unacceptable false alarm rate |
| **Ode 2023** | 74% | 0.85/h | High FPR limits clinical utility |

### Balanced Performance

| Study | Sensitivity | FPR | Assessment |
|-------|-------------|-----|------------|
| **Dong 2026** | 71.6% | 0.165/h | Moderate sensitivity, acceptable FPR |
| **Wang 2025** | 56.4-95.3% | 0.354/h | Wide range, borderline FPR |

---

## Metrics Reporting Completeness

### Detection Studies
| Metric | Studies Reporting | % of Detection Studies |
|--------|-------------------|------------------------|
| **Sensitivity** | 8/8 | 100% |
| **FPR** | 5/8 | 63% |
| **Specificity** | 2/8 | 25% |
| **AUC-ROC** | 2/8 | 25% |
| **Detection Latency** | 2/8 | 25% |
| **Precision** | 2/8 | 25% |

### Forecasting Studies
| Metric | Studies Reporting | % of Forecasting Studies |
|--------|-------------------|---------------------------|
| **AUC** | 2/5 | 40% |
| **Sensitivity** | 3/5 | 60% |
| **Specificity** | 1/5 | 20% |
| **IoC** | 1/5 | 20% |
| **TiW** | 2/5 | 40% |
| **FPR** | 1/5 | 20% |

**Key Finding:** Inconsistent metric reporting across studies makes direct comparison challenging.

---

## Performance Outliers

### Exceptional Performers

| Study | Metric | Value | Context |
|-------|--------|-------|---------|
| **Spahr 2025** | FPR | 0.005/h | Best FPR in review |
| **Fine 2025** | Sensitivity | 100% | Perfect detection (small test set) |
| **Stirling 2021** | Patient Success | 100% | All patients above chance |

### Challenging Cases

| Study | Issue | Value | Context |
|-------|-------|-------|---------|
| **Reintjes 2025** | High FPR | 39.75/h | ECG anomaly detection |
| **Meisel 2020** | Low success | 43/69 (62%) | LOSO validation |
| **Borujeny 2013** | Small sample | 3 pts | Earliest study |

---

## Key Performance Findings

1. **Benchmark achievement:** Only 2/8 detection studies meet ILAE Phase 3 FPR benchmark
2. **Sensitivity ceiling:** Detection sensitivity reaches 100%, forecasting AUC plateaus at 0.75
3. **Validation matters:** LOSO validation shows substantially lower performance than other methods
4. **FPR challenge:** Many studies report FPR too high for home use (>0.1/h)
5. **Trade-off evident:** Higher sensitivity often correlates with higher FPR
6. **Metric inconsistency:** Forecasting studies use diverse metrics (IoC, TiW, AUC) complicating comparison

---

**End of Performance Metrics Report**
