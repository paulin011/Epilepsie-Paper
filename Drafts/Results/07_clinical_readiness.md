# Clinical Readiness and Deployment

**Date:** 2026-01-22
**Topic:** Validation Phases, Commercialization Status, and Deployment Barriers

---

## Overview

This report assesses the **clinical readiness** of **13 wearable seizure detection and forecasting studies** for real-world deployment. Clinical readiness encompasses validation phase, device status, real-world testing, and barriers to adoption.

---

## Study Phase Distribution

### Detection Studies (n=8)

| Phase | Count | Studies | Characteristics |
|-------|-------|---------|-----------------|
| **Phase 1** | 1 | Fine 2025 | Initial validation, small test set (10 szs, 3 pts) |
| **Phase 2 (equivalent)** | 2 | Spahr 2025, Dong 2026 | Larger samples, prospective |
| **Retrospective validation** | 3 | Reintjes 2025, Wang 2025, Elemam 2025 | Hospital data analysis |
| **Case study** | 1 | Singh 2024 | Single patient, limited generalizability |
| **Early feasibility** | 1 | Borujeny 2013 | 3 patients, 2013 study |

### Forecasting Studies (n=5)

| Phase | Count | Studies | Characteristics |
|-------|-------|---------|-----------------|
| **Phase IV trial data** | 1 | Vieluf 2025 | Existing trial data, retrospective analysis |
| **Phase 2 (equivalent)** | 2 | Meisel 2020, Nasseri 2021 | Moderate samples, rigorous validation |
| **Retrospective / Feasibility** | 2 | Stirling 2021, Ode 2023 | Small samples, exploratory |

**Key Finding:** No study has achieved Phase 3 prospective validation in home settings. Detection shows more advanced validation phases.

---

## Commercial Device Status

### Commercially Available Devices

| Study | Device | Status | Availability |
|-------|--------|--------|--------------|
| **Spahr 2025** | Empatica E4 | Research device | Available for research |
| **Meisel 2020** | Empatica E4 | Research device | Available for research |
| **Nasseri 2021** | Empatica E4 | Research device | Available for research |
| **Vieluf 2025** | Embrace | Commercial | FDA-cleared for seizure detection |
| **Stirling 2021** | Fitbit | Consumer watch | Widely available |
| **Dong 2026** | NightWatch | Commercial (Europe) | Available as medical device |

### Research Prototypes

| Study | Device | Status |
|-------|--------|--------|
| **Fine 2025** | 6-axis wristband | Research prototype |
| **Wang 2025** | Biovital-P1 | Research prototype |
| **Elemam 2025** | Camera-based system | Research prototype |
| **Reintjes 2025** | Single-lead ECG patch | Research prototype |
| **Singh 2024** | Multi-modal wearable | Not specified |
| **Ode 2023** | ECG patch | Research prototype |
| **Borujeny 2013** | MICAz accelerometer | Obsolete sensor platform |

**Key Finding:** 6/13 studies use commercial devices; 7/13 use research prototypes. No device has FDA/CE approval specifically for seizure forecasting.

---

## Real-World Validation

### Hospital / EMU Settings (n=8)

| Study | Setting | Duration | Notes |
|-------|---------|----------|-------|
| **Spahr 2025** | 8 EMUs | vEEG monitoring | Multi-center prospective |
| **Fine 2025** | EMU | 1-3 days per patient | Standard of care monitoring |
| **Reintjes 2025** | Hospital (SeizeIT2) | 11,640 hours | Largest dataset |
| **Wang 2025** | Hospital | Not specified | Two hospitals |
| **Elemam 2025** | Hospital | Not specified | Mansoura University |
| **Meisel 2020** | Hospital | 2311.4 hours | LOSO validation |
| **Ode 2023** | Hospital | 85 seizures | Multiple centers |
| **Borujeny 2013** | Hospital | Not specified | Clinical environment |

### Home / Ambulatory Settings (n=6)

