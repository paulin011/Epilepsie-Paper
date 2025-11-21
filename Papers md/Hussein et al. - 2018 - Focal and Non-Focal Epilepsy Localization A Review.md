# Hussein et al. - 2018 - Focal and Non-Focal Epilepsy Localization A Review

SPECIAL SECTION ON NEW TRENDS IN BRAIN SIGNAL PROCESSING AND ANALYSIS

Received July 26, 2018, accepted August 22, 2018, date of publication August 24, 2018, date of current version September 28, 2018.

Digital Object Identifier 10.1109/ACCESS.2018.2867078

Focal and Non-Focal Epilepsy
Localization: A Review

AHMED FAEQ HUSSEIN 1, (Member, IEEE), ARUNKUMAR N 2, (Member, IEEE),
CHANDIMA GOMES3, ABBAS K. ALZUBAIDI4, QAIS AHMED HABASH1,
LUZ SANTAMARIA-GRANADOS5,6, JUAN FRANCISCO MENDOZA-MORENO5,6,
AND GUSTAVO RAMIREZ-GONZALEZ 6
1Bio-Medical Engineering Department, Faculty of Engineering, AL-Nahrain University, Baghdad 10072, Iraq
2Department of Electronics and Instrumentation, SASTRA University, Thanjavur 613401, India
3Department of Electrical and Electronics Engineering, Universiti Putra Malaysia, Serdang 43400, Malaysia
4Department of Psychology and Biomedical Engineering, University of Saskatchewan, Saskatoon, SK S7N 5A2, Canada
5Faculty of Systems Engineering, University of Santo Tomás, Tunja 5878797, Colombia
6Telematics Department, University of Cauca, Popayán 190009, Colombia

Corresponding author: Gustavo Ramirez-Gonzalez (gramirez@unicauca.edu.co)

ABSTRACT The focal and non-focal epilepsy is seen to be a chronic neurological brain disorder, which
has affected ≈ 60 million people in the world. Hence, an early detection of the focal epileptic seizures can
be carried out using the EEG signals, which act as a helpful tool for early diagnosis of epilepsy. Several
EEG-based approaches have been proposed and developed to understand the underlying characteristics of
the epileptic seizures. Despite the fact that the early results were positive, the proposed techniques cannot
generate reproducible results and lack a statistical validation, which has led to doubts regarding the presence
of the pre-ictal state. Various methodical and algorithmic studies have indicated that the transition to an
ictal state is not a random process, and the build-up can lead to epileptic seizures. This study reviews many
recently-proposed algorithms for detecting the focal epileptic seizures. Generally, the techniques developed
for detecting the epileptic seizures were based on tensors, entropy, empirical mode decomposition, wavelet
transform and dynamic analysis. The existing algorithms were compared and the need for implementing a
practical and reliable new algorithm is highlighted. The research regarding the epileptic seizure detection
research is more focused on the development of precise and non-invasive techniques for rapid and reliable
diagnosis. Finally, the researchers noted that all the methods that were developed for epileptic seizure
detection lacks standardization, which hinders the homogeneous comparison of the detector performance.

INDEX TERMS Focal epilepsy, non-focal epilepsy, time and frequency domain features, nonlinear features,
machine learning algorithms, EEG signal analysis.

I. INTRODUCTION
Epilepsy is described as the momentary occurrence of symp-
toms as well as signs due to irregular synchronous or exces-
sive neuronal activities in the human brain [1]. Furthermore,
epilepsy is also deﬁned as the long-term predisposition
of the human brain to produce epileptic seizures, which
can lead to psychological, cognitive, neurobiological or
social consequences [1]. The patients are said to suffer
from epilepsy if they encounter any one of these following
conditions: (i) A minimum of 2 unprovoked (or reﬂex)
seizures which occur at least 24 h apart; (ii) An unpro-
voked (or reﬂex) seizure, with a similar seizure recur-
rence risk (≥60%) after the reﬂexed seizures in the next
10 years; and (iii) The interpretation of
the epilepsy
disorder [2].

Several involuntary body movements, involving the entire
body or some body parts can be caused by epilepsy.
These episodes are usually accompanied by a loss of
bladder or bowel control functions. The epileptic seizures
happen due to extreme or abnormal electrical charge distur-
bances within the different parts of the brain. The seizures
also vary from a momentary attention lapse to prolonged
spasms [3]. Partial or focal epileptic seizures primarily affect
one hemisphere of the brain. The human brain comprises of
2 hemispheres, with 4 lobes in every hemisphere, i.e., frontal,
partial, temporal and the occipital lobes. Focal epilepsy can
affect either the complete hemisphere or some lobes in the
hemisphere. The non-focal signals can be detected from
the brain hemispheres which have not been affected by the
epileptic seizures [3]–[6].

49306

2169-3536 
 2018 IEEE. Translations and content mining are permitted for academic research only.
Personal use is also permitted, but republication/redistribution requires IEEE permission.
See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

VOLUME 6, 2018

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

Epilepsy has led to a massive burden on the global
medical system, while the gap between the disease occur-
rence and treatment remains unpredictably large. In their
report,
stated
the World Health Organisation (WHO)
that epilepsy is a very common neurological syndrome,
affecting ≥50 million people, globally. Around 80% of
the epileptic patients are seen to live in the low or the
middle-income countries [7]. Despite the development and
availability of many novel antiepileptic medications, around
33% of the affected people still suffer from regular seizures.
Furthermore, even after the control of the epileptic seizures,
the unpredictable and stochastic nature of these seizures can
prove to be life-threatening [8].

The medical treatment is signiﬁcantly improved if the clin-
ical epileptic seizures are easily detected. This information is
used for maintaining accurate seizure-related dairies, which
further help in providing treatment during the higher seizure
susceptibility. This ability to precisely and rapidly detect
the epileptic seizures can help in providing treatments for
the progressing seizures. Also, the detection of the seizures
before their occurrence could be very advantageous [9].

The EEG signals or the electrophysiological nerve activ-
ities in the brain have to be acquired for diagnosing and
localising the epileptic seizures clinically. These EEG signals
can provide a lot of useful information regarding the posi-
tion and the markers of the disease. These signals also
provide data regarding the neurological conditions, activi-
ties, and the mental inadequacy [10]. Rhythmic sinusoidal
activities are determined from the EEG signals. For analysing
the EEG signals, 5 frequency bands are normally used,
i.e., Delta (up to 4 Hz), Theta (4–8 Hz), Alpha (8–12 Hz),
Beta (12–26 Hz), and Gamma (26–100 Hz) [11]. The EEG
signals in the epileptic patients display 2 abnormal activities,
1) Ictal – which occurs during the epileptic seizures; and
2) Interictal or seizure-free activity occurring between the
2 epileptic seizure episodes. The ictal EEG signals are seen to
be continuous or uninterrupted waveforms having sharp and
spiky wave complexes. The interictal EEG signals are seen to
be temporary waveforms which exhibit spikes, spiky or sharp
waves [12]. In a few of the epilepsy patients, the doctors
have to acquire the EEG signals from the deep brain struc-
tures or from the surface of the brain. The intracranial signals
are recorded for determining the regions of the brain where
the epileptic seizures are initiated. These signals also help
in understanding if the patients can be beneﬁted from the
neurosurgical re-sectioning of the brain components. Many
neurologists stated that these signals disclose the intriguing
dynamics occurring in the brain during the acute epileptic
seizures and seizure-free intervals. Hence, these intracranial
recordings can be effectively applied for the nonlinear signal
analysis. Usually, the doctors rely on the identiﬁcation of the
interictal (seizure-free) EEG signals for predicting the onset
of the disease, since the ictal signals are very rare. Hence,
a longer duration of the EEG signals is required for visual
monitoring and analysis, for localising the normal, ictal and
the interictal episodes in the patients [13].

The univariate nonlinear analysis can estimate the features
like the predictability, entropy or the dimensionality of the
individual dynamics data derived from the input signals.
Furthermore,
these signals are used for measuring and
analysing the bivariate nonlinear measures for detecting the
interactions between the different dynamics. The features
that are selected and extracted from the EEG signal can
be evaluated based on their time-domain [14]–[17] or
frequency-domain characteristic features [18], [19], joint
time-frequency distribution [20]–[23], chaotic [24]–[26],
or their Empirical Mode Decomposition (EMD) character-
istics [27], [28]. In many studies, the feature combination
is carried out for increasing the accuracy and the general
performance of the whole system [29].

The EEG wave morphology noted between the focal or
non-focal epileptic seizures is similar, which makes it difﬁ-
cult
to visually distinguish between them [30]. Hence,
machine learning algorithms are used for automating the
detection and localisation techniques, as they provide accu-
rate and precise EEG signal interpretation. Also, researchers
developed hybrid techniques for improving the detection
accuracy. These techniques combined the feature extrac-
tion processes and the machine learning algorithms. In one
study, the researchers combined the fuzzy logic and Genetic
Algorithm (GA) for classifying the focal and non-focal
epileptic seizures [31]. Furthermore, researchers also devel-
oped a hybrid computational GA-based technique for
detecting the features and the electrode sites, which helped in
predicting the optimum seizures [32]. Besides, many machine
learning algorithms were also combined [33]–[38].

In this study, the authors present an analysis on the non-
focal and the focal epilepsy detection processes. They anal-
ysed the contributions made by the advanced monitoring and
closed-loop epilepsy detection methods, which are used in
hospitals and patient care centres. This paper is prepared in
following way. Section 2 provides the focal and non-focal
detection methods. Section 3 describes the classiﬁcation
algorithms. Section 4 illustrates the machine learning regu-
larisation. The main observations are discussed in section 5.
While, the paper conclusion is presented in section 6.

A. EPILEPTIC SEIZURES CLASSIFICATION
The classiﬁcation of the various epileptic disorders has
been very controversial and debatable for many years.
In 1981, the International League Against Epilepsy (ILAE),
the main commission that classiﬁes and deﬁnes the various
epilepsy-related terminologies, proposed the International
Classiﬁcation of the epileptic seizures [39]. The seizures
classiﬁcation are shown in Figure 1 [40]. Later, in 2010,
the ILAE proposed a few changes in the nomenclature and
the approach which is involved in the ﬂexible multidimen-
sional framework. However, the details of this new class are
still evolving based on the results provided by the various
studies [41].

One suggestion involved the replacement of the term
‘‘partial’’ by ‘‘focal’’ for the seizures which originated in

VOLUME 6, 2018

49307

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

boundaries further. On the other hand, the conceptual clas-
siﬁcation of the focal and the generalised seizures is very
clinically useful and valid. This classiﬁcation, along with
the descriptions provided by the patients, further helps the
clinician to diagnose the type of seizure. If the history is not
clear (i.e., un-witnessed ‘‘blackouts’’ or a brief loss of aware-
ness), the EEG signals can help in distinguishing between
the complex partial seizures with focal IED and no seizures
with a generalised IED [45]. The focal and the non-focal EEG
signals (derived from the Bern-Barcelona EEG database [46])
have been described in Figure 2.

FIGURE 2. The EEG signal for (a) Focal Epilepsy (b) non-Focal Epilepsy.

II. METHODES
A. FOCAL EPILEPSY DETECTION
The focal epilepsy detection systems can detect and differ-
entiate between the existing focal and non-focal seizures
and can provide the doctors with the detailed seizure-related
data, which helps in epilepsy management. Furthermore,
the detection systems provide a rapid treatment process
for the early-onset seizures, thereby decreasing the spread
of the seizures and arresting their clinical complications.
The seizure detection scheme should be able to detect the
absence or presence of the existing seizures. A majority
of the seizure detection algorithms include 2 major stages:
1) Stage 1 includes appropriate quantiﬁable features, like
the biomarkers or the EEG features, which are assessed
from the patient data; 2) Stage 2 applies a threshold or a
model-based measure to all the features for determining the
presence or the absence of the seizures. This is known as the
classiﬁcation and could involve the use of a threshold value or
models which have been derived using the machine learning
algorithms [47].

FIGURE 1. The seizure classification.

the

focal

are not

the neuronal networks from one of the cerebral hemispheres.
Thereafter,
classiﬁed as
seizures
simple or complex, based on the presumed changes in the
consciousness levels. Thus, the symptoms and signs of the
focal seizures must be properly diagnosed, even if the indi-
vidual displays bilateral motor manifestations. The gener-
alised seizures originate within the bilaterally-distributed
cortical or the cortical-subcortical networks, which rapidly
become involved without any focal point, and can also engage
the structures of the cortical and the subcortical, but not the
whole cortex. Though the different syndromes include the
generalised or the focal epilepsy seizure types, the researchers
must determine whether the epilepsy results due to focal
pathology, since they include many surgical options. Epilepsy
is also categorised as metabolic or structural and could
immune causes. Owing to
occur due to infectious or
the different complex deﬁnitions and systems involved in
epilepsy, an appropriate classiﬁcation scheme must be devel-
oped which provides advanced knowledge about the ﬁeld,
but can be easily understood by the common people or
laymen [42], [43].

B. EEG SIGNAL CHARACTERISTICS
EEG signals help in determining the epilepsy seizure types
and syndromes in the patients, which further helps in
predicting the prognosis of the disease and use of proper
antiepileptic medication. The EEG results assist
in the
multi-axial epilepsy diagnosis, with regards to whether
the epilepsy seizures are idiopathic or symptomatic, focal
or generalised, or a component of the particular epilepsy
syndrome [44]. The focal and the generalised seizures
show overlapping clinical and electrographic manifesta-
tions, while the uni-hemispheric epilepsies can blur these

49308

VOLUME 6, 2018

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

When all

