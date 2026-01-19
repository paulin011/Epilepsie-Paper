# Main Study Comparison Table - Verification Checklist

## Instructions for Verification

### How to Use This Checklist

1. **For each study**, locate the original paper and verify the values in the "Current Value" column
2. **Add the source** in the "Source Needed" column (e.g., "Page 3, Table 1", "Abstract", "Line 245")
3. **Mark the status** in the "Status" column:
   - ✅ `Verified` - value matches the source
   - ⚠️ `Needs correction` - value is incorrect (note correct value in comments)
   - ❓ `Not found` - value not reported in the paper
   - `--` - not yet checked

### Where to Find the Papers

Papers are located in multiple directories in your project:

3. **`/home/paulin/Documents/Epilepsie/all-papers/`** - All papers in the table
4. **`/home/paulin/Documents/Epilepsie/all_papers_md/`** - Extracted text versions of the papers in the table (.md files)

### Tips for Finding Information

- **Sample size**: Check Abstract, Methods section, or Table 1
- **Device/sensors**: Abstract, Methods, or Figure captions
- **Algorithm**: Abstract, Methods, or title
- **Performance metrics** (Sensitivity, Specificity, FPR): Results section, Abstract, or main results table
- **Study design**: Abstract or Methods
- **Limitations**: Discussion section or Conclusion

### Quick Reference: File Naming Convention

Most papers follow this pattern:
```
FirstAuthor et al. - Year - Title of Paper.pdf
```

For example: `Spahr et al. - 2025 - Deep Learning-based Detection of Convulsive Seizures.pdf`

---

## Detection Studies

### 1. Spahr et al. 2025 ✅ VERIFIED
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | Convulsive multi-center DET | Lines 64-66 | ✅ Verified |
| Design | Prospective | Lines 198-199 | ✅ Verified |
| Sample | n=384, 49 CSs | Lines 490-493 | ✅ Verified |
| Device | Empatica E4 (ACC) | Lines 220-227 | ✅ Verified |
| Location | Wrist | Lines 70-72 | ✅ Verified |
| Algorithm | Ensemble 1D CNN | Lines 73-74, 292-294 | ✅ Verified |
| Sensitivity | 96% | Line 116 | ✅ Verified |
| Specificity | -- | N/A | ✅ Correct (not reported) |
| FPR | <1/8d | Line 117 | ✅ Verified |
| Key Limitation | EMU, offline | Lines 2300-2307 | ✅ Verified |

**CONFLICTS FOUND**: None

---

### 2. Reintjes et al. 2025 ⚠️ NEEDS REVIEW
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | ECG anomaly DET | Lines 4-5, 31 | ✅ Verified |
| Design | Retro | Line 211 | ✅ Verified |
| Sample | n=120, 856 szs | Line 209 | ✅ Verified |
| Device | Single-lead ECG | Lines 132, 144 | ✅ Verified |
| Location | Chest | Line 213 | ✅ Verified |
| Algorithm | Matrix Profile | Lines 25, 149 | MANUALLY Verified
| Sensitivity | 38.0%/98.16% | Lines 829, 833 | ✅ Verified |
| Specificity | -- | N/A | ✅ Correct (not reported) |
| FPR | 1.91--39.8/h | Lines 847, 865 | ✅ Verified |
| Key Limitation | Severe sens/FAR trade-off | Lines 30-31, 1119-1120 | ✅ Verified |

**CONFLICTS FOUND**:
- **Algorithm (lines 25, 149, 309-310)**: Paper evaluates THREE algorithms (Matrix Profile, MADRID, TimeVQVAE-AD), not just Matrix Profile alone. Current value is incomplete.

---

### 3. Fine 2025 ⚠️ NEEDS REVIEW
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | Tonic DET | Line 17 | ✅ Verified |
| Design | Phase 1 | Line 21 | ✅ Verified |
| Sample | n=15/3 | Lines 23-26 | ✅ Verified |
| Device | 6-axis band | Lines 59-61 | ✅ Verified |
| Location | Wrist | Lines 58-59 | ✅ Verified |
| Algorithm | ANN (594 feat) | Lines 22, 63 | ✅ Verified |
| Sensitivity | 100% | Lines 27, 85 | ⚠️ **CLARIFICATION NEEDED** |
| Specificity | -- | N/A | ✅ Correct (not reported) |
| FPR | 0.23/n, 0.023/h | Lines 84, 86 | ✅ Verified |
| Key Limitation | Small test, Possible overfitting | Lines 116-117, 121-122 | ✅ Verified |

