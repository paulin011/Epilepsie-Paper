# Reintjes et al. - 2025 - ECG-Based Detection of Epileptic Seizures in Real-World Wearable Settings Insights from the SeizeIT

Article
ECG-Based Detection of Epileptic Seizures in Real-World
Wearable Settings: Insights from the SeizeIT2 Dataset

Conrad Reintjes †, Janosch Fabio Hagenbeck †
and Detlef Schoder

, Mohamed Ballo †, Tim Rahlmeier

, Simon Maximilian Wolf ∗

Cologne Institute for Information Systems, University of Cologne, 50923 Cologne, Germany;
schoder@wim.uni-koeln.de (D.S.)
* Correspondence: wolf@wim.uni-koeln.de
† These authors contributed equally to this work.

Abstract

Epilepsy is a prevalent neurological disorder where reliable seizure tracking is essential
for patient care. Existing documentation often relies on self-reports, which are unreliable,
creating a need for objective, wearable-based solutions. Prior work has shown that Electro-
cardiography (ECG)-based seizure detection is feasible but limited by small datasets. This
study addresses this issue by evaluating Matrix Profile, MADRID, and TimeVQVAE-AD on
SeizeIT2, the largest open wearable-ECG dataset with 11,640 recording hours and 886 anno-
tated seizures. Using standardized preprocessing and clinically motivated windows, we
benchmarked sensitivity, false-alarm rate (FAR), and a Harmonic Mean Score integrating
both metrics. Across methods, TimeVQVAE-AD achieved the highest sensitivity, while
MADRID produced the lowest FAR, illustrating the trade-off between detecting seizures
and minimizing spurious alerts. Our findings show ECG anomaly detection on SeizeIT2
can reach clinically meaningful sensitivity while highlighting the sensitivity–false alarm
trade-off. By releasing reproducible benchmarks and code, this work establishes the first
open baseline and enables future research on personalization and clinical applicability.

Keywords: seizure detection; machine learning; electrocardiography; anomaly detection;
epilepsy; wearable sensors

1. Introduction

Epilepsy is a chronic neurological disorder characterized by the recurrent occurrence
of epileptic seizures and affects approximately 0.6% of the world’s population [1]. Seizures
can lead to serious medical and psychosocial consequences, e.g., falls, injuries, social
isolation, anxiety, cognitive impairments, and, in extreme cases, sudden death [2]. Accurate
tracking of seizure frequency is essential for individualized medication management, since
it allows the assessment of effectiveness as well as the modification of dosages, and also
enables an objective evaluation of the disease progression [3]. However, in clinical practice,
seizure documentation is often based on patients’ self-reports, despite the well-established
unreliability and incompleteness of self-reporting [4]. Hoppe et al. [5] found that less than
50% of seizures were recognized and reported by patients, while Swinnen et al. [6] observed
that only about 8% of absence seizures were captured by self-reporting. Accordingly,
there is a strong need for objective and automated methods for seizure detection in real-
world settings.

Academic Editor: Piotr Augustyniak

Received: 31 October 2025

Revised: 11 December 2025

Accepted: 15 December 2025

Published: 18 December 2025

Citation: Reintjes, C.; Hagenbeck, J.F.;

Ballo, M.; Rahlmeier, T.; Wolf, S.M.;

Schoder, D. ECG-Based Detection of

Epileptic Seizures in Real-World

Wearable Settings: Insights from the

SeizeIT2 Dataset. Sensors 2025, 25,

7687. https://doi.org/10.3390/

s25247687

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

Sensors 2025, 25, 7687

https://doi.org/10.3390/s25247687

Sensors 2025, 25, 7687

2 of 27

In current research on seizure detection, two main approaches have emerged as
follows: Electroencephalography (EEG)-based and Electrocardiography (ECG)-based meth-
ods. The EEG-based line of research follows the clinical gold standard, the full-scalp EEG,
which directly measures neuronal activity and therefore provides the highest diagnostic
accuracy [7,8]. However, this approach is hardly feasible for everyday use [9]. Conse-
quently, recent efforts have focused on the development of wearable EEG systems, such as
those explored in the SeizeIT1 [10] and SeizeIT2 [11] projects. These devices enable mobile
measurements but typically cover only limited areas of the scalp, resulting in reduced
detection performance [12]. Moreover, long-term use of wearable EEG-based systems (e.g.,
headbands or small electrodes) is often not acceptable to many people with epilepsy (PwE)
due to concerns about visibility, wearing comfort, and stigma [1,13].

In parallel, a second research direction has emerged focusing on ECG-based ap-
proaches. From a practical perspective, this line of research is particularly attractive, as
wearable ECG devices, ranging from medical long-term monitors to consumer-grade chest
patches and smartwatches, are already widely available [14,15]. Surveys indicate that
PwE are generally much more open to using such unobtrusive ECG-based wearables for
seizure detection compared to EEG-based wearables [1]. Physiologically, there exists a close
connection between the brain and the heart via the autonomic nervous system, allowing
epileptic seizures to manifest indirectly in ECG signals [16,17]. This heart–brain interac-
tion is clinically well established. For example, modern vagus nerve stimulation systems
use heart-rate changes as a biomarker for seizure detection in FDA-approved closed-loop
neurostimulation devices [18]. Thus, the ECG serves as a proxy signal: less specific than
EEG, but considerably more robust and suitable for daily life, a classic trade-off between
practicality and precision.

With the SeizeIT2 dataset, a publicly available dataset is now accessible for the first time
that simultaneously records a two-channel EEG and a single-channel ECG in a wearable
setting [11]. It represents the “first open dataset of wearable data recorded in patients with
focal epilepsy” [11] (p. 1). This enables a systematic investigation of the potential of both
approaches and, in particular, allows for the first evaluation of ECG-based seizure detection
under real-world conditions. To our knowledge, no study has yet evaluated ECG-based
seizure detection methods on this dataset. To verify this, we performed a literature search in
PubMed, IEEE Xplore, and Google Scholar using the terms “SeizeIT2” and “ECG”. Because
the SeizeIT2 dataset was first released in 2025, we restricted the search to publications from
2025 onward and screened titles and abstracts of the studies found.

To address this gap, we focus on the ECG signal to investigate the seizure detection
potential contained in this single modality. In this work, “ECG-based seizure detection”
refers to analyzing the full single-lead ECG waveform as a univariate time series. Our
methods operate directly on the preprocessed ECG amplitude signal and do not extract
hand-crafted heart-rate or HRV features. Instead, they detect seizure-related changes
by identifying waveform segments whose temporal patterns deviate from a patient’s
typical cardiac dynamics. Using this definition, we employ three different time-series
anomaly-detection (AD) methods—Matrix Profile, MADRID, and TimeVQVAE-AD—to
evaluate the extent to which epileptic seizures can be identified as abnormal cardiac activity.
Anomaly-detection methods are particularly well suited for ECG-based epilepsy detection,
as autonomic nervous system and ECG responses during seizures are highly individual
and variable [19]. Classifiers often fail to capture such patient-specific patterns due to
their reliance on predefined training data, whereas anomaly-detection models identify
deviations from each patient’s normal heart rate behavior and are thus potentially more
sensitive to previously unobserved disturbances [19]. These methods are assessed on the
SeizeIT2 dataset based on sensitivity, false-alarm rate (FAR), and the Harmonic Mean Score

Sensors 2025, 25, 7687

3 of 27

(HMS), a composite metric that balances sensitivity and FAR through weighted penalization
of false alarms.

Overall, our findings indicate that ECG-based seizure detection is feasible and that
ictal changes can be captured directly from the ECG waveform. At the same time, the
comparison between anomaly-detection methods highlights substantial variability in how
sensitively and specifically different approaches respond to patient-specific cardiac dynam-
ics. These general patterns underline both the potential of ECG as a practical and wearable
modality and the remaining challenges related to false alarms, heterogeneous physiological
responses, and the need for patient-tailored detection strategies.

Taken together, this study provides a first benchmark for ECG-based seizure detection
on SeizeIT2 and motivates further research toward more robust, multimodal, and clinically
scalable solutions.

The paper is organized to first outline a description of the dataset and methods,
followed by a presentation of the experimental results, and a discussion of the implications,
limitations, and directions for future research.

2. Materials and Methods

An overview of the full processing pipeline is presented in Figure 1. The workflow
illustrates how raw ECG recordings from the SeizeIT2 dataset pass through quality control
and standardized preprocessing before entering the model development stages. During
training, each anomaly-detection method is evaluated across a broad configuration space,
including model-specific parameters and post-processing strategies. In the subsequent
test phase, the selected configuration is applied to unseen patient data to generate model
outputs and final seizure detections.

2.1. Dataset

This study utilizes ECG recordings from the SeizeIT2 dataset, an open-source, mul-
timodal wearable dataset comprising 11,640 h of physiological data from 125 patients
(51 female, 41%) with focal epilepsy. Similar to the split of Bhagubai et al. [11], the vali-
dation set used to assess method performance comprises data from patients sub-001 to
sub-096, while the test set includes patients sub-097 to sub-125. As noted in the paper,
the patient numbering does not follow a specific order. The corpus includes 886 video-
EEG-verified seizures: 317 focal aware, 393 focal impaired awareness, 55 focal-to-bilateral
tonic–clonic, and 121 other/unclear events.

However, of the total 886 annotated seizures, 27 do not have corresponding ECG
recordings. On the patient level, five patients (sub-048, sub-049, sub-054, sub-058, and
sub-097) have no seizures with ECG recordings at all. To ensure data quality in the test set,
we further examined signal saturation and excluded recordings in which at least 10% of
the ECG samples were saturated. This criterion led to the exclusion of 14 recordings and
reduced the total number of test seizures by three. After applying these exclusions, a total
of 856 seizures with usable ECG recordings from 120 patients remained for analysis.

The data were obtained 2020–2022 across five European epilepsy monitoring cen-
ters [11]. ECG was recorded using the Sensor Dot wearable device, with electrodes placed
on the left chest, extending to the lower rib cage and left parasternal region. The sampling
rate was 256 Hz. All participants provided written informed consent; the original study
was approved by the UZ Leuven ethics committee (ID S63631, amendment S67350).

Sensors 2025, 25, 7687

4 of 27