Many studies have applied the bivariate measures for
seizure prediction, like the nonlinear interdependence [48],
phase synchronisation and the cross-correlation [49]. In one
study, when the researchers compared the bivariate and
the univariate system performances, with regards to the
seizure prediction [50], the bivariate techniques showed a
better performance than the univariate measures. Generally,
the univariate and the bivariate systems provide different but
complementary and very relevant information [51]. Hence,
for characterising the preictal stages and achieving a better
clinical performance across the different patients, many
univariate and bivariate features must be combined for devel-
oping proper seizure localisation implements and tools [52].
these features are included in a technique,
it leads to a compromise between the accuracy and the speed
criteria (i.e., more accurate data lowers the speed of the
system, and vice-versa). Many feature-based computation
processes use the line length method [53], frequency [54]
or linear time-frequency analysis (i.e., Wavelet Transfor-
mation) [55], Principle Component Analysis (PCA) [56],
and a higher-order
[57]–[59]. The
various classiﬁcation techniques use the Support Vector
[60]–[62], Artiﬁcial Neural Network
Machines (SVM)
(ANN)
[65], Markov
[64], Fuzzy logic model
modelling [66], and the deep learning algorithms [67], [68].
Analysis modelling using the supervised machine learning
algorithms can be carried out during the training and the
testing stages and includes 3 sub-steps: pre-processing,
feature computation, and feature extraction or feature reduc-
tion. Every process is a specialised research ﬁeld and has not
been described here [69]. Figure 3 presents the block diagram
algorithm for the general focal estimation, which is supported
by the supervised machine learning algorithms.

analysis

spectral

[63],

B. EEG DATABASE AND ACQUISITION PROCESS
The focal and the non-focal epileptic seizure detection studies
consider both the scalp and the iEEG recordings. The scalp
EEG signals are acquired with the help of surface electrodes
that are attached at an equal distance on the scalp; while the
iEEG signals are derived by the intracranial electrodes that
are placed in the regions having suspected epileptogenicity,
which are identiﬁed using the structural, clinical or functional
data, collected before implantation [70].

The earlier studies used the local databases which were
developed using the data from the patients who were
evaluated before their epileptic surgeries. However, these
studies were restricted to the analysis of the short time
period before the seizures, small sample size and few ictal
actions. This restricted the probability of evaluating the speci-
ﬁcity of algorithm in the interictal epoch. In their study,
Eftekhar et al. [71] applied the coefﬁcients of nonparametric
correlation for Kendall’s tau and noted a statistically signif-
icant correlation in the sensitivity of the different systems,
based on the number of the seizures and the mean capturing
time period between the seizures. They stated that long-term
recording data, with numerous seizures, was necessary, for

FIGURE 3. The general focal estimation algorithm block diagram.

enabling the reliable estimation of the algorithm speciﬁcity
and sensitivity, ideally during future testing [72]. In the
past few years, many web-based databases were developed
in the University of Freiburg, University of Bonn, and
the Boston Children’s Hospital. The European Database on
Epilepsy [73] is seen to be the biggest existing seizure predic-
tion database, which consists of information for 2500 seizures
and 45,000 h of EEG recordings. All this data was acquired
from ≥250 patients, out of which, 50 underwent iEEG,
with ≤122 channels that were sampled at a frequency
of 250–2500 Hz. Besides the above-mentioned databases
comprising of the EEG signals, which were acquired in the
epilepsy-monitoring units, many recent studies [74], [75]
adopted the data collected by the Neuro Vista ambulatory
monitoring system. This system provided continuous iEEG
data for many months, however, from very few patients [76].
Cook et al. [50] assessed the safety and performance of the
seizure advisory system in the 15 Neuro Vista-implanted
patients. These long iEEG signal recordings, derived from the
naturally-occurring seizures, would prove to be very beneﬁ-
cial for the epilepsy seizure prediction in future.

C. EEG SIGNAL PRE-PROCESSING
The detection and the elimination of the EEG signal artefacts
can be a complex and difﬁcult task. However, it is impor-
tant for the development of good systems for EEG analysis.

VOLUME 6, 2018

49309

A majority of the important physiological artefacts include
the ElectroOculoGraphy (EOG) artefacts, muscular activi-
ties, respiration, and the body or head movements [77]. Many
studies have described techniques for detecting and elim-
inating the EEG artefacts. However, these described tech-
niques require an individual manual adjustment, or are based
on the inﬂexible and restricting decision criteria, and have
proved to be very unsatisfactory [78], [79]. The techniques
used for correcting the eye movement artefacts were based
on the autoregressive process of subtracting the EOG signals
from the EEG [80]. In their study, Maddirala and Shaik [80]
proposed a novel algorithm for eliminating the muscle arte-
facts by applying the Singular Spectrum Analysis (SSA) and
the Adaptive Noise Canceler (ANC) for removing the EOG
artefacts from the EEG signals. De Vos et al. [81] proposed
a novel algorithm for removing the respiration-related arte-
facts by decomposing the EEG signals using the ICA.
Furthermore, O’Regan et al. [82] proposed a novel algorithm
using the support vector machines for eliminating the head
movement-related EEG signal artefacts, which were cate-
gorised and eliminated as a different class.

D. EEG ANALYSIS APPROACHES
The EGG variations before the seizures can be theoretically
sensed for determining the oncoming seizures [83]. The
earlier EEG-based techniques used for identifying the focal
patterns used to rely on the linear processes for determining
the EEG features using a sliding window [84]–[86]. Such
models used the nonlinear signal processing techniques for
studying the spontaneous formation of the temporal, spatial,
and spatiotemporal patterns. In the past few years, auto-
mated techniques for EEG analysis have emerged based on
the normal brain dynamics. These novel techniques involve
the transient and limited synchronisation of the disorgan-
ised neuronal activity and display a synchronised and persis-
tent state which can incorporate numerous brain regions
during the epileptic seizures [87], [88]. Though the EEG
signals provide a large amount of data which can be deduced
using automated techniques, the patients ﬁnd it tedious to
constantly wear the EEG electrodes for a long time period.
It is also difﬁcult to read the prolonged surface electrode
signals owing to increasing impedance. Some patients can
develop a few skin abrasions because of their prolonged expo-
sure to the surface electrodes [89]–[91]. Studies describing
the various focal epilepsy detection techniques are presented
in Table 1.

E. FEATURES SELECTION AND EXTRACTION
Generally,
the features are categorised based on their
domains: time, frequency, joint time-frequency and non-
linear [85]. These features can be extracted from the derived
signals using a single electrode. On the other hand, some
features are seen to combine many electrodes, and these have
been used in this review. Based on the notations, described
earlier [92], [93], λ (t) ∈ K T refers to the vector which
contains the time series from one electrode, T indicates the

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

sample number in λ while λ (t) refers to the time derivative.
A λ (t) feature is represented as x, and the Matrix X =
[x1, . . . , xF ] comprises all features from all samples, xirefers
to the vector with a single feature, and F denotes the number
of features.

1) TIME DOMAIN FEATURES
As the EEG signals are seen to be multi-component and non-
stationary, the time domain features are not predominantly
used in the EEG analysis. However, many techniques have
been used for determining the EEG characteristic features
which describe the EEG signals, enabling their classiﬁcation.
One such technique used for computing a non-stationary time
series like the EEG signals involves considering them as
many stationary segments.

a: STATISTICAL FEATURE ANALYSIS
Diykh et al. [94] proposed a few statistical analysis tech-
niques for extracting the necessary features from the 1 second
EEG epoch, which are described below:

Maximum XMax = Max[xn]
Minimum XMin = Min[xn]

Range XRang = XMax − XMin

Mean Xmean =

Median Xme =

First Quartile XQ1 =

Variation XVar =

Standard Deviation

XSD =

Kurtosis XKu =

Skewness XSke =

Second Quartile XQ2 =

(cid:19)th

n
(cid:88)

xi

1
n
1
(cid:18) N + 1
2
1
4 (N + 1)
N
(cid:88)

(xn − Xmean)

2
N − 1

n=1

(cid:114)

(cid:88)n
1

(xn − Xmean)

2
n − 1

4
(N − 1)X 4
SD

3
(N − 1)S3
SD

N
(cid:88)

n=1
N
(cid:88)

(xn − Xmean)

(xn − Xmean)

n=1
4
4(N +1)

(1)

(2)

(3)

(4)

(5)

(6)

(7)

(8)

(9)

(10)

(11)

The EEG data can show a symmetric or a skewed distri-
bution. The symmetric distribution of the time series is
measured by the mean and standard deviation, while the
skewed distribution uses the median, range and quartile
for measuring the centre and spread of the EEG dataset.
However, the feature mode, which provides the frequency
values, is applied for measuring the location of the time series.
The remaining statistical features, like the variation, skew-
ness, minimum, and kurtosis, are also used for determining
the vital time series-related data [95], [96].

49310

VOLUME 6, 2018

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

TABLE 1. Summary of the focal and non-focal epilepsy detection studies.

VOLUME 6, 2018

49311

TABLE 1. (Continued.) Summary of the focal and non-focal epilepsy detection studies.

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

b: HJORTH TIME DOMAIN DESCRIPTORS
Hjorth [97] characterised the EEG signals based on the
interdependence between the EEG values. The researchers
proposed a novel technique, based on the concept of deriving
the quantifying parameters and using their efﬁciency for
determining their auto-correlation functions. Hjorth intro-
duced the different parameters as the descriptors of graphical
characteristic features of the EEG signals, with regards to
the slope, amplitude, and the slope spread. These descriptor
names, like, ‘‘mobility’’, ‘‘activity’’ and ‘‘complexity’’ are
retained; however, the descriptor ‘‘complexity’’ is redeﬁned
as the ‘‘complexity of ﬁrst order’’. This provides an absolute
value of the spread of the slope as the standard deviation per
unit time.

c: EEG CROSS-CORRELATION
Correlation is deﬁned as the mathematical
technique,
which is similar to the convolution process. In correlation,
the sequence between the energy of signals can measure
the similarity which is known as a cross-correlation tech-
nique [98]. If the signal correlates with itself, the resultant
sequence is known as the autocorrelation sequence. Consider
2 signal sequences, x(n) and y(n), with a ﬁnite energy. Thus,
the cross-correlation between these signals is seen as:
(cid:40)(cid:88)N −m−1
n=0
ˆRxy (−m)

xn+myn m ≥ 0
m < 0

ˆRxy (m) =

(12)

Wherein; m = . . . − 2, −1, 0, 1, 2, . . . and is deﬁned as the
time shift parameter index or the lag; xy subscript indicates

the sequences that are being correlated. The order of the
subscript with x preceding y indicates the direction in which
one of the sequences gets shifted, with regards to the other.
If both the x(n) and y(n) signals consist of a determinate
sample number, L, the resultant cross-correlation sequence
is seen to consist of 2M − 1 samples.

d: PRINCIPLE COMPONENT ANALYSIS (PCA)
PCA refers to a statistical technique which is used for trans-
forming the input space into a novel lower dimensional space,
while the coordinate system can be swapped using the linear
transformation. In the PCA, the axes (or the components) that
belong to the novel coordinate system are seen to be the linear
combination of the primary axes. Furthermore, the major axis
(or the principal component) represents the direction of the
maximal variation, noted in the dataset. However, the minor
axis, which is orthogonal to the major axis, is seen to charac-
terise the direction of the second biggest deviation in datasets,
and so on. Thereafter, in the new re-oriented space, a majority
of the data variation is concentrated within the initial few
components. As a result, the components which consist of
valid information regarding the data variability are reserved,
while the other components are disregarded. This reduces
the dimensionality without affecting the data accuracy in any
way [99]–[101].

The basic PCA technique is theoretically simple. Firstly,
the values of the d-dimensional mean vector, i.e., µ and the
m × m covariance matrix, R, are estimated for the complete
dataset. Thereafter, the Eigenvectors and the Eigenvalues

49312

VOLUME 6, 2018

highest probable differences in the mean scores of the classes.
Furthermore, the overlapping degree amongst the discrim-
inant score distribution is used for measuring the success
of LDA. The discriminant scores are determined using the
discriminant function, with the following form [107]:

D = w1Z1 + w2Z2 + w3Z3 + · · · + wnZn

(17)

As shown in Eq. (17), the discriminant score refers to
the weighted linear predictor combination. All weights are
calculated for maximising the difference between the mean
discriminant class scores. Generally,
the predictors with
dissimilar class mean values show a larger weight; whereas
the predictors with similar class means show small weights.

2) FREQUENCY DOMAIN ANALYSIS
The spectral or frequency domain analysis refers to the
description of the details regarding the multiple frequency
components involved in signal construction. A Fourier Trans-
form (FT) process is used for computing all signal compo-
nents. Many researchers developed novel FT-based processes
for extracting the EEG features that are used in the parametric
and non-parametric techniques for determining the 1D signal
in the frequency domain. Many non-linear mechanisms are
used for generating the EEG signals. A lot of research has
been devoted to developing these non-linear methods [108].
The Power Spectral Density (PSD) technique used to analyse
the focal and non-focal EEG signals is described in Figure 4.

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

are ﬁgured and arranged according to the decreasing Eigen-
values, i.e., Eigenvectors, g_1 having an Eigenvalue of δ_1,
while g_2 has an Eigenvalue of δ_2, etc. Then, the k Eigen-
vectors are selected, by observing the complete Eigenvector
spectrum. Usually, one dimension, which implies the inherent
dimensionality of the subspace, controls the ‘‘signal’’. Noise
is another dimension. Finally, a k × k matrix A, with columns
consisting of k Eigenvectors is formed and pre-processed as
described earlier [102]:

x(cid:48) = AT (x − µ)

(13)

