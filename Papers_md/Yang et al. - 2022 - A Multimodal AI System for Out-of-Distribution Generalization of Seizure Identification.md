# Yang et al. - 2022 - A Multimodal AI System for Out-of-Distribution Generalization of Seizure Identification

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 26, NO. 7, JULY 2022

3529

A Multimodal AI System for Out-of-Distribution
Generalization of Seizure Identiﬁcation

Yikai Yang , Nhan Duy Truong , Jason K. Eshraghian , Christina Maher, Armin Nikpour,

and Omid Kavehei

, Senior Member, IEEE

and

accurate

automatic

Abstract—Artiﬁcial intelligence (AI) and health sensory
data-fusion hold the potential to automate many laborious
and time-consuming processes in hospitals or ambulatory
settings, e.g. home monitoring and telehealth. One such
unmet challenge is rapid and accurate epileptic seizure
approach
annotation. An
can provide an alternative way to label seizures in
epilepsy or deliver a substitute for inaccurate patient
self-reports. Multimodal sensory fusion is believed
to provide an avenue to improve the performance of
AI systems in seizure identiﬁcation. We propose a
state-of-the-art performing AI system that combines
electroencephalogram (EEG) and electrocardiogram (ECG)
for seizure identiﬁcation, tested on clinical data with early
evidence demonstrating generalization across hospitals.
The model was trained and validated on the publicly
available Temple University Hospital (TUH) dataset. To
evaluate performance in a clinical setting, we conducted
non-patient-speciﬁc pseudo-prospective inference tests on
three out-of-distribution datasets,
including EPILEPSIAE
(30 patients) and the Royal Prince Alfred Hospital (RPAH) in
Sydney, Australia (31 neurologists-shortlisted patients and
30 randomly selected). Our multimodal approach improves
the area under the receiver operating characteristic curve
(AUC-ROC) by an average margin of 6.71% and 14.42% for
deep learning techniques using EEG-only and ECG-only,
respectively. Our model’s state-of-the-art performance
and robustness to out-of-distribution datasets show the
accuracy and efﬁciency necessary to improve epilepsy
diagnoses. To the best of our knowledge, this is the ﬁrst
pseudo-prospective study of an AI system combining

Manuscript received July 4, 2021; revised December 6, 2021 and
February 3, 2022; accepted March 2, 2022. Date of publication March
9, 2022; date of current version July 4, 2022. The work of Omid Kavehei
was supported by The University of Sydney through a SOAR Fellowship
and Microsoft’s support through a Microsoft AI for Accessibility grant.
(Corresponding author: Omid Kavehei.)

Yikai Yang, Nhan Duy Truong, Christina Maher, and Omid Kavehei
are with the School of Biomedical Engineering, and the Australian
Research Council Training Centre for Innovative BioEngineering, Faculty
of Engineering, The University of Sydney, Sydney, NSW 2006, Aus-
tralia (e-mail: yikai.yang@sydney.edu.au; duy.truong@sydney.edu.au;
christina.maher@sydney.edu.au; omid.kavehei@sydney.edu.au).

Armin Nikpour

is with the Comprehensive Epilepsy Services,
Department of Neurology, The Royal Prince Alfred Hospital, Camper-
down, NSW 2050, Australia, and also with the Faculty of Medicine and
Health, The University of Sydney, Sydney, NSW 2006, Australia (e-mail:
armin@sydneyneurology.com.au).

Jason K. Eshraghian is with the Department of Electrical Engineering
and Computer Science, University of Michigan, Ann Arbor 48109 USA,
and also with the School of Medicine, University of Western Australia,
Crawley, WA 6009, Australia (e-mail: jasonesh@umich.edu).

This article has supplementary downloadable material available at

https://dx.doi.org/10.21227/w85b-jr11, provided by the authors.

Digital Object Identiﬁer 10.1109/JBHI.2022.3157877

EEG and ECG modalities for automatic seizure annotation
achieved with fusion of two deep learning networks.

Index

Terms—Affective

computing,

autonomous

systems, expert systems.

I. INTRODUCTION

E PILEPSY affects about 1% of people globally, placing it

as one of the most common severe neurological disorders
worldwide [1]–[5]. Accurate and objective seizure counting
plays an integral role in a wide range of clinical diagnoses and
management decisions for epilepsy. For example, the Interna-
tional League Against Epilepsy (ILAE) deﬁnes epilepsy as a
brain disorder with (1) at least two unprovoked seizures that
are more than 24 hrs apart, (2) one unprovoked seizure and
at least 60% general recurrence risk over the next ten years,
or (3) diagnosis of an epilepsy syndrome [6]. Accurate seizure
counting in the long-term has important implications for driving
the management of epilepsy [6], for instance, being seizure-free
for ten years, while off anti-epileptic drugs (AEDs) for at least
ﬁve, identiﬁes whether epilepsy is considered in remission.

The golden standard of epilepsy diagnosis relies on surface
or scalp electroencephalogram (EEG) readings and accurate
annotation [7]. Nonetheless, epilepsy misdiagnosis or delayed
diagnosis is unfortunately still common and has serious conse-
quences [8], [9]. False positives can lead to the inappropriate
prescription of AEDs that result in mistreated or worsening
symptoms [9], [10]. A strong case can be made for an assis-
tive EEG interpretation given the difﬁculties in reading and
interpreting EEG. While automated EEG interpretation is an
opportunity for seizure identiﬁcation models to act as clinician
support systems [11], [12], alternative data modalities can also
be used to developing more robust models.

More speciﬁcally, epileptic seizures are known to cause
short-term and long-term heart rate disturbances. Ictal tachy-
cardia occurs in over 80% of partial onset-seizures [13], [14],
which may precede electrographic or clinical onset [15], [16].
Compared with EEG, electrocardiograms (ECG) are relatively
more portable and are routinely recorded simultaneously with
EEG [17]. Most successful studies using ECG have focused on
identiﬁcation of seizure onset (early prediction) [18], [19], for
instance, using heart-rate variability (HRV) to predict events in
children with temporal-lobe epilepsy [15], [20]–[23]. In con-
trast, ECG for seizure identiﬁcation has had limited focus as
its performance is not comparable with multi-channel EEG.

2168-2194 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:44 UTC from IEEE Xplore.  Restrictions apply. 

3530

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 26, NO. 7, JULY 2022

Despite the lower performance of lone usage, ECG recordings
can also extract markers of seizure events that EEG may not pick
up [24], [25].

In this paper, we propose a multimodal AI system that demon-
strates the state-of-the-art performance of non-patient-speciﬁc
seizure identiﬁcation, and provides early evidence of generaliza-
tion on out-of-distribution datasets across continents with dif-
ferent data acquisition hardware infrastructure. We achieve this
by designing a multimodal neural network model that accounts
for the independent contributions of EEG and ECG towards the
classiﬁcation of seizure events, in addition to their correlated
contribution. We expect this novel network architecture to be
capable of improving other multimodal tasks as well. The spe-
ciﬁc contributions of this paper are summarized below:

(cid:2)

(cid:2)

(cid:2)