Figure 1. Overview of the proposed ECG-based seizure detection pipeline using the SeizeIT2 dataset.
The overall workflow is divided into a training phase and a test phase. The dataset is first split
at the patient level into a training set (sub-001–096) and a test set (sub-097–125). ECG recordings
undergo data quality checks (ECG availability, and saturation detection) and preprocessing (bandpass
filtering, normalization, and downsampling), resulting in preprocessed training and test sets. In the
training phase, all three anomaly-detection models (Matrix Profile, MADRID, and TimeVQVAE-AD)
are trained and evaluated across multiple configurations, followed by post-processing via temporal
clustering. Based on training performance, the best model and post-processing configuration are
selected. In the test phase, this selected configuration is applied to the held-out test patients, and
seizure events are detected and evaluated. Performance metrics are reported separately for all patients
and for the subgroup of responders exhibiting pronounced ictal heart-rate changes.

2.2. Performance Metrics

Recent reviews underscore the importance of sensitivity and FAR as key bench-
marks [16,20,21]. Therefore, method performance is assessed using sensitivity (recall)
and FAR and the HMS. The sensitivity is calculated using any overlap between predicted
and real seizure event [22] while the HMS was introduced in a SeizeIT2 seizure detection
challenge and is defined as

HMS = Sensitivity (%) − 0.4 · FAR (FA/h).

(1)

It combines both sensitivity and FAR into a single aggregated metric, thereby capturing the
trade-off between accurate detection and alarm burden.

Sensors 2025, 25, 7687

5 of 27

Statistical comparisons between models were performed using McNemar’s test for
paired nominal data. For each pair of models, detection outcomes (detected vs. missed)
were compared on the same seizure instances from the test set. Comparisons were con-
ducted separately for each optimization objective (sensitivity-optimized, FAR-optimized,
and HMS-optimized) and for each evaluation setting. The latter includes both the strict
ictal-only detection criterion and the extended evaluation window introduced later in
Section 2.4.

McNemar’s Chi-square statistic with Yates’ continuity correction was computed as

χ2 =

(|n10 − n01| − 1)2
n10 + n01

,

(2)

where n10 denotes seizures detected only by model A and n01 seizures detected only by
model B. Statistical significance was assessed at α = 0.05.

To quantify uncertainty in the performance estimates, we computed 95% confidence
intervals by bootstrapping at the patient level. For each model, configuration, and evalua-
tion setting (strict and SDW), we resampled patients with replacement (1000 iterations) and
recomputed the patient-wise mean sensitivity, FAR, and HMS for each bootstrap sample.
The 2.5th and 97.5th percentiles of the resulting empirical distributions were taken as the
bounds of the 95% confidence interval. For readability and to avoid cluttering the main
result tables, the confidence intervals are not included in the Results Section 3 but are
reported in full in Appendix A.

Jeppesen et al. [17] showed that patients with a maximal heart rate change of more
than 50 beats/min (BPM) during an seizure had significantly better performance results
with ECG-based detection methods. These patients are referred to as “responders”. The
distinction between responders and all patients is useful because not every patient shows
pronounced autonomic changes in the ECG during a seizure [17]. This allows the actual
performance of the method to be realistically evaluated and the identification of the specific
patient group for whom ECG-based seizure detection is clinically appropriate.

Following Jeppesen et al. [17], we classified patients as responders if their first recorded
seizure exhibited a maximum heart-rate change of more than 50 beats per minute (BPM)
within a 100-RR-interval window. This responder definition was applied on a per-patient
basis using the first seizure available in the SeizeIT2 recordings.

For each patient, we first detected R-peaks in the ECG using the method of Elgendi [23]
and computed RR intervals for the first seizure. If this seizure contained at least 100 valid
RR intervals, the maximum heart-rate change was computed directly within the seizure
window. In cases where the first seizure was too short to provide 100 RR intervals, we
automatically extended the analysis window symmetrically before and after the seizure,
using pre-ictal and post-ictal ECG segments, until at least 100 RR intervals were available.
Using this procedure, 55.55% of patients met the responder criterion: their first
recorded seizure showed a maximum heart-rate change greater than 50 BPM within the
100-RR-interval window. For this group of responders, the performance metrics are docu-
mented separately from all patients in the Results Section 3.

2.3. Machine Learning Methods

The time-series anomaly detection algorithms Matrix Profile, MADRID, and
TimeVQVAE-AD each exhibit distinct, model-specific hyperparameters and underlying op-
erational mechanisms. For data preprocessing, we implemented a two-fold preprocessing
pipeline. First, we applied a bandpass filter to reduce the noise of the data, using a lower
cutoff frequency of 0.5 Hz, a higher cutoff frequency of 40.0 Hz, and a filter order of 4. In
the consecutive step, we downsampled the signal to 8 Hz to reduce the computational costs.

Sensors 2025, 25, 7687

6 of 27

All three anomaly-detection methods operate directly on the preprocessed ECG time series,
meaning they take the amplitude of the single-lead ECG over time as input. We do not
extract features such as heart rate, HRV indices, or QRS morphology. Instead, the models
treat the ECG as a generic time series and flag segments whose waveform shape, envelope,
or rhythm deviates from the typical cardiac pattern. While the preprocessing pipeline was
used for all methods, we applied tailored post-processing steps for each model further
detailed in the next subchapters.

2.3.1. Matrix Profile

Figure 2 provides a concise overview of the anomaly-detection workflow based on
the Matrix Profile. The method evaluates all z-normalized subsequences of the ECG signal
and assigns each position a discord value that reflects how dissimilar the corresponding
subsequence is from the similar subsequence in the time series [24]. Large peaks in the
resulting Matrix Profile curve indicate discords, which are highly unusual subsequences
that serve as primary anomaly candidates after global thresholding and an overlap-based
filtering step. This representation forms the basis on which further refinement is applied.
To reduce the number of falsely classified seizure events produced by this pipeline,
we implemented an additional post-processing step based on temporal clustering. This
procedure requires a minimum of n consecutive detected anomalies to form a valid event,
thereby mitigating false alarms caused by isolated deviations. To preserve sensitivity, short
gaps between anomalies are permitted. Once a cluster is confirmed, its final anomaly index
is determined as the nearest integer to the mean index of all anomalies within the group.

Figure 2. Overview of the Matrix Profile-based anomaly-detection workflow. From a preprocessed
ECG signal, all z-normalized subsequences of length m are extracted and compared using the Matrix
Profile, which assigns to each position the distance to its nearest neighbor subsequence. Large values
mark discords (candidate anomalies) which are then filtered through percentile thresholding and an
overlap criterion to remove redundant or weak candidates.

2.3.2. MADRID

A visual overview of the MADRID workflow is provided in Figure 3. MADRID builds
upon the matrix profile approach by extending anomaly detection to multiple subsequence
lengths simultaneously [25]. Instead of using a fixed length m, discords are computed
across a range of lengths m ∈ [mmin, mmax] [25]. The original MADRID algorithm was

Sensors 2025, 25, 7687

7 of 27

extended to allow for more detected anomalies, as the original implementation returned
too few anomalies for successful detection. Specifically, we introduced (i) percentile-based
filtering of anomalies; (ii) a flexible top-k selection per subsequence length; and (iii) an
overlap constraint (see Figure 3). The selected values for the parameters are documented in
Appendix B.

Figure 3. Overview of the MADRID anomaly-detection workflow. The algorithm first extracts
subsequences for multiple lengths m, ranging from mmin to mmax in steps of ∆m (step size). For each
subsequence, MADRID computes a discord score that quantifies the degree of deviation from typical
patterns in the time series; higher scores indicate stronger dissimilarity. The resulting multi-length
discord matrix is refined through a three-stage anomaly-selection procedure: (1) Global percentile
filtering: subsequences below a global percentile threshold are removed, ensuring that only strongly
deviant patterns remain. (2) Per-length ranking and top-k selection: subsequences are ranked by
discord score for each length and the top k candidates are retained. (3) Overlap constraint: candidates
overlapping more than 25% with already selected anomalies are discarded, yielding a final set of
non-redundant anomaly candidates. This filtered anomaly list forms the basis for post-processing,
clustering, and seizure-detection evaluation.

Then, MADRID returns a list of anomaly candidates. To further reduce the number of
reported anomalies while preserving sensitivity, we applied a clustering step to this list.
Specifically, we grouped anomalies that occurred within a short temporal window into
clusters, assuming that closely occurring detections represent the same underlying event.
Concretely, time-based clustering groups anomalies purely by temporal distance: for a
given threshold ∆t (we tested values from 2 s to 900 s), anomalies are added to the current
cluster as long as the gap to the last anomaly is ≤∆t; otherwise, a new cluster is started.
For each cluster, a representative anomaly is selected as the point with the minimal mean
temporal distance to all others (a temporal medoid). To compare different ∆t values, we
defined a clustering score function that combines improvements:

Score = 0.6 · False Positives Reduction (%) + 0.3 · Anomaly Reduction (%) − 2.0 · Sensitivity Loss (%).

(3)

The procedure runs in three phases: (1) strategy evaluation: compute metrics and
scores for each ∆t on the training set, (2) global selection: choose the ∆t with the high-
est average score, and (3) application: apply the selected ∆t to the test set and report
final metrics.

Sensors 2025, 25, 7687

8 of 27

2.3.3. TimeVQVAE-AD

TimeVQVAE-AD models normal temporal dynamics as a probabilistic density over
discrete, time-frequency tokens and detects anomalies by low likelihood. The method has
two stages followed by an evaluation/scoring [26]. A visual overview of the TimeVQVAE-
AD approach is provided in Figure 4.

Figure 4. TimeVQVAE-AD overview. During training (Stages 1 and 2), only normal intervals are used;
anomalous regions are excluded. Stage 1 (Tokenizer): Normal segments are transformed by the STFT
and passed through the encoder and vector quantizer to obtain the token map s ∈ {1, . . . , K}H×W .
The encoder, vector quantizer, and decoder are optimized with a reconstruction objective; iSTFT
of the decoded STFT yields an approximate waveform. Green boxes denote modules optimized
in this stage. Stage 2 (Prior): The tokenizer is frozen. From the same normal-only data, randomly
chosen windows M are masked and a bidirectional transformer prior is trained to predict masked
tokens by maximizing pθ(s | sM), equivalent to minimizing masked negative log-likelihood. Green
boxes denote modules optimized in this stage. Evaluation: With the tokenizer and prior fixed, a
masking window of width α slides along time. For each center index w, the prior outputs categorical
distributions that quantify how likely the masked tokens are under the learned normal model; the
anomaly score is the mean negative log-likelihood over the masked span. Repeating over w yields a
score map ˜a. Scores across multiple α may be summed, and a threshold τ determines anomaly labels.

