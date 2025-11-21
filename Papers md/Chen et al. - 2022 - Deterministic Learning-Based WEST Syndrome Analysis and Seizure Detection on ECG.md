# Chen et al. - 2022 - Deterministic Learning-Based WEST Syndrome Analysis and Seizure Detection on ECG

IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS—II: EXPRESS BRIEFS, VOL. 69, NO. 11, NOVEMBER 2022

4603

Deterministic Learning-Based WEST Syndrome
Analysis and Seizure Detection on ECG

Shiyao Chen , Runze Zheng, Tianlei Wang , Tiejia Jiang , Feng Gao , Danping Wang ,
and Jiuwen Cao , Senior Member, IEEE

Abstract—WEST syndrome is an unknown etiology infant
epilepsy, which is characterized by the ﬂexion spastic seizure,
intellectual motion development lag, electrode abnormalities,
arrhythmia. In this brief, we present a novel electrocardiogram
(ECG) based WEST syndrome epilepsy seizure detection method.
Based on deterministic learning (DT) theory, the dynamic model
of ECG is ﬁrstly constructed. The cardiodynamicsgrams (CDGs)
of ECGs in seizure and interictal periods are then derived.
Nonlinear features on CDGs are extracted for WEST syndrome
characterization. For performance evaluation, experiments on
ECGs of 12 WEST syndrome patients from the Children’s
Hospital of Zhejiang University School of Medicine (CHZU) is
carried out. The proposed method can obtain an average of
94.49% F1-score, 93.76% precision and 95.58% accuracy, that
outperforms the heart rate variability (HRV) based methods.

Index Terms—WEST epilepsy syndrome, ECG, seizure detec-

tion, heart rate variability, infantile spasms.

Manuscript received 24 May 2022; revised 21 June 2022; accepted 29
June 2022. Date of publication 13 July 2022; date of current version
28 October 2022. This work was supported in part by the National Key
Research and Development Program of China under Grant 2021YFE0100100
and Grant 2021YFE0205400;
in part by the National Natural Science
Foundation of China under Grant U1909209; in part by the Open Research
Projects of Zhejiang Lab under Grant 2021MC0AB04;
in part by the
Key Research and Development Program of Zhejiang Province under
Grant 2020C03038; in part by the Fundamental Research Funds for the
Provincial Universities of Zhejiang under Grant GK219909299001-411; and
in part by the General Research Projects in Zhejiang Province under Grant
Y202146999. This brief was recommended by Associate Editor G. Jovanovic
Dolecek. (Shiyao Chen and Tiejia Jiang contributed equally to this work.)
(Corresponding author: Jiuwen Cao.)

This work involved human subjects or animals in its research. Approval
of all ethical and experimental procedures and protocols was granted by the
Second Afﬁliated Hospital of Zhejiang University and registered in Chinese
Clinical Trail Registry (ChiCTR1900020726).

Shiyao Chen, Runze Zheng, and Tianlei Wang are with the Machine
Learning and I-Health International Cooperation Base of Zhejiang
Institute, Hangzhou Dianzi
Province
Intelligence
University, Hangzhou
csy_9716@163.com;
runzewuyu@hdu.edu.cn; tianleiwang@hdu.edu.cn).

and the Artiﬁcial

310018, China

