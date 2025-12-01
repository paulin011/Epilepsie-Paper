# Preliminary search memo — Non-EEG wearable seizure detection/prediction (2015–2025)

Date: 2025-12-01
Scope: ECG/HRV, PPG, EDA, ACC; alarm-based metrics preferred (sensitivity, FAR/h, latency); designs spanning retrospective, pseudo‑prospective, prospective; ambulatory emphasis.

## RQ1. Reported ranges of sensitivity, FAR, and latency by study design; alarm- vs sample-based

High-level ranges from recent reviews and representative studies (units normalized where possible):

- Convulsive detection (wrist EDA+ACC; hospital/ambulatory, phase 2–3)
  - Sensitivity ≈ 92–95%; FAR ≈ 0.2–1.26 per 24 h (≈ 0.008–0.053/h); latency ≈ 30–40 s.
  - Notes: FAR often higher in children; distribution skewed by a few high-FAR patients.
  - Sources: Miron 2025 (phase 2 multi-center; pediatric vs adult FAR differences), Empatica/Nightwatch series.

- ECG/HRV-based detection (ambulatory/patch)
  - Sensitivity ≈ 78–93%; FAR ≈ 0.03–0.11/h (patient‑adaptive thresholding can reduce FAR ~30%).
  - Sources: Mason 2024 scoping review; Jeppesen series summarized therein.

- Multimodal wearable (ECG±PPG±ACC±EDA) detection (mixed designs)
  - Sensitivity ≈ 67–92%; FAR ≈ 0.03/h to several per day depending on cohort and logic.
  - Sources: Seth 2023 (systematic review), Miron 2025.

- Preictal forecasting with cardiac HR/HRV only (early phase)
  - Sensitivity ≈ 85–89% with prediction horizon ~15 min; FAR ≈ 10–14 per day (0.42–0.58/h), typically patient‑specific.
  - Sources: Miron 2025.

- Alarm‑ vs sample‑based: sample‑based accuracy/ROC commonly overstates real‑time usefulness; when converted to alarms, FAR/h increases and sensitivity may drop; latency only defined in alarm‑based setups. Reviews urge prioritizing alarm metrics (FAR/h, time‑in‑warning) over sample metrics.
  - Sources: Mason 2024; Seth 2023; Yang 2022 (OOD pseudo‑prospective emphasis).

Caveats: Units vary (per hour vs per 24 h), cohort mix (convulsive vs non‑convulsive), and study phase (retrospective often best; pseudo‑/prospective degrade).

## RQ2. Classical feature models vs 1D‑CNN/TCN/LSTM; evidence for attention/transformers and latency/compute

- Classical (HRV/EDA/ACC features + SVM/RF/kNN)
  - Competitive in retrospective settings; rely on engineered features; low compute; can be paired with adaptive thresholds for low FAR/h in specific cohorts (e.g., ictal tachycardia cases).
  - Sources: Mason 2024; Seth 2023; Leal 2017.

- 1D‑CNN/LSTM/TCN
  - Generally improve robustness and phase discrimination; TCN/CNN‑LSTM effective for streaming and low‑latency inference; compact 1D models are viable on-device.
  - Sources: Yang 2022 (multimodal CNN‑RNN; OOD generalization); Wang 2025 (LSTM on attitude angles); Andrade 2024 (performance synthesis across databases).

- Attention/transformers
  - Emerging on wearable cardiac signals; early reports on interpretable ECG features (2024–2025) suggest gains in complex settings, but compute/latency overhead vs 1D‑CNN/TCN is a concern for wearables; evidence base smaller than CNN/RNN.
  - Sources: Abtahi 2025 (interpretable ECG features for prediction), Kalousios 2024; Pordoy 2025 (attention-based fusion).

Compute/latency notes: Shallow feature models have minimal latency but may require costly preprocessing (R‑peak/HRV). 1D‑CNN/TCN provide favorable accuracy‑latency trade‑offs. Transformers typically heavier unless distilled/pruned.

## RQ3. Temporal choices (window, stride, context) vs alarm performance