Our proposed non-patient-speciﬁc multimodal deep learn-
ing model using both EEG and ECG data is shown to
achieve state-of-the-art results on the publicly available
Temple University Hospital (TUH) dataset (US). We im-
prove the area under the receiver operating characteristic
curve (AUC-ROC) by a margin of 2.18% over the use
of EEG alone, and by 1.67% when we test it against the
previously best performing multimodal neural network
that combines EEG and ECG signals together.
Early evidence of generalization is shown by pseudo-
prospectively assessing performance on datasets acquired
across hospitals in two different continents without any re-
training. The European EPILEPSIAE dataset (30 patients)
and the Australian RPAH datasets (a total of 61 patients
in two groups) are acquired with different electrophysio-
logical recording infrastructures. The AUC-ROC on the
European dataset is 0.8595, while for Australian datasets,
the averaged AUC-ROC value for the RPA-selected and
RPA-random datasets is 0.8549. The EEG-only approach
and the ECG-only approach result in averaged AUC-ROC
values of 0.8026 and 0.7485 across the three out-of-
distribution datasets, while our proposed model obtains an
AUC-ROC value of 0.8564 which respectively improves
the two comparative methods by 6.71% and 14.42%.
Our proposed model maintains its effectiveness when
either EEG or ECG data modality is missing (i.e., mea-
surement dropout), which conﬁrms the robustness of our
data fusion approach.

The remainder of the paper is organized as follows. The
following section provides a background of related work, and
Section III describes the features of the datasets used in the mod-
els. Section IV introduces the proposed method for automatic
seizure identiﬁcation and the multimodal network. Finally, we
discuss the results and conclude the paper.

II. BACKGROUND

A. Prior Art

Recently, several deep learning techniques have achieved
promising results using EEG for non-patient-speciﬁc seizure
identiﬁcation on the TUH EEG dataset [26]. Beyond clinical
use (in- and out-patients), EEG-based methods are limited as the
recording apparatus is typically not designed for ongoing wear
and would otherwise cause discomfort. Attempts to reduce the

number of EEG channels have yielded limited results. A recent
approach saw the Neureka 2020 Epilepsy Challenge accounting
for the number of channels in their scoring formula. Despite
this, the winner of this challenge relied on a 16-channel EEG
and still only managed to achieve 12.37% sensitivity (with one
false alarm per 24 hours) [27]. 16-channels are inappropriate for
ambient use, and the state-of-the-art result highlights the chal-
lenges associated with developing a high-performance EEG-
based seizure identiﬁcation system using a constrained number
of electrodes. Portability requires complementary biomarkers to
EEG that are already integrated into wearable devices [28]. The
work in [29] implemented several machine learning methods
(HMM, CNN) that were trained on only a small portion of
the TUH dataset using EEG-only, achieving sensitivity ranging
between 30.05% to 39.09%, speciﬁcity from 96.86% to 73.35%.
The low sensitivity may be a bottleneck to practical clinical
deployment due to the large number of unidentiﬁed seizures,
and may be a result of using limited training data. Our proposed
method can achieve a balanced result of 75.40% sensitivity and
76.60% speciﬁcity, which offers a more practical solution in
clinical usage.

On clinical utility, a signiﬁcant challenge in AI-based seizure
identiﬁcation is the need for models that generalize across
patients, recording equipment, and hospitals. Unfortunately, all
prior works reported in a recent review [30] on the application
of deep learning on seizure identiﬁcation are retrospective and
were only benchmarked on test sets sourced identically to the
training set. Such models provide low conﬁdence for deploy-
ment in clinics that differ from where the data was gathered.
This requires rigorous testing and high performance on out-of-
distribution datasets. Despite being a key barrier to deployment,
generalization across hospitals is not a common metric that is
optimized for due to its associated difﬁculties.

As an example of a study that aims to overcome general-
ization, the work in [31] leveraged the abundance of weak
annotations that were analyzed by a mixed group of technicians,
fellows, students, and epileptologists to train a convolutional
neural network (CNN), achieving an AUC-ROC score of 0.78.
When generalizing the network to the Stanford hospital dataset,
the AUC-ROC score dropped to 0.70. Our recent work in [32]
reached an AUC-ROC score of 0.84 using a convolutional long
short-term memory (ConvLSTM) network tested on unseen
patient data. These two studies are among the few publicly
available inter-hospital results of a deep learning algorithm using
EEG-only recordings.

These results show the potential to attain specialist-level diag-
nostic capability that can be used as either a primary diagnostic
tool or a secondary decision support system. But not only is
there insufﬁcient evidence of a practical out-of-distribution per-
formance; these deep learning methods ignore insight provided
by other biomarkers that clinicians have access to. We aim to
address this by including simultaneously recorded ECG signals.

B. Novelty and Signiﬁcance

This study aims to improve the seizure identiﬁcation rate in
adults by combining simultaneously acquired EEG and ECG

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:44 UTC from IEEE Xplore.  Restrictions apply. 

YANG et al.: MULTIMODAL AI SYSTEM FOR OUT-OF-DISTRIBUTION GENERALIZATION OF SEIZURE IDENTIFICATION

3531

TABLE I
DATASET COMPARISON

Details of all three datasets are in the Supplementary Information Table I, II, III, IV. All three datasets’ EEG arrangement of electrodes we used
for testing followed the International 10/20 system setting, which have at least 19 electrodes and the names are described as following: “Fp1,”
“Fp2,” “F7,” “F3,” “Fz,” “F4,” “F8,” “T3,” “C3,” “Cz,” “C4,” “T4,” “T5,” “P3,” “Pz,” “P4,” “T6,” “O1,” “O2”; while ECG only have one electrode.
EPILPSIAE dataset does not contain session number information, and in the RPAH dataset, each ﬁle represents one session. Besides, we resample
the signal to the same frequency (250 Hz).

recordings in a fused deep learning system. Our study demon-
strates that using both recordings in an appropriately structured
multimodal neural network can provide a more robust diag-
nosis than either measurement alone and also improves upon
previously reported state-of-the-art multimodal neural networks
applied to this task [33]. To the best of our knowledge, only a
set of limited works concatenates EEG and ECG recordings for
seizure identiﬁcation, one, in particular, achieving an AUC-ROC
improvement of 0.01 and 0.11, when compared with EEG-only
and ECG-only models, respectively [34]–[36]. However, naively
concatenating different features in a machine learning model
poses several challenges [37], which show even lower perfor-
mance compared with the EEG-only. The use of more features
opens up susceptibility to overﬁtting; combining heterogeneous
sources of data increases the difﬁculty of feature extraction;
the inability to isolate the noise of correlated distributions can
increase the bias of the network. These issues can severely
harm the out-of-distribution performance on unseen patients and
datasets.

III. DATASET

Three datasets are used in this work: the Temple University
Hospital (TUH) seizure corpus v1.5.1 [26], EPILEPSIAE [38],
and two sets from the Royal Prince Alfred Hospital (RPAH) [32].
All datasets contain surface EEG data from adult individuals liv-
ing with epilepsy. A comparison of these datasets is summarized
in Table I, and the detailed information among these datasets is
shown in the Supplementary Information Table I, II, III, IV.
Only the TUH dataset is used to train and validate our network.
Pseudo-prospective evaluations are performed on the EPILEP-
SIAE and RPAH datasets (without any re-training). The TUH
(US), EPILEPSIAE (Germany), and RPAH (Australia) datasets
are from three continents recorded with different data acquisition
infrastructures.