(e-mail:

Tiejia Jiang and Feng Gao are with the Department of Neurology,
The Children’s Hospital, Zhejiang University School of Medicine, National
Clinical Research Center for Child Health, Hangzhou 310003, China (e-mail:
jiangyouze@zju.edu.cn; epilepsy@zju.edu.cn).

Danping Wang is with the Machine Learning and I-Health International
Cooperation Base of Zhejiang Province and the Artiﬁcial Intelligence Institute,
Hangzhou Dianzi University, Hangzhou 310018, China, and also with
the Plateforme Sensorimotricité, BioMedTech Facilities INSERM US36-
CNRS UMS2009, Université de Paris, 75270 Paris, France (e-mail: dan-
ping.wang@parisdescartes.fr).

Jiuwen Cao is with the Machine Learning and I-Health International
Cooperation Base of Zhejiang Province and the Artiﬁcial Intelligence Institute,
Hangzhou Dianzi University, Hangzhou 310018, China, and also with the
Research Center for Intelligent Sensing, Zhejiang Lab, Hangzhou 311100,
China (e-mail: jwcao@hdu.edu.cn).

Color versions of one or more ﬁgures in this article are available at

https://doi.org/10.1109/TCSII.2022.3188162.

Digital Object Identiﬁer 10.1109/TCSII.2022.3188162

I. INTRODUCTION

W EST epilepsy syndrome, known as infantile spasm,

has complex etiology and unknown mechanism. It
is characterized by decreased intellectual development and
arrhythmia. Most children have seizures within one year after
birth, with peak incidence occurring between 3-8 months.
More than half of WEST syndrome subjects will evolve
into other epilepsy syndromes, such as Lennox-Gastaut syn-
drome [1]. About 50% patients have movement disorders
and 70% suffer from intellectual disability, usually accompa-
nied by mental and behavioral problems, such as autism and
hyperactivity. Electroencephalogram (EEG) is most effective
in epilepsy analysis [2]–[6], but is inconvenient in acquisition.
Electrocardiogram (ECG) became favorable in epilepsy
analysis in recent years. WEST syndrome affects the auto-
nomic nervous system (ANS) with the accelerated tachy-
cardia [7]. In [8],
the fused features on EEG and ECG
have been studied for WEST and childhood absence epilepsy
(CAE) syndrome classiﬁcation. An early seizure detection
method for WEST syndrome based on cardiac autonomic reg-
ulation dynamics has been developed in [9]. It is recently
shown that [10] WEST syndrome subjects apparently have
an increased prevalence of cardio metabolic derangement.
Although fruitful results have been done on ECG based
epilepsy analysis, most are using heart rate variability (HRV).
The essence of the heart as a nonlinear dynamic system is
usually ignored.

As an effective and accurate modeling method for unknown
regression
dynamical nonlinear systems with periodic or
trajectories, deterministic learning (DT) [11] has been suc-
cessfully applied in myocardial ischemia of ECG [12], [13].
Inspired by DT, we present a novel WEST epilepsy syn-
drome analysis and seizure detection method in this brief.
A high-gain observer (HGO) [14] is ﬁrstly adopted to esti-
mate the ECG signal velocity and acceleration states, which
are more effective in characterizing the instantaneous change
of ECGs [15]. Then, the ECG cardiodynamicsgram (CDG) is
derived based on DT. Further, popular nonlinear features are
extracted from CDGs for WEST syndrome epilepsy character-
ization and seizure detection. The contributions of this brief
are threefold:

• The DT method is ﬁrstly applied on ECGs of WEST
syndrome for epilepsy detection through CDG features.
• A HGO is adopted for velocity and acceleration estima-
tion to effective characterize the instantaneous change.

1549-7747 c(cid:2) 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:21 UTC from IEEE Xplore.  Restrictions apply. 

4604

IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS—II: EXPRESS BRIEFS, VOL. 69, NO. 11, NOVEMBER 2022

Fig. 1. WEST syndrome epilepsy analysis and seizure detection using ECG based deterministic learning algorithm.

• Nonlinear features on CDG are derived to achieve WEST

seizure detection using machine learning method.

Experiments conducted on ECGs of 12 WEST syndrome
children recorded in children’s Hospital of Zhejiang University
(CHZU) are provided to show the advantage of our method.

II. PROPOSED DT BASED WEST SYNDROME ANALYSIS

Fig. 1 shows the structure of the proposed WEST syn-
drome seizure detection algorithm. Firstly, a HGO is adopted
on single lead ECG to estimate the velocity and acceler-
the cardiac
ation for deriving the dynamic system. Then,
dynamics extracted from ST-T ECG segments is used in
DT algorithm to build the CDGs of ECGs. Finally,
the
approximation entropy (ApEn), spectral entropy (SE), instan-
taneous frequency (IF), are taken from CDGs for epilepsy
characterization and detection.

A. High-Gain Observer

is extremely complex,

Dynamic pattern extraction in ECGs is always challeng-
ing. Since human heart
identifying
its dynamics becomes vital. It is pointed out [14] that any
dissipative systems can be approximated by a 3-dimensional
ordinary differential function with arbitrary accuracy, provid-
ing a way for ECG dynamics analysis. Based on DT, the
cardiac dynamics of ECG for myocardial ischemia has been
analyzed [16].

To effectively characterize the instantaneous change of
ECGs, we recur to using HGO [16] to estimate the ECGs’
velocity and acceleration [17], [18]. As an effective state esti-
mation method, HGO is robust to model disturbances and
uncertainties, and can estimate the derivative of the output
robustly with a rapid convergence. After ﬁltering by a median
ﬁlter, a 50 Hz notch ﬁlter and 0.5-70 Hz bandpass ﬁlter, HGO
is employed for ECG dynamics modeling. Particularly, the
velocity and acceleration estimation is performed below.

The discrete-time HGO design [19] is

q(k + 1) = Adq(k) + Bdy(k)
ˆx(k) = Cdq(k) + Ddy(k),
q(k)
the
the ECG,
estimated ECG. Here,

the

is

is

(1)

vector
state
the bilinear

where
and

y(k)
is

ˆx(k)

is

D

for

with

applied

implemen-
transformation method
Ad = (I + (α/2)Ao)(I − (α/2)Ao)−1,
tation,
Bd = α(I − (α/2)Ao)−1Ho, Cd =D−1(I − (α/2)Ao)−1,
diag[1, ε, . . . , εn−1],
Dd = (α/2)CdoHo,
Ho= [h1, h2, . . . , hn]T ,
α = Ts/ε.
Here, I is the identity matrix, Ts = 1000 Hz is the ECG
sampling frequency, α = 1, ε = 1000, and
⎞
1
0
0

=
Ao = A − HoC,

A0 =

0
1
0

0
0
0

0
0
1

and

⎛

⎝

⎞

⎛

⎠

⎝

⎠, B0 =
⎛

⎞

C0 =

(cid:6)

(cid:7)
, D0 =

⎝

0 0 1

1
0
0

0
1000
0

0
0
10002

⎠

(2)

It is shown [19] that when the observer gain and sam-
pling frequency are large enough, ˆx(k) can converge to a small
enough neighborhood. With the estimated velocity and accel-
eration, the ST-T segments will be obtained from the 3-lead
signal as they are more effective in describing myocardial
ischemia. As shown in [20], myocardial ischemia also exists
in children with epilepsy.

The ECG R wave is determined by a dynamic threshold as
SR(i) = [R(i), R(i + 1)], i = 1, . . . , N − 1

Range(i) = [R(i) + α, SR(i) + SR(i + 1)

],

(3)

2

where N and R are the R wave number and position, α is a
dynamic threshold.

B. Deterministic Learning

Deterministic learning theory (DT) [16], [21] has been
developed for dynamic system modeling with promising
achievements in many applications. Based on the persistent
excitation (PE) of radial basis function (RBF) neural network,
it is proved that local RBF can be used as the parameterized
model to accurately model unknown nonlinear system.

Assume the model of a periodic or regression trajec-

tory [12] is

x = [x1, . . . , xn]T

˙x = F(x; p), x(t0) = x0,
Rn
system parameter vector,

constant

the

is

∈

(4)

system
and

where
state, p is

a

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:21 UTC from IEEE Xplore.  Restrictions apply. 

CHEN et al.: DETERMINISTIC LEARNING-BASED WEST SYNDROME ANALYSIS AND SEIZURE DETECTION

4605

Fig. 2. CDGs of different periods of WEST epilepsy syndrome (m: minutes).

F(x; p) = [f1(x; p), . . . , fn(x; p)]T is the continuous unknown
nonlinear function. The trajectory initial point x0 is expressed
as φζ , either a periodic or a recurrent motion. To estimate
F(x; p), the estimator of RBF neural network in DT [12] is

˙ˆxi = −ai(ˆxi − xi) + ˆWT

i Si(x),

(5)

where ˆx and xi are the estimator and system states,
ai > 0 is a constant, and ˆWT
i Si(x) is used to approxi-
(4) with ˆWi = [wi1, . . . , wiN]T ∈ RN and
mate fi(x; p) of
Si(x) = [si1((cid:4)x − ξ1(cid:4)), . . . , siN((cid:4)x − ξN(cid:4))]T , sij(·) being the
Gaussian function and ξj being different points in state space.
With (4) and (5), the derivative of the state estimation error

˜xi = ˆxi − xi satisﬁes [12]

where εi = fi(x; p) − Wi
error and ˜Wi = ˆWi − Wi

˙˜xi = −ai ˜xi + ˆWT
= −ai ˜xi + ˆWT

i Si(x) − fi(x; p)
i Si(x) − εi,

(6)
T∗Si(x) is the ideal approximation
∗. Then, ˆWT
[12] can be updated by
i
˙ˆWi = ˙˜Wi = −(cid:7)iSi(x)˜xi − σi(cid:7)i

ˆWi,

(7)

where (cid:7)i is the set positive learning gain, and σi > 0 is a small
constant. Setting ˆWi(0) = 0, it has been shown in DT that for
almost every trajectory model φζ , accurate modeling of the
unknown dynamics fi(x; p) can be achieved along φζ [12]
i Si(φζ ) + εζ i = ¯WT
ˆWζ (t)
where
the arithmetic mean,
0 < ta < tb is the period after the transient process and
εζ i1 = O(εζ i) = O(εi) is the approximation error.

fi(φζ ; p) = ˆWT
¯Wζ = meant∈[ta,tb]

i Si(φζ ) + εζ i1,

(8)

is

In this brief, the ECG dynamic is modeled [12] using the

ST-T segments as

˙V = F(V),

(9)

where V = [vX, vY , vZ]T represents the ECG and its velocity,
acceleration obtained by HGO, F(V) = [fX(V), fY (V), fZ(V)]T
is the CDGs underlying the 3D pattern φV . Based on DT
theory, (i ∈ {X, Y, Z}), the CDGs fi(V)(i ∈ {X, Y, Z}) can be
accurately estimated using 3 RBF networks ˆWT

i Si(φζ ).

Fig. 2 shows the ECG CDGs of 5 different periods, namely
seizure onset, interictal periods with 0-10, 10-20, 20-30, more
than 30 minutes from seizure onset of a WEST epilepsy sub-
ject. As clearly observed, 1) the CDG morphology of ECG in
interictal stage with 30 minutes away from epilepsy seizure
shows a regular curve, 2) the CDG morphology becomes
messy for ECGs gradually approaching the onset period,

