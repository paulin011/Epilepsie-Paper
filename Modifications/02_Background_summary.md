# Summary of Section 02: Theoretical Foundations for Ambulatory Seizure Monitoring

## Section Overview

This section provides the clinical and technical background necessary for understanding ambulatory seizure detection systems. It covers the requirements for wearable monitoring, the physiological biosignals used, seizure manifestations and their corresponding biosignals, and evaluation frameworks.

---

## 2.1 The Ambulatory Monitoring Paradigm: Requirements and Challenges

### Key Transition: Clinical to Ambulatory Setting

- **Source citations**: Beniczky & Chen 2021, Chen et al. 2022
- Translation from controlled clinical environments to ambulatory settings fundamentally redefines approaches and performance requirements

### Performance Metrics Trade-off

| Clinical Environment | Ambulatory Setting |
|---------------------|-------------------|
| Maximum sensitivity prioritized over FAR | Balance of both metrics required |

### Risks of Imbalanced Performance

- **Low sensitivity**: Failing to detect a seizure poses a direct safety risk
- **High FAR**: Excessive false alarms lead to "alarm fatigue" - users become desensitized and may ignore or abandon the device

### User Requirements (Sivathamboo et al. 2022)

- **Sensitivity**: High (>= 90%) required
- **Acceptable FAR thresholds**:
  - Patients with >= 1 seizure/week: 1-2 false alarms per week
  - Patients with < 1 seizure/week: 1-2 false alarms per month

### Model Complexity Considerations

- More complex models can detect more intricate patterns BUT introduce the "black-box" problem
- Lack of transparency affects user trust and regulatory compliance
- **Citations**: Abualrob 2025, Ghaderi 2025, Miron 2025

---

## 2.2 Physiological Biosignals for Wearable Sensing

### Rationale for Non-EEG Approaches

Wearable devices circumvent EEG impracticality by capturing **peripheral biosignals** that serve as proxies for central nervous system activity during seizures.

### Fundamental Limitations

- These proxies inherently relay **incomplete and noisy signals**
- **Solution**: Combination of multiple sensors is required

### Sensor Characteristics

| Sensor | Detects | Limitations |
|--------|---------|-------------|
| Accelerometer/Attitude | Muscle convulsions | Noisy in daily use - captures ALL movement |
| EDA (Electrodermal Activity) | Autonomic arousal via skin conductance (sweat gland activity) | - |

---

## 2.3 Seizure Manifestations and Corresponding Biosignals

### Core Principle

Wearable biosignals act as **peripheral proxies** for cerebral activity during seizures. Different seizure types produce distinct physiological signatures.

### Two Primary Manifestations

1. **Motor activity**
2. **Autonomic activation**

### Motor Signatures: Convulsive Seizures

- **Seizure types**: Generalized tonic-clonic (GTCS), focal-to-bilateral tonic-clonic (FBTCS)
- **Biosignal**: Accelerometry (ACC)
- **What it captures**: Movement and posture changes characteristic of ictal events
- **Citations**: Wang 2025, Wu 2024

### Autonomic Signatures

| Biosignal | Measures | Physiological Basis | Citations |
|-----------|----------|---------------------|-----------|
| EDA | Sympathetic nervous system arousal | Skin conductance changes | Jain 2017, Miron 2025 |
| ECG | Heart rate and rhythm alterations | Cardiac electrical activity | Leal 2017, Ghaderi 2025 |
| HRV | Autonomic balance dynamics | Heart rate variability quantification | Mason 2024, Pavei 2017 |
| PPG | Pulse rate and variability | Blood volume pulse (practical cardiac alternative) | Chen 2022, Seth 2023 |

### PPG vs ECG Trade-off

- PPG serves as a **practical alternative** for cardiac monitoring in wearable applications
- Can derive pulse rate and variability
- **Limitation**: Greater motion sensitivity compared to ECG

### Detection Strategy Conclusion

Multimodal fusion provides the most reliable approach for ambulatory monitoring, combining biosignals according to target seizure types.

---

## 2.4 Evaluation Frameworks: From Retrospective Analysis to Prospective Validity

### ILAE Phased Framework (Phases 0-4)

**Citations**: Beniczky 2018, Beniczky 2021