into two test sets: one set includes 31 patients with different
seizure foci and are shortlisted (selected) by neurologists from
a long list of patients. The aim was to consider seizure type
and semiology in the expert selection of patients. The second
set includes 30 randomly selected patients from the same pool
without any prior information. The gold standard is labeled
by a group of board-certiﬁed neurologists and EEG specialists
combined with multiple sources, including professional EEG
reading, clinical reports, and video information.

A. TUH Dataset

The world’s largest open database, the Temple University
Hospital (TUH) seizure corpus v1.5.1 [26], was used for training
and validation of our deep learning model. The TUH dataset
consists of simultaneously recorded EEG and ECG data. Pa-
tients with missing ECG recordings were omitted, leaving 1,095
sessions with 540 patients (174 participants with seizures) in
the training set. The training set was randomly split (80/20) for
training and validation. After training and parameter tuning, the
model is then ﬁxed for all future evaluation, hence a pseudo-
prospective analysis can be undertaken.

For testing on the TUH dataset, we used 228 sessions with 46
patients (36 patients with seizures). In the absence of a publicly
released labeled test set, we treat the TUH development dataset
as the unseen test set to reduce bias in our assessment. This is
summarized in the Supplementary Information Table I. To assess
clinical utility, strictly no further training, tuning, or model
selection took place beyond what we were satisﬁed with on the
TUH train and development sets. This strictly inference-only
approach on the out-of-distribution test sets is adopted to emulate
a prospective study.

B. EPILEPSIAE Dataset

For a rigorous evaluation on challenging data, such as a variety
of seizure types, and various foci on the brain network inputs to
the autonomic nervous system [39], the RPAH dataset is divided

EPILEPSIAE is the largest epilepsy EEG database in Europe,
containing EEG and ECG data from 275 patients [38]. In this
work, we analyze scalp-EEG and ECG with 19 electrodes of 30

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:44 UTC from IEEE Xplore.  Restrictions apply. 

3532

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 26, NO. 7, JULY 2022

TABLE II
INFERENCE (AUC) RESULTS COMPARISON

EmbraceNet (MC): Missing ECG information to the EmbraceNet fused network, Proposed (MC): Missing ECG information to the proposed fused
network, EmbraceNet (ME): Missing EEG information to the EmbraceNet fused network, Proposed (ME): Missing EEG information to the Proposed
fused network. Numbers in brackets indicate the relative difference when compared with AUC value of the corresponding baseline model (ConvLSTM
or ResConv).

patients with 238 seizures and 4,604 recording hours in total.
The sampling rate of the EEG is 256 Hz. (see Supplementary
Information Table II).

knowledge that 10-15 s is a sufﬁcient window of time for human
experts to extract relevant information. Thus, we chose a 12-
second window length.

C. RPAH Datasets

We have extracted 192 adult in-patient EEG monitoring data
from 2011 to 2019 at RPA Hospital in Sydney, and long-listed
111 patients with seizures recorded. In this study, RPAH neu-
rologists assist in shortlisting 31 epilepsy adults with different
seizure foci. Speciﬁcally, neurologists are asked to select pa-
tients with the six most common seizure types, namely general-
ized, frontal, frontotemporal, temporal, parietal, and unspeciﬁed
focal epilepsy (see Supplementary Information Table III). The
total number of seizures and the mean seizure duration are 238
and 97.2 seconds, respectively. To conﬁrm the reliability of our
fused network, a randomized test is also performed where 30
patients from 111 adult patients with seizures are randomly
selected without any prior information. (see Supplementary
Information Table IV) Note that the ratio of the total seizure
duration (time) over the total background data for RPAH data
is signiﬁcantly higher than the curated TUH dataset; hence
it creates a highly realistic inference-only evaluation for false
positives. This is mainly due to more network exposure to noise
and artifacts.

IV. METHODS

Our study on RPAH clinical data is approved by the local

Research Ethics Committee (see Ethics Declaration section).

A. Pre-Processing

The EEG and ECG signal segment lengths are chosen to be
identical, such that one modality does not have a higher impact
than the other [31]. Furthermore, clinicians typically read EEG
signals in 10–15 s long pages, which is sufﬁcient for expert
EEG-readers to extract relevant features from the pre-seizure
phase. To better compare with [31], and as we have domain

1) EEG: Prior to being passed into the neural network, eye
artifacts are removed, and frequency information is extracted
by using independent component analysis (ICA) [40] and short-
time Fourier Transform (STFT).

The EEG signals are ﬁrst split into 12-second segments, and
then the ICA algorithm is applied to decompose the signal
into several statistically independent components. Blind source
separation (BSS) [41] is used in the ICA [40] algorithm to obtain
several statistically independent topographic maps. Eq 1 shows
the working principle of BSS, where T ∈ RIt×Ie is the multi-
channel EEG signal, It represents the number of samples over
time, and Ie is the number of electrodes. After decomposition,
M ∈ RIt×R contains temporal information of the decomposed
signal, A ∈ RIe×R contains the topographic weight map, and
R is the source number estimation.

T ≈ MA(cid:4)

(1)

Eye movement

information is recorded on the electro-
oculography (EOG) channel, which is physically close to the
EEG channels labeled ‘FP1’ and ‘FP2’. To remove this artifact,
a fully automated approach based on Pearson correlation is
used [42]. Independent signal information with a strong cor-
relation with channels ‘FP1’ and ‘FP2’ above a given thresh-
old (based on adaptive z-scoring) are removed. STFT is then
applied to the clean EEG signals with a 250 sample (or 1 s)
window length and 50% overlapping. The direct-current (DC)
components refer to the 0-Hz component in the EEG signal.
The DC component is susceptible to changes in recording envi-
ronments (e.g., change in power line current, slight movements
of electrodes). The mean value of the post-processed electrode
is 0, but it varies across each recording. This DC part is re-
moved as it is known to have no relation to seizure occurrences.
The pre-processed dimensionality of the input data becomes
(19 × 23 × 125), where 19 is the number of electrodes, 23 is

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:44 UTC from IEEE Xplore.  Restrictions apply. 

YANG et al.: MULTIMODAL AI SYSTEM FOR OUT-OF-DISTRIBUTION GENERALIZATION OF SEIZURE IDENTIFICATION

3533

Fig. 1. Proposed multimodal network.

the time sample, and 125 is the range of frequencies. Artifact
removal is performed using the MNE Python package [43].

2) ECG: Heart rate variability (HRV) [44] is one of the most
common features extracted from ECG for seizure identiﬁcation.
HRV typically requires around (50 or 100 R-R intervals) 60
seconds of raw ECG to have a reliable estimation [45]. This
may eliminate the time information within those 60 seconds,
which is critical for our ResConv. Therefore, we used deep
learning to extract features from STFT of raw ECG signals by
itself. As the ECG will ultimately be processed by a CNN, we
expect the network can inherently extract relevant information
without manual feature engineering. Although raw ECG signals
can be directly fed into the neural network, the lack of explicit
frequency information makes it difﬁcult for the network to
extract essential features. As with the EEG recordings, we apply
an STFT to the ECG to translate 12 s segments of raw ECG
signals into spectra as input to the neural network. To address
differences in sample rates of recording equipment, all ECG
signals are re-sampled to 250 Hz. Therefore, a 12 s ECG signal
contains a total of 3,000 samples. We used a window length of
250 samples (or 1 s) with 50% overlapping when applying the
STFT to transform the data dimensions to (23 × 1 × 126). The
DC component in the spectrogram is removed, resulting in the
dimensionality of (23 × 1 × 125).

