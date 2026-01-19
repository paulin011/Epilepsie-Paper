# Deep Learning Architecture & Biosignal Modality Comparison Framework

## Research Goal
> "How do different deep learning architectures and biosignal modalities excluding EEG compare in their ability to achieve an optimal trade-off between sensitivity and false alarm rate for ambulatory seizure monitoring?"

---

## Cross-Reference with Existing Tables

**Existing Tables in `Sections(tex)/04_Study_Comparison.tex`:**

| Table | Columns Already Captured |
|-------|---------------------------|
| **Table 1** (tab:study-matrix) | Study, Objective, Design, Sample, Device, Location, Algorithm, Sensitivity, Specificity, FPR, Key Limitation |
| **Table 2** (tab:detailed-metrics) | Study, Validation, Detect. Latency, Patient Success, Precision/PPV, Other Metrics, Clinical Notes |
| **Table 3** (tab:metrics-summary) | Metric reporting prevalence across studies |

**Legend:**
- ✅ = Already captured in existing tables
- 🆕 = New dimension to extract (not in existing tables)
- 🔗 = Partially covered, needs expansion

---

## Part 1: Comparison Dimensions (Categorization Framework)

### Category 1: Deep Learning Architecture Type

| Sub-Category | Status | Options | Description |
|-------------|--------|---------|-------------|
| **Paradigm** | 🆕 | Feature-based / End-to-end | Whether model uses handcrafted features or learns from raw data |
| **Primary Architecture** | 🔗 | CNN / LSTM / GRU / Transformer / Hybrid / Ensemble / Autoencoder / Other | Core DL architecture type (partially in "Algorithm" column) |
| **Secondary Architecture** | 🆕 | None / CNN / LSTM / Attention / etc. | For hybrid models |
| **Learning Paradigm** | 🆕 | Supervised / Semi-supervised / Unsupervised / Self-supervised | Training approach |
| **Anomaly Detection** | 🆕 | Yes / No | Uses anomaly detection (e.g., Matrix Profile, VAE) |
| **Attention Mechanism** | 🆕 | Yes / No | Uses attention layers |
| **Ensemble Method** | 🆕 | Yes / No | Uses multiple models combined (mentioned for some but not systematically) |

### Mapping to Existing Tables:
- ✅ **Algorithm** column (Table 1) captures primary architecture name
- 🆕 **Paradigm** (feature-based vs end-to-end) is NOT captured
- 🆕 **Anomaly detection** flag is NOT captured
- 🆕 **Attention mechanism** flag is NOT captured
- 🆕 **Ensemble details** beyond name are NOT captured

---

### Category 2: Biosignal Modality

| Sub-Category | Status | Options | Description |
|-------------|--------|---------|-------------|
| **Number of Modalities** | 🆕 | Single-modal / Multi-modal | How many signal types used |
| **Primary Signal** | 🔗 | ACC / ECG / PPG / EDA / HR / HRV / SpO2 / Audio / Other | Main biosignal (partially in "Device" column) |
| **Secondary Signals** | 🆕 | (list) | Additional signals for multi-modal |
| **Sensor Location** | ✅ | Wrist / Chest / Ankle / Arm / Thigh / Finger / Head / Other | Body placement (fully in "Loc." column) |
| **Signal Processing** | 🆕 | Raw / Filtered / Extracted Features | How signal is preprocessed |
| **Sampling Frequency** | 🆕 | (Hz value) | Signal sampling rate |

### Mapping to Existing Tables:
- ✅ **Device** column (Table 1) captures sensor/modality name
- ✅ **Loc.** column (Table 1) captures sensor location
- 🆕 **Number of modalities** (single vs multi) is NOT explicitly captured
- 🆕 **Secondary signals** for multi-modal are NOT systematically listed
- 🆕 **Sampling frequency** is NOT captured

---

### Category 3: Personalization Strategy

