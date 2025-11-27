# Pordoy et al. - 2025 - Enhanced Non-EEG Multimodal Seizure Detection A Real-World Model for Identifying Generalised Seizur

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 5, MAY 2025

3329

Enhanced Non-EEG Multimodal Seizure
Detection: A Real-World Model for
Identifying Generalised Seizures
Across the Ictal State

J. Pordoy , G. Jones , N. Matoorian, M. Evans, N. Dadashiserej

, and M. Zolgharni

Abstract—Non-electroencephalogram seizure detection
holds promise for the early identiﬁcation of generalised on-
set seizures. However, existing methods often suffer from
high false alarm rates and difﬁculty distinguishing normal
movements from seizure manifestations. To address this,
we obtained exclusive access to the Open Seizure Database
and selected a representative dataset of 94 events (42 gen-
eralised tonic-clonic seizures, 19 focal seizures, and 33 la-
belled as Other), totaling approximately 5 hours and 29 min-
utes. Each event contains acceleration and heart rate data,
which were expertly annotated by a clinician in 5 sec-
ond timesteps, with each timestep assigned a class la-
bel of Normal, Pre-Ictal, or Ictal. We introduce AMBER
(Attention-guided Multi-Branching pipeline with Enhanced
Residual Fusion), a multimodal seizure detection model
designed for Ictal-Phase Detection. AMBER constructs
multiple branches to form independent feature extraction
pipelines for each sensing modality. The outputs of each
branch are passed to a Residual Fusion layer, where the ex-
tracted features are combined into a fused representation
and propagated through two densely connected blocks.
The results of these experiments highlight the effective-
ness of Ictal Phase Detection, with the model recording
an accuracy and f1-score of 0.9027 and 0.9035, respec-
tively, on unseen test data. Further experiments recorded
True Positive Rate of 0.8342, 0.9485, and 0.9118 for the
Normal, Pre-Ictal, and Ictal phases, respectively, with an
average False Positive Rate of 0.0502. This study presents
a novel
Ictal Phase Detection technique that enhances
seizure phase classiﬁcation while showing reduced false
alarms, laying the groundwork for further advancements
in non-electroencephalogram-based seizure detection re-
search.

Index Terms—Seizure detection, multimodal, attention,

residual fusion, multi-branching, 1D CNN, acceleration.

Received 26 June 2023; revised 10 November 2023, 8 June 2024,
and 13 November 2024; accepted 16 January 2025. Date of publication
21 January 2025; date of current version 7 May 2025. (Corresponding
author: J. Pordoy.)

J. Pordoy, N. Matoorian, N. Dadashiserej, and M. Zolgharni are with
the Department of Computing, University of West London, W5 5RF
London, U.K. (e-mail: pordjam@uwl.ac.uk, jamiepordoy@hotmail.com,
jamie.pordoy@uwl.ac.uk; nasser.matoorian@uwl.ac.uk; nasim.dadashi
serej@uwl.ac.uk; massoud.Zolgharni@uwl.ac.uk).

G. Jones is with Open Seizure Detector, TS26 Hartlepool, U.K.

(e-mail: graham@openseizuredetector.org.uk).

M. Evans is with Pleotek, BT9 7BG Belfast, U.K. (e-mail: molly_evans

@live.com).

Digital Object Identiﬁer 10.1109/JBHI.2025.3532223

I. INTRODUCTION

A FFECTING approximately 1% of the global population,

epilepsy is a chronic neurological disorder that is char-
acterised by a lasting predisposition to generate recurring, un-
provoked seizures [1]. Seizures are transient, paroxysmal alter-
ations of the neurologic function resulting from an excessive,
hypersynchronous electrical discharge of neurons [2]. The ictal
state refers to the sequence of events and physiological changes
encompassing an epileptic seizure and can be divided into the
inter-ictal (normal state between seizures), pre-ictal (the state
before a seizure), ictal (seizure activity) and post-ictal (the state
following the seizure) phases. As deﬁned by the International
League Against Epilepsy, epileptic seizures are divided into four
sub-categories: focal, generalised, focal to bilateral tonic-clonic,
and unknown [3]. Focal seizures, also known as auras, are
conﬁned to one cerebral hemisphere and can affect a patient’s
muscle activity and cognitive awareness. Generalised seizures
involve abnormal electrical ﬂuctuations between communicat-
ing neuronal pathways and affect both hemispheres, resulting in
muscle twitches, clonic jerking, a loss of consciousness, and
compromised breathing [4]. A focal to bilateral tonic-clonic
(FBTC) seizure begins as a focal event and subsequently gener-
alises as the electrical discharge spreads across both hemispheres
during the ictal phase into a generalised seizure. Despite phar-
macological and surgical advancements, approximately 25%
of patients diagnosed with epilepsy continue to experience
spontaneous, unprovoked seizures. This condition is known as
refractory or drug-resistant epilepsy. Epilepsy-related mortality
remains a signiﬁcant concern, with Sudden Unexpected Death
in Epilepsy (SUDEP) documented as the predominant cause
of premature epilepsy-related death with an incidence in adults
recorded at 1.2 per 1000 patients [5].

Sveinsson et al. [6] conducted a clinical review to identify
several leading risk factors for SUDEP, highlighting that patients
with epilepsy (PWE) who experience uncontrolled generalised
tonic-clonic (GTC) seizures are the primary at-risk group. Ad-
ditionally, the risk of SUDEP is further increased if a PWE
lives alone and experiences nocturnal GTC seizures, resulting
in a 15-fold increased risk of early mortality. However, in 69%
of cases, Sveinsson et al. also observed that premature death
could have been prevented if there was an assistive form of
in-home supervision during nocturnal hours. Due to the sub-
stantial proportion of unsupervised, in-home cases, there is a
growing need for automated in-home seizure detection to miti-
gate the risk of SUDEP. As postulated by Friedman and Kazl [7],

2168-2194 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies.
Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html
for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

3330

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 5, MAY 2025

non-invasive detection systems could be used to augment in-
home, nocturnal supervision and reduce the number of SUDEP
cases through the early identiﬁcation of generalised onset
seizures.

A. Related Work

Conventional electroencephalogram (EEG) monitoring is
classed as the gold standard for the diagnosis, monitoring and
detection of epileptic seizures. Clinicians can evaluate real-time
neurological activity to diagnose the onset of a generalised
event before it is clinically apparent. However, this method of
detection is inadequate for real-world, in-home use as EEG mon-
itoring is an expensive, time-consuming technique that requires
a full clinical team with an electro-neurodiagnostic technician
to afﬁx a series of scalp-based electrodes for neurological ob-
servation [8].

Lamberts et al. [9] emphasised the need for preventive in-
home measures, including nocturnal supervision to monitor
high-risk patients susceptible to SUDEP and status epilepti-
cus. To address the practical limitations associated with in-
home EEG detection, researchers have explored the use of
non-electroencephalogram (non-EEG) sensors to measure phys-
iological changes in PWE. Thus, non-EEG detection has become
a signiﬁcant area of research, that employs non-invasive sensors
to detect different types of epileptic seizure.

Most non-EEG systems are designed for real-world use out-
side of a hospital or epilepsy monitoring unit (EMU), and com-
bine wireless sensing modalities with state-of-the-art algorithms
and commercial smart devices to form closed-loop detection sys-
tems [10]. Due to the large proportion of epilepsy-related deaths
accounted for by SUDEP, there has been an increase in the num-
ber of studies devising novel closed-loop detection and ambula-
tory monitoring systems. These studies have examined the utility
of accelerometers (ACMs), photoplethysmography (PPG), sur-
face electromyography, and video motion sensors for non-EEG
seizure detection. Among these, ACMs have demonstrated the
greatest efﬁcacy in detecting the initial convulsive muscle move-
ments associated with GTC seizures. ACMs are non-invasive,
lightweight, and cost-effective sensors that measure accelera-
tion, making them a favourable modality for seizure detection.
However, despite the success of ACM detection, a review of
the literature found that ACM detection systems often have a
high false alarm rate when detecting generalised onset seizures,
ranging from several times a day [12], [13] to once every ﬁve
days [11].

To reduce the false alarm rate, a 2020 study investigated how
seizure and non-seizure movements could be distinguished using
a three-dimensional spatial plane. The study measured 94.45%
for classiﬁcation accuracy, and successfully distinguished the
convulsive movements of a GTC seizure from 12 common ev-
eryday movements [14]. However, this approach is only partially
viable as on closer observation we can see that 80% of the data
used in this study was simulated from healthy participants, thus it
is hard to deduce whether this classiﬁcation technique is feasible
in the real-world.

Zia et al. [15], investigated real-time seizure detection using
embedded wireless sensors and signal processing techniques to
record 99% classiﬁcation accuracy. However, this study only
had access to data from three GTC seizures, which was recorded
using a smartphone ACM. Whilst this study presented a series
of novel ideas and contributes one of the ﬁrst non-EEG datasets,

its overall impact was hindered by the breadth and depth of the
available data. Several ground-breaking studies have also used
simulated patient data to pioneer non-EEG seizure detection
research [13], [16].