B. Deep Learning Network

The overall model structure can be separated into three parts.
A ConvLSTM network dedicated to the EEG data, a residual
CNN for the ECG data, and a fused network that takes the outputs
of the individual networks to model the cross-modal represen-
tation of the EEG and ECG signals. All three networks are then
connected (using both sequential and residual connections) to a
terminal network consisting of several dense layers.

1) EEG-ConvLSTM Network: The deep learning network
used for training the EEG signal is adopted from our previous
work [32]. It is well recognized that the frequency content
of EEG signals is crucial for identifying seizures [46], [47].

Different types of seizures may have different brain effects,
but frequency evolution [48] is one of the common biomarkers
during seizure onset, and the Short-Time Fourier Transform
(STFT) is useful for frequency-based feature extraction. Thus,
we use the STFT for seizure pre-processing, and use ConvLSTM
as convolutions are effective at capturing local temporal depen-
dencies typically on the order of several time-steps (via shared
weights), while LSTMs are effective at long-range temporal
dependencies (typically on the order of 100 s of time-steps).
A ConvLSTM combines the best of both worlds, where the
temporal data is the frequency evolution of the spectrogram in
our case.

Three deep convolutional long short term memory (Con-
vLSTM) blocks [49] are combined with three fully-connected
layers. The detailed structure is shown in Supplementary Infor-
mation Fig. 1. The ﬁrst ConvLSTM layer uses 16 (n × 2 × 3)
kernels with (1 × 2) stride, where n represents the number of
channels. The next two ConvLSTM blocks both use (1 × 2)
stride and (1 × 3) kernel sizes. 32 ﬁlters and 64 for the ConvL-
STM block 2 and 3, respectively. The three ConvLSTM blocks
are two fully connected layers with sigmoid activation and output
sizes of 256 and 2, respectively.

2) ECG-ResConv Network: Recently, a deep network based
on convolutional neural network (CNN)-residual [50] blocks
achieved excellent performance on cardiovascular disease clas-
siﬁcation problems using 12-lead ECG channels [51]. In ECG
recordings, localized features (i.e., changes that occur within
short ranges of times) seem to carry more signiﬁcance than
long-range disturbances. Therefore, we use convolutions and
avoid LSTMs to avoid learning around long-range dependen-
cies that do not exist in the data. However, LSTMs exist to
alleviate the vanishing gradient problem in deep networks. The
residual connections compensate for this in the ResConv archi-
tecture. Another evidence is that a similar architecture has been
successfully employed to identify abnormalities in single-lead
ECG signals [52]. Thus, we bring this idea to the epileptic
seizure identiﬁcation, as this network is proved to be the best
in identifying of ECG abnormalities. Our model ﬁne-tunes this

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:44 UTC from IEEE Xplore.  Restrictions apply. 

3534

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 26, NO. 7, JULY 2022

Fig. 2. Pseudo-prospective seizure identiﬁcation performance comparison. ConvLSTM: EEG-only with ConvLSTM network, ResConv: ECG-only
with ResConv network, EmbraceNet: EmbraceNet architecture trained on combined EEG and ECG data, Proposed: our approach to combined
EEG and ECG data, EmbraceNet (MC): EmbraceNet architecture trained on EEG and ECG data, but missing ECG during inference, EmbraceNet
(ME): as above but missing EEG during inference, Proposed (MC): Our proposed approach trained on EEG and ECG data, but missing ECG data
during inference, Proposed (ME): As above, but missing EEG data during inference.

ResConv (CNN-residual) network to efﬁciently and accurately
use ECG signals for seizure identiﬁcation. As shown in the
Supplementary Information Fig. 2, the input was ﬁrst fed into a
batch normalization layer, ensuring the input data has zero mean
and unit variance to reduce the internal covariate shift [53]. The
ReLU activation function was used inside the network [54], and
the kernel size for all blocks was (3 × 1). The residual block was
designed with a skip connection combined with two branches,
and the down-sampling value in the max-pooling layer was
selected to normalize the output sample sizes. The output feature
size was halved block-by-block, from 64 to 8, while the number
of ﬁlters was doubled block-by- block, from 32 to 256. The four
residual blocks were ﬂattened, followed by a fully connected
layer with sigmoid activation and output dimension of 2. Both
the ﬂattened layer and fully connected layer had a 0.5 dropout
rate.

To avoid overﬁtting to the training data, dropout (p = 0.5
in ﬂattened and fully-connected layers) and early-stopping (pa-
tience of 20 epochs on the validation set) were applied to
terminate the training process. In general, the hyperparameters
of the architecture, dropout rate, and the overﬁtting patience
parameters were chosen via a combination of grid search and
manual tuning. We used a learning rate of 5e-4 and batch size
of 32 with the Adam optimizer during training. While during
the ﬁne-tuning of the terminal network, the patience for early
stopping is set to 5 as this step only updates the terminal layers
and validation accuracy/loss did not change much after the ﬁrst
epoch. We implemented our model in Python with Keras 2.0
with a Tensorﬂow 1.4.0 backend.

C. Proposed Multimodal Network

1) Additive Representation of Multimodal Data Distributions:
The proposed network is derived from the calculation of additive
signal power from a pair of correlated random variables. Multi-
modal data obtained from the same target is typically expected
to be correlated. As an example, the average power of two
superimposed waveforms containing noise content is calculated
using the following equation:

Pav = Pav1 + Pav2 + lim

ΔT →∞

(cid:2) +T /2

−T /2

1

T

2x1(t)x2(t)dt

(2)

where Pav1 and Pav2 denote the average power of time-varying
input signals x1(t) and x2(t) respectively. The third term is
the correlation between the two input signals. The EmbraceNet
architecture from [33] models the cross-modal correlation from
the integral term, lessening the dependence on the independent
contributions of the input signals present in the ﬁrst two terms
of (2).

To address the lack of contribution from the independent input
data distributions, the EmbraceNet architecture is stacked with
residual connections from the EEG-ConvLSTM network and
the ECG-ResConv network (see Fig. 1). This provides a more
faithful representation of correlated signals, and also addresses
the vanishing gradient problem in deep networks by introducing
skipped pathways for gradient backpropagation.

2) Network Structure: The fused network takes ﬂattened
vectors x(k) of the independent network models as inputs. In
our case, the ﬂattened layers of the EEG and ECG network are

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:44 UTC from IEEE Xplore.  Restrictions apply. 

YANG et al.: MULTIMODAL AI SYSTEM FOR OUT-OF-DISTRIBUTION GENERALIZATION OF SEIZURE IDENTIFICATION

3535

denoted as x(1) and x(2), respectively. The i-th input for both
networks are x

, x

.

(2)
i

(1)
i

a) Cross-modal correlation using EmbraceNet: The
cross-modal network that ﬁnds a joint representation of the
two data modalities originates from the state-of-the-art network
“EmbraceNet” [33]. The outputs of the independent EEG and
ECG networks are ﬁrst connected to a pair of dense layers
to standardize the input feature vector (c = 256 in our tests),
reﬂected in the equation below:
i = w(k)

