# Wu et al. - 2024 - A Novel Seizure Detection Method Based on the Feature Fusion of Multimodal Physiological Signals

IEEE INTERNET OF THINGS JOURNAL, VOL. 11, NO. 16, 15 AUGUST 2024

27545

A Novel Seizure Detection Method Based on the
Feature Fusion of Multimodal Physiological Signals

Duanpo Wu , Jun Wei

, Pierre-Paul Vidal, Danping Wang, Yixuan Yuan , Senior Member, IEEE,

Jiuwen Cao , Senior Member, IEEE, and Tiejia Jiang

Abstract—Seizure detection is

traditionally done using
video/electroencephalography monitoring, but for out-of-hospital
patients, this method is costly. In recent years, portable device
to detect seizures gains attention. In this article, multimodal
signals collected by portable devices are studied, and a seizure
detection algorithm is proposed based on adaptive multibit
local differential
ternary pattern (MLDTP). This algorithm
is used for detecting seizure period and interseizure period.
Traditional
local binary pattern has certain limitations in
describing 1-D time-series signals. It can only describe two
types of structures in signals: 1) rising structure and 2) falling
structure, making the signal patterns overly monotonous and
not conducive to classiﬁcation tasks. To address this issue,
this article introduces two additional structures, slowly rising
structure and slowly falling structure, into the signal description
using the MLDTP method. This method constructs multibit
neighboring relationships of the signals and adaptively selects
the optimal MLDTP parameters for different modalities using
the Archimedes optimization algorithm (AOA). Additionally, this

Manuscript received 1 April 2024; revised 1 May 2024; accepted 6 May
2024. Date of publication 8 May 2024; date of current version 8 August 2024.
This work was supported in part by the National Key Research and
Development Program under Grant 2021YFE0100100; in part by the National
Natural Science Foundation of China under Grant 62301203; in part by the
Fundamental Research Funds for the Provincial Universities of Zhejiang under
Grant GK239909299001-401; in part by the Joint Fund of Zhejiang Provincial
Natural Science Foundation of China under Grant LBY21H090001; and in
part by the NSFC–Zhejiang Integration Joint Fund under Grant U1909209.
(Corresponding author: Duanpo Wu.)

This work involved human subjects or animals in its research. Approval of
all ethical and experimental procedures and protocols was granted by the Ethic
Committee of Zhejiang University under Application No. 2020-IRB-124.

Duanpo Wu is with the School of Communication Engineering and
the Artiﬁcial Intelligence Institute, Hangzhou Dianzi University, Hangzhou
310018, Zhejiang, China (e-mail: wuduanpo@hdu.edu.cn).

Jun Wei is with the School of Communication Engineering, Hangzhou
Dianzi University, Hangzhou 310018, China (e-mail: weijun7529@163.com).
Pierre-Paul Vidal is with the Machine Learning and I-Health International
Cooperation Base of Zhejiang Province, Hangzhou Dianzi University,
Hangzhou 310018, China, also with the Centre Borelli, CNRS, SSA,
INSERM, Université Paris Cité, Université Paris Saclay, ENS Paris
Saclay, 75006 Paris, France, and also with the Plateforme d’Etude de la
Sensorimotricité, INSERM US36-CNRS2009, Université Paris Cité, 75006
Paris, France (e-mail: pierre-paul.vidal@u-paris.fr).

Danping Wang is with the Machine Learning and I-Health International
Cooperation Base of Zhejiang Province, Hangzhou Dianzi University,
Hangzhou 310018, China, and also with the Plateforme d’Etude de la
Sensorimotricité, INSERM US36-CNRS2009, Université Paris Cité, 75006
Paris, France (e-mail: danping.wang@u-paris.fr).

Yixuan Yuan is with the Department of Electronic Engineering, The Chinese

University of Hong Kong, Hong Kong (e-mail: yxyuan@ee.cuhk.edu.hk).

Jiuwen Cao is with the Machine Learning and I-Health International
Cooperation Base of Zhejiang Province and the Artiﬁcial Intelligence Institute,
Hangzhou Dianzi University, Hangzhou 310018, Zhejiang, China (e-mail:
jwcao@hdu.edu.cn).

Tiejia Jiang is with the Children’s Hospital, Zhejiang University School of

Medicine, Hangzhou 310052, China (e-mail: jiangyouze@zju.edu.cn).

Digital Object Identiﬁer 10.1109/JIOT.2024.3398418

article extensively discusses a multimodal signal fusion strategy,
mapping features of different modal signals to the same feature
space through the MLDTP algorithm to achieve information
complementarity. Long-term recorded data from 18 patients were
collected using the wearable device Biovital P1, with 13 cases
from the Children’s Hospital afﬁliated with Children’s Hospital,
Zhejiang University School of Medicine, and ﬁve cases from
the fourth Afﬁliated Hospital of Anhui Medical University. The
data set underwent ﬁvefold cross-validation, resulting in average
accuracy, precision, sensitivity, and F1 score of 96.81%, 98.55%,
95.24%, and 96.87%, respectively.

Index Terms—Archimedes optimization algorithm (AOA), fea-
ture fusion, local differential ternary pattern, portable device,
seizure detection.

I. INTRODUCTION

E PILEPSY is caused by paroxysmal abnormal hypersyn-

chronous electrical activity of neurons in the brain [1]
and is one of the most common psychiatric system disorders
worldwide. It is characterized by recurrent seizures that are
unpredictable and short duration [2]. While electroencephalog-
raphy (EEG) can be used to effectively diagnose seizures,
it is not the most convenient diagnostic method and is not
suitable for long-term or nighttime monitoring outside the
hospital [3]. New methods for seizure detection are sought by
studying physiological signals generated from different modal-
ities recorded by portable devices [4], including accelerometry
(ACC), gyroscope (GYR), electromyogram (EMG), and elec-
trodermal (EDA).

The rapid progress in multimodal seizure detection technol-
ogy is marking a signiﬁcant breakthrough in modern medical
science [3], [5], [6]. This approach integrates an array of
sensor modules, such as ACC, GYR, EMG, and EDA, to
monitor and analyze patients’ physiological signals. These
divergent modal signals hold signiﬁcant correlations with
seizures [3], [6], [7], [8], [9]. ACC and GYR detect
the
physical movements and vibrations during seizures [7], [8],
EMG captures involuntary muscle contractions throughout
such events [9], and EDA indicates autonomic nervous system
ﬂuctuations [8]. Comprehensive analysis of the data harvested
by wearable devices not only enhances seizure detection but
also advances early warning and monitoring capabilities for
epilepsy [10], [11], [12]. In the ﬁeld of signal processing,
there is a growing interest in researching the conversion of
signals into code. The local binary pattern (LBP) method
enjoys widespread adoption in the analysis of both 1-D

