# ECG-Based Seizure Detection/Prediction – Review Overview

## 1. Planned Sections and Topics

### 1. Introduction
- Epilepsy: prevalence, burden, and why seizure prediction matters.
- Current standard: EEG as gold standard and its limitations (invasiveness, cost, usability).
- Why ECG/HR/HRV:
  - Autonomic nervous system changes before/during seizures.
  - Availability via consumer wearables (e.g., smartwatches; connect to Heart-to-Wear findings on HR accuracy).
- Aim of the review:
  - "To systematically review methods that use ECG/heart rate/HRV to detect or predict epileptic seizures in humans."

### 2. Background: Physiology & Signals
- Basic cardiac physiology relevant to epilepsy:
  - Heart rate (HR) and heart rate variability (HRV).
  - Time-domain measures (e.g., SDNN, RMSSD, pNN50).
  - Frequency-domain measures (e.g., LF, HF, LF/HF).
  - Non-linear measures (e.g., entropy, Poincaré plot indices).
- Autonomic changes in preictal and ictal periods (sympathetic activation, ictal tachycardia).
- Differences between:
  - Clinical ECG vs PPG (smartwatches, fitness trackers).
  - Single-lead vs multi-lead ECG setups.

### 3. Problem Formulation
- Clarify the target problem:
  - Detection vs prediction:
    - Detection: classify segments as seizure vs non-seizure (often ictal vs interictal).
    - Prediction: identify preictal windows before seizures.
  - Prediction horizon and preictal period (SPH/SOP terminology if used in the literature).
- Scope: primarily focus on prediction, but include detection papers using ECG if they are influential.
- Patient-specific vs generalized models.

### 4. Datasets and Data Collection
- Summarize datasets used across papers:
  - Private clinical datasets from epilepsy monitoring units, ICUs, etc.
  - Any public datasets with ECG/HR in epilepsy (if found).
- Extract for each study:
  - Number of patients and seizures.
  - Recording duration, sampling rate, ECG leads.
  - Environment: hospital vs home/ambulatory.
  - Patient characteristics if available (age, epilepsy type, comorbidities).

### 5. Feature Engineering and Preprocessing
- ECG/HR/HRV feature types:
  - Time domain: mean HR, RR mean, SDNN, RMSSD, pNN50, etc.
  - Frequency domain: LF, HF, LF/HF, total power.
  - Non-linear features: entropy, Poincaré plot indices, fractal measures.
- Preprocessing steps:
  - Filtering, artifact removal, handling ectopic beats.
  - Segmentation (window length, overlap) and label assignment (preictal/interictal/ictal).
- For deep learning approaches:
  - Use of raw ECG, RR series, or HR sequences.
  - Any signal transforms (e.g., spectrograms) used as model input.

### 6. Model Types and Methods

#### 6.1. Classical Machine Learning
- Methods such as logistic regression, SVMs, random forests, k-NN, etc.
- Typically with hand-crafted HRV features.
- How they handle class imbalance and patient-specific vs generalized training.

#### 6.2. Deep Learning
- CNN, RNN/LSTM/GRU, CNN-LSTM hybrids, Transformers.
- Inputs: raw ECG, RR intervals, HRV sequences, or 2D transforms.
- Regularization and personalization strategies.

#### 6.3. Anomaly / Change Detection
- Unsupervised and semi-supervised approaches:
  - Autoencoders, one-class SVM, change-point detection on HR/HRV.
- Idea: learn "normal" cardiac behavior and detect preictal deviations.

### 7. Evaluation Protocols and Metrics
- Validation schemes:
  - Train/test splits, cross-validation, leave-one-seizure-out, leave-one-patient-out.
  - Discussion of data leakage issues and how studies avoid (or fail to avoid) them.
- Metrics:
  - Detection: sensitivity, specificity, accuracy, AUC-ROC, AUC-PR.
  - Prediction: seizure prediction horizon (SPH), seizure occurrence period (SOP), time in warning, false prediction rate (FPR) per hour/day.
- Compare consistency and comparability of metrics across studies.

### 8. Practical and Technical Considerations
- Signal quality and artifacts:
  - ECG vs PPG; motion artifacts; wearable device accuracy (link to Heart-to-Wear).
- Real-time vs offline analysis; computational demands for edge devices.
- Patient comfort, battery life, and practical feasibility of long-term monitoring.

### 9. Synthesis of Findings
- What works best and under which conditions:
  - Most promising feature sets and model families.
  - Typical prediction horizons achieved.
- Patterns across studies:
  - Patient-specific vs generalized performance.
  - Differences between hospital vs real-world settings.

### 10. Limitations of Existing Work
- Small sample sizes and limited diversity.
- Heterogeneous protocols and metrics making comparison difficult.
- Lack of external validation and prospective, continuous monitoring studies.

### 11. Future Directions
- Larger and more diverse ECG datasets in real-world conditions.
- Combination of ECG with other modalities (EEG, ACC, EDA, PPG).
- Standardized benchmarking protocols and open datasets.
- Clinical integration, safety, and regulatory aspects.

---

## 2. Search Keywords / Query Templates

Use and adapt these for Google Scholar, PubMed, IEEE Xplore, etc. Combine terms and restrict by year (e.g., 2010–2025).

### 2.1 Core Concept Queries

