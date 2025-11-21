# Mikos et al. - 2019 - A Wearable, Patient-Adaptive Freezing of Gait Detection System for Biofeedback Cueing in Parkinson's

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 3, JUNE 2019

503

A Wearable, Patient-Adaptive Freezing of Gait
Detection System for Biofeedback Cueing in
Parkinson’s Disease

Val Mikos

, Student Member, IEEE, Chun-Huat Heng , Senior Member, IEEE, Arthur Tay, Shih-Cheng Yen ,
Nicole Shuang Yu Chia, Karen Mui Ling Koh, Dawn May Leng Tan, and Wing Lok Au

Abstract—Freezing of Gait (FoG) is a common motor-related
impairment among Parkinson’s disease patients, which substan-
tially reduces their quality of life and puts them at risk of falls.
These patients beneﬁt from wearable FoG detection systems that
provide timely biofeedback cues and hence help them regain con-
trol over their gait. Unfortunately, the systems proposed thus far
are bulky and obtrusive when worn. The objective of this paper
is to demonstrate the ﬁrst integration of an FoG detection system
into a single sensor node. To achieve such an integration, features
with low computational load are selected and dedicated hardware
is designed that limits area and memory utilization. Classiﬁcation
is achieved with a neural network that is capable of learning in real
time and thus allows the system to adapt to a patient during run-
time. A small form factor FPGA implements the feature extraction
and classiﬁcation, whereas a custom PCB integrates the system into
a single node. The system ﬁts into a 4.5 × 3.5 × 1.5 cm3 housing
case, weighs 32 g, and achieves 95.6% sensitivity and 90.2% speci-
ﬁcity when adapted to a patient. Biofeedback cues are provided
either through auditory or somatosensory means and the system
can remain operational for longer than 9 h while providing cues.
The proposed system is highly competitive in terms of classiﬁcation
performance and excels with respect to wearability and real-time
patient adaptivity.

Index Terms—FPGA, freezing of gait, machine learning, patient

adaptivity, parkinson’s disease, wearable devices.

I. INTRODUCTION

P ARKINSON’S disease (PD) is a chronic, progressive and

neurodegenerative condition marked by motor related im-
pairments. It is estimated that at least 8.4 million individuals
currently suffer from PD, the majority of them being 50 years
old or more [1]. Since the disease progresses rather slowly, the

Manuscript received December 5, 2018; revised February 18, 2019; accepted
April 26, 2019. Date of publication May 1, 2019; date of current version May
24, 2019. This work was supported in part by NUS-NNI 2016 under Grant
R263000C36133 and in part by NMRC/CISSP/2014/2015. This paper was rec-
ommended by Associate Editor R. Jafari. (Corresponding author: Val Mikos.)
V. Mikos, C.-H. Heng, A. Tay, and S.-C. Yen are with the Department of
Electrical and Computer Engineering, National University of Singapore, Singa-
pore 117583 (e-mail: mikos.val@gmail.com; elehch@nus.edu.sg; arthurtay@
nus.edu.sg; shihcheng@nus.edu.sg).

N. S. Y. Chia, K. M. L. Koh, and W. L. Au are with the Department
of Neurology, National Neuroscience Institute, Singapore 308433 (e-mail:
Nicole_CHIA@nni.com.sg; karenkoh7@gmail.com; au.wing.lok@singhealth.
com.sg).

D. M. L. Tan is with the Department of Physiotherapy, Singapore General

Hospital, Singapore 169608 (e-mail: dawn.tan.m.l@sgh.com.sg).

Color versions of one or more of the ﬁgures in this paper are available online

at http://ieeexplore.ieee.org.

Digital Object Identiﬁer 10.1109/TBCAS.2019.2914253

struggle of managing the motor related impairments lasts sev-
eral years. Eventually, PD patients get overwhelmed and require
more sick leaves, begin to show signs of absenteeism and opt to
retire earlier [2], [3]. Such losses in productivity, coupled with
medical health care expenses, are furthermore the cause of sub-
stantial societal costs [2], [3]. A primary goal of this research
is to help PD patients manage their motor related impairments
effectively such that they remain integrated in their social envi-
ronment for a prolonged period of time.

The motor impairment that arguably poses the biggest chal-
lenge to accomplish that goal is known as freezing of gait (FoG).
As the name suggests, it describes a patient’s inability to initiate,
sustain or generally control their gait. An episode is usually con-
ﬁned to a short period of time followed by the patient regaining
control and resuming their regular gait. Roughly half of all PD
patients are burdened by FoG at least twice a month, while a third
experiences episodes on a daily basis [4]. As a direct result of
FoG, patients experience a deterioration in mobility, bodily com-
fort, activity in daily living and emotional well-being [5]. They
are furthermore at risk of falls due to FoG [6], [7]. Falls among el-
derly people result in 20-30% of cases in injuries [8]. This makes
the occurrence of FoG a serious health concern for PD patients.
It is thus desirable to provide a means for mitigating the effect
of FoG and thereby augmenting a patient’s quality of life [9].

Wearable, biofeedback cueing devices are one such promising
proposal to accomplish exactly that. These systems detect the
occurrence of a FoG episode in real-time and provide biofeed-
back cues to the patient in an attempt to help them overcome
the episode and hence reduce the risk of falls. The supply of
such biofeedback cues to a PD patient has shown to reduce the
overall severity of FoG [21]–[23], as well as shorten the total
duration of FoG by 34% [24]. Unfortunately, a plethora of re-
search focuses on FoG classiﬁcation algorithms built only in
software without providing a wearable hardware implementa-
tion for biofeedback cueing. The recent proposals for machine
learning (ML) FoG classiﬁers are prime examples of FoG detec-
tion systems that are solely designed in software [25], [26]. Map-
ping these algorithms onto hardware is not straightforward since
wearable, battery-powered electronics have substantial power
and area constraints that need to be met. It is thus not surprising
that the few FoG detection systems that do provide a hardware
implementation are rather bulky and obtrusive to the patient
when worn. Nevertheless, there are several recent studies that

1932-4545 © 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply. 

504

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 3, JUNE 2019

TABLE I
OVERVIEW OF VARIOUS PROPOSED FOG DETECTION SYSTEMS IN LITERATURE (AS OF LATE 2018)

have successfully mapped complex, real-time capable classiﬁ-
cation algorithms onto dedicated hardware for wearable health
care applications. For example, FPGA based designs were pro-
posed for cardiovascular disease monitoring [27], [28], seizure
detection [29] and assistive technologies [30]. Learning on wear-
able hardware with support vector machines has also been pro-
posed to provide patient adaptivity in seizure detection [29]. In
light of these recent advances, this paper demonstrates the ﬁrst
ML based FoG detection system integrated into an FPGA based
wearable sensor node. It implements a neural network classi-
ﬁcation algorithm and allows for real-time, online learning on
the sensor node to provide patient adaptivity. The paper details
the design efforts and the compromises that made the employ-
ment of small, wearable hardware possible while remaining as
competitive as possible in terms of classiﬁcation performance.
The paper ﬁrst provides a brief overview of published FoG de-
tection systems in Section II and illustrates the research gap that
ought to be addressed. In Section III, features are selected that
minimize the computational load on the hardware while retain-
ing a high classiﬁcation accuracy. Section IV then demonstrates
the proposed dedicated hardware that allows for learning of the
algorithm on wearable hardware in real-time. The overall FoG
detection system and thus the successful mapping of the func-
tionality onto a single sensor node is demonstrated in Section V
followed by a performance evaluation in Section VI. Finally, the
main ﬁndings are summarized in the conclusive Section VII.

II. REVIEW OF FREEZING OF GAIT DETECTION
SYSTEMS IN LITERATURE

Table I summarizes hardware based FoG detection systems
found in literature, all of which employ inertial measurement
units (IMUs) to classify FoG. It distinguishes three parts that
are of particular interest when discussing FoG detection systems:
hardware, algorithm and performance.

