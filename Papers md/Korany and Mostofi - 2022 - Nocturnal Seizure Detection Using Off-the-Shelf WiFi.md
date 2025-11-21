# Korany and Mostofi - 2022 - Nocturnal Seizure Detection Using Off-the-Shelf WiFi

6996

IEEE INTERNET OF THINGS JOURNAL, VOL. 9, NO. 9, MAY 1, 2022

Nocturnal Seizure Detection Using
Off-the-Shelf WiFi

Belal Korany , Member, IEEE, and Yasamin Mostoﬁ , Fellow, IEEE

Abstract—The detection of nocturnal seizures in epilepsy
patients is essential, both for the quick management of the seizure
complications, and for the assessment of the ongoing seizure treat-
ment. Traditional seizure detection products (e.g., wearables),
however, are either very costly, uncomfortable, or unreliable. In
this article, we then propose to utilize everyday WiFi signals
for robust, fast, and noninvasive detection of nocturnal seizures.
We ﬁrst present a new and rigorous mathematical character-
ization for the spectral content/bandwidth of the WiFi signal,
measured on a WiFi device placed near a sleeping patient, dur-
ing different kinds of sleep motions: seizures, normal movements
(e.g., posture adjustments), and breathing. Based on this math-
ematical modeling, we propose a novel pipeline for processing
the received WiFi signals to robustly detect all nocturnal non-
breathing movements, and then classify them into normal body
movements or seizures. In order to validate this, we carry out
extensive experiments in seven different typical bedroom loca-
tions, where a set of 20 actors simulate the state of having seizures
(a total of 260 instances), as well as normal sleep movements (a
total of 410 instances). Our proposed system detects 93.85% of
the seizures with a mean response time (MRT) of only 5.69 s
since the onset of the seizure. Moreover, our proposed system
achieves a probability of false alarm of only 0.0097, when clas-
sifying normal sleep movements. Overall, our new mathematical
modeling and experimental results show the great potential the
ubiquitous WiFi signals have for detecting nocturnal seizures,
which can provide better support for epilepsy patients and their
caregivers.

Index Terms—Breathing monitoring, seizure detection, sleep

monitoring, WiFi.

I. INTRODUCTION

E PILEPSY is a neurological disorder that causes a patient

to have different kinds of seizures. It has gained a lot
of attention in the public health domain since it is one of the
most common neurological disorders, causing a large number
of people to suffer from persistent health and socioeconomic
issues. The World Health Organization (WHO) estimates that
50 million people around the world suffer from epilepsy, as
of 2019 [1]. Epilepsy is treated using different anti-epileptic
drugs (AEDs), depending on the speciﬁc type of seizure it

Manuscript received March 24, 2021; revised May 27, 2021 and July 27,
2021; accepted September 15, 2021. Date of publication September 27, 2021;
date of current version April 25, 2022. This work was supported in part by
NSF NeTS under Award 1816931, and in part by ONR under Award N00014-
20-1-2779. (Corresponding author: Belal Korany.)

This work involved human subjects or animals in its research. Approval
of all ethical and experimental procedures and protocols was granted by the
Institutional Review Board (IRB) Committee at UCSB.

The authors are with the Department of Electrical and Computer
Engineering, University of California at Santa Barbara, Santa Barbara,
CA 93106 USA (e-mail: belalkorany@ece.ucsb.edu; ymostoﬁ@ece.ucsb.edu).

Digital Object Identiﬁer 10.1109/JIOT.2021.3115505

is causing. The assessment of the ongoing seizure treatment
requires the caregivers of the patient to continuously monitor
and document the seizures (i.e., their frequency and duration).
Seizures which take place during night sleep medically known
as Nocturnal Seizures then pose a higher risk for epilepsy
patients, since they can go unobserved by the caregivers [2].
This necessitates the need for in-home seizure monitoring
devices that can detect nocturnal seizures in epilepsy patients
and alert their caregivers. The presence of a caregiver dur-
ing a seizure is also very important so that they can help the
patient, prevent them from falling, administer rescue medica-
tions (if necessary), and/or call for medical help if the seizure
is lasting for too long. Moreover, patients who continue to
have unattended nocturnal seizures have a higher risk of death
due to the complications caused by the unattended seizures,
a condition that is medically known as sudden unexpected
death in epilepsy (SUDEP) [2]. SUDEP has been found to
usually follow a speciﬁc type of seizures, called tonic-clonic
seizures, which happens more frequently than other types dur-
ing sleep [3]. Tonic-clonic seizures are characterized by a tonic
phase, in which the body muscles stiffen for a few seconds,
followed by a clonic phase, in which the body muscles rapidly
and rhythmically jerk for 1–3 min [4].1

In order to detect nocturnal seizures, several products have
been made available, such as smart watches [5], smart mat-
tresses [6], and cameras [7]. Smart watches measure the
acceleration of the wrist to detect violent jerky movements,
while smart mattresses measure the changes in the pressure on
the mattress. However, the large cost of these products pro-
hibits their widespread use. For instance, smart watches (e.g.,
Apple Watch and Embrace2 [5]) and the MP5 bed motion
monitoring unit [6] all cost more than U.S. $250 per unit.
Moreover, the comfort of patients and the reliability of detec-
tion of some of these products have been questioned by several
studies, as we shall discuss in Section II.

On the other hand, radio-frequency (RF) signals (e.g., WiFi)
have become ubiquitous these days, due to the rapid growth
of the number of wireless devices. These signals interact and
bounce off of different objects in the environment, thereby car-
rying crucial information about them. Consequently, researchers
in the RF sensing community have utilized RF signals to realize
various applications, e.g., localization and tracking [8], imag-
ing [9], health monitoring [10], occupancy estimation [11],
activity recognition [12], and others.

1This article will focus on tonic-clonic seizures. Therefore, unless otherwise
stated, we henceforth use the term “seizure” to refer to a tonic-clonic seizure.

2327-4662 c(cid:2) 2021 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply. 

KORANY AND MOSTOFI: NOCTURNAL SEIZURE DETECTION USING OFF-THE-SHELF WiFi

6997

In this article, we propose to utilize RF signals to detect
nocturnal seizures in epilepsy patients. Using everyday RF
signals, i.e., WiFi signals, for such a task has several advan-
tages. First, it is an affordable solution when compared to
the high cost of the existing approaches. It is also contact-
less since it does not require the patient to wear any device
or have units installed under their mattress. Moreover, an RF-
based system, unlike cameras, does not require any lighting
conditions to accurately achieve its task. In this article, we
then propose to use a pair of WiFi transceivers to detect noc-
turnal seizures. More speciﬁcally, we propose a robust, fast,
and theoretically driven approach to process the WiFi channel
state information (CSI) measured on a WiFi receiver device
placed near a sleeping patient, in order to extract their motion
information and decide whether the motion indicates a seizure
or not. By “robust,” we mean that our proposed framework
has a very low probability of false alarm, i.e., it has a very
low probability of declaring a seizure when there is none,
while detecting all the seizures with a high probability. This
is important as the sleeping person may have several normal
body movements, such as pose adjustments, and they should
not be classiﬁed as a seizure. By “fast,” we mean that our
system detects a seizure in a very short time since its onset,
in order to alert the caregiver in a timely manner. Finally, by
“theoretically driven,” we mean that our proposed approach is
backed by a new and rigorous mathematical characterization of
the spectral content of the received signal during sleep-related
movements: seizure, normal body movements, and breathing.
In our setup, a pair of WiFi transceivers (e.g., two laptops)
is placed near the patient’s bed. The WiFi receiver measures
both the WiFi CSI-squared magnitude signal and the phase
difference between the antennas of the receiver (a total of
three antennas) for the purpose of seizure detection. We then
propose a new mathematical characterization for the spectral
content of the received WiFi signal during motions relevant
to sleep, i.e., seizure, normal sleep movements, and breathing,
and show how our spectral analysis can be used to design a
new and robust seizure detection pipeline. We next explicitly
discuss the contributions of this article.

Statement of Contributions:
1) We develop a novel and rigorous mathematical model
for the received CSI-squared magnitude signal as well
as the CSI antenna phase difference during different
kinds of motions relevant to sleep: seizure, normal body
movements, and breathing. More speciﬁcally, we ﬁrst
show that both the WiFi CSI-squared magnitude and
phase difference signals are frequency-modulated by
the body motion. We then show our main theoretical
contribution: to mathematically characterize the spec-
tral content/bandwidth of the WiFi CSI signal during
the aforementioned motions. Based on this new spec-
tral analysis, we then show that the bandwidth of the
received WiFi signal can be used to robustly and efﬁ-
ciently differentiate seizure events from normal sleep
movements.

2) Based on our theoretical analysis, we propose a new
pipeline for the detection of nocturnal seizures using
WiFi CSI, which consists of the following three steps.

First, our data preprocessing pipeline denoises the raw
measured CSI and selects the least noisy data streams of
different receiver antennas/subcarriers using our spectral
analysis ﬁndings. Then, our event detection algorithm
detects any kind of nonbreathing motion, based on the
spectral content of the denoised CSI. Finally, an event
classiﬁcation algorithm decides whether a detected event
is a seizure or normal body movement, based on the
bandwidth of the WiFi signal during the event.

3) In order to validate our proposed framework, we carry
out extensive experiments on 20 test subjects (5 females
and 15 males) in seven different
locations of typi-
cal bedrooms, where the subjects act out seizures and
normal sleep movements while we collect WiFi CSI
data. In total, we collect 260 different seizure instances
and 410 different normal nonbreathing sleep movement
instances. Our system was able to detect 93.85% of the
seizures with an average response time (RT) of 5.69 s
since the onset of the seizure, which is much less than
the state of the art, as we shall see in Section VII.
Moreover, in terms of false alarm rate (the probabil-
ity that a normal sleep event is classiﬁed as seizure),
our system had a false alarm probability of 0.0097,
which indicates its robust performance. We further study
the impact of varying several different parameters (e.g.,
TX/RX positions) on the performance of our proposed
system. Overall, our results establish that our proposed
mathematically motivated system is fast and robust and
is also independent of person’s pose/orientation.
As we shall see, our derivations can also contribute beyond
seizure detection, in the general area of breathing-based RF
sensing, since they show that a common assumption regarding
the frequency content of the received signal during nor-
mal breathing is not always correct, explaining some of the
unexplained observations in the corresponding literature.

