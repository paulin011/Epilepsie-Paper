# Hashash et al. - 2021 - Energy-Aware Distributed Edge ML for mHealth Applications With Strict Latency Requirements

IEEE WIRELESS COMMUNICATIONS LETTERS, VOL. 10, NO. 12, DECEMBER 2021

2791

Energy-Aware Distributed Edge ML for mHealth
Applications With Strict Latency Requirements

Omar Hashash , Sanaa Sharafeddine , Senior Member, IEEE, Zaher Dawy , Senior Member, IEEE,
Amr Mohamed , Senior Member, IEEE, and Elias Yaacoub , Senior Member, IEEE

Abstract—Edge machine learning (Edge ML) is expected to
serve as a key enabler for real-time mobile health (mHealth)
applications. However, its reliability is governed by the limited
energy and computing resources of user equipment (UE), along
with the wireless channel variations and dynamic resource allo-
cation at edge servers. In this letter, we incorporate both UE and
edge server computing to satisfy the strict latency requirements of
mHealth applications while efﬁciently utilizing the UE’s energy
resources. Speciﬁcally, we separate the feature extraction and
classiﬁcation processes of Edge ML inference and formulate an
optimization problem to distribute them between the UE and the
edge server while determining the optimal UE transmit power.
We demonstrate the effectiveness of the proposed approach using
an mHealth case study for predicting epileptic seizures using data
from wearable health devices.

Index Terms—Machine learning, mobile edge computing, neu-
rological mHealth systems, seizure detection and prediction.

I. INTRODUCTION

R EAL-TIME remote healthcare applications demand reli-

able solutions to satisfy their quality of service require-
ments. Emerging mobile health (mHealth) applications rely on
data collected from various sources including wearable health
devices and require utilization of effective machine learning
(ML) algorithms for prediction and inference purposes.

In edge machine learning (Edge ML)-based mHealth appli-
cations, the processing can take place at the end-user level,
such as IoT device or user equipment (UE) [1]. Example
applications include epileptic seizure prediction using elec-
troencephalogram (EEG) signals [2] and cardiac abnormalities
detection using electrocardiogram (ECG) signals [3]. The main
challenge with end-user processing is the limited energy and
computing resources. Therefore, efforts have been focused
on enabling real-time mHealth applications using advances
in mobile edge computing (MEC). For example, MEC-based

Manuscript received August 31, 2021; accepted September 28, 2021. Date
of publication October 5, 2021; date of current version December 9, 2021.
This work was supported by the Qatar National Research Fund (a mem-
ber of Qatar Foundation) under Grant NPRP12S-0305-190231. The ﬁndings
achieved herein are solely the responsibility of the authors. The associate edi-
tor coordinating the review of this article and approving it for publication was
J. Tang. (Corresponding author: Zaher Dawy.)

Omar Hashash and Zaher Dawy are with the Department of Electrical and
Computer Engineering, American University of Beirut, Beirut 1107 2020,
Lebanon (e-mail: onh02@mail.aub.edu; zd03@aub.edu.lb).

Sanaa Sharafeddine is with the Department of Computer Science and
Mathematics, Lebanese American University, Beirut 1102 2801, Lebanon
(e-mail: sanaa.sharafeddine@lau.edu.lb).

Amr Mohamed and Elias Yaacoub are with the Department of Computer
Science and Engineering, College of Engineering, Qatar University, Doha,
Qatar (e-mail: amrm@qu.edu.qa; eliasy@ieee.org).

Digital Object Identiﬁer 10.1109/LWC.2021.3117876

epileptic seizure detection has been shown to achieve accurate
results with low latency [4]. However, most mHealth applica-
tions that rely on MEC merely address the ofﬂoading aspects,
such as assigning UE transmit power, enabling efﬁcient resource
allocation, and mitigating wireless channel variations. With the
concept of distributed inference between UE and MEC evolv-
ing, an optimization problem is proposed in [5] to minimize the
weighted-sum cost that includes delay and energy consump-
tion of partitioning the lower and higher layers of a pre-trained
convolutional neural network (CNN). Moreover, an inference
ofﬂoading problem of deep neural network (DNN) partitioning
is formulated in [6] to enhance energy efﬁciency of both UEs
and base stations (BSs) while meeting stringent application
delay. This concept could be further extended to reach out
ML algorithms suitable for mHealth monitoring applications
that allow for separable feature extraction and classiﬁcation
processes, e.g., logistic regression and SVM.