The hardware summary shows that FoG detection systems
predominantly deliver biofeedback (BF) using auditory (A) or
sematosensory (S) cues [10]–[15], [17], [19], [20], with only a
single implementation opting to provide visual (V) cues [18].
The hardware that computes the classiﬁcation result and de-
livers these cues is commonly a smartphone [13]–[15], [19],
[20]. Exceptions are Bächlin et al.’s waist-worn, portable PC
using an Intel XScale family processor [10]–[12], Ahn et al.’s
Epson BT-200 smart glasses providing visual cues [18] and
Lorenzi et al.’s proposed dedicated hardware for FoG detection
[17]. All non-dedicated hardware implementations and smart-
phone reliant FoG detection systems weigh 130 g or more,
while Lorenzi et al.’s dedicated hardware reduces weight by
more than 5× to a miniscule 25 g. Such compact size is
achieved at the expense of limited battery life of 2 hours and
its inability to process any ML algorithm. In addition, a wire-
less communication between multiple nodes needs to be main-
tained which could incur reliability issues. Although there are
systems that integrate the overall design into a single node,
they rely on bulky, usually waist-worn smart devices to do so

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply. 

MIKOS et al.: WEARABLE, PATIENT-ADAPTIVE FOG DETECTION SYSTEM FOR BIOFEEDBACK CUEING IN PARKINSON’S DISEASE

505

[14], [15], [18]. This calls for an energy efﬁcient hardware
innovation with integrated FoG detection on a single sensor
node.

Regarding the algorithmic aspect, most systems rely on the
computationally inexpensive threshold based approach to FoG
classiﬁcation. The only ML based FoG classiﬁers are Mazilu
et al.’s random forest [13] and Kim et al.’s boosted ensem-
ble classiﬁer [15], which require the computational power of a
smartphone. The recent algorithmic advances in ML based FoG
classiﬁcation employing neural networks [25] or support vector
machines [26] have yet to be implemented in wearable hardware.
The reported systems also differ in their interval choice between
two successive classiﬁcations, with some classifying every IMU
data sample [10]–[13], [17] and others adopting larger time in-
tervals [14], [15], [19], [20]. Nevertheless, too large intervals
between successive classiﬁcations should be avoided to ensure
a timely FoG classiﬁcation.

Finally, FoG detection systems are only viable if the classiﬁ-
cation performance is satisfactory. That performance has been
evaluated by determining the sensitivity and speciﬁcity when
classifying datasets consisting of roughly a dozen patients in
most cases [10]–[15], [17]–[19] and 32 patients at most [20]. All
threshold based approaches were built and evaluated using the
complete dataset, and the attained performance metrics are thus
best regarded as training performance only. The average of the
attained sensitivity and speciﬁcity ranges from 73.6% to 95.6%.
On the other hand, ML implementations build their model based
on a training dataset and evaluate the performance on a disjunct
test dataset. The achieved average of sensitivity and speciﬁcity
of 78.6% and 88.8% are thus more objective as they are obtained
from an unseen test dataset. Patient-speciﬁc classiﬁers are also
another interesting aspect to explore. Compared to classiﬁers
that generalize on all patients, patient-speciﬁc classiﬁers have
shown signiﬁcant improvements in sensitivity and speciﬁcity
[10]–[13]. This suggests that the design of patient-speciﬁc or
patient-adaptive FoG detection systems could be a worthwhile
endeavor.

This paper addresses the limitations mentioned above. It
demonstrates a ML based classiﬁcation algorithm, provides real-
time patient adaptivity and integrates the functionality with dedi-
cated hardware into a single sensor node. The following sections
illustrate the design methods and compromises adopted that en-
able such an integration while remaining competitive in terms
of classiﬁcation accuracy.

III. HARDWARE CONSTRAINED FEATURE
AND ALGORITHM SELECTION

The real-time extraction of features in hardware can be costly.
While software based implementations can virtually add as
many features as desired to a classiﬁcation algorithm, hardware
implementations will face repercussions in terms of power con-
sumption and area requirements. This section illustrates the se-
lection of features and classiﬁcation algorithm that reduces the
number of employed features and thus the computational load
on the hardware.

A. Candidate Features and Dataset