**CONFLICTS FOUND**:
- **Sensitivity (lines 27, 85)**: 100% applies ONLY to independent test dataset; complete dataset achieved 96%. Should clarify which value refers to which dataset.

---

### 4. Dong et al. 2026 ✅ VERIFIED
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | Nocturnal severe szs | Lines 38-39, 293-294 | ✅ Verified |
| Design | Prospective | Lines 40, 329 | ✅ Verified |
| Sample | n=68, 1846 szs | Lines 40, 47-48 | ✅ Verified |
| Device | NightWatch | Lines 11, 40-41 | ✅ Verified |
| Location | Arm | Lines 11, 39, 40, 330 | ✅ Verified |
| Algorithm | CNN-LSTM | Lines 44, 291, 819 | ✅ Verified |
| Sensitivity | 71.6% | Lines 50, 837-838 | ✅ Verified (overall system) |
| Specificity | -- | N/A | ✅ Correct (not reported) |
| FPR | 0.165/h | Lines 50-52 | ✅ Verified |
| Key Limitation | Single-center | Lines 19-21, 1233-1235 | ✅ Verified |

**CONFLICTS FOUND**: None
**Note**: Sensitivity of 71.6% is overall system (pre-screening + DL). DL model alone has 76.2% (lines 50, 310-311).

---

### 5. Wang et al. 2025 ⚠️ MAJOR CONFLICTS
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | Sz DET (acc: 97.8%) | Line 843-844 | ⚠️ **MISLEADING** |
| Design | Retro | N/A | ❓ **NOT FOUND** |
| Sample | n=28, 62 szs | Lines 201-204, 271-274 | ✅ Verified |
| Device | Biovital-P1 | Lines 274-275 | ✅ Verified |
| Location | Wrist | Lines 274, 303 | ✅ Verified |
| Algorithm | LSTM+SVM/LDA | Lines 466-467, 514-516 | ✅ Verified |
| Sensitivity | -- | Lines 527-534, 604-606 | ⚠️ **INCORRECT** |
| Specificity | -- | N/A | ✅ Correct (not reported) |
| FPR | 8.5/24h | Lines 773-781 | ✅ Verified |
| Key Limitation | Hospital only | Lines 207-208, 269-271 | ✅ Verified |

**CONFLICTS FOUND**:
1. **Objective/Accuracy (line 843-844)**: 97.8% is patient-specific result for patient ID 26 ONLY. Overall LSTM accuracies: 80.1%, 83.4%, 82.5% (lines 770-781).
2. **Design**: Study design (retrospective vs prospective) is NOT explicitly stated in the paper.
3. **Sensitivity**: Marked as "--" but recall (equivalent to sensitivity) IS reported: 56.40% to 95.3% depending on classifier (lines 527-534, 604-606).

---

### 6. Singh Rathore 2024 ✅ VERIFIED
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | Multimodal DET | Lines 243-248 | ✅ Verified |
| Design | Case study | Line 500 | ✅ Verified |
| Sample | 1 pt, 6 hrs, 3.2M pts | Lines 500-501 | ✅ Verified |
| Device | Wearable (EDA+ACC+HR) | Lines 576-580 | ✅ Verified |
| Location | -- | Not specified | ✅ Correct |
| Algorithm | MLP | Line 519 | ✅ Verified |
| Sensitivity | 96.8% | Line 520 | ✅ Verified |
| Specificity | 94.8% | Line 520 | ✅ Verified |
| FPR | -- | Not reported | ✅ Correct |
| Key Limitation | Single patient | Line 501 | ✅ Verified |

**CONFLICTS FOUND**: None

---