For stage 1, each time series x{1:T} undergoes a Short-Time Fourier Transform (STFT)

preprocessing step. With fast Fourier transform size nfft, the latent height is

H = ⌊nfft/2⌋ + 1.

(4)

A convolutional encoder maps the STFT to a latent grid z ∈ RD×H×W, where W is the
downsampled temporal width and D is the number of latent channels. Vector quantization
assigns each spatial location to a codebook entry from K prototypes, yielding a token map

Sensors 2025, 25, 7687

9 of 27

s ∈ {1, . . . , K}H×W and its quantized embedding zq. Stage 1 trains the encoder, vector
quantizer, and decoder by minimizing the reconstruction loss.

In stage 2, a bidirectional transformer prior pθ(s) is trained to predict masked tokens
from surrounding context by maximizing pθ(s | sM), where sM is obtained by replacing
a uniformly random subset of tokens with [MASK]. This corresponds to minimizing the
negative log-likelihood of the true tokens at the masked positions. Through this process,
the model learns a density over typical token configurations on the H × W grid.

For evaluation and scoring in the discrete latent space s ∈ RH×W, we slide a mask-
ing window along time. For each temporal index w, we mask the segment s:,w−α:w+α
and compute

aw = E[− log pθ(s:,w−α:w+α | sM(:, w − α : w + α))],

assigning scores only to the masked region M′ via

aM′ = a ⊙ (1 − m).

(5)

(6)

Repeating over all w yields ˜a ∈ RH×W. To capture different durations, we repeat this for
multiple α and sum the resulting ˜a maps.

We adapted the model with a coarse, multi-stage grid search. We first tuned stage 1 and
carried the two best configurations forward into a stage 2 grid search. For selection, we used
a fixed 1-hour training budget and chose the model with the lowest objective: reconstruction
loss for stage 1 and masked negative log-likelihood for stage 2, favoring configurations that
learn efficiently on our data. We then swept anomaly-score thresholds to pick operating
points optimized for specific metrics. Finally, we post-processed detections with a clustering
procedure analogous to MADRID (see Section 2.3.2). Unlike MADRID, at low thresholds,
TimeVQVAE-AD sometimes formed very large clusters, occasionally covering more than
50% of a recording. Therefore, we added an adaptive penalty mechanism for the evaluation
of the best clustering strategies.

2.4. Seizure Detection Window (SDW)

Heart rate and HRV changes often precede the seizure onset by several minutes. Pavei
et al. [27] quantified significant HRV changes extending up to five minutes pre-ictally.
Furthermore, Jeppesen et al. [28] showed that counting an ECG-based HRV alarm as a true
positive when it occurred from one minute before to three minutes after the EEG-marked
seizure onset produced clinically meaningful sensitivity with an acceptable false-alarm rate.
Motivated by these findings, we define a Seizure Detection Window (SDW) ranging
from –5 min to +3 min around the EEG-marked seizure onset. Any overlap of an ECG-
based alarm with this SDW interval is counted as a true positive, while alarms outside
this window are treated as false positives. Conceptually, the SDW captures seizure-related
autonomic changes that may build up before and persist after the electrographic onset,
and thus aligns the evaluation with clinically meaningful warning behavior rather than a
purely ictal-only timing criterion.

To illustrate the effect of this framework in a controlled setting, Figure 5 shows
synthetic ECG examples with and without SDW: without SDW, only anomalies during the
ictal period are labelled as true positives, whereas with SDW, pre- and post-ictal anomalies
within the [–5 min, +3 min] window are also considered true positives.

Sensors 2025, 25, 7687

10 of 27

(a)

(b)

Figure 5. Illustration of the Seizure Detection Window (SDW) concept on a synthetic ECG example.
The colored regions mark the ictal period and the extended SDW interval from five minutes before to
three minutes after seizure onset. Anomalies occurring outside the SDW are treated as false positives,
whereas anomalies within the SDW are counted as true positives, reflecting clinically meaningful
pre- and post-ictal autonomic changes. (a) Without SDW: only ictal anomalies are counted as true
positives. (b) With SDW: pre- and post-ictal anomalies inside the –5 min, +3 min window are also
counted as true positives.

2.5. Seizure Type Analysis

To examine whether detection performance differs across seizure types, we conducted
a seizure-type-specific sensitivity analysis based on the clinical annotations provided in the
SeizeIT2 dataset [11]. The analysis was restricted to the sensitivity-optimized configurations
of all three models (Matrix Profile, MADRID, and TimeVQVAE-AD).

Table 1 summarizes the seizure types represented in the test set, along with their

respective sample sizes.

Table 1. Seizure types included in the test set and their frequencies.

Seizure Type (Expanded Description)

Focal aware, unimpaired awareness, non-motor (FA-UA-NM)
Focal impaired awareness (FIA)
Focal to bilateral tonic-clonic (F2B)
Focal aware, unspecified motor signs (FA-A-UM)
Focal aware, non-motor (FA-A-NM)
Focal aware, motor hyperkinetic (FA-A-M-Hyperkinetic)
Focal impaired awareness, motor automatisms (FIA-M-Automatisms)
Focal impaired awareness, motor hyperkinetic (FIA-M-Hyperkinetic)
Focal impaired awareness, non-motor (FIA-NM)

n

4
15
21
15
15
12
16
10
55

For each seizure type, we computed sensitivity at the level of individual seizures
as the proportion of seizures correctly detected by a model within the given evaluation
window (strict or SDW). We then aggregated these results in two ways: (i) as model-
specific sensitivities per seizure type, and (ii) as the mean sensitivity across all three models,
providing a model-agnostic estimate of relative detection difficulty across seizure types. The
resulting average sensitivities are reported in the Results Section 3, whereas full per-model
tables are included in Appendix C for completeness.

3. Results

This chapter presents the results of our conducted experiments. We begin by reporting
outcomes in Section 3.1 based on a strict definition of seizure detection: a seizure is consid-
ered correctly classified only if the prediction falls within the original seizure timespan. This
strict definition may not reflect practical relevance, as seizure related heart rate variability

Sensors 2025, 25, 7687

11 of 27

(HRV) alterations can occur beyond the original seizure timespan. An extended evaluation
window is introduced in Section 2.4, and the results using it are reported in Section 3.2.
For each of the three metrics: sensitivity, FAR, and HMS, we performed individual opti-
mizations, and the best results for each metric based on the overall group are presented in
the table of each subchapter. The selection was performed by filtering according to each
metric on the validation set, and the corresponding values are subsequently reported on
the test set.

3.1. Experiment Results Anomaly Detection

The results of our initial experiment, in which the strict seizure definition was applied,
are presented in Table 2. We evaluate the performance using the selected metrics described
in Section 2.2. Detailed information regarding the Config is provided in Appendix B.

Table 2. Performance metrics of Matrix Profile, MADRID, and TimeVQVAE-AD optimized for
different objectives without SDW applied. Sensitivity, FAR, and HMS are reported for both responders
and all patients. Boldfaced values indicate the best performance within each metric and test set. The
p-value indicates the statistical difference in the All-metric compared to the best-performing model
for the respective optimization objective (as marked in bold).

Method

Optimized for

Sensitivity (%)

FAR (FA/h)

HMS

Responder

All

Responder

All

Responder

All

FAR
Matrix Profile
FAR
MADRID
TimeVQVAE-AD FAR

Sensitivity
Matrix Profile
MADRID
Sensitivity
TimeVQVAE-AD Sensitivity

HMS
Matrix Profile
MADRID
HMS
TimeVQVAE-AD HMS

48.78%
9.52%
43.01%

90.24%
38.10%
90.71%

87.80%
38.10%
90.71%

19.63%
2.44%
36.90%

60.12%
13.40%
82.79%

50.92%
13.40%
82.79%

1.92
0.11
8.34

65.62
1.47
25.95

21.22
1.47
25.95

1.92
0.11
8.58

66.80
1.53
26.12

21.94
1.53
26.12

48.01
9.48
39.76

63.99
37.51
80.33

79.32
37.51
80.33

18.86
2.40
33.46

33.40
12.80
72.34

42.14
12.80
72.34

p-Value

<0.0001
–
<0.0001

<0.0001
<0.0001
–

<0.0001
<0.0001
–

The results show that Matrix Profile with FAR-optimized configuration achieves a
sensitivity of 48.78% on the responder subset and 19.63% on the general test set, while
maintaining fewer than two false alarms per hour. When adjusted to prioritize higher
sensitivity, Matrix Profile achieves 90.24% sensitivity on the responder subset and 60.12%
on the general test set. However, this improvement is accompanied by a substantial increase
in the FAR, reaching 65.62 FA/h for the responder subset and 66.80 FA/h for the general
test set.

When evaluating the MADRID model, distinct trade-offs between sensitivity and FAR
become apparent. In the low–false alarm configuration, the model detects only about 2.44%
of seizures in the overall dataset while generating almost no false alarms (0.11 FA/h). In
contrast, tuning the model for maximum sensitivity results in a perfect detection rate of
38.1% on the responder subset and 13.4% on the overall dataset, but this comes with a
notable increase in false alarms (1.47 FA/h for responders and 1.53 FA/h overall).

From the table, TimeVQVAE-AD tuned to minimize false alarms reaches 43.01% sensi-
tivity on responders and 36.9% on the full test set, while keeping the false-alarm rate below
nine per hour (8.34 FA/h and 8.58 FA/h). When tuned for higher sensitivity, sensitivity rises
to 90.71% on responders and 82.79% overall, at the cost of roughly 26 FA/h (25.95 FA/h
and 26.12 FA/h). As with MADRID, in this case, the HMS-optimized configuration is the
same as the sensitivity-optimized one.

Sensors 2025, 25, 7687

12 of 27

Statistical comparison using McNemar’s test (see Appendix Table A1) showed that,
without applying the SDW, all pairwise differences between methods were statistically
significant (p < 0.05). In particular, the sensitivity advantages of TimeVQVAE-AD over
both Matrix Profile and MADRID were highly significant in the no-SDW setting.

To complement the point estimates in Table 2, the patient-level 95% confidence inter-
vals help contextualize the variability of the models’ performance (Appendix Table A2).
For example, TimeVQVAE-AD in the sensitivity-optimized setting shows comparatively
narrow CIs for sensitivity (73.42–90.28%), indicating stable performance across patients. In
contrast, wider sensitivity CIs are exhibited by MADRID (11.02–31.99%) and Matrix Profile
(50.71–74.34%), highlighting greater between-patient variability.

