# Forooghifar et al. - 2019 - Resource-Aware Distributed Epilepsy Monitoring Using Self-Awareness From Edge to Cloud

1338

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 6, DECEMBER 2019

Resource-Aware Distributed Epilepsy Monitoring
Using Self-Awareness From Edge to Cloud

Farnaz Forooghifar

, Amir Aminifar

, and David Atienza

, Fellow, IEEE

Abstract—The integration of wearable devices in humans’ daily
lives has grown signiﬁcantly in recent years and still continues
to affect different aspects of high-quality life. Thus, ensuring the
reliability of the decisions becomes essential in biomedical applica-
tions, while representing a major challenge considering battery-
powered wearable technologies. Transferring the complex and
energy-consuming computations to fogs or clouds can signiﬁcantly
reduce the energy consumption of wearable devices and result in
a longer lifetime of these systems with a single battery charge. In
this work, we aim to distribute the complex and energy-consuming
machine-learning computations between the edge, fog, and cloud,
based on the notion of self-awareness that takes into account the
complexity and reliability of the algorithm. We also model and
analyze the trade-offs in terms of energy consumption, latency,
and performance of different Internet of Things (IoT) solutions.
We consider the epileptic seizure detection problem as our real-
world case study to demonstrate the importance of our proposed
self-aware methodology.

Index Terms—Cloud, distributed health monitoring, edge,

epilepsy, fog, IoT, self-awareness.

I. INTRODUCTION

W EARABLE devices are integrated in everyday life of

humans, monitoring their activities and analyzing their
health conditions using many different sensors [1], [2]. Accord-
ing to the statistics, by 2021, the number of wearable devices will
be approximately 929 million, which is a massive increase from
the 325 million of 2016 [3]. To guarantee reliable functioning
of these devices for real-time health monitoring, a long battery
lifetime, and thus, an intelligent energy management technique
is required.

The solution recently being considered to manage battery
lifetime of wearable devices is the migration of complex and
energy-hungry tasks to higher level infrastructures that can pro-
vide more computational resources [4]. Different computation
layers including fog (personal devices such as cellphones and
smart watches) and cloud are available for interaction with

Manuscript received July 15, 2019; revised September 13, 2019; accepted
October 25, 2019. Date of publication November 4, 2019; date of current version
December 31, 2019. This work was supported in part by the MyPreHealth
research project Hasler Foundation project No. 16073, in part by the ML-Edge
research grant by the Swiss NSF GA No. 200020_182009/1, in part by the
EC H2020 DeepHealth project GA No. 825111, and in part by the Human
Brain Project (HBP) SGA2 GA No. 785907. This paper was recommended by
Associate Editor Y. Zheng. (Corresponding author: Farnaz Forooghifar.)

The authors are with the Embedded Systems Laboratory, Swiss Fed-
eral Institute of Technology Lausanne, 1015 Lausanne, Switzerland (e-mail:
farnaz.forooghifar@epﬂ.ch; amir.aminifar@epﬂ.ch; david.atienza@epﬂ.ch).

Color versions of one or more of the ﬁgures in this article are available online

at http://ieeexplore.ieee.org.

Digital Object Identiﬁer 10.1109/TBCAS.2019.2951222

Fig. 1. Overview of distributed health monitoring over the Internet of Things
(IoT) infrastructure: (1) Edge computing, (2) Edge plus fog computing, (3) Edge
plus cloud computing with communication through fog gateway, and (4) Edge
plus cloud computing.

wearable devices as shown in Fig. 1. Deciding whether to com-
municate with higher layers depends on the trade-off between
communication and computation costs, in order to reduce the
overall energy consumption of wearable devices and improve
their battery lifetime.

Self-awareness is a promising solution for reducing system’s
energy consumption and improving battery lifetime of wearable
devices. Self-aware systems are equipped with control units
which facilitate monitoring their own performance, adapting
to changes and improving autonomously [5], [6]. The notion
of self-awareness provides the system with knowledge about
itself and also its environment and their changes during the
time. Thus, the system can adapt to these new situations and
predict the effect of dynamic changes to fulﬁll continuous high
performance operation according to the deﬁned goals of the sys-
tem. In the task distribution over higher computation layers via
communication, self-awareness can provide us with information
to determine whether this communication can contribute in total
energy reduction.

In this article, we analyze workload distribution over edge,
fog and cloud in order to minimize the energy consumption
of the edge device and enhance its battery lifetime. We study
the communication and computation costs of edge device for
different workload distribution scenarios, which provides us
with the information to obtain the most efﬁcient solution for
the particular application we consider. Moreover, we adopt the
notion of self-awareness to gain maximum energy saving using
task distribution. In order to evaluate our proposed methodology,
we consider a real-time epileptic seizure detection system, as our
real-world case study.

1932-4545 © 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply. 

FOROOGHIFAR et al.: RESOURCE-AWARE DISTRIBUTED EPILEPSY MONITORING USING SELF-AWARENESS FROM EDGE TO CLOUD

1339

Epilepsy is one of the most common chronic diseases affecting
more than 50 million people worldwide [7]. Despite the recent
advances in anti-epileptic drugs, one-third of the epileptic pa-
tients still suffer from this disorder. Moreover, epilepsy repre-
sents the second neurological cause of years of potential life lost,
primarily due to seizure-triggered accidents and sudden unex-
pected death in epilepsy (SUDEP) [8]. To be able to notify family
members, caregivers, and emergency units in case of a seizure for
help, monitoring epileptic patients in real time is necessary. This
can help reducing seizure-related injuries, status epilepticus, and
SUDEP [9]. Although the gold standard in epilepsy monitoring
is based on the video-electroencephalogram, due to its intru-
sive nature [10], [11], electrocardiogram (ECG) monitoring has
recently attracted a lot of attention.

We consider the cost of different workload distribution sce-
narios for the ECG-based epilepsy monitoring system proposed
in [12], [13] and optimize the energy consumption for this target
system using self-awareness. The main contributions of this
article are as follows:

(cid:2)

(cid:2)

The ﬁrst contribution of this work is distributed epilepsy
monitoring over edge, fog, and cloud with the goal of
improving the battery lifetime of the edge device. We
investigate task distribution between edge and higher level
computing infrastructures, including fog and cloud. We
model the latency and energy of four main task distribution
scenarios, all shown in Fig. 1, considering both computa-
tion and communication infrastructures. These scenarios
include: 1) Edge computing, 2) Edge plus fog comput-
ing, 3) Edge plus cloud computing with communication
through fog gateway, and 4) Edge plus cloud computing,
which are thoroughly analyzed in this article.
The second contribution of this work is utilizing the notion
of self-awareness to perform optimization and select an
energy-efﬁcient strategy for distributed health-monitoring
between edge, fog and cloud, in order to maximize the bat-
tery lifetime of the edge device. Leveraging self-awareness,
the heavy computation is distributed over the fog and
cloud engines, only when a computationally light-weight
low-power learning algorithm on the edge wearable de-
vice is not sufﬁcient to make a conﬁdent decision about
patient’s status. Besides, communication with cloud is
also done in emergency cases to notify doctors. We val-
idate our technique on an epileptic seizure detection sys-
tem with the INYU platform [14] using the EPILEPSIA
dataset [15], which consists of ECG data from 30 patients
with 277 seizures recorded in 4603 hours.

The rest of this article is organized as follows. In Section II, we
brieﬂy review the latest studies on task distribution over edge
and higher level computation infrastructures and also on the
self-awareness in biomedical applications. Section III contains
the details on the components of IoT platforms including the
computation and communication infrastructures. In Sections IV
and V, we formulate the energy and latency of both computation
and communication for edge devices in different task distribu-
tion scenarios, both including or not the notion of self-awareness.
the experimental setup and results are discussed in
Then,
Sections VI and VII, respectively. In particular, we evaluate the

efﬁciency of our proposed self-aware medical wearable solution
in terms of energy, latency and performance against the system
without self-aware energy management. Finally, in Section VIII,
we summarize the main conclusions of this article.

II. STATE-OF-THE-ART

