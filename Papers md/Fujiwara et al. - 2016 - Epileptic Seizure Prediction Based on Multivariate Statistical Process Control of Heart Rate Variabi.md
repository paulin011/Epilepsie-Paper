# Fujiwara et al. - 2016 - Epileptic Seizure Prediction Based on Multivariate Statistical Process Control of Heart Rate Variabi

IEEE TRANSACTIONS ON BIOMEDICAL ENGINEERING, VOL. 63, NO. 6, JUNE 2016

1321

Epileptic Seizure Prediction Based on Multivariate
Statistical Process Control of Heart
Rate Variability Features
Koichi Fujiwara∗, Member, IEEE, Miho Miyajima, Toshitaka Yamakawa, Member, IEEE, Erika Abe, Member, IEEE,
Yoko Suzuki, Yuriko Sawada, Manabu Kano, Member, IEEE, Taketoshi Maehara, Katsuya Ohta,
Taeko Sasai-Sakuma, Tetsuo Sasano, Masato Matsuura, and Eisuke Matsushima

Abstract—Objective: The present study proposes a new epileptic
seizure prediction method through integrating heart rate variabil-
ity (HRV) analysis and an anomaly monitoring technique. Meth-
ods: Because excessive neuronal activities in the preictal period
of epilepsy affect the autonomic nervous systems and autonomic
nervous function affects HRV, it is assumed that a seizure can be
predicted through monitoring HRV. In the proposed method, eight
HRV features are monitored for predicting seizures by using mul-
tivariate statistical process control, which is a well-known anomaly
monitoring method. Results: We applied the proposed method to
the clinical data collected from 14 patients. In the collected data,
8 patients had a total of 11 awakening preictal episodes and the
total length of interictal episodes was about 57 h. The application
results of the proposed method demonstrated that seizures in ten
out of eleven awakening preictal episodes could be predicted prior
to the seizure onset, that is, its sensitivity was 91%, and its false
positive rate was about 0.7 times per hour. Conclusion: This study
proposed a new HRV-based epileptic seizure prediction method,
and the possibility of realizing an HRV-based epileptic seizure pre-
diction system was shown. Signiﬁcance: The proposed method can
be used in daily life, because the heart rate can be measured easily
by using a wearable sensor.

Index Terms—Epilepsy, heart rate variability analysis, multi-

variate statistical process control (MSPC), seizure prediction.

I. INTRODUCTION

E PILEPSY is a diverse set of chronic neurological disor-

ders characterized by seizures, and about 1% of people
worldwide have epilepsy [1]. Although epileptic seizures can
be usually controlled with appropriate medications, about 30%
of epileptic patients do not have seizure control even if they use
the best available medications [2].

Manuscript received May 1, 2015; revised December 3, 2015; accepted De-
cember 16, 2015. Date of publication December 24, 2015; date of current
version May 18, 2016. This work was supported in part by JSPS KAKENHI
25282175, the SEI Group CSR Foundation, the Japan Prize Foundation, the
Japan Epilepsy Research Foundation, and the Mitsubishi Foundation. Asterisk
indicates corresponding author.

*K. Fujiwara is with the Department of Systems Science, Kyoto University,

Kyoto 606-8501, Japan (e-mail: fujiwara.koichi@i.kyoto-u.ac.jp).

E. Abe and M. Kano are with the Department of Systems Science, Kyoto

University.

Y. Suzuki, Y. Sawada, M. Miyajima, T. Maehara, K. Ohta, T. Sasano,
M. Matsuura, and E. Matsushima are with the Tokyo Medical and Dental Uni-
versity.

T. Yamakawa is with the Kumamoto University.
T. S. Sasai is with the Tokyo Medical University.
Color versions of one or more of the ﬁgures in this paper are available online

at http://ieeexplore.ieee.org.

Digital Object Identiﬁer 10.1109/TBME.2015.2512276

Convulsions or loss of consciousness associated with un-
controlled seizures may cause serious injuries not only for pa-
tients themselves but also for people around them. If patients
can be given a warning before the seizure onset, their qual-
ity of life (QoL) may be improved because their safety can be
ensured.

Closed-loop seizure treatment systems have been proposed,
which consist of two parts: seizure prediction and automatic
seizure treatment. These systems automatically give a warn-
ing to caretakers or hospitals, or switch ON a neurostimulator
implanted in a patient for normalizing brain activities, when a
seizure is predicted [3]. An accurate seizure prediction method
is needed for realizing such systems.

Epileptic seizure prediction based on the electroencephalo-
gram (EEG) has been studied [4], [5]. However, the use of EEG
in daily life is not realistic because EEG recording strongly puts
restrictions on the body and is intolerant to artifacts.

On the other hand, epileptic seizures can lead to changes in
cardiac autonomic nervous function affecting both sympathetic
and parasympathetic nervous systems [6], [7]. The activation of
central autonomic nervous system by epileptic discharge prop-
agation during a seizure is thought to be responsible for the
preictal cardiac autonomic symptoms [8]. Ictal tachycardia and
bradycardia are well-known autonomic phenomena associated
with epileptic seizures, and such cardiac changes occur not only
at the same time as but also prior to the EEG seizure onset [9],
[10].

The RR interval (RRI) ﬂuctuation in an electrocardiogram
(ECG), called heart rate variability (HRV), is a well-known phe-
nomenon which reﬂects the autonomic nervous function [11],
and changes in HRV in preictal phase have been reported [12],
[13]. In addition, seizure detection based on HRV has been at-
tempted [14]. This method was able to detect seizures by using
the Lorentz plot; however, seizures of only three out of 17 pa-
tients could be detected before their onset. A new methodology
for predicting an epileptic seizure needs to be developed.

Another problem of HRV-based epileptic seizure prediction
is developing an RRI measurement device that can be used in
daily life. Although the Holter monitor has been used to mea-
sure long-term RRI, its home-use is difﬁcult because the Holter
monitor is expensive and requires operation skills. Yamakawa
et al. developed a wearable RRI sensor, which can measure RRI
without any special skills and be manufactured for less than
US $ 100 [15]. If an HRV-based seizure detection method can

