# Deep Learning Architecture Coverage Analysis: Gaps and Recommendations

**Date:** 2026-01-28
**Purpose:** Analysis of DL architecture discussion in current literature review with identified gaps

---

## Executive Summary

This analysis examines the current discussion of deep learning architectures across 13 epilepsy seizure detection and forecasting studies. Six specialized analyses were conducted on: (1) CNN architectures, (2) LSTM architectures, (3) Ensemble/Two-stage methods, (4) Handcrafted feature engineering, (5) Multi-modal fusion strategies, and (6) Anomaly detection approaches.

**Key Finding:** The current discussion covers architectural diversity and patterns, but lacks critical depth on design justifications, comparative analysis, and clinical deployment considerations.

---

## 1. Currently Covered Content (Status Quo)

### 1.1 In `d2_technical_insights.tex`

The technical insights subsection covers:

- **Architecture Selection:** Detection vs forecasting architectural patterns, methodological diversity, LSTM concentration in forecasting
- **Handcrafted features:** Acknowledged as competitive with end-to-end approaches
- **Ensemble methods:** Noted as requiring greater computational resources

### 1.2 In `03_merged_architectures_personalization.tex`

The architectures subsection covers:

- **Learning paradigms:** Feature-based, end-to-end, hybrid, ensemble, anomaly detection
- **Architecture patterns by application:** CNN-based methods for detection, LSTM for forecasting
- **Temporal evolution:** Architecture choices from 2013-2026
- **Computational considerations:** On-device vs cloud-based processing

### 1.3 Coverage Assessment

| Aspect | Covered? | Depth |
|--------|----------|-------|
| Architectural diversity | Yes | Moderate |
| Detection vs forecasting patterns | Yes | Good |
| Learning paradigm classification | Yes | Good |
| Detailed architectural parameters | No | Minimal |
| Design justifications | No | Absent |
| Comparative analysis | Partial | Limited |
| Clinical deployment feasibility | No | Absent |

---

## 2. Critical Gaps Identified

### 2.1 Architectural Reporting Standards

**Problem:** Studies vary dramatically in how completely they describe their architectures.

| Study | Reporting Quality | Missing Information |
|-------|-------------------|-------------------|
| Spahr 2025 | Good | Layer count justification, kernel size rationale |
| Dong 2026 | Good | Attention mechanism specifics |
| Elemam 2025 | **Poor** | Number of layers, filter sizes, kernel dimensions, parameter count |
| Nasseri 2021 | Good | Activations for all layers |
| Wang 2025 | Moderate | Why 40 hidden units? |
| Meisel 2020 | Moderate | Dropout rate, weight initialization |
| Stirling 2021 | Moderate | Batch size, weight initialization |
| Reintjes 2025 | **Poor** | CNN encoder architecture completely unspecified |

**Impact:** Poor reporting prevents reproduction, comparison, and understanding of what drives performance.

**Gap:** No discussion of this reporting heterogeneity or its implications for the field.

---

### 2.2 Design Justifications

**Problem:** Architectural choices are rarely justified.

| Design Choice | Studies Providing Justification | Studies Without |
|---------------|--------------------------------|-----------------|
| Why CNN vs LSTM vs Transformer? | **0/13** | All |
| Layer count selection | **0/13** | All |
| Filter/kernel sizes | 1/4 CNN studies | 3/4 CNN studies |
| Hidden unit count | 0/5 LSTM studies | All |
| Pooling strategy | 0/4 CNN studies | All |
| Dropout rate selection | 0/8 studies using dropout | All |

**Gap:** The discussion notes that CNN approaches dominate detection and LSTM dominates forecasting, but does not address *why* these choices were made or whether they are optimal.

---

### 2.3 Comparative Analysis

**Problem:** Very few studies provide ablation or comparative analysis.

| Comparison Type | Studies Providing Comparison | Key Finding |
|----------------|----------------------------|-------------|
| Single vs multi-modal | 3/6 multi-modal studies | Fusion improves performance |
| Feature-based vs E2E | **0/13** | No evidence |
| Different architectures | 1/13 | Ode 2023 only |
| Layer depth ablation | 1/13 | Meisel 2020 (10 vs 100 units) |
| Attention vs no-attention | 0/13 | No evidence |

**Gap:** The discussion states "ensembles achieve excellent results" but cannot quantify how much better than single models because baselines are missing. Same for "handcrafted features remain competitive" - no direct comparison.

---

### 2.4 Multi-Modal Fusion Depth