2327-4662 c(cid:2) 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:50 UTC from IEEE Xplore.  Restrictions apply. 

27546

IEEE INTERNET OF THINGS JOURNAL, VOL. 11, NO. 16, 15 AUGUST 2024

signals and 2-D images due to its distinct discriminatory
capabilities and computationally efﬁcient characteristics. The
concept of 1-D LBP is originally introduced by Hatlani et al.
and has demonstrated successful application in the detection
of nonsmooth speech signals [13]. Kaya et al. [14] harnessed
1-D LBP to extract distinctive characteristics from unpro-
cessed EEG signals, effectively showcasing its remarkable
performance and minimal computational demands when deal-
ing with nonsmooth EEG signals. Although the performance
of LBP on nonsmooth signals is very objective, it is poorly
adapted to noise and prone to interference. To address this
problem, Khan et al. [15] proposed a hybrid method based
on LBP wavelets to classify the EEG of epileptic patients.
Local pattern transformation is widely applied not only in the
ﬁeld of electroencephalogram signals but also demonstrates
unique advantages in other modalities of signal applications.
Ohini and Mignotte [16] proposed classifying environmental
noise using LBP combined with audio features, which has
lower computational complexity compared to convolutional
neural networks. Luo et al. [17] proposed a scale-selective
and noise-robust extended LBP (SNELBP) descriptor, which
achieves good performance between scale invariance and
noise robustness. El Merabet et al. [18] proposed a novel
attractive-and-repulsive center-symmetric LBP (ACS-LBP and
RCS-LBP) texture descriptor, enhancing the discriminative
power of LBP and its
to small variations.
Huang et al. [19] introduced a discriminative spatiotemporal
LBP (STLBP) based on integral projections, incorporating
extracted shape attributes into spatiotemporal texture features.
Ding et al. [20] enhanced STLBP by introducing a method
that employed pixel difference vector (PDV) hashing and
multiscale volume dictionary learning, effectively addressing
the problem of utilizing small neighborhoods in STLBP due
to high-dimensional data. Zheng et al. [21] proposed a new
texture recognition model of the circular local ternary pattern
(CLTP) in response to the shortcomings of LBP in texture
recognition. Zhang et al. [22] proposed a seizure detection
algorithm based on multibit local neighborhood difference
pattern (MLNDP) and constructed a multibit neighboring
relationship.

robustness

In recent years, researches on pattern recognition and clas-
siﬁcation of local pattern transformations on single modality
have continued, such as Lan et al. [23], Akbal et al. [24],
[26], while the
Al-wajih et al. [25], and Kumar et al.
performance under multimodality has not been well validated,
selecting the appropriate algorithm for multimodal recognition
remains a signiﬁcant challenge.

In this article, we improve the LBP and MLNDP algo-
local
rithms and propose a robust and efﬁcient multibit
differential ternary pattern (MLDTP) algorithm. It is applied
to multimodal seizure detection, effectively enhancing the
classiﬁcation performance of the model. The Archimedes
optimization algorithm (AOA) is utilized to optimize the
parameters of MLDTP. The algorithm is brieﬂy described
as follows. First, different modal signals are transformed
into MLDTP codes and their parameters are optimized
the MLDTP
using AOA. Second, histogram features of
codes from different modalities are extracted and feature

fusion is performed. Finally,
as
model.

input

and classiﬁed using a

the fused features are used
(RF)
random forest

The algorithm primarily provides the following three con-

tributions to multimodal seizure detection.

1) We propose a novel multimodal pattern transformation
method: MLDTP maps features of different modal sig-
nals to the same feature space.

2) We optimize the parameters of MLDTP using AOA,
and the results indicate that the performance metrics of
the model tend to converge after a certain number of
algorithm iterations, with the greatest improvement often
observed in the ﬁrst iteration.

3) We extensively discuss the impact of different fusion
strategies on model performance, including decision-
level fusion and feature-level fusion. A comparison
reveals that under the second fusion strategy, accuracy,
precision, and F1 score are superior to the ﬁrst strategy,
while sensitivity may be higher under the ﬁrst strategy
in speciﬁc circumstances.

The remainder of this article is organized as follows.
the data set and the methodology used
In Section II,
including multimodal signal data acquisi-
are described,
tion, multimodal data preprocessing, MLDTP coding, feature
extraction, parameter selection, feature fusion, and classiﬁca-
tion. In Section III, the performance of the experimental results
is evaluated and analyzed. In Section IV, the effectiveness
of the algorithm proposed in this article is discussed. In
Section V, this article is summarized.

II. DATA SET AND METHODOLOGY

This method ﬁrst preprocesses the multimodal data, encodes
the preprocessed multimodal signals separately using MLDTP,
and then employs the AOA algorithm to select the optimal
MLDTP parameters for each modality. Next,
it extracts
histogram features of the MLDTP, performs feature fusion,
and ﬁnally inputs these fused features into the RF classiﬁer
for seizure detection. The framework of
the multimodal
signal classiﬁcation algorithm is shown in Fig. 1. A spe-
is given
ciﬁc description of
below.

the details of each part

A. Multimodal Data Collection

The data of epileptic patients is collected by the Biovital
P1 system, which consists of the Oppo Watch 2 and Biovital
Sensor. This device enables continuous data collection for
up to 12 h and features a simple wearing mechanism that
does not require specialized training for users. The use of
the Biovital P1 for data collection is not constrained by
environmental settings nor is it disrupted by physical activity,
thereby ensuring the capture of data in the most authentic
scenarios. The precision of the collected data for ACC, GYR,
EMG, and EDA activity are 0.0005 g, 0.61 deg/s, 12 bit,
and 0.01 ms, respectively. Their sampling frequencies are
50, 50, 200, and 4 Hz, respectively. The data for this study
is collected at the Children’s Hospital, Zhejiang University
School of Medicine (CHZU) and the fourth Afﬁliated Hospital

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:50 UTC from IEEE Xplore.  Restrictions apply. 

WU et al.: NOVEL SEIZURE DETECTION METHOD BASED ON THE FEATURE FUSION

27547

Fig. 1. Framework for classiﬁcation of multimodal signals.

TABLE I
SPECIFICATIONS OF DATA SET

Fig. 2. Process of collecting data from epileptic patients.