When limiting the number of employed features, it becomes
crucial to select those that are highly potent in detecting FoG. In
order to not overlook potentially potent features during the se-
lection process, a list of candidate features is compiled ﬁrst from
a wide range of proposals found in literature. We have conducted
a thorough survey of FoG related features in [31] and employ
them here as the set of candidate features. They consist of 117
features extracted from various IMU signal axes (accelerations
ax, ay, az, |a|, and angular velocities ωx, ωy, ωz, |ω|). They can
be divided into the following three categories. First are features
based on frequency domain computations, such as freeze index
(FI), freeze band (FB), locomotor band (LB), mean frequency
( ¯f ), dominant frequency (DF), power (P) and spectral entropy
(S). The second category includes features derived from arith-
.2),
metic operations on IMU data, namely root mean square (
mean (¯.), standard deviation (σ), coefﬁcient of variation (CV),
kurtosis (K), maximum acceleration ((cid:3).(cid:4)), range of acceleration
(R) and stride peak (SP). And lastly are features that rely on
spatio-temporal domain algorithms, such as stride time (ST),
velocity (V), stride length (SL) and the FoG criterion (FoGC).
The selection of features from this set of candidate features
is based on a dataset consisting of 25 PD patients who wore an
IMU on their ankles (fs = 50 Hz) during 7-meter timed up-
and-go exercises. The dataset amounts to a total of 1 hour and
33 minutes of gait data with 221 FoG episodes. The average
duration of a FoG episode was 10.2 s. We employed the same
dataset in [31] to select optimal feature sets for various machine
learning algorithms. Here, we propose a new feature selection
approach speciﬁcally for hardware implementations by limiting
the number of features and thus the computational load on the
hardware.

√

B. Minimal Feature Set Selection

Although software implementations of ML based FoG clas-
siﬁers employ as many as sixty-four unique features [25], hard-
ware implementations relied on seven [13] and twelve [15] only.
Furthermore, both of these hardware implementations relied on
the processing power of a bulky smartphone (see Table I) and it
is questionable whether a smaller, battery-powered sensor node
can accommodate as many. Thus, it is desirable to select as small
a set from the candidate features as possible without conceding
any signiﬁcant loss in terms of classiﬁcation potency. This is ac-
complished by the feature selection process illustrated in Fig. 1.
First, a conventional wrapper method selects optimal feature
sets for various ML algorithms from the set of candidate fea-
tures. This results in an optimal feature set of Nopt features for
each ML algorithm. Then, a greedy stepwise search algorithm
attempts to form a smaller feature set with similar classiﬁca-
tion performance as observed with the optimal feature set just
derived. Initially, its set of selected features is empty. It then
executes a step by adding one feature from the set of candidate
features to its set of selected features. The decision about which
feature it selects falls onto the feature that maximizes the classiﬁ-
cation accuracy when added to the set of selected features. If the

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply. 

506

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 3, JUNE 2019

Fig. 1.
Feature selection approach to ﬁnd feature sets with as small a number
of features as possible while retaining a high classiﬁcation performance in terms
of f1-score.

feature set concludes with the same number of features as the
optimal one, it is most likely inferior in classiﬁcation perfor-
mance. This is because the greedy algorithm is only considering
the effect of adding one more feature to a set of already selected
features, while the wrapper approach is more ﬂexible in that
it evaluates various combinations of any number of features to
build a feature set. Nevertheless, the minimal feature sets even-
tually fall within 1% of the optimal f1-score performance, the
exception being the k-nearest neighbor classiﬁer which required
Nmin = 6 > Nopt to do so.

Since the core motivation is to minimize the computational
load on the hardware, the feature set with the smallest extraction
cost ought to be selected rather than the set with the lowest num-
ber of features. To that end, the estimated extraction cost of the
selected feature sets is provided in Table II (see Appendix A for
derivation). It illustrates the number of additions (subtractions),
multiplications, divisions (Div) and non-linear (NL) functions
needed to extract the derived feature set. Based on these ﬁnd-
ings, a neural network approach is chosen for our implementa-
tion. Besides the low computational load, neural networks can
also conduct online learning which is critical to enable patient
adaptivity in real-time. Moreover, its potency has been clearly
demonstrated in software [25] and porting it into a miniaturized,
energy efﬁcient sensor node would prove its feasibility for FoG
detection systems. To facilitate online learning and counteract
the vanishing gradient problem, one hidden layer with ﬁve units
is implemented here. The features that are thus extracted for the
proposed FoG detection system are as follows. The freeze index
(FI), proposed in [32], is given by

(cid:2) 8
3 |A(f )|2 df
(cid:2) 3
0.5 |A(f )|2 df

,

(1)

Fig. 2. The gradual improvement of adding more features using a greedy
stepwise search. For illustrative purposes, feature count Nmin is increased even
after f1-score performance has been reached.

FI|a| =

classiﬁcation accuracy with that newly added feature is within
1% of the classiﬁcation performance observed with the optimal
feature set in terms of f1-score, then the algorithm concludes.
Otherwise, it continues to execute further steps by adding more
features until the classiﬁcation performance is comparable to
the one observed with the optimal feature set, or until Nopt fea-
tures have been added. Once the greedy algorithm concludes, an
alternative feature set consisting of Nmin features is obtained,
where Nmin ≤ Nopt ≤ 117.

C. Selected Features and Classiﬁcation Algorithm

The proposed minimal feature set selection was implemented
using Weka 3.8. The results are illustrated in Fig. 2. The ﬁtting
curve to the f1-scores indicates that, on average, three features
sufﬁce to achieve a classiﬁcation performance similar to the one
observed when using the optimal feature set. The number of se-
lected features in the optimal and minimal sets is summarized in
Table II for various ML algorithms. Optimal feature sets range
in size from two features for naive Bayes up to seventeen for
boosted decision trees. Overall, the proposed minimal feature
selection procedure succeeded in all but two cases to reduce that
number of features. It needs to be noted that even if the minimal

where A(f ) is the 128-point discrete Fourier transform (DFT) of
the IMU’s most recent acceleration’s absolute values |a|. During
FoG, high frequency related tremors arise due to the loss of
control over one’s lower limbs. The increase of high frequency
components within the spectrum is captured by the numerator,
which enlarges the freeze index. On the other hand, regular gait
has a distinct frequency peak around 1 Hz. Such frequencies are
captured by the denominator, which diminishes the FI. Hence,
the FI is expected to increase during FoG episodes, but remain
small during regular gait. The second feature, stride peak (SP),
was proposed in [31] as

⎧
⎨

(cid:6)

ω(i−2)
z

ω(i−1)
if
z
SP(i−1) otherwise.

SP(i) =

⎩

< ω(i−1)
z

> ω(i)
z

(cid:7)

,

(2)

z

Here, ω(i)
is the ith sample of the IMU’s angular velocity in
the patient’s frontal plane. Wide swings are inherent to regular
gait patterns, but during FoG episodes these swings considerably
subside. Smaller SP values thus capture the abatement of swings
and indicate a potential FoG episode. For the third and ﬁnal
feature, rather than extracting the standard deviation, σωz , the
computational complexity is furthermore reduced by extracting
the variance instead. This eliminates one non-linear function
which is especially cumbersome to implement in hardware. It is

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply. 

MIKOS et al.: WEARABLE, PATIENT-ADAPTIVE FOG DETECTION SYSTEM FOR BIOFEEDBACK CUEING IN PARKINSON’S DISEASE

507

TABLE II
RESULTING FEATURE SETS AND FEATURE COUNT REDUCTION USING THE PROPOSED FEATURE SELECTION PROCEDURE. THE EXTRACTION
COST OF THE FEATURE SETS ARE INDICATED

a small form factor FPGA for later integration into a wearable
sensor node.

A. Data Acquisition and Feature Extraction

The proposed design ﬁrst acquires a patient’s gait data from
an off-chip IMU using the I2 C protocol. A UART interface is
furthermore supported in order to allow for the receiving and
sending of data via BLE. Once a data sample from the IMU has
been acquired, the three aforementioned features (FI, SP, Var)
are extracted. We have demonstrated the extraction of these three
features in detail in our previous work [33]. The computations
of (2) and (3) are relatively straightforward and do not require
substantial hardware resources. However, the extraction of the
FI with (1) is computationally expensive due to the required
DFT. Area utilization has been signiﬁcantly reduced by relying
on a spectrum analyzer proposed in [34] to compute the DFT.
The spectrum analyzer was implemented with as little as three
adders and two multipliers that are time-shared among the nec-
essary computations. Once the features are extracted, they are
normalized and routed as a feature vector (FV) to the neural net-
work core shown in Fig. 4. The neural network core consists of
four computational blocks using three RAM memories to clas-
sify the feature vector for biofeedback generation and provide
patient adaptivity through real-time online learning.

B. Real-time Classiﬁcation For Biofeedback Cueing

The feed forward processing unit (FFPU) is the only pro-
cessing block required for classiﬁcation. All other blocks within
the core are accommodating the online learning functionality.
Forward propagating a sample in a neural network requires the
computation of the induced ﬁeld z(l)
j and the corresponding ac-
tivation a(l)

for every jth unit of every lth layer, as in

j

u(l−1)(cid:8)

z(l)
j =

θ(l−1)
j,i

· a(l−1)
i

,

i=0
(cid:6)

a(l)
j = σ

z(l)
j

(cid:7)

,

∀j ∈ [1, u(l)]

∀j ∈ [1, u(l)]

(4)

(5)

Fig. 3. Overview of the proposed VLSI design of a neural network and feature
extraction that is mapped onto an FPGA.

also computed from the IMU’s angular velocity readings ωz, as
in

Varωz

=

1
N

i(cid:8)

(cid:6)

ω(j)
z − ωz

(cid:7)2

(cid:9)
(cid:9)
(cid:9) N = 64

(3)

j=i−N +1

The window length N has been deliberately set to a power of 2,
as this reduces the division in (3) to a simple bit shift operation
in hardware. During regular gait, wide swings engender large
variations in observed angular velocity values, while a more
rigid, constrained gait is conﬁned to smaller variations. This is
again exploited to detect FoG. With the selected features and ML
algorithm, the paper next demonstrates the design of hardware
for a neural network that is capable of learning in real-time on
a sensor node.

IV. HARDWARE DESIGN OF A PATIENT ADAPTIVE NEURAL
NETWORK CLASSIFIER

One of the main goals of this paper is to transfer learning
from a desktop PC or cloud computer onto a wearable, battery-
powered sensor node using dedicated hardware. It is necessary to
limit area and power consumption when mapping the learning
algorithm onto such wearable hardware. The proposed VLSI
design of a neural network capable of operating under these
limitations is illustrated in Fig. 3. The goal is to ﬁt the design onto

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply. 

508

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 3, JUNE 2019

Fig. 4. Neural network accelerator with online learning capability. Left: Block diagram of the core processor consisting of three RAM blocks (Theta RAM,
Cache, OLBFIFO) and four main computation blocks (FFPU, BPPU, OLBC, Theta Updater). Right: A computational ﬂow diagram illustrating the neural network
along with the role of the various RAM and computational blocks.

section of the OLBFIFO RAM along with the corresponding
feature vector for online learning purposes.

C. Online Learning Batch Creator (OLBC)

Once a feature vector has been classiﬁed by the FFPU, the
neural network core begins with learning. First and foremost,
the learning algorithm requires data to be trained with. The task
of assembling such training data is handled by the online learn-
ing batch creator (OLBC). The OLBC reads the feature vectors
stored in the most recent samples section of the OLBFIFO RAM
to create and manage the online learning batch (OLB). That on-
line learning batch is then used to train the neural network. Un-
fortunately, the batch cannot store the complete training dataset
as software implementations do. The available on-chip memory
on wearable hardware is far from sufﬁcient to do so. Learn-
ing on wearable hardware thus requires to be done with smaller
learning batches and feature vectors need to be discarded in a
ﬁrst-in ﬁrst-out (FIFO) fashion to make space for new training
data. Smaller learning batches result in a more stochastic learn-
ing progress instead of a smooth one, but should not prevent the
ML algorithm from adopting a potent, ﬁnal model. Therefore,
the online learning batch is assembled with 32 feature vectors
only, with one half reserved for feature vectors representing FoG
and one half for feature vectors representing regular gait. The
OLBFIFO RAM with its two sections, the online learning batch
and the most recent samples, is illustrated in Fig. 6. It shows the
online learning batch’s 32 feature vectors and the schematic of
the OLBC that decides which feature vectors from the most re-
cent samples section are added to the online learning batch and
which are not. The inclusion of feature vectors into the online
learning batch depends on whether supervised or unsupervised
learning is selected.

1) Supervised Learning: For supervised learning, the correct
label (FoG or no FoG) of the feature vector is known and supplied
along with the feature vector. This is possible if the patient is part
of the dataset that the neural network is being trained with or if