In this section, we review the recent studies in distributed
biomedical health monitoring systems over the edge, fog and
cloud. In addition, we review the recent studies, which leverage
the notion of self-awareness for performance enhancement and
energy optimization.

A. Edge, Fog, and Cloud in Biomedical Domain

Several studies have recently addressed task distribution over
wearable devices and higher computation layers. A survey on
cloud-based processing for health-monitoring is done in [16].
One of the main beneﬁts of moving computations on cloud is
long-term storing of patients’ bio-signals for better analysis of
their health condition and its changes during long periods. The
concept of cloudlet computing is also analyzed as a platform
to run time-critical tasks. Storing data in clouds also removes
the necessity to repeat the same test in different hospitals for
the same patient [17]. In [18], the challenge of security of the
communication with higher layers is addressed using water mark
and user identiﬁcation codes. Another issue in using higher
computation levels is management of huge amount of medical
data which is addressed in [19], where the scheduling of virtual
machines in cloud environments is improved using parallel
processing.

In [20], the fog layer is introduced as a third level of com-
putation between edge and cloud for healthcare IoTs, which
could achieve more than 90% bandwidth efﬁciency in their
ECG feature extraction case study. In [21], Convolutional neural
network is implemented in fog layer which is again considered
in ECG classiﬁcation and impressive reduction in transmission
time is achieved replacing cloud with the fog layer. In [22], the
authors propose a concept architecture for real-time remote car-
diac health-monitoring with long QT syndrome case study. They
use ZigBee to communicate with cloudlet for resource-intensive
tasks with context-aware concentration of data. However, none
of these works have considered cloud as the third layer to handle
higher complexity tasks or to share the information with the
doctors.

The authors of [23] have developed an Android app to monitor
the ECG signal of patients and save it in private cloud server to
be retrieved by medical personnel for analysis. As a result, their
main focus is on sending the data efﬁciently using compression
and also guaranteeing the security of the platform by applying
encryption methods. Thus, they do not do energy and latency
modeling and do not perform any distributed pathology detection
over cloud. In [24], the connection between wearable sensors
and cloud infrastructure is provided by personal servers, which
is used for basic analysis and aggregation. They have considered
congestive heart failure as the case study to analyze their pro-
posed system. However, the authors do not consider dynamic

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply. 

1340

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 6, DECEMBER 2019

distribution of workload over the edge, fog, and cloud infras-
tructure using the self-awareness concept. Then, it is shown
in [25], that for their platforms, which are smartglasses and
smartwatches, the overall energy consumption and communica-
tion delay are reduced with direct internet connection via WiFi
compared to using Bluetooth. Nevertheless, the authors do not
formulate the end-to-end latency and energy consumption and
do not consider the self-aware distribution of workload over the
edge, fog, and cloud infrastructure.

The analysis of Mobile Cloud Computing (MCC) is done
in [26], using analytical modeling where the energy and delay
trade-offs are discussed. They have discussed different scenarios
of task ofﬂoading to smartphone and cloud analyzing delay
and power consumption of using WiFi and LTE standards.
Although they have provided energy and latency formulation
for both computation and communication between wearable
system, smart phone and cloud, their modeling do not contain
any energy-management technique. In [27], the best computa-
tion migration scenario is selected to optimize the latency of
the system in arrhythmia classiﬁcation. However, the authors
have not considered the energy consumption and lifetime of
such edge devices. Moreover, they do not leverage the notion of
self-awareness to distribute workload over the fog/cloud infras-
tructure with higher processing power. In [28], a high-quality
and low-power cardiovascular monitoring system is proposed
which communicates with cloud using Bluetooth Low Energy
(BLE) and LoRA. This work provides a comparison between
BLE and LoRa, but does not provide a general formulation for
the optimization of energy and latency in different distribution
scenarios. In conclusion, the previous studies do not consider a
general formulation of dynamic distribution of workload over
the edge, fog, and cloud infrastructure using the self-awareness
concept, taking into account both the real-time operation or end-
to-end latency and the energy consumption or battery lifetime.

B. Self-Awareness in Biomedical Applications

Self-awareness has been one of the promising concepts to
improve system’s performance and reduce its energy consump-
tion in literature [29]–[33]. In health monitoring this concept
is used to reduce energy consumption and extend the battery
lifetime of wearable devices. In [34], remote health monitoring
is performed based on personalized data (such as age, gender,
etc.) and situation-awareness is adopted to increase the accuracy
of remote health monitoring. In addition, different priorities
are given to the sensory data collection to consider the energy
efﬁciency and dependability of the system.

In [35], different observation parameters such as conﬁdence
and history are described and a high-quality description of the
system from raw data using these parameters is provided for
an emotion recognition system. In [13], a self-aware seizure
detection system is proposed where both energy reduction and
performance improvement are obtained using conﬁdence evalu-
ation. In [36], automatic labeling of seizure in epilepsy detection
system is performed using self-learning.

In conclusion,

there is no global optimum scenario for
all health monitoring applications. Thus, in order to enable

distributed health monitoring over edge, fog and cloud, the
latency, energy, and lifetime of the system should be analyzed for
each particular case study. Therefore, in this article we propose a
model to estimate the energy and latency of both computations
and communications that should be done by the edge device
plus the energy consumed by the fog layer in different task
distribution scenarios over edge, fog and cloud. Our system also
beneﬁts from the notion of self-awareness to adopt the most
efﬁcient scenario among all to minimize energy consumption.
This is fulﬁlled by managing multiple levels of computation
over edge, fog and cloud. Different scenarios are then applied
on an ECG-based seizure detection system to build a distributed
epilepsy monitoring system using self-awareness over edge, fog,
and cloud.

III. INTERNET OF THINGS (IOT) INFRASTRUCTURE

In this section, we provide the background for computa-
tion and communication infrastructures in IoT platforms. The
high-level overview of an IoT platform is shown in Fig. 1,
including the edge sensors, the fog devices and the cloud en-
gines. Four different distribution scenarios are considered for
this framework: 1) performing all the tasks on the edge sensors,
2) task distribution between the edge sensors and the fog devices,
3) task distribution between the edge sensors and the cloud
engines using the fog devices as gateways, and 4) direct task
distribution between the edge sensors and the cloud engines.

A. Computation Infrastructure

(cid:2)

(cid:2)

(cid:2)

Edge: These local devices are equipped with bio-sensors
and perform multi-signal acquisition, which results in
signiﬁcant energy consumption even without considering
other processes. Although using edge sensors for light
computational tasks results in the lowest response time,
in order to enable them to operate for days with single
battery charge, the energy-hungry computations are often
distributed to higher computation layers, e.g., fog and cloud
engines, which are equipped with more computational
resources.
Fog: These devices are usually within short distances from
the edge devices and, as a result, the latency overhead of
communication with them is not very high. On the other
hand, ofﬂoading the energy-hungry computations on the
fog devices reduces the computation overhead on the edge
devices. Despite the aforementioned advantages, still, such
devices are limited in terms of computational power and
energy consumption to run very complex machine learning
and signal processing techniques.
Cloud: The cloud engines are the most computationally
powerful platforms and provide the illusion of inﬁnite com-
putational resources, with no energy limitation. However,
as cloud engines are at long distances from the users and
edge devices, the latency and energy of communication
are substantial and become the main limitation. Although
the communication energy forced on edge devices can be
reduced by performing a two-phase communication, i.e.,
ﬁrst, between the edge and fog and, then, between the

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply. 

FOROOGHIFAR et al.: RESOURCE-AWARE DISTRIBUTED EPILEPSY MONITORING USING SELF-AWARENESS FROM EDGE TO CLOUD

1341

TABLE I
NOTATION USED FOR MODELING RESPONSE-TIME LATENCY AND ENERGY CONSUMPTION

fog and cloud, the long latency still remains a signiﬁcant
drawback.

B. Communication Infrastructure

(cid:2)

(cid:2)

(cid:2)

