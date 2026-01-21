# Detailed Findings Outline: Wearable Seizure Detection and Forecasting (2013-2026)

> **Scope:** Bachelor seminar paper, 15 pages total (excluding bibliography and figures)
> **Findings section:** 5 to 7 pages (the largest section)
>
> **Narrative Arc:** Technical Progress vs. Clinical Translation. The field has achieved algorithmic sophistication but remains constrained by the sensitivity-FPR trade-off, patient heterogeneity, and validation limitations.

---

## STYLE GUIDELINES (READ BEFORE WRITING)

### Punctuation Rules
- **NO em-dashes** (do not use "—" or "–")
- **NO semicolons** (use periods or commas instead)
- Use simple commas and periods only

### AI Words to Avoid
Do NOT use: crucial, pivotal, underscore, elucidate, landscape, realm, delve, leverage, robust, seamless, multifaceted, nuance, intricate, groundbreaking, state-of-the-art, cutting-edge

### Tone
- Academic but direct
- Active voice preferred
- Clear topic sentences
- One idea per sentence

---

## SECTION 3.1: OVERVIEW OF INCLUDED STUDIES (~1 page)

### Paragraph 1: Study Selection and Scope
**Topic Sentence:** The final corpus comprises 13 studies published between 2013 and 2026 that explicitly apply deep learning or artificial neural networks to wearable seizure detection or forecasting.

**Evidence to include:**
- Time span: 13 years (2013-2026) showing the evolution of DL in epilepsy monitoring
- Selection criterion: Explicit inclusion of DL/ANN approaches
- Split: 9 detection studies, 4 forecasting studies
- Recent surge: 5 studies from 2024-2026 showing accelerating interest

**Key studies to cite:** Borujeny 2013 (earliest), recent studies 2024-2026

---

### Paragraph 2: Sample Size Distribution
**Topic Sentence:** The included studies exhibit substantial variation in sample size, ranging from small pilot feasibility studies to large prospective trials.

**Evidence to include:**
- Sample size range: 3 to 384 patients
- Median approximately 15-20 patients
- Three tiers:
  - Small pilots (n < 10): Borujeny 2013 (n=3), Nasseri 2021 (n=6), Stirling 2021 (n=11)
  - Medium studies (n=10-100): Dong 2026 (n=68), Meisel 2020 (n=69), Fine 2025 (n=15+3)
  - Large studies (n > 100): Spahr 2025 (n=384), Reintjes 2025 (n=120)

**Key studies to cite:** Borujeny 2013, Spahr 2025, Reintjes 2025

---

### Paragraph 3: Settings and Validation Designs
**Topic Sentence:** The research spans multiple settings, from controlled hospital environments to fully ambulatory home monitoring.

**Evidence to include:**
- Settings continuum: EMU/hospital to home monitoring
- Detection: 7 of 9 in EMU/hospital
- Forecasting: 3 of 4 in home
- Only Dong 2026 achieved home-validated detection
- Prospective studies: Only 3 of 13 (Spahr 2025, Dong 2026, Elemam 2025)

**Key studies to cite:** Dong 2026 (home), Meisel 2020 (EMU LOSO), Nasseri 2021 (RNS)

---

### Paragraph 4: Modality Overview
**Topic Sentence:** Studies employ diverse biosignal modalities, with accelerometer-based approaches dominating detection and multi-modal methods becoming increasingly common.

**Evidence to include:**
- Modalities: ACC, ECG, PPG, EDA, HR/HRV, temperature, gyroscope
- Single-modal ACC: Spahr 2025, Borujeny 2013
- Single-modal ECG: Reintjes 2025, Ode 2023
- Multi-modal: 9 of 13 studies

**Key studies to cite:**
- Spahr 2025: ACC only, 96% sens, 0.0125/h FPR
- Reintjes 2025: ECG only, 38-98% sens
- Dong 2026: ACM+PPG multi-modal

---