Remark 1: In this article, we use the term normal sleep
events to refer to normal nonbreathing body movements dur-
ing sleep, such as pose adjustments, stretching, scratching,
coughing, sneezing, jerking, and others.

II. RELATED WORK

To the best of our knowledge, this work is the ﬁrst to use
RF signals for seizure detection. In this section, we summarize
the state of the art related to different aspects of our problem
of interest.

A. WiFi-Based Vital Signs Monitoring

There has been a great body of work on utilizing wireless
signals for vital signs monitoring, e.g., using high-bandwidth
radar [13], mmWave [14], or WiFi. In this article, we are
interested in utilizing off-the-shelf WiFi devices for seizure
detection.

Several papers have utilized the ﬁne-grained WiFi
CSI magnitude data for breathing rate and/or heart rate
estimation [15], [16]. Other researchers utilized the CSI phase
difference between receiver antennas to achieve the same
task [17], [18]. None of such RF-based existing works,

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply. 

6998

IEEE INTERNET OF THINGS JOURNAL, VOL. 9, NO. 9, MAY 1, 2022

however, is on seizure detection. Nevertheless, our ﬁndings
can have a signiﬁcant impact on such work for the following
reason. All the existing WiFi CSI-based breathing rate esti-
mation works assume that the bandwidth of the received CSI
signal, in the vicinity of a person who is breathing normally,
is the same as the breathing rate. In order for us to develop
a robust nocturnal seizure detection system, we also need to
fundamentally understand and characterize the spectral con-
tent of normal breathing in this article. As we shall see, using
our proposed rigorous mathematical analysis, the bandwidth
of the WiFi signal caused by normal breathing is not neces-
sarily the same as the breathing rate and can be higher. As
such, this article can contribute to the ongoing research that
is using breathing signals for other health monitoring appli-
cations. In fact, our mathematical analysis can immediately
explain the observation made in [16] that the quality of the
breathing rate estimation, which was designed assuming the
signal bandwidth is the same as the breathing rate, degrades
at some locations relative to others. Similarly, it can explain
the unexplained frequency peaks that were observed in [19]
and were attributed to noise.

B. Seizure Detection and Analysis

In-home seizure detection is an important topic that has
gained a lot of attention in the research community. Most
seizure detection algorithms in the literature rely on the detec-
tion of the motion of the clonic phase of the tonic-clonic
seizure via accelerometry [20]–[22], and/or video analy-
sis [23], [24]. In accelerometry, a wearable accelerometer is
attached to one or more of the patient’s body parts, such as
wrist, ankle, and/or chest. In addition to their high cost, wear-
able devices are usually not well tolerated by certain groups of
patients, such as children and people with intellectual disabili-
ties, who usually try to dislodge the devices [24]. Furthermore,
Beniczky et al. [25] concluded that commercial wrist-worn
watches have a seizure detection accuracy of 89.7%, which
is not very high. Video-based seizure detection has shown
good detection accuracy of more than 95%, but with a high
false alarm rate of 0.78 events per night [23], [24]. However,
video-based detection requires a clear unobstructed view of the
patient with good lighting conditions, which may not always
be possible, and further invade the patient’s privacy. Overall,
an accurate, noninvasive, comfortable, and affordable way of
detecting nocturnal seizures is lacking, which is the main
motivation for this article.

C. Sleep Analysis

People engage in different kinds of normal nonbreathing
movements during sleep, such as posture adjustments and
limb jerks. An important aspect of our proposed system is
to minimize false alarms by identifying such normal events
and distinguishing them from seizure events. Hence, we utilize
some of the results of the sleep analysis medical literature in
order to design our system. For instance, Coussens et al. [26]
and De Koninck et al. [27] studied the duration and rate of
normal events during sleep, using accelerometry and video
analysis, concluding that these events typically happen at a

Fig. 1.
Illustration of the application scenario. A pair of WiFi transceivers
collects WiFi CSI measurements while a person is sleeping, in order to analyze
their sleep motions and detect if they are having a seizure. Note that our design
does not assume or require that the person lies on their back, and they can be
in any pose/orientation. Furthermore, the TX/RX can be in any conﬁguration
as well.

rate of three events per hour, last for an average of 8–10 s,
and can go up to 15 s. Walch et al. [28] have published an
online data set of accelerometry data of 31 healthy adults dur-
ing their sleep. We shall utilize such results/data in this article
for our spectral analysis of WiFi signals during normal sleep.

III. SIGNAL MODEL

In this section, we develop a mathematical model for the
received WiFi CSI in a general setting, an example of which is
shown in Fig. 1. More speciﬁcally, a person is lying down on
a bed in any generic pose while a WiFi transmitter (Tx) emits
wireless signals that are reﬂected off of the person’s body and
received by a WiFi receiver (Rx). We ﬁrst derive closed-form
expressions for the WiFi CSI-squared magnitude and the WiFi
CSI phase difference signals, during a generic motion pattern
of the body, in this part. In Section IV, we then use this model
to provide a new and rigorous mathematical analysis of the
spectral content of the WiFi signals during speciﬁc kinds of
sleep motions relevant to this article, i.e., breathing, seizures,
and normal sleep movements.

Let c(t) denote the complex baseband received signal at the
Rx, which can be decomposed into the direct path from the
Tx to the Rx, and the reﬂected path off of the person’s moving
body. More speciﬁcally, c(t) can be written as [8]
(cid:8)

c(t) = αdejμd
(cid:2) (cid:3)(cid:4) (cid:5)
direct path

j
+ αre
(cid:2)

(cid:7)

(cid:6)
μr+ 2π
λ ψ
(cid:3)(cid:4)
reﬂected path

v(t)dt

(cid:5)

(1)

where αd and μd are the amplitude and phase of the direct
path from the Tx to the Rx, αr is the amplitude of the reﬂected
path arriving at the Rx, μr is the phase of the reﬂected path
at time t = 0, and ψ = 2 cos(φ) is a scale parameter that
depends on the location of the bed/person with respect to the
Tx and Rx. Consider the ellipse whose foci are the Tx and
Rx, which passes through the person’s body, φ is then the
angle between the line connecting the person to the Tx (or
Rx) and the perpendicular line to this ellipse at the point that
it passes through the person’s body (see Fig. 1). v(t) is the
instantaneous speed component of the body motion along the
perpendicular line to the ellipse, and λ is the wavelength.

Note that the value of ψ depends on the scene conﬁgura-
tion, i.e., the relative location of the bed with respect to the
Tx and Rx, and does not depend on the person’s posture and

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply. 

KORANY AND MOSTOFI: NOCTURNAL SEIZURE DETECTION USING OFF-THE-SHELF WiFi

6999

orientation while sleeping. In other words, if the width of the
bed is small as compared to the Tx–Rx distance, or the person
does not drastically move from one side of the bed to the other
(which is common in practice), the sleeping person’s general
location with respect to the Tx and the Rx does not drasti-
cally change, and hence, ψ can be taken as a constant and
can be calculated only once upon Tx–Rx placement. The per-
son can change their pose/orientation several times, but those
movements will not affect the value of ψ.

(cid:7)

For simplicity of notation, we deﬁne β = (2π ψ/λ), and
v(t)dt. Hence, the phase of the reﬂected path at the Rx
d(t) =
becomes μr + βd(t). Next, we derive closed-form expressions
for the squared magnitude and phase of c(t) to understand the
information they carry about the body’s motion.

Remark 2: The static multipath in the environment does
not affect this analysis since all the static multipath can be
integrated into the ﬁrst term of (1). This indicates that the
performance of the system is agnostic to the deployment
environment. This observation will be further validated by
our extensive experiments in several different locations and
real-world scenarios, as we shall see in Section VII.

Squared Magnitude of c(t): The squared magnitude of c(t)
can be written, after a straightforward derivation, as follows:

∗(t) = α2
d

|c(t)|2 = c(t)c

+ Am cos(βd(t) + (cid:8)μm)

+ α2
r
where Am = 2αdαr, and (cid:8)μm = μr − μd is the difference
between the initial phase of the reﬂected path and the phase
of the direct path. Since the dc component of |c(t)|2 does not
carry any information about the motion of the body, we sub-
tract the dc term (which can be easily implemented in practice)
to have the following:

(2)

sm(t) = Am cos

β

v(t)dt + (cid:8)μm

(3)

(cid:9)

(cid:10)

(cid:11)
.

For the ease of discussion, we then refer to sm(t) as the

squared magnitude signal in the rest of the article.

Phase of c(t): Without loss of generality, we analyze the
phase of the scaled signal c(cid:4)(t) = e−jμd c(t)/αd. This scaling
shifts the phase of c(t) by a constant amount, preserving the
time-varying behavior of the phase of c(t) which carries the
motion information of the body. Let θ (t) be the phase of c(cid:4)(t).
It is easy to conﬁrm that

θ (t) = tan

−1

(cid:12) αr
αd
1 + αr
αd

sin(βd(t) + (cid:8)μm)

cos(βd(t) + (cid:8)μm)

(cid:13)

.

(4)

Due to its longer length and the reﬂection loss at the body,
we can assume that the amplitude of the reﬂected path is much
less than that of the direct path, i.e., (αr/αd) (cid:5) 1. In such a
case, θ (t) can be approximated as

≈

θ (t) ≈ tan(θ (t))
αr
αd
αr
αd
αr
αd

≈

=

sin(βd(t) + (cid:8)μm)

sin(βd(t) + (cid:8)μm) −

sin(βd(t) + (cid:8)μm)

(cid:9)

1 −

αr
αd

(cid:11)

cos(βd(t) + (cid:8)μm)

α2
r
2α2
d