Bluetooth Low Energy (BLE): To communicate between
edge and fog, we use BLE protocol [37], which is a low-
power protocol suitable for short distance communications.
We consider common rate of transmission for BLE, which
is 1 Mbps. To calculate the power, we also adopt the values
provided by Nordic DevZone online power analyzer [38].
It assumes that the transmission current is consumed by the
system during transmission and for the rest of the times the
idle current is consumed. Then, the average current and the
power are calculated according to this assumption.
Sigfox: This is a light-weight protocol used for sending
small amount of data with low power consumption. We can
send 6 messages per hour (12 bytes) and thus, 144 messages
per day containing 140 uplink and 4 downlink [39]. This
protocol is energy-efﬁcient as it consumes only 15 to
45 mA during a few seconds (6 s per message) and the
idle consumption is negligible. As discussed, according to
its low communication capacity per day only small data or
messages can be transmitted through this protocol.
LoRa: This protocol follows fair access policy that limits
the uplink air time to 30 seconds per day (24 hours)
per node. For 10 bytes of payload, this translates in 20
messages per day at SF12 or 500 messages per day at
SF7. The downlink messages are limited to 10 messages
per day (24 hours) per node. A reliable goal is to keep
the application payload under 12 bytes, and the interval
between the messages at least several minutes [40].

(cid:2)

WiFi: The communication with cloud is done using WiFi
standard considering several data centers in between. Up
to 100 Mbps can be obtained from this protocol depending
on the trafﬁc [41]. Also, continuous transmission of data
is possible provided that there is an access to the network.

IV. MODELING OF ENERGY AND LATENCY FOR THE EDGE
SENSOR IN DISTRIBUTED HEALTH MONITORING

In this section, we formulate the energy consumption and
response-time latency of different distribution scenarios, which
will then be used to optimize the system and improve battery
lifetime in wearable health monitoring devices. All notations
used in this section and the next section can be found in Table I.

A. Edge Formulation

In this part we describe the scenario where there is no com-

munication between the edge and the higher layers.

(cid:2)

Latency: This is the latency of performing different training
phases of the system which includes the steps shown in
Fig. 2 in our epilepsy detection case study. The latency of
the communication (LEdge) is calculated as:

LEdge = LAC + LP P + LF E + LM L,

(1)

where LAC, LP P , LF E, and LM L are the latencies for
acquisition of sufﬁcient number of samples to be processed
by the signal processing and machine learning algorithms,
preprocessing, feature extraction and machine learning,
respectively.
Energy: This energy consists of the energies for performing
different steps in the learning procedure (Fig. 2 as an

(cid:2)

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply. 

1342

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 6, DECEMBER 2019

Fig. 2. Overview of the epileptic seizure detection system used as our case study [13].

example):

EEdge = EAC + EP P + EF E + EM L + Eidle,

(2)

where EAC, EP P , EF E, and EM L are the energies due to
acquisition of sufﬁcient number of samples to be processed
by the signal processing and machine learning algorithms,
preprocessing, feature extraction and machine learning,
respectively. We also consider the Eidle, which represents
the energies consumed in the idle phase, containing leakage
energy as well as the energy from different power saving
states of the edge device.

In the latest low-power sensor nodes, which do not need
to update memory regularly, thanks to advanced power
management techniques [42], the system is in the sleep
mode during the idle phase and only a small subsystem
monitors the state of the system to wake up the entire
system when there is pending processing needed to be
done. Therefore, we assume that for such systems, the idle
energy is almost equal to the sleep energy, with negligible
energy spent in sleep states, compared to the computation
energy.

B. Edge→Fog Formulation

In this section, we formulate the scenario when the edge sen-
sor communicates with the fog device and complex calculations
are handled by the fog layer instead of the edge sensor.

(cid:2)

Latency: This is the latency calculated in Eq. (1) plus the
latency of communication between the edge and the fog.
LEdge(E → F ) = LAC + LP P + γF · (LF E + LM L)

+ LE→F,T X ,

(3)

where LE→F,T X is the transmission latency. We assume
that the most complex tasks, which are the feature extrac-
tion and machine learning, are performed by the higher
layer, where γF is the speed-up factor at the fog. As the fog
devices include high-performance computing resources,
the computation time is reduced and we have γF ≤ 1.

To communicate between the edge and the fog, we use
the BLE and, in order to compute the latency, we calculate

the amount of data we transfer. As a result, the formula is:

LE→F,T X =

V(E→F ) · (1 + BERF )
BBLE

,

(4)

where V(E→F ) is the volume of data being transferred
between the edge and the fog and BBLE is the bandwidth
of the BLE, which is commonly 1 Mbps. For our epilepsy
detection system, the sampling frequency is 256 Hz and
we assume that each data sample is 4 Bytes. As a result,
the entire amount of data being transferred in one second
is 8192 bits, which is equal to 8.192 ms of latency. The
term BERF is bit error rate, which is the probability of
missing a bit being transmitted from the edge device to the
fog layer.
Energy: In this case, the total energy is:

(cid:2)

EEdge(E → F ) = EAC + EP P + EE→F,T X .

(5)

Compared to Eq. (2), the EF E and EM L are removed from
the computation energy of the edge, as they are performed
on the fog instead of the edge device. Besides the energy of
the edge sensors, the energy consumption of the fog device
should also be modeled, as it also has a limited source of
energy:

EFog(E → F ) = EF E + EM L + EE→F,RX .

(6)

To calculate the communication energy between the edge
and the fog, which is done using BLE, we have extracted
the values from Nordic DevZone power estimator [38],
with the following formulas:

EE→F,T X = IT X · LT X · VT X

= IT X · LE→F,T X · VT X ,

EE→F,RX = IRX · LRX · VRX

= IRX · LE→F,T X · VRX ,

(7)

(8)

where IT X and LT X are the average current and latency
of transmission and VT X is the voltage of transmission
between the edge and the fog. Similarly, IRX , LRX , and
VRX are the average current, latency, and voltage of the

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply. 

FOROOGHIFAR et al.: RESOURCE-AWARE DISTRIBUTED EPILEPSY MONITORING USING SELF-AWARENESS FROM EDGE TO CLOUD

1343

receiver in the fog device. The latency of the transmission
is obtained from Eq. (4).

C. Edge→Cloud Formulation

In this section, we model the scenario in which the edge
device communicates with the cloud and complex calculations
are performed by the cloud engine instead of the edge device.

(cid:2)

Latency: The total latency is composed of the computation
latency (Eq. (1)) and the communication latency between
edge and cloud, namely:

LEdge(E → C) = LAC + LP P

+ γC · (LF E + LM L) + LE→C,T X .
(9)

Similar to the fog layer the computation time is reduced on
the cloud engine and we have γC ≤ 1. We adopt the latency
model proposed in [43] and consider a fully-connected
network with full-duplex peer-to-peer global optical ﬁber
links among the data centers. Moreover, for a fast data
transfer, we use an all-bandwidth policy, with predeter-
mined reserved bandwidth for communication among each
two data centers. Therefore, it is sufﬁcient to consider the
source i and the destination data center j, in our analysis,
connected to the edge sensor and cloud, respectively. The
communication latency between the edge sensor and the
cloud engine is then, calculated as follows [43]:

LE→C,T X = V i,j
B

j
l

+ V i,j · (1 + BERC)
B

i,j
E

+ Di,j
Sl

.

(10)

The ﬁrst term correspond to the local latency of the desti-
nation data center, where V i,j is the volume of data being
j
transferred from i to j and B
l is the local bandwidth of
j. The second term captures the transmission latency of
i,j
the network, where B
E is the bandwidth reserved for
communication between source i and destination j. The
bit-error-rate is captured by BERC in the transmission
latency and is used to obtain the effective communication
bandwidth between the source and destination data centers.
Finally, the last term captures the propagation latency,
where Di,j is distance from i to j and Sl is the speed
of light.
Energy: In this case, the total energy is the energy con-
sumed for calculation on the edge device plus the energy
of communication with cloud (EE→C,T X ):

(cid:2)

EEdge(E → C) = EAC + EP P + EE→C,T X .

(11)

We consider LoRa [40] to communicate between the edge
device and the cloud engine. The transmission energy for
this protocol can be calculated as:

EE→C,T X = Epacket · Npacket

