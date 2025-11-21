# Search plan: ECG- and wearable-sensor-based prediction & detection of epileptic seizures

Purpose

- Define a reproducible literature search and study selection plan focused on seizure prediction/detection using ECG and other non-EEG sensors (PPG, accelerometer, EDA, respiration). Exclude EEG-only studies.
- Identify public and proprietary datasets suitable for model development/evaluation and list candidate ML/DL models and validation protocols informed by the review "Seizure Prediction ECG Machine Learning Review".

Scope and research questions

1. Which ECG-only and multimodal (ECG + wearable sensors) datasets exist that contain pre-ictal, ictal and inter-ictal labels suitable for prediction/detection tasks? (exclude EEG-only datasets)
2. Which feature families (time, frequency, nonlinear HRV metrics) and preprocessing pipelines are commonly used and effective for ECG-based seizure forecasting/detection?
3. Which ML/DL model families (classical ML, CNN, RNN/LSTM, hybrid CNN-LSTM, Transformer, GNN, self-supervised) have been applied to ECG/PPG-based seizure prediction or detection, and what performance/limitations are reported under clinically relevant validation (pseudo-prospective / patient-specific)?
4. What validation practices and clinical metrics should be standard (FPR/h, sensitivity, prediction horizon/SPH, pseudo-prospective testing)?

Databases to search

- PubMed / MEDLINE
- IEEE Xplore
- Scopus
- Web of Science
- PubMed Central (PMC)
- arXiv / bioRxiv / medRxiv (for recent preprints)
- Google Scholar (for citation chaining)

Time window

- 2015–2025 (to match the decade reviewed; extend forward as needed for newest work)

Inclusion criteria

- Studies using surface ECG, wearable ECG/PPG, or ECG fused with other non-EEG sensors (accelerometer, gyroscope, EDA, respiration, SpO2).
- Studies addressing seizure prediction (pre-ictal forecasting) or seizure detection using cardiac and/or wearable biosignals.
- Papers reporting evaluation with clinically-relevant metrics (FPR/h, sensitivity, prediction horizon/SPH or SOP) or using pseudo-prospective / real-time simulation.
- Public dataset descriptions or papers that release data or clear dataset provenance.
- Peer-reviewed papers, conference proceedings, and preprints.

Exclusion criteria

- Studies relying exclusively on EEG or intracranial EEG (iEEG).
- Papers without labeled seizure events or without sufficient description of timing for pre-ictal/ictal/inter-ictal periods.
- Purely theoretical papers without empirical evaluation.

Search strings / keywords (examples)

- "seizure prediction" AND (ECG OR electrocardiogram OR heart rate variability OR HRV OR cardiac) NOT EEG
- "seizure detection" AND (ECG OR PPG OR wearable OR photoplethysmography OR heart rate variability) NOT EEG
- "wearable" AND ("seizure" OR "epilepsy") AND (ECG OR PPG OR EDA OR accelerometer) NOT EEG
- "pre-ictal" OR "preictal" AND (ECG OR HRV OR heart rate) NOT EEG
- "pseudo-prospective" OR "prospective" AND (seizure prediction OR seizure detection) AND (ECG OR wearable)

Suggested screening and selection workflow

1. Run database searches with the keywords above; export results (RIS/BibTeX) into a reference manager.
2. Title/abstract screening: apply inclusion/exclusion criteria; mark reasons for exclusion.
3. Full-text screening of selected records; extract dataset used, sensors, preprocessing, models, validation protocol, metrics (FPR/h, sensitivity, AUC), and availability of code/data.
4. Backward and forward citation chaining on key papers (snowballing).
5. Maintain a PRISMA-style flowchart and a spreadsheet with extracted attributes for later analysis.

Priority datasets to identify and evaluate (ECG / wearables)

- EPILEPSIAE: long-term clinical recordings that include ECG (reported in the review). Valuable for HRV-based forecasting studies. Verify access/restrictions.
- Siena dataset (as cited in review): continuous recordings with ECG and seizure annotations—confirm public availability and licensing.
- CHB-MIT: primarily EEG but some files contain ECG — include cautiously and only if ECG channels are available for the specific records used.
- PhysioNet repositories (investigate ECG waveform datasets that include long-term monitoring and clinical annotations). Note: many PhysioNet collections are cardiac-focused; screen for seizure labels or co-recorded seizure annotations.
- Wearable-device cohorts / studies: search for studies that collected ECG/PPG + accelerometry + EDA with seizure logs (e.g., wearable validation studies cited in the review and in Frontiers wearables papers).