| Sub-Category | Status | Options | Description |
|-------------|--------|---------|-------------|
| **Model Scope** | 🆕 | Patient-specific / Global / Mixed | Whether model is personalized or population-based |
| **Validation Type** | 🔗 | LOSO / Patient-independent / Same-patient / K-fold | Cross-validation approach (partially in "Validation" column) |
| **Training Data** | 🆕 | Includes target patient / Excludes target patient | Whether test patient data used in training |
| **Adaptation** | 🆕 | None / Online / Transfer / Fine-tuning | Personalization mechanism |
| **Patient Selection** | 🆕 | All-consecutive / Responders-only / Subgroup | Inclusion criteria |

### Mapping to Existing Tables:
- 🔗 **Validation** column (Table 2) partially captures validation type
- 🔗 **Design** column (Table 1) partially captures study design
- 🆕 **Model scope** (global vs patient-specific) is NOT explicitly captured
- 🆕 **Training data inclusion** for test patients is NOT captured
- 🆕 **Adaptation mechanism** is NOT captured

---

### Category 4: Fusion Type (Multi-modal Only)

| Sub-Category | Status | Options | Description |
|-------------|--------|---------|-------------|
| **Fusion Stage** | 🆕 | Early / Late / Intermediate / Decision / Hybrid | When modalities are combined |
| **Fusion Method** | 🆕 | Concatenation / Attention-weighted / Gating / Ensemble / Other | How fusion is implemented |
| **Cross-Modal Attention** | 🆕 | Yes / No | Whether attention operates across modalities |

### Mapping to Existing Tables:
- 🆕 All fusion-related dimensions are NOT captured in existing tables

---

### Category 5: Performance Trade-off Configuration

| Sub-Category | Status | Options | Description |
|-------------|--------|---------|-------------|
| **Operating Points** | 🆕 | Single / Multiple / Tunable | Number of sensitivity-FAR configurations tested |
| **Optimization Target** | 🆕 | Sensitivity / FAR / HMS / AUC / Other | Primary optimization metric |
| **Threshold Strategy** | 🆕 | Fixed / Adaptive / Patient-specific | How detection threshold is set |
| **Sensitivity Range** | 🆕 | (min-max)% | Range of sensitivity values reported |
| **FAR Range** | 🔗 | (min-max) | Range of false alarm rates reported (partially in "FPR" column) |
| **Best Configuration** | 🆕 | Sens-opt / FAR-opt / HMS-opt / Balanced | Which configuration performs best |

### Mapping to Existing Tables:
- ✅ **Sens** column (Table 1) captures sensitivity value
- ✅ **FPR** column (Table 1) captures false positive rate value
- 🔗 **Sensitivity/FAR ranges** are partially captured in "Algorithm" column for some studies (e.g., "38.0%/98.16%")
- 🆕 **Number of operating points tested** is NOT systematically captured
- 🆕 **Optimization target** (sens-opt vs FAR-opt) is partially captured for Reintjes only
- 🆕 **Threshold strategy** is NOT captured

---

### Category 6: Ambulatory Deployment Factors

| Sub-Category | Status | Options | Description |
|-------------|--------|---------|-------------|
| **Real-time Capability** | 🆕 | Yes / No / Unknown | Whether system processes in real-time |
| **On-device Processing** | 🆕 | Yes / No / Cloud / Hybrid | Where computation occurs |
| **Power Consumption** | 🆕 | Reported / Not reported | Whether power/battery life discussed |
| **Device Type** | 🔗 | Research / Commercial / Prototype | Hardware used (partially in "Device" column) |
| **Deployment Setting** | 🔗 | EMU / Home / Hospital / Mixed | Validation environment (partially in "Design", "Clinical Notes") |
| **Monitoring Duration** | 🆕 | (value) | Total monitoring time in study |

### Mapping to Existing Tables:
- 🔗 **Device** column (Table 1) partially captures device type
- 🔗 **Design** column (Table 1) partially captures setting (retrospective/prospective)
- 🔗 **Clinical Notes** column (Table 2) partially captures deployment info
- 🆕 **Real-time capability** is NOT captured
- 🆕 **On-device vs cloud** is NOT captured
- 🆕 **Power consumption** is NOT captured

---

### Category 7: Data Characteristics

