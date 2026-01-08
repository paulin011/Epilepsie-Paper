# Verification Summary: Comparison Table Corrections

**Date:** 2026-01-08
**Total Papers Verified:** 13/13

---

## Executive Summary

| Status | Count | Papers |
|--------|-------|--------|
| **Fully Correct** | 6 | Vieluf 2025, Meisel 2020, Stirling 2021, Reintjes 2025, Fine 2025, Spahr 2025, Dong 2026 |
| **Minor Corrections Needed** | 4 | Wang 2025, Singh Rathore 2024, Borujeny 2013, Elemam 2025 |
| **Major Corrections Needed** | 3 | Ode 2023, Nasseri 2021 |

---

## Detailed Corrections Required

### 1. Wang et al. 2025 - TWO CRITICAL ERRORS

| Field | Current Value | Correct Value | Issue |
|-------|--------------|---------------|-------|
| Seizure Type | "Not specified" | **Motor seizures** | Paper specifies focal onset motor seizures and GTCS |
| Sensitivity | "Up to 97.8%" | **Accuracy: 97.8%** | 97.8% is accuracy, NOT sensitivity. Paper does not report sensitivity. |

**Additional Details Missing:**
- Only 7 labeled seizure events used for testing
- Hospital environment only
- 6 patients had no recorded seizures

---

### 2. Singh Rathore et al. 2024 - ONE CRITICAL ERROR

| Field | Current Value | Correct Value | Issue |
|-------|--------------|---------------|-------|
| Specificity | "94.8% (MLP)" | **Precision: 94.8%** | 94.8% is precision (TP/(TP+FP)), NOT specificity (TN/(TN+FP)) |

**Correct Interpretation:**
- Sensitivity (Recall): 96.8%
- Precision: 94.8%
- Specificity: **NR** (not reported in paper)

---

### 3. Ode et al. 2023 - ONE MAJOR ERROR

| Field | Current Value | Correct Value | Issue |
|-------|--------------|---------------|-------|
| Design | "Prospective with SA-AE training" | **Retrospective validation** | Data analysis was retrospective using existing clinical databases |

**Correct Sample Description:**
- Training: 131 interictal episodes (77.4 hours)
- Validation: 264 interictal + 85 preictal episodes (195 hours)

---

### 4. Borujeny et al. 2013 - ONE MINOR ERROR

| Field | Current Value | Correct Value | Issue |
|-------|--------------|---------------|-------|
| FPR | "3 FAs (ANN k=1)" | **ANN: 3 FAs; KNN k=1: 3 FAs** | ANN doesn't have a "k" parameter - that's KNN-specific |

**Clarification:**
- ANN: 3 false alarms total (85% sensitivity)
- KNN k=1: 3 false alarms
- KNN k=5: 0 false alarms (100% sensitivity)

---

### 5. Nasseri et al. 2021 - TWO CRITICAL ERRORS

| Field | Current Value | Correct Value | Issue |
|-------|--------------|---------------|-------|
| Design | "Prospective 6+ month home" | **Retrospective analysis of prospective data** | Paper states "Phase 2 retrospective evidence" |
| Sensitivity | "75% mean (50-92)" | **AUC-ROC: 0.75 (0.50-0.92)** | Primary metric is AUC-ROC, NOT sensitivity |
| FPR/TiW | "TiW 0.62-7.2h/d" | **TiW 0.9-7.2h/d** | Minimum is 0.9, not 0.62 |

**Important Context:**
- Mean AUC-ROC: 0.75 (range 0.50-0.92)
- 5 of 6 patients achieved better-than-chance forecasting
- Mean pre-seizure alert time: 33 minutes

---

### 6. Elemam et al. 2025 - ONE MAJOR ERROR

| Field | Current Value | Correct Value | Issue |
|-------|--------------|---------------|-------|
| Design | "Prospective validation" | **Cross-sectional observational** | Paper describes "transversal observational study" |

**Important Limitations:**
- PPG measured for only 15 seconds in sitting position
- Not representative of real-world ambulatory monitoring
- Different sample sizes for each component (Q:198, HRV:30, Audio:20)

---

## Papers with All Claims Verified Correct

### 1. Vieluf et al. 2025 ✓
All claims verified as accurate. Additional context:
- Wearable data alone performed poorly (AUC_PR .49 for detection)
- Best performance came from diary-based features
- Study includes both detection AND prediction objectives

### 2. Meisel et al. 2020 ✓
All claims verified as accurate. Additional context:
- Only 30 of 69 patients (43.5%) had significant forecasting results
- Pediatric population (mean age 9.8 ± 5.9 years)
- Uses IoC (Improvement over Chance) instead of specificity

### 3. Stirling et al. 2021 ✓
All claims verified as accurate. Additional context:
- 100% of patients had above-chance forecasting with hourly predictions
- 91% with daily predictions
- HR cycles were the strongest predictor

### 4. Reintjes et al. 2025 ✓
All claims verified as accurate. Important context:
- FAR is orders of magnitude above clinically acceptable levels
- Goal: ~0.01 FA/h; Achieved: 1.91-39.75 FA/h
- Not suitable for stand-alone deployment

### 5. Fine 2025 ✓
All claims verified as accurate. Additional context:
- 100% sensitivity for test dataset; 96% for complete dataset
- Algorithm run offline on PC, not embedded in wristband
- Excluded subtle tonic seizures without motor manifestations

### 6. Spahr et al. 2025 ✓
All claims verified as accurate. Additional context:
- Final ensemble used 10 best models (selected from 30 trained)
- Two seizures missed due to arm positioning
- Phase 2 validation study

### 7. Dong et al. 2026 ✓
All claims verified as accurate. Additional context:
- Two-step approach reduced data volume by 81%
- HR increases precede movement by ~100 seconds
- First long-term (months) home monitoring study

---

## Summary of Corrections Needed in Comparison Table

| Paper | Corrections Required | Priority |
|-------|---------------------|----------|
| Wang 2025 | Seizure type, Sensitivity label | High |
| Singh Rathore 2024 | Specificity label | High |
| Ode 2023 | Design label | High |
| Nasseri 2021 | Design, Sensitivity metric, TiW range | High |
| Elemam 2025 | Design label | High |
| Borujeny 2013 | FPR clarification | Medium |

---

## Recommendations for Updated Table

1. **Standardize metrics reporting**:
   - Clearly distinguish between Accuracy, Sensitivity, Precision, and Specificity
   - Use "NR" consistently when metrics are not reported
   - Add notes when primary metric differs (e.g., AUC-ROC, IoC)

2. **Add design clarity**:
   - Distinguish between prospective data collection and retrospective analysis
   - Use "Retrospective analysis of prospective data" where appropriate

3. **Include important limitations**:
   - Small sample sizes (especially single-patient studies)
   - Controlled environment vs. real-world settings
   - Offline vs. real-time analysis

4. **Performance tier reporting**:
   - When studies report both overall and significant-subset results (e.g., Meisel), clearly label both
