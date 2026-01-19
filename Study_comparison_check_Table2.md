# Table 2 - Detailed Clinical and Technical Metrics - Verification Checklist

This section verifies claims in **Table 2 (tab:detailed-metrics)** from `Sections(tex)/04_Study_Comparison.tex` (lines 78-119).

---

## Detection Studies - Table 2

### 1. Spahr et al. 2025 ⚠️ NEEDS REVIEW
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | Indep. test (347 pt) | Line 110 | ✅ Verified |
| Detect. Latency | 26 s median | Line 548 | ✅ Verified |
| Patient Success | -- | N/A | ✅ Correct (not reported) |
| Precision/PPV | -- | N/A | ✅ Correct (not reported) |
| Other Metrics | HMS 92.6 | N/A | ❓ **NOT FOUND** |
| Clinical Notes | Phase 2, 2 CSs missed | Lines 125, 118 | ✅ Verified |

**CONFLICTS FOUND**:
- **HMS 92.6**: This metric is NOT found anywhere in the paper. The paper reports sensitivity (96%), FAR (1/8 days), and detection latency (26 s), but does NOT report an HMS (Harmonic Mean Score) of 92.6 or any HMS metric.

---

### 2. Reintjes et al. 2025 ⚠️ NEEDS REVIEW
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | Retro (SeizeIT2) | Line 194 | ✅ Verified |
| Detect. Latency | -- | N/A | ✅ Correct (not reported) |
| Patient Success | 55.6% responders | Line 302 | ⚠️ **MISLABELLED** |
| Precision/PPV | -- | N/A | ✅ Correct (not reported) |
| Other Metrics | HMS 86.8 (sens-opt), HMS 57.4 (FAR-opt) | Lines 873, 891 | ⚠️ **UNCLEAR** |
| Clinical Notes | HMS 57.4 (FAR-opt) | Line 873 | ⚠️ **UNCLEAR** |

**CONFLICTS FOUND**:
1. **Patient Success (55.6% responders)** - Line 302: The 55.55% value is the percentage of patients classified as "responders" based on having >50 BPM heart rate change during seizures. This is a SUBGROUP DEFINITION used for analysis, NOT a detection success rate or performance metric.
2. **HMS 86.8 (sens-opt)** - Line 891: The value 86.76 (rounded to 86.8) is TimeVQVAE-AD's HMS under sensitivity-optimized configuration for "All" patients. However, the BEST sensitivity-optimized HMS is actually **92.60** (Matrix Profile, line 885), not 86.8.
3. **HMS 57.4 (FAR-opt)** - Line 873: The value 57.36 (rounded to 57.4) is Matrix Profile's HMS under FAR-optimized configuration for "All" patients.

---

### 3. Fine 2025 ✅ VERIFIED
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | Indep. test (3 pt) | Line 25 | ✅ Verified |
| Detect. Latency | 14 s mean | Line 28 | ✅ Verified (14.1 s rounded) |
| Patient Success | -- | N/A | ✅ Correct (not reported) |
| Precision/PPV | -- | N/A | ✅ Correct (not reported) |
| Other Metrics | 95% CI: 69--100 | Line 27 | ✅ Verified |
| Clinical Notes | Phase 1 only | Lines 21, 56 | ✅ Verified |

**CONFLICTS FOUND**: None

---

### 4. Dong et al. 2026 ⚠️ MAJOR CONFLICTS
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | 10-fold CV | Lines 603-604 | ✅ Verified |
| Detect. Latency | <30 s | N/A | ❌ **INCORRECT** |
| Patient Success | -- | N/A | ✅ Correct (not reported) |
| Precision/PPV | -- | Lines 50-51, 833-834 | ⚠️ **SHOULD BE 0.334** |
| Other Metrics | AUC 0.793 | Lines 821-822 | ✅ Verified |
| Clinical Notes | First long-term home | Lines 53, 294 | ❓ **NOT SUPPORTED** |

