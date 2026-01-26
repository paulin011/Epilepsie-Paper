# Citation and Reference Accuracy Report

**Date:** 2026-01-26
**Scope:** All sections in `/home/paulin/Documents/Epilepsie/Sections(tex)/`
**Bibliography files checked:** `Epilepsie.bib`, `included_papers/included_items.bib`

---

## Executive Summary

Overall citation accuracy is **GOOD**. All cited bibkeys exist in the bibliography. The main issues identified are:
1. Missing table labels in included_items.bib (2 of 13 studies)
2. Some overcitation with redundant citations
3. A few unsubstantiated claims in the Abstract
4. Inconsistent citation command usage (`\cite{}` vs `\textcite{}` vs `\parencite{}`)

---

## 1. Critical Errors

### 1.1 Missing Bibkeys in Included Items

**Issue:** Two of the 13 primary studies are missing from `included_papers/included_items.bib`:
- `reintjesECGBasedDetectionEpileptic2025` - exists in main `Epilepsie.bib` but NOT in `included_items.bib`
- `nasseriAmbulatorySeizureForecasting2021` - exists in main `Epilepsie.bib` but NOT in `included_items.bib`
- `spahrDeepLearningbasedDetection2025` - exists in main `Epilepsie.bib` but NOT in `included_items.bib`

**Impact:** If only `included_items.bib` is used for compiling, these citations will fail. The document currently works because `Epilepsie.bib` (the full bibliography) is used.

**Recommendation:** Add the missing entries to `included_papers/included_items.bib` for consistency:
```bibtex
@article{reintjesECGBasedDetectionEpileptic2025,
  title = {{{ECG-Based Detection}} of {{Epileptic Seizures}} in {{Real-World Wearable Settings}}}},
  author = {Reintjes, Conrad and Hagenbeck, Janosch Fabio and Ballo, Mohamed and Rahlmeier, Tim and Wolf, Simon Maximilian and Schoder, Detlef},
  date = {2025-01},
  journaltitle = {Sensors},
  volume = {25},
  number = {24},
  pages = {7687},
  doi = {10.3390/s25247687}
}

@article{nasseriAmbulatorySeizureForecasting2021,
  title = {Ambulatory Seizure Forecasting with a Wrist-Worn Device Using Long-Short Term Memory Deep Learning},
  author = {Nasseri, Mona and Pal Attia, Tal and Joseph, Boney and Gregg, Nicholas M. and Nurse, Ewan S. and Viana, Pedro F. and Worrell, Gregory and Dümpelmann, Matthias and Richardson, Mark P. and Freestone, Dean R. and Brinkmann, Benjamin H.},
  date = {2021-11-09},
  journaltitle = {Scientific Reports},
  volume = {11},
  number = {1},
  pages = {21935},
  doi = {10.1038/s41598-021-99311-9}
}

@article{spahrDeepLearningbasedDetection2025,
  title = {Deep Learning-Based Detection of Generalized Convulsive Seizures Using a Wrist-Worn Accelerometer},
  author = {Spahr, Antoine and Bernini, Adriano and Ducouret, Pauline and Baumgartner, Christoph and Koren, Johannes P. and Imbach, Lukas and Beniczky, Sàndor and Larsen, Sidsel A. and Rheims, Sylvain and Fabricius, Martin and Seeck, Margitta and Steinhoff, Berhard J. and Beuchat, Isabelle and Dan, Jonathan and Atienza, David A. and Bardyn, Charles-Edouard and Ryvlin, Philippe},
  date = {2025-09},
  journaltitle = {Epilepsia},
  volume = {66 Suppl 3},
  pages = {53--63},
  doi = {10.1111/epi.70000}
}
```

---

## 2. Citation Format Issues

### 2.1 Inconsistent Citation Commands

**Issue:** Mix of `\cite{}`, `\textcite{}`, and `\parencite{}` commands throughout.

**Current usage:**
| File | Issue | Location |
|------|-------|----------|
| `01_introduction3.tex:7` | Uses `\cite{}` instead of `\textcite{}` or `\parencite{}` | `\cite{sveinssonClinicalRiskFactors2020} found...` |
| `02_background2.tex:5` | Uses `\cite{}` for parenthetical claim | `\cite{beniczkyAutomatedSeizureDetection2021}, \cite{chenSeizuresDetectionUsing2022}` |
| `02_background2.tex:19` | Multiple `\cite{}` where `\parencite{}` would be clearer | `\cite{abualrobUnlockingNewFrontiers2025, ghaderiAdvancesMachineLearning2025}` |
| `02_background2.tex:22` | Multiple `\cite{}` where `\parencite{}` would be clearer | `\cite{abualrobUnlockingNewFrontiers2025, mironAutonomicBiosignalsSeizure2025}` |

