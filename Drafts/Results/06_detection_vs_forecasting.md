# Detection vs Forecasting Comparison

**Date:** 2026-01-22
**Topic:** Comparative Analysis of Seizure Detection and Forecasting Approaches

---

## Overview

This report provides a **side-by-side comparison** of **8 detection studies** and **5 forecasting studies** on wearable seizure monitoring. The two tasks have fundamentally different clinical objectives, leading to distinct algorithmic approaches and evaluation metrics.

---

## Fundamental Differences

| Aspect | Detection | Forecasting |
|--------|-----------|-------------|
| **Objective** | Identify seizure as it occurs | Predict seizure before onset |
| **Clinical utility** | Alert caregivers, enable intervention | Allow patient to prepare, take preventive action |
| **Time window** | Seconds to minutes after onset | Minutes to hours before onset |
| **Target** | Motor manifestations (convulsions) | Pre-ictal physiological changes |
| **Primary modalities** | ACC, Gyro (movement) | EDA, HRV, ECG (autonomic) |
| **Key metric** | Sensitivity vs FPR | AUC, IoC, TiW |

---

## Study Characteristics Comparison

| Characteristic | Detection (n=8) | Forecasting (n=5) |
|----------------|-----------------|-------------------|
| **Total participants** | 687 | 225 |
| **Median sample size** | 44 | 11 |
| **Prospective studies** | 2 (25%) | 0 (0%) |
| **Home/ambulatory** | 3 (38%) | 3 (60%) |
| **Multi-modal** | 6 (75%) | 3 (60%) |
| **Wrist-worn** | 5 (63%) | 3 (60%) |

**Key Finding:** Forecasting studies tend to be smaller (median n=11 vs n=44) but more commonly conducted in home settings (60% vs 38%).

---

## Algorithmic Approaches Comparison

### Learning Paradigm Distribution

| Paradigm | Detection | Forecasting |
|----------|-----------|-------------|
| **Feature-based** | 3 (38%) | 1 (20%) |
| **End-to-end** | 0 (0%) | 2 (40%) |
| **Hybrid** | 1 (13%) | 1 (20%) |
| **Ensemble** | 1 (13%) | 0 (0%) |
| **Two-stage** | 1 (13%) | 0 (0%) |
| **Anomaly** | 1 (13%) | 1 (20%) |

**Key Finding:** Forecasting relies more heavily on end-to-end deep learning (40% vs 0%), while detection uses more diverse approaches.

### Architecture Comparison

| Architecture Type | Detection Studies | Forecasting Studies |
|-------------------|-------------------|---------------------|
| **CNN / Ensemble CNN** | Spahr 2025, Elemam 2025 | - |
| **LSTM** | Wang 2025 | Meisel 2020, Nasseri 2021, Stirling 2021 |
| **ANN / MLP** | Fine 2025, Singh 2024, Borujeny 2013 | - |
| **Anomaly detection** | Reintjes 2025, Ode 2023 | Ode 2023 |
| **Hybrid / Ensemble** | Dong 2026 | Stirling 2021, Vieluf 2025 |

**Key Finding:** LSTM dominates forecasting (60% of forecasting studies), while detection uses more varied architectures.

---

## Modality Preferences

### Detection Modality Usage

| Modality | Studies | Reason |
|----------|---------|--------|
| **ACC** | 6/8 | Captures motor manifestations |
| **Gyro** | 3/8 | Enhances movement detection |
| **ECG/HRV** | 2/8 | Secondary modality |
| **EDA** | 2/8 | Secondary modality |

### Forecasting Modality Usage

| Modality | Studies | Reason |
|----------|---------|--------|
| **EDA** | 3/5 | Autonomic changes precede seizures |
| **ECG/HRV** | 3/5 | Heart rate cycles show predictive patterns |
| **ACC** | 3/5 | Activity patterns contribute |
| **Temperature** | 2/5 | Circadian patterns |

**Key Finding:** Detection emphasizes movement sensors (ACC, Gyro); forecasting emphasizes autonomic sensors (EDA, ECG/HRV).

---

## Performance Metrics Comparison

### Detection Metrics

| Metric | Range | Best Performer | Clinical Benchmark |
|--------|-------|----------------|-------------------|
| **Sensitivity** | 38-100% | Fine 2025 (100%) | Higher is better |
| **FPR** | 0.005-39.75/h | Spahr 2025 (0.005/h) | <0.05-0.1/h (Phase 3) |
| **AUC** | Not commonly reported | - | - |
| **Detection latency** | 10-47 s | Fine 2025 (10 s median) | Lower is better |

### Forecasting Metrics

| Metric | Range | Best Performer | Notes |
|--------|-------|----------------|-------|
| **AUC** | 0.74-0.75 | Nasseri 2021 (0.75) | Consistent ceiling |
| **Sensitivity** | 51-82% | Vieluf 2025 (82%) | Lower than detection |
| **IoC** | 14.1% | Meisel 2020 | Improvement over chance |
| **TiW** | 37 min - 7.2 h/d | Variable | Time in warning |

**Key Finding:** Detection achieves higher sensitivity (up to 100%) but with FPR challenges; forecasting shows consistent AUC ceiling (~0.75).

---

## Clinical Maturity Comparison