Notes on dataset selection

- Prioritize datasets with: continuous long-term ECG or PPG traces, explicit seizure onset timestamps, metadata about seizure type and state (sleep/wake), and multiple seizures per subject for within-patient modeling.
- Respect access conditions: some clinical repositories (EPILEPSIAE) require application or collaboration.
- Where public ECG seizure-labeled datasets are scarce, annotate potential private/proprietary datasets for possible collaboration or simulated experiments (e.g., inject synthetic pre-ictal segments) but mark limitations.

Preprocessing & feature extraction checklist

- R-peak detection & RR interval cleaning: robust detectors (Pan–Tompkins or modern variants), outlier removal, interpolation for missing beats.
- Artifact detection and handling: motion/artifact flags from accelerometer, spectral filters, rejection of segments with deficient signal ("deficit time").
- Standard HRV features: time domain (mean RR, SDNN, RMSSD, pNN50), frequency domain (LF, HF, LF/HF), and VLF when appropriate.
- Nonlinear & complexity features: DFA, LLE (Maximum Lyapunov Exponent), correlation dimension, entropy measures (sample entropy, permutation entropy).
- Time–frequency analyses: wavelet transforms or short-time Fourier for evolving dynamics.
- Multimodal fusion features: coherence/cross-correlation between ECG-derived HR and other sensors (e.g., accelerometry/EDA), sensor-specific event features (movement bursts, tonic-clonic signatures).

Candidate models and modeling strategies

- Classical ML baselines: logistic regression, SVM, Random Forest, XGBoost on engineered HRV and multimodal features.
- Deep learning on raw or minimally preprocessed signals:
  - 1D-CNNs for morphology and local temporal patterns.
  - RNNs / LSTM / GRU for long-term temporal dependencies in HR/HRV.
  - Hybrid CNN-LSTM to combine local feature extraction and sequence modeling (high-performing in review).
  - Transformer-based time-series models for long-range dependencies and non-stationarity.
  - Graph Neural Networks for modeling relations across sensors or leads (if multichannel ECG)
  - Self-supervised pretraining (contrastive learning, masked reconstruction) to leverage large unlabeled wearable datasets.

- Training strategies:
  - Patient-specific models (fine-tuning per subject) vs. subject-independent models.
  - Domain adaptation and transfer learning for small-cohort generalization.
  - Data augmentation: jittering RR series, bootstrapping, synthetic pre-ictal simulation (use with caution).

Validation protocols and clinical metrics (recommended)

- Pseudo-prospective evaluation: withhold later chronological data and evaluate models in a rolling or simulated real-time fashion.
- Patient-specific cross-validation: train on earlier seizures and test on later seizures for each patient when multiple events exist.
- Report primary clinical metrics: FPR/h (primary), sensitivity, time-in-warning (fraction of time patient is in high-risk state), and prediction horizon (SPH). Also report AUC and precision/recall for comparison.
- Statistical reporting: confidence intervals, per-patient distributions (median, IQR) and aggregated metrics; report false alarm distribution across patients.

Implementation & reproducibility

- Prefer methods that publish code and model weights. Record software environment (Python version, libraries like PyTorch/TensorFlow, biosignal toolboxes).
- Share preprocessing scripts (R-peak detection, artifact filtration) and explicit SPH/SOP definitions.
- Use standardized splits and provide a benchmark protocol (which windows are preictal, how many minutes excluded around ictal period, how time-in-warning is calculated).

Quality assessment criteria for included studies

- Clear sensor description (sampling rate, lead placement, ECG/PPG modality).
- Explicit seizure labeling and timing protocol.
- Validation protocol that simulates a real-time deployment (pseudo-prospective or prospective testing).
- Reporting of clinically meaningful metrics (FPR/h) and alarm burden/time-in-warning.

Deliverables and timeline

- Week 1: Run initial searches, export references, and screen titles/abstracts.
- Week 2: Full-text screening and data extraction into spreadsheet (datasets, sensors, preprocessing, models, validation, metrics).
- Week 3: Dataset access applications (EPILEPSIAE or others), begin reimplementation of 1–2 baseline pipelines (HRV-based Random Forest, CNN-LSTM) on available dataset(s).
- Week 4: Run pseudo-prospective evaluations, compile benchmarking table and PRISMA flowchart, and prepare a methods appendix describing preprocessing and evaluation.