### Paragraph 5: Algorithm Paradigms
**Topic Sentence:** The methodological approaches range from simple feedforward ANNs to complex ensemble systems, reflecting increasing sophistication over the 13-year period.

**Evidence to include:**
- Paradigm distribution: Feature-based (4/13), Deep learning (5/13), Anomaly (2/13), Hybrid (2/13)
- Early period: Simple architectures (Borujeny ANN, Meisel LSTM)
- Recent period: Ensemble methods, attention mechanisms

**Key studies to cite:**
- Borujeny 2013: Early ANN
- Spahr 2025: Ensemble of 30 CNN models
- Dong 2026: CNN-LSTM with attention
- Reintjes 2025: Anomaly detection

---

### Paragraph 6: Performance Overview
**Topic Sentence:** Reported performance varies widely due to differing evaluation protocols, but several studies approach or exceed clinically relevant benchmarks.

**Evidence to include:**
- Sensitivity range: 38-100% (detection), AUC 0.74-0.80 (forecasting)
- FPR range: 0 to 0.165/h among detection studies
- ILAE Phase 3 benchmark: FPR < 0.05-0.1/h

**Benchmark studies:**
- Spahr 2025: 96% sens, 0.0125/h FPR (meets benchmark)
- Fine 2025: 100% sens, 0.023/h FPR (meets benchmark)
- Dong 2026: 71.6% sens, 0.165/h FPR (above benchmark)
- Meisel 2020: 51.2% sens (LOSO, most rigorous)

---

### Paragraph 7: Key Limitations
**Topic Sentence:** Several methodological limitations restrict direct comparison across studies, including small sample sizes, inconsistent validation protocols, and heterogeneous evaluation metrics.

**Evidence to include:**
- Small samples limit generalizability (Borujeny n=3, Nasseri n=6)
- Validation inconsistency: LOSO vs temporal vs k-fold
- Metric heterogeneity: Not all report FPR, specificity
- Setting differences: EMU vs home affects FPR interpretation

---

## SECTION 3.2: BIOSIGNAL MODALITY TRENDS (~1.5 pages)

### Paragraph 1: Modality Distribution Overview
**Topic Sentence:** The thirteen studies reveal a clear preference for multi-modal approaches over single-modal signal processing in wearable seizure detection and forecasting.

**Evidence:**
- 9 of 13 studies (69%) use multi-modal approaches
- Only 4 single-modal studies: 2 ACC-based, 2 ECG-based
- All 4 forecasting studies are multi-modal by design

**Citations:**
- Multi-modal: Dong 2026, Wang 2025, Singh 2024, Fine 2025, Elemam 2025, Vieluf 2025, Nasseri 2021, Meisel 2020, Stirling 2021
- Single-modal ACC: Spahr 2025, Borujeny 2013
- Single-modal ECG: Reintjes 2025, Ode 2023

---

### Paragraph 2: Single-Modal Accelerometer Approaches
**Topic Sentence:** Accelerometer-based detection demonstrates that motion sensing alone can achieve competitive performance for convulsive seizures while maintaining computational efficiency.

**Evidence:**
- Spahr 2025 achieves best-in-class FPR of 0.0125/h with 96% sensitivity using only ACC
- Ensemble 1D CNN architecture enables strong performance without additional modalities
- Borujeny 2013 used ACC with ANN, establishing motion as viable baseline
- ACC directly captures motor manifestations of tonic-clonic seizures
- Practical advantages: low power consumption, widely available in consumer wearables

**Citations:** Spahr 2025, Borujeny 2013

**Limitation:** Motor seizures only, ineffective for focal aware or non-motor seizures

---

### Paragraph 3: Single-Modal ECG Approaches and Heterogeneity
**Topic Sentence:** Cardiac-based methods face greater performance variability than accelerometer approaches due to the indirect relationship between heart activity and seizure events.

