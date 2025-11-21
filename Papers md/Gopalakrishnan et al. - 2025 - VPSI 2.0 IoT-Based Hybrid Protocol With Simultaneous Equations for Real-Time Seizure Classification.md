# Gopalakrishnan et al. - 2025 - VPSI 2.0 IoT-Based Hybrid Protocol With Simultaneous Equations for Real-Time Seizure Classification

5412

IEEE INTERNET OF THINGS JOURNAL, VOL. 12, NO. 5, 1 MARCH 2025

VPSI 2.0: IoT-Based Hybrid Protocol With
Simultaneous Equations for Real-Time Seizure
Classiﬁcation and False-Negative Mitigation

Karthikeyan Gopalakrishnan , Arunkumar Balakrishnan , Kousalya Govardhanan,
and Kandala N. V. P. S. Rajesh

Abstract—Nonepileptic seizures are a clinical symptom of
abnormally high synchronous cortical activity known as psy-
chogenic nonepileptic seizures (PNESs) as they exhibit no
outward signs of neurological damage. The need for differenti-
ating PNES from full-body general seizures (GTCSs) decreases
therapy time and ensures proper hospice. Internet of Medical
Things (IoMT) provide a closed-loop mechanism to accurately
measure seizures. The erratic nature of seizures has drawn the
attention where false detection could have catastrophic impact.
This article discusses the vibration proﬁle seizure identiﬁer
(VPSI) 2.0 where vibration proﬁle analysis of an ictal patient is
measured in real-time to classify seizures in an IoMT framework.
The novel seizure detection model has been proposed for
differentiating between multiple seizure types. The simultaneous
equation (S.E) protocol
is developed for noninvasive stigma-
free monitoring of seizures for continual monitoring. S.E-based
Internet of Things (IoT) seizure classiﬁer is helpful to mitigate
challenges present in detecting real-time occurrences of seizure
by 95.683% in a controlled environment.

Index Terms—Generalized tonic-clonic

(GTCS),
Internet of Medical Things (IoMT), Internet of Things (IoT),
psychogenic nonepileptic seizure (PNES), seizures.

seizure

I. INTRODUCTION

P SYCHOGENIC nonepileptic seizures (PNESs) mimic

epileptic seizures but do not involve aberrant electrical
discharges in the brain. These episodes might cause tonic
or clonic limb movements. Sexually or physically abused
people, especially adult women, are more likely to acquire
PNES. Few PNES patients obtain the necessary information
to control seizures without psychological trauma. The inter-
play between these risk factors that cause ictal episodes is
unknown. Depression, anxiety, post-traumatic stress disorder,
and psychological difﬁculties may occur as adverse effects.

Received 6 August 2024; revised 3 October 2024; accepted 22 October
2024. Date of publication 28 October 2024; date of current version
21 February 2025. (Corresponding author: Arunkumar Balakrishnan.)

Karthikeyan Gopalakrishnan is with the Department of Computer Science
and Engineering, Coimbatore Institute of Technology, Coimbatore 641014,
India (e-mail: karthikeyan.g@cit.edu.in).

Arunkumar Balakrishnan is with Department of Information Technology,
Manipal Institute of Technology Bengaluru, Manipal Academy of Higher
Education, Manipal, India (e-mail: arunkumar.b@manipal.edu).

Kousalya Govardhanan is with the Department of Computer Science
and Engineering, Dayananda Sagar University, Bengaluru 560078, India
(e-mail: kousalya-cse@dsu.edu.in).

Kandala N. V. P. S. Rajesh is with SENSE, VIT-AP, Amaravathi 522237,

India (e-mail: rajesh.k@vitap.ac.in).

Digital Object Identiﬁer 10.1109/JIOT.2024.3486991

Thus, an intelligent healthcare solution is needed to improve
seizure detection and management, reducing long-term issues.
The research provides an intelligent sensor prototype for
epileptic seizure detection. These sensors can detect seizures
by replicating them on a prosthesis.

PNESs are misdiagnosed as status epilepticus 8.1% of the
time, making treatment difﬁcult. At a rate of 20.1%, adolescents
and young adults had the highest relative occurrence. Poor
diagnosis of PNES patients can lead to respiratory depression
and inappropriate intubation, which occurred in 26% of cases
of anti-seizure medicine maladministration. In 33% of patients,
adjunctive pharmacotherapy causes nonresponsiveness and
signiﬁcant adverse effects. This emphasizes the importance of
precise diagnosis and individualized treatment [1].

The detection of seizures encompasses a range of tech-
niques, such as clinical observation conducted by healthcare
experts, electroencephalography (EEG), video-EEG monitor-
ing, ambulatory EEG, diagnostic imaging, seizure diaries, and
seizure alarms. However, these methods have drawbacks. EEG
and imaging are limited by cost and availability. Invasive
monitoring is risky and not always necessary. Different detec-
tion methods are sensitive to seizures, which could potentially
miss subtle manifestations. External factors, including patient
adherence and subjective seizure diary and clinician observa-
tion can also cause diagnostic changes and ambiguity. Patients
feel even more ostracized because many detecting tools tend
to be inappropriate for public wear. Existing seizure detection
systems, including EEG caps, large-scale monitoring devices,
and wrist-worn sensors, are often highly visible and intrusive,
which may exacerbate the social stigma faced by patients
when used in public settings. These tools can draw unwanted
attention, leading to feelings of self-consciousness and social
ostracization. To address this issue, the proposed wearable
technology aims to be discreet and seamlessly integrated into
everyday clothing or accessories, thereby reducing the visibil-
ity of the device and helping patients feel more comfortable
and less stigmatized in public settings.

This study seeks to address these challenges by developing
a compact, unobtrusive device for ictal monitoring and seizure
classiﬁcation. The system enables continuous monitoring and
accurate seizure detection without disrupting patients’ daily
activities. Utilizing advanced sensor technologies and real-time
data processing algorithms, the wearable device offers dis-
creet, noninvasive seizure detection and classiﬁcation. Unlike

2327-4662 c(cid:2) 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:25 UTC from IEEE Xplore.  Restrictions apply. 

GOPALAKRISHNAN et al.: VPSI 2.0: IoT-BASED HYBRID PROTOCOL WITH SIMULTANEOUS EQUATIONS

5413

TABLE I
LIST OF ACRONYMS AND TERMS

Fig. 1. Closed loop solution of epilepsy monitoring.

traditional monitoring methods, such as cumbersome EEG
systems or manual recordings by caregivers,
these smart-
watches are inconspicuous and integrate effortlessly into daily
life. Historically, individuals with epilepsy have experienced
social stigmatization stemming from misunderstandings and
misconceptions about the condition. The presence of visible
monitoring devices or the necessity for constant supervi-
sion can intensify feelings of being different or singled
out, potentially leading to social isolation or discrimination.
Additionally, the noninvasive nature of this technology elim-
inates the need for uncomfortable attachments or intrusive
procedures, making the monitoring process more comfortable
and less distressing for patients. This level of discretion signif-
icantly reduces the visibility of the medical condition, thereby
minimizing the stigma often associated with epilepsy and
other seizure disorders. The device’s portability and simplicity
provide patients more autonomy and trust in managing their
medical condition, improving their quality of life.

