# Detailed Summary: Findings, Results, Discussion, and Conclusion

**Source:** Literature review on wearable seizure detection and forecasting using deep learning approaches (13 studies, 2013-2026)

---

## PART 1: RESULTS SECTION

### Overview
- Total participants: 912 (687 in detection studies, 225 in forecasting studies)
- 9 detection studies, 4 forecasting studies
- Publication dates: 2013-2026

---

### 1. Study Characteristics

#### Sample Size Variation
- **Detection studies**: Median 44 participants (range: 1-384)
- **Forecasting studies**: Median 11 participants (range: 6-70)
- **Total evidence base**: 687 participants (detection) + 225 participants (forecasting)

#### Study Design
- **Prospective designs** (3 studies):
  - Spahr et al. 2025: Multi-center prospective study across 8 epilepsy monitoring units
  - Dong et al. 2022: Prospective home monitoring for up to 3 months
  - Fine et al. 2025: Prospective EMU data from 15 patients for tonic seizure detection
- **Remaining studies**: Retrospective analysis of existing datasets or small-scale feasibility designs

#### Temporal Trends
- 2013-2015: Only 1 study published
- 2020-2022: 3 forecasting studies published
- 2023-2026: 9 detection studies published
- **Pattern**: Accelerated research attention on detection approaches in recent years

#### Validation Settings
- **Hospital/EMU settings**: 8 studies
- **Home/ambulatory validation**: 6 studies

#### Key Limitation
- Four studies with sample sizes below 20 participants
- Singh Rathore 2024: Single-patient case study (limited generalizability)
- Borujeny 2013: Only 3 patients evaluated
- Small samples limit reliability of performance estimates and generalizability

---

### 2. Modality Performance

#### Modality Usage Frequency
| Modality | Number of Studies | Percentage |
|----------|-------------------|------------|
| Accelerometer (ACC) | 9/13 | 69% |
| Electrodermal Activity (EDA) | 5/13 | 38% |
| ECG/HRV data | 5/13 | 38% |
| Photoplethysmography (PPG) | 4/13 | 31% |
| Gyroscope | 3/13 | 23% (detection only) |

- **Multi-modal approaches**: 9/13 studies (69%)
- **Single-modality approaches** (4 studies):
  - Spahr et al. 2025 (ACC only)
  - Reintjes et al. 2025 (ECG only)
  - Borujeny 2013 (ACC only)
  - Ode et al. 2023 (ECG RRI only)

#### Sensor Location
- **Wrist-worn**: 8 studies (62%)
- **Arm/armband**: 3 studies
- **Chest**: 1 study
- **Thigh**: 1 study
- **Multiple locations**: Borujeny 2013 (right arm, left arm, left thigh)

**Commercial devices used:**
- Empatica E4 wristband: 3 studies
- Embrace watch: 1 study
- Fitbit smartwatches: 1 study
- NightWatch armband: 1 study

#### Detection Performance by Modality

**Single-modality ACC approaches:**
- Spahr et al. 2025: 96% sensitivity with 0.0054/h FPR (lowest FPR among all detection studies)
- Borujeny 2013: 85% sensitivity using 2D ACC (only 3 patients)

**ECG-based detection:**
- High FPR variability
- Reintjes et al. 2025: Sensitivity 13.4-82.8%, FPR 0.11-65.62/h depending on method
  - Lowest FPR (0.11/h) detected only 2.44% of seizures
- Ode et al. 2023: 74% sensitivity with 0.85/h FPR using ECG RRI

**Direct modality comparison:**
- Wang et al. 2025: Attitude angle features (PITCH and ROLL) outperformed raw ACC and gyroscope
  - Achieved 56.4-95.3% sensitivity depending on feature configuration

#### Forecasting Performance by Modality
- Nasseri 2021: Combined ACC, PPG, EDA, temperature, HR → AUC 0.75 (SD 0.15)
- Meisel 2020: EDA, PPG, temperature, ACC → 51.2% sensitivity, IoC 14.1% (LOSO)
- Vieluf 2025: EDA, ACC, temperature + diary data → 24-hour harmonic patterns contain predictive information