= Epacket · LenT X + LenH

Spacket

,

(12)

where Epacket and Npacket are the energy of transferring one
packet and the number of packets, respectively. The num-
ber of packets is calculated as the length of the transmitted
data (LenT X ) plus the header length (LenH ) of minimum
13 bytes divided by the size of each packet (Spacket).

D. Edge

Fog−−→Cloud Formulation

In this section, the formulas of the latency and energy in the
case of communication between the edge device and the cloud
engine through the fog layer are calculated.

(cid:2)

Latency: In case of latency, this communication is almost
equal to the sum of communication of the edge with the
fog and with the cloud (as the distance of the edge to the
fog is negligible compared to the distance with the cloud).
As a result, for the latency we have:

LEdge(E F−→ C) = LAC + LP P + γC · (LF E + LM L)

+ LE→F,T X + LE→C,T X ,

(13)

(cid:2)

where LE→F,T X and LE→C,T X are calculated as in Eq. (4)
and Eq. (10).
Energy: In this case, we ﬁrst transfer the data from the
edge to the fog and then from the fog to the cloud. As a
result, the wearable device is only involved with the ﬁrst
part of transmission to the fog and the energy consumed
for communication will be EE→F,T X and thus, the total
energy is calculated as follows:

EEdge(E F−→ C) = EAC + EP P + EE→F,T X ,

(14)

which is the same as Eq. (5). In this case, for the fog layer
we obtain:

EFog(E F−→ C) = EE→F,RX + EF →C.

(15)

V. SELF-AWARE DISTRIBUTION OF MACHINE
LEARNING ALGORITHM

In this section, we ﬁrst describe brieﬂy our self-aware energy
management technique. Then, we extend the response-time la-
tency and energy consumption models developed in Section IV
by introducing the notion of self-awareness in such systems.

A. Self-Aware Classiﬁcation Algorithm

To reduce the energy consumption without sacriﬁcing the
quality of the classiﬁcation, in our previous work [13], we pro-
posed a two-level self-aware classiﬁer. There, we have developed
a self-aware seizure detection technique where classiﬁcation
can be done with either a simple set of features or a more
complex set. In fact, the entire set of features are not used for
seizure detection unless conﬁdent classiﬁcation based on the
set of simple features is not possible. Then, we take advantage
of the multi-mode execution possibilities of the platform, in
a self-aware fashion, thus the energy consumption is reduced
while the quality of system remains in an acceptable level

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply. 

1344

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 6, DECEMBER 2019

Fig. 3. Test phase of the self-aware energy management proposed in [13].

for medical use. Moreover, our system is kept in an ultra-
low power (energy-saving) mode when tasks terminate their
execution.

Moreover, we extend this classiﬁcation algorithm to multiple
levels with several classiﬁers, with different detection perfor-
mances and energy consumptions. The system starts with the
simplest classiﬁer, namely, with the minimum energy consump-
tion and detection performance. If the result is not deemed
reliable, it invokes the next simplest classiﬁer and continues
this procedure until the decision is reliable. In this technique, to
reach the maximum energy saving, the system has to be aware
of the detection quality that it can provide in each level. To
achieve this, we adopt the self-awareness concept and introduce
the notion of conﬁdence to investigate whether the decision of
a classiﬁer is reliable.

Several previous studies consider efﬁcient implementation of
neural networks over resource-constrained edge IoT platforms
and embedded systems to improve energy efﬁciency [44]–[50].
On the other hand, our proposed technique in this article is
complementary to the solutions proposed for the implementation
of neural networks in [44]–[50], i.e., the previous techniques
can be adopted together with our proposed technique in this
article, demonstrating the generality of our proposed self-aware
solution.

The test phase in case of the two-level classiﬁer is shown in
Fig. 3, where the conﬁdence model, which is extracted in the
train phase, decides whether the simple model is conﬁdent to
classify the new data (Xts). If so, the classiﬁcation is done by
the simple classiﬁer (with the ﬁnal decision LabelS); otherwise,
the complex classiﬁcation is invoked (with the ﬁnal decision
LabelC ). Combining this technique with our distributed health
monitoring approach, as shown in Fig. 4, only in the case that
the complex classiﬁcation is required to ensure the reliability
of the decision, we ofﬂoad the complex computation on the
fog and cloud engines. We also consider a threshold for the
conﬁdence, which shows the minimum number of trees (out
of 100) in the random forest algorithm that should agree on
using the simple classiﬁer. By increasing this threshold, the
frequency of decisions that are made by the simple classiﬁer is
reduced, which leads to an increase in the overall classiﬁcation
performance. On the other hand, higher thresholds increase the
overall complexity and the energy consumption of the proposed
classiﬁcation algorithm.

Fig. 4. Task distribution scenario over edge, fog and cloud using the notion
of self-awareness and concept of conﬁdence.

B. Edge Formulation

(cid:2)

In this section, we consider the case when no communication
is done between the edge device and the fog and cloud engines.
Latency: As in our self-aware system, we consider several
levels of classiﬁcation. First, we calculate the latency of
each of these levels, as follows:

Li = LF E(i) + LM L(i),

i = 1, . . . , l,

(16)

where Li is the total latency of ith level and LF E(i) and
LM L(i) are the latencies of ith level feature extraction and
machine learning, respectively. The total number of levels
is equal to l.
Based on the probability of invoking the ith classiﬁer,
denoted by Pi, the total latency of computation on the edge
device for our wearable system is calculated as follows:

LSA(Edge) = LAC + LP P +

Pi · Li

l(cid:2)

i=1
⎛

⎞

+ LCF (1) +

l(cid:2)

⎝1 −

i−1(cid:2)

i=2

j=1

⎠ · LCF (i),

Pj

(17)

where LCF (i) is the latency of calculating ith level con-
ﬁdence. Then, second line of this equation indicates the
total latency of conﬁdence calculation. As demonstrated,
we always calculate the conﬁdence of ﬁrst layer and for the
next layers we just calculate the conﬁdence if a classiﬁer of
lower level is not chosen yet (the probability is calculated
as 1 −
Energy: Similar to the latency, we calculate the energy of
each level as follows:

j=1 Pj).

(cid:7)i−1

(cid:2)

Ei = EF E(i) + EM L(i),

i = 1, . . . , l,

(18)

where EF E(i) and EM L(i) are the energies of the ith
level feature extraction and machine learning, respectively.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply. 

FOROOGHIFAR et al.: RESOURCE-AWARE DISTRIBUTED EPILEPSY MONITORING USING SELF-AWARENESS FROM EDGE TO CLOUD

1345

Then, for the entire computation on the edge, we have:

ESA(Edge) = EAC + EP P +

l(cid:2)

⎛
i=1

Pi · Ei

⎞

+ ECF (1) +

l(cid:2)

⎝1 −

i−1(cid:2)

i=2

j=1

⎠ · ECF (i),

Pj

(19)

where ECF (i)
conﬁdence.

is the energy of calculating ith level

C. Edge→Fog Formulation

In this section, we consider the scenario when the edge sensor
communicates with the fog device and the complex calculations
are performed on the fog, instead of the edge sensor. This is done
when the system needs the classiﬁers with levels higher than
t − 1, which is selected according to the available resources, on
the edge sensor.

(cid:2)

Latency: The communication is done only when we need
classiﬁcation of levels equal or higher than t, which are the
energy-hungry tasks. According to Eq., (3) we have the
following latency for our self-aware system:

LSA(E → F ) = LAC + LP P +

t−1(cid:2)

i=1

Pi · Li

+

l(cid:2)

i=t

Pi · (LE→F,T X + γF · Li)

t−1(cid:2)

i=2

i−1(cid:2)

+ LCF (1) +

⎛

l(cid:2)

+

⎝1 −

i=t

j=1

⎞

⎠ · LCF (i)

Pj

⎛

⎝1 −

⎞

i−1(cid:2)

j=1

⎠ · γF · LCF (i),

Pj

(20)