Notably the seminal work of Conradsen et al. [17], whose
research into non-invasive detection of seizure motor manifesta-
tions laid forth an early framework for multimodal classiﬁcation
still used today. However, a large proportion of the data used for
research and commercial seizure detection originates in EMUs,
often in the presence of a full clinical team with state-of-the-art
technology, and a fully controlled environment [18]. Seizures in
EMUs will be different to those in a residential environment, as
PWE will have to handle the daily tasks and challenges of living
with a neurological disorder without relying on a team of clinical
experts assisted by video-EEG monitoring. Furthermore, EMUs
are often afﬁliated with commercial collaborators and large
consortiums, thus preventing the sharing of data and results due
to intellectual property restrictions and conﬂicts of interest [19].
Most ﬁelds of neurological research have access to clinically
annotated data, however as a research ﬁeld non-EEG seizure
detection is missing the core components required to facilitate
rapid progression. As a result, we can see a trend across literature
where studies have had to use simulated data to produce algo-
rithms with excessively high accuracy scores and frequent false
alarms.

Several studies have employed the EEG to extract neuro-
logical features to distinguish the different phases of the ictal
state. Early studies encountered challenges in accurately dis-
tinguishing each ictal phase when analysing EEG recordings.
A pioneering approach applied adaptive threshold modelling to
detect convergence in short-term maximum Lyapunov exponent
values from intracranial EEG recordings. However, this method
yielded inconsistent results, with a p-value score of 0.5 and a
high false prediction rate, rendering it unsuitable as a clinical
diagnostic technique [20].

Similar research was conducted by Zeljkovi´c et al. [21] whose
optical ﬂow extraction and band-pass temporal ﬁltering tech-
niques were used to analyse video-EEG recordings to differ-
entiate the phases of the ictal state. However, this technique
failed to predict 46% of video-EEG recordings, incorrectly
classifying 4% and 42% of normal and ictal instances as pre-ictal
respectively.

A more recent study by Eftekhar et al. [22], utilised N-gram-
based pattern recognition with similarity metrics (Hamming dis-
tance and Needleman-Wunsch algorithm) to identify the epoch
thresholds between ictal classes, achieving an average prediction
sensitivity score of 93.81%, along with a false prediction rate of
0.06/h.

However,

the seminal work by Sharif and Jafari [23]
presents the most compelling EEG research. By employing
optimised Poincaré plane analysis, each ictal phase was de-
tected, recording an average sensitivity score between 91.8%
and 96.6%, and an average false prediction rate of 0.05–0.08 per
hour.

While previous studies have classiﬁed distinct ictal phases,
the practical application of EEG-based seizure detection re-
mains primarily conﬁned to clinical settings due to operational
costs. Conversely, non-EEG methodologies have demonstrated
potential with real-world application. However, they face in-
herent challenges in distinguishing between different types of
seizure-related movement, leading to recurrent false alarms and
inaccuracies in seizure detection.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

PORDOY et al.: ENHANCED NON-EEG MULTIMODAL SEIZURE DETECTION: A REAL-WORLD MODEL

3331

To improve the clinical utility and reliability of non-EEG
seizure detection systems, it is imperative to address these lim-
itations. While previous studies have explored the feasibility of
detecting ictal classes using EEG techniques, to our knowledge,
no prior research has investigated whether non-EEG modalities
can distinguish between these phases. Thijs et al. [24] sug-
gested that ictal autonomic changes could serve as diagnostic
indicators, providing unique target variables for seizure detec-
tion mechanisms to identify. Autonomic manifestations often
become more pronounced as a seizure traverses the ictal state,
particularly in focal seizures originating from the temporal lobe
and generalising into a FBTC seizure. However, the absence of
publicly available data with clinical annotations has impeded
the validation of this hypothesis and the development of a
viable non-EEG detection methodology capable of discerning
the different ictal phases.

B. Contributions

This section outlines the contributions of this study, which are

summarised as follows.

1) This study introduces a novel seizure detection tech-
nique (Ictal-Phase Detection) capable of distinguishing
between high-amplitude convulsive movement typical of
the ictal phase and low-amplitude myoclonic movement
observed in the pre-ictal phase.

2) AMBER is a new deep learning model designed for
non-EEG, multimodal seizure detection. The model em-
ploys multiple branches (multi-branching) to indepen-
dently process features, which are then fused into a sin-
gle representation and propagated through a dense net-
work, enabling effective multimodal detection for com-
plex biomedical tasks.

3) The proposed model achieved accuracy, f1, Cohen’s
Kappa, and MCC scores of 0.9027, 0.9035, 0.8498,
and 0.8519, respectively. These results underscore the
model’s ability to effectively distinguish between posi-
tive and negative classes while accurately classifying the
different phases of the ictal state.

4) We conducted a per-participant evaluation of the model’s
performance by grouping events in the test set by user
and measuring the classiﬁcation performance for each
participant. The model achieved an average accuracy
score of 0.8412 for participants exclusive to the testing
subset, demonstrating the models ability to generalise
effectively on unseen data from participants with different
types of epilepsy.

II. METHODOLOGY

In this methodology, we introduce a non-EEG seizure de-
tection technique called Ictal-Phase Detection. This detection
technique is based on the hypothesis that it is feasible to distin-
guish pre-ictal manifestations from the convulsive jerking and
clonic movements characteristic of the ictal phase in generalised
onset seizures. While conventional non-EEG seizure detection
techniques primarily focus on the classiﬁcation of seizure and
non-seizure states, a signiﬁcant number of seizures exhibit a pre-
ictal phase characterised by subtle, low-amplitude myoclonic
movements that are often referred to as focal seizures or auras.

The aim of this study is to differentiate the phases of the
ictal state by distinguishing between high-amplitude and low-
amplitude movements. We hypothesise that there are quantiﬁ-
able variances in acceleration and heart rate between the normal
(seizure-free), pre-ictal, and ictal phases. While accelerometers
easily capture high-amplitude convulsive movements, detect-
ing pre-ictal, low-amplitude movements is more challenging.
However, subtle heart rate elevations during the pre-ictal phase,
in conjunction with low amplitude movements could provide
indications of seizure onset. Thus, heart rate data will serve
as a secondary modality to complement the acceleration data,
enhancing the models ability to detect different seizure mani-
festation.

To address this, we propose the development of a new model
that can independently leverage sensor data from two or more
modalities. We posit that independent feature extraction will
improve predictive reliability as a true representation of each
modality is extracted. These representations can then be fused
to form a single output vector of key features, thus enhancing
the model’s ability to generalise.

To our knowledge, this represents the ﬁrst study undertaking
non-EEG seizure detection research into the ictal state. As there
are no publicly available datasets to validate our hypothesis,
Open Seizure Detector granted the University of West London
early access to the Open Seizure Database [25], [26] [27].

A. The Open Seizure Database

This is the ﬁrst study to use the newly developed Open
Seizure Database (OSDB) - Version 3 [28]. Designed by Open
Seizure Detector (OSD) [26], to facilitate research into non-EEG
seizure detection, the OSDB contains multimodal sensor data
from 49 participants in real-world environments. The database is
comprised from 494 events, encompassing 139 epileptic seizures
and is collected over a duration of 453 days [28]. Continuous
patient monitoring was facilitated for this period where patient
data was recorded using wearable Garmin devices equipped with
embedded ACM and PPG sensors.

B. Dataset

For this study, we initially selected 139 events from the OSDB,
categorised as GTC, Aura, Atonic/Fall, Other, and Simulated.
For consistency, we removed 36 events that lacked simultaneous
acceleration and heart rate data. We then ﬁltered events labelled
as Simulated and Atonic/Fall, as they were outside the scope of
our experiments. This resulted in a ﬁnal representative dataset
of 94 events, consisting of 42 GTC Seizures, 19 Auras/Focal
Seizures, and 33 seizures categorised as Other. The OSDB labels
a seizure as Other if the event lacks further categorisation [28].
The ﬁnal representative dataset consists of non-EEG data
from 18 participants diagnosed with generalised epilepsy, with
a combined duration of 5 hours, 29 minutes, and 5 seconds.
Each event is assigned an identiﬁer and structured using a
one-to-many relationship, where one event is formed from mul-
tiple sub-events, each representing a 5-second timestep. Each
timestep contains simultaneous acceleration and heart rate data
as shown in Fig. 1. The acceleration data, denoted as A, was
sampled at 25Hz, resulting in 125 datapoints for each 5-second
timestep and can be expressed as At={a1, a2, . . . , a125} where
an denotes the indexed acceleration datapoint within timestep
t. The heart rate, data denoted as H, was recorded using a PPG

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

3332

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 5, MAY 2025

Fig. 1. Event 15039 Time-series Plot: The upper plot maps one-
dimensional acceleration data as vector magnitude, while the lower plot
shows interpolated heart rate data recorded in beats per minute.

Fig. 2. Event 7261 Analysis Plots: Rate of change of acceleration (left),
standard deviation (centre) and maximum acceleration (right).

sensor with a lower sample rate of 0.2 Hz, computing a single
heart rate datapoint (h1) for each 5-second timestep, which can
expressed as Ht = {h1}.

C. Clinical Annotation