(cid:6)

(cid:7)

0 0 1
−1(x(1)T − Ddy(1))

Algorithm 1 DT Based WEST Epilepsy ECG Learning
Input: ECG y(i), α, Ts, Ad, Bd, Cd, Dd, N, α
˙ˆx, ApEn, IF, SE
Output: CDG,
1: ˆx(1) =
2: q(1) = Cd
3: for k = 1 to N do
4:
5:
6: end for
7: for i = 1 to N do
8:

ˆx(k) = Cdq(k) + Ddy(k)
q(k + 1) = Adq(k) + Bdy(k)

mean(i) = (R(i) + R(i + 1))/2
Range(i) = [R(i) + α, mean(i)]

9:
10: end for
11:

˙ˆxi = −ai(ˆxi − xi) + ˆWT
˙ˆx ⇒ Obtain CDG based ApEn, IF and SE

i Si(x)

12:

3) The closer to seizure, the more cluttered CDG morphology
curves will be.

C. Dynamic Feature Extraction

To further characterize CDGs, 3 popular nonlinear features,
approximation entropy (ApEn), spectral entropy (SE), instanta-
neous frequency (IF), are extracted. ApEn reﬂects the stability
and regularity of a signal. SE measures the spectral power
distribution of a signal. Instantaneous frequency (IF) is gen-
erally more effective than conventional Fourier transform in
representing non-stationary signals. The unique instantaneous
effectiveness of IF in depicting non-steady signal makes it
promising to extract the local pattern.