Across seizure types, substantial variability in detectability emerges when using
the sensitivity-optimized configurations under the strict evaluation criterion (no SDW).
As illustrated in Figure 6, focal-to-bilateral tonic-clonic seizures (f2b) show the highest
average sensitivity (76.19%, n = 21), indicating that these seizures exhibit the most con-
sistent ECG abnormalities detectable by all three models. Hyperkinetic and automatisms-
dominant focal impaired-awareness seizures also achieve comparatively high sensitivities
(ia_m_automatisms: 68.75%, n = 16; ia_m_hyperkinetic: 60.0%, n = 10).

Figure 6. Average seizure-type-specific sensitivity across all models in the sensitivity-optimized
configuration, evaluated under the strict detection criterion (no SDW). Sensitivity values represent
the mean sensitivity across TimeVQVAE-AD, Matrix Profile, and MADRID; numbers below each bar
indicate the number of seizures of that type in the test set.

In contrast, several seizure types demonstrate only moderate detection performance:
non-motor focal aware seizures (a_nm: 51.11%, n = 15), non-motor focal impaired-
awareness seizures (ia_nm: 47.88%, n = 55), and autonomic/mixed-awareness seizures
(a_um: 44.44%, n = 15). The weakest performance appears for unspecific non-motor focal
seizures (ua_nm: 41.67%, n = 4) and hyperkinetic focal aware seizures (a_m_hyperkinetic:
36.11%, n = 12). Pure focal impaired-awareness seizures without motor features (ia)
achieve the lowest average sensitivity overall (26.67%, n = 15).

3.2. Experiment Results Anomaly Detection with SDW

Table 3 presents the results of our second experiment, in which the SDW definition
was applied. The same performance metrics as in the previous experiment are used
for consistency. Further details on the post-processing configuration are provided in
Appendix B.

Sensors 2025, 25, 7687

13 of 27

Table 3. Performance metrics of Matrix Profile, MADRID, and TimeVQVAE-AD optimized for
different objectives with SDW applied. Sensitivity, FAR, and HMS are reported for both responders
and all patients. Boldfaced values indicate the best performance within each metric and test set. The
p-value indicates the statistical difference in the All-metric compared to the best-performing model
for the respective optimization objective (as marked in bold).

Method

Optimized for

Sensitivity (%)

FAR (FA/h)

HMS

Responder All

Responder All

Responder All

FAR
Matrix Profile
MADRID
FAR
TimeVQVAE-AD FAR

Sensitivity
Matrix Profile
MADRID
Sensitivity
TimeVQVAE-AD Sensitivity

Matrix Profile
HMS
HMS
MADRID
TimeVQVAE-AD HMS

70.73%
7.14%
59.05%

38.04%
1.80%
61.09%

100.00% 98.16%
65.24%
100.00% 96.43%

66.67%

97.56%
66.67%
93.33%

96.93%
65.24%
92.86%

1.91
0.06
4.23

13.27
4.00
40.46

10.92
3.77
15.57

1.90
0.05
4.22

13.90
4.13
39.75

11.37
3.96
15.25

69.97
7.12
57.36
94.69 1
65.07
83.82

93.19
65.16
87.11

37.28
1.78
59.40
92.60 1
63.59
80.53

92.39
63.65
86.76

p-Value

<0.0001
–
<0.0001

–
<0.0001
0.2482

–
0.0056
<0.0001

1 For Matrix Profile, the sensitivity- and HMS-optimized configurations were nearly identical on the training set,
which can cause the sensitivity-optimized setting to yield slightly higher HMS on the test data.

As shown in Table 3, Matrix Profile with FAR-optimized configuration achieves a
sensitivity of 38.04% on the full dataset and 70.73% on the responder subset, both at around
1.9 false alarms per hour. When adjusted to maximize sensitivity, performance increases to
100% on the responder subset and 98.16% on the full test set. However, consistent with the
trade-off observed in Table 2, this adjustment leads to a higher FAR, reaching 13.27 FA/h
for the responder subset and 13.90 FA/h for the full dataset.

When analyzing the MADRID model on the SDW extension, similar trade-offs can be
observed. In the low–false alarm configuration, the model achieves 7.14% sensitivity on the
responder subset and only 1.8% on the overall dataset, while producing low false alarms
(0.06 FA/h for responders and 0.05 FA/h overall). In contrast, the sensitivity-focused
configuration reaches 66.67% sensitivity on the responder subset and 65.24% on the overall
dataset, at the cost of higher FARs (4 FA/h for responders and 4.13 FA/h overall). The
HMS-optimized configuration yields the same sensitivity values of 66.67% (responders)
and 65.24% (overall) while slightly reducing the FAR to 3.77 FA/h for responders and
3.96 FA/h overall.

As shown in Table 3, TimeVQVAE-AD tuned to minimize false alarms attains 59.05%
sensitivity on responders and 61.09% on the full set, with 4.23 FA/h on responders and
4.22 FA/h overall. When tuned to maximize sensitivity, sensitivity rises to 100% on
responders and 96.43% overall, accompanied by 40.46 FA/h on responders and 39.75 FA/h
overall. Optimizing for the HMS preserves 93.33% responder sensitivity and reaches 92.86%
overall, with 15.57 FA/h on responders and 15.25 FA/h overall and yields the highest HMS
at 87.11 for responders and 86.76 overall.

When applying the SDW extension, most differences between models remained statis-
tically significant (see Appendix Table A1). Notably, Matrix Profile detected a significantly
larger number of seizures than MADRID across all optimization objectives (p < 0.05).
However, the sensitivity difference between Matrix Profile and TimeVQVAE-AD in the
sensitivity-optimized configuration was not statistically significant (p = 0.2482).

Confidence intervals under the SDW setting reveal a marked reduction in uncertainty
for the high-performing configurations (Appendix Table A3). Matrix Profile’s sensitivity-
optimized setting reaches tight CIs (88.07–100.00%), reflecting highly consistent pre-ictal
and post-ictal detections across patients. Likewise, TimeVQVAE-AD shows narrow ranges

Sensors 2025, 25, 7687

14 of 27

in both sensitivity (89.29–100.00%) and FAR (38.34–40.82 FA/h), whereas MADRID main-
tains substantially wider intervals (e.g., 50.71–74.34% sensitivity), again indicating larger
patient-level variability.

When applying the Seizure Detection Window (SDW), average sensitivities increase
markedly across all seizure types, reflecting the extended temporal tolerance for detecting
seizure-related ECG abnormalities. As shown in Figure 7, the highest detectability is
observed for hyperkinetic focal impaired-awareness seizures (ia_m_hyperkinetic), which
reach an average sensitivity of 96.67% (n = 10). Non-motor focal aware seizures (a_nm)
also achieve very high sensitivity (95.56%, n = 15), followed by non-motor focal impaired-
awareness seizures (ia_nm) with 90.30% (n = 55), which represent the most frequent seizure
type in the test set.

Figure 7. Average seizure-type–specific sensitivity across all models in the sensitivity-optimized
configuration, evaluated under the expanded detection criterion (SDW). Sensitivity values represent
the mean sensitivity across TimeVQVAE-AD, Matrix Profile, and MADRID; numbers below each bar
indicate the number of seizures of that type in the test set.

Focal-to-bilateral tonic-clonic seizures (f2b) reach an average sensitivity of 88.89%
(n = 21), while autonomic or mixed-awareness focal seizures (a_um) show similarly high
detectability at 86.67% (n = 15). Automatisms-dominant focal impaired-awareness seizures
(ia_m_automatisms) achieve 85.42% (n = 16), and hyperkinetic focal aware seizures
(a_m_hyperkinetic) remain slightly lower at 83.33% (n = 12). Pure focal impaired-
awareness seizures (ia) reach 77.78% (n = 15).

The lowest sensitivity under the SDW setting is still relatively high: unspecific non-
motor focal seizures (ua_nm) achieve 75.00% (n = 4), demonstrating that even seizure types
with subtle manifestations benefit substantially from the extended detection window.

4. Discussion
4.1. Interpretation

The comparative evaluation of Matrix Profile, MADRID, and TimeVQVAE-AD on
the SeizeIT2 dataset reveals clear differences in their performance profiles and under-
scores the strong influence of the evaluation framework. While the evaluated models
demonstrate that ECG-based seizure detection can achieve clinically meaningful sensitivity
levels, they simultaneously show that false-alarm rates remain substantially above clinically
acceptable thresholds.

Under the strict seizure definition, TimeVQVAE-AD achieved the highest overall HMS
(72.34) due to its favorable balance between sensitivity (82.79%) and FAR (26.12 FA/h).
In contrast, Matrix Profile in its HMS-oriented configuration reached 50.92% sensitivity
but at the cost of an increased FAR (21.94 FA/h), which substantially reduced its overall

Sensors 2025, 25, 7687

15 of 27

HMS (42.14). MADRID, while capable of operating with very low FARs, struggled with
extremely limited sensitivity (13.4%) under the strict criterion, resulting in the weakest
HMS of 12.8. These results indicate that the models differ not only in their raw detection
capability but also in how alarms are distributed relative to annotated seizure intervals.
These differences are also reflected in the statistical analysis. McNemar’s tests showed that,
under the no-SDW setting, all pairwise differences between models in terms of seizure
detection were highly significant (p < 0.05). The bootstrapped 95% confidence intervals
further support this picture (Appendix Table A2): in the FAR-optimized setting, MADRID’s
FAR CI does not overlap with those of Matrix Profile or TimeVQVAE-AD. Conversely, in
the HMS-optimized configuration, the HMS CI of TimeVQVAE-AD for all patients ([63.41,
79.67]) overlaps only marginally with that of Matrix Profile ([39.10, 66.64]), indicating a
consistently higher overall score for TimeVQVAE-AD under the strict evaluation criterion
and aligning with the significant McNemar test results.