By integrating seizure detection sensors with intelligent
categorization and identiﬁcation algorithms, the efﬁciency and
accuracy of identifying appropriate hospice care protocols can
be signiﬁcantly enhanced. Seizure monitors measure periodic
vibration proﬁles to track preictal, postictal, and ictal states [2],
[3], [4], [5]. The neurologist can develop an appropriate
course of treatment for an individual with epilepsy, whether
they experience psychogenic nonepileptic seizures (PNESs) or
generalized seizures. The Internet of Things (IoT) closed-loop
monitoring system uses S.E. technology to detect seizures.
Refer to Fig. 1. The suggested seizure monitoring system is
an IoT-integrated system for nonclinical seizure observation.
It would make classifying sporadic and unpredictable seizures
easier to reduce their impact.

A. Preliminaries and Background

Currently, patients with seizures often face a signiﬁcant
loss of independence due to the unpredictable onset of their
episodes. This study examines an IoT-based vagus nerve stim-
ulation (VNS) system designed to deliver calibrated electrical
impulses to the vagus nerve via the jugular region, providing
targeted therapeutic intervention. The detection mechanism
was limited by to detecting generalized tonic-clonic seizure

(GTCS) seizure by studying the pulse and blood circulation
parameters. If the patient is suffering from a localized seizure
the system under study will be ignorant of the difference. Thus,
for patients with PNES to beneﬁt from therapies like VNS or in
general to have a quicker and clearer understanding of the type
of seizures encountered by patients a system with demarcation
prerogatives for accurate classiﬁcation is mandatory. The
proposed system utilizes the seizure protocols of GTCS and
trained protocols for PNES for accurate classiﬁcation.

B. Acronyms and Terms

To facilitate a clear understanding of

the terminology
and abbreviations used throughout this article, we provide a
comprehensive list of acronyms and terms in Table I. This
section includes deﬁnitions for key terms related to seizure
disorders, diagnostic methods, and treatment approaches,
ensuring that readers can easily reference and comprehend the
concepts discussed in the following sections. The table below
outlines these terms and their meanings.

C. Our Vision: Precise IoMT Seizure Classiﬁcation: VPSI
2.0

During ictal and preictal stages, monitoring indicators like
blood pressure (B.P.), heart rate, and bodily motions can help
control epilepsy. This enables proper control. Consult [6].
Epileptics with unexpected seizures must recognize and iden-
tify seizures. The patient’s EEG is monitored in real time
during ictal stages. Neurologist understands and advises on
seizure prevention. However, EEG is not a practical method
time. B.P., heart rate,
for nonclinical monitoring in real
and vibration patterns are thus examined as an alternative
biomarker. Continuous monitoring could improve epilepsy
care with the data. Refer to Fig. 2 for our Internet of Medical
Things (IoMT)-based seizure classiﬁcation concept.

vibration proﬁle seizure identiﬁer (VPSI) 2.0 is a noninva-
sive, wearable intelligent biomarker observation device with
a continuous seizure classiﬁer. This classiﬁer uses a body
vibration sensing method [7]. It expands on our previous
article, “GTCS-Vagus Nerve Stimulator Automation Using
Private IoT-Blockchain Smartcontract.” It addresses electri-
cal therapy for grand-mal seizures with security measures.
Training data from an 18-year-old Brazilian patient with
the seizure
myoclonic GTCSs were utilized to construct
classiﬁer. Normal and ictal seizure patterns were analyzed

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:25 UTC from IEEE Xplore.  Restrictions apply. 

5414

IEEE INTERNET OF THINGS JOURNAL, VOL. 12, NO. 5, 1 MARCH 2025

(SUDEP) requires a clear plan and caregiver advice. Medical
device categorization protocols in the IoT are essential for
seizure diagnosis and treatment. The S.E approach improves
PNES sensor detection of small patterns. S.E. optimizes the
accuracy of detection by effectively counterbalancing error
patterns identiﬁed in a patient’s seizures, thereby eliminating
the necessity for human intervention. This balancing is nec-
essary because conventional sensors can only detect 38.2% of
seizures (simulated). The objective of S.E. is to determine a
solution that satisﬁes all equations simultaneously [23]. S.E is
a set of two or more equations that involve multiple variables,
where the goal is to ﬁnd a common solution that satisﬁes all
equations simultaneously [23]. The S.E solution is a simple
and efﬁcient approach that may be implemented with minimal
specialized apparatus. Seizure classiﬁers use S.E protocols to
improve closed loop epilepsy monitoring system precision and
conﬁdence.

This article’s ﬂow is as follows. Section II summarizes the
main contribution and prior research. Section III discusses the
S.E classiﬁcation prosthetic model. The S.E model is explained
in Section IV. Section V discusses the outcomes. Section VI
concludes and outlines future directions.

II. PRIOR RESEARCH WORK AND NOVEL CONTRIBUTION

A. Related Work and Consumer Products

Smart healthcare is one of the most sought-after applications
of IoT with an estimated 176 billion by 2026 [24]. IoT in
healthcare has allowed physicians and caregivers an afford-
able avenue to treat patients continuously in a nonclinical
environment. This technology allows patients, including those
to
who may be unconscious or incapacitated by seizures,
receive timely and continuous care while managing their
health conditions outside of traditional clinical settings. This
advancement enhances both the convenience and accessi-
bility of medical monitoring and intervention. Neuro-Detect
presented a smart healthcare solution that combined EEG with
a machine learning model [23], [23], [24]. The IoT framework
was utilized to create an automated seizure recognition system,
which employed DWT and DNN approaches. Similarly, the
smart IoT-edge gateway for wellness care was designed to
work with a variety of medical equipment [24]. A novel
packet generation structure was created to address interoper-
ability difﬁculties with healthcare sensors in consumer medical
ecosystems. GTCS epilepsy monitor via smart watch heart
rate monitoring was developed using Blockchain framework.
The biomarker spike percentile was used to detect patterns in
real time. For seizure management, speciﬁc seizure category-
based monitoring was lacking due to the erratic nature of
seizures. Continuous monitoring technology was sought to
replace traditional observation techniques to maintain a round-
the-clock situation report in epilepsy patients.

as

such

Commercial epilepsy monitoring devices are primarily
“Epileptic-Seizure-Detection-Using-

EEG-based,
DWT-Based-Fuzzy-Approximate-Entropy-And-Support-
Vector-Machine.” However, they lack wearability, requiring
patients to remain still, hindering daily monitoring and causing
[24].
social stigma if openly disclosed [23],

[23],

[24],

Fig. 2. Stakeholder communication ﬂow of closed loop solution.

