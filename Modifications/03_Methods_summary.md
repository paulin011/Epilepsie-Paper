# Methods Section Summary

This summary details the methodological approach for the systematic literature review on deep learning approaches and biosignal modalities for ambulatory epilepsy monitoring, based on the Methods section files.

---

## 1. Methodological Framework

The review follows two structured literature review guidelines:

- **Webster & Watson concept matrix approach** \parencite{websterAnalyzingPrepareFuture2002}
- **PRISMA principles** \parencite{tugwellPRISMA20202021}

The approach uses:
- Multi-stage search
- Transparent extraction procedures
- Structured synthesis methods

---

## 2. Search Strategy

### 2.1 Multi-Stage Process (2015-2025)

The search strategy consists of three sequential stages:

1. **Scoping Stage**
   - Platform: Google Scholar
   - Purpose: Broad coverage and identification of candidate papers

2. **Formal Queries Stage**
   - Databases:
     - IEEE Xplore
     - PubMed
     - Scopus
   - Method: Controlled keyword strings with deduplication

3. **Citation Chasing Stage**
   - Method: Backward and forward citation tracking on key papers
   - Purpose: Ensuring completeness of the search

### 2.2 PICO-Based Search Methodology

The literature search was structured using the **PICO framework** (Patient/Problem, Intervention, Comparison, Outcome) with Boolean operators (AND, OR, NOT).

#### P (Patient/Problem)
- **Definition**: Epileptic seizures in need of detection or prediction
- **Keywords**: `epilepsy`, `seizure`, `ictal`, `preictal`
- **MeSH Terms (PubMed)**: Epilepsy, Seizures

#### I (Intervention)
- **Definition**: Diagnostic method based on wearable biosignals and deep learning
- **Biosignal Keywords**:
  - `electrocardiogram`, `ECG`
  - `heart rate variability`, `HRV`
  - `photoplethysmography`, `PPG`
  - `electrodermal activity`, `EDA`
  - `accelerometer`, `ACC`
- **Technology Keywords**: `wearable`, `wearable device`
- **Method Keywords**:
  - `deep learning`, `machine learning`
  - `convolutional neural network`, `CNN`
  - `long short-term memory`, `LSTM`
  - `neural network`
- **MeSH Terms (PubMed)**: Wearable Electronic Devices, Electrocardiography, Deep Learning

#### C (Comparison)
- **Definition**: Explicit exclusion of studies focused solely on EEG as the primary modality
- **Exclusion Keywords**: `EEG`, `electroencephalography`, `iEEG`, `intracranial`
- **Search Logic**: The `NOT` operator was applied to this group in all database searches

#### O (Outcome)
- **Definition**: Metrics quantifying detection or prediction system performance
- **Keywords**:
  - `detection`, `prediction`
  - `sensitivity`, `specificity`
  - `false alarm rate`, `FAR`
  - `area under the curve`, `AUC`

### 2.3 Exploration Phase

Due to insufficient papers from the initial systematic review, an additional exploration was conducted:
- Used graph tools to visualize backlinks
- Used Gemini Deep Research feature to find relevant papers
- Result: Acquired 4 additional papers
- Final total: 13 papers
- Expanded timeframe: 2013-2026

---

## 3. Inclusion and Exclusion Criteria

### 3.1 Inclusion Criteria

Studies meeting the following criteria were included:
- Use of wearable/non-EEG autonomic signals
- Focus on seizure detection OR preictal prediction

### 3.2 Exclusion Criteria

Studies were excluded if they:
- Focused solely on EEG (EEG-only studies)
- Used invasive recordings
- Were limited to purely algorithmic simulations without human data

### 3.3 Note on EEG Exclusions

Non-EEG wearable studies that rely on video-EEG for labeling were NOT excluded. EEG-related terms were used to filter only EEG-only modalities, not to exclude studies that mention EEG solely as a reference standard.

---