Applying the Seizure Detection Window (−5 to +3 min relative to EEG onset) sub-
stantially altered the performance landscape and led to marked improvements across all
models. Matrix Profile benefited most strongly, with sensitivity increasing from 60.12%
to 98.16% and the FAR dropping to 13.9 FA/h, thereby achieving the highest HMS in
the all-patient setting (92.6). TimeVQVAE-AD also improved under the SDW, reaching
92.86% sensitivity at 15.25 FA/h with a HMS of 86.76, which is highly competitive though
slightly below Matrix Profile. The shift in relative ranking indicates that Matrix Profile often
generates detections in the pre-ictal or post-ictal period alarms that were penalized under
the strict definition but recognized as clinically meaningful within the SDW. MADRID
likewise improved substantially, rising from 13.4% to 65.24% sensitivity while maintaining
a relatively low FAR of 3.96 FA/h, increasing its HMS from 12.8 to 63.59. Under the SDW
setting, McNemar’s tests confirmed that Matrix Profile detects significantly more seizures
than MADRID across all optimization objectives (p < 0.05). In contrast, the difference
in sensitivity between Matrix Profile and TimeVQVAE-AD in the sensitivity-optimized
configuration was not statistically significant (p = 0.2482), suggesting that both models
perform comparably in terms of seizure detection when SDW is applied. This interpretation
is further supported by the substantial overlap of their bootstrapped 95% sensitivity CI for
the sensitivity-optimized configuration (Matrix Profile: [88.07%, 100.00%], TimeVQVAE-
AD: [89.29%, 100.00%]), indicating that their achievable sensitivities fall within nearly
identical ranges.

When comparing operating points, distinct trade-offs become apparent. MADRID
remains the model with the lowest FARs, in some cases approaching zero, but this comes
at the expense of substantially reduced sensitivity. Without the SDW, TimeVQVAE-AD
achieves the best overall performance, combining the highest sensitivities with compar-
atively moderate FARs and thus yielding the strongest HMS across all methods. When
applying the SDW, Matrix Profile slightly surpasses TimeVQVAE-AD in terms of overall
balance, reaching similar sensitivities but slightly higher HMS values, although the differ-
ence in sensitivity between these two models is not statistically significant according to
McNemar’s test (p = 0.2482). Together, these operating regimes delineate a clear trade-off
curve: MADRID represents the low-alarm regime, TimeVQVAE-AD dominates under strict
evaluation criteria (no SDW), and Matrix Profile leads in the extended detection framework
(with SDW), highlighting that different models may be preferable depending on the chosen
evaluation window and clinical tolerance for false alarms.

The responder analysis further highlights substantial inter-individual variability. Un-
der the SDW, both Matrix Profile and TimeVQVAE-AD achieved 100% sensitivity in re-
sponders, but Matrix Profile at more moderate alarm rates around 13.27 FA/h, while
TimeVQVAE-AD had 40.46 FA/h. In contrast, the all-patient sensitivity was consistently

Sensors 2025, 25, 7687

16 of 27

lower, reflecting the presence of non-responders whose ECG signatures showed weaker or
atypical ictal dynamics. Our findings are consistent with prior research showing that ECG-
based seizure detection methods perform better on responders (patients with a maximum
heart rate change of >50 BPM during a seizure) [17,29]. Furthermore, the divergence be-
tween responder and all-patient performance suggests that personalization strategies, such
as patient-specific thresholds or adaptive retraining, will be essential to lift performance in
non-responders without over-alarming responders.

This interpretation is further supported by the CI reported in the Appendix A. Several
of the sensitivity and HMS intervals remain relatively broad, reflecting substantial disper-
sion in patient-wise performance. Because these intervals are derived from patient-level
sensitivity estimates, their width highlights the pronounced heterogeneity in how seizures
are detected across individuals in the SeizeIT2 cohort. This variability underscores the
importance of personalization strategies.

Beyond inter-individual variability, a second source of heterogeneity arises from dif-
ferences between seizure types themselves. Under the strict evaluation criterion, seizure
types characterized by pronounced motor activity or marked autonomic involvement such
as focal-to-bilateral tonic-clonic seizures or hyperkinetic impaired-awareness seizures ex-
hibited the highest sensitivity, whereas non-motor and subtle impaired-awareness seizures
remained substantially more difficult to identify. This pattern aligns with the expectation
that stronger sympathetic activation and movement-related artifacts produce clearer ECG
anomalies, but it partially matches prior ECG-based findings. Vandecasteele et al. [30]
reported that focal aware (a) and focal-to-bilateral tonic-clonic (f2b) seizures were detected
more reliably on only ECG data than focal impaired-awareness (ia) seizures, whereas in
our analysis, impaired-awareness seizures with prominent motor features are among the
best-detected types, while non-motor ia events remain challenging. At the same time,
both studies consistently identify focal-to-bilateral tonic-clonic seizures as one of the most
reliably captured types in ECG-based detection. This broader trend is further supported by
HRV-based work: Nouboue et al. [31] reported higher sensitivity for convulsive than for
non-convulsive seizures, and Chen et al. [32] found more frequent and pronounced ictal
tachycardia in complex-partial (=ia) and secondarily generalized seizures (=f2b) compared
to simple-partial events (=a).

When applying the SDW, however, sensitivities increased across all seizure types,
with several categories exceeding 90%. This uniform improvement suggests that many
seizure-related ECG changes occur outside the narrowly defined EEG onset window,
particularly in seizure types with gradual autonomic buildup or post-ictal cardiac effects.
Taken together, these findings indicate that ECG-based detection is most effective for
seizures with robust autonomic signatures, while the SDW framework mitigates some of
the challenges inherent to more subtle seizure types by capturing clinically relevant pre-
and post-ictal cardiac dynamics.

A broader physiological perspective helps contextualize these findings, as the ECG
anomalies detected by our models ultimately arise from generic autonomic and cardio-
physiological responses. Previous studies have demonstrated that epileptic seizures are
often accompanied by characteristic changes in cardiac activity, including alterations in
ECG waveform morphology [33,34]. These effects are generally attributed to rapid shifts
in autonomic regulation, where seizures can briefly increase sympathetic drive or reduce
vagal influence [35]. Such autonomic responses can lead to measurable changes in heart
rate as well as in specific ECG segments [35,36]. Our findings are consistent with this line of
research, as the evaluated models capture several of these atypical seizure-related cardiac
patterns as anomalies. At the same time, the approaches used here do not aim to explain

Sensors 2025, 25, 7687

17 of 27

the underlying physiology in full detail, but rather to make use of the observable ECG
dynamics that reliably co-occur with many seizures.

Bhagubai et al. [11] also evaluated two models on the SeizeIT2 dataset using EEG data,
a Support Vector Machine (SVM) and the deep learning architecture ChronoNet. Similar
to our results, their findings illustrate the same fundamental trade-off between sensitivity
and false-alarm rate: while ChronoNet achieved the highest sensitivity reported in their
study (84.2%), this operating point corresponded to 100.5 FA/h. The SVM reached a lower
sensitivity (71.1%) with substantially fewer false alarms (11.0 FA/h).

In contrast, our experiments using only ECG data show that the TimeVQVAE-AD
model, as our best performing model without the SDW extension, reaches a comparable
sensitivity of 82.79% while producing nearly four times fewer false alarms per hour than
ChronoNet (26.12 FA/h vs. 100.5 FA/h). This relationship is illustrated in Figure 8,
which directly compares sensitivities and false-alarm rates of EEG-based and ECG-based
approaches. A direct comparison with the SVM baseline is less straightforward, as none
of the ECG or EEG models operate at a similar sensitivity-to-false-alarm ratio. When
optimizing TimeVQVAE-AD for minimal false alarms (approximately 8 FA/h), sensitivity
decreases to 36.9%, indicating that future work could explore an SVM-based approach
applied to ECG data.

(a) Sensitivity comparison

(b) False-alarm comparison

Figure 8. Comparison of EEG-based and ECG-based seizure detection performance on the SeizeIT2
dataset. (a) Sensitivity of ChronoNet and SVM (EEG-based baselines from Bhagubai et al. [11])
compared with TimeVQVAE-AD evaluated on ECG data in its sensitivity-optimized and false-alarm-
optimized configurations. (b) Corresponding false-alarm rates (FA/h) for the same models. The
figure highlights the fundamental trade-off between sensitivity and false-alarm rate and demonstrates
that ECG-based TimeVQVAE-AD can achieve sensitivity comparable to ChronoNet while producing
substantially fewer false alarms.

While some earlier studies working exclusively with ECG data have reported lower
FAR values [16,29,37], these results were often achieved on smaller or more curated
datasets. Seth et al. [21] found that in their systematic review, none of the reviewed ECG-
only studies have been validated on cohorts exceeding 43 patients. In contrast, the SeizeIT2
dataset encompasses a broader and more heterogeneous patient population, which intro-
duces additional variability but also better reflects real-world conditions. In line with calls
in the literature for more open benchmark datasets [38,39], we encourage the community to
further explore SeizeIT2, develop new approaches, and share results to support transparent
comparison and collective progress in seizure detection research.

Building on this perspective, the use of large, open datasets such as SeizeIT2 can be
seen as a key enabler for scalable clinical translation. ECG sensors are already integrated
into many wearables and hospital monitors, making ECG-based approaches attractive for

Sensors 2025, 25, 7687

18 of 27

low-burden, widely deployable seizure monitoring. Although the achieved FARs remain
too high for autonomous clinical deployment (goal of 90% sensitivity and 2 FA/week
(≈0.01 FA/h)) [40], the sensitivity levels reached in this work already enable clinician-
assisted workflows. For example, an ECG-based anomaly detector embedded in a wearable
and linked to a smartphone application could screen the ECG in the background, notify
the user or caregiver about suspicious events, and store them as an objective seizure
diary that can be reviewed during consultations. In this scenario, clinicians would receive
preselected segments and summary statistics rather than raw continuous ECG, which
could support therapy adjustments, remote follow up, and shared decision making. From
the user perspective, such a wearable would provide a discreet and always available
companion that helps to document seizures more reliably. Moreover, the strong responder
performance indicates that ECG-based monitoring could be particularly useful for patients
with pronounced autonomic changes during seizures, where personalized models could be
calibrated to the individual wearable signal over time. Together, these elements outline a
realistic pathway for integrating ECG-based seizure detection into wearable devices and
clinical workflows once false alarms can be further reduced. In this sense, the presented
models should not be interpreted as standalone diagnostic tools, but as a first benchmark
that demonstrates the potential of ECG only anomaly detection on SeizeIT2 and motivates
future work on wearable centred applications.

4.2. Limitations and Further Research

This study has several limitations, which at the same time highlight promising direc-

tions for future research.

Our optimization for TimeVQVAE-AD was computationally constrained as follows:
we used a coarse grid search and capped training at a fixed 48 h budget per stage. As a
result, some models likely did not fully converge, and longer training or a broader search
may yield stronger performance. In the evaluation, we also set the rolling window stride to
the smallest value we could afford computationally, rather than the theoretical minimum
of a one-sample shift. While this ensured computational tractability, an even smaller stride
could provide denser coverage and potentially better accuracy.

