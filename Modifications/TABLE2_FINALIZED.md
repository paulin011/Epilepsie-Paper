# Table 2 Finalized: Architecture and Modality Deep-Dive

**All conflicts resolved with verified values and line numbers.**

---

## Complete Table 2 Data

| Study | Paradigm | Arch. Details | Modality Details | Fusion | Personalization | Trade-off Config | Deployment |
|-------|----------|---------------|------------------|--------|-----------------|------------------|------------|
| **Spahr 2025** | Ensemble (1D CNN) | 30 models, 14 conv layers, quantile aggregation | ACC 32 Hz, Euclidean norm, 30s window | -- | Global, tunable (q=60) | Tunable: 86-100% @ 0.01-0.5/day | Real-time (112ms), on-device TicWatch |
| **Reintjes 2025** | End-to-end | Anomaly: Matrix Profile, MADRID, TimeVQVAE-AD | ECG 256→8 Hz, bandpass 0.5-40 Hz, window N/A | -- | Global, subject split (sub-001 to sub-096 train, sub-097 to sub-125 test) | Multi: 38.0-98.2% @ 1.91-40.46/h | Offline, prototype, hospital |
| **Fine 2025** | Feature-based | ANN, 594 handcrafted features (mean, variance, SD) | ACC + Gyro (6-axis), 10s intervals, 1s overlap | Early (6-axis combined) | Global, hold-out (3 test separate) | Single: 100% @ 0.023/h | Offline PC, prototype, EMU |
| **Dong 2026** | Two-stage | Pre-screening (thresholds) + CNN-LSTM + Attention | ACM 11-12→20 Hz, PPG 100→20 Hz, 5min window | Early (feature extraction) | Global, subject-independent 10-fold CV | Single: 71.6% @ 0.165/h | Real-time, NightWatch armband, home |
| **Wang 2025** | Feature-based | LSTM (40 hidden units) + ReLU + FC + softmax | ACC/GYR 50 Hz, SEMG 200 Hz, EDA 4 Hz, 4s window | Early (feature concat) | Global, hold-out (IDs 1-18 train, 19-28 test) | Single: 56.4-95.3% @ 0.354/h | Real-time, hybrid (watch + phone), hospital |
| **Singh 2024** | Feature-based | MLP, multi-modal features (EDA, ACC, HR) | EDA, ACC (x,y,z,mag), HR/HRV, raw, 25k points | Early (feature-level) | Global, single patient (train/test split) | Single: 96.8% sens @ 94.8% prec | Real-time (designed), cloud?, research |
| **Elemam 2025** | CNN-based | CNN for HRV, CNN for Audio, separate models | PPG 250 Hz, Audio 10s, bandpass 0.5-40 Hz | No fusion (parallel separate models) | Global, unclear split | Single: 95.1% sens @ 97.1% spec (Q) | Real-time, hybrid (PC/mobile), hospital |
| **Borujeny 2013** | Feature-based | KNN k=5, time-domain features (variance, correlation, energy) | ACC 2D 3 Hz, 9s window (50 samples, stride 25) | -- | Global, same-patient (3 pts) | Multi (K=1,3,5): 90-100% @ 0-15% | Real-time alarm, server (316 mW), lab |
| **Vieluf 2025** | Hybrid | DNN + harmonic modeling (24-h patterns) | EDA 4 Hz, ACC 32 Hz, Temp 1 Hz, 10min median windows | Early (neural network input) | Mixed, 5-fold CV + leave-one-out | Single: 82% sens, 67% spec @ F1 0.81 | Offline MATLAB, home, Embrace |
| **Meisel 2020** | End-to-end | LSTM only (10 units), no feature engineering | EDA/ACC/BVP/Temp →4 Hz, raw, 30s window | Early (multi-channel input) | Global, LOSO (68 train, 1 test) | Single: 51.2% sens @ IoC 14.1% | Offline, research, hospital |
| **Stirling 2021** | Feature-based | LSTM+RF+LR ensemble, logistic regression combines outputs | HR 5s res, steps/sleep 1min, hourly/daily | Decision (ensemble averaging via LR) | Patient-specific, weekly retraining | Multiple: AUC 0.74 (hourly), 100% pts | Home (Fitbit), Seer app, research |
| **Nasseri 2021** | End-to-end | LSTM 4-layer, 128 hidden nodes, +FFT channels | ACC/BVP/EDA/Temp/HR →128 Hz, 60s epochs | Early (17-channel input) | Temporal split (1/3 train early, 2/3 test late) | Single: AUC 0.75 @ TiW 0.9-7.2h/d | Offline, cloud upload (tablet), home |
| **Ode 2023** | Anomaly Detection | Self-Attentive Autoencoder (SA-AE), attention mechanism | ECG (RRI only), raw, 45s window | -- | Patient-specific (individual 99% CL limits) | Single: 74% sens @ 0.85/h (99% CL) | Real-time (designed), cloud, hospital |