of Anhui Medical University. The process of data collection
is illustrated in Fig. 2. Between 2021 and 2024, a total of 18
patients with valid seizure data (MS_1–MS_18) are used in
this study, with a total recording duration of 121.9 h. Because
the duration of interseizure period data recorded for patients
far exceeds that of seizure periods, this study averages the
data of interseizure periods and seizure periods, truncating
the interseizure period data to the same length as the seizure
periods for experimental research. This study focuses on the
classiﬁcation of seizure period and interseizure period. The
patient statistics information of gender, age, and seizures is
detailed in Table I.

B. Multimodal Data Preprocessing

The data is preprocessed to eliminate artifacts for further
analysis. Band-pass ﬁltering is performed on ACC, GYR, and
EMG data at 1–24 Hz, 1–24 Hz, and 20–90 Hz, respectively,

to eliminate motion artifacts and baseline noise contamination
as well as high-frequency interference [27], and calculate the
acceleration norms Facc and Fgyr for ACC and GYR

Facc =

(cid:2)

(cid:2)

acc2
x

+ acc2
y

+ acc2
z

Fgyr =

gyr2
x

+ gyr2
y

+ gyr2
z

(1)

(2)

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:50 UTC from IEEE Xplore.  Restrictions apply. 

27548

IEEE INTERNET OF THINGS JOURNAL, VOL. 11, NO. 16, 15 AUGUST 2024

where α1 and α2 are the determination thresholds of the
LDTP code, which are adaptively optimized by AOA. The
three values solved by LDTP correspond to four different
microstructures. When ψ(k) = 1,
is deﬁned as rising
structure. When ψ(k) = −1, it is deﬁned as falling structure.
When ψ(k) = 0 (α2 ≤ d(k) < 0), it is deﬁned as slowly falling
structure. When ψ(k) = 0 (0 ≤ d(k) < α1), it is deﬁned as
slowly rising structure. Fig. 5 illustrates these various states,
with the region between the blue and orange dashed lines
referred to as the difference intervals c1 and c2, where c1 ∈
[0, α1) and c2 ∈ [α2, 0).

it

2) Double Threshold Binarization: Encode LDTP into
RLDTP for rising mode and FLDTP for falling mode using
binary threshold functions rψ(k) and f ψ(k). They are then
considered as two independent channels of MLDTP encoding
for the input of multibit relation construction. rψ(k) and f ψ(k)
are calculated as follows:

(cid:9)

rψ(k) =

f ψ(k) =

1, ψ(k) = 1
0, ψ(k) ≤ 0

(cid:9)

1, ψ(k) = −1
0, ψ(k) ≥ 0.

(6)

(7)

3) Multibit Relational Representation: After calculating
RLDTP and FLDTP codes,
relationships of
FLDTP and RLDTP codes can be converted into decimal
codes using (8) and (9), respectively

the multibit

rBP(p, n) =

fBP(p, n) =

n−1(cid:10)

j=0
n−1(cid:10)

j=0

rψ(p) · f (n, j)

f ψ(p) · f (n, j)

(8)

(9)

where p ∈ [1, r−n] is the pth sampling point and n ∈ [1, r−1]
is the number of bits of the ﬁrst-order difference matrix used
to construct the multibit code for the number of bits selected
in the determination, f (n, j) is an encoding equation deﬁned as

f (n, j) = 2n−j−1 ∀j ∈ [0, n − 1].

(10)

Differential binarization of FLDTP and RLDTP decimal codes
can be expressed as
(cid:9)

mRLDTP(p, n) =

mFLDTP(p, n) =

1,
0,

(cid:9)

1,
0,

rBP(p + 1, n) − rBP(p, n) > 0
otherwise

fBP(p + 1, n) − fBP(p, n) > 0
otherwise

(11)

(12)

where p ∈ [1, r − n − 1]. Then, the MLDTP code value can
be expressed as

Fig. 3. Description of the two independent channels of LDTP.

where accx, accy, and accz are the components of acceleration
on x-axis, y-axis, and z-axis, respectively. gyrx, gyry, and gyrz
are the components of angular velocity on x-axis, y-axis, and
z-axis, respectively. Then, multimodal data is segmented into
5 s epochs with overlap of 80%.

C. Adaptive MLDTP Conversion

MLDTP can be divided into three stages.
1) The local difference ternary pattern (LDTP) is achieved
by comparing the sample values of adjacent points. It
deﬁnes three types of structures in the signal: rising state,
falling state, and steady state, represented by 1, −1, and
0, respectively, providing a comprehensive reﬂection of
the signal’s ﬂuctuation characteristics.

2) Double threshold binarization is applied to encode
LDTP,
representing the rising mode (RLDTP) and
falling mode (FLDTP), simplifying the complex ternary
patterns into simple binary patterns, and simplify the
LDTP code while retaining the original encoding
information, as shown in Fig. 3.

3) Multibit relationship representation. After converting
multimodal signals into RLDTP codes and FLDTP
codes, construct multibit relationships for ascending and
descending patterns separately. The correlation between
different bits is enhanced while maintaining local struc-
tural features. Fig. 4 illustrates the process of converting
multimodal signal into MLDTP code.

1) Local Differential Ternary Pattern: Let a segment of
sampled signal be represented by X, where x represents the
value of the sampled signal

(cid:3)
x1

X =

(cid:4)

x2

. . .

xr

(3)

where r denotes the number of sampling points. The calcula-
tion process is consistent for different modal signals.

The differential values are obtained by performing differen-

tiation operations on the sample points of the signal

d(k) = xk+1 − xk
where k ∈ [1, r − 1] is the number of bits of the ﬁrst-order
difference matrix. Comparing d(k) with the thresholds α1 and
α2. Values greater than α1 are mapped to 1, values less than α2
are mapped to −1, and values between α1 and α2 are mapped
to 0. The equation for LDTP encoding is as follows:

(4)

ψ(k) =

⎧
⎪⎨

⎪⎩

1,
0,
−1,

d(k) ≥ α1
α2 ≤ d(k) < α1
d(k) < α2

(5)

fMLDTP(i, v, n) =

rMLDTP(i, v, n) =

v−1(cid:10)

j=0
v−1(cid:10)

j=0

mRLDTP(i + j, n) · f (v, j)

(13)

mFLDTP(i + j, n) · f (v, j)

(14)

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:50 UTC from IEEE Xplore.  Restrictions apply. 

WU et al.: NOVEL SEIZURE DETECTION METHOD BASED ON THE FEATURE FUSION

27549

Fig. 4. Adaptive MLDTP conversion process.

Fig. 5. Four types of signal structures.

where i ∈ [1, r − v − n], v ∈ [1, r − n − 1] is the number of
bits of the second neighborhood difference binarization used to
determine the bit code selected for constructing the MLDTP.

D. Feature Extraction