| Study | Setting | Duration | Validation |
|-------|---------|----------|------------|
| **Dong 2026** | Home | Up to 3 months | Prospective, 788 nights |
| **Singh 2024** | Home | 6 hours | Case study |
| **Nasseri 2021** | Ambulatory | 60+ days | Concurrent iEEG (RNS) |
| **Stirling 2021** | Home | Mean 14.6 months | Diary validation |
| **Vieluf 2025** | Home | >30 weeks | Phase IV trial data |
| **Reintjes 2025** | Real-world | 11,640 hours | Wearable ECG |

**Key Finding:** 6/13 studies include home validation. Only Nasseri 2021 achieves ambulatory validation with concurrent invasive EEG confirmation.

---

## Deployment Approaches

| Deployment | Count | Studies | Characteristics |
|------------|-------|---------|-----------------|
| **On-device** | 2 | Spahr 2025, Borujeny 2013 | Real-time, low latency |
| **Real-time armband** | 1 | Dong 2026 | NightWatch device |
| **Cloud processing** | 3 | Nasseri 2021, Ode 2023, Singh 2024 | Requires connectivity |
| **Offline / PC** | 2 | Fine 2025, Elemam 2025 | Hospital setting |
| **Smartphone app** | 1 | Stirling 2021 | Consumer device integration |
| **Not specified** | 4 | Others | - |

**Key Finding:** Only 3 studies achieve real-time on-device processing. Cloud-based approaches limit home deployment reliability.

---

## Power and Processing Requirements

| Study | Power/Processing | Notes |
|-------|------------------|-------|
| **Spahr 2025** | 112 ms inference | On-device capable |
| **Borujeny 2013** | 316 mW | Server-based processing |
| **Fine 2025** | Offline PC | Not real-time |
| **Dong 2026** | Two-stage (pre-screen + DL) | 81% data reduction |
| **Stirling 2021** | Weekly retraining | App-based |

**Key Finding:** Computational requirements vary widely. Only Spahr 2025 reports inference time compatible with real-time on-device processing.

---

## User Compliance and Acceptance

| Study | Compliance Data | Findings |
|-------|-----------------|----------|
| **Vieluf 2025** | >30 weeks wear | 70/102 patients completed |
| **Stirling 2021** | Mean 14.6 months | 11/11 completed |
| **Dong 2026** | 788 recordings | 68 patients, up to 3 months |
| **Nasseri 2021** | 60+ days per patient | 6 patients with RNS |
| **Others** | Not reported | - |

**Key Finding:** Only 4/13 studies report compliance data. Long-term monitoring (>30 weeks) is feasible but challenging.

---

## Barriers to Clinical Adoption

### 1. False Alarm Rates

| Study | FPR | Clinical Viability |
|-------|-----|-------------------|
| **Spahr 2025** | 0.005/h | Clinically viable |
| **Fine 2025** | 0.023/h | Clinically viable |
| **Dong 2026** | 0.165/h | Borderline |
| **Wang 2025** | 0.354/h | Too high |
| **Ode 2023** | 0.85/h | Too high |
| **Reintjes 2025** | 1.91-39.75/h | Unacceptable |

**Barrier:** 6/8 detection studies have FPR above clinical benchmark for home use.

### 2. Limited Seizure Type Coverage

| Study | Seizure Types | Limitation |
|-------|---------------|------------|
| **Spahr 2025** | Generalized convulsive | Only CSs |
| **Fine 2025** | Tonic seizures | Only tonic with visible movement |
| **Dong 2026** | Major nocturnal | Nocturnal only |
| **Most studies** | Motor seizures | Non-motor seizures not detected |

**Barrier:** Most approaches only detect convulsive/motor seizures, missing focal aware seizures.

### 3. Small Sample Sizes