Fig. 5. The FFPU relies on two time-shared DSP blocks and an LUT storing
the sigmoid activation function.

j,i

where u(l) denotes the number of units in layer l, σ(.) the sig-
moid function and θ(l−1)
the neural network parameter from unit
i in layer l − 1 to unit j in layer l. Note that every zeroth unit is
a bias unit, as in a(l)
0 = 1 for all layers l. The VLSI implemen-
tation of the FFPU is shown in Fig. 5. It time-shares one adder
and multiplier to reduce area utilization and implements the sig-
moid function, σ(.), with a lookup table (LUT). The LUT stores
256 entries with 22-bit ﬁxed point precision (sQ1.20), which
was sufﬁcient to ensure accurate classiﬁcation. Since the neural
network parameters θ(l)
j and activations a(l)
j,i , induced ﬁelds z(l)
need to be shared among multiple processing blocks, the RAM
blocks are implemented with dual ports to allow for simultane-
ous access. The FFPU computes the ﬁelds z(l)
and activations
a(l)
j unit by unit and writes the results into the cache. An arbiter
ensures that the results are written into a section of the cache that
other processing blocks are currently not reading from. Once
the FFPU computes the activation for the output unit in the ﬁ-
nal layer L, a(L)
, it is rounded to obtain the classiﬁcation result
and outputted as the signal FoG to control biofeedback cueing.
That activation value is referred to as the FFPU prediction score,
hθ ∈ (0, 1), and is written into the most recent samples (MRS)

j

j

j

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply. 

MIKOS et al.: WEARABLE, PATIENT-ADAPTIVE FOG DETECTION SYSTEM FOR BIOFEEDBACK CUEING IN PARKINSON’S DISEASE

509

OLBC proceeds to write the feature vector into the online learn-
ing batch’s real-time section of “FoG” or “no FoG” according
to the determined label. Note that for unsupervised learning, the
online learning batch reserves half of all feature vectors for of-
ﬂine database feature vectors that have a known label. These
feature vectors can only be overwritten during supervised learn-
ing. Hence, 50% of the online learning batch does not change
during unsupervised online learning and at least 50% of the on-
line learning batch has deﬁnitely a correct label assigned to it.

D. Online Batch Learning With Backpropagation

With training data assembled in the online learning batch,
the neural network can begin with learning. Learning in neural
networks is the search for suitable parameters θ that lead to a
high classiﬁcation accuracy on the online learning batch training
data. Here, a stochastic gradient descent algorithm searches for
suitable parameters by iteration of

θn+1 = θn − α

∂
∂θn

J(θ)

(8)

where α is the learning rate, n the iteration index and J(θ)
the cost function of classifying training samples incorrectly. For
the proposed implementation, the cross-entropy cost function
is adopted and one gradient descent iteration is conducted per
assembled online learning batch. Hence, learning requires the
computation of the partial derivative of the cost function. The
backpropagation processing unit (BPPU) is designated to com-
pute these partial derivatives for all units in the network. For
every feature vector in the online learning batch, it quantiﬁes
the error δ(L)
at the output layer L as the difference between the
FFPU’s prediction score , hθ = a(L)
, and the correct label yj. It
then backpropagates that error to compute the relative error of
every unit according to

j

j

⎧
⎨

⎩

δ(l)
j =

a(l)
j − yj
σ(cid:8)(z(l)

j ) ·

l = L

(cid:11)u(l+1)
i=1

i,j · δ(l+1)
θ(l)

i

∀l ∈ [2, L − 1]

(9)

j and z(l)

Backpropagation of the errors using (9) requires the intermedi-
ate results a(l)
j of the forward propagated feature vector.
Therefore, a feature vector from the online learning batch is ﬁrst
forward propagated by the FFPU to obtain these intermediate
results and store them in the shared cache. The FFPU then for-
ward propagates the next feature vector from the online learning
batch, while the BPPU begins to backpropagate the ﬁrst feature
vector using the results stored in the cache. The FFPU and BPPU
thus always work in parallel on two subsequent samples when
learning. Once the BPPU computes the errors δ(l) for all required
units in the neural network, the gradient is computed through
i,j + δ(l+1)

i,j = Δ(l)

j , ∀i, j, l

· a(l)

Δ(l)

(10)

i

These gradients represent an estimate of the cross-entropy cost
function’s partial derivatives required for the gradient descent
algorithm. The partial derivatives can therefore be obtained by

∂
∂θ(l)
i,j

J(θi,j) :=

1
m

Δ(l)
i,j

(cid:9)
(cid:9)
(cid:9) m = 32

(11)

Fig. 6. The online learning batch creator reads the feature vectors from the
OLBFIFO’s most recent samples (MRS) section and decides if they are added
into the online learning batch (OLB).

the labels are provided in real-time, e.g. through a BLE enabled
push button while the patient is walking. Fig. 6 shows that if
supervised learning is selected, the OLBC routes the provided
label through to the online learning batch multiplexer and sets
the write enable (WE) to 1. Thus, when labels are provided the
OLBC indiscriminately adds feature vector after feature vector
into the online learning batch. According to the provided label,
the feature vector is written into any section of the online learning
batch labeled “no FoG” or “FoG”.

2) Unsupervised Learning: If no label is provided, the neural
network core allows for a self-training mechanism based on our
proposed software algorithm in [35]. It demonstrates two criteria
that the OLBC can employ to self-label the feature vectors with
a high degree of conﬁdence. Criteria 1 computes the mean FFPU
prediction score, hθ ∈ (0, 1), of the most recent feature vectors.
If that mean is highly positive, or highly negative, the OLBC
self-labels the feature vectors according to
⎧
⎪⎪⎨

hθ (F V ) > 0.85

1,

ˆy =

⎪⎪⎩

0,

hθ (F V ) < 0.25

(6)

discard, otherwise.

A total of 16 FV-hθ pairs are available in the most recent sam-
ples section of the OLBFIFO RAM. Thus, the OLBC computes
the mean by accumulating the individual prediction scores in
register A and bit shifting the result. Criteria 2 triggers the write
enable for those feature vector that are not too far off from a
known reference F Vref . For example, if a feature vector is self-
labeled as FoG using criteria 1, then the feature vector needs to
satisfy
(FI − FIref )2 + (SP − SPref )2 + (Var − Varref )2 < lim (7)

in order to be included into the online learning batch. The OLBC
stores the squared terms of (7) in register S before accumulat-
ing them in register A. The motivation behind the two criteria
are thoroughly described in [35]. If both criteria are met, the

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply. 

510

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 3, JUNE 2019

Fig. 7. A time-shared implementation of the BPPU to compute the gradients
necessary for one subsequent gradient descent iteration.

The BPPU concludes by writing these derivatives into Theta
RAM. The Theta Updater then reads these values and executes
one iteration of the stochastic gradient descent in (8) to conclude
learning for the currently assembled online learning batch.