e: INDEPENDENT COMPONENT ANALYSIS (ICA)
ICA refers to a feature extraction technique that can manip-
ulate the random and multivariate signals into signals with
jointly-independent components. This method is used for
extracting these independent components from all assorted
signals. Furthermore, in this technique, the independence
refers to the fact that the data carried by a single component
is not inferred from other components. This indicates that
the independent quantities with joint probability are acquired
as a product of the probability of each component. Assume
the presence of c source signals of independent scalar, such
that x_i (t), i = 1, 2, . . . , c wherein, t refers to the time key:
1 ≤ t ≤ T. For the notational convenience, the researchers
grouped the c values into vector x(t) and further assumed
that this vector has a 0 mean. Based on the independence
hypothesis, and the hypothesis of no noise, the researchers
described the multivariate density function as [103]–[105]:

P (x (t)) = (cid:89)c

i=1

Pxi(t)

(14)

Assume that the d-dimensional data vector can be spotted

at every instant:

y (t) = Ax(t)

(15)

Wherein; A refers to the m × n scalar matrix, while
n ≥ m. The ICA recovers the source signals from all
detected signals. This equation is used for obtaining the real
matrix, W , as follows:

z (t) = Wy (t) = WAx(t)

(16)

FIGURE 4. The Power Spectral Density for the focal and non-focal EEG
signals.

In the previous equation, z refers to the value of the
source, x(t). The researchers aimed to compute W = A−1,
however, the value of A or its inverse is not known.

f: LINEAR DISCRIMINANT ANALYSIS (LDA)
The LDA method is used for generating new variables
which group the primary predictors. This can be obtained
by maximising the differences among the predeﬁned groups,
related to the novel variable. Furthermore, the predictor
scores are combined for designing the single novel composite
variable, i.e., discriminant score. LDA also refers to an exces-
sive data dimension reduction process which can compress
the multi-dimensional predictors to form a 1-D line [106].
Finally, the researchers expected that every class displays
a normal distribution of the discriminant scores, with the

VOLUME 6, 2018

a: NON-PARAMETRIC ANALYSIS TECHNIQUES
Polat and Güne? [109] proposed a novel
technique for
epileptic identiﬁcation, wherein they initially computed
the autocorrelation between the time sequenced dataset.
In Step 2, the power spectrum was estimated by applying
FT processes to the autocorrelation sequences. The Welch
technique was used for estimating the average value over
a period of time, for determining the PSD values. If the
available data derived from the signals comprises of sample
x(n) wherein n = 1, 2, . . . , N, the periodogram spectra can
be estimated as follows:

ˆPPER (f ) =

1
N

(cid:12)
(cid:12)
(cid:12)
(cid:12)

(cid:88)N

n=1

x(n)e−iωfn

2

(cid:12)
(cid:12)
(cid:12)
(cid:12)

(18)

49313

Here, ˆPPER (f ) refers to the periodogram power estima-
tion. Based on the Welch frequency estimation technique,
the signals can be separated into the overlapping fragments,
and each data fragment is windowed, all periodograms are
estimated and averaged. xl(n), l = 1, . . . , S refers to the data
segments, with M as the length of every segment. A 50%
overlap is generally selected. Finally, the Welch spectrum is
estimated as follows:
1
S
1
M

n=1
Here ˆPl (f ) refers to the periodogram estimation of the
lth segment, v(n) denotes a data-window, P = average of v(n),
i.e., P = 1/M (cid:80)M
n=1 |v(n)|2; ˆPw (f ) refers to the Welch
PSD value, M denotes the length of every signal fragment
(segment); while S denotes the segment number.

v (n) xl (n) e−iωfn

l=1
(cid:12)
(cid:12)
(cid:12)
(cid:12)

ˆPw (f ) =

ˆPl (f ) =

ˆPl(f )

(cid:88)M

(cid:12)
2
(cid:12)
(cid:12)
(cid:12)

(cid:88)S

(19)

1
P

b: PARAMETRIC ANALYSIS TECHNIQUE
The main disadvantage of using the non-parametric tech-
nique is the spectral leakage because of the windows. This
limitation can be overcome by the model-based power spec-
trum or the parametric methods. Also, compared to the non-
parametric technique, the parametric allows better frequency
resolution. In the parametric process, the signal was consid-
ered as a random stationary process. Then, the signal was
modelled as the ﬁlter output, with the noise as its input.
Thereafter, the corresponding ﬁlter parameters were deter-
mined. The Auto-Regressive (AR) model is a parametric
process which interprets the signal as the linear combina-
tion of its earlier activities in addition to the uncorrelated
noise [85], [110], [111], as follows:

Ajxi−j

ei = (cid:88)p
j=0
where Aj refers to the model coefﬁcient matrix, p = model
order, xi = input EEG signal, while ei = multivariate 0 mean
uncorrelated vector. Furthermore, the Aj matrix was obtained
after solving the linear equation, m × p:

(20)

(cid:88)p

j=0

AjR (j-k) = −R (−k),

k = 1, . . . , m

(21)

Wherein; m = no. of channels, p = calculated order
of AR model, R(k) refers to the covariance matrix biased
values. The researchers carried out the AR spectral analysis
for the EEG signal dataset employing the technique proposed
by Franaszczuk et al. [112] and Fernandes et al. [113].

3) TIME-FREQUENCY ANALYSIS
The primary objective of using the Time-Frequency Distri-
bution (TFD) analysis is to derive a function which char-
acterises the energy densities of the signals in the time and
the frequency domains. Intermediate Frequency (IF) and the
Spectral Delay (SD) are common terms used in the TFD
analysis. IF represents a local maximal frequency at a speciﬁc
time which corresponds to the sine wave frequency for the

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

best-analysed signal. On the other hand, SD refers to the esti-
mation of the frequency-time arrival for the combined time-
frequency example. The TFD analysis is used for indicating
the time and the frequency laws for every signal component
within the time-frequency domains. This simpliﬁes the IF
and SD calculation. This process also provides information
regarding the amplitude and the duration of every signal
component, along with its instantaneous bandwidth which
refers to the IF surrounding the spread spectra [114].

a: DISCRETE WAVELET TRANSFORM (DWT)
The Wavelet Transform (WT) analysis is an important and
crucial in automated process of seizure detection and has
been used in many studies. Based on the Wavelet Anal-
ysis [23], the signal is characterised by the set of linear
combination of functions, which are acquired after expanding
and translation the individual function. This single function
is identiﬁed as the mother wavelet and can be used for
interpreting the primary signal into a few sub-signals which
are half its spectra and size. In the case of the Discrete
Wavelet Transform (DWT), all scaling and translating factors
are expressed as the power of 2. DWT uses some Quadrature
Mirror Filters (QMF), which are known as the high-pass and
the low-pass ﬁlters. In the DWT level 1, the input signal
is passed over the conjugate low and the high pass ﬁlters,
simultaneously [115]. The output achieved is in the form
of coefﬁcients, called the wavelet coefﬁcients. The result
obtained from the low-pass ﬁlter, called approximation, gets
sub-decomposed, while the output from the high-pass ﬁlter,
called detail, is not sub-decomposed.

This process is repeated recursively to generate a single-
sided, pyramid-like structure. It is very important to select the
appropriate no. of decomposition levels and mother wavelet.
The decomposition level number is selected according to
their dominant frequencies. The mother wavelet function is
selected from the Daubechies wavelets after a visual exam-
ination. In their study, Tzimourta et al. [116] proposed a
novel automated seizure detection technique based on the
WT analysis for decomposing the 2 epoch segments into
5 wavelet decomposition levels. Thereafter, the necessary
features are submitted to the SVM classiﬁer for the clas-
siﬁcation. Figure 5 describes the wavelet decomposition
process [114].

FIGURE 5. Wavelet decomposition process.

b: SPECTROGRAM
A spectrogram distribution denotes a single processing tech-
nique which can be used for analysing the multicomponent

49314

VOLUME 6, 2018

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

non-stationary signals. This technique extracts several frames
from an analysed signal, having a moving window, over a
period of time. Every extracted frame is stationary and the
FT is applied. A spectrogram distribution can be deﬁned as
follows [117]:

P (t, ω) =

(cid:90)

(cid:12)
(cid:12)
(cid:12)
(cid:12)

1
√
2π

e−jωτ

s (τ ) h (τ − t) dτ

(cid:12)
2
(cid:12)
(cid:12)
(cid:12)

(22)

In their study, Stamoulis et al. [118] applied the spectro-
gram distribution for detecting the onset of new focal EEG
seizures. This process applies high-frequency neural network
modulations, for analysing the EEG signals from the frontal
and temporal lobes. The limitation of this method is that it
uses ﬁnite-sized windows. A narrow window can provide
a low frequency but a better time resolution. On the other
hand, wide windows generate poor time resolution but a better
frequency resolution. However, the wider windows violate
the stationary conditions [119].

c: THE EMPIRICAL MODE DECOMPOSITION (EMD)
An EMD process is a type of adaptive technique that analyses
the non-stationary and non-linear signals [120]. This process
comprises of a data-driven and local separation of signals in
slow or fast oscillations. The EMD process aims to decom-
pose the signals into the Intrinsic Mode Functions (IMFs).
In the past few years, novel processes were recommended
for the classiﬁcation and analysis of the focal epileptic EEG
seizure signals based on the EMD. The average frequency of
the IMF was used as a factor for identifying the differences
between the ictal and the seizure-free EEG signals [121].
The normal and the epileptic seizure EEG signals were
compared using the Hilbert weighted frequencies for the
different IMFs [122].

The EMD process is an adaptive, simple and a nonlinear
process which provides variability in a speciﬁc time
series [123]. This process generates a few IMFs that are
frequency and amplitude-modulated (AM and FM) waves.
The scalp EEG seizures along with their 13 IMFs have been
described in Figure 6. It can be seen that the speciﬁc IMF4,
5 and 6 oscillations appeared during the time of the seizure.
Hence, these functions are applied for the seizure detec-
tion. The speciﬁc frequencies appear in varying modes as
the EMD process depends on the frequency of the EEG
signal. This distinguishes the EMD process from the DWT
technique.

4) NON-LINEAR TECHNIQUES
The frequency domain processes determine the rhythmic
oscillations within the signals but are restricted by their
inability to detect the nonlinear coupling or the phase locking
amongst the harmonics within that spectra [124]. All biolog-
ical systems are effectively described based on the nonlinear
processes, which is also applicable for the EEG signal
analysis.

The variations in the EEG signals are not easily noted
inspection alone since they are very chaotic

by visual

FIGURE 6. EEG IMFs Decompositions.

and variable in nature. Hence, an automated system must
be developed that can categorise the various sleep stages
using the signal processing methods based on a statis-
tical analysis of nonlinear and linear characteristics of the
EEG signals. The time and the frequency analysis cannot
provide very accurate results since these processes cannot
detect the minute data from the EEG signals owing to their
nonlinear and non-stationary status [125]. The nonlinear
dynamics are used for sleep EEG signals for differen-
tiating the various sleep stages. Chouvarda et al. [126]
analysed the different sleep stages using fractal dimen-
sions, approximation and sample entropies. These methods
showed a variation in the features at differing sleep
stages.

VOLUME 6, 2018

49315

a: SPECTRAL ANALYSIS EIGENVECTOR TECHNIQUES
The Pisarenko method is used for computing PSD. It consists
of sharp peaks that localised at expected frequencies [127].
Besides, Polynomial K (f ) holds 0s on a unit circle and is used
for estimating PSD:

K (f ) = (cid:88)m

ak e−j2π fk

(23)

k=0
wherein K (f ) is the necessary polynomial, ak = coefﬁcients
of the polynomial, and m = order of the Eigen ﬁlter K (f ).
This polynomial is expressed as an autocorrelation matrix, R,
for the input signal. Assume that white noise is used in the
signals:

R = E

(cid:110)

x(n)∗ · x(n)T (cid:111)

= SPS# + σ v2I

(24)

where x(n) denotes the detected signal; S denotes the path
of the signal in the dimension matrix (m + 1) × B;
while, B refers to the signal subspace dimensions; R denotes
an autocorrelation matrix for the elements (m + 1) ×
(m + 1); p refers to the signal power, of the dimension matrix,
(B) × (B); σ v2 denotes the power of the noise; ∗ refers to
the complex conjugate; I is an identity matrix; # denotes
the complex conjugate transposed; T refers to the transposed
matrix. S is a signal route matrix, which is represented as:
S = [Sw1Sw2, . . . , SwL], i = 1, 2, . . . , B. For all the
practical applications, the autocorrelation matrix, ˆR, must be
constructed using the autocorrelation lags:

ˆR(k) =

1
N

(cid:88)N −1−k
n=0

x(n + k) · x(n),

k = 0, 1, . . . , m

(25)

Wherein; k denotes the autocorrelation lag index; and the
no. of the signal samples are denoted by N . Thereafter, the
autocorrelation matrix gets transformed to:

ˆR (k) =











ˆR (0)
ˆR (1)
ˆR (2)

ˆR (m)

ˆR (2)
ˆR (1)
ˆR (0)

ˆR (1)
ˆR (0)
ˆR (1)
...
ˆR (m − 1)

ˆR (m)
ˆR (m − 1)
ˆR (m − 2)
...
ˆR (0)











· · ·

. . .
· · ·

(26)

b: ENTROPY
Entropy is deﬁned as the measurement of the rate of data
generation which is used for separating the beneﬁcial signals
from the background noise. Generally, a higher entropy value
is seen to correspond to the increased unpredictability and
irregularity, whereas a lower value indicates a higher regu-
larity. Furthermore, entropy indicates a nonlinear index which
reﬂects the chaos in the system [128], [129]. Entropy is
applied for analysing the epileptic EEG signals and detecting
the occurrence of an epileptic attack or for inspecting the
seizures. Entropy is classiﬁed into spectral or embedding
entropy. The spectral entropy is deﬁned as the entropy which
is calculated from the amplitude component of a power

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

spectra in the signal; while the embedding entropies are
directly estimated using a time series [130].