**Key Finding:**
- Multi-modal approaches are common but not universally superior
- Single-modality ACC (Spahr 2025) achieves best FPR in detection literature
- Forecasting consistently requires multi-modal autonomic data
- AUC-ROC plateaus around 0.75 regardless of modality combination

---

### 3. Architecture and Algorithm Patterns

#### Learning Paradigms

| Paradigm | Count | Examples |
|----------|-------|----------|
| Feature-based | 4 studies | Fine 2025 (594 features), Wang 2025 (attitude angles), Singh Rathore 2024 (multi-modal features) |
| End-to-end | 2 studies | Meisel 2020 (LSTM 10 units), Nasseri 2021 (4-layer LSTM, 128 hidden) |
| Hybrid | 2 studies | Vieluf 2025 (DNN + harmonic features), Elemam 2025 (CNNs for HRV + audio) |
| Ensemble | Detection | Spahr 2025 (30 CNNs), Dong 2022 (two-stage CNN-LSTM + pre-screening) |
| Anomaly detection | 2 studies | Reintjes 2025 (3 methods compared), Ode 2023 (self-attentive autoencoder) |

#### Architecture Details by Application

**Detection:**
- CNN-based approaches dominate
- Spahr 2025: Ensemble of 30 CNN models, 14 convolutional layers each, ACC at 32 Hz, 30-second windows
- Elemam 2025: Separate CNNs for HRV and audio
- Wang 2025: LSTM with 40 hidden units for attitude angle features
- Fine 2025: ANN with 594 handcrafted features

**Forecasting:**
- LSTM architectures dominate (3 of 5 studies)
- Meisel 2020: Minimal LSTM with 10 hidden units on raw data
- Nasseri 2021: 4-layer LSTM with 128 hidden units per layer
- Stirling 2021: LSTM + RF + LR ensemble
- **No forecasting study uses CNN-based approaches**

**Window sizes:**
- Detection: 4 seconds to 5 minutes
- Forecasting: 30 seconds to 60 minutes

#### Temporal Evolution of Architectures
- **2013**: Traditional ANN (Borujeny)
- **2020-2022**: LSTM-based forecasting architectures
- **2023-2026**: Complex architectures including ensembles, hybrids, attention mechanisms

**Key Finding:**
- Detection: Architectural diversity (CNNs, LSTMs, ANNs, anomaly detection)
- Forecasting: Concentrated on LSTM variants (possibly because forecasting requires temporal dependency modeling rather than spatial patterns)

---

### 4. Architectures and Personalization

#### Personalization Strategies

| Strategy | Count | Description |
|----------|-------|-------------|
| Global models | 5 studies | Train on population data, apply to all patients |
| Patient-specific | 4 studies | Train individual models per patient |
| Mixed | 1 study | Vieluf 2025: Population harmonics + individual diary |

##### Global Models
- Spahr 2025: 384 patients, tunable parameters, 112 ms inference time
- Fine 2025: 15 patients trained, 3 tested
- Dong 2022: 68 patients, 10-fold cross-validation
- Elemam 2025: 198 questionnaire responses + 30 HRV recordings
- Meisel 2020: Global model with LOSO validation → 62% patient success (43/69 above chance)

**Advantages:** On-device processing, no individual training required
**Disadvantages:** May not capture individual seizure patterns

##### Patient-Specific Models
- Stirling 2021: Weekly retraining for 11 patients → 100% patient success
- Nasseri 2021: Separate models for 6 patients → 83% patient success (5/6)
- Ode 2023: Anomaly detection at 99% confidence for 66 patients
- Singh Rathore 2024: Single-patient case study

**Advantages:** Higher individual success rates (83-100% vs 62%)
**Disadvantages:** Cold-start problem - requires mean of 14.6 months or 60+ days of data per patient

##### Mixed Approaches
- Vieluf 2025: Population-level 24-hour harmonic patterns + individual diary data
- Results: 82% sensitivity, 67% specificity
- May balance advantages of both approaches