using this data [8]. Seizures are categorized using vibration
characteristics in this study. The wearable classiﬁcation system
VPSI 2.0 confronts many challenges, including: 1) patients’
seizure patterns ﬂuctuate; 2) sensor selection and response
for seizure detection; and 3) identifying seizure types without
false-negatives throughout preictal and ictal stages.

While the classiﬁer was trained using data from a single
18-year-old Brazilian patient with myoclonic GTCSs,
the
consistent features of GTCS—such as generalized spike-and-
wave discharges and rhythmic muscle contractions—support
the applicability of this dataset. The classiﬁer’s generalizability
is reinforced by rigorous validation, including cross-validation
techniques, which ensure its reliability. Clinical experts have
the dataset accurately reﬂects typical GTCS
afﬁrmed that
presentations. Although expanding the dataset remains a chal-
lenge, the scalable methodology employed allows for future
integration of diverse data to further validate and reﬁne the
model. The model has demonstrated robust effectiveness in
distinguishing GTCS from normalcy to detect PNES, with sev-
eral factors ensuring its scalability. Seizure types often exhibit
overlapping physiological markers, such as EEG patterns and
autonomic responses, which allow the model to generalize
across diverse seizure presentations. Rigorous cross-validation
strengthens its reliability, while the simultaneous equation
(S.E) framework ensures adaptability by integrating features
speciﬁc to other seizures. Incorporating insights from absence
and focal seizures, further expanding the S.Es can achieve
broader generalizability and scalability across all seizure types.
A seizure classiﬁer for epileptic patients’ erratic movements
has been developed. This classiﬁer detects preictal and ictal
epilepsy using vibration oscillations, B.P. spikes, and heart
rate ﬂuctuations. Patient seizures, such as GTCS (Grand-Mal)
or PNES, would be classiﬁed using the vibration model in
the proposed seizure classiﬁer. Citations include [9], [23]. The
model would delineate seizures based on observed deviations
in nominal and seizure states and BP and HR data. Nonclinical
epilepsy monitoring can be done with the classiﬁer to protect
patients’ privacy and minimize social shame. GTCS and
PNESs can be accurately measured and analyzed with the
technology. Preventing sudden unexpected death in epilepsy

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:25 UTC from IEEE Xplore.  Restrictions apply. 

GOPALAKRISHNAN et al.: VPSI 2.0: IoT-BASED HYBRID PROTOCOL WITH SIMULTANEOUS EQUATIONS

5415

TABLE II
COMPARISON OF SEIZURE DETECTION RESEARCH WORKS

Another FDA-approved device is the “Embrace” smart system,
employing sensors like accelerometer, electrodermal activity,
temperature, and gyroscope to record data and alert seizures,
albeit without distinguishing among them [23], [23], [24].
Gammacore (nVNS—Vagus Nerve Stimulator) technology
targets chronic headaches through VNS but lacks speciﬁcity in
post-ictal therapy [24], [25]. Existing devices detect seizures
but
limited to speciﬁc types and require frequent patient-
speciﬁc calibrations, lacking robust classiﬁcation and 24 × 7
nonclinical assessment [26], [27], [28], [29], [30].

The parameters outlined in Table II provide a comprehen-
sive framework for evaluating the multidimensional impact
of seizures on both patients and caregivers, as commonly
considered by epileptologists. Given these limitations, there is
a pressing need for more advanced and user-friendly epilepsy
monitoring solutions. Addressing these challenges, the current
paper introduces a novel approach that signiﬁcantly improves
upon existing technologies.

B. Novel Contributions of the Current Paper

the current paper

Building upon these insights,

intro-
duces an accurate noninvasive edge device, the GTCS-Vagus
Nerve Stimulator Automation Using Private IoT-Blockchain
Smartcontract. This device delivers electrical
therapy to
GTCS seizure patients securely and inexpensively. It is an
IoT-integrated wearable gadget that uses instantaneous heart
rate and pulse variation with Smartcontract for security. To
reduce false positives (FPs), patient-speciﬁc seizure patterns
were calibrated against an open-source seizure data set of an
18-year-old myoclonic GTCS epileptic patient. The current
paper presents an accurate real-time seizure classiﬁcation
employing calibrated vibration protocols as VPSI 2.0, which
provides IoMT-integrated continuous seizure monitoring. It
presents a novel and reliable seizure classiﬁcation approach for
on-site diagnosis, incorporating a closed-loop control system
to mitigate associated stigma. The need for a transparent
and robust sensing technology as outlined by Qi et al., [31]
is evident from the inferences of patient clinical and oral
testimonies.

This article proposes the following major contributions.
1) Affordable counter-balanced closed-loop monitoring

system.

2) VPSI 2.0 serves IoMT networks with a wearable, low-
energy protocol. Mitigates stigma as it can be worn
beneath clothes.

3) The IoMT-incorporated closed-loop system assesses HR,
BP, and movement patterns to categorize seizures.

Fig. 3.

Ictal vibration classiﬁer with IoMT framework.

4) The system is caregiver-independent and uses a cali-

brated, low-cost counter-balance for accuracy.

III. PROPOSED SEIZURE CLASSIFIER: VPSI 2.0

The seizure model integrates with VPSI 2.0 to detect ictal
vibrations in real time. Furthermore, the heart rate and B.P. are
used to corroborate and validate the preictal and ictal ﬁndings.
The ictal categorization system responds to biomarker stimuli,
as seen in Fig. 3.

A. Closed Loop Ictal Classiﬁer

The intelligent VPSI 2.0 ictal sensor at the carotid, ulnar,
and radial nodes will continually monitor the epileptic patient.
The ictal phase of a seizure causes erratic body movements
at one node or throughout the body. Brain discharges that
deviate from the expected course induce GTCS seizures in
humans. Stress-related, psychological, or emotional displays
may resemble epileptic convulsions. GTCS’s ictal phase
affects the entire body, causing post-ictal coma. In contrast,
PNES localizes ictal symptoms to one or more limbs while
retaining consciousness. In preictal and ictal stages, B.P. and
heart rate ﬂuctuate greatly, although GTCS and PNES differ
minimally. The distinctions in GTCS and PNES symptoms,
together with B.P. and pulse rate, can assist delineate seizure
types in such circumstances. Localized ictal episodes and
biomarker spikes can indicate PNES, while a trigger of all
three nodes and a drop in biomarkers due to LOC can
indicate GTCS. Accurate seizure type detection necessitates
effective noise elimination and minimization of false negatives
(FNs), which are critical for improving nonclinical monitoring

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:25 UTC from IEEE Xplore.  Restrictions apply. 

5416

IEEE INTERNET OF THINGS JOURNAL, VOL. 12, NO. 5, 1 MARCH 2025

and optimizing therapeutic recommendations. Nonetheless, the
presence of FNs diminishes detection accuracy, making the
application of counterbalance techniques essential.

B. Proposed Seizure Classiﬁcation Model