The rMLDTP and fMLDTP codes which derive from
relationship
Section II-C are used to construct multibit
between the neighboring bits of RLDTP and FLDTP codes,
respectively. Each code implies the local information of differ-
ent modal signals. Therefore, it is very effective to represent
the frequency of these local information by histogram features
which can be calculated as follows:

(cid:11)

P(ci) = s{ci}
i s{ci}
where ci denotes one of the code values of the MLDTP code,
and s{ci} denotes frequency of the code value appears in the
MLDTP code.

, 1 ≤ i ≤ 2v

(15)

Four different modal signals pass through MLDTP to obtain
eight channel code values, half of which are in the rising mode
channels and the other half are in the falling mode channels.
Feature extraction is performed on the code values of these two
sets of modes to reﬂect the local detailed features of different
modal signals. The length of the feature vectors for different
modes is determined by the number of multibit encoding bits

v in MLDTP, with the encoding length being 2v. By extracting
histogram features, different modal signals are mapped to
the same feature space. Information complementarity between
different modes is achieved through feature fusion. We provide
a new perspective for multimodal signal processing, especially
for 1-D time-series signals like physiological electrical signals,
where local ﬂuctuation information is of signiﬁcant importance
for seizure detection.

E. Optimal MLDTP Parameter Selection

AOA is a population-based optimization algorithm proposed
by Hashim et al. [28]. It is a versatile optimization method
capable of addressing a wide range of problems across various
domains. The algorithm draws inspiration from Archimedes’
principle, modeling the behavior of objects submerged in
ﬂuid. In this method, the individuals of the population are
submerged objects, and each individual has three attributes
besides position: 1) density; 2) volume; and 3) acceleration.
The acceleration of an object is adjusted by altering its density
and volume, and the acceleration, together with the current
position, determines the new position of the individual. Similar
to other population-based metaheuristic algorithms, AOA also
features an initial population search process with random
volumes, densities, and accelerations. After the evaluation of
the population ﬁtness, the AOA iteration begins and continues
until the number of iterations reaches the value preset by the
user. In this article, the AOA algorithm is utilized to optimize
the parameters α1 and α2 of MLDTP. The parameter settings
for AOA are shown in Table II.

1) Initialization: First, we need to initialize the positions of
all objects. The position Oi of the ith object is determined by
Oi = lbi + rand · (ubi − lbi), i = 1, 2, . . . , N

(16)

where ubi and lbi represent the upper and lower bounds on
α1 and α2 in MLDTP, N is the initial population size, rand is
a random number in the range [0, 1] (including the following
rand), proceed to initialize the volume and density of the ith
object:

deni = rand

(17)

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:50 UTC from IEEE Xplore.  Restrictions apply. 

27550

IEEE INTERNET OF THINGS JOURNAL, VOL. 11, NO. 16, 15 AUGUST 2024

TABLE II
AOA INITIALIZATION PARAMETERS

voli = rand.

(18)

Similarly, an object in ﬂuid will inevitably have accelera-

tion. Use (19) to initialize the acceleration of the ith object

acci = lbi + rand · (ubi − lbi).

(19)

After initialization is complete, we need to evaluate the
ﬁtness of the object and select the object with the best MLDTP
parameters. The optimal properties of the object are updated
simultaneously (denbest, volbest, accbest, and xbest).

2) Update the Density and Volume: The volume and den-
sity of the object are updated. In AOA,
the volume and
density of an object are not ﬁxed and are calculated using the
following formula:
dent+1
i
volt+1
i

(cid:12)
denbest − dent
i
(cid:13)
(cid:12)
volbest − volt
i

+ rand ·
+ rand ·

= dent
i
= volt
i

(20)

(21)

(cid:13)

where denbest and volbest are the density and volume of the
best individual in the population from the initialization to the
tth iteration. t represents the current iteration of the algorithm,
and t + 1 represents the next iteration.

3) Transfer the Operator and Density Factor: In the early
stages of the algorithm, collisions occur between objects,
and over time, objects attempt to reach an equilibrium state.
This process is implemented by the transfer operator TF.
TF increases over time until it reaches 1, helping the object
transition from the exploration phase to the exploitation phase
(cid:14)

(cid:15)

TF = exp

t − tmax
tmax

where tmax is the maximum number of iterations. The density
decay factor helps the AOA algorithm transition from global
search to local search

d = exp

(cid:14)

tmax − t
tmax

(cid:15)

(cid:14)

−

(cid:15)
.

t
tmax

4) Update the Acceleration: The updating process of accel-
eration can be divided into two phases based on the value of
the transfer operator, which are the exploration phase and the
exploitation phase.

Exploration Phase: When TF ≤ 0.5, collisions occur
between individuals, so the update method for the individual
acceleration of object i is

acct+1
i

= denmr + volmr · accmr

dent+1
i

· volt+1
i

(24)

where denmr, volmr, and accmr represent
density, and volume of random materials, respectively.

the acceleration,

(22)

(23)

Exploitation Phase: When TF > 0.5, collisions no longer
occur between individuals, and the update method for the
individual acceleration of object i is

= denbest + volbest · accbest

acct+1
i

dent+1
i
where accbest represents the optimal acceleration from the
initialization to the tth iteration.

· volt+1
i

Normalize the Acceleration: The acceleration is standard-

(25)

ized to obtain at+1

i−norm

at+1
i−norm

= u ·

− mini
(cid:17)

acct+1
i
(cid:16)
acct+1
i

− mini

(cid:17)

(cid:16)
acct+1
i
(cid:16)
acct+1
i

maxi

(cid:17) + l

(26)

where u and l are set to 0.9 and 0.1, respectively, to denote
the normalization range.

5) Update Position: When the object is in the exploration
phase (TF ≤ 0.5), update the individual position using (27).
When the object is in the exploitation phase (TF > 0.5),
update the individual position using (28)
(cid:12)
+ C1 · rand · acct+1
xrand − xt
i
(cid:12)
H · xbest − xt
· d ·
i
(28)

· d ·
+ Q · C2 · rand · acct+1

xt+1
i
xt+1
i

= xt
i
= xt

(27)
(cid:13)

i−norm

i−norm

best

(cid:13)

(cid:9)

Q =

+1,
−1,

if P ≤ 0.5
if P > 0.5

(29)

where xt
best represents the optimal object position in the tth
iteration. xbest represents the optimal object position from the
initialization to the tth iteration. H = C3 · TF is directly
proportional to the transfer operator. The initial setting for H
is [0.3 · C3, 1], and it takes a certain percentage of the optimal
position. The percentage it occupies is increasing over time,
and this increase in percentage is shortening the distance to
the globally optimal solution. Q is a ﬂag for changing the
direction of motion. P is a random number within a speciﬁed
range, deﬁned as P = 2 · rand − C4. The values of C1, C2,
C3, and C4 are 2, 6, 1, and 0.5, respectively. It should be
noted that the values of C1, C2, C3, and C4 are set according
to [28].