In this letter, we optimize the performance of real-time
mHealth monitoring applications by efﬁciently distributing the
feature extraction and classiﬁcation processes of Edge ML
between the UE and MEC server in response to wireless chan-
nel variations and dynamic resource allocation. The proposed
approach demonstrates the value of integrating Edge ML with
MEC, with the UE and edge server acting as cooperative
agents to meet the application’s strict latency requirements
while minimizing the UE’s energy consumption.

II. SYSTEM MODEL
Consider a UE operating a real-time mHealth monitoring
application to monitor health data from wearable devices as
shown in Fig. 1. The UE falls under the coverage of a network
BS, which is equipped with an MEC server that is capable
of computing the UE ofﬂoaded computations. The applica-
tion relies on Edge ML to initiate real-time responses, where
it is assumed that both UE and edge server have the same
pre-trained ML model speciﬁc to run the mHealth applica-
tion. Thus, we can characterize the feature extraction process
of the ML application with a processing density of Lf CPU
cycles/bit. Similarly, the classiﬁcation process is characterized
with a processing density of Lc CPU cycles/bit [7], [8].

Operating in an MEC framework, the system timeline can
be divided into timeslots τ of duration T seconds (sec) as
shown in Fig. 1. At the beginning of each timeslot τ , the
UE periodically receives a data vector of size Af (bits) for
feature extraction. After extracting the features, the resultant
feature vector of size Ac (bits) is used for model classiﬁcation.
Hence, the resulting classiﬁcation vector Ic (bits) that contains

2162-2345 c(cid:2) 2021 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:45 UTC from IEEE Xplore.  Restrictions apply. 

2792

IEEE WIRELESS COMMUNICATIONS LETTERS, VOL. 10, NO. 12, DECEMBER 2021

Fig. 1. Neurological mHealth monitoring system over the edge with the
associated timeline processes.

the response should be used for real-time interpretation at the
UE. This real-time process requires maintaining the computa-
tion time of the feature extraction and classiﬁcation processes
below maximum time limit Tmax, where Tmax ≤ T . Hence,
timeslot of this
to consider each individual
it is essential
monitoring application in an independent manner.

Before the beginning of each timeslot, the MEC server noti-
ﬁes the UE about the computing resources available for the
application. The assigned computing resources are represented
in terms of the CPU frequency fMEC(τ ) (Hz) constant over
timeslot τ . Meanwhile, the UE assigns its available computing
resources fUE(τ ) (Hz) that is constant over each timeslot τ .
To enable distributed Edge ML, the feature extraction and
classiﬁcation processes are partitioned between the UE and
MEC server, leading to four possible cases as shown in Fig. 2.
To illustrate, case 1 refers to feature extraction and classiﬁca-
tion executed locally at the UE. On the other hand, case 4
refers to remote feature extraction and classiﬁcation execution
by ofﬂoading to the MEC server. Furthermore, cases 2 and
3 refer to distributed feature extraction and classiﬁcation exe-
cution. Speciﬁcally, feature extraction is executed on UE and
followed by classiﬁcation at the MEC server in case 2, while
feature extraction is performed at the MEC server and fol-
lowed by classiﬁcation at the UE in case 3. With the different
vector sizes that can be ofﬂoaded while taking into consid-
eration UE and MEC resource allocation, we can manage to
choose the most energy efﬁcient case that reliably guarantees
meeting strict latency requirements for each τ .

Assuming that the response Ic has a minimal size in com-
parison with other vectors [6], [8], the latency Ti (τ ) of each
case i ∈ {1, 2, 3, 4} shown in Fig. 2 is stated as:

T1(τ ) =

T2(τ ) =

T3(τ ) =

T4(τ ) =

Af Lf
fUE(τ )
Af Lf
fUE(τ )
Af
Ru (τ )
Af
Ru (τ )

+

+

+

+

,

AcLc
fUE(τ )
Ac
Ru (τ )
Af Lf
fMEC(τ )
Af Lf
fMEC(τ )

+

,

AcLc
fMEC(τ )
Ac
Rd (τ )
AcLc
fMEC(τ )

+

+

+

(1)

(2)

(3)

(4)

AcLc
fUE(τ )

,

,

Fig. 2. Distributed Edge ML cases for mHealth monitoring system.

where Rd (τ ) is the downlink data rate from the MEC server,
and Ru (τ ) = W log2(1 +
N0W ) is the UE uplink data
rate where h(τ ) is the wireless channel gain, Pt (τ ) is the UE
uplink transmit power for ofﬂoading, N0 is the noise spectral
density, and W is the uplink channel bandwidth.