The proposed design of the BPPU computing (9) and (10) is
shown in Fig. 7. As for the FFPU, the BPPU time-shares one
adder and multiplier to reduce area utilization at the expense
of increased computation time. The execution of one gradient
descent iteration, however, has to conclude before a new fea-
ture vector is supplied to the core which creates a new online
learning batch. The time intensive computation of the non-linear
derivative of the sigmoid function, σ(cid:8)(.), is thus implemented
with a LUT to reduce its computation time to a single clock
cycle. The LUT stores 256 entries with 22-bit ﬁxed point preci-
sion (sQ1.20), which was sufﬁcient to ensure accurate learning.
The register D stores the error δ(l+1)
, while a register T stores
i
the temporary results δ(l+1)
· σ(cid:8)(z(l)
j ) when computing (9), or
δ(l+1)
j when computing (10). Note that the summation term
i
in (9) simpliﬁes to a single term if u(l+1) = 1. This is the case
in the neural network discussed here when computing the errors
for the hidden layer, since u(L) = 1.

· a(l)

i

V. WEARABLE FREEZING OF GAIT DETECTION SYSTEM

This section illustrates the proposed FoG detection system
and shows that it has been successfully integrated into a single
sensor node with real-time learning capability as a result of the
efforts discussed in the previous sections.

A. Overview of the Freezing of Gait Detection System

The FoG detection system in its entirety is shown in Fig. 9.
It integrates all fundamental elements of FoG detection systems
into a single, ankle-worn sensor node, namely data acquisition,
feature extraction, FoG classiﬁcation and biofeedback genera-
tion. Data is acquired through an IMU (LSM9DS1, STMicro-
electronics), while an FPGA implements the feature extraction
and neural network architecture for classiﬁcation and real-time

Fig. 8. Area and memory utilization of the proposed design and its ability to
ﬁt onto small form factor FPGAs such as the Artix-7 35T (10 × 10 mm2).

learning (Artix-7 35T, Xilinx). A 32 Mb ﬂash memory stores
the FPGA conﬁguration bitstream and ensures that the FPGA
is properly conﬁgured upon power up. Biofeedback cues can be
delivered in two different ways. Sematosensory cues are gener-
ated by a vibration motor that is attached to the inside of the strap
and connects to the sensor node with wires. Auditory cues on the
other hand are delivered through BLE capable earphones. Four
DIP switches deﬁne the system operation modes, which deter-
mine the cueing type and enable online learning. The system is
enclosed in a 4.5 × 3.5 × 1.5 cm3 housing case and weighs only
32 g, which is an order of magnitude improvement compared
to other reported systems without dedicated hardware. Power is
supplied to the system using a chargeable Li-ion battery with
800 mAh capacity.

B. Meeting the FPGA Resource Limitations

In our attempt to design a neural network based FoG detection
system, a substantial focus has been put on limiting the design’s
overall resource requirements. There are three main design ef-
forts that have contributed to that goal. First, the computational
load on the FPGA has been limited by reducing the number
of features that are extracted. Second, a substantial part of the
neural network classiﬁcation and learning computations employ
time-shared circuitry. And third, the learning algorithm operates
sequentially with batches consisting of 32 feature vectors that
are discarded as new feature vectors arrive, circumventing the
storage of a large dataset.

The proposed design’s area and memory utilization are illus-
trated in Fig. 8. It indicates that the largest area consumption
comes from the extraction of features (54% of total), mostly
due to the required DFT of the FI in (1). Had the number of
features not been reduced, it would have certainly been more
challenging to ﬁt the overall design onto the available resources
of the Artix-7 FPGA. The neural network on the other hand re-
quires comparatively little area as the majority of the functional-
ity is computed with time-shared resources. The ﬁgure indicates
what repercussions would result if no time-sharing had been em-
ployed. If the standard, vectorized approach to neural network
computation were implemented, the required area would exceed
the limitations of the Artix-7. A Kintex-7 480T FPGA would be
required for the standard approach, which has a form factor of
31 × 31 cm2 and is thus substantially larger than the Artix-7

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply. 

MIKOS et al.: WEARABLE, PATIENT-ADAPTIVE FOG DETECTION SYSTEM FOR BIOFEEDBACK CUEING IN PARKINSON’S DISEASE

511

Fig. 9. Overview of the proposed FoG detection system. A single, ankle-worn system on module integrates all fundamental elements of FoG detection systems
and biofeedback cueing into a single sensor node.

power is supplied by the USB cable rather than the battery. As a
direct result of that, learning can be conducted at a high data rate
without having to worry about battery lifetime. The maximum
data rate is limited by the time it takes the FPGA to compute
one learning cycle and accept new incoming data samples. The
proposed design requires 19.4μs to do so, hence a data rate
51.4 kHz can be achieved.

2) IMU Mode: In this mode, the IMU data collected when the
system is worn by a patient is directly used for online learning.
The sampling frequency of IMU is set to 50 Hz to limit the
dynamic power consumption. Learning in both modes can be
supervised and unsupervised. For supervised learning in IMU
mode, the labels have to be transmitted in real-time, possibly
through a BLE enabled push button.

VI. SYSTEM PERFORMANCE EVALUATION

This section evaluates and discusses the proposed FoG sys-
tem’s viability in terms of learning performance, classiﬁcation
accuracy, power consumption and comfort for wearability.

A. FoG Dataset and Methodology

We base our evaluation on a dataset consisting of 63 patients
that wore IMUs on their ankles (fs = 50 Hz) while performing
7-meter timed up-and-go exercises and random walks. A subset
of 25 patients from this dataset has been previously used to select
features in Section III. The patient data has been labeled by two
independent raters qualiﬁed to identify FoG by analyzing video
recordings of the exercises. A third rater acted as an arbiter in
case of disagreements between the ﬁrst two raters. The dataset
amounts to 3 hours and 50 minutes of gait data with 485 observed
FoG episodes. The average duration of a FoG episode was 10.2 s.
This makes the acquired FoG dataset the largest to date (see
Table I). The study was approved by the Singhealth Centralized
Institutional Review Board (CIRB 2011/255/A).

The dataset is split into a training and test set to obtain a
reliable representation of the system’s performance on unseen
patients. The 25 patients used previously to select features form

Fig. 10. Learning modes on the FoG detection system sensor node.

with 10 × 10 cm2. Giving up computational speed by time-
sharing circuitry has thus enabled the employment of FPGAs
with smaller form factors, reducing the required FPGA LUT
slices to 3.07%. Similarly, if the standard approach to learn-
ing were implemented, no FPGA would have sufﬁcient on-chip
memory to store the whole dataset. The proposed design of rely-
ing on a small online learning batch which discards training data
with a FIFO replacement method for new data signiﬁcantly re-
duces memory utilization. Compared to the standard, vectorized
implementation in software, memory utilization for the time-
shared design is reduced to 1.92%. Hence, online learning on
small form factor FPGAs is made possible.

C. Learning on the Sensor Node

The sensor node allows for two different learning modes, as
illustrated in Fig. 10. The ﬁrst mode, USB mode, enables fast
learning, while the second mode, IMU mode, enables power
efﬁcient, real-time learning for patient adaptivity.

1) USB Mode: This mode requires the sensor node to connect
via USB cable to a desktop PC that stores a FoG dataset. A
python script then transmits that data to the FPGA using the USB
to UART bridge (FT2232). The FPGA accepts the incoming
data and manages its online learning batch to conduct learning.
Since a wired connection to a desktop PC is required, learning in
this mode cannot be conducted during a patient’s system usage.
However, power consumption thus becomes inconsequential, as

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply. 

512

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 3, JUNE 2019

TABLE III
TRAINING ACCURACY AND TIME OF THE NEURAL NETWORK WHEN
EXECUTED ON A CONVENTIONAL DESKTOP PC (INTEL I5-4690 @3.5 GHZ)
AND THE PROPOSED SENSOR NODE

TABLE IV
CLASSIFICATION PERFORMANCE ON THE SENSOR NODE