sin(2βd(t) + 2(cid:8)μm)

(5)

where the ﬁrst-order Taylor approximation (1 + x)−1 ≈ 1 − x
for x (cid:5) 1 is used in the second line to derive (5), since
(αr/αd) (cid:5) 1.

In practice, the phase measurements on off-the-shelf WiFi
devices are corrupted by multiple sources of error, such as car-
rier frequency offset (CFO) and sampling time offset (STO),
rendering these phase measurements unreliable [29]. However,
since different antennas of the same WiFi card share the same
oscillator, those errors are common to all the antennas of the
same card, and as such, the phase difference between two
antennas of the same card carries stable phase information, as
has been used in the literature. In this article, we also rely
on the phase difference between the antennas of one receiver
WiFi card. Let θi(t) be the phase of the CSI at the ith antenna
of the Rx. The phase difference between the ith and the jth
receiver antennas can then be written as
(cid:10)

sp(t) = θi(t) − θj(t) = Ap cos(β

v(t)dt + (cid:8)μp)

(6)

where Ap = 2(αr/αd) sin(0.5((cid:8)μm,i − (cid:8)μm,j)), (cid:8)μp =
0.5((cid:8)μm,i + (cid:8)μm,j), and (cid:8)μm,i and (cid:8)μm,j are the values
of (cid:8)μm at the ith and the jth receiver antennas, respectively.
Equation (6) shows that as long as (cid:8)μm,i (cid:7)= (cid:8)μm,j (which
depends on the direct and reﬂected path lengths to the receiver
antennas as well as the wavelength), the phase difference
between the receiver antennas has a similar structure, in terms
of the information it carries about the body movements, as the
squared magnitude of the received signals (3).

(cid:7)

Body Acting as an FM Radio: Frequency modulation (FM)
is a classic analog transmission technique,
introduced in
1902 [30], to ensure robust transmissions for radio applica-
tions. A typical FM transmitted signal will have the form
m(t)dt), where m(t) is the signal of interest
cos(2π fct + kf
to be transmitted, fc is the carrier frequency, and kf is the
modulation index constant. As can be seen, both the squared
magnitude signal of (3) and the phase difference signal of (6)
can be interpreted as FM signals, in which v(t) is the mod-
ulating signal and fc = 0. In other words, the moving body
part (e.g., the chest) can be thought of as modulating the body
motion into an FM signal that is then received by the WiFi
receiver. This way of interpretation allows us to delve into the
classic mathematical analysis of FM signals for our system
design, as we shall see in the next section. However, one dif-
ference with a typical FM signal is the existence of the (cid:8)μm
term in (3) [or (cid:8)μp in (6)]. We shall see the impact of such
a term in the spectral analysis of the next section.

IV. SPECTRAL ANALYSIS OF THE RECEIVED SIGNAL

In this section, we analyze the received squared magni-
tude signal (or, equivalently, the phase difference signal) of
Section III, for different kinds of nocturnal body movements:
breathing, seizures, and normal sleep events (e.g., posture shifts,
moving limbs, etc.). More speciﬁcally, we develop our ﬁrst
major contribution: to mathematically characterize the spectral
content/bandwidth of the received signal for each of the afore-
mentioned three types of motions. We shall see that, due to
the different body motion characteristics during a seizure as
compared to normal sleep events, the spectral content of the

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply. 

7000

IEEE INTERNET OF THINGS JOURNAL, VOL. 9, NO. 9, MAY 1, 2022

(cid:14)

(cid:7)

received signals can be used to design a robust nocturnal seizure
detection system, as we shall see in Section V.

Let y(t) = A cos(β

v(t)dt + (cid:8)μ) represent a general form
for either the squared magnitude signal of (3) or the phase
difference signal of (6). First, assume that v(t) is a sinusoidal
signal of the form v(t) = vmax cos(ωot). This assumption
applies to both the seizure and respiration cases. The following
characterizes the Fourier response of y(t).

Theorem 1: Consider the signal y(t) = A cos(β

v(t)dt +
(cid:8)μ) with a sinusoidal speed signal of v(t) = vmax cos(ωot).
The spectrum of this signal, i.e., its Fourier transform, can be
written as follows:

(cid:7)

Y(f ) = A cos((cid:8)μ)

Jn(β(cid:4))(δ(f − nfo) + δ(f + nfo))

n even
n≥0
+ jA sin((cid:8)μ)

(cid:14)

n odd
n>0

Jn(β(cid:4))(δ(f − nfo) + δ(f + nfo))

(7)
where Jn(.) is the nth-order Bessel function, β(cid:4) = βvmax/ωo,
δ(.) is the Dirac-Delta function, and fo = ωo/2π is the
fundamental frequency of v(t).

Proof: If v(t) = vmax cos(ωot), then y(t) becomes

y(t) = A cos((cid:8)μ) cos(β(cid:4)

sin(ωot))

− A sin((cid:8)μ) sin(β(cid:4)

(cid:15)

sin(ωot))
(cid:16)

= A cos((cid:8)μ)R

− A sin((cid:8)μ)I

ejβ(cid:4) sin(ωot)
(cid:15)
ejβ(cid:4) sin(ωot)

(cid:16)

(8)

where β(cid:4) = βvmax/ωo, R{.} is the real part of the argument,
and I{.} is the imaginary part of the argument. The exponential
term ejβ(cid:4) sin(ωot) is periodic with a period 2π/ωo, and can be
expanded by its Fourier series as [31]

ejβ(cid:4) sin(ωot) =

∞(cid:14)

Jn(β(cid:4))ejnωot

(9)

n=−∞
where Jn(.) is the nth-order Bessel function. By substituting
(9) into (8), we get

∞(cid:14)

y(t) =

A Jn(β(cid:4))(cos((cid:8)μ) cos(nωot)

n=−∞
− sin((cid:8)μ) sin(nωot)).

By making use of the fact that J−n(x) = (−1)nJn(x), y(t)

can be written as

y(t) = 2A cos((cid:8)μ)

(cid:14)

Jn(β(cid:4)) cos(nωot)

n even
n≥0

(cid:14)

− 2A sin((cid:8)μ)

Jn(β(cid:4)) sin(nωot).

n odd
n>0

By taking the Fourier transform of y(t), we get (7).
Theorem 1 states that the spectrum of y(t) consists of an
inﬁnite number of deltas, located at the fundamental frequency
of v(t) and its harmonics. We next characterize the bandwidth
of this signal. In order to do so, we need to ﬁnd the frequency

point after which the power of the subsequent delta functions
has become negligible, as compared to the earlier terms.

Theorem 2: The bandwidth of y(t) can be characterized as

follows, for β(cid:4) ≥ 1:

BW|β(cid:4)≥1

= (β(cid:4) + 1)fo = ψvmax/λ + fo

where fo is the fundamental frequency of v(t). Moreover, for
β(cid:4) < 1, the bandwidth of y(t) is best characterized as follows:

BW|β(cid:4)<1

= 2fo.
Proof: It is well established in the literature that Jn(β(cid:4)) is
negligible for n > β(cid:4) + 1 [31]. By applying this to (7), we can
then estimate the bandwidth as follows: BW = (β(cid:4) + 1)fo for
β(cid:4) ≥ 1 since some even and odd terms are both present for
β(cid:4) ≥ 1 and terms can be compared accordingly within each
even and odd groups. When β(cid:4) < 1, however, the previous
result implies that the term n = 1 is the only dominating term
in the spectrum of y(t). However, due to the different scaling
factors of the even and odd terms in (7), there could exist
cases (e.g., small (cid:8)μ) where the term corresponding to n = 1
is suppressed by the sin((cid:8)μ) factor. In such cases, even though
J2(β(cid:4)) is small as compared to J1(β(cid:4)), cos((cid:8)μ)J2(β(cid:4)) can be
comparable or larger than sin((cid:8)μ)J1(β(cid:4)). Higher order terms
can always be neglected with respect to the ﬁrst two terms.
Hence, the bandwidth of y(t) for the case of β(cid:4) < 1 is 2fo.

Remark 3: In his seminal paper of [32], Carson was the
ﬁrst to theoretically characterize the bandwidth of an FM sig-
nal and show that it can be larger than the bandwidth of the
modulating signal. Carson has shown that his bandwidth rule
is exact for sinusoidal modulating signals, but can be general-
ized to approximate the bandwidth for general nonsinusoidal
modulating signals as well. As mentioned earlier, our received
signal y(t) has a close resemblance to an FM signal, except
for the (cid:8)μ terms. As such, our bandwidth analysis has some
resemblance to Carson’s derivations except for the impact of
(cid:8)μ. Following a similar argument to Carson’s, we will then
also use Theorem 2 to approximate the bandwidth of y(t) when
v(t) is a general nonsinusoidal signal in the next section. In
such a case, fo would denote the bandwidth of the signal v(t).
Theorem 2 states that the bandwidth of y(t) depends on
motion parameters, such as vmax and fo (or the bandwidth of
v(t) for nonsinusoidal signals). We next utilize Theorem 2 to
estimate the bandwidth of the WiFi CSI2 during three speciﬁc
kinds of sleep-related motions: 1) breathing; 2) seizure; and
3) normal sleep movements.

A. CSI Bandwidth During Breathing

A sleeping person’s chest volume expands and shrinks dur-
ing the inhalation and exhalation phases of respiration. It is
established in the literature that the instantaneous chest speed,
i.e., v(t) of Section III, can be approximated by a sinusoid of
frequency fo,br, where fo,br is the number of breathing cycles
per second [33]. As such, (7) can describe the spectrum of the
WiFi signal during breathing.

2Henceforth, the bandwidth of WiFi CSI means either the squared magni-

tude or phase difference, since they both have the same generic form y(t).

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply. 

KORANY AND MOSTOFI: NOCTURNAL SEIZURE DETECTION USING OFF-THE-SHELF WiFi

7001

(Left) CSI phase difference at multiple subcarriers of the Rx and
Fig. 2.
(right) the spectra of the CSI phase difference signals showing different
spectral content for different antennas.