In this subsection, we detail the clinical annotation process for
Ictal-Phase Detection. To test our hypothesis of differentiating
the various phases of the ictal state, the clinical team annotated
the timesteps for each event with a class label of 0, 1, or 2, corre-
sponding to the normal, pre-ictal, and ictal phases respectively. It
is important to note that, in a clinical or descriptive context, ictal
phases are referred to in lowercase (normal, pre-ictal, and ictal),
while the corresponding class labels are capitalised (Normal,
Pre-Ictal, and Ictal).

The Normal class denotes movements outside of the con-
vulsive scope, speciﬁcally during the inter-ictal and post-ictal
phases. This approach was inspired by Abdulhay et al. [39], who
also used the Normal class to express inter-ictal (seizure-free)
states in EEG signal classiﬁcation. The Pre-Ictal class represents
focal seizures, auras, and low-amplitude myoclonic movement
that typically precedes seizure onset. We then used the Ictal class
to represent high-amplitude signals, indicative of the convulsive
movements and clonic jerking that occur between seizure on-
set and cessation. We conducted an analysis of each event to
compute a set of averages which provided guidelines for the
clinical annotation process (see Fig. 2). The rate of change of
acceleration was the main technique used to guide the annotation
process and can be expressed as:

Rate of Change of Acceleration =

At − At−1
Δt

(1)

Fig. 3. Clinical Annotation Plots: White, blue and green annotations
represent the Normal, Pre-Ictal and Ictal classes respectively.

At - At−1 represents the difference in acceleration datapoints
between two adjacent timesteps, where At represents acceler-
ation at the end of timestep t, At−1 represents acceleration at
the end of the previous timestep, and Δt denotes the duration of
timestep t.

We conducted secondary computations to validate the results
of (1), calculating the average acceleration range, maximum
acceleration, and standard deviation of acceleration for each
timestep. The clinician then utilised these results along with
partial video footage to annotate each 5-second timestep with a
class label.

Table I presents the average thresholds calculated to guide
the clinical team in annotating each timestep. Annotations were
conducted using Oxford University’s VGG Image Annotation
software [29], where 2D boundary boxes were employed to
visualise the segmented data into ictal phases (Fig. 3). The
annotated timesteps were stored as a CSV ﬁle and grouped by
event. All events were consolidated into a single dataframe, and
then a new column called Outcome was appended to denote the
ground truth annotations.

D. Cubic Spline Interpolation

This subsection details the interpolation techniques used to
reshape our heart rate data. For each instance of t, acceleration
data consists of 125 datapoints, whereas heart rate data is com-
prised of a single datapoint, resulting from the different sampling
rates used when the OSDB was recorded.

We used linear interpolation to address the disparity in
size between acceleration and heart rate features. This gener-
ated a straight-line connection of interpolated values between
heart rate datapoints. However, this straight-line approxima-
tion did not accurately reﬂect the heart rates natural curvature
and we felt linear interpolation could negatively impact our
results.

To further address this disparity and create a curvature that
represents uniform dimensions for each feature, we employed
cubic spline interpolation to mathematically construct a piece-
wise continuous curve that passes through each of the heart rate
datapoints (xi, yi) for i = 0, 1, . . . , N , where xi represents the
sequence index and yi represents the heart rate value at that point.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

PORDOY et al.: ENHANCED NON-EEG MULTIMODAL SEIZURE DETECTION: A REAL-WORLD MODEL

3333

TABLE I
CLINICAL ANNOTATION AVERAGES: THESE AVERAGES WERE EMPLOYED TO ASSIGN CLASS LABELS (0 FOR NORMAL, 1 FOR PRE-ICTAL, AND 2 FOR ICTAL)
TO EACH TIMESTEP

Fig. 4. Cubic Spline Interpolation. Each timestep t corresponds to a
single heart rate datapoint (blue). Linear interpolation (green) connects
adjacent timesteps, followed by cubic spline interpolation (orange), re-
sulting in a smooth curve with 125 interpolated datapoints.

The resulting function y = f (x) represents the heart rate value
y as a continuous function of x, providing a smooth transition
through the datapoints. Since there are 125 datapoints in At, we
interpolated 124 interpolated indices for Ht. For each instance
of i within Ht(i), a cubic polynomial can be calculated as:
Ht(i) = ai + bi(t − ti) + ci(t − ti)2 + di(t − ti)3
(2)
where Ht(i) denotes the computed polynomial for interval i.
The coefﬁcients ai, bi, ci, and di are calculated to generate a
smooth interpolation between datapoints. The linear coefﬁcient
bi represents the rate of change between ti and ti+1. The
quadratic coefﬁcient ci captures the quadratic behaviour, and
the cubic coefﬁcient di models the curvature between ti and
ti+1. To calculate the polynomial values at ti, coefﬁcients ai, bi,
ci, and di are iteratively computed for each instance of i in t. This
process yields a smooth cubic polynomial interpolation between
datapoints at ti and ti+1 (Fig. 4). As a result, the heart rate
data for timestep t has been reshaped into a set of interpolated
datapoints where Ht = {h1, h2, . . . , h125.

Since the heart rate datapoints are recorded using a PPG
sensor at 5-second intervals, they serve as accurate cardiac
biomarkers. While the original datapoints remain unchanged,
interpolated values are used to align the lengths of At and
Ht. It is important to note that the PPG signal cannot be
substituted, as it directly reﬂects heart rate activity, while the
interpolated values create a continuous signal between the PPG
datapoints. This approach ensures the integrity of the heart rate
signal is maintained, without negatively impacting the model’s
performance.

E. Preprocessing

In this subsection we describe the preprocessing techniques
that were undertaken. Following the reshaping of our
representative dataset, a class imbalance was observed in
which the Normal class accounted for 48.23% (1534 timesteps)
of the overall dataset with the Pre-Ictal (901 timesteps) and Ictal
(745 timesteps) classes accounting for 28.34% and 23.42%
respectively. This imbalance was expected, given that
the
average duration of the ictal phase of a generalised seizure is

≈ 39.3 ± 17.7 seconds, while the pre-ictal phase can range
from seconds to minutes before generalisation [30].

To address this imbalance, time-series random oversampling
was employed. This technique increased the representation of
minority classes, making all classes proportionate to the majority
class while preserving the sequential order of the datapoints in
each timestep. The result was a resampled dataset comprised of
4602 timesteps with a balanced distribution, where each class
accounted for 33.3% (≈ 1534 timesteps).

We then reshaped the preprocessed dataset into a three-
dimensional vector denoted as Xt to facilitate time-series mod-
elling. This input vector integrates the preprocessed accel-
eration data, represented as At, and heart rate data, repre-
sented as Ht into a single vector which can be expressed as
Xt = [a1, h1, a2, h2, . . . , a125, h125]. The reshaped vector Xt
is formed from three dimensions: the number of timesteps, the
timestep length, and the number of features, resulting in a ﬁnal
size of (4602, 125, 2).

F. Proposed Model

In this subsection, we introduce AMBER (Attention-guided
Multi-Branching-pipeline with Enhanced Residual fusion). The
architecture of the proposed model is shown in Fig. 5. AM-
BER constructs multiple branches upon initialisation, where the
number of branches is proportionate to the number of input
features. Each branch establishes a dedicated feature extraction
pipeline, incorporating attention mechanisms as the ﬁnal layer
to identify salient features. The output of each branch is then
passed in parallel to the model’s custom layer called, Enhanced
Residual Fusion, which fuses the output of both branches into a
single representation, combining the acceleration and heart rate
features. The fused representation is then passed to the model’s
classiﬁer. To introduce non-linearity, the output is propagated
through two densely connected blocks before being passed to the
ﬁnal dense layer, which employs a softmax activation function
for multi-class classiﬁcation.

G. Model Overview

The AMBER model employs branch-speciﬁc vector partition-
ing to construct independent branches denoted as β, where the
number of branches equals the number of input features. The
model takes the reshaped multivariate array Xt as input, which
is then partitioned and a permutation is applied to reshape the
vectors’ dimensions, forming two independent input vectors.
The acceleration and heart rate input vectors now expressed
as X A and X H are passed to branch βA and βH as input.
We can express these vectors mathematically as X A
t =
[x1, x2, x3, . . . , x125] ∈ R125, where 125 real-valued datapoints
(x) are passed as input for each instance of t.

t or X H

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

3334

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 5, MAY 2025

Fig. 5. Architecture of the Attention-guided Multi-Branching-pipeline with Enhanced Residual fusion (AMBER) Model.

Layered Representation of AMBER: (1) = Feature Extraction Pipeline with 3 * convolutional blocks (b1, b2, b3), 1 * BiLSTM and 1 * Attention,

Fig. 6.
(2) = Fusion Layer (Enhanced Residual Fusion), (3) = Classiﬁer with 2 * dense blocks (d1, d2) and a softmax layer.

H. Feature Extraction Pipeline

The following notation is a representation of input vector
Xt as it traverses through the layers in the AMBER model
(see Fig. 6). For each branch, Xt is passed as input through
a dedicated feature extraction pipeline, comprised from three
convolutional blocks denoted as b1, b2, and b3. For each block,
the 1D convolutional layer has a ﬁlter size 256, 128 and 64
respectively. We then conﬁgured the convolutional layer with
a kernel size of 2, a stride of 1, followed by ReLU activation
function to introduce non-linearity. The layer then performs a
convolutional operation which can be mathematically expressed
as:

(cid:4)

yl
j = σ

Conv1D(wl

i,j, xl−1
i

) + bl
j

(3)

(cid:2)

Nl−1(cid:3)

i=1

Let yl
j represent the output of the j-th feature map in the l-th
layer, computed by applying a sigmoid activation function to
the sum of the convolutional operations between the ﬁlter of the
l-th layer (wl
i,j) and the feature map from the previous layer
(xl−1
). Let bl
j express the bias of the j-th feature map in layer l,
i
which we then add to the result of the convolutional operation
to introduce an offset. A summation is then computed for all
neurons in the previous layer (Nl−1), resulting in the activation
of the j-th feature map in layer l.

The output of the convolutional operation undergoes standard-
isation through a batch normalisation layer to improve training
stability and accelerate convergence. Proceeding, a ReLU acti-
vation layer is applied, introducing non-linearity to the block.
We then conducted downsampling through a max pooling layer
to extract features while reducing dimensionality. This process
iterates through blocks b1 to b3, where the features are ﬂattened

to form a 1D vector, denoted as X. The vector is then reshaped
into a 3D tensor for instance of t. The reshaped 3D tensor, xt,
is then passed as input to the proceeding bidirectional Long
Short-Term Memory (BiLSTM) layers.

−→ct and
←−ct and

The pipeline’s bidirectional layers utilise a pair of hidden (h)
−→
ht represent
and cell (c) states. For each time step t,
←−
ht represent
these states in a forward direction, while
the states in a backward direction. To regulate the information
ﬂow to the cell state, three non-linear gating mechanisms are
employed, expressed as the input gate (it), the output gate (ot),
and the forget gate (ft).
−→
ft applies a sigmoid function to determine
For each timestep,
what information should be retained from the previous cell state
−−→ct−1) and xt. This can be expressed by:
(

−→
ft = σ(

−→
Wf · [

−−→
ht−1, xt] +

−→
bf )

(4)

−→
it to calculate the information that should be added
We then use
−→ct , and then employ
−→ct is used
−→ot to calculate how much of
to
as output for the current timestep. These gates are deﬁned as:

−→
it = σ(
−→ot = σ(

−→
bi )

−→
Wi · [
−→
Wo · [

−→
ht, xt] +
−−→
ht−1, xt] +

−→
bo )

(5)

(6)

For each timestep, parallel computations are conducted in both
←−
ht)
the forward and backward directions. Hidden states (
from both directions are concatenated to form ht. The cell states
−→ct , ←−ct ) are aggregated using ft and it, forming the output
(
ct. The output gate ot then reﬁnes the cell state by applying
a sigmoid function, regulating the gating mechanism with a
hyperbolic tangent function to control the information ﬂow. The
results from the forward and backward layers are concatenated

−→
ht,

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

PORDOY et al.: ENHANCED NON-EEG MULTIMODAL SEIZURE DETECTION: A REAL-WORLD MODEL

3335

computation of attention weights has already been explained
in (7), we do not repeat it here. The attention scores for each
head are then calculated using a scaled dot-product, as shown in
the following equation:

hi = Softmax

· Vt

(11)

(cid:5)

(cid:6)

Qt · K (cid:7)
t√
dk

Fig. 7. Architecture of the Enhanced Residual Fusion Layer illustrating
how attention weights X A and X H are outputted from branch βA and
βH , concatenated, passed to a multi-head attention mechanism, and
then fused with the original inputs via a residual connection.

←−
ht].