The mean spectral entropy is based on the power spectrum
of a signal and is used for estimating the time series regularity.
Also, the amplitude component of a power spectrum is used
for computing the probabilities for estimating the entropy
value. The spectral entropy [131] can be assessed with the
help of the normalised Shannon entropy that can quantify
the spectral complexity in a time series. FT is applied for
deriving the PSD of the datasets time series representation.
PSD denotes the power scattering of the signal based on
the signal components (frequencies) [132]. For obtaining the
power level of every frequency, the FT for the signal can be
calculated, while the power of the frequency factor can be
denoted by the Pf . The normalisation of power is derived by
calculating total power ((cid:80) Pf ) and then, dividing the power
value, consistent to the frequency of (cid:80) Pf as:

pf =

Pf
(cid:80) Pf
Entropy can be computed by power multiplication in every
frequency and logarithm of the inverse of that power value.
Thereafter, the spectral entropy is calculated as follows [133]:

(27)

Ensh = (cid:88)

pf log

1
pf

(28)

The embedding entropy values are seen to provide a lot
of information regarding the manner in which the EEG
signals ﬂuctuate with respect to time. This is carried out by
comparing the time series using a delayed version of the
same [134]. A popular embedding entropy technique includes
the Kolmogorov-Sinai (KS) technique, which estimates the
signal uncertainty with regards to time [135] using the
embedded signals. KS entropy also refers to a metric entropy
value that is 0 for the non-chaotic signals and is >0 for the
chaotic signals. The entropy value is determined by locating
the points which are nearer to one another on the trajectory
in space but are not correlated with time. The divergence rate
of the point pairs generates the KS value.

Other entropy approaches used for the process of feature
extraction from EEG signals are Approximate Entropy [136],
Sample Entropy [137], Renyi’s Entropy [88], Permuta-
tion Entropy [138], Tsallis Entropy [139], Kolmogorov
entropy [140], Fuzzy Entropy [141] and the Normalised
Bispectrum Entropy [124].

5) GENETIC ALGORITHM
It is signiﬁcant to select suitable features for improving the
accuracy and efﬁciency of the classiﬁers. Different feature
selection techniques, like the wrapper-selection and ﬁlter-
selection, were developed. In one study, the researchers
applied the GA and Fisher discriminant analysis (FDA), for
the variable range of the EEG signals, and compared their
performance. GA is a type of optimisation technique which is
based on the Darwinian evolution theory and genetics [142].
The conventional gradient-based optimisation processes are

49316

VOLUME 6, 2018

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

seen to search for an optimal point in the multidimen-
sional optimisation surface by iteratively reﬁning the solu-
tion. However, GA enables the parallel collection of the
candidate solutions. Using this technique, GA shows a high
probability of searching for a global optimum point instead
of the conventional techniques that get stuck at the local
optima near the primary prediction. The initial individual
population in the GA technique represents a probable solu-
tion for the optimisation problem. Thereafter, the evolution
procedure is based on the selection, crossover and muta-
tion. As per the Darwinian principle of ‘the survival of the
ﬁttest’, this GA process can derive the optimal solutions after
carrying out iterative computations. Crossover and muta-
tions maintain the population diversity. GA handles the huge
search space effectively and avoids the local prime solutions
after combining the exploration as well as the exploitation
processes [143]–[145].

III. CLASSIFICATION ALGORITHMS
After carrying out the steps for detection, and presuming that
all extracted features can distinguish between the seizure and
non-seizure EEG states, the data is used for classifying the
features into their respective categories. Hence, a decision-
making step and data classiﬁcation in the feature space is
necessary. This is a global technique which includes a feature
selection stage and another step wherein the features can be
combined for optimising the system performance.

The data classiﬁcation aims to deﬁne the boundaries
between the classes and label them according to their features.
The data classiﬁcation classiﬁer can be simple like altering
the feature thresholds or complicated like using the machine
learning algorithms. In the multidimensional feature space,
the margin is converted into a separate hyper plane. This
process aims to determine the hyper planes which have a
maximal distance from the classes [17].

Many classiﬁcation and clustering techniques were devel-
oped, like the association rules, LDA, ANNs, Hidden Markov
Modelling (HMM), fuzzy logic, k-means clustering, and
SVMs, for epileptic seizure detection. Many studies have
described the mathematical basis of all these techniques. This
study presents a brief overview of these techniques. The
association rules can be used for inspecting the feature set
and establishing a simple relationship between all features.
Thresholds help in making decisions. The Monitor algorithm
was proposed by Truccolo et al. [146]. This algorithm used
the thresholding of the waveforms into a feature space for
detecting the focal epilepsy seizures of the single-neuron
dynamics. Furthermore, Zijlmans et al. [147] investigated
the ictal and the interictal high-frequency oscillations and
proposed a threshold-based method for determining the inter-
ictal spikes. In their study, Niederhauser et al. [148] used
a time-frequency feature threshold. Mitra et al. [149] deter-
mined a set of rules (varies from the threshold) for the artefact
rejection, along with those for estimating the general seizure
quality.

For the complex relationship between the features, auto-
mated techniques, like the LDA [150], fuzzy logic [151], and
k-means clustering [152], [153] have been used for detecting
the epilepsy seizures. The popular classiﬁers are ANN and
SVM-based.

ANNs can be deﬁned as a mathematical example based
on the low-level functions of the biological neurons. In the
ANN technique, the knowledge regarding the problem can
be distributed in every functional neuron and the connecting
weighted links between the neurons. This neural network
must be appropriately trained for generating the neces-
sary mapping. During the training stage, the feature vectors
act as the input while the network can adjust the vari-
able parameters, biases and the weights, for establishing
the relationship concerning the input and output values.
Based on the network’s ability to learn from the estab-
lished patterns, the ANNs help in classifying the epileptic
seizure detection [154] or spikes [155]. Similar to the ANNs,
the SVM-based processes are also applied for epilepsy
detection by determining the hyperplanes for the multidi-
mensional data. The SVM process aims to determine the
hyperplane within a feature space which optimally sepa-
rates 2-more classes. Furthermore, the SVM technique can
generate a speciﬁc solution for minimising the expected
misclassiﬁcation-related risks. The training algorithms apply
the solutions derived from a popular quadratic programming-
related optimisation problem, which is computationally
effective and generates global solutions [75].

IV. MACHINE LEARNING REGULARISATION
After classifying the data, a regularisation function has to
be added for decreasing the false alarms. For this purpose,
techniques like Kalman ﬁltering [156] and ﬁring power
method [157], which consider the temporal signal dynamics
are used. They aim to improve the classiﬁer speciﬁcity
after restricting the false alarm generation. The ﬁring power
method measures the no. of predictions which are cate-
gorised as preictal during SOP. If this value is higher than
the normalised threshold, it generates an alarm. Many studies
used the ﬁring power process and reported satisfactory
results [158]. Teixeira et al. [159] used a ﬁxed threshold
of 0.5; where some others [160] compared various thresh-
olds (0.10, 0.15, . . . , 0.85) and noted that the lower threshold
values led to low FPRs. No one reported optimal threshold
values. In one study, the researchers used the AR modelling
coefﬁcients as SVM input values and compared the perfor-
mance of their technique with the non-regularised classiﬁer
using iEEG signals derived from 9 patients in the University
of Freiburg database. They noted a signiﬁcantly improved
performance; however, they did not conduct any statistical
testing. Kalman ﬁltering is also used in many reports [156].
Park et al. [161] used the 2nd-order discrete-time Kalman
ﬁlter for smoothening the undesired SVM output ﬂuctu-
ations. Teixeiria et al. [160] compared these regularisation
methods and noted that the ﬁring power technique used a
conservative approach while raising alarms. The researchers

VOLUME 6, 2018

49317

it was a better technique as it could main-
stated that
tain a longer memory of the classiﬁcation dynamics and
created time constraints for raising alarms. They also noted
that the Kalman ﬁltering raised many alarms, which was
impractical [160].

V. DISCUSSION
A lot of effort and time has been directed towards improving
the prediction of the seizures; however, the conversion of the
existing methods into the development of clinical devices has
not been possible. Majority of the algorithmic and analyt-
ical studies have indicated that the physiological transition
to a seizure state is not a random process and a speciﬁc
build-up is responsible for seizure development. The hetero-
geneity between all studies indicates that the ictogenesis
mechanisms are very complicated and hence, appropriate
precaution must be taken for dealing with this seizure state.
In this study, the researchers have summarised, analysed
and discussed all the progress which has been made in the
focal epileptic seizure prediction ﬁeld. Out of all the various
techniques, the nonlinear and bivariate linear methods have
been very promising for seizure prediction. Though a few
of the nonlinear univariate methods can be predictive, they
have been unable to show a better performance than the
linear methods, which has limited their application in the
focal seizure prediction studies. The bivariate methods can
be very helpful in determining the brain dynamics. The phase
synchronisation techniques show a better predictive capacity
than the nonlinear bivariate methods.

As mentioned here, many researchers applied the
WT or the entropy-based techniques. WT,
in combina-
tion with other methods, like chaos, can decompose the
EEG signal into different ﬁxed scales, associated with the
signal’s sampling rate, for differentiating between the normal
and the epileptic EEG signals, as described in Table 1.
The entropy-based processes are used for quantifying the
level of the disorder (or order) in the EEG signals, during
the focal epileptic seizure. Furthermore, the EMD process
has been used as an alternative to the traditional time-
frequency methods. It is seen to be an adaptive decom-
position process which depends on the frequency of the
EEG signal (rather than the ﬁxed cut-off frequency used
in the WT). In the past few years, epilepsy detection is
based on many tensor models and other modelling techniques
which analyse the multimodal data and gather a lot of data
regarding the complex behaviour. This technique helps in
analysing multiple domains simultaneously, like the 3-way
array epilepsy feature tensor that has the time samples ×
frequency × electrode modes.

A combination of the univariate and the bivariate features
is a good alternative. Many studies aimed to investigate
the cross time and the frequency features, coupled in the
feature extraction block [162]–[164]. They reported satis-
factory results in comparison to the conventional spec-
tral power features. These features were based on the
univariate phase-amplitude coupling along with the bivariate

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

amplitude-amplitude coupling. It would be helpful to investi-
gate other coupling types for improving the feature extraction
during the detection and prediction of the focal epileptic
seizures. Furthermore, combining many features for tracking
the preictal stage can also enhance the feature space dimen-
sions, which has increased the need to develop better feature
selection algorithms. Though many researchers have vali-
dated the performance of their classiﬁers using statistical
evaluation-based methods, the feature selection methods have
not been statistically tested. Hence, it is vital to evaluate
the statistical operations of the proposed feature selection
method with other methods. Many seizure prediction studies
have mentioned the need to develop better subject-speciﬁc
and individually-tailored algorithms, while some described
the main discriminative features for all issues. Furthermore,
the out-of-sample testing must be regarded during feature
selection. Also, samples must not be used for evaluating the
performance of the feature selection techniques.

Many classiﬁers have been studied for seizure predic-
tion. However, a comparison between them is difﬁcult
because of heir heterogeneous input features, pre-processing,
and diverse patient data. Many researchers showed that
combining the linear and the nonlinear classiﬁcation methods
can be helpful. The ANN classiﬁers are commonly used for
determining the patterns which are revealed during feature
extraction. These classiﬁers provide vital data about the EEG
seizures and help in differentiating the normal and the seizure
rhythms. SVM is a technique similar to ANN, but is easier and
faster to implement than the ANN, with comparable results.
Hence, SVMs are replacing the ANNs for seizure detection.
The epilepsy detection is based on 2 steps. Step 1 involves
the development of precise and non-invasive detection tech-
niques. The major issue noted in this step involves the identi-
ﬁcation of the artefacts that can interfere with the signal. The
other step is involved in drug delivery and neuro stimulation,
wherein the signal recording or therapy could be very inva-
sive, but the developed techniques aim to detect the onset and
precisely quantify the seizure strength.

Another issue noted during seizure detection involves
the standardisation of all techniques. Firstly, all different
metrics used for evaluating the detector performance must
be combined for homogenous comparison. Secondly, a few
guidelines are necessary for recording the EEG signals
(scalp or intracranial) and their duration (the amount of data
derived after few seconds is different from that obtained after
an hour), while implementing the algorithms.

VI. CONCLUSIONS
This critical review highlights the need to improve and opti-
mise the framework of the focal and non-focal epileptic
seizure detection techniques. Every prediction method must
be subjected to further investigation for improving the ﬁnal
outcome of the proposed techniques. Furthermore, a compre-
hensive point of view must be achieved while developing the
seizure prediction block diagram, which combines the data

49318

VOLUME 6, 2018

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

acquisition and performance evaluation steps. This would
ensure a better and more realistic system performance.

REFERENCES
[1] R. S. Fisher et al., ‘‘Epileptic seizures and epilepsy: Deﬁnitions proposed
by the international league against epilepsy (ILAE) and the international
bureau for epilepsy (IBE),’’ Epilepsia, vol. 46, no. 4, pp. 470–472, 2005.
[2] R. S. Fisher et al., ‘‘ILAE ofﬁcial report: A practical clinical deﬁnition of

epilepsy,’’ Epilepsia, vol. 55, no. 4, pp. 475–482, 2014.

[3] M. Panebianco, C. Zavanone, S. Dupont, D. A. Restivo, and A. Pavone,
‘‘Vagus nerve stimulation therapy in partial epilepsy: A review,’’ Acta
Neurologica Belgica, vol. 116, no. 3, pp. 241–248, 2016.

[4] A. C. Brower and D. J. Flemming, ‘‘Bradley’s neurology in clinical prac-

tice,’’ J. Amer. Med. Assoc., vol. 308, no. 16, p. 1694, Oct. 2012.

[5] A. K. Al-Bashir et al., ‘‘Computer-based Cobb angle measurement using
deﬂection points in adolescence idiopathic scoliosis from radiographic
images,’’ Neural Comput. Appl., pp. 1–15, 2018.