In order to characterize the bandwidth for the case of nor-
mal breathing, we need to estimate β(cid:4)
= ([ψvmax,br]/[λfo,br]),
br
where fo,br is the breathing rate of the person, which is typi-
cally in the range of 0.2–0.3 Hz [34]. By integrating v(t), it can
be easily conﬁrmed that vmax,br/2π fo,br is equal to the max-
imum chest displacement during respiration, which has been
reported in the literature to be around 5 mm [16]. This results
in β(cid:4)
≈ 0.55 when using WiFi channel 48, which has a carrier
br
frequency fc = 5.24 GHz, and ψ = 1.3 By using Theorem 2,
we can then estimate the bandwidth of the received WiFi CSI
during normal breathing as BWbr = 2fo,br. Note that if the
maximum chest displacement is not along the perpendicular
line to the ellipse whose foci are the Tx and Rx (see Fig. 1),
e.g., if the person is in a different pose, the chest speed will
have a smaller velocity component along that line (i.e., smaller
vmax,br). In such a case, the value of β(cid:4) will be even smaller
and, thus, still less than 0.55. Thus, according to Theorem 2,
the bandwidth still remains BWbr = 2fo,br for all the cases.

It is worth noting that the previous literature on breathing
monitoring using WiFi signals (either magnitude [15], [33],
[35] or phase difference [17]) assume that the received WiFi
signal rises and falls with the same frequency as the rise
and fall (inhalation and exhalation) of the chest during the
breathing process. Hence, they assume that the received signal
has the same spectral content/bandwidth as that of the phys-
ical chest motion (i.e., they take BWbr to be fo,br). However,
Theorem 2 shows that the received WiFi signals can have a
spectral content that is different from the physical breathing
rate, depending on the value of (cid:8)μ, with a maximum band-
width of 2fo,br. To see this in effect, Fig. 2 shows the phase
difference of the measured WiFi signals between the Rx anten-
nas in a sample experiment, where a person was breathing with
a frequency of fo,br ≈ 0.18 Hz. It can be seen that while the
measured phase difference between antennas 3 and 1 of the
Rx has a sinusoid-like pattern similar to that of the breathing
motion, the phase difference between antennas 2 and 1 (due
to having a different (cid:8)μ) is experiencing a different pattern,
which has a strong frequency component at 2fo,br.

B. CSI Bandwidth During Seizures

As described earlier, a tonic-clonic seizure consists of a
tonic phase, in which the body muscles stiffen for a few

3In our experiments, we use WiFi channel 48 (fc = 5.24 GHz) in a setup in
which ψ ≈ 1 (see Section VI for the detailed scene conﬁguration). Extension
to different values of ψ is straightforward, as we shall discuss in Section VII-B
where we show experiments with different ψs. Hence, we set λ = 5.72 cm
and ψ = 1 for our numerical calculations in the rest of the article up to
Section VII-B.

seconds, immediately followed by a clonic phase, which is
a strong, fast, and repeated stiffening and relaxing of the body
muscles that can last for 1–3 min [4]. Several medical stud-
ies have been conducted to analyze body motion during a
tonic-clonic seizure through data obtained by accelerometry.
These studies have found that during the clonic phase of a
tonic-clonic seizure, the body muscles rhythmically stiffen and
relax with a frequency fo,sz between 1.5 and 5 Hz [20], [36],
[37], thus making a sinusoid a good approximation for v(t).
Therefore, (7) also characterizes the frequency spectrum of the
WiFi CSI during a seizure. In order to ﬁnd the value of the
parameter vmax and, thus, β(cid:4), we have looked extensively into
the medical literature on seizures. Several papers have found
that the maximum acceleration, amax, of the body parts dur-
ing a tonic-clonic seizure typically exceeds 15 m/s2 [21], [22].
Since v(t) is sinusoidal, then vmax,sz = (amax/2π fsz), and a
lower bound for the value of vmax,sz can be calculated as
vmax,sz ≥ (15/2π × 5) = 0.48 m/s.

Based on the aforementioned seizure motion parameters,
one can estimate a lower bound for the bandwidth of the WiFi
CSI during a seizure using Theorem 2 as BWsz = (β(cid:4)
+
sz
1)fsz = ([ψvmax,sz]/λ)+fo,sz. More speciﬁcally, by using WiFi
channel 48 and ψ = 1, vmax,sz = 0.48 m/s, and fo,sz = 1.5 Hz,
a lower bound for the bandwidth of the WiFi signal during
the seizure is estimated as BWsz ≥ 9.9 Hz. Note that the
aforementioned characterization of the CSI bandwidth during
a seizure assumes that the motion of at least one body part is
aligned with (or has a strong component on) the perpendicular
line to the Tx–Rx ellipse of Fig. 1. This assumption is practical
since the uncontrolled muscle jerks during the seizure result
in the body parts moving randomly in all different directions.
Moreover, it has been shown in the medical literature that a
patient’s body posture can change to many different positions
during a seizure [38]. Therefore, there will at least be one body
part whose motion direction is aligned with the perpendicular
line to the Tx/Rx ellipse.

It is worth stressing that the traditional assumption that the
WiFi signal rises and falls with the same frequency of the body
motion will result in a bandwidth estimation of BWsz = fo,sz,
which is far off from the true bandwidth during a seizure.

C. CSI Bandwidth During Normal Sleep Events

We next delve into the medical literature on sleep motion
analysis in order to characterize the parameters relevant for
signal bandwidth characterization during normal sleep events,
such as position adjustments and jerking in limbs, which
people tend to make during different stages of sleep. It is
found that these normal sleep events occur at an average rate
of three events per hour [27], and can last for up to 15 s
each [26]. Furthermore, other studies have performed time-
frequency analysis of the accelerometry data of normal sleep
and established that most of the power of normal sleep event
signals [e.g., v(t)] is concentrated below fo,nm = 2 Hz [39].
While v(t) is nonsinusoidal, and no exact closed-form expres-
sion exists for the spectrum of the CSI signals for a general
v(t), Theorem 2 can still be used to approximate the bandwidth
of the WiFi CSI, as discussed in Remark 3.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply. 

7002

IEEE INTERNET OF THINGS JOURNAL, VOL. 9, NO. 9, MAY 1, 2022

TABLE I
MOTION PARAMETERS AND THE CORRESPONDING BANDWIDTH FOR
THREE KINDS OF SLEEP MOVEMENTS

Fig. 3. Block diagram of the proposed WiFi CSI-based nocturnal seizure
detection system. The data preprocessing and event detection blocks utilize the
derived WiFi CSI bandwidth during breathing (BWbr). The event classiﬁcation
module then utilizes the derived WiFi CSI bandwidth during both seizure
(BWsz) and normal sleep movements (BWnm).

In order to calculate an upper bound for the WiFi CSI
bandwidth in case of normal sleep events, we focus on wrist
movements during sleep, which can have higher speeds due
to its relatively lower mass as compared to other body parts.
We utilize the online data set published by Walch et al. [28]
for the accelerometry data of 31 adults during their sleep,
collected from wrist-worn Apple watches. By integrating this
acceleration data over time, we get the instantaneous speeds of
the wrist during sleep. We then use the 99th percentile value
of the speeds calculated from the data set, which is found
to be 0.33 m/s, as an estimate for the maximum possible
speed of body parts during normal sleep events.4 To esti-
mate an upper bound for vmax during normal sleep events, we
assume that the body part with the fastest motion is aligned
with the perpendicular line to the Tx–Rx ellipse of Fig. 1.
Hence, vmax,nm ≤ 0.33 m/s. Then, Theorem 2 estimates the
bandwidth of the WiFi signals during a normal sleep event
as BWnm = ([ψvmax,nm]/λ) + fo,nm, where fo,nm denotes the
bandwidth of the modulating signal v(t). At WiFi channel 48
and ψ = 1, an upper bound of this bandwidth will then be
BWnm ≤ (0.33/λ) + 2 = 7.8 Hz.

Table I summarizes the results of our WiFi CSI bandwidth
analysis during the three considered nocturnal movements:
1) breathing; 2) seizure; and 3) normal sleep events. It can
be seen from the table that the bandwidth of the WiFi signal
during a movement can be used as a distinguishing feature
that differentiates seizures from normal sleep events. We make
use of this observation to design a robust nocturnal seizure
detection system in the next section.

V. SYSTEM DESCRIPTION

In this section, we describe our proposed framework for
nocturnal seizure detection using WiFi CSI signals based
on the mathematical analysis of Section IV. Fig. 3 shows
the block diagram of our proposed system, which starts by

4Larger speed values are only recorded when quick jerky limb motions
take place. Such events are easily identiﬁable and differentiable from seizures,
since they typically last for less than 400 ms [37].

preprocessing the WiFi CSI input data to denoise the measured
CSI signal and extract the part that carries the information
about the human motion. Then, the denoised signal is passed
to an event detection module, which decides whether the per-
son is moving or is staying still. In case a movement event
is detected (other than breathing), the CSI data during the
event are then forwarded to an event classiﬁcation module,
which determines whether this event is a normal sleep event
or a seizure. In the latter case, the system alarms the caregiver
to take the necessary action. We next describe each of these
components in details.

A. Data Preprocessing

As discussed in Section III, we utilize both the CSI-squared
magnitude and phase difference since they both carry crucial
information about the body motion. In this article, we con-
sider off-the-shelf WiFi devices that can be used to extract the
complex WiFi CSI information, e.g., Intel 5300 or Atheros
AR9580 WiFi cards. In any of these devices, the receiver
has NR receiver antennas, which measure the WiFi CSI
information on Nsc subcarriers. Therefore, we extract a total of
NR × Nsc CSI-squared magnitude streams, and (NR − 1) × Nsc
phase difference streams (i.e., the phase difference between
each antenna and antenna 1, for all the Nsc subcarriers). In
total, we get ND = (2NR − 1) × Nsc data streams that can be
used to extract the motion information. The Intel 5300 WiFi
card, for instance, has NR = 3 receiver antennas and Nsc = 30
subcarriers, resulting in a total of ND = 150 data streams car-
rying the motion information of the body. We next show how
we process these ND data streams to extract the informative
part about the body motion.