TABLE III
IMPACT OF VARIABLES ON DETECTION ACCURACY

GTCS(t) dt{t, 35, 75}

.

(2)

C. S.E Protocol–Augmenting Vibration Accuracy

A new seizure detection and classiﬁcation model uses
vibration patterns as the major classiﬁcation parameter and
mean arterial pressure (MAP) and B.P. as supplementary
factors. The patient’s wrist and neck’s ulnar, carotid, and radial
nodes determine the vibration pattern. Equations (1) and (2)
deﬁne the PNES-GTCS difference equation

PNESId(Rw)n =

Test Cases(cid:2)

(cid:3)(cid:4)

75

0.025 · BP(t) dt{t, 35, 75}

35

(cid:5)

(1)

GTCS(t) dt{t, 35, 75}
(cid:3)(cid:4)

75

0.025 · BP(t) dt{t, 35, 75}

35

(cid:5)

n=0
(cid:4)

75

−

35
Test Cases(cid:2)

n=0
(cid:4)

75

35

−

PNESId(Lw)n =

The system was calibrated against the B.P limit of (35, 75)
to restrict detection to the nominal range of age considered,
and non-PNES indicators were eliminated using a comparable
range of veriﬁed GTCS seizures. This is to generate a close
approximation of the myoclonic patient used as a reference.
0.025 is the ﬁrst calibration offset
to improve detection
accuracy. Whereas PNES_Id(L_W)n and PNES_Id(R_W)n
indicate the variation rate displayed in the ulnar and radial
nodes, using GTCS parameters from the previous model as
references to highlight differences. The two nodes will identify
seizures alone during PNES, whereas all nodes experience
GTCS

PNESId(N_k)n =

Test Cases(cid:2)

(cid:4)

75

n=0

35

0.025 · BP(t) dt{t, 35, 75}. (3)

Whereas PNES_Id(L_Wrist)n is detected exclusively
because both PNES and GTCS use the carotid nerve as an
intermediate; (4) deﬁnes seizure range by active seizure rate
change

(cid:6)

Range =

PNESId(Rw)n − PNESId(Lw)n
(cid:6)
Vp ∗ PNESId(N_k)n
ModBm

(cid:7)
.

(4)

(cid:7)

In (4), the “Range” [−0.025 to −0.075] rate measurement
compares node statements and differentiates them to identify
seizure type, where Bp, Hr, and Vp indicate node biomarkers.
The modulus function is used to separate the inﬂuence of
outliers observed on account of noise and unexpected volatility
in ictal states

Sez_Tpe =

PNES_Id(N_k)n
Range · (PNES_Id(L_W) + R_W)n

.

(5)

In (4), “Sez_Type” represents seizure type detection, using
the carotid node as a reference for GTCS absence. Grand-mal
seizures result in “-ve” ranges, while PNES results in zero

ranges. The original system had a 38.5% detection accuracy
due to sensor errors caused by noise, particularly from metal
prostheses in the experimental study. These introduced false
readings, especially in the vibration parameters, affecting
detection reliability. Additional factors, refer Table III, such as
motion artifacts, sensor sensitivity, environmental noise, and
signal interference, also contributed to the inaccuracies.

To mitigate these issues, artiﬁcial calibration using S.E
methods was applied to calculate counter-balance variables
at each detection point, signiﬁcantly reducing the impact of
noise and improving the system’s precision. This adjustment
provided more reliable seizure detection across parameters.

Individual SW-420 vibration sensors that monitor seizure
patients’ vibration patterns limit equation (5) via FNs. To
offset inaccurate negative results, we build deliberate inaccu-
racies into the equation. Under simulated scenarios of GTCSs,
PNESs, and normal states, equations show the proportion
of successfully recognized seizures to the total number of
seizures. The identiﬁcation of PNES includes LPNES (the left
wrist), RPNES (the right wrist), and NPNES (neck or jugular).
SW-420 vibration sensors are labeled α (the left wrist), β
(jugular), and γ (the right wrist) for S.Es.

S.E Hypothesis 1: Asymmetric Localized-Sensor

0.5α + 0.5β + 0.5γ = 0.7 GTCS
1.3α + 0.3β + 0.15γ = 0.43 L_PNES
0.15α + 0.3β + 1.3γ = 0.47 R_PNES
0.3α + 1.4β + 0.3γ = 0.6 N_PNES

α + β + γ = 1 Nominal.

(6)

S.E Hypothesis 2: Symmetric Localized-Sensor

0.5α + 0.5β + 0.5γ = 0.7 GTCS

α + 0.5β + 0.25γ = 0.43 L_PNES
0.25α + 0.5β + γ = 0.47 R_PNES
0.5α + β + 0.5γ = 0.6 N_PNES

α + β + γ = 1 Nominal.

(7)

These systems of equations, upon balancing, yield a factor
to counterbalance FNs from each wrist sensor. The Arduino
Uno, despite its limited computational power, can efﬁciently
solve a 5 × 5 system of linear equations, handling 125 cubic
operations within milliseconds and utilizing 120 bytes of its
2 KB SRAM capacity. The use of precomputed values (α =
0.346, β = 0.274, and γ = 0.034) signiﬁcantly reduces
computational complexity and ensures numerical stability.
This approach not only enhances real-time processing but also

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:25 UTC from IEEE Xplore.  Restrictions apply. 

GOPALAKRISHNAN et al.: VPSI 2.0: IoT-BASED HYBRID PROTOCOL WITH SIMULTANEOUS EQUATIONS

5417

maintains minimal computational impact, making it a viable
solution for accurate and efﬁcient seizure detection in practical
applications.

TABLE IV
ASYMMETRIC AND SYMMETRIC FINAL BALANCING FACTORS PER NODE

1) S.E Hypothesis 1: Asymmetric Localized-Sensor Biased
Counter-Balance Ratio Distribution: Individual sensors
at isolated seizure nodes are prioritized for seizure detec-
tion. The two ancillary sensors corroborate the seizure
site sensors’ detection percentile. GTCS is a grand-
mal seizure, an ictal phenomena experienced roughly
uniformly across the patient’s physiology, hence its
equation is symmetrical. “α, β, and γ ” indicate the
vibration sensor values from the left wrist, jugular, and
the right wrist, respectively

(cid:2)

a) Arriving β:

GTCS − N_PNES:0.5α + 0.5β + 0.5γ
= 0.7 − (0.5α + β + 0.5γ = 0.6)
thus, β = 0.2.

(13)

Principal_equation =

(GTCS + L_PNES + R_PNES

b) Arriving subequation γ via β in Principal_equation

+ N_PNES + Nominal)
= 3.25α + 3.5β + 3.25γ = 3.2.

(8)

a) Eliminating β:

L_PNES − R_PNES : 1.3α + 0.3β + 0.15γ = 0.43

Principal_equation = 3.25α + 3.5 × 0.2 + 3.25
(14)

