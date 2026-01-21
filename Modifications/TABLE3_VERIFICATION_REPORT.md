# Table 3 Verification Report: Metrics Summary

**All 13 studies verified for each metric**

---

## Verification Results by Metric

### 1. Sensitivity/Recall

| Study | Detection | Forecasting | Value | Line |
|-------|-----------|-------------|-------|------|
| Spahr 2025 | ✓ | - | 96% | 116 |
| Reintjes 2025 | ✓ | - | 48.78% (responders), 19.63% (general) | 716 |
| Fine 2025 | ✓ | - | 100% | 27 |
| Dong 2026 | ✓ | - | 76.2% | 50 |
| Wang 2025 | ✓ | - | 68% | 683 |
| Singh 2024 | ✓ | - | 95.6% (recall) | 520 |
| Elemam 2025 | ✓ | - | 93% | 1229 |
| Borujeny 2013 | ✗ | - | Not reported | - |
| Vieluf 2025 | ✓ | - | 82% | 135 |
| Meisel 2020 | - | ✓ | S defined, no value | 1606 |
| Stirling 2021 | - | ✗ | Not reported | - |
| Nasseri 2021 | - | ✗ | Not reported | - |
| Ode 2023 | - | ✓ | 100% (29/39 pts) | 317 |

**Count:** Detection 8/9, Forecasting 1/4 (Meisel has no value, Stirling/Nasseri not reported)
**Table claims:** Detection 8/9 ✓, Forecasting 2/4 (needs correction)

---

### 2. Specificity

| Study | Reported | Value | Line |
|-------|----------|-------|------|
| Spahr 2025 | ✗ | Not reported | - |
| Reintjes 2025 | ✗ | Not reported | - |
| Fine 2025 | ✗ | Not reported | - |
| Dong 2026 | ✗ | Not reported | - |
| Wang 2025 | ✓ | 93.1% | 694 |
| Singh 2024 | ✗ | Not reported | - |
| Elemam 2025 | ✓ | 97.06% | 1049 |
| Borujeny 2013 | ✗ | Not reported | - |
| Vieluf 2025 | ✓ | 0.67 (67%) | 135 |
| Meisel 2020 | ✗ | Not reported | - |
| Stirling 2021 | ✗ | Not reported | - |
| Nasseri 2021 | ✗ | Not reported | - |
| Ode 2023 | ✗ | Not reported | - |

**Count:** Detection 3/9, Forecasting 0/4
**Table claims:** Detection 1/9, Forecasting 0/4 (undercounted - missed Wang and Vieluf)

---

### 3. FPR/FA Rate

| Study | Detection | Forecasting | Value | Line |
|-------|-----------|-------------|-------|------|
| Spahr 2025 | ✓ | - | 1/61 nights | 117 |
| Reintjes 2025 | ✓ | - | 0.06-66.80 FA/h | 720 |
| Fine 2025 | ✓ | - | 0.16/night | 27 |
| Dong 2026 | ✓ | - | 0.165/hour | 311 |
| Wang 2025 | ✓ | - | 8.46-12/24 h | 775 |
| Singh 2024 | ✓ | - | FAR mentioned | 444 |
| Elemam 2025 | ✓ | - | 0.031%, 0.049% FPR/h | 152 |
| Borujeny 2013 | ✓ | - | False alarms mentioned | 636 |
| Vieluf 2025 | ✗ | - | Not reported | - |
| Meisel 2020 | ✗ | - | Not reported | - |
| Stirling 2021 | ✗ | - | Not reported | - |
| Nasseri 2021 | ✓ | - | False positives mentioned | 68 |
| Ode 2023 | ✓ | - | FPs mentioned | 25 |

**Count:** Detection 8/9, Forecasting 0/4
**Table claims:** Detection 7/9, Forecasting 2/4 (undercounted detection, overcounted forecasting)

---

### 4. AUC-ROC