i + b

· x(k)

(k)
i

(3)

(k)

z

i

where k = 1, indicates the EEG network output, and k = 2 is
the ECG network modality output. w(k)
are the weights
and biases, respectively.

(k)
i

, b

i

A nonlinear activation function fa (e.g. ReLU) is applied to
(k)
i

, obtaining:

z

)

d

(k)
i

(k)
i = fa(z
Note that d(k) is of dimension c.
Rather than using summation to fuse the vectors, the Em-
braceNet model employs an elaborate fusion technique based
on a multinomial sampling process:

(4)

(1)
ri = [r
i

(2)
, r
i

](cid:2) which is drawn from a multinomial distri-

bution.

(cid:3)

ri ∼ Multinomial(1, p)

(5)
where p = [p1, p2](cid:2) and
j pj = 1, indicating that only one
element of the vector ri is equal to 1, while the rest are 0. The
Hadamard product between rk and dk is taken to obtain the
output d(cid:8)(k) in EmbraceNet.

d(cid:8)(k) = r(k) ◦ d(k)

(6)

Finally, the output vector is the sum across all elements of

d(cid:8)(k).

ei =

(cid:4)

k

(cid:8)(k)
i

d

(7)

b) Residual connections: To include the independent
contributions of the input data distributions, residual connections
are applied to the outputs of the EEG-ConvLSTM and ECG-
ResConv networks (i.e., the inputs to EmbraceNet), xk.

(cid:8)k = gk

x

c/t(cid:4)

i=0

max(xk

i , . . .xk

i+t−1)

(8)

where c is the dimension of xk, and t is the 1D max pooling
stride. The function of gk represents the max pooling. In our
experiments, t is chosen to be a power of 2 which sets the
dimensions of x(cid:8)k close to that of e. This is desirable as by
setting the dimensions of the latent representations of each
data modality to be close to the cross-modal representation,
the network capacity for each distribution is normalized before
being combined. The practical effect is that the complexity of
relationships that are learnable for each data modality are made
to be uniform.

Finally, the output of the fused network e(cid:8) is the combination
of both residual networks (Fig. 1, labeled part I: x(cid:8)1 and part II:
x(cid:8)2), with the EmbraceNet output e. In our case, the terminal net-
work is three dense layers of sizes 256, 128, and 2, sequentially.
The output represents the probability that a seizure is occurring.

D. Performance Metrics

1) AUC-ROC Score: To evaluate the performance of the
proposed method for the seizure identiﬁcation task, we used the
area under the Receiver Operating Characteristic curve (AUC-
ROC). The AUC-ROC measures the area under the recall vs. the
false-positive rate (FPR) plots. Formal deﬁnitions of the recall
and the FPR are provided below:

Recall = TP

TP+FN

FPR = FP

TN+FP

(9)

(10)

where TP, TN, FP, and FN represent true positives (correct
seizure identiﬁcation), true negatives (correct non-seizure iden-
tiﬁcation), false positives (incorrect seizure identiﬁcation), and
false negatives (incorrect non-seizure identiﬁcation).

2) The Wilcoxon Signed-Rank Test: To evaluate the perfor-
mance of our model, the Wilcoxon signed-rank statistic [55]
is used. The obtained p-value provides a metric indicating the
signiﬁcance of performance improvement.

V. RESULTS

A. Test Cases

The following tests are applied to the TUH test set, with
a pseudo-prospective study on the EPILEPSIAE and RPAH
(selected and randomized) groups.

1) Multimodal Approach: To explore the effectiveness of our
proposed network, we compare the following options, using the
networks shown in Fig. 1, on EEG and ECG recordings:

ConvLSTM (EEG only)
ResConv (ECG only)
EmbraceNet (EN), prior state-of-the-art for multimodal
data [33] (EEG and ECG)
Proposed (ECG and EEG)

(cid:2)
(cid:2)
(cid:2)

(cid:2)

2) Missing Modalities: The above networks are then tested
for the cases where either EEG or ECG recordings are un-
available, which may occur due to poor electrode contact or
unexpected signal dropout during recording.

a) Missing ECG (MC): The ECG channel is treated as
missing and is set to zero. The EEG channel is kept the same,
and the same network models described above are used for
testing (without retraining). Our proposed approach is compared
to EmbraceNet, and the single-modal ConvLSTM EEG-only
network.

b) Missing EEG (ME): All EEG inputs are set to zero
while ECG recordings are used as per normal. The same compar-
ison as the missing ECG case is made, but with the single-modal
ResConv ECG-only network instead.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:44 UTC from IEEE Xplore.  Restrictions apply. 

3536

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 26, NO. 7, JULY 2022

B. Performance

VI. DISCUSSION

The distribution of AUC-ROC for the pseudo-prospective
out-of-distribution analyses are shown in Fig. 2, tabulated in
Table II, and the ROCs under all test scenarios are provided in
Supplementary Information Fig. 3.

The AUC-ROC for each individual patient across the EPILEP-
SIAE, RPA-selected and randomized groups is shown in Fig. 2.
The ﬁrst column depicts the results for the multimodal approach.
Combining EEG and ECG data using a fused network (for
both EmbraceNet and our proposed method) improves perfor-
mance across all three out-of-distribution datasets. Our proposed
method consistently outperforms EmbraceNet across the three
experiments. From Table II, the absolute AUC improvement
of our proposed method when compared with EmbraceNet is
0.0139 for the TUH test set, 0.0078 for the ELIEPSIAE set,
0.0181 for the selected RPA group, and 0.0191 for the random-
ized RPA group.

The absolute margin of the AUC-ROC from our approach
improves upon the prior state-of-the-art fusion method [33] on
the out-of-distribution datasets by 6.71% for EEG-only, 14.42%
for ECG-only, and 1.76% for EmbraceNet’s multimodal ap-
proach. The AUC-ROC curves across each dataset are shown in
Supplementary Information Fig. 3. The p-value derived from the
Wilcoxon signed-rank test for our proposed model (EEG+ECG)
when compared with EEG only, ECG only and EmbraceNet
(EEG+ECG) is (p < 0.0001, p < 0.0001, p = 0.0418) in the
EPILEPSIAE dataset, (p < 0.0001, p = 0.0037, p = 0.0013)
for the selected RPA group, and (p = 0.0001, p = 0.0006, p =
0.0003) RPA-random group. This demonstrates the statistically
signiﬁcant performance of our model for a speciﬁed threshold
of 0.01.

For the test case of the missing ECG modality (MC), we
repeat the above tests when the two fused networks (our pro-
posed and EmbraceNet) are missing ECG information. Com-
pared with EEG-only performance using the ConvLSTM net-
work,
the performance of EmbraceNet dropped by 8.86%
(TUH), 6.51% (EPILEPSIAE), 5.70% (RPA-selected), and
8.99% (RPA-random). In contrast, our proposed method in-
creases performance of the ConvLSTM EEG-only network by
0.33% (TUH), 1.93% (EPILEPSIAE), 2.66% (RPA-selected),
and 0.44% (RPA-random). The p-value under this case for our
proposed approach against EmbraceNet is (p < 0.0001, p =
0.0001, p < 0.0001) EPILEPSIAE, RPA-selected and -random
datasets, respectively.