Figs. 3∼5 show the scatter plots and probability density dis-
tributions (PDFs) of ApEn, SE and IF, respectively. For each
ﬁgure, the comparisons are made between ECGs of seizure
and 2 different
interictal periods of WEST syndrome. As
observed, for all 3 dynamic features, there have clear distri-
bution differences between seizure vs two interictal periods,
making them discriminative in characterizing WEST syn-
drome. Algorithm 1 brieﬂy summarizes the proposed WEST
epilepsy seizure detection algorithm.

III. RESULTS AND ANALYSIS

A. Experiment Setups

To study the effectiveness of our proposed method, we adopt
popular machine learning algorithms for performance evalua-
tion [22], [23], including Long short-term memory (LSTM),

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:21 UTC from IEEE Xplore.  Restrictions apply. 

4606

IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS—II: EXPRESS BRIEFS, VOL. 69, NO. 11, NOVEMBER 2022

Fig. 3. Comparisons of ECG ApEn in seizure vs interictal.

Fig. 4. Comparisons of ECG SE in seizure vs interictal.

Fig. 6. Detection results comparing with ECG HRV features.

TABLE I
SPECIFICATIONS OF CHZU DATASET

Fig. 5. Comparisons of ECG IF in seizure vs interictal.

TABLE II
SAMPLES IN CHZU WEST SYNDROME DATASET