to form the bidirectional output of t, which we can express as
Xt = [

−→
ht,

We then pass Xt through a single-headed attention mech-
anism, denoted as Attt, positioned as the ﬁnal layer in each
pipeline to extract relevant features. Vector Xt undergoes a linear
transformation to construct three attention matrices: Query (Qt),
Key (Kt), and Value (Vt). This transformation is expressed as:
Qt = Xt · WQ, Kt = Xt · WK , Vt = Xt · WV

(7)
In these equations, WQ, WK , and WV are pre-set weighted ma-
trices with the dimensions d × dk, where d is the dimensionality
of the input feature. The attention scores for timestep t are then
computed by taking the dot product of Qt and transposed matrix
K T
t .

Attention Scorest = Qt · K T
(8)
t
These scores are then scaled by the square root of dk to maintain
numerical stability, which we can express as:

Scaled Scorest = Attention Scorest

√

dk

(9)

The Scaled Scores are then passed through a softmax function
and multiplied by Vt to compute a ﬁnal set of attention weights
for Attt.

Xt = Softmax(Scaled Scorest) · Vt

(10)

I. Enhanced Residual Fusion Layer

In this subsection, we introduce our enhanced Residual Fusion
layer, designed to merge the outputs of two or more branches into
a single fused representation (see Fig. 7). Attention weights X A
t
and X H
from branches βA and βH are passed in parallel to the
t
Residual Fusion layer, where the weights from both branches are
concatenated to create vector Xt. Mathematically, this operation
is expressed as Xt = concat[X A
t ], with Xt formed from the
dimensions R(|A|+|H|)×d.

t , X H

Vector Xt is then passed through a multi-head attention
mechanism, denoted as AttM
t , which consists of 8 attention
heads, denoted as h1 through h8. Each attention head operates
on a low-dimensional (32-dimensions) projection space derived
from the original concatenated inputs.

The attention heads, h1 through h8, independently compute
the Qt, Kt, and Vt matrices using learned weights. Since the

where Kt and Vt are the key and value matrices used to compute
the i-th attention head. The dimensions of the Kt and Vt matrices
are R(|A|+|H|)×dk and R(|A|+|H|)×dv , respectively. The output
for each head is then concatenated and linearly projected to form
the output of AttM
t :
AttM
t = concat(h1, h2, . . . , h8) · WO

(12)

To complete the Residual Fusion layer, AttM
is then multiplied
t
with the original concatenated input vector Xt through a residual
connection, outputting a fused vector denoted as Ft:

Ft = [Xt ∗ AttM
t ]

(13)

The residual connection is used to retain key features from both
branches while integrating the new information derived from
AttM
t . Thus, the Residual Fusion layer combines inputs from
X A and X H to form an attention guided, fused representation
of extracted features.

J. Classiﬁer and Loss Function

Vector Ft is then propagated through a fully connected net-
work, passing through dense blocks d1 and d2. Each dense
block consists of a single dense layer consisting of 128 neurons,
followed by a dropout layer with a dropout rate of 0.2, followed
by a batch normalisation layer. The output of d2 is then passed
to the ﬁnal dense layer, which employs a softmax activation
function to calculate the prediction probability of timestep t.
This can be calculated as:

ˆyt = Softmax(Ft · w + b)
(14)
where w represents the layers weights, b is the networks bias
and ˆyt is the predicted class label for timestep t.

III. EXPERIMENTAL SETUP

In this section, we detail the experimental setup employed for
this study. A shared Google Drive was established, facilitating
collaboration between technical and clinical team members for
annotating data. For each event, clinical annotations were stored
using a CSV ﬁle, which was accompanied by a visualisation plot
that represents the annotated phases (see Fig. 3). Experiments
were then conducted using Python 3.7 and TensorFlow 2.4.

The dataset was divided into two subsets: Approximately 70%
was allocated for training, while the remaining 30%, consisting
of 30 randomly selected events, was partitioned for independent
testing. The testing subset was comprised of events from 10 par-
ticipants, ﬁve of whom were independent and did not contribute
to the training data, while the remaining ﬁve provided events
for both subsets. However, the subsets were partitioned at the
event level to ensure that data from the same event could not be
in both the training and the testing subsets. The training subset
was further partitioned using stratiﬁed k-Fold Cross-Validation,
dividing the training data into 5 (k = 5) equal folds. We then
used k-1 folds (80%) to train the model, while the remaining
instance of k (20%) was utilised for our validation experiments.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

3336

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 5, MAY 2025

TABLE II
COMPARATIVE ANALYSIS: EVALUATION OF PERFORMANCE SCORES OBTAINED BY THE AMBER MODEL COMPARED TO SEVERAL STATE-OF-THE-ART
CLASSIFICATION MODELS AND CONFIGURATION

For each set of experiments in k, the proposed model was
trained for 100 epochs. Through iterative experimentation and
hyperparameter optimisation, we selected an RMSprop opti-
miser with a reduced learning rate of 0.0001 and an augmented
epsilon score of 1e–09. To improve generalisation and prevent
overﬁtting, we applied an l2 regulariser to the dense layers in d1
and d2, with the regularisation penalty set to 0.001. Furthermore,
if there were no improvements in the loss function for 10
consecutive epochs, the ReduceLROnPlateau callback function
was used to reduce the learning rate by 50%. We then chose a
batch size of 16 and employed a categorical cross-entropy loss
function to quantify the model’s performance. Experiments were
conducted to evaluate the models performance by calculating
the number of True Positive (TP), True Negative (TN), False
Positive (FP), and False Negative (FN) predictions.

1) TP represents the number of predictions where our model

