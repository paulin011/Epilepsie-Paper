# Lu et al. - 2025 - Leveraging Channel Coherence in Long-Term iEEG Data for Seizure Prediction

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 8, AUGUST 2025

5541

Leveraging Channel Coherence in Long-Term
iEEG Data for Seizure Prediction

Sha Lu , Lin Liu , Jiuyong Li

, Jordan Chambers , Mark J. Cook , and David B. Grayden

Abstract—Epilepsy affects millions worldwide, posing
signiﬁcant challenges due to the erratic and unexpected
nature of seizures. Despite advancements, existing seizure
prediction techniques remain limited in their ability to fore-
cast seizures with high accuracy,
impacting the quality
of life for those with epilepsy. This research introduces
the Coherence-based Seizure Prediction (CoSP) method,
which integrates coherence analysis with deep learning
to enhance seizure prediction efﬁcacy.
In CoSP, elec-
troencephalography (EEG) recordings are divided into 10-
second segments to extract channel pairwise coherence.
This coherence data is then used to train a four-layer con-
volutional neural network to predict the probability of be-
ing in a preictal state. The predicted probabilities are then
processed to issue seizure warnings. CoSP was evaluated
in a pseudo-prospective setting using long-term iEEG data
from ten patients in the NeuroVista seizure advisory sys-
tem. CoSP demonstrated promising predictive performance
across a range of preictal intervals (4 to 180 minutes).
CoSP achieved a median Seizure Sensitivity (SS) of 0.79,
a median false alarm rate of 0.15 per hour, and a median
Time in Warning (TiW) of 27%, highlighting its potential for
accurate and reliable seizure prediction. Statistical analy-
sis conﬁrmed that CoSP signiﬁcantly outperformed chance
(p = 0.001) and other baseline methods (p <0.05) under
similar evaluation conﬁgurations.

Index Terms—Seizure prediction, seizure forecasting,

iEEG, coherence, epilepsy.

Received 9 July 2024; revised 27 February 2025; accepted 25 March
2025. Date of publication 1 April 2025; date of current version 7 August
2025. This work was supported by the Australian Government through
the Australian Research Council’s Training Centre in Cognitive Com-
puting for Medical Technologies under project Number ICI70200030.
(Corresponding authors: Sha Lu; Lin Liu; David B. Grayden.)

This work involved human subjects or animals in its research. The
NeuroVista dataset used in the research was collected following ethical
approval from the Human Research Ethics Committee at St. Vincent’s
Hospital, Melbourne under Application No. LRR145/13.

Sha Lu, Lin Liu, and Jiuyong Li are with the STEM, University of South
Australia, Adelaide, SA 5001, Australia (e-mail: Sha.Lu@unisa.edu.au;
Lin.Liu@unisa.edu.au; Jiuyong.Li@unisa.edu.au).

Jordan Chambers is with the Department of Biomedical Engineering,
The University of Melbourne, Melbourne, VIC 3010, Australia (e-mail:
jordanc@unimelb.edu.au).

Mark J. Cook and David B. Grayden are with the Department of
Biomedical Engineering, The University of Melbourne, Melbourne, VIC
3010, Australia, and also with the Department of Medicine, St. Vin-
cent’s Hospital and Graeme Clark Institute, University of Melbourne,
Melbourne, VIC 3010, Australia (e-mail: markcook@unimelb.edu.au;
grayden@unimelb.edu.au).

Digital Object Identiﬁer 10.1109/JBHI.2025.3556775

I. INTRODUCTION

E PILEPSY is a signiﬁcant neurological disorder character-

ized by recurrent seizures that can manifest as abnormal
movements, behaviors, or altered consciousness, and it affects
approximately 50 million people worldwide [32]. The primary
approach to managing epilepsy involves the use of anti-epileptic
drugs and surgical interventions in selected cases unresponsive
to medication. However, about 30% of epilepsy patients do not
respond to these treatments, living with seizures refractory to
current pharmacological and surgical options [32]. The erratic
and often unexpected nature of seizures poses challenges for
these patients in maintaining regular daily activities. Recent
advancements in computational models, particularly those based
on electroencephalography (EEG) data, have shown promise in
predicting seizures, potentially enhancing the quality of life for
epilepsy patients [11], [21], [32].

EEG is a crucial tool for diagnosing and treating epilepsy [5],
[22], [34]. A seizure is characterized by an excessive, hyper-
synchronous neuronal discharge in the brain, which is often
detectable through EEG [40]. There are two primary types of
EEG data: scalp EEG and intracranial EEG (iEEG). Scalp EEG,
a non-invasive technique, involves placing electrodes on the
patient’s scalp, making it suitable for broad diagnostic pur-
poses. Conversely, iEEG requires the implantation of electrodes
directly onto or within the brain, offering higher resolution
signals critical for studying severe refractory epilepsy. Recent
technological advances, exempliﬁed by initiatives such as Neu-
roVista [17] and Epi-Minder [6], are advancing the ﬁeld through
the development of technologies for chronic implantation of
electrodes for continuous, ultra-long-term seizure monitoring.
When conducting seizure prediction based on EEG data, tradi-
tional approaches often require the manual extraction of features
from EEG data before the application of seizure prediction
algorithms [15], [22]. This process requires expert knowledge
to identify the features to ensure the efﬁcacy and accuracy of
predictions [11], [18], [21]. In contrast, deep learning methods
provide the advantage of automatically extracting features from
EEG recordings [25]. A common deep learning approach is
to utilize deep neural network classiﬁcation models trained
through supervised learning. Speciﬁcally, EEG recordings are
categorized into four phases: preictal (the period shortly before
a seizure onset), ictal (during a seizure), postictal (immediately
after a seizure), and interictal (the period between seizures) [33].
Seizure prediction can be considered a classiﬁcation task that

