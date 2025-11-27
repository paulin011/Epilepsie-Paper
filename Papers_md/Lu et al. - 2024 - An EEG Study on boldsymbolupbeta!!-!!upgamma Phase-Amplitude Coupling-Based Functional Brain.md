# Lu et al. - 2024 - An EEG Study on boldsymbolupbeta!!-!!upgamma Phase-Amplitude Coupling-Based Functional Brain

3446

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 28, NO. 6, JUNE 2024

An EEG Study on β−γ Phase-Amplitude
Coupling-Based Functional Brain Network in
Epilepsy Patients

Junfeng Lu , Anyu Li

, Kaijie Li

, Renping Yu , Yuxia Hu , Rui Zhang , Lipeng Zhang ,

Hong Wan , and Mingming Chen

Abstract—Epilepsy, a chronic neuropsychiatric brain dis-
order characterized with recurrent seizures, is closely as-
sociated with abnormal neural communications within the
brain. Despite that the phase-amplitude coupling (PAC) has
been suggested to offer a new way to observe neural in-
teractions during epilepsy, however, few studies pay atten-
tion to alterations of the epileptic functional brain network
based on PAC, especially on the β−γ PAC. Therefore, we
use scalp electroencephalography (EEG) data of epileptic
patients and the β−γ PAC modulation index (MI) to con-
struct functional brain networks to examine variations of
neural interactions during different epileptic phases. Statis-
tically, the ﬁndings show that between-channel MI values in
the post-ictal period signiﬁcantly increase compared to that
in the pre-ictal period, and the between-channel MI value
has a close association with the information of phase and
amplitude provided by the channels. Importantly, in both
the phase-amplitude and amplitude-phase functional brain
networks, the average node degree is remarkably higher
in the post-ictal period than that in the pre-ictal period,
whereas the characteristic path length in the ictal and post-
ictal periods is signiﬁcantly lower than that in the pre-ictal
period. Besides, the average betweenness centrality in the
post-ictal period is remarkably higher than that in the ic-
tal period. Interestingly, the positive correlations between
within-channel MI values and between-channel MI values
can be observed during the pre-ictal, ictal and post-ictal
periods. These ﬁndings suggest that the β−γ PAC-based
functional brain network may provide a novel perspective

Manuscript received 17 July 2023; revised 15 December 2023 and
8 March 2024; accepted 14 March 2024. Date of publication 20 March
2024; date of current version 6 June 2024. This work was supported
in part by the National Natural Science Foundation of China under
Grant 62173310, in part by the MOST 2030 Brain Project under Grant
2022ZD0208500, and in part by the Technology Project of Henan
Province under Grant 222102310031. (Corresponding authors: Hong
Wan; Mingming Chen.)

Junfeng Lu, Anyu Li, Kaijie Li, Yuxia Hu, Lipeng Zhang, and Hong
Wan are with the Henan Key Laboratory of Brain Science and Brain-
Computer Interface Technology, School of Electrical and Information
Engineering, Zhengzhou University, Zhengzhou 450001, China (e-mail:
wanhong@zzu.edu.cn).

Renping Yu, Rui Zhang, and Mingming Chen are with the Henan Key
Laboratory of Brain Science and Brain-Computer Interface Technology,
School of Electrical and Information Engineering, Zhengzhou Univer-
sity, Zhengzhou 450001, China, and also with the Research Center for
Intelligent Science and Engineering Technology of Traditional Chinese
Medicine, School of Electrical and Information Engineering, Zhengzhou
University, Zhengzhou 450001, China (e-mail: mmchen@zzu.edu.cn).

This article has supplementary downloadable material available at

https://doi.org/10.1109/JBHI.2024.3379194, provided by the authors.

Digital Object Identiﬁer 10.1109/JBHI.2024.3379194

to understanding alterations of neural interactions during
the epileptic evolution, and may contribute to effectively
controlling the spread of epileptic seizures.

Index Terms—Epilepsy, phase-amplitude

coupling,

modulation index, functional brain network.

I. INTRODUCTION

E PILEPSY is a chronic neurological brain disease, and is

closely related to abnormal neural oscillations observed
on electroencephalography (EEG) [1]. Epileptic seizures are
recurrent and uncertain, usually leading to damage to the central
nervous system of patients and seriously affecting their physical
and mental health [2]. Although the level of epilepsy treatment
has greatly improved, about 30% of epilepsy patients world-
wide still develop into intractable epilepsy due to insensitivity
to antiepileptic drugs [3]. Moreover, the diversity of epilepto-
genic factors and the complexity of alterative neural interac-
tions within the brain seriously hinder the effective treatment
of intractable epilepsy [4]. Therefore, uncovering alterations
of neural interactions during different epileptic phases may
contribute to understanding transitions between non-ictal and
ictal states, as well as mechanisms underlying the genesis of
epilepsy.

Recently, growing evidence has suggested that epilepsy is
a complex brain network disease, which is tightly associated
with aberrant interactions between different brain regions [5],
[6], [7]. Indeed, epileptic functional brain networks have been
demonstrated to play crucial roles in localizing epileptogenic fo-
cus and understanding mechanisms of epilepsy transmission and
controllability [8], [9], [10]. Of note, most of previous studies are
often based on the phase information of epileptic EEG signals,
using the phase locked value (PLV) and phase lag index (PLI)
methods to construct epileptic functional brain networks [11],
[12]. In contrast, due to the volume conduction and nonlinearity
of EEG signals, few studies utilize the amplitude information-
related correlation to construct functional brain networks [13].
However, it should be pointed out that both the phase and
amplitude information of epileptic EEG signals have signiﬁcant
impacts on the construction of functional brain networks. Hence,
to closely observe variations of functional brain networks, it is

2168-2194 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:42 UTC from IEEE Xplore.  Restrictions apply. 

LU et al.: EEG STUDY ON β−γ PHASE-AMPLITUDE COUPLING-BASED FUNCTIONAL BRAIN NETWORK IN EPILEPSY PATIENTS

3447

necessary to combine the phase and amplitude information of
epileptic EEG signals.

Phase-amplitude coupling (PAC) represents the coupling re-
lationship between low-frequency phase and high-frequency
amplitude of EEG signals [14]. In recent years, PAC has been
commonly used to investigate neural interactions within the
brain [15]. Especially, increasing evidence suggests that abnor-
mal PAC may be associated with various neurological disor-
ders, including Parkinson’s disease, schizophrenia, Alzheimer’s
disease, and epilepsy [16]. For example, Ghinda et al. used
intracranial EEG signals of ictal period to examine the dynamic
evolution of modulation index (MI) PAC, and found that the
locally increased PAC can be observed earlier than the onset of
seizures [17]. Similarly, Hashimoto et al. found that the θ−γ
PAC gradually increases along with the evolution of epilepsy
and spreads from the local area to other brain regions [18].
Additionally, a recent animal experimental study has shown that
the θ−γ PAC of epileptic rats in the interictal period is larger
than that of normal rats, and deep brain stimulation could reduce
the pathologically increased PAC, indicating that θ−γ PAC may
contribute to predicting seizures and monitoring effectiveness of
clinical treatment [19]. Obviously, PAC could provide a novel
perspective to understanding neural interactions during different
epileptic phases, as well as mechanisms underlying the onset and
propagation of epileptic seizures.

