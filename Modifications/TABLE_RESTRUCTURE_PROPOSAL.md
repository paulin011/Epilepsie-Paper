# Table Restructure Proposal: Study Comparison Section

## Research Goal
> "How do different deep learning architectures and biosignal modalities excluding EEG compare in their ability to achieve an optimal trade-off between sensitivity and false alarm rate for ambulatory seizure monitoring?"

---

## Executive Summary

This proposal addresses the structural reorganization of the two main comparison tables in `Sections(tex)/04_Study_Comparison.tex`:

| Table | Current Focus | Proposed Focus | Rationale |
|-------|--------------|----------------|-----------|
| **Table 1** (tab:study-matrix) | General overview | Enhanced overview + architecture indicators | Maintain clinical quick-reference while adding key architectural dimensions |
| **Table 2** (tab:detailed-metrics) | Clinical metrics | **Architecture & Modality Deep-Dive** | Align with research question; shift from clinical to technical focus |

**Key Insight**: The current Table 2 focuses on clinical deployment metrics (validation, latency, patient success). This should be moved to a separate "Clinical Deployment" table. Table 2 should instead focus on the **technical dimensions** that directly answer the research question about architectures and modalities.

---

## Part 1: Analysis of Current Structure

### Current Table 1 (tab:study-matrix)

| Column | Current Content | Status for Research Question |
|--------|----------------|------------------------------|
| Study | Author + Year | Essential |
| Objective | Detection/Forecasting | Essential |
| Design | Prospective/Retro/n= | Essential |
| Sample | Patient count, seizures | Essential |
| Device | Empatica E4, NightWatch, etc. | Essential |
| Loc. | Wrist, Chest, etc. | Essential |
| Algorithm | CNN-LSTM, Ensemble, etc. | Partial - architecture name only |
| Sens | Sensitivity % | Essential |
| Spec | Specificity % | Essential |
| FPR | False positive rate | Essential |
| Key Limitation | One-sentence summary | Useful |

**Assessment**: Table 1 is well-structured for general overview. Missing: **architecture paradigm** (feature-based vs end-to-end), **modality count** (single vs multi), **personalization** indicators.

### Current Table 2 (tab:detailed-metrics)

| Column | Current Content | Relevance to Research Question |
|--------|----------------|-------------------------------|
| Validation | LOSO, K-fold, etc. | Indirect - affects generalizability |
| Detect. Latency | Seconds/minutes | Clinical metric, not architectural |
| Patient Success | Proportion achieving usable performance | Clinical metric |
| Precision/PPV | Positive predictive value | Clinical metric |
| Other Metrics | AUC, HMS, IoC, etc. | Performance summary |
| Clinical Notes | Phase, setting, comments | Does not address research question |

**Assessment**: Table 2 currently focuses on **clinical deployment metrics** rather than **architectural and modal dimensions**. For the research question about architectures and modalities, this table needs fundamental restructure.

---

## Part 2: Proposed Table 1 Enhancements

### Option A: Add Compact Indicator Columns (Recommended)

Add three new compact columns to Table 1:

| New Column | Width | Values | Description |
|------------|-------|--------|-------------|
| **Para.** | 0.8cm |Feat/E2E| Feature-based vs. End-to-end paradigm |
| **Mod.** | 0.6cm |1/M | Single vs. Multi-modal |
| **Pers.** | 0.8cm |Glb/Pat | Global vs. Patient-specific model scope |

**Rationale**:
- Minimal width impact (adds ~2.2cm total)
- Enables quick cross-study pattern recognition
- Answers key research questions at a glance
- Complements existing "Algorithm" column

### Option B: Integrate into Existing Columns (Alternative)

Instead of new columns, add shorthand notation to existing columns:

| Existing Column | Enhancement | Example |
|----------------|-------------|---------|
| Algorithm | Add paradigm suffix | "Ensemble 1D CNN (E2E)" |
| Device | Add modality count suffix | "Empatica E4 (Multi)" |
| Design | Add personalization suffix | "Prospective (Pat-spec)" |