#### Validation Approaches
- **Subject-split**: Reintjes 2025 (train on one patient set, test on different set) - showed poor generalization
- **Temporal split**: Nasseri 2021 (early data train, later data test) - assesses temporal stability
- **LOSO**: Meisel 2020

#### Computational Considerations
- **On-device deployment**: Spahr 2025 (112 ms inference), Dong 2022 (NightWatch armband)
- **Cloud-based processing**: Nasseri 2021, Ode 2023 (potential connectivity/latency issues)
- **Smartphone-based**: Stirling 2021 (weekly retraining)

**Key Limitation:**
- Detection studies rarely report patient-level success (only 2/8 studies)
- This prevents assessment of which patients benefit from global detection models

**Trade-off Identified:**
- Patient-specific models: Higher success (83-100%) but require weeks-months of data
- Global models: Immediate deployment, on-device processing, but lower success (62%)
- Mixed approaches: May offer middle path (limited evidence)

---

### 5. Performance Metrics

#### Detection Performance
- **Sensitivity range**: 38.0% to 100%
- **High performers**:
  - Fine 2025: 100% sensitivity
  - Spahr 2025: 96% sensitivity
  - Singh Rathore 2024: 96.8% (single-patient case study)
  - Elemam 2025: 95.1% using HRV-based detection

##### False Positive Rate (FPR)
- **ILAE Phase 3 benchmark**: Below 0.05 to 0.1 per hour for home settings
- **Studies meeting benchmark** (2):
  - Spahr 2025: 0.0054/h (~1 false alarm per 8 days) - roughly 10x below clinical benchmark
  - Fine 2025: 0.023/h
- **Studies NOT meeting benchmark**:
  - Dong 2022: 0.165/h
  - Wang 2025: 0.354/h
  - Reintjes 2025: 0.11-65.62/h
  - Ode 2023: 0.85/h

**Three detection studies do not report FPR:**
- Singh Rathore 2024
- Elemam 2025
- Borujeny 2013

#### Forecasting Performance
- **Sensitivity range**: 51.2% to 82%
  - Vieluf 2025: 82% sensitivity, 67% specificity
  - Meisel 2020: 51.2% sensitivity (LOSO validation)

**Forecasting-specific metrics:**
- Meisel 2020: IoC 14.1%, TiW 43.7%
- Nasseri 2021: TiW 0.9-7.2 h/day
- Stirling 2021: Mean prediction time 37 min (hourly), 3 days (daily)

**AUC Performance:**
- Consistently 0.74-0.75 across studies
- Suggests performance ceiling for non-invasive forecasting approaches

---

### 6. Detection Versus Forecasting Comparison

#### Clinical Objectives

| Aspect | Detection | Forecasting |
|--------|-----------|-------------|
| Purpose | Identify seizures as they occur | Predict seizures before onset |
| Enables | Timely intervention during/after seizure | Preventive action, activity modification |
| Most valuable for | Generalized tonic-clonic seizures | Quality of life improvement |
| Key metrics | Sensitivity, FPR | AUC-ROC, IoC, TiW |

#### Clinical Maturity
- **Detection**: Greater clinical maturity
  - Two studies meet Phase 3 FPR benchmarks
  - Commercial devices exist (Embrace, NightWatch)
  - ILAE guidelines exist for validation

- **Forecasting**: Less mature
  - No clear clinical benchmark
  - No regulatory approval for forecasting devices
  - No standardized guidelines

#### Reporting Practices
- **Forecasting studies**: Consistently report patient-level success rates
- **Detection studies**: Rarely report individual patient outcomes (only 2/9)
- **Different metrics** complicate cross-domain comparison

**Key Finding:**
- Detection is closer to clinical translation than forecasting
- Forecasting shows consistent AUC ~0.75 but lacks benchmarks and regulatory pathways

---

### 7. Clinical Readiness and Deployment

#### Validation Phase Distribution
- **No study** has achieved Phase 3 prospective validation in home settings
- **Approaching Phase 3** (2 detection studies):
  - Spahr 2025: Prospective multi-center, 384 patients, met FPR benchmarks but in EMU (not home)
  - Dong 2022: Prospective home monitoring, 68 patients, but FPR above benchmarks