However, it should be pointed out that the literature on neu-
ral interactions in epilepsy mainly focuses on the θ−γ PAC,
whereas too little attention has been paid to the β−γ PAC and
the corresponding functional brain networks constructed with
the β−γ PAC. Rampp et al. calculated the coupling between
the γ amplitude and δ, θ, α and β phase of the iEEG data
during the interval between attacks, and found that the PAC of
each band in areas enriched for dysmorphic neurons increased,
especially in the δ or θ bands [20]. Furthermore, certain stud-
ies on neurological disorders suggest that the PAC between
β band and high-frequency band provides better explanatory
power for signal variations than β band activity alone [21],
[22]. Experimentally, β rhythm, which plays a role in vari-
ous brain cognitive functions, has been conﬁrmed as the most
widespread cortical oscillatory activity during resting-state brain
activity in epilepsy patients [23], [24], and the PAC between the
low-frequency and gamma rhythms has been observed during
epilepsy [18]. Accordingly, it is reasonable to speculate that
alterations of the β−γ PAC can be observed during different
epileptic periods. If this hypothesis holds, it may complement
the current commonly used θ−γ PAC methods for investigating
neural interactions within the brains of epilepsy patients. To
conﬁrm this assumption, in the present study, we quantify β−γ
PAC by MI value calculated with EEG signals of intractable
epilepsy patients, and construct the corresponding functional
brain networks with MI values. Statistical analysis suggests
that the β−γ PAC of between-channels, as a whole shows an
increasing trend during epileptic periods. Especially, the MI
values of β−γ PAC of between-channels in the post-ictal period
are signiﬁcantly higher than those during the pre-ictal period.
Correspondingly, network analysis shows that both the average
node degree and characteristic path length in the pre-ictal and

Fig. 1. An Example of EEG data segmentation.

post-ictal periods have signiﬁcant differences. Of note, relative
to the ictal period, the characteristic path length in the pre-ictal
period increases remarkably, and the average betweenness cen-
trality in the post-ictal period also increases remarkably. More-
over, the strong functional connectivity of F3-C3 brain region
during different epileptic phases suggests that this brain region
may play critical roles in the genesis of seizures. Interestingly,
the average β−γ PAC of within-channels is positively corre-
lated with those of between-channels during epileptic periods.
These results provide new ideas for understanding alterations
of neural interactions within the brain during different epileptic
phases, and may contribute to effectively controlling epileptic
seizures.

II. MATERIALS AND METHODS

A. EEG Data and Preprocessing

used

this work
Scalp

ac-
are
EEG data
in
The
EEG Database
quired
from the CHB-MIT
(https://physionet.org/content/chbmit/1.0.0/)
jointly created
by Children’s Hospital Boston (CHB) and the Massachusetts
Institute of Technology (MIT) [25]. These EEG data are
recorded with the 10-20 international system, and the sampling
rate is 256 Hz. Totally, 22 intractable epilepsy patients with 23
cases have been recorded, including 5 males aged 3-22 and 17
females aged 1.5–19.

Due to various differences of the EEG data for each epilepsy
patient, the data selected to statistical analysis in the current
study should satisfy a single seizure duration longer than 5
seconds. Notably, the priority has been considered to select the
EEG data with an interval of more than 1 h between seizures.
Accordingly, 6 hours EEG data of each epilepsy patient are se-
lected, and there are 65 seizures in all selected data. Then, we use
EEGLAB toolbox [26] to preprocess the selected raw EEG data.
The average reference method is ﬁrstly used to re-reference the
raw EEG data. To eliminate 60 Hz power frequency interference,
the frequency component of 58–62 Hz in the data is ﬁltered out
through a notch ﬁlter. Lastly, independent component analysis
(ICA) is employed to remove physiological artifacts in EEG
signals.

Next, the preprocessed EEG data of each epilepsy patient is
further selected based on the seizures marked by time labels. As
shown in Fig. 1, assuming that the duration of the ictal period
(red) is L seconds, in this work, we deﬁne the pre-ictal period
(light blue) as 3 L seconds before the onset of seizure and the
post-ictal period (blue) as 3 L seconds after the offset of seizure.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:42 UTC from IEEE Xplore.  Restrictions apply. 

3448

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 28, NO. 6, JUNE 2024

Note that the ictal data are divided into 5 seconds per segment,
as well as the pre-ictal and post-ictal data. Accordingly, there are
totally 195 data segments of the three periods, and each period
has 65 data segments. Here, the β rhythm is in the frequency
range from 13 to 30 Hz, and the γ rhythm is from 30 to 100 Hz.
All data analysis and processing are performed on MATLAB
2021a.

B. PAC Method

In the current study, we use the MI to quantify the β−
γ PAC [27]. MI utilizes the Kullback-Leibler (KL) distance
to measure the deviation of the high-frequency amplitude
distribution-like function over low-frequency phase bins relative
to the uniform distribution [15]. Speciﬁcally, the calculation of
MI is as follows [27]:

1) Firstly, the original signal xraw(t) is bandpass ﬁltered
to obtain low-frequency and high-frequency signals, and
denoted as xfP (t) and xfA(t), respectively.

2) Using the Hilbert transform to calculate the phase time
series ΦfP (t) of low-frequency signals xfP (t) and the
amplitude time series AfA(t) of high-frequency signals
xfA(t), respectively.

3) Dividing the phase time series ΦfP (t) into uniform inter-
(cid:3)ΦfP
vals and calculating the corresponding means (cid:2)AfA
of AfA(t) within each phase interval.
4) Normalizing the mean amplitude (cid:2)AfA

(cid:3)ΦfP as shown in

(1).

P (j) =

(cid:3)ΦfP (j)

(cid:2)N

(cid:2)AfA
k=1 (cid:2)AfA

(cid:3)ΦfP (k)

,

(1)

where (cid:2)AfA
(cid:3)ΦfP (j) is the average amplitude at the phase
bin j, and N is the number of phase bins and typically set
to N = 18.

5) Calculating KL distance. For the discrete distribution P
and the discrete distribution Q, their KL distance is shown
in (2).

DKL(P, Q) =

N(cid:3)

j=1

P (j) log

(cid:4)

(cid:5)

,

P (j)
Q(j)

(2)

where DKL(P, Q) ≥ 0. DKL(P, Q) = 0 if and only if
P = Q, and at this point, P and Q represent the same
distribution.
The Shannon entropy H(P ) of the P distribution is de-
ﬁned as (3).

H(P ) = −

N(cid:3)

j=1

P (j) log[P (j)],

(3)

By combining (2) and (3), the relationship between KL
distance and Shannon entropy can be obtained, as shown
in (4).

DKL(P, U ) = log (N ) − H(P ),

(4)

where U is a uniform distribution, and log (N ) is the
potential maximum entropy value.

6) Finally, the Modulation index M I is deﬁned, as shown in

(5).

M I =

DKL(P, U )
log (N )

,

(5)

According to the deﬁnition of MI, it can be seen that 0 ≤
M I ≤ 1. If and only if the high-frequency amplitude is uni-
formly distributed over the low-frequency phase, which is no
phase-amplitude coupling and M I = 0. Clearly, the magnitude
of the MI value is positively correlated with the deviation be-
tween the discrete distribution P and the uniform distribution
U . It should be noted that the MI is calculated with phase in β
frequency range and amplitude in γ frequency range, and the
step size is 1 Hz.

C. Topological Characteristics of β−γ PAC-Based
Functional Brain Networks

Traditional functional brain networks typically utilize the cor-
relation or phase synchronization between signals to quantify the
functional connectivity of different brain regions [28]. Numer-
ous studies have shown that functional brain networks are able
to effectively reveal interactions between different brain regions
and contribute to deeply understanding epilepsy [10]. Given that
MI calculated with the phase and amplitude information of EEG
signals indirectly reﬂects neural interactions within the brain,
which may be more suitable for constructing the functional brain
network. Therefore, in this study, we use MI to construct the β−γ
PAC-based functional brain network, and the speciﬁc process is
as follows.