**Trade-off**: Less visual clarity, saves horizontal space.

### Recommended: Option A with Compact Indicators

```
Study | Obj. | Des. | Sample | Device | Loc. | Para. | Mod. | Pers. | Algorithm | Sens | Spec | FPR | Key Lim.
      |      |      |        |        |      | Feat  | 1    | Glb   |            |      |      |     |
      |      |      |        |        |      | /E2E  | /M    | /Pat  |            |      |      |     |
```

---

## Part 3: Proposed Table 2 Restructure

### Complete Column Replacement

**Current Columns** (Clinical focus):
```
Study | Validation | Detect. Latency | Patient Success | Precision/PPV | Other Metrics | Clinical Notes
```

**Proposed Columns** (Architecture/Modality focus):
```
Study | Paradigm | Arch. Details | Modality Details | Fusion | Personalization | Trade-off Config | Deployment
```

### Detailed Column Specifications

| Column | Width | Content | Values/Format |
|--------|-------|---------|---------------|
| **Study** | 2.5cm | Author + Year | Same as Table 1 |
| **Paradigm** | 2.0cm | Feature-based vs. End-to-end | "Feature-based (594 feat)", "End-to-end", "Hybrid" |
| **Arch. Details** | 3.0cm | Architecture-specific features | "Ensemble (30 models)", "Self-Att AE", "Anomaly: Matrix Profile", "Attention: weighted" |
| **Modality Details** | 2.5cm | Signal breakdown | "ACC only", "ECG single-lead", "ACC+EDA+HR (3)", "PPG+Audio (2)" |
| **Fusion** | 1.8cm | Fusion strategy (multi-modal only) | "Early", "Late", "Decision", "--" (for single) |
| **Personalization** | 2.0cm | Model scope and validation | "Global (LOSO)", "Patient-specific", "Mixed" |
| **Trade-off Config** | 2.0cm | Operating points and optimization | "Sens-opt: 98%@14/h", "FAR-opt: 38%@2/h", "Single: 96%@<1/8d", "Tunable" |
| **Deployment** | 2.0cm | Real-time, on-device, setting | "Offline, EMU", "Online, Cloud", "Real-time, Edge?", "Home, Long-term" |

### Column Content Mapping by Study

| Study | Paradigm | Arch. Details | Modality Details | Fusion | Personalization | Trade-off Config | Deployment |
|-------|----------|---------------|------------------|--------|-----------------|------------------|------------|
| **Spahr 2025** | End-to-end | Ensemble: 30 CNN models | ACC | -- | Global | Single: 96%@<1/8d | Offline, EMU |
| **Reintjes 2025** | End-to-end (unsup) | Anomaly: 3 methods (Matrix Profile, MADRID, TimeVQVAE) | ECG single-lead | -- | Global | Multi: 38-98%@1.9-40/h | Offline |
| **Fine 2025** | Feature-based | ANN with 594 handcrafted features | ACC 6-axis | -- | Patient-specific | Single: 100%@0.023/h | Offline, EMU |
| **Dong 2026** | End-to-end | CNN-LSTM + Attention | ACC (night-focused) | -- | Global | Single: 71.6%@0.165/h | Offline |
| **Wang 2025** | Hybrid | LSTM + SVM/LDA (2-stage) | PPG | -- | Global | Range: 56-95%@8.5/24h | Offline, Hospital |
| **Singh 2024** | Feature-based | MLP (594 features extracted) | EDA+ACC+HR (3) | Late | Patient-specific | Single: 96.8% | Offline |
| **Elemam 2025** | Hybrid | CNN + Rule-based fusion | PPG+Audio (2) | Decision | Global | Single: 95.1%@<2s | Real-time?, Hospital |
| **Borujeny 2013** | Feature-based | KNN k=5 (time-domain features) | ACC | -- | Patient-specific (3pt) | Single: 100%@0 | Offline |
| **Vieluf 2025** | Hybrid | DNN + harmonic features + diary | ACC+Diary | Late | Global | Single: 82% sens, 67% spec | Home, Long-term |
| **Meisel 2020** | End-to-end | LSTM + 1D Conv | ACC | -- | Global (LOSO) | Single: 51.2%, IoC 14.1% | Offline |
| **Stirling 2021** | Feature-based | LSTM+RF+LR (HRV features) | HR (Fitbit) | -- | Patient-specific | AUC 0.74, 100% hourly | Offline |
| **Nasseri 2021** | End-to-end | 4-layer LSTM | ACC | -- | Patient-specific | AUC 0.75, TiW 0.9-7.2h/d | Offline |
| **Ode 2023** | End-to-end (unsup) | Self-Attentive AE | ECG (RRI) | -- | Individual tuning | Single: 74%@0.85/h | Offline |

