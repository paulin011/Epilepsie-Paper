# Jain et al. - 2017 - A Compressed Sensing Based Decomposition of Electrodermal Activity Signals

A Compressed Sensing Based Decomposition of
Electrodermal Activity Signals

Swayambhoo Jain, Urvashi Oswal, Kevin S. Xu, Brian Eriksson, and Jarvis Haupt

1

7
1
0
2

n
a
J

6
2

]
L
M

.
t
a
t
s
[

2
v
4
5
7
7
0
.
2
0
6
1
:
v
i
X
r
a

Abstract—The measurement and analysis of Electrodermal
Activity (EDA) offers applications in diverse areas ranging
from market research, to seizure detection, to human stress
analysis. Unfortunately, the analysis of EDA signals is made
difﬁcult by the superposition of numerous components which
can obscure the signal information related to a user’s response
to a stimulus. We show how simple pre-processing followed by
a novel compressed sensing based decomposition can mitigate
the effects of the undesired noise components and help reveal
the underlying physiological signal. The proposed framework
allows for decomposition of EDA signals with provable bounds
on the recovery of user responses. We test our procedure on both
synthetic and real-world EDA signals from wearable sensors and
demonstrate that our approach allows for more accurate recovery
of user responses as compared to the existing techniques.

Index Terms—Galvanic skin response, electrodermal activity,

compressed sensing, wearables, sparse deconvolution

I. INTRODUCTION

Electrodermal Activity, or EDA, is typically recorded as the
conductance over a person’s skin, near concentrations of sweat
glands (e.g., palm of the hand or ﬁnger tips [1]). EDA signals
have been shown to include signiﬁcant information pertaining
to human neuron ﬁring [2] and psychological arousal [3].
While previously a signal that was only practically measured in
a controlled laboratory setting, recent wearable devices, such
as the Affectiva Q sensor [4] and the Empatica E4 sensor [5],
offer the ability to non-invasively measure EDA signals in
real-world environments.

An EDA signal

is generally characterized by a slowly
changing Skin Conductance Level (SCL) combined with sev-
eral short-lived Skin Conductance Responses (SCRs). The
physiological explanation can be summarized as follows: the
SCL is measuring the overall absorption of sweat
in the
user’s skin, while each SCR is measuring a discrete event of
sweat expulsion triggered by user excitement or psychological
arousal in response to stimuli [6]. We refer to these discrete
events as SCR events. The primary focus of prior EDA signal
analysis has been to extract the informative SCR events from
the observed signals, due to applications ranging from content
valence classiﬁcation [7], to audience cohort analysis [8], to
stress detection [9]. This can prove to be quite challenging
due to the overlap of SCR signal components, a dominant

SJ, JH are with the Department of Electrical and Computer Engineering,
University of Minnesota – Twin Cities, UO is with the Department of
Electrical and Computer Engineering, University of Wisconsin – Madison,
KSX is with the Electrical Engineering and Computer Science Department,
University of Toledo, BE is with Technicolor Research – Los Altos. Author
{jainx174, jdhaupt}@umn.edu, uoswal@wisc.edu,
emails:
kevin.xu@utoledo.edu, brian.eriksson@technicolor.com

SCL signal, signal artifacts due to motion, and the inclusion
of measurement noise. As a result, there are a large number
of proposed techniques to extract SCR events from observed
EDA signals [6], [7], [10]–[14], which are discussed in detail
later in the paper.

Unfortunately, these prior techniques have a series of draw-
backs. First, many of these techniques perform only simple
heuristic-based approaches to extract the SCR events, which
causes the techniques to be sensitive to noise and motion
artifacts, i.e. sudden shifts in skin conductance due to changes
in the position of the sensor. Second, these techniques lack
error bounds on the recovered SCR events, so there is no
guarantee for accuracy. Finally, most of the prior methods
have ignored the contribution of motion artifacts. As EDA
becomes more commonly observed via wearable devices, it is
more important to mitigate such motion artifacts.

In this paper, we offer a new, more realistic EDA signal
model that considers the observed EDA signal as the super-
position of a baseline signal (signal component due to SCL
changes and motion artifacts), informative SCR components,
and measurement noise. Given this cluttered observed signal,
we discuss how existing signal de-mixing work (e.g., [15],
[16]) indicates signiﬁcant challenges in reliably extracting
our desired sparse SCR event signal. We overcome these
challenges by providing a new signal model for the baseline
signal component which captures changes in measured skin
conductance due to motion as well as changes in SCL. Further,
we exploit this signal structure by a simple pre-processing step,
which transforms this recovery problem into the more tractable
problem of sparse deconvolution in the presence of bounded
noise.

The problem of sparse deconvolution has been examined
extensively in the compressed sensing literature (e.g., [17]–
[22]). We show how our EDA problem setup requires addi-
tional changes to the standard compressed sensing problem.
We use modiﬁed compressed sensing tools to estimate the SCR
events using a concise optimization program and correspond-
ing recovery error bounds. This results in “ﬁrst-of-its-kind”
EDA signal decomposition with known error rates.

We test this methodology on a series of both synthetic and
real-world EDA signals. Using synthesized data we are able
to sweep varying noise and sparsity levels to reveal regimes
where our technique accurately recovers the sparse responses.
We then show on real-world EDA signals that user reactions to
simple stimuli can be extracted with high accuracy compared
with existing EDA decomposition algorithms.

The rest of the paper is organized as follows. We review
prior work on EDA signal analysis and compressed sensing

 
 
 
 
 
 
in Section II. Our reﬁned model for observed EDA signals
is detailed in Section III. Error bounds for our compressed
sensing approach on EDA signals are shown in Section IV.
Experiments on both synthetic and real-world EDA signals are
shown in Section V. Finally, we conclude and discuss future
work in Section VI.

II. RELATED WORK

The study of Electrodermal Activity signals, or EDA sig-
nals, dates back to the early 20th century (e.g., [3]) with the
observation of a connection between changes in user skin
conductance and psychological state. In recent years,
this
connection has been validated by examining brain function via
fMRI and skin conduction via EDA concurrently in [23], and
by showing the speciﬁc regions of the brain that correspond
with EDA changes and video recordings of sweat glands
in [2]. The promise of EDA as a window into user psychol-
ogy resulted in extensive work on evaluating the connection
between EDA and user interactions [24], stress detection [9],
content and audience segmentation [8], and reaction to video
content [7]—to name only a few.

Applications using EDA signal analysis rely on the ex-
traction of a user’s ﬁne-grained responses embedded in the
EDA signal called Skin Conductance Responses, or SCRs.
These SCRs measure the expulsion of sweat triggered by
a user’s spike-like stimulus responses, which we call SCR
events. SCR events are not explicitly observed in the EDA
signal; we observe only the SCRs, which can be modeled
as the convolution of the SCR events with a distinguishing
impulse response. Signiﬁcant prior literature has focused both
on how to model the SCR impulse response and extract the
SCR events from the observed EDA signal. Examples include
a parametric sigmoid-exponential model [10], a bi-exponential
impulse response [11], nonnegative deconvolution [6], and a
variational Bayesian decomposition methodology [12]. These
prior techniques are limited by either computational complex-
ity [12] or overly simple models that ignore or heuristically
remove additional EDA signal components, such as the SCL,
that disguise the SCR events [6], [11].

The authors of [6] treat the SCL as a constant estimated by
averaging the skin conductance signal over the time windows
when the estimated SCR (by deconvolution) is below a certain
amplitude. The work of [7] presented a methodology to extract
relevant SCR events while considering the SCL signal, but
their matching pursuit-based technique used only a rough
heuristic to remove this additional signal by deleting the
two coarsest-scale components of a discrete-cosine transform
applied to the skin conductance.

More recent work has incorporated SCL in a more princi-
pled manner into the EDA signal model. The sparse represen-
tation of SCR signal was exploited in [14]. In this work, the
SCL signal was modeled as a slowly varying linear signal, and
the SCR signal was modeled as a sparse linear combination
of atoms of a dictionary containing time shifts of variety of
function shapes. A greedy method exploiting the sparsity was
also proposed for extracting the SCR events signal. Recently,
the authors of [13] proposed an approach which exploited

2

Fig. 1: An example of EDA signal where the Skin Conduc-
tance Responses (SCRs) resulting from SCR events signal are
shown [7].

sparsity from a Bayesian perspective in which the SCL signal
was modeled as a sum of cubic B-spline functions, an offset
and a linear trend, whereas the SCR signal was modeled
by a sparse signal in the dictionary obtained by shifts of
bilinear transformations of a Bateman function. Following the
maximum a posteriori (MAP) estimation principle, a convex
formulation was obtained which can be solved efﬁciently. In
contrast to these works [13], [14] we propose a model for the
baseline signal that incorporates shifts in skin conductance due
to changes in the positioning of the sensors due to motion,
which is crucial when data is collected using wearables.

Given the sparse nature of the SCR events signal, in order
to obtain bounds on our recovery, we leverage literature on
compressed sensing [17]. Usually focused on sparse signal
inference after transformation by random sensing matrices,
here we are informed by recent work on sparse deconvolution
in a compressed sensing regime [18], de-mixing of structured
signals [15], [16], and corrupted sensing for signals with
known structure [25]. Our analysis differs from this prior work
via the inclusion of a baseline signal model. This requires
signiﬁcant reformulation of the problem to develop new theory
and recovery methodologies.

III. MODEL

The observed EDA skin conductance signal is typically
characterized by two dominant components. The ﬁrst is a
slowly varying Skin Conductance Level (SCL), also referred
to as the “tonic” component. The second component is the
observation of multiple Skin Conductance Responses (SCRs)
arising each from a corresponding SCR event. This component
is sometimes referred to as the “phasic” component. These two
signal types are detailed in Figure 1.

The user’s physiology explains the existence of these two
signal components. The SCRs are driven by occurrences of
SCR events, a sparse selection of events where the user has
responded with psychological arousal or excitement to stimu-
lus. The SCR events signal is denoted by the impulse train at
the bottom of Figure 1. Prior research in the psychophysiology

TABLE I: EDA Signal Notation Summary

Component
Baseline
SCR Events
SCR
Noise

Model Notation
b
x
h ∗ x
n

Description
Baseline Signal - Slowly varying skin conductance level with jump discontinuities due to motion
Skin Conductance Response Events - Signal of sparse stimulus response events from the user
Skin Conductance Response - Measured sweat expulsion resulting from the SCR events
Additive noise observed from measurement process and model mismatch

3

Fig. 2: Observation model showing the various components in the observed EDA signal.

community (e.g., [6]) has recognized that these SCR events
(i.e., user excitement events) are correlated with sudomotor
neuron bursts, resulting in a user’s eccrine glands to expel
sweat. This sweat causes changes in skin conductance in the
form of an SCR observation in the shape similar to that shown
in Figure 1. This shape is the result of expelling, pooling, and
evaporation of sweat on the surface of the user’s skin.

Additionally, this act results in some sweat being absorbed
into the surface of the user’s skin, which affects the SCL.
We consider the SCL to be a slowly varying signal. The SCL
signal can be changed by temperature, humidity, and other
environmental factors along with the physiology of the user
(e.g., thickness of the user’s skin).

In addition to the SCL, there may also be sudden shifts
in the skin conductance caused by changes in the positioning
of the sensors or the amount of contact of the sensors with
the skin, especially in the wearable sensor setting. Such
changes are often reﬂected by jump discontinuities in the skin
conductance. We account for such discontinuities, as well as
the SCL, in what we call the baseline signal component.

A. Model Deﬁnition

Let us consider an observed EDA signal, y, discretized into
T time steps. At each time step there is the possibility of an
SCR event. We denote the SCR events signal corresponding
to this content by a vector x ∈ RT , where each component
represents the intensity of the user’s reaction to the T possible
events. Whenever the user has an SCR event, prior research
has shown (e.g., [6], [10], [11]) that there are typical ways in
which the EDA measurements record conductance changes.
We denote this typical sweat response of an user by a vector
h ∈ Rt. In the past [6], [11], the resulting SCR signal has
been modeled as a linear time-invariant (LTI) system where
the SCR events signal x is convolved with the sweat response
signal h which we denote as h ∗ x ∈ Rt+T −1.

As mentioned earlier, the SCR signal h ∗ x is superimposed
with a baseline signal consisting of SCL and motion artifacts.
Denote the baseline signal as b ∈ Rt+T −1 and the errors

arising due to observation noise and model mismatch as
n ∈ Rt+T −1. These notations are summarized in Table I. The
observed EDA signal can now be represented as

y = h ∗ x + b + n.

(1)

The ﬁnal observation model is shown in Figure 2. Given prior
work on the shape of the SCR impulse response h, we assume
that the impulse response is known a priori (we discuss the
speciﬁc choice of h in Section V). We consider the SCR events
signal x, the baseline b, and noise n to all be unknown.

In this paper we propose a model for the observed EDA
signal y that accounts for both the baseline b and observation
noise n in a principled manner. This requires further speciﬁ-
cations on the signals x, b, and noise n which we detail in
the following.

B. SCR Events Signal Model

Due to physiology, there are limitations to how often hu-
mans can generate SCR events. Motivated by this, we impose
a sparsity assumption on the SCR events signal. Speciﬁcally,
we assume that there are no more than s < T events to which
a user responds signiﬁcantly. More formally, the SCR events
signal is assumed to lie in the set

X s

δ =

(cid:110)

x

(cid:12)
(cid:12) x ∈ RT , (cid:107)x − xs(cid:107)1 ≤ δ
(cid:12)

(cid:111)

,

(2)

where δ is a small constant and xs ∈ RT with exactly s non-
zero components obtained by retaining the s-largest magnitude
components of x.

The above set is the collection of vectors which can be
approximated within some distance (in terms of the (cid:96)1-norm)
δ from an exactly s-sparse signal. Notice that when δ = 0, the
above set is the set of s-sparse vectors in Rt+T −1. We note that
in most prior literature, the model for the SCR events signal
is strictly positive. Here we drop this constraint for a simpler
analysis of recovery guarantees. Our experimental results
in Section V show that even without positivity constraints
comparable performance can be achieved.

4

E. Problem Overview

The goal of this paper is to obtain the SCR events signal
x from the EDA observation signal y = h ∗ x + b + n given
the prior information that x ∈ X s
γ. We assume
that the impulse response h is known, but the baseline b, the
SCR events signal x, and the measurement noise n are all
unknown.

δ and b ∈ Bc

IV. EDA SIGNAL DECOMPOSITION

The task of recovering the true SCR events x from the
observed EDA signal y is particularly challenging due to the
presence of the baseline b. For example, consider the setting
when there is an observed signal with no baseline and no
noise, i.e., b = 0, n = 0, and y = h ∗ x. The problem
of recovering x from y simply reduces to solving an over-
determined linear system of equations given knowledge of
h. As a result, this problem can be solved with standard
deconvolution techniques given very mild assumptions on h
and without any assumptions needed on true x.

In another case, consider there is no baseline but noise is
present, i.e., b = 0, n (cid:54)= 0, and y = h ∗ x + n. This
is a standard problem of deconvolution in noise, which in
general is a difﬁcult problem to solve. But, when we consider
the added structure of the sparsity of SCR events signal x,
one could exploit this to estimate x with provable guarantees.
This setting has been explored in prior work in the ﬁeld of
compressed sensing, e.g., [18].

A. Dealing with the Baseline Signal

The main challenge here is the case where the baseline
signal is present and non-zero. One obvious approach could
be to consider the baseline as noise and follow previously
proposed deconvolution for noisy settings e.g., [18]. However,
this would likely fail because the baseline b could have very
large magnitude. Our proposed alternative is to exploit the
structure of the baseline signal to facilitate the recovery of x.
We linearly transform the baseline signal and jointly recover
the transformed baseline and x. This is often known as a
de-mixing problem, and there has been recent work on using
convex techniques for de-mixing structured signals [15], [16].
These papers have theoretical guarantees in terms of statistical
dimension. Unfortunately, these guarantees assume a speciﬁc
random signal generation model which does not hold true for
our problem setting.

Recent work has proposed a corrupted sensing approach
[25] which extends compressed sensing to a setting where
observations are corrupted with structured signals. Our prob-
lem is different from this setup on two counts: (1) Our sparse
signal is convolved with a known SCR impulse response and
(2) the baseline signal in our setting has structure that has not
yet been considered in the corrupted sensing literature. Hence,
we leave this as an interesting future direction.

B. EDA Signal Preprocessing

We propose an approach that exploits the structure of the
EDA signals to mitigate the effects of the baseline signal.

Fig. 3: An example EDA signal collected using a commercially
available wearable EDA sensor showing the impact of baseline
shifts due to movement.

C. Baseline Model

We propose a novel baseline model, inspired by the wear-
able setting where changes in the positions of sensors due to
movement may lead to rapid changes in the EDA signal. These
rapid changes, or baseline shifts, are illustrated in Figure 3
along with several SCRs. To the best of our knowledge, such
baseline shifts have not been examined by previous work on
recovering SCR events. We incorporate these baseline shifts
along with the SCL component into a baseline signal b. We
assume b changes its magnitude signiﬁcantly or has jump
discontinuities at no more than c < t + T − 1 locations. More
formally, the baseline signal is assumed to lie in the set

Bc

γ =

(cid:110)

b

(cid:12)
(cid:12) b ∈ Rt+T −1, (cid:107)Db − (Db)c(cid:107)1 ≤ γ
(cid:12)

(cid:111)

,

(3)

where D ∈ R(t+T −2)×(t+T −1) denotes the pairwise difference
matrix deﬁned by

D =



1 −1
0


...


0

0
1 −1
...
. . .
· · ·
0








0
· · ·
0
· · ·
...
. . .
1 −1

(4)

so that Db = [b1 − b2, b2 − b3, . . . , bt+T −2 − bt+T −1]
and (Db)c ∈ Rt+T −2 with exactly c non-zero components
obtained by retaining the c-largest magnitude components of
Db. Hence the baseline signal, after pairwise differencing, is
assumed to be within some distance (in terms of the (cid:96)1-norm)
γ from a c-sparse signal.

D. Bounded Noise Model

Finally, we consider the additional noise induced by the
wearable sensor recording the EDA signals as well as po-
tential model mismatch. Rather than assuming a form for
the distribution of this term, we will simply assume that the
noise and model inaccuracies are bounded by a ﬁxed value,
i.e. (cid:107)n(cid:107)2 ≤ (cid:15)/2 where (cid:15) > 0. Here the constant factor 1/2 is
included only to simplify further analysis.

020406080100120140160Time (sec)00.10.20.30.4EDA (µ S)Baseline shiftsdue to movementSCRs5

Fig. 4: Block diagram showing the SCR events signal recovery using compressed sensing based decomposition.

Namely, we can consider that the baseline signals have almost
the same consecutive components for most of the signal
elements. As a result, they can be converted to approximately
sparse signals by multiplying with the pairwise difference
matrix D deﬁned in (4).

Of course, we only have access to the observed signal,
y. Therefore, we follow a very simple approach in which
we linearly transform the observation y using the difference
matrix D as follows:

Dy = DThx + Db + Dn,

(5)

where η > 0 is a parameter that can be chosen based on
the energy of noise n as detailed in the next subsection. The
above problem is known to be a convex problem which can
be solved by using well-known convex optimization software
(e.g., CVX [27]). The ﬁnal recovery procedure based on
above discussion is summarized in Figure 4. We note that
our problem has Toeplitz structure which can be exploited for
developing computationally efﬁcient algorithm using the ideas
from matrix-free convex optimization modeling [28], [29]. We
leave this as an interesting future direction of work.

where Th denotes a (t+T −1)×T Toeplitz matrix constructed
from a vector h ∈ Rt and is deﬁned as follows:




h1

0

Th =















h1
h2
...
...
ht ht−1
ht
0
...
...
· · ·
0

(cid:124)

(cid:123)(cid:122)
T columns

· · ·
...
. . .
...

0
...
0

h1

. . .
· · · ht















(cid:125)

such that the convolution between vectors h ∈ Rt and x ∈ RT ,
denoted by h ∗ x, is a vector in Rt+T −1 and can be written
in terms of matrix-vector multiplications as h ∗ x = Thx.

With this transformation, the modiﬁed baseline signal Db is
approximately sparse because of the structure of b ∈ Bc
γ. Due
to this sparsity, the transformed baseline signal has similar
structure to the true SCR events signal x. We leverage this
fact to jointly estimate x and Db. Rearranging this term, the
observation model becomes

Dy = (cid:2)DTh

I(cid:3)

(cid:21)

(cid:20) x
Db

+ Dn,

where I denotes the identity matrix. We have transformed this
problem into estimating a vector that is approximately sparse
with s + c signiﬁcant components in Rt+T −2, where s is the
number of signiﬁcant non-zero elements in x, and c is the
number of signiﬁcant non-zeros in Db.

Using recent advances in compressed sensing [26], we
propose to solve the following problem to estimate x and Db:

min
˜x∈RT ,˜u

∈ RT +t−2

(cid:107)˜x(cid:107)1 + (cid:107)˜u(cid:107)1

subject to

(cid:13)
(cid:13)
(cid:13)
(cid:13)

Dy − [DTh I]

(cid:20)˜x
˜u

(cid:21)(cid:13)
(cid:13)
(cid:13)
(cid:13)2

≤ η,

(7)

C. Error Guarantees

The fundamental question that arises here is how well the
estimates obtained by solving above problem work. Speciﬁ-
cally, how close is the optimal solution ˆx of (7) to the true SCR
events signal x? We have the following theorem to speciﬁcally
detail the error in our recovered SCR events signal.

(6)

δ , b ∈ Bc
Theorem IV.1. Let y = h∗x+b+n, where x ∈ X s
γ.
Denote C = [DTh I] and deﬁne the coherence parameters
µh, µm, µc as

µh = max
i(cid:54)=j

µm = max
i,j

, µc = max
i(cid:54)=j

|cT

i cj|
(cid:107)ci(cid:107)2(cid:107)cj(cid:107)2

|tT

i tj|
(cid:107)ti(cid:107)2(cid:107)tj(cid:107)2
|tT

i ej|
(cid:107)ti(cid:107)2(cid:107)ej(cid:107)2

where ti, ei, and ci are the ith columns of matrices
DTh, I, and C, respectively. If (cid:107)n(cid:107) ≤ (cid:15)/2 and

s + c < max

(cid:40)

2(1 + µh)
µh + 2µc + (cid:112)µ2

h + µ2
m

(cid:41)

,

,

1 + µc
2µc

then the solution ˆx, ˆu of (7) using (cid:15) ≤ η satisﬁes

(cid:107)x − ˆx(cid:107)2 ≤ C1((cid:15) + η) + C2(δ + γ)

where C1, C2 > 0 depend on µc, µh, µm, s, and c.

Proof: See Appendix.

The above theorem states that, when the combined sparsity
of the true SCR events signal and the baseline signal after
the difference ﬁlter is small enough, the estimate of the SCR
events signal ˆx is accurate. More speciﬁcally, the (cid:96)2 norm of
the error vector (i.e., the difference between the true and the
estimated SCR events signal) is upper bounded by a quantity
which is proportional to the constants (cid:15), δ and γ, which are
part of our signal model, and the optimization parameter η,
provided that it is chosen to be greater than or equal to (cid:15).
As long as these constants are small, our approach yields an
accurate solution. In our setting, it is reasonable to assume that

6

(a)

(b)

(c)

Fig. 5: Estimation error diagrams with synthetic data for various values of number of SCR events s ∈ {5, 10, . . . , 230} and
baseline jumps c ∈ {5, 10, . . . , 350}. Panels (a), (b), and (c) correspond to scaling the magnitude of the baseline component
using α = 0.01, 0.1 and 1, respectively.

these constants are indeed small for the following reasons. The
SCR events signal x is sparse due to physiological reasons,
as previously discussed. The baseline signal should not have
too many jump discontinuities provided that the user is not
constantly moving the sensor, which causes Db to also be
sparse. Finally, (cid:15) depends on the noise power and model
mismatch and is small provided that the noise power is much
lower than the signal power and that our model assumptions
are close to reality.

The terms C1 and C2 are known to decrease with decreasing
s, c [26]. This implies that the error in the recovery decreases
as the signals become more sparse. The range of values of s+c
for which the error bounds holds depends on the coherence
parameters. These parameters critically depend on the shape
and length of h which we assume are known. It is known that
with decreasing coherence parameters µc, µh, and µm, the
recovery of a sparse signal improves [26]. All the coherence
parameters can be viewed as the maximum entries of the sub-
blocks of the matrix

G =

(cid:20)(DThΛ)T
I

(cid:21)

(cid:2)DThΛ I(cid:3) − I

=

(cid:20)(DThΛ)T DThΛ − I
DThΛ

(DThΛ)T
0

(cid:21)

,

where Λ is a diagonal matrix such that the columns of the
matrix DThΛ have unit (cid:96)2 norm. The coherence parameters
can be written in terms of sub-blocks of matrix G as follows

µh = (cid:107)(DThΛ)T DThΛ − I(cid:107)max
µm = (cid:107)DThΛ(cid:107)max
µc = max{µh, µm},

where for a matrix X, the maximum absolute entry of the
matrix is denoted by (cid:107)X(cid:107)max.

V. EXPERIMENTS

Using a combination of both synthetic and real-world EDA
data, in this section we demonstrate the feasibility and accu-
racy of our proposed compressed sensing approach to EDA
decomposition. Our synthetic data experiments sweep a wide

Fig. 6: The impulse response h was obtained by sampling the
for u ≥ 0 and f (u) = 0
function f (u) = 2
otherwise. Here τ1 = 10, τ2 = 1 and the is function sampled
at the rate of 4 samples per second in the interval u ∈ [0, 40].

τ1 − e− u

e− u

(cid:16)

(cid:17)

τ2

selection of sparsity values and baseline signal energy levels
to demonstrate SCR event recovery accuracy. Using real-world
EDA data, we then show how our technique allows for more
accurate inference of EDA events signal as compared to prior
techniques.

A. Synthetic Data Experiment

The ﬁrst experiment is dedicated to demonstrating the recov-
ery accuracy of our procedure on synthetic data. We obtained
the impulse response vector h by sampling the function f (u)
shown in Figure 6 at the rate of 4 samples per second in
the interval u ∈ [0, 40]. This choice of impulse response was
informed by prior psychophysiology literature [11]. The h
obtained in such manner lies in R160. We ﬁxed T = 240, δ =
0.01 and γ = 0.01.

For a given number of SCR events s and number of baseline
jumps c, we randomly generate x ∈ X s
γ. A
random x ∈ X s
δ is generated by ﬁrst choosing the s signiﬁcant
components uniformly at random and ﬁlling these components
with a random vector in Rs with i.i.d. exponentially distributed
entries with mean 2. This is followed by adding to it a rescaled

δ and b ∈ Bc

AverageErrorkx−ˆxk2kxk2,α=0.0150 100150200250300350c225200175150125100 75 50 25s0.10.20.30.40.50.60.7AverageErrorkx−ˆxk2kxk2,α=0.150 100150200250300350c225200175150125100 75 50 25s0.10.20.30.40.50.60.7AverageErrorkx−ˆxk2kxk2,α=150 100150200250300350c225200175150125100 75 50 25s0.10.20.30.40.50.60.70.80.9010203040Time (sec.)00.511.5hImpulse Response7

(a)

(b)

Fig. 7: Decomposition of real-world EDA data for two users in (a) and (b) respectively. Stimuli are presented to the users at
moments denoted by red dotted vertical lines. We show results for our compressed sensing approach with and without positivity
constraints for data downsampled to 4 Hz.

standard Gaussian random vector in RT with (cid:96)1 norm δ.
Similarly, a random Db was generated by ﬁrst choosing the c
signiﬁcant components uniformly at random and ﬁlling each of
these components with a standard Gaussian variable followed
by adding a rescaled standard Gaussian random vector in
Rt+T −2 with (cid:96)1 norm γ. Using these steps we generate the
observations as follows:

Dy = DThx + αDb + n,

(8)

where n is also a rescaled Gaussian random vector with (cid:96)2
norm equal to (cid:15) = 0.01. We generate multiple experiments
using different values of α, a scaling factor applied to Db
relative to DThx. These observations are then used to obtain
the estimate ˆx by solving the problem in (7) with η = 1.05(cid:15).
Figure 5 shows the average relative estimation error (cid:107)x−ˆx(cid:107)2
,
(cid:107)x(cid:107)2
where the average is obtained by 30 random observations for
various values of s and c. For baseline components with low
energy in Figure 5a, we ﬁnd that the ability to recover is almost
entirely dependent on the number of SCR events embedded
in the generated EDA signal. Regardless of the number of
baseline jumps, we ﬁnd that for fewer than 75 SCR events
in an EDA signal, we can accurately recover the SCR signal.
On the other hand, as the energy in the baseline increases, as
shown in Figures 5b and 5c, we ﬁnd that a large number
of jumps in the baseline signal can degrade our ability to
accurately recover the SCR events.

B. Experiments with Real-World EDA Data

Our second experiment examines the performance of our
methodology on real-world EDA signals. We used EDA

signals from a simple video stimulus experiment, originally
published in [7]. The video consists of six short stimulus
clips (each lasting less than 10 seconds) with differing levels
of complexity. Speciﬁcally, this video contains a baby crying
sound, a gun shot sound, a dog barking sound, the image of
a gun, and two short videos of a subject injuring themselves.
This stimulus is interspersed with silence where no audio or
video is presented to the user. The EDA data consists of EDA
traces from nine subjects (6 male, 3 female, with ages ranging
between 20 and 50 years old) who watched the same video
content in a darkened environment. The EDA was recorded
using the Affectiva Q Sensor [30] with sampling at 32 Hz.

Unlike with the synthetic data experiment, we cannot assess
relative estimation error (cid:107)x−ˆx(cid:107)2
because we do know the
(cid:107)x(cid:107)2
magnitudes of the ground-truth SCR events x. We do, however,
know the times at which the stimulus clips and periods of
silence were presented to the users. Very few SCR events
should occur during the periods of silence, while many SCR
events should occur during the stimulus clips, thus we can
use these times to assess how well our EDA decomposition
technique is able to detect SCR events. Speciﬁcally, we used
10 second windows around each stimulus and silence clip, and
then aggregated the estimated SCR event coefﬁcients between
the start of the clip and the end of the clip. These aggregated
values are then compared to a threshold to produce a binary
decision as to whether SCR events are present in the time
window. The impulse response vector h was obtained by
sampling the function f (u) = 2(e− u
τ2 ) for u ≥ 0
and f (u) = 0 otherwise. We chose τ1 = 10, τ2 = 1. For our
proposed technique and deﬁned h, we obtained estimates of

τ1 − e− u

050100150200250t0246yObservedsignal050100150200250t-0.500.51DyAfterdiﬀerenceﬁlter050100150200250t-0.0500.050.10.15ˆxRecoveredSCRevents050100150200250t-0.200.20.4h∗ˆxRecoveredSCRs050100150200250t00.050.10.15ˆxRecoveredSCReventswithpositivity050100150200250t00.20.4h∗ˆxRecoveredSCRswithpositivity050100150200250t00.511.5yObservedsignal050100150200250t-0.06-0.04-0.0200.02DyAfterdiﬀerenceﬁlter050100150200250t-0.0200.020.040.06ˆxRecoveredSCRevents050100150200250t00.050.10.150.2h∗ˆxRecoveredSCRs050100150200250t00.020.040.06ˆxRecoveredSCReventswithpositivity050100150200250t00.050.10.150.2h∗ˆxRecoveredSCRswithpositivityTABLE II: AUC values for SCR event detection at multiple
sampling rates for various approaches on real data experiment.

Sampling Compressed

Rate
4 Hz
8 Hz
32 Hz

Sensing
0.848
0.857
0.868

Compressed
Sensing (+)
0.825
0.821
0.895

Raw
cvxEDA Signal
0.539
0.493
0.514

0.622
0.771
0.819

Ledalab
0.817
0.824
0.837

SCR events signal for each user by solving (7) with η = 0.14.
To evaluate our performance we use four alternative
methodologies: (1) aggregated raw EDA signal for each user
in the stimulus and silence time windows, (2) the non-
negative deconvolution analysis technique of Benedek and
Kaernbach [6] using the Ledalab software package [31], (3) the
convex optimization approach cvxEDA proposed in [13], and
(4) a modiﬁcation of our approach with positivity constraint
for the SCR events signal1. The raw EDA analysis will com-
municate if the mean EDA signal is informative with respect to
our stimulus, while the deconvolution approach demonstrates
EDA decomposition that ignores the prominent baseline sig-
nal. The cvxEDA approach will compare our proposed model
with a recent EDA decomposition technique using convex
optimization. The approach with positivity constraints will test
whether including positivity constraints in our problem setup
improves recovery accuracy.

We perform experiments on the original 32 Hz data as
well as 4 Hz and 8 Hz downsampled versions, which are
more in-line with the sampling rates of commercially available
wearable sensors such as the Empatica E4 [5] and Microsoft
Band 2 [32] (4 and 5 Hz, respectively). For cvxEDA, the same
values τ1 = 10 and τ2 = 1 as for our approach were used2,
whereas for Ledalab, τ1 and τ2 were automatically optimized
by the software package.

Discussion of results: The result of signal decomposition
on the 4 Hz downsampled signal is shown in Figure 7. In this
ﬁgure we highlight the recovered signals with our approach
and a modiﬁed version with positivity constraints on the SCR
events signal. Figures 7a and 7b correspond to two different
users that were chosen at random from our data set. Stimuli
are presented to the users at moments denoted by red dotted
vertical lines. We see that the recovered SCR events signal
is similar for both techniques except for the events with
small negative amplitudes when no positivity constraints are
enforced. The reconstructed SCR signal h ∗ ˆx using both
approaches are also shown. Overall, we ﬁnd that our proposed
approach performs similarly to its variation with positivity
constraints.

Further, aggregating the accuracy across all nine users, we
present the Receiver Operating Characteristic (ROC) curve
in Figure 8, which shows the detection rate for any given
false alarm rate at the sampling rate of 4 Hz. We summarize
the ROC curve using the Area Under the Curve (AUC).

1Speciﬁcally, we solve problem (7) with positivity constraint x ≥ 0.
2cvxEDA also requires speciﬁcation of the sampling interval δ, which was
set to 1/sampling frequency, and other parameters δ0 , α, and γ, which were
set to the default values in the software package.

8

Fig. 8: ROC curves for real data SCR event detection experi-
ment at the sampling rate of 4 Hz. Our compressed sensing-
based approaches is compared with a variation of our approach
with positivity constraints,
the non-negative deconvolution
approach in Ledalab, the cvxEDA convex optimization based
approach, and the raw EDA signal.

We ﬁnd that our compressed sensing based decomposition
(AUC = 0.848) and its variation with positivity constraints
(AUC = 0.825) perform better than both the non-negative
deconvolution method in Ledalab (AUC = 0.817) and the
convex optimization based cvxEDA approach (AUC = 0.622).
Another insight from these results is that using the raw EDA
traces results in accuracy roughly no better than random
guessing (i.e., detection rate equal to the false alarm rate),
showing the need for processing of the observed EDA signals.
The results at various sampling rates are shown in Table II.
We see that our scheme gives better performance than all other
schemes at sampling rates 4 Hz and 8 Hz. This is an important
regime when considering EDA observations from power and
storage-constrained wearables. Our observations also suggest
that, at these sampling rates, adding positivity constraints to
our approach does not necessarily improve accuracy. In fact, at
4 Hz and 8 Hz, adding positivity constraints actually lowered
the AUC. The only improvements for the positivity constrained
techniques was at a sampling rate of 32 Hz.

VI. CONCLUSIONS

In this work we proposed a novel compressed sensing
based framework for processing of EDA signals. The proposed
framework explicitly models the baseline signal and allows
for recovery of the users responses via simple pre-processing
followed by compressed sensing based decomposition. We also
provided theoretical error bounds on the accuracy of the pro-
posed recovery procedure. Our approach accurately recovers
SCR events in experiments on simulated data. Furthermore,
our recovery procedure also outperforms existing recovery
procedures for an SCR event detection task on real-world EDA
data obtained from a video stimulus experiment.

00.20.40.60.81False Alarm Rate00.10.20.30.40.50.60.70.80.91Detection RateCompressed sensingCompressed sensing (+)cvxEDARaw SignalLedalabFuture works include considering modiﬁed EDA signal
models that vary the shape of the impulse response with time
and varied noise models, developing computationally efﬁcient
algorithms that exploit the Toeplitz structure, exploring the
possibility of better recovery guarantees by considering ran-
dom signal models and with positivity constraints.

APPENDIX

Proof of Theorem IV.1:

The proof is a straightforward extension of the following

theorem from [26]:

Theorem A.1 ( [26], Thm. 4 ). Let t = Cw + z, with C =
[A B], wT = [xT uT ], and (cid:107)z(cid:107)2 ≤ (cid:15). Deﬁne the coherence
parameters µa, µb, µm, and µc for the dictionary C as

µa = max
i(cid:54)=j

, µb = max
i(cid:54)=j

|aT

i aj|
(cid:107)ai(cid:107)2(cid:107)aj(cid:107)2
|aT

µm = max
i,j

i bj|
(cid:107)ai(cid:107)2(cid:107)bj(cid:107)2
Assume µb ≤ µa without loss of generality. If

, µc = max
i(cid:54)=j

|bT

i bj|
(cid:107)bi(cid:107)2(cid:107)bj(cid:107)2
|cT
i cj|
(cid:107)ci(cid:107)2(cid:107)cj(cid:107)2

(cid:40)

s + c < max

2(1 + µa)
µa + 2µc + (cid:112)µ2

a + µ2
m

,

1 + µc
2µc

(cid:41)

(9)

then the solution of ˆw

min
˜w
subject to

(cid:107) ˜w(cid:107)1

(cid:107)t − C ˜w(cid:107)2 ≤ η,

(10)

using (cid:15) ≤ η satisﬁes

(cid:107)w − ˆw(cid:107)2 ≤ C1((cid:15) + η) + C2(cid:107)w − wn+s(cid:107)1

where C1, C2 > 0 depend on µa, µb, µm, µc, s, and c.

We use the above Theorem A.1 with t = Dy, A =
DTh, B = I, z = Dn, and wT = [xT u] with u = Db.
First we show that the (cid:96)2 norm of the noise z satisﬁes the
assumption in Theorem A.1. This can be easily seen as follows

(cid:107)z(cid:107)2 = (cid:107)Dn(cid:107)2

≤ (cid:107)D(cid:107)2(cid:107)n(cid:107)2
≤ 2((cid:15)/2) = (cid:15),

where the last inequality is due the fact that (cid:107)D(cid:107)2 ≤ 2 and
(cid:107)n(cid:107)2 ≤ (cid:15)/2 by our model assumption. Also, as B = I is an
orthonormal matrix, it is easy to see that µb = 0. Since µa
is strictly positive under our model assumption, the condition
µb ≤ µa is also satisﬁed. Further, since we can write (cid:107) ˜w(cid:107)1 =
(cid:107)˜x(cid:107)1 + (cid:107)˜u(cid:107)1, the optimization problem (10) in Theorem A.1
takes the following form:

min
˜x∈RT ,˜u∈RT +t−2

(cid:107)˜x(cid:107)1 + (cid:107)˜u(cid:107)1

subject to

(cid:13)
(cid:13)
(cid:13)
(cid:13)

Dy − [DTh I]

(cid:20)˜x
˜u

(cid:21)(cid:13)
(cid:13)
(cid:13)
(cid:13)2

≤ η

The above problem is exactly same as the problem in (7),
for which error bounds are outlined in Theorem IV.1. This
essentially establishes that Theorem A.1 can be used to obtain
the recovery guarantees of problem (7). Provided that the

9

combined sparsity s + c satisﬁes condition (9) and we choose
η such that it satisﬁes (cid:15) ≤ η, we have the following bound
from Theorem A.1:
(cid:113)

(cid:107)w − ˆw(cid:107)2 =

(cid:107)x − ˆx(cid:107)2

2 + (cid:107)Db − ˆu(cid:107)2
2

≤ C1((cid:15) + η) + C2(cid:107)w − wn+s(cid:107)1
≤ C1((cid:15) + η) + C2 {(cid:107)x − xs(cid:107)1 + (cid:107)b − bc(cid:107)1}

Further, combining the above inequality with the fact that

(cid:113)

(cid:107)x − ˆx(cid:107)2

2 + (cid:107)Db − ˆu(cid:107)2

2 ≥ (cid:107)x − ˆx(cid:107)2,

(cid:107)w − ˆw(cid:107)2 =

we have arrive at

(cid:107)x − ˆx(cid:107)2 ≤ C1((cid:15) + η) + C2 {(cid:107)x − xs(cid:107)1 + (cid:107)b − bc(cid:107)1} ,

which, by our model assumption, can be reduced to

(cid:107)x − ˆx(cid:107)2 ≤ C1((cid:15) + η) + C2(δ + γ).

The coherence parameters µh, µm, and µc in Theorem IV.1
are equivalent to coherence parameters µa, µm, and µc re-
spectively in Theorem A.1.

REFERENCES

[1] N. Taylor and C. Machado-Moreira, “Regional variations in transepi-
dermal water loss, eccrine sweat gland density, sweat secretion rates
and electrolyte composition in resting and exercising humans,” Extrem.
Physiol. Med., vol. 2, p. 4, 2013.

[2] T. Nishiyama et al., “Irregular activation of individual sweat glands in
human sole observed by a videomicroscopy,” Autom. Neurosci.: Basic
Clin., vol. 88, pp. 117–126, 2001.

[3] B. Sidis, “The nature and cause of the galvanic phenomenon,” J. Abnorm.

Psychol., vol. 5, no. 2, pp. 69–74, 1910.

[4] “Liberate yourself from the lab: Q Sensor measures EDA in the wild,”

Affectiva Inc., White Paper, 2012.

[5] M. Garbarino et al., “Empatica e3 - a wearable wireless multi-sensor
device for real-time computerized biofeedback and data acquisition,” in
Proc. 4th Int. Conf. Wirel. Mob. Commun. Healthc., 2014, pp. 39–42.

[6] M. Benedek, and C. Kaernbach, “Decomposition of skin conduc-
tance data by means of nonnegative deconvolution,” Psychophysiology,
vol. 47, pp. 647–658, 2010.

[7] F. Silveira et al., “Predicting audience responses to movie content from
electro-dermal activity signals,” in Proc. ACM Int. Jt. Conf. Pervasive
Ubiquitous Comput., 2013, pp. 707–716.

[8] W. Lian et al., “Modeling correlated arrival events with latent semi-
Markov processes,” in Proc. 31st Int. Conf. Mach. Learn., 2014, pp.
396–404.

[9] H. Lu et al., “StressSense: Detecting stress in unconstrained acoustic
environments using smartphones,” in Proc. ACM Conf. Ubiquitous
Comput., 2012, pp. 351–360.

[10] C. Lim et al., “Decomposing skin conductance into tonic and phasic
components,” Int. J. Psychophysiol., vol. 25, pp. 97–109, 1997.
[11] D. Alexander et al., “Separating individual skin conductance responses
in a short interstimulus-interval paradigm,” J. Neurosci. Methods, vol.
146, pp. 116–123, 2005.

[12] D. Bach et al., “Dynamic causal modeling of spontenous ﬂuctuations in

skin conductance,” Psychophysiology, vol. 48, pp. 1–6, 2010.

[13] A. Greco et al., “cvxEDA: A convex optimization approach to electro-
dermal activity processing,” IEEE Trans. Biomed. Eng., vol. 63, no. 4,
pp. 797–804, 2016.

[14] T. Chaspari et al., “Sparse representation of electrodermal activity with
knowledge-driven dictionaries,” IEEE Trans. Biomed. Eng., vol. 62,
no. 3, pp. 960–971, 2015.

[15] M. B. McCoy and J. A. Tropp, “The achievable performance of convex

demixing,” arXiv preprint arXiv:1309.7478 [cs.IT], 2013.

[16] ——, “Sharp recovery bounds for convex demixing, with applications,”

Found. Comput. Math., vol. 14, no. 3, pp. 503–567, 2014.

[17] D. L. Donoho, “Compressed sensing,” IEEE Trans. Inf. Theory, vol. 52,

no. 4, pp. 1289–1306, 2006.

10

[18] J. Haupt et al., “Toeplitz compressed sensing matrices with applications
to sparse channel estimation,” IEEE Trans. Inf. Theory, vol. 56, no. 11,
pp. 5862–5875, 2010.

[19] J. Romberg, “Compressive sensing by random convolution,” SIAM J.

Imaging Sci., vol. 2, no. 4, pp. 1098–1128, 2009.

[20] H. Rauhut et al., “Restricted isometries for partial random circulant
matrices,” Appl. Comput. Harmon. Anal., vol. 32, no. 2, pp. 242–254,
2012.

[21] W. Yin et al., “Practical compressive sensing with Toeplitz and circulant
matrices,” in Proc. Vis. Commun. Image Process. Conf., 2010, p.
77440K.

[22] C. R. Berger et al., “Sparse channel estimation for multicarrier under-
water acoustic communication: From subspace methods to compressed
sensing,” IEEE Trans. Signal Process., vol. 58, no. 3, pp. 1708–1721,
2010.

[23] H. Critchley et al., “Neural activity relating to generation and represen-
tation of galvanic skin conductance responses: A functional magnetic
resonance imaging study,” J. Neurosci., vol. 20, no. 8, pp. 3033–3040,
2000.

[24] J. Healey et al., “Out of the lab and into the fray: Towards modeling
emotion in everyday life,” in Proc. 8th Int. Conf. Pervasive Comput.,
2010, pp. 156–173.

[25] R. Foygel and L. Mackey, “Corrupted sensing: Novel guarantees for
separating structured signals,” IEEE Trans. Inf. Theory, vol. 60, no. 2,
pp. 1223–1247, 2014.

[26] C. Studer and R. G. Baraniuk, “Stable restoration and separation of
approximately sparse signals,” Appl. Comput. Harmon. Anal., vol. 37,
no. 1, pp. 12–35, 2014.

[27] M. Grant and S. Boyd, “CVX: Matlab software for disciplined
convex programming, version 2.1,” Mar. 2014. [Online]. Available:
http://cvxr.com/cvx

[28] S. Diamond and S. Boyd, “Matrix-free convex optimization modeling,”

arXiv preprint arXiv:1506.00760 [math.OC], 2015.

[29] S. Becker et al., “TFOCS: Templates for ﬁrst-order conic solvers,”

2012. [Online]. Available: http://cvxr.com/tfocs/

[30] “Affectiva.” [Online]. Available: http://www.affectiva.com/
[31] “Ledalab MATLAB toolbox.” [Online]. Available: http://www.ledalab.

de/

[32] “Microsoft Band SDK.”
microsoftband.com/bandsdk

[Online]. Available:

https://developer.