**Recommendation:** Standardize to:
- `\textcite{}` for narrative citations (author as subject)
- `\parencite{}` for parenthetical citations
- Avoid `\cite{}` unless specifically needed

**Specific fixes needed:**
- Line 7 of `01_introduction3.tex`: Change `\cite{sveinssonClinicalRiskFactors2020}` to `\textcite{sveinssonClinicalRiskFactors2020}`
- Line 5 of `02_background2.tex`: Change `\cite{beniczkyAutomatedSeizureDetection2021}, \cite{chenSeizuresDetectionUsing2022}` to `\parencite{beniczkyAutomatedSeizureDetection2021, chenSeizuresDetectionUsing2022}`
- Line 19 of `02_background2.tex`: Change to `\parencite{abualrobUnlockingNewFrontiers2025, ghaderiAdvancesMachineLearning2025}`
- Line 22 of `02_background2.tex`: Change to `\parencite{abualrobUnlockingNewFrontiers2025, mironAutonomicBiosignalsSeizure2025}`

---

## 3. Missing Citations (Undercitation)

### 3.1 Abstract - Unsubstantiated Claims

**Issue:** The Abstract contains factual claims without citations.

| Claim | Location | Suggested Citation |
|-------|----------|-------------------|
| "Epilepsy affects 60 million people worldwide" | `00_Abstract.tex:4` | Needs citation (WHO or epidemiology source) |
| "69% of deaths from generalized tonic-clonic seizures could be prevented" | `00_Abstract.tex:4` | `\textcite{sveinssonClinicalRiskFactors2020}` (used in intro but not abstract) |
| "EEG-based prediction is effective but unsuitable for ambulatory use" | `00_Abstract.tex:4` | Needs support from background literature |
| "AUC consistently plateaus around 0.74-0.75" | `00_Abstract.tex:12` | Cite specific studies: \parencite{meiselMachineLearningWristband2020, nasseriAmbulatorySeizureForecasting2021, vielufSeizureMonitoringCombined2025} |
| "Wrist-worn devices predominate (62% of studies)" | `00_Abstract.tex:14` | Derivable from data but formal citation helps |

**Recommendation:** Add citations to the Abstract for key factual claims.

### 3.2 Introduction - Uncited Statistics

**Issue:** `01_introduction3.tex:5` states "Epilepsy, a chronic neurological disorder affecting 60 million people worldwide" but lacks citation for the epidemiology figure. The drug-resistant statistic is cited (`\parencite{husseinFocalNonFocalEpilepsy2018}`), but the prevalence figure is not.

**Recommendation:** Add citation for the "60 million" statistic.

---

## 4. Overcitation Issues

### 4.1 Redundant Citations

**Issue:** Some paragraphs cite multiple sources where a single representative citation would suffice.

| Location | Overcitation | Recommendation |
|----------|--------------|----------------|
| `02_background2.tex:46` | `\parencite{wangEpilepticSeizureDetection2025, wuNovelSeizureDetection2024}` | Both support the claim, but consider if both needed |
| `02_background2.tex:50` | `\parencite{jainCompressedSensingBased2017, mironAutonomicBiosignalsSeizure2025}` | One may be sufficient if they make the same point |
| `02_background2.tex:70` | `\parencite{beniczkyStandardsTestingClinical2018, beniczkyAutomatedSeizureDetection2021}` | Two Beniczky papers - likely both relevant for ILAE standards |
| `02_background2.tex:76` | `\parencite{kalousiosECGbasedEpilepticSeizure2024, wongEEGDatasetsSeizure2023}` | Both address data leakage, citation may be appropriate |

**Assessment:** Most multi-citations are appropriate for supporting claims about multiple studies or consensus views. No critical overcitation found.

---

## 5. Citation Accuracy (Bibkey Verification)

### 5.1 All Cited Keys Verified

**Status:** PASS - All 32 unique citation keys used in the document exist in `Epilepsie.bib`.