**Evidence:**
- Reintjes 2025 shows massive heterogeneity: 38-98% sensitivity, 1.91-39.75/h FPR
- Only 55.55% of patients classified as "responders" in Reintjes 2025
- Ode 2023 achieves 74% sens with 0.85/h FPR using only RRI from ECG
- Anomaly detection paradigm used by both ECG studies (unsupervised)
- Cardiac changes during seizures are physiologically indirect compared to motor activity

**Citations:** Reintjes 2025, Ode 2023

---

### Paragraph 4: Multi-Modal Detection Advantages
**Topic Sentence:** Multi-modal detection systems consistently demonstrate improved robustness by combining complementary information about motor, autonomic, and cardiovascular seizure manifestations.

**Evidence:**
- Dong 2026: ACC+PPG achieves 71.6% sens, 0.165/h FPR, home-validated
- Singh 2024: EDA+ACC+HR achieves 96.8% sens, 94.8% spec
- Wang 2025: ACC+GYR+SEMG+EDA shows 56-95% sens range
- Fine 2025: 6-axis (ACC+Gyro) with 594 handcrafted features
- Elemam 2025: camera PPG from thumbs

**Citations:** Dong 2026, Singh 2024, Wang 2025, Fine 2025, Elemam 2025

---

### Paragraph 5: Forecasting Requires Multi-Modal by Necessity
**Topic Sentence:** All four forecasting studies rely on multi-modal inputs, reflecting the challenge of predicting seizures from pre-ictal physiological changes that are subtler than ictal manifestations.

**Evidence:**
- Vieluf 2025: EDA+ACC+Temp, 82% sens, 67% spec
- Nasseri 2021: multi-modal RNS data, AUC 0.80, 4-layer LSTM
- Meisel 2020: multi-modal LSTM, 51.2% sens, LOSO validation
- Stirling 2021: Fitbit multi-modal, ensemble LSTM+RF+LR
- Pre-ictal changes are less pronounced than ictal changes

**Citations:** Vieluf 2025, Nasseri 2021, Meisel 2020, Stirling 2021

---

### Paragraph 6: Trade-offs and Clinical Considerations
**Topic Sentence:** The choice of biosignal modality involves fundamental trade-offs between detection scope, performance stability, and practical deployment constraints.

**Evidence:**
- ACC: excellent for convulsive seizures, poor for non-convulsive
- ECG: broader seizure type coverage but high inter-patient variability (55.55% responders)
- Multi-modal: balances scope and stability but increases power consumption
- Home validation only achieved by multi-modal Dong 2026
- Patient-specific factors should guide modality selection

---

### Paragraph 7: Synthesis and Emerging Trends
**Topic Sentence:** The collective evidence suggests a trend toward hybrid architectures that leverage motion sensing for reliability while incorporating cardiac and autonomic signals to extend detection coverage.

**Evidence:**
- ACC remains foundational component in 7 of 9 multi-modal studies
- ECG/PPG increasingly incorporated for autonomic coverage
- No clear "best" modality for all patients or seizure types
- Future systems likely need adaptive modality selection
- Home validation achieved only by multi-modal approach (Dong 2026)

---

## SECTION 3.3: ALGORITHMIC PARADIGM EVOLUTION (~1.5 pages)

### Paragraph 1: Historical Context (2013-2026)
**Topic Sentence:** The algorithmic landscape has undergone substantial transformation from 2013 to 2026, evolving from early feature-based artificial neural networks to sophisticated ensemble and attention-based architectures.

**Evidence:**
- Four distinct phases of algorithmic development
- Early approaches (2013) relied on basic ANNs
- By 2020-2021, LSTM architectures emerged for forecasting
- 2023-2026 brought ensembles, attention mechanisms, anomaly detection

**Key studies:** Borujeny 2013 (early ANN), Meisel 2020 (first LSTM), Spahr 2025 (30 CNN ensemble)

---

### Paragraph 2: Feature-Based ANNs
**Topic Sentence:** Feature-based artificial neural networks represented the initial paradigm, relying on handcrafted features extracted from accelerometer and physiological signals before classification.