0018-9294 © 2015 IEEE. Translations and content mining are permitted for academic research only. Personal use is also permitted, but republication/redistribution
requires IEEE permission. See http://www.ieee.org/publications standards/publications/rights/index.html for more information.

1322

IEEE TRANSACTIONS ON BIOMEDICAL ENGINEERING, VOL. 63, NO. 6, JUNE 2016

Fig. 1. Example of a typical ECG.

be implemented in such a device, a wearable epileptic seizure
prediction system becomes available.

The present study proposes a new HRV-based epileptic
seizure prediction method for realizing a seizure prediction de-
vice that can be used in daily life. The proposed method consists
of two parts: HRV feature extraction from RRI data of epileptic
patients, and epileptic seizure prediction by utilizing an anomaly
monitoring technique whose inputs are the extracted HRV fea-
tures. Multivariate statistical process control (MSPC) [16]–[18],
which is a well-known anomaly monitoring method, is used for
the epileptic seizure prediction.

This paper is organized as follows. Section II introduces HRV
analysis, and a new seizure prediction method is proposed by
integrating HRV analysis and MSPC in Section III. Section IV
reports application results of the proposed method to clinical
data and discusses the results. The conclusion and future work
are described in Section V.

II. HRV ANALYSIS

Since HRV reﬂects autonomic nervous activities, HRV anal-
ysis has been used for monitoring stress, drowsiness, and car-
diovascular disease [19]–[22]. In this section, the HRV features
used for seizure prediction are explained brieﬂy.

A. RR Interval

A typical ECG trace of the cardiac cycle (standard lead II)
consists of some peaks as shown in Fig. 1, and the highest peak
is called the R wave. The RRI [ms] is deﬁned as the interval
between an R wave and the next R wave.

A part of the raw RRI data collected from a healthy person is
shown in Fig. 2(a). Since the raw RRI data are not sampled at
equal intervals, frequency domain features cannot be extracted.
Thus, the raw RRI data are interpolated by using spline and
resampled at equal intervals. Fig. 2(b) shows the resampled RRI
data whose sampling interval is 1 s.

B. Time Domain Features

The following time domain features can be calculated from

the original RRI data [19].

1) meanNN: Mean of RRI.
2) SDNN: Standard deviation of RRI.
3) RMSSD: Root mean square of difference of adjacent RRI.
4) Total Power (TP): Variance of RRI.

Fig. 2. Example of RRI data analysis: (a) the raw RRI data, (b) the resampled
RRI data and (c) the PSD and its LF/HF.

5) NN50: The number of pairs of adjacent RRI whose dif-
ference is more than 50 ms within a given length of mea-
surement time.

C. Frequency Domain Features

The following frequency domain features can be obtained
from the power spectrum density (PSD) of the resampled RRI
data, and the PSD can be calculated by using Fourier analysis
or an autoregressive (AR) model [19].

1) LF: Power of the low frequency band (0.04–0.15 Hz) in
a PSD. LF reﬂects both the sympathetic and parasympa-
thetic activity nervous systems activity.

2) HF: Power of the high frequency band (0.15–0.4 Hz) in
a PSD. HF reﬂects the parasympathetic nervous system
activity.

3) LF/HF: Ratio of LF to HL. LF/HF expresses the bal-
ance of the sympathetic nervous system activity with the
parasympathetic nervous system activity.

Fig. 2(c) shows the PSD and its LF/HF of the resampled
RRI data shown in Fig. 2(b). According to the HRV analysis
guideline, the RRI data should be measured for 2 to 5 min for
frequency analysis [19].

III. EPILEPTIC SEIZURE PREDICTION

Since seizure prediction can be formulated as an anomaly
detection problem,
the present study uses MSPC, which
is a useful statistical technique for detecting anomalies in

FUJIWARA et al.: EPILEPTIC SEIZURE PREDICTION BASED ON MULTIVARIATE STATISTICAL PROCESS CONTROL OF HRV FEATURES

1323

multivariate systems, and it has been widely used in many man-
ufacturing processes [16]–[18].

A. Data Preprocessing

The proposed epileptic seizure prediction method uses eight
HRV features described in Section II as input variables, and they
are extracted from RRI data.

In HRV feature extraction, a rectangular moving window is
used and the window size is 3 min. The time domain features
can be extracted directly from the raw RRI data. For frequency
domain feature extraction, the RRI data need to be resampled so
that its sampling points are arranged at equal intervals. In this
study, the third-order spline is used for RRI interpolation, and
the sampling rate is 1 Hz. Since HRV reﬂects blood pressure
change and respiration change and their cycles are 10 s and 3–4
s, respectively, HRV is usually less than 0.5 Hz [19]. That is, 1
Hz sampling is enough for frequency domain analysis according
to the sampling theorem. This point is discussed in Section IV-
E. In addition, an AR model of order ten was used to calculate
frequency domain features.

For precise seizure prediction, appropriate HRV preprocess-
ing is needed since HRV has large individuality between pa-
tients. For example, the mean heart rate is different for every
person and it also changes with age. To cope with individuality
in HRV, normalized frequency domain features have been pro-
posed [23]. LF normalized unit (LFnu) and HF normalized unit
(HFnu) are deﬁned as follows:

LFnu = LF/TP

HFnu = HF/TP.

(1)

(2)

The present study uses LFnu and HFnu instead of LF and HF. On
the other hand, in order to emphasize important HRV features
for seizure prediction, any weighted function can be introduced;
however, such a weighted function is not used here, because it
is difﬁcult to determine which HRV features should be empha-
sized and which type of weighted function is appropriate for
seizure prediction, and the dimensionality of HRV features can
be reduced by using principal component analysis (PCA), which
is a tool for data compression and information extraction.

Finally, each HRV feature is standardized with zero mean and

a standard deviation of one for analysis.

In the following sections, the nth sampling of HRV features
can be denoted by xn = [xn ,1, xn ,2, . . . , xn ,M ]T where xn ,m
is the nth sampling of any mth HRV feature, where M = 8 in
this study because the number of HRV features used for seizure
prediction is eight. In addition, X ∈ (cid:4)N ×M is a matrix whose
nth row is xT
n .