Then, the object that obtained the optimal MLDTP parame-
ters from the initialization to the current iteration is evaluated
using the objective function, and denbest, volbest, accbest, and
xbest are updated. When the maximum number of iterations
is reached,
the optimization ends, and the best MLDTP
parameters are passed on to complete the subsequent seizure
detection process. Fig. 6 represents the MLDTP parameter
optimization process.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:50 UTC from IEEE Xplore.  Restrictions apply. 

WU et al.: NOVEL SEIZURE DETECTION METHOD BASED ON THE FEATURE FUSION

27551

that of interseizure periods, the RF output is deemed to be in
favor of seizure periods. This multimodel voting mechanism
effectively mitigates the risk of overﬁtting while enhancing
model stability [29], [30], [31]. In this study, when utilizing
the RF classiﬁer, a balance is struck between the accuracy,
robustness and computational cost of the RF model, resulting
in the integration of 300 decision trees.

This study assesses the classiﬁcation performance of the
algorithm through ﬁvefold cross-validation. Initially, data from
four different modalities are divided into ﬁve equally sized
subsets using the same methodology. One of these subsets
is set aside as a test set for evaluating model performance,
while the remaining subsets are employed for model training.
Subsequently, each subset takes its turn as the test set in a total
of ﬁve iterations. Performance metrics, including accuracy,
precision, sensitivity, and F1 score, are employed as evaluation
criteria. Finally, the results of the ﬁve performance evaluations
are averaged to provide the ultimate assessment of model
performance.

III. EXPERIMENTS AND RESULTS

In this section, we conduct a series of experimental analysis
on a multimodal data set. First, we examine the inﬂuence
of LDTP parameters passed during each iteration of AOA
on model performance. Second, we discuss the correlation
between the number of multibit optimized coding bits and the
model performance, and verify the feasibility of the algorithm
and its effectiveness by comparing the results before and after
classiﬁcation. Finally, we analyze and discuss the impact of
two fusion strategies (decision-level fusion and feature-level
fusion) on the experimental results, and compared MLDTP
with existing methods based on this data set.

To assess the performance of the model, this article employs
accuracy, precision, sensitivity, and F1 score as metrics, which
can be calculated as follows:

Ac =

TP + TN
TP + FN + FP + TN

Pr =

TP
TP + FP
TP
Se =
TP + FN
F1 = 2 · Pr · Se
Pr + Se

(32)

(33)

(34)

(35)

where TP, TN, FP, and FN, respectively, represent the number
of correct seizure periods detected, the number of correct
interseizure periods detected, the number of incorrect seizure
interseizure
periods detected, and the number of incorrect
periods detected during the detection process.

A. Selection of LDTP Parameters

In order to explore the effect of LDTP parameters α1
and α2 on model performance separately, we investigate
the effect of the threshold parameters of LDTP on model
performance without using multibit coding, and compare the
model performance under different parameters. The default
LDTP initial thresholds α1 and α2 are 0, and after optimizing

Fig. 6. Utilize AOA to optimize the parameters of the MLDTP process.

F. Seizure Detections

article

discusses

Fusion: This

1) Information

two
multimodal fusion methods: 1) feature-level fusion and 2)
decision-level fusion. Feature-Level Fusion: The MLDTP
algorithm used in Section II-C maps features from different
to a common feature space, enhancing the
modalities
accuracy of data analysis and processing. By concatenating
feature matrices,
information from different modal signals
complements each other, addressing the issue of insufﬁcient
from individual modalities. Decision-Level
information
Fusion: A voting system based on weighted fusion is
designed, where signals from each modality are individually
trained to obtain different modality classiﬁcation models, and
corresponding weights are assigned to each model. The voting
result L is determined by the decision threshold θ

θ = 0.2 · Lacc + 0.3 · Lgyr + 0.4 · Lemg + 0.1 · Leda

(cid:9)

L =

θ > γ
1,
0, otherwise

(30)

(31)

where Lacc, Lgyr, Lemg, and Leda represent the voting results of
the four modalities, with 1 indicating the seizure period and
0 indicating the interseizure period. The weights for different
modalities are determined based on their accuracy. The issue
of the value of γ will be discussed in detail in the experimental
section.

2) Random Forest: In this study, RF is used as the clas-
siﬁcation model for seizure detection. RF is an ensemble of
numerous decision trees, with the ﬁnal classiﬁcation result
being a collective decision made by these constituent trees. In
the context of binary classiﬁcation for seizure and interseizure
periods, if the count of votes favoring seizure periods exceeds

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:50 UTC from IEEE Xplore.  Restrictions apply. 

27552

IEEE INTERNET OF THINGS JOURNAL, VOL. 11, NO. 16, 15 AUGUST 2024

TABLE III
APPLICATION OF DIFFERENT ENCODING METHODS ON ACC, GYR, EMG, AND EDA

Fig. 7. AOA-LDTP performance optimization curve.

the model performance for the LDTP thresholds for the
four modalities, the curve of model performance with the
number of iterations is shown in Fig. 7. When using AOA
to optimize LDTP parameters, we ﬁrst initialize AOA with
a population size of 20 and a population dimension of 2.
Next, we specify different LDTP threshold ranges for different
modalities. The LDTP parameter ranges for different modal
signals are shown in Table II. From the accuracy change curve
of the model prediction results, it is evident that selecting
appropriate LDTP parameters is crucial for improving the
classiﬁcation performance of the model.

B. Performance Analysis of MLDTP

To study the impact of different bit numbers on MLDTP,
we discuss MLDTP encoding bit numbers in Table III (indi-
vidually for ACC, GYR, EMG, and EDA). From LDTP to
AOA-MLDTP (multibit encoding with n = 4), the accuracy,
precision, sensitivity, and F1 score for each modality are
listed. We ﬁnd that the accuracy for all modalities reaches the
optimum when the encoding bit number in MLDTP is n = 2.

Fig. 8.
Classiﬁcation accuracy of the model under different encoding
methods, where L, A-L, and A-M, respectively, represent LDTP, AOA-LDTP,
and AOA-MLDTP (when n = 2, the accuracy of all modalities is at its
highest).

Therefore, we select n = 2 as the optimal MLDTP parameter.
The classiﬁcation accuracy under different methods is shown
in Fig. 8.

In order to verify that