| Sub-Category | Status | Options | Description |
|-------------|--------|---------|-------------|
| **Sample Size** | ✅ | (n value) | Number of patients (in "Sample" column) |
| **Seizure Count** | 🔗 | (n value) | Number of seizures (partially in "Sample" column) |
| **Class Balance** | 🆕 | Balanced / Imbalanced (ratio) | Seizure vs. non-seizure ratio |
| **Dataset Split** | 🔗 | Train/Val/Test / K-fold / LOSO / Other | How data was partitioned (partially in "Validation" column) |
| **Temporal Resolution** | 🆕 | (ms/s) | Time window or epoch size |
| **Data Augmentation** | 🆕 | Yes / No | Whether augmentation used |

### Mapping to Existing Tables:
- ✅ **Sample** column (Table 1) captures sample size and partially seizure count
- 🔗 **Validation** column (Table 2) partially captures dataset split type
- 🆕 **Class balance** (seizure vs non-seizure ratio) is NOT captured
- 🆕 **Temporal resolution** (window size, epoch duration) is NOT captured
- 🆕 **Data augmentation** is NOT captured

---

### Category 8: Clinical Applicability

| Sub-Category | Status | Options | Description |
|-------------|--------|---------|-------------|
| **Seizure Types Detected** | 🔗 | (list) | Which seizure types (partially in "Objective" column) |
| **Detection Latency** | ✅ | (value) | Time from seizure onset to alarm (in "Detect. Latency" column, Table 2) |
| **False Alarm Tolerance** | 🆕 | (value) | Clinically acceptable FAR |
| **Phase** | 🔗 | Phase 1 / Phase 2 / Phase 3 / Unknown | ILAE validation phase (partially in "Design", "Clinical Notes") |
| **Regulatory Status** | 🆕 | CE / FDA / None | Regulatory approval |
| **Clinical Validation** | ✅ | Retrospective / Prospective / Both | Study design (in "Design" column) |

### Mapping to Existing Tables:
- ✅ **Detect. Latency** column (Table 2) captures detection latency
- ✅ **Design** column (Table 1) captures prospective/retrospective
- 🔗 **Objective** column (Table 1) partially captures seizure types
- 🔗 **Clinical Notes** column (Table 2) partially captures phase info
- 🆕 **False alarm tolerance** (clinically acceptable threshold) is NOT explicitly captured
- 🆕 **Regulatory status** is NOT captured

---

---

## Part 9: Focused Agent Assignments (NEW Dimensions Only)

### Priority: Extract Data NOT Already in Existing Tables

**Legend for agent focus:**
- 🆕 = NEW dimension to extract (not in existing tables)
- 🔗 = PARTIALLY covered, needs systematic extraction
- Skip = Already fully covered in existing tables

### Agent Assignments

| Agent # | Category | Focus Area | Priority |
|---------|----------|------------|----------|
| **1** | Architecture Paradigm 🆕 | Feature-based vs. End-to-end | HIGH |
| **2** | Architecture Details 🆕 | Anomaly Detection, Attention, Ensemble details | HIGH |
| **3** | Modality Count 🆕 | Single vs. Multi-modal classification | HIGH |
| **4** | Modality Details 🆕 | Secondary signals, Sampling frequency | MEDIUM |
| **5** | Personalization 🆕 | Model scope (Global vs. Patient-specific) | HIGH |
| **6** | Fusion Type 🆕 | Fusion stage, method for multi-modal studies | MEDIUM |
| **7** | Trade-off Config 🆕 | Operating points, Optimization target, Threshold strategy | HIGH |
| **8** | Deployment 🆕 | Real-time, On-device, Power consumption | HIGH |

### What NOT to Extract (Already in Tables):

Skip these - already captured in existing tables:
- ✅ Study name, Objective, Design
- ✅ Sample size (n=)
- ✅ Device name
- ✅ Sensor location (wrist, chest, etc.)
- ✅ Algorithm name
- ✅ Sensitivity value
- ✅ Specificity value
- ✅ FPR value
- ✅ Detection latency (when reported)
- ✅ Patient success rate
- ✅ Precision/PPV (when reported)
- ✅ Key limitation

---

## Part 10: Agent Scanning Instructions (Updated)

### Agent 1: Architecture Paradigm 🆕

**Task:** Extract whether each study uses feature-based or end-to-end learning