© 2025 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more
information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

5542

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 8, AUGUST 2025

aims to distinguish between the preictal and interictal peri-
ods. Various neural network architectures have been explored
for seizure prediction, such as convolutional neural network
(CNN) [7], [12], [26], long short-term memory (LSTM) net-
work [9], [14], and graph neural network (GNN) [24].

However, most seizure prediction methods utilize short-term
EEG data for their analysis, and only a few studies are based on
long-term EEG data. Research [13] has highlighted that seizure
prediction models trained on time-correlated data from short-
term EEG recordings often struggle to generalize to datasets
gathered in more prospective, real-world settings. In contrast,
long-term EEG data, captured from patients during their daily
activities, not only provide a larger volume of data but also
exhibit greater variability. This helps mitigate the issue of time-
correlation in analyses, presenting a more robust basis for seizure
prediction models.

Therefore, this study utilized long-term iEEG data from
the NeuroVista dataset [17] to evaluate the effectiveness of
the proposed method. Previous research using the NeuroVista
dataset has advanced the ﬁeld by demonstrating the potential of
critical slowdown as a biomarker for seizure prediction [16], the
informativeness of high-frequency activity to epilepsy [27], [28],
and the application of CNNs on wearable devices for seizure
prediction [12]. Despite these advancements, there remain sig-
niﬁcant opportunities for further exploration and development
using this dataset.

Research [1], [10], [20], [31] has shown that channel coher-
ence in EEG data is a valuable indicator of epileptic seizures.
Coherence in EEG measures the linear dependency between
waveform signals across various frequency bands, and it pro-
vides insights into how different brain regions function in a
coordinated manner or synchronize with each other [30], [38],
[41]. Coherence analysis has been used in epilepsy research to
gain valuable insights into seizure dynamics [20], [23], detect
seizure onset [10], and understand changes in brain connectivity
during epileptic seizures [1], [31].

However, no EEG-based seizure prediction method to date
has utilized the full channel coherence as a feature. It is a
non-trivial task to effectively utilize channel coherence as a
feature for seizure prediction. The computation of pairwise
coherence across frequencies and time results in intricate, high-
dimensional data, posing challenges for traditional seizure pre-
diction methodologies that rely on manual feature extraction.
Prior work on coherence analysis tackled this by reducing di-
mensions either through channel strategies, selecting channel
subsets [31], averaging across channels [10], [20], [23], or
employing global coherence [1], or frequency approaches, such
as narrowing frequency ranges [1], [10], [23] or focusing on
key EEG sub-bands [20], [31]. These approaches, however, do
not fully leverage the detailed information available in pairwise
coherence.

In this paper, we propose to use full pairwise channel
coherence as a feature for seizure prediction. The proposed
Coherence-based Seizure Prediction (CoSP) method addresses
the challenges associated with the high-dimensionality and com-
plexity of pairwise coherence data by leveraging deep learning
techniques that excel at extracting meaningful features from

TABLE I
SEIZURE INFORMATION OF THE PATIENTS IN THE STUDY

intricate datasets. This enables the effective utilization of pair-
wise coherence for seizure prediction. CoSP has demonstrated
promising performance on the NeuroVista dataset across various
preictal intervals.

II. MATERIALS AND METHODS

A. Data Preparation

The NeuroVista dataset [17] comprises iEEG recordings from
15 patients with refractory focal epilepsy. The dataset, approved
by the Human Research Ethics Committee of St. Vincent’s
Hospital, Melbourne (approval LRR145/13), was collected for a
clinical feasibility study. The recording duration for each patient
ranges from 0.5 to 2.1 years, with an average duration of 520
days across all patients. The recordings were captured using 16
electrodes at a 400 Hz sampling rate. For our experiment, we
excluded patients with fewer than 20 lead seizures, speciﬁcally
patients 4, 5, 12, and 14. Additionally, we excluded patient 7 due
to the short recording duration. The total number of seizures and
the recording period for each patient are detailed in Table I. More
details about the data can be found at [17].

As is common in seizure prediction, we focused only on lead
seizures [16], which were deﬁned as seizures occurring without
any preceding seizures for at least four hours. To minimize
contamination from postictal data, we excluded recordings from
the four hours following a seizure. Additionally, the initial 100
days of EEG recordings for each patient were excluded to
address inconsistencies caused by device implantation [17]. The
remaining recordings were categorized into ictal, postictal, in-
terictal, and preictal phases, as illustrated in Fig. 2. Interictal and
preictal recordings were divided into 10-second EEG segments
for analysis.

The NeuroVista dataset includes data dropouts lasting from
minutes to days across all patients. To maintain data integrity,
any 10-second segments with more than 10% data dropouts were
excluded. For segments with less than 10% dropouts, missing
values were imputed with the median value of the respective
channels in that segment. EEG segments were ﬁltered using a
low-pass ﬁnite impulse response ﬁlter with a cutoff frequency
of 170 Hz to eliminate a 200 Hz artifact associated with device
charging [16].