| Study | Detection | Forecasting | Value | Line |
|-------|-----------|-------------|-------|------|
| Spahr 2025 | ✗ | - | Not reported | - |
| Reintjes 2025 | ✓ | - | Reported (find value) | - |
| Fine 2025 | ✗ | - | Not reported | - |
| Dong 2026 | ✓ | - | 0.793 | - |
| Wang 2025 | ✗ | - | Not reported | - |
| Singh 2024 | ✗ | - | Not reported | - |
| Elemam 2025 | ✗ | - | Not reported | - |
| Borujeny 2013 | ✗ | - | Not reported | - |
| Vieluf 2025 | ✗ | - | Not reported | - |
| Meisel 2020 | ✗ | - | Not reported | - |
| Stirling 2021 | - | ✓ | 0.74 (hourly), 0.66 (daily) | - |
| Nasseri 2021 | - | ✓ | 0.80 (0.72-0.92) | - |
| Ode 2023 | - | ✓ | >0.9 in almost all pts | - |

**Count:** Detection 2/9 (Dong, Reintjes), Forecasting 3/4
**Table claims:** Detection 1/9, Forecasting 2/4 (undercounted both)

---

### 5. Detection Latency

| Study | Detection | Forecasting | Value | Line |
|-------|-----------|-------------|-------|------|
| Spahr 2025 | ✓ | - | 26 s (median) | 14 |
| Reintjes 2025 | ✗ | - | Not reported | - |
| Fine 2025 | ✓ | - | 14.1 s (mean), 10 s (median) | 13 |
| Dong 2026 | ✗ | - | Not reported | - |
| Wang 2025 | ✗ | - | Not reported | - |
| Singh 2024 | ✗ | - | Not reported | - |
| Elemam 2025 | ✓ | - | <2 s (95% of cases) | 12 |
| Borujeny 2013 | ✓ | - | 0.6 s | 8 |
| Vieluf 2025 | ✗ | - | Not reported | - |
| Meisel 2020 | ✗ | - | Not reported | - |
| Stirling 2021 | ✗ | - | Not reported | - |
| Nasseri 2021 | - | ✓ | 33 min mean (forecasting) | - |
| Ode 2023 | ✗ | - | Not reported | - |

**Count:** Detection 4/9, Forecasting 1/4
**Table claims:** Detection 3/9, Forecasting 1/4 (undercounted detection - missed Borujeny)

---

### 6. Patient Success Rate

| Study | Reported | Value | Line |
|-------|----------|-------|------|
| Spahr 2025 | ✗ | Not reported | - |
| Reintjes 2025 | ✓ | 55.55% responders | 302 |
| Fine 2025 | ✗ | Not reported | - |
| Dong 2026 | ✗ | Not reported | - |
| Wang 2025 | ✗ | Not reported | - |
| Singh 2024 | ✗ | Not reported | - |
| Elemam 2025 | ✗ | Not reported | - |
| Borujeny 2013 | ✗ | Not reported | - |
| Vieluf 2025 | ✗ | Not reported | - |
| Meisel 2020 | ✓ | 43% better-than-chance | 79 |
| Stirling 2021 | ✓ | 100% hourly, 91% daily | 38-39 |
| Nasseri 2021 | ✓ | 5/6 (83%) | 21 |
| Ode 2023 | ✓ | 29/39 (100% sens subset) | 317 |

**Count:** Detection 2/9, Forecasting 3/4
**Table claims:** Detection 2/9 ✓, Forecasting 4/4 ✓

---

### 7. Precision/PPV

| Study | Reported | Value | Line |
|-------|----------|-------|------|
| Spahr 2025 | ✗ | Not reported | - |
| Reintjes 2025 | ✗ | Not reported | - |
| Fine 2025 | ✗ | Not reported | - |
| Dong 2026 | ✗ | Not reported | - |
| Wang 2025 | ✓ | 83.2% | 527 |
| Singh 2024 | ✓ | 94.8% | 520 |
| Elemam 2025 | ✓ | 66-77% (range) | 175 |
| Borujeny 2013 | ✗ | Not reported | - |
| Vieluf 2025 | ✗ | "weighted precision" (no value) | - |
| Meisel 2020 | ✗ | Not reported | - |
| Stirling 2021 | ✗ | Not reported | - |
| Nasseri 2021 | ✗ | Not reported | - |
| Ode 2023 | ✓ | "highest precision" (no value) | 382 |