B. Multivariate Statistical Process Control

operating condition is deﬁned by two monitored indexes, i.e.,
the T 2 and Q statistics [24].

Given a normal data matrix X ∈ (cid:4)N ×M whose ith row is the
ith sample xi ∈ (cid:4)M , samples are preprocessed appropriately.
The singular value decomposition of X is as follows:

X = U ΣV T
(cid:2)

(cid:4)

(cid:3)

=

U R U 0

(cid:5)

(cid:2)

ΣR

0

0 Σ0

(cid:3)

V R V 0

(3)

where U is the left singular matrix, Σ is the diagonal matrix
whose diagonal elements are singular values, and V is the right
singular matrix. In the PCA, the loading matrix V R ∈ (cid:4)M ×R
is derived as the right singular matrix of X. The column space
of V R is the subspace spanned by principal components and
it expresses the correlation among variables. Here, M , N , and
R(≤ M ) denote the number of variables, samples, and principal
components retained in the PCA model, respectively.

The score is a projection of X onto the subspace spanned
by principal components. The score matrix T R ∈ (cid:4)N ×R is
given by

T R = XV R .

(4)

X can be reconstructed or estimated from T R with linear trans-
formation V R ,

ˆX = T R V T

R = XV R V T
R .

(5)

The information lost by the dimensional compression, that is,
errors, is written as

E = X − ˆX = X(I − V R V T

R ).

(6)

Using the errors, the Q statistic is deﬁned as

Q =

M(cid:6)

m =1

(xm − ˆxm )2

= xT (I − V R V T

R )x

(7)

where x is a sample. The Q statistic is the squared distance be-
tween the sample and the subspace spanned by principal compo-
nents. In other words, the Q statistic is a measure of dissimilarity
between the sample and the modeling data from the viewpoint
of the correlation among variables.

In addition, to monitor anomalies on the subspace spanned
by principal components, Hotelling’s T 2 statistic is used. The
T 2 statistic is deﬁned as

T 2 =

R(cid:6)

r =1

t2
r
σ2
tr

= xT V R Σ−2

R V T

R x

(8)

MSPC can detect anomalies that cannot be detected by
monitoring each variable independently, because it models the
correlation among variables with PCA, which ﬁnds linear com-
binations of variables that describe major trends in a dataset.
That is, MSPC detects a sample that does not follow the major
trend in the modeling data as an anomaly. In MSPC, the normal

where σtr denotes the standard deviation of the rth score tr .
The T 2 statistic expresses the Mahalanobis distance from the
origin in the subspace spanned by principal components. When
the T 2 statistic is small, the sample is close to the mean of the
modeling data. MSPC detects an anomaly when either the T 2
or Q statistic exceeds the predeﬁned control limit.

1324

IEEE TRANSACTIONS ON BIOMEDICAL ENGINEERING, VOL. 63, NO. 6, JUNE 2016

The number of principal components R has to be determined
carefully as a tuning parameter. When R is small, the PCA
model cannot capture important data trends and this leads to
a deterioration in the anomaly detection performance. On the
other hand, since PCA models noisy data variance as well as
normal data variance when R is large, it increases false positives
(FPs). Although it is difﬁcult to determine R appropriately, the
cumulative proportion of principal components can be used for
its tuning. The proportion of the rth principal component Cr is
as follows:

Cr =

σ2
tr(cid:7)
M
m =1 σ2
tm

.

(9)

Cr shows the rate of the data represented by the rth principal
component in the original data. The cumulative proportion until
the rth principal component is deﬁned as follows:
r(cid:6)

(cid:7)

Pr =

Cr =

(cid:7)

m =1

r
m =1 σ2
tm
M
m =1 σ2
tm

.

(10)

Using Pr , the number of principal components R can be deter-
mined so that Pr reaches the predeﬁned value, such as 80% or
90%.

The control limits, for example, can be determined as α%
conﬁdence limits. In other words, they are set so that α% of
samples representing the normal condition are below the control
limits, and the other (100 − α)% are above them. The control
limits become large as α becomes large. That is, α controls the
sensitivity and the speciﬁcity of MSPC, and usually the 99% or
95% conﬁdence limits are adopted.

In seizure prediction, the interictal RRI data and the preictal
RRI data are deﬁned as normal data and anomalous data, re-
spectively. It is difﬁcult to collect a sufﬁcient number of preictal
RRI data from epileptic patients, and collecting the interictal
RRI data and the RRI data of healthy people is much easier than
preictal RRI data collection. Although, in general, both normal
and anomalous data are needed for modeling, MSPC requires
only normal data, which is one of its advantages.

C. Seizure Prediction

The present study proposes a new seizure prediction method,
in which the HRV features are extracted from the RRI data mea-
sured from epileptic patients, and the extracted HRV features
are monitored by using MSPC.

Before prediction, the interictal RRI data of epileptic patients
are analyzed for preparation. The procedure described in Algo-
rithm 1 is adopted.

In this procedure, y{i} is the interictal RRI data recorded from
the ith patient and I is the number of patients. First, interictal
HRV features are extracted from y{i}, and these HRV features
are merged into one matrix and preprocessed in steps 1–5. The
singular value matrix ΣR and the loading matrix V R are derived
from the preprocessed HRV data matrix for calculating the T 2
and Q statistics in step 6. At this time, the number of principal
components R has to be selected carefully for precise seizure
prediction. Finally, their control limits have to be determined
for each patient in steps 7–9.

Extract the ith patient interictal HRV features ˜X

Algorithm 1 Preparation of seizure prediction
1: for all i such that 1 ≤ i ≤ I do
2:
from y{i}.
3: end for
, . . . , ˜X
4: Merge matrixes ˜X
5: Preprocess ˜X appropriately, and it is referred to as X.
6: Derive ΣR and V R from X through singular value

into one matrix ˜X.

{I }

{1}

{i}

decomposition.

7: for all i such that 1 ≤ i ≤ I do
8: Deﬁne the control limits of the T 2 and Q statistics for