- **Phase 1**:
  - Fine 2025: Small independent test set (3 patients, 10 seizures), 100% sensitivity, 0.023/h FPR

#### Forecasting Validation Status
- Vieluf 2025: Used Phase IV trial data but retrospective analysis
- Meisel 2020, Nasseri 2021: Phase 2-equivalent validation

#### Commercial Device Status
- **FDA 510(k) clearance**: Embrace watch (detection)
- **CE approval**: NightWatch (Europe, detection)
- **No regulatory approval** for seizure forecasting devices

**Commercial devices in studies:**
- Empatica E4: 3 studies
- Embrace watch: 1 study
- NightWatch: 1 study
- Fitbit: 1 study

#### Real-World Deployment
- **6 studies** include home/ambulatory validation
  - Dong 2022: Most extensive home validation (788 overnight recordings, 3 months)
  - Stirling 2021: Longest duration (mean 14.6 months per patient)
  - Nasseri 2021: Most rigorous (concurrent invasive EEG via RNS, but only 6 patients)

- **7 studies** entirely in hospital/EMU settings
  - May not capture real-world activities that cause false alarms

#### Deployment Architecture
- **On-device/real-time** (3 studies):
  - Spahr 2025: 112 ms inference
  - Dong 2022: NightWatch armband
  - Borujeny 2013: 316 mW power consumption

- **Cloud-based** (3 studies):
  - Nasseri 2021, Ode 2023

#### Barriers to Clinical Adoption

1. **High FPR limits utility** (6/8 detection studies above acceptable thresholds)
   - Dong 2022: 0.165/h
   - Wang 2025: 0.354/h
   - Reintjes 2025: 0.11-65.62/h

2. **Limited seizure type coverage**
   - Current approaches only detect convulsive seizures with motor manifestations
   - Focal aware seizures without motor signs remain undetectable
   - ~70-75% of people with epilepsy have non-convulsive seizures not covered by ACC-based approaches

3. **Small sample sizes**
   - Four studies with <20 patients
   - Singh Rathore 2024: Single-patient case study

4. **Validation setting bias**
   - Hospital settings don't capture real-world activities (exercise, cooking, chores)

5. **Device burden and battery life**
   - Multi-modal systems consume substantial power
   - Daily charging needed, may reduce adherence

#### Most Advanced Approaches

**Detection:**
- **Spahr 2025**: Most clinically advanced
  - 384 patients, prospective multi-center
  - 96% sensitivity, 0.0054/h FPR (lowest reported)
  - 112 ms inference for on-device processing
  - Limitation: EMU setting, not home

- **Dong 2022**: Most advanced home-validated
  - 788 overnight recordings, 3 months
  - NightWatch commercial device
  - FPR 0.165/h exceeds benchmark but may be acceptable for some patients

**Forecasting:**
- **Stirling 2021**: Most clinically advanced
  - 100% patient success
  - Long home validation with consumer Fitbit devices
  - LSTM+RF+LR ensemble with weekly retraining
  - Limitation: No clear clinical benchmarks or regulatory pathways

**Key Limitation:**
- No study has achieved all requirements for clinical deployment
- All have limitations in sample size, validation setting, FPR, or generalizability
- No Phase 3 prospective home validation with sufficient sample and duration

---

## PART 2: DISCUSSION SECTION

### 1. Clinical Implications

#### Seizure Type Coverage Gap
- Current wearable approaches address only subset of seizure types
- Accelerometer-based systems: Reliable for motor manifestations
- Non-motor seizures: Difficult to detect
- ECG-based approach (Reintjes 2025): Poor sensitivity-FPR tradeoff
  - Lowest FPR detected <3% of seizures
  - Acceptable sensitivity generated FPR orders of magnitude above thresholds

**Coverage statistics:**
- Generalized convulsive seizures: ~25-30% of 50 million people with epilepsy
- Non-convulsive seizures: ~70-75% - undetectable by current ACC-based wearables
- Substantial unmet need requiring invasive monitoring or alternative biomarkers