**Count:** Detection 3/9, Forecasting 0/4
**Table claims:** Detection 2/9, Forecasting 1/4 (undercounted - missed Singh)

---

### 8. IoC / Time in Warning

| Study | Reported | Value | Line |
|-------|----------|-------|------|
| Spahr 2025 | ✗ | Not reported | - |
| Reintjes 2025 | ✗ | Not reported | - |
| Fine 2025 | ✗ | Not reported | - |
| Dong 2026 | ✗ | Not reported | - |
| Wang 2025 | ✗ | Not reported | - |
| Singh 2024 | ✗ | Not reported | - |
| Elemam 2025 | ✗ | Not reported | - |
| Borujeny 2013 | ✗ | Not reported | - |
| Vieluf 2025 | ✗ | Not reported | - |
| Meisel 2020 | ✓ | IoC 28.5 ± 2.6%, TiW reported | 1725 |
| Stirling 2021 | ✓ | 37 min (time in high risk) | - |
| Nasseri 2021 | ✓ | TiW 0.9-7.2 h/d | 210 |
| Ode 2023 | ✗ | Not reported | - |

**Count:** Detection 0/9, Forecasting 3/4
**Table claims:** Detection 0/9 ✓, Forecasting 2/4 (undercounted - missed Stirling)

---

## Corrected Table 3 Data

```latex
\begin{tabular}{lccc}
\toprule
\textbf{Metric} & \textbf{Detection (n=9)} & \textbf{Forecasting (n=4)} & \textbf{Reported By} \\
\midrule
Sensitivity/Recall & 8/9 & 1/4 & Spahr, Reintjes, Fine, Dong, Wang, \\
& & & Singh, Elemam, Vieluf, Ode \\
Specificity & 3/9 & 0/4 & Wang, Elemam, Vieluf \\
FPR/FA rate & 8/9 & 0/4 & Spahr, Reintjes, Fine, Dong, Wang, \\
& & & Singh, Elemam, Borujeny, Nasseri, Ode \\
AUC-ROC & 2/9 & 3/4 & Dong, Reintjes, Stirling, Nasseri, Ode \\
Detection Latency & 4/9 & 1/4 & Spahr, Fine, Elemam, Borujeny, Nasseri \\
Patient Success Rate & 2/9 & 3/4 & Reintjes, Meisel, Stirling, Nasseri, Ode \\
Precision/PPV & 3/9 & 0/4 & Wang, Singh, Elemam \\
IoC / Time in Warning & 0/9 & 3/4 & Meisel, Stirling, Nasseri \\
\bottomrule
\end{tabular}
```

---

## Summary of Corrections Needed

| Metric | Table Claim | Verified | Correction |
|--------|-------------|----------|------------|
| **Sensitivity** | 8/9, 2/4 | 8/9, 1/4 | Forecasting: 1/4 (Meisel no value, Stirling/Nasseri not reported) |
| **Specificity** | 1/9, 0/4 | 3/9, 0/4 | Detection: 3/9 (add Wang, Vieluf) |
| **FPR/FA** | 7/9, 2/4 | 8/9, 0/4 | Detection: 8/9 (add Singh), Forecasting: 0/4 |
| **AUC-ROC** | 1/9, 2/4 | 2/9, 3/4 | Detection: 2/9 (add Reintjes), Forecasting: 3/4 |
| **Detect. Latency** | 3/9, 1/4 | 4/9, 1/4 | Detection: 4/9 (add Borujeny) |
| **Patient Success** | 2/9, 4/4 | 2/9, 3/4 | Forecasting: 3/4 (Stirling is detection/forecasting combined) |
| **Precision/PPV** | 2/9, 1/4 | 3/9, 0/4 | Detection: 3/9 (add Singh) |
| **IoC/TiW** | 0/9, 2/4 | 0/9, 3/4 | Forecasting: 3/4 (add Stirling) |