**For each paper extract:**
```
## [Paper Name]
- Paradigm: [Feature-based / End-to-end / Hybrid]
- Evidence: [quote from paper]
- Line: [line number]
```

**Search terms:** `feature extraction, handcrafted, end-to-end, raw data, deep features`

---

### Agent 2: Architecture Details 🆕

**Task:** Extract anomaly detection, attention mechanism, ensemble details

**For each paper extract:**
```
## [Paper Name]
- Anomaly Detection: [Yes/No - method if yes]
- Attention: [Yes/No - type if yes]
- Ensemble: [Yes/No - size, voting method]
- Secondary Architecture: [if applicable]
```

**Search terms:** `anomaly, attention, self-attention, transformer, ensemble, voting, bagging, matrix profile, VAE, autoencoder`

---

### Agent 3: Modality Count 🆕

**Task:** Classify each study as single-modal or multi-modal

**For each paper extract:**
```
## [Paper Name]
- Modality Count: [Single / Multi]
- If Multi: [List all signals used]
- Line: [line number]
```

**Search terms:** `multimodal, multi-modal, fusion, combined signals, accelerometer AND, ECG AND, PPG AND`

---

### Agent 4: Modality Details 🆕

**Task:** Extract secondary signals and sampling frequency

**For each paper extract:**
```
## [Paper Name]
- Primary Signal: [ACC/ECG/PPG/EDA/HR/HRV]
- Secondary Signals: [list or N/A]
- Sampling Frequency: [Hz value or N/A]
- Signal Processing: [Raw/Filtered/Features]
```

**Search terms:** `sampling frequency, Hz, sample rate, signals used, biosignals, modalities`

---

### Agent 5: Personalization 🆕

**Task:** Extract model scope (global vs. patient-specific)

**For each paper extract:**
```
## [Paper Name]
- Model Scope: [Global / Patient-specific / Mixed]
- Validation: [LOSO / Patient-independent / K-fold / Same-patient]
- Training includes test patient: [Yes/No]
- Adaptation method: [None/Online/Transfer/Fine-tune]
```

**Search terms:** `patient-specific, personalized, LOSO, leave-one-out, global model, generalization, transfer learning, fine-tuning, adaptive`

---

### Agent 6: Fusion Type 🆕 (Multi-modal only)

**Task:** Extract fusion details for multi-modal studies

**For each paper extract:**
```
## [Paper Name]
- Fusion Stage: [Early/Late/Intermediate/Decision]
- Fusion Method: [Concatenation/Attention-weighted/Gating/Ensemble]
- Cross-modal Attention: [Yes/No]
```

**Multi-modal studies:** Singh Rathore 2024, Elemam 2025, possibly others

**Search terms:** `fusion, early fusion, late fusion, feature fusion, decision fusion, concatenation, attention-weighted`

---

### Agent 7: Trade-off Configuration 🆕

**Task:** Extract operating points, optimization targets, threshold strategy

**For each paper extract:**
```
## [Paper Name]
- Operating Points: [Single/Multiple/Tunable]
- Optimization Target: [Sensitivity/FAR/HMS/AUC/Balanced]
- Threshold Strategy: [Fixed/Adaptive/Patient-specific]
- Sensitivity Range: [min-max%]
- FAR Range: [min-max]
```

**Search terms:** `operating point, sensitivity-optimized, FAR-optimized, threshold, tunable, trade-off, ROC curve, HMS`

---

### Agent 8: Deployment Factors 🆕

**Task:** Extract real-time capability, on-device processing, power consumption

**For each paper extract:**
```
## [Paper Name]
- Real-time: [Yes/No/Unknown]
- On-device: [Yes/No/Cloud/Hybrid]
- Power reported: [Yes/No]
- Device type: [Research/Commercial/Prototype]
- Deployment: [EMU/Home/Hospital/Mixed]
```

**Search terms:** `real-time, on-device, edge, cloud, offline, online, power consumption, battery, ambulatory, home monitoring`

---

## Part 11: Summary Matrix for NEW Dimensions

### Matrix A: Paradigm × Modality × Performance