**Evidence:**
- Feature engineering requires domain expertise
- The paradigm persists in recent studies
- These approaches can achieve excellent performance for well-defined seizure types

**Key studies:**
- Borujeny 2013: ANN on accelerometer data
- Fine 2025: ANN with 594 handcrafted features, 100% sens, 0.023/h FPR
- Wang 2025: LSTM (40 hidden) with handcrafted features
- Singh 2024: MLP with EDA+ACC+HR features

---

### Paragraph 3: Deep Learning Emergence (CNN and LSTM)
**Topic Sentence:** The emergence of deep learning architectures, particularly CNNs and LSTMs, marked a shift toward end-to-end learning from raw or minimally processed time-series data.

**Evidence:**
- CNNs excel at extracting patterns from multi-axis accelerometer data
- LSTMs address the sequential nature of physiological signals
- These architectures reduce reliance on manual feature engineering
- The paradigm shift accelerated around 2020-2021

**Key studies:**
- Meisel 2020: LSTM with 10 units, LOSO validation
- Nasseri 2021: 4-layer LSTM (128 hidden), AUC 0.80
- Dong 2026: CNN-LSTM with attention mechanism
- Elemam 2025: CNN with rule-based fusion

---

### Paragraph 4: Anomaly Detection Paradigm
**Topic Sentence:** Anomaly detection methods offer an alternative to supervised classification by learning normal physiological patterns and flagging deviations as potential seizures.

**Evidence:**
- These methods address the challenge of limited seizure data for training
- They use unsupervised learning on predominantly interictal data
- Despite theoretical appeal for rare events, practical performance has shown limitations
- FPR remains unacceptably high

**Key studies:**
- Reintjes 2025: Matrix Profile, MADRID, TimeVQVAE on ECG
- Ode 2023: Self-Attentive Autoencoder on R-R intervals

**Paradox:** Theoretical appeal does not translate to clinical utility due to high FPR

---

### Paragraph 5: Ensemble and Hybrid Methods
**Topic Sentence:** The most recent developments (2021-2026) have focused on ensemble and hybrid approaches that combine multiple models or algorithmic strategies.

**Evidence:**
- Ensemble methods aggregate predictions to reduce variance
- Hybrid approaches combine different algorithmic families
- These methods represent the current state-of-the-art

**Key studies:**
- Spahr 2025: Ensemble of 30 CNN models with quantile aggregation
- Stirling 2021: LSTM + RF + LR ensemble, AUC 0.74
- Vieluf 2025: DNN + diary + harmonic features
- Elemam 2025: CNN + rule-based fusion

---

### Paragraph 6: The Feature-Based Paradox
**Topic Sentence:** Contrary to expectations, feature-based approaches continue to demonstrate competitive performance, creating a methodological paradox in the literature.

**Evidence:**
- Fine 2025 achieved 100% sensitivity with 0.023/h FPR using handcrafted features
- This performance matches or exceeds many deep learning approaches
- Domain knowledge embedded in feature engineering remains valuable
- Choice between paradigms depends on application context

**Key studies:** Fine 2025 vs Spahr 2025 comparison

---

### Paragraph 7: Validation Paradigms and Generalization
**Topic Sentence:** Beyond architectural choices, the evolution of validation strategies from global to patient-specific approaches has fundamentally altered how algorithmic performance is assessed.

**Evidence:**
- Global models train on pooled data but may not generalize
- Patient-specific models adapt to individual physiology
- LOSO provides intermediate assessment of generalizability
- Temporal split validation approximates real-world deployment

**Key studies:**
- Meisel 2020: LOSO validation
- Nasseri 2021: Temporal split validation
- Stirling 2021: Patient-specific weekly retraining

---

### Paragraph 8: Conclusion and Future Directions
**Topic Sentence:** The algorithmic evolution demonstrates increasing sophistication but has not yielded a single dominant paradigm, suggesting future progress may depend on hybrid approaches.