LU et al.: LEVERAGING CHANNEL COHERENCE IN LONG-TERM IEEG DATA FOR SEIZURE PREDICTION

5543

Fig. 1. The framework of the CoSP method. The CoSP method comprises three main modules: coherence computation, preictal probability
estimation, and seizure warning. The input EEG segment X (dimensions 4000 × 16) is processed into a coherence matrix C (dimensions 120 × 109)
in the coherence computation module. The coherence matrix C is then passed through the preictal probability estimation module to yield the
estimated preictal probability ρ. The seizure warning module decides whether or not to issue a seizure warning based on ρ.

TABLE II
SEIZURE PREDICTION PERFORMANCE OF COSP

Subsequently, the EEG segments were divided into training,
validation, and test sets based on the lead seizure counts, with
recordings from the chronologically ﬁrst 60% of seizures used
for training, the next 20% for validation, and the ﬁnal 20% for
testing. The number of seizures used in the training, validation,
and test sets for each patient is detailed in Table II. It is important
to note that CoSP was trained using only the training and
validation sets, while the test set was employed exclusively for
evaluating model performance.

B. The CoSP Method

As shown in Fig. 1, the CoSP method comprises three main
modules: coherence computation, preictal probability estima-
tion, and a seizure warning module. In the coherence computa-
tion module, a pairwise coherence matrice are computed from
each 10-second EEG segment. These matrices are then used as
inputs in the preictal probability estimation module, where a
CNN predicts the probability of each segment being preictal.
Finally, the predicted probabilities are process in the seizure
warning module to issue seizure warnings.

1) Coherence Computation: Given an input EEG segment
X ∈ Rn×h, where n represents the number of time steps and
h represents the number of channels, this module computes the
pairwise coherence between channels across different frequency
bands.

Fig. 2. Schematic of EEG data preparation for our study: continuous
EEG recordings are shown as pale traces, with seizures marked by red
lines. Our analysis only focused on predicting lead seizures, indicated by
longer red lines with inverted triangles. The time between two consec-
utive seizure clusters was divided into four phases: the postictal period
(τs, set at 4 hours), the interictal period (τi), the preictal period (τp),
and the prediction reservation time (τr, set at 1 minute). For seizure
prediction, we utilize only the interictal and preictal data, which were
divided into 10-second EEG segments for subsequent analysis.

First, for a signal Xi ∈ Rn×1 in X, where i ∈ 1, . . . , h, we
compute the Fourier transform Xi(f ) at each frequency band
f , f ∈ 1, . . . , q. The Magnitude Squared Coherence (MSC) [35]
between signals from channels i and j, denoted as Xi and Xj,
at frequency f is then computed using the following formula:

Cij(f ) =

|Sij(f )|2
Sii(f ) · Sjj(f )

,

(1)

where Sij(f ) is the cross-spectral density between Xi and Xj
at frequency f , and Sii(f ) and Sjj(f ) are the power spectral
densities of Xi and Xj, respectively. They are deﬁned as:

Sab(f ) = E [Xa(f )X ∗

b (f )] , a, b ∈ {1, . . . , n}

(2)

where Xa(f ) and Xb(f ) are the Fourier transforms of Xa and
Xb, respectively, and the asterisk (*) indicates the complex
conjugate of the Fourier transform.

For each pair of channels, MSC is computed across all q
frequency bands. The result is a pairwise coherence matrix
C ∈ Rp×q, where p = h · (h − 1)/2. Each entry Ck(f ) in C
represents the coherence value, i.e., the MSC value, for the
k-th pair of channels at frequency f , where k ∈ {1, . . . , p}.

5544

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 8, AUGUST 2025

Fig. 3. An illustration of the coherence calculation in CoSP. (a) The raw
EEG signal of a 10-second segment with 4000 time steps and 16 chan-
nels. (b) Coherence heatmaps for discretized frequencies from 0.5 Hz
to 170 Hz. Each heatmap corresponds to a speciﬁc frequency, where
each cell depicts the MSC between channel pairs at that frequency,
with the color intensity indicating the level of coherence. The heatmaps
are symmetric with diagonal cells omitted to represent self-coherence
as 1. (c) A two-dimensional matrix stores the coherence values across
different frequency bands, with 120 channel pairs on the x-axis and 109
frequencies on the y-axis. The color of each point indicates the MSC
magnitude.

The matrix C serves as the input for the subsequent preictal
probability estimation module.

Fig. 3 presents an illustrative example of transforming a
10-second EEG segment in the NeuroVista dataset into the
pairwise coherence matrix as described above. The number
of time steps, n, is 4000, corresponding to a sampling rate
of 400 Hz. The segment comprises 16 channels, i.e., h = 16,
resulting in 120 channel pairs, i.e., p = 15 × 16/2 = 120 . The
frequency spectrum, which ranges from 0.5 Hz to 170 Hz, was
discretized at intervals of 1.6 Hz, yielding a total of 109 discrete
frequencies, i.e., q = 109.