#### Detection Readiness
- Clinically acceptable FPR achievable with ACC-based approaches
- Two studies meet ILAE Phase 3 benchmark using ACC
- Motor seizure detection has reached maturity for clinical translation

**EMU-to-Home Translation Gap:**
- Studies achieving benchmark FPR were in hospital settings
- Home environments introduce motion patterns not in EMUs (exercise, chores, etc.)
- FPR increase: 0.165/h (home) vs 0.0054/h (EMU)
- Algorithm robustness to real-world activities must become research priority

#### Forecasting Status
- Consistent performance ceiling: AUC ~0.74-0.75
- Suggests fundamental limit on pre-ictal predictability using non-invasive sensors
- Lacks standardized validation guidelines
- Clinical utility of AUC 0.75 remains uncertain

**Personalization impact:**
- Global LOSO: 43% patient success (majority receive no benefit)
- Patient-specific: 100% success but requires weeks-months of data
- Cold-start problem: Newly diagnosed patients can't wait months for protection

**Regulatory status:**
- No device has regulatory approval specifically for seizure forecasting
- Lack of clear benchmarks complicates regulatory pathway
- Research remains sparse and unfocused with different forecasting windows/methods

---

### 2. Technical Insights and Trade-offs

#### Modality Paradox
- Multi-modal approaches dominate research (69% of studies)
- But lowest FPR achieved by single-modality accelerometry (Spahr 2025)
- Sensor fusion not always necessary for reliable detection
- Biological specificity of motor manifestations may be more important than modality count

**Physiological requirements differ:**
- **Detection**: Can succeed with movement sensors alone (ictal motor manifestations produce clear ACC signals)
- **Forecasting**: Requires autonomic modalities (pre-ictal changes before symptoms)
  - All forecasting studies incorporate EDA, ECG, or temperature

#### Architecture Selection
- **Detection**: Methodological diversity (CNNs, LSTMs, ANNs, ensembles, anomaly detection)
  - Broader exploration phase
- **Forecasting**: Concentrated on LSTM variants (3 of 4 studies)
  - Different temporal demands (longer-term dependencies)

**Handcrafted features:**
- Remain competitive despite end-to-end learning trend
- Engineered features achieve excellent performance in some studies
- Purely data-driven approaches may not grasp physiological signatures

**Ensemble methods:**
- Excellent results but require greater computational resources
- Trade-off between complexity and deployability for commercial translation

#### Personalization Dilemma
- **Global models**: Immediate deployment, but only 43% patient success above chance
  - Most patients receive no meaningful protection
- **Patient-specific**: 100% success rates, but substantial data collection required
  - Cold-start problem for newly diagnosed patients
- **Mixed approaches**: May offer middle path, but limited to single study evidence

#### The False Positive Challenge

**By modality:**
- ACC-based: Can achieve FPR <0.05/h (clinically acceptable)
- ECG-based: FPR an order of magnitude higher
  - Even best ECG method exceeded clinical benchmark substantially
  - Cardiac signals alone cannot reliably distinguish seizures from normal activities

**Multi-modal fusion:**
- Does not automatically solve false positive problem
- Studies combining modalities still report FPR above clinical targets
- Challenge: Seizure-related changes similar to exercise, stress, sleep transitions

**Forecasting ceiling:**
- AUC consistency around 0.75 across methods/modalities
- Suggests fundamental limits on pre-ictal predictability
- May reflect genuine biological variability in pre-ictal states
- Requires further research on biological mechanisms

---

### 3. Limitations of the Evidence Base

#### Sample Size Constraints
- Five studies with sample sizes below 20
- Single-patient case studies, 3-patient evaluations
- Small samples limit reliability and generalizability
- Epilepsy varies drastically between patients
- Forecasting particularly affected (6-11 patients due to invasive EEG requirements)

#### Validation Setting Bias
- 8 of 13 studies in hospital/EMU settings
- Systematic bias may underestimate real-world FPR
- Hospital environments lack diversity of daily activities