**Evidence:**
- No single paradigm dominates across all studies
- The trade-off between sensitivity and false alarm rate remains central
- Future directions include attention mechanisms and personalized adaptation

**Summary:** Feature-based ANNs remain competitive, LSTM emergence (2020-2021), Ensemble innovation (Spahr, Stirling), Anomaly detection paradox (Reintjes, Ode)

---

## SECTION 3.4: PERFORMANCE - SENSITIVITY-FPR TRADE-OFF (~1.5 pages)

### Paragraph 1: The Clinical Standard
**Topic Sentence:** The International League Against Epilepsy has established that successful home deployment requires maintaining a false positive rate below 0.05 to 0.1 false alarms per hour.

**Evidence:**
- Define ILAE Phase 3 benchmark
- Explain why FPR matters: caregiver fatigue leads to device abandonment
- Higher FPR creates alarm fatigue, users stop trusting device
- This is the primary barrier preventing translation to clinical practice

---

### Paragraph 2: Benchmark Achievement (Two Success Cases)
**Topic Sentence:** Only two of the nine detection studies meet this clinical threshold, representing just 22 percent of the literature.

**Evidence:**
- **Spahr 2025:** 96% sensitivity, 0.0125/h FPR (well below threshold)
  - Ensemble CNN, on-device, prospective validation
- **Fine 2025:** 100% sensitivity, 0.023/h FPR
  - Feature-based ANN with 594 features
  - Caveat: small sample (n=15 patients), Phase 1 study

---

### Paragraph 3: Near Misses
**Topic Sentence:** An additional group of studies approaches the benchmark but exceeds the acceptable false positive rate by 1.5 to 8.5 times the clinical threshold.

**Evidence:**
- **Dong 2026:** 71.6% sensitivity, 0.165/h FPR
  - 1.65 to 3.3 times above threshold
  - Two-stage CNN-LSTM with attention
  - Would generate excessive alarms at home
- **Ode 2023:** 74% sensitivity, 0.85/h FPR
  - 8.5 times above threshold
  - Anomaly detection using ECG RRI only

---

### Paragraph 4: Failure Cases
**Topic Sentence:** The remaining studies exhibit false positive rates that render them unsuitable for home deployment without significant algorithmic refinement.

**Evidence:**
- **Reintjes 2025:** FPR ranging from 1.91 to 39.75/h
  - Multiple anomaly detection methods tested
  - Even the best method fails clinical threshold
- **Wang 2025:** FPR of 0.354/h in table, 8.5/h in text
  - Either way exceeds acceptable threshold
- These systems would trigger 2 to 40 false alarms per hour
- Caregivers would experience alarm fatigue within hours

---

### Paragraph 5: Summary Statistics
**Topic Sentence:** Collectively these results demonstrate that false positive rate remains the primary obstacle preventing wearable seizure detection systems from achieving widespread clinical adoption.

**Evidence:**
- Only 2 of 9 studies (22%) meet ILAE Phase 3 benchmark
- 78% fail to achieve clinically acceptable FPR
- This gap persists despite advances in deep learning architectures
- The sensitivity-FPR trade-off is not solved by more complex models alone
- Algorithm innovation must prioritize specificity

---

### Paragraph 6: Innovation in Tunability
**Topic Sentence:** A notable methodological advancement comes from Spahr and colleagues, who developed a quantile-based ensemble system allowing users to adjust the sensitivity-FPR balance.

**Evidence:**
- Spahr 2025 tunability mechanism:
  - Ensemble of 30 CNN models with quantile aggregation
  - Allows adjustment based on clinical priority
  - Range from 86% sens at minimal FPR to 100% sens at moderate FPR
- This addresses a key gap: fixed thresholds do not work for all patients
- Represents move toward patient-centered configurable systems

---

### Paragraph 7: Forecasting Performance
**Topic Sentence:** Seizure forecasting systems require distinct performance metrics because they operate on a different temporal paradigm, predicting events before they occur.

