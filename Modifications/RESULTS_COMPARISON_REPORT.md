# Results Section Comparison Report
**Date:** 2026-01-23
**Compared:** `Sections(tex)/Results/` vs `Sections(tex)_old/Results/`

## Executive Summary

Substantial information has been removed from the Results section. The current versions are significantly shorter and lack many specific study details, performance statistics, and comparative analyses.

---

## File-by-File Analysis

### 01_study_characteristics.tex

**Information removed:**
- Specific patient numbers from `\textcite{spahrDeepLearningbasedDetection2025}` (384 patients)
- Specific patient numbers from `\textcite{dongTwoLayerEnsembleMethod2022}` (68 patients)
- Details about longest home monitoring duration (788 overnight recordings over three months)
- Details about longest overall monitoring period (14.6 months mean per patient)

**Information added:**
- Cross-references to other sections (Section~\ref{sec:clinical-readiness})

---

### 02_modality_performance.tex

**Information removed:**
- Results from `\textcite{fineDetectionKeyAutomated2025}` (100% sensitivity with 6-axis band, 0.023/h FPR)
- Results from `\textcite{dongTwoLayerEnsembleMethod2022}` (71.6% sensitivity, 0.165/h FPR, CNN-LSTM)
- Results from `\textcite{wangEpilepticSeizureDetection2025}` multi-modal approach (56.4% to 95.3% sensitivity)
- Results from `\textcite{vielufSeizureMonitoringCombined2025}` (82% sensitivity, 67% specificity)
- Results from `\textcite{stirlingForecastingSeizureLikelihood2021}` (AUC 0.74, 100% patient success, Fitbit)
- The entire paragraph about "Key finding"

---

### 03_architecture_patterns.tex

**Information removed:**
- Subsection label `\label{sec:architecture-patterns}`
- Entire "Detection Architectures" subsection with details about CNN implementation specifications
- Entire "Forecasting Architectures" subsection with LSTM specifications
- Entire "Input Representations" subsection about handcrafted features and window size variations
- Detailed statistics (e.g., "Three of eight detection studies use feature-based approaches")

---

### 04_modalities_architectures.tex

**Major structural change** - The old version had a completely different structure:
- **Old version:** 32 lines covering "Modality Selection and Sensor Placement" with detailed statistics and performance numbers
- **Current version:** 46 lines with "Architecture Patterns" and "Personalization Strategies" structure

**Key information removed:**
- "Modality Selection and Sensor Placement" subsection with specific modality counts and performance details
- Details about `\textcite{nasseriAmbulatorySeizureForecasting2021}` AUC results (0.75 SD 0.15, with significant predictors achieving mean AUC 0.80)
- Several specific performance statistics and study details

---

### 05_personalization.tex

**Catastrophic information loss:**
- **Old version:** 47 lines with detailed content covering:
  - Global Models (5 studies)
  - Patient-Specific Models (4 studies)
  - Mixed Approaches
  - Subject-Split Validation
  - Comparison by Strategy
  - Computational Considerations
  - Key Limitation about patient-level success reporting
- **Current version:** 7 lines stating content was "merged into Section~\ref{sec:modalities-architectures}"

---

### 06_performance_metrics.tex

**Information removed:**
- Specific details about `\textcite{fineDetectionKeyAutomated2025}` (100% sensitivity, 10 tonic seizures, 3 patients)
- Specific details about `\textcite{spahrDeepLearningbasedDetection2025}` (96% sensitivity, 384-patient multi-center study)
- Specific details about `\textcite{singhrathoreDevelopmentMultimodalMachine2024}` (96.8% sensitivity, single-patient)
- Specific details about `\textcite{elemamAutomatedValidatedTool2025}` (95.1% sensitivity)
- Entire paragraph about `\textcite{reintjesECGBasedDetectionEpileptic2025}` three anomaly detection methods with detailed FPR tradeoff analysis
- Paragraph listing studies that exceed ILAE Phase 3 benchmark (Dong, Wang, Ode, Reintjes)

---

### 07_detection_vs_forecasting.tex

**Information removed (6 paragraphs):**
- "Algorithmic Differences" subsection (about detection vs forecasting paradigms)
- "Modality Preferences" subsection (about movement sensors vs autonomic indicators)
- "Performance Comparison" subsection
- "Sample Size Disparity" subsection (median 44 vs 11, larger studies)
- "Validation Setting" subsection (hospital vs home, 6 of 8 detection in EMU)
- "Performance Ceiling" subsection

---

### 08_clinical_readiness.tex

**Information removed:**
- Paragraph about "Benchmark Achievement" listing specific FPR values for:
  - `\textcite{spahrDeepLearningbasedDetection2025}` (0.0054/h, ~10x below benchmark)
  - `\textcite{fineDetectionKeyAutomated2025}` (0.023/h, ~2x below benchmark)
  - Six detection studies exceeding benchmark (Dong 0.165/h, Wang 0.354/h, Ode 0.85/h, Reintjes 0.11-65.62/h)
- Specific details about barriers to clinical adoption (individual FPR values removed)
- Specific details about most advanced approaches (some performance numbers removed)

---

### 09_detection_forecasting_readiness.tex

**Information removed:**
- "Barriers to Clinical Adoption" subsection with detailed FPR values
- "Most Advanced Approaches" subsection with specific study details

---

### results_main.tex

**Identical** - No changes detected.

---

## Summary by Impact Level

### Critical Losses (Information may be missing)
1. **05_personalization.tex** - 85% content removed (47 lines -> 7 lines)
2. **07_detection_vs_forecasting.tex** - 6 paragraphs of comparative analysis removed
3. **03_architecture_patterns.tex** - Entire subsections removed

### Moderate Losses (Some details removed)
4. **02_modality_performance.tex** - Specific study results removed
5. **06_performance_metrics.tex** - Detailed performance breakdowns removed
6. **08_clinical_readiness.tex** - Specific FPR values removed
7. **09_detection_forecasting_readiness.tex** - Detailed subsections removed

### Minor Changes
8. **01_study_characteristics.tex** - Some specific numbers replaced with cross-references
9. **04_modalities_architectures.tex** - Structural reorganization (possibly merged content)

---

## Next Steps

For each section, verify whether removed information:
1. Was intentionally removed for page limits
2. Was relocated to another section
3. Needs to be restored