**Cited keys:**
```
abualrobUnlockingNewFrontiers2025
beniczkyAutomatedSeizureDetection2021
beniczkyStandardsTestingClinical2018
borujenyDetectionEpilepticSeizure2013
chenSeizuresDetectionUsing2022
dongDetectionNocturnalEpileptic2026
dongTwoLayerEnsembleMethod2022
elemamAutomatedValidatedTool2025
fineDetectionKeyAutomated2025
ghaderiAdvancesMachineLearning2025
husseinFocalNonFocalEpilepsy2018
jainCompressedSensingBased2017
kalousiosECGbasedEpilepticSeizure2024
lealViabilityECGFeatures2017
luLeveragingChannelCoherence2025
masonHeartRateVariability2024
meiselMachineLearningWristband2020
mironAutonomicBiosignalsSeizure2025
nasseriAmbulatorySeizureForecasting2021
odeDevelopmentEpilepticSeizure2023
paveiEarlySeizureDetection2017
reintjesECGBasedDetectionEpileptic2025
sethFeasibilityCardiacbasedSeizure2023
shumCommerciallyAvailableSeizure2021
singhrathoreDevelopmentMultimodalMachine2024
sivathambooPreferencesUserExperiences2022
spahrDeepLearningbasedDetection2025
stirlingForecastingSeizureLikelihood2021
sveinssonClinicalRiskFactors2020
tugwellPRISMA20202021
vielufSeizureMonitoringCombined2025
wangEpilepticSeizureDetection2025
websterAnalyzingPrepareFuture2002
wongEEGDatasetsSeizure2023
wuNovelSeizureDetection2024
```

### 5.2 The 13 Primary Studies - Citation Status

| Study | Bibkey | Cited in text? | In included_items.bib? |
|-------|--------|----------------|------------------------|
| Spahr 2025 | `spahrDeepLearningbasedDetection2025` | YES | NO |
| Reintjes 2025 | `reintjesECGBasedDetectionEpileptic2025` | YES | NO |
| Elemam 2025 | `elemamAutomatedValidatedTool2025` | YES | YES |
| Dong 2022 | `dongTwoLayerEnsembleMethod2022` | YES | YES |
| Dong 2026 | `dongDetectionNocturnalEpileptic2026` | YES | YES |
| Wang 2025 | `wangEpilepticSeizureDetection2025` | YES | YES |
| Singh Rathore 2024 | `singhrathoreDevelopmentMultimodalMachine2024` | YES | YES |
| Fine 2025 | `fineDetectionKeyAutomated2025` | YES | YES |
| Borujeny 2013 | `borujenyDetectionEpilepticSeizure2013` | YES | YES |
| Ode 2023 | `odeDevelopmentEpilepticSeizure2023` | YES | YES |
| Vieluf 2025 | `vielufSeizureMonitoringCombined2025` | YES | YES |
| Meisel 2020 | `meiselMachineLearningWristband2020` | YES | YES |
| Stirling 2021 | `stirlingForecastingSeizureLikelihood2021` | YES | YES |
| Nasseri 2021 | `nasseriAmbulatorySeizureForecasting2021` | YES | NO |

**Note:** There are 14 studies listed here because Dong et al. has both a 2022 and 2026 paper, both cited.

---

## 6. Self-Reference Consistency (Section Labels)

### 6.1 All Referenced Labels Verified

**Status:** PASS - All `\ref{}` commands reference valid labels.

**Section labels defined:**
- `EMU-to-home` (custom label for clinical implications section)
- `fig:prisma`
- `sec:architecture-patterns`
- `sec:clinical-readiness`
- `sec:conclusion`
- `sec:detection-forecasting-readiness`
- `sec:detection-vs-forecasting`
- `sec:discussion`
- `sec:ilae-standards`
- `sec:modalities-architectures`
- `sec:modality-performance`
- `sec:pico-search`
- `sec:results`
- `sec:study-characteristics`

**Table labels defined (in separate table files):**
- `tab:detection-matrix`
- `tab:forecasting-matrix`
- `tab:detection-architecture`
- `tab:forecasting-architecture`
- `tab:metrics-summary`

**Warning:** One reference to `sec:modalities-architectures` appears in text, but this label is defined correctly in the file.

---

## 7. Table References

### 7.1 Table Reference Status

**Status:** PASS - All table references point to valid labels.