| Phase | Description | Requirements |
|-------|-------------|--------------|
| **Phase 0** | Proof of concept | - |
| **Phase 1** | Retrospective, small sample | - |
| **Phase 2** | Retrospective, larger | Minimum 10 patients with seizures, 15 recorded seizures |
| **Phase 3** | Prospective, multicenter | >= 30 seizures from >= 20 patients, real-time detection, locked algorithm, video-EEG reference standard |
| **Phase 4** | Real-world home validation | In-field evaluation in patients' homes |

### Retrospective Studies (Phases 0-2): Limitations

- **Risk**: Substantial data leakage and optimistic bias
- **Cause**: Non-chronological data splits allowing future information to inform training
- **Citations**: Kalousios 2024, Wong 2023

### Pseudo-Prospective Validation

- **Solution**: Enforces chronological order
- **Method**: Train only on past seizures, test on subsequent ones
- **Benefit**: More realistic performance estimate
- **Citations**: Kalousios 2024, Lu 2025

### Phase 3: Clinical Gold Standard

**Requirements**:
- Locked algorithm
- Video-EEG reference standard
- Testing on new, unseen data from multiple centers

**ILAE Systematic Review Findings**:
- Only **three** Phase 3 studies met strict validation standards (Beniczky 2021)
- Performance demonstrated:
  - Sensitivity: **90-96%** for GTCS and FBTCS
  - FAR: **0.2-0.67 per 24 hours** (approximately 0.008-0.028/h)
- This represents the **clinically validated performance benchmark** for convulsive seizure detection

### Acceptable False Alarm Rate: Perspectives

The definition of "acceptable FAR" varies by stakeholder:

| Perspective | Sensitivity Requirement | Acceptable FAR |
|-------------|------------------------|----------------|
| **Patients/Caregivers** | 100% | ~1 false alarm per seizure OR 1/week for seizure-free patients |
| **Clinicians** | 90% (adequate) | 2/week to 1/month (depending on seizure frequency) |

**Implication**: This gap between user and clinician expectations creates fundamental tension for device development.

### Phase 4: In-Field Evaluation

- **Setting**: Patients' homes
- **Key metric**: False alarm rate per hour (FAR/h) becomes decisive for practical usability
- **Example**: Nightwatch long-term studies (Miron 2025, Shum 2021)

### Current ILAE Recommendations

**For GTCS/FBTCS detection in unsupervised patients**:
- **Recommendation**: Wearable devices may be used
- **Condition**: Where alarms can enable rapid intervention
- **Strength**: Weak/conditional recommendation
- **Evidence level**: Moderate

**For all other seizure types**:
- **Recommendation**: ILAE does NOT recommend clinical use of currently available wearable devices

---

## Key Concepts and Definitions Summary

| Term | Definition |
|------|------------|
| **Ambulatory monitoring** | Seizure detection in uncontrolled, real-world settings (outside clinical environments) |
| **Alarm fatigue** | Desensitization resulting from excessive false alarms, leading to device abandonment |
| **Peripheral proxies** | Biosignals captured outside the CNS that correlate with cerebral seizure activity |
| **Data leakage** | When model training inadvertently includes information from the test period, causing optimistic bias |
| **Pseudo-prospective** | Validation enforcing chronological data splits to simulate real-world deployment |
| **ILAE Phases** | Staged validation framework (0-4) for seizure detection algorithm development |

---

## Modalities Discussed

| Modality | Full Name | Primary Use |
|----------|-----------|-------------|
| ACC | Accelerometry | Motor signatures, movement, posture changes |
| EDA | Electrodermal Activity | Sympathetic arousal, skin conductance |
| ECG | Electrocardiography | Heart rate, rhythm alterations |
| HRV | Heart Rate Variability | Autonomic balance dynamics |
| PPG | Photoplethysmography | Pulse rate, variability (cardiac proxy) |
| EEG | Electroencephalography | Reference standard (not typically used in wearables) |

---

## Key Challenges Summary

1. **Performance trade-off**: Balancing sensitivity vs. false alarm rate
2. **Signal quality**: Peripheral biosignals are inherently incomplete and noisy
3. **User adherence**: Alarm fatigue from excessive false alarms
4. **Model transparency**: Black-box complexity vs. interpretability for trust/regulation
5. **Validation rigor**: Many studies fail to meet Phase 3 standards
6. **Stakeholder alignment**: Different expectations between patients, caregivers, and clinicians
7. **Motion artifacts**: Particularly problematic for PPG compared to ECG
8. **Limited applicability**: Current devices only recommended for GTCS/FBTCS, not other seizure types