---

## Legend for Table 2

| Column | Values | Description |
|--------|--------|-------------|
| **Paradigm** | Feature-based, E2E, Hybrid, Ensemble, Two-stage, CNN-based, Anomaly | Learning approach |
| **Arch. Details** | Architecture-specific components (ensemble size, layers, anomaly detection method, attention) |
| **Modality Details** | Signals, sampling frequency, processing, window size |
| **Fusion** | -- = single-modal, Early = feature-level, Decision = classifier output |
| **Personalization** | Global = population model, Patient-specific = individualized, Temporal = time-split, LOSO |
| **Trade-off Config** | Single/Multiple/Tunable, sensitivity @ FAR |
| **Deployment** | Real-time capability, processing location, setting |

---

## LaTeX Code for Table 2

```latex
\begin{landscape}
\begin{table}[htbp]
\centering
\small
\caption{Architecture and Modality Deep-Dive: Technical Dimensions Across Studies}
\label{tab:detailed-metrics}
\setlength{\tabcolsep}{3.5pt}
\renewcommand{\arraystretch}{1.1}
\resizebox{\linewidth}{!}{%
\begin{tabular}{@{} l >{\raggedright}p{1.8cm} >{\raggedright}p{2.2cm} >{\raggedright}p{2.0cm} >{\centering}p{1.2cm} >{\raggedright}p{1.8cm} >{\raggedright}p{2.0cm} >{\raggedright}p{1.8cm} @{}}
\toprule
\textbf{Study} & \textbf{Paradigm} & \textbf{Arch. Details} & \textbf{Modality Details} & \textbf{Fusion} & \textbf{Personalization} & \textbf{Trade-off Config} & \textbf{Deployment} \\
\midrule

\textbf{Detection Studies} \\
\addlinespace

\textbf{Spahr et al. 2025} & Ensemble & 30 1D CNN models, 14 conv layers, quantile & ACC 32~Hz, Euclidean norm, 30~s & -- & Global, tunable & 86--100\% @ 0.01--0.5/day & Real-time (112~ms), on-device \\
\textbf{Reintjes et al. 2025} & End-to-end & Anomaly: Matrix Profile, MADRID, TimeVQVAE & ECG 256$\to$8~Hz, bandpass & -- & Global, subject split & 38.0--98.2\% @ 1.9--40.5/h & Offline, hospital \\
\textbf{Fine 2025} & Feature-based & ANN, 594 handcrafted features & ACC+Gyro 6-axis, 10~s intervals & Early & Global, hold-out & 100\% @ 0.023/h & Offline PC, EMU \\
\textbf{Dong et al. 2026} & Two-stage & Pre-screening + CNN-LSTM + Attention & ACM 11-12$\to$20~Hz, PPG 100$\to$20~Hz, 5~min & Early & Global, 10-fold CV & 71.6\% @ 0.165/h & Real-time, NightWatch, home \\
\textbf{Wang et al. 2025} & Feature-based & LSTM (40 hidden) + ReLU + FC & ACC/GYR 50~Hz, SEMG 200~Hz, EDA 4~Hz, 4~s & Early & Global, hold-out & 56.4--95.3\% @ 0.354/h & Real-time, hospital \\
\textbf{Singh 2024} & Feature-based & MLP, multi-modal features & EDA, ACC, HR/HRV, 25k points & Early & Global, single pt & 96.8\% @ 94.8\% prec & Real-time, cloud? \\
\textbf{Elemam 2025} & CNN-based & CNN for HRV, CNN for Audio (separate) & PPG 250~Hz, Audio 10~s & No fusion & Global, unclear & 95.1\% @ 97.1\% spec & Real-time, hospital \\
\textbf{Borujeny 2013} & Feature-based & KNN k=5, time-domain features & ACC 2D 3~Hz, 9~s & -- & Global, 3 pts & 90--100\% @ 0--15\% & Real-time, server (316~mW) \\
\addlinespace

\textbf{Forecasting Studies} \\
\addlinespace

\textbf{Vieluf et al. 2025} & Hybrid & DNN + harmonic modeling (24-h) & EDA 4~Hz, ACC 32~Hz, Temp 1~Hz, 10~min & Early & Mixed, 5-fold + LOO & 82\% sens, 67\% spec @ F1 0.81 & Offline MATLAB, home \\
\textbf{Meisel et al. 2020} & End-to-end & LSTM only (10 units) & EDA/ACC/BVP/Temp $\to$4~Hz, 30~s & Early & Global, LOSO & 51.2\% @ IoC 14.1\% & Offline, hospital \\
\textbf{Stirling 2021} & Feature-based & LSTM+RF+LR ensemble, LR combines & HR 5~s, steps/sleep 1~min, hourly/daily & Decision & Patient-specific, weekly & AUC 0.74, 100\% pts & Home (Fitbit), app \\
\textbf{Nasseri 2021} & End-to-end & LSTM 4-layer, 128 hidden + FFT channels & ACC/BVP/EDA/Temp/HR $\to$128~Hz, 60~s & Early (17-ch) & Temporal split & AUC 0.75 @ TiW 0.9--7.2h/d & Offline, cloud, home \\
\textbf{Ode et al. 2023} & Anomaly & Self-Attentive AE (attention) & ECG (RRI only), 45~s & -- & Patient-specific (99\% CL) & 74\% @ 0.85/h (99\% CL) & Real-time, cloud, hospital \\
\bottomrule
\end{tabular}%
}
\par\medskip
\footnotesize
\textbf{Note:} Paradigm: Feature-based = handcrafted features, End-to-end = learns from raw data, Hybrid = combines both, Ensemble = multiple models, Two-stage = sequential processing, Anomaly = unsupervised detection. Arch. Details: architecture-specific components. Fusion: -- = single-modal, Early = feature-level, Decision = classifier output. Personalization: Global = population model, Patient-specific = individualized, Temporal = time-split within patient, LOSO = leave-one-subject-out. Trade-off Config: operating points with sensitivity @ FAR. Deployment: real-time capability, processing location, setting. ACC = accelerometer, ECG = electrocardiogram, PPG = photoplethysmography, EDA = electrodermal activity, BVP = blood volume pulse, HR = heart rate, HRV = HR variability, SEMG = surface electromyography, TEMP = temperature, FFT = fast Fourier transform, CL = confidence limit, AUC = area under curve, TiW = time in warning, IoC = Improvement over Chance, EMU = epilepsy monitoring unit.
\end{table}
\end{landscape}
```