| Study | Sample | Issue |
|-------|--------|-------|
| **Nasseri 2021** | n=6 | Too small for generalization |
| **Singh 2024** | 1 patient | Case study only |
| **Borujeny 2013** | n=3 | Too small |
| **Fine 2025** | Test: n=3 | Small test set |

**Barrier:** 4/13 studies have n < 10, limiting generalizability.

### 4. Validation Setting Limitations

- 8/13 studies conducted in hospital/EMU
- Limited real-world activity variety
- Activities of daily living not fully represented
- Nighttime studies may not capture daytime challenges

### 5. Battery and Device Considerations

- Multi-modal devices (EDA+ACC+PPG+Temp) have high power consumption
- Sampling at 32-50 Hz for ACC increases battery drain
- Continuous monitoring requires daily charging
- Patient compliance decreases with burden

### 6. Data Quality Issues

- Motion artifacts in ambulatory settings
- Skin contact problems for EDA/ECG
- Data loss during real-world use
- Signal quality degradation over time

---

## Most Clinically Advanced Approaches

### Detection

| Rank | Study | Readiness | Evidence |
|------|-------|-----------|----------|
| **1** | **Spahr 2025** | Near-commercial | 96% sens, 0.005/h FPR, prospective multicenter, on-device |
| **2** | **Dong 2026** | Home-ready | 71.6% sens, 0.165/h FPR, home validation, NightWatch device |
| **3** | **Fine 2025** | Phase 1 complete | 100% sens, 0.023/h FPR, needs Phase 3 validation |

### Forecasting

| Rank | Study | Readiness | Evidence |
|------|-------|-----------|----------|
| **1** | **Stirling 2021** | Feasibility shown | 100% patient success, 14.6-month home validation |
| **2** | **Nasseri 2021** | Ambulatory proven | AUC 0.75, concurrent iEEG validation |
| **3** | **Vieluf 2025** | Diary-integration | 82% sens, Phase IV trial data |

---

## Regulatory Status

| Device | FDA Status | CE Status | Notes |
|--------|------------|-----------|-------|
| **Empatica Embrace** | 510(k) cleared (seizure detection) | CE marked | For alerting caregivers |
| **NightWatch** | Not FDA cleared | CE approved | Available in Europe |
| **Fitbit** | Consumer device only | Consumer device | No medical claims |
| **Empatica E4** | Research use only | Research use | Not for clinical use |

**Key Finding:** No device has regulatory approval specifically for seizure forecasting.

---

## Clinical Readiness Summary

### Detection Readiness

| Criterion | Status |
|-----------|--------|
| **Phase 3 validation** | Not achieved (Spahr, Dong closest) |
| **FPR benchmark met** | 2/8 studies (Spahr, Fine) |
| **Commercial devices** | 2 available (Embrace, NightWatch) |
| **Home validation** | 3/8 studies |
| **On-device processing** | 2/8 studies |
| **Regulatory approval** | Embrace FDA 510(k) for detection |

**Overall:** Detection is approaching clinical readiness but lacks Phase 3 home validation.

### Forecasting Readiness

| Criterion | Status |
|-----------|--------|
| **Phase 3 validation** | Not achieved |
| **Clear performance benchmark** | No established benchmark |
| **Commercial devices** | None for forecasting |
| **Home validation** | 3/5 studies |
| **On-device processing** | 0/5 studies |
| **Regulatory approval** | None for forecasting |

**Overall:** Forecasting remains in feasibility stage with no clear path to clinical deployment.

---

## Recommendations for Clinical Translation

1. **Standardize validation:** Adopt ILAE guidelines for Phase 3 home validation
2. **Report patient-level success:** Both detection and forecasting should report individual patient performance
3. **FPR focus:** Detection research should prioritize FPR reduction over sensitivity gains
4. **Long-term studies:** Need >6 month home validation with real-world activity diversity
5. **Regulatory pathway:** Define clear regulatory requirements for forecasting devices
6. **User-centered design:** Incorporate patient and caregiver feedback on device acceptance

---

**End of Clinical Readiness Report**