Outlier Removal: We use the Hampel identiﬁer [15] to
remove the sudden and very short abrupt changes that happen
in the data streams due to hardware imperfections [15].

Stream Selection: Different subcarriers on the same Rx
antenna have different carrier frequencies (or wavelengths),
and consequently,
levels of fading,
they undergo different
making some subcarriers noisier than others. To enhance the
system’s robustness, it is then important to select only the
most informative/least noisy data streams to be subsequently
used in the rest of the seizure detection algorithm. In order
to do so, we use the data of a short calibration period, in
which the sleeping person is only breathing and not doing
any movements or having a seizure. This one-time calibra-
tion can be easily administered by a caregiver prior to system
deployment, and recalibration can be done as needed.

The stream selection algorithm works as follows. Since the
calibration period is known to have only breathing motion,
the CSI data contain frequency components only in the band
f ≤ BWbr, where BWbr is the maximum bandwidth for WiFi
CSI during breathing, which we have shown in Section IV
to be 2fo,br. Any frequency content above BWbr is thus due
to noise. Hence, given all the data streams in a calibration
window of duration Tcal, we calculate the signal-to-noise ratio
(SNR) of the ith data stream as follows:

SNRi =

(cid:14)

Si(f )

(cid:17) (cid:14)

0<f ≤BWbr

f >BWbr

Si(f )

(10)

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply. 

KORANY AND MOSTOFI: NOCTURNAL SEIZURE DETECTION USING OFF-THE-SHELF WiFi

7003

(Top) Sample output of the accelerometer attached to the arm of a subject during 4 h of overnight sleep. (Bottom) The PCA-denoised stream p(t)
Fig. 4.
of the WiFi data collected during the same time period. The dashed red line in the zoomed-in part shows the start of a sample event that is detected by our
event detection module, while the dashed–dotted red line indicates its end.

(cid:18)

t si(t)e−j2π ft|2, si(t) is the ith data stream,
where Si(f ) = |
BWbr = 2fo,br, and fo,br is the maximum normal breathing
frequency, which is equal to 0.3 Hz in adults.

We then select the K data streams with the highest SNRs
from the calibration data and use only this set of streams in the
operation phase until after a major event happens (for instance,
a seizure). The system can then recalibrate by processing all
the data streams again and reselecting the new top K streams
in terms of SNR in the new person’s pose/orientation. For the
implementation of our system (see details in Section VI), we
set Tcal = 13 s and K = 15.

PCA Denoising: After extracting the set of the best K data
streams, we further denoise these streams during operation
phase using principal component analysis (PCA) as described
in [40]. More speciﬁcally, we extract the ﬁrst principal com-
ponent p(t) of the data, which carries the motion information
since it is common to all the data streams, while the noise is
distributed among all the different principal components [40].
In order to show the performance of the preprocessing mod-
ule, we conduct an overnight sleep experiment, where WiFi
transceivers are placed on both sides of a bed on which a sub-
ject sleeps. An accelerometer is attached to the upper right
arm of the subject to collect ground truth sleep motion data.
Fig. 4 shows a 4-h snippet of the processed WiFi data p(t)
as well as the accelerometer output during the same period. A
13-s calibration period is chosen right after the subject goes to
sleep and the selected streams are then used for the rest of the
night. It can be clearly seen that the preprocessed WiFi data
p(t) carries the same motion information as the accelerome-
ter. In the right part of the ﬁgure, we zoom in to one of the
movements, where the breathing signal, as well as the motion,
can be clearly seen in the WiFi data.

B. Event Detection

As described in the previous section, the data preprocessing
module outputs a signal p(t), which is the denoised version of
the CSI measurements at the receiver. This signal is then fed
to an event detection module. By “event,” we mean the state
of the sleeping person engaging in any kind of nonbreathing
movement. More speciﬁcally, the movement can be normal
sleep events, e.g., posture adjustments, or abnormal, e.g., a
seizure. The nature of the event (whether it is normal or abnor-
mal) will be decided in a later stage, which we shall describe
in Section V-C.

In order to detect an event in the signal p(t), we use a
moving window of duration T ED
win. If the person was only
breathing during an instance of the moving window, the signal
p(t) during that window will have a frequency spectrum that is

concentrated below BWbr, as discussed in Section V-A. On the
other hand, if the person engages in any type of nonbreathing
movement, the signal p(t) within the time window will have
nonnegligible frequency content above BWbr. Therefore, we
can utilize the energy content of the spectrum of p(t) above
the frequency BWbr to indicate the presence of an event. More
speciﬁcally, let H1 denote the hypothesis of having an event,
and Ho denote otherwise. To decide if there is an event at
time t = τ , we use the decision rule

(cid:19)
(cid:19)
(cid:19)
(cid:19)
(cid:19)

(cid:14)

f >BWbr, adj

(cid:14)

t

p(t)w(t, τ )e

−j2π ft

2 H1≷
H0

γth

(11)

(cid:19)
(cid:19)
(cid:19)
(cid:19)
(cid:19)

where w(t, τ ) is a rectangular window of length T ED
win ending
at time t = τ . Note that due to the time windowing of the
signal p(t), the frequency spectrum of the windowed signal
is that of the original signal convolved with a sinc function,
which increases the bandwidth of the signal by an amount of
win. Hence, the value of BWbr is adjusted to be BWbr, adj =
1/T ED
2fo,br + 1/T ED
win, where fo,br is the maximum normal breathing
frequency.5

In order to determine the value of γth, we utilize the pro-
cessed data of the calibration period (whose duration is Tcal)
described in Section V-A to evaluate the following:
(cid:19)
(cid:19)
(cid:19)
(cid:19)
(cid:19)

⎫
⎬
⎭ (12)

pc(t)w(t, τ )e

= max
τ

−j2π ft

σ 2
c

⎧
⎨

(cid:14)

(cid:14)

(cid:19)
(cid:19)
(cid:19)
(cid:19)
(cid:19)

⎩

2

f >BWbr,adj

t

where pc(t) is the processed data of the calibration period. σ 2
c
is then the maximum energy content of the calibration data
above BWbr,adj, which is an estimate of the noise power in
the band of f > BWbr,adj when there is no event. We then set
γth = q σ 2

c , where q is a design parameter.

The zoomed-in part of Fig. 4 shows a sample normal sleep
movement from a sleeping subject. The vertical red-dashed
line shows the start of the detected event using our proposed
event detection module, while the vertical red-dashed–dotted
line shows its end. It can be seen that our event detection
module was able to accurately localize the start and the end
of the event.

C. Event Classiﬁcation

Once an event has been detected, the processed data p(t)
is then passed to an event classiﬁcation

during the event

5Note that for a large window size (large Twin), the additional bandwidth
1/Twin can be neglected with respect to the original signal bandwidth. In such
cases, the bandwidth calculations need not be adjusted.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply. 

7004

IEEE INTERNET OF THINGS JOURNAL, VOL. 9, NO. 9, MAY 1, 2022

Fig. 5. We tested our proposed approach in seven different locations. Four sample locations are shown here.

module that determines whether this event is normal or abnor-
mal. As discussed in Section IV, the duration of a seizure is
usually longer than that of any normal event. However, rely-
ing solely on event duration for deciding whether the event is
a seizure or not induces an unfavorable delay in the system
response, as the system would have to wait for a relatively
long period of time before declaring an event as a seizure,
which can lead to undesirable complications for the patient. It
is then crucial to analyze the detected events in terms of their
frequency content, using the analysis and parameters derived
in Section IV, in order to have an early and robust detection.
We next describe our event classiﬁcation algorithm.

First, any event whose duration is less than a tolerable value
Tmin is declared as a normal event. This step is important
to avoid the unnecessary computational overhead of analyz-
ing very short events, such as sleep jerks or very quick limb
movements, since it is almost impossible for a tonic-clonic
seizure to have such a short duration [37]. It is worth noting
that this comes at the expense of a small delay in the RT,
since a seizure would only be declared at least Tmin after its
onset. As a design choice, we set Tmin = 5 s for our system
implementation. We will show the effect of varying Tmin on
the system performance in Section VII.

For the rest of the events (whose durations are larger than
Tmin), let pe(t) denote the processed CSI measurements during
the event. We divide pe(t) to consecutive overlapping win-
win, and estimate the bandwidth of pe(t) as
dows of length T EC
the median of the bandwidths of the signals in the overlap-
ping windows. More speciﬁcally, the bandwidth of pe(t) is
estimated as

Bpe

= median
τ

⎧
⎨
⎩B:

(cid:18)

f >B

(cid:18)

f >0

(cid:18)

(cid:19)
(cid:19)
(cid:19)
(cid:18)
(cid:19)

t pe(t)w(cid:4)(t, τ )e−j2π ft
t pe(t)w(cid:4)(t, τ )e−j2π ft

(cid:19)
(cid:19)2
(cid:19)
(cid:19)2

⎫
⎬

= 0.1

⎭

(13)

where w(cid:4)(t, τ ) is a rectangular window of length T EC
win ending at
t = τ , and the quantity inside the braces is the 90th percentile
bandwidth of the signal within the window ending at t = τ .
For an ongoing long event, bandwidth Bpe is updated by adding
more time windows of the new data to the calculation of (13).
This method of estimating the bandwidth of the signal pe(t)
is favorable for real-time operation, since it requires a ﬁxed-
length FFT operation for a window of size T EC
win to update the
bandwidth of an ongoing event.

We declare a seizure if the bandwidth Bpe exceeds a thresh-
old fth. By using the spectral analysis of Section IV and
the corresponding bandwidth calculations of Table I, we set
fth = (9.9 + 7.8/2) = 8.85 Hz, since this value optimally

separates the bandwidths of the WiFi signal during seizures
from the ones during normal events. We will study the effect
of changing fth on the system performance in Section VII.

VI. EXPERIMENTAL SETUP