- Longer windows (e.g., 5 min HRV with heavy overlap) stabilize features in retrospective analyses; short windows (4–10 s) with overlap favored for real‑time detection to limit latency.
- Overlap/stride: zero overlap increases FAR; increasing overlap reduces FAR and smooths alarms, at the cost of compute and correlation between samples.
- Context length: sequence models (LSTM/TCN) benefit from 30–120 s context for detection; forecasting typically needs longer history and explicit SPH/SOP definitions.
- Sources: Leal 2017 (5‑min, 98% overlap); Chen 2022 (8 s, 50% overlap); Wang 2025 (overlap reduces FAR); review guidance in Organization/search-plan-ECG-epilepsy.md.

## RQ4. Robustness to domain shift (patient/device/site/activity); cross‑dataset effects

- Pseudo‑prospective/OOD tests show measurable degradation vs retrospective; alarm‑based metrics are more sensitive to shift than sample‑based.
- Cross‑dataset results (e.g., TUH→RPAH/EPILEPSIAE) highlight distribution shift; personalization/calibration and patient‑preserving splits are critical.
- Activity/motion: children and high‑activity contexts inflate FAR; adding posture/activity logic can reduce false alarms (e.g., alarms only when horizontal).
- Sources: Yang 2022; Andrade 2024; Miron 2025 (pediatric FAR; posture gating); Seth 2023.

## RQ5. Dataset gaps, class imbalance, augmentation/synthetic data impact

- Gaps: Few large, publicly available, long‑term wearable non‑EEG datasets with synchronized labels; many studies are short clinical recordings or proprietary.
- Imbalance: rare seizures → severe class imbalance; per‑patient seizure counts low.
- Augmentation: time‑warping, jitter, scaling, noise injection used; helps training stability, but external validity gains are modest without patient‑preserving design.
- Synthetic data: limited and risky for bias; must validate against alarm metrics and per‑patient distributions.
- Sources: Mason 2024; Seth 2023; Kalousios 2024; internal notes (search‑plan).

## Do these RQs make sense? Preliminary assessment and refinements

- Overall: Questions are coherent, clinically grounded, and actionable.
- Refinements to ensure clarity/comparability:
  - Standardize FAR to per hour in reporting; convert per‑day values when synthesizing.
  - Separate detection vs prediction when summarizing ranges; include prediction horizon (SPH) and time‑in‑warning for forecasting.
  - Specify latency definition (e.g., median time from clinical onset to alarm) and whether post‑processing/alarm logic is included.
  - Stratify by seizure type (convulsive vs non‑convulsive) and setting (EMU vs ambulatory) where possible.
  - Require patient‑preserving splits and highlight external/cross‑dataset tests.

## Key pointers to evidence in this workspace

- Reviews/syntheses
  - Mason 2024 — Heart Rate Variability as a Tool for Seizure Prediction (scoping review): Papers_md/Mason et al. - 2024 - Heart Rate Variability as a Tool for Seizure Prediction A Scoping Review.md
  - Seth 2023 — Cardiac‑based seizure detection/prediction (systematic review): Papers_md/Seth et al. - 2023 - Feasibility of cardiac‑based seizure detection and prediction....md
  - Miron 2025 — Autonomic biosignals, seizure detection/forecasting (broad review): Papers_md/Miron et al. - 2025 - Autonomic biosignals, seizure detection, and forecasting.md
  - Yang 2022 — Multimodal AI OOD generalization (pseudo‑prospective): Papers_md/Yang et al. - 2022 - A Multimodal AI System for Out‑of‑Distribution Generalization....md

- Representative primary studies
  - Leal 2017 — ECG HRV features for anticipation (long‑term; 5‑min windows): Papers_md/Leal et al. - 2017 - On the viability of ECG features....md
  - Chen 2022 — ECG deterministic learning (8 s frames): Papers_md/Chen et al. - 2022 - Deterministic Learning‑Based WEST....md
  - Wang 2025 — Attitude angles (ROLL/PITCH) + LSTM; overlap vs FAR: Papers_md/Wang et al. - 2025 - Epileptic Seizure Detection Based on Attitude Angle....md

## Next steps

- Extract a concept matrix with standardized units: Sensitivity, FAR/h, latency, design (retro/pseudo/prospective), modality, cohort, seizure type, personalization.
- Prioritize studies with alarm‑based evaluation and patient‑preserving or external validation.
- Quantify degradation from retrospective → pseudo‑prospective → prospective where data permit.