γ = 0.769 − α(sol2) =⇒ γ = 3.2.

c) Arriving α via backpropagation of β = 0.2 and

γ = 0.769 − α in R_PNES

− (0.15α + 0.3β + 1.3γ = 0.47)
Sub − equation (1) : γ = 0.034 + α.

(9)

thus, α = 0.532.

(15)

0.25α + 0.5 × 0.2 + (0.769 − α) = 0.47

b) Arriving α:

d) Arriving γ through backpropagation to sol 2

N_PNES − Nominal : 0.3α + 1.4β + 0.3γ = 0.6

γ = 0.769 − α =⇒ γ = 0.237.

(16)

− (1.4α + 1.4β + 1.4γ = 1.4).

Replacing γ = 0.034 + α in N_PNES - Nominal

α = 0.346(sol1).

c) Arriving γ via backpropagation of α in (1)

γ = 0.034 + α = 0.38.

(10)

(11)

d) Arriving β through “Nominal” equation α + β +

γ = 1

β = 1 − 0.346 − 0.38 =⇒ β = 0.274.

(12)

Table I, titled “asymmetric factor,” validates counterbal-
ance variables for seizures and normalcy, reducing errors
by 32% and increasing detection to 68.375%.

2) S.E Hypothesis 2: Symmetric Localized-Sensor Biased

Counter-Balance Ratio Distribution:
localized seizure nodes at
The individual sensors at
the wrist are allocated equal priority in this iteration
to detect seizures. The subsequent
two sensors are
considered ancillary to the seizure site. The distribution
is symmetrical in the equation representing GTCS, and
the nominal values remain unchanged as they represent
the totality of seizures experienced throughout the body
in both nominal and ictal states

Principal_equation =

(cid:2)

GTCS + L_PNES + R_PNES

+ N_PNES + Nominal

= 3.25α + 3.5β + 3.25γ = 3.2 [Congruent of asymmetric].

This establishes that even if the distribution is modiﬁed
the overall contribution by sensors remain unaffected.

Counterbalance values are validated and displayed in
Table I. The variables are added into the Principal equation to
evaluate their validity in seizure-related and normal conditions.
The error mitigation achieved with sensor counterbalance is
18% higher compared to asymmetric distribution, resulting in
an increase in the detection percentile to 95.683%.

Exclusive PNES symptoms encompass limb thrashing, con-
trolled head movements, coherent verbal expression, loss of
consciousness, and responsiveness, distinguishing them from
GTCS manifestations.

IV. OUR PROPOSED VPSI 2.0 CLASSIFIER

Conventional seizure detection protocols are limited in their
ability to accurately classify closely similar ictal symptoms,
requiring precise calibration to address patient biomarker
variability and system-induced signal irregularities. Detection
in misdiagnosis and delays in therapy
errors may result
administration. The S.E protocol serves as a calibration
primitive, balancing FPs and negatives in medical devices.
Despite the inherent biomarker noise in epilepsy, S.E-based
hardware calibration, as depicted in Fig. 6,
incorporating
vibration sensors and biomarker recorders, proves useful for
identifying erroneous ictal
instances in automated seizure
detection systems. The S.E concept leverages patient-speciﬁc
seizure patterns recorded during nonictal phases and cali-
brated in real-time through the IoMT, offering a vital role
in identifying FNs during the patient’s ictal phase in PNES
cycles. The erratic nature of seizure detection enables S.E
to detect error patterns and issue counter-balance variables,
relying on offsets created by patient-speciﬁc seizure patterns
during ictal onset. While exact ictal offsets between patients

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:25 UTC from IEEE Xplore.  Restrictions apply. 

5418

IEEE INTERNET OF THINGS JOURNAL, VOL. 12, NO. 5, 1 MARCH 2025

Fig. 4. S.E-based PNES detection optimizer on VPSI 2.0.

Fig. 5. ASE on VPSI 2.0.

may be challenging to determine, S.E offers a generalized
solution for PNES versus GTCSs classiﬁcation with mini-
mal storage requirements. Consequently, S.E counter-balance
presents a promising approach to enhance detection integrity
and accuracy in nonclinical seizure monitoring.

A. S.E–VPSI 2.0 Architecture

S.E is useful to generate accurate response/detection and
is implemented on an Arduino-based wearable hardware to
extract the eccentricities of ictal phase. Arbiter S.E (ASE) is
considered where the three nodes generate erratic outcomes
and are reconﬁgured by activating the counter-balance as
shown in Figs. 4 and 5. ASE consists of three main com-
ponents known as calibration factor, node average, and node
corroboration factor (NCF). The calibration factor is created
with various unpredictable anomalies incurred during ictal
phase and the NCF is estimated per sensor failure versus
overall expected outcomes. The response is generated by
collectively quantifying distinctive detection failures of each
node.

Fig. 6.
torso prosthesis -1, 4) Arduino nano, and 5) Raspberry Pi housing.

Experimental testbed: 1) pulse input, 2) pulse sensor, 3) metallic

B. Hardware and Software Conﬁguration

To evaluate the proposed VPSI 2.0 classiﬁer framework, we
have deployed a real-world rest bed. The test bed consists of
two systems: 1) a Raspberry Pi 2 generator that simulates the
seizure patterns on a metallic prosthesis and 2) an Arduino
nano sensor that houses the S.E-based VPSI 2.0 protocol as
shown in Fig. 6.

The Raspberry Pi3, operating Raspbian on 1 GB RAM,
integrates with a plastic prosthesis mimicking human torso
dimensions. Adjusted by 32 cm for the neck and 15.2 cm
for the wrist, the prosthesis meets wrist girth requirements.
Seizure detection sites are strategically placed within 85 cm,
typical for a 170 cm person’s neck-to-wrist span. Vibration
patterns from the seizure dataset accurately represent patient
status during the ictal phase, while both the Raspberry Pi3
and metallic prosthesis facilitate data sensing. The Arduino R(cid:2)
Nano, powered by the ATmega328 microcontroller, offers
versatile functionality with 14 digital I/O, eight analog inputs,
and six PWM pins, including communication protocols and
input voltages of 7–12 V. The prototype’s laptop (Intel
Core i7-8550u CPU, 16 GB RAM, and 64-bit Windows 10)
collects data. The prototype system shows signiﬁcant potential
for accurate seizure detection through advanced sensing and
data collection. However, deploying this system on seizure
patients requires extensive testing to ensure safety and efﬁcacy.
In addition, regulatory approval from the Drugs Controller
General of India (DCGI) under the Central Drugs Standard
Control Organization (CDSCO) is crucial to ensure adherence
to the required standards and regulations prior to clinical
implementation.

C. S.E-Based VPSI 2.0 Device Optimization

S.E.-based lightweight counter-balance protocol ensures
device accuracy. A trusted seizure detection mechanism in
the IoMT network is established using the offered economic
method. Two phases incorporate counter-balance variables into
identiﬁed variables in the proposed optimization mechanism:
1) validation and 2) feed-forward.