Furthermore, we did not systematically evaluate the real-time capabilities of the
methods. The analysis of the dataset required several days of computation across all
methods, indicating that substantial optimization is necessary before practical deployment
becomes feasible. Future research should therefore aim to improve computational efficiency
and systematically investigate whether these anomaly-detection approaches can achieve
real-time performance.

Our seizure type analysis shows that some seizure types are detected considerably
more reliably than others across models. Although these findings highlight meaningful
differences in detectability, some seizure types are represented by only a small number of
events, with the smallest group comprising just four seizures. This constrains the robust-
ness of our overall assessment of detection reliability, especially for seizure types with low
sample sizes. Furthermore, we did not investigate the underlying physiological or algo-
rithmic causes in detail. Future work could explore these mechanisms more systematically
and assess whether model adaptations or even type-specific detection strategies such as
training dedicated models for selected seizure types may further improve performance.

In addition, the proposed methods were based solely on ECG data rather than feature-
based or multimodal anomaly detection, even though the dataset also provides additional
physiological modalities like EEG. While effective, this approach excludes the potential
benefits of domain-specific features such as HRV or other ECG-derived biomarkers, as well
as the complementary information that could be gained from combining multiple biosignals.

Sensors 2025, 25, 7687

19 of 27

Future research could therefore explore hybrid or multimodal approaches.including the
incorporation of HRV features or arrhythmia indicators, which may capture seizure-related
cardiac phenomena beyond the coarse waveform dynamics analyzed in the present study.
A direct comparison with earlier ECG detection approaches was not feasible within
our evaluation setup. In general, such comparisons are limited either by fundamental
methodological differences, most notably the use of personalized training schemes instead
of evaluation on unseen patients as required in the SeizeIT2 framework, or by the lack of
publicly available implementations, which hampers reproducibility. Nevertheless, prior
work has shown that personalization strategies can substantially improve sensitivity and
reduce false alarms [29,41]. These findings make personalization an interesting avenue
for future research; however, it is important to recognize that such approaches operate
under fundamentally different conditions than the models evaluated here, which were
assessed strictly on previously unseen patients. Incorporating personalized methods into
the SeizeIT2 benchmark would therefore require a dedicated extension of the evaluation
design and should be explored in future studies.

5. Conclusions

This study provides the first systematic benchmark of ECG-based seizure detection
on the large-scale SeizeIT2 dataset using three advanced anomaly-detection methods. By
analyzing more than 11,000 h of wearable ECG recordings with 886 video-EEG-verified
seizures, the evaluation yields a more realistic estimate of expected performance in everyday
real-world application.

The results demonstrate that seizure-wise sensitivities exceeding 90% are achievable.
Under the SDW, Matrix Profile achieved 98.16% sensitivity at 13.9 false alarms per hour
with a HMS of 92.60, while TimeVQVAE-AD reached 92.86% sensitivity at 15.25 false
alarms per hour with a HMS of 86.76. MADRID showed a different profile, with lower
sensitivity (65.24%) but substantially fewer alarms (3.96 FA/h), indicating that it can be
tuned for alarm reduction at the cost of missed detections. These findings highlight the
existence of distinct operating regimes: Matrix Profile provided the most favorable balance
between sensitivity and false alarms under the SDW, TimeVQVAE-AD dominates without
the SDW, and MADRID offered low-alarm configurations with moderate sensitivity.

Despite these encouraging sensitivities, the observed FAR remain far above levels
acceptable for practical use. In real-world scenarios, user acceptance typically requires
fewer than two false alarms per week, whereas the best-performing models in this study
still generated more than 10 FA/h. This discrepancy indicates that current implemen-
tations are not yet suitable for stand-alone deployment. However, they can be used as
pre-screening tools.

In conclusion, this work establishes a reproducible baseline for ECG-based seizure
detection on a large open dataset and underscores both the promise and the limitations of
anomaly-detection methods. Future research should prioritize strategies for false alarm
reduction, patient-specific adaptation, and multimodal signal integration in order to bridge
the gap between algorithmic performance and the requirements of real-world applicability.

Author Contributions: Conceptualization, T.R. and S.M.W.; methodology, C.R., J.F.H. and M.B.;
software, C.R., J.F.H. and M.B.; validation, C.R., J.F.H. and M.B.; formal analysis, C.R., J.F.H. and M.B.;
investigation, T.R. and S.M.W.; resources, T.R. and S.M.W.; writing—original draft preparation, C.R.,
J.F.H. and M.B.; writing—review and editing, T.R., S.M.W. and D.S.; visualization, C.R., J.F.H. and
M.B.; supervision, D.S.; project administration, T.R. and S.M.W.; funding acquisition, S.M.W. and D.S.
All authors have read and agreed to the published version of the manuscript.

Sensors 2025, 25, 7687

20 of 27

Funding: This research was funded by the state government of North Rhine-Westphalia, Germany
under the grant number ZM-2-08B.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: The dataset is publicly available for research, meets all legal and
ethical standards, and contains no personally identifiable information, thus ensuring subject privacy.

Data Availability Statement: The data presented in this study are openly available in OpenNeuro at
https://doi.org/10.18112/openneuro.ds005873.v1.1.0 (accessed on 17 March 2025), reference number
ds005873. The source code is available via a GitHub repository: https://github.com/creintjes/ecg-
seizure-detection.

Acknowledgments: During the preparation of this manuscript/study, the authors used GPT-5 for the
purposes of language refinement and as a programming copilot. It was employed to enhance clarity,
coherence, and coding accuracy without influencing the scientific interpretation or conclusions.
The authors have reviewed and edited the output and take full responsibility for the content of
this publication.

Conflicts of Interest: The authors declare no conflicts of interest.

Abbreviations

The following abbreviations are used in this manuscript:

AD
BPM
CI
ECG
EEG
FA
FAR
HMS
HRV
PwE
SDW
STFT
SVM
VQ-VAE Vector Quantized Variational Autoencoder

Anomaly Detection
Beats Per Minute
Confidence Interval
Electrocardiography
Electroencephalography
False Alarm
False-Alarm Rate
Harmonic Mean Score
Heart Rate Variability
People with Epilepsy
Seizure Detection Window
Short-Time Fourier Transform
Support Vector Machine

Appendix A. Additional Results Statistics

Table A1. McNemar’s test results comparing paired seizure detection outcomes between model pairs.
Comparisons are stratified by optimization objective and by whether SDW was applied. Reported
are the Chi-square statistics (with Yates’ correction) and corresponding p-values.

Model A

Model B

Optimized for

SDW
Applied

χ2

p-Value

Sensitivity
Sensitivity

TimeVQVAE-AD Matrix Profile
TimeVQVAE-AD Matrix Profile
TimeVQVAE-AD Matrix Profile HMS
TimeVQVAE-AD Matrix Profile HMS
FAR
TimeVQVAE-AD Matrix Profile
FAR
TimeVQVAE-AD Matrix Profile
Sensitivity
TimeVQVAE-AD MADRID
Sensitivity
TimeVQVAE-AD MADRID
HMS
TimeVQVAE-AD MADRID
HMS
TimeVQVAE-AD MADRID

Yes
No
Yes
No
Yes
No
Yes
No
Yes
No

1.3333
16.5000
62.1324
18.3824
14.1324
11.7551
46.0208
105.2174
40.5000
105.2174

0.2482
<0.0001
<0.0001
<0.0001
0.0002
0.0006
<0.0001
<0.0001
<0.0001
<0.0001

Sensors 2025, 25, 7687

21 of 27

Table A1. Cont.

Model A

Model B Optimized for

SDW
Applied

χ2

p-Value

TimeVQVAE-AD MADRID FAR
TimeVQVAE-AD MADRID FAR
Matrix Profile
Matrix Profile
Matrix Profile
Matrix Profile
Matrix Profile
Matrix Profile

MADRID Sensitivity
MADRID Sensitivity
MADRID HMS
MADRID HMS
MADRID FAR
MADRID FAR

Yes
No
Yes
No
Yes
No
Yes
No

85.0989
50.1607
48.1667
69.5904
7.6800
133.0647
55.1475
25.2903

<0.0001
<0.0001
<0.0001
<0.0001
0.0056
<0.0001
<0.0001
<0.0001

Table A2. 95% Confidence Intervals (CI) for Sensitivity, FAR, and HMS for all methods and optimiza-
tion objectives without SDW applied. CIs were computed across patients using bootstrapping.

Method

Optimized for

Sensitivity CI

FAR CI

HMS CI

Responder

All

Responder

All

Responder

All

Matrix Profile

FAR

MADRID

FAR

TimeVQVAE-AD FAR

Matrix Profile

Sensitivity

MADRID

Sensitivity

TimeVQVAE-AD Sensitivity

Matrix Profile

HMS

MADRID

HMS

TimeVQVAE-AD HMS

[28.10%,
65.56%]

[0.00%,
16.83%]

[23.10%,
63.10%]

[80.00%,
100.00%]

[17.94%,
49.54%]

[81.43%,
98.33%]

[76.58%,
96.67%]

[17.78%,
50.16%]

[80.71%,
98.33%]

[21.45%,
49.31%]

[0.00%,
8.84%]

[24.11%,
49.93%]

[55.26%,
81.92%]

[11.02%,
31.99%]

[73.42%,
90.28%]

[49.67%,
75.42%]

[10.53%,
31.99%]

[73.69%,
90.46%]

[1.75, 2.22]

[1.83, 2.15]

[0.06, 0.17]

[0.06, 0.14]

[7.61, 9.16]

[7.99, 9.21]

[50.81,
95.75]

[61.13,
89.19]

[1.30, 1.60]

[1.43, 1.65]

[25.14,
26.63]

[18.11,
27.57]

[25.61,
26.53]

[20.83,
27.52]

[1.29, 1.60]

[1.43, 1.64]

[25.16,
26.65]

[25.67,
26.60]

[27.98,
65.97]
[−0.04,
16.30]

[20.80,
59.00]

[45.42,
77.93]

[17.39,
48.45]

[70.46,
88.58]

[65.51,
88.75]

[18.26,
49.71]

[69.59,
88.07]

[20.95,
47.49]
[−0.04,
8.89]

[20.78,
47.20]

[22.45,
54.75]

[9.51,
30.75]