correctly classiﬁed a positive class as positive.

2) FP represents the number of predictions where our model

incorrectly classiﬁed a negative class as positive.

3) FN represents the number of predictions where our model

correctly classiﬁed a negative class as negative.

4) TN represents the number of predictions where our model

incorrectly classiﬁed a positive class as negative.

IV. RESULTS

This section presents the results of this study and demon-
strates the application of the Ictal-Phase Detection technique.
The results are derived from several sets of experiments aimed
at evaluating overall performance. The model achieved an
average training accuracy of 0.9187, ranging from 0.9090
to 0.9242 across 5 folds (see supplementary material). Vali-
dation metrics indicated robust generalisation, with accuracy
scores slightly higher, between 0.9304 and 0.9701, and a
steady validation loss between 0.0317 and 0.0445. These re-
sults underscore the model’s ability to maintain high accu-
racy without overﬁtting, performing consistently across all
folds.

A. Comparative Analysis With State-of-The-Art Models

In this subsection, we compare the performance of AM-
BER with several state-of-the-art models, using the same data
and hyperparameter conﬁgurations (Table II). Our model (m1)
achieved a balance between generalisation and predictive preci-
sion, recording an overall accuracy of 0.9027 and an f1-score of
0.9035 on unseen test data. Additional experiments measured a

Cohen Kappa score of 0.8498 and a MCC of 0.8519, indicat-
ing consistent performance across both positive and negative
classes. Furthermore, the Positive Predictive Value (PPV) of
0.8914 and True Positive Rate (TPR) of 0.8981 further demon-
strate the model’s precision in identifying TPs while effectively
minimising FPs.

In comparison, models such as the 1D-CNN (m10), Stacked
LSTM (m9) and Stacked BiLSTM (m7) recorded lower per-
formance scores, while those incorporating attention mecha-
nisms (speciﬁcally, m2 and m4) recorded higher performance.
Models utilising multi-branching (m2, m3, and m5) recorded
notably higher accuracy and f1 scores, ranging from 0.8613
to 0.8698 and 0.8759 to 0.8952, respectively. Models m2 and
m3 employed multi-branching architectures, recording accuracy
scores of 0.8696 and 0.8613, respectively, outperforming 80%
of the tested models. However, m2 and m3 did not employ a
Residual Fusion layer, and the extracted features were concate-
nated, resulting in lower performance. These results underscore
the importance of independent feature extraction processes and
highlight the advantages of fusing features to maximise perfor-
mance.

B. Per-Class Classiﬁcation Analysis

In this subsection, we present the results of our model across
several confusion matrix experiments (Fig. 8), plotting the an-
notated ground truth against the models predicted labels.

Fig. 8(a) shows the confusion matrix results for our model on
the unseen testing subset. For the Normal class, 471 timesteps
were correctly classiﬁed, achieving a TP score of 86.42%.
However, 13.58% were misclassiﬁed, with 4.77% incorrectly
classiﬁed as Pre-Ictal and 8.81% as Ictal, suggesting an overlap
in feature space. For the Pre-Ictal class, the model classiﬁed
94.91% of TPs, correctly classifying 258 out of 272 timesteps,
with only 3.68% misclassiﬁed as Normal and 1.47% as Ictal.
Similarly, the model recorded a TP score of 91.87% for the
Ictal class, with 6.84% misclassiﬁed as Pre-Ictal and 1.29% as
Normal, indicating some overlap with Pre-Ictal markers.

Similar results were observed in our validation experiments
as shown in Fig. 8(b)–(f). Each experiment represents a k-1
partition of the training data used to validate each fold. The
model exhibited strong performance, with the Normal class
recording an average TP score of 96.38% across all folds, with
scores ranging from 94.44% to 98.46%. The model showed a
low FP score of 2.88% for the Normal class, indicating minimal
misclassiﬁcations when averaged across the validation data.
Similar results were observed for the Pre-Ictal and Ictal classes,
recording an average TP score of 96.88% and 96.43% respec-
tively. These results demonstrate the model’s effectiveness in

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

PORDOY et al.: ENHANCED NON-EEG MULTIMODAL SEIZURE DETECTION: A REAL-WORLD MODEL

3337

Fig. 8. Confusion Matrix Results: Each matrix maps the models predicted results to the ground truth labels for Normal, Pre-Ictal, and Ictal classes.
(a) presents the results of our model on the testing subset. (b)–(f) shows the validation results across each fold.

TABLE III
CLASSIFICATION ANALYSIS DISTRIBUTED BY ICTAL CLASS - NOTATION =
TPR = TRUE POSITIVE RATE, TNR = TRUE NEGATIVE RATE, PPV =
POSITIVE PREDICTED VALUE, NPV = NEGATIVE PREDICTED VALUE, FPR =
FALSE POSITIVE RATE, FNR = FALSE NEGATIVE RATE

identifying Ictal timesteps, with only 2.96% misclassiﬁed as FP
and 2.48% as FN.

Although the model recorded 96.38% TPs for the Normal
class during validation, performance on the test set dropped
to 86.42%, suggesting signiﬁcant variability. While there was
noticeable overlap between the Normal and Pre-Ictal classes,
it is important to note that the model demonstrated strong
generalisation, clearly distinguishing between the Pre-Ictal and
Ictal classes.

In Table III, we present further classiﬁcation results, dis-
tributed by class, based on predicted results in Fig. 8(a). These
results show the model recorded a high TPR across all classes,
with scores between 0.8342 and 0.9485, averaging 0.8981. A
high TNR was observed across all classes (average 0.9497),
highlighting the model’s effectiveness in correctly classifying
non-seizure timesteps. We observed variability in the PPV, with
the Normal class achieving a high score of 0.9652, while the
Pre-Ictal class recorded a lower score of 0.8037. This disparity

indicates a higher incidence of FPs for Pre-Ictal events com-
pared to the Normal class. The model’s False Positive Rate
(FPR) remained consistently low across all classes, averag-
ing 0.0502, indicating effective generalisation and inference.
Furthermore, the model achieved an average False Negative
Rate (FNR) of 0.1018, with the highest FNR of 0.1658 ob-
served in the Normal class. While the model performed well
in detecting Ictal events, we can see there is room for im-
provement when distinguishing between Normal and Pre-Ictal
classes.

C. Per-Participant Classiﬁcation Analysis

This subsection provides an analysis of the model’s perfor-
mance on the unseen testing subset, focusing on individual
participants rather than events. As shown in Fig. 9, further
experiments were conducted to evaluate the model’s effective-
ness across different participants, allowing for a more granular
understanding of the overall performance. The test set includes
events from 15 tonic-clonic seizures, 8 auras, and 8 additional
seizures denoted as Other. To ensure an independent evaluation,
events from Participants p83, p55, p62, p236, and p421 were
excluded from the training data and used exclusively in the
testing subset. In contrast, Participants p8, p39, p45, p144, and
p149 contributed events to both the training and testing subsets.
We recorded an overall accuracy score of 0.8874 across
all participants, although performance exhibited notable vari-
ability (see Fig. 9(a)). Participants p8, p39, p45, and p144
demonstrated high accuracy scores (above 0.9139), with an
average TPR of 0.9477,
indicating effective generalisation
across these subjects. However, for Participant p149, the model
showed lower performance, recording an accuracy score of

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

3338

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 5, MAY 2025

1, and 2 representing the Normal (white), Pre-Ictal (blue), and
Ictal (green) classes respectively.

In Fig. 10(a) to (d), the presence of a clear pre-ictal phase is ev-
ident, as indicated by both the acceleration and heart rate signals.
The acceleration data displays gradual increases in amplitude,
corresponding with higher intensity movements associated with
pre-ictal manifestations. Simultaneously, heart rate trends show
a steady increase of approximately 10% from the point of onset
to cessation. This pattern can be observed in all four plots,
where both modalities present a clear transition into the ictal
phase, marked by an elevated increase in beats per minute
and repetitive convulsive movements exceeding 2000 milli-g.
In contrast, Fig. 10(e) and (f) show GTC events with no clear
pre-ictal phase, where the ﬁrst signs of convulsive movements
emerge seconds before the onset of the ictal phase. Despite the
absence of a well-deﬁned pre-ictal phase, both modalities exhibit
trends that align with the observations seen in Fig. 10(a)–(d).
Heart rate increases of approximately 10% were observed prior
to repetitive ﬂuctuations in acceleration, reinforcing the notion
that even without a pre-ictal phase, there are clear physiological
changes that indicate seizure onset.

From these results, it is evident that the proposed model can
distinguish the convulsive movements of the Ictal class from the
movements observed in the Normal and Pre-Ictal classes. The
ictal phase was correctly classiﬁed across all six plots, accurately
detecting approximately 92.1% (35/38) of Ictal timesteps. A
degree of uncertainty was observed in Fig. 10(d), where two
Pre-Ictal classes were incorrectly labelled as Ictal. However,
the onset and cessation timesteps of each event was clearly
detected, demonstrating the models ability to detect convulsive
movements during the ictal phase.