1) S.E-Based Validation in VPSI 2.0: The validation phase
occurs concurrently with seizure detection in-house during
the ictal phase. Node-speciﬁc counterbalances are applied and
collected for each detection. Following successful detection,

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:25 UTC from IEEE Xplore.  Restrictions apply. 

GOPALAKRISHNAN et al.: VPSI 2.0: IoT-BASED HYBRID PROTOCOL WITH SIMULTANEOUS EQUATIONS

5419

Algorithm 1 Seizure Detection and Validation
Require: α, β, γ , TD_Nominal[n],

TD_Ict[n], Balances:0.532(α), 0.2(β), 0.237(γ )
Ensure: Decision on the validity of detected seizures
1: for k ← 0 to n do
2:

Calculate Errors: Err_α[k] ← |α − TD_Nominal[k]| &
Err_β[k] ← |β − TD_Nominal[k]| & Err_γ [k] ← |γ −
TD_Nominal[k]|
Counterbalance Errors: Err_α_bal ← Err_α ∗ 0.532 &
Err_β_bal ← Err_β ∗ 0.2 & Err_γ _bal ← Err_γ ∗ 0.237
Bal Err: Tot_err ← Err_α_bal + β_bal + γ _bal
Des:Tot_err[w_in]th_hld?seiz ⇒ valid:Declaration ⇒ NFR.

3:

4:
5:
6: end for

Algorithm 2 Detection Optimization With SGD
Require: T_D_Nominal, T_D_Ict, α, β, γ , lr, batch_size
Ensure: Decision on the validity of detected seizures
Deﬁne

1: Initialize

cntr-bal:

α, β, γ

L(α, β, γ ), tot_err, bat_err, mini_bat(tra_data, bat_sz)

2: Err_Cal(data_point,

α, β, γ ),
Grad_Calc(Errors), validation_data

loss_fun:

Tot_Err_Cal(Errors),

for batch in mini_bat(trai_data, bat_sz) do

batch_error = 0
for data_point in batch do

3: for epoch in range(num_epochs) of Rand_train_data do
4:
5:
6:
7:
8:

Errors ← ErrorCalculation(data_point, α, β, γ )
∂α , ∂L
Grad = ∂L
(Errors), Grad_Calc(Errors)

∂β , ∂L

∂γ & Tot_Err, Grad ← Tot_Err_Cal

9:
10:

end for
Update SGD cnt-bal: α = α − lr ∗ ∂L
γ = γ − lr ∗ ∂L
∂γ

∂α β = β − lr ∗ ∂L
∂β

end for

11:
12: end for

the reﬁned node detections are consolidated by the wearable
Arduino processor, as detailed in Algorithm 1.

2) Feedforward Protocol for VPSI 2.0: The validation pro-
tocols are implemented through a feed-forward mechanism
using stochastic gradient descent (SGD) to minimize the
loss function during training. Training proceeds over a ﬁxed
number of epochs. Within each epoch, the training data is
shufﬂed and divided into mini-batches of a speciﬁed size. For
each mini-batch (batch_size), the total error and gradients of
the loss function with respect to the counter-balance values
are computed for each data point. The counter-balance values
are then updated using SGD with a ﬁxed learning rate (lr)
and the computed gradients. After processing each mini-batch,
the average batch error is computed to track training progress.
Subsequently, the performance of the updated counter-balance
values is validated on a separate dataset to assess generaliza-
tion. The authentication phase is detailed in Algorithm 2.

V. EXPERIMENTAL RESULTS

The proposed seizure detection technique was validated in
1754 trials on a synthetic prosthesis generating artiﬁcially
generated ictal proﬁles from three GTCS and four PNES
patients under neurologist supervision. Gait, physical vibra-
tions, pre- and post-ictal investigations, B.P., and heart rate
ﬂuctuations were used to create the ictal proﬁle. The model’s
detection results were tracked and compared to real-time ictal

patterns to ensure accuracy. The simulation uses functional
parameters to observe ictal detection false-negatives. A range
of conditions were utilized to evaluate the proposed approach
across multiple ictal variations in both grand mal and localized
epilepsy patterns.

Table II compares our proposed ictal optimization model
with state-of-the-art studies. While previous validation relied
on one-on-one interviews, our real-time seizure pattern anal-
ysis, coupled with hardware security, validates our model for
safe detection of GTCS and PNES seizures.The experiment
rate post-counter-
recorded ﬂuctuations in BP and heart
balance. MAP denotes MAP, while SBP, DBP, and HR
represent systolic and diastolic B.P., and heart rate, respec-
tively. Where MAP=DBP+1/3(SBP-DBP). Refer Tables VI
the experiment carried
and VII. The overall dataset
out can be referred to at https://archive.org/download/data-
comparison-ﬁndings-submissionArchive.org Data Submission.

for

A. Comparison: S.E Calibrated Detection Outcomes

The system’s performance was re-evaluated over 1754
iterations using an asymmetric error balance with alpha set at
0.346, beta at 0.274, and gamma at 0.034. The results showed a
62% increase in accuracy for the ulnar node, a 71.2% increase
for the carotid node, and a 68.5% increase for the radial node.
The accuracy equation, detailed in (18), involves true positives
(TPs), true negatives (TNs), FPs, and FNs

Accuracy = (TP + TN) ÷ (TP + TN + FP + FN).

(17)

Retesting with symmetric error balancing led to a positive
detection percentile increase of 79.68%, 81.68%, and 80.68%
for ulnar, carotid, and radial nodes, respectively.

In the simulation model, ulnar nodes exhibited a failure
rate 0.73% higher than comparable nodes. The carotid node
outperformed radial and ulnar nodes by 2.5% in GTCS and
PNES identiﬁcation. Housing material vibration dampness
signiﬁcantly affects detection loss. System sensitivity exhibited
slight inverse proportionality to augmented protocol calibration
oscillation, optimizing FPs and FNs by 58.645%. See Fig. 7,
where Sensitivity = TP ÷ (TP + FN), speciﬁcity = TN ÷ (TN
+ FP), F-P Rate = FP ÷ (TN + FP), F-N Rate = FN ÷ (TP
+ FN), and F1-score = 2 * T P ÷ (2 * (T P + F P + F N)).
The overall improvement factor was assessed for all three
nodes against asymmetric localized-sensor biased counter
balance ratio distribution outcomes. Symmetric counterbalance
yielded a 21.69% enhancement in ulnar node performance
compared to asymmetric calibration. In the trials, the carotid
node exhibited resilience and responded favorably to the
counter-balance methods, closely followed by the radial
node. Symmetric counter-balance enhanced carotid sensitivity
by 13.84% and radial node sensitivity by 16.39%. Refer
Figs. 8–10. The system successfully differentiated between
GTCS and PNES with 95.683% accuracy (refer Fig. 11).
Fig. 8 illustrates the system’s overall sensitivity surpassing
each parameter’s speciﬁcity in the ﬁnal assessment.