the AOA algorithm can effec-
tively enhance the performance of the MLDTP algorithm,
we conduct multibit encoding on the unoptimized LDTP.
The comparison results are shown in Fig. 9. Through the
comparison, we observed that
the performance of AOA-
MLDTP is superior to MLDTP. Therefore, we can infer
that optimizing LDTP parameters is necessary for improving
model performance. Additionally, it is evident that multibit
encoding, whether in MLDTP or AOA-MLDTP, consistently
enhances model performance.

C. Performance Analysis of Decision-Level Fusion and
Feature-Level Fusion

In this section, we extensively discuss decision-level fusion
and feature-level fusion, further analyzing the impact of

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:50 UTC from IEEE Xplore.  Restrictions apply. 

WU et al.: NOVEL SEIZURE DETECTION METHOD BASED ON THE FEATURE FUSION

27553

Fig. 9.
AOA and multibit encoding simultaneously.

Comparing the use of multibit encoding alone versus using both

TABLE IV
PERFORMANCE ANALYSIS UNDER DIFFERENT SENSITIVITIES
OF VOTING SYSTEM

fusion strategies on seizure detection. The optimal MLDTP
parameters obtained in Sections III-A and III-B are used for
the feature extraction part of this section.

Decision-Level Fusion: We employ a fusion strategy based
on weighted voting (30) and (31), setting weights for seizure
detection accuracy from different modalities (ACC, GYR,
EMG, and EDA with weights of 0.2, 0.3, 0.4, and 0.1, respec-
tively), and discuss seizure detection scenarios at different
threshold values γ , as shown in Table IV.

By observing the relationship between threshold γ and
model performance, we notice that as the threshold gradually
increases, the accuracy, sensitivity, and F1 score of the model
all show a decreasing trend, with only precision showing
continuous improvement. The reason for this phenomenon is
that a lower threshold allows fewer votes or lower weighted
votes to determine whether a seizure occurs, leading to an
increase in model sensitivity. In the case of γ = 0.05, only
any one modality signal is required to detect seizures. On
the other hand, a higher threshold requires more votes or
higher weighted votes to determine a seizure, resulting in a
decrease in sensitivity but an increase in precision. In the case
of γ = 0.95, all modalities is required to detect a seizure
for the system to classify the result as a seizure event. In
some scenarios where high sensitivity is required for detecting
seizures, this can be achieved by setting appropriate thresholds.
The analysis results are illustrated in Fig. 10.

Fig. 10. Curve of classiﬁer performance with varying threshold γ in a voting
system.

Feature-Level Fusion: In this section, we focus on dis-
cussing the impact of different modality combinations on
seizure detection. In Sections III-A and III-B, we map signals
from different modalities to the same feature space. Now, we
concatenate signals from different modalities. The results are
presented in Table V. From Table V, we observe that when
integrating information from four modalities ACC, GYR,
EMG, and EDA, the model achieves accuracy, sensitivity, and
F1 scores of 96.81%, 95.24%, and 96.87%, respectively, which
are the highest among all fusion methods. This indicates that
integrating information from multiple modalities can lever-
age complementary information between different modalities,
thereby enhancing the classiﬁcation performance of the model.
In Table VI, we compare our method with conventional
time–frequency domain feature extraction and MLNDP meth-
ods using the same data set. Compared to the other two
methods, our method improves the accuracy, precision, sensi-
tivity, and F1 score by 2.54%–3.65%, 0.95%, 3.73%–7.08%,
and 2.42%–6.87%,
respectively. Therefore, our proposed
seizure detection algorithm based on MLDTP is indeed effec-
tive in the application of multimodal signals, providing new
insights for multimodal seizure detection.

IV. DISCUSSION

In Table VI, we compare our method with other methods.
When using conventional time–frequency feature extraction
methods, the accuracy, sensitivity, and F1 score of seizure
detection are 93.16%, 88.16%, and 90.00%, respectively.
When using the MLNDP proposed in 2023, the accuracy,
precision, sensitivity, and F2 score of seizure detection
are 94.27%, 97.60%, 91.51%, and 94.45%,
respectively.
Compared to the above two methods, AOA-MLDTP achieves
the best performance in all performance metrics, with an accu-
racy, precision, sensitivity, and F1 score of 96.81%, 98.55%,
95.24%, and 96.87% for seizure detection. This indicates that
the application of AOA-MLDTP on multimodal signals is
indeed effective. Local pattern encoding has achieved positive
results in the classiﬁcation performance of signals across
different modalities, thanks to its effectiveness in describing

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:50 UTC from IEEE Xplore.  Restrictions apply. 

27554

IEEE INTERNET OF THINGS JOURNAL, VOL. 11, NO. 16, 15 AUGUST 2024

TABLE V
PERFORMANCE ANALYSIS OF MODEL CLASSIFICATION UNDER DIFFERENT FUSION STRATEGIES

TABLE VI
COMPARISON OF DIFFERENT FEATURE EXTRACTION METHODS

texture features of signals. For 1-D time-series
the local
signals,
the ﬁrst-order difference between adjacent sample
points can describe the signal’s trend at the current moment.
Each MLDTP code value obtained using the MLDTP method
can correspond to a speciﬁc inherent change pattern of the
signal within that time period. Traditional binary encoding can
only describe two types of structures in signals rising and
falling, which is not conducive to a comprehensive description
of a signal segment. To address this, MLDTP encoding
introduces two additional structures for signals: 1) slowly
rising structure and 2) slowly falling structure (as shown in
Fig. 5), containing richer local texture features. By statistically
analyzing the frequencies of different code words, the overall
change pattern of the signal within that time period can be
reﬂected. Compared to the cumbersome process of calculat-
ing multimodal signal features in conventional methods, the
MLDTP algorithm simpliﬁes the feature extraction process
while ensuring performance. Furthermore, compared to tra-
ditional local pattern transformation algorithms, it achieves
better results across different modalities.

V. CONCLUSION

In this article, we propose a novel multimodal seizure
detection algorithm. By extracting the MLDTP histogram
features, we map features from different modalities to the same
feature space. We optimize the MLDTP parameters separately
for different modalities to achieve the best seizure detection
performance on individual modalities. Through feature fusion,
we enhance information complementarity between different

modalities, effectively improving the precision and sensitivity
of seizure detection.