**Evidence:**
- Forecasting uses AUC-ROC rather than sensitivity and FPR
- **Nasseri 2021:** AUC 0.80 (best performing)
- **Stirling 2021:** AUC 0.74, ensemble approach
- **Meisel 2020:** 51.2% sensitivity with IoC of 14.1%
- **Vieluf 2025:** TiW of 43.7%
- Forecasting evaluation framework is still evolving

---

### Paragraph 8: Conclusion
**Topic Sentence:** The performance analysis reveals a clear research priority: the field must shift focus from maximizing sensitivity alone to achieving the optimal sensitivity-FPR balance.

**Evidence:**
- Current state: 22% meeting benchmark is insufficient
- Algorithm development must optimize for specificity
- Promising directions: tunable systems, patient-specific calibration, hybrid architectures
- Without addressing FPR, even high-sensitivity systems will fail in home settings

---

## SECTION 3.5: VALIDATION RIGOR AND GENERALIZATION (~1 page)

### Paragraph 1: The Validation Spectrum
**Topic Sentence:** Validation approaches exist on a continuum of rigor, with Leave-One-Subject-Out cross-validation representing the most conservative assessment of generalizability.

**Evidence:**
- **Meisel 2020:** LOSO CV, 51.2% mean sensitivity
  - Only study using true LOSO
  - Result substantially lower than population-level k-fold
  - Represents realistic performance on unseen patients
- LOSO tests model on completely new patients
- Performance gap: LOSO yields 20-30% lower sensitivity than aggregated k-fold

---

### Paragraph 2: Subject-Split Validation
**Topic Sentence:** Subject-split validation reveals substantial performance variance that may indicate patient-specific pattern differences.

**Evidence:**
- **Reintjes 2025:** Subject-split, 38-98% sensitivity range
  - Massive 60-percentage-point variance
  - Suggests models struggle with certain patient patterns
  - Less rigorous than LOSO but more than temporal split

---

### Paragraph 3: Temporal Split Validation
**Topic Sentence:** Temporal split validation produces optimistic metrics that may not reflect performance on new patients.

**Evidence:**
- **Nasseri 2021:** Temporal split, AUC 0.80
  - Trains on early data, tests on later data from same patients
  - Within-patient patterns may be more consistent
  - Does not assess true generalization to unseen individuals

---

### Paragraph 4: Global k-Fold Validation
**Topic Sentence:** Global k-fold cross-validation produces the highest reported metrics but may substantially overestimate real-world utility.

**Evidence:**
- **Spahr 2025:** Global k-fold, 96% sensitivity
  - Aggregates across all patients in folds
  - No guarantee of patient separation
- **Dong 2026:** Global k-fold, 71.6% sensitivity
- Risk: These metrics may be optimistic for deployment on new patients

---

### Paragraph 5: Small Hold-Out Samples
**Topic Sentence:** Studies with very small sample sizes provide limited evidence about generalizability due to insufficient statistical power.

**Evidence:**
- **Fine 2025:** Hold-out, n=15 with only 3 complete datasets
  - Phase 1 study with substantial missing data
- **Borujeny 2013:** n=3 patients
  - Extremely limited sample
  - Performance cannot be generalized

---

### Paragraph 6: The EMU vs. Home Gap
**Topic Sentence:** A critical gap exists between the controlled EMU environment and real-world home settings, with most detection research remaining institution-bound.

**Evidence:**
- **Detection studies:** 7 of 9 (78%) in EMU or hospital
- **Forecasting studies:** 3 of 4 (75%) in home
- **Only home-validated detection:** Dong 2026
  - Exception that proves the rule
- EMU environment differs from home in activity patterns and adherence

---

### Paragraph 7: The Prospective Validation Gap
**Topic Sentence:** Only a minority of studies employed prospective validation, with most relying on retrospective datasets.

**Evidence:**
- **Prospective studies:** Only 3 of 13 (23%)
  - Spahr 2025: Multi-center prospective
  - Dong 2026: Prospective home cohort
  - Elemam 2025: Cross-sectional prospective