the ith patient, ¯T 2{i} and ¯Q{i}.

9: end for

Algorithm 2 Seizure prediction
1: set τ [0] ←− 0, C[0] ←− N .
2: while do
3:
4:
5:
6:

Collect the newly measured tth RRI y[t].
Extract the HRV features ˜x[t].
Preprocess ˜x[t], and it is denoted as x[t].
Calculate the tth T 2 and Q statistics, T 2[t] and Q[t]
from x[t] by using (7) and (8).
if ((T 2[t] > ¯T 2 ∨ Q[t] > ¯Q) ∧ C[t − 1] = N )
∨((T 2[t] ≤ ¯T 2 ∧ Q[t] ≤ ¯Q) ∧ (C[t − 1] = P)) then

7:

τ [t] = 0.

τ [t] = τ [t − 1] + y[t].
else

8:
9:
10:
11:
12:
13:
14:
15: Wait until the next RRI data y[t + 1] is measured.
16: end while

end if
if τ [t] ≥ ¯τ then
C[t] = ¬ C[t − 1] and τ [t] = 0.
end if

The proposed seizure prediction algorithm discriminates the
patient status between “preictal” and “interictal,” where “pre-
ictal” means an epileptic seizure will occur in the near future.
Before seizure prediction starts, the initial RRI data of an epilep-
tic patient have to be stored for more than the window size W ,
because HRV feature extraction requires RRI data whose length
is W . After the initial RRI data collection, seizures can be mon-
itored by following Algorithm 2.

In this algorithm, y[t] ∈ (cid:4) denotes the tth RRI and t de-
notes the number of sampling from the prediction start. τ is a
time counter variable and C expresses the binary patient status
C = {N , P} where N and P are “interictal” and “preictal,”
respectively. That is, ¬N = P and vice versa.

When either the T 2 or Q statistic exceeds its control limit for
more than the predeﬁned period ¯τ continuously, the patient sta-
tus is determined as “preictal,” because the T 2 and Q statistics
can easily ﬂuctuate due to ECG artifacts. Conversely, to change
the patient status from “preictal” to “interictal,” both statistics
have to stay below their control limits for more than ¯τ continu-
ously. Steps 7–14 discriminate the patient status, and the patient

FUJIWARA et al.: EPILEPTIC SEIZURE PREDICTION BASED ON MULTIVARIATE STATISTICAL PROCESS CONTROL OF HRV FEATURES

1325

TABLE I
PATIENTS DEMOGRAPHIC AND CLINICAL CHARACTERISTICS

Patient

Sex

Age

Epilepsy syndromes

Medication∗ [mg/day]

A
B
C
D
E
F
G
H
I
J
K
L
M
N

male
male
male
male
female
female
male
female
male
male
male
male
male
female

25
30
14
24
31
26
41
39
20
43
24
21
63
27

right frontal lobe epilepsy
left temporal lobe epilepsy
right occipital, parietal, temporal lobe epilepsy
left frontal lobe epilepsy
left mesial temporal lobe epilepsy
left occipital lobe epilepsy
right temporal lobe epilepsy
frontal lobe epilepsy
right temporal lobe epilepsy
left temporal lobe epilepsy
right parietal lobe epilepsy
right temporal lobe epilepsy
left temporal lobe epilepsy
right frontal lobe epilepsy

CBZ 800
CBZ 400, CLB 10
TPM 550, PHT 250, CLB 20, LTG 400
LEV 2000, CBZ 500
PHT 225, TPM 200, CBZ 600, VPA 1200, ZNS 300
PHT100, LEV 500
CLB 10, LEV 2000, VPA 800
VPA 50, LEV 250
CBZ 200, LEV 2000
ZNS 300, LTG 40
CBZ 600, LEV 3000, CLB 10, LTG 50
CBZ 800, LTG 200
CBZ 200, VPA 400, DZP 5
LEV 2000

∗VPA: valproic acid, LEV: levetiracetam, CZP: clonazepam, CBZ: carbamazepine, ZNS: zonisamide,
TPM: topiramate, CLB: clobazam, PHT: phenytoin, LTG: lamotrigine, GBP: gabapentin, DZP: diazepam

TABLE II
COLLECTED EPISODES

Interictal

Preictal

Patient

Episode

Length [h]

Episode

Length [h]

A∗∗
B∗∗
C
D
E
F
G
H
I
J
K
L
M
N
Total

A1, A2
B1, B2
C1 - C3
D1 - D6
E1 - E7
F1 - F3
G1 - G7
H1- H7
I1 - I3
J1 - J11
K1 - K3
L1 - L6
M1, M2
N1, N2

2.3
3.0
2.0
5.3
7.5
1.9
6.0
4.0
1.7
12.7
3.6
4.7
2.5
0.8
58.0

∗∗ Seizures occurred during sleep.

As1 – As3
Bs1
–
–
Es1
Fs1, Fs2
Gs1
–
Is1
Js1
Ks1
–
Ms1 – Ms4
Ns1

2.1
0.7
–
–
0.7
1.4
0.7
–
0.7
0.7
0.7
–
2.8
0.7
11.0

can be given a warning when the algorithm predicts a seizure in
the near future, that is, C = P.

IV. APPLICATION TO CLINICAL DATA

This section reports actual application results of the proposed

seizure prediction method to clinical data.

A. Data Collection

The clinical data of patients with refractory epilepsy were
collected prospectively or retrospectively from patients admit-
ted to the Department of Neurosurgery of Medical Hospital of
Tokyo Medical and Dental University (TMDU), the Department
of Psychiatry of the National Center of Neurology and Psychi-
atry (NCNP) hospital, and the Department of Epileptology of
the Tohoku University Hospital (TUH) for clinical video-EEG
monitoring for presurgical evaluation or assessment of seizure.
These prospective and retrospective evaluations of clinically
acquired data were approved by the Medical Research Ethics

Committee of TMDU, NCNP, and TUH. Written informed con-
sent was obtained from each participant who was involved in
the prospective evaluation.