#### Reporting Inconsistency
- **Forecasting**: Routinely report patient-level success rates
- **Detection**: Rarely provide individual outcomes (only 2/9 studies)
  - High aggregate sensitivity may mask patient variability
  - Model likely focuses on largest subset with similar seizure patterns
  - Bad performance for patients with irregular patterns

#### Monitoring Duration and Cold-Start Problems
- Patient-specific approaches: Weeks to months before useful
- Conflicts with clinical need for immediate protection
- Global models: Immediate deployment but lower success
- Trade-off remains unresolved without hybrid approach evidence

---

### 4. Future Directions (Nine Research Priorities)

1. **Standardized clinical benchmarks for forecasting**
   - Detection has ILAE Phase 3 benchmark (FPR <0.05-0.1/h)
   - Forecasting lacks equivalent standard
   - AUC ~0.74-0.75 consistent, but clinical meaning unclear
   - IoC and TiW need standardization
   - Field should establish minimum acceptable performance levels

2. **Large-scale home validation**
   - Only 2 detection studies with prospective home validation
   - Hospital/EMU settings don't capture real-world activities
   - Exercise, cooking, chores present challenges not in controlled environments
   - Dong 2022: 0.165/h FPR in home, exceeds benchmark but comes close
   - Future studies: Prospective validation in intended use environments

3. **Novel modalities for non-convulsive seizures**
   - Current approaches detect only motor seizures with convulsive manifestations
   - Focal aware seizures without motor signs undetectable
   - Spahr 2025: Excellent for convulsive seizures using ACC, but cannot detect without movement
   - Multi-modal autonomic approaches show promise but haven't addressed non-convulsive types
   - Novel biosignals, advanced feature engineering, or research on seizure mechanics needed

4. **Adaptive personalization strategies**
   - Global models: Immediate deployment, may not work for all
   - Meisel 2020: 43% patient success with LOSO (substantial inter-patient variability)
   - Patient-specific: Higher success but requires weeks-months
     - Stirling 2021: Mean 14.6 months per patient
     - Nasseri 2021: 6+ months (median 220 days)
   - Mixed approaches (Vieluf 2025): May balance population patterns with individual adaptation
   - Need to address cold-start problem

5. **Real-time processing and edge deployment**
   - Most studies offline on PCs/servers, not on wearable devices
   - Clinical utility demands real-time on-device for timely intervention
   - Requires low power consumption and limited memory optimization
   - Spahr 2025 exception: 112 ms inference suitable for smartwatch
   - Future work should report computational requirements and demonstrate deployment

6. **Model explainability and interpretability**
   - Deep learning (CNNs, LSTMs, autoencoders) operate as black boxes
   - Clinicians and patients need to understand what features trigger detections/forecasts
   - Nasseri 2021: Ablation studies on feature contributions
   - Reintjes 2025: Analyzed feature importance
   - Systematic interpretability frameworks missing
   - Future: Integrate explainable AI techniques

7. **Regulatory pathways and clinical integration**
   - None of reviewed studies address FDA or CE marking requirements
   - Clinical workflow integration unexplored
   - Liability considerations unexplored
   - Ethical implications remain unexplored
   - Device approval requires rigorous validation, standardized manufacturing, post-market surveillance
   - Research should engage with regulatory frameworks early

8. **Algorithm robustness and generalizability**
   - Most studies: Single-site or single-country data
   - Limits generalizability across populations and healthcare systems
   - Need multi-continental validation with diverse demographics
   - Cross-device validation lacking
   - Studies evaluate on specific hardware (Empatica E4), performance may differ on consumer devices (Apple Watch, Fitbit)
   - Standardized datasets and benchmarks needed for fair comparison

9. **Long-term algorithm stability**
   - Seizure patterns evolve due to medication changes, disease progression, physiological changes
   - Stirling 2021: Weekly retraining, acknowledging performance drift
   - No study reports systematic evaluation beyond several months
   - Longitudinal studies on performance decay needed
   - Adaptive algorithms that detect and compensate for degradation needed

---

## PART 3: CONCLUSION SECTION

### Summary of Evidence Base
- 13 studies on wearable seizure detection and forecasting using deep learning
- 912 participants total (9 detection studies, 4 forecasting studies)
- Published 2013-2026