The above process was repeated for the missing EEG modal-
ity case (ME). When compared with the ECG-only ResConv
network, the performance of EmbraceNet with missing EEG in-
formation dropped by 3.12% (TUH), 2.27% (RPA-selected), and
4.84% (RPA-random) and improved by 2.88% (EPILEPSIAE).
The proposed method dropped by 1.99% (TUH), 1.45% (RPA-
selected), and 2.87% (RPA-random), and improved by 0.33%
(EPILEPSIAE). The p-values when compared to EmbraceNet
(ME) are p = 0.2644 (RPA-selected), and p = 0.3897 (RPA-
random) respectively. Other than the EPILEPSIAE dataset, the
decrease in our model’s performance is less than the decrease
in EmbraceNet’s performance, demonstrating it is robust when
the EEG modality is missing.

For

the multimodal case, described in Section V-A1,
our proposed model outperforms the AUC-ROC for seizure
identiﬁcation compared to the EEG-only network, ECG-only
network, and the EmbraceNet fused approach across all datasets.
The work in [31] uses a 12-second windows convolutional
neural network (CNN), achieving an AUC-ROC score of 0.78
on the TUH dataset v1.4.0 (detail comparison with the v1.5.1 and
v1.4.0 are shown in the Supplementary Information Table I), and
when generalizing the network to the Stanford hospital dataset,
the AUC-ROC score dropped to 0.70. Our proposed methods
show better results with 0.8450 on the TUH dataset, and an
average of 0.8564 using the three out-of-distribution datasets.

Our approach tested on the non-prospective TUH test set im-
proved the AUC-ROC attained using EmbraceNet from 0.8311
to 0.8450. This improvement of 1.67% is the smallest margin of
all cases. All pseudo-prospective trials showed a larger improve-
ment other than for EPILEPSIAE (0.0078), thus demonstrating
our method’s capacity for generalization and potential for use in
a clinical setting. The ECG-only network was the only approach
to improve upon the TUH test set baseline on pseudo-prospective
samples, but came with the cost of large performance variation
and signiﬁcantly lower absolute AUC-ROC. We expect this
variation arises from individuals with different seizure origins
which variably inﬂuence the autonomic nervous system [56].
The table shows that performance on the RPA-random set is
better than the RPA-selected by 9.15% when using the proposed
method to test. Based on Supplementary Information Table IV,
we ﬁnd that generalized patients and patients with seizure foci
on the frontotemporal and temporal lobes typically show higher
performance than patients with seizure foci on other locations.
There are 20 patients under these groups in the RPAH selected
dataset and 23 patients in the RPAH random dataset. Further-
more, seizure identiﬁcation performance varies from patient
to patient, and the mechanism is rather complicated. In our
test, based on our observation, we believe it may be caused by
different proportions of the seizure foci.

For the ECG-missing case, described in Section V-A2a, we
evaluated the AUC performance when all ECG data was omitted.
Our results show that the proposed method is still able to
marginally improve the performance over the EEG-only network
(average improvement of 1.30%), whereas the EmbraceNet
approach has a signiﬁcant drop in performance (average drop
of 7.51%). This reﬂects that our proposed network has high
robustness for missing (potentially corrupted) ECG recordings.
Finally, we analyze the case for missing EEG information,
discussed in Section V-A2b. Our proposed method experienced
a slight drop in performance when compared to the dedicated
ECG-only ResConv model on the TUH and RPAH groups,
and an increase on the EPILEPSIAE dataset by 0.33%. The
performance of EmbraceNet dropped more (in the range of
2.27% and 4.84%), other than for the EPILEPSIAE dataset. Our
network is much more stable than EmbraceNet, although this
test makes it evident that our network relies more on EEG data
to surpass the other networks.

We note that EmbraceNet (ME) and Proposed (ME) are almost
worse than using ResConv (ECG). However, the important note

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:44 UTC from IEEE Xplore.  Restrictions apply. 

YANG et al.: MULTIMODAL AI SYSTEM FOR OUT-OF-DISTRIBUTION GENERALIZATION OF SEIZURE IDENTIFICATION

3537

is that the proposed method is robust to missing EEG signals
(ME). EmbraceNet and our proposed method still perform com-
parably to ResConv, trained speciﬁcally for ECG. The fusion
layer, initially proposed by EmraceNet and then improved by
our method, which ensures the model does not rely wholly on an
individual modality. In other words, the fusion layer strengthens
the feature learning using both EEG and ECG signals. The
underlying mechanism for fusing ECG and EEG features using
the proposed methods is explained following: The EEG-only
embedding of data is designed for patients whose seizures can
only be identiﬁed by the EEG, which is especially important
for patients whose epileptic seizures occur without obvious
convulsive behavioral manifestations [57].On the other hand,
not all seizures can be identiﬁed by the EEG, but some patients
may have tachycardia [24], or in other words, life-threatening
arrhythmias are ampliﬁed during a seizure [57], [58]. Finally,
the joint embedding of EEG and ECG enables our model to
account for patients who exhibit both biomarkers in the EEG
and the tachycardia from ECG during the seizures. In practice,
the two are rarely mutually exclusive events, and there may
be subtle biomarkers in either or both data modalities. The
joint embedding modelled by the EmbraceNet architecture aims
to model the joint distribution of EEG and ECG signals that
represent the onset of a seizure.

Compared with EEG-only and ECG-only methods, the pro-
posed method can identify more seizures while maintaining the
same false-positive rate veriﬁed on data that includes a very large
amount of background (non-seizure) data. AUC score is a good
metric for comparing the general method, while in real seizure
identiﬁcation applications, a certain threshold will be selected
to achieve a balanced sensitivity and speciﬁcity. For example, in
the TUH test set, one of the balance points we apply for clinical
usage for the proposed method results in 75.40% sensitivity and
76.60% speciﬁcity. In comparison with the EEG-only method,
the sensitivity drops to 73.06% to achieve the same speciﬁcity,
and for the ECG-only method, the sensitivity can only achieve
around 39.61%. The total number of seizures in the TUH test
set is 650, which means that while maintaining the same false-
positive rate, using the proposed fusion methods can identify 15
and 232 more seizures than EEG-only and ECG-only methods in
the real-world application. For a long-duration recording clinical
dataset like the RPAH dataset, the proposed method will be more
helpful, for example, in the RPAH-select dataset, the ratio of
background duration over seizure duration will be around 389:1,
which means that neurologists need to review 389 seconds of
EEG data on average to ﬁnd only 1 s of seizure information.
Finding 10 more seizures would require experts to review 10.5
hours of background EEG information without assistance from
the AI. It should be noted that the average seizure duration is 97.2
seconds in the RPAH-select dataset. Due to the small number of
seizures relative to the background data, even small performance
improvements add up to large savings in terms of time and effort
in seizure identiﬁcation and annotation.

Our results illustrate the proposed model and method are
generalizable across different datasets acquired with different
equipment. We have also shown the robustness of our network in
terms of performance and susceptibility to missing data modal-
ities when compared to the state-of-the-art in data fusion [33].

Our experiments conﬁrm that multimodal data can achieve better
performance than either EEG or ECG alone. We envision a
potential use of our system in decision support systems in the
context of providing a conﬁrmatory secondary reading. In such
a case, our proposed system would act as the risk mitigation
strategy in supporting clinical readings.

VII. CONCLUSION