| Study | Paradigm 🆕 | Modality Count 🆕 | Multi-modal Fusion 🆕 | Personalization 🆕 | Sens | FAR |
|-------|-------------|------------------|---------------------|-----------------|------|-----|
| Spahr 2025 | | | | | 96% | <1/8d |
| Reintjes 2025 | | | | | 38-98% | 1.91-39.8/h |
| Fine 2025 | | | | | 100% | 0.023/h |
| Dong 2026 | | | | | 71.6% | 0.165/h |
| Wang 2025 | | | | | 56-95% | 8.5/24h |
| Singh 2024 | | | | | 96.8% | -- |
| Elemam 2025 | | | | | 95.1% | -- |
| Borujeny 2013 | | | | | 100% | 0 |
| Vieluf 2025 | | | | | 82% | -- |
| Meisel 2020 | | | | | 51.2% | TiW 43.7% |
| Stirling 2021 | | | | | -- | AUC 0.74 |
| Nasseri 2021 | | | | | AUC 0.75 | TiW 0.9-7.2h/d |
| Ode 2023 | | | | | 74% | 0.85/h |

### Matrix B: Deployment Readiness 🆕

| Study | Real-time 🆕 | On-device 🆕 | Power 🆕 | Setting | Phase |
|-------|-------------|-------------|---------|---------|-------|
| Spahr 2025 | | | | EMU | Phase 2 |
| Dong 2026 | | | | Home/Long-term | Prospective |
| ... | | | | | |

### Matrix C: Personalization vs. Performance 🆕

| Study | Model Scope 🆕 | Validation 🆕 | Sens | FAR | Patient Success |
|-------|----------------|------------|------|-----|----------------|
| Meisel 2020 | | LOSO | 51.2% | IoC 14.1% | 30/69 (43.5%) |
| ... | | | | | |

### For Each Paper, Extract:

```
## Paper: [First Author et al. - Year]

### Category 1: Architecture
- Paradigm: [Feature-based / End-to-end]
- Primary Architecture: [CNN/LSTM/etc.]
- Secondary Architecture: [if applicable]
- Learning Paradigm: [Supervised/Unsupervised/etc.]
- Anomaly Detection: [Yes/No]
- Attention: [Yes/No]
- Ensemble: [Yes/No]

### Category 2: Modality
- Number of Modalities: [Single/Multi]
- Primary Signal: [ACC/ECG/etc.]
- Secondary Signals: [list]
- Sensor Location: [Wrist/Chest/etc.]
- Sampling Frequency: [Hz]

### Category 3: Personalization
- Model Scope: [Patient-specific/Global/Mixed]
- Validation Type: [LOSO/Patient-independent/etc.]
- Training Data: [Includes/Excludes target patient]
- Adaptation: [None/Online/Transfer/etc.]

### Category 4: Fusion (if multi-modal)
- Fusion Stage: [Early/Late/etc.]
- Fusion Method: [Concatenation/Attention/etc.]
- Cross-Modal Attention: [Yes/No]

### Category 5: Performance Trade-off
- Operating Points: [Single/Multiple]
- Optimization Target: [Sens/FAR/HMS/AUC]
- Threshold Strategy: [Fixed/Adaptive/etc.]
- Sensitivity Range: [x%-y%]
- FAR Range: [x-y]

### Category 6: Ambulatory Deployment
- Real-time: [Yes/No]
- On-device: [Yes/No/Cloud]
- Power: [Reported/Not reported]
- Device Type: [Research/Commercial]
- Deployment Setting: [EMU/Home/Hospital]

### Category 7: Data Characteristics
- Sample Size: [n=]
- Seizure Count: [n=]
- Dataset Split: [Train/Val/Test etc.]

### Category 8: Clinical Applicability
- Seizure Types: [list]
- Detection Latency: [value]
- Phase: [1/2/3]
- Clinical Validation: [Retro/Prospective]

### Key Performance Summary:
- Best Sensitivity: [%] at [FAR]
- Best FAR: [value] at [Sens]
- Optimal Trade-off: [description]
```

---

## Part 3: Analysis Templates for Synthesis

### Template 1: Architecture vs. Performance Matrix

