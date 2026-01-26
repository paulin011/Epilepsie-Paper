# Abstract Summary

## Background

Wearable devices using non-EEG biosignals offer potential for continuous ambulatory seizure monitoring without the burden of scalp electrodes. This systematic review examines the current state of deep learning approaches for seizure detection and forecasting using accelerometry, cardiac signals, and other wearable modalities.

## Methods

- **Guidelines followed**: PRISMA guidelines
- **Number of studies**: 13 primary studies
  - 9 detection studies
  - 4 forecasting studies
- **Publication range**: 2013 to 2026
- **Evaluation framework**: Based on Webster and Watson (2002)
- **Key metrics evaluated**:
  - Sensitivity
  - False alarm rate (FAR)
  - Validation methodology
  - ILAE phase of development

## Results

### Seizure Detection

**Performance for convulsive seizures:**
- Sensitivity range: 71.6--100%
- Primary modality: Accelerometry-based approaches

**Systems approaching ILAE Phase 3 benchmark (validated devices):**

| Study | Seizure Type | Sensitivity | FAR |
|-------|-------------|-------------|-----|
| Fine et al. | Tonic seizures | 100% | 0.023/h |
| Dong et al. | Nocturnal severe seizures | 71.6% | 0.165/h |

**ECG-based detection:**
- Consistently fails clinical utility
- Excessive FAR: 1.91--39.75/h

**Time-of-day performance:**
- Nighttime monitoring substantially outperforms daytime
- Ratio: 1/61 nights vs. 1/9 days

### Seizure Forecasting

**Current state:** Remains immature

**Performance with rigorous LOSO validation:**
- Only 43.5% of patients achieve better-than-chance performance

**Impact of patient-specific tuning:**
- Inflates performance by 30--40 percentage points
- Creates unrealistic expectations for real-world deployment

**Reliable forecasting signals:**
- Circadian patterns provide the most reliable signals
- Wearable-only features fail at daily resolution

### Validation Rigor

| Issue | Statistic |
|-------|-----------|
| Prospective designs | Only 3 of 13 studies |
| Leave-one-subject-out cross-validation | Rare |
| EMU setting validation | 11 of 13 studies |

**Key concern:** Validation in controlled epilepsy monitoring unit settings likely overestimates real-world performance.

## Conclusions

**Positive findings:**
- Wearable seizure detection for convulsive seizures has achieved clinical viability for specific use cases
- Particularly effective for nocturnal monitoring

**Challenges:**
1. **Seizure forecasting**: Faces a fundamental responder problem that prevents clinical translation
2. **False alarm rates**: Remain the primary barrier for daytime detection
3. **Real-world validation**: Urgently needed

**Future research priorities:**
1. Standardized metrics
2. Edge deployment optimization
3. Identification of baseline biomarkers to predict which patients will benefit from wearable monitoring systems

## Key Numbers Summary

| Metric | Value |
|--------|-------|
| Studies reviewed | 13 (9 detection, 4 forecasting) |
| Publication years | 2013--2026 |
| Detection sensitivity range | 71.6--100% |
| Systems near ILAE Phase 3 | 2 (Fine et al., Dong et al.) |
| Fine et al. FAR | 0.023/h |
| Dong et al. FAR | 0.165/h |
| ECG-based FAR range | 1.91--39.75/h |
| Nighttime vs. daytime performance ratio | 1/61 nights vs. 1/9 days |
| Forecasting patients with better-than-chance performance (LOSO) | 43.5% |
| Performance inflation from patient-specific tuning | 30--40 percentage points |
| Prospective validation studies | 3 of 13 |
| EMU-validated studies | 11 of 13 |