h(τ )Pt (τ )

t

To determine the consumed UE energy, we deﬁne the
local computing power as k [fUE(τ )]3, where k is a param-
eter directly related to the CPU hardware implementation [7].
Moreover, we deﬁne P max
as the maximum UE transmit
power and assume the consumed UE energy in the down-
link is negligible. The corresponding UE energy for each case
is the sum of local computing energy and energy needed for
ofﬂoading over a timeslot. The UE energy consumed Ei (τ )
for each case i is denoted as:
3 × (

E1(τ ) = k [fUE(τ )]

(5)

),

+

Af Lf
fUE(τ )
Af Lf
fUE(τ )
AcLc
fUE(τ )

AcLc
fUE(τ )

+ Pt (τ ) ×

+ Pt (τ ) ×

Ac
Ru (τ )
Af
Ru (τ )

,

,

(6)

(7)

(8)

E2(τ ) = k [fUE(τ )]

3 ×

E3(τ ) = k [fUE(τ )]

3 ×

E4(τ ) = Pt (τ ) ×

Af
Ru (τ )

.

It can be seen that the alternation between the cases can
generate a mitigation process from elevated delays that might
occur due to the dynamic resource allocation fUE(τ ) and
fMEC(τ ), and the wireless conditions modeled in the channel
gain h(τ ). In addition, to design an energy efﬁcient scheme
while ensuring that latency requirements are met, the optimal
value of Pt (τ ) should be speciﬁed as it plays a vital role in
determining latency and energy.

III. PROBLEM FORMULATION
To model the alternation in response to dynamic resource
allocations and wireless channel conditions, it is required to
formulate an optimization problem to determine the optimal
case with the corresponding transmit power Pt . As the UE
receives the channel gain h(τ ) and the allocated resources
fMEC(τ ) through control signaling, and has access to its own
computing resources fUE(τ ), a decision making process can
be initiated by the UE to determine the optimal case.

We deﬁne two binary variables a and b to denote whether
feature extraction and classiﬁcation, respectively, are per-
formed locally at the UE or remotely at the MEC sever as

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:45 UTC from IEEE Xplore.  Restrictions apply. 

HASHASH et al.: ENERGY-AWARE DISTRIBUTED EDGE ML FOR mHEALTH APPLICATIONS

2793

TABLE I
LOCAL AND REMOTE EXECUTION

TABLE II
SIMULATION PARAMETERS

shown in Table I. Furthermore, we omit the index τ from the
variables for ease of notations. Then, we formulate the general
latency To and energy Eo as a function of the binary variables
as follows:
Eo = akAf Lf [fUE]
(cid:2)

+ bkAcLc[fUE]
(cid:3)

2

2

Af + (Ac − Af )a − abAc

W log2(1 +

hPt
N0W )

,

(9)

Pt

(cid:5)

−

AcLc
AcLc
fMEC
fUE
Af + a(Ac − Af ) − abAc

b

W log2(1 +

hPt
N0W )

(10)

Af Lf
fUE

+

+

(cid:4)

+

(cid:5)

a +

−

Af Lf
fMEC
Af Lf + AcLc
fMEC
b(1 − a)Ac
Rd

.

+

(cid:4)

To =

The optimization problem can then be formulated with UE

energy minimization objective function as follows:
Eo

minimize
a,b,Pt

subjectto To ≤ Tmax,

Pt ≥ 0,
Pt − P max
t
a, b ∈ {0, 1}.

(1 − ab) ≤ 0,

(11)

This is a mixed integer non-linear programming (MINLP)
optimization problem. This problem is subject to the following
constraints: i) the latency To in (10) should be maintained less
than Tmax, ii) the transmit power Pt is a non-zero variable
for all the cases except that of local feature extraction and
classiﬁcation and having an upper bound of P max
, and iii) a
and b are binary decision variables referring to the optimal
case from Table I.

t

To transform the problem to a mixed integer linear program-
ming (MILP) problem, the non-linearity introduced by the log
function is removed by discretizing Pt into N levels such that

Pt = Pi =

iP max
t
N

,

(12)

where i ∈ {0, 1, 2, . . . , N }.

Then, the variables X and Y are introduced in (9) and (10)

respectively, such that
Pt

X =

log2(1 +

hPt
N0W )

, Y =

1

log2(1 +

hPt
N0W )

(13)

Since N discrete values of Pt are deﬁned, then we have N
values for X and Y, respectively. Thus, X and Y are formulated
as a summation of individual Pt values as follows:

X =

N(cid:6)

i=1

ki xi =

N(cid:6)

i=1

ki Pi
log2(1 +

hPi
N0W )

,

(14)

N(cid:6)

Y =

ki yi =

N(cid:6)

ki
log2(1 +

,

hPi
N0W )

(15)

i=1
where ki ∈ {0, 1} ∀i ∈ {1, 2, . . . , N }.

i=1

To further handle the non-linearity in (11), common lin-
earization techniques are utilized, where the product of the
binary variables a and b is replaced by an additional binary
variable c. In addition, the product of binary and continuous
variables obtained from the multiplication of X and Y with the
binary variables is also replaced. The resulting problem is a
MILP and is solved using MATLAB.

IV. NEUROLOGICAL MHEALTH CASE STUDY:
PERFORMANCE RESULTS AND ANALYSIS
As an application to the presented problem, we target
an mHealth application that demands real-time inference to
predict epileptic seizures occurrence. The system is based on
the EEG feature extraction algorithm in [9]. To simulate this
system, we consider a UE at a distance of d = 50 m from
the BS and an operating frequency f = 5.8 GHz. We assume
that the channels are subject to Rayleigh ﬂat fading of unity
variance, and the coherence time is considered greater than
Tmax. The rest of the parameters are found in Table II [8].

A. System Performance Over a Single Timeslot

In this section, we aim to verify the optimal decision making
by recording how the system responds to simulation conditions
that can be encountered for a single timeslot. Hence, we con-
sider one timeslot having a gain h = −140 dBm and assigned
fUE = 0.5 GHz. Then, according to the value of fMEC that has
been assigned for this timeslot, the optimal decision to ensure
that the latency requirement is not violated while maintaining
energy efﬁciency can be determined. Thus, we consider fMEC
to have a uniform distribution ranging below 1 GHz, and show
the proposed decision making with the corresponding Pt in
Fig. 3.

As shown in Fig. 3, when fMEC is relatively minimal, the
optimal decision leads to completing the feature extraction
and classiﬁcation process on the UE with no transmit power.
However, if fMEC is assigned slightly beyond 0.02 GHz, dis-
tributed computing is favored by executing feature extraction
on the UE and followed by classiﬁcation at the MEC server
with Pt reaching 25% of max power P max
. This scenario
remains favored for assigned fMEC values reaching 0.58 GHz,
after which the decision is shifted towards remote MEC with
Pt reaching 75% of the max power for fMEC slightly beyond
0.58 GHz. The increase in Pt
is veriﬁed as to explicitly
increase the data rate to compensate computing delay result-
ing from the limited share of fMEC. When fMEC is assigned

t

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:45 UTC from IEEE Xplore.  Restrictions apply. 

2794

IEEE WIRELESS COMMUNICATIONS LETTERS, VOL. 10, NO. 12, DECEMBER 2021

Fig. 3. Decision making with optimal transmit power over one timeslot
according to fMEC (GHz) assuming h = −140 dB and fUE = 0.5 GHz.

Fig. 4.
0.3 GHz ≤ fUE ≤ 0.8 GHz and 0.15 GHz ≤ fMEC ≤ 1.2 GHz.

a) Cumulative energy and b) latency over 30 timeslots where

beyond this critical inﬂection stage, the increased data rate is
no longer needed to preserve the delay below Tmax, and Pt
can be gradually decreased to 50% of the max power. For
fMEC beyond 0.75 GHz, Pt can be decreased to 25% of the
max transmit power afterwards to facilitate ofﬂoading. With
the advantage of limiting Pt below P max
while considering
the optimal decision making over the range of fMEC, we can
facilitate higher UE energy efﬁciency.

t

B. System Performance Over Multiple Timeslots

In this section, we consider decision making over multiple
timeslots and record the performance in terms of the cumu-
lative UE energy consumed and the computing latency. For
this purpose, we simulate the system over a series of 30
timeslots, where both fUE and fMEC are assumed to have a
uniform distribution such that 0.3 GHz ≤ fUE ≤ 0.8 GHz
and 0.15 GHz ≤ fMEC ≤ 1.2 GHz. Over each timeslot,
the optimal decision is determined to choose the most energy
efﬁcient case without violating the latency Tmax, with the
corresponding optimal Pt . Moreover, we compare the effec-
tiveness of our approach, with a static method which operates
for one of the four cases explicitly with constant transmit
power P max
, and with a baseline that represents the global
optimal solution found through exhaustive search.

t