1) Based on (1) to (5), the MI value of β−γ PAC can be
calculated by EEG signals of any two brain regions. For example,
we denote the MI value between brain regions m and n as
M Imn, meaning that the M Imn is calculated by EEG signals
of brain regions m and n, which provide phase and amplitude
information, respectively.

2) Constructing functional brain networks, and the corre-
sponding MI-based connectivity matrix WM I is deﬁned in (6).

WM I =

⎛

⎜
⎜
⎜
⎜
⎝

M Im1 M Im2

...
M I21
0

...
0
M I12

⎞

⎟
⎟
⎟
⎟
⎠

,

0
...

. . .
. . .
. . . M I2n
. . . M I1n

(6)

To further reveal the topological characteristics of the functional
brain networks at different epileptic phases, we analyze the
node degree, the average node degree and the characteristic
path length, which have been widely used to portray network
characteristics in epilepsy research [29]. In this work, the node
degree Km of the m − th node in the functional brain network
is calculated by (7).

N(cid:3)

Km =

M Imn,

(7)

n=1
where N is the number of network nodes, and M Imn is the MI
value of β−γ PAC between node m and node n.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:42 UTC from IEEE Xplore.  Restrictions apply. 

LU et al.: EEG STUDY ON β−γ PHASE-AMPLITUDE COUPLING-BASED FUNCTIONAL BRAIN NETWORK IN EPILEPSY PATIENTS

3449

Also, the calculation of the average node degree K of the

functional brain network is shown in (8).

K =

1
N

N(cid:3)

m=1

Km,

(8)

The characteristic path length has been conﬁrmed to be associ-
ated with the efﬁciency of brain information transmission, where
the smaller the characteristic path length, the higher efﬁciency of
brain information transmission and the stronger brain functional
integration [30]. The characteristic path length of the functional
brain network is calculated by (9).
(cid:3)

L =

1
N (N − 1)

m,n∈V,m(cid:7)=n

lmn,

(9)

where lmn represents the shortest path length between the nodes
m and n.

Betweenness centrality measures the number of shortest paths
passing through a node, primarily to assess the node’s ability to
appear on the shortest paths between other nodes in the network,
reﬂecting its importance in the process of network information
transmission and its ability to serve as an information hub [31].
In the brain network, a higher value of average betweenness
centrality indicates that nodes throughout the whole network are
relatively important, which suggest that the information trans-
mission in the network may be more uniform, rather than relying
on a few nodes. On the other hand, a lower average betweenness
centrality may indicate the presence of some important nodes
in the network, while the betweenness centrality of other nodes
is lower. Mathematically, the betweenness centrality of node m
and the average betweenness centrality of the functional brain
network are calculated by (10) and (11), respectively.

Bm =

1
(N − 1)(N − 1)

(cid:3)

m,n∈V,k(cid:7)=m,n(cid:7)=m,k(cid:7)=n

B =

1
N

N(cid:3)

m=1

Bm,

ρkn(m)
ρkn

,

(10)

(11)

where ρkn is the number of shortest paths between k and n, and
ρkn(m) is the number of shortest paths between k and n that
passes through m.

Of note, the minimum spanning trees (MSTs) and the ec-
centricity have also been applied in this study to overcome the
potential biases caused by disconnected syndromes and to quan-
tify the role of brain network node in information transmission,
respectively [32], [33] (see the Supplementary Information).

D. Statistical Analysis

In the current study, two-sample t test is used to compare the
differences in functional brain networks at different epileptic
phases, and the test results are corrected by false discovery rate
(FDR) at a level of 0.05. Moreover, because the data of network
topological characteristics at different epileptic phases do not
satisfy normal distribution, the rank sum test is used for statistical

Fig. 2. β−γ PAC between the FP1-F7 and T7-P7 channels of patient
chb01.

comparisons. Also, the spearman rank correlation analysis is em-
ployed to investigate the relationship between the PAC coupling
strength of within-channels and between-channels. P < 0.05
indicates a statistically signiﬁcant difference.

Additionally, it should be pointed out that to avoid pseudo MI
values caused by data randomness, 200 random surrogate data
have been used to calculate MI values, and the permutation test
is conducted between the MI value calculated from the original
data and that calculated from the surrogate data. The MI value
is retained if P < 0.05, otherwise, M I = 0.

III. RESULTS
A. β−γ PAC of Between-Channels At Different Epileptic
Phases

Unlike the θ−γ PAC that has been widely used to investi-
gate epilepsy, in the current study, we assume that the β−γ
PAC can also be observed during different epileptic phases,
which may provide a new perspective to understanding neural
interactions within the brain. To examine our assumption, three
channel signals with electrode labeled FP1-F7, T7-P7, and P3-
O1 are randomly selected to explore the potential β−γ PAC of
between-channels. Here, to distinguish the phase and amplitude
information provided by different channels, we use “P” and “A”
to denote the phase and amplitude information, respectively.
For example, the labels FP1-F7(P), T7-P7(P) and P3-O1(P)
represent the channels FP1-F7, T7-P7 and P3-O1 providing
the phase information to calculate PAC. The labels FP1-F7(A),
T7-P7(A) and P3-O1(A) denote the channels FP1-F7, T7-P7 and
P3-O1 providing the amplitude information to calculate PAC.

Furthermore, we select the FP1-F7 and T7-P7 channels of
patient chb01 to show that the β−γ PAC can also be observed
during different epileptic phases, as shown in Fig. 2. Obviously,

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:42 UTC from IEEE Xplore.  Restrictions apply. 

3450

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 28, NO. 6, JUNE 2024

the pre-ictal period, whereas the level of neural interactions
signiﬁcantly increases after the offset of epileptic seizures.

B. β−γ PAC-Based Functional Brain Networks At
Different Epileptic Phases

The above results show that the β−γ PAC of between-
channels signiﬁcantly alter with the epileptic phases, and the MI
values are inﬂuenced by the phase and amplitude information
provided by different channels. Theoretically, using the MI value
of β−γ PAC to construct the functional brain network will
greatly contribute to understanding neural interactions within the
brain during different epileptic phases. Therefore, in the current
study, it is very necessary to construct the β−γ PAC-based
functional brain network. However, it should be pointed out
that the MI values of β−γ PAC may be affected by the EEG
signals recoded with close electrodes, which may lead to signal
redundancy. Indeed, previous studies have demonstrated that the
spatial position of the brain regions has remarkable impacts on
the correlation of EEG signals [34]. To avoid these potential
effects on MI values and also to reduce the computational
cost, we randomly select eight channel signals with relatively
dispersed recorded electrodes, which the corresponding labels
are FP1-F7, T7-P7, P7-O1, FP1-F3, F3-C3, P3-O1, F8-T8 and
FZ-CZ.

Based on the selected EEG signals, we use the MI values of
β−γ PAC to construct the functional brain networks of different
epileptic phases, as shown in Fig. 4. Note that the channels of
the horizontal axis provide the amplitude information for calcu-
lating the MI, which the phase information is provided by the
channels of the vertical axis. Besides the obvious alterations of
the functional brain networks during the three epileptic periods,
the functional brain networks are not symmetric, which is due
to the asymmetry of phase and amplitude information provided
by different channels (Fig. 4(a)). According to the asymmetric
functional brain networks, we correspondingly construct two
symmetric functional networks, which are the phase-amplitude
network constructed with the functional connectivity of the
triangle in the upper left (Fig. 4(b)) and the amplitude-phase
network constructed with the functional connectivity of the
triangle in the lower right (Fig. 4(c)). Despite the signiﬁcant
differences between the phase-amplitude and amplitude-phase
networks during the three epileptic periods, the MI values
gradually increase with the evolution of epilepsy in both brain
networks. Moreover, we can observe that the FP1-F7 channel
in the phase-amplitude network has higher MI values than that
of other channels during the three epileptic periods. However,
in the amplitude-phase networks, compared to other channels,
both the FP1-F3 and F3-C3 channels have relatively higher MI
values during the evolution of epilepsy.