[6] B. Godman et al., ‘‘Initiatives among authorities to improve the quality and
efﬁciency of prescribing and the implications,’’ J. Pharmaceutical Care
Health Syst., vol. 1, no. 3, pp. 1–15, 2014.

[7] S. Saxena and S. Li, ‘‘Defeating epilepsy: A global public health commit-

ment,’’ Epilepsia Open, vol. 2, no. 2, pp. 153–155, 2017.

[8] P. Kwan et al., ‘‘Deﬁnition of drug resistant epilepsy: Consensus proposal
by the ad hoc task force of the ILAE commission on therapeutic strategies,’’
Epilepsia, vol. 51, no. 6, pp. 1069–1077, 2010.

[9] M. Nandan, S. S. Talathi, S. Myers, W. L. Ditto, P. P. Khargonekar, and
P. R. Carney, ‘‘Support vector machines for seizure detection in an animal
model of chronic epilepsy,’’ J. Neural Eng., vol. 7, no. 3, p. 036001, 2010.
[10] D. H. Kerem and A. B. Geva, ‘‘Brain state identiﬁcation and forecasting
of acute pathology using unsupervised fuzzy clustering of EEG temporal
patterns,’’ in Fuzzy and Neuro-Fuzzy Systems in Medicine. Boca Raton, FL,
USA: CRC Press, 2017, pp. 19–68.

[11] F. Bylsma, C. Peyser, S. Folstein, C. Ross, and J. Brandt, ‘‘EEG power
spectra in Huntington’s disease: Clinical and neuropsychological corre-
lates,’’ Neuropsychologia, vol. 32, no. 2, pp. 137–150, 1994.

[12] S.-F. Liang, H.-C. Wang, and W.-L. Chang, ‘‘Combination of EEG
complexity and spectral analysis for epilepsy diagnosis and seizure
detection,’’ EURASIP J. Adv. Signal Process., vol. 62, p. 853434,
Feb. 2010.

[13] K. Lehnertz, ‘‘Epilepsy and nonlinear dynamics,’’ J. Biol. Phys., vol. 34,

nos. 3–4, pp. 253–266, 2008.

[14] C. Donos, M. Dümpelmann, and A. Schulze-Bonhage, ‘‘Early seizure
detection algorithm based on intracranial EEG and random forest classi-
ﬁcation,’’ Int. J. Neural Syst., vol. 25, no. 5, p. 1550023, 2015.

[15] D. Gupta et al., ‘‘Optimized cuttleﬁsh algorithm for diagnosis of
Parkinson’s disease,’’ Cogn. Syst. Res., vol. 52, pp. 36–48, Dec. 2018.
[16] A. R. Hassan and M. A. Haque, ‘‘Epilepsy and seizure detection using
statistical features in the complete ensemble empirical mode decomposi-
tion domain,’’ in Proc. IEEE Region Conf. TENCON, Nov. 2015, pp. 1–6.
[17] P. M. Shanir, K. A. Khan, Y. U. Khan, O. Farooq, and H. Adeli, ‘‘Automatic
seizure detection based on morphological features using one-dimensional
local binary pattern on long-term EEG,’’ Clin. EEG Neurosci., vol. 49,
no. 5, pp. 351–362, 2017.

[18] K. Fu, J. Qu, Y. Chai, and T. Zou, ‘‘Hilbert marginal spectrum analysis
for automatic seizure detection in EEG signals,’’ Biomed. Signal Process.
Control, vol. 18, pp. 179–185, Apr. 2015.

‘‘Evaluation of

[20] D. Hernández, L. Trujillo, E. Z-Flores, O. Villanueva,

[19] I. Mporas, V. Tsirka, E. Zacharaki, M. Koutroumanidis,

and
V. Megalooikonomou,
time and frequency domain
features for seizure detection from combined EEG and ECG signals,’’ in
Proc. 7th Int. Conf. Pervasive Technol. Rel. Assist. Environ., 2014, p. 28.
and
O. Romo-Fewell, ‘‘Detecting epilepsy in EEG signals using time,
frequency and time-frequency domain features,’’ in Computer Science
and Engineering—Theory and Applications. Springer, 2018, pp. 167–182.
[21] B. Boashash and S. Ouelha, ‘‘Automatic signal abnormality detection using
time-frequency features and machine learning: A newborn EEG seizure
case study,’’ Knowl. Based Syst., vol. 106, pp. 38–50, Aug. 2016.

[22] G. Chen, ‘‘Automatic EEG seizure detection using dual-tree complex
features,’’ Expert Syst. Appl., vol. 41, no. 5,

wavelet-Fourier
pp. 2391–2394, 2014.

[23] O. Faust, U. R. Acharya, H. Adeli, and A. Adeli, ‘‘Wavelet-based EEG
processing for computer-aided seizure detection and epilepsy diagnosis,’’
Seizure-Eur. J. Epilepsy, vol. 26, pp. 56–64, Mar. 2015.

[24] S. Panahi, Z. Aram, S. Jafari, J. Ma, and J. Sprott, ‘‘Modeling of epilepsy
based on chaotic artiﬁcial neural network,’’ Chaos, Solitons Fractals,
vol. 105, pp. 150–156, Dec. 2017.

[25] A. Tharwat, M. Elhoseny, A. E. Hassanien, T. Gabel, and A. Kumar,
‘‘Intelligent Bézier curve-based path planning model using chaotic particle
swarm optimization algorithm,’’ Cluster Comput., pp. 1–22, 2018.

[26] J. E.

Jacob, V. V. Sreelatha, T.

and
D. G. Yohannan, ‘‘Diagnosis of epilepsy from interictal EEGs based
on chaotic and wavelet transformation,’’ Analog Integr. Circuits Signal
Process., vol. 89, pp. 131–138, Oct. 2016.

Iype, G. K. Nair,

[27] S. M. S. Alam and M. I. H. Bhuiyan, ‘‘Detection of seizure and epilepsy
using higher order statistics in the EMD domain,’’ IEEE J. Biomed. Health
Inform., vol. 17, no. 2, pp. 312–318, Mar. 2013.

[28] F. Riaz, A. Hassan, S. Rehman, I. K. Niazi, and K. Dremstrup, ‘‘EMD-
based temporal and spectral features for the classiﬁcation of EEG signals
using supervised learning,’’ IEEE Trans. Neural Syst. Rehabil. Eng.,
vol. 24, no. 1, pp. 28–35, Jan. 2016.

[29] A. Temko, G. Lightbody, E. M. Thomas, G. B. Boylan, and W. Marnane,
‘‘Instantaneous measure of EEG channel importance for improved patient-
adaptive neonatal seizure detection,’’ IEEE Trans. Biomed. Eng., vol. 59,
no. 3, pp. 717–727, Mar. 2012.

[30] R. S. Fisher and H. E. Scharfman, ‘‘How can we identify ictal and interictal
abnormal activity?’’ in Issues in Clinical Epileptology: A View From the
Bench. Springer, 2014, pp. 3–23.

[31] Q. Zhu and A. T. Azar, Complex System Modelling and Control Through

Intelligent Soft Computations. Springer, 2015.

[32] A. Yadollahpour and M. Jalilifar, ‘‘Seizure prediction methods: A review
of the current predicting techniques,’’ Biomed. Pharmacol. J., vol. 7, no. 1,
pp. 153–162, 2015.

[33] A. Subasi, J. Kevric, and M. A. Canbaz, ‘‘Epileptic seizure detection using
hybrid machine learning methods,’’ Neural Comput. Appl., pp. 1–9, 2017.
[34] N. Arunkumar et al., ‘‘Classiﬁcation of focal and non focal EEG using
entropies,’’ Pattern Recognit. Lett., vol. 94, pp. 112–117, Jul. 2017.
[35] M. Li, W. Chen, and T. Zhang, ‘‘Automatic epileptic EEG detection using
DT-CWT-based non-linear features,’’ Biomed. Signal Process. Control,
vol. 34, pp. 114–125, Apr. 2017.

[36] G. Wang, Z. Sun, R. Tao, K. Li, G. Bao, and X. Yan, ‘‘Epileptic seizure
detection based on partial directed coherence analysis,’’ IEEE J. Biomed.
Health Inform., vol. 20, no. 3, pp. 873–879, May 2016.

[37] J. Wei, F. Meng, and N. Arunkumar, ‘‘A personalized authoritative user-
based recommendation for social tagging,’’ Future Gener. Comput. Syst.,
vol. 86, pp. 355–361, Sep. 2018.

[38] A. Bhattacharyya, R. B. Pachori, A. Upadhyay, and U. R. Acharya,
‘‘Tunable-Q wavelet transform based multiscale entropy measure for auto-
mated classiﬁcation of epileptic EEG signals,’’ Appl. Sci., vol. 7, no. 4,
p. 385, 2017.

[39] J. Engel, Seizures and Epilepsy, vol. 83. London, U.K.: Oxford Univ. Press,

2013.

[40] S. Shorvon, R. Guerrini, M. Cook, and S. Lhatoo, Oxford Textbook of
Epilepsy and Epileptic Seizures. London, U.K.: Oxford Univ. Press, 2012.
[41] A. T. Berg et al., ‘‘Revised terminology and concepts for organization of
seizures and epilepsies: Report of the ILAE commission on classiﬁcation
and terminology, 2005–2009,’’ Epilepsia, vol. 51, no. 4, pp. 676–685,
2010.

[42] I. E. Scheffer, S. F. Berkovic, G. Capovilla, M. B. Connolly,
L. Guilhoto, and E. Hirsch. The Organization of
the Epilepsies:
Report of the ILAE Commission on Classiﬁcation and Terminology.
Accessed:
https://pdfs.
semanticscholar.org/df6f/cd6ebbf34f51212a5124fce4dbcbb701dea6.pdf

[Online]. Available:

2018.

Jun.

28,

[43] C. Liu and N. Arunkumar, ‘‘Risk prediction and evaluation of transna-
tional transmission of ﬁnancial crisis based on complex network,’’ Cluster
Comput., pp. 1–7, 2018.

[44] A. Russo, M. Duchowny, A. Boni, M. Giannotta, M. Filippini, and
G. Gobbi, ‘‘West syndrome in three patients with brain injury and a benign
course,’’ Epilepsy Behav. Case Rep., vol. 8, pp. 35–39, Mar. 2017.
[45] M. M. Basha, A. Alqallaf, and A. K. Shah, ‘‘Drug-induced EEG pattern
predicts effectiveness of ketamine in treating refractory status epilepticus,’’
Epilepsia, vol. 56, no. 4, pp. e44–e48, 2015.

[46] R. G. Andrzejak, K. Schindler, and C. Rummel, ‘‘Nonrandomness,
nonlinear dependence, and nonstationarity of electroencephalographic
recordings from epilepsy patients,’’ Phys. Rev. E, Stat. Phys. Plasmas
Fluids Relat. Interdiscip. Top., vol. 86, no. 4, p. 046206, 2012.

[47] S. Marsland, Machine Learning: An Algorithmic Perspective. Boca Raton,

FL, USA: CRC Press, 2015.

VOLUME 6, 2018

49319

[48] F. Mormann, R. G. Andrzejak, C. E. Elger, and K. Lehnertz, ‘‘Seizure
prediction: The long and winding road,’’ Brain, vol. 130, no. 2,
pp. 314–333, 2006.

[49] C. J. Stam and E. C. W. van Straaten, ‘‘The organization of physiological
brain networks,’’ Clin. Neurophysiol., vol. 123, no. 6, pp. 1067–1087,
2012.

[50] M. J. Cook et al., ‘‘Prediction of seizure likelihood with a long-term,
implanted seizure advisory system in patients with drug-resistant epilepsy:
A ﬁrst-in-man study,’’ Lancet Neurol., vol. 12, no. 6, pp. 563–571, 2013.
[51] K. Lehnertz et al., ‘‘Its possible use for interictal focus localization, seizure
anticipation, and prevention: Nonlinear EEG analysis in epilepsy,’’ J. Clin.
Neurophysiol., vol. 18, no. 3, pp. 209–222, 2001.

[52] S. Sarbadhikari and K. Chakrabarty, ‘‘Chaos in the brain: A short review
alluding to epilepsy, depression, exercise and lateralization,’’ Med. Eng.
Phys., vol. 23, no. 7, pp. 447–457, 2001.

[53] A. L. Brewster, K. Marzec, A. Hairston, M. Ho, A. E. Anderson, and
Y. C. Lai, ‘‘Early cardiac electrographic and molecular remodeling in a
model of status epilepticus and acquired epilepsy,’’ Epilepsia, vol. 57,
no. 11, pp. 1907–1915, 2016.

[54] N. Ellenrieder, B. Frauscher, F. Dubeau, and J. Gotman, ‘‘Interaction
with slow waves during sleep improves discrimination of physiologic and
pathologic high-frequency oscillations (80–500 Hz),’’ Epilepsia, vol. 57,
no. 6, pp. 869–878, 2016.

[55] M. Sharma, A. Dhere, R. B. Pachori, and U. R. Acharya, ‘‘An auto-
matic detection of focal EEG signals using new class of time–frequency
localized orthogonal wavelet ﬁlter banks,’’ Knowl. Based Syst., vol. 118,
pp. 217–227, Feb. 2017.

[56] S. Chen, X. Zhang, and Z. Yang, ‘‘Epileptic seizure detection by
combining robust-principal component analysis and least square-support
vector machine,’’ Int. J. Imag. Syst. Technol., vol. 27, no. 4, pp. 368–375,
2017.

[57] U. R. Acharya, H. Fujita, V. K. Sudarshan, S. Bhat, and J. E. Koh,
‘‘Application of entropies for automated diagnosis of epilepsy using EEG
signals: A review,’’ Knowl. Based Syst., vol. 88, pp. 85–96, Nov. 2015.

[58] X. Du, S. Dua, R. U. Acharya, and C. K. Chua, ‘‘Classiﬁcation of epilepsy
using high-order spectra features and principle component analysis,’’
J. Med. Syst., vol. 36, no. 3, pp. 1731–1743, 2012.