where LE→F,T X is calculated as in Eq. (4).
The ﬁrst two terms in Eq. (20) are latencies of acquisition
and pre-processing steps for the entire signal. Then, the
latency of the levels of classiﬁcations that are performed on
the edge device is calculated, which is equal to multiplying
probability of each level with its latency. For level t and
higher we have the latency of transmission from the edge
device to the fog layer (LE→F,T X ) and also the latency of
computation multiplied by fog speed-up factor (γF ). The
third line of the equation corresponds to the conﬁdence
levels that are calculated on the edge device, and the last
line is the latency of calculating these conﬁdence levels in
the fog device.
Energy: Similar to the latency, according to Eq. (5), we
obtain:

(cid:2)

ESA(E → F ) = EAC + EP P +

t−1(cid:2)

i=1

Pi · Ei

+

l(cid:2)

i=t

Pi · EE→F,T X

+ ECF (1) +

t−1(cid:2)

⎛

⎝1 −

i−1(cid:2)

i=2

j=1

⎞

⎠· ECF (i),

Pj

(21)

where EE→F,T X is calculated as in Eq. (7).
Here, the ﬁrst two terms are acquisition and preprocessing
energy of the entire signal and then we have energy of
classiﬁcations, which are done on the edge device. In the
second line we calculate transmission energy for the level
t and higher and in the last line the energy of calculating
conﬁdence of levels lower than t is considered.

D. Edge→Cloud Formulation

In this section, the edge communicates with the cloud in
case of classiﬁcation of layers t and higher and energy-hungry
calculations are performed by the cloud engine instead of the
edge sensors.

(cid:2)

Latency: According to Eq. (9), we have the following
latency:

LSA(E → C) = LAC + LP P +

t−1(cid:2)

i=1

Pi · Li

+

l(cid:2)

i=t

Pi · (LE→C,T X + γC · Li)

+ LCF (1) +

t−1(cid:2)

⎛

⎝1 −

i−1(cid:2)

i=2

j=1

⎞

⎠· LCF (i),

Pj

⎛

⎞

l(cid:2)

+

⎝1 −

i−1(cid:2)

i=t

j=1

⎠ · γC · LCF (i),

Pj

(22)

where LE→C,T X is calculated as in Eq. (10), taking into
account the limitation of the communication protocol to
obtain the effective bandwidth. The terms are deﬁned in
the same order as Eq. (20).
Energy: According to Eq. (11), we have the following
energy:

(cid:2)

ESA(E → C) = EAC + EP P +

t−1(cid:2)

i=1

Pi · Ei

+

l(cid:2)

i=t

Pi · EE→C,T X

+ ECF (1) +

t−1(cid:2)

⎛

⎝1 −

i−1(cid:2)

i=2

j=1

⎞

⎠· ECF (i),

Pj

(23)

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply. 

1346

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 6, DECEMBER 2019

where EE→C,T X is calculated as in Eq. (12). The terms
are deﬁned with the same order as Eq. (21).

E. Edge

Fog−−→Cloud Formulation

In this section, the formulas of latency and energy in case of
communication between the edge sensor and the cloud engine
through fog layer are calculated.

(cid:2)

Latency: According to Eq. (13), we have the following
latency:

LSA(E F−→ C) = LAC + LP P +

t1−1(cid:2)

i=1

Pi · Li

+

+

t2−1(cid:2)

i=t1

l(cid:2)

i=t2

Pi · (LE→F,T X + γF · Li)

Pi · (LE→F,T X

+ LE→C,T X + γC · Li)

⎛

⎞

+ LCF (1) +

t1−1(cid:2)

⎝1 −

i−1(cid:2)

j=1

⎠ · LCF (i)

Pj

Fig. 5. Dataset information including (a) total number of hours for different
patients, (b) number of seizures for different patients, and (c) duration of seizures
for different patients in seconds.

VI. EXPERIMENTAL SETUP

In this section, we discuss the experimental setup for the
evaluation of our proposed technique in terms of latency, energy
consumption, and classiﬁcation performance. We consider the
epileptic seizure detection problem, a real-world problem, as our
case study.

⎞

⎠ · γF · LCF (i)

Pj

⎞

⎛

⎝1 −

⎛

⎝1 −

i=2

i−1(cid:2)

j=1

i−1(cid:2)

j=1

+

+

t2−1(cid:2)

i=t1

l(cid:2)

i=t2

⎠ · γC · LCF (i).

Pj

A. Datasets

(24)

Here, we assume that ﬁrst t1 − 1 levels of classiﬁcation
are done on the edge device, then from classiﬁcation t1 to
t2 − 1 are performed on the fog layer, and the rest of the
levels are calculated on the cloud engine. This formulation
results in adding two more terms compared to Eq. (22),
which correspond to the latency of classiﬁers on the fog
layer (second line) as well as the latency of conﬁdence
calculation on the fog layer (5th line).
Energy: According to Eq. (14), we have the following
energy:

(cid:2)

ESA(E F−→ C) = EAC + EP P +

t1−1(cid:2)

i=1

Pi · Ei

+

l(cid:2)

i=t1

Pi · EE→F,T X

+ ECF (1) +

t1−1(cid:2)

⎛

⎝1 −

i−1(cid:2)

i=2

j=1

⎞

⎠ · LCF (i).

Pj

(25)

The proposed distributed epilepsy monitoring approach is
evaluated with the EPILEPSIAE dataset [15], which is the
largest epilepsy dataset manually annotated by doctors for
seizure detection and prediction worldwide and enables us to
rigorously evaluate our proposed methodology. This dataset con-
sists of one-lead ECG and 19-channel EEG data. The recordings
are made in a routine clinical environment, so nonseizure activity
and artifacts such as head/body movement, chewing, blinking,
early stages of sleep, and electrode pops/movement are present.
No constraints regarding the types of seizure are imposed; the
dataset contains complex partial (CP), simple partial (SP), and
secondarily generalized seizures (GS) [51].

We have used the ECG data of 30 patients with 4603 hours of
recordings separated to one-hour ﬁles containing 277 seizures.
The data is acquired at a sampling rate of 256 Hz with 16-bit
resolution. The number of seizures among different patients
differs from 5 to 23 seizures per patient with an average of 9.23
seizures per patient. The average duration of these seizures is
75.81 seconds. The total recording duration per patient differs
from 92.90 to 266.36 hours, with an average of 153.43 hours.
The details of this dataset is also presented in Fig. 5.

B. Performance Metrics

The terms are deﬁned with the same order as Eq. (21).

As the Fig. 5 shows, the seizures are not distributed evenly
among the patients. As a result, in order to have a reliable analysis

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply. 

FOROOGHIFAR et al.: RESOURCE-AWARE DISTRIBUTED EPILEPSY MONITORING USING SELF-AWARENESS FROM EDGE TO CLOUD

1347

TABLE II
SUMMARIZING THE ENERGY CONSUMPTION OF BOTH COMPUTATION AND COMMUNICATION IN DIFFERENT SCENARIOS PLUS THE DETECTION PERFORMANCE OF
THE SYSTEM WITH AND WITHOUT SELF-AWARENESS. THE ENERGIES ARE NORMALIZED WITH RESPECT TO THE INYU BATTERY POWER (710 mAh)

Fig. 6. Experimental setup including: (a) the INYU hardware board and
platform and (b) the INYU touch and thoracic sensors.

of the detection system for different modes of classiﬁcation, in
each iteration of testing the system 70% of the data is randomly
picked as the training data and the rest is picked as the test
data. The performance of the proposed algorithm is evaluated
by measuring the speciﬁcity (Spec), sensitivity (Sen), and the
geometric mean (Gmean), which are deﬁned as follows:

Spec =

Sen =

Gmean =

,

T N
F P + T N
T P
T P + F N
(cid:8)
Spec · Sen,

,

(26)

(27)

(28)

(cid:2)

(cid:2)

where F P , T N , T P and F N deﬁnitions are the following ones:
False positive (F P ): The patient is in the inter-ictal state,
but the sample is classiﬁed as ictal.
True negative (T N ): The patient is in the inter-ictal state,
and the algorithm declared this situation.
True positive (T P ): The patient is in the ictal state, and the
algorithm detected this state.
False negative (F N ): The patient is in the ictal state, and
the sample is not classiﬁed correctly.