- **Retrospective studies:** 10 of 13 (77%)
- Barriers: Cost, recruitment challenges, regulatory hurdles

---

### Paragraph 8: Synthesis and Implications
**Topic Sentence:** The combination of weak validation approaches, EMU-bound data collection, and retrospective design creates substantial uncertainty about real-world performance.

**Evidence:**
- Validation rigor summary: Only Meisel 2020 uses LOSO
- Setting gap: Detection research remains in controlled environments
- Prospective gap: Most studies are retrospective
- Performance inflation risk: LOSO produces 20-30% lower sensitivity
- Dong 2026 as benchmark: 71.6% sens in prospective home represents most realistic estimate

---

## SECTION 3.6: PATIENT HETEROGENEITY (~0.5 page)

### Paragraph 1: The Clinical Reality
**Topic Sentence:** The effectiveness of wearable seizure detection varies substantially across individual patients due to differences in seizure semiology, signal quality, and physiological responses.

**Evidence:**
- Patient success rates range from 43.5% to 100%
- No single algorithm achieves uniform performance
- This variability represents a fundamental challenge for clinical deployment

**Studies:**
- Meisel 2020: 43.5% of patients achieved IoC above chance (LOSO)
- Reintjes 2025: only 55.55% showed sufficient HR elevation
- Stirling 2021: 100% with patient-specific weekly retraining

---

### Paragraph 2: Physiological Variability
**Topic Sentence:** Individual differences in autonomic nervous system responses during seizures create a fundamental limitation for systems relying on physiological signals.

**Evidence:**
- Not all patients exhibit detectable heart rate changes during seizures
- ECG-based methods require sufficient autonomic involvement
- Responder identification is a prerequisite for this modality

**Studies:**
- Reintjes 2025: only 55.55% responders (HR >50 BPM)
- Ode 2023: false positives concentrated in subset
- Nasseri 2021: 5 of 6 patients (83%) achieved above-chance forecasting

---

### Paragraph 3: Seizure Type Limitations
**Topic Sentence:** The type of seizure a patient experiences strongly determines whether a wearable detection system can be effective.

**Evidence:**
- Motion-based systems require convulsive motor activity
- Different seizure types produce different signal signatures
- Algorithm selection must be matched to seizure semiology

**Studies:**
- Spahr 2025: convulsive seizures only
- Fine 2025: tonic seizures only
- Reintjes 2025: autonomic changes only

---

### Paragraph 4: Validation Strategy Effects
**Topic Sentence:** Reported patient success rates depend heavily on validation methodology.

**Evidence:**
- LOSO validation: 43.5% success (Meisel 2020, most rigorous)
- Temporal split: 83% success (Nasseri 2021)
- Patient-specific: 100% success (Stirling 2021)

---

### Paragraph 5: Clinical Implications
**Topic Sentence:** The observed heterogeneity suggests successful clinical implementation will require adaptive systems that can identify responders and adjust to individual patient characteristics.

**Evidence:**
- No universal solution exists (43.5% to 100% range)
- Responder identification protocols are needed
- Patient-specific or adaptive models may be necessary

**Studies:**
- Reintjes 2025: implemented pre-screening for HR-responders
- Stirling 2021: demonstrated feasibility of weekly retraining

---

## SECTION 3.7: DEPLOYMENT READINESS (~0.5 page)

### Paragraph 1: Introduction to Deployment Gap
**Topic Sentence:** The translation of deep learning systems from research prototypes to clinically viable wearable devices reveals significant disparities in deployment readiness.

**Evidence:**
- Only one study (Spahr 2025) meets multiple deployment criteria
- 6 of 13 studies demonstrate real-time processing
- Only 2 of 13 validated in home environments
- ILAE Phase 3 benchmark remains primary barrier

---

### Paragraph 2: FPR as Primary Bottleneck
**Topic Sentence:** Achieving clinically acceptable false alarm rates emerges as the single most significant barrier preventing clinical translation.