---

## Part 4: Clinical Metrics Relocation

### Create New Table 3: Clinical Deployment Metrics

Since current Table 2 contains valuable clinical information, relocate it to a new focused table:

| Study | Validation | Latency | Pt. Success | PPV | Phase | Setting |
|-------|------------|---------|-------------|-----|-------|---------|
| Spahr 2025 | Indep. test (347 pt) | 26 s median | -- | -- | Phase 2 | EMU |
| Reintjes 2025 | Retro (SeizeIT2) | -- | -- (subgroup) | -- | -- | EMU |
| Fine 2025 | Indep. test (3 pt) | 14 s mean | -- | -- | Phase 1 | EMU |
| Dong 2026 | 10-fold CV | -- | -- | 0.334 | Prospective | Home |
| Wang 2025 | Hospital retro | -- | 4/10 pts | 83-87% | -- | Hospital |
| Singh 2024 | Train/test split | -- | -- | 94.8% | -- | Case study |
| Elemam 2025 | Cross-sect | <2 s | -- | 90.3% | -- | Hospital |
| Borujeny 2013 | 3-pt retro | -- | 3/3 pts | 100% | -- | EMU |
| Vieluf 2025 | Retro longitudinal | -- | -- | 0.89 | -- | Home |
| Meisel 2020 | **LOSO CV** | -- | 30/69 (43.5%) | -- | -- | EMU |
| Stirling 2021 | Pseudo-prospective | -- | 100% hourly | -- | -- | Ambulatory |
| Nasseri 2021 | Retro analysis | 33 min mean | 5/6 (83%) | -- | -- | Ambulatory |
| Ode 2023 | Retro | -- | 29/66 | 0.35 | -- | EMU |

---

## Part 5: LaTeX Implementation

### Table 1 Modified (Add 3 Columns)

```latex
\begin{tabular}{@{} l l l l l l >{\centering}p{0.8cm} >{\centering}p{0.6cm} >{\centering}p{0.8cm} l l l l >{\raggedright\arraybackslash}p{2.8cm} @{}}
\toprule
Study & Obj. & Des. & Sample & Device & Loc. & \thead{Para.} & \thead{Mod.} & \thead{Pers.} & Algorithm & Sens & Spec & FPR & Key Lim. \\
\midrule
\textbf{Spahr et al. 2025} & Det & Prosp. & n=384, 49 CSs & Empatica E4 (ACC) & Wrist & E2E & 1 & Glb & Ensemble 1D CNN & 96\% & -- & $<$0.013/h & EMU, offline \\
\bottomrule
\end{tabular}
```

### Table 2 Restructured (New Focus)