**CONFLICTS FOUND**:
1. **Detect. Latency <30 s**: INCORRECT - Line 1217-1218 states "caregiver response times to nocturnal seizures at home often range from 30 s to several minutes" - this refers to CAREGIVER response time, NOT system detection latency. Detection latency is not explicitly specified.
2. **Precision/PPV**: Paper reports "mean PPV was 0.334 [95% CI: 0.229-0.356]" (lines 50-51, 833-834). Table incorrectly shows "--".
3. **Clinical Notes "First long-term home"**: NOT SUPPORTED - Paper describes home/ambulatory monitoring but does NOT claim to be the "first" such study.

---

### 5. Wang et al. 2025 ⚠️ NEEDS REVIEW
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | Hospital retro | Lines 32-34 | ✅ Verified |
| Detect. Latency | -- | N/A | ✅ Correct (not reported) |
| Patient Success | 7/22 pts | N/A | ❓ **NOT FOUND** |
| Precision/PPV | 83--87% | Lines 527, 531 | ✅ Verified |
| Other Metrics | Acc 97.8% | Line 844 | ⚠️ **PATIENT-SPECIFIC** |
| Clinical Notes | Single hospital | Lines 32-34 | ❌ **INCORRECT** |

**CONFLICTS FOUND**:
1. **Patient Success 7/22 pts**: NOT FOUND in paper. Paper states "four patients achieved the test accuracy exceeding 90%" out of patient IDs 19-28 (10 patients), not 7/22.
2. **Clinical Notes "Single hospital"**: INCORRECT - Lines 32-34 show TWO hospitals (Fourth Affiliated Hospital of Anhui Medical University AND Children's Hospital, Zhejiang University School of Medicine).
3. **Acc 97.8%**: This is patient-specific for patient ID 26 only (line 844).

---

### 6. Singh Rathore 2024 ⚠️ NEEDS REVIEW
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | Case study, train/test split | Lines 500-503 | ⚠️ **MISLABELLED** |
| Detect. Latency | -- | N/A | ✅ Correct (not reported) |
| Patient Success | -- | N/A | ✅ Correct (not reported) |
| Precision/PPV | 94.8% | Line 520 | ✅ Verified |
| Other Metrics | Acc 97.4%, F1 95.6% | Lines 520-521 | ✅ Verified |
| Clinical Notes | 3.2M data pts, 25k segments | Lines 500-502 | ✅ Verified |

**CONFLICTS FOUND**:
- **Validation "Case study"**: Lines 500-503 describe train/test split on data from "a single patient" over "six hours", not a "case study". The methodology is train/test split, not case study design.

---

### 7. Elemam et al. 2025 ⚠️ NEEDS REVIEW
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | Cross-sect | Line 799 | ✅ Verified |
| Detect. Latency | -- | Lines 1316-1317 | ⚠️ **SHOULD BE < 2 s** |
| Patient Success | -- | N/A | ✅ Correct (not reported) |
| Precision/PPV | 90.3% | Line 1139 | ⚠️ **ECG-SPECIFIC** |
| Other Metrics | -- | Lines 1049-1050, 1137-1141 | ⚠️ **INCOMPLETE** |
| Clinical Notes | PPG 15 s only | Line 462 | ✅ Verified |

**CONFLICTS FOUND**:
1. **Detect. Latency**: Lines 1316-1317 report "triggered alerts with a latency of less than 2 seconds in 95% of the cases". Should show "< 2 s" instead of "--".
2. **Precision 90.3%**: Line 1139 - This is for ECG classification system (Table 7), not audio system.
3. **Other Metrics**: Should specify which system - paper has THREE separate systems with different metrics: Questionnaire (95.10%/97.06%), ECG/HRV (91.5% acc, 90.3% prec, 93% sens, 90% spec), Audio (92.5% acc, <2 s latency).

---

### 8. Borujeny 2013 ⚠️ NEEDS REVIEW
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | 3-pt retro | Lines 176-177 | ✅ Verified |
| Detect. Latency | -- | N/A | ✅ Correct (not reported) |
| Patient Success | 3/3 pts | Lines 720-722 | ✅ Verified |
| Precision/PPV | -- | Lines 720-722 | ⚠️ **SHOULD BE 100%** |
| Other Metrics | -- | Lines 712, 720-722 | ⚠️ **INCOMPLETE** |
| Clinical Notes | 20 szs total | Line 179 | ✅ Verified |

**CONFLICTS FOUND**:
1. **Precision/PPV**: Lines 720-722 state "for k = 5 no seizure has been missed by the system and we have no false alarm" = 100% PPV for k=5.
2. **Other Metrics**: Should note that KNN k=5 achieved 100% sensitivity and 100% PPV; ANN had 85% sensitivity (line 712).

---

## Forecasting Studies - Table 2

### 9. Vieluf et al. 2025 ⚠️ NEEDS REVIEW
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | Retro longitudinal | Lines 193, 172 | ✅ Verified |
| Detect. Latency | -- | N/A | ✅ Correct (not reported) |
| Patient Success | -- | Lines 135, 972 | ⚠️ **SHOULD BE .82/.67** |
| Precision/PPV | -- | Lines 135, 972 | ⚠️ **SHOULD BE .89** |
| Other Metrics | F1 0.81 | Lines 135, 973 | ✅ Verified |
| Clinical Notes | Daily predictions | Lines 139, 1353 | ✅ Verified |

**CONFLICTS FOUND**:
1. **Patient Success**: Should show sensitivity=.82 and specificity=.67 for Detection (Allranked model, line 972), not blank "--".
2. **Precision/PPV**: Table 2 shows weighted precision=.89 for Detection (line 972), not blank "--".

---

### 10. Meisel et al. 2020 ✅ VERIFIED
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | LOSO CV | Line 78 | ✅ Verified |
| Detect. Latency | -- | N/A | ✅ Correct (forecasting study) |
| Patient Success | 30/69 (43.5%) | Line 1724 | ✅ Verified |
| Precision/PPV | -- | N/A | ✅ Correct (not reported) |
| Other Metrics | IoC 14.1% | Line 1730 | ✅ Verified |
| Clinical Notes | Pediatric only | Lines 32, 221 | ✅ Verified |

**CONFLICTS FOUND**: None

---

### 11. Stirling 2021 ✅ VERIFIED
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | Pseudo-prospective | Line 208 | ✅ Verified |
| Detect. Latency | -- | N/A | ✅ Correct (forecasting study) |
| Patient Success | 100% hourly | Lines 38-39, 761 | ✅ Verified |
| Precision/PPV | -- | N/A | ✅ Correct (not reported) |
| Other Metrics | AUC 0.74 | Lines 762, 993 | ✅ Verified |
| Clinical Notes | HR cycles key | Lines 41-42, 1006-1008 | ✅ Verified |

**CONFLICTS FOUND**: None

---

### 12. Nasseri 2021 ⚠️ NEEDS REVIEW
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | Retro analysis | Line 552 | ✅ Verified |
| Detect. Latency | 33 s mean | Line 226 | ❌ **WRONG UNIT** |
| Patient Success | 5/6 (83%) | Line 223 | ✅ Verified |
| Precision/PPV | -- | N/A | ✅ Correct (not reported) |
| Other Metrics | AUC 0.75 (0.50--0.92) | Lines 21-224 | ⚠️ **RANGE INCORRECT** |
| Clinical Notes | RNS validation req | Lines 88, 95-98 | ✅ Verified |

**CONFLICTS FOUND**:
1. **Detect. Latency**: Line 226 states "Seizure alerts occurred on average 33 **min** before the EEG-recorded seizure onset", not 33 seconds. Wrong unit.
2. **AUC range**: Lines 21-224 report mean 0.75 (SD 0.15) with range 0.72-0.92; claimed range (0.50-0.92) incorrectly includes the 0.50 random predictor value.

---

### 13. Ode et al. 2023 ⚠️ NEEDS REVIEW
| Field | Claimed Value | Source | Status |
|-------|---------------|--------|--------|
| Validation | Retro | Lines 265-289 | ✅ Verified |
| Detect. Latency | -- | Line 20 | ✅ Correct (forecasting horizon 15-20 min) |
| Patient Success | 29/66 (44%) | Line 317 | ⚠️ **CALCULATED, NOT EXPLICIT** |
| Precision/PPV | 0.35 | Lines 315-316 | ✅ Verified |
| Other Metrics | AUC 0.97 | Lines 315-316 | ✅ Verified |
| Clinical Notes | Individual tuning | Line 436 | ✅ Verified |

**CONFLICTS FOUND**:
- **Patient Success 29/66 (44%)**: Line 317 only states "A sensitivity of 100% was achieved in 29 patients". The 44% calculation (29/66) is implicit, not explicitly stated as "patient success rate".

---

## Summary of Table 2 Verification Results

| Study | Status | Action Required |
|-------|--------|-----------------|
| Spahr et al. 2025 | ⚠️ Partial | HMS 92.6 not found in paper - verify source |
| Reintjes et al. 2025 | ⚠️ Major Issues | Fix "responders" labeling, clarify HMS values |
| Fine 2025 | ✅ Fully Verified | None |
| Dong et al. 2026 | ⚠️ Major Issues | Fix detection latency, add PPV 0.334, remove "first" claim |
| Wang et al. 2025 | ⚠️ Partial | Fix patient success, correct to "two hospitals" |
| Singh Rathore 2024 | ⚠️ Partial | Correct validation method description |
| Elemam et al. 2025 | ⚠️ Major Issues | Add detection latency <2s, clarify metrics for each system |
| Borujeny 2013 | ⚠️ Partial | Add PPV 100%, clarify KNN vs ANN results |
| Vieluf et al. 2025 | ⚠️ Partial | Add sensitivity/specificity and precision values |
| Meisel et al. 2020 | ✅ Fully Verified | None |
| Stirling 2021 | ✅ Fully Verified | None |
| Nasseri 2021 | ⚠️ Partial | Fix latency unit (min not s), fix AUC range |
| Ode et al. 2023 | ⚠️ Minor | Note patient success is calculated value |

**Overall Table 2**: 4/13 studies fully verified ✅ | 9/13 studies need corrections ⚠️

---

## Combined Summary (Table 1 + Table 2)

| Study | Table 1 | Table 2 | Overall Status |
|-------|---------|---------|----------------|
| Spahr et al. 2025 | ✅ | ⚠️ | ⚠️ Minor issues |
| Reintjes et al. 2025 | ⚠️ | ⚠️ | ⚠️ Major issues |
| Fine 2025 | ⚠️ | ✅ | ⚠️ Minor issues |
| Dong et al. 2026 | ✅ | ⚠️ | ⚠️ Major issues |
| Wang et al. 2025 | ⚠️ | ⚠️ | ⚠️ Major issues |
| Singh Rathore 2024 | ✅ | ⚠️ | ⚠️ Minor issues |
| Elemam et al. 2025 | ⚠️ | ⚠️ | ⚠️ Major issues |
| Borujeny 2013 | ✅ | ⚠️ | ⚠️ Minor issues |
| Vieluf et al. 2025 | ✅ | ⚠️ | ⚠️ Minor issues |
| Meisel et al. 2020 | ⚠️ | ✅ | ⚠️ Minor issues |
| Stirling 2021 | ✅ | ✅ | ✅ Fully verified |
| Nasseri 2021 | ✅ | ⚠️ | ⚠️ Minor issues |
| Ode et al. 2023 | ✅ | ⚠️ | ⚠️ Minor issues |

**Combined Overall**: 1/13 studies fully verified (Stirling 2021) ✅ | 12/13 studies need corrections ⚠️

---

## Critical Issues Requiring Immediate Attention

### High Priority (Major Misstatements)
1. **Dong et al. 2026**: Detection latency <30 s is INCORRECT (caregiver response time, not system latency)
2. **Wang et al. 2025**: "Single hospital" is INCORRECT (uses two hospitals)
3. **Nasseri 2021**: Latency unit is WRONG (33 min, not 33 s)
4. **Elemam et al. 2025**: Detection latency is missing (<2 s should be shown)
5. **Reintjes et al. 2025**: "55.6% responders" is mislabeled (subgroup definition, not success rate)

### Medium Priority (Clarifications Needed)
1. **Spahr et al. 2025**: HMS 92.6 value source unclear
2. **Singh Rathore 2024**: "Case study" is inaccurate description
3. **Vieluf et al. 2025**: Sensitivity, specificity, precision values missing