The MLDTP algorithm proposed in this article improves
upon the traditional local pattern transformation method by
introducing a dual-channel encoding mode that includes both
rising and falling patterns. The advantage of dual-channel
encoding over traditional encoding is its ability to incorporate
more local signal ﬂuctuation information. Additionally, we
construct neighborhood multibit relationships for both rising
and falling patterns, enriching local features while increasing
temporal correlations. The algorithm is validated on a data
set containing data from 18 epilepsy patients, achieving
accuracy, precision, sensitivity, and F1 score of 96.81%,
98.55%, 95.24%, and 96.87%, respectively. Compared to other
algorithms, this algorithm demonstrates better classiﬁcation
performance on multimodal signals. This study is conducted
under the condition of balanced positive and negative sample
sizes. In the future, we will consider adding more samples
and choose one of g-mean, Matthews correlation coefﬁcient
(MCC), or kappa as the performance metric for optimizing the
parameters of the MLDTP algorithm, in order to address the
optimization error issue caused by the imbalance of positive
and negative sample data. We will further reﬁne our device
and algorithms, transmit data through Bluetooth and WiFi,
and develop it into an IoT product, allowing for its extensive
application in outpatient medical settings.

REFERENCES

[1] A. Shoeibi et al., “A comprehensive comparison of handcrafted features
and convolutional autoencoders for epileptic seizures detection in EEG
signals,” Expert Syst. Appl., vol. 163, Jan. 2021, Art. no. 113788.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:50 UTC from IEEE Xplore.  Restrictions apply. 

WU et al.: NOVEL SEIZURE DETECTION METHOD BASED ON THE FEATURE FUSION

27555

[2] T. Kim et al., “Epileptic seizure detection and experimental treatment:

A review,” Front. Neurol., vol. 11, p. 701, Jul. 2020.

[3] F. S. Leijten et al., “Multimodal seizure detection: A review,” Epilepsia,

vol. 59, pp. 42–47, Jun. 2018.

[4] B. H. Brinkmann et al., “Seizure diaries and forecasting with wear-
ables: Epilepsy monitoring outside the clinic,” Front. Neurol., vol. 12,
Jul. 2021, Art. no. 690404.

[5] S. Jahan et al., “AI-based epileptic seizure detection and prediction in
Internet of healthcare things: A systematic review,” IEEE Access, vol. 11,
pp. 30690–30725, Mar. 2023.

[6] J. Li and Q. Wang, “Multi-modal bioelectrical signal fusion analysis
based on different acquisition devices and scene settings: Overview,
challenges, and novel orientation,” Inf. Fusion, vol. 79, pp. 229–247,
Mar. 2022.

[7] M. Miloševi´c et al., “Automated detection of tonic–clonic seizures
using 3-D accelerometry and surface electromyography in pedi-
atric patients,” IEEE J. Biomed. Health Informat., vol. 20, no. 5,
pp. 1333–1341, Sep. 2015.

[8] F. Onorati et al., “Multicenter clinical assessment of improved wearable
multimodal convulsive seizure detectors,” Epilepsia, vol. 58, no. 11,
pp. 1870–1879, Oct. 2017.

[9] J. J. Halford et al., “Detection of generalized tonic–clonic seizures
using surface electromyographic monitoring,” Epilepsia, vol. 58, no. 11,
pp. 1861–1869, Oct. 2017.

[10] A. V. de Vel et al., “Non-EEG seizure detection systems and potential
SUDEP prevention: State of the art: Review and update,” Seizure,
vol. 41, pp. 141–153, Oct. 2016.

[11] C. Jory, R. Shankar, D. Coker, B. McLean, J. Hanna, and C. Newman,
“Safe and sound? A systematic literature review of seizure detection
methods for personal use,” Seizure, vol. 36, pp. 4–15, Mar. 2016.
[12] J. van Andel, R. D. Thijs, A. de Weerd, J. Arends, and F. Leijten, “Non-
EEG based ambulatory seizure detection designed for home use: What
is available and how will it inﬂuence epilepsy care?” Epilepsy Behav.,
vol. 57, pp. 82–89, Apr. 2016.

[13] Y. Li, H. Tang, W. Xie, and W. Luo, “Multidimensional local binary
pattern for hyperspectral image classiﬁcation,” IEEE Trans. Geosci.
Remote Sens., vol. 60, Apr. 2021, Art. no. 5505113.

[14] Y. Kaya, M. Uyar, R. Tekin, and S. Yildirim, “1D-local binary
pattern based feature extraction for classiﬁcation of epileptic EEG
signals,” Appl. Math. Comput., vol. 243, pp. 209–219, Sep. 2014.
[15] K. A. Khan, P. P. Shanir, Y. U. Khan, and O. Farooq, “A hybrid
local binary pattern and wavelets based approach for EEG classiﬁcation
for diagnosing epilepsy,” Expert Syst. Appl., vol. 140, Feb. 2020,
Art. no. 112895.

[16] O. K. Toffa and M. Mignotte, “Environmental sound classiﬁcation using
local binary pattern and audio features collaboration,” IEEE Trans.
Multimedia, vol. 23, no. 1, pp. 3978–3985, Nov. 2020.

[17] Q. Luo, J. Su, C. Yang, O. Silven, and L. Liu, “Scale-selective and noise-
robust extended local binary pattern for texture classiﬁcation,” Pattern
Recognit., vol. 132, Dec. 2022, Art. no. 108901.

[18] Y. El Merabet, Y. Ruichek, and A. El Idrissi, “Attractive-and-repulsive
center-symmetric local binary patterns for texture classiﬁcation,” Eng.
Appl. Artif. Intell., vol. 78, pp. 158–172, Feb. 2019.

[19] X. Huang, S.-J. Wang, X. Liu, G. Zhao, X. Feng, and M. Pietikäinen,
“Discriminative spatiotemporal
local binary pattern with revisited
integral projection for spontaneous facial micro-expression recog-
nition,” IEEE Trans. Affect. Comput., vol. 10, no. 1, pp. 32–47,
Jan.–Mar. 2019.

[20] R. Ding, J. Ren, H. Yu, and J. Li, “Dynamic texture recognition using
PDV hashing and dictionary learning on multi-scale volume local binary
pattern,” in Proc. IEEE Int. Conf. Acoust., Speech Signal Process.
(ICASSP), May 2022, pp. 1840–1844.

[21] Z. Zheng et al., “Circumferential local ternary pattern: New and efﬁcient
feature descriptors for anti-counterfeiting pattern identiﬁcation,” IEEE
Trans. Inf. Forensics Security, vol. 17, pp. 970–981, Feb. 2022.
[22] W. Zhang, D. Wu, J. Cao, L. Jiang, and T. Jiang, “Multi-bit local
neighborhood difference pattern optimization for seizure detection of
west syndrome EEG signals,” IEEE Sensors J., vol. 23, no. 19,
pp. 22693–22703, Oct. 2023.