[62.51,
80.05]

[39.10,
66.64]

[10.12,
30.17]

[63.41,
79.67]

Table A3. 95% Confidence Intervals (CI) for Sensitivity, FAR, and HMS for all methods and optimiza-
tion objectives with SDW applied. CIs were computed across patients using bootstrapping.

Method

Optimized for

Sensitivity CI

FAR CI

HMS CI

Responder

All

Responder

All

Responder

All

Matrix Profile

FAR

MADRID

FAR

TimeVQVAE-AD FAR

Matrix Profile

Sensitivity

[50.00%,
83.33%]

[0.00%,
13.02%]

[43.08%,
74.06%]

[100.00%,
100.00%]

[41.00%,
68.32%]

[0.00%,
7.06%]

[50.06%,
71.85%]

[88.07%,
100.00%]

[1.74, 2.21]

[1.76, 2.09]

[0.02, 0.10]

[0.02, 0.07]

[3.52, 5.05]

[3.74, 4.74]

[11.68,
16.44]

[13.34,
16.80]

[49.17,
82.55]
[−0.02,
13.32]

[41.45,
72.41]

[93.31,
95.35]

[38.53,
66.02]
[−0.02,
7.12]

[48.50,
69.78]

[82.02,
94.17]

Sensors 2025, 25, 7687

22 of 27

Table A3. Cont.

Method

Optimized for

Sensitivity CI

FAR CI

HMS CI

Responder

All

Responder

All

Responder

All

MADRID

Sensitivity

TimeVQVAE-AD Sensitivity

Matrix Profile

HMS

MADRID

HMS

TimeVQVAE-AD HMS

[50.56%,
86.11%]

[100.00%,
100.00%]

[96.67%,
100.00%]

[49.43%,
84.46%]

[83.33%,
100.00%]

[50.71%,
74.34%]

[89.29%,
100.00%]

[87.46%,
99.71%]

[50.37%,
74.29%]

[83.93%,
100.00%]

[3.43, 4.09]

[3.76, 4.23]

[39.32,
41.50]

[9.55,
13.31]

[38.34,
40.82]

[10.92,
13.58]

[3.45, 4.09]

[3.76, 4.23]

[14.69,
16.45]

[14.37,
16.07]

[48.34,
84.07]

[83.44,
84.28]

[91.73,
96.03]

[49.55,
83.05]

[77.20,
93.93]

[48.89,
72.95]

[73.30,
84.50]

[82.50,
94.86]

[48.66,
72.07]

[77.96,
93.83]

Appendix B. Configurations Used in Experiments

Table A4. Matrix Profile: configuration details.

Optimized for

SDW

Key Parameters

FAR

Sensitivity

HMS

FAR

Sensitivity

HMS

No

No

No

Yes

Yes

Yes

anomaly_ratio=0.01, max_gap=30, n_cons=35,
window=25, downsample=8

anomaly_ratio=0.06, max_gap=0.2, n_cons=1,
window=25, downsample=8

anomaly_ratio=0.06, max_gap=5, n_cons=1,
window=25, downsample=8

anomaly_ratio=0.01, max_gap=30, n_cons=35,
window=25, downsample=8

anomaly_ratio=0.06, max_gap=20, n_cons=1,
window=25, downsample=8

anomaly_ratio=0.06, max_gap=30, n_cons=1,
window=25, downsample=8

Table A5. MADRID: configuration details.

Optimized for

SDW

Key Parameters

FAR

No

Sensitivity

No

HMS

No

time-based clustering (600 s),
threshold=0.66537, mmin = 10 s, mmax = 100 s,
mstep = 10 s, k = 5, percentile=90%,
overlap≤25%, train_minutes=20

time-based clustering (600 s),
threshold=0.59463, mmin = 10 s, mmax = 100 s,
mstep = 10 s, k = 5, percentile=90%,
overlap≤25%, train_minutes=20

time-based clustering (600 s),
threshold=0.61408, mmin = 10 s, mmax = 100 s,
mstep = 10 s, k = 5, percentile=90%,
overlap≤25%, train_minutes=20

Sensors 2025, 25, 7687

23 of 27

Table A5. Cont.

Optimized for

SDW

Key Parameters

FAR

Yes

Sensitivity

Yes

HMS

Yes

time-based clustering (180 s),
threshold=0.66537, mmin = 10 s, mmax = 100 s,
mstep = 10 s, k = 5, percentile=90%,
overlap≤25%, train_minutes=20

time-based clustering (180 s),
threshold=0.59623, mmin = 10 s, mmax = 100 s,
mstep = 10 s, k = 5, percentile=90%,
overlap≤25%, train_minutes=20

time-based clustering (180 s),
threshold=0.61330, mmin = 10 s, mmax = 100 s,
mstep = 10 s, k = 5, percentile=90%,
overlap≤25%, train_minutes=20

Table A6. TimeVQVAE-AD: configuration details.

Optimized for

SDW

Key Parameters

FAR

Sensitivity

HMS

FAR

Sensitivity

HMS

No

No

No

Yes

Yes

Yes

time-based clustering (90 s), threshold=0.75,
expand_labels=False

time-based clustering (45 s), threshold=0.70,
expand_labels=False

time-based clustering (45 s), threshold=0.70,
expand_labels=False

time-based clustering (120 s), threshold=0.75,
expand_labels=True

time-based clustering (30 s), threshold=0.65,
expand_labels=True

time-based clustering (60 s), threshold=0.70,
expand_labels=True

Table A7. Overall TimeVQVAE-AD configuration (summary).

Component

Dataset

Dataset

Dataset

Dataset

Dataset

Dataset

Dataset

Training

Training

Trainer

Field

name

Value

SeizeIT2-ECG-TimeVQVAE-AD

downsample_freq

stride

in_channels

batch_sizes

8

−1

1

{stage1: 1792, stage2: 576}

n_periods/bpm

120/75

expand_labels

“see config”

lr

{stage1: 0.001, stage2: 0.001}

linear_warmup_rate

0.1

max_hours

{stage1: 48, stage2: 48}

Sensors 2025, 25, 7687

24 of 27

Table A7. Cont.

Component

Field

Value

val_check_interval

{stage1: 1000, stage2: 1000}

Encoder/Decoder

n_resnet_blocks

dim

downsampled _width

n_fft

codebook_size

choice_temperature

T

128

10/10

16

16

1024

2

25

mask_scheduling _func

cosine

MaskGIT prior

hidden_dim/depth/heads 384/8/6

MaskGIT prior

attn_dim_head/ff_mult

32/4

MaskGIT prior

rmsnorm/dropout

true/0.2

Trainer

Encoder

Encoder

VQ-VAE

VQ-VAE

MaskGIT

MaskGIT

MaskGIT

Windows

Evaluation

Evaluation

Evaluation

window_size

768

threshold

“see Table A6”

latent_window
_size_rates

rolling_window
_stride_rate

[0.005, 0.01, 0.03]

0.25

0.95

Evaluation

q

Appendix C. Seizure Type Analysis

Figure A1. Sensitivity by seizure type (strict evaluation, no SDW) for all three anomaly-detection
models (TimeVQVAE-AD, Matrix Profile, and MADRID) and their across-model average. Bars are
grouped by seizure type and sorted by average sensitivity; the number of seizures per type is shown
below each label.

Sensors 2025, 25, 7687

25 of 27

Figure A2. Sensitivity by seizure type using the extended Seizure Detection Window (SDW; −5 min
to +3 min) for all three anomaly-detection models (TimeVQVAE-AD, Matrix Profile, and MADRID)
and their across-model average. Bars are grouped by seizure type and sorted by average sensitivity;
the number of seizures per type is shown below each label.

References

1.

2.
3.

4.

Bruno, E.; Simblett, S.; Lang, A.; Biondi, A.; Odoi, C.; Schulze-Bonhage, A.; Wykes, T.; Richardson, M.P. Wearable technology in
epilepsy: The views of patients, caregivers, and healthcare professionals. Epilepsy Behav. 2018, 85, 141–149. [CrossRef] [PubMed]
Jones, M.W. Consequences of Epilepsy: Why do We Treat Seizures? Can. J. Neurol. Sci. 1998, 25, S24–S26. [CrossRef] [PubMed]
Clary, H.M.; Josephson, S.A.; Franklin, G.; Herman, S.T.; Hopp, J.L.; Hughes, I.; Meunier, L.; Moura, L.M.; Parker-McFadden, B.;
Pugh, M.J.; et al. Seizure Frequency Process and Outcome Quality Measures. Neurology 2022, 98, 583–590. [CrossRef] [PubMed]
Zabler, N.; Swinnen, L.; Biondi, A.; Novitskaya, Y.; Schütz, E.; Epitashvili, N.; Dümpelmann, M.; Richardson, M.P.; Van Paesschen,
W.; Schulze-Bonhage, A.; et al. High precision in epileptic seizure self-reporting with an app diary. Sci. Rep. 2024, 14, 15823.
[CrossRef]

5. Hoppe, C.; Poepel, A.; Elger, C.E. Epilepsy: Accuracy of Patient Seizure Counts. Arch. Neurol. 2007, 64, 1595–1599. [CrossRef]
6.

Swinnen, L.; Chatzichristos, C.; Jansen, K.; Lagae, L.; Depondt, C.; Seynaeve, L.; Vancaester, E.; Van Dycke, A.; Macea, J.; Vandecas-
teele, K.; et al. Accurate detection of typical absence seizures in adults and children using a two-channel electroencephalographic
wearable behind the ears. Epilepsia 2021, 62, 2741–2752. [CrossRef]
Vandecasteele, K.; De Cooman, T.; Gu, Y.; Cleeren, E.; Claes, K.; Van Paesschen, W.; Van Huffel, S.; Hunyadi, B. Automated
Epileptic Seizure Detection Based on Wearable ECG and PPG in a Hospital Environment. Sensors 2017, 17, 2338. [CrossRef]
Kim, T.; Nguyen, P.; Pham, N.; Bui, N.; Truong, H.; Ha, S.; Vu, T. Epileptic Seizure Detection and Experimental Treatment: A
Review. Front. Neurol. 2020, 11, 701. [CrossRef]
Van de Vel, A.; Cuppens, K.; Bonroy, B.; Milosevic, M.; Jansen, K.; Van Huffel, S.; Vanrumste, B.; Lagae, L.; Ceulemans, B.
Non-EEG seizure-detection systems and potential SUDEP prevention: State of the art. Seizure 2013, 22, 345–355. [CrossRef]