| Aspect | Detection | Forecasting |
|--------|-----------|-------------|
| **ILAE Phase 3 eligible** | 2 studies (Spahr, Fine) | 0 studies |
| **Prospective validation** | 2 studies | 0 studies |
| **Commercial devices** | NightWatch, Empatica E4 | None |
| **Home validation** | 3 studies | 3 studies |
| **Real-world deployment** | Limited | Very limited |

**Key Finding:** Detection shows greater clinical maturity with 2 studies meeting Phase 3 FPR benchmarks.

---

## Validation Approach Differences

### Detection Validation

| Method | Studies | Examples |
|--------|---------|----------|
| **10-fold CV** | 2 | Spahr 2025, Dong 2026 |
| **Hold-out** | 2 | Fine 2025, Wang 2025 |
| **Subject-split** | 1 | Reintjes 2025 |
| **Not specified** | 2 | Elemam 2025, Singh 2024 |
| **Case study** | 1 | Singh 2024 |

### Forecasting Validation

| Method | Studies | Examples |
|--------|---------|----------|
| **LOSO** | 1 | Meisel 2020 |
| **Temporal split** | 1 | Nasseri 2021 |
| **Pseudo-prospective** | 1 | Stirling 2021 |
| **5-fold + LOO** | 1 | Vieluf 2025 |
| **Not specified** | 1 | Ode 2023 |

**Key Finding:** Forecasting uses more diverse validation approaches, including pseudo-prospective evaluation.

---

## Patient Success Rates

### Detection

| Study | Success Metric | Result |
|-------|----------------|--------|
| **Spahr 2025** | Population-level | 96% sensitivity |
| **Fine 2025** | Test set | 100% (10 seizures) |
| **Most detection studies** | Do not report patient-level success | - |

**Gap:** Detection studies rarely report patient-level success rates.

### Forecasting

| Study | Patient Success Rate | Result |
|-------|---------------------|--------|
| **Stirling 2021** | 11/11 patients | 100% (hourly), 91% (daily) |
| **Nasseri 2021** | 5/6 patients | 83% above chance |
| **Meisel 2020** | 43/69 patients | 62% above chance (LOSO) |

**Key Finding:** Forecasting studies consistently report patient-level success, enabling better assessment of individual utility.

---

## Real-World Validation

### Detection

| Study | Setting | Duration | Notes |
|-------|---------|----------|-------|
| **Dong 2026** | Home | Up to 3 months | NightWatch armband |
| **Singh 2024** | Home | 6 hours | Case study |
| **Spahr 2025** | EMU (8 centers) | Prospective | Multi-center |

### Forecasting

| Study | Setting | Duration | Notes |
|-------|---------|----------|-------|
| **Nasseri 2021** | Ambulatory | 60+ days | RNS + Empatica E4 |
| **Stirling 2021** | Home | Mean 14.6 months | Fitbit + diary |
| **Vieluf 2025** | Home | >30 weeks | Phase IV trial |

**Key Finding:** Forecasting studies achieve longer home monitoring durations (weeks-months vs days-weeks).

---

## Performance Ceiling Analysis

### Detection

- **Sensitivity ceiling:** Reached 100% (Fine 2025)
- **FPR challenge:** Most studies above clinical benchmark
- **Best performer:** Spahr 2025 (96% sens, 0.005/h FPR)

### Forecasting

- **AUC ceiling:** Consistently 0.74-0.75 across studies
- **Patient success:** 62-100% depending on validation
- **IoC range:** 14.1% (Meisel 2020)

**Interpretation:** Detection has achieved sensitivity ceiling but struggles with FPR. Forecasting shows consistent AUC ceiling across approaches, suggesting fundamental limits.

---

## Summary Comparison Table

| Aspect | Detection | Forecasting | Advantage |
|--------|-----------|-------------|-----------|
| **Clinical maturity** | More advanced | Earlier stage | Detection |
| **Sensitivity** | 38-100% | 51-82% | Detection |
| **FPR control** | Challenging | Different metrics | Detection |
| **Patient success reported** | Rarely | Commonly | Forecasting |
| **Validation rigor** | Moderate | Higher diversity | Forecasting |
| **Home deployment** | Some studies | More studies | Forecasting |
| **Sample sizes** | Larger | Smaller | Detection |
| **Prospective data** | 2 studies | 0 studies | Detection |
| **AUC consistency** | Variable | 0.74-0.75 | Forecasting |

---

## Key Findings

1. **Detection is more clinically mature:** 2 studies meet Phase 3 benchmarks; no forecasting studies do
2. **Forecasting has better validation:** More diverse approaches including pseudo-prospective
3. **Modality split:** Detection uses movement (ACC/Gyro); forecasting uses autonomic (EDA/HRV)
4. **Performance ceiling:** Detection reaches 100% sensitivity; forecasting plateaus at AUC ~0.75
5. **Sample size disparity:** Detection studies larger (median n=44 vs n=11)
6. **Patient success reporting:** Forecasting studies consistently report individual success; detection studies rarely do
7. **Home validation:** Forecasting more commonly validated in home settings (60% vs 38%)

---

## Clinical Implications

### Detection Readiness
- Two approaches (Spahr, Fine) achieve clinically acceptable FPR
- Commercial devices exist (NightWatch, Empatica)
- Main barrier: FPR too high for many approaches

### Forecasting Readiness
- No approaches meet clear clinical benchmark
- AUC ceiling (~0.75) suggests fundamental limitations
- May require invasive EEG for substantial improvement
- Value in patient-specific risk assessment

---

**End of Detection vs Forecasting Comparison Report**