**Currently Covered:** The discussion notes "69% of studies use multiple sensor types" and "sensor fusion is not always necessary."

**Missing Depth:**

1. **Fusion strategy classification:** None of the studies classify their approach as early/late/intermediate fusion
2. **Fusion timing optimization:** Dong 2026 notes HR precedes movement by ~100s but no study optimizes temporal alignment
3. **Redundancy analysis:** No formal correlation or mutual information analysis between modalities
4. **Adaptive fusion:** Only Dong 2026 uses attention for dynamic modality weighting
5. **Modality contribution:** Only Meisel 2020 and Dong 2026 systematically analyze individual modality contributions

**Gap:** The discussion mentions fusion but does not analyze *how* fusion is accomplished or *which* strategies work best.

---

### 2.5 Attention Mechanisms

**Problem:** Attention is mentioned but never analyzed in depth.

| Study | Uses Attention | Detail Provided |
|-------|----------------|-----------------|
| Dong 2026 | Yes (CNN-LSTM-Attn) | Minimal - "dynamically focus on temporal features" |
| Ode 2023 | Yes (Self-Attentive AE) | Provides attention heatmaps |
| Other studies | No | N/A |

**Gap:** No discussion of:
- Why attention might be useful for seizure detection/forecasting
- Whether attention improves interpretability
- What the attention weights reveal about seizure physiology
- Why bidirectional LSTMs are not used

---

### 2.6 Anomaly Detection vs Supervised Learning

**Currently Covered:** The discussion notes anomaly detection as a distinct paradigm.

**Missing Analysis:**

| Aspect | Current Coverage | Missing |
|--------|------------------|---------|
| Performance comparison | Mentions both exist | Direct comparison shows anomaly has 20-70x higher FPR |
| When to use which | Not discussed | Anomaly better when labeled data scarce |
| Clinical viability | Not analyzed | Anomaly NOT viable for autonomous deployment |
| Interpretability | Not discussed | Anomaly worse than supervised |

**Gap:** The discussion does not address when anomaly detection is preferable to supervised approaches, despite clear performance differences.

---

### 2.7 Computational Deployment Considerations

**Currently Covered:** Brief mention of "global models enable on-device deployment" and "112 ms inference time."

**Missing Analysis:**

| Aspect | Studies Reporting | Gap |
|--------|-------------------|-----|
| Energy/battery consumption | **0/13** | Critical for wearable deployment |
| Memory requirements | 1/13 (Spahr) | Not assessed for most approaches |
| Real-time feasibility claims | 2/13 | Rarely validated |
| Cloud vs on-device trade-offs | Mentioned | Not analyzed in depth |
| Ensemble deployability | Spahr deployed | Ensembles typically impractical |

**Gap:** The discussion notes "ensemble methods require greater computational resources" but does not analyze what this means for clinical deployment or which architectures are actually feasible on low-power wearables.

---

### 2.8 Personalization vs Architecture Interaction

**Currently Covered:** Personalization strategies are discussed (global, patient-specific, mixed).

**Missing Analysis:**

1. **Architecture impact on personalization:** Do certain architectures (anomaly detection, attention) inherently handle patient variability better?
2. **Ensemble vs personalization:** No study compares global ensemble vs patient-specific single model
3. **Transfer learning:** Not addressed as a strategy
4. **Domain adaptation:** Not discussed

**Gap:** The discussion treats personalization and architecture as independent topics, but they interact significantly.

---

### 2.9 Feature Engineering Justification

**Currently Covered:** Handcrafted features are noted as "competitive."

**Missing Analysis:**

| Study | Feature Count | Justification Quality |
|-------|---------------|----------------------|
| Fine 2025 | 594 | **Very poor** - no rationale for most features |
| Wang 2025 | ~30-40 | Moderate - attitude angles well-justified |
| Singh Rathore 2024 | ~15-25 | Moderate - ANS-based |
| Vieluf 2025 | Not specified | Strong - seizure cycle evidence |
| Stirling 2021 | ~15 | **Very strong** - with empirical validation |
| Borujeny 2013 | 3 | Weak - simplistic |

**Gap:** No critique of the "594 features" approach or discussion of overfitting concerns. No analysis of which feature types (cyclic, ANS-based, motor) are theoretically justified vs arbitrary.

---

### 2.10 Temporal Aspects of Architecture Design

**Problem:** Window size and sequence length choices are not justified.

| Study | Window/Sequence | Justification Provided |
|-------|----------------|------------------------|
| Detection studies | 4 s - 5 min | Rarely |
| Forecasting studies | 30 s - 60 min | Stirling provides 7-day rationale |
| Optimal window analysis | **0/13** | None |