(cid:2)

(cid:2)

The geometric mean Gmean is adopted since its high values
reﬂect that both speciﬁcity (Spec) and sensitivity (Sen) are
high, which is equal to high quality detection. Conversely, if the
geometric mean Gmean is low, then Spec, Sen, or both are low,
which is undesirable. Finally, we include the geometric mean,
as it is the only correct average of normalized measurements,
according to [52].

C. Implementation Platform

The target hardware platform for our system is the SmartCar-
dia INYU wearable sensor [14], which is consistent with the
standard signal acquisition equipment in hospitals, to evaluate
the complexity of proposed solution and battery lifetime of the
device. This is done by porting the entire machine-learning
algorithms on the INYU device, which includes an ARM Cortex-
M3 chipset (STM32L151RDT6) [53] as its processor for data
analysis and classiﬁcation, which is a low-power 32-bit micro-
controller with 48 kB RAM and 384 kB ﬂash storage and the
maximum frequency of 32 MHz. This processor has several
power-management modes, including active and sleep modes,
with the possibility of dynamically switching between different
modes. The INYU device is powered by a 710 mAh battery,
which is used as reference to calculate the relative energies in Ta-
ble II. The ECG signal acquisition is done using silver-chloride
electrodes for impedance pneumography [54]. The analog-to-
digital converter (ADC) is the ADS7142 module [55], which is
an event-driven ADC. This ADC has a low power consumption
of 900 nW and works with 0.5 uA current.

VII. EXPERIMENTAL RESULTS

In this section, we evaluate the efﬁciency of our proposed
distributed epilepsy monitoring system, in terms of latency,
energy consumption, and classiﬁcation performance. For sim-
plicity’s sake we assume that γF = γC = 1 and BER = 0. We
consider the maximum distance of two points on the earth for
the Di,j in cloud communication formulation. Moreover, our
detection system consists of two classiﬁcation levels (l = 2) and
the simpler level is always performed on the edge device (t = 2).
Table II shows the energy consumption of two different sce-
narios considering both self-aware system with different conﬁ-
dence thresholds and the system without self-awareness. These
two scenarios are ﬁrst, computing completely on the edge device
and second, communicating with the fog level. The energies are
normalized with respect to the INYU battery power (710 mAh)
in this table and also in Table III. The results show that the
energy reduction of 13–21% (13%, 21%, 19%, 17%, 15%) is
achieved by adopting distributed epilepsy monitoring techniques

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply. 

1348

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 6, DECEMBER 2019

TABLE III
SUMMARIZING THE TRADE-OFFS BETWEEN DIFFERENT MODES OF SYSTEM
WITH AND WITHOUT SELF-AWARE ENERGY MANAGEMENT (VALUES ARE FOR
60 SECONDS OF DATA ACQUISITION AND ANALYSIS). THE ENERGIES ARE
NORMALIZED WITH RESPECT TO THE INYU BATTERY POWER (710 mAh)

that exploit the heterogeneous computing and communication
infrastructure. Also, in both scenarios, by using self-awareness,
the energy is reduced by 81–49% compared to using the complex
classiﬁer all the time. This table also contains detection perfor-
mance of the system with and without self-awareness, which
shows that the reduction in the geometric mean due to adopting
self-awareness in the system is only 1.22% to 4.58%, when the
conﬁdence threshold is reduced from 90% to 60%. As a result,
combining the notion of self-awareness with distributed epilepsy
monitoring results in signiﬁcant improvements in battery life-
time with negligible reduction in performance.
Table III summarizes the performance,

latency, and en-
ergy consumption of different design solutions. Among these
solutions, the most energy-efﬁcient choice is to ofﬂoad the
computationally-complex tasks to the fog. This solution reduces
the energy consumption substantially with only a negligible
communication latency overhead. The energy overhead of com-
munication with the cloud engine through the fog is the same as
communication of the wearable device with the fog. However,
as the communication with the cloud is done using WiFi, the la-
tency increases about 1.213 seconds for each 60-second window.
Therefore, this solution is not efﬁcient in terms of end-to-end
latency.

We summarize this discussion for our epileptic seizure detec-

tion system in the following:

(cid:2)

(cid:2)

(cid:2)

The communication with the fog requires the lowest energy
(3.65 mJ) and the latency overhead is only approximately
10.4% of the entire end-to-end latency. Therefore, we
transfer the data to the fog layer via BLE and receive back
the outcome of the complex classiﬁcation performed on
the fog device, which improves the overall performance.
In the case that the fog device is not available, either
because of poor Bluetooth connection or because the fog
device is out of charge, the application is executed on the
edge device. In this case, we can decrease the conﬁdence
threshold so that the complex classiﬁer is invoked less
frequently. This, of course, depends also on the criticality
of the situation.
In our case study, the communication with the cloud en-
gines via LoRa protocol is only used to notify the hospital in
case of emergency for rescue, due to the limited bandwidth
and the major energy overhead of transmission via this

protocol. Thus, we do not use this protocol to transmit the
ECG signal to the cloud engines.

Although in our epilepsy detection system, the distribution
of tasks over edge and fog provides us with the best trade-
off among the performance, latency, and energy, this result
cannot be extended to all other biomedical applications. That
is, based on the volume of data that is processed (data in-
tensive) and the complexity of computation that is performed
by the system (computation intensive), other scenarios can be
shown to provide the best outcome among the four possible
options.

Let us now consider four possible scenarios. The ﬁrst scenario
belongs to the category of applications that are handled by
the edge device. These are applications with a computation
load within the edge energy budget, i.e., executing these ap-
plications on the edge sensors is more energy/latency efﬁcient
than transferring the data to the fog/cloud layer to perform the
computation on the fog/cloud layer. On the other hand, the
second scenario, in which the tasks are distributed to the fog
device, is favorable if transferring the data to the fog layer is
more energy-efﬁcient compared to the computation over the
edge sensor. Then, we have the third scenario in which the fog
layer is used as a gateway to the cloud, which is suitable for the
very high-complexity algorithms that can only be executed on
the cloud engines. The third and second scenarios are the same
in terms of edge-sensor energy efﬁciency, while the end-to-end
latency depends on the computational complexity of tasks to
be performed and the volume of data to be transferred to the
fog/cloud. Finally, in the fourth scenario, the edge sensor di-
rectly communicates with the cloud engines via LoRa protocol,
which is limited in terms of bandwidth and has huge energy
overheads, hence relevant for informing the hospitals in case of
emergencies.

Let us consider two other applications, which belong to
different scenarios than our case study of the epileptic seizure
detection system. The ﬁrst case study is the obstructive sleep ap-
nea monitoring system proposed in [28]. In this application, the
system operates more efﬁciently locally on the edge sensor, i.e.,
the ﬁrst discussed scenario, mainly due to the highly optimized
and lightweight algorithms adopted.

The second application is training an epileptic seizure detec-
tion classiﬁer, using the data from several patients. Note that the
training phase of machine-learning algorithms often involves
solving complex optimization problems, which is substantially
more complicated when compared to the inference phase. In
such applications, the computational complexity involved in
training a state-of-the-art classiﬁer often is beyond the capacity
of the edge and fog devices. Therefore, such complex training
algorithms need to be performed on the cloud engines, based on
the data transferred to the cloud from the edge sensors.

Finally, considering the very limited bandwidth and huge
energy consumption of LoRa/Sigfox, we believe that the case of
direct communication between the edge sensors and the cloud
engines is the most useful in reliably notifying the emergency
units in case of life-threatening events such as epileptic seizures,
as the fog devices (e.g., mobile phone) might be out of reach and
unavailable.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply. 

FOROOGHIFAR et al.: RESOURCE-AWARE DISTRIBUTED EPILEPSY MONITORING USING SELF-AWARENESS FROM EDGE TO CLOUD

1349

VIII. CONCLUSION