7.

8.

9.

10. Chatzichristos, C.; Claro Bhagubai, M. SeizeIT1, version 1.1; KU Leuven: Leuven, Belgium, 2023. [CrossRef]
11. Bhagubai, M.; Chatzichristos, C.; Swinnen, L.; Macea, J.; Zhang, J.; Lagae, L.; Jansen, K.; Schulze-Bonhage, A.; Sales, F.; Mahler, B.;

et al. SeizeIT2: Wearable Dataset Of Patients With Focal Epilepsy. Sci. Data 2025, 12, 1228. [CrossRef]

12. Gu, Y.; Cleeren, E.; Dan, J.; Claes, K.; Van Paesschen, W.; Van Huffel, S.; Hunyadi, B. Comparison between Scalp EEG and
Behind-the-Ear EEG for Development of a Wearable Seizure Detection System for Patients with Focal Epilepsy. Sensors 2018,
18, 29. [CrossRef] [PubMed]
Schulze-Bonhage, A.; Sales, F.; Wagner, K.; Teotonio, R.; Carius, A.; Schelle, A.; Ihle, M. Views of patients with epilepsy on seizure
prediction devices. Epilepsy Behav. 2010, 18, 388–396. [CrossRef] [PubMed]

13.

14. Bouzid, Z.; Al-Zaiti, S.S.; Bond, R.; Sejdi´c, E. Remote and wearable ECG devices with diagnostic abilities in adults: A state-of-the-

science scoping review. Heart Rhythm 2022, 19, 1192–1201. [CrossRef]

15. Wolf, S.; Seidel, P.; Ockenga, T.A.; Schoder, D. Heart-to-Wear: Assessing the Accuracy of Heart Rate Sensor Measurements of
Wearable Devices in Uncontrolled Environments. In Proceedings of the 2024 Hawaii International Conference on System Sciences
(HICSS), Honolulu, HI, USA, 3–6 January 2024; pp. 3183–3191. [CrossRef]

16. Miron, G.; Halimeh, M.; Jeppesen, J.; Loddenkemper, T.; Meisel, C. Autonomic biosignals, seizure detection, and forecasting.

Epilepsia 2024, 66, 25–38. [CrossRef] [PubMed]

Sensors 2025, 25, 7687

26 of 27

17.

Jeppesen, J.; Fuglsang-Frederiksen, A.; Johansen, P.; Christensen, J.; Wüstenhagen, S.; Tankisi, H.; Qerama, E.; Hess, A.; Beniczky,
S. Seizure detection based on heart rate variability using a wearable electrocardiography device. Epilepsia 2019, 60, 2105–2113.
[CrossRef]

18. Afra, P.; Adamolekun, B.; Aydemir, S.; Watson, G.D.R. Evolution of the Vagus Nerve Stimulation (VNS) Therapy System

Technology for Drug-Resistant Epilepsy. Front. Med. Technol. 2021, 3, 696543. [CrossRef]

19. Karasmanoglou, A.; Antonakakis, M.; Zervakis, M. ECG-Based Semi-Supervised Anomaly Detection for Early Detection and

Monitoring of Epileptic Seizures. Int. J. Environ. Res. Public Health 2023, 20, 5000. [CrossRef]

20. van Westrhenen, A.; De Cooman, T.; Lazeron, R.H.C.; Van Huffel, S.; Thijs, R.D. Ictal autonomic changes as a tool for seizure

21.

22.

detection: A systematic review. Clin. Auton. Res. 2019, 29, 161–181. [CrossRef]
Seth, E.A.; Watterson, J.; Xie, J.; Arulsamy, A.; Md Yusof, H.H.; Ngadimon, I.W.; Khoo, C.S.; Kadirvelu, A.; Shaikh, M.F. Feasibility
of cardiac-based seizure detection and prediction: A systematic review of non-invasive wearable sensor-based studies. Epilepsia
Open 2024, 9, 41–59. [CrossRef]
Shah, V.; Golmohammadi, M.; Obeid, I.; Picone, J. Objective evaluation metrics for automatic classification of EEG events. In
Biomedical Signal Processing; Springer International Publishing: Cham, Switzerland, 2021; pp. 223–255. [CrossRef]

23. Elgendi, M. Fast QRS Detection with an Optimized Knowledge-Based Method: Evaluation on 11 Standard ECG Databases. PLoS

ONE 2013, 8, e73557. [CrossRef]

24. Yeh, C.C.M.; Zhu, Y.; Ulanova, L.; Begum, N.; Ding, Y.; Dau, H.A.; Silva, D.F.; Mueen, A.; Keogh, E. Matrix Profile I: All Pairs
Similarity Joins for Time Series: A Unifying View That Includes Motifs, Discords and Shapelets. In Proceedings of the 2016 IEEE
16th International Conference on Data Mining (ICDM), Barcelona, Spain, 12–15 December 2016; pp. 1317–1322. [CrossRef]
25. Lu, Y.; Srinivas, T.V.A.; Nakamura, T.; Imamura, M.; Keogh, E. Matrix Profile XXX: MADRID: A Hyper-Anytime and Parameter-
Free Algorithm to Find Time Series Anomalies of all Lengths. In Proceedings of the 2023 IEEE International Conference on Data
Mining (ICDM), Shanghai, China, 1–4 December 2023; pp. 1199–1204. [CrossRef]

26. Lee, D.; Malacarne, S.; Aune, E. Explainable Time Series Anomaly Detection using Masked Latent Generative Modeling. Pattern

Recognit. 2024, 156, 110826. [CrossRef]

27. Pavei, J.; Heinzen, R.G.; Novakova, B.; Walz, R.; Serra, A.J.; Reuber, M.; Ponnusamy, A.; Marques, J.L.B. Early Seizure Detection

28.

29.

Based on Cardiac Autonomic Regulation Dynamics. Front. Physiol. 2017, 8, 765. [CrossRef] [PubMed]
Jeppesen, J.; Beniczky, S.; Johansen, P.; Sidenius, P.; Fuglsang-Frederiksen, A. Detection of epileptic seizures with a modified heart
rate variability algorithm based on Lorenz plot. Seizure 2015, 24, 1–7. [CrossRef] [PubMed]
Jeppesen, J.; Christensen, J.; Johansen, P.; Beniczky, S. Personalized seizure detection using logistic regression machine learning
based on wearable ECG-monitoring device. Seizure Eur. J. Epilepsy 2023, 107, 155–161. [CrossRef]

30. Vandecasteele, K.; De Cooman, T.; Chatzichristos, C.; Cleeren, E.; Swinnen, L.; Macea Ortiz, J.; Van Huffel, S.; Dümpelmann, M.;
Schulze-Bonhage, A.; De Vos, M.; et al. The power of ECG in multimodal patient-specific seizure monitoring: Added value to an
EEG-based detector using limited channels. Epilepsia 2021, 62, 2333–2343. [CrossRef]

31. Nouboue, C.; Diab, E.; Gacquer, W.; Derambure, P.; Perin, B.; Chen, S.; Mercier-Bryczman, M.; Jonckheere, J.D.; Szurhaj, W. Heart
rate variability-based detection of epileptic seizures: Machine learning analysis and characterization of discriminant metrics.
Clin. Neurophysiol. 2025, 177, 2110793. [CrossRef]

32. Chen, W.; Guo, C.L.; Zhang, P.S.; Liu, C.; Qiao, H.; Zhang, J.G.; Meng, F.G. Heart rate changes in partial seizures: Analysis of

33.

influencing factors among refractory patients. BMC Neurol. 2014, 14, 135. [CrossRef]
van der Lende, M.; Surges, R.; Sander, J.W.; Thijs, R.D. Cardiac arrhythmias during or after epileptic seizures. J. Neurol. Neurosurg.
Psychiatry 2016, 87, 69–74. [CrossRef]

34. Gigli, L.; Sala, S.; Preda, A.; Okubo, K.; Peretto, G.; Frontera, A.; Varrenti, M.; Baroni, M.; Carbonaro, M.; Vargiu, S.; et al.
Electrocardiogram Changes in the Postictal Phase of Epileptic Seizure: Results from a Prospective Study. J. Clin. Med. 2023,
12, 4098 . [CrossRef]
Senapati, S.G.; Bhanushali, A.K.; Lahori, S.; Naagendran, M.S.; Sriram, S.; Ganguly, A.; Pusa, M.; Damani, D.N.; Kulkarni, K.;
Arunachalam, S.P. Mapping of Neuro-Cardiac Electrophysiology: Interlinking Epilepsy and Arrhythmia. J. Cardiovasc. Dev. Dis.
2023, 10, 433 . [CrossRef]

35.

36. Ufongene, C.; El Atrache, R.; Loddenkemper, T.; Meisel, C. Electrocardiographic changes associated with epilepsy beyond heart
rate and their utilization in future seizure detection and forecasting methods. Clin. Neurophysiol. Off. J. Int. Fed. Clin. Neurophysiol.
2020, 131, 866–879. [CrossRef]
Jeppesen, J.; Fuglsang-Frederiksen, A.; Johansen, P.; Christensen, J.; Wüstenhagen, S.; Tankisi, H.; Qerama, E.; Beniczky, S. Seizure
detection using heart rate variability: A prospective validation study. Epilepsia 2020, 61, S41–S46. [CrossRef]

37.

38. Mei, Z.; Zhao, X.; Chen, H.; Chen, W. Bio-Signal Complexity Analysis in Epileptic Seizure Monitoring: A Topic Review. Sensors

2018, 18, 1720. [CrossRef]

39. Beniczky, S.; Ryvlin, P. Standards for testing and clinical validation of seizure detection devices. Epilepsia 2018, 59, 9–13. [CrossRef]

Sensors 2025, 25, 7687

27 of 27

40. Van De Vel, A.; Smets, K.; Wouters, K.; Ceulemans, B. Automated non-EEG based seizure detection: Do users have a say? Epilepsy

41.

Behav. 2016, 62, 121–128. [CrossRef]
Forooghifar, F.; Aminifar, A.; Teijeiro, T.; Aminifar, A.; Jeppesen, J.; Beniczky, S.; Atienza, D. Self-Aware Anomaly-Detection for
Epilepsy Monitoring on Low-Power Wearable Electrocardiographic Devices. In Proceedings of the 2021 IEEE 3rd International
Conference on Artificial Intelligence Circuits and Systems (AICAS), Washington, DC, USA, 6–9 June 2021; pp. 1–4. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