**Gap:** No discussion of how window size affects:
- Detection latency vs false positive trade-off
- Computational requirements
- Physiological plausibility (what time scales contain seizure information?)

---

## 3. Additional Topics Not Currently Addressed

### 3.1 Architecture Evolution Trends

**Observation:** From 2013-2026, architectures have evolved from simple ANN to complex hybrid designs, but this is not analyzed.

| Period | Dominant Architecture | Trend |
|--------|----------------------|-------|
| 2013-2019 | ANN, KNN | Traditional ML |
| 2020-2022 | LSTM (forecasting) | First DL approaches |
| 2023-2026 | Ensembles, Hybrids, Attention | Increasing complexity |

**Gap:** Is this complexity justified by performance gains, or is it a trend toward over-engineering?

---

### 3.2 Transformer/Modern Architecture Absence

**Observation:** No studies use Transformers, despite their dominance in other time-series domains.

**Gap:** Discussion should address whether Transformers are worth exploring for seizure detection/forecasting.

---

### 3.3 Model Size and Overfitting

**Observation:** Several studies use very large models relative to dataset size.

| Study | Parameters (est.) | Dataset Size | Concern |
|-------|-------------------|--------------|---------|
| Fine 2025 | 594 features input | n=5 | High overfitting risk |
| Nasseri 2021 | 4 x 128 LSTM | n=6 | Patient-specific only |
| Elemam 2025 | Not specified | n=30 | Unknown |

**Gap:** No discussion of model size vs data requirements.

---

## 4. Recommendations for Enhanced Discussion

### 4.1 Add: Critical Analysis of Architecture Reporting

```latex
\subsubsection{Architecture Reporting Heterogeneity}

Architecture descriptions vary substantially in completeness across studies.
Some studies report complete layer-by-layer specifications while others
provide minimal information. This variability complicates direct comparison
and replication. For example, Elemam et al. (2025) use a CNN for audio-based
detection but do not specify the number of layers, filter sizes, or input
dimensions. Reintjes et al. (2025) use a CNN encoder within their VQ-VAE
framework but provide no architectural details. Without complete reporting,
assessing what drives performance differences becomes impossible.
```

### 4.2 Add: Performance vs Complexity Analysis

```latex
\subsubsection{Performance-Complexity Trade-offs}

More complex architectures do not consistently outperform simpler designs.
Meisel et al. (2020) compared an LSTM with 10 hidden units to 100 units and
found no improvement with increased complexity. Similarly, ensemble methods
achieve excellent sensitivity but whether they substantially outperform
single models remains unknown because no study provides single-model
baselines. The field requires systematic ablation studies to determine
optimal complexity levels rather than assuming more is better.
```

### 4.3 Add: Multi-Modal Fusion Strategy Analysis

```latex
\subsubsection{Fusion Strategy Comparison}

Multi-modal studies employ different fusion strategies without systematic
comparison. Early fusion (Meisel et al., 2020) concatenates raw multi-modal
time-series at the input layer. Intermediate fusion (Dong et al., 2026;
Singh Rathore et al., 2024) combines features after extraction. Late fusion
(Stirling et al., 2021) combines model outputs at the decision level. Only
Dong et al. (2026) provide ablation results showing combined modalities
outperform single modalities by 8.5\% AUC. Attention-based adaptive fusion
appears promising for handling noisy modalities but is only explored in
one study. The field lacks comparison of fusion strategies to determine
optimal approaches for different applications.
```

### 4.4 Add: Anomaly Detection vs Supervised Performance

```latex
\subsubsection{Supervised vs Anomaly Detection Trade-offs}

Anomaly detection approaches achieve comparable sensitivity to supervised
methods but with substantially higher false alarm rates. The best anomaly
detection methods (Reintjes et al., 2025) reach 92--98\% sensitivity but
with FPR of 3.96--26/h, an order of magnitude above clinical targets
(<0.05--0.1/h). Supervised CNN approaches (Spahr et al., 2025) achieve
96\% sensitivity with FPR of 0.0054/h. This suggests anomaly detection,
while theoretically attractive for handling patient variability without
labeled seizure data, is not currently viable for autonomous deployment.
Anomaly methods may serve as screening tools in clinician-assisted workflows
but require substantial FPR reduction before standalone use.
```

### 4.5 Add: Feature Engineering Critique