The video, ECG, and EEG data of patients were simul-
taneously recorded for about 24–72 h by using a long-term
video-EEG monitoring system (Neurofax EEG-1200, NIHON
KOHDEN). These tests were conducted in the epilepsy moni-
toring unit, and the sampling frequency of ECG and EEG was
500 or 1000 Hz. ECG data containing strong artifacts or ar-
rhythmia were eliminated. In this study, a clinical seizure onset
is deﬁned as a time point when clinical epileptic seizure mani-
festation occurs, such as convulsion, automatism, and alteration
of consciousness. Two clinical epilepsy specialists, certiﬁed by
the Japan Epilepsy Society, determined a clinical seizure onset
by consulting the seizure video and the EEG data.

The clinical datasets were collected from 14 epileptic pa-
tients A–N with localization-related epilepsy. Tables I and II
show patient proﬁles and their collected episodes, respectively.
Medication in Table I means the anticonvulsant dosage [mg/day]
on the inspection day, and length in Table II denotes the total
recorded length [h] of the collected episodes. Unfortunately,
the preictal episodes of patients C, D, H, and L could not be
recorded.

The data 15 min before and 5 min after seizure onsets were
stored as preictal episodes. The data recorded during periods
apart from at least 50 min from seizure onsets were deﬁned as in-
terictal episodes. In addition, a clinical technologist determined
sleep stages during interictal periods based on the EEG data,
and the interictal data during sleep were eliminated because
HRV is affected by sleep stage transition and microarousal
[25], [26].

On the other hand, in order to validate whether or not the pro-
posed method can predict seizures during sleep, some preictal
episodes during sleep, As1–As3 and Bs1, were also evaluated
independently from awakening preictal episodes. The epilepsy
types of patients A and B were frontal lobe epilepsy (FLE) and
temporal lobe epilepsy (TLE), respectively. In FLE, seizures
frequently occur during sleep, whereas temporal seizures occur
during both wakefulness and sleep in TLE [27], [28].

1326

IEEE TRANSACTIONS ON BIOMEDICAL ENGINEERING, VOL. 63, NO. 6, JUNE 2016

Fig. 3. Obtained RRI data of A2 (top) and As3 (bottom).

Fig. 4. Obtained RRI data of I3 (top) and Is1 (bottom).

The total numbers of collected awakening and sleeping pre-
ictal episodes and interictal episodes used for analysis were 11,
4, and 64, respectively.

B. RRI Data and HRV Features

The R waves in the collected ECG datasets were detected
by using a ﬁrst derivative-based peak detection algorithm, and
each RRI was calculated. The obtained raw RRI data of patients
A, I, M, and N recorded in interictal and preictal periods are
shown in Figs. 3–6. In these ﬁgures, a vertical line denotes the
seizure onset. Although these ﬁgures show that patients experi-
enced sudden tachycardia after the seizure onset, it was difﬁcult
to calculate RRI during seizures due to large ECG artifacts
because seizures often have dramatic clinical manifestations
including posturing, hypermotor automatisms, and ambulation,
which cause ECG artifacts. That is, the RRI data after the seizure
onset were not reliable.

Eight HRV features described in Section II were extracted
by following the procedure in Section III-A. Figs. 7–14 are the
obtained HRV features of the RRI data shown in Figs. 4–6. The
preictal HRV data show that almost all features, in particular
frequency domain features, changed before the seizure onset,
while the interictal HRV features did not ﬂuctuate so much.

On the other hand, for example, LF between 200-600 s and
LF/HF around 600 s of episode M2 greatly changed as shown
in Fig. 11; nevertheless this episode did not contain seizures.
According to its RRI data, patient I experienced tachycardia
during these periods.

These results indicate that it is difﬁcult to predict seizures
by monitoring changes in respective HRV features, and that
relationships between multiple features should be monitored.

C. Prediction Preparation

Seizure prediction was prepared by following Algorithm 1.
The HRV features derived from 22 interictal episodes summa-
rized in Table III were used for modeling. The total recorded
length of the analyzed episodes was about 18.9 h.

All HRV features calculated in Section IV-B were used as
inputs. To cope with individuality between patients, LFnu and
HFnu were used instead of LF and HF. In the MSPC, the number
of retained principal components R was determined so that the
cumulative proportion reached more than 90%, and R = 6. The

Fig. 5. Obtained RRI data of M2 (top) and Ms2 (bottom).

Fig. 6. Obtained RRI data of N2 (top) and Ns1 (bottom).

control limits of the T 2 and Q statistics were deﬁned for each
patient so that they represent 99% conﬁdence limits, i.e., 99% of
the interictal data of each patient were recognized as “interictal.”
This 99% conﬁdence limit is a common setting in anomaly
detection. In addition, the parameter ¯τ was determined as 10 s
by following opinions from clinical epilepsy specialists.

D. Seizure Prediction

All preictal episodes and all interictal episodes that were not
used for modeling were monitored by following Algorithm 2
for validation. The numbers of validated awakening preictal
and interictal episodes were 11 and 41, respectively. The total
length of the validated interictal episodes was 38.4 h. In this

FUJIWARA et al.: EPILEPTIC SEIZURE PREDICTION BASED ON MULTIVARIATE STATISTICAL PROCESS CONTROL OF HRV FEATURES

1327

Fig. 7. HRV features derived from A2.

Fig. 10. HRV features derived from Is1.

Fig. 8. HRV features derived from As3.

Fig. 11. HRV features derived from M2.

Fig. 9. HRV features derived from I3.

Fig. 12. HRV features derived from Ms2.

paper, seizure prediction success means that a seizure can be
predicted from 15 min before to just before the seizure onset.

was not discriminated as seizure prediction, since it did not
exceed its control limit for more than 10 s continuously.

Monitoring results of preictal episodes As3, Is1, Ms2, and
Ns1 are shown in Figs. 15–18. In these ﬁgures, horizontal dashed
lines and vertical lines express the control limits of the T 2
and Q statistics and the seizure onset, respectively. A colored
band denotes a preictal period discriminated by the proposed
method.

According to Algorithm 2, a seizure is predicted only when
either T 2 and Q statistic exceeds its control limit continuously
for more than ¯τ = 10 s. The Q statistic around 500 s in Fig. 17