To statistically quantify the alterations of β−γ PAC-based
functional brain networks during the three epileptic periods, the
paired two-sample t tests for the functional brain networks are
conducted, and the false positive rate is controlled and corrected
through the FDR to avoid spurious connections (edges), where
the signiﬁcant deviations between MI values are calculated, as

Fig. 3. β−γ PAC between FP1-F7, T7-P7, and P3-O1 channels of all
patients.

as we expected, the β−γ PAC can be observed between the
FP1-F7 and T7-P7 channels during the three epileptic periods.
Intuitively, compared to the MI values of the pre-ictal and ictal
periods, the MI values of β−γ PAC increase signiﬁcantly in the
post-ictal period. Interestingly, the increasing trend of MI values
is not affected by the phase and amplitude information provided
by the FP1-F7 and T7-P7 channels. However, the phase and
amplitude information provided by each channel may have an in-
ﬂuence on the strength of the β−γ PAC. Moreover, relative to the
consistent distribution of the phase information, the distribution
of central frequencies of the amplitude information is discrete.
These results indicate that the β−γ PAC of between-channels
may provide a new way to view the evolution of epilepsy, and
the strength of β−γ PAC may be inﬂuenced by the type of
information provided by the channels.

To quantify the alterations of β−γ PAC of between-channels
at different epileptic phases, we use the rank sum test to analyze
the statistical differences of MI values calculated with the FP1-
F7, T7-P7 and P3-O1 channels during the three epileptic periods,
as shown in Fig. 3. According to the statistical analysis, there
are four types of alterations of MI values within the six cases
combined by the three selected channels. Speciﬁcally, in terms
of the ﬁrst type combined by the FP1-F7(P) and T7-P7(A), the
MI values in the post-ictal period are signiﬁcantly higher than
those in the ictal and pre-ictal periods. The combinations of
the second type are involved in the FP1-F7(P) and P3-O1(A),
T7-P7(P) and P3-O1(A), which show that the MI values in the
post-ictal period are remarkably higher than those in the pre-
ictal period. Unlikely, in the third type combined by the T7-
P7(P) and FP1-F7(A), P3-O1(P) and FP1-F7(A), the MI values
in the ictal and post-ictal periods are signiﬁcantly higher than
those in the pre-ictal period. The combination of P3-O1(P) and
T7-P7(A) is the fourth type, where the MI values in the post-
ictal period are remarkably higher than those in the ictal and
pre-ictal periods, and the MI values in the ictal period are also
signiﬁcantly higher than those in the pre-ictal period. Although
the statistical differences of MI values are different in the four
types, the MI values in the three epileptic periods, as a whole
show an increasing trend. Particularly, the MI values of between-
channels in the post-ictal period are signiﬁcantly higher than
those in the pre-ictal period.

Taken together, these results indicate that neural interactions
alter with the evolution of epilepsy. Especially, the neural inter-
actions within the brain may be at a relatively low level during

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:42 UTC from IEEE Xplore.  Restrictions apply. 

LU et al.: EEG STUDY ON β−γ PHASE-AMPLITUDE COUPLING-BASED FUNCTIONAL BRAIN NETWORK IN EPILEPSY PATIENTS

3451

Fig. 4. β−γ PAC-based functional brain networks in different epileptic
phases. (a), Asymmetric functional brain network. (b), Phase-amplitude
network; (c), Amplitude-phase network.

Fig. 5. Alterations of the β−γ PAC-based functional brain networks
during the evolution of epilepsy. (a), Signiﬁcant changes in the phase-
amplitude network. left: Compared to the ictal period, the enhanced MI
values in the post-ictal period; right: compared to the pre-ictal period,
the enhanced MI values in the post-ictal period. (b), Signiﬁcant changes
in the amplitude-phase network. Compared to the pre-ictal period, the
enhanced MI values in the post-ictal period.

shown in Fig. 5. In terms of the phase-amplitude network, the
MI value of β−γ PAC between the F8-F8 and P7-O1 channels is
signiﬁcantly enhanced in the post-ictal period compared to that
in the ictal period (Fig. 5(a)). Also, compared to the pre-ictal
period, the MI values of β−γ PAC between the T7-P7 and
the other three channels, including the FP1-F3, P3-O1 and
FZ-CZ channels, signiﬁcantly enhanced in the post-ictal period
(Fig. 5(a)). Interestingly, in the amplitude-phase networks, the
MI values of β−γ PAC between the FP1-F7 and other two
channels that the F3-C3 and T7-P7 channels in the post-ictal pe-
riod are signiﬁcantly enhanced compared to that in the pre-ictal
period (Fig. 5(b)). These results indicate that both the epileptic
phases and information provided by EEG signals have important
effects on the β−γ PAC-based functional brain networks.

the β−γ PAC-based functional brain
Fig. 6. The Node degree of
network during different epileptic phases. (a), the node degree of the
phase-amplitude network. (b), the node degree of the amplitude-phase
network.

C. Topological Characteristics of β−γ PAC-Based
Functional Brain Networks During Epileptic Phases

To further investigate alterations of topological characteris-
tics of β−γ PAC-based functional brain networks during the
three epileptic periods, we ﬁrstly calculate the degree of each
node in the phase-amplitude and amplitude-phase networks,
respectively (Fig. 6). Note that the functional brain network has
8 nodes and 65 seizures. Intuitively, the statistical differences
of node degree are obvious during different epileptic phases.
The common change observed in the two networks is that all
node degrees exhibit a signiﬁcant increase in the post-ictal
period compared to that in the pre-ictal period. Besides, in the
phase-amplitude network, the node degree of the T7-P7, P7-O1
and F8-T8 channels in the post-ictal period also signiﬁcantly
increases compared to that in the ictal period, but compared
to that observed in the pre-ictal period, the node degree of the
T7-P7, FP1-F3 and FZ-CZ channels increases signiﬁcantly in
the ictal period (Fig. 6(a)). Of note, the remarkable differences
of the node degree during the three epileptic periods can only
be observed in the T7-P7 channel. Similarly, in the amplitude-
phase network, compared to the node degree observed in the
ictal period, the node degree of the FP1-F7,P7-O1 and F8-T8
channels also shows signiﬁcant increase in the post-ictal period
(Fig. 6(b)).

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:42 UTC from IEEE Xplore.  Restrictions apply. 

3452

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 28, NO. 6, JUNE 2024

TABLE I
CHANNEL CLASSIFICATION BASED ON THE NODE DEGREE OF
PHASE-AMPLITUDE NETWORK

Fig. 7. The Average node degree of the β−γ PAC-based functional
brain networks during epileptic phases. (a), the average node degree
of the phase-amplitude network. (b), the average node degree of the
amplitude-phase network.

Fig. 8. Characteristic path length of the β−γ PAC-based functional
brain networks during epileptic phases. (a),
the characteristic path
length of the phase-amplitude network. (b), the characteristic path length
of the amplitude-phase network.

interactions within the brain may be enhanced in the post-ictal
period.