The graphs Figs. 7–9 collectively infer that symmetric error
balancing demonstrated a substantial improvement in detection
accuracy across all three monitored nodes—ulnar, carotid, and

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:25 UTC from IEEE Xplore.  Restrictions apply. 

5420

IEEE INTERNET OF THINGS JOURNAL, VOL. 12, NO. 5, 1 MARCH 2025

TABLE V
COMPARISON OF SEIZURE DETECTION RESEARCH WORKS

TABLE VI
VIBRATION PATTERNS OBSERVED ICTAL STATES

TABLE VII
RAW DATA - PERFORMANCE METRICS

Fig. 7. S.E output: sensitivity comparison of seizure nodes.

radial—associated with seizure classiﬁcation through B.P. and
heart rate monitoring. The graph illustrates the comparative
detection performance before and after the application of
symmetric error balancing. Prior to this adjustment, detection
accuracy was likely hampered by noise and irregularities in
the BP and heart rate data. The signiﬁcant gains observed
post-retesting conﬁrm the effectiveness of this approach in
reﬁning signal precision and improving the overall reliability
of seizure detection. Furthermore,
the consistency of the
improvement across all three nodes underscores the robustness
of the method, reinforcing its potential for widespread clinical
application in seizure monitoring.

To further enhance the evaluation of the system’s robustness
and scalability, 1547 additional tests were performed using a
mixed dataset of both nominal and abnormal EEG readings
from the Fp1-Ref and Fp2-Ref electrodes, particularly focus-
ing on values exceeding 100 μV. These tests supplemented
the synthetic dataset of 1754 ictal patients,
incorporating
B.P. and heart rate parameters. By integrating real-world
EEG data, the model’s generalizability across diverse patient
proﬁles and seizure conditions was rigorously assessed. The
results conﬁrmed the system’s accuracy and the reliability
of the S.E-based counter-balance approach. The supplemen-
tary dataset for the experiment carried out can be referred
to at https://archive.org/details/dataset-sampleSupplementary
submission.

Fig. 8. S output: speciﬁcity comparison of seizure nodes.

The current prototype, which operates for approximately 2 h
on battery power while processing and transmitting around
2000 raw data entries, establishes a solid foundation for its
core functionality. Power management will be addressed in
the deployment phase, incorporating duty cycling, local data
processing, and energy-efﬁcient communication protocols.
This phased approach ensures robust core functionality while
optimizing for power consumption, leading to a reliable and
efﬁcient ﬁnal product. The reﬁned design is precise, suitable
for chronic seizures, and socially acceptable while worn
beneath clothing. This allows seizure patients to use the device

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:25 UTC from IEEE Xplore.  Restrictions apply. 

GOPALAKRISHNAN et al.: VPSI 2.0: IoT-BASED HYBRID PROTOCOL WITH SIMULTANEOUS EQUATIONS

5421

Fig. 9. S.E output: false-positive comparison of seizure nodes.

Fig. 10. S.E output: false-negative comparison of seizure nodes.

VI. CONCLUSION

PNES resemble epilepsy symptoms but

lack abnormal
brain electrical activity, while seizures stem from psycho-
logical distress. A safety addendum addresses distinguishing
full-body GTCS seizures from psychiatric origin seizures
for reliable automated detection. The IoT-based architecture,
which enable real-time, scalable, and remote patient moni-
toring with continuous data collection, that monitors nerve
terminals to autonomously identify convulsions, aided by a
peripheral device and wearable Arduino nano processor (to aid
compact, customizable, and low-cost solutions for embedded
monitoring). The method aims to classify both seizure types,
showcasing a prototype with 95.683% failure prevention accu-
racy. Future research will focus on enhancing accuracy through
patient-speciﬁc seizure pattern addendum to enhance rotary
training of S.E counterbalance protocol. Strict conﬁdentiality
and validation using IoT-based medical actuators will further
support and reﬁne the approach’s efﬁcacy.

REFERENCES

[1] J. Jungilligens, R. Michaelis, and S. Popkirov, “Misdiagnosis of
prolonged psychogenic non-epileptic seizures as status epilepticus:
Epidemiology and associated risks,” J. Neurol., Neurosurg. Psy., vol. 92,
no. 12, pp. 1341–1345, 2021.

[2] G. Karthikeyan and G. Kousalya, “GTCS-vagus nerve stimulator
automation using private IoT-blockchain smartcontract,” Comput. Syst.
Sci. Eng., vol. 44, pp. 1325–1340, Feb. 2023.

[3] J. M. Stern and N. Salamon, “Vagus nerve stimulator,” in Imaging
Epilepsy. Cham, Switzerland: Springer, 2022, pp. 373–375. [Online].
Available: https://link.springer.com/book/10.1007/978-3-030-86672-3
[4] A. Bozorgi et al., “Signiﬁcant postictal hypotension: Expanding the spec-
trum of seizure-induced autonomic dysregulation,” Epilepsia, vol. 54,
no. 9, pp. 127–130, 2013.

[5] E. Grillo, “Postictal MRI abnormalities and seizure-induced brain injury:
Notions to be challenged,” Epilepsy Behav., vol. 44, pp. 195–199,
Mar. 2015.

[6] I.-H. Cioriceanu, D. A. Constantin, L. G. Marceanu, C. V. Anastasiu,
A. N. Serbanica, and L. Rogozea, “Impact of clinical and socio-
demographic factors on Quality of Life in Romanian people with
epilepsy,” Healthcare, vol. 10, no. 10, p. 1909, 2022.

[7] C. C. Ogoke, W. C.

Igwe, and E. N. Umeadi, “Clinical and
socio-demographic factors associated with electroencephalographic
abnormalities in children with epilepsy,” Annal. Clin. Biomed. Res.,
vol. 2, pp. 35–40, Sep. 2021.

[8] P. J. Thompson and D. Upton, “The impact of chronic epilepsy on the

family,” Seizure, vol. 1, no. 1, pp. 43–48, 1992.

[9] I. Faimanet, J. Hodsoll, A. H. Young, and P. Shotbolt, “Increased suicide
attempt risk in people with epilepsy in the presence of concurrent
psychogenic nonepileptic seizures,” J. Neurol., Neurosurg. Psy., vol. 93,
no. 8, pp. 895–901, 2022.

[10] T. S. Saker, M. Katson, S. E. Herskovitz, and M. Herskovitz,
“Knowledge and emotional attitudes of health care practitioners regard-
ing patients with psychogenic nonepileptic seizures,” Arquivos de
Neuro-Psiquiatria, vol. 80, no. 11, pp. 1097–1103, 2022.

[11] J. Doss, “Psychogenic non-epileptic seizures in youth: Individual and
family psychiatric characteristics,” Front. Psy., vol. 13, Dec. 2022,
Art. no. 1068439.

[12] “The