Fig. 11 presents the results of our experiments classifying low-
amplitude signals indicative of an Aura or Focal seizure. The
signal data for these events are more challenging to distinguish
compared to the high-amplitude movements compounded by
the elevated heart rate observed in the ictal phase. Convulsive
movements are indicative of rapid ﬂuctuations that traverse a
signiﬁcant distance in terms of vector magnitude, whereas Pre-
Ictal events are often characterised by sequential timesteps with
minimal or near-zero movement.

In Fig. 11(a) and (b), the pre-ictal phase is marked by
low-intensity signals with sudden spikes in acceleration. In
Fig. 11(a), the proposed model classiﬁed the event, accurately
predicting 87% (13/15) of the timesteps that showed acceleration
waveform ﬂuctuations in acceleration, compounded by elevated
heart rate readings. However, the model did not label any seizure
activity between 15s and 35s and 40s - 60s, due to the minimal
variation in movements and reoccurring decline in heart rate
between 84 - 78,/m. In Fig. 11(b), the model detected 80%
(16/20) of the timesteps. However, at 50s to 70s, we can see
that the acceleration and heart rate waveforms exhibited minimal
ﬂuctuations, indicating an overlap in feature space between the
Normal and Pre-Ictal classes.

Fig. 11(c) highlights the complexities of classifying Pre-Ictal
signals, with the model misclassifying ﬁve timesteps as Ictal
due to sudden acceleration spikes. Despite these challenges,
the data reveals a substantial overlap with the Normal class
at speciﬁc intervals (10s–30s and 55s–65s). Subtle heart rate
elevations further complicate the classiﬁcation process; how-
ever, the model accurately identiﬁed 22 out of 28 timesteps as
either Pre-Ictal or Ictal, highlighting the models ability to detect

Fig. 9. Classiﬁcation results distributed by participant. (a) maps accu-
racy, TPR and TNR, presenting a comprehensive view of classiﬁcation
success and the model’s reliability. (b) illustrates error-related metrics,
measuring the FPR and FNR for each participant.

0.8484 and a low TPR of 0.5555, suggesting challenges in
accurately classifying the Pre-Ictal and Ictal classes for this
participant.

The participants exclusively in the test set exhibited vary-
ing performance, with accuracy scores ranging from 0.5714
to 0.9870. Notably, Participants p83 and p209 achieved high
accuracy scores of 0.9695 and 0.9870, respectively, with TPRs
above 0.9215. Conversely, Participants p55 and p421 exhibited
lower performance, particularly in terms of accuracy and FNR.
For Participant p55, the model recorded an accuracy of 0.5714
and an FNR of 0.4313 (see Fig. 9(b)), highlighting difﬁculties in
classifying the pre-ictal phase, likely due to variability in unseen
seizure manifestations.

Participants whose events were exclusively in the test set had a
lower average accuracy of 0.8412. In contrast, participants who
contributed events to both the training and test sets exhibited
higher accuracy, ranging from 0.9139 to 0.9870, suggesting that
including data from the same participants in both sets improved
the model’s ability to generalise across varying seizure types.
These results underscore the inherent challenges in generalizing
to different events, as events are unique, yet common signal
ﬂuctuations can still be observed across different events for the
same participant (see Fig. 10(a) and (b)). Despite slightly lower
performance scores for test-only participants, it is important to
note that all seizures in the test set were successfully detected,
demonstrating the model’s robustness even when evaluated on
unseen data.

D. Ictal-Phase Detection

This subsection demonstrates the Ictal-Phase Detection tech-
nique on a representative subset of events. Fig. 10 shows the
results of six experiments where each event is labelled as GTC
seizure. The upper x-axis displays the predicted labels, with 0,

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

PORDOY et al.: ENHANCED NON-EEG MULTIMODAL SEIZURE DETECTION: A REAL-WORLD MODEL

3339

Fig. 10. GTC Experiments: The lower x -axis represents time in 5-second intervals (e.g., Timesteps 0s → 10 s represents the timesteps from
0 to 10 seconds). The y-axis denotes the acceleration (left) and heart rate (right) signals which are measured in milli-g and beats per minute
respectively. The upper x-axis shows the predicted class labels for each timestep, where 0, 1, and 2 correspond to Normal (white), Pre-Ictal (blue),
and Ictal (green) phases. The clinically annotated ground truth labels are provided as sub-captions for each ﬁgure, deﬁning the timesteps that start
and end each phase where s = seconds, N = Normal, PI = Pre-Ictal, and I = Ictal.

Fig. 11. Aura/Focal Seizure Experiments: For a full description of the experiments, annotations and class labels see the caption in Fig. 10.

seizure-related timesteps. In Fig. 11(d), high-amplitude Pre-Ictal
movements exceeding 2000 milli-g coincide with a 25% heart
rate increase that gradually returns to a baseline. However, some
low-amplitude signals in later phases went undetected due to
minimal ﬂuctuations. These plots highlight the challenges we
encountered when classifying the Pre-Ictal class. This is because

the model must account for the broad spectrum of normal, non-
epileptic movements, while addressing the variability inherent
in the different types of Auras and myoclonic movements and
heart rate ﬂuctuations that precede the ictal phase.

Fig. 12 illustrates several experiments conducted on events
labelled as Other Seizure. The structure of these acceleration

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

3340

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 5, MAY 2025

Fig. 12. Other Seizure Experiments: For a full description of the experiments, annotations and class labels see the caption in Fig. 10.

waveforms differs from those shown in Fig. 10. In most instances
of the Other Seizure class, there is minimal low-amplitude
indicative of the pre-ictal phase seen in other
movement
generalised events. Furthermore, these seizures exhibit higher
intensity compared to those analysed in Fig. 10, where the
maximum acceleration peaked at approximately 3000 milli-g.
However, in Fig. 12(a) and (b) acceleration exceeds 4000 milli-g,
while in Fig. 12(c) and (d) the acceleration waveforms exceed
6000 milli-g, representing a doubling of intensity compared
to Fig. 10. There are also notable heart rate ﬂuctuations in
Fig. 12 where each plot exceeds 100 beats per minute, with a
notable increase occurring at the time of onset, continuing until
cessation. Overall the proposed model accurately detected the
ictal phase in Fig. 12, approximately detecting 91.6% (11/12),
81.81% (9/11), 73.33% (10/14) and 90.91% (10/11) of Ictal
timesteps for Fig. 12(a)–(d) respectively.

V. DISCUSSION

In this section, we discuss our investigation into Ictal-Phase
Detection, a non-EEG technique designed to distinguish the dif-
ferent phases of the ictal state when detecting epileptic seizures.
We hypothesised that high-amplitude convulsive movements,
characteristic of the ictal phase, can be differentiated from
low-amplitude myoclonic movements indicative of the pre-ictal
phase. To the best of our knowledge, this study is the ﬁrst to
investigate the viability of non-EEG multimodal data to detect
these distinct phases, offering a novel approach for seizure mon-
itoring and detection. To address the challenges in distinguishing
between Normal, Pre-Ictal, and Ictal classes, we introduced a
new model (AMBER) that constructs independent branches for
each modality, generating attention weights that fuse extracted
features into a single representation to enhance feature extraction
and propagation.

The results of our experiments underscore the effectiveness
of our model, achieving an accuracy score of 0.9027 and ef-
fectively distinguishing between different phases of the ictal
state. With Cohen’s Kappa and MCC scores of 0.8498 and
0.8519, respectively, demonstrating strong agreement between
the predicted and ground-truth labels, highlighting consistent

generalisation across positive and negative classes. The high
TNR of 0.9497 reﬂects the model’s ability to accurately detect
non-seizure timesteps, while an average TPR of 0.8981 conﬁrms
its effectiveness in detecting seizures. A slight bias toward
speciﬁcity is observed, with a marginally lower TPR for the
Normal class compared to its TNR. The PPV range of 0.8037
to 0.9652 indicates high conﬁdence in positive classiﬁcations,
although a FNR of 0.1018 indicates some seizure timesteps are
occasionally missed. The model’s trade-off between a high TNR
and moderate FNR indicates a preference for minimising FPs
over FNs.

From our analysis of GTC events, we recorded approximately
91% of timesteps where seizure onset and cessation occurred
(see Fig. 10(a), (b) and (d)). Moreover, in events classiﬁed
as Other, the model accurately identiﬁed 89% of the speciﬁc
timesteps marking the onset of seizure activity. These results
highlight the model’s ability to detect low-amplitude movement
followed by a sudden spikes indicative of the generalised activity
seen in the ictal phase (see Fig. 12(b) and (c)).

To assess the model’s performance on individual participants,
we conducted a participant-level analysis. The model achieved
an average accuracy score of 0.8874 across the 10 participants,
with notable variability in performance. Participants p8, p39, and
p144 demonstrated high accuracy scores of 0.9828, 0.9139, and
0.9762, respectively, indicating effective generalisation for these
subjects. In contrast, participants p55 and p421 showed lower
accuracy, particularly with higher FNRs in Pre-Ictal class. For
p55, the accuracy dropped to 0.5714, highlighting the challenges
in capturing unique seizure manifestations not observed in the
training data. Notably, participants who contributed events to
both the training and testing subsets, such as p8, p39, p45 and
p209, exhibited higher accuracy scores ranging from 0.9139 to
0.9870. This suggests that while seizure events are unique to each
participant, they share common characteristics across different
manifestations, facilitating better generalisation when the model
is exposed to a variety of events from the same participant.

An important observation from our analysis was the notice-
able increase in cardiac manifestations during the pre-ictal and
ictal phases, particularly in seizures categorised as Other. This
trend highlights the potential link between cardiac activity and

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

PORDOY et al.: ENHANCED NON-EEG MULTIMODAL SEIZURE DETECTION: A REAL-WORLD MODEL

3341

seizure progression. Consistent with existing literature [36],
[37], ictal-tachycardia manifestations were observed prior to
seizure onset in a signiﬁcant portion of the events. Of the 94
events used in this study, 36.18% (N = 34/94) exhibited ictal
tachycardia manifestations, characterised by a heart rate increase
exceeding 100 beats per minute. While only one event labelled as
Aura exceeded the ictal tachycardia threshold, this number rose
to 10 for GTC and 23 for seizures denoted as Other. Across these
events, a consistent heart rate increase of approximately 10%
was observed, starting from seizure onset, lasting roughly 15–20
seconds, and returning to baseline once clonic activity ceased.
This observation underscores the potential of heart rate as a re-
liable secondary biomarker for multimodal seizure detection. In
contrast, Aura events, characterised by low-amplitude pre-ictal
activity, showed this response less frequently. However, ictal
tachycardia manifestations were more prevalent in seizures with
distinct heart rate changes during the ictal phase, particularly for
events categorised as GTC and other.

A. Summary

In summary, the observed uncertainty in the pre-ictal phase
could be attributed to the broad range of movements encom-
passed by this class. Challenges arose in distinguishing high-
amplitude normal movements from low-amplitude pre-ictal
movements, as well as high-amplitude pre-ictal movements
from low-amplitude ictal movements. This overlap introduced a
degree of uncertainty when classifying the Pre-Ictal class, further
compounded by the Normal class, which included both post-ictal
and everyday (inter-ictal) movements. However, despite these
challenges, the model demonstrated proﬁciency in detecting
generalized events preceding seizure onset through the identiﬁ-
cation of the Pre-Ictal class. Rather than predicting a seizure at
the ﬁrst sign of high-amplitude movement, our model assessed
whether the analysed signal is indicative of high amplitude or
low amplitude movement. This, combined with a multimodal
approach that leverages heart rate readings, presents a robust
seizure detection technique that has real-world application.

It should be noted that traditional studies in existing literature
measure performance based on whether an event is detected.
In contrast, our approach focuses on classifying each 5-second
timestep, calculating the overall performance score based on
the models ability to classify three distinct classes: Normal,
Pre-Ictal, and Ictal. We feel this technique enhances diagnos-
tic accuracy by improving the detection of generalised onset
seizures and enabling the early identiﬁcation of pre-seizure
states, offering a more reliable method for seizure detection in
real-world environments.

B. Limitations and Future Work

While our study provides valuable insights, several limitations
should be considered. A key challenge was using a single class
label (Normal) to represent common human movements during
the inter-ictal and post-ictal phases. This decision, inﬂuenced by
previous work such as Abdulhay et al. [39], proved restrictive in
the context of non-EEG detection. The variability of movements
in these phases is considerable, making a single label insufﬁcient
to capture this diversity. Future work will expand the number of
input classes to reduce uncertainty between Normal and Pre-
Ictal classes. Incorporating a range of human activities, such as
lying down, walking, or brushing teeth, could improve phase-
speciﬁc classiﬁcation by capturing subtle variations in baseline

movements and isolating seizure-related signals. This approach
aims to enhance both the speciﬁcity and sensitivity of the model
in identifying distinct movement patterns characteristic of the
ictal state.

A further limitation was encountered during the annotation of
the non-EEG data due to the lack of established methodologies
for segmenting and quantifying timesteps across events. De-
veloping an appropriate technique required close collaboration
between our technical and clinical teams, as no clear benchmarks
were available for this process. Reaching a consensus on the
annotation proved time-consuming, highlighting the complexity
of the task. Future work could focus on developing standardised
annotation techniques for labelling non-EEG data, which would
streamline the process and improve the reliability of event clas-
siﬁcation.

VI. CONCLUSION

In summary, this study has made advancements in non-EEG
seizure detection through the introduction of the Ictal-Phase
Detection technique. By applying a multimodal approach that
combined acceleration and heart rate data, we highlighted the po-
tential of cardiac manifestations as biomarkers and demonstrated
how high-amplitude and low-amplitude movements, indicative
of the pre-ictal and ictal phases, can be distinguished. Our
Proposed model demonstrated high performance, with an overall
accuracy of 0.9027, clearly distinguishing between seizure and
non-seizure states. We believe this approach has the potential to
reduce the number of FPs and enable future detection method-
ologies to identify different types of convulsive movement. In
conclusion, this study contributes a new detection technique
and model designed for multimodal seizure detection and lays
the groundwork for further advancements in non-EEG seizure
detection.

We are committed to advancing this research and promoting
collaboration within the ﬁeld by ensuring the accessibility of
our ﬁndings. To further support the development of non-EEG
seizure detection, we are dedicated to sharing the results, model
and annotated dataset from this study.

ACKNOWLEDGMENT

We extend our sincere gratitude to Open Seizure Detector
for providing early access to the Open Seizure Database. Their
dedication to open research will greatly enhance the progress
of non-EEG seizure detection research. We acknowledge and
commend their unwavering support and commitment to advanc-
ing scientiﬁc exploration and knowledge within the epilepsy
community. We also wish to express our appreciation to the par-
ticipants of the Open Seizure Database. Without their dedication
and commitment, this research would not have been possible.

AVAILABILITY OF DATA AND MATERIALS

We are committed to advancing non-EEG detection research
and are pleased to announce the availability of our study’s
results, dataset, and code base. The AMBER model is now
distributed under the MIT license as open-source [41]. We
welcome technical contributions aimed at enhancing the model’s
performance and extending its application in non-EEG seizure
detection. The full code base and annotated dataset for this
project are available at GitHub [42].

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply. 

3342

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 5, MAY 2025

REFERENCES

[1] E. Beghi, G. Giussani, and J. W. Sander, “The natural history and prognosis
of epilepsy,” Epileptic Disorders: Int. Epilepsy J. With Videotape, vol. 17,
no. 3, pp. 243–253, Sep. 2015.

[2] H. Anwar, Q. U. Khan, N. Nadeem, I. Pervaiz, M. Ali, and F. F. Cheema,
“Epileptic seizures,” Discoveries, vol. 8, no. 2, Jun. 2020, Art. no. e110.
[3] S. T. Sarmast, A. M. Abdullahi, and N. Jahan, “Current classiﬁcation of
seizures and epilepsies: Scope, limitations and recommendations for future
action,” Cureus, vol. 12, no. 9, Sep. 2020, Art. no. e10549.

[4] A. Kumar et al., “Simple Partial Seizure,” in StatPearls, Treasure Island,
FL, USA: StatPearls Publishing, Jul. 2020. Accessed: Sep. 15, 2022.
[Online]. Available: https://www.ncbi.nlm.nih.gov/books/NBK500005/

[5] C. DeGiorgio, A. Curtis, D. Hertling, and B. Moseley, “Sudden unexpected
death in epilepsy: Risk factors, biomarkers and prevention,” Acta Neuro-
logica Scandinavica, vol. 139, no. 11, Dec. 2018, doi: 10.1111/ane.13049.
[6] O. Sveinsson, T. Andersson, P. Mattsson, S. Carlsson, and T. Tomson,
“Clinical risk factors in SUDEP: A nationwide population-based case-
control study,” Neurology, vol. 94, no. 4, pp. e419–e429, Jan. 2020,
doi: 10.1212/WNL.0000000000008741.

[7] R. Friedman and J. Kazl, “Seizure detection and SUDEP prevention,”
Bryn Mawr Commun., Nov. 2018. Accessed: Dec. 19, 2022. [On-
line]. Available: https://practicalneurology.com/articles/2018-nov-dec/
seizuredetection-and-sudep-prevention

[8] R. M. J. Cook et al., “Prediction of seizure likelihood with a long-term, im-
planted seizure advisory system in patients with drug-resistant epilepsy: A
ﬁrst-in-man study,” Lancet Neurol., vol. 12, no. 6, pp. 563–571, Jun. 2013,
doi: 10.1016/S1474-4422(13)70075-9.

[9] R. J. Lamberts, R. D. Thijs, A. Laffan, Y. Langan, and J. W. Sander,
“Sudden unexpected death in epilepsy: People with nocturnal seizures
may be at highest risk,” Epilepsia, vol. 53, no. 2, pp. 253–257, Feb. 2012,
doi: 10.1111/j.1528-1167.2011.03360.x.

[10] M. Dümpelmann, “Early seizure detection for closed loop direct neu-
rostimulation devices in epilepsy,” J. Neural Eng., vol. 16, no. 4,
Aug. 2019, Art. no. 041001, doi: 10.1088/1741-2552/ab094a.

[11] S. Beniczky, T. Polster, T. W. Kjaer, and H. Hjalgrim, “Detection of
generalised tonic-clonic seizures by a wireless wrist accelerometer: A
prospective, multicenter study,” Epilepsia, vol. 54, no. 4, pp. e58–61,
Apr. 2013, doi: 10.1111/epi.12120.

[12] K. Cuppens et al., “Accelerometry-based home monitoring for detection
of nocturnal hypermotor seizures based on novelty detection,” IEEE J.
Biomed. Health Informat., vol. 18, no. 3, pp. 1026–1033, May 2014,
doi: 10.1109/JBHI.2013.2285015.

[13] J. Lockman, R. S. Fisher, and D. M. Olson, “Detection of seizure-like
movements using a wrist accelerometer,” Epilepsy Behavior: EB, vol. 20,
no. 4, pp. 638–641, Apr. 2011, doi: 10.1016/j.yebeh.2011.01.019.
[14] J. Pordoy, Y. Zhang, N. Matoorian, and M. Zolgharni, “Predicting epileptic
seizures with a stacked long short-term memory network,” Int. J. Automat.
Artif. Intell. Mach. Learn., vol. 1, no. 1, pp. 93–108, Oct. 2020.

[15] S. Zia, A. N. Khan, M. Mukhtar, S. E. Ali, J. Shahid, and M. Sohail,
“Detection of motor seizures and falls in mobile application using machine
learning classiﬁers,” in Proc. IEEE Int. Conf. Artif. Intell., Commun.
Technol., Jul. 2020, pp. 62–68, doi: 10.1109/IAICT50021.2020.9172028.
[16] P. Vergara, J. Villar, E. Marín, M. M. González, and J. Sedano, “Pre-clinical
study on the detection of simulated epileptic seizures,” Int. J. Uncertainty,
Fuzziness Knowl.-Based Syst., vol. 24, no. 6, pp. 33–46, Dec. 2016,
doi: 10.1142/S0218488516400092.

[17] I. Conradsen, S. Beniczky, P. Wolf, T. W. Kjaer, T. Sams, and H. B. D.
Sorensen, “Automatic multi-modal intelligent seizure acquisition (MISA)
system for detection of motor seizures from electromyographic data and
motion data,” Comput. Methods Programs Biomed., vol. 107, no. 2,
pp. 97–110, Aug. 2012, doi: 10.1016/j.cmpb.2011.06.005.

[18] G.-Q. Zhang, L. Cui, S. Lhatoo, S. U. Schuele, and S. S. Sahoo, “MEDCIS:
Multi-modality epilepsy data capture and integration system,” in Proc.
AMIA Annu. Symp. Proc., 2014, pp. 1248–1257.

[19] J. Wagenaar, G. Worrell, Z. Ives, M. Dümpelmann, B. Litt, and A.
Schulze-Bonhage, “Collaborating and sharing data in epilepsy research,”
J. Clin. Neurophysiol. Publ. Am Electroencephalogr. Soc., vol. 32, no. 3,
pp. 235–239, Jun. 2015.

[20] J. C. Sackellares et al., “Predictability analysis for an automated seizure
prediction algorithm,” J. Clin. Neuriophysiol., vol. 23, no. 6, Dec. 2006,
Art. no. 509.

[21] V. Zeljkovi´c, V. Valev, C. Tameze, and M. Bojic, “Pre-ictal-phase
detection algorithm based on one-dimensional EEG signals and two-
dimensional formed images analysis,” in Proc. 2013 IEEE Int. Conf.
High Perform. Comput. Simul., Jul. 2013, pp. 607–614, doi: 10.1109/HPC-
Sim.2013.6641477.

[22] A. Eftekhar, W. Juffali, J. El-Imad, T. G. Constandinou, and C. Toumazou,
“Ngram-derived pattern recognition for the detection and prediction of
epileptic seizures,” PLoS One, vol. 9, no. 6, Jun. 2014, Art. no. e96235,
doi: 10.1371/journal.pone.0096235.

[23] B. Sharif and A. H. Jafari, “Prediction of epileptic seizures from EEG using
analysis of ictal rules on poincaré plane,” Comput. Methods Programs
Biomed., vol. 145, pp. 11–22, Jul. 2017, doi: 10.1016/j.cmpb.2017.04.001.
[24] R. D. Thijs, P. Ryvlin, and R. Surges, “Autonomic manifes-
tations of epilepsy: Emerging pathways to sudden death?,” Na-
ture Rev. Neurol., vol. 17, no. 12, pp. 774–788, Dec. 2021,
doi: 10.1038/s41582-021-00574-w.

[25] The Open Seizure Database
Hartlepool, U.K., 2022.
OpenSeizureDetector/OpenSeizureDatabase

(OSDB), Open Seizure Detector,
[Online]. Available: https://github.com/

[26] Open Seizure Detector, Open Seizure Detector, Hartlepool, U.K., 2013.

[Online]. Available: https://www.openseizuredetector.org.uk

[27] University of West London, University of West London, London, U.K.,

2022. [Online]. Available: https://www.uwl.ac.uk

seizure

detection,”

[28] J. Pordoy, “The open seizure database facilitating research into
https:

non-eeg
//www.techrxiv.org/articles/preprint/The_Open_Seizure_Database_
Facilitating_Research_Into_Non-EEG_Seizure_Detection/23957625
[29] E. Coto and A. Zissermann, “VGG image classiﬁcation (VIC) engine,”
Version: X. Y. Z., 2017, Accessed: Aug. 31, 2023. [Online]. Available:
http://www.robots.ox.ac.uk/vgg/software/vic/

[Online]. Available:

2023.

[30] L. Vilella et al., “Association of peri-ictal brainstem posturing with
seizure severity and breathing compromise in patients with generalised
convulsive seizures,” Neurology, vol. 96, no. 3, pp. e352–e365, Jan. 2021,
doi: 10.1212/WNL.00000000000112.

[31] A. Ullah, S. U. Rehman, S. Tu, R. M. Mehmood, Fawad, and M.
Ehatisham-ul-haq, “A hybrid deep CNN model for abnormal arrhythmia
detection based on cardiac ECG signal,” Sensors, vol. 21, no. 3, Feb. 2021,
Art. no. 951, doi: 10.3390/s21030951.

[32] G. Jana, R. Sharma, and A. Agrawal, “A 1D-CNN-Spectrogram based
approach for seizure detection from EEG signal,” Procedia Comput. Sci.,
vol. 167, pp. 403–412, 2020, doi: 10.1016/j.procs.2020.03.248.

[33] J. Zhang, Y. Zeng, and B. Starly, “Recurrent neural networks with
long term temporal dependencies in machine tool wear diagnosis and
prognosis,” SN Appl. Sci., vol. 3, no. 4, Mar. 2021, Art. no. 442,
doi: 10.1007/s42452-021-04427-5.

[34] J. Raitoharju, “Convolutional neural networks,” in Deep Learning for
Robot Perception and Cognition, vol. 3, 1st ed. Cambridge, MA, USA:
Academic Press, 2022, pp. 35–69.

[35] A. Ghatak, “Optimization,” in Deep Learning With R, vol. 1, 1st ed., Sin-
gapore: Springer, 2022, pp. 103–147, doi: 10.1007/978-981-13-5850-0_5.
[36] W. Chen, C. L. Guo, and P. S. Zhang, “Heart rate changes in partial seizures:
Analysis of inﬂuencing factors among refractory patients,” BMC Neurol.,
vol. 14, no. 153, pp. 1–10, Jun. 2014, doi: 10.1186/1471-2377-14-135.

[37] S. S. Allana, H. N. Ahmed, K. Shah, and A. F. Kelly, “Ictal brady-
cardia and atrioventricular block: A cardiac manifestation of epilepsy,”
Oxford Med. Case Rep., vol. 2014, no. 2, pp. 33–35, May 2014,
doi.org/10.1093/omcr/omu015.

[38] K. S. Pedersen et al., “Leukocyte DNA methylation signature differentiates
pancreatic cancer patients from healthy controls,” PLoS One, vol. 6, no. 3,
Mar. 2011, Art. no. e18223, doi: 10.1371/journal.pone.0018223.

[39] E. Abdulhay, M. Alafeef, A. Abdelhay, and A. Al-Bashir, “Classiﬁcation
of normal, ictal and inter-ictal EEG via direct quadrature and random forest
tree,” J. Med. Biol. Eng., vol. 37, no. 6, pp. 843–857, Jun. 2017.

[40] A. M. Khalil et al., “Real-time system prediction for heart rate using
deep learning and stream processing platforms,” Complexity, vol. 2021,
Feb. 2021, Art. no. 5535734.

[41] AMBER” GitHub, 2024. [Online] Available: https://github.com/jpordoy/

AMBER

[42] J.

Pordoy,

“Epilepsy
repository.” Accessed:
Jan. 30, 2025.
//github.com/jpordoy/Epilepsy-Ictal-Phase-Detection-Dataset/tree/
Ictal_Phase_Detection_Dataset/Sample_Events

dataset, GitHub
detection
[Online]. Available: https:

phase

Ictal

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:56 UTC from IEEE Xplore.  Restrictions apply.