```latex
\begin{tabular}{@{} l >{\raggedright}p{2.0cm} >{\raggedright}p{3.0cm} >{\raggedright}p{2.5cm} >{\centering}p{1.8cm} >{\raggedright}p{2.0cm} >{\raggedright}p{2.0cm} >{\raggedright}p{2.0cm} @{}}
\toprule
\textbf{Study} & \thead{Paradigm} & \thead{Arch. Details} & \thead{Modality Details} & \thead{Fusion} & \thead{Personalization} & \thead{Trade-off Config} & \thead{Deployment} \\
\midrule

\textbf{Detection Studies} \\
\addlinespace

\textbf{Spahr et al. 2025} & End-to-end & Ensemble: 30 1D CNN models & ACC only & -- & Global & Single: 96\%@<1/8d & Offline, EMU \\
\addlinespace

\textbf{Reintjes et al. 2025} & End-to-end (unsup) & Anomaly: Matrix Profile, MADRID, TimeVQVAE-AD & ECG single-lead & -- & Global & Multi: 38.0--98.2\%@1.9--40/h & Offline \\
\addlinespace

\textbf{Fine 2025} & Feature-based & ANN with 594 handcrafted features & ACC 6-axis & -- & Patient-specific & Single: 100\%@0.023/h & Offline, EMU \\
\addlinespace

\textbf{Dong et al. 2026} & End-to-end & CNN-LSTM + Attention & ACC (night) & -- & Global & Single: 71.6\%@0.165/h & Offline, Home \\
\addlinespace

\textbf{Wang et al. 2025} & Hybrid & LSTM + SVM/LDA classifier & PPG only & -- & Global & Range: 56.4--95.3\%@0.354/h & Offline, Hospital \\
\addlinespace

\textbf{Singh Rathore 2024} & Feature-based & MLP (594 extracted features) & EDA+ACC+HR (3) & Late & Patient-specific & Single: 96.8\% & Offline \\
\addlinespace

\textbf{Elemam et al. 2025} & Hybrid & CNN + Rule-based fusion & PPG+Audio (2) & Decision & Global & Single: 95.1\%@<2s & Real-time?, Hospital \\
\addlinespace

\textbf{Borujeny 2013} & Feature-based & KNN k=5 (time-domain features) & ACC only & -- & Patient-specific (3pt) & Single: 100\%@0 & Offline \\
\addlinespace

\textbf{Forecasting Studies} \\
\addlinespace

\textbf{Vieluf et al. 2025} & Hybrid & DNN + harmonic features + diary & ACC+Diary (2) & Late & Global & Single: 82\% sens, 67\% spec & Home, Long-term \\
\addlinespace

\textbf{Meisel et al. 2020} & End-to-end & LSTM + 1D Convolution & ACC only & -- & Global (LOSO) & Single: 51.2\%, IoC 14.1\% & Offline, EMU \\
\addlinespace

\textbf{Stirling 2021} & Feature-based & LSTM+RF+LR (HRV features) & HR (Fitbit) & -- & Patient-specific & AUC 0.74, 100\% hourly & Offline \\
\addlinespace

\textbf{Nasseri 2021} & End-to-end & 4-layer LSTM & ACC only & -- & Patient-specific & AUC 0.75, TiW 0.9--7.2h/d & Offline \\
\addlinespace

\textbf{Ode et al. 2023} & End-to-end (unsup) & Self-Attentive Autoencoder & ECG (RRI) & -- & Individual tuning & Single: 74\%@0.85/h & Offline \\
\bottomrule
\end{tabular}
```

### New Table 3: Clinical Deployment Metrics