Also, to observe changes of the information transmission efﬁ-
ciency within the two functional brain networks during epileptic
phases, we calculate the characteristic path length of these
networks (Fig. 8). Statistically, the characteristic path length
of the two functional brain networks in the ictal and post-ictal
periods is signiﬁcantly reduced compared to that in the pre-ictal
period. However, there is no signiﬁcant difference between the
ictal and post-ictal periods. These results indicate that epilep-
tic seizures may have remarkable effects on the information
transmission efﬁciency, which may strengthen the functional
integration ability of the brain.

Accordingly, it is reasonable for us to speculate that the signif-
icant changes of the characteristic path during epileptic phases
may provide a potential biomarker for predicting seizures.

Similarly, to analyze the changes of information transmission
uniformity within the two functional brain networks during
epileptic phases, we calculate the average betweenness centrality
of these networks (Fig. 9). Statistically, the average betweenness
centrality of the two functional brain networks in the post-ictal
period signiﬁcantly increases compared to that in the ictal period.
These results suggest that during seizures, several key nodes
may play a dominant role in information transmission in the
brain network. However, in the post-ictal period, information
transmission in the brain network no longer relies on a few
key nodes and becomes more evenly distributed. Of note, the
betweenness centrality of each node in both the phase-amplitude
and amplitude-phase networks has also been calculated and
statistically analyzed (see Fig. S1 in the Supplementary Infor-
mation). The statistical results indicate that the betweenness

TABLE II
CHANNEL CLASSIFICATION BASED ON THE NODE DEGREE OF
AMPLITUDE-PHASE NETWORK

Together, despite that the increased trend of the node degree is
the same in the post-ictal period, alterations of the node degree
of the two β−γ PAC-based functional brain networks during
the three epileptic periods are partially different, which may be
associated with the phase or amplitude information provided by
each channel. Furthermore, to observe the consistent alterations
of the node degree during different epileptic phases, the EEG
channels are divided into four categories in the phase-amplitude
network (Table I), as well as two categories in the amplitude-
phase network (Table II). Interestingly, although the number of
category is different for the two functional brain networks, the
statistical differences of several EEG channels are the same, such
as P7-O1, F3-C3, P3-O1 and F8-T8 channels. Theoretically, the
various changes of the node degree indicate that these nodes
may have different contributions to the dynamical evolution of
epilepsy, which may also provide a new way to localize the
epileptic zone.

Additionally, to observe alterations of the global network
property during epileptic phases, the average node degree of the
two functional brain networks is calculated (Fig. 7). Obviously,
the average node degree of the two functional brain networks
in the post-ictal period is signiﬁcantly higher than that in the
pre-ictal period, which is consistent with the ﬁndings observed
in the node degree of each channel (see Fig. 6). These obser-
vations indicate that the sparsity of functional brain networks
may be lower in the post-ictal period, meaning that the neural

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:42 UTC from IEEE Xplore.  Restrictions apply. 

LU et al.: EEG STUDY ON β−γ PHASE-AMPLITUDE COUPLING-BASED FUNCTIONAL BRAIN NETWORK IN EPILEPSY PATIENTS

3453

exists in the FZ-CZ and F3-C3 brain regions, suggesting that the
overall information interaction between the FZ-CZ and F3-C3
brain regions may be stronger during different epileptic phases.
Notably, in the ictal period, connection between FZ-CZ and
other brain regions is enhanced and that between F8-T8 and
other brain regions is weakened, suggesting that seizures may
enhance information interaction between FZ-CZ and other brain
regions, but may inhibit information interaction between F8-T8
and other brain regions. These results indicate that the func-
tional connectivity of the two functional brain networks varies
during different epileptic phases, and that of the amplitude-phase
network varies comparatively more. The F3-C3 region showed
strong functional connectivity in two functional brain networks,
indicating that the F3-C3 region may be a key brain region in
seizures.

In addition, to overcome the potential biases caused by dis-
connected syndromes, the minimum spanning trees (MSTs) of
the phase-amplitude and amplitude-phase networks have been
computed (see Fig. S2 in the Supplementary Information). Ob-
viously, the FP1-F7 region has more connections than other
brain regions during different epileptic phases, which is con-
sistant with observations in Fig. 10. Furthermore, the average
eccentricity of the two functional brain networks based on the
MSTs has also been calculated (see Fig. S3 in the Supplementary
Information). Although there no signiﬁcant difference of the
average eccentricity can be observed in each functional brain
network, the signiﬁcant changes of the eccentricity of several
brain regions still can be observed during epileptic phases (see
Fig. S4 in the Supplementary Information), which further sup-
port the observations in Fig. 10.

D. The Relationship of β−γ PAC Between
Within-Channels and Between-Channels During
Epileptic Phases

As mentioned above, the β−γ PAC-based functional brain
networks signiﬁcantly change with the evolution of epilepsy.
However, it should be pointed out that both the phase-amplitude
and amplitude-phase networks are constructed by different EEG
channels, which the information of phase and amplitude is
provided by two different channels. Correspondingly, a question
that whether there exists a relationship of β−γ PAC between
within-channels and between-channels during epileptic phases
may be arisen. To examine this question, we use the Spearman
rank correlation to analyze the potential relationship. Of note, the
within-channel MI value is calculated with phase and amplitude
provided by the same channel, and then averaging these MI
values to obtain the averaged within-channel MI value. Corre-
spondingly, the between-channel MI value is calculated with
phase or amplitude from one channel but amplitude or phase
provided by all other channels, and then calculating the mean
of these MI values to obtain the averaged between-channel MI
value.

As shown in Fig. 11, the positive correlations of averaged β−γ
PAC between within-channels and between-channels are signiﬁ-
cant and different during the three epileptic periods. Importantly,
the information of phase and amplitude has different inﬂuences

Fig. 9. The Average betweenness centrality of the β−γ PAC-based
functional brain networks during epileptic phases. (a), the average be-
tweenness centrality of the phase-amplitude network. (b), the average
betweenness centrality of the amplitude-phase network.

Fig. 10. The Functional brain network connectivity of β−γ PAC during
epileptic phases. (a), phase-amplitude network. (b), amplitude-phase
network.

centrality of each node in the two functional brain networks
changes variously during different epileptic phases. Interest-
ingly, the betweenness centrality of each node observed in the
ictal period often shows signiﬁcantly decrease compared to that
in the pre-ictal and post-ictal periods, which is partly consistent
with observations in Fig. 9.

Along with the changes of network property observed in the
two β−γ PAC-based functional brain networks, theoretically, the
alterations of functional connectivity of the two networks should
be remarkable. As shown in Fig. 10, the functional connectivities
of the top 20% of each network have been selcted to show
the variations during epileptic phases. It is easy to observe that
besides the signiﬁcant changes of functional connectivity in the
phase-amplitude and amplitude-phase networks, the variations
of functional connectivity are different for the two networks.

Obviously, there are differences in phase-amplitude network
connectivity during different epileptic phases, as shown in
Fig. 10(a). Speciﬁcally, the functional connectivity of the phase-
amplitude network mainly exists in the FP1-F7, FP1-F3 and
F3-C3 brain regions, among which the functional connectivity
between the FP1-F7 and other brain regions remains stable
during different epileptic phases. Similarly, the connectivity of
the amplitude-phase network during different epileptic phases is
also different, as shown in Fig. 10(b). However, compared with
phase-amplitude network, amplitude-phase network connectiv-
ity varies more during different epileptic phases. Speciﬁcally,
functional connectivity of the amplitude-phase network mainly

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:42 UTC from IEEE Xplore.  Restrictions apply. 