Despite the extensive studies over the past four decades of
using EEG in seizure identiﬁcation, the use of ECG is quite
limited and never previously reported in a multimodal deep
learning model. Our proposed model and fused modality ap-
proach show promise in using EEG and ECG signals together,
and were demonstrated to generalize to pseudo-prospective
studies. Our analysis shows that a seizure identiﬁcation system
can sustain state-of-the-art performance on out-of-distribution
samples, which is a critical feature for clinical translation.

ACKNOWLEDGMENT

The author Yikai Yang would like to thank the Research
Training Program (RTP) support provided by the Australia
Government.

ETHICS DECLARATIONS

Ethics approval number X19-0323-2019/STE16040 on Vali-
dating epileptic seizure detection, prediction and classiﬁcation
algorithms approved on 19 September 2019 by the NSW Local
Health District (LHD) for implementation in the Comprehensive
Epilepsy Services, Department of Neurology, The Royal Prince
Alfred Hospital (RPAH).

DATA AVAILABILITY

The Temple University Hospital dataset

is publicly
available at https://www.isip.piconepress.com/projects/tuh_
eeg/html/downloads.shtml. The training on the publicly avail-
level
able TUH dataset provides readers with sufﬁcient
of ability to independently conﬁrm some of
the re-
sults reported. The EPILEPSIAE dataset
is available at
cost via http://www.epilepsiae.eu/project_outputs/european_
database_on_epilepsy. The Royal Prince Alfred Hospital was
used under ethics Review Board approval for our use only.

CODE AVAILABILITY

The code used to generate all results in this manuscript can

be made available upon request.

REFERENCES

[1] P. N. Banerjee, D. Filippi, and W. A. Hauser, “The descriptive epidemiol-
ogy of epilepsy-A review,” Epilepsy Res., vol. 85, no. 1, pp. 31–45, 2009.
[2] E. Foster et al., “The costs of epilepsy in Australia: A productivity-based

analysis,” Neurol., vol. 95, no. 24, pp. e3221–e3231, 2020.

[3] E. Beghi, “Addressing the burden of epilepsy: Many unmet needs,” Phar-

macological Res., vol. 107, pp. 79–84, 2016.

[4] A. Jacoby, D. Snape, and G. A. Baker, “Epilepsy and social identity: The
stigma of a chronic neurological disorder,” Lancet Neurol., vol. 4, no. 3,
pp. 171–178, 2005.

[5] R. S. Fisher et al., “The impact of epilepsy from the patient’s perspective
i. descriptions and subjective perceptions,” Epilepsy Res., vol. 41, no. 1,
pp. 39–51, 2000.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:44 UTC from IEEE Xplore.  Restrictions apply. 

3538

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 26, NO. 7, JULY 2022

[6] R. S. Fisher et al., “ILAE ofﬁcial report: A practical clinical deﬁnition of

epilepsy,” Epilepsia, vol. 55, no. 4, pp. 475–482, 2014.

[7] S. R. Benbadis, S. Beniczky, E. Bertram, S. MacIver, and S. L. Moshé,
“The role of EEG in patients with suspected epilepsy,” Epileptic Disord.,
vol. 22, no. 2, pp. 143–155, 2020.

[8] M. M. Oto, “The misdiagnosis of epilepsy: Appraising risks and managing

uncertainty,” Seizure, vol. 44, pp. 143–146, 2017.

[9] S. R. Benbadis, “The tragedy of over-read EEGs and wrong diagnoses
of epilepsy,” Expert Rev. Neurotherapeutics, vol. 10, no. 3, pp. 343–346,
2010.

[10] E. Lee-Lane et al., “Epilepsy, antiepileptic drugs, and the risk of major

cardiovascular events,” Epilepsia, vol. 62, no. 7, pp. 1604–1616, 2021.

[11] N. D. Truong et al., “Convolutional neural networks for seizure predic-
tion using intracranial and scalp electroencephalogram,” Neural Netw.,
vol. 105, pp. 104–111, 2018.

[12] N. D. Truong et al., “Seizure susceptibility prediction in uncontrolled

epilepsy,” Front. Neurol., vol. 12, 2021, Art. no. 721491.

[13] K. Jansen and L. Lagae, “Cardiac changes in epilepsy,” Seizure, vol. 19,

no. 8, pp. 455–460, 2010.

[14] C. Sevcencu and J. J. Struijk, “Autonomic alterations and cardiac changes

in epilepsy,” Epilepsia, vol. 51, no. 5, pp. 725–737, 2010.

[15] M. Zijlmans, D. Flanagan, and J. Gotman, “Heart rate changes and ECG
abnormalities during epileptic seizures: Prevalence and deﬁnition of an
objective clinical sign,” Epilepsia, vol. 43, no. 8, pp. 847–854, 2002.
[16] F. Leutmezer, C. Schernthaner, S. Lurger, K. Pötzelberger, and C. Baum-
gartner, “Electrocardiographic changes at the onset of epileptic seizures,”
Epilepsia, vol. 44, no. 3, pp. 348–354, 2003.

[17] P. Boon et al., “A prospective, multicenter study of cardiac-based seizure
detection to activate vagus nerve stimulation,” Seizure, vol. 32, pp. 52–61,
2015.

[18] J. Pavei et al., “Early seizure detection based on cardiac autonomic

regulation dynamics,” Front. Physiol., vol. 8, p. 765, 2017.

[19] J. J. Thiagarajan, D. Rajan, S. Katoch, and A. Spanias, “DDxNet: A deep
learning model for automatic interpretation of electronic health records,
electrocardiograms and electroencephalograms,” Sci. Rep., vol. 10, no. 1,
pp. 1–11, 2020.

[20] K. Schiecke, M. Wacker, F. Benninger, M. Feucht, L. Leistritz, and H.
Witte, “Advantages of signal-adaptive approaches for the nonlinear, time-
variant analysis of heart rate variability of children with temporal lobe
epilepsy,” in Proc. IEEE Eng. Med. Biol. Soc., 2014, pp. 6377–6380.
[21] I. Osorio and B. Manly, “Probability of detection of clinical seizures using

heart rate changes,” Seizure, vol. 30, pp. 120–123, 2015.

[22] T. De Cooman, C. Varon, B. Hunyadi, W. Van Paesschen, L. Lagae, and S.
Van Huffel, “Online automated seizure detection in temporal lobe epilepsy
patients using single-lead ECG,” Int. J. Neural Syst., vol. 27, no. 7, 2017,
Art. no. 1750022.

[23] T. De Cooman, T. W. Kjær, S. Van Huffel, and H. B. Sorensen, “Adaptive
heart rate-based epileptic seizure detection using real-time user feedback,”
Physiol. Meas., vol. 39, no. 1, 2018, Art. no. 014005.

[24] C. A. Galimberti, E. Marchioni, F. Barzizza, R. Manni, I. Sartori, and A.
Tartara, “Partial epileptic seizures of different origin variably affect cardiac
rhythm,” Epilepsia, vol. 37, no. 8, pp. 742–747, 1996.

[25] K. Vandecasteele et al., “The power of ECG in multimodal patient-speciﬁc
seizure monitoring: Added value to an EEG-based detector using limited
channels,” Epilepsia, vol. 62, no. 10, pp. 2333–2343, 2021.