K-Nearest Neighbor (KNN), support vector machine (SVM)
and Random Forest (RF). For KNN, the nearest neighbor is
set to be 8. In SVM, the linear kernel is used, with C = 2,
sigma = 3. For RF, 80 decision trees are used. For LSTM,
the neural network with the bi-directional structure is applied,
and at each time step, the input feature dimensions are 3.

Besides the proposed CDGs nonlinear features, we also
compare with the ECG HRV features. For HRV, 8 time-
domain, 7 frequency-domain and 4 nonlinear features are
derived,
including the standard deviation of RR intervals,
the standard deviation of successive RR intervals, the square
root of the mean squared differences between successive RR
intervals, the mean of between successive RR intervals, the
the
quartiles of RR intervals,
the ratio
number of successive RR intervals over 50 ms,
of successive RR intervals over 50 ms, the power spectrum
of very low frequency (0.03-0.04 Hz), low frequency (LF,
0.04-0.15 Hz), high frequency (HF, 0.15-0.4 Hz), LF/HF, the
total power of all frequency bands (TP), the norms of LF
(LF-norm) and HF (HF-norm), the standard derivation (SD)
of Poincare curve of RR interval, SD1 (rapid beat-to-beat
changes), SD2 (long-term beat-to-beat changes), and SD1/SD2
are also obtained.

the coefﬁcient of variation,

For feature extraction, the frame length of ECG is set to
be 8 s with 50% overlap. Tables I and II show the dataset
speciﬁcations, and the detailed training and testing samples of
all subjects. The ECGs are collected by Nicolet V32 ampli-
ﬁer with 1000 Hz sampling frequency. All data are labeled
by neuroscientists of CHZU. The experiments are conducted

under the scenario by identifying seizure to different interictal
periods. For performance evaluation, accuracy, precision and
F1-score are calculated using the 5-fold cross-validation.

B. Results and Discussion