```
| Architecture Type | Sensitivity | FAR | Studies | Notes |
|-------------------|-------------|-----|---------|-------|
| CNN-only | | | | |
| LSTM-only | | | | |
| CNN+LSTM | | | | |
| Transformer | | | | |
| Anomaly Detection | | | | |
| Ensemble | | | | |
```

### Template 2: Modality vs. Performance Matrix

```
| Modality | Sensitivity | FAR | Studies | Notes |
|----------|-------------|-----|---------|-------|
| ACC only | | | | |
| ECG only | | | | |
| PPG only | | | | |
| ACC+ECG | | | | |
| ACC+EDA | | | | |
| Multi (3+) | | | | |
```

### Template 3: Personalization vs. Performance Matrix

```
| Personalization | Sensitivity | FAR | Studies | Notes |
|----------------|-------------|-----|---------|-------|
| Global model | | | | |
| Patient-specific | | | | |
| LOSO validated | | | | |
```

### Template 4: Trade-off Analysis Matrix

```
| Study | Multiple Operating Points? | Sens Range | FAR Range | Tunable? | Optimization Target |
|-------|---------------------------|------------|-----------|----------|---------------------|
| | | | | | |
```

---

## Part 4: Guiding Questions for Synthesis

### Q1: Architecture-Performance Relationship
- Which architecture types achieve the best sensitivity-FAR trade-off?
- Do end-to-end approaches outperform feature-based methods?
- Does attention mechanism improve trade-off?
- Do ensembles provide better generalization?

### Q2: Modality-Performance Relationship
- Which single modality performs best?
- Does multi-modal fusion improve trade-off?
- Which modality combinations are most effective?
- How does sensor location affect performance?

### Q3: Personalization-Performance Relationship
- How much does patient-specific tuning improve trade-off?
- What is the performance gap between global and LOSO-validated models?
- Which patients benefit most from personalization?

### Q4: Clinical Deployment Readiness
- Which approaches meet ILAE Phase 3 benchmarks?
- What are the minimum requirements for ambulatory deployment?
- Which factors most limit real-world applicability?

---

## Part 5: Agent Instructions for Systematic Scanning

### Agent Task Assignment Template

```
AGENT [N]: Scan Papers for [CATEGORY NAME]

Papers to scan:
1. [Paper 1]
2. [Paper 2]
...

For each paper, extract:
- [Sub-category 1]: [value]
- [Sub-category 2]: [value]
...

Return format:
## [Paper Name]
| Sub-category | Value |
|-------------|-------|
...
```

### Example Agent Assignments

**Agent 1: Category 1 (Architecture)**
- Scan all papers for architecture type, paradigm, ensemble usage, attention, anomaly detection

**Agent 2: Category 2 (Modality)**
- Scan all papers for biosignal types, sensor locations, sampling frequencies

**Agent 3: Category 3 (Personalization)**
- Scan all papers for model scope, validation type, personalization strategy

**Agent 4: Category 4 (Fusion)**
- Scan multi-modal papers for fusion type, method, cross-modal attention

**Agent 5: Category 5 (Trade-offs)**
- Scan all papers for operating points, optimization targets, sensitivity/FAR ranges

**Agent 6: Category 6 (Ambulatory)**
- Scan all papers for real-time capability, on-device processing, deployment setting

---

## Part 6: Output Format for Synthesis

### Paper-Level Summary Format

```markdown
## [First Author et al. - Year]

### Quick Reference
- **Architecture**: [Type] | **Paradigm**: [Feature-based/End-to-end]
- **Modality**: [Single/Multi] | **Signals**: [list]
- **Personalization**: [Global/Patient-specific] | **Validation**: [LOSO/etc.]
- **Best Sens**: [%] @ [FAR] | **Best FAR**: [value] @ [Sens]

### Architecture Details
- Primary: [description]
- Secondary: [description]
- Notable: [unique features]

### Modality Details
- Primary signal: [details]
- Fusion approach: [if applicable]
- Sensor placement: [details]

### Performance Trade-off
- Multiple configurations: [Yes/No]
- Sensitivity range: [x-y%]
- FAR range: [x-y]
- Optimal configuration: [description]

### Deployment Readiness
- Real-time: [Yes/No]
- On-device: [Yes/No]
- Setting: [EMU/Home/etc.]
- Phase: [1/2/3]
```