[59] P. Ashokkumar, N. Arunkumar, and S. Don, ‘‘Intelligent optimal route
recommendation among heterogeneous objects with keywords,’’ Comput.
Elect. Eng., vol. 68, pp. 526–535, May 2018.

[60] R. Sharma, R. B. Pachori, and S. Gautam, ‘‘Empirical mode decomposition
based classiﬁcation of focal and non-focal seizure EEG signals,’’ in Proc.
Int. Conf. Med. Biometrics, 2014, pp. 135–140.

[61] E. Abdulhay, N. Arunkumar, K. Narasimhan, E. Vellaiappan, and
V. Venkatraman, ‘‘Gait and tremor investigation using machine learning
techniques for the diagnosis of Parkinson disease,’’ Future Gener. Comput.
Syst., vol. 83, pp. 366–373, Jun. 2018.

[62] A. Hussein, S. Hashim, A. A. Aziz, F. Rokhani, and W. W. Adnan, ‘‘Auto-
mated and high accuracy out-of-hospital heart diseases early detection
system,’’ Int. J. Cardiol., vol. 249, pp. S9–S10, Dec. 2017.

[63] S. Adler et al., ‘‘Novel surface features for automated detection of focal
cortical dysplasias in paediatric epilepsy,’’ NeuroImage, Clin., vol. 14,
pp. 18–27, Jan. 2017.

[64] M. Vardhana, N. Arunkumar, S. Lasrado, E. Abdulhay,

and
G. Ramírez-González, ‘‘Convolutional neural network for bio-medical
image segmentation with hardware acceleration,’’ Cogn. Syst. Res.,
vol. 50, pp. 10–14, Aug. 2018.

[65] H. Niknazar, K. Maghooli, and A. M. Nasrabadi, ‘‘Epileptic seizure predic-
tion using statistical behavior of local extrema and fuzzy logic system,’’ Int.
J. Comput. Appl., vol. 113, no. 2, pp. 24–30, 2015.

[66] B. Direito, C. Teixeira, B. Ribeiro, M. Castelo-Branco, F. Sales, and
A. Dourado, ‘‘Modeling epileptic brain states using EEG spectral anal-
ysis and topographic mapping,’’ J. Neurosci. Methods, vol. 210, no. 2,
pp. 220–229, 2012.

[67] R. T. Schirrmeister et al., ‘‘Deep learning with convolutional neural
networks for EEG decoding and visualization,’’ Hum. Brain Mapping,
vol. 38, no. 11, pp. 5391–5420, 2017.

[68] U. R. Acharya, S. L. Oh, Y. Hagiwara, J. H. Tan, and H. Adeli, ‘‘Deep
convolutional neural network for the automated detection and diagnosis of
seizure using EEG signals,’’ Comput. Biol. Med., vol. 100, pp. 270–278,
Sep. 2017.

[69] D. Spencer, ‘‘B (I) RD watching: A way to stratify seizure risk?’’ Epilepsy

Currents, vol. 14, no. 6, pp. 341–342, 2014.

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

[70] M. T. Salam, S. Desgent, S. Duss, L. Carmant, D. K. Nguyen, and
M. Sawan, ‘‘New subdural electrode contacts for intracerebral electroen-
cephalographic recordings: Comparative studies on neural signal recording
in vivo,’’ in Proc. IEEE Biomed. Circuits Syst. Conf. (BioCAS), Nov. 2011,
pp. 241–244.

[71] A. Eftekhar, W. Juffali, J. El-Imad, T. G. Constandinou, and C. Toumazou,
‘‘Ngram-derived pattern recognition for the detection and prediction of
epileptic seizures,’’ PLoS ONE, vol. 9, no. 6, p. e96235, Jun. 2014.
[72] P. van Mierlo et al., ‘‘Functional brain connectivity from EEG in epilepsy:
Seizure prediction and epileptogenic focus localization,’’ Prog. Neurobiol.,
vol. 121, pp. 19–35, Oct. 2014.

[73] A. Schulze-Bonhage, H. Feldwisch-Drentrup, and M. Ihle, ‘‘The role of
high-quality EEG databases in the improvement and assessment of seizure
prediction methods,’’ Epilepsy Behav., vol. 22, pp. S88–S93, Dec. 2011.

[74] J. J. Howbert et al., ‘‘Forecasting seizures in dogs with naturally occurring

epilepsy,’’ PLoS ONE, vol. 9, no. 1, p. e81920, Jan. 2014.

[75] B. H. Brinkmann et al., ‘‘Forecasting seizures using intracranial EEG
measures and SVM in naturally occurring canine epilepsy,’’ PLoS ONE,
vol. 10, no. 8, p. e0133900, 2015.

[76] K. A. Davis et al., ‘‘A novel implanted device to wirelessly record and
analyze continuous intracranial canine EEG,’’ Epilepsy Res., vol. 96,
pp. 116–122, Sep. 2011.

[77] C. Guerrero-Mosquera, A. M. Trigueros, and A. Navia-Vazquez, ‘‘EEG
signal processing for epilepsy,’’ in Epilepsy-Histological, Electroen-
cephalographic and Psychological Aspects. Vukovar, Croatia: InTech,
2012.

[78] M. Chaumon, D. V. M. Bishop, and N. A. Busch, ‘‘A practical guide to
the selection of independent components of the electroencephalogram for
artifact correction,’’ J. Neurosci. Methods, vol. 250, pp. 47–63, Jul. 2015.
[79] M. Vardhana, N. Arunkumar, E. Abdulhay, and P. Vishnuprasad, ‘‘IoT
based real time traﬁc control using cloud computing,’’ Cluster Comput.,
pp. 1–10, 2018.

[80] A. K. Maddirala and R. A. Shaik, ‘‘Removal of EOG artifacts from
single channel EEG signals using combined singular spectrum analysis and
adaptive noise canceler,’’ IEEE Sensors J., vol. 16, no. 23, pp. 8279–8287,
Dec. 2016.

[81] M. De Vos et al., ‘‘Automated artifact removal as preprocessing reﬁnes
neonatal seizure detection,’’ Clin. Neurophysiol., vol. 122, no. 12,
pp. 2345–2354, 2011.

[82] S. O’Regan, S. Faul, and W. Marnane, ‘‘Automatic detection of EEG
artefacts arising from head movements using EEG and gyroscope signals,’’
Med. Eng. Phys., vol. 35, no. 7, pp. 867–874, 2013.

[83] D. Dudkowski, S. Jafari, T. Kapitaniak, N. V. Kuznetsov, G. A. Leonov, and
A. Prasad, ‘‘Hidden attractors in dynamical systems,’’ Phys. Rep., vol. 637,
pp. 1–50, Jun. 2016.

[84] B. M. Bogdanoff, C. R. Stafford, L. Green, and C. F. Gonzalez, ‘‘Comput-
erized transaxial tomography in the evaluation of patients with focal
epilepsy,’’ Neurology, vol. 25, no. 11, p. 1013, 1975.

[85] U. R. Acharya, S. V. Sree, G. Swapna, R. J. Martis, and J. S. Suri,
‘‘Automated EEG analysis of epilepsy: A review,’’ Knowl.-Based Syst.,
vol. 45, pp. 147–165, Jun. 2013.

[86] G. Meng, ‘‘Construction of employee training program evaluation system
of three exponential forecast based on sliding window,’’ Cluster Comput.,
pp. 1–7, 2018.

[87] L. Guo, D. Rivero, and A. Pazos, ‘‘Epileptic seizure detection using
multiwavelet transform based approximate entropy and artiﬁcial neural
networks,’’ J. Neurosci. Methods, vol. 193, no. 1, pp. 156–163, 2010.
[88] N. Arunkumar, K. R. Kumar, and V. Venkataraman, ‘‘Automatic detec-
tion of epileptic seizures using permutation entropy, Tsallis entropy and
Kolmogorov complexity,’’ J. Med. Imag. Health Inform., vol. 6, no. 2,
pp. 526–531, 2016.

[89] A. C. Schomer and F. W. Drislane, ‘‘Severe hemispatial neglect as a
manifestation of seizures and nonconvulsive status epilepticus: Utility
of prolonged EEG monitoring,’’ J. Clin. Neurophysiol., vol. 32, no. 2,
pp. e4–e7, 2015.

[90] Z. Tareq, B. Zaidan, A. Zaidan, and M. Suzani, ‘‘A review of disability
EEG based wheelchair control system: Coherent taxonomy, open chal-
lenges and recommendations,’’ Comput. Methods Programs Biomed.,
Jun. 2018.

[91] A. F. Hussein, A. Kumar, M. Burbano-Fernandez, G. Ramírez-González,
E. Abdulhay, and V. H. C. de Albuquerque, ‘‘An automated remote
cloud-based heart rate variability monitoring system,’’ IEEE Access,
May 2018.

49320

VOLUME 6, 2018

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

[92] R. Jenke, A. Peer, and M. Buss, ‘‘Feature extraction and selection for
emotion recognition from EEG,’’ IEEE Trans. Affect. Comput., vol. 5,
no. 3, pp. 327–339, Jul. 2014.

[93] M. Sarvaghad-Moghaddam, A. A. Orouji, Z. Ramezani, M. Elhoseny, and
A. Farouk, ‘‘Modelling the spice parameters of SOI MOSFET using a
combinational algorithm,’’ Cluster Comput., pp. 1–10, 2018.

[94] M. Diykh, Y. Li, and P. Wen, ‘‘EEG sleep stages classiﬁcation based on
time domain features and structural graph similarity,’’ IEEE Trans. Neural
Syst. Rehabil. Eng., vol. 24, no. 11, pp. 1159–1168, Nov. 2016.

[95] H.-Y. Huang and P.-C. Lo, ‘‘EEG dynamics of experienced Zen meditation
practitioners probed by complexity index and spectral measure,’’ J. Med.
Eng. Technol., vol. 33, no. 4, pp. 314–321, 2009.

[96] A. F. Hussein, S. J. Hashim, A. F. A. Aziz, F. Z. Rokhani, and
W. A. W. Adnan, ‘‘A real time ECG data compression scheme for enhanced
bluetooth low energy ECG system power consumption,’’ J. Ambient Intell.
Humanized Comput., pp. 1–14, 2017.

[97] B. Hjorth, ‘‘EEG analysis based on time domain properties,’’ Electroen-
cephalogr. Clin. Neurophysiol., vol. 29, no. 3, pp. 306–310, 1970.
[98] S. M. Kuo, B. H. Lee, and W. Tian, Real-Time Digital Signal Processing:
Fundamentals, Implementations and Applications. Hoboken, NJ, USA:
Wiley, 2013.

[99] S. Ghosh-Dastidar, H. Adeli, and N. Dadmehr, ‘‘Principal component
analysis-enhanced cosine radial basis function neural network for robust
epilepsy and seizure detection,’’ IEEE Trans. Biomed. Eng., vol. 55, no. 2,
pp. 512–518, Feb. 2008.

[100] X. Chen, L. Pang, P. Guo, X. Sun, Z. Xue, and N. Arunkumar, ‘‘New upper
degree of freedom in transmission system based on wireless G-MIMO
communication channel,’’ Cluster Comput., pp. 1–9, 2017.

[101] A. K. AlZubaidi, F. B. Sideseq, A. Faeq, and M. Basil, ‘‘Computer
aided diagnosis in digital pathology application: Review and perspective
approach in lung cancer classiﬁcation,’’ in Proc. Annu. Conf. New Trends
Inf. Commun. Technol. Appl. (NTICT), 2017, pp. 219–224.

[102] L. Cao, K. Chua, W. Chong, H. Lee, and Q. Gu, ‘‘A comparison of PCA,
KPCA and ICA for dimensionality reduction in support vector machine,’’
Neurocomputing, vol. 55, nos. 1–2, pp. 321–336, 2003.

[103] A. Widodo and B.-S. Yang, ‘‘Application of nonlinear feature extraction
and support vector machines for fault diagnosis of induction motors,’’
Expert Syst. Appl., vol. 33, no. 1, pp. 241–250, 2007.

[104] F. Moeller, P. LeVan, and J. Gotman, ‘‘Independent component analysis
(ICA) of generalized spike wave discharges in fMRI: Comparison with
general linear model-based EEG-fMRI,’’ Human Brain Mapping, vol. 32,
no. 2, pp. 209–217, 2011.

[105] E. Abdulhay, M. A. Mohammed, D. A. Ibrahim, N. Arunkumar, and
V. Venkatraman, ‘‘Computer aided solution for automatic segmenting
and measurements of blood leucocytes using static microscope images,’’
J. Med. Syst., vol. 42, no. 4, p. 58, 2018.

[106] A. Fielding, Cluster and Classiﬁcation Techniques for the Biosciences.

Cambridge, U.K.: Cambridge Univ. Press, 2007.

[107] G. Ouyang, J. Li, X. Liu, and X. Li, ‘‘Dynamic characteristics of absence
EEG recordings with multiscale permutation entropy analysis,’’ Epilepsy
Res., vol. 104, no. 4, pp. 246–252, 2013.

[108] A. Pikovsky, M. Rosenblum, J. Kurths, and J. Kurths, Synchronization:
A Universal Concept in Nonlinear Sciences, vol. 12. Cambridge, U.K.:
Cambridge Univ. Press, 2003.

[109] K. Polat and S. Güneş, ‘‘Classiﬁcation of epileptiform EEG using a hybrid
system based on decision tree classiﬁer and fast Fourier transform,’’ Appl.
Math. Comput., vol. 187, no. 2, pp. 1017–1026, 2007.

[110] M. G. Frei et al., ‘‘Controversies in epilepsy: Debates held during the
fourth international workshop on seizure prediction,’’ Epilepsy Behav.,
vol. 19, no. 1, pp. 4–16, 2010.