2) Preictal Probability Estimation: The preictal probability
estimation module employs a CNN to predict the probability of
an 10-second EEG segment being preictal. As shown in Fig. 1
the CNN architecture consists of four convolutional blocks.
Each block includes batch normalization to standardize inputs,
a convolutional layer with ReLU activation for nonlinear pro-
cessing, and a max pooling layer to reduce spatial dimensions.
The convolutional sequence begins with 32 kernels of size 7x7,
followed by 64 kernels of size 5x5, then 128 kernels, and ﬁnally
256 kernels, both of size 3x3. All blocks use a stride of 1 and
perform max pooling over a 2x2 area.

When applying the CNN to the NeuroVista dataset, the input
is the coherence matrix C with the dimension of 120 × 109, with
output dimensions of the convolutional blocks being 60 × 54,
30 × 27, 15 × 15, and 7 × 6, respectively. After the convolu-
tional layers, the output is ﬂattened and passed through a fully
connected layer with 128 units, batch normalization, ReLU
activation, and a dropout rate of 50% to prevent overﬁtting. The
ﬁnal fully connected layer outputs the preictal probability of the
EEG segment, denoted as ρ.

In the model training, class imbalance is a challenge due to the
much longer interictal periods compared to the preictal periods.
To address this, we down-sampled the interictal segments and
up-sampled the preictal segments. For interictal sampling, we
ﬁrst identiﬁed speciﬁc days as the interictal interval preceding
the preictal period. During this interval, we selected the ﬁrst
10-second segment from every 10 minutes of EEG recordings.
For the preictal segments, we created overlapping samples by
taking 10-seconds segment at calculated time step intervals,
and the interval was calculated to ensure that the number of

preictal segments matched the count of interictal segments. To
maintain training efﬁciency, a cap of 18,000 training segments
was imposed when the total exceeded this number. The model
was trained using the Adam optimizer with a learning rate of
1 × 10−5 and binary cross-entropy as the loss function. In the
testing phase, 10-second interictal and preictal segments were
sampled without overlap throughout the entire duration of the
interictal and preictal periods.

3) Seizure Warning: Following a commonly used approach
in previous studies [4], [39], [42], the seizure warning module
processes the predicted probabilities from the probability esti-
mation module to generate seizure warnings. Two critical param-
eters for developing and evaluating seizure warning systems are
the Seizure Occurrence Period (SOP) and the Seizure Prediction
Horizon (SPH). The SPH provides patients with lead time to
take preventive measures, such as administering medication or
moving to a safe environment, before a seizure occurs. The SOP,
on the other hand, represents the window during which a seizure
is expected to happen. In CoSP, the SOP is set to match the
length of the preictal intervals, while the SPH corresponds to
the prediction reservation time, which is ﬁxed at 1 minute as
shown in Fig. 2.

To mitigate large variations in 10-second predictions, the
warning module applies a moving window to the predicted
probabilities of 10-second EEG segments with the window
length equal to the SOP. The moving average accumulates the
predicted outputs of multiple consecutive segments. This aggre-
gation mechanism smooths out noisy predictions and reduces the
likelihood of triggering warnings due to transient ﬂuctuations in
the predictions.

A warning is triggered when the averaged probability exceeds
a predeﬁned threshold. Once a warning is issued, the module
transitions into a warning state, initiating a refractory period
equal to the SOP length. During this refractory period, the
module is disabled from generating additional warnings, even if
another smoothed probability exceeds the threshold.

Following a common way [39], the warning module is retrig-
gerable. If a probability exceeds the threshold while the patient
remains in the warning state, the refractory period resets to
start from the corresponding 10-second segment, which extends
the warning state. In this design, an uninterrupted warning is
treated as a single warning, regardless of its total duration. This
mechanism helps prevent alarm fatigue by reducing excessive
alerts within a short time frame.

The choice of the threshold to trigger a warning signiﬁcantly
impacts the performance of the warning module. Hence with
CoSP, a grid search is performed to optimize this threshold,
aiming to maximize a balanced performance metric known as
the Performance Product (PP) (discussed in Section III-A). This
optimization is conducted exclusively on the validation set,
which contains data that chronologically precedes the test set,
to prevent information leakage to the test stage.

III. RESULTS

In this section, we ﬁrst introduce the performance metrics
used for evaluation. We then analyze the overall performance

LU et al.: LEVERAGING CHANNEL COHERENCE IN LONG-TERM IEEG DATA FOR SEIZURE PREDICTION

5545

of CoSP, followed by a comparative analysis against a chance
predictor and baseline methods.

A. Performance Metrics

The performance metrics utilized in the study included
Area Under the Receiver Operator Characteristic Curve (ROC
AUC) [29], Seizure Sensitivity (SS) [4], [42], Time in Warning
(TiW) [4], [42], False Positive Rate per hour (FPR/h) [42],
and Performance Product (PP) [16]. Notably, ROC AUC is
a segment-level metric, used to evaluate the performance of
the preictal probability estimation module using the predicted
probabilities of 10-second EEG segments. In contrast, SS, TiW,
FPR/h, and PP are seizure-level metrics, designed to assess the
overall performance of the CoSP model including the seizure
warning module.

ROC AUC is a threshold-free metric that evaluates the per-
formance of classiﬁcation models by summarizing the trade-off
between the True Positive Rate (TPR) and the False Positive Rate
(FPR) across all possible thresholds. It is particularly robust to
class imbalance because it considers the proportion of true pos-
itives and false positives relative to the total actual positives and
negatives. An ROC AUC value close to 1.0 indicates excellent
model performance, while a value of 0.5 suggests performance
equivalent to random guessing.