As shown in Fig. 4(a), the cumulative UE energy con-
sumed for 30 timeslots has shown variations for different
cases. Hence, cases 1 and 2 reach around 159 Joules (J) in
comparison to 24.73 J in cases 3 and 4. Nonetheless, with
the optimal decision making we reach a cumulative energy of
42.43 J, which is close to the range of cases 3 and 4. As the
optimal decision making process allows for energy reduction,
this also offers an advantage in terms of latency restriction
over all timeslots as compared to all other alternative cases.
As shown in Fig. 4(b), the latency over each timeslot changes
reaching values beyond the strict latency Tmax. Comparing
the static technique to the dynamic decision making process
in terms of latency, a latency mitigation process arises specif-
ically for situations having latency above Tmax, where the
cases have recorded values over timeslots reaching up to 100
sec. Remarkably, it can be seen that optimal decision making
records latency values below Tmax for the 30 timeslots, and
performs close to the global optimal solution.

V. CONCLUSION
In this letter, we present a distributed Edge ML system for
mHealth monitoring applications with strict latency require-
ments. We partition the feature extraction and classiﬁcation
processes of the real-time inference application between UE
and MEC server. This aims to mitigate elevated latency
values due to the dynamic wireless conditions and comput-
ing resource allocation of the UE and MEC server, whilst
ensuring UE energy efﬁciency. We formulate an optimization
problem to model the decision making process and deter-
mine the optimal transmit power. We include an mHealth
seizure prediction case study with our proposed method and
demonstrate performance gains in terms of reduced energy and
latency. An interesting extension is to leverage deep learning
as an efﬁcient approach to solve the optimization problem [10].

REFERENCES

[1] G. Zhu, D. Liu, Y. Du, C. You, J. Zhang, and K. Huang, “Toward
an intelligent edge: Wireless communication meets machine learning,”
IEEE Commun. Mag., vol. 58, no. 1, pp. 19–25, Jan. 2020.

[2] F. Samie, S. Paul, L. Bauer, and J. Henkel, “Highly efﬁcient and accurate
seizure prediction on constrained IoT devices,” in Proc. Design Autom.
Test Eur. Conf. Exhibit., Mar. 2018, pp. 955–960.

[3] S. Raj, “An efﬁcient IoT-based platform for remote real-time cardiac
activity monitoring,” IEEE Trans. Consum. Electron., vol. 66, no. 2,
pp. 106–114, May 2020.

[4] Z. S. Ali, N. Subramanian, and A. Erbad, “Smart health monitoring for
seizure detection using mobile edge computing,” in Proc. Int. Wireless
Commun. Mobile Comput., Jun. 2020, pp. 1903–1908.

[5] B. Yang, X. Cao, C. Yuen, and L. Qian, “Ofﬂoading optimization in
edge computing for deep learning enabled target tracking by Internet-
of-UAVs,” 2020. [Online]. Available: arXiv:2008.08001.

[6] Z. Xu et al., “Energy-aware inference ofﬂoading for DNN-driven appli-
cations in mobile edge clouds,” IEEE Trans. Parallel Distrib. Syst.,
vol. 32, no. 4, pp. 799–814, Apr. 2021.

[7] C.-F. Liu, M. Bennis, M. Debbah, and H. V. Poor, “Dynamic task
ofﬂoading and resource allocation for ultra-reliable low-latency edge
computing,” IEEE Trans. Commun., vol. 67, no. 6, pp. 4132–4150,
Jun. 2019.

[8] O. Hashash, S. Sharafeddine, and Z. Dawy, “MEC-based energy-aware
distributed feature extraction for mHealth applications with strict latency
requirements,” in Proc. IEEE ICC 4th Int. Workshop IoT Enabling
Technol. Healthcare, Montreal, QC, Canada, Jun. 2021, pp. 1–6.
[9] M. Nassrallah, M. Haidar, H. Alawieh, A. El Hajj, and Z. Dawy,
“Patient-aware EEG-based feature and classiﬁer selection for e-health
epileptic seizure prediction,” in Proc. IEEE Global Commun. Conf.
(GLOBECOM), Abu Dhabi, UAE, Dec. 2018, pp. 1–6.

[10] B. Yang, X. Cao, J. Bassey, X. Li, and L. Qian, “Computation ofﬂoading
in multi-access edge computing: A multi-task learning approach,” IEEE
Trans. Mobile Comput., vol. 20, no. 9, pp. 2745–2762, Sep. 2021.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:45 UTC from IEEE Xplore.  Restrictions apply.