[111] R. Hamza, K. Muhammad, A. Nachiappan, and G. Ramírez-González,
‘‘Hash based encryption for keyframes of diagnostic hysteroscopy,’’ IEEE
Access, Nov. 2017.

[112] P. J. Franaszczuk, G. K. Bergey, and M. J. Kamiński, ‘‘Analysis of mesial
temporal seizure onset and propagation using the directed transfer function
method,’’ Electroencephalogr. Clin. Neurophysiol., vol. 91, pp. 413–427,
1994.

[113] S. L. Fernandes, V. P. Gurupur, N. R. Sunder, N. Arunkumar, and S. Kadry,
‘‘A novel nonintrusive decision support approach for heart rate measure-
ment,’’ Pattern Recognit. Lett., 2017.

[114] A. F. Hussein, S. J. Hashim, A. F. A. Aziz, F. Z. Rokhani, and
W. A. W. Adnan, ‘‘Performance evaluation of time–frequency distributions
for ECG signal analysis,’’ J. Med. Syst., vol. 42, p. 15, 2018.

[115] M. Elhoseny, G. Ramírez-González, O. M. Abu-Elnasr, S. A. Shawkat,
N. Arunkumar, and A. Farouk, ‘‘Secure medical data transmission model
for IoT-based healthcare systems,’’ IEEE Access, vol. 6, pp. 20596–20608,
2018.

[116] K. Tzimourta, A. Tzallas, N. Giannakeas, L. Astrakas, D. Tsalikakis, and
M. Tsipouras, ‘‘Epileptic seizures classiﬁcation based on long-term EEG
signal wavelet analysis,’’ in Precision Medicine Powered by pHealth and
Connected Health. Springer, 2018, pp. 165–169.

[117] E. J. Candès, ‘‘The restricted isometry property and its implications
for compressed sensing,’’ Comp. Rendus Math., vol. 346, nos. 9–10,
pp. 589–592, May 2008.

[118] C. Stamoulis, L. J. Gruber, D. L. Schomer, and B. S. Chang, ‘‘High-
frequency neuronal network modulations encoded in scalp EEG precede
the onset of focal seizures,’’ Epilepsy Behav., vol. 23, no. 4, pp. 471–480,
2012.

[119] M. Kuisma and P. Silventoinen, ‘‘Using spectrograms in EMI-analysis-an
overview,’’ in Proc. 20th Annu. IEEE Appl. Power Electron. Conf. Expo.
(APEC), Mar. 2005, pp. 1953–1958.

[120] P. Flandrin, P. Gonçalvès, and G. Rilling, ‘‘EMD equivalent ﬁlter banks,
from interpretation to applications,’’ in Hilbert-Huang Transform and its
Applications. Singapore: World Scientiﬁc, 2014, pp. 99–116.

[121] R. B. Pachori, ‘‘Discrimination between ictal and seizure-free EEG
signals using empirical mode decomposition,’’ Res. Lett. Signal Process.,
vol. 8, p. 14, 2008.

[122] R. J. Oweis and E. W. Abdulhay, ‘‘Seizure classiﬁcation in EEG signals
utilizing Hilbert–Huang transform,’’ BioMed. Eng. Online, vol. 10, p. 38,
May 2011.

[123] Z. Wu and N. E. Huang, ‘‘Ensemble empirical mode decomposition:
A noise-assisted data analysis method,’’ Adv. Adapt. Data Anal., vol. 1,
no. 1, pp. 1–41, 2008.

[124] E. Abdulhay, V. Elamaran, M. Chandrasekar, V. Balaji,

and
K. Narasimhan, ‘‘Automated diagnosis of epilepsy from EEG signals
using ensemble learning approach,’’ Pattern Recognit. Lett., 2017.
[125] O. Faust and M. G. Bairy, ‘‘Nonlinear analysis of physiological signals:

A review,’’ J. Mech. Med. Biol., vol. 12, no. 4, p. 1240015, 2012.

[126] I. Chouvarda et al., ‘‘Assessment of the EEG complexity during activa-
tions from sleep,’’ Comput. Methods Programs Biomed., vol. 104, no. 3,
pp. e16–e28, 2011.

[127] H. Sakai, ‘‘Statistical analysis of Pisarenko’s method for sinusoidal
frequency estimation,’’ IEEE Trans. Acoust., Speech, Signal Process.,
vol. ASSP-32, no. 1, pp. 95–101, Feb. 1984.

[128] J. V. Stone, Information Theory: A Tutorial Introduction. Sebtel Press,

2015.

[129] N. Arunkumar, K. R. Kumar, and V. Venkataraman, ‘‘Entropy features
for focal EEG and non focal EEG,’’ J. Comput. Sci., vol. 27, pp. 440–444,
Jul. 2018.

[130] L. Guo, D. Rivero, J. Dorado, J. R. Rabuñal, and A. Pazos, ‘‘Automatic
epileptic seizure detection in EEGs based on line length feature and artiﬁ-
cial neural networks,’’ J. Neurosci. Methods, vol. 191, no. 1, pp. 101–109,
2010.

[131] S. Motamedi-Fakhr, M. Moshreﬁ-Torbati, M. Hill, C. M. Hill, and
P. R. White, ‘‘Signal processing techniques applied to human sleep EEG
signals—A review,’’ Biomed. Signal Process. Control, vol. 10, pp. 21–33,
Mar. 2014.

[132] N. Arunkumar, K. R. Kumar, and V. Venkataraman, ‘‘A moving window
approximate entropy in wavelet framework for automatic detection of the
onset of epileptic seizures,’’ Biomed. Res., vol. 29, pp. 161–170, Jun. 2017.
[133] P. Li, C. Karmakar, C. Yan, M. Palaniswami, and C. Liu, ‘‘Classiﬁcation
of 5-s epileptic eeg recordings using distribution entropy and sample
entropy,’’ Frontiers Physiol., vol. 7, p. 136, Apr. 2016.

[134] D. Abásolo, R. Hornero, P. Espino, D. Alvarez, and J. Poza, ‘‘Entropy
analysis of the EEG background activity in Alzheimer’s disease patients,’’
Physiol. Meas., vol. 27, no. 3, p. 241, 2006.

[135] B. K. Shivamoggi, Nonlinear Dynamics and Chaotic Phenomena:

An Introduction, vol. 103. Springer, 2014.

[136] S. Pincus, ‘‘Approximate entropy (ApEn) as a complexity measure,’’

Chaos, Interdiscipl. J. Nonlinear Sci., vol. 5, no. 1, pp. 110–117, 1995.

[137] M. Costa, A. L. Goldberger, and C.-K. Peng, ‘‘Multiscale entropy analysis
of biological signals,’’ Phys. Rev. E, Stat. Phys. Plasmas Fluids Relat.
Interdiscip. Top., vol. 71, no. 2, p. 021906, 2005.

[138] M. Zanin, L. Zunino, O. A. Rosso, and D. Papo, ‘‘Permutation entropy and
its main biomedical and econophysics applications: A review,’’ Entropy,
vol. 14, no. 8, pp. 1553–1577, 2012.

VOLUME 6, 2018

49321

[139] M. Thilagaraj, M. P. Rajasekaran, and N. A. Kumar, ‘‘Tsallis entropy:
As a new single feature with the least computation time for classiﬁcation
of epileptic seizures,’’ Cluster Comput., pp. 1–9, 2018.

[140] N. Arunkumar, K. R. Kumar, and V. Venkataraman, ‘‘Automatic detection
of epileptic seizures using new entropy measures,’’ J. Med. Imag. Health
Inform., vol. 6, no. 3, pp. 724–730, Jun. 2016.

[141] R. Sharma and R. B. Pachori, ‘‘Automated classiﬁcation of focal and non-
focal EEG signals based on bivariate empirical mode decomposition,’’ in
Biomedical Signal and Image Processing in Patient Care. Hershey, PA,
USA: IGI Global, 2018, pp. 13–33.

[142] A. E. Eiben, ‘‘Multiparent recombination in evolutionary computing,’’ in
Advances in Evolutionary Computing. Springer, 2003, pp. 175–192.
[143] C.-L. Huang and C.-J. Wang, ‘‘A GA-based feature selection and parame-
ters optimizationfor support vector machines,’’ Expert Syst. Appl., vol. 31,
no. 2, pp. 231–240, 2006.

[144] A. F. Hussein, N. Arunkumar, G. Ramírez-González, E. Abdulhay,
J. M. R. Tavares, and V. H. C. de Albuquerque, ‘‘A medical records
managing and securing blockchain based system supported by a genetic
algorithm and discrete wavelet transform,’’ Cogn. Syst. Res., vol. 52,
pp. 1–11, Dec. 2018.

[145] M. Z. Parvez, M. Paul, and M. Antolovich, ‘‘Detection of pre-stage of
epileptic seizure by exploiting temporal correlation of EMD decomposed
EEG signals,’’ J. Med. Bioeng., vol. 4, no. 2, pp. 110–116, 2015.

[146] W. Truccolo et al., ‘‘Single-neuron dynamics in human focal epilepsy,’’

Nature Neurosci., vol. 14, no. 5, p. 635, 2011.

[147] M. Zijlmans, J. Jacobs, Y. U. Kahn, R. Zelmann, F. Dubeau, and
J. Gotman, ‘‘Ictal and interictal high frequency oscillations in patients with
focal epilepsy,’’ Clin. Neurophysiol., vol. 122, no. 4, pp. 664–671, 2011.

[148] J. J. Niederhauser, R. Esteller, J. Echauz, G. Vachtsevanos, and
B. Litt, ‘‘Detection of seizure precursors from depth-EEG using a sign
periodogram transform,’’ IEEE Trans. Biomed. Eng., vol. 50, no. 4,
pp. 449–458, Apr. 2003.

[149] J. Mitra et al., ‘‘A multi-stage system for the automated detection of
epileptic seizures in neonatal EEG,’’ J. Clin. Neurophysiol. Ofﬁcial Publi-
cation Amer. Electroencephalogr. Soc., vol. 26, no. 4, pp. 218–226, 2009.
[150] L. Orosco, A. G. Correa, and E. Laciar, ‘‘A survey of performance and
techniques for automatic epilepsy detection,’’ J. Med. Biol. Eng., vol. 33,
no. 6, pp. 526–537, 2013.

[151] A. F. Rabbi and R. Fazel-Rezai, ‘‘A fuzzy logic system for seizure onset
detection in intracranial EEG,’’ Comput. Intell. Neurosci., vol. 2, p. 1,
2012.

[152] M. J. Cook et al., ‘‘Human focal seizures are characterized by populations
of ﬁxed duration and interval,’’ Epilepsia, vol. 57, no. 3, pp. 359–368,
Mar. 2016.

[153] S. Sargolzaei, M. Cabrerizo, M. Goryawala, A. S. Eddin, and
M. Adjouadi, ‘‘Scalp EEG brain functional connectivity networks in pedi-
atric epilepsy,’’ Comput. Biol. Med., vol. 56, pp. 158–166, Jan. 2015.
[154] C. Haegelen et al., ‘‘High-frequency oscillations, extent of surgical resec-
tion, and surgical outcome in drug-resistant focal epilepsy,’’ Epilepsia,
vol. 54, no. 5, pp. 848–857, 2013.

[155] F. Cong et al., ‘‘Frequency-response-based wavelet decomposition for
extracting children’s mismatch negativity elicited by uninterrupted sound,’’
J. Med. Biol. Eng., vol. 32, pp. 205–214, Jun. 2012.

[156] L. Chisci et al., ‘‘Real-time epileptic seizure prediction using AR models
and support vector machines,’’ IEEE Trans. Biomed. Eng., vol. 57, no. 5,
pp. 1124–1132, May 2010.

[157] C. Teixeira et al., ‘‘EPILAB: A software package for studies on the
prediction of epileptic seizures,’’ J. Neurosci. Methods, vol. 200, no. 2,
pp. 257–271, 2011.

[158] M. Bandarabadi, C. A. Teixeira, J. Rasekhi, and A. Dourado,
‘‘Epileptic seizure prediction using relative spectral power features,’’ Clin.
Neurophysiol., vol. 126, no. 2, pp. 237–248, 2015.

[159] C. A. Teixeira et al., ‘‘Epileptic seizure predictors based on computa-
tional intelligence techniques: A comparative study with 278 patients,’’
Comput. Methods Programs Biomed., vol. 114, no. 3, pp. 324–336,
2014.

[160] C. Teixeira, B. Direito, M. Bandarabadi, and A. Dourado, ‘‘Output regu-
larization of SVM seizure predictors: Kalman ﬁlter versus the ‘ﬁring
power’ method,’’ in Proc. Annu. Int. Conf. IEEE Eng. Med. Biol. Soc.
(EMBC), Aug. 2012, pp. 6530–6533.

[161] Y. Park, L. Luo, K. K. Parhi, and T. Netoff, ‘‘Seizure prediction with
spectral power of EEG using cost-sensitive support vector machines,’’
Epilepsia, vol. 52, no. 10, pp. 1761–1770, 2011.

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

[162] P. Karthick, H. Tanaka, H. M. Khoo, and J. Gotman, ‘‘Prediction of
secondary generalization from a focal onset seizure in intracerebral EEG,’’
Clin. Neurophysiol., vol. 129, no. 5, pp. 1030–1040, 2018.

[163] E. Abdulhay, V. Elamaran, N. Arunkumar, and V. Venkataraman, ‘‘Fault-
tolerant medical imaging system with quintuple modular redundancy
(QMR) conﬁgurations,’’ J. Ambient Intell. Humanized Comput., pp. 1–13,
2018.

[164] A. B. Das and M. I. H. Bhuiyan, ‘‘Discrimination and classiﬁca-
tion of focal and non-focal EEG signals using entropy-based features
in the EMD-DWT domain,’’ Biomed. Signal Process. Control, vol. 29,
pp. 11–21, Aug. 2016.