SS, TiW, FPR/h, and PP are threshold-dependent metrics used
to evaluate the performance of the CoSP model. SS measures the
proportion of seizures that are correctly predicted, with a seizure
considered successfully predicted if it occurs while the patient
is in a warning state. TiW represents the percentage of time a
patient remains in a warning state, calculated as the proportion of
time spent in the warning state relative to the total test time. False
Positive Rate per Hour (FPR/h) quantiﬁes the average number
of false warnings issued per hour. A warning is regarded as
false if no seizure occurs during the warning period. SS reﬂects
the sensitivity of the model, while TiW and FPR/h capture the
speciﬁcity.

To assess the overall performance, the PP metric is utilized,
providing a balanced measure of performance. The PP metric
is deﬁned as P P = SS × (1 − T iW ), where higher values of
SS (better seizure detection) combined with lower TiW (fewer
false alarms) indicate better overall model performance. A PP
value close to 1 signiﬁes optimal performance, balancing high
sensitivity and speciﬁcity.

B. Overall Performance of CoSP

In the experiments, the interictal period was set to 2 days prior
to the preictal period. As the optimal preictal duration varies
across individuals, we evaluated CoSP using preictal intervals
of 4, 15, 30, 45, 60, 90, 120, 150, and 180 minutes. The results
corresponding to the highest PP for each patient are reported in
Table II.

From Table II, the ROC AUC values across all patients exceed
0.5, indicating that CoSP consistently outperforms random pre-
diction at the segment level. Overall, the ROC AUC values range
from 0.65 to 0.91, with a median of 0.76. However, a high ROC
AUC does not necessarily translate to superior seizure-level

Fig. 4. PP values of CoSP models across different preictal interval
lengths.

performance. For instance, for Patient 11, CoSP achieves an
ROC AUC of 0.91 but a PP of 0.63, whereas for Patient 1, despite
a lower ROC AUC of 0.78, CoSP attains a higher PP of 0.68.
This discrepancy arises because seizure-level performance is
inﬂuenced not only by segment-level accuracy but also by the
selection of the warning triggering threshold and the distribution
of predicted probabilities across segments.

For seizure-level performance, SS ranges from 0.63 to 0.92,
with a median of 0.79. FPR/h varies from 0.03 to 0.79, with a
median of 0.15. TiW ranges from 12% to 35%, with a median
of 27%. PP ranges from 0.44 to 0.69, with a median of 0.64. In
summary, while CoSP achieves strong predictive performance,
considerable inter-patient variability remains.

Additionally, as shown in Table II, the optimal preictal interval
varies across patients. For some patients, such as patients 6, 11,
and 13, CoSP demonstrated the best performance with very short
preictal intervals of 4 minutes. In contrast, for patients 2 and
10, better results were achieved with longer preictal intervals
of 90 and 180 minutes, respectively. The PP values across all
preictal interval lengths is presented in Fig. 4, which shows
that the selection of the preictal interval greatly impacts seizure
prediction performance.

C. Comparison With the Baseline Methods

In this section, we compare CoSP with other seizure pre-
diction methods applied to the NeuroVista dataset. Several
studies have utilized the NeuroVista dataset for seizure pre-
diction, including both non-deep learning methods [16], [17],
[19], [28] and deep learning-based methods [2], [8], [12]. As
CoSP is a deep learning-based approach, we compare it with
all existing deep learning-based seizure prediction methods
that used the NeuroVista dataset. Additionally, we also com-
pare CoSP with two non-deep learning methods: the critical

5546

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 8, AUGUST 2025

TABLE III
PERFORMANCE COMPARISON OF COSP WITH OTHER STUDIES USING THE NEUROVISTA DATASET, PRESENTED IN THE FORMAT OF SS/TIW/PP

slowdown model [16], considered the state-of-the-art (SOTA)
on the NeuroVista dataset, and the machine learning approach
from the original NeuroVista clinical trial [17], which serves as
a baseline for comparison.

Among the deep learning-based methods compared, the Deep
CNN model [12] applies a CNN to the spectrogram of EEG
for seizure prediction. The CNN-LSTM model [8] combines
LSTM and CNN to capture temporal changes in EEG features
for improved prediction accuracy. The study by [2] explores
using raw EEG data for seizure prediction. Notably, these meth-
ods incorporate time-of-day information to enhance prediction
accuracy. Among the non-deep learning approaches, the original
NeuroVista clinical trial [17] presents results utilizing an ensem-
ble machine learning method for seizure prediction. The critical
slowdown model [16] uses critical slowing down indicators and
is considered the SOTA on the NeuroVista dataset.

Additionally, to verify whether CoSP performs above chance
level, we implemented a chance predictor based on a Pois-
son process [39]. A seizure prediction model is considered
to perform above chance if its results are statistically sig-
niﬁcantly better than random chance, with the signiﬁcance
level set to 0.05. This chance predictor operates indepen-
dently of EEG signals, simulating a sensorless approach by
generating preictal classiﬁcations uniformly across test time
intervals.