### Key Finding 1: Accelerometer Predominance in Detection
- Six of nine detection studies rely on accelerometry
- Two studies achieving ILAE Phase 3 benchmarks both use ACC
  - Spahr 2025: 0.0054/h FPR with single-modality ACC
  - Fine 2025: 0.023/h FPR with 6-axis ACC + gyroscope band

**Implication:**
- Reflects biological reality: convulsive seizures produce distinct motor signatures extractable by deep learning
- Current approaches can only serve subset of patients with motor manifestations
- ~30% of people with epilepsy have non-convulsive seizures undetectable by movement-based approaches

### Key Finding 2: Forecasting Performance Ceiling
- Consistent AUC plateau around 0.74-0.75 across different methods, modalities, patient populations
- Suggests fundamental limit on pre-ictal predictability using non-invasive sensors
- Unlike detection (ictal motor event produces clear signal), forecasting relies on autonomic precursors
- Autonomic nervous system responds to stress, exercise, sleep transitions, other daily events
- These confounds may establish performance ceiling not breachable without EEG biomarkers or novel sensing

### Key Finding 3: Clinical Adoption Barriers
- No study has achieved all requirements for widespread clinical adoption
- Commercial detection devices exist with FDA/CE approval, but reviewed deep learning approaches lack large-scale prospective validation
- Forecasting faces additional barrier: No regulatory approval, no established clinical benchmarks
- Performance achieved to date: scientifically promising but may be insufficient for regulatory approval or clinical utility

### Clinical Pathway Forward: Three Gaps to Address

1. **Home validation at scale**
   - Bridge EMU-to-home translation gap
   - Two studies meeting FPR benchmarks conducted in hospital settings
   - Real-world deployment introduces activities/confounds not in EMU environments

2. **Standardized clinical benchmarks for forecasting**
   - Define what level of AUC, IoC, or TiW constitutes clinically meaningful performance

3. **Novel modalities/approaches for non-convulsive seizures**
   - ECG-based detection shows some promise for autonomic changes during non-motor seizures
   - Current performance remains insufficient
   - Mixed personalization strategies (population patterns + individual adaptation) may address deployability vs. performance trade-off without requiring months of data collection

---

## KEY TAKEAWAYS BY THEME

### Modality Comparison
| Aspect | Finding |
|--------|---------|
| Most common modality | Accelerometer (69% of studies) |
| Best FPR achievement | Single-modality ACC (0.0054/h) |
| Forecasting requirement | Multi-modal autonomic data (EDA, ECG, temperature) |
| Wrist-worn dominance | 62% of studies use wrist placement |
| Multi-modal vs single | 69% multi-modal, but best result is single-modality |

### Algorithm Comparison
| Aspect | Detection | Forecasting |
|--------|-----------|-------------|
| Dominant architecture | CNNs (diverse) | LSTMs (concentrated) |
| Learning paradigms | Feature-based, E2E, hybrid, ensemble, anomaly | Primarily E2E LSTM |
| Window sizes | 4 sec - 5 min | 30 sec - 60 min |
| Best performers | Spahr 2025 (30 CNN ensemble), Fine 2025 (594 features) | Stirling 2021 (LSTM+RF+LR ensemble) |

### Clinical Implications
1. **Coverage gap**: 70-75% of epilepsy patients have non-convulsive seizures not covered by current wearable approaches
2. **Detection readiness**: Two studies meet clinical benchmarks but only in EMU settings
3. **Forecasting status**: Performance ceiling at AUC ~0.75, no clinical benchmarks established
4. **Personalization dilemma**: Trade-off between immediate deployment (global, 43% success) and high performance (patient-specific, requires months of data)

### Future Directions Summary
1. Standardized forecasting benchmarks
2. Large-scale home validation
3. Novel modalities for non-convulsive seizures
4. Adaptive personalization
5. Real-time edge deployment
6. Model explainability
7. Regulatory pathway engagement
8. Multi-site generalizability validation
9. Long-term stability assessment

---

**End of Summary**