### 7. Elemam et al. 2025 ⚠️ NEEDS REVIEW
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | Q+HRV+Audio | Lines 17-22 | ✅ Verified |
| Design | Cross-sect | Lines 799-800 | ✅ Verified |
| Sample | Q:198, HRV:30 | Lines 21-22, 1081-1083 | ✅ Verified |
| Device | Camera PPG | Lines 461-463 | ✅ Verified |
| Location | Finger | Lines 462-463 | ⚠️ **SHOULD BE "Thumbs"** |
| Algorithm | CNN, rule based | Lines 26, 103, 514 | ✅ Verified |
| Sensitivity | 95.1% | Lines 23, 1049, 1504 | ⚠️ **Q-SPECIFIC** |
| Specificity | 97.1% | Lines 23, 1049, 1504 | ⚠️ **Q-SPECIFIC** |
| FPR | -- | N/A | ❓ Not reported |
| Key Limitation | Small samples | Lines 1081-1084, 1236-1237 | ✅ Verified |

**CONFLICTS FOUND**:
1. **Location (line 462-463)**: Paper specifies "thumbs" (plural), not general "finger".
2. **Sensitivity/Specificity**: 95.1% and 97.06% values apply to QUESTIONNAIRE component only (line 1049-1050). HRV has 93%/90% (lines 1229-1230); Audio has 92.5% accuracy (line 1286).

---

### 8. Borujeny 2013 ✅ VERIFIED
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | Wireless ACC | Lines 20-21 | ✅ Verified |
| Design | 3-pt | Lines 176-178 | ✅ Verified |
| Sample | 3 pts, 20 szs | Lines 176-179 | ✅ Verified |
| Device | MICAz ACC | Lines 25-26, 538-541 | ✅ Verified |
| Location | Arm/thigh | Lines 174-176 | ✅ Verified |
| Algorithm | KNN k=5 | Lines 720-723 | ✅ Verified |
| Sensitivity | 100% | Lines 720-723 | ✅ Verified |
| Specificity | -- | N/A | ✅ Correct (not reported) |
| FPR | 0 | Lines 720-723 | ✅ Verified |
| Key Limitation | Very small | Lines 176-179 | ✅ Verified |

**CONFLICTS FOUND**: None

---

## Forecasting Studies

### 9. Vieluf et al. 2025 ✅ VERIFIED
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | Diary+wearable | Lines 53-59 | ✅ Verified |
| Design | Retro | Line 193 | ✅ Verified |
| Sample | n=70, 5437 d | Lines 531-532 | ✅ Verified |
| Device | Embrace | Line 260 | ✅ Verified |
| Location | Wrist | Lines 57, 884 | ✅ Verified |
| Algorithm | DNN+harmonic | Lines 66-69, 342-344 | ✅ Verified |
| Sensitivity | 82% | Line 135, Table 2 | ✅ Verified |
| Specificity | 67% | Line 135, Table 2 | ✅ Verified |
| FPR | -- | N/A | ✅ Correct (not reported) |
| Key Limitation | Daily res only | Lines 1353-1355 | ✅ Verified |

**CONFLICTS FOUND**: None

---

### 10. Meisel et al. 2020 ⚠️ NEEDS REVIEW
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | LOSO forecast | Lines 299-302 | ✅ Verified |
| Design | LOSO CV | Lines 299-302 | ✅ Verified |
| Sample | n=69, 452 szs | Lines 1681-1683 | ✅ Verified |
| Device | Empatica E4 | Line 222 | ✅ Verified |
| Location | Wrist | Lines 222-223, 1823-1824 | ⚠️ **INCOMPLETE** |
| Algorithm | LSTM+1DConv | Lines 337-338, 1516-1520 | ✅ Verified |
| Sensitivity | 51.2% | Line 1731 | ✅ Verified |
| Specificity | -- | N/A | ✅ Correct (not reported) |
| FPR | TiW 43.7% | Line 1731 | ✅ Verified |
| Key Limitation | Pediatric | Lines 1682, 1961-1964 | ✅ Verified |

**CONFLICTS FOUND**:
- **Location (lines 222-223, 1823-1824)**: Device placed on "either the left or right wrist or ankle" - 31 wrist, 38 ankle. Should be "Wrist/Ankle" to be accurate.

---