From the preictal episode results, the Q statistic could detect
10 out of 11 awakening seizures except episode Is1 as shown
in Fig. 16. On the other hand, the T 2 statistic could predict 6
out of 11 seizures except episodes Es1, Fs2, Is1, Js1, and Ks1.
Therefore, the sensitivity of the T 2 and Q statistics are 55%
and 91%, respectively. In addition, the mean and the standard
deviation of the ﬁrst seizure prediction time [s] by the T 2 and
Q statistics were 524 ± 216 and 494 ± 262 s before seizure
onsets, respectively.

1328

IEEE TRANSACTIONS ON BIOMEDICAL ENGINEERING, VOL. 63, NO. 6, JUNE 2016

Fig. 13. HRV features derived from N2.

Fig. 15. Monitoring result of preictal episode As3 by MSPC.

Fig. 14. HRV features derived from Ns1.

TABLE III
INTERICTAL EPISODES USED FOR MODELING

Patient

Episodes

Length [h]

Patient

Episodes

Length [h]

A
B
C
D
E
F
G

A1
B1
C1, C2
D1, D2
E1, E2
F1
G1, G2

1.0
1.5
0.6
2.7
2.3
0.6
2.0

H
I
J
K
L
M
N
Total

H1, H2
I1
J1, J2
K1, K2
L1–L3
M1
N1

1.2
0.8
1.7
1.4
1.6
1.1
0.4
18.9

Regarding seizures during sleep,

three sleeping preictal
episodes As1–As3 could be detected by both the T 2 and Q
statistics, while neither the T 2 nor Q statistics could detect
episode Bs1.

There may still be FPs in the preictal periods in which seizure
detection was possible; this is because, while the the epileptic
neuronal activities that start in the patient brain before the clin-
ical seizure onset can be deﬁned as the true seizure onset, this
true seizure onset is difﬁcult to detect even if EEG data could
be used.

Figs. 19–22 show prediction results of interictal episodes A2,
I3, M2, and M2. There were no FPs in episodes A2 and I3;
however, some FPs occurred according to the T 2 statistic in
episodes M2 and N2.

Fig. 16. Monitoring result of preictal episode Is1 by MSPC.

Fig. 17. Monitoring result of preictal episode Ms2 by MSPC.

Fig. 18. Monitoring result of preictal episode Ns1 by MSPC.

FUJIWARA et al.: EPILEPTIC SEIZURE PREDICTION BASED ON MULTIVARIATE STATISTICAL PROCESS CONTROL OF HRV FEATURES

1329

TABLE IV
FPS EXCEPT FOR ECG ARTIFACTS

T 2

Q

Patient

Length [h]

#FP

FP rate

#FP

FP rate

A
B
C
D
E
F
G
H
I
J
K
L
M
N
Total

1.1
1.5
1.3
2.4
4.8
1.1
5.7
3.4
0.7
10.4
1.6
2.8
1.2
0.4
38.4

0
5
0
3
16
0
2
8
0
6
0
0
5
1
46

0
3.5
0
1.3
3.3
0
0.3
2.4
0
0.6
0
0
3.9
2.5
1.2

1
4
1
1
2
6
1
4
0
8
0
0
1
0
29

0.9
2.8
0.8
0.4
0.4
5.5
0.2
1.2
0
0.8
0
0
0.8
0
0.7

Fig. 23.
change.

Prediction performances when the number of principal components