The comparison results are presented in Table III, which
shows that Critical Slowdown generally achieves the best per-
formance across most patients, while CoSP also demonstrates
strong performance for a majority of patients. To further eval-
uate the models, Wilcoxon signed-rank tests were conducted
to compare the PP scores of CoSP with each baseline model
and the chance predictor in a pairwise manner. These tests were
designed to assess the hypothesis that CoSP outperforms the
comparison methods. A p-value below 0.05 was considered sta-
tistically signiﬁcant. CoSP performed signiﬁcantly better than
chance predictor, with a p-value of 0.001, and also outperformed
Deep CNN, Original Trial, and CNN-LSTM, with p-values well
below 0.05.

It is noted that although all models report SS and TiW,
comparisons may not be entirely fair due to differences in eval-
uation conﬁgurations, such as segment-level vs. seizure-level
analysis and variations in SOP lengths. The LSTM method uses
segment-level predictions, while Deep CNN, Original Trial, and

CNN-LSTM apply seizure-level evaluations with different SOP
lengths. For Critical Slowdown, SS is seizure-level, but TiW’s
evaluation level is unclear.

IV. DISCUSSION

In this section, we present a case study to investigate why and
how CoSP works. Using the results from Patient 13, we ﬁrst
analyze the coherence patterns in the iEEG data of Patient 13.
Then, we explore how these patterns are captured and utilized
by CoSP to make predictions, offering insights into the ability of
CoSP to effectively differentiate between interictal and preictal
states.

Analysis of Coherence Patterns. Coherence is a measure
of synchronization, connection, and communication between
brain regions. A high coherence value between two channels
indicates a strong connection between the brain regions where
the corresponding electrodes are located [37]. CoSP leverages
coherence to predict seizures by analyzing the changes in these
connectivity patterns.

Fig. 5 illustrates the top 15 strongest brain region connec-
tions, based on the average coherence values computed from
the coherence matrices of 1,000 randomly selected interictal
and preictal segments, respectively. These coherence values are
averaged across six primary frequency bands: Delta (0–4 Hz),
Theta (4–8 Hz), Alpha (8–12 Hz), Beta (12–30 Hz), Gamma Low
(30–100 Hz), and Gamma High (100–170 Hz). The connections
are visualized as lines overlaid on an X-ray of the patient’s brain,
showing the locations of the 16 electrodes. The color intensity of
each line represents the magnitude of the coherence value, with
stronger connections (i.e., higher coherence values) indicated by
more intense colors.

Signiﬁcant connectivity changes are observed in the Gamma
High frequency band. In the interictal state, the connectivity
network displays a somewhat clustered pattern around elec-
trodes in the lower part of the X-ray, while maintaining scattered
connections spanning different areas of the brain. In contrast,
during the preictal state, the connectivity becomes highly fo-
cused and directional, with a clear convergence toward Electrode
1 (Channel 1), positioned on the far-right side of the X-ray.
Lower frequency bands, on the other hand, exhibit relatively sta-
ble connectivity patterns between interictal and preictal states,
showing fewer connectivity changes.

LU et al.: LEVERAGING CHANNEL COHERENCE IN LONG-TERM IEEG DATA FOR SEIZURE PREDICTION

5547

Fig. 5. Top 15 strongest brain region connections based on average coherence values computed from 1,000 randomly selected interictal and
preictal segments across six frequency bands: Delta (0–4 Hz), Theta (4–8 Hz), Alpha (8–12 Hz), Beta (12–30 Hz), Gamma Low (30–100 Hz), and
Gamma High (100–170 Hz). Signiﬁcant changes are observed in the Gamma High band, where interictal connectivity is somewhat scattered and
clustered in the lower brain regions, while preictal connectivity becomes strongly focused toward Electrode 1 (Channel 1) on the far-right side of the
X-ray. Lower frequency bands show relatively stable connectivity patterns.

approximates complex models locally by ﬁtting interpretable
inﬂuential
models, enabling the identiﬁcation of the most
features—channels and frequency bands—that contribute to the
decision-making process of CoSP.

We applied LIME to interpret the 1,000 highest probability
predictions and averaged the feature importance values to gen-
erate an importance heatmap, shown in Fig. 6. The heatmap
reveals that Channel 1 (C1) at approximately 120 Hz holds the
highest importance. This observation aligns with the coherence
patterns in Fig. 5, where Channel 1 exhibited the most signiﬁcant
connectivity changes between interictal and preictal states in the
Gamma High frequency band. The consistency between these
ﬁndings conﬁrms that CoSP effectively identiﬁes and prioritizes
the most relevant brain regions and frequencies for accurate
seizure prediction.

Furthermore, this ﬁnding regarding Patient 13 aligns with
prior research on high-frequency activity (HFA) in the Neu-
roVista dataset [3], [28], which reported that the iEEG data
of Patient 13 exhibited signiﬁcantly increased HFA in speciﬁc
electrodes several minutes before seizure onset.

In summary, this case study has demonstrated that CoSP
effectively captures subtle spatial and spectral changes across
interictal and preictal states in pairwise channel coherence ma-
trices, enabling accurate and reliable seizure prediction. Notably,
these changes are complex, diverse, subtle, and highly patient-
speciﬁc [3], [16], [28]. By leveraging deep learning, CoSP
can automatically identify and learn these intricate patterns,
highlighting the importance of utilizing full pairwise channel
coherence information in conjunction with deep learning for
robust and accurate seizure prediction.

V. CONCLUSION