| Reference | Location | Status |
|-----------|----------|--------|
| `tab:detection-matrix` | `03_Methods.tex:32`, `results_main.tex:7` | OK |
| `tab:forecasting-matrix` | `03_Methods.tex:32`, `results_main.tex:7` | OK |
| `tab:detection-architecture` | `03_Methods.tex:43`, `results_main.tex:7` | OK |
| `tab:forecasting-architecture` | `03_Methods.tex:43`, `results_main.tex:7` | OK |
| `tab:metrics-summary` | `results_main.tex:7` | OK |

---

## 8. Specific File-by-File Analysis

### 8.1 `00_Abstract.tex`

**Issues:**
- Line 4: "Epilepsy affects 60 million people worldwide" - NO CITATION
- Line 4: "69% of deaths from generalized tonic-clonic seizures could be prevented" - NO CITATION (source exists in intro)
- Line 4: "EEG-based prediction is effective but unsuitable for ambulatory use" - NO CITATION
- Line 10: Mentions "Spahr et al." and "Fine et al." without citations

**Recommendations:**
1. Add citation for prevalence statistic
2. Add `\parencite{sveinssonClinicalRiskFactors2020}` for 69% statistic
3. Add citations for "Spahr et al." and "Fine et al."

### 8.2 `01_introduction3.tex`

**Issues:**
- Line 5: "Epilepsy, a chronic neurological disorder affecting 60 million people wordlwide" - NO CITATION for prevalence
- Line 6: Typo "wordlwide" should be "worldwide"
- Line 7: Uses `\cite{}` instead of `\textcite{}` or `\parencite{}`

**Recommendations:**
1. Fix typo "wordlwide" -> "worldwide"
2. Add citation for 60 million statistic
3. Change `\cite{sveinssonClinicalRiskFactors2020}` to `\textcite{sveinssonClinicalRiskFactors2020}` since author is grammatical subject

### 8.3 `02_background2.tex`

**Issues:**
- Line 5: Uses `\cite{}` commands that should be `\parencite{}`
- Line 19: Uses `\cite{}` for two sources
- Line 22: Uses `\cite{}` for two sources
- Line 46-60: Multiple multi-citations that may be appropriate but should be reviewed

**Recommendations:**
1. Standardize `\cite{}` to `\parencite{}` for parenthetical citations
2. Consider consolidating some multi-citations

### 8.4 `03_Methods.tex`

**Status:** GOOD - All citations use `\parencite{}` correctly.

### 8.5 `3.1_Search Strategy.tex`

**Status:** GOOD - No citations (search methodology).

### 8.6 Discussion Files (`Discussion/*.tex`)

**Status:** GOOD - Citations are appropriate and use `\textcite{}` or `\parencite{}` correctly.

### 8.7 Results Files (`Results/*.tex`)

**Status:** GOOD - Citations are appropriate. Uses `\textcite{}` for study references consistently.

### 8.8 `conclusion.tex`

**Status:** GOOD - Uses `\textcite{}` appropriately for narrative citations.

---

## 9. Recommendations Summary

### Priority 1 (Critical)
1. Add missing bibkeys to `included_papers/included_items.bib`:
   - `spahrDeepLearningbasedDetection2025`
   - `reintjesECGBasedDetectionEpileptic2025`
   - `nasseriAmbulatorySeizureForecasting2021`

### Priority 2 (Important)
2. Add citations to Abstract for:
   - "60 million people" prevalence statistic
   - "69% of deaths preventable" statistic
   - "Spahr et al." and "Fine et al." mentions
   - "AUC plateaus around 0.74-0.75" claim

3. Fix typo in `01_introduction3.tex`: "wordlwide" -> "worldwide"

4. Add citation for prevalence statistic in `01_introduction3.tex:5`

### Priority 3 (Style/Consistency)
5. Standardize citation commands:
   - Replace `\cite{}` with `\textcite{}` or `\parencite{}` throughout
   - `01_introduction3.tex:7`: `\cite{}` -> `\textcite{}`
   - `02_background2.tex`: Multiple `\cite{}` -> `\parencite{}`

---

## 10. Verification Checklist

- [x] All cited bibkeys exist in bibliography
- [ ] All 13 primary studies in `included_items.bib` (3 missing)
- [x] All `\ref{}` commands reference valid labels
- [x] All table references are correct
- [ ] Abstract citations complete
- [ ] Introduction prevalence statistic cited
- [x] No broken citations
- [ ] Consistent use of `\textcite{}` vs `\parencite{}`

---

**Overall Grade:** B+ (Good accuracy, with room for improvement in consistency and completeness)