1. Broad ECG-based seizure detection/prediction
- `"epilepsy" AND ("ECG" OR "electrocardiogram" OR "heart rate" OR "heart-rate" OR "HRV" OR "heart rate variability") AND ("seizure detection" OR "seizure prediction" OR "seizure forecasting")`

2. HRV-focused approaches
- `"epileptic seizure" AND ("HRV" OR "heart rate variability") AND (prediction OR detection OR forecasting)`
- `"epilepsy" AND ("tachycardia" OR "ictal tachycardia") AND ("seizure prediction" OR "autonomic")`

3. Prediction emphasis
- `"epilepsy" AND ("ECG" OR "HRV") AND ("preictal" OR "pre-ictal" OR "prediction" OR "forecasting")`
- `"seizure prediction" AND "cardiac" AND ("heart rate" OR "HRV")`

4. Machine learning / deep learning
- `("epilepsy" OR "epileptic seizures") AND ("ECG" OR "HRV") AND ("machine learning" OR "deep learning" OR "neural network" OR "random forest" OR "support vector machine")`
- `"epileptic seizure prediction" AND ("ECG" OR "heart rate") AND ("CNN" OR "LSTM" OR "autoencoder" OR "transformer")`

5. Wearable / remote monitoring
- `"epilepsy" AND ("wearable" OR "smartwatch" OR "wrist-worn" OR "portable monitor") AND ("heart rate" OR "ECG" OR "HRV")`
- `"autonomic" AND "epilepsy" AND ("wearable" OR "remote monitoring")`

### 2.2 Filtering Tips

- Time span: focus on the last 10–15 years (e.g., since 2010).
- Humans only; deprioritize pure animal studies unless conceptually important.
- Exclude EEG-only studies unless ECG/HR/HRV is explicitly analyzed.

---

## 3. Recommended Reading Order

Think in layers: (A) Background → (B) Core ECG/HRV seizure papers → (C) Recent DL & wearable → (D) Multimodal / edge topics.

### 3.1 Layer A – Background and Conceptual Papers

1. Physiological / autonomic background
   - Papers on ictal tachycardia, autonomic changes during seizures, HRV changes in epilepsy.
   - Goal: understand why ECG/HR/HRV might carry predictive information.

2. General reviews on non-EEG seizure detection/prediction (if available)
   - Reviews that mention cardiac/ANS methods among others.
   - Use to map the space and identify key primary ECG papers.

### 3.2 Layer B – Core ECG/HRV Seizure Papers (Classical ML)

3. Older foundational works (pre-deep-learning)
   - Classical HRV-based detection/prediction using SVM, k-NN, etc.
   - Read in chronological order (oldest → ~2015) to see how:
     - Features evolved.
     - Evaluation protocols were originally designed.

4. Intermediate phase (early ML and early DL on ECG/HRV)
   - Papers introducing more advanced ML and first DL on ECG-based seizure data.
   - Focus on their experimental design and validation strategy.

### 3.3 Layer C – Recent DL and Wearable Papers

5. Recent deep learning / complex models (last ~5 years)
   - Most relevant recent DL and advanced ML studies on ECG/HRV.
   - Prioritize those with:
     - Larger/cleaner datasets.
     - Robust validation (e.g., leave-one-patient-out, separate test set).

6. Wearable / real-world studies
   - Studies using cardiac information from wearable devices (smartwatches, patches) in real-world settings.
   - Read after you know the classical and DL approaches, so you can compare:
     - Lab vs real-world performance.
     - ECG vs PPG; connect to Heart-to-Wear regarding HR measurement accuracy.

### 3.4 Layer D – Multimodal and Edge Topics

7. Multimodal ANS/physiology papers
   - Papers combining ECG with EEG, accelerometer, EDA, etc.
   - Read last to see how ECG contributes in multimodal contexts.

8. Methodology / evaluation critique papers
   - Commentaries or reviews that critique seizure prediction methodology.
   - Use them to sharpen your Discussion and Limitations sections.

---

## 4. High-Level Timeline (Example 8-Week Plan)

You can adapt this to your actual semester schedule.

### Week 1–2: Scoping and Background
- Refine the exact review question and inclusion/exclusion criteria.
- Run initial searches with the queries above.
- Identify and read:
  - 2–3 physiological/ANS/HRV epilepsy background papers.
  - 1–2 broad reviews that mention cardiac/HRV methods.
- Start a master list of candidate papers (e.g., in a spreadsheet).

### Week 2–3: Classical ECG/HRV Methods
- Select ~5–8 older/mid-range ECG/HRV seizure detection/prediction papers.
- Read them in chronological order.
- Start a structured extraction table (CSV/Excel) for each paper with:
  - Dataset, features, models, evaluation, metrics, and key findings.

### Week 3–5: Recent ML/DL and Wearable Studies
- Select ~8–12 relevant recent ML/DL and wearable studies.
- Read the most rigorous ones first (strong data and validation).
- Continue populating the extraction table.

### Week 5–6: Multimodal and Edge Topics
- Read selected multimodal and methodological critique papers.
- Note how ECG contributes and how evaluation should ideally be done.

### Week 6–8: Synthesis and Writing
- Use your extraction table to:
  - Draft Sections 4–7 (Datasets, Features, Methods, Evaluation).
  - Summarize performance patterns and practical considerations.
  - Formulate Limitations and Future Directions.
- Iterate on Introduction and Background to align with your findings.

You can adjust this timeline depending on your deadline and reading speed, but this file now gives you a central overview of sections, search strategy, and reading order.