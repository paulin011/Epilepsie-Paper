# Pavei et al. - 2017 - Early Seizure Detection Based on Cardiac Autonomic Regulation Dynamics

METHODS
published: 05 October 2017
doi: 10.3389/fphys.2017.00765

Early Seizure Detection Based on
Cardiac Autonomic Regulation
Dynamics

Jonatas Pavei 1*, Renan G. Heinzen 1, Barbora Novakova 2, Roger Walz 3, Andrey J. Serra 4,
Markus Reuber 2, Athi Ponnusamy 2 and Jefferson L. B. Marques 1

1 Department of Electrical and Electronic Engineering, Institute of Biomedical Engineering, Federal University of Santa
Catarina, Florianópolis, Brazil, 2 Department of Neurology and Clinical Neurophysiology, Royal Hallamshire Hospital, Shefﬁeld
Teaching Hospitals NHS Foundation Trust, University of Shefﬁeld, Shefﬁeld, United Kingdom, 3 Neurology Unit, Department of
Clinical Medicine, Federal University of Santa Catarina, Florianópolis, Brazil, 4 Biophotonic Laboratory, Nove de Julho
University, São Paulo, Brazil

Epilepsy is a neurological disorder that causes changes in the autonomic nervous system.
Heart rate variability (HRV) reﬂects the regulation of cardiac activity and autonomic
nervous system tone. The early detection of epileptic seizures could foster the use of
new treatment approaches. This study presents a new methodology for the prediction of
epileptic seizures using HRV signals. Eigendecomposition of HRV parameter covariance
matrices was used to create an input for a support vector machine (SVM)-based
classiﬁer. We analyzed clinical data from 12 patients (9 female; 3 male; age 34.5 ± 7.5
years), involving 34 seizures and a total of 55.2 h of interictal electrocardiogram (ECG)
recordings. Data from 123.6 h of ECG recordings from healthy subjects were used
to test false positive rate per hour (FP/h) in a completely independent data set. Our
methodological approach allowed the detection of impending seizures from 5 min to
just before the onset of a clinical/electrical seizure with a sensitivity of 94.1%. The FP rate
was 0.49 h−1 in the recordings from patients with epilepsy and 0.19 h−1 in the recordings
from healthy subjects. Our results suggest that it is feasible to use the dynamics of HRV
parameters for the early detection and, potentially, the prediction of epileptic seizures.

Keywords: electrocardiogram, heart rate variability, epilepsy, epileptic seizure prediction, support vector
machines

1. INTRODUCTION

Epilepsy is a chronic disorder that has a signiﬁcant impact on patients’ quality of life and health
care budgets. The prevalence of epilepsy has been reported to range from 0.5 to 2% in the
general population (Nunes et al., 2011). It is characterized by sudden recurrent and transient
disturbances of perception or behavior resulting from the excessive synchronization of cortical
neuronal networks due to abnormal bursts of electrical discharge in the brain (Tzallas et al., 2012).
One of the most disabling aspects of the disorder is the unpredictability of the seizures.

Although a wide range of drugs and surgical treatments are available, seizures remain
uncontrolled in over 25% of patients (Valderrama et al., 2012). Most epileptic seizures are self-
limiting but they occasionally develop into a potentially life-threatening, more persistent condition
(status epilepticus). Although most seizures, including generalized tonic clonic seizures (GTCS), do
not cause lasting damage to the brain, they are associated with a small risk of death due to cardiac

Edited by:
Ahsan H. Khandoker,
Khalifa University,
United Arab Emirates

Reviewed by:
Mohammad Hasan Imam,
American International
University-Bangladesh, Bangladesh
Steffen Schulz,
Ernst-Abbe-Hochschule Jena,
Germany
Antonio Gambardella,
Magna Græcia University, Italy

*Correspondence:
Jonatas Pavei
jonatas.pavei@posgrad.ufsc.br

Specialty section:
This article was submitted to
Computational Physiology and
Medicine,
a section of the journal
Frontiers in Physiology

Received: 06 May 2017
Accepted: 19 September 2017
Published: 05 October 2017

Citation:
Pavei J, Heinzen RG, Novakova B,
Walz R, Serra AJ, Reuber M,
Ponnusamy A and Marques JLB
(2017) Early Seizure Detection Based
on Cardiac Autonomic Regulation
Dynamics. Front. Physiol. 8:765.
doi: 10.3389/fphys.2017.00765

Frontiers in Physiology | www.frontiersin.org

1

October 2017 | Volume 8 | Article 765

Pavei et al.

Seizure Prediction Based on HRV

or respiratory complications sudden unexpected death in
epilepsy (SUDEP). The SUDEP risk is particularly high in
individuals who sleep on their own and have GTCS during sleep
(Lamberts et al., 2012). Studies have shown that individuals with
epilepsy often remain unaware of their own seizures, especially
the milder seizures and seizures associated with sleep (Hoppe
et al., 2007). Thus, there is a great interest in the development
of reliable tools for early seizure detection, and potentially for
seizure prediction, in order to allow acute intervention or, at least,
to give patients an opportunity to prepare themselves for a seizure
(Carney et al., 2011).
techniques

the detection and prediction of
epileptic seizures involve linear and non-linear processing
of electroencephalographic (EEG) signals, which reﬂect the
electrical activity in the brain (Acharya et al., 2012; Rana et al.,
2012; Duque-Munoz et al., 2014; Hassan et al., 2016; Li et al.,
2016). Some studies have achieved excellent results, with 100%
accuracy for seizure detection (Alam and Bhuiyan, 2013). In
terms of prediction, one of the best techniques achieved a
sensitivity of 97.5% and a false positive rate of 0.27 h−1 (Park
et al., 2011).

Most

for

Previous studies have indicated that the analysis of autonomic
nervous system (ANS) activity may help to identify epileptic
seizures. Information on ANS activity can be obtained through
heart rate variability (HRV) analyses. HRV analyses are based
on the measurement of the time intervals between successive
QRS complexes, which reﬂect the regulation of the heart rate
by the ANS via its sympathetic and parasympathetic control
mechanisms (Ponnusamy et al., 2012). This means that HRV
analyses can be used to provide indirect clues about nervous
system activity.

Therefore, electrocardiographic (ECG) signals have been used
for seizure detection and prediction, based on ECG signals
associated with established seizures. In 2009, one study reported
that this technique had a sensitivity of 85.7% and a speciﬁcity of
84.6% (Malarvili and Mesbah, 2009). Subsequently, Varon et al.
(2014) used ECG signals to achieve a positive predictive value
(PPV) of 86.2% and a sensitivity of 100% for partial seizures, and
a PPV of 84.3% and a sensitivity of 93.1% for generalized seizures.
More recently, researchers described a multivariate statistical
process for epileptic seizure prediction with a sensitivity of 91%
and false positive rate of 0.7 h−1 (Fujiwara et al., 2016).

Although these studies demonstrate that established seizures
can be reliably detected using ECG signals, it remains uncertain
how well HRV-derived parameters could work for the early
detection or prediction of seizures. As diﬀerences between
interictal and preictal HRV parameters have been noted in several
studies (Ponnusamy et al., 2011, 2012; Behbahani et al., 2013;
Pavei et al., 2014), the utility of these diﬀerences was investigated
in the present study.

EEG-based seizure detection algorithms depend on the
detection of speciﬁc ictal EEG patterns. Ictal EEG patterns
diﬀer between epileptic seizure types. Seizures are detected more
reliably by systems involving a larger number of electrodes
attached to the scalp or intracranial electrodes which would need
to be surgically implanted (and would therefore be associated
with risks, such as bleeding or infection). ECG signals are much

more readily accessible and can be picked up reliably using non-
invasive means (such as wristbands or stick-on electrodes). The
ECG signal is also much less complex than EEG signals and
can be interpreted with more limited computational resources.
Heart rate changes associated with seizures are more generic and
have been well-studied previously (Eggleston et al., 2014). In-
loop ECG recording devices based on heart rate changes have
already been in routine clinical use for several years in Vagus
Nerve Stimulators. Therefore, ECG-based seizure detection is
currently more promising that EEG-based approaches (Boon
et al., 2015).

The aim of this study was to explore the feasibility of using
a method for the early detection or forecasting of epileptic
seizures based on a set of HRV parameters, in which the principal
components of the HRV parameter covariance matrix were used
as inputs for a support vector machine (SVM). The feasibility
assessment was carried out with ECG recordings of 34 temporal
lobe epileptic seizures (TLE), 55.2 h of interictal recordings
from patients with TLE, and 123.6 h of recordings from healthy
subjects.

2. MATERIALS AND METHODS

2.1. Subjects
To address the objective of this study (i.e., establishing the
feasibility of seizure detection/forecasting) and to minimize
physiological variability, we focused exclusively on ECG
recordings capturing occurrences of focal seizures from patient
with temporal
lobe epilepsy. Some patients had secondary
generalized seizures, but ECG recordings from this phase of
the seizures are not included as we analyze HRV during the
interictal and preictal phase of the focal seizures for early seizure
detection.
We

clinical
video-electroencephalographic (V-EEG) recordings of seizures in
12 patients (9 female; 3 male; age 34.5 ± 7.5 years) with temporal
lobe epilepsy (see Table 1 for clinical details). All the ECG
recordings were recorded whilst the patients were hospitalized
for inpatient V-EEG monitoring at the Santa Catarina Epilepsy
Center (CEPESC), which is a regional referral center for patients
with refractory epilepsy in the state of Santa Catarina in southern
Brazil.

collected

during

ECG

data

For some of our analyses, we also used ECG data from the
PhysioNet Massachusetts Institute of Technology (MIT)-Beth
Israel Hospital (BIH) Long-Term Database (1 female; 5 male; age
64.5 ± 16.7 years) (Goldberger et al., 2000).

The study was approved by the Ethics Committee of the
Federal University of Santa Catarina, and informed consent was
obtained from all the patients.

2.2. Methodological Framework
Our proposed methodology for the early detection of seizures is
based on the analysis of dynamic changes in HRV parameters and
the detection of diﬀerences between the interictal and preictal
periods. Our approach is based on a framework involving ﬁve
stages, as presented in Figure 1. The next sections present the
details of this framework.

Frontiers in Physiology | www.frontiersin.org

2

October 2017 | Volume 8 | Article 765

Pavei et al.

Seizure Prediction Based on HRV

TABLE 1 | Summary data for the subjects studied.

Patient

Recording type

Gender

Age

Localization of

seizure onset

Type of

seizure

Drugs

P1

P2

P3

P4

P5

P6

P7

P8

P9

P10

P11

P12

Scalp

Scalp

Scalp

Scalp

Scalp

Scalp

Scalp

Intracranial EEG

Intracranial EEG

Intracranial EEG

Intracranial EEG

Intracranial EEG

F

F

F

F

F

M

F

F

M

F

F

M

43

36

40

31

32

51

29

30

33

48

42

30

LTL

LTL

RTL

LTL

LTL

LTL

RTL

RTL

LTL

LTL

LTL

RTL

CP

CP

CP

CP

CP

CP

CP

CP

CP

CP

CP

CP

CBZ 400 mg, RIS 1 mg

CBZ 200 mg, CLB 10 mg

CBZ 200 mg , PB 100 mg

CBZ 200 mg, CLZ 2 mg

CBZ 200 mg, PB 100 mg

CBZ 200 mg, VPA 500 mg

CBZ 200 mg, CLB 20 mg

CBZ 400 mg

CBZ 200 mg, CLB 20 mg

OCBZ 600 mg, PB 100 mg

VPA 500 mg, PB 100 mg

CBZ 200 mg, PB 150 mg

Localization of seizure onset: LTL, left temporal lobe epilepsy; RTL, right temporal lobe epilepsy.
Type of seizure: CP, complex partial.
Drugs: CBZ, carbamazepine; CLB, clobazam; CLZ, Clonazepam; OCBZ, oxcarbazepine; PB, phenobarbital; RIS, risperidone; VPA, valproic acid.

FIGURE 1 | Proposed framework for early seizure detection. The methodology comprises ﬁve stages: the acquisition of an ECG recording from the patient, the HRV
signal extraction from the recording, the linear and non-linear analysis of the HRV time series, the pre-processing of the parameters derived from the HRV analysis,
and the use of a classiﬁer algorithm to identify any preictal states.

2.2.1. ECG Data Recording
The ECG recording is the ﬁrst stage of the methodology. HRV
time series were extracted from these recordings. It was necessary
to collect data in two periods: (1) immediately before seizure
onset (up to 10 min before seizure onset), which was deﬁned as
the preictal period, and (2) the resting period in between seizures
(at least 1 h before or after a seizure), which was deﬁned as the
interictal period.

The ﬁrst indication of the onset of an epileptic seizure may
be detected in diﬀerent ways. For the purposes of this study,
we were keen to identify the earliest seizure-related changes in
behavior, perception, consciousness or EEG and the moment
of transition from the interictal to the ictal phase as precisely
as possible. Bearing in mind that the ﬁrst observable seizure
manifestation could be a subjective symptom only reportable
by the patient, a change in patient’s visible behavior without
prior subjective “warning” or a change in the EEG without
preceding subjective or visible seizure manifestations, we deﬁned
the moment of seizure onset as the earliest of three time-points:
(1) when the patient pressed a button to indicate that they had
begun to experience seizure symptoms (the “button press” refers
to patient’s pressing the seizure alarm button synchronized with

the video-EEG recording software. A button press will insert a
marker in the EEG recording enabling health care professionals
to identify the exact timing of onset of a seizure warning or
aura). In those cases in which a subjective symptom was the ﬁrst
seizure manifestation this would represent the “clinical onset” of
a seizure; (2) at the onset of the ﬁrst seizure-related changes in the
patient’s behavior on video (if there is no initial subjective seizure
warning and the seizure alarm button has not been pressed, the
ﬁrst visible change in a patient’s behavior captured on video or
audio during the video-EEG recording marks the clinical onset
of a seizure; or (3) at the onset of the ﬁrst seizure-related changes
in the EEG recording (in this case the ﬁrst occurrence of an
ictal EEG pattern, i.e., a change to an EEG pattern typically
associated with an epileptic seizure and recognizable by an expert
neurophysiologist marks the “EEG onset” of a seizure).

We collected 34 data segments (10 min per segment)
capturing preictal periods; 47 data segments totaling 7.8 h (10
min per segment) capturing interictal periods, for training; and
47.4 h of HRV recordings of interictal periods, for testing.
We also used a total of 123.6 h of ECG recordings from six
healthy subjects to explore the speciﬁcity of false positive seizure
detections in patients with epilepsy.

Frontiers in Physiology | www.frontiersin.org

3

October 2017 | Volume 8 | Article 765

Pavei et al.

Seizure Prediction Based on HRV

the second stage of

2.2.2. HRV Signal Extraction
The HRV signal extraction is
the
methodology, as described in Figure 1. The approach is based on
the HRV time series. Several parameters are extracted from this
series, processed, and inputted into the classiﬁer. These signals
reﬂect the activity of the ANS, which in turn is aﬀected by the
brain and any seizure related changes in the central nervous
system.

The ﬁrst step in the extraction of the HRV signal was to
identify all R-peaks in each ECG recording. To this end, all
ECG segments were inspected visually to ensure that the whole
sample was artifact-free. The sampling rate used to record the
ECG was identiﬁed (256 or 512 Hz). Based on this sampling rate,
an ECG text ﬁle was converted into a corresponding time series,
which was fed into custom software using the SciPy: Open Source
Scientiﬁc Tools for Python (Millman and Aivazis, 2011). Starting
with the raw signal, a set of ﬁlters was applied to remove low
frequency baseline wander and high frequency artifacts, such as
muscular activity and power line interference (a high-pass and
a low-pass butterworth ﬁlters with order 2). Having completed
this step, a wavelet-based QRS detection algorithm (Kohler et al.,
2002) based on triggering of the R wave detected and computed
all consecutive RR intervals values.

In order to eliminate artifacts and ectopic heartbeats, we used
a custom algorithm designed to detect all HRV points exceeding 3
times the standard deviation of the sample and changing by more
than 30% compared to the previous HRV point. Once identiﬁed,
these points were removed and a cubic spline interpolation
correction method was used to ﬁll the gap in the data thus
created. As corrections methods can change the reliability of the
HRV assessment (Peltola, 2012), only ECG recordings with <2%
ectopic or R waves misdetection instances were included in the
analysis.

The proposed methodology is based on the dynamic
analysis of HRV parameters. HRV parameters were extracted
during multiple periods in each ECG recording (i.e., using an
overlapping sliding observation window). For this purpose, two
variables were deﬁned: the observation window (Wo, the length
of the ECG segment used to extract the HRV parameters, in
seconds) and the step (S, representing the step, in seconds, that
the observation window slides through between the start of one
extraction period and the start of the next). Therefore, there is a
diﬀerent HRV time series for each extraction period. To deﬁne
both variables, the characteristics of the signal to be analyzed
must be considered. For instance, to analyze low-frequency
components, the size of Wo must be large enough to capture the
desired frequency band. Thus, for each HRV parameter, a speciﬁc
Wo was deﬁned.

2.2.3. HRV Analysis
The HRV analysis is the third stage of the methodology. The main
purpose of this stage is to construct a matrix, called a prediction
matrix (X), representing data to be processed and inputted into a
classiﬁer. To produce the prediction matrix, another variable, the
prediction window (Wp), must be deﬁned. This is the duration of
the period analyzed by the classiﬁer. Thus, a prediction matrix is
produced from samples of HRV parameters calculated from the

HRV times series (extracted in the Wo range as described earlier)
for each step in the ECG recording. Each column of X contains
the set of HRV parameters of the HRV time series extracted
during a speciﬁc period. The total number of columns is deﬁned
by Wp and S.

A prediction matrix is deﬁned as follows:

X =

x11 · · · x1n
...
...
. . .
xp1 · · · xpn






∈ ℜp×n,






(1)

where p is the number of HRV parameters and n the number
of samples, with n = Wp
S . The HRV parameters are in turn
calculated from the HRV signal extracted in the Wo range, as
shown in Figure 2.

2.2.3.1. HRV Parameters
Over the last decade, researchers have proposed several analyses
and measures to evaluate HRV (Lotufo et al., 2012; Kranjec et al.,
2014). The methods used in our study were based on linear and
non-linear analyses in the time and frequency domains.

Time domain measures include basic parameters, such as the
mean RR interval. The parameters in the time domain used in
this study were as follows:

SDNN (ms): The standard deviation of all normal RR
intervals (SDNN). This parameter provides information on all
components that contribute to the HRV, and it is very dependent
on the total time used for the HRV analysis. In patients with
epilepsy, the SDNN has a lower value than in healthy subjects
(Ponnusamy et al., 2011, 2012; Lotufo et al., 2012), which is
related to the reduced parasympathetic activity in those with
epilepsy.

RMSSD (ms): The root mean square of the sum of the squared
diﬀerences of successive normal RR intervals (RMSSD). This
parameter reﬂects parasympathetic activity (DeGiorgio et al.,
2010), which is expected to be reduced in patients with epilepsy.
The HRV signal is composed of multiple frequencies that
provide information about sympathetic and parasympathetic
activity. The contributions of diﬀerent frequencies to the total
RR variability are usually separated using a fast Fourier transform
(FFT)-based power spectral density (PSD) analysis. The two main
spectral bands that comprised the signal’s spectrum used in this
work are as follows:

LF: The PSD of the low-frequency range with components
ranging from 0.04 to 0.15 Hz. The LF component is largely related
to sympathetic activity but can also be modiﬁed by vagal activity
(Ponnusamy et al., 2012). Most authors consider LF a measure of
sympathetic activity (Cliﬀord, 2002).

HF: The PSD of the high-frequency range with components
ranging from 0.15 to 0.4 Hz. The HF component is considered a
measure of parasympathetic activity (Cliﬀord, 2002).

The HRV signal has a non-linear nature and the use of linear
techniques may not allow the identiﬁcation of abnormal HRV
patterns. Therefore, non-linear methods have increasingly been
used for HRV signal analyses. In this study, we used the following
two non-linear parameters:

Frontiers in Physiology | www.frontiersin.org

4

October 2017 | Volume 8 | Article 765

Pavei et al.

Seizure Prediction Based on HRV

FIGURE 2 | Relationship between Wo and Wp. RR interval data were extracted from multiple overlapping observation windows of Wo seconds in the ECG recording.
Subsequently, a set of HRV parameters was calculated and inserted into prediction matrix X (which is shown in the shaded area of the overall matrix), with duration
Wp (i.e., the duration of the period analyzed by the classiﬁer). k, the last step of the overlapping observation window slide in a ECG sample; S, step, in seconds, that is
the overlapping observation window slides through between the current extraction period and the start of the next one; Wo, observation window, in seconds, the
length of the ECG segment used to extract the HRV parameters; Wp, prediction window, in seconds, the duration of the period analyzed by the classiﬁer; xp(n), the
pth parameter extracted in the nth sample.

entropy

SampEn:

(SampEn)

and complexity of

sample
is
(Richman and Moorman, 2000),
the quantiﬁcation of
series.

an
The
entropy parameter
the
the
calculation of which allows
In patients
regularity
with epilepsy, marked diﬀerences
in entropy have been
observed between ictal and interictal periods (Ponnusamy
et al., 2011, 2012). Entropy decreases during the ictal
sympathetic
phase
activity.

associated with

increased

probably

time

Lorenz plot: The Lorenz plot

is a non-linear dynamic
technique that can be used to indicate ﬂuctuations in RR
interval time series. This method involves plotting each RR(n)
interval against the subsequent interval, RR(n + 1). In the
resulting chart, the length of the transverse axis (T) reﬂects
the variability of
the heart rate, which is related to the
dominance of the parasympathetic system. The length of the
longitudinal axis (L) reﬂects the general behavior of the HRV
signal due to the inﬂuences of both systems, sympathetic and
parasympathetic. The measures derived from this plot are as
follows:

CSI: The cardiosympathetic index (CSI) is calculated as follows:

CSI =

L
T

.

CVI: The cardiovagal index (CVI) is calculated as follows:

CVI = log[L × T].

(2)

(3)

It has been suggested that these indices provide complementary
information
sympathetic
parasympathetic
contributions to HRV parameters based on spectral analysis
alone (Toichi et al., 1998).

about

and

Lorenz plots have been widely used in HRV analyses of
diﬀerent disease groups (Toichi et al., 1998; Ponnusamy et al.,
2011, 2012). In patients with epilepsy, a reduction in variability is
observed in the ictal period, both qualitatively by observing the
Lorenz plot and quantitatively, as reﬂected by higher CSI values.
More recently, this method has also been used for the detection
of epileptic seizures (Jeppesen et al., 2015).

Frontiers in Physiology | www.frontiersin.org

5

October 2017 | Volume 8 | Article 765

Pavei et al.

Seizure Prediction Based on HRV

In summary, we used seven HRV metrics (SDNN, RMSSD, LF,
HF, SampEn, CSI, and CVI) to construct a matrix X ∈ RP×T for
each recording analyzed.

2.2.4. Pre-processing
The pre-processing is the fourth stage of the methodology. In this
step of the analytic process, we calculated the covariance matrix
of X followed by the eigendecomposition to be inputted into the
classiﬁer. The main aim of this process was to obtain a vector
with information on the principal components at each moment
in time.

A covariance matrix is a square matrix that contains the
variance and covariance associated with several variables. These
are important descriptors that indicate the dispersion of a
distribution. Consider the case in which we have p parameters
from n samples. We deﬁne the covariance matrix Rxx to be a
symmetric p × p matrix with element rij equal to the covariance
between variable i and variable j. Naturally, the ith diagonal
element of this matrix contains the covariance of variable i with
itself, i.e., its variance. Accordingly, the covariance matrix of X
can be obtained as follows:

R =

1
k − 1

k

X
i=1

(cid:0)

Xi − ¯X

Xi − ¯X

(cid:1) (cid:0)

′

(cid:1)

(4)

where k = p. Since we have assumed that there are p parameters,
the rank of matrix R is necessarily p, as long as the parameters
are not correlated. Therefore, the eigendecomposition of matrix
R provides p non-zero eigenvalues and p eigenvectors.

To deﬁne good parameters as inputs for the classiﬁer, we
selected the principal components of X once it was in an
arrangement that best represented the distribution of the data.
Thus, the vector inputted into the classiﬁer was composed of
the largest eigenvalue (λ) plus the eigenvector (v) of the largest
eigenvalue representing the maximum variance of the data. The
vector was deﬁned as follows:

3 = [λ, v1, . . . , vp−1] ∈ ℜp

(5)

where p is the number of parameter types. During these
calculations and for the classiﬁcation process, neither the
signals nor the eigenvalues were normalized but the eigenvector
components were.

2.2.5. Classiﬁer
The use of a classiﬁer is the last stage of the methodology.
According to the scheme shown in Figure 1, in this stage, the
input vector (which was calculated in the pre-processing stage)
is classiﬁed according to whether it is associated with a preictal
or interictal state. We propose the use of supervised machine
learning algorithms for the early detection of seizures based
on changes in the eigenvalues and eigenvectors of the HRV
parameter covariance matrix.

SVM classiﬁers have been widely used in recent research as a
machine learning solution for a highly diverse range of problems.
Applications in the ﬁeld of medicine have yielded several
notable results using ECG recordings (i.e., results regarding ECG

quality estimation and computer-aided morphological analysis)
(Jankowski et al., 2003; Morgado et al., 2015). The pattern
recognition algorithm deals with a convex optimization problem
involving a maximum margin hyperplane separating two classes.
This hyperplane depends on a subset of training patterns called
support vectors (Schölkopf and Smola, 2002).

Using a similarity function, it is possible to map the data
onto a higher-dimensional space and then apply the hyperplane
strategy. For this application, the Gaussian kernel was employed,
as deﬁned by the following equation:

k(u, v) = exp(−

ku − vk2
γ

),

(6)

where u is the input sample, v is the landmark deﬁned by the
training set, and k.k represents the Euclidean distance operator
(Schölkopf and Smola, 2002). Thus, the main aim was focused on
the standard classiﬁcation problem that consists of constructing
a classiﬁer to distinguish between two disjointed sets of points in
a Euclidean space.

For

this purpose,

two important parameters must be
considered. The penalty parameter (C), which controls model
overﬁtting, and the parameter gamma (γ ), which controls
the model’s degree of nonlinearity. To obtain the optimum
classiﬁcation performance, it was necessary to ﬁnd the best
combination of these parameters based on training accuracy as
described in the next section.

A major advantage of using SVM for distinguishing between
interictal and preictal periods is its robustness regarding diﬀerent
types of interictal patterns.

2.3. Training Process
The training process involved structuring a model that had
received parameter matrices from preictal and interictal periods.
To construct, train, and validate the model, three steps were
the prediction matrices; (2)
necessary: (1) constructing all
deﬁning the training setup, and (3) evaluating the performance.

2.3.1. Prediction Matrix Construction
To construct the prediction matrices for training the classiﬁer,
we created an algorithm that extracts HRV features from the
prediction window. The algorithm was deﬁned as follows:

Algorithm 1 Prediction matrix construction

1: t = actualTime − Wo − Wp
2: while actualTime ≥ t do
3:

4:

5:

6:

window ← data from t to t + S
Extract RR intervals from window
Compute HRV parameters
Fill prediction matrix with a column of p parameters
t ← t +S

7:
8: end while

Importantly, the actualTime variable was deﬁned as an instant
in which we know an event of interest is occurring or about to
occur, i.e., interictal or preictal periods in this case. Therefore, we

Frontiers in Physiology | www.frontiersin.org

6

October 2017 | Volume 8 | Article 765

Pavei et al.

Seizure Prediction Based on HRV

TABLE 2 | Wo values for each HRV parameter.

HRV parameter

SDNN

RMSSD

LF

HF

SampEn

CSI

CVI

Wo value (s)

60

60

180

180

60

60

60

index; CSI, cardiosympathetic index; HF, high frequency; LF,

low
CVI, cardiovagal
frequency; RMSSD, root mean square of the sum of the squared differences of successive
normal RR intervals; SampEn, sample entropy; SDNN, standard deviation of all normal RR
intervals.

applied a causal signal analysis (Allen and Mills, 2004) with the
point of interest based on actualTime (i.e, the output was always
computed from present and past inputs).

In this process, the observation window acts as a circular
buﬀer, meaning that for each step S the window removes data
from the oldest S seconds and adds data from the next S seconds.

2.3.2. Training Setup
Due to the limited availability of data (i.e., only data on 34
seizures were used), we used a leave-one-out cross-validation
(LOOCV) approach to derive a more accurate estimate of model
prediction performance.

Training data were generated and separated as follows:

1. We initially selected 33 samples of preictal data for training
and one sample of preictal data for test purposes. The training
process was repeated 34 times as part of the cross-validation
process.

2. Interictal training samples were generated using randomly
chosen intervals from the periods when no seizure had
occurred 1 h before or after the sample period. A total of
47 interictal HRV matrices were extracted to make up the
training set, totaling 7.8 h of data. The training process also
was repeated 47 times as part of the cross-validation process.

We calculated a set of prediction matrices based on the
recordings before seizure onset in order to train the classiﬁer to
categorize the input as being associated with the preictal period.
These matrices were constructed based on a Wp = 60 s and S =
10 s, representing 6 columns of HRV parameters that preceded
the moment of interest (i.e., seizure onset). For each value in each
column, Wo seconds of HRV data were selected to extract the
HRV parameters in order to construct the matrix. A Wo value
was deﬁned for each parameter, as shown in Table 2. Thus, each
prediction matrix represents a moment in the signal involving
causal data.

The dimension of these matrices was 7 × 6, as deﬁned in
Equation (1). Each X was used to calculate a vector (3), which
was used in the early detection and prediction model.

To deﬁne the best combination of SVM parameters (C and
γ ), each combination was checked using the cross-validation
approach and the parameters with the best cross-validation
accuracy were selected.

2.3.3. Evaluation of Early Detection Performance
The most commonly used performance measures to evaluate
an early detection or prediction model are sensitivity and false
positive rate. In seizure prediction studies, a seizure is considered

to have been predicted correctly if there is at least one warning
within the preceding prediction horizon (Wang et al., 2013). In
this study, the sensitivity was calculated based on the prediction
of seizures from 5 min before to just before seizure onset. This
prediction horizon was deﬁned based on the number of true
positives in each minute before seizure onset; the true positive
rate decreased signiﬁcantly for the time periods >5 min before
seizure onset. Furthermore, given the nature of the causal signal
analysis, the sum of Wo, Wp and prediction horizon period can
not be higher than the preictal total period in order to provide
suﬃcient ECG data for analysis.

The LOOCV approach was used to calculate the sensitivity.
Each false positive rate was calculated by applying the model
to the relevant set of samples (based on the ECG recordings
from the interictal periods and healthy subjects). Given previous
results based on the use of EEG and ECG recordings (Park
et al., 2011; Fujiwara et al., 2016), we deﬁned the acceptable false
positive rate as a rate of <0.5 h−1.

3. RESULTS

To assess early epileptic seizure recognition, we used (1) a set of
ECG signals recorded during (and immediately before) at least
one seizure, (2) a set of ECG signals recorded during interictal
periods, with a total length of 55.2 h (7.8 h for training and 47.4 h
for testing), and (3) a set of ECG signals from the MIT-BIH Long-
Term Database with a total length of 123.6 h (Goldberger et al.,
2000).

For each assessment of the methodology, a set of HRV
parameters was calculated using the set of Wo values shown in
Table 2, and S = 10 s, which were determined on the basis of
the particular characteristics of the diﬀerent HRV parameters.
Sympathetic and parasympathetic tone can vary considerably
over a 24-h cycle and can change abruptly in response to external
and internal stimuli, such as fear and pain. Therefore, we used
relatively short observation windows (see Table 2) to minimize
the eﬀects of ANS responses to external inﬂuences that could have
interfered with the analysis of interest.
Figure 3 shows the dynamics of

four HRV parameters
(CVI, CSI, SampEn, and SDNN) in ﬁve signals from one patient.
Four of these signals were associated with seizure onset (and have
been synchronized to the point of seizure onset shown in the
ﬁgure) while one shows the signal during an interictal period.
Note that diﬀerent HRV parameters show similar dynamic
changes around the time of seizure onset while the signals
in the interictal periods do not show any similar changes.
Figure 4 shows the dynamics of the four HRV parameters
from 12 patients. Although there were diﬀerences in patient
characteristics, the dynamic behavior of the HRV parameters was
similar. These stereotypical dynamic changes in HRV parameters
around the time of seizure onset suggest that the parameters
could be useful for the early detection or prediction of epileptic
seizures.

The optimum combination of SVM parameters, C = 4.3 and
γ = 0.5, reached an accuracy of 95.6%. Thus, the results for the
prediction of impending seizures from 5 min before to just before

Frontiers in Physiology | www.frontiersin.org

7

October 2017 | Volume 8 | Article 765

Pavei et al.

Seizure Prediction Based on HRV

FIGURE 3 | Dynamics of HRV parameters. Each panel presents dynamic changes in one particular HRV parameter during four seizures and one interictal period
experienced by the same patient. Clinical/EEG seizure onset is represented by the vertical red lines. Each of the signals associated with seizure-related ﬁndings has
been synchronized to seizure onset. CSI, cardiosympathetic index; CVI, cardiovagal index; SampEn, sample entropy; SDNN, standard deviation of all normal RR
intervals.

FIGURE 4 | Dynamics of HRV parameters. Dynamic changes of four HRV parameters, from 12 patients, with the signals synchronized to seizure onset. Clinical/EEG
seizure onset is represented by the vertical red lines. CVI, cardiovagal index; CSI, cardiosympathetic index; SampEn, sample entropy; SDNN, standard deviation of all
normal RR intervals.

clinical/EEG seizure onset indicated a sensitivity of 94.1%, based
on a detection rate (up to 5 min before onset) of 32 of the 34
seizures. Figure 5 presents the prediction results for four seizures.
The upper two panels show the prediction of seizures of diﬀerent
patients, and the lower two panels are based on recordings from
a third patient. These two panels show that, in one case, accurate
seizure prediction was not achieved.

The false positive rate in the interictal ECG segments was 0.49
false positives (FP)/h. For the data from the MIT-BIH Long-Term
Database, the false positive rate was 0.19 FP/h. Figure 6 shows
four results used to calculate the false positive rate for interictal
periods. All results are summarized in Table 3.

4. DISCUSSION

In this
study, we propose a methodology for the early
detection and prediction of epileptic seizures using HRV signals
only. This method is based on the extraction of a range
of HRV parameters that reﬂect changes in sympathetic and
parasympathetic tone around the onset of epileptic seizures. The
methodology could be used in closed-loop seizure treatment
systems or seizure warning devices. This paper presents a
classiﬁcation approach that combines a linear signal subspace
analysis (i.e., the eigendecomposition of covariance matrices)
with an interpretable machine learning process. The feasibility

Frontiers in Physiology | www.frontiersin.org

8

October 2017 | Volume 8 | Article 765

Pavei et al.

Seizure Prediction Based on HRV

FIGURE 5 | Early detection of seizures. Each chart presents the results of the early detection/prediction model, with positive output (indicating seizure prediction)
highlighted using shading. Clinical/EEG seizure onset is represented by the vertical red lines. The top two panels show successful early prediction/detection of
seizures in two different patients. The bottom panels are from a third patient: the left panel shows a successful seizure detection the right panel an example of a
seizure which was not detected.

FIGURE 6 | False positive rate of seizure prediction. Each chart presents the results of the early detection/prediction model, with positive output (indicating seizure
prediction) highlighted using shading. Each of the graphs show the HRV signal from a different ECG recording of an interictal period.

of implementing the methodology was investigated by ﬁrst
analyzing diﬀerent timepoints prior to seizure onset (to assess
the maximum prediction time that can be achieved with this
methodological conﬁguration) and also by analyzing ECG data
on healthy subjects.

Epilepsy and seizures can have profound eﬀects on both
subdivisions of the ANS, the sympathetic and parasympathetic
systems. ANS is fundamental to homeostasis and including
regulation of heart rate. The parasympathetic output (mediated

by the vagus nerve) and sympathetic output (controlled by
neurons in the rostral medulla) to the heart are modulated by
the central autonomic network. This includes the insular cortex,
orbitofrontal cortex, cingulate, amygdala, hypothalamus and
peri-aqueductal gray matter. The insula and prefrontal cortex are
considered as the key representations of the autonomic nervous
system at the cortical level. Epileptic discharges aﬀecting these
parts of the brain aﬀect the functioning of these components of
the central autonomic network.

Frontiers in Physiology | www.frontiersin.org

9

October 2017 | Volume 8 | Article 765

Pavei et al.

Seizure Prediction Based on HRV

TABLE 3 | Summary of results.

Sensitivity

Accuracy

94.1%

95.6%

FP/ha

0.49

FP/hb

0.19

aFalse positive rate in the interictal ECG segments.
bFalse positive rate in ECG segments from MIT-BIH Long-Term Database.

Heart rate variability can be used as a tool to provide
the autonomic
information about
the functional state of
nervous system. Ictal activation of the ANS can be detected by
analyzing HRV on electrocardiography (Sevcencu and Struijk,
2010) as HRV is a mirror of neuronal
inﬂuences on the
cardiac pacemaker. HRV parameters reﬂect the beat-to-beat
variability of the intrinsic oscillators, which are controlled by the
sympathovagal balance. In this sense, heart rate variability can be
considered as a biomarker of the autonomic dysfunction caused
by seizures. As such the early recognition of such HRV changes
could be clinically useful for the rapid detection and, perhaps,
prediction of impending seizures.

The methodology is based on the observation that HRV
parameters diﬀer signiﬁcantly between interictal, preictal, and
ictal phases. However, to observe the dynamics of these variations
and analyze the preictal changes in the parameters, the HRV
parameters must be calculated continuously. The choice of the
observation and prediction windows is of great importance to
the success of early seizure detection or prediction algorithms.
In addition,
further study is needed on the inﬂuence of
physiological activities that potentially aﬀect HRV parameters,
signal acquisition quality, ectopic heartbeats, seizure type, seizure
focus location, and the patient’s age before the analysis of HRV
parameters can be used in clinical settings for seizure detection or
prediction. This research will require larger prospective studies.

Having said that, the relative ease of ECG acquisition from
patients means that there is considerable clinical interest in
ECG-based seizure detection and warning systems (Osorio and
Manly, 2014). Furthermore, these systems could be made more
eﬀective by using a multimodal monitoring approach that also
incorporates other biological or behavioral signals. ECG-based
algorithms are certainly more practical and convenient than
devices using EEG signals. The high signal-to-noise ratio and ease
of recording favor ECG over EEG-based approaches. In addition,
as about 82% of epileptic seizures are associated with ictal
tachycardia (which often precede ictal EEG changes) (Eggleston
et al., 2014), our proposed method of seizure detection/prediction
based on HRV parameters may be very useful for seizure warning
devices.

Approaches for early detection of seizures based on HRV
parameter dynamics may also be useful for treatment. Vagal
nerve stimulation devices provide safe and eﬀective treatment
for refractory epilepsy. Vagal nerve stimulation is usually
delivered intermittently in an open-loop fashion. Recently, an
automated seizure detection system that uses ictal tachycardia
to trigger vagal nerve stimulation in a closed-loop fashion
was piloted and found to be potentially eﬃcacious for the
management of diﬃcult-to-treat patients with epilepsy (Boon
et al., 2015). Our methodological approach of HRV-derived

seizure detection/prediction may be used in a similar fashion in
closed-loop seizure management devices. It may prove to be a
more responsive and speciﬁc approach than tachycardia-based
approaches.

The use of HRV parameters for the early detection and/or
forecasting of epileptic seizures may facilitate the development
of new devices for continuous monitoring in other applications
that involve time-variant biological signals and applications
associated with closed-loop electroceutical devices. Furthermore,
early detection of epileptic seizures can play a key role in enabling
patients to reach a specialized treatment center promptly and
in optimizing the diagnosis and treatment of epilepsy. Overall,
these factors may be linked to a reduction in mortality rates
and comorbidities (Maguire et al., 2016; Granbichler et al.,
2017).

Despite the high computational cost, we used the LOOCV
approach due to the possibility of training the classiﬁer using
the greatest amount of data in each case, which increases
the probability of producing an accurate classiﬁer (Witten
et al., 2011). However, the high variance associated with this
approach can lead to unreliable estimates. Nevertheless, we
evaluated the false positive rate in an independent dataset and,
furthermore, 32 of the 34 outputs (considering only preictal
periods) were true positive outputs, indicating that the model is
reliable.

in order

Future research will need to include a greater number
to examine the possible eﬀects of
of patients,
clinical characteristics, such as the patient’s age, seizure type,
and,
in particular, HRV parameters. Future studies using
the methodology presented in this study should address the
limitations of the present study, which include the small case
number, the fact that only focal seizures were studied, and
the moderate quantity of interictal ECG recordings analyzed.
There was a diﬀerence in the gender ratios of the patient and
control groups in this study. Although there are indications
of gender diﬀerences between some HRV parameters (Koenig
and Thayer, 2016), these diﬀerences have not been replicated
in studies of patients with epilepsy (Lotufo et al., 2012). What
is more, the most important analyses in the present study
rely on comparisons of ictal and interictal data from the same
patient. Nevertheless, it would be important for conﬁrmatory
future studies to ensure that the observations made here are
not aﬀected by patient’s gender. Furthermore, new HRV-based
approaches, such as non-linear analyses based on chaos theory
could be integrated into the methodology to explore its full
potential for assessing ANS dynamics in multiple physiological
conditions.

5. CONCLUSION

It is feasible to use the dynamics of HRV parameters for
the early detection and, potentially, the prediction of epileptic
seizures. The use of SVM for classifying input according to
whether it is associated with an interictal or preictal period is a
robust technique regarding the classiﬁcation of diﬀerent types
of interictal patterns. We achieved an acceptable (<0.5 FP/h)

Frontiers in Physiology | www.frontiersin.org

10

October 2017 | Volume 8 | Article 765

Pavei et al.

Seizure Prediction Based on HRV

false positive rate of 0.49 FP/h for ECG recordings from all
the interictal periods, with a sensitivity of 94.1% for seizure
prediction based on recordings capturing the period 0–5 min
before seizure onset. For the recordings from the MIT-BIH Long-
Term Database, the false positive rate was 0.19. The results of
this study show that early detection of epileptic seizure is possible
using HRV parameters.

ETHICS STATEMENT

study was

carried out

This
in accordance with the
recommendations of Ethics Committee of the Federal University
from all
of Santa Catarina with written informed consent
in
subjects. All
accordance with the Declaration of Helsinki. The protocol

subjects gave written informed consent

REFERENCES

Acharya, U. R., Molinari, F., Sree, S. V., Chattopadhyay, S., Ng, K.-H., and Suri, J. S.
(2012). Automated diagnosis of epileptic EEG using entropies. Biomed. Signal
Proc. Control 7, 401–408. doi: 10.1016/j.bspc.2011.07.007

Alam, S., and Bhuiyan, M. (2013). Detection of seizure and epilepsy using higher
order statistics in the emd domain. Biomed. Health Inf. IEEE J. 17, 312–318.
doi: 10.1109/JBHI.2012.2237409

Allen, R., and Mills, D. (2004). Signal Analysis: Time, Frequency, Scale, and

Structure. Hoboken, NJ: Wiley.

Behbahani, S., Jafarnia Dabanloo, N., Motie Nasrabadi, A. A., Teixeira, C., and
Dourado, A. (2013). Pre-ictal heart rate variability assessment of epileptic
seizures by means of linear and non-linear analyses. Anatol. J. Cardiol. 13,
797–803. doi: 10.5152/akd.2013.237

Boon, P., Vonck, K., van Rijckevorsel, K., Tahry, R. E., Elger, C. E.,
Mullatti, N., et al. (2015). A prospective, multicenter study of cardiac-based
seizure detection to activate vagus nerve stimulation. Seizure 32, 52–61.
doi: 10.1016/j.seizure.2015.08.011

Carney, P. R., Myers, S., and Geyer, J. D. (2011). Seizure prediction: methods.

Epilepsy Behav. 22(Suppl.1), S94–S101. doi: 10.1016/j.yebeh.2011.09.001

Cliﬀord, G. D. (2002). Signal Processing Methods For Heart Rate Variability

Analysis. PhD Thesis, University of Oxford.

DeGiorgio, C. M., Miller, P., Meymandi, S., Chin, A., Epps, J., Gordon, S., et al.
(2010). Rmssd, a measure of vagus-mediated heart rate variability, is associated
with risk factors for sudep: the sudep-7 inventory. Epilepsy Behav. 19, 78–81.
doi: 10.1016/j.yebeh.2010.06.011
Duque-Munoz, L., Espinosa-Oviedo,

and Castellanos-Dominguez, C.
J.,
(2014). Identiﬁcation and monitoring of brain activity based on stochastic
relevance analysis of short-time eeg rhythms. Biomed. Eng. Online 13:123.
doi: 10.1186/1475-925X-13-123

Eggleston, K. S., Olin, B. D., and Fisher, R. S. (2014). Ictal tachycardia: the
head-heart connection. Seizure 23, 496–505. doi: 10.1016/j.seizure.2014.02.012
Fujiwara, K., Miyajima, M., Yamakawa, T., Abe, E., Suzuki, Y., Sawada, Y., et al.
(2016). Epileptic seizure prediction based on multivariate statistical process
control of heart rate variability features. IEEE Trans. Biomed. Eng. 63, 1321–
1332. doi: 10.1109/TBME.2015.2512276

Goldberger, A. L., Amaral, L. A. N., Glass, L., Hausdorﬀ, J. M., Ivanov, P. C., Mark,
R. G., et al. (2000). Physiobank, physiotoolkit, and physionet. Circulation 101,
e215–e220. doi: 10.1161/01.CIR.101.23.e215

Granbichler, C. A., Oberaigner, W., Kuchukhidze, G., Ndayisaba, J.-P., Ndayisaba,
A., Taylor, A., et al. (2017). Decrease in mortality of adult epilepsy patients since
1980: lessons learned from a hospital-based cohort. Eur. J. Neurol. 24, 667–672.
doi: 10.1111/ene.13267

Hassan, A. R., Siuly, S., and Zhang, Y. (2016). Epileptic seizure detection in eeg
signals using tunable-q factor wavelet transform and bootstrap aggregating.
Comput. Methods Prog. Biomed. 137, 247–259. doi: 10.1016/j.cmpb.2016.09.008

was approved by the Ethics Committee of the Federal University
of Santa Catarina.

AUTHOR CONTRIBUTIONS

JP, RH, BN, RW, MR, AS, AP, and JM participated in the design
of the entire study and helped to draft the manuscript. JP and
RH contributed to the model implementation and simulation and
interpreted the data. All the authors read and approved the ﬁnal
manuscript.

ACKNOWLEDGMENTS

JP and JM thank CNPq, Brazil-DF, for their scholarships and for
supporting this work.

Hoppe, C., Poepel, A., and Elger, C. E. (2007). Epilepsy: accuracy of patient seizure

counts. Arch. Neurol. 64, 1595–1599. doi: 10.1001/archneur.64.11.1595

Jankowski, S., Oreziak, A., Skorupski, A., Kowalski, H., Szymanski, Z., and
Piatkowska-Janko, E. (2003). “Computer-aided morphological analysis of
holter ecg recordings based on support vector learning system,” in Computers in
Cardiology, 2003 (Halkidiki: IEEE), 597–600. doi: 10.1109/CIC.2003.1291226

Jeppesen,

J., Beniczky, S.,

and Fuglsang-
Frederiksen, A. (2015). Detection of epileptic seizures with a modiﬁed
heart rate variability algorithm based on lorenz plot. Seizure 24, 1–7.
doi: 10.1016/j.seizure.2014.11.004

Johansen, P., Sidenius, P.,

Koenig, J., and Thayer, J. F. (2016). Sex diﬀerences in healthy human heart
rate variability: a meta-analysis. Neurosci. Biobehav. Rev. 64, 288–310.
doi: 10.1016/j.neubiorev.2016.03.007

Kohler, B.-U., Hennig, C., and Orglmeister, R. (2002). The principles of software
qrs detection. Eng. Med. Biol. Mag. IEEE 21, 42–57. doi: 10.1109/51.993193
Kranjec, J., Begus, S., Gersak, G., and Drnovsek, J. (2014). Non-contact heart rate
and heart rate variability measurements: a review. Biomed. Signal Proc. Control
13, 102–112. doi: 10.1016/j.bspc.2014.03.004

Lamberts, R. J., Thijs, R. D., Laﬀan, A., Langan, Y., and Sander, J. W. (2012).
Sudden unexpected death in epilepsy: people with nocturnal seizures may
be at highest risk. Epilepsia 53, 253–257. doi: 10.1111/j.1528-1167.2011.
03360.x

Li, P., Karmakar, C., Yan, C., Palaniswami, M., and Liu, C. (2016). Classiﬁcation
of 5-s epileptic eeg recordings using distribution entropy and sample entropy.
Front. Physiol. 7:136. doi: 10.3389/fphys.2016.00136

Lotufo, P. A., Valiengo, L., Benseñor, I. M., and Brunoni, A. R. (2012). A systematic
review and meta-analysis of heart rate variability in epilepsy and antiepileptic
drugs. Epilepsia 53, 272–282. doi: 10.1111/j.1528-1167.2011.03361.x

Maguire, M. J., Jackson, C. F., Marson, A. G., and Nolan, S. J. (2016). Treatments
for the prevention of sudden unexpected death in epilepsy (sudep). Cochrane
Database of Syst. Rev. 7:CD011792. doi: 10.1002/14651858.CD011792.pub2
Malarvili, M., and Mesbah, M. (2009). Newborn seizure detection based
IEEE Trans. 56, 2594–2603.

rate variability. Biomed. Eng.

on heart
doi: 10.1109/TBME.2009.2026908

Millman, K. J., and Aivazis, M. (2011). Python for scientists and engineers.

Comput. Sci. Eng. 13, 9–12. doi: 10.1109/MCSE.2011.36

Morgado, E., Alonso-Atienza, F., Santiago-Mozos, R., Barquero-Pérez, Ó., Silva,
I., Ramos, J. et al. (2015). Quality estimation of the electrocardiogram
using
14:59.
doi: 10.1186/s12938-015-0053-1

leads. Biomed. Eng. Online

cross-correlation among

Nunes,

J. C., Zakon, D. B., Claudino, L. S., Guarnieri, R., Bastos, A.,
Queiroz, L. P., et al. (2011). Hippocampal sclerosis and ipsilateral headache
lobe epilepsy patients. Seizure 20, 480–484.
among mesial
doi: 10.1016/j.seizure.2011.02.014

temporal

Osorio, I., and Manly, B. (2014). Is seizure detection based on EKG clinically
relevant? Clin. Neurophysiol. 125, 1946–1951. doi: 10.1016/j.clinph.2014.01.026

Frontiers in Physiology | www.frontiersin.org

11

October 2017 | Volume 8 | Article 765

Pavei et al.

Seizure Prediction Based on HRV

Park, Y., Luo, L., Parhi, K. K., and Netoﬀ, T. (2011). Seizure prediction with
spectral power of eeg using cost-sensitive support vector machines. Epilepsia
52, 1761–1770. doi: 10.1111/j.1528-1167.2011.03138.x

Pavei, J., Walz, R., and Marques, J. L. B. (2014). “Study of biomarkers for prediction
of epileptic seizures using ECG,” in Proceedings CBEB 2014 XXIV Brazilian
Conference on Biomedical Engineering—CBEB 2014 (Uberlândia), 1677–1680.
Peltola, M. (2012). Role of editing of r-r intervals in the analysis of heart rate

variability. Front. Physiol. 3:148. doi: 10.3389/fphys.2012.00148

Ponnusamy, A., Marques, J. L., and Reuber, M. (2011). Heart rate variability
in patients with psychogenic nonepileptic
685–691.
limitations. Epilepsy Behav.

measures
seizures: Potential
doi: 10.1016/j.yebeh.2011.08.020

as biomarkers
and

22,

Ponnusamy, A., Marques,

J. L., and Reuber, M.

rate variability parameters during complex partial

(2012). Comparison
seizures
1314–1321.

53,

of heart
and
doi: 10.1111/j.1528-1167.2012.03518.x

nonepileptic

psychogenic

seizures.

Epilepsia

Rana, P., Lipor, J., Lee, H., van Drongelen, W., Kohrman, M., and van Veen,
B. (2012). Seizure detection using the phase-slope index and multichannel
ecog. Biomed. Eng. IEEE Trans. 59, 1125–1134. doi: 10.1109/TBME.2012.
2184796

Richman, J. S., and Moorman, J. R. (2000). Physiological time-series analysis using
approximate entropy and sample entropy. Am. J. Physiol. 278, H2039–H2049.
Schölkopf, B., and Smola, A. J. (2002). Learning with Kernels : Support Vector
Machines, Regularization, Optimization, and Beyond. Adaptive Computation
and Machine Learning. Cambridge: MIT Press.

Sevcencu, C., and Struijk, J. J. (2010). Autonomic alterations and cardiac changes

in epilepsy. Epilepsia 51, 725–737. doi: 10.1111/j.1528-1167.2009.02479.x

Toichi, M., Murai, T., Sengoku, A., and Miyoshi, K. (1998). Interictal change
in cardiac autonomic function associated with eeg abnormalities and
clinical symptoms: a longitudinal study following acute deterioration in two
patients with temporal lobe epilepsy. Psychiatry Clin. Neurosci. 52, 499–505.
doi: 10.1046/j.1440-1819.1998.00446.x

Tzallas, A. T., Tsipouras, M. G., Tsalikakis, D. G., Karvounis, E. C., Astrakas,
L., Konitsiotis, S., et al. (2012). “Automated epileptic seizure detection
methods: a review study,” in Epilepsy: Histological, Electroencephalographic
and Psychological Aspects, ed D. Stevanovic (Rijeka:
InTech), 75–97.
doi: 10.5772/31597

Valderrama, M., Alvarado, C., Nikolopoulos, S., Martinerie, J., Adam, C., Navarro,
V., et al. (2012). Identifying an increased risk of epileptic seizures using a
multi-feature eeg-ecg classiﬁcation. Biomed. Signal Proc. Control 7, 237–244.
doi: 10.1016/j.bspc.2011.05.005

Varon, C., Caicedo, A.,

Jansen, K., Lagae, L., and Huﬀel, S. V. (2014).
“Detection of epileptic seizures from single lead ecg by means of phase
rectiﬁed signal averaging,” in 36th Annual International Conference of the
IEEE Engineering in Medicine and Biology Society (Chicago, IL), 3789–3790.
doi: 10.1109/EMBC.2014.6944448

Wang, S., Chaovalitwongse, W., and Wong, S. (2013). Online seizure prediction
using an adaptive learning approach. Knowl. Data Eng. IEEE Trans. 25, 2854–
2866. doi: 10.1109/TKDE.2013.151

Witten, I. H., Frank, E., and Hall, M. A. (2011). Data Mining: Practical Machine
Learning Tools and Techniques, 3rd Edn. San Francisco, CA: Morgan Kaufmann
Publishers Inc.

Conﬂict of Interest Statement: The authors declare that the research was
conducted in the absence of any commercial or ﬁnancial relationships that could
be construed as a potential conﬂict of interest.

Copyright © 2017 Pavei, Heinzen, Novakova, Walz, Serra, Reuber, Ponnusamy and
Marques. This is an open-access article distributed under the terms of the Creative
Commons Attribution License (CC BY). The use, distribution or reproduction in
other forums is permitted, provided the original author(s) or licensor are credited
and that the original publication in this journal is cited, in accordance with accepted
academic practice. No use, distribution or reproduction is permitted which does not
comply with these terms.

Frontiers in Physiology | www.frontiersin.org

12

October 2017 | Volume 8 | Article 765