### 11. Stirling 2021 ✅ VERIFIED
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | HR cycle forecast | Lines 197-201 | ✅ Verified |
| Design | Retro+pseudo | Line 208 | ✅ Verified |
| Sample | n=11, 136 szs | Lines 29, 32, 546 | ✅ Verified |
| Device | Fitbit | Line 246 | ✅ Verified |
| Location | Wrist | Line 246 | ✅ Verified |
| Algorithm | LSTM+RF+LR | Lines 343-345 | ✅ Verified |
| Sensitivity | -- | N/A | ✅ Correct (not reported) |
| Specificity | -- | N/A | ✅ Correct (not reported) |
| FPR | AUC 0.74 | Lines 762-763 | ✅ Verified |
| Key Limitation | Self-report | Lines 1230-1231 | ✅ Verified |

**CONFLICTS FOUND**: None

---

### 12. Nasseri 2021 ✅ VERIFIED
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | Ambulatory forecast | Lines 5-8 (title) | ✅ Verified |
| Design | Retro | Line 552 | ✅ Verified |
| Sample | n=6 | Line 214 | ✅ Verified |
| Device | Empatica E4 | Lines 112-113 | ✅ Verified |
| Location | Wrist | Lines 112, 242-297 | ✅ Verified |
| Algorithm | LSTM 4-layer | Lines 120-121 | ✅ Verified |
| Sensitivity | AUC 0.75 | Line 224 | ✅ Verified |
| Specificity | -- | N/A | ✅ Correct (not reported) |
| FPR | TiW 0.9--7.2h/d | Table 2, Lines 663-673 | ✅ Verified |
| Key Limitation | RNS required | Lines 94-96 | ✅ Verified |

**CONFLICTS FOUND**: None
**Note**: Abstract states mean AUC-ROC of 0.80 for 5 of 6 patients; 0.75 is overall cohort mean.

---

### 13. Ode et al. 2023 ✅ VERIFIED
| Field | Current Value | Source | Status |
|-------|---------------|--------|--------|
| Objective | RRI prediction | Lines 21-23 | ✅ Verified |
| Design | Retro | Lines 265-285 | ✅ Verified |
| Sample | n=66, 85 szs | Lines 265-289 | ✅ Verified |
| Device | ECG | Lines 71-74, 265-273 | ✅ Verified |
| Location | -- | Lines 265-273 | ✅ Correct (multi-center) |
| Algorithm | Self-Att AE | Lines 23, 111 | ✅ Verified |
| Sensitivity | 74% | Lines 314-316 | ✅ Verified |
| Specificity | -- | N/A | ✅ Correct (not reported) |
| FPR | 0.85/h | Lines 314-316 | ✅ Verified |
| Key Limitation | FPs in some pts | Lines 24-26, 389-391 | ✅ Verified |

**CONFLICTS FOUND**: None
**Note**: Location if needed: Japan (6 centers) + European database (lines 265-273).

---

## Summary of Verification Results

| Study | Status | Action Required |
|-------|--------|-----------------|
| Spahr et al. 2025 | ✅ Fully Verified | None |
| Reintjes et al. 2025 | ⚠️ Partial | Update Algorithm field to include all 3 methods |
| Fine 2025 | ⚠️ Partial | Clarify sensitivity values (test vs complete dataset) |
| Dong et al. 2026 | ✅ Fully Verified | None |
| Wang et al. 2025 | ⚠️ Major Issues | Fix accuracy claim, add sensitivity values, clarify design |
| Singh Rathore 2024 | ✅ Fully Verified | None |
| Elemam et al. 2025 | ⚠️ Partial | Update location to "thumbs", clarify metrics are questionnaire-specific |
| Borujeny 2013 | ✅ Fully Verified | None |
| Vieluf et al. 2025 | ✅ Fully Verified | None |
| Meisel et al. 2020 | ⚠️ Partial | Update location to "Wrist/Ankle" |
| Stirling 2021 | ✅ Fully Verified | None |
| Nasseri 2021 | ✅ Fully Verified | None |
| Ode et al. 2023 | ✅ Fully Verified | None |

**Overall**: 9/13 studies fully verified ✅ | 4/13 studies need corrections ⚠️