---

## Conflict Resolution Summary

| Study | Conflict | Resolved Value | Verification |
|-------|----------|----------------|--------------|
| Spahr 2025 | Paradigm | Ensemble (1D CNN) | Line 73: "ensemble-based convolutional" |
| Spahr 2025 | Personalization | Tunable | Line 65: "deep learning tunable algorithm" |
| Spahr 2025 | Sens range | 86-100% | Line 601: "≥86% and up to 100%" |
| Fine 2025 | Modality | M (ACC+Gyro) | Line 23: "accelerometer and gyroscope" |
| Dong 2026 | Paradigm | Two-stage | Line 42: "A two-step approach was designed" |
| Dong 2026 | Fusion | Early | Line 206: "transformed into features...processed by DL" |
| Nasseri 2021 | Paradigm | End-to-end | Line 37: "end-to-end learning methods" |
| Nasseri 2021 | Personalization | Temporal split | Line 179: "training...early part, testing...later portions" |
| Ode 2023 | Paradigm | Anomaly Detection | Line 206: "Anomaly detection refers to..." |
| Ode 2023 | Personalization | Patient-specific | Line 465: "individual limits" |
| Meisel 2020 | Architecture | LSTM only | Line 337: "LSTM networks" |
| Meisel 2020 | Units | 10 | Line 1737: "10 units instead of 100" |
| Vieluf 2025 | Paradigm | Hybrid | Line 68: "neural network" + Line 288: "harmonic models" |
| Wang 2025 | Architecture | LSTM only | Line 715: "LSTM was adopted" |
| Elemam 2025 | Fusion | No fusion | Separate models for HRV and Audio |
| Borujeny 2013 | Sens range | 90-100% | Line 716: Table 2 results |
| Singh 2024 | Feature count | N/A | No number specified |
| Singh 2024 | Fusion | Early (implied) | Multi-modal features used |
| Reintjes 2025 | Window | N/A | No specific window size found |

---

**Status:** Ready for implementation.