the training set, while the remaining 38 are grouped into a test
set. Learning performance is evaluated by the time it takes for the
neural network to learn a “database model” using the training set.
Classiﬁcation performance on the other hand observes the ability
of that database model to classify patients from the test set. To al-
low for comparisons within the FoG literature, the classiﬁcation
performance is assessed by sensitivity and speciﬁcity. Finally,
patient adaptivity is evaluated by feeding the database model a
stream of data from a particular test patient and let the neural
network conduct learning as it receives that data. The classiﬁca-
tion performance when using patient adaptivity is then assessed
by evaluating the resulting adapted model on unseen data of the
same patient. This is done for all patients in the test set and the
average is taken to summarize the efﬁcacy of patient adaptivity.

B. Learning Performance

Table III summarizes the resulting training accuracy and train-
ing time when learning a database model using either the pro-
posed sensor node or a desktop PC. The ﬁrst thing to note is that
learning on the sensor node leads to virtually the same database
model with only a slight difference in training accuracy. The
sensor node can learn such a model about 22.7 times faster than
a desktop PC when using the USB learning mode. This is despite
the fact that the proposed design time-shares most hardware re-
sources and is only running at a frequency of 12 MHz, whereas
the desktop PC is clocked at 3.5 GHz.

On the other hand, learning in IMU mode will take 45.5 times
longer than a desktop PC. This is due to the data rate of the
IMU which has been set low in order to limit dynamic power
consumption. Hence, the sensor node is meant to learn a patient-
independent database model in USB mode ﬁrst and only learn
in IMU mode for adapting that model to a patient in real-time.
Such patient-speciﬁc adaptations are usually gradual enough to
not require many learning samples, which justiﬁes the use of
lower data rates in IMU mode.

Fig. 11.
the sensor node.

Patient adaptivity provided through real-time learning capability on

increases up to 92.9%. Such classiﬁcation performance is com-
parable to those of recently reported ML based FoG classiﬁers
that are purely based on software implementations (90.7% [25]
and 96.1%[26]). These comparisons clearly demonstrate the ef-
fectiveness of the proposed patient-adaptive sensor node.

The sensor node’s learning ability is illustrated in Fig. 11. It
shows how the database model is improved by adapting it to the
patient currently wearing the system. As was to be expected, a
supervised learning approach yields superior classiﬁcation per-
formance compared to the unsupervised counterpart. In fact, the
unsupervised method barely shows any noticeable improvement
on average when compared to the database model. Nevertheless,
unsupervised learning has the potential to signiﬁcantly improve
the classiﬁcation performance of patients which are not classi-
ﬁed well with the database model and which have no means of
labeling their gait. For example, patient 40 attained only 64.1%
sensitivity and 97.6% speciﬁcity using the database model. With
the use of unsupervised learning, the sensitivity improved to
85.3% with only a slight deterioration of speciﬁcity to 94.7%.

C. Classiﬁcation Performance

Table IV demonstrates the attained classiﬁcation performance
on the test set of 38 patients. The patient-independent database
model achieves 87.0% in average of sensitivity and speci-
ﬁcity. Other ML based FoG detection systems required powerful
smartphones to reach comparable performance values (78.6%
[13], 88.8% [15], Table I). Once the sensor node’s ability to
adapt to patients is accounted for, the classiﬁcation performance

D. Wearability and Power Consumption

The proposed FoG detection system is the ﬁrst to provide
dedicated hardware integrated into a single sensor node. With an
overall weight of 32 g, this is to date perhaps the least obstructive
system yet. The 25 g reported in [17] is achieved using a battery
with a 90 mAh capacity that allows for only 2 hours of operation.
If a battery with similar capacity as ours was used, the weight

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply. 

MIKOS et al.: WEARABLE, PATIENT-ADAPTIVE FOG DETECTION SYSTEM FOR BIOFEEDBACK CUEING IN PARKINSON’S DISEASE

513

TABLE V
POWER CONSUMPTION OF THE SENSOR NODE

A. Frequency Domain Features

Features in Table II in this category are freeze index (FI), loco-
motor band (LB), mean frequency ( ¯f ) and dominant frequency
(DF). They all rely on the computation of a discrete Fourier
transform for the time-series data xn

Xk =

N −1(cid:8)

n=0

xn · e− 2πi

N kn,

(12)

would increase to 36 g. The power consumption for the differ-
ent operating modes of the sensor node are shown in Table V.
It shows that the node can operate continuously for 10 hours
and 9.3 hours if auditory biofeedback is provided. The excita-
tion of the vibration motor is more power intensive than sending
BLE data, which explains the slightly lower lifetime of 8.3 hours
when opting for sematosensory biofeedback. Any of these op-
erating modes has a lifetime that exceeds previously published
FoG detection systems, a possible exception being the smart-
phone based systems (see Table I). In any case, these ﬁgures
impressively demonstrate the viability of the proposed design.

VII. CONCLUSION

This paper demonstrated the various design steps conducted
to integrate a FoG detection system into a single sensor node. In
order to achieve such an integration, certain design efforts and
compromises were adopted. First, the computational load on
the hardware was reduced by relying on features that incur min-
imum computational cost. It was shown that, on average, three
features are most likely sufﬁcient to build a ML based FoG clas-
siﬁer with comparable classiﬁcation accuracy as one built with
a larger, optimal feature set. Second, dedicated hardware for a
neural network was designed such that it time-shared resources
to reduce area utilization. The advantage of time-sharing was
demonstrated by the ability to map the proposed design onto
FPGAs with smaller form factors. Third, online learning with
small batches of 32 samples was proposed to enable learning
on the sensor node, where samples are discarded with a FIFO
replacement method as new samples arrive. This signiﬁcantly re-
duces memory requirement and allows the design to ﬁt onto the
chosen FPGA. With these design efforts, the proposed FoG de-
tection system was successfully integrated into a sensor node that
allows for patient adaptivity in real-time. The classiﬁcation ac-
curacy is comparable to recent software implemented ML based
FoG classiﬁers, and exceeds other FoG detection systems when
evaluated on an unseen test set. Speciﬁcally, the system achieves
92.9% in average of sensitivity and speciﬁcity when exploiting
its patient adaptive learning capability. Due to its small form
factor, the design is one of the least obstructive FoG detection
systems when worn and operates for more than 9 hours while
providing auditory biofeedback cues.

which requires 2N k real additions, 2N k real multiplications
and has 1 non-linear function.

1) Freeze Index: N = 220 for |a|, ωz, ax. The two bands
thus use bins k = [3, 35], or 33 bins. k − 1 = 32 to add the bins
together. Total cost is 2N k + (k − 1) additions, 2N k multipli-
cations, 1 division, 1 non-linear function.

2) Locomotor Band: N = 100 for ωz, ax. Band thus uses
bins k = [1, 5], or 5 bins. k − 1 = 4 to add the bins together.
Total cost is 2N k + (k − 1) additions, 2N k multiplications, 1
non-linear function.

3) Mean Frequency: N = 120 for ωz. Band thus uses bins
k = [1, 19], or 19 bins. k − 1 = 18 to add the bins together, 1
division for mean. Total cost is 2N k + (k − 1) additions, 2N k
multiplications, 1 division, 1 non-linear function.

4) Dominant Frequency: N = 60 for ay. Band thus uses bins
k = [1, 9], or 9 bins. Needs 6 comparisons that require 2 ad-
ditions/subtraction each [36, p. 331]. Total cost is 2N k + 12
additions, 2N k multiplications, 1 non-linear function.

B. Arithmetic IMU Data Features

Features in Table II in this category are standard deviation
.2), maxima ((cid:3).(cid:4)), range (R) and stride

√

(σ), root mean square (
peak (SP).

1) Standard Deviation: N = 80 for ωz, use N = 64 to elim-
inate divisions via bit shift operation. Total cost is 3N additions,
N multiplications, 1 non-linear function (square root).

2) Root Mean Square: N = 80 for ωz, use N = 64 to elim-
inate division via bit shift operation. Total cost is N additions,
N multiplications, 1 non-linear function (square root).