3454

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 28, NO. 6, JUNE 2024

and amplitude-phase networks. Interestingly, both the phase-
amplitude and amplitude-phase networks show that the averaged
node degree and characteristic path length in the post-ictal period
signiﬁcantly different from that in the pre-ictal period. Besides,
the average betweenness centrality in the post-ictal period sig-
niﬁcantly increases compared to that in the ictal period. These
ﬁndings indicate that neural interactions within the brain change
signiﬁcantly along with the evolution of epilepsy, and β−γ
PAC may complement the current commonly utilized θ−γ PAC
methods and provide a new perspective to view the dynamics of
epilepsy.

The β−γ PAC-based functional brain network may offer a
new way to predict epileptic seizure. Statistically, the charac-
teristic path length observed in the β−γ PAC-based functional
brain networks changes signiﬁcantly during epileptic phases.
Especially, both in the phase-amplitude and amplitude-phase
networks, the characteristic path length in the ictal period is
signiﬁcantly reduced compared to that during the pre-ictal pe-
riod. These observations indicate that the characteristic path
length may contribute to the prediction of epileptic seizures.
Actually, previous studies have also shown that the topological
characteristics of brain functional networks can be applied to
predict seizures. For example, an EEG-based functional brain
network study has found that the characteristic path length in-
creases continuously during the evolution of epilepsy, which can
be used to predict seizures [34]. In another study, the functional
brain network was jointly constructed with nine graph-theoretic
parameters (assortativity coefﬁcient, transitivity, clustering co-
efﬁcient, strength of node, modularity, betweenness centrality,
characteristic path length, global efﬁciency and radius), and had
excellent epilepsy prediction performance [35]. Clearly, these
studies further support our assumption that the characteristic
path length may be a useful predictor for epileptic seizures,
which is helpful for the early clinical diagnosis and treatment of
epilepsy.

It has been demonstrated that the PAC and PAC-based func-
tional brain networks greatly contribute to localizing epilepto-
genic zones. Speciﬁcally, a previous study based on the frontal
EEG signals of epileptic patients found that the characteris-
tics of EEG coupling strength in the interictal and pre-ictal
periods can be used to accurately locate the epileptogenetic
regions, where the channels with strong PAC are mostly con-
ﬁned to the seizure onset zones and resection zones [36]. Simi-
larly, the θ−γ PAC-based functional brain networks constructed
by stereo-electroencephalography data accquired from patients
with temporal lobe epilepsy indicated that there exists a strong
cross-frequency coupling within epileptogenic regions during
seizures, and the corresponding network is more regular than
that in the interictal period, which suggests that PAC may
contribute to identifying seizures and localizing epileptogenic
zones [37]. Actually, the analysis of functional brain networks
is also useful for accurately locating epileptogenic zones of
patients with focal epilepsy. For example, Adkinson et al. used
the centrality measurements to investigate characteristics of
network nodes of patients with temporal lobe epilepsy and
found that the electrode sites with maximum Katz centrality
and degree centrality are closely related to epileptogenic zones

Fig. 11. Relationship of β−γ PAC between within-channels and
between-channels during epileptic phases. (a), the between-channel
MI value calculated with one channel providing phase information. (b),
the between-channel MI value calculated with one channel providing
amplitude information. RS represents the correlation coefﬁcient and P
represents the signiﬁcance level. P=0 indicates that P approaches 0.

on the between-channel MI values, which the correlation coefﬁ-
cients are higher for the case that one channel provides amplitude
information and all other channels provide phase information
during the pre-ictal and ictal periods (Fig. 11(b)). However, in
the post-ictal period, both the phase and amplitude information
may have less effects on the correlation coefﬁcients, which are
relatively smaller than that in the pre-ictal and ictal periods.
These observations suggest that the neural interactions may be
more complex during the post-ictal period.

IV. DISCUSSION

The PAC has been suggested to play key roles in uncovering
the neural interactions during different cognitive states and brain
diseases, especially the abnormal θ−γ PAC widely observed in
epilepsy has provided several new insights into understanding
the evolution of epilepsy. However, few studies pay attention
to β−γ PAC during epileptic phases. In the current study, we
use MI method to calculate β−γ PAC and construct β−γ PAC-
based functional brain networks, including phase-amplitude and
amplitude-phase networks. We expect to seek a new perspective
to understanding alterations of neural interactions during the
epileptic evolution on the basis of β−γ PAC, and to explore
the alterations of β−γ PAC-based functional brain networks
during different epileptic phases. Statistical analysis shows that
the PAC of epilepsy patients is abnormal, which is consistent
with previous research results [16]. Speciﬁcally, there exists β−γ
PAC during epileptic phases, which changes signiﬁcantly and
differently for each EEG channel. Especially, the remarkably
increased β−γ PAC can be observed in most channels at the
post-ictal period. Moreover, the between-channel MI values
can be inﬂuenced by the information of phase and amplitude
provided by different channels, which lead to statistical differ-
ences of several network properties between phase-amplitude

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:42 UTC from IEEE Xplore.  Restrictions apply. 

LU et al.: EEG STUDY ON β−γ PHASE-AMPLITUDE COUPLING-BASED FUNCTIONAL BRAIN NETWORK IN EPILEPSY PATIENTS

3455

during seizures [38]. Goodale et al. used the resting state stereo-
electroencephalography data acquired from patients with focal
epilepsy to investigate the functional connectivity of sampled
brain regions, and constructed a logistic regression model to
predict epileptogenicity of individual regions, and found that
the functional connectivities within the epileptogenic regions
and between the epileptogenic regions and other structures
are increased compared to that within nonepileptogenic struc-
tures [39]. Unlikely, we employed the MI method to construct
the β−γ PAC-based functional brain networks of pre-ictal, ictal
and post-ictal periods, where statistical anlaysis shows that the
changes of node degree of each channel are signiﬁcant and
different during the evolution of epilepsy. Particularly, both in
the phase-amplitude and amplitude-phase networks, the node
degree signiﬁcantly increases in the post-ictal period compared
to that in the pre-ictal period, which suggests that neural in-
teractions during post-ictal period may be enhanced between
some different brain regions. Of note, these alterations of node
degree are very useful for identifying potential contributions of
each channel to the evolution of epilepsy. Accordingly, both the
node degree and betweenness centrality suggest that the F3-C3
channel may be an important node in epileptic phases in our
work. Brieﬂy, all these studies demonstrate that the PAC and
PAC-based functional brain networks may provide a new way
to locate epileptogenic zones.

The topological characteristics of β−γ PAC-based functional
brain networks may serve as a new point to understanding
epilepsy. Indeed, numerous studies have shown that epilepsy
is a network disease, which the related topological character-
istics can provide new views to observe dynamical evolution
of epilepsy [30], [40], [41], [42]. An EEG-based functional
brain network study has found that the edge density slowly
increases in the second half of the seizure and reaches a peak
after the seizure, which suggests that the increased synchroniza-
tion of neuronal activity may be an emergent self-regulatory
mechanism underlying seizure termination [43]. Relative to
the variations of network edges, the averaged node degree of
the β−γ PAC-based functional brain networks in our study
also signiﬁcantly changes during epileptic phases, which in
the post-ictal period is signiﬁcantly higher than that in the
pre-ictal period. In addition, compared to the ictal period, the
average betweenness centrality in the post-ictal period also
signiﬁcantly increased, which suggests that after the offset of
seizures, the brain state may change from being dominated by
multiple activated nodes to being dominated by fewer nodes.
However, the characteristic path length in the ictal and post-ictal
periods is signiﬁcantly reduced compared to that in the pre-ictal
period. Importantly, these observations can be supported by a
previous study, which found that the characteristic path length
corresponding to focal epilepsy slightly decreases with the onset
of seizures and then slowly rebounds, while the characteristic
path length corresponding to bilaterally spread focal epilepsy
signiﬁcantly decreases with the onset of seizures [44].These
ﬁndings suggest that the topological characteristics have a close
association with the type of epilepsy, which can provide new
insights into the evolution of epilepsy. Similarly, the statistical
results of node degree, minimum spanning trees, and eccentricity