1) Results by CDG Nonlinear Features: Table III shows
the detailed epilepsy detection results by ECG CDGs nonlinear
features obtained by our method. As observed, 1) among these
4 classiﬁers, LSTM always achieves the best performance,
2) with CDG nonlinear features, LSTM can obtain 95.58%
accuracy when comparing seizure with the interictal period
(30 m above), 3) among 4 different scenarios, the performance
gradually becomes better when the interictal period is far away
from the seizure onset.

2) Comparisons With HRV Features: Fig. 6 shows the
detection performance comparison with ECG HRV features.
In our proposed method, we use LSTM with CDG non-
linear features, while for HRV, the classiﬁer with the best
performance is presented, namely RF. As observed, CDG non-
linear features extracted by DT algorithm on ECGs are more
discriminate than HRV features in characterizing WEST syn-
drome. The poor performance of HRV could attribute to the
feature depending on subject’s heart rate, which can be easily
interfered as WEST syndrome subjects are usually infants.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:21 UTC from IEEE Xplore.  Restrictions apply. 

CHEN et al.: DETERMINISTIC LEARNING-BASED WEST SYNDROME ANALYSIS AND SEIZURE DETECTION

4607

TABLE III
RESULTS BY CDG NONLINEAR FEATURE

IV. CONCLUSION

This brief presents a novel ECG based WEST syndrome
epilepsy analysis and seizure detection method. Applying
deterministic learning, the cardiodynamicsgram morphology
is built. The dynamic nonlinear features
of ECG signal
extracted on CDG can effectively characterize the dynamics
of WEST epilepsy ECGs in seizure and interictal periods.
The superiority of detection performance is validated using
ECGs of 12 WEST syndrome subjects. The research results
open up a new door for epilepsy syndrome and seizure detec-
tion with ECG signals using deterministic learning theory. In
the future, to reduce the false detection rate in the interic-
tal period closer to onset, more types of nonlinear features
will be explored. At the same time, the speciﬁcity of the
algorithm will be studied to exploit the applicability in real
applications.

REFERENCES

[1] A. Beaumanoir and W. Blume, “The Lennox-Gastaut syndrome,” in
Epileptic Syndromes Infancy, Childhood Adolescence, vol. 2. Montrouge,
France: John Libbey Eurotext, 2005, pp. 115–132.

[2] C. M. McCrimmon et al., “Automated detection of ripple oscillations
in long-term scalp EEG from patients with infantile spasms,” J. Neural
Eng., vol. 18, no. 1, Feb. 2021, Art. no. 016018.

[3] D. Hu, J. Cao, X. Lai, Y. Wang, S. Wang, and Y. Ding, “Epileptic state
classiﬁcation by fusing hand-crafted and deep learning EEG features,”
IEEE Trans. Circuits Syst. II, Exp. Briefs, vol. 68, no. 4, pp. 1542–1546,
Apr. 2021.

[4] Z. Wang, D. Wu, F. Dong, J. Cao, T. Jiang, and J. Liu, “A novel
spike detection algorithm based on multi-channel of BECT EEG sig-
nals,” IEEE Trans. Circuits Syst. II, Exp. Briefs, vol. 67, no. 12,
pp. 3592–3596, Dec. 2020.

[5] T. Jiang et al., “Improved spike detection algorithm based on multi-
template matching and feature extraction,” IEEE Trans. Circuits Syst.
II, Exp. Briefs, vol. 69, no. 1, pp. 249–253, Jan. 2022.

[6] Y. Feng et al., “3D residual-attention-deep-network-based child-
hood epilepsy syndrome classiﬁcation,” Knowl.-Based Syst., vol. 248,
Jul. 2022, Art. no. 108856.

[7] P. Pavone et al., “West syndrome: A comprehensive review,” Neurol.

Sci., vol. 41, no. 12, pp. 3547–3562, 2020.

[8] Q. Yang et al., “Childhood epilepsy syndromes classiﬁcation based on
fused features of electroencephalogram and electrocardiogram,” Cogn.
Comput. Syst., vol. 4, no. 1, pp. 1–10, 2022.