Notes & cautions from the review

- The review highlights high inter- and intra-individual variability in preictal HRV dynamics and the non-stationarity of signals; prefer adaptive and patient-specific modeling strategies.
- Pay special attention to artifact-prone periods and the so-called "deficit time" during convulsive events where ECG quality degrades; document how these segments are treated.
- Use clinically-relevant FPR/h thresholds when assessing feasibility (target values cited in literature: e.g., 0.01–0.1 h^-1 for clinical usefulness).

References and provenance

- Use the attached review "Seizure Prediction ECG Machine Learning Review.md" as primary guidance for dataset names, pitfalls (deficit time, non-stationarity), feature families and candidate models; supplement with additional primary studies found by the searches.

## Screening progress, extraction template, and PRISMA flowchart

Current collection: ~91 PDF files in the `Papers/` folder (convert or verify corresponding Markdown in `papers md/`). The following section documents the screening workflow, the minimum extraction fields, and a PRISMA-style flowchart you can use to record counts and decisions.

Screening workflow (recommended)

1. Create a master spreadsheet (CSV) for screening & extraction with the columns below. Use this to record decisions at each step and reasons for exclusion.

2. Title/abstract screening: mark each record as `include`, `exclude`, or `maybe`. Record a short reason for exclusions.

3. Full-text screening: open the PDF (or Markdown conversion) and confirm eligibility according to the inclusion/exclusion criteria above. Move `maybe` -> `include`/`exclude` with reasons.

4. Data extraction: for included studies, extract metadata and study attributes (see template below). Note dataset access instructions and whether code is available.

5. Quality assessment & notes: annotate study quality concerns (small N, no pseudo-prospective testing, missing timing info, only EEG, etc.).

Minimum extraction template (spreadsheet columns)

- id: unique integer
- filename_pdf: path or basename in `Papers/`
- filename_md: path or basename in `papers md/` (if available)
- title
- authors
- year
- study_type: (prediction / detection / review / dataset paper)
- sensors: (ECG / PPG / accelerometer / EDA / multimodal)
- dataset_used: (name(s) or 'proprietary')
- n_subjects
- n_seizures
- seizure_types
- preprocessing: short summary (R-peak algorithm, artifact handling)
- features_or_model: (HRV features, CNN-LSTM, RandomForest, etc.)
- validation_protocol: (pseudo-prospective, leave-one-seizure-out, cross-subject, etc.)
- metrics_reported: (FPR/h, sensitivity, AUC, time-in-warning)
- included: yes / no
- reason_for_exclusion: short text
- notes: free text for useful quotes or page numbers
- code_or_data_links: URL(s)

PRISMA-style flowchart (Mermaid)

Use this Mermaid block in the methods or README to record counts. Replace the placeholder counts with your numbers from the screening spreadsheet.

```mermaid
flowchart TD
  A[Records identified through database searching (n = ___)] --> B[Records after duplicates removed (n = ___)]
  B --> C[Records screened (title/abstract) (n = ___)]
  C --> D[Records excluded (title/abstract) (n = ___)]
  C --> E[Full-text articles assessed for eligibility (n = ___)]
  E --> F[Full-text articles excluded, with reasons (n = ___)]
  E --> G[Studies included in qualitative synthesis (n = ___)]
  G --> H[Studies included in quantitative synthesis (meta-analysis) (n = ___)]
```

Notes on using the PRISMA block

- If you publish the paper or repository, leave the mermaid block and fill the counts before finalizing. GitHub, many static site generators, and some Markdown editors render mermaid diagrams automatically; alternatively export as PNG using a mermaid renderer for the manuscript.
- For transparency, keep the screening CSV and a column with the exclusion reason; include it as Supplementary Material or in a repository.

Quick next steps I can perform for you

- Generate a starter screening CSV (pre-populated with filenames) from the `Papers/` folder.
- Convert PDFs to Markdown for missing items (requires tools and approval).
- Produce a rendered PRISMA diagram (PNG/SVG) from the mermaid block and add it to the repo.

If you want any of the quick next steps, tell me which one and I will proceed.