In this section, we describe the experimental setup we shall
use as a proof of concept for our proposed seizure detection
system.

Experimental Setup: For the WiFi CSI data collection, we
use two laptops equipped with Intel 5300 WiFi cards. One
of the laptops (the Tx) transmits WiFi packets at a rate of
200 packets per second on WiFi channel 48, which has a car-
rier frequency of 5.24 GHz. The other laptop (the Rx) uses
CSItool [41] to measure the CSI data of 30 WiFi subcarriers
on three Rx antennas. The CSI magnitude data and the phase
difference data with respect to antenna 1 [i.e., θ2(t) − θ1(t)
and θ3(t) − θ1(t)] are then logged and processed ofﬂine using
MATLAB. We collect the WiFi data in seven different dorm
rooms/bedrooms (some of which are shown in Fig. 5). In all
the locations, we start by placing the Tx and Rx on two differ-
ent sides of the bed on which the test subject lies down (with
Tx–Rx distance of ∼ 2.5 m). The antennas of the Tx and Rx
are both elevated by 70 cm above the bed level. We then study
the impact of different Tx/Rx conﬁgurations in Section VII.
Note that for Rx, external tripod-mounted antennas may be
used in order to make the Rx at the same height as the Tx.
This conﬁguration for the relative positioning of the Tx, Rx,
and bed results in ψ ≈ 1 (the angle φ in Fig. 1 is ∼ 60◦),
independent of the person’s pose or orientation on the bed.

Test Subjects and Experiment Protocol: We recruited a total
of 20 student actors (5 females and 15 males) to participate
in our experiments, where each subject participates in one or
more of the experimental locations. In total, the number of
subjects participating in each of the seven locations are 11,
6, 4, 2, 1, 1, and 1 subjects, respectively.6 Each participant
was consensually trained on how to simulate a tonic-clonic
seizure and shown public online YouTube videos explaining
how tonic-clonic seizures look like. It is worth noting that
seizure acting is a common practice in medical schools, where
healthy persons (known as standardized patients) are recruited
to act out different medical conditions to provide introductory
training opportunities for medical students [42], [43]. Hence,
testing a system on simulated seizures is an important step
toward more advanced clinical trials.

6The institutional

review board (IRB) committee has reviewed this
research and determined that it does not constitute human subject research.
Furthermore, all the experiments that were carried out during the pandemic
followed the strict COVID-19 safety guidelines put in place by our institution.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply. 

KORANY AND MOSTOFI: NOCTURNAL SEIZURE DETECTION USING OFF-THE-SHELF WiFi

7005

For each subject, the receiver starts logging the CSI data
when the subject is in a sleep state (only breathing and in
any generic position) for at least 15 s (part of which to be
used as one-time calibration data). Then the subject starts sim-
ulating seizures and normal sleep movements. Each seizure
instance is simulated for at least 20 s.7 In total, each partici-
pant does ten seizure simulations per location, resulting in a
total of 260 independent instances of seizure data across all the
locations. Similarly, each subject performs several normal non-
breathing sleep movements spontaneously in each experiment.
By observing the subjects’ movements, they included posture
adjustments (e.g., switching from lying on their side to lying
on their back), limb-only movements (e.g., stretching or tuck-
ing the knee), scratching, stretching, coughing, sneezing, and
sleep jerks. Overall, we collected a total of 410 independent
normal sleep events from all subjects in all the locations.8

Performance Metrics: We test

the performance of our
system according to the following three performance metrics.
1) Seizure Detection Rate (SDR): It is deﬁned as the num-
ber of detected seizures, divided by the total number of
seizures (expressed as a percentage).

2) Probability of False Alarm (PFA): It is deﬁned as the
number of normal sleep events that is incorrectly classi-
ﬁed as seizures, divided by the total number of detected
normal sleep events.

3) Response Time for Seizures: It is deﬁned as the time at
which the event classiﬁcation module detects the seizure,
measured with respect to the seizure’s onset.

Algorithm Parameter Values: We set the following values
= 2 s,
for different algorithm parameters, Tcal = 13 s, T ED
win
= 4 s, Tmin = 5 s, K = 15, and q = 2. The optimum clas-
T EC
win
siﬁcation threshold fth is then found based on our proposed
mathematical framework to be fth = 8.85 Hz, as shown in
Section IV. It is worth stressing that this threshold is found
based on our rigorous theoretical characterization of the band-
width, and not based on empirical data. The effect of varying
some of these parameters on system performance is shown in
Section VII.

VII. EVALUATION RESULTS

In this section, we present

the performance evaluation

results of our proposed seizure detection algorithm.

For the seizure data instances in all

the locations, our
proposed system was able to detect 244 out of the 260 seizures,
resulting in a SDR of 93.85%. It is worth noting that the
event detection module was able to detect all the 260 seizures.
However, the event classiﬁcation module misclassiﬁed 16 out
of the detected 260 events. Fig. 6 (left) shows the CDF of the
RTs of the detected seizures, showing that our system achieves
a mean RT (MRT) of 5.69 s. Such an early detection is impor-
tant for the caregiver to provide the needed medical assistance
as soon as possible. In terms of locations, the SDR in the
seven locations was 93.6%, 95%, 90%, 90%, 100%, 100%,

7An actual tonic-clonic seizure can last for 1–3 min. However, it is a phys-
ically challenging task for a healthy person to simulate it for such a long
time.

8Sample data ﬁles and detection/classiﬁcation codes are available in this

URL https://doi.org/10.21229/M9ZT09.

Fig. 6.
(Left) CDF of the system’s RT. The mean RT is 5.69 s. (Right) PDF
of the bandwidths of seizure events and normal sleep events, showing a gap
in the 7–9 Hz band.

TABLE II
COMPARISON WITH STATE-OF-THE-ART IN SEIZURE DETECTION

and 100%, while the mean RT in the seven locations was 5.8,
5.8, 5.68, 5.58, 5.65, 5, and 5.1 s, respectively. This shows
that the system’s performance is insensitive to the deploy-
ment environment, since the static multipath does not affect
the information-bearing parts of the received WiFi signal, as
discussed in Remark 2.

In terms of normal events, our event detection module was
able to detect 406 out of the 410 normal events. It is worth
noting that it is irrelevant if the system misses some nor-
mal events, as the main purpose of the system is seizure
detection with as few false alarms as possible. Out of the
detected normal events, only four events were incorrectly clas-
siﬁed as seizures, resulting in a probability of false alarm
PFA = 0.0097. Fig. 6 (right) shows the densities of the mea-
sured bandwidths of the WiFi signals during seizure events
as well as normal sleep events. The distributions of the band-
widths show a clear gap in the band of 7–9 Hz, which validates
the theoretical bandwidth characterization of Section IV.

Processing Time: It takes 18 ms, on average, to process one

second of collected data, using our algorithm of Section V.

Comparison to State of the Art: Van Andel et al. [44]
provided a survey for in-home tonic-clonic seizure detection
algorithms that use different modalities, e.g., accelerometry,
mattress units, and video, to detect tonic clonic seizures on real
epilepsy patients. Table II compares the performance of our
proposed system to the performance of the different detection
techniques reported in the survey of Van Andel et al. [44], as
well as other multimodal seizure detection papers. Overall, our
results show the robustness of our proposed system, in terms
of achieving a very good SDR, probability of false alarm,
and a fast average RT of 5.69 s to detect a seizure, while
being noninvasive and privacy preserving. We note that part
of the contribution of this article was also to develop a new
mathematical model that can enable seizure detection using

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply. 

7006

IEEE INTERNET OF THINGS JOURNAL, VOL. 9, NO. 9, MAY 1, 2022

TABLE III
PERFORMANCE IN DIFFERENT TX/RX PLACEMENT SETTINGS

(Left) PFA and (1-SDR) as a function of fth: increasing fth degrades
Fig. 7.
SDR while improving PFA. (Right) MRT and PFA as a function of Tmin:
increasing Tmin degrades MRT while improving PFA.

WiFi signals, while most of the existing works are mainly
either testing an existing product, or utilizing straightforward
modalities, e.g., accelerometry. Furthermore, our approach is
the only privacy-preserving one that is also noninvasive. While
our results are based on simulated seizures, they constitute a
strong proof-of-concept for our proposed idea/mathematical
models, which shows how RF signals (e.g., WiFi) can be used
as a noninvasive, robust, and affordable alternative for noctur-
nal seizure detection. Hence, our proposed algorithms serve as
a basis for a system that can be subsequently tested in clinical
settings, toward the ultimate goal of making such technology
available to the public.

A. Effect of Varying fth and Tmin

Based on our theoretical analysis of Section IV, we con-
cluded that a threshold of fth = 8.85 Hz optimally separates the
bandwidth of the WiFi signals during normal sleep movements
from that during seizures. In this section, we study the effect
of varying fth, while keeping all other system parameters at
their default values. Fig. 7 (left) shows (1-SDR) and PFA as
a function of fth. It can be seen that SDR decreases (becomes
worse) when increasing fth, since more seizure events can go
undetected due to their bandwidth being less than the higher
fth. On the other hand, increasing fth improves PFA, since it
becomes less likely for the bandwidth of the WiFi signal dur-
ing a normal sleep event to exceed a higher fth. We can see
that the mathematically driven value of 8.85 Hz strikes a good
balance between SDR and PFA.

Next, we study the effect of varying Tmin, which is the
minimum duration for an event to be passed to the event clas-
siﬁcation module. Fig. 7 (right) shows MRT and PFA as a
function of Tmin. Expectedly, increasing Tmin increases MRT,
since a higher Tmin means that the event classiﬁcation module
(which determines whether the event is a seizure or not) is
not activated for a longer time after the seizure onset. On the
other hand, increasing Tmin improves PFA, since a higher por-
tion of the normal events are declared normal by default due
to their short duration. It can be seen that the chosen value of
Tmin = 5 s strikes a good balance in the MRT-PFA tradeoff.
It is worth noting that SDR does not change as a function of
Tmin in Fig. 7, and as such is not plotted.