role of

and signiﬁcance.”
2023. [Online]. Available: https://onomondo.com/blog/the-role-of-iot-in-
healthcare-dynamics-and-signiﬁcance/

IoT in healthcare: Dynamics

Fig. 11. F1-score before and after VPSI 2.0.

24 × 7 and maintain independence. Lifestyle choices and
preictal symptoms can inform seizure early warning systems
for prediction of countermeasures.

[13] T. Sawchuk, J. Buchhalter, and B. Senft, “Psychogenic non-epileptic
seizures in children–psychophysiology & dissociative characteristics,”
Psy. Res., vol. 294, Dec. 2020, Art. no. 113544.

[14] K. Newmaster et al., “A review of the multi-systemic complications of a
ketogenic diet in infants with epilepsy,” Children, vol. 9, no. 9, p. 1372,
2022.

[15] M. S. Nafea and Z. H. Ismail, “Supervised machine learning and
Deep Learning techniques for epileptic seizure recognition using EEG
signals—A systematic literature review,” Bioengineering, vol. 9, no. 12,
p. 781, 2022.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:25 UTC from IEEE Xplore.  Restrictions apply. 

5422

IEEE INTERNET OF THINGS JOURNAL, VOL. 12, NO. 5, 1 MARCH 2025

[16] D. Zambrana-Vinaroz, J. M. Vicente-Samper, and J. M. Sabater-Navarro,
“Validation of continuous monitoring system for epileptic users in
outpatient settings,” Sensors, vol. 22, no. 8, p. 2900, 2022.

[17] Y.-T. Ng, “Maximizing quality of life in children with epilepsy,”

Children, vol. 10, no. 1, p. 65, 2022.

[18] R. Caplan, “Cognition and quality of life in children with new-onset

epilepsy,” Epilepsy Currents, vol. 13, no. 2, pp. 85–87, 2013.

[19] K. Song, J. Fang, L. Zhang, F. Chen, J. Wan, and N. Xiong, “An
intelligent epileptic prediction system based on synchrosqueezed wavelet
transform and multi-level feature CNN for smart healthcare IoT,”
Sensors, vol. 22, no. 17, p. 6458, 2022.

[20] A. A. Malibari, “An efﬁcient IOT-artiﬁcial intelligence-based disease
prediction using lightweight CNN in healthcare system,” Meas., Sensors,
vol. 26, Apr. 2023, Art. no. 100695.

[21] D. P. Yedurkaret, S. P. Metkar, F. Al-Turjman, T. Stephan, M. Kolhar,
and C. Altrjman, “A novel approach for multichannel epileptic seizure
classiﬁcation based on Internet of Things framework using critical spec-
tral verge feature derived from ﬂower pollination algorithm,” Sensors,
vol. 22, no. 23, p. 9302, 2022.

[22] D. Zambrana-Vinaroz, J. M. Vicente-Samper, J. Manrique-Cordoba,
J. M. Sabater-Navarro, “Wearable epileptic seizure prediction system
based on machine learning techniques ECG, PPG and EEG Signals,”
Sensors, vol. 22, no. 23, p. 9372, 2022.

[23] K. K. Dutta, P. Manohar, K. Indira, F. Naaz, M. Lakshminarayan, and
S. Rajagopalan, “Seven epileptic seizure type classiﬁcation in pre-ictal,
ictal and inter-ictal stages using machine learning techniques,” Adv.
Mach. Learn. Artif. Intell., vol. 4, no. 1, pp. 1–10, 2023.

[24] M. H. Andarevi and A. A. Iskandar, “A prototype of IOT-based real-time
respiratory rate monitoring using an accelerometer sensor,” in Proc. 4th
Int. Conf. Biomed., Eng. (IBIOMED), 2022, pp. 42–46.

[25] P. Verma, A. Gupta, M. Kumar, and S. S. Gill, “FCMCPS-COVID: AI
propelled fog–cloud inspired scalable medical cyber-physical system,
speciﬁc to coronavirus disease,” Internet Things, vol. 23, Oct. 2023,
Art. no. 100828.

[26] P. Bellini, L. A.

Ipsaro Palesi, A. Giovannoni, and P. Nesi,
“Managing complexity of data models and performance in broker-
based Internet/Web of Things architectures,” Internet Things. vol. 23,
Oct. 2023, Art. no. 100834.

[27] J. Li and Y. Sawanoi, “The history and innovation of home blood pres-
sure monitors,” in Proc. IEEE Hist. Electrotechnol. Conf. (HISTELCON),
2017, pp. 82–86.

[28] M. Genoveseet al., “Safety and efﬁcacy of neurostimulation with a
miniaturised vagus nerve stimulation device in patients with multidrug-
refractory rheumatoid arthritis: A two-stage multicentre, randomised
pilot study,” Lancet Rheumatol., vol. 2, pp. e527–e538, Sep. 2020.
[29] H. Luan and Y. Zhang, “Programmable stimulation and actuation
in stretchable electronics,” Adv. Intell. Syst., vol. 3, no. 6, 2021,
Art. no. 2000228.

[30] K. Gopalakrishnan, A. Balakrishnan, K. Govardhanan, and S. Selvarasu,
“Propositional inference for IOT based dosage calibration system using
private patient-speciﬁc prescription against fatal dosages,” Sensors,
vol. 23, no. 1, p. 336, 2022.

[31] M. Qi, Z. Wang, Q. Han, J. Zhang, S. Chen, and Y. Xiang, “Privacy
protection for blockchain-based healthcare IoT systems: A survey,”
IEEE/CAA J. Automatica Sinica, vol. 11, no. 8, pp. 1757–1776, 2024.

Karthikeyan Gopalakrishnan received the M.E.
and Ph.D. degrees from Anna University, Chennai,
India, in 2012 and 2023, respectively.

He is an Assistant Professor with the Department
of Computer Science, Coimbatore Institute of
Technology (Anna University), Coimbatore, India.
Specialization: Application of IoT in seizures.

Arunkumar Balakrishnan received the M.E. and
Ph.D. degrees from Anna University, Chennai, India,
in 2011 and 2022, respectively.

He is an Assistant Professor with the Department
of Computer Science and Engineering, VIT-AP
Specialization:
University, Amaravathi,
Cryptography, medical
and
security,
blockchain.

India.
image

Kousalya Govardhanan received the M.E. and
Ph.D. degrees from Anna University, Chennai, India,
in 2001 and 2008, respectively.

Specialization: Cloud computing, AI, and IoT.

Kandala N. V. P. S. Rajesh received the
M.Tech. and Ph.D. degrees from Vellore Institute of
Technology, Vellore, India, 2013 and 2018, respec-
tively.

He is an Associate Professor with the School
of Electronics Engineering, VIT-AP University,
Amaravati, India. Specialization: Biomedical signal
processing, image processing, and machine and deep
learning.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:25 UTC from IEEE Xplore.  Restrictions apply.