```latex
\begin{tabular}{@{} l >{\raggedright}p{2.0cm} >{\centering}p{1.5cm} >{\centering}p{2.0cm} >{\centering}p{1.5cm} >{\centering}p{1.5cm} >{\raggedright}p{2.0cm} @{}}
\toprule
\textbf{Study} & \textbf{Validation} & \textbf{Latency} & \textbf{Pt. Success} & \textbf{PPV} & \textbf{Phase} & \textbf{Setting} \\
\midrule
\textbf{Detection Studies} \\
\addlinespace
\textbf{Spahr et al. 2025} & Indep. test (347 pt) & 26~s median & -- & -- & Phase 2 & EMU \\
\textbf{Reintjes et al. 2025} & Retro (SeizeIT2) & -- & -- (subgroup) & -- & -- & EMU \\
\textbf{Fine 2025} & Indep. test (3 pt) & 14~s mean & -- & -- & Phase 1 & EMU \\
\textbf{Dong et al. 2026} & 10-fold CV & -- & -- & 0.334 & Prospective & Home \\
\textbf{Wang et al. 2025} & Hospital retro & -- & 4/10 pts & 83--87\% & -- & Hospital \\
\textbf{Singh Rathore 2024} & Train/test split & -- & -- & 94.8\% & -- & Case study \\
\textbf{Elemam et al. 2025} & Cross-sect & $<$2~s & -- & 90.3\% & -- & Hospital \\
\textbf{Borujeny 2013} & 3-pt retro & -- & 3/3 pts & 100\% & -- & EMU \\
\addlinespace
\textbf{Forecasting Studies} \\
\addlinespace
\textbf{Vieluf et al. 2025} & Retro longitudinal & -- & -- & 0.89 & -- & Home \\
\textbf{Meisel et al. 2020} & \textbf{LOSO CV} & -- & 30/69 (43.5\%) & -- & -- & EMU \\
\textbf{Stirling 2021} & Pseudo-prospective & -- & 100\% hourly & -- & -- & Ambulatory \\
\textbf{Nasseri 2021} & Retro analysis & 33~min mean & 5/6 (83\%) & -- & -- & Ambulatory \\
\textbf{Ode et al. 2023} & Retro & -- & 29/66 & 0.35 & -- & EMU \\
\bottomrule
\end{tabular}
```

---

## Part 6: Legend Updates

### Add to Table 1 Note:
```
Para. = Paradigm (Feat = feature-based, E2E = end-to-end)
Mod. = Modality count (1 = single-modal, M = multi-modal)
Pers. = Personalization (Glb = global model, Pat = patient-specific)
```

### New Legend for Table 2:
```
Paradigm: Learning approach (feature-based uses handcrafted features, end-to-end learns from raw data)
Arch. Details: Architecture-specific features (ensemble size, anomaly detection method, attention mechanism)
Modality Details: Signal types and count (number in parentheses)
Fusion: How multi-modal signals are combined (-- = single-modal, Early/Late/Decision = fusion stage)
Personalization: Model scope (global = population model, patient-specific = individualized)
Trade-off Config: Operating point configuration (Single/Multi, sensitivity @ FAR)
Deployment: Processing mode and setting (Offline/Online, EMU/Home/Hospital)
```

### Legend for New Table 3:
```
Validation: Cross-validation approach (LOSO = leave-one-subject-out)
Latency: Detection latency (time from seizure onset to alarm)
Pt. Success: Patient-level success rate (proportion achieving usable performance)
PPV: Positive predictive value / Precision
Phase: ILAE validation phase (1 = retrospective, 2 = prospective, 3 = real-world validated)
Setting: Validation environment (EMU = epilepsy monitoring unit)
```

---

## Part 7: Implementation Checklist

### Phase 1: Data Extraction
- [ ] Extract Paradigm (feature-based vs. end-to-end) for all 13 studies
- [ ] Extract Arch. Details (ensemble size, anomaly detection, attention)
- [ ] Extract Modality Details (signal list, count)
- [ ] Extract Fusion type (for multi-modal studies)
- [ ] Extract Personalization (global vs. patient-specific)
- [ ] Extract Trade-off Configuration (operating points, optimization target)
- [ ] Extract Deployment (real-time, on-device, setting)

### Phase 2: Table Modification
- [ ] Add 3 columns to Table 1 (Para., Mod., Pers.)
- [ ] Replace Table 2 columns with new architecture-focused columns
- [ ] Create new Table 3 for clinical deployment metrics
- [ ] Update legends and notes