---

## Part 7: Quality Checklist

For each extracted data point:
- [ ] Source line number provided
- [ ] Value directly quoted from paper
- [ ] Interpretation verified
- [ ] Consistent across agents
- [ ] Ready for synthesis

---

## Part 8: Synthesis Matrix Templates

### Matrix A: Architecture × Modality × Performance

| Architecture | Modality | Best Sens | Best FAR | Study Count | Representative Studies |
|-------------|----------|-----------|----------|-------------|----------------------|
| CNN | ACC | | | | |
| CNN | ECG | | | | |
| LSTM | ACC | | | | |
| LSTM+ECG | | | | | |
| Ensemble | Multi | | | | |

### Matrix B: Personalization × Performance Gap

| Validation | Mean Sens | Mean FAR | Patient Success | Study Count |
|------------|-----------|-----------|-----------------|-------------|
| LOSO | | | | |
| Patient-independent | | | | |
| Patient-specific | | | | |
| K-fold (mixed) | | | | |

### Matrix C: Deployment Readiness Scorecard

| Study | Real-time | On-device | Phase | Setting | Sens | FAR | Readiness Score |
|-------|-----------|-----------|-------|---------|------|-----|-----------------|
| | | | | | | | |

---

## Part 9: Automated Scanning Script Template

```bash
# Example grep commands for systematic scanning

# Find architecture mentions
grep -i "CNN\|LSTM\|transformer\|attention\|ensemble" all_papers_md/*.md

# Find modality mentions
grep -i "accelerometer\|ECG\|PPG\|EDA\|heart rate" all_papers_md/*.md

# Find personalization mentions
grep -i "LOSO\|patient-specific\|personalized\|individual" all_papers_md/*.md

# Find performance metrics
grep -i "sensitivity\|specificity\|FAR\|false alarm" all_papers_md/*.md
```

---

## Part 10: Final Synthesis Structure

```markdown
# Synthesis: DL Architectures & Modalities for Seizure Monitoring

## Executive Summary
[Key findings in 3-4 bullet points]

## 1. Architecture Analysis
### 1.1 CNN-based Approaches
### 1.2 LSTM-based Approaches
### 1.3 Hybrid/Ensemble Approaches
### 1.4 Anomaly Detection Approaches

## 2. Modality Analysis
### 2.1 Single-Modal Performance
### 2.2 Multi-Modal Fusion
### 2.3 Optimal Modality Combinations

## 3. Personalization Analysis
### 3.1 Global vs. Patient-Specific
### 3.2 Validation Rigor Impact
### 3.3 Responder Identification

## 4. Trade-off Analysis
### 4.1 Achievable Performance Ranges
### 4.2 Configuration Flexibility
### 4.3 Clinical Thresholds

## 5. Deployment Readiness
### 5.1 Real-time Capable Systems
### 5.2 Ambulatory Validated Systems
### 5.3 Commercial Readiness

## 6. Recommendations
### 6.1 For Researchers
### 6.2 For Clinicians
### 6.3 For Industry

## 7. Future Directions
### 7.1 Architecture Innovations Needed
### 7.2 Modality Combinations to Explore
### 7.3 Validation Infrastructure Gaps
```

---

## Quick Reference for Agent Assignment

| Agent # | Category | Key Search Terms |
|---------|----------|-------------------|
| 1 | Architecture | CNN, LSTM, GRU, transformer, attention, ensemble, autoencoder, end-to-end |
| 2 | Modality | accelerometer, ECG, PPG, EDA, heart rate, HRV, SpO2, multimodal |
| 3 | Personalization | LOSO, patient-specific, global, personalized, transfer learning, adaptation |
| 4 | Fusion | early fusion, late fusion, intermediate fusion, decision fusion, concatenation |
| 5 | Trade-offs | sensitivity, FAR, false alarm, operating point, threshold, optimization |
| 6 | Ambulatory | real-time, on-device, edge, cloud, power, battery, ambulatory, home |
| 7 | Data | sample size, seizure count, training, validation, cross-validation |
| 8 | Clinical | detection latency, phase, prospective, retrospective, EMU, hospital |
