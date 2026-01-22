# Results Section Overview

**Date:** 2026-01-22
**Purpose:** High-level narrative flow for the Results section

---

## Narrative Structure

The Results section should follow this logical flow:

1. **Study Characteristics Overview** (Section 4.1)
   - Establish the evidence base
   - Sample sizes, designs, settings
   - Publication timeline (2013-2026)

2. **Modality Performance Analysis** (Section 4.2)
   - What biosignals work best
   - Single vs multi-modal comparison
   - Sensor location trends

3. **Architecture and Algorithm Patterns** (Section 4.3)
   - Learning paradigms (Feature-based, E2E, Hybrid, Ensemble)
   - Detection vs forecasting architecture differences
   - Temporal evolution of approaches

4. **Performance Metrics Synthesis** (Section 4.4)
   - Sensitivity and FPR distributions
   - Clinical benchmark achievement
   - Detection vs forecasting metric comparison

5. **Personalization Strategies** (Section 4.5)
   - Global vs patient-specific approaches
   - Patient success rates
   - Generalizability analysis

6. **Detection vs Forecasting Comparison** (Section 4.6)
   - Side-by-side comparison
   - Clinical maturity assessment
   - Strengths and limitations of each approach

7. **Clinical Readiness and Deployment** (Section 4.7)
   - Validation phase distribution
   - Commercialization status
   - Barriers to adoption

---

## Key Findings Summary

### 1. Evidence Base Characteristics

**Sample Size Distribution:**
- Total participants: 912 (687 detection, 225 forecasting)
- Median sample size: 28 (detection: 44, forecasting: 11)
- Range: 1 patient (case study) to 384 patients (Spahr 2025)

**Study Design:**
- Prospective: 2/13 (15%)
- Retrospective: 7/13 (54%)
- Case study: 1/13 (8%)
- Other: 3/13 (23%)

**Temporal Trend:**
- 2013-2015: 1 study
- 2020-2022: 3 studies (forecasting peak)
- 2023-2026: 9 studies (detection acceleration)

---

### 2. Modality Insights

**Dominant Modalities:**
- ACC: 69% of studies (9/13)
- Multi-modal: 69% of studies (9/13)
- Wrist location: 62% of studies (8/13)

**Performance by Modality:**
- Single-modality ACC (Spahr 2025): 96% sens, 0.005/h FPR (best FPR)
- ACC+Gyro (Fine 2025): 100% sens, 0.023/h FPR
- ECG-based: High FPR variability (1.91-39.75/h)

**Key Finding:** Multi-modal approaches are common but single-modality ACC can achieve excellent performance.

---

### 3. Architecture Patterns

**Paradigm Distribution:**
- Feature-based: 4/13 (31%)
- End-to-end: 2/13 (15%)
- Hybrid: 2/13 (15%)
- Ensemble: 1/13 (8%)
- Anomaly detection: 2/13 (15%)

**Detection vs Forecasting:**
- Detection: Feature-based, ensemble, two-stage
- Forecasting: End-to-end LSTM dominates

**Temporal Evolution:**
- 2013: Traditional ML (ANN, KNN)
- 2020-2022: LSTM-based forecasting
- 2023-2026: Advanced ensembles and hybrids

---

### 4. Performance Metrics

**Detection Performance:**
- Sensitivity range: 38-100%
- FPR range: 0.005-39.75/h
- ILAE Phase 3 benchmark (<0.05-0.1/h): Only 2/8 studies meet

**Forecasting Performance:**
- AUC range: 0.74-0.75 (consistent ceiling)
- Patient success rate: 62-100%
- No established clinical benchmark

**Key Finding:** Detection has achieved sensitivity ceiling but struggles with FPR. Forecasting shows consistent AUC ceiling across approaches.

---

### 5. Personalization Strategies

**Strategy Distribution:**
- Global: 5/13 (38%)
- Patient-specific: 4/13 (31%)
- Other: 4/13 (31%)

**Success Rates:**
- Patient-specific: 83-100% individual success
- Global (LOSO): 62% patient success

**Trade-off:** Patient-specific achieves higher individual success but requires longitudinal data per patient.

---

### 6. Detection vs Forecasting

| Aspect | Detection | Forecasting |
|--------|-----------|-------------|
| Clinical maturity | More advanced | Earlier stage |
| Sensitivity/AUC | 38-100% | AUC 0.74-0.75 |
| Phase 3 eligible | 2 studies | 0 studies |
| Sample sizes | Larger (median 44) | Smaller (median 11) |
| Home validation | 38% | 60% |

**Key Finding:** Detection is closer to clinical deployment but forecasting achieves longer home validation durations.

---

### 7. Clinical Readiness

**Detection:**
- 2/8 studies meet Phase 3 FPR benchmark
- Commercial devices exist (Embrace, NightWatch)
- Barrier: FPR too high for most approaches

**Forecasting:**
- No studies meet clear clinical benchmark
- No regulatory approval for forecasting
- AUC ceiling suggests fundamental limitations

**Overall:** No study has achieved full Phase 3 validation for home deployment.

---

## Narrative Flow for Writing

### Introduction to Results

"This systematic review analyzed 13 primary studies (2013-2026) comprising 8 detection and 5 forecasting studies on wearable seizure monitoring devices. The evidence base includes 912 total participants with substantial variation in study design, sample size, and validation approach."

### Flow Through Topics

1. **Study Characteristics** -> Establish the foundation
2. **Modality Performance** -> What works, what does not
3. **Architecture Patterns** -> How approaches differ
4. **Performance Metrics** -> Quantitative results
5. **Personalization** -> Generalizability assessment
6. **Detection vs Forecasting** -> Comparative synthesis
7. **Clinical Readiness** -> Translation potential

---

## Critical Insights for Discussion

1. **Performance Ceiling:** Forecasting AUC consistently ~0.75 suggests fundamental limits of non-invasive approaches
2. **FPR Challenge:** Most detection studies fail to meet clinical FPR benchmark
3. **Validation Gap:** Lack of Phase 3 prospective home validation
4. **Sample Size Disparity:** Forecasting studies substantially smaller than detection
5. **Modality Surprise:** Single-modality ACC (Spahr 2025) achieves best overall FPR
6. **Personalization Trade-off:** Patient-specific models show higher success but require more data

---

## Tables and Figures Referenced

- **Table 1A:** Detection Studies Matrix (8 studies)
- **Table 1B:** Forecasting Studies Matrix (5 studies)
- **Table 2A:** Detection Architecture Deep-Dive
- **Table 2B:** Forecasting Architecture Deep-Dive
- **Table 3:** Metrics Summary

---

## Word Count Allocation (15 pages total)

| Section | Estimated Pages |
|---------|-----------------|
| Study Characteristics | 2 pages |
| Modality Performance | 2 pages |
| Architecture Patterns | 2 pages |
| Performance Metrics | 2 pages |
| Personalization Strategies | 1.5 pages |
| Detection vs Forecasting | 2 pages |
| Clinical Readiness | 2 pages |
| Tables and Figures | 1.5 pages |

---

## Supporting Files

Detailed analysis for each topic is available in:
- `01_study_characteristics.md`
- `02_modality_performance.md`
- `03_architecture_patterns.md`
- `04_performance_metrics.md`
- `05_personalization_strategies.md`
- `06_detection_vs_forecasting.md`
- `07_clinical_readiness.md`

---

**End of Overview**