## 4. Practical Filters and Reproducibility

### 4.1 Time Range
- **Primary**: 2015-2025
- **Extended**: 2013-2026 (after exploration phase)

### 4.2 Publication Type
- **Primary focus**: Journal articles
- **Exceptions made**: Some conference proceedings

### 4.3 Documentation
- All database searches were documented with:
  - Query string
  - Platform
  - Execution date
- Results were deduplicated prior to screening

---

## 5. Data Extraction

### 5.1 Concept Matrix Tables

Two concept matrix tables were created following the Webster & Watson methodology:

#### Table 1: Study Matrix

**For Detection Studies** (Table ~\ref{tab:detection-matrix}) and **Forecasting Studies** (Table ~\ref{tab:forecasting-matrix}):

| Field | Description |
|-------|-------------|
| Study identification | Author, year |
| Objective | Detection vs forecasting, seizure type |
| Design | Prospective, retrospective, pseudo-prospective, LOSO CV |
| Sample | Participant count, seizure count |
| Device and sensor location | Hardware specifics |
| Algorithm architecture | Model type and structure |
| Performance metrics | Sensitivity, specificity, FPR |
| Key limitations | Study constraints |

#### Table 2: Detailed Metrics Matrix

**For Detection Studies** (Table ~\ref{tab:detection-architecture}) and **Forecasting Studies** (Table ~\ref{tab:forecasting-architecture}):

| Field | Description |
|-------|-------------|
| Validation approach | Independent test, cross-validation, LOSO |
| Detection latency | Time from seizure onset to detection |
| Patient-level success rate | Percentage of patients with successful detection |
| Precision/PPV | Positive predictive value |
| Additional clinical metrics | HMS, IoC, AUC, F1 |
| Clinical notes | Qualitative observations |

### 5.2 Additional Extracted Dimensions

The following dimensions were extracted for narrative synthesis in Section~\ref{sec:results}:

- **Setting**: Clinical vs ambulatory
- **Modality details**: ECG/HRV, PPG, EDA, ACC
- **Evaluation granularity**: Sample-based vs alarm-based
- **Windowing specifics**: Window length, stride, overlap
- **Personalization strategies**: Global vs patient-specific
- **Interpretability and safety considerations**
- **Data characteristics and dataset identity**
- **Missing data handling**: Imputation, exclusion, synthetic data use
- **Inference requirements**: Latency, computational load, hardware

---

## 6. Study Selection Process

### 6.1 PRISMA Flow Diagram

A PRISMA-style flow diagram summarizes and visualizes:
- Screening process
- Inclusion/exclusion at each stage
- Final count of included studies

The diagram is included as Figure~\ref{fig:prisma} with the caption "PRISMA flow diagram of the study selection process."

### 6.2 Prioritization Criteria

For the synthesis phase, studies were prioritized based on:
- Inclusion of splits preserving patient-specific data
- Reporting of FAR/h (false alarm rate per hour)
- Use of external validation or cross-validation

---

## 7. Final Study Count

- **Total studies included**: 13
- **Detection studies**: 9
- **Forecasting studies**: 4
- **Timeframe covered**: 2013-2026

---

## 8. Quality Assessment Approach

The review employs:
- Transparent documentation of all search queries
- Deduplication procedures
- Structured extraction following established frameworks (Webster & Watson, PRISMA)
- Prioritization of studies with rigorous validation (LOSO, patient-specific splits)
- Two-table concept matrix approach for comprehensive yet readable comparison

---

## 9. Key References

- Webster, J. & Watson, R. (2002) - Concept matrix methodology
- Tugwell, P. et al. (2021) - PRISMA 2020 guidelines

---

*Summary created from:*
- `/home/paulin/Documents/Epilepsie/Sections(tex)/03_Methods.tex`
- `/home/paulin/Documents/Epilepsie/Sections(tex)/3.1_Search Strategy.tex`