In this article, we have proposed a methodology to distribute
the complex and energy consuming machine-learning computa-
tions to the fogs/clouds, based on the notion of self-awareness
that takes into account the complexity and reliability of the
algorithm. We have also analyzed the trade-offs in terms of
energy consumption, latency, and performance of different In-
ternet of Things (IoT) solutions. Then, we have considered the
epileptic seizure detection problem, as our real-world case study,
to demonstrate the importance of our proposed resource-aware
distributed health monitoring methodology. Overall, analyzing
different scenarios with and without self-awareness shows that
using distributed epilepsy monitoring can result in 13–21%
energy reduction while self-awareness can reduce the energy
by 49–81%. This is while the detection performance is only
reduced by 1.22–4.58% making the advantage of distributed
health monitoring and self-awareness more than its overhead.

REFERENCES

[1] G. Surrel, A. Aminifar, F. Rincon, S. Murali, and D. Atienza, “Online
obstructive sleep apnea detection on wearable devices,” IEEE Trans.
Biomed. Circuits Syst., vol. 12, no. 4, pp. 762–773, Aug. 2018.

[2] D. Sopic, A. Aminifar, A. Aminifar, and D. Atienza, “Real-time event-
driven classiﬁcation technique for early detection and prevention of my-
ocardial infarction on wearable systems,” IEEE Trans. Biomed. Circuits
Syst., vol. 12, no. 5, pp. 982–992, Oct. 2018.

[3] H. Jung, “Cisco visual networking index: Global mobile data trafﬁc
forecast update 2010–2015,” Cisco Systems Inc, San Jose, CA, USA,
2011.
[Online]. Available: https://www.cisco.com/c/en/us/solutions/
collateral/service-provider/visual-networking-index-vni/white-paper-
c11-738429.html. Accessed on: Oct. 2018.

[4] H. Sun, Z. Zhang, R. Q. Hu, and Y. Qian, “Wearable communications in
5 G: Challenges and enabling technologies,” IEEE Veh. Technol. Mag.,
vol. 13, no. 3, pp. 100–109, Sep. 2018.

[5] P. R. Lewis, M. Platzner, B. Rinner, J. Tørresen, and X. Yao, Self-Aware

Computing Systems. Berlin, Germany: Springer, 2016.

[6] P. R. Lewis et al., “A survey of self-awareness and its application in com-
puting systems,” in Proc. 5th IEEE Conf. Self-Adaptive Self-Organizing
Syst. Workshops, 2011, pp. 102–107.

[7] World Health Organization, “Epilepsy,” 2016. [Online]. Available: http:

//www.who.int/mental_health/neurology/epilepsy/en/index.html

[8] D. J. Thurman, D. C. Hesdorffer, and J. A. French, “Sudden unexpected
death in epilepsy: Assessing the public health burden,” Epilepsia, vol. 55,
no. 10, pp. 1479–1485, 2014.

[9] S. Shorvon and T. Tomson, “Sudden unexpected death in epilepsy,” Lancet,

vol. 378, no. 9808, pp. 2028–2038, 2011.

[10] A. Van de Vel et al., “Non-EEG seizure detection systems and potential
sudep prevention: State of the art: Review and update,” Seizure, vol. 41,
pp. 141–153, 2016.

[11] C. Hoppe, M. Feldmann, B. Blachut, R. Surges, C. E. Elger, and C. Helm-
staedter, “Novel techniques for automated seizure registration: Patients’
wants and needs,” Epilepsy Behav., vol. 52, pp. 1–7, 2015.

[12] F. Forooghifar et al., “A self-aware epilepsy monitoring system for real-
time epileptic seizure detection,” in Proc. ACM/Springer Mobile Netw.
Appl., 2019, pp. 1–14.

[13] F. Forooghifar, A. Aminifar, and D. Atienza, “Self-aware wearable systems
in epileptic seizure detection,” in Proc. Euromicro Conf. Digit. Syst. Des.,
2018, pp. 426–432.

[14] S. Murali, F. Rincon, and D. Atienza, “A wearable device for physical
and emotional health monitoring,” in Proc. Comput. Cardiol. Conf., 2015,
pp. 121–124.

[15] M. Ihle et al., “Epilepsiae–a european epilepsy database,” Comput. Meth-

ods Programs Biomed., vol. 106, no. 3, pp. 127–138, 2012.

[16] M. Hassanalieragh et al., “Health monitoring and management using
Internet-of-Things (IoT) sensing with cloud-based processing: Oppor-
tunities and challenges,” in Proc. IEEE Int. Conf. Serv. Comput., 2015,
pp. 285–292.

[17] B. Xu, L. Xu, H. Cai, L. Jiang, Y. Luo, and Y. Gu, “The design of
an m-health monitoring system based on a cloud computing platform,”
Enterprise Inf. Syst., vol. 11, no. 1, pp. 17–36, 2017.

[18] M. S. Hossain and G. Muhammad, “Cloud-assisted industrial Internet of
Things (IIoT)–enabled framework for health monitoring,” Comput. Netw.,
vol. 101, pp. 192–202, 2016.

[19] M. Elhoseny, A. Abdelaziz, A. S. Salama, A. M. Riad, K. Muhammad,
and A. K. Sangaiah, “A hybrid model of Internet of Things and cloud
computing to manage big data in health services applications,” Future
Gener. Comput. Syst., vol. 86, pp. 1383–1394, 2018.

[20] T. N. Gia, M. Jiang, A.-M. Rahmani, T. Westerlund, P. Liljeberg, and
H. Tenhunen, “Fog computing in healthcare Internet of Things: A case
study on ECG feature extraction,” in Proc. IEEE Int. Conf. Comput.
Inf. Technol.; Ubiquitous Comput. Commun.; Dependable, Auton. Secure
Comput.; Pervasive Intell. Comput., 2015, pp. 356–363.

[21] I. Azimi, J. Takalo-Mattila, A. Anzanpour, A. M. Rahmani, J.-P. Soininen,
and P. Liljeberg, “Empowering healthcare IoT systems with hierarchical
edge-based deep learning,” in Proc. IEEE/ACM Int. Conf. Connected
Health, Appl., Syst. Eng. Technol., 2018, pp. 63–68.

[22] A. Page, M. Hassanalieragh, T. Soyata, M. K. Aktas, B. Kantarci, and
S. Andreescu, “Conceptualizing a real-time remote cardiac health moni-
toring system,” in Medical Imaging: Concepts, Methodologies, Tools, and
Applications. Hershey, PA, USA: IGI Global, 2017, pp. 160–193.
[23] J. Mohammed, C.-H. Lung, A. Ocneanu, A. Thakral, C. Jones, and A.
Adler, “Internet of Things: Remote patient monitoring using web ser-
vices and cloud computing,” in Proc. IEEE Int. Conf. Internet Things,
IEEE Green Comput. Commun. IEEE Cyber, Phys. Social Comput., 2014,
pp. 256–263.

[24] J. H. Abawajy and M. M. Hassan, “Federated Internet of Things and cloud
computing pervasive patient health monitoring system,” IEEE Commun.
Mag., vol. 55, no. 1, pp. 48–53, Jan. 2017.

[25] H. Kolamunna et al., “Are wearable devices ready for https? Measuring
the cost of secure communication protocols on wearable devices,” 2016,
arXiv:1608.04180.

[26] C. Ragona, F. Granelli, C. Fiandrino, D. Kliazovich, and P. Bouvry,
“Energy-efﬁcient computation ofﬂoading for wearable devices and smart-
phones in mobile cloud computing,” in Proc. IEEE Global Commun. Conf.,
2015, pp. 1–6.

[27] S. Shahhosseini et al., “Dynamic computation migration at the edge:
Is there an optimal choice?” in Proc. Great Lakes Symp. VLSI, 2019,
pp. 519–524.

[28] G. Surrel, T. Teijeiro, M. Chevrier, A. Aminifar, and D. Atienza,
“Event-triggered sensing for high-quality and low-power cardiovas-
cular monitoring systems,” in Proc.
IEEE Des. Test, 2019, doi:
10.1109/MDAT.2019.2951126.

[29] J. S. Preden, K. Tammemäe, A. Jantsch, M. Leier, A. Riid, and E. Calis,
“The beneﬁts of self-awareness and attention in fog and mist computing,”
Computer, vol. 48, no. 7, pp. 37–45, 2015.

