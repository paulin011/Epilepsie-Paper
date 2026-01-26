# Introduction Section Summary

**Source File:** `/home/paulin/Documents/Epilepsie/Sections(tex)/01_introduction3.tex`

---

## Section Structure

The introduction consists of two main subsections:
1. Problem Statement and Motivation
2. Key Research Question

---

## 1. Problem Statement and Motivation

### Background on Epilepsy

**Epilepsy Statistics:**
- Chronic neurological disorder affecting **60 million people worldwide**
- Approximately **one-third of patients** remain drug-resistant
- Source: `husseinFocalNonFocalEpilepsy2018`

### Mortality and Prevention

**Seizure-Related Deaths:**
- **69% of deaths** due to a generalized tonic-clonic seizure could have been prevented if not left unattended
- Source: `sveinssonClinicalRiskFactors2020`
- This finding **highlights the demand** for reliable and timely prediction

### Current Limitations of EEG-Based Detection

**EEG Challenges:**
- Reliable prediction through electroencephalography (EEG) is already possible
- However, **operational complexity renders EEG unsuitable for ambulatory use**
- This gap has driven experimentation with **autonomic and motion signals** for seizure detection and prediction

### Limitations of Traditional Machine Learning

**Challenges with Traditional ML:**
- Translating and analyzing **noisy and complex time-series physiological signals** has pushed traditional ML to its limits
- Traditional approaches require:
  - **Manual engineering** of data
  - **Manual cleaning** of data
  - **Manual extraction** of features
- These methods often **fail to capture**:
  - The **intricate** temporal dynamics of signals
  - The **non-linear** temporal dynamics of signals
  - The **complex** temporal dynamics of signals

### Advantages of Deep Learning

**DL Model Capabilities:**
- Designed to overcome the limitations of traditional ML
- Key abilities:
  - **Hierarchical feature extraction**
  - **Learned feature extraction**
- These capabilities **uniquely address** the limitations of manual feature engineering

### Focus of This Review

**Scope of Examination:**
- Recent advances in **time-series deep learning**
- Specific architectures of interest:
  - **Convolutional Neural Networks (CNNs)**
  - **Long Short-Term Memory networks (LSTMs)**
- **Application domain:** Seizure detection and prediction using **non-EEG wearable biosignals**

### Central Analysis Questions

The review focuses on how three key elements can converge to meet clinical requirements:

1. **Architectural Choices**
   - Selection of DL model types and configurations

2. **Training Paradigms**
   - Examples mentioned:
     - Transfer learning
     - Personalization

3. **Thorough Prospective Evaluation**
   - Rigorous validation methodologies

### Clinical Requirements for Real-World Deployment

**Stringent Requirements:**
- **High sensitivity** - detecting actual seizures
- **Minimal false alarm rates (FAR)** - avoiding unnecessary alarms

---

## 2. Key Research Question

**Primary Research Question:**

> "How do different deep learning architectures and biosignal modalities excluding EEG compare in their ability to achieve a optimal trade-off between sensitivity and false alarm rate for ambulatory seizure monitoring?"

**Key Elements of the Question:**

| Component | Specification |
|-----------|---------------|
| **Technology** | Deep learning architectures |
| **Modalities** | Biosignal modalities (excluding EEG) |
| **Outcome Measure** | Optimal trade-off between sensitivity and false alarm rate |
| **Setting** | Ambulatory seizure monitoring |

---

## Key Themes and Concepts

1. **Unmet Clinical Need:** Drug-resistant epilepsy patients need ambulatory monitoring solutions

2. **Preventable Mortality:** Majority of seizure-related deaths could be prevented with timely detection

3. **Technical Gap:** EEG works but is not suitable for ambulatory/real-world use

4. **ML Limitations:** Traditional machine learning cannot handle the complexity of physiological time-series data

5. **DL Promise:** Deep learning offers hierarchical and learned feature extraction to address these challenges

6. **Comparative Focus:** The review compares different architectures and modalities on the key clinical trade-off (sensitivity vs. false alarms)

---

## Citations Referenced

| Citation Key | Context |
|--------------|---------|
| `husseinFocalNonFocalEpilepsy2018` | Epilepsy prevalence and drug resistance statistics |
| `sveinssonClinicalRiskFactors2020` | Preventability of seizure-related deaths |

---

## Notes on Writing Style

The introduction follows the project's writing style guidelines:
- No em-dashes or semicolons used
- Direct, plain language
- Concise presentation (entire section is 35 lines)
- Clear statement of the research problem and question
- Establishes clinical motivation (69% preventable deaths)
- Establishes technical motivation (limitations of traditional ML, promise of DL)