[165] Y. Xia, W. Zhou, C. Li, Q. Yuan, and S. Geng, ‘‘Seizure detection
approach using S-transform and singular value decomposition,’’ Epilepsy
Behav., vol. 52, pp. 187–193, Nov. 2015.

[166] Y. Song and J. Zhang, ‘‘Discriminating preictal and interictal brain states
in intracranial EEG by sample entropy and extreme learning machine,’’
J. Neurosci. Methods, vol. 257, pp. 45–54, Jan. 2016.

[167] Q. Yuan, W. Zhou, Y. Liu, and J. Wang, ‘‘Epileptic seizure detection with
linear and nonlinear features,’’ Epilepsy Behav., vol. 24, no. 4, pp. 415–421,
2012.

[168] S. Xie and S. Krishnan, ‘‘Wavelet-based sparse functional linear model
with applications to EEGs seizure detection and epilepsy diagnosis,’’ Med.
Biol. Eng., Comput., vol. 51, nos. 1–2, pp. 49–60, 2013.

[169] D. Rangaprakash, ‘‘Connectivity analysis of multichannel EEG signals
using recurrence based phase synchronization technique,’’ Comput. Biol.
Med., vol. 46, pp. 11–21, Mar. 2014.

[170] A. Pathak, A. Ramesh, A. Mitra, and K. Majumdar, ‘‘Automatic seizure
detection by modiﬁed line length and Mahalanobis distance function,’’
Biomed. Signal Process. Control, vol. 44, pp. 279–287, 2018.

[171] A. S. Zandi, M. Javidan, G. A. Dumont, and R. Tafreshi, ‘‘Automated real-
time epileptic seizure detection in scalp EEG recordings using an algorithm
based on wavelet packet transform,’’ IEEE Trans. Biomed. Eng., vol. 57,
no. 7, pp. 1639–1651, Jul. 2010.

[172] A. Bhattacharyya, M. Sharma, R. B. Pachori, P. Sircar, and U. R. Acharya,
‘‘A novel approach for automated detection of focal EEG signals using
empirical wavelet transform,’’ Neural Comput. Appl., vol. 29, no. 8,
pp. 47–57, 2018.

[173] H. Soleimani-B, C. Lucas, B. N. Araabi, and L. Schwabe, ‘‘Adaptive
prediction of epileptic seizures from intracranial recordings,’’ Biomed.
Signal Process. Control, vol. 7, no. 5, pp. 456–464, 2012.

[174] N. Sriraam and S. Raghu, ‘‘Classiﬁcation of focal and non focal epileptic
seizures using multi-features and SVM classiﬁer,’’ J. Med. Syst., vol. 41,
no. 10, p. 160, 2017.

[175] H. Khan, L. Marcuse, M. Fields, K. Swann, and B. Yener, ‘‘Focal onset
seizure prediction using convolutional networks,’’ IEEE Trans. Biomed.
Eng., vol. 65, no. 9, pp. 2109–2118, Sep. 2017.

[176] J. Martinez-del-Rincon et al., ‘‘Non-linear classiﬁers applied to EEG
analysis for epilepsy seizure detection,’’ Expert Syst. Appl., vol. 86,
pp. 99–112, Nov. 2017.

[177] M. Niknazar, S. R. Mousavi, B. V. Vahdat, and M. Sayyah, ‘‘A new
framework based on recurrence quantiﬁcation analysis for epileptic seizure
detection,’’ IEEE J. Biomed. Health Informat., vol. 17, no. 3, pp. 572–578,
May 2013.

[178] A. G. Correa, L. Orosco, P. Diez, and E. Laciar, ‘‘Automatic detection of
epileptic seizures in long-term EEG records,’’ Comput. Biol. Med., vol. 57,
pp. 66–73, Feb. 2015.

[179] Y. Liu, W. Zhou, Q. Yuan, and S. Chen, ‘‘Automatic seizure detection
using wavelet transform and SVM in long-term intracranial EEG,’’ IEEE
Trans. Neural Syst. Rehabil. Eng., vol. 20, no. 6, pp. 749–755, Nov. 2012.
[180] S. Deivasigamani, C. Senthilpari, and W. H. Yong, ‘‘Classiﬁcation of
focal and nonfocal EEG signals using ANFIS classiﬁer for epilepsy detec-
tion,’’ Int. J. Imag. Syst. Technol., vol. 26, no. 26, pp. 277–283, 2016.
[181] S. Chatterjee, S. Pratiher, and R. Bose, ‘‘Multifractal detrended ﬂuc-
tuation analysis based novel feature extraction technique for automated
detection of focal and non-focal electroencephalogram signals,’’ IET Sci.,
Meas., Technol., vol. 11, no. 8, pp. 1014–1021, 2017.

[182] P. Singh and R. B. Pachori, ‘‘Classiﬁcation of focal and nonfocal EEG
signals using features derived from Fourier-based rhythms,’’ J. Mech. Med.
Biol., vol. 17, no. 7, pp. 1740002-1–1740002-16, 2017.

[183] R. Panda, P. Khobragade, P. Jambhule, S. Jengthe, P. Pal, and T. Gandhi,
‘‘Classiﬁcation of EEG signal using wavelet transform and support vector
machine for epileptic seizure diction,’’ in Proc. Int. Conf. Syst. Med. Biol.
(ICSMB), 2010, pp. 405–408.

49322

VOLUME 6, 2018

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

[184] R. Sharma, M. Kumar, R. B. Pachori, and U. R. Acharya, ‘‘Decision
support system for focal EEG signals using tunable-Q wavelet transform,’’
J. Comput. Sci., vol. 20, pp. 52–60, May 2017.

[185] A. Aarabi and B. He, ‘‘A rule-based seizure prediction method for focal
neocortical epilepsy,’’ Clin. Neurophysiol., vol. 123, no. 6, pp. 1111–1122,
2012.

[186] R. Sharma, R. Pachori, and U. Acharya, ‘‘Application of entropy
measures on intrinsic mode functions for the automated identiﬁca-
tion of focal electroencephalogram signals,’’ Entropy, vol. 17, no. 2,
pp. 669–691, 2015.

[187] A. Bhattacharyya, R. B. Pachori, and U. R. Acharya, ‘‘Tunable-Q wavelet
transform based multivariate sub-band fuzzy entropy with application to
focal EEG signal analysis,’’ Entropy, vol. 19, no. 3, p. 99, 2017.

[188] M. Bedeeuzzaman, T. Fathima, Y. U. Khan, and O. Farooq, ‘‘Seizure
prediction using statistical dispersion measures of intracranial EEG,’’
Biomed. Signal Process. Control, vol. 10, pp. 338–341, Mar. 2014.
[189] W. Zhou, Y. Liu, Q. Yuan, and X. Li, ‘‘Epileptic seizure detection using
Lacunarity and Bayesian linear discriminant analysis in intracranial EEG,’’
IEEE Trans. Biomed. Eng., vol. 60, no. 12, pp. 3375–3381, Dec. 2013.

[190] H. Azami, A. Fernández, and J. Escudero, ‘‘Reﬁned multiscale fuzzy
entropy based on standard deviation for biomedical signal analysis,’’ Med.
Biol. Eng., Comput., vol. 55, no. 11, pp. 2037–2052, 2017.

[191] M. Gehlot, Y. Kumar, H. Meena, V. Bajaj, and A. Kumar, ‘‘EMD
based features for discrimination of focal and non-focal EEG signals,’’ in
Information Systems Design and Intelligent Applications. Springer, 2015,
pp. 85–93.

[192] V. Bajaj, K. Rai, A. Kumar, D. Sharma, and G. K. Singh, ‘‘Rhythm-based
features for classiﬁcation of focal and non-focal EEG signals,’’ IET Signal
Process., vol. 11, no. 6, pp. 743–748, 2017.

[193] J. R. Williamson, D. W. Bliss, D. W. Browne, and J. T. Narayanan,
‘‘Seizure prediction using EEG spatiotemporal correlation structure,’’
Epilepsy Behav., vol. 25, no. 2, pp. 230–238, 2012.

[194] K. Rai, V. Bajaj, and A. Kumar, ‘‘Novel feature for identiﬁcation of focal
EEG signals with K-means and fuzzy C-means algorithms,’’ in Proc. IEEE
Int. Conf. Digit. Signal Process. (DSP), Jul. 2015, pp. 412–416.

[195] G. Zhu, Y. Li, P. P. Wen, S. Wang, and M. Xi, ‘‘Epileptogenic focus
detection in intracranial EEG based on delay permutation entropy,’’ in
Proc. AIP Conf., 2013, pp. 31–36.

[196] T. Wu et al., ‘‘Automatic lateralization of temporal lobe epilepsy based
on MEG network features using support vector machines,’’ Complexity,
vol. 8, Feb. 2018, Art. no. 4325096.

Iraq,

AHMED FAEQ HUSSEIN (M’16)
received
the B.Sc. degree in electrical engineering from
Al-Mustansiriyah University,
in 1998,
the M.Sc. degree in computer engineering from the
University of Technology, Iraq, in 2004, and the
Ph.D. degree in computer and embedded system
engineering from Universiti Putra Malaysia
in 2018. He was a Senior Engineer at the Medical
Department, Ministry of Health, Iraq, until 2009,
the Bio-Medical
and has been a Lecturer at
Engineering Department, Al-Nahrain University, since 2009. His research
interests include bio-medical signal processing,
low energy Bluetooth
communication, and cloud-based application.

ARUNKUMAR N is with SASTRA University,
where he is active in research. He has published
several papers in engineering streams in various
top journals. He has been guiding several students
from various countries in their research works.

CHANDIMA GOMES received the degree
(Hons.) in physics from the University of Colombo
in 1993 and the Ph.D. degree from Uppsala
University, Sweden, in 1999. His post-doctoral
research on lightning protection and high voltage
engineering. He is currently a Professor of elec-
trical engineering and a Researcher in high voltage
engineering and lightning protection at Univer-
siti Putra Malaysia. He is also an expert
in
power and energy, electromagnetic interference
and compatibility, and occupational safety management. He was one of
the founders of the Centre for Electromagnetics and Lightning Protection
Research, Malaysia, and the ﬁrst Head of the Institute. He has held full-
time/adjunct/visiting professorship and lectureship in physics, engineering
and meteorology at universities based in Malaysia, Sri Lanka, USA,
Australia, Kazakhstan, Pakistan, Zambia, and Japan. He is a Senior Adviser
to the National Lightning Safety Institution, USA, and was the Chief Adviser
to African Centers for Lightning and Electromagnetics based in Uganda.
Being an engineering consultant for several companies in Asia and Africa.
He has over 20 years of international experience in designing lightning
protection systems and providing solutions for electromagnetic issues. He is
well known at international frontiers as a trainer of trainers and adviser
for entrepreneurship in several engineering subjects, including lightning,
electrical safety, and electromagnetism. He has conducted over 120 training
programs in 12 countries so far. He has published over 300 research papers
and several books on his expertise.

ABBAS K. ALZUBAIDI was born in Baghdad,
Iraq,
in 1979. He received the B.Sc. and
M.Sc. degrees in biomedical engineering from
Al-Nahrain University in 2001 and 2004, respec-
tively, and the Ph.D. degree in medical informa-
tion technology from RWTH Aachen University,
Germany, in 2015. He worked for several biomed-
ical and healthcare corporates in Iraq and Middle
East. He helped in supporting and consolidating
different healthcare sectors in Iraq (radiology,
pediatrics, and rehabilitation engineering). He is also a devoted comics
painter and in love with philosophy and ancient archeological surveys and
sciences. He is interested in developing artiﬁcial intelligence platforms for
healthcare applications and is also an astronomy and astrophysics hobbyist.
He is currently involved in developing biomedical imaging project with
Canadian Space Agency for human mission of deep space explorations.

QAIS AHMED HABASH received the B.Sc.
and M.Sc. degrees from Al-Nahrain Univer-
sity in 2004 and 2007,
respectively. He is
currently pursuing the Ph.D. degree in elec-
trical and electronic engineering at Univer-
sity Putra Malaysia. He has been a Faculty
Member with the Bio-Medical Engineering
Department, Al-Nahrain University, since 2007.
His researches focused on biomedical signal and
image processing.

LUZ SANTAMARIA-GRANADOS is currently
pursuing the Ph.D. degree in telematics engi-
neering with the University of Cauca, Popayán,
Colombia. She is also a Professor with the Faculty
of Systems Engineering, University of Santo
Tomás, Colombia, and also a magister in commu-
nication and information sciences. Her research
areas are recommender systems and wearable
devices.

VOLUME 6, 2018

49323

JUAN FRANCISCO MENDOZA-MORENO is
currently pursuing the Ph.D. degree in telem-
atics engineering with the University of Cauca,
Popayán, Colombia. He is also a Professor with
the Faculty of Systems Engineering and the
Program of Master in pedagogy at the Univer-
sity of Santo Tomás, Tunja, Colombia, and also a
magister in free software. His areas of research are
software engineering, knowledge management,
and applied ICT.

A. F. Hussein et al.: Focal and Non-Focal Epilepsy Localization: Review

GUSTAVO RAMIREZ-GONZALEZ received the
B.S. degree in electronic and telecommunica-
tions engineering from the University of Cauca,
Colombia, in 2001, the M.S. degree in telematics
engineering from the University of Cauca, and the
Ph.D. degree in telematics engineering from the
Universidad Carlos III de Madrid, Spain, in 2010.
He is currently a Professor and a Researcher at the
Department of Telematics, University of Cauca.
He has participated in national and international
projects in Colombia and Spain. His research interests include image
processing, secure communication, machine learning, and IoT. He has
published several research papers in reputed journals and served as a guest
editor for several special issues at many journals.

49324

VOLUME 6, 2018