In this study, we have presented CoSP, an innovative seizure
prediction method that integrates full pairwise channel coher-
ence with deep learning to capture subtle spatial and spectral
changes in brain connectivity, thereby improving seizure predic-
tion performance. Experimental evaluation using the long-term
iEEG data of the NeuroVista dataset demonstrated that CoSP
achieves high seizure sensitivity while maintaining reasonable

Fig. 6.
Importance heatmap for CoSP predictions of Patient 13, ex-
plained using LIME. The heatmap visualizes the contributions of individ-
ual channels (C1–C16) and frequencies (0.5–170 Hz) to the predictions
from CoSP. Brighter colors represent higher importance values. The
heatmap reveals that Channel 1 (C1) at approximately 120 Hz holds
the highest importance, aligning with the coherence patterns in Fig. 5.

How CoSP Captures Coherence Patterns for Prediction.
To further investigate why CoSP is effective despite the lack
of signiﬁcant connectivity changes in most frequency bands,
we applied Local Interpretable Model-Agnostic Explanations
(LIME) [36] to analyze how CoSP makes predictions. LIME

5548

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 8, AUGUST 2025

speciﬁcity across 10 patients. Statistical validation conﬁrmed
that CoSP signiﬁcantly outperforms both chance predictor (p =
0.001) and baseline methods (p < 0.05) under similar evaluation
conﬁgurations. Additionally, a detailed case study provided
insights into why and how CoSP works, showcasing its ability
to capture critical changes in brain connectivity before a seizure.
Future research could focus on incorporating temporal coher-
ence patterns to analyze how brain connectivity evolves over
time, potentially enhancing predictive performance. Addition-
ally, integrating multiple biomarkers—such as auto-correlation,
variance, spike rate, and seizure cycles—alongside coherence
could contribute to the development of a more robust and clini-
cally applicable seizure prediction system.

REFERENCES

[1] R. S. Fard, B. Abbaszadeh, and M. C. E. Yagoub, “Application of global
coherence measure to characterize coordinated neural activity during
frontal and temporal lobe epilepsy,” in Proc. 42nd Annu. Int. Conf. IEEE
Eng. Med. Biol. Soc., 2020, pp. 3699–3702.

[2] J. D. Chambers, M. J. Cook, A. N. Burkitt, and D. B. Grayden, “Using
long short-term memory (LSTM) recurrent neural networks to classify
unprocessed eeg for seizure prediction,” Front. Neurosci., vol. 18, 2024,
Art. no. 1472747.

[3] Z. Chen et al., “Spatiotemporal patterns of high-frequency activity (80–170
Hz) in long-term intracranial EEG,” Neurology, vol. 96, no. 7, pp. e1070–
e1081, 2021.

[4] H. Chenand and V. Cherkassky, “Performance metrics for online seizure

prediction,” Neural Netw., vol. 128, pp. 22–32, 2020.

[5] R. Cooper, J. W. Osselton, and J. C. Shaw,” EEG Technology. Berlin,

Germany: Springer, 2014.

[6] EpiMinder, “Epiminder: Pioneering epilepsy management,” 2024, Ac-

cessed: Jun. 20, 2024. [Online]. Available: https://epiminder.com/

[7] C. Li et al., “EEG-based seizure prediction via model uncertainty learning,”
IEEE Trans. Neural Syst. Rehabil. Eng., vol. 31, pp. 180–191, 2022.
[8] D. E. Payne et al., “Epileptic seizure forecasting with long short-term

memory (LSTM) neural networks,” 2023, arXiv-2309.

[9] D. Lee et al., “A Resnet-LSTM hybrid model for predicting epileptic
seizures using a pretrained model with supervised contrastive learning,”
Sci. Rep., vol. 14, no. 1, 2024, Art. no. 1319.

[10] G. Wang et al., “Epileptic seizure detection based on partial directed
coherence analysis,” IEEE J. Biomed. Health Inform., vol. 20, no. 3,
pp. 873–879, May 2016.

[11] I. Ahmad et al., “EEG-based epileptic seizure detection via machine/deep
learning approaches: A systematic review,” Comput Intell Neurosci,
vol. 2022, 2022, Art. no. 6486570.

[12] I. K. Kiral et al., “Epileptic seizure prediction using Big Data and deep
learning: Toward a mobile system,” EBioMedicine, vol. 27, pp. 103–111,
2018.

[13] J. West et al., “Machine learning seizure prediction: One problematic but
accepted practice,” J. Neural Eng., vol. 20, no. 1, 2023, Art. no. 016008.
[14] K. M. Tsiouris et al., “A long short-term memory deep learning network
for the prediction of epileptic seizures using EEG signals,” Comput. Biol.
Med., vol. 99, pp. 24–37, 2018.

[15] K. Rasheed et al., “Machine learning for predicting epileptic seizures using
EEG signals: A review,” IEEE Rev. Biomed. Eng., 14, pp. 139–155, 2020.
[16] M. I. Maturana et al., “Critical slowing down as a biomarker for seizure
susceptibility,” Nature Commun., vol. 11, no. 1, 2020, Art. no. 2172.
[17] M. J. Cook et al., “Prediction of seizure likelihood with a long-term,
implanted seizure advisory system in patients with drug-resistant epilepsy:
A ﬁrst-in-man study,” Lancet Neurol., vol. 12, no. 6, pp. 563–571, 2013.