```latex
\subsubsection{Handcrafted Feature Quality}

Handcrafted feature approaches vary widely in theoretical justification.
Feature sets range from 3 basic features (Borujeny et al., 2013) to 594
features (Fine et al., 2025). Well-justified features leverage domain
knowledge about seizure physiology: cyclic features capture circadian and
multiday seizure rhythms (Stirling et al., 2021; Vieluf et al., 2025);
attitude angles capture characteristic seizure postures (Wang et al., 2025);
ANS-based features reflect autonomic changes (Singh Rathore et al., 2024).
In contrast, the 594-feature approach uses generic statistical features
without clear physiological rationale, raising overfitting concerns given
the small sample size (n=5). No study directly compares feature-based to
end-to-end learning on identical data, leaving the relative merits of each
approach unresolved.
```

---

## 5. Priority Gaps to Address

Given the 15-page constraint, prioritize addressing these gaps:

| Priority | Gap | Estimated Lines | Impact |
|----------|-----|-----------------|--------|
| **High** | Anomaly detection performance critique | 10-15 | Clarifies clinical viability |
| **High** | Feature engineering quality assessment | 10-12 | Addresses overfitting concerns |
| **Medium** | Multi-modal fusion strategy analysis | 8-10 | Provides practical guidance |
| **Medium** | Performance-complexity relationship | 8-10 | Questions trend toward complexity |
| **Low** | Architecture reporting heterogeneity | 5-8 | Methodological concern |
| **Low** | Attention mechanism discussion | 5-6 | Emerging technique |

**Total estimated addition:** 46-61 lines (approximately 1/2 - 3/4 page)

---

## 6. Sources Referenced

**CNN Architecture Analysis:**
- Spahr et al. 2025 - 1D CNN ensemble, 30 models, quantile aggregation
- Dong et al. 2026 - CNN-LSTM-Attention hybrid
- Elemam et al. 2025 - CNN for audio/HRV (poorly specified)
- Reintjes et al. 2025 - CNN encoder in VQ-VAE (unspecified)

**LSTM Architecture Analysis:**
- Meisel et al. 2020 - Minimal LSTM (10 units)
- Nasseri et al. 2021 - Deep LSTM (4 x 128 units)
- Stirling et al. 2021 - Ensemble with LSTM component
- Wang et al. 2025 - Single-layer LSTM (40 units)
- Dong et al. 2026 - CNN-LSTM hybrid

**Ensemble/Two-Stage Analysis:**
- Spahr et al. 2025 - 30-model ensemble with quantile aggregation
- Dong et al. 2026 - Two-stage pre-screening + DL
- Stirling et al. 2021 - LSTM + RF + LR ensemble

**Feature Engineering Analysis:**
- Fine et al. 2025 - 594 handcrafted features
- Wang et al. 2025 - Attitude angle features
- Singh Rathore et al. 2024 - ANS-based features
- Vieluf et al. 2025 - Harmonic/cyclic features
- Stirling et al. 2021 - Cyclic features with validation

**Multi-Modal Fusion Analysis:**
- Meisel et al. 2020 - Early fusion (raw data)
- Dong et al. 2026 - Intermediate fusion with attention
- Stirling et al. 2021 - Late fusion (ensemble)
- Vieluf et al. 2025 - Wearable + diary fusion
- Singh Rathore et al. 2024 - Feature-level fusion

**Anomaly Detection Analysis:**
- Reintjes et al. 2025 - Matrix Profile, MADRID, TimeVQVAE-AD
- Ode et al. 2023 - Self-Attentive Autoencoder

---

## 7. Summary Table: Architecture Coverage

| Architecture Aspect | Currently Discussed | Depth | Gap Severity |
|---------------------|---------------------|-------|--------------|
| Architectural diversity | Yes | Moderate | Low |
| Detection vs forecasting patterns | Yes | Good | None |
| Learning paradigms | Yes | Good | None |
| Design justifications | No | N/A | **High** |
| Feature engineering quality | Partial | Limited | **High** |
| Multi-modal fusion strategies | Partial | Limited | **Medium** |
| Anomaly vs supervised comparison | No | N/A | **High** |
| Performance-complexity relationship | No | N/A | **Medium** |
| Attention mechanisms | Mentioned | Minimal | **Medium** |
| Computational deployment | Brief | Minimal | **Medium** |
| Architecture reporting standards | No | N/A | **Low** |
| Temporal design choices | No | N/A | **Medium** |
| Transformer/modern methods | No | N/A | Low |

---

**Document Status:** Analysis complete. Ready for integration into discussion section.