[26] V. Shah et al., “The Temple University Hospital seizure detection corpus,”

Front. Neuroinformat., vol. 12, p. 83, 2018.

[27] C. Chatzichristos et al., “Epileptic seizure detection in EEG via fusion
of multi-view attention-gated U-net deep neural networks,” Proc. IEEE
Signal Process. Med. Biol. Symp., 2020, pp. 1–7.

[28] J. Engel Jr et al., “Epilepsy biomarkers,” Epilepsia, vol. 54, pp. 61–69,

2013.

[29] M. Golmohammadi, V. Shah, I. Obeid, and J. Picone, “Deep learning
approaches for automated seizure detection from scalp electroencephalo-
grams,” in Proc. Signal Process. Med. Biol., 2020, pp. 235–276.

[30] A. Shoeibi et al., “Epileptic seizures detection using deep learning tech-
niques: A review,” Int. J. Environ. Res. Public Health, vol. 18, no. 11,
2021, Art. no. 5780.

[31] K. Saab, J. Dunnmon, C. Ré, D. Rubin, and C. Lee-Messer, “Weak
supervision as an efﬁcient approach for automated seizure detection in
electroencephalography,” NPJ Digit. Med., vol. 3, no. 1, pp. 1–12, 2020.
[32] Y. Yang, N. D. Truong, C. Maher, A. Nikpour, and O. Kavehei, “Continen-
tal generalization of an AI system for clinical seizure recognition,” 2021,
arXiv:2103.10900.

[33] J.-H. Choi and J.-S. Lee, “EmbraceNet: A robust deep learning archi-
tecture for multimodal classiﬁcation,” Inf. Fusion, vol. 51, pp. 259–270,
2019.

[34] B. R. Greene, G. B. Boylan, R. B. Reilly, P. de Chazal, and S. Con-
nolly, “Combination of EEG and ECG for improved automatic neonatal
seizure detection,” Clin. Neuriophysiol., vol. 118, no. 6, pp. 1348–1359,
2007.

[35] D. Cogan, J. Birjandtalab, M. Nourani, J. Harvey, and V. Nagaraddi,
“Multi-biosignal analysis for epileptic seizure monitoring,” Int. J. Neural
Syst., vol. 27, no. 01, 2017, Art. no. 1650031.

[36] P. M. d. C. B. Maia, “NeuroMov: Multimodal approach for epileptic seizure
detection and prediction,” Ph.D. dissertation, Universidade do Porto,
Jul. 2019. [Online]. Available: https://repositorio-aberto.up.pt/bitstream/
10216/122327/2/352306.pdf

[37] F. Fürbass et al., “Automatic multimodal detection for long-term seizure
documentation in epilepsy,” Clin. Neuriophysiol., vol. 128, no. 8,
pp. 1466–1472, 2017.

[38] J. Klatt et al., “The EPILEPSIAE database: An extensive electroen-
cephalography database of epilepsy patients,” Epilepsia, vol. 53, no. 9,
pp. 1669–1676, 2012.

[39] K. Vandecasteele et al., “Automated epileptic seizure detection based on
wearable ECG and PPG in a hospital environment,” Sensors, vol. 17, no. 10,
2017, Art. no. 2338.

[40] P. Comon, “Independent component analysis, a new concept,” Signal

Process., vol. 36, no. 3, pp. 287–314, 1994.

[41] A. Belouchrani, K. Abed-Meraim, J.-F. Cardoso, and E. Moulines, “A
blind source separation technique using second-order statistics,” IEEE
Trans. Signal Process., vol. 45, no. 2, pp. 434–444, Feb. 1997.

[42] J. Dammers et al., “Integration of amplitude and phase statistics for
complete artifact removal in independent components of neuromagnetic
recordings,” IEEE Trans. Biomed. Eng., vol. 55, no. 10, pp. 2353–2362,
Oct. 2008.

[43] A. Gramfort et al., “MEG and EEG data analysis with MNE-Python,”

Front. Neurosci., vol. 7, p. 267, 2013.

[44] M. B. Malarvili and M. Mesbah, “Newborn seizure detection based
on heart rate variability,” IEEE Trans. Biomed. Eng., vol. 56, no. 11,
pp. 2594–2603, Nov. 2009.

[45] J. Jeppesen et al., “Seizure detection based on heart rate variability us-
ing a wearable electrocardiography device,” Epilepsia, vol. 60, no. 10,
pp. 2105–2113, 2019.

[46] S. J. Smith, “EEG in the diagnosis, classiﬁcation, and management of
patients with epilepsy,” J. Neurol., Neurosurgery Psychiatry, vol. 76,
no. suppl 2, pp. ii2–ii7, 2005.

[47] M. Zijlmans, P. Jiruska, R. Zelmann, F. S. Leijten, J. G. Jefferys, and J.
Gotman, “High-frequency oscillations as a new biomarker in epilepsy,”
Ann. Neurol., vol. 71, no. 2, pp. 169–178, 2012.

[48] R. Q. Quiroga, H. Garcia, and A. Rabinowicz, “Frequency evolution during
tonic-clonic seizures,” Electromyogr. Clin. Neuriophysiol., vol. 42, no. 6,
pp. 323–332, 2002.

[49] X. Shi, Z. Chen, H. Wang, D. Y. Yeung, W. K. Wong, and W. C. Woo,
“Convolutional LSTM network: A machine learning approach for precipi-
tation nowcasting,” Adv. Neural Inf. Process. Syst., vol. 2015, pp. 802–810,
2015.

[50] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
recognition,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2016,
pp. 770–778.

[51] A. H. Ribeiro et al., “Automatic diagnosis of the 12-lead ECG using a
deep neural network,” Nature Commun., vol. 11, no. 1, pp. 1–9, 2020.
[52] A. Y. Hannun et al., “Cardiologist-level arrhythmia detection and classi-
ﬁcation in ambulatory electrocardiograms using a deep neural network,”
Nature Med., vol. 25, no. 1, pp. 65–69, 2019.

[53] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep network
training by reducing internal covariate shift,” in Proc. Int. Conf. Mach.
Learn., 2015, pp. 448–456.

[54] B. Xu, N. Wang, T. Chen, and M. Li, “Empirical evaluation of rectiﬁed

activations in convolutional network,” 2015, arXiv:1505.00853.

[55] R. F. Woolson, “Wilcoxon signed-rank test,” Wiley Encyclopedia Clin.

Trials, pp. 1–3, 2007.

[56] S. G. Mueller, L. M. Bateman, M. Nei, A. M. Goldman, and K. D.
Laxer, “Brainstem atrophy in focal epilepsy destabilizes brainstem-brain
interactions: Preliminary ﬁndings,” NeuroImage: Clin., vol. 23, 2019,
Art. no. 101888.

[57] A. Bardai et al., “Epilepsy is a risk factor for sudden cardiac arrest in the
general population,” PLoS One, vol. 7, no. 8, 2012, Art. no. e42749.
[58] E. J. d. S. Luz, W. R. Schwartz, G. Cámara-Chávez, and D. Menotti,
“ECG-based heartbeat classiﬁcation for arrhythmia detection: A survey,”
in Proc. Comput. Methods Prog. Biomed., 2016, vol. 127, pp. 144–164.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:44 UTC from IEEE Xplore.  Restrictions apply.