in current study indicate that neural interactions between F8-T8
and P3-O1 brain regions and other brain regions may be inhibited
during seizures, which may also contribute to understanding the
mechanism of epileptic seizures.

Of note, it has been demonstrated that PAC is not limited wthin
a local brain region, which can also be observed between various
functional brain regions [45]. As shown in our present study,
alterations of between-channel MI values are signiﬁcant during
epileptic phases, which are different from that concentating on
PAC within local brain regions. More importanly, we found
that there exists positive correlations between within-channel
PAC and between-channel PAC, which also change along with
the evolution of epilepsy. Due to that the phase and amplitude
information of EEG signals are taken into account to calculate
PAC, it is reasonable for us to speculate that compared to the
within-channel PAC, the between-channel PAC may provide
more evidence to show neural interactions during epileptic
phases, as well as locating the seizure onset zone.

Despite that the β−γ PAC is ﬁrstly employed in our study to
examine the alterations of neural interactions during epileptic
phases, we must admit that there are still some limitations in
this work. For example, the EEG data analyzed in the work are
acquired from the CHB-MIT public dataset, which has limited
clinical information of each patient, lacks records of clinical
symptoms or seizure frequency, and the labeling of seizure areas
is not clear enough. Thus, it is difﬁcult for us to accurately
contrast the seizure onset zone with the locations identiﬁed by
the β−γ PAC. Notably, due to that the MI is least inﬂuenced by
some confounding factors, such as noise data, short data epoch
and low sampling rate, only MI-based PAC has been calculated
in this work. Also, to avoid effects of spatial factor on MI values
and reduce the computational cost, only eight channel signals
have been selected to construct the β−γ PAC-based functional
brain networks. In addition, it should be noted that besides the
β−γ PAC calculated with MI method, various cross-frequency
couplings have been proposed to investigate brain rhythms with
different frequency bands [46], [47], [48]. In this study, despite
that we particularly focused on the β−γ PAC, couplings between
other rhythms within the brain of epilepsy patients also deserve
further investigation. Therefore, it is essential for us to system-
atically explore neural interactions with more cross-frequency
couplings and more clinical EEG data with multi-channels, and
explore the relationship between these neural interactions and
patient clinical features in the future study.

V. CONCLUSION
The β−γ PAC-based functional brain networks have been
constructed to investigate alterations of neural interactions dur-
ing the evolution of epilepsy. Statistical analyses show that the
between-channel β−γ PAC signiﬁcantly increases in the post-
ictal period compared to that in the pre-ictal period. Similarly, the
remarkably increased node degree and averaged node degree, as
well as the decreased characteristic path length, can be observed
in both phase-amplitude and amplitude-phase networks in the
post-ictal period. In addition, the average betweenness centrality
in the post-ictal period signiﬁcantly increased compared to the

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:42 UTC from IEEE Xplore.  Restrictions apply. 

3456

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 28, NO. 6, JUNE 2024

ictal period. More importantly, there exists positive correlations
between within-channel MI values and between-channel MI
values during epileptic phases. In conclusion, these ﬁndings
suggest that the β−γ PAC-based functional brain networks can
provide a novel perspective to understanding the dynamical
evolution of epilepsy, and may offer a new biomarker to locate
the seizure onset zone.

REFERENCES

[1] J. Falco-Walter, “Epilepsy-deﬁnition, classiﬁcation, pathophysiology, and
epidemiology,” Seminars Neurol., vol. 40, no. 06, pp. 617–623, Dec. 2020.
[2] E. Beghi, “The epidemiology of epilepsy,” Neuroepidemiology, vol. 54,

no. 2, pp. 185–191, Mar. 2020.

[3] S. Sinha and K. A. Siddiqui, “Deﬁnition of intractable epilepsy,” Neuro-

sciences, vol. 16, no. 1, pp. 3–9, Jan. 2011.

[4] W. O. Pickrell and P. E. Smith, “Treatment of resistant epilepsy,” Clin.

Med., vol. 14, pp. s1–6, Dec. 2014.

[5] N. Barot, “Networks in frontal lobe epilepsy,” Neurosurgery Clin. North

Amer., vol. 31, no. 3, pp. 319–324, Jul. 2020.

[6] G. Slinger, W. M. Otte, K. P. J. Braun, and E. van Diessen, “An updated
systematic review and meta-analysis of brain network organization in focal
epilepsy: Looking back and forth,” Neurosci. Biobehavioral Rev., vol. 132,
pp. 211–223, Jan. 2022.

[7] M. J. Vaessen et al., “White matter network abnormalities are associated
with cognitive decline in chronic epilepsy,” Cereb. Cortex, vol. 22, no. 9,
pp. 2139–2147, Sep. 2012.

[8] E. van Diessen, S. J. H. Diederen, K. P. J. Braun, F. E. Jansen, and C. J.
Stam, “Functional and structural brain networks in epilepsy: What have
we learned?,” Epilepsia, vol. 54, no. 11, pp. 1855–1865, Nov. 2013.
[9] A. Vetkas et al., “Identifying the neural network for neuromodulation in
epilepsy through connectomics and graphs,” Brain Commun., vol. 4, no. 3,
May 2022.

[10] W. Stacey et al., “Emerging roles of network analysis for epilepsy,”

Epilepsy Res., vol. 159, Jan. 2020, Art. no. 106255.

[11] V. S. G. M. Tenorio, J. M. de Assis, and F. M. de Assis, “Functional and
effective connectivity characterization of absence seizures,” in Proc. IEEE
27th Int. Conf. Syst., Signals Image Process., 2020, pp. 81–86.

[12] J. M. den Heijer et al., “The relation between cortisol and functional con-
nectivity in people with and without stress-sensitive epilepsy,” Epilepsia,
vol. 59, no. 1, pp. 179–189, Jan. 2018.

[13] R. Rosch, T. Baldeweg, F. Moeller, and G. Baier, “Network dynamics in
the healthy and epileptic developing brain,” Netw. Neurosci., vol. 2, no. 1,
pp. 41–59, 2018.

[14] O. Jensen and L. L. Colgin, “Cross-frequency coupling between neuronal
oscillations,” Trends Cognit. Sci., vol. 11, no. 7, pp. 267–269, Jul. 2007.
[15] S. Kullback and R. A. Leibler, “On information and sufﬁciency,” Ann.
Math. Statist., vol. 22, no. 1, pp. 79–86, 1951. [Online]. Available: http:
//www.jstor.org/stable/2236703

[16] Y. Salimpour, K. A. Mills, B. Y. Hwang, and W. S. Anderson, “Phase-
targeted stimulation modulates phase-amplitude coupling in the motor
cortex of the human brain,” Brain Stimulation, vol. 15, no. 1, pp. 152–163,
2022.

[17] D. C. Ghinda, Y. Salimpour, N. E. Crone, J. Kang, and W. S. Anderson,
“Dynamical analysis of seizure in epileptic brain: A dynamic phase-
amplitude coupling estimation approach,” in Proc. IEEE 43rd Annu. Int.
Conf. Eng. Med. Biol. Soc., 2021, pp. 5970–5973.