**Evidence:**
- Only 2 of 9 detection studies meet ILAE Phase 3 FPR benchmark
- Median FPR approximately 0.15/h
- Offline studies show similar FPR to real-time (algorithmic, not computational bottleneck)

**Meets benchmark:**
- Spahr 2025: 0.0125/h
- Fine 2025: 0.023/h

**Above benchmark:**
- Dong 2026: 0.165/h
- Ode 2023: 0.85/h

---

### Paragraph 3: Validation Setting Gap
**Topic Sentence:** The contrast between controlled EMU environments and unstructured home settings represents a second critical dimension limiting deployment readiness.

**Evidence:**
- 11 of 13 studies validated exclusively in EMU or hospital
- Only 2 studies conducted prospective home validation
- Home-validated studies show higher FPR than EMU-only counterparts

**Home-validated:**
- Dong 2026: NightWatch, FPR 0.165/h
- Stirling 2021: Fitbit, retrospective
- Nasseri 2021: RNS, offline

---

### Paragraph 4: On-Device Processing Capability
**Topic Sentence:** Real-time processing capability varies significantly across studies with only half demonstrating the computational efficiency required for ambulatory deployment.

**Evidence:**
- 6 of 13 studies implement real-time processing
- 2 studies explicitly report on-device inference with latency
- Cloud-based approaches introduce network dependency
- Offline batch processing remains predominant (4 of 13)

**On-device with latency:**
- Spahr 2025: 112ms on TicWatch Pro 3
- Dong 2026: NightWatch on-device

**Real-time hospital:**
- Wang 2025, Elemam 2025

**Cloud:**
- Ode 2023

**Offline batch:**
- Fine 2025, Reintjes 2025, Vieluf 2025, Nasseri 2021

---

### Paragraph 5: Deployment Readiness Synthesis
**Topic Sentence:** A tripartite classification framework reveals significant heterogeneity in deployment readiness with only one system satisfying all criteria for immediate clinical translation.

**Evidence:**
- **High readiness:** Spahr 2025 (meets FPR, real-time, on-device, prospective EMU)
- **Medium-high:** Dong 2026 (fails FPR, but real-time, on-device, prospective home)
- **Medium:** Fine 2025 (meets FPR, but offline, EMU-only, small sample)
- **Medium (forecasting):** Stirling 2021, Nasseri 2021 (home, but retrospective or offline)
- **Low:** All other studies (8 of 13) fail at least two deployment criteria

---

## SUMMARY TABLE FOR REFERENCE

| Category | Studies | Key Finding |
|----------|---------|-------------|
| Modality - Single ACC | Spahr 2025, Borujeny 2013 | Excellent for convulsive, limited scope |
| Modality - Single ECG | Reintjes 2025, Ode 2023 | High heterogeneity, 55.55% responders |
| Modality - Multi-modal | 9 studies | Better FPR control, home validation achieved |
| Algorithm - Feature-based | Fine 2025, Wang 2025, Singh 2024, Borujeny 2013 | Remains competitive |
| Algorithm - Deep Learning | Spahr 2025, Dong 2026, Elemam 2025, Meisel 2020, Nasseri 2021 | Architectural sophistication |
| Algorithm - Anomaly | Reintjes 2025, Ode 2023 | Unacceptable FPR |
| Performance - Meets ILAE | Spahr 2025, Fine 2025 | Only 22% of detection studies |
| Performance - Above ILAE | Dong 2026, Ode 2023, others | 78% fail benchmark |
| Validation - LOSO | Meisel 2020 | Most rigorous, 51.2% sens |
| Validation - EMU-based | 7 of 9 detection | Limited ecological validity |
| Heterogeneity range | All studies | 43.5% to 100% success |
| Deployment - High | Spahr 2025 | Only 1 study |

---

**Generated:** 2026-01-21
**Based on:** Verified tables in Sections(tex)/04_Study_Comparison.tex
**Word count estimate:** 5-7 pages when written as full prose