[9] J. Pavei et al., “Early seizure detection based on cardiac autonomic

regulation dynamics,” Front. Physiol., vol. 8, p. 765, Oct. 2017.
[10] I. Gilboa et al., “Cardiometabolic outcomes in children and adolescents

with west syndrome,” BMC Pediatr., vol. 21, no. 1, pp. 1–11, 2021.

[11] C. Wang and D. J. Hill,

Deterministic Learning Theory: For
Identiﬂcation, Recognition, and Conirol. Boca Raton, FL, USA: CRC
Press, 2018.

[12] C. Wang, X. Dong, S. Ou, W. Wang, J. Hu, and F. Yang, “A new method
ischemia: Cardiodynamicsgram

for early detection of myocardial
(CDG),” Sci. China Inf. Sci., vol. 59, no. 1, pp. 1–11, 2016.

[13] S. Qing-Hua et al., “Early detection of myocardial ischemia based
on deterministic learning and cardiodynamicsgram,” Acta Automatica
Sinica, vol. 46, no. 9, pp. 1908–1926, 2020.

[14] J. C. Robinson, “All possible chaotic dynamics can be approximated in

three dimensions,” Nonlinearity, vol. 11, no. 3, p. 529, 1998.

[15] Z.-D. Liu, Q.-T. Lu, S.-X. Dong, and M.-C. Chen, “Research on veloc-
ity and acceleration geophones and their acquired information,” Appl.
Geophys., vol. 9, no. 2, pp. 149–158, 2012.

[16] C. Wang, T.-R. Chen, and T.-F. Liu, “Deterministic learning and data-
based modeling and control,” Acta Automatica Sinica, vol. 35, no. 6,
pp. 693–706, 2009.

[17] G. Tan, Z. Wang, and Z. Shi, “Proportional-integral state estima-
tor for quaternion-valued neural networks with time-varying delays,”
IEEE Trans. Neural Netw. Learn. Syst., early access, Aug. 23, 2021,
doi: 10.1109/TNNLS.2021.3103979.

[18] G. Tan and Z. Wang, “Reachable set estimation of delayed Markovian
jump neural networks based on an improved reciprocally convex
inequality,” IEEE Trans. Neural Netw. Learn. Syst., vol. 33, no. 6,
pp. 2737–2742, Jun. 2022.

[19] J. Hu, W. Wu, B. Ji, and C. Wang, “Observer design for sampled-data
systems via deterministic learning,” IEEE Trans. Neural Netw. Learn.
Syst., early access, Jan. 14, 2021, doi: 10.1109/TNNLS.2020.3047226.
[20] H. Y. Tomoum, R. H. Aly, O. I. Youssef, H. Abdelal, M. U. Nour, and
A. H. El Sharkasy, “Heart type fatty acid binding protein, a marker
of myocardial ischemia in children with epilepsy,” J. Pediatr. Neurol.,
vol. 11, no. 3, pp. 149–157, 2013.

[21] C. Yuan and C. Wang, “Design and performance analysis of determin-
istic learning of sampled-data nonlinear systems,” Sci. China Inf. Sci.,
vol. 57, no. 3, pp. 1–18, 2014.

[22] X. Cui, J. Cao, T. Wang, and X. Lai, “Robust randomized autoencoder
and correntropy criterion-based one-class classiﬁcation,” IEEE Trans.
Circuits Syst. II, Exp. Briefs, vol. 68, no. 4, pp. 1517–1521, Apr. 2021.
[23] J. Yang, J. Cao, and A. Xue, “Robust maximum mixture correntropy
criterion-based semi-supervised ELM with variable center,” IEEE Trans.
Circuits Syst. II, Exp. Briefs, vol. 67, no. 12, pp. 3572–3576, Dec. 2020.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:21 UTC from IEEE Xplore.  Restrictions apply.