[18] H. Hashimoto et al., “Phase-amplitude coupling of ripple activities during
seizure evolution with theta phase,” Clin. Neurophysiol., vol. 132, no. 6,
pp. 1243–1253, Jun. 2021.

[19] I. Mihaly, K. Orban-Kis, Z. Gall, A.-J. Berki, R.-B. Bod, and T. Szi-
lagyi, “Amygdala low-frequency stimulation reduces pathological phase-
amplitude coupling in the pilocarpine model of epilepsy,” Brain Sci.,
vol. 10, no. 11, Nov. 2020, Art. no. 856.

[20] S. Rampp et al., “Dysmorphic neurons as cellular source for phase-
amplitude coupling in focal cortical dysplasia type ii,” Clin. Neuriophys-
iol., vol. 132, no. 3, pp. 782–792, 2021.

[21] T. Murta et al., “Phase–amplitude coupling and the BOLD signal: A
simultaneous intracranial eeg (ICEEG)-FMRI study in humans performing
a ﬁnger-tapping task,” Neuroimage, vol. 146, pp. 438–451, 2017.
[22] M. Boˇcková et al., “Coupling between beta band and high frequency
oscillations as a clinically useful biomarker for DBS,” npj Parkinson’s
Dis., vol. 10, no. 1, 2024, Art. no. 40.

[23] M. Lundqvist, J. Rose, P. Herman, S. L. Brincat, T. J. Buschman, and E.
K. Miller, “Gamma and beta bursts underlie working memory,” Neuron,
vol. 90, no. 1, pp. 152–164, 2016.

[24] M. Chikermane et al., “Cortical beta oscillations map to shared brain

networks modulated by dopamine,” bioRxiv, 2024.

[25] A. H. Shoeb, “Application of machine learning to epileptic seizure onset

detection and treatment,” Massachusetts Institute of Technology, 2009.

[26] A. Delorme and S. Makeig, “EEGLAB: An open source toolbox for
analysis of single-trial EEG dynamics including independent component
analysis,” J. Neurosci. Methods, vol. 134, no. 1, pp. 9–21, Mar. 2004.
[27] W. O. Pickrell and P. E. Smith, “Treatment of resistant epilepsy,” Clin.

Med., vol. 14, pp. s1–s6, Dec. 2014.

[28] D. Liu, T. Cao, Q. Wang, M. Zhang, X. Jiang, and J. Sun, “Construction and
analysis of functional brain network based on emotional electroencephalo-
gram,” Med. Biol. Eng. Comput., vol. 61, no. 2, pp. 357–385, Feb. 2023.
[29] S.-C. Hung et al., “Early recovery of interhemispheric functional connec-
tivity after corpus callosotomy,” Epilepsia, vol. 60, no. 6, pp. 1126–1136,
Jun. 2019.

[30] K. M. Park et al., “Progressive topological disorganization of brain net-
work in focal epilepsy,” Acta Neurologica Scandinavica, vol. 137, no. 4,
pp. 425–431, Apr. 2018.

[31] M. Rubinov and O. Sporns, “Complex network measures of brain
connectivity: Uses and interpretations,” Neuroimage, vol. 52, no. 3,
pp. 1059–1069, 2010.

[32] C. Stam, P. Tewarie, E. Van Dellen, E. Van Straaten, A. Hillebrand, and P.
Van Mieghem, “The trees and the forest: Characterization of complex brain
networks with minimum spanning trees,” Int. J. Psychophysiol., vol. 92,
no. 3, pp. 129–138, 2014.

[33] P. Hage and F. Harary, “Eccentricity and centrality in networks,” Social

Netw., vol. 17, no. 1, pp. 57–63, 1995.

[34] M. Christodoulakis, M. Anastasiadou, S. S. Papacostas, E. S. Papathana-
siou, and G. D. Mitsis, “Investigation of network brain dynamics from eeg
measurements in patients with epilepsy using graph-theoretic approaches,”
in Proc. IEEE 12th Int. Conf. Bioinf. Bioeng., 2012, pp. 303–308.
[35] A. A. H. Mubaraki, “Predicting epileptic seizures from electroencephalog-
raphy,” Ph.D. dissertation, Univ. Southampton, Southampton, U.K., 2020.
[36] H. Ma, Z. Wang, C. Li, J. Chen, and Y. Wang, “Phase-amplitude coupling
and epileptogenic zone localization of frontal epilepsy based on intracra-
nial EEG,” Front. Neurol., vol. 12, Sep. 2021, Art. no. 718683.

[37] X. Liu, F. Han, R. Fu, Q. Wang, and G. Luan, “Epileptogenic zone location
of temporal lobe epilepsy by cross-frequency coupling analysis,” Front.
Neurol., vol. 12, Nov. 2021, Art. no. 764821.

[38] J. A. Adkinson, R. Liu, I. Vlachos, and L. Iasemidis, “Connectivity
analysis for epileptogenic focus localization,” in Proc. IEEE 32nd Southern
Biomed. Eng. Conf., 2016, pp. 3–4.

[39] S. E. Goodale et al., “Resting-state SEEG may help localize epileptogenic
brain regions,” Neurosurgery, vol. 86, no. 6, pp. 792–801, Jun. 2020.
[40] S. Fang et al., “Decreasing shortest path length of the sensorimotor network
induces frontal glioma-related epilepsy,” Front. Oncol., vol. 12, Feb. 2022,
Art. no. 840871.

[41] F. Xiao et al., “Functional brain connectome and sensorimotor networks
in rolandic epilepsy,” Epilepsy Res., vol. 113, pp. 113–125, Jul. 2015.
[42] T. Zhang et al., “Aberrant basal ganglia-thalamo-cortical network topology
in juvenile absence epilepsy: A resting-state EEG-fMRI study,” Seizure-
Euro. J. Epilepsy, vol. 84, pp. 78–83, Jan. 2021.

[43] K. A. Schindler, S. Bialonski, M.-T. Horstmann, C. E. Elger, and K.
Lehnertz, “Evolving functional network properties and synchronizabil-
ity during human epileptic seizures,” Chaos, vol. 18, no. 3, Sep. 2008,
Art. no. 033119.

[44] N. Rungratsameetaweemana, C. Lainscsek, S. S. Cash, J. O. Garcia, T.
J. Sejnowski, and K. Bansal, “Brain network dynamics codify hetero-
geneity in seizure evolution,” Brain Commun., vol. 4, no. 5, Sep. 2022,
Art. no. fcac234.

[45] A. C. E. Onslow, R. Bogacz, and M. W. Jones, “Quantifying phase-
amplitude coupling in neuronal network oscillations,” Prog. Biophys. Mol.
Biol., vol. 105, no. 1/2, pp. 49–57, Mar. 2011.

[46] A. Shakeshaft et al., “Heterogeneity of resting-state EEG features in
juvenile myoclonic epilepsy and controls,” Brain Commun., vol. 4, no. 4,
Jul. 2022, Art. no. fcac180.

[47] Y. Varatharajah et al., “Characterizing the electrophysiological abnormal-
ities in visually reviewed normal EEGs of drug-resistant focal epilepsy
patients,” Brain Commun., vol. 3, no. 2, 2021, Art. no. fcab102.

[48] D. A. Hsu et al., “Correlation of EEG with neuropsychological sta-
tus in children with epilepsy,” Clin. Neurophysiol., vol. 127, no. 2,
pp. 1196–1205, Feb. 2016.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:42 UTC from IEEE Xplore.  Restrictions apply.