Some FPs, which were caused by ECG artifacts according to
the ECG data, were not used for evaluation. Table IV summa-
rizes the number of FPs whose causes were not ECG artifacts
(#FP) and FP rates. In this paper, the FP rate is deﬁned as #FP
per hour, and this evaluation is common in the ﬁeld of seizure
prediction [3]. The #FP in all interictal periods (total 38.4 h) by
the T 2 and Q statistics were 46 and 29, and the FP rates were
1.2 and 0.7 times per hour, respectively.

E. Discussion

In this case study, the T 2 and Q statistics could predict 6
and 10 out of 11 awakening seizures prior to seizure onsets,
and neither the T 2 nor Q statistic could predict preictal episode
Is1. According to the video data of episode I1 that was used
for modeling, patient I walked around in the hospital room and
ate something. On the other hand, he rarely moved in bed while
other episodes were recorded. That is, his conditions were com-
pletely different between the modeling data and the validation
data, and MSPC did not function well. This result indicates that

Fig. 19. Monitoring result of interictal episode A2 by MSPC.

Fig. 20. Monitoring result of interictal episode I3 by MSPC.

Fig. 21. Monitoring result of interictal episode M2 by MSPC.

Fig. 22. Monitoring result of interictal episode N2 by MSPC.

1330

IEEE TRANSACTIONS ON BIOMEDICAL ENGINEERING, VOL. 63, NO. 6, JUNE 2016

Fig. 24.

Interictal paroxysmal rhythmic θ activity over the bilateral frontal pole area in episode Bs3.

modeling data should be selected carefully for constructing a
highly accurate seizure prediction model.

Whether the proposed method can predict seizures during
sleep or not was validated. In this case study, three out of four
interictal episodes during sleep could be predicted, which shows
that the proposed method cannot always cope with seizures
during sleep because the modeling data did not contain sleeping
interictal data.

The interictal epileptiform discharges corresponding to the
increase of the T 2 and Q statistics were observed. Fig. 24 shows
the interictal paroxysmal rhythmic θ wave over the bilateral
frontal pole area, which corresponds to the ﬁrst seizure detection
by the T 2 statistic around 100 s in the prediction result of preictal
episode As3 (see Fig. 15). In addition, an interictal sharp wave
over the right frontal and the central area corresponding to the
second seizure detection by the T 2 statistic around 500 s in the
prediction result of preictal episode As3 was observed. Actually,
Fig. 8 shows that HRV features suddenly changed around these
interictal discharges.

frequently during the interictal period, and six out of nine FPs
in interictal episodes of patient F seemed to correspond to them.
Fig. 25 shows an example of the interictal paroxysmal rhythmic
δ waves associated with spikes over frontal, central, and parietal
area with left hemisphere dominance in episode F3. Although
other interictal discharges corresponding to the increase in T 2
and Q statistics were not observed, these correspondences be-
tween seizure prediction and interictal discharges support the
validity of the proposed method. These results agree with the
previous study which suggests the inﬂuence of interictal dis-
charges on HRV [29].

In order to validate the effect of the use of the normalized
frequency domain features, the prediction performance of the
seizure prediction model using LFnu and HFnu was compared
with that of the model using original LF and HF. The latter
model could predict 5 and 7 out of 11 seizures, and its pre-
diction performance was inferior to the former. That is, it is
important to consider HRV individuality among patients for
seizure prediction.

Although Table IV shows that the FP rate of patient F by the Q
statistic was particularly high, epileptiform discharges occurred

In addition, the number of principal components R adopted
for the seizure prediction model was validated. The prediction

FUJIWARA et al.: EPILEPTIC SEIZURE PREDICTION BASED ON MULTIVARIATE STATISTICAL PROCESS CONTROL OF HRV FEATURES

1331

Fig. 25.

Interictal paroxysmal rhythmic δ waves associated with spikes over frontal, central, and parietal area with left hemisphere dominance in episode F3.

performances when R changed from one to seven is shown
in Fig. 23. In this ﬁgure, the horizontal and vertical axes de-
note the number of principal components R and the number of
awakening preictal episodes whose seizure could be predicted,
respectively. This result shows that the prediction performance
of the Q statistic changed greatly between R = 5 and 7 while
that of the T 2 statistic did not change much.

Table IV shows that the T 2 statistic caused more FPs than the
Q statistic in most patients. The seizure prediction model was
constructed by using the video-EEG monitoring data for presur-
gical tests, and patients rarely moved in bed while the data were
recorded. The FPs may have been caused by patient body mo-
tion affecting HRV. The number of principal components R was
six while the number of HRV features used in this analysis was
eight. Their cumulative proportion Pr of the adopted principal
components reached more than 90%. In general, most of the
large ﬂuctuations in HRV are covered by major principal com-
ponents and are represented by the T 2 statistic. Thus, the T 2
statistic is expected to capture the effect of patient body motion
on HRV. In fact, most FPs observed in the T 2 statistic coincided
with patient motion according to the video.

According to Fig. 23, the seizure prediction performance of
the Q statistic deteriorated when R = 7 because almost all in-
formation retained in the residual subspace monitored by the
Q statistic was noise. In other words, when R = 7, information

associated with epileptic seizures was contained in the T 2 statis-
tic and actually its prediction performance was improved.

The FP rates by the T 2 and Q statistics were 1.2 and 0.7 times
per hour, which are worse than conventional EEG-based seizure
prediction methods whose FP rates are about 0.1–0.3 times per
hour [4], [30]–[32]; however, the proposed HRV-based method
does not restrict the patient’s body because RRI can be easily
measured by a wearable device [15], while the use of EEG-
based methods in daily life is difﬁcult because of the nature
of EEG recording. In addition, since the computational load
of the proposed method is much lighter than the EEG-based
methods, it can be easily implemented into mobile computers.
Furthermore, the proposed method can be used for closed-loop
seizure treatment systems because of its ease of implementation.
In this study, the third-order spline was used for RRI interpo-
lation and its resampling rate was 1 Hz for frequency domain
feature extraction because ﬂuctuation of RRI is usually less
than 0.5 Hz. However it is possible that high-frequency HRV
occurs due to arrhythmia or other circulatory diseases; in this
case, 1-Hz RRI resampling is insufﬁcient. The effect of the
resampling rate for frequency domain feature extraction was
validated. The frequency domain features were extracted using
4-Hz RRI resampling, and seizures were predicted by follow-
ing the same procedure. The seizure prediction performance
with the 4-Hz RRI resampling was the same as the 1-Hz RRI

1332

IEEE TRANSACTIONS ON BIOMEDICAL ENGINEERING, VOL. 63, NO. 6, JUNE 2016

resampling, which shows that 1-Hz resampling is enough for
HRV-based seizure prediction. Considering implementation of
the proposed method in a wearable RRI sensor [15], the amount
of data should be reduced because computational resources of
a microcomputer used in the sensor is limited. Therefore, the
1-Hz RRI resampling is suitable for the proposed method.

It is concluded that the proposed HRV-based seizure predic-
tion method is more promising than the conventional EEG-based
methods from the viewpoint of practical use.

V. CONCLUSION AND FUTURE WORK

A new HRV-based epileptic seizure prediction monitoring
method was proposed, by which RRI data recorded from epilep-
tic patients were translated into HRV features, and the HRV fea-
tures were monitored by MSPC. The application results to the
clinical data showed that the sensitivity of the proposed method
was 91%, and its FP rate was about 0.7 times per hour.

We are presently developing a mobile seizure prediction sys-
tem based on a smartphone and a wearable RRI sensor. In this
system, the wearable RRI sensor measures RRI data of a patient
and sends them to the smartphone wirelessly. The smartphone
app analyzes the received RRI data and discriminates the patient
status between “interictal” and “preictal” in real time. Finally,
the patient can receive a warning when the patient status be-
comes “preictal.” The developing system has the potential for
improving QoL of epileptic patients through real-time seizure
warning.

In future works, additional clinical data will be collected for
improving accuracy of the seizure prediction algorithm, and the
developing system will be tested in hospitals.

ACKNOWLEDGMENT

The authors would like to thank the staff of the Department of
Neurosurgery of Medical Hospital, Tokyo Medical and Dental
University, the Department of Psychiatry of the National Cen-
ter Hospital of Neurology and Psychiatry and Department of
Epileptology, Tohoku University Hospital who provided patient
data.

REFERENCES

[1] D. J. Thurman et al., “Standards for epidemiologic studies and surveil-

lance of epilepsy,” Epilepsia, vol. 52, pp. 2–26, 2011.

[2] B. Chang and D. H. Lowenstein, “Epilepsy,” New Engl. J. Med., vol. 345,

pp. 1257–1266, 2003.

[3] S. Ramgopala et al., “Seizure detection, seizure prediction, and closed-
loop warning systems in epilepsy,” Epilepsy Behav., vol. 37, pp. 291–307,
2014.

[4] L. D. Iasemidis, “Epileptic seizure prediction and control,” IEEE Trans.

Biomed. Eng., vol. 50, no. 5, pp. 549–558, May 2003.

[5] P. R. Carney et al., “Seizure prediction: methods,” Epilepsy Behav., vol. 22,

pp. S94–S101, 2011.

[6] K. S. Eggleston et al., “Ictal tachycardia: The head-heart connection,”

Seizure, vol. 23, pp. 496–505, 2014.

[7] C. Sevcencu and J. J. Struijk, “Autonomic alterations and cardiac changes

in epilepsy,” Epilepsia, vol. 51, pp. 725–737, 2010.

[8] K. Jansen et al., “Peri-ictal ECG changes in childhood epilepsy: implica-

[9] G. D. Gennaro et al., “Ictal heart rate increase precedes EEG discharge
in drug-resistant mesial temporal lobe seizures,” Clin. Neurophysiol.,
vol. 115, pp. 1169–1177, 2004.

[10] K. Kato et al., “Earlier tachycardia onset in right than left mesial temporal

lobe,” Neurology, vol. 83, pp. 1332–1336, 2014.

[11] M. Pagani et al., “Power spectral analysis of heart rate and arterial pres-
sure variabilities as a marker of sympatho-vagal interaction in man and
conscious dog,” Circ. Res., vol. 59, pp. 178–193, 1986.

[12] S. Behbahani et al., “Pre-ictal heart rate variability assessment of epileptic
seizures by means of linear and non-linear analyses,” Anadolu Kardiyol
Derg., vol. 13, pp. 797–803, 2013.

[13] G. Calandra-Buonaura et al., “Physiologic autonomic arousal heralds
motor manifestations of seizures in nocturnal frontal lobe epilepsy: Im-
plications for pathophysiology,” Sleep Med., vol. 13, pp. 252–262, 2012.
[14] J. Jeppesen et al., “Detection of epileptic seizures with a modiﬁed heart
rate variability algorithm based on lorenz plot,” Seizure, vol. 24, pp. 1–7,
2015.

[15] T. Yamakawa et al., “Real-time heart rate variability monitoring employ-
ing a wearable telemeter and a smartphone,” in Proc. Asia-Paciﬁc Signal
Inf. Process. Assoc. Annu. Summit Conf., Kaohsiung, Taiwan, Oct. 29,
2014–Nov. 1, 2014, pp. 1–4.

[16] P. Nomikos and J. F. MacGregor, “Monitoring batch processes using
multiway principal component analysis,” AIChE J., vol. 40, pp. 1361–
1375, 1994.

[17] J. F. MacGregor and T. Kourti, “Statistical process control of multivariate

processes,” Control Eng. Pract., vol. 3, pp. 403–414, 1995.

[18] M. Kano et al., “A new multivariate statistical process monitoring method
using principal component analysis,” Comput. Chem. Eng., vol. 25,
pp. 1103–1113, 2001.

[19] A. J. Camm et al., “Guidelines heart rate variability—Standards of mea-
surement, physiological interpretation, and clinical use,” Eur. Heart J.,
vol. 115, pp. 354–381, 1996.

[20] R. E. Kleiger et al., “Decreased heart rate variability and its associa-
tion with increased mortality after acute myocardial infarction,” Amer. J.
Cardiol., vol. 59, pp. 256–262, 1987.

[21] A. Malliani, “Cardiovascular neural regulation explored in the frequency

domain,” Circulation, vol. 84, pp. 482–492, 1991.

[22] E. Abe et al., “Development of drowsiness detection method by integrating
heart rate variability analysis and multivariate statistical process control,”
SICE J. Control. Meas. Syst. Integr., vol. 9, no. 1, pp. 001–008, Jan. 2016.
[23] R. L. Burr, “Interpretation of normalized spectral heart rate variability
indices in sleep research: A critical review,” Sleep, vol. 30, pp. 913–919,
2007.

[24] J. E. Jackson et al., “Control procedures for residuals associated with
principal component analysis,” Technometrics, vol. 21, pp. 341–349, 1973.
[25] E. Sforza et al., “Cardiac activation during arousal in humans: Further evi-
dence for hierarchy in the arousal response,” Clin. Neurophysiol., vol. 111,
pp. 1611–1619, 2000.

[26] N. Gosselinaand et al., “Age difference in heart rate changes associated
with micro-arousals in humans,” Clin. Neurophysiol., vol. 113, pp. 1517–
1521, 2002.

[27] Commission on Classiﬁcation and Terminology of the International
League Against Epilepsy, “Proposal for revised classiﬁcation of epilepsies
and epileptic syndromes,” Epilepsia, vol. 30, pp. 389–399, 1989.
[28] A. Crespel et al., “Proposal for revised classiﬁcation of epilepsies and
epileptic syndromes,” Clin. Neurophysiol., vol. 111, pp. S54–S59, 2000.
[29] M. M. Zaatreh et al., “Heart rate variability during interictal epileptiform

discharges,” Epilepsy Res., vol. 54, pp. 85–90, 2003.

[30] A. Shoeb and J. Guttag, “Application of machine learning to epileptic

seizure detection,” in Proc. 27th Int. Conf. Mach. Learn., 2010.

[31] M. D’Alessandro et al., “Epileptic seizure prediction using hybrid feature
selection over multiple intracranial EEG electrode contacts: A report of
four patients,” IEEE Trans. Biomed. Eng., vol. 50, no. 8, pp. 603–614,
Aug. 2003.

[32] L. D. Iasemidis et al., “Adaptive epileptic seizure prediction system,”
IEEE Trans. Biomed. Eng., vol. 50, no. 5, pp. 616–626, May 2003.

tions for detection systems,” Epilepsy Behav., vol. 29, pp. 72–76, 2013.

Authors’ photographs and biographies not available at the time of publication.