3) Maxima: N = 95 for ωz. Need 94 comparisons that re-
quire 2 additions/subtraction each [36, p. 331]. Total cost is
2(N − 1) additions.

4) Range: N = 55 for ωy. Same as maxima, but once for
maxima and minima. Hence, total cost is 4(N − 1) additions.
5) Stride Peak: According to [31], a 4th order Butterworth

ﬁlter is needed

H(z) =

b0 + b1z−1 + b2z−2 + b3z−3 + b4z−4
1 + a1z−1 + a2z−2 + a3z−3 + a4z−4

.

(13)

When implemented in the canonical form results in 8 additions
and 9 multiplications with no divisions. Need 2 comparison that
require 2 additions/subtraction each [36, p. 331]. The total cost
is 12 additions, 9 multiplications.

APPENDIX A
ESTIMATED FEATURE EXTRACTION COST
IMU sampling frequency is fs = 50 Hz. Window lengths (N )

C. Spatio-Temporal Features

Features in Table II in this category are stride time (ST) and

are taken from [31].

stride length (SL).

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply. 

514

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 3, JUNE 2019

1) Stride Time: Requires to ﬁnd peaks, as for stride peak.
Computation of time duration is neglected here, hence total cost
is 12 additions, 9 multiplications.

2) Stride Length: Extraction is based on Madgwick et al.’s
algorithm [37] using quaternions. The reader may contact the
authors for a run down of the computational expense. The total
cost is 5050 multiplications, 3551 additions and 52 divisions.

REFERENCES

[1] T. Pringsheim, N. Jette, A. Frolkis, and T. D. Steeves, “The prevalence of
Parkinson’s disease: A systematic review and meta-analysis,” Movement
Disorders, vol. 29, no. 13, pp. 1583–1590, 2014.

[2] Y. J. Zhao et al., “Economic burden of Parkinson’s disease in Singapore,”

Eur. J. Neurology, vol. 18, no. 3, pp. 519–526, 2011.

[3] Y. J. Zhao et al., “Estimating the lifetime economic burden of Parkinson’s
disease in Singapore,” Eur. J. Neurology, vol. 20, no. 2, pp. 368–374,
2013.

[4] M. Macht et al., “Predictors of freezing in Parkinson’s disease: A sur-
vey of 6,620 Patients,” Movement Disorders, vol. 22, no. 7, pp. 953–956,
2007.

[5] S. T. Moore, H. G. MacDougall, J.-M. Gracies, H. S. Cohen, and W. G.
Ondo, “Long-term monitoring of gait in Parkinson’s disease,” Gait Posture,
vol. 26, no. 2, pp. 200–207, 2007.

[6] B. R. Bloem, J. M. Hausdorff, J. E. Visser, and N. Giladi, “Falls and
freezing of gait in Parkinson’s disease: A review of two interconnected,
episodic phenomena,” Movement Disorders, vol. 19, no. 8, pp. 871–884,
2004.

[7] M. D. Latt, S. R. Lord, J. G. Morris, and V. S. Fung, “Clinical and phys-
iological assessments for elucidating falls risk in Parkinson’s disease,”
Movement Disorders, vol. 24, no. 9, pp. 1280–1289, 2009.

[8] WHO and Ageing and Life Course Unit, WHO Global Report on Falls Pre-
vention in Older Age. Geneva, Switzerland: World Health Organization,
2008.

[9] I. Farag et al., “Economic evaluation of a falls prevention exercise program
among people with Parkinson’s disease,” Movement Disorders, vol. 31,
no. 1, pp. 53–61, 2016.

[10] M. Bächlin, J. M. Hausdorff, D. Roggen, N. Giladi, M. Plotnik, and G.
Tröster, “Online detection of freezing of gait in Parkinson’s disease pa-
tients: A performance characterization,” in Proc. 4th Int. Conf. Body Area
Netw., 2009, Art. no. 11.

[11] M. Bächlin, M. Plotnik, D. Roggen, N. Giladi, J. M. Hausdorff, and G.
Tröster, “A wearable system to assist walking of Parkinson’s disease pa-
tients,” Methods Inf. Med., vol. 49, pp. 88–95, 2010.

[12] M. Bächlin et al., “Wearable assistant for Parkinson’s disease patients
with the freezing of gait symptom,” IEEE Trans. Inf. Technol. Biomed.,
vol. 14, no. 2, pp. 436–446, Mar. 2010.

[13] S. Mazilu et al., “Online detection of freezing of gait with smartphones and
machine learning techniques,” in Proc. 6th Int. Conf. Pervasive Comput.
Technologies Healthcare, May 2012, pp. 123–130.

[14] L. Pepa, F. Verdini, M. Capecci, and M. Ceravolo, “Smartphone based
freezing of gait detection for Parkinsonian patients,” in Proc. IEEE Int.
Conf. Consumer Electron., 2015, pp. 212–215.

[15] H. Kim et al., “Unconstrained detection of freezing of gait in Parkinson’s
disease patients using smartphone,” in Proc. 37th Annu. Int. Conf. IEEE
Eng. Med. Biol. Soc., 2015, pp. 3751–3754.

[16] D. Comotti, M. Galizzi, and A. Vitali, “Nememsi: One step forward in
wireless attitude and heading reference systems,” in Proc. Int. Symp. In-
ertial Sensors Syst., 2014, pp. 1–4.

[17] P. Lorenzi, R. Rao, G. Romano, A. Kita, and F. Irrera, “Mobile devices for
the real-time detection of speciﬁc human motion disorders,” IEEE Sensors
J., vol. 16, no. 23, pp. 8220–8227, Dec. 2016.

[18] D. Ahn et al., “Smart gait-aid glasses for Parkinson’s disease patients,”

IEEE Trans. Biomed. Eng., vol. 64, no. 10, pp. 2394–2402, Oct. 2017.

[19] C. Punin, B. Barzallo, M. Huerta, A. Bermeo, M. Bravo, and C.
Llumiguano, “Wireless devices to restart walking during an episode of
FOG on patients with Parkinson’s disease,” in Proc. IEEE Ecuador Tech-
nical Chapters Meet., 2017, pp. 1–6.

[20] A. Kita, P. Lorenzi, R. Rao, and F. Irrera, “Reliable and robust detection of
freezing of gait episodes with wearable electronic devices,” IEEE Sensors
J., vol. 17, no. 6, pp. 1899–1908, Mar. 2017.

[21] A. Nieuwboer et al., “Cueing training in the home improves gait-related
mobility in Parkinson’s disease: The rescue trial,” J. Neurology, Neuro-
surgery Psychiatry, vol. 78, no. 2, pp. 134–140, 2007.

[22] A. Delval et al., “Auditory cueing of gait initiation in Parkinson’s disease
patients with freezing of gait,” Clin. Neurophysiology, vol. 125, no. 8,
pp. 1675–1681, 2014.

[23] P. J. McCandless, B. J. Evans, J. Janssen, J. Selfe, A. Churchill, and J.
Richards, “Effect of three cueing devices for people with Parkinson’s
disease with gait initiation difﬁculties,” Gait Posture, vol. 44, pp. 7–11,
2016.

[24] O. A. Cando, K. R. Hidalgo, and B. C. Palacios, “A low-cost vibratory
stimulus system to mitigate freezing of gait in Parkinson’s disease,” in
Proc. IEEE ANDESCON, 2016, pp. 1–4.

[25] J. Camps et al., “Deep learning for freezing of gait detection in Parkinson’s
disease patients in their homes using a waist-worn inertial measurement
unit,” Knowledge-Based Syst., vol. 139, pp. 119–131, 2018.

[26] C. Ahlrichs et al., “Detecting freezing of gait with a tri-axial accelerometer
in Parkinson’s disease patients,” Med. Biol. Eng. Comput., vol. 54, no. 1,
pp. 223–233, 2016.