[18] P. Boonyakitanont et al., “A review of feature extraction and performance
evaluation in epileptic seizure detection using EEG,” Biomed. Signal
Pessing Control, vol. 57, 2020, Art. no. 101702.

[19] P. J. Karoly et al., “The circadian proﬁle of epilepsy improves seizure

forecasting,” Brain, 140, no. 8, pp. 2169–2182, 2017.

[20] R. Shriram et al., “Energy distribution and coherence-based changes
in normal and epileptic electroencephalogram,” in Title of the Book or
Conference Proceedings, Singapore: Springer, 2019, pp. 625–635.
[21] S. M. Usman et al., “Using scalp EEG and intracranial EEG signals for
predicting epileptic seizures: Review of available methodologies,” Seizure,
vol. 71, pp. 258–269, 2024.

[22] U. R. Acharya et al., “Automated EEG analysis of epilepsy: A review,”

Knowl.-Based Syst., vol. 45, pp. 147–165, 2013.

[23] V. L. Towle et al., Electrocorticographic Coherence Patterns of Epileptic

Seizures. Berlin, Germany: Springer, 2003, pp. 69–81.

[24] Y. Li et al., “Spatio-temporal-spectral hierarchical graph convolutional
network with semisupervised active learning for patient-speciﬁc seizure
prediction,” IEEE Trans. Cybern., vol. 52, no. 11, pp. 12189–12204,
Nov. 2022.

[25] Y. Roy et al., “Deep learning-based electroencephalography analysis: A
systematic review,” J. Neural Eng., vol. 16, no. 5, 2019, Art. no. 051001.
[26] Y. Zhao, C. Li, X. Liu, R. Qian, R. Song, and X. Chen, “Patient-speciﬁc
seizure prediction via adder network and supervised contrastive learning,”
IEEE Trans. Neural Syst. Rehabil. Eng., vol. 30, pp. 1536–1547, 2022.

[27] Z. Chen et al., “High-frequency oscillations in epilepsy: What have
we learned and what needs to be addressed,” Neurol., vol. 96, no. 9,
pp. 439–448, 2021.

[28] Z. Chen et al., “Seizure forecasting by high-frequency activity (80–170
Hz) in long-term continuous intracranial Eeg recordings,” Neurol., vol. 99,
no. 4, pp. e364–e375, 2022.

[29] J. A. Hanley and B. J. McNeil, “The meaning and use of the area under a
receiver operating characteristic curve,” Radiol., vol. 143, no. 1, pp. 29–36,
1982.

[30] A. Harris and J. A. Gordon, “Long-range neural synchrony in behavior,”

Annu. Rev. Neurosci., vol. 38, pp. 171–194, 2015.

[31] R. Hartanto, I. Wijayanto, and H. A. Nugroho, “Quantitative analysis of
inter- and intrahemispheric coherence on epileptic electroencephalography
signal,” J. Med. Signals Sensors, vol. 12, no. 2, pp. 145–154.

[32] “International league against epilepsy,” 2019, Accessed: Jun. 20, 2024.

[Online]. Available: www.ilae.org

[33] T. A. Pedley, J. Engel, and J. Aicardi, Epilepsy: A Comprehensive Textbook.

Philadelphia, PA, USA: Lippincott Williams & Wilkins, 2008.

[34] S. Shelagh, “EEG in the diagnosis, classiﬁcation, and management of
patients with epilepsy,” J. Neurol. Neurosurgery Psychiatry, vol. 76,
no. suppl 2, pp. ii2–ii7, 2005.

[35] J. G. Proakis. Digital Signal Processing: Principles, Algorithms, and

Applications. Noida, India: Pearson Education India, 2007.

[36] M. T. Ribeiro, S. Singh, and C. Guestrin, ““Why should I trust you?”
explaining the predictions of any classiﬁer,” in Proc. 22nd ACM SIGKDD
Int. Conf. Knowl. Discov. Data Mining, 2016, pp. 1135–1144.

[37] B. Schelter, M. Winterhalder, J. Timmer, and J. Kurths, “Phase syn-
chronization and coherence analysis: Sensitivity and speciﬁcity,” Int. J.
Bifurcation Chaos, vol. 17, no. 10, pp. 3551–3556, 2007.

[38] J. C. Shaw, “Correlation and coherence analysis of the EEG: A selective
tutorial review,” Int. J. Psychophysiol., vol. 1, no. 3, pp. 255–266, 1984.
[39] D. E. Snyder et al., “The statistics of a practical seizure warning system,”

J. Neural Eng., vol. 5, no. 4, pp. 392–401, 2008.

[40] C. E. Stafstrom and L. Carmant, “Seizures and epilepsy: An overview
for neuroscientists,” Cold Spring Harbor Perspectives Med., vol. 5, no. 6,
2015, Art. no. a022426.

[41] S. Weiss and H. M. Mueller, “The contribution of EEG coherence to the
investigation of language,” Brain Lang., vol. 85, no. 2, pp. 325–343, 2003.
[42] M. Winterhalder, T. Maiwald, H. U. Voss, R. Aschenbrenner-Scheibe, J.
Timmer, and A. Schulze-Bonhage, “The seizure prediction characteristic:
A general framework to assess and compare seizure prediction methods,”
Epilepsy Behav., vol. 4, no. 3, pp. 318–325, 2003.