B. Effect of Tx–Rx Positioning

For all the previous results, we considered a setting (hence-
forth denoted by C#1) where the position of the Tx/Rx with
respect to the bed resulted in a value of ψ ≈ 1 (see Fig. 5). In
this section, we test our system with different Tx/Rx positions
resulting in different ψs. Based on our analysis of Section III,

ψ impacts the bandwidth characterization of seizure and nor-
mal sleep movements as follows: BW = (ψvmax/λ+fo), where
vmax and fo denote the vmax and fo of the corresponding cases.
To test the sensitivity of our system to different Tx/Rx
positions and their corresponding ψ, we carry out extensive
experiments on one test subject (in location 4 of Fig. 5) by
changing either the Tx/Rx locations in the same horizontal
plane (to which we refer as changing their conﬁguration), or
changing their heights.

Changing Tx/Rx Conﬁguration: In order to test the sen-
sitivity of the system to the placement of the Tx/Rx in the
horizontal plane, we conduct experiments in two additional
conﬁgurations, C#2 and C#3. In C#2, the Tx and the Rx are
placed on one side of the bed, such that the line connect-
ing the Tx and Rx is parallel to the edge of the bed and
70 cm away from it. Such a conﬁguration can be of partic-
ular interest in practical situations in which one side of the
bed is not accessible, e.g., if the bed is placed next to a
wall. The distance between the Tx and the Rx is 2 m, and
both are elevated by 70 cm above the bed level. This setup
results in ψ ≈ 1.4, which will result in BWsz ≥ 13.23 Hz,
and BWnm ≤ 10.06 Hz using our mathematical deriva-
tions. We thus use fth = (13.23 + 10.06/2) = 11.64 Hz
for this conﬁguration. On the other hand, in C#3, the Tx
and Rx are placed on two different sides of the bed, with
a Tx–Rx distance of 3.6 m, while they are elevated by 70 cm
above the bed level. This setup results in ψ ≈ 0.7, and
fth = (7.36 + 6.03/2) = 6.69 Hz.

In each of the conﬁgurations, the test subject simulates a
total of ten seizure instances and 125 normal sleep events.
We summarize the evaluation results of these experiments in
Table III. It can be seen that the performance of the system in
C#2 and C#3 is comparable to that of the main conﬁguration
(C#1), showing that the performance of our proposed pipeline
is robust to different Tx/Rx conﬁgurations.

Changing Tx/Rx Heights: In order to test the sensitivity of
the system to antenna heights, we conduct experiments in two
additional settings, C#4 and C#5. In both settings, the Tx and
Rx are placed ∼2.5 m apart on both sides of the bed (similar
to C#1), but their heights are elevated to 1.3 m above the bed
level in C#4, and 1.7 m above the bed level in C#5. Using
simple geometry, it can be veriﬁed that in C#4, ψ = 1.44
(fth = 11.94 Hz), while in C#5, ψ = 1.61 (fth = 13.15 Hz).
Again, in both settings, the test subject simulates a total of
ten seizure instances and 125 normal sleep events. Table III
shows that the performance of the system in C#4 and C#5 is
comparable to that of the other conﬁgurations, indicating that
our proposed pipeline is robust to different Tx/Rx heights.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply. 

KORANY AND MOSTOFI: NOCTURNAL SEIZURE DETECTION USING OFF-THE-SHELF WiFi

7007

mathematical models that can enable this. We also validated
our proposed approach by extensive experiments on seizures
simulated by actors. The results of this preliminary validation
show the great potential of using WiFi signals as an appeal-
ing alternative to the currently available products, which are
costly, uncomfortable, or unreliable. Toward the ultimate goal
of making this technology available to the public, the next
step is to develop a prototype of the proposed system, which
can then undergo extensive clinical trials on real patients, and
become available to the epilepsy patients and their caregivers.

IX. CONCLUSION

In this article, we have considered the problem of noctur-
nal seizure detection in epilepsy patients using WiFi signals
measured on a device placed in the vicinity of the sleep-
ing patient. We ﬁrst provided a mathematical analysis for
the spectral content/bandwidth of the WiFi signal during dif-
ferent kinds of sleep body movements (e.g., seizure, normal
movements, and breathing), showing that the bandwidth of
the signal can be used to robustly differentiate a seizure from
normal movements. We then utilized this analysis to design a
robust seizure detection system, which detects all nonbreath-
ing body motion events and classiﬁes them, based on their
spectral content, to normal movements and seizures. We exper-
imentally validated our proposed system using WiFi CSI data
collected from 20 actors in seven different locations, where
they simulated a total of 260 seizures as well as 410 nor-
mal sleep movements. Our proposed system achieved a very
low probability of false alarm of 0.0097, while being very
responsive to seizure events, detecting 93.85% of the seizure
instances with an average RT of only 5.69 s. These promising
results show the potential of using WiFi signals as an accurate
and cheap alternative to traditional seizure detection systems.

REFERENCES

[1] World Health Organization.

(2020). Epilepsy.

[Online]. Available:

https://www.who.int/news-room/fact-sheets/detail/epilepsy

[2] M. van der Lende, D. C. Hesdorffer, J. W. Sander, and R. D. Thijs,
“Nocturnal supervision and SUDEP risk at different epilepsy care
settings,” Neurology, vol. 91, no. 16, pp. 1508–1518, 2018.

[3] S. D. Lhatoo et al., “Nonseizure SUDEP: Sudden unexpected death in
epilepsy without preceding epileptic seizures,” Epilepsia, vol. 57, no. 7,
pp. 1161–1168, 2016.

[4] S. Jenssen, E. J Gracely, and M. R. Sperling, “How long do most seizures
last? A systematic comparison of seizures recorded in the epilepsy
monitoring unit,” Epilepsia, vol. 47, no. 9, pp. 1499–1503, 2006.
[5] Empatica. (2020). Embrace2. [Online]. Available: https://www.empatica.

com/embrace2/

[6] Medpage. MP5 Seizure Detection Monitor. Accessed: Jun. 1, 2020.
https://medpage-ltd.com/epileptic-tonic-clonic-

[Online]. Available:
seizure-alarm-MP5

[7] SAMi.

(2020). The Sleep Activity Monitor.

[Online]. Available:

https://www.samialert.com/

[8] C. R. Karanam, B. Korany, and Y. Mostoﬁ, “Magnitude-based angle-of-
arrival estimation, localization, and target tracking,” in Proc. ACM/IEEE
IPSN, 2018, pp. 254–265.

[9] A. Gonzalez-Ruiz and Y. Mostoﬁ, “Cooperative robotic structure map-
ping using wireless measurements—A comparison of random and
coordinated sampling patterns,” IEEE Sensors J., vol. 13, no. 7,
pp. 2571–2580, Jul. 2013.

[10] R. Nandakumar, S. Gollakota, and N. Watson, “Contactless sleep apnea
detection on smartphones,” in Proc. Annu. Int. Conf. Mobile Syst. Appl.
Services, 2015, pp. 45–57.

(Top) The PCA-denoised data p(t) in a 10-min experiment with two
Fig. 8.
subjects. (Bottom) The bandwidth of p(t) during the detected events. It can
be seen that the seizures are the only events whose bandwidth exceeds fth for
an extended period of time.

C. Multiperson Operation

In-home seizure detection systems are primarily designed
for caregivers who do not share the same bed (or bedroom)
as the patient, since, otherwise, they would be alerted by the
patient’s seizure movements. However, in order to show the
robustness of our proposed system, we next show that it can
still be deployed in a multiperson setting, where multiple peo-
ple share the same bed. In such a case, the event detection
module detects any movement done by any of the sleep-
ing persons. In order to test this, we conducted a 10-min
experiment, where two people lie down next to each other
on a bed. Person 1 simulates seizures at the 6 and 9 min
marks. Otherwise, both people frequently simulate normal
sleep movements. As such, there are a number of instances
where both people move at the same time, or one person
moves normally while the other one is simulating a seizure.
Fig. 8 (top) shows the PCA-denoised stream p(t), in which per-
turbations are clearly visible whenever either persons engages
in any kind of movement, while Fig. 8 (bottom) shows the
bandwidth of the WiFi signals during the detected events. It
can be seen that the bandwidth exceeds fth for an extended
period of time only during the seizure instances, which are
correctly classiﬁed as seizures, even though the second person
was moving during the second seizure instance. Otherwise,
during normal movements, even if both persons are moving
simultaneously, the events are not classiﬁed as seizures.

VIII. FURTHER DISCUSSIONS

Robustness

to Movements

by Other People:

In
Section VII-C, we have shown that our proposed system
to movements by other sleeping people in the
is robust
same environment, since their normal sleeping movements
have the same characteristics as those of the patient. Next,
consider
the case where other simultaneous movements
happen, such as those of a walking person. The spectrogram
of the signal reﬂected off of a walking person has speciﬁc
characteristics. Thus, as part of future work, one can study
the differentiability of the signals induced by walking from
those induced by seizures. Furthermore, the reﬂected signals
off of other moving targets can also be ﬁltered out at the Rx
by exploiting more signal dimensions. For instance, multiple
antennas at the Rx can separate the received signals based on
their Angle of Arrival (AoA).

Clinical Trials: In this article, we proposed the ﬁrst RF-
based system for nocturnal seizure detection, by developing

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply. 

7008

IEEE INTERNET OF THINGS JOURNAL, VOL. 9, NO. 9, MAY 1, 2022

[11] S. Depatla and Y. Mostoﬁ, “Crowd counting through walls using WiFi,”

[37] H. Lüders et al., “Semiological seizure classiﬁcation,” Epilepsia, vol. 39,

in Proc. IEEE PerCom, 2018, pp. 1–10.

no. 9, pp. 1006–1013, 1998.

[12] H. Cai, B. Korany, C. R. Karanam, and Y. Mostoﬁ, “Teaching RF to
sense without RF training measurements,” Proc. ACM Interact. Mobile
Wearable Ubiquitous Technol., vol. 4, no. 4, pp. 1–22, 2020.

[13] F. Adib, H. Mao, Z. Kabelac, D. Katabi, and R. C. Miller, “Smart homes
that monitor breathing and heart rate,” in Proc. Conf. Human Factors
Comput. Syst., 2015, pp. 837–846.

[14] Z. Yang, P. H. Pathak, Y. Zeng, X. Liran, and P. Mohapatra, “Monitoring
vital signs using millimeter wave,” in Proc. ACM Symp. Mobile Ad Hoc
Netw. Comput., 2016, pp. 211–220.

[15] X. Liu, J. Cao, S. Tang, J. Wen, and P. Guo, “Contactless respira-
tion monitoring via off-the-shelf WiFi devices,” IEEE Trans. Mobile
Comput., vol. 15, no. 10, pp. 2466–2479, Oct. 2015.

[16] H. Wang et al., “Human respiration detection with commodity WiFi
devices: Do user location and body orientation matter?” in Proc. ACM
Ubicomp, 2016, pp. 25–36.

[17] X. Wang, C. Yang, and S. Mao, “PhaseBeat: Exploiting CSI phase data
for vital sign monitoring with commodity WiFi devices,” in Proc. IEEE
Conf. Distrib. Comput. Syst. (ICDCS), 2017, pp. 1230–1239.

[18] X. Wang, C. Yang, and S. Mao, “ResBeat: Resilient breathing beats mon-
itoring with realtime bimodal CSI data,” in Proc. IEEE GLOBECOM,
2017, pp. 1–6.

[19] F. Wang, F. Zhang, C. Wu, B. Wang, and K. R. Liu, “Respiration tracking
for people counting and recognition,” IEEE Internet Things J., vol. 7,
no. 6, pp. 5233–5245, Jun. 2020.

[20] T. Nijsen, “Accelerometry based detection of epileptic seizures,” Ph.D.
dissertation, Ter Verkrijging van de Graad van Doctor aan de, Technische
Universiteit Eindhoven, Eindhoven, The Netherlands, 2008.

[21] M. Velez, R. S. Fisher, V. Bartlett, and S. Le, “Tracking generalized
tonic-clonic seizures with a wrist accelerometer linked to an online
database,” Seizure, vol. 39, pp. 13–18, Jul. 2016.

[22] S. Kusmakar, C. Karmakar, B. Yan, T. Obrien, R. Muthuganapathy, and
M. Palaniswami, “Automated detection of convulsive seizures using a
wearable accelerometer device,” IEEE Trans. Biomed. Eng., vol. 66,
no. 2, pp. 421–432, Feb. 2019.

[23] S. Kalitzin, G. Petkov, D. Velis, B. Vledder, and F. L. da Silva,
“Automatic segmentation of episodes containing epileptic clonic seizures
in video sequences,” IEEE Trans. Biomed. Eng., vol. 59, no. 12,
pp. 3379–3385, Dec. 2012.

[24] E. Geertsema et al., “Automated video-based detection of nocturnal con-
vulsive seizures in a residential care setting,” Epilepsia, vol. 59, no. S1,
pp. 53–60, Jun. 2018.

[25] S. Beniczky, T. Polster, T. W. Kjaer, and H. Hjalgrim, “Detection of
generalized tonic–clonic seizures by a wireless wrist accelerometer: A
prospective, multicenter study,” Epilepsia, vol. 54, no. 4, pp. e58–e61,
Apr. 2013.

[26] S. Coussens et al., “Movement distribution: A new measure of sleep
fragmentation in children with upper airway obstruction,” Sleep, vol. 37,
no. 12, pp. 2025–2034, 2014.

[27] J. De Koninck, D. Lorrain, and P. Gagnon, “Sleep positions and position
shifts in ﬁve age groups: An ontogenetic picture,” Sleep, vol. 15, no. 2,
pp. 143–149, 1992.

[28] O. Walch, Y. Huang, D. Forger, and C. Goldstein, “Sleep stage prediction
with raw acceleration and photoplethysmography heart rate data derived
from a consumer wearable device,” Sleep, vol. 42, no. 12, 2019, Art. no.
zsz180.

[29] Y. Zhuo, H. Zhu, and H. Xue, “Identifying a new non-linear CSI phase
measurement error with commodity WiFi devices,” in Proc. IEEE 22nd
Int. Conf. Parallel Distrib. Syst. (ICPADS), 2016, pp. 72–79.

[30] D. G. Tucker, “The invention of frequency modulation in 1902,” Radio

Electron. Eng., vol. 40, no. 1, pp. 33–37, 1970.

[31] B. P. Lathi, Modern Digital and Analog Communication Systems.

Oxford, U.K.: Oxford Univ. Press, 1998.

[32] J. R. Carson, “Notes on the theory of modulation,” Proc. Inst. Radio

Eng., vol. 10, no. 1, pp. 57–64, 1922.

[33] J. Zhang, W. Xu, W. Hu, and S. S. Kanhere, “WiCare: Towards in-situ
breath monitoring,” in Proc. EAI Conf. Mobile Ubiquitous Syst. Comput.
Netw. Services, 2017, pp. 126–135.

[34] K. Barrett, S. Barman, H. Brooks, and J. Yuan, Ganong’s Review of

Medical Physiology. London, U.K.: McGraw-Hill Educ., 2019.

[35] J. Liu, Y. Wang, Y. Chen, J. Yang, X. Chen, and J. Cheng, “Tracking
vital signs during sleep leveraging off-the-shelf WiFi,” in Proc. ACM
Symp. Mobile Ad Hoc Netw. Comput., 2015, pp. 267–276.

[36] R. Quiroga, H. Garcia, and A. Rabinowicz, “Frequency evolution dur-
ing tonic-clonic seizures,” EMG Clin. Neurophysiol., vol. 42, no. 6,
pp. 323–332, 2002.

[38] K. Mahr et al., “Prone, lateral, or supine positioning at seizure onset
determines the postictal body position: A multicenter video-EEG mon-
itoring cohort study,” Seizure, vol. 76, pp. 173–178, Feb. 2020.
[39] T. M. E. Nijsen, R. M. Aarts, P. J. M. Cluitmans, and P. A. M. Griep,
“Time-frequency analysis of accelerometry data for detection of
myoclonic seizures,” IEEE Trans. Inf. Technol. Biomed., vol. 14, no. 5,
pp. 1197–1203, Sep. 2010.

[40] W. Wang, A. X. Liu, M. Shahzad, K. Ling, and S. Lu, “Understanding
and modeling of WiFi signal based human activity recognition,” in Proc.
ACM Int. Conf. Mobile Comput. Netw., 2015, pp. 65–76.

[41] D. Halperin, W. Hu, A. Sheth, and D. Wetherall, “Tool release: Gathering
802.11n traces with channel state information,” ACM SIGCOMM
Comput. Commun. Rev., vol. 41, no. 1, p. 53, 2011.

[42] H. S. Barrows, “An overview of the uses of standardized patients for
teaching and evaluating clinical skills,” Acad. Med., vol. 68, no. 6,
pp. 443–443, 1993.

[43] B. Dworetzky et al., “Interprofessional simulation to improve safety in
the epilepsy monitoring unit,” Epilepsy Behav., vol. 45, pp. 229–233,
Apr. 2015.

[44] J. Van Andel, R. D. Thijs, A. de Weerd, J. Arends, and F. Leijten, “Non-
EEG based ambulatory seizure detection designed for home use: What
is available and how will it inﬂuence epilepsy care?” Epilepsy Behav.,
vol. 57, pp. 82–89, Apr. 2016.

[45] U. Kramer, S. Kipervasser, A. Shlitner, and R. Kuzniecky, “A novel
portable seizure detection alarm system: Preliminary results,” J. Clin.
Neurophysiol., vol. 28, no. 1, pp. 36–38, 2011.

[46] K. Van Poppel, S. P. Fulton, A. McGregor, M. Ellis, A. Patters, and
J. Wheless, “Prospective study of the EMFIT movement monitor,”
J. Child Neurol., vol. 28, no. 11, pp. 1434–1436, 2013.

[47] J. Arends et al., “Multimodal nocturnal seizure detection in a residential
care setting: A long-term prospective trial,” Neurology, vol. 91, no. 21,
pp. e2010–e2019, 2018.

Belal Korany (Member, IEEE) received the B.Sc.
and M.Sc. degrees in electrical and computer engi-
neering from Cairo University, Giza, Egypt, in 2012
and 2015, respectively. He is currently pursuing the
Ph.D. degree in electrical and computer engineering
with the University of California at Santa Barbara,
Santa Barbara, CA, USA, in 2015.

His research interests include wireless sensing
and signal processing. His research has appeared
in several reputable news outlets, such as BBC,
TechXplore, and others.

IEEE)

Yasamin Mostoﬁ (Fellow,
received the
B.S. degree in electrical engineering from Sharif
University of Technology, Tehran, Iran, in 1997, and
the M.S. and Ph.D. degrees in the area of wireless
communications from Stanford University, Stanford,
CA, USA, in 1999 and 2004, respectively.

She is currently a Professor with the Department
of Electrical and Computer Engineering, University
of California at Santa Barbara, Santa Barbara, CA,
USA. Her research has appeared in several reputable
news venues, such as BBC, Hufﬁngton Post, Daily
Mail, Engadget, and NSF Science360, among others. Her research is on
mobile sensor networks. Current research thrusts include X-ray vision for
robots, RF sensing, communication-aware robotics, occupancy estimation,
see-through imaging, and human–robot collaboration.

Prof. Mostoﬁ was a recipient of 2016 Antonio Ruberti Prize from IEEE
Control Systems Society, the Presidential Early Career Award for Scientists
and Engineers, the National Science Foundation CAREER award, and the
IEEE 2012 Outstanding Engineer Award of Region 6, among other awards.
She currently serves on the Board of Governors for IEEE Control Systems
Society and is also a Senior Editor for the IEEE TRANSACTIONS ON
CONTROL OF NETWORK SYSTEMS.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:20 UTC from IEEE Xplore.  Restrictions apply.