[27] J. P. Dominguez-Morales, A. F. Jimenez-Fernandez, M. J. Dominguez-
Morales, and G. Jimenez-Moreno, “Deep neural networks for the recog-
nition and classiﬁcation of heart murmurs using neuromorphic auditory
sensors,” IEEE Trans. Biomed. Circuits Syst., vol. 12, no. 1, pp. 24–34,
Feb. 2018.

[28] X. Tang, Q. Hu, and W. Tang, “A real-time QRS detection system with
PR/RT interval and ST segment measurements for wearable ECG sen-
sors using parallel delta modulators,” IEEE Trans. Biomed. Circuits Syst.,
vol. 12, no. 4, pp. 751–761, Aug. 2018.

[29] L. Feng, Z. Li, and Y. Wang, “VLSI design of SVM-based seizure detection
system with on-chip learning capability,” IEEE Trans. Biomed. Circuits
Syst., vol. 12, no. 1, pp. 171–181, Feb. 2018.

[30] A. Jafari, N. Buswell, M. Ghovanloo, and T. Mohsenin, “A low-power
wearable stand-alone tongue drive system for people with severe dis-
abilities,” IEEE Trans. Biomed. Circuits Syst., vol. 12, no. 1, pp. 58–67,
Feb. 2018.

[31] V. Mikos et al., “Optimal window lengths, features and subsets thereof for
freezing of gait classiﬁcation,” in Proc. Int. Conf. Intell. Informat. Biomed.
Sci., 2017, pp. 1–8.

[32] S. T. Moore, H. G. MacDougall, and W. G. Ondo, “Ambulatory monitoring
of freezing of gait in Parkinson’s disease,” J. Neurosci. Methods, vol. 167,
no. 2, pp. 340–348, 2008.

[33] V. Mikos et al., “A neural network accelerator with integrated feature
extraction processor for a freezing of gait detection system,” in Proc. Asian
Solid-State Circuits Conf., 2018, pp. 59–62.

[34] B. Widrow, P. Baudrenghien, M. Vetterli, and P. Titchener, “Fundamental
relations between the LMS algorithm and the DFT,” IEEE Trans. Circuits
Syst., vol. 34, no. 7, pp. 814–820, Jul. 1987.

[35] V. Mikos et al., “Real-time patient adaptivity for freezing of gait classiﬁ-
cation through semi-supervised neural networks,” in Proc. 16th IEEE Int.
Conf. Mach. Learn. Appl., Dec. 2017, pp. 871–876.

[36] N. H. Weste, D. Harris, and A. Banerjee, CMOS VLSI Design, 3rd ed.

London, U.K.: Pearson, 2010.

[37] S. Madgwick, A. Harrison, and R. Vaidyanathan, “Estimation of IMU and
MARG orientation using a gradient descent algorithm,” in Proc. IEEE Int.
Conf. Rehabil. Robot., Jun. 2011, pp. 1–7.

Val Mikos (S’16) received the B.Sc. and M.Sc.
degrees in electrical engineering and information
technology from the Swiss Federal Institute of Tech-
nology, Zürich, Switzerland, in 2012 and 2014, re-
spectively. Since 2015, he has been working toward
the Ph.D. degree with the National University of Sin-
gapore, Singapore.

His research interests include VLSI design for
machine learning and system design for battery-
powered, miniaturized hardware.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply. 

MIKOS et al.: WEARABLE, PATIENT-ADAPTIVE FOG DETECTION SYSTEM FOR BIOFEEDBACK CUEING IN PARKINSON’S DISEASE

515

Chun-Huat Heng (S’96–M’04–SM’13) received the
B.Eng. and M.Eng. degrees from the National Uni-
versity of Singapore (NUS), Singapore, in 1996 and
1999, respectively, and the Ph.D. degree from the Uni-
versity of Illinois at Urbana-Champaign, Champaign,
IL, USA, in 2003.

From 2001 to 2004, he was with Wireless Inter-
face Technologies, San Diego, CA, USA, which was
later acquired by Chrontel. Since 2004, he has been
with the NUS, Singapore, where he is currently an
Associate Professor. He has been involved in CMOS
integrated circuits involving synthesizer, delay-locked loop, and transceiver cir-
cuits.

Dr. Heng is currently a Technical Program Committee Member for the In-
ternational Solid-State Circuits Conference and the Asian Solid-State Circuits
Conference. He was a recipient of the NUS Annual Teaching Excellence Award
in 2008, 2011, and 2013, the Faculty Innovative Teaching Award in 2009, and
the ATEA Honor Roll in 2014. He was an Associate Editor of the IEEE TRANS-
ACTIONS ON CIRCUITS AND SYSTEMS II.

Arthur Tay received the B.Eng. (ﬁrst class hons.)
and Ph.D. degrees in electrical engineering from the
National University of Singapore, Singapore, in 1995
and 1998, respectively.

He was a visiting scholar with the Information Sys-
tem Laboratory, Stanford University, Stanford, CA,
USA, from 1998 to 2000. He is currently an Associate
Professor with the Department of Electrical and Com-
puter Engineering, National University of Singapore.
His research interests include applications of mathe-
matical system science tools in healthcare, semicon-

ductor manufacturing, and process control.

Karen Mui Ling Koh received the Bachelor’s degree
in health sciences (Physiotherapy) from The Univer-
sity of Sydney, Sydney, Australia, in 1999. Her re-
search interest includes rehabilitation.

Dawn May Leng Tan received the Doctor of Clini-
cal Physiotherapy degree from the University of Mel-
bourne, Parkville, VIC, Australia, in 2011.

Dr. Dawn is currently a Senior Principal Phys-
iotherapist with the Singapore General Hospital and
works with patients with neurological and vestibu-
lar disorders in the outpatient setting. She is also an
Assistant Professor with the Singapore Institute of
Technology, and teaches in the undergraduate phys-
iotherapy degree program. Her areas of interests in-
clude stroke, Parkinson’s disease and vestibular re-
habilitation, and promoting evidence-based practice (EBP) such as conducting
systematic reviews and running EBP workshops. She is a recipient of The Efﬁ-
ciency Medal from Singapore’s Ministry of Health.

Shih-Cheng Yen received the B.S.E. and M.S.E. de-
grees in 1993, and the Ph.D. degree in 1998, all
from the Department of Bioengineering, University
of Pennsylvania, Philadelphia, PA, USA.

He is currently an Assistant Professor with the
Department of Electrical and Computer Engineering,
National University of Singapore. His research inter-
ests include neural coding, neuroprosthetic devices,
and telehealth solutions.

Nicole Shuang Yu Chia received the B.A. degree
(magna cum laude) in psychology and communica-
tion from the State University of New York, Buffalo,
NY, USA, in 2015.

Since 2016, she has been working on Parkinson’s
disease and movement disorders research with the
National Neuroscience Institute, Singapore. Her re-
search interests include telerehabilitation, gait disor-
ders, and neuropsychology.

Wing Lok Au received the Bachelor’s of Medicine,
Bachelor’s of Surgery (MBBS) degree from the Na-
tional University of Singapore, Singapore, in 1994.

He is currently the Deputy Medical Director (Clin-
ical) of National Neuroscience Institute of Singa-
pore, Singapore, and the Academic Deputy Chair
of the Neuroscience Academic Clinical Programme,
SingHealth-DukeNUS, Singapore. He received his
neurology training at the National Neuroscience In-
stitute of Singapore, and underwent two years of Fel-
lowship training in movement disorders at the Pa-
ciﬁc Parkinson’s Research Centre, Vancouver, Canada, from 2004 to 2005. In
2012, he went for further training in neurophysiology in movement disorders at
the Toronto Western Hospital, Toronto, Canada. His research interests include
functional neuroimaging, neurophysiology, and biosensor devices in movement
disorders. He was a recipient of the Distinguished Team Award, SingHealth Ex-
cellence Award in 2015, and Outstanding Clinician Award, GCEO Excellence
Award, SingHealth in 2018. He has been a Fellow of the Academy of Medicine
(Singapore) since 2004, and a Fellow of the Royal College of Physicians (Ed-
inburgh) since 2007.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:24 UTC from IEEE Xplore.  Restrictions apply.