[23] S. Lan, H. Fan, S. Hu, X. Ren, X. Liao, and Z. Pan, “An edge-located
uniform pattern recovery mechanism using statistical feature-based
optimal center pixel selection strategy for local binary pattern,” Expert
Syst. Appl., vol. 221, Jul. 2023, Art. no. 119763.

[24] E. Akbal, P. D. Barua, S. Dogan, T. Tuncer, and U. R. Acharya,
“Explainable automated anuran sound classiﬁcation using improved
one-dimensional local binary pattern and tunable Q wavelet transform
techniques,” Expert Syst. Appl., vol. 225, Sep. 2023, Art. no. 120089.

[25] E. Al-Wajih and R. Ghazali, “Threshold center-symmetric local binary
convolutional neural networks for bilingual handwritten digit recogni-
tion,” Knowl.-Based Syst., vol. 259, Jan. 2023, Art. no. 110079.
[26] T. S. Kumar, K. N. V. P. S. Rajesh, S. Maheswari, V. Kanhangad,
and U. R. Acharya, “Automated schizophrenia detection using local
descriptors with EEG signals,” Eng. Appl. Artif. Intell., vol. 117,
Jan. 2023, Art. no. 105602.

[27] K. Cuppens et al., “Accelerometry-based home monitoring for detection
of nocturnal hypermotor seizures based on novelty detection,” IEEE J.
Biomed. Health Inform., vol. 18, no. 3, pp. 1026–1033, May 2014.
[28] F. A. Hashim, K. Hussain, E. H. Houssein, M. S. Mabrouk, and
W. Al-Atabany, “Archimedes optimization algorithm: A new meta-
heuristic algorithm for solving optimization problems,” Appl. Intell.,
vol. 51, pp. 1531–1551, Mar. 2021.

[29] J. L. Speiser, M. E. Miller, J. Tooze, and E. Ip, “A comparison of
random forest variable selection methods for classiﬁcation prediction
modeling,” Expert Syst. Appl., vol. 134, pp. 93–101, Nov. 2019.
[30] R. R. Fernández, I. M. De Diego, V. Aceña, A. Fernández-Isabel, and
J. M. Moguerza, “Random forest explainability using counterfactual
sets,” Inf. Fusion, vol. 63, pp. 196–207, Nov. 2020.

[31] W. Gao and Z.-H. Zhou, “Towards convergence rate analysis of random
forests for classiﬁcation,” in Proc. 34th Adv. Neural Inf. Process. Syst.,
2020, pp. 9300–9311.

[32] Y. Ge et al., “Epilepsy analysis with portable device based multi-modal
physiological signals,” in Proc. 38th Youth Acad. Annu. Conf. Chin.
Assoc. Autom. (YAC), 2023, pp. 154–159.

Duanpo Wu received the B.S. degree from the
College of Electronics and Information, Hangzhou
Dianzi University, Hangzhou, China,
in 2009,
and the Ph.D. degree
from the College of
Information Science and Electronic Engineering,
Zhejiang University, Hangzhou, in 2014.

Since 2022, he has been an Associate Professor
with Hangzhou Dianzi University. His research
interests
signal processing,
intelligent
biological data analysis, and machine learning.

include

is

currently pursuing the master’s
Jun Wei
degree with Hangzhou Dianzi University, Hangzhou,
China.

His research interests include the signal process-
ing and machine learning applications in the ﬁeld of
seizure detection.

Pierre-Paul Vidal received the M.D. degree in 1978
and the Scientiﬁc Ph.D. degree from Univercité Paris
in 1986.

He is the Director of Research Emeritus with
the National Center for Scientiﬁc Research (CNRS),
Paris, France. He served as the Head of
the
Laboratory, CNRS from 1990 to 2020. He is also
the Scientiﬁc Director of the Platform for the Study
of Sensorimotricity with Université Paris Cité, Paris.
He also serves as a Professor in Portugal, Spain, and
China. Under his leadership, numerous achievements
in the ﬁelds of neurorehabilitation treatment equipment, electric pulse steril-
ization equipment, and smart health evaluation and monitoring systems have
been successfully implemented in hospitals in both China and France for the
fragility prevention.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:50 UTC from IEEE Xplore.  Restrictions apply. 

27556

IEEE INTERNET OF THINGS JOURNAL, VOL. 11, NO. 16, 15 AUGUST 2024

Danping Wang received the engineering and Master
of Science degrees from the Northeast Institute
of Heavy Machinery, Qiqiaer, China, in 1982 and
1988, respectively, and the Ph.D. degree from the
University Technologie de Compiègne, Compiègne,
France, in 1999.

Since 2006, she has been working as a Research
Engineer with Université Paris Cité, Paris, France.
Her research focuses on human behavior in neuro-
science and biomechanics.

IEEE)

Jiuwen Cao (Senior Member,
received
the B.Sc. and M.Sc. degrees from the School
of Applied Mathematics, University of Electronic
Science and Technology of China, Chengdu, China,
in 2005 and 2008,
respectively, and the Ph.D.
degree from the School of Electrical and Electronic
Engineering, Nanyang Technological University
(NTU), Singapore, in 2013.

From 2012 to 2013, he was a Research Fellow
with NTU. He is a Full Professor and the Dean of the
School of Automation, Hangzhou Dianzi University,
Hangzhou, China. His main research interests include machine learning, neural
networks, and intelligent signal processing.

Dr. Cao is serving as an Associate Editor of IEEE TRANSACTIONS
ON CIRCUITS AND SYSTEMS—PART I: REGULAR PAPER, Journal of the
Franklin Institute, Multidimensional Systems and Signal Processing, Memetic
Computing, and Military Medical Research.

IEEE)

Yixuan Yuan (Senior Member,
received
the B.S. degree from the College of Information
Countermeasure,
Polytechnical
University, Xi’an, China, in 2010, and the Ph.D.
degree from the College of Biomedical Engineering,
The Chinese University of Hong Kong, Hong Kong,
China, in 2016.

Northwestern

Since 2022, she has been an Assistant Professor
with The Chinese University of Hong Kong. Her
research interests include biomedical image analysis
and deep learning.

Tiejia Jiang received the B.S. degree from the
Department of Clinical Medicine, Wenzhou Medical
University, Wenzhou, China,
in 2008, and the
M.S. degree in pediatrics from Zhejiang University,
Hangzhou, China, in 2017.

He is currently the Deputy Chief Physician with
the Children’s Hospital, Zhejiang University School
of Medicine. He is mainly engaged in electrophys-
iological signal analysis and research of various
children’s neurological diseases.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:11:50 UTC from IEEE Xplore.  Restrictions apply.