[30] N. Dutt, A. Jantsch, and S. Sarma, “Toward smart embedded systems:
A self-aware system-on-chip (soc) perspective,” ACM Trans. Embedded
Comput. Syst., vol. 15, no. 2, pp. 22-1–22-27, 2016.

[31] N. Taherinejad,

“Wearable medical

self-aware solutions,” IEEE life Sci., 2019.
https://lifesciences.ieee.org/lifesciences-newsletter/2019/april-2019/
wearable-medical-devices-challenges-and-self-aware-solutions/

devices: Challenges

and
[Online]. Available:

[32] A. Aminifar, Analysis, Design, and Optimization of Embedded Control
Systems. Linköping, Sweden: Linköping University Electronic Press,
2016.

[33] K. Tammemäe, A. Jantsch, A. Kuusik, J.-S. Preden, and E. Õunapuu, “Self-
aware fog computing in private and secure spheres,” in Fog Computing in
the Internet of Things. Berlin, Germany: Springer, 2018, pp. 71–99.
[34] A. Anzanpour et al., “Self-awareness in remote health monitoring systems
using wearable electronics,” in Proc. Conf. Des., Autom. Test Europe, 2017,
pp. 1056–1061.

[35] N. TaheriNejad, A. Jantsch, and D. Pollreisz, “Comprehensive observation
and its role in self-awareness; an emotion recognition system example,”
Self, vol. 11, pp. 117–124, 2016.

[36] D. Pascual, A. Aminifar, and D. Atienza, “A self-learning methodology
for epileptic seizure detection with minimally-supervised edge labeling,”
in Proc. Des., Autom. Test Europe Conf. Exhib., 2019, pp. 764–769.
[37] C. Gomez, J. Oller, and J. Paradells, “Overview and evaluation of blue-
tooth low energy: An emerging low-power wireless technology,” Sensors,
vol. 12, no. 9, pp. 11734–11753, 2012.

[38] N. Semiconductor, “Online power proﬁler,” 2019. [Online]. Available:

https://devzone.nordicsemi.com/power/

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply. 

1350

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 13, NO. 6, DECEMBER 2019

[39] S. Support, “Sigfox documentation,” 2019. [Online]. Available: https://

support.sigfox.com/docs

[40] The things network, “Lorawan overview,” 2019. [Online]. Available: https:

//www.thethingsnetwork.org/docs/lorawan/

[41] NetSpot, “Wiﬁ standards in a nutshell,” 2019. [Online]. Available: https:

//www.netspotapp.com/explaining-wiﬁ-standards.html

[42] A. Pullini, D. Rossi, I. Loi, G. Tagliavini, and L. Benini, “Mr. wolf:
An energy-precision scalable parallel ultra low power soc for IoT edge
processing,” IEEE J. Solid-State Circuits, vol. 54, no. 7, pp. 1970–1981,
Jul. 2019.

[43] A. Pahlevan, “Multi-objective system-level management of green cloud

data centers,” EPFL, 2019.

[44] A. Garofalo, M. Rusci, F. Conti, D. Rossi, and L. Benini, “PULP-NN:
Accelerating quantized neural networks on parallel ultra-low-power RISC-
V processors,” 2019, arXiv:1908.11263.

[45] Y. Zhang, Y. Guo, P. Yang, W. Chen, and B. Lo, “Epilepsy seizure
prediction on eeg using common spatial pattern and convolutional neural
network,” IEEE J. Biomed. Health Inform., 2019.

[46] D. Ravì et al., “Deep learning for health informatics,” IEEE J. Biomed.

Health Inform., vol. 21, no. 1, pp. 4–21, Jan. 2017.

[47] D. Ravi, C. Wong, B. Lo, and G.-Z. Yang, “A deep learning approach to
on-node sensor data analytics for mobile or wearable devices,” IEEE J.
Biomed. Health Inform., vol. 21, no. 1, pp. 56–64, Jan. 2017.

[48] A. Jafari, A. Ganesan, C. S. K. Thalisetty, V. Sivasubramanian, T. Oates,
and T. Mohsenin, “Sensornet: A scalable and low-power deep convolu-
tional neural network for multimodal data classiﬁcation,” IEEE Trans.
Circuits Syst. I, Reg. Papers, vol. 66, no. 1, pp. 274–287, Jan. 2019.
[49] D. Biswas et al., “Cornet: Deep learning framework for PPG-based
heart rate estimation and biometric identiﬁcation in ambulant environ-
ment,” IEEE Trans. Biomed. Circuits Syst., vol. 13, no. 2, pp. 282–291,
Apr. 2019.

[50] H. Li, K. Ota, and M. Dong, “Learning IoT in edge: Deep learning for
the Internet of Things with edge computing,” IEEE Netw., vol. 32, no. 1,
pp. 96–101, Jan./Feb. 2018.

[51] M. Qaraqe, M. Ismail, E. Serpedin, and H. Zulﬁ, “Epileptic seizure onset
detection based on EEG and ECG data fusion,” Epilepsy Behav., vol. 58,
pp. 48–60, 2016.

[52] P. J. Fleming and J. J. Wallace, “How not to lie with statistics: The correct
way to summarize benchmark results,” Commun. ACM, vol. 29, no. 3,
pp. 218–221, 1986.

[53] STM32L151RD, Ultra-low-power ARM Cortex-M3 MCU with 384
Kbytes Flash, 32 MHz CPU, USB, 3xOp-amp - STMicroelectronics, Oct.
2017.

[54] ECG Electrode for Sensitive Skin, Ambu BlueSensor VLC, 2015.
[55] T. Instruments, “Ads7142,” 2018. [Online]. Available: http://www.ti.com/

product/ADS7142/description

Amir Aminifar received the Ph.D. degree from
the Swedish National Computer Science Graduate
School, Linköping University, Linköping, Sweden,
in 2016. During 2014–2015, he visited the Cyber-
Physical Systems Laboratory of the University of
California, Los Angeles, USA, and the Real-Time
Systems Laboratory of Scuola Superiore Sant’Anna,
Italy. He is currently a Research Scientist with the
Embedded Systems Laboratory of the Swiss Fed-
eral Institute of Technology Lausanne, Lausanne,
Switzerland. His current research interests are cen-
tered around mobile health technologies and medical informatics for reliable
detection and prediction of pathological health conditions.

David Atienza (M’05–SM’13–F’16) received the
Ph.D. degree in computer science and engineering
from Complutense University of Madrid, Madrid,
Spain, and IMEC, Leuven, Belgium,
in 2005.
He is an Associate Professor of electrical and
computer engineering, and the Director of the Em-
bedded Systems Laboratory with the Swiss Fed-
eral Institute of Technology Lausanne, Lausanne,
Switzerland. His research interests include system-
level design and thermal-aware optimization method-
ologies for 2D/3D high-performance multi-processor
system-on-chip (MPSoC) and ultra-low power system architectures for wireless
body sensor nodes. He is a co-author of more than 250 papers in peer-reviewed
international journals and conferences, several book chapters, and seven patents.
He was the recipient of the DAC Under-40 Innovators Award in 2018, IEEE
TCCPS Mid-Career Award in 2018, an ERC Consolidator Grant in 2016, the
IEEE CEDA Early Career Award in 2013, the ACM SIGDA Outstanding New
Faculty Award in 2012, and a Faculty Award from Sun Labs at Oracle in 2011.
He was DATE 2015 Program Chair and DATE 2017 General Chair. He is an
ACM Distinguished Member.

Farnaz Forooghifar received the B.Sc. and M.Sc.
degrees in electrical engineering from the University
of Tehran, Tehran, Iran, in 2014 and 2017, respec-
tively. She is a Ph.D. Researcher in the Embedded
Systems Laboratory with the Swiss Federal Institute
of Technology Lausanne, Lausanne, Switzerland. Her
research interests include real-time health monitor-
ing systems, embedded systems design, approximate
computing, and parallel processing.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:48 UTC from IEEE Xplore.  Restrictions apply.