### Phase 3: Verification
- [ ] Verify all extracted values against source papers
- [ ] Cross-check with existing verification documents
- [ ] Ensure consistency across all three tables
- [ ] Update text references to tables in Findings section

### Phase 4: Text Updates
- [ ] Update Section 4.3 (Dimensional Analysis) to reference new table structure
- [ ] Update Section 4.4 (Synthesis and Gaps) to reference new columns
- [ ] Update Findings section to reference new table 3 for clinical metrics
- [ ] Add discussion of paradigm trends (feature-based vs. end-to-end)

---

## Part 8: Expected Benefits

### For Research Question Alignment
- **Directly addresses** "deep learning architectures" via Paradigm + Arch. Details columns
- **Directly addresses** "biosignal modalities" via Modality Details + Fusion columns
- **Directly addresses** "optimal trade-off" via Trade-off Configuration column
- **Directly addresses** "ambulatory" via Deployment column

### For Cross-Study Analysis
- **Paradigm trends**: Easy to see evolution from feature-based (2013) to end-to-end (2023-2026)
- **Modality patterns**: Quick comparison of single vs. multi-modal approaches
- **Personalization impact**: Direct comparison of global vs. patient-specific performance
- **Trade-off landscape**: Visual representation of sensitivity-FAR configurations

### For Clinical Translation
- **Deployment readiness**: Clear indication of which systems are real-time/home-ready
- **Validation rigor**: LOSO and patient-specific approaches clearly identified
- **Clinical metrics preserved**: New Table 3 maintains clinical deployment information

---

## Part 9: Next Steps

1. **Launch 8 extraction agents** to populate the new columns (as specified in DEEP_LEARNING_COMPARISON_FRAMEWORK.md)

2. **Create extraction results document** with all 13 studies × new dimensions

3. **Verify extracted data** using existing verification checklists

4. **Implement LaTeX changes** to Section 04_Study_Comparison.tex

5. **Update cross-references** in Findings and Takeaways section

---

## Appendix: Dimension Definitions

### Paradigm (Feature-based vs. End-to-end)
- **Feature-based**: Uses handcrafted features extracted from signals (e.g., HRV features, time-domain features)
- **End-to-end**: Learns directly from raw or minimally processed signals
- **Hybrid**: Combines both approaches (e.g., deep learning on extracted features)

### Architecture Details
- **Ensemble**: Multiple models combined (specify count and voting method)
- **Anomaly Detection**: Unsupervised methods (Matrix Profile, Autoencoder, VAE)
- **Attention**: Attention mechanisms (self-attention, cross-modal attention)
- **Secondary**: Additional architectural components (e.g., "CNN-LSTM", "LSTM+SVM")

### Modality Details
- **Single-modal**: One signal type (ACC, ECG, PPG, HR, etc.)
- **Multi-modal**: Multiple signal types (list in parentheses)

### Fusion Type
- **Early**: Signal-level fusion before feature extraction
- **Late**: Feature-level fusion before classification
- **Decision**: Classifier output fusion
- **--**: Single-modal (no fusion)

### Personalization
- **Global**: Population model, same for all patients
- **Patient-specific**: Individualized model per patient
- **Mixed**: Combination (e.g., global pre-training + patient fine-tuning)

### Trade-off Configuration
- **Single**: One operating point reported
- **Multiple**: Multiple configurations tested (e.g., sens-opt vs. FAR-opt)
- **Tunable**: Adjustable threshold for clinical deployment
- **Format**: "Single: [sens]%@[FAR]" or "Multi: [min-max]%@[min-max]"

### Deployment
- **Real-time**: Processes streaming data with low latency
- **Offline**: Batch processing, not suitable for real-time detection
- **On-device**: Computation on wearable device
- **Cloud**: Server-side processing
- **Setting**: EMU, Hospital, Home, Ambulatory
