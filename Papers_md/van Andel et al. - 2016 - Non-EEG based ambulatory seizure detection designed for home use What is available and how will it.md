# van Andel et al. - 2016 - Non-EEG based ambulatory seizure detection designed for home use What is available and how will it

Epilepsy & Behavior 57 (2016) 82–89

Contents lists available at ScienceDirect

Epilepsy & Behavior

j o u r n a l h o m e p a g e : w w w . e l s e v i e r . c o m / l o c a t e / y e b e h

Review

Non-EEG based ambulatory seizure detection designed for home use:
What is available and how will it inﬂuence epilepsy care?
Judith van Andel a,⁎, Roland D. Thijs b,c, Al de Weerd d, Johan Arends e, Frans Leijten a
a University Medical Centre Utrecht, Department of Clinical Neurophysiology, Utrecht, The Netherlands
b Stichting Epilepsie Instellingen Nederland SEIN, Department of Clinical Neurophysiology, Heemstede, The Netherlands
c Leiden University Medical Centre, Department of Neurology, Leiden, The Netherlands
d Stichting Epilepsie Instellingen Nederland SEIN, Department of Clinical Neurophysiology, Zwolle, The Netherlands
e Academic Centre for Epileptology Kempenhaeghe, Department of Clinical Neurophysiology, Heeze, The Netherlands

a r t i c l e

i n f o

a b s t r a c t

Article history:
Received 15 June 2015
Revised 31 December 2015
Accepted 2 January 2016
Available online 27 February 2016

Keywords:
Seizure detection

Objective: This study aimed to (1) evaluate available systems and algorithms for ambulatory automatic seizure
detection and (2) discuss beneﬁts and disadvantages of seizure detection in epilepsy care.
Methods: PubMed and EMBASE were searched up to November 2014, using variations and synonyms of search
terms “seizure prediction” OR “seizure detection” OR “seizures” AND “alarm”.
Results: Seventeen studies evaluated performance of devices and algorithms to detect seizures in a clinical setting.
Algorithms detecting generalized tonic–clonic seizures (GTCSs) had varying sensitivities (11% to 100%) and false
alarm rates (0.2–4/24 h). For other seizure types, detection rates were low, or devices produced many
false alarms. Five studies externally validated the performance of four different devices for the detection of
GTCSs. Two devices were promising in both children and adults: a mattress-based nocturnal seizure detector
(sensitivity: 84.6% and 100%; false alarm rate: not reported) and a wrist-based detector (sensitivity: 89.7%;
false alarm rate: 0.2/24 h).
Signiﬁcance: Detection of seizure types other than GTCSs is currently unreliable. Two detection devices for GTCSs
provided promising results when externally validated in a clinical setting. However, these devices need to be
evaluated in the home setting in order to establish their true value. Automatic seizure detection may help prevent
sudden unexpected death in epilepsy or status epilepticus, provided the alarm is followed by an effective inter-
vention. Accurate seizure detection may improve the quality of life (QoL) of subjects and caregivers by decreasing
burden of seizure monitoring and may facilitate diagnostic monitoring in the home setting. Possible risks are oc-
currence of alarm fatigue and invasion of privacy. Moreover, an unexpectedly high seizure frequency might be
detected for which there are no treatment options. We propose that future studies monitor beneﬁts and disad-
vantages of seizure detection systems with particular emphasis on QoL, comfort, and privacy of subjects and im-
pact of false alarms.

© 2016 Published by Elsevier Inc.

1. Introduction

Despite the rapid expansion of pharmaceutical and surgical treat-
ment options, a signiﬁcant proportion of people with epilepsy continue
to have seizures. They are faced with the prospect of having to cope with
seizures for a long time, if not lifelong. Forty years ago, the prevalence of
refractory epilepsy was estimated at approximately 30% [1], and this
percentage has not changed substantially since then [2]. The mortality
rate, which is 2–4 times higher in people with epilepsy than in their
peers without epilepsy, has also not changed over the last decades
[3–5]. Epilepsy adversely affects quality of life (QoL), with unsuccessful

⁎ Corresponding author. Tel.: +31 88 755 6782.

E-mail address: judithvanandel@gmail.com (J. van Andel).

http://dx.doi.org/10.1016/j.yebeh.2016.01.003
1525-5050/© 2016 Published by Elsevier Inc.

achievement of seizure freedom, passive coping styles, and low socio-
economic status being major determinants of an impaired QoL [6]. In
our experience, many people struggle with the random nature of sei-
zures. Moreover, seizures are dangerous, potentially leading to falls, vi-
olent movements, confusional wandering, sudden unexpected death in
epilepsy (SUDEP), or status epilepticus.

There is an urgent need for alternative strategies to reduce the bur-
den of epilepsy. Devices to detect seizures have been promoted as a way
to reduce seizure-related risk, but the scientiﬁc validity of this notion is
questionable, and the implications for epilepsy care have not been in-
vestigated. Here, we describe various in-home seizure detection devices
and present the results of a literature search of current systems for au-
tomatic detection. We then discuss the risks and beneﬁts of continuous
automated seizure monitoring and describe the ideal setup of future de-
vices for seizure detection.

J. van Andel et al. / Epilepsy & Behavior 57 (2016) 82–89

83

2. Devices for automatic seizure detection

2.1. EEG

Many research groups have worked on the development of EEG al-
gorithms to automatically predict seizures or detect seizure onset in
people with epilepsy. Seizure prediction aims to rapidly detect early sei-
zure activity, with a view to instigating timely interventions to prevent
further seizure activity. Automatic seizure prediction has proven difﬁ-
cult [7]. A recent long-term ambulatory study of intracranial EEG re-
cordings [8] yielded promising results regarding prediction accuracy
in speciﬁc subjects, but there is still a long way to go before this method
can be used clinically, mainly because interventional techniques, such as
closed-loop stimulation and fast-working locally administered medica-
tion, are still under investigation. The method is invasive and costly, re-
quiring implantation of an intracranial device, accurate localization of
the seizure-onset zone, and deﬁnition of the EEG dynamics of seizure
onset. For these reasons, it will be reserved for a small number of people
with refractory epilepsy.

Automatic seizure detection with scalp EEG focuses on a more efﬁ-
cient analysis of long-term, diagnostic EEG data, as collected in
presurgical screening of people with epilepsy. Many studies have been
performed to develop reliable algorithms. The main issue in develop-
ment is reducing the number of false positives. In early algorithms, the
false positive rates were up to 5 false detections per hour [9]. False pos-
itives are mainly caused by artifacts in the EEG signal often because of
muscle activity. More recently developed algorithms include methods
of artifact rejection, greatly improving false alarm rates. Several algo-
rithms reach sensitivities N80% and false alarm rates b 0.5 false alarms/
h [10–12]. Artifact rejection could lead to decreased sensitivity in detec-
tion of seizures where high amounts movement are present from sei-
zure onset. However, evaluation in long-term data of a recent
algorithm presented promising results [10]. Development of new algo-
rithms beneﬁts from modern techniques of classiﬁcation, such as ran-
dom forest classiﬁers or techniques from genome analysis [13,14]. No
system based on automatic EEG analysis is currently used in clinical
practice. In theory, these algorithms could also be used online in an
ambulatory setting. In this context, it is important to consider that
real-time classiﬁcation of seizures with a portable system requires an al-
gorithm with relatively low computational complexity [15]. Also, long-
term scalp EEG is uncomfortable, sensitive to artifacts, and cosmetically
difﬁcult to hide from the outside world, making its application imprac-
tical in daily life. New developments include 4-electrode subcutaneous
EEG recording, which is currently being evaluated for the detection of
hypoglycemia in diabetes [16]. This review will focus on non-EEG-
based systems.

2.2. Non-EEG sensors

As EEG recording is currently too cumbersome for in-home seizure
monitoring, systems based on extracerebral signals have been devel-
oped, based on seizure-induced movements and autonomic changes
[17]. Movement and position can be recorded with accelerometers, gy-
roscopes (measuring rotational acceleration), or magnetometers (mea-
suring position) attached to the body. Movements caused by nocturnal
or sleep-related seizures can also be detected with a mattress-based
sensor, which is less bothersome than on-body sensors. Other contact-
free technologies are radar and video. With radar signals, the position
of the body can be monitored continuously and, therefore, also changes
in position due to movement. A video camera can also be used in com-
bination with automatic movement analysis, for instance, using optical
ﬂow analysis [18]. Video or radar technologies are contact-free and,
therefore, less burdensome, but can only be used in the room in which
the equipment is set up. Electromyography is used to measure muscle
contractions, which is especially useful in assessing the tonic phase of
seizures. Electromyography requires electrodes attached to the skin,

which can be sensitive to artifacts or uncomfortable to wear. Electrocar-
diography (ECG) or plethysmography can be used to measure changes
in heart rate and heart rate variability. Two-lead ECG can also be used
to detect ECG abnormalities. Electrocardiography also requires elec-
trodes which can be sensitive to artifacts. Another option to assess auto-
nomic changes is through measurement of electrodermal activity.
Electrodermal activity (EDA) can be measured by assessing conduc-
tance between two electrodes on the skin. It changes as a result of
sweating, which is regulated by the sympathetic nervous system.
Changes in respiration can also be interesting parameters for seizure de-
tection, especially when the goal is detection of clinically urgent sei-
zures. A pulse oximeter can be used to measure respiration-related
changes in blood oxygenation. Respiration is usually measured with
body sensors assessing the movement of the chest wall or with a
mask or sensor placed over or under the nose to measure airﬂow.
Video and radar can also be used for this purpose, and it even seems
possible to measure heart rate with these techniques [19]. These
methods have their advantages and disadvantages for seizure detec-
tion; for example, changes in sensitivity, false-positive seizure detection
due to autonomic changes as a result of arousal or nightmares, the pos-
sibility to monitor vital signs, susceptibility to technical failure, difﬁculty
of instruction, energy consumption, and burden and side effects to
users. When considering non-EEG sensors for long-term monitoring, it
is important to keep these sensors wearable. Currently, there is a
surge in wearable sensors in watches, bands, or clothing in a commer-
cial setting. These sensors combine several modalities in one compact
sensor which can easily be worn around a wrist or an upper arm. This
provides researchers with opportunities for commercial collaboration
or to develop integrated sensor systems with existing technology.

2.3. Clinical evaluation of available systems

A number of products are marketed for automatic, non-EEG, in-
home seizure detection. Some systems focus on nocturnal seizure de-
tection and other systems on continuous use. Though they are becom-
ing more popular, in practice, these products are still infrequently
used because of detection failures, frequent false alarms, and limited sci-
entiﬁc proof of efﬁcacy [19].

Unique publications 
identified in Pubmed and 
EMBASE:
723

Publications after 
screening for in/exclusion 
criteria:
15

Publications included in 
review:
17

Inclusion criteria

-  Automatic, ambulatory 
real-time seizure 
detection
-  Human studies
Exclusion criteria:

-  Detection of neonatal 

seizures

-  Less than 5 subjects
-  Description of an 

algorithm validated in 
another study

Screening of references of 
related articles: 2 
publications not included in 
search strategy

Fig. 1. Flow chart of search strategy.

Table 1
Summary of results of studies reporting performance of automatic, non-EEG, seizure detection algorithms and devices.

Modality

Setup

N
patients
(with
seizures)

N
seizures

Seizure type
(N seizures)

Hours of
recording

Outcomea

Intention to
diagnoseb

External
validation

Remark

Nijsen et al. [20]

Nijsen et al. [21]

Kramer et al. [22]

ACM

ACM

ACM

Sensor on one arm

36 (18)

Sensors on arms

36 (36)

1 sensor in bracelet
on limb

31 (15)

Lockman et al. [24]

ACM

Sensor wrist/ankle

40 (6)

Beniczky et al. [25]

ACM

Sensor on wrist

73 (20)

Van de Vel et al. [23]

ACM

Sensor on extremities

7 (7)

27

64

22

8

39

51

T

M

NR

NR

Sens: 80%PPV: 35%

Sens: 80%PPV: 16%

No

Yes

C, GTC (16)

1692

Sens: 91%Latency: 17sFA: 0.1/24h

No

GTC

GTC

HM

NR

Sens: 88%

Yes

4878

Sens: 89.7%FA: 0.2/24hLatency: 55s

Yes

NR

Sens: 95.7%PPV: 57.84%

Yes

Luca et al. [32]

ACM

Sensor on extremities

7 (7)

51

HM

NR

Average sens: 85%Average PPV: 46%

Yes

Poh et al. [26]

ACM, EDA Wristworn sensor

80 (7)

Narechania et al. [34]

Mvt

Pressure sensor in
mattress

51 (13)

16

18

GTC

GTC

4213

Sens: 94%Latency: 31.4sFA: 0.74/24h Yes

3741

Sens: 89%PPV: 43%Latency: 9s in
clonic phase

No

No

No

No

No

Yes

Yes

–

No

Yes

Van Poppel et al. [28]

Mvt

Pressure sensor in
mattress

45 (26)

78

GTC (13)GM, T, CP NR

Overall sens: 29.5%;Sens GTC:
84.6%FA: NR

Yes

Yes

Fulton et al. ST2® [30] Mvt

Sensor under mattress 27 (15)

69

GTC (3), GM, T, CP NR

Overall sens: 2.2%Sens GTC: 0/3

Yes

Yes

Carlson et al. [27]

Mvt, sound Sensor + microphone

64 (6)

8

GTC

1528

Sens: 62.5% (5/8)FA: 4/24h

Fulton et al. MP5® [30] Mvt, sound Sensor + microphone

27 (15)

69

GTC (9), GM, T, CP NR

under mattress

Conradsen et al. [31]

EMG

Van Elmpt et al. [33]

Heart rate

under mattress

Electrode on left
deltoid muscle
ECG

60 (11)

22

GTC

17 (16)

104

T, GM, GTC

Osorio [29]

Heart rate

ECG

81 (81)

241

NR

Kalitzin et al., 2012 [18] Video

Infrared camera in
room

50 (50)

72

C, GTC

776

NR

303

NR

Overall sens: 4.3%Sens GTC:
11.1% (1/9)

Sens: 100%Latency: 13.7FA: 1/24h

No

Best performance (1 pt):
sens N 90%, PPV N 50%

1: Sens: 98%, FA: 9.5/h2:
Sens: 86%, FA: 1.1/h
Sens: 95%FA: b1/24h

Yes

Yes

No

Yes

No

No

Yes

Yes

No

No

No

No

No

de Bruijne et al. [35]

Sound

Microphone

17 (17)

95

NR

NR

Sens: 95–98%PPV: 2–40%

42% of false alarms were myoclonic or clonic
seizures.
Algorithm trained on 29 seizures and tested on 35
seizures.
Pts with dystonic posturing or behavioral
automatisms were excluded; available as Epilert®
(BioLert, Ltd., Even Yehuda, Israel).
204 FA canceled by pts, 1 nocturnal FA; available as
SmartWatch® (SmartMonitor, San Jose, USA).
Available as Epi-Care Free® (Danish Care
Technology, Sorø, Denmark).
System targeted to children. Only nocturnal data
included. No patient-speciﬁc information necessary
for detection algorithm.
Only nocturnal data included. Unsupervised
method based on extreme value statistics. No
labeled trianing data necessary.
Algorithm based on patient-speciﬁc information,
scored baseline signal necessary.
Commercially available, Emﬁt® (Emﬁt Ltd,
Vaajakoski, Finland). Only adult pts. 8 nocturnal
GTCSs recorded (sens: 100%, no nocturnal FA).
Commercially available, Emﬁt® (Emﬁt Ltd,
Vaajakoski, Finland). Only pediatric pts. nocturnal
detection.
ST2® (MedPage, no longer commercially available)
was used in unspeciﬁed subset of patients.
Nocturnal detection.
No individual calibration applied. Available as
MP5® (MedPage, Corby, UK). Nocturnal detection.
MP5® was used in unspeciﬁed subset of patients. 4
patients found device too uncomfortable for
long-term use. Nocturnal detection.
In future available as IctalCare® (IctalCare,
Hørsholm, Denmark).
Heart rate changes found in 50/104 seizures.
Eventual detection algorithm tested on 3 patients,
varying results.
Results of the most (1) and least (2) sensitive
settings are reported.
FA rate based on 37 h of recording without seizures.
Sensitivity based on detection of seizure fragments.
Nocturnal detection.
Classiﬁcation of seizure-related sounds and
simulated nonseizure sounds. Varying performance
based on sound type.

Mvt = movement; Snd = sound; ACM = accelerometry; EMG = electromyography; ECG = electrocardiography; EDA = electrodermal activity; GTC = generalized tonic–clonic; TC = tonic–clonic; C = clonic; GM = generalized myoclonic; T =
tonic; CP = complex partial; HM = hypermotor; sens = sensitivity; spec = speciﬁcity; FA = false alarm rate; PPV = positive predictive value; h = hour; s = second; NR = not reported.

a Reported outcome measures are over all seizure types, unless speciﬁed otherwise.
b Intention to diagnose: “Yes” if performance of the system was based on all patients included in the study, not on a selection of patients.

8
4

J
.

v
a
n
A
n
d
e
l

e
t
a
l
.

/
E
p
i
l
e
p
s
y
&
B
e
h
a
v
i
o
r
5
7
(
2
0
1
6
)
8
2
–
8
9

J. van Andel et al. / Epilepsy & Behavior 57 (2016) 82–89

85

Recent encouraging developments include new algorithms and
existing devices. We performed a systematic literature search to critical-
ly review the performance of non-EEG, automatic systems for in-home
seizure detection.

2.3.1. Methods — search strategy and selection of articles

PubMed and EMBASE databases were searched for human studies
published in English up to November 2014, using variations and syno-
nyms of search terms “seizure prediction” OR “seizure detection” OR “sei-
zures” AND “alarm”. Articles were screened for relevance to automatic,
ambulatory, real-time seizure detection, based on title and abstract. If
an algorithm was described in one paper and validated in another,
only the validation study was included. Articles on the detection of neo-
natal seizures were excluded as this is a very speciﬁc area of expertise.
Studies reporting results for fewer than 5 subjects were also excluded
(Fig. 1). References and related articles of relevant studies were
screened to check for articles not included in the search strategy.

2.3.2. Results

This search strategy yielded 723 articles of which 15 studies fulﬁlled
the inclusion and exclusion criteria. Screening of related articles and ref-
erences led to 2 additional relevant studies, making a total of 17 includ-
ed studies (Fig. 1). A summary of the studies is presented in Table 1.

2.3.3. Sensor types

None of the studies evaluated EEG-based automatic seizure detec-
tion devices intended for in-home use. All studies used extracerebral
signals including acceloremetry (n = 7), mattress-based sensor
(n = 4), heart rate (n = 2), sound (n = 1) or video (n = 1), a combina-
tion of accelerometry and EDA (n = 1), and EMG (n = 1) (Table 1)
[12–17,19–25,32,33].

2.3.4. Study quality

All studies were performed in a hospital setting. Seven studies re-
ported the recording time, which varied between several hours to
3 days per patient. No long-term data were reported.

2.3.5. Detection of generalized tonic–clonic seizures

Most studies (10 out of 17) focused on the detection of GTCSs. Five of
these studies reported performance measures based on algorithms de-
veloped within the same study population; the other ﬁve studies re-
ported on algorithm validation in a different population. In the former
studies, sensitivity ranged from 88% to 100%, with false alarm rates be-
tween 0.1 and 1/24 h [18,22,24,26,31]. Performance was probably
overestimated because of ‘overﬁtting’ of the algorithm for one speciﬁc
dataset. One study focused on the detection of nocturnal seizures
using automated video analysis of 72 seizures in 51 patients (sensitivity:
95%, false alarm rate: b1/24 h) [29]. Results of the other studies were
based on small numbers of seizures (8–22) and included both daytime
and nighttime data.

2.3.6. Detection of hypermotor seizures

Two studies evaluated the nocturnal detection of hypermotor sei-
zures, both in the same subset of 7 subjects (who had 51 hypermotor
seizures), using different methods. The ﬁrst method evaluated the per-
formance of an unsupervised detection algorithm, which does not re-
quire external validation. The second method was external validation
of a previously developed detection algorithm. Sensitivities of 85% and
95.7% and positive predictive values of 58% and 46% were found [23,
25,32]. The positive predictive value (PVV) represents the proportion
of correct detections, and a PPV of 60% means that 60% of the alarms
generated by the device are true detections and 40% are false alarms.

2.3.7. Detection of other seizure types

Five studies also reported on the detection of other types of seizure,
such as myoclonic, tonic, and complex partial seizures. Tonic and

myoclonic seizures were investigated in two studies by the same re-
search group. For both seizure types, sensitivity was 80%, with a very
low positive predictive value (35% and 16%) [20,21]. The algorithms
were not validated in an external population. Two other studies report-
ed on the external validation of three mattress-based pressure sensors
for the detection of GTCSs, myoclonic, tonic, and complex partial sei-
zures. The overall performance of the sensors was poor, with an overall
sensitivity of 2.2%, 4.3%, and 29.5% for the three sensors. Sensitivity per
seizure type was only reported for GTCSs (sensitivities: 0%, 11.1%, and
84.6%) [28,30]. One study investigated the performance of heart rate-
derived algorithms for the detection of tonic, myoclonic, and GTC sei-
zures in three patients, with very discrepant results (sensitivity: up to
90%, PPV: generally below 50%).

2.3.8. Available devices

In ﬁve studies, the performance of existing devices was prospective-
ly evaluated in an epilepsy monitoring unit. All studies focused on the
detection of GTCSs. The ST2® (MedPage, Corby, UK), a mattress sensor
for detecting nocturnal GTCSs, provided poor results [30]. This device
is currently no longer available. The MP5® (MedPage, Corby, UK) mat-
tress detector was evaluated in two studies [27,30] and had a detection
rate for nocturnal GTCSs of 62.5% (5/8 seizures) with a false alarm rate of
4/24 h in one study and a detection rate of 11% (1/9 seizures, false alarm
rate not reported) in the other. Why these results are so different is un-
clear. The Emﬁt® (Emﬁt Ltd., Vaajakoski, Finland) was evaluated in 51
adults [34] and in 45 children [28]. In adults, 18 seizures were recorded:
the sensitivity of detection was 89% with a PPV of 43%. Eight nocturnal
GTCSs were recorded (sensitivity: 100% and no false alarms). In chil-
dren, 13 nocturnal GTCSs were recorded with a sensitivity of 84.6%;
the number of false alarms was not reported. The Epi-care Free® (Dan-
ish Care Technology, Sorø, Denmark) uses accelerometry data to detect
GTCSs. This device was evaluated in 73 patients in an epilepsy monitor-
ing unit; 35 out of 39 GTCSs were detected (sensitivity: 89.7%) with a
false alarm rate of 0.2/24 h [25].

2.3.9. Conclusion on clinical evaluation of available systems

The sensitivity (11% to 100%) and false alarm rates (0.2–4/24 h) of
various devices for detecting GTCSs vary considerably, and for other sei-
zure types, either detection rates are low or devices produce many false
alarms. Of the four devices for the detection of GTCSs externally validated
in prospective studies in a clinical setting, two had a sensitivity higher
than 80% and acceptable false alarm rates: a mattress-based device for
the detection of nocturnal GTCSs (sensitivity: 84.6% in children, false
alarm rate not reported and sensitivity: 100% in adults, no false alarms)
and a wrist-based detector of GTCSs, which can be used 24 h a day
(sensitivity: 89.7%; false alarm rate: 0.2/24 h). Both devices were tested
in children and adults. However, it should be mentioned that there
were relatively few seizures in the validation population during the 3-
day validation period. These devices need to be evaluated in a home-
care setting for a longer time in order to assess the true value of these
systems.

3. Beneﬁts of seizure detection — safety

In this section, we discuss the potential beneﬁts of automatic seizure
detection in terms of safety issues, including SUDEP, status epilepticus,
and physical injury due to seizures.

3.1. SUDEP

Sudden unexpected death in epilepsy is deﬁned as “Sudden, unex-
pected, witnessed or unwitnessed, nontraumatic and nondrowning death,
occurring in benign circumstances, in an individual with epilepsy, with or
without evidence for a seizure and excluding documented status epilepticus
(seizure duration ≥ 30 min or seizures without recovery in between), in
which postmortem examination does not reveal a cause of death” [36].

86

J. van Andel et al. / Epilepsy & Behavior 57 (2016) 82–89

Though SUDEP is relatively rare, with an incidence of 1.16/1000 person-
years (meta-analysis by Thurman et al. [37]), the lifetime risk of SUDEP
in people with epilepsy is between 8% and 12% [37], making it a very rel-
evant issue in epilepsy care. The incidence of SUDEP is higher in speciﬁc
groups, such as people with refractory epilepsy (3.8–9.3/1000 person-
years, median: 6.2/1000 person-years) [38] and people with learning
disabilities (3.4–3.6/1000) [39].

3.1.1. Can detection of seizures help prevent SUDEP?

A meta-analysis of four case–control studies showed that a history of
GTCSs is the main risk factor for SUDEP (OR: 5, 95% CI: 3–8.6, in subjects
with 1–2 GTCSs/year and OR: 15.6, 95% CI: 10.1–24.2, in subjects with
N2 GTCSs/year) [40]. Other risk factors include male sex, symptomatic
epilepsy, and duration of epilepsy. Sudden unexpected death in epilepsy
is often a sleep-related (58%) and unwitnessed (86%) event [41]. In one
case–control study, nocturnal seizure was reported as independent risk
factor (OR: 2.6, 95%: CI 1.3–5.0) and nocturnal supervision a protective
factor (OR: 0.4, 95% CI: 0.2 to 0.8) for SUDEP [41,42]. Unfortunately,
these factors have not been evaluated in other studies. In a cohort of
children with learning disability attending a school with very close su-
pervision, all 14 SUDEP cases occurred during holidays when the chil-
dren were under less intensive supervision. As most cases are
unwitnessed, supervision would seem to have a protective effect [37].
It is not known why SUDEP is more often unwitnessed than
witnessed, but
timely stimulation
(e.g., through shaking) of a subject with cardiorespiratory depression
following a seizure might help arouse the subject and restore cardiore-
spiratory function [43,44]. The scientiﬁc and clinical epilepsy communi-
ty recommends nocturnal supervision in high-risk subjects, although it
is debated how this should be done [43,44]. Continuous supervision for
a low-frequency event during the night is not realistic in most care set-
tings, either at home or in institutions. Better monitoring of especially
nocturnal seizures with automatic seizure detectors would give care-
givers the opportunity to intervene, and this might be a way to prevent
SUDEP. As long as SUDEP pathophysiology remains elusive, it is unlikely
that speciﬁc SUDEP prevention devices will be developed soon. Howev-
er, as SUDEP is closely related to GTCSs, a sensitive ambulatory device
detecting GTCSs is a realistic ﬁrst step towards SUDEP prevention. It
will be a challenge to obtain scientiﬁc proof for this ﬁrst step as this
will require large, long-term follow-up studies.

it has been proposed that

3.2. Other aspects of safety

Status epilepticus (SE) and injuries related to seizures are a major
risk to patients. The annual incidence of SE is about 10–20/100,000
[45] of which about a third occur in people with a history of epilepsy
[46,47]. The earlier an intervention can take place to stop tonic–clonic
SE, the better the prognosis is in terms of mortality, cognition, and func-
tional outcome [48]. More accurate and earlier detection of seizures will
give caregivers the opportunity to administer emergency medication
and, thus, reduce treatment delay.

The absolute risk of seizure-related injuries ranges from 12% to 35%
in various populations (general population, institutionalized, children,
and subjects with and without learning disability) [49]. Most injuries
are due to falls, burns, trafﬁc accidents, and swimming-related inci-
dents. Nocturnal seizures may cause the subject to fall out of bed, aspi-
rate, or wander (postictal confusional wandering). The incidence of
these complications is not clear from the literature. Apart from postictal
wandering, it is unlikely that automatic seizure detection will help pre-
vent injuries as these events mostly occur at seizure onset.

4. Beneﬁts of seizure detection — caregiver perspective

In the following sections, we discuss the beneﬁts of seizure detection
regarding other stakeholders in epilepsy care, i.e., caregivers at home
and professional caregivers, clinicians, and researchers.

4.1. Caregivers at home

The caregivers of people with epilepsy feel that they should be there
when a potentially harmful seizure occurs. This psychological burden
affects the health-related QoL of caregivers [50], but the extent to
which their health-related QoL is affected depends on their personal
coping style. A passive response style towards negative events is associ-
ated with a worse health-related QoL [51]. The parents of children with
epilepsy often sleep in the same bedroom or next to their child in the
hope of detecting or preventing nocturnal seizures. These parents are
more fatigued and experience more disturbed sleep than the parents
of healthy children [52]. Moreover, these sleeping arrangements can
have detrimental effects on the love life of the parents and negatively in-
ﬂuence the child's development.

Installation of a video observation system was found to improve
parent-reported quality of family life [53]. However, this requires con-
tinuous surveillance of the video images, which is still a burden. Reliable
nocturnal seizure monitoring with a seizure detector may help care-
givers cope better with the uncertainty of epilepsy and improve their
QoL.

4.2. Professional care setting

A signiﬁcant number of people with refractory epilepsy also have
intellectual disability that necessitates their receiving specialized care.
In our experience, although these institutions aim to provide the same
level of care and safety as at home, they are dependent on the availabil-
ity of nursing staff for nocturnal supervision. Sudden unexpected death
in epilepsy in an institutional setting may cause a lot of commotion and
media attention. This is understandable, but expectations of the care
provided cannot always be met. Currently, no guidelines indicate how
these high-risk institutionalized individuals should be monitored.
Camera supervision alone is not likely to solve the problem, because
continuous visual inspection of multiple individuals requires numerous
personnel and is tedious, so that there is a high chance of an event being
missed. Optimal automatic seizure detection would enable better and
more efﬁcient monitoring of high-risk individuals, both with regard to
manpower and costs. Care professionals can devote their time to care-
giving instead of monitoring videoscreens.

5. Beneﬁts of seizure detection — clinical perspective

In-home seizure monitoring may provide clinicians with valuable
information. Self-reported seizure frequencies are notoriously unreli-
able, especially in the case of nocturnal seizures, as has been shown by
nocturnal video-EEG and intracranial recordings [14,54]. Long-term
monitoring in a video-EEG monitoring unit is costly, and the change of
environment often inﬂuences seizure frequency. More possibilities for
in-home monitoring and telecare could reduce the number of hospital
visits [55].

It is disputable whether accurate knowledge of seizure frequency
will lead to more effective treatment strategies — people with refractory
epilepsy have often unsuccessfully tried a number of treatment options.
However, in early stages of the disease, more accurate information may
improve diagnosis and treatment, which could inﬂuence the disease
course. This is especially the case with epileptic encephalopathy [56].

6. Beneﬁts of seizure detection — research perspective

In-home seizure detection could improve the quality of clinical re-
search. In clinical trials, the effects of new drugs or other interventions
should ideally be monitored with an objective measure. There is
relatively little research-based knowledge of seizure frequency, seizure
semiology, and response to treatment of people with refractory epilepsy
and learning disabilities. The majority of especially nocturnal seizures
go unnoticed in people with learning disabilities living in a residential

J. van Andel et al. / Epilepsy & Behavior 57 (2016) 82–89

87

care setting [57]. A reliable seizure detection system may help avoid
undertreatment of these subjects.

7. Disadvantages of seizure detection

There are also disadvantages to seizure detection in epilepsy care.
Primarily, an automatic device is never foolproof and could give care-
givers a false sense of security. Moreover, caregivers need to be able to
cope with the system and use it correctly. They should also appreciate
the limits and uses of a detection system — a seizure detector is not
necessarily a vital sign monitor. Thus, clear information about what a
detector can and cannot do is needed to ensure the proper use and
acceptance of a device.

Another aspect of automatic detection is the risk of “alarm fatigue”.
Seizures occur in varying frequencies and not all seizures require care.
Every device will also occasionally produce false alarms. If only a small
proportion of alarms is relevant to the caregiver, then the caregiver
will stop responding to alarms as these alarms tend to be “nothing” in
most occasions [58]. A device that leads to such alarm fatigue defeats
its purpose.

Also, the availability of devices might stimulate unnecessary moni-
toring by overprotective caregivers. A child might (un)consciously trig-
ger the alarm to attract the attention of the caregiver. Furthermore,
monitoring might reveal a higher seizure frequency than expected or
show that treatment does not make any difference. This knowledge
can be hard for caregivers to cope with if treatment options are limited.
An alarm system gives carers the responsibility to respond to an alarm
and to provide proper ictal and postictal care, and carers will feel guilty
if they ignore a ‘real’ alarm.

Privacy is also an issue with video monitoring systems, especially in
children and people with learning disabilities. This is particularly impor-
tant in the context of sexual behavior (for example, masturbation might
trigger a false alarm).

8. Economic evaluation of seizure detection

Automatic seizure detection should be affordable, but detectors for
continuous monitoring are expensive. However, as epilepsy detectors
might reduce costs, by reducing the need for long-term in-hospital diag-
nostic monitoring, reducing the need for 24-hour care, and reducing hos-
pital admissions for SE, health insurance companies might be persuaded
to cover the costs of these systems. An economic cost–beneﬁt analysis
will be complex, as potential beneﬁts in health-care utilization will prob-
ably be outweighed by beneﬁts to the quality of life of caregivers.

9. Seizure monitoring in a broader context

Personalized health monitoring in a home setting is an emerging
trend in modern health care. Examples are monitoring of oxygen satu-
ration in people with chronic obstructive pulmonary disease (COPD),
glucose monitoring in people with diabetes, and weight monitoring in
people with heart failure. In these cases, the goal is to obtain ambulatory
data so that health-care professionals can decide if and what further
action/treatment is necessary. The ﬁrst large-scale trial of this type of
monitoring in people with COPD, diabetes, and heart failure showed
promising overall results at 12 months, with a reduced likelihood of
hospital admission (OR: 0.82, 95% CI: 0.70–0.97) and death (OR: 0.54
95% CI: 0.37–0.75) [52]. In pediatric asthma care, electronic evaluation
of adherence to inhaled steroids has led to valuable insights into reasons
for nonadherence, which has enabled pediatricians to provide better in-
formation on medication use [59]. Whether seizure monitoring will
provide comparable beneﬁts is difﬁcult to say, but studies have shown
that disease monitoring in the home setting provides valuable informa-
tion not obtained with monitoring in the hospital setting.

Other developments might ﬁnd their parallel in epilepsy monitoring.
For example, in COPD, care algorithms are being developed to predict

exacerbation based on several clinical parameters [60]. In the care for el-
derly people, camera or radar technology could be used to monitor falls
and nocturnal wandering. To date, there have been no studies of the
safety and inﬂuence on QoL and perceived privacy of the habitants of
this approach. Elderly people have expressed their concern about priva-
cy issues. However, most people are willing to give up a certain amount
of privacy to maintain autonomy and to be able to continue living in
their own home as opposed to moving to a residential care facility
[61]. More needs to be learned about the attitude of people with epilep-
sy regarding autonomy and privacy before online monitoring can be
considered a viable option.

10. Future perspectives

In our opinion, automatic seizure detectors can be used in three
main settings: (1) home-based monitoring with alarm, (2) monitor-
ing with alarm in institutionalized subjects, and (3) in-hospital
or home-based recording with a diagnostic or clinical research
purpose.

When considering home-based, monitoring with alarm, an opti-
mal seizure detector will detect only seizures that require an inter-
vention. Alarms are especially relevant during the night, so
caregivers can sleep in separate bedrooms. The tolerance for false
alarms during the night will be low, as they will unnecessarily
wake a caregiver. A future system needs to be simple to use in a
home setting and not only function in a controlled research environ-
ment with highly trained caregivers.

In an institutional setting, detection of seizures that need inter-
vention is also needed, but the deﬁnition of ‘a seizure needing inter-
vention’ is more focused on situations where the subject requires
medical attention. Especially during the night, one caregiver will at-
tend to multiple subjects who may not reside in the same location.
This means that the false alarm rate needs to be relatively low, as
the caregiver could have to cope with multiple alarms depending
on the number of residents. On the other hand, online camera images
can help make false alarms more manageable by giving the opportu-
nity of a fast visual check of the state of the subject. The availability of
camera images at a central location is an extra requirement for a use-
ful automatic seizure detector in this setting. Especially in institu-
tions with many residents, monitoring can become a high ﬁnancial
burden, so systems need to be as cheap as possible.
In the
MORTEMUS study of registered cases of SUDEP, in all cases, a time
window of at least 3 min after the end of the seizure and before the
start of fatal respiratory and cardiac disruptions was observed [62].
This indicates that there is time for a professional caregiver to assess
the urgency of an automatically detected seizure through camera
images and, subsequently, to decide if physical attendance is needed.
In this scenario, caregivers should be able to provide proper mea-
sures of resuscitation [44]. When the aim of a system is purely
SUDEP prevention, vital sign monitoring instead of seizure detection
could also be an option. Reliable detection of prolonged cardiorespi-
ratory dysfunction is a possibility; however, this is only effective
when very immediate care can be provided.

For seizure detection with a diagnostic or clinical research purpose, a
seizure detector needs to meet different requirements. Many different
seizure types need to be detected and classiﬁed. As the purpose here
is diagnostic, no alarm is necessary and false detections will not have
direct practical care consequences.

Based on the known setting and most prevalent seizure types, it is
probably feasible to optimize seizure detection by adapting the detec-
tion algorithms to the situation. Techniques such as active learning
[63] can further improve a personalized system over time by incorpo-
rating feedback on the correctness of detections. If necessary, this can
be done in a professional care setting where each detection can be
evaluated.

88

10. Conclusion

J. van Andel et al. / Epilepsy & Behavior 57 (2016) 82–89

Not all types of seizures can be successfully detected with existing
seizure detection algorithms and devices. Automatic detection of espe-
cially nocturnal GTCSs seems feasible, though results vary. More studies
in the home setting and involving more subjects with long-term record-
ings are necessary because the general behavior and semiology of sei-
zures can be different, inﬂuencing algorithm or device performance.
Studies tend to be overoptimistic when they report on the performance
of GTCS detection based on the same data used to develop the
algorithm [18,22,26,31]. These algorithms need to be tested in an inde-
pendent population before we know their true value in practice.

Further development of seizure detectors could help improve epi-
lepsy care. Automatic seizure detection could play an important role
in SUDEP prevention, facilitating early intervention in SE, improving
the QoL of caregivers, monitoring drug therapy, and improving long-
term diagnostic investigations and the quality of clinical research. Avail-
able detectors and algorithms are inadequate for detecting other seizure
types, such as hypermotor seizures or generalized tonic seizures.

Future research should involve long-term data collection in a home-
care setting. Detector performance should be expressed as the ‘number
needed to warn’, representing the number of alarms generated to detect
one clinically relevant seizure. This number will differ depending on sei-
zure frequency and can reﬂect the usefulness of monitoring in speciﬁc
patient groups. The beneﬁts and risks of seizure detection should be
monitored, taking into account the QoL of caregivers, the comfort and
privacy of subjects, and the impact of false alarms. Other factors to con-
sider include the increased number of interventions because of SE and
the effects of more accurate knowledge of seizure frequency on
compliance and treatment decisions. Such an integrative approach
could provide insight into the societal beneﬁt of seizure detection in
epilepsy care.

Acknowledgments

This study was funded by ZonMW, grant number 300040003 and by
the Dutch Epilepsy Foundation. The funders had no role in study design,
data collection and analysis, decision to publish, or preparation of the
manuscript.

Conﬂict of interest statement

None of the authors has a personal, commercial interest in automatic

seizure detection.

RDT receives research support from the Dutch Epilepsy Foundations
(project number 15-10), NUTS Ohra Fund, Medtronic, Christelijke
Vereniging voor de Verpleging van Lijders aan Epilepsie and AC
Thomson Foundation. RDT has received fees for lectures from
Medtronic, UCB Pharma, and GSK.

References

[1] Coatsworth JJ. NINDS monograph, 12. Bethesda, MD: US Department of Health and

Education; 1971.

[2] Löscher W, Schmidt D. Modern antiepileptic drug development has failed to deliver:

ways out of the current dilemma. Epilepsia 2011;52(4):657–78.

[3] Hauser W, Allen F, Annegers J, Elveback LR. Mortality in patients with epilepsy.

Epilepsia 1980;21(4):399–412.

[4] Neligan A, Bell GS, Shorvon SD, Sander JW. Temporal trends in the mortality of

people with epilepsy: a review. Epilepsia 2010;51(11):2241–6.

[9] Pauri F, Pierelli F, Chatrian GE, Erdly WW. Long-term EEG-video-audio monitoring:
focal EEG seizure patterns. Electroencephalogr Clin

computer detection of
Neurophysiol 1992;82:1–9.

[10] Hopfengärtner R, Kasper BS, Graf W, Gollwitzer S, Kreiselmeyer G, Stefan H, Hamer
H. Automatic seizure detection in long-term scalp EEG using an adaptive
thresholding technique: a validation study for clinical routine. Clin Neurophysiol
2014;125(7):1346–52.

[11] Ramgopal S, Thome-Souza S, Jackson M, Kadish NE, Fernández IS, Klehm J, et al.
Seizure detection, seizure prediction, and closed-loop warning systems in epilepsy.
Epilepsy Behav 2009;37:291–307.

[12] Duun-Henriksen J, Madsen RE, Remvig LS, Thomsen CE, Sorensen HB, Kjaer TW.
Automatic detection of childhood absence epilepsy seizures: toward a monitoring
device. Pediatr Neurol 2012;46(5):287–92.

[13] Donos C, Dümpelmann M, Schulze-Bonhage A. Early seizure detection algorithm
based on intracranial EEG and random forest classiﬁcation. Int J Neural Syst 2015;
25(5), 1550023. http://dx.doi.org/10.1142/S0129065715500239.

[14] Bhardwaj A, Tiwari A, Krishna R, Varma V. A novel genetic programming ap-
proach for epileptic seizure detection. Comput Methods Prog Biomed 2016;
124:2–18.

[15] Logesparan L, Casson AJ, Rodriguez-Villegas E. Optimal features for online seizure

detection. Med Biol Eng Comput 2012;50(7):659–69.

[16] Juhl CB, Højlund K, Elsborg R, Poulsen MK, Selmar PE, Holst JJ, et al. Automated de-
tection of hypoglycemia-induced EEG changes recorded by subcutaneous electrodes
in subjects with type 1 diabetes — the brain as a biosensor. Diabetes Res Clin Pract
2010;88(1):22–8.

[17] Osorio I, Schachter S. Extracerebral detection of seizures: a new era in epileptology?

Epilepsy Behav 2011;22:S82–7.

[18] Kalitzin S, Petkov G, Velis D, Vledder B, Lopes da Silva F. Automatic segmentation of
episodes containing epileptic clonic seizures in video sequences. IEEE Trans Biomed
Eng 2012;59(12):3379–85.

[19] Van de Vel A, Cuppens K, Bonroy B, Milosevic M, Jansen K, Van Huffel S, et al.
Ceulemans B non-EEG seizure-detection systems and potential SUDEP prevention:
state of the art. Seizure 2013;22(5):345–55.

[20] Nijsen TME, Aarts RM, Arends JBAM, Cluitmans PJM. Automated detection of tonic

seizures using 3-D accelerometry. IFMBE Proc 2008;22:188–91.

[21] Nijsen TM, Aarts RM, Cluitmans PJ, Griep PA. Time–frequency analysis of
accelerometry data for detection of myoclonic seizures. IEEE Trans Inf Technol
Biomed 2010;14(5):1197–203.

[22] Kramer U, Kipervasser S, Shlitner A, Kuzniecky R. A novel portable seizure detection

alarm system: preliminary results. J Clin Neurophysiol 2011;28(1):36–8.

[23] Van de Vel A, Cuppens K, Bonroy B, Milosevic M, Van Huffel S, Vanrumste B, et al.
Long-term home monitoring of hypermotor seizures by patient-worn accelerome-
ters. Epilepsy Behav 2013;26(1):118–25.

[24] Lockman J, Fisher RS, Olson DM. Detection of seizure-like movements using a wrist

accelerometer. Epilepsy Behav 2011;20(4):638–41.

[25] Beniczky S, Polster T, Kjaer TW, Hjalgrim H. Detection of generalized tonic–clonic
seizures by a wireless wrist accelerometer: a prospective, multicenter study.
Epilepsia 2013;54(4):e58–61.

[26] Poh MZ, Loddenkemper T, Reinsberger C, Swenson NC, Goyal S, Sabtala MC, et al.
Convulsive seizure detection using a wrist‐worn electrodermal activity and
accelerometry biosensor. Epilepsia 2012;53(5):e93–7.

[27] Carlson C, Arnedo V, Cahill M, Devinsky O. Detecting nocturnal convulsions: efﬁcacy

of the MP5 monitor. Seizure 2009;18(3):225–7.

[28] Van Poppel K, Fulton SP, McGregor A, Ellis M, Patters A, Wheless J. Prospective study

of the emﬁt movement monitor. J Child Neurol 2013;28(11):1434–6.

[29] Osorio I. Automated seizure detection using EKG. Int J Neural Syst 2014;24(02).
[30] Fulton S, Van Poppel K, McGregor A, Ellis M, Patters A, Wheless J. Prospective study
of 2 bed alarms for detection of nocturnal seizures. J Child Neurol 2013;28(11):
1430–3.

[31] Conradsen I, Beniczky S, Hoppe K, Wolf P, Sorensen HB. Automated algorithm for
generalized tonic–clonic epileptic seizure onset detection based on semg zero-
crossing rate. IEEE Trans Biomed Eng 2012;59(2):579–85.

[32] Luca S, Karsmakers P, Cuppens K, Croonenborghs T, Van de Vel A, Ceulemans B, et al.
Detecting rare events using extreme value statistics applied to epileptic convulsions
in children. Artif Intell Med 2014;60(2):89–96.

[33] van Elmpt WJ, Nijsen TM, Griep PA, Arends JB. A model of heart rate changes to de-

tect seizures in severe epilepsy. Seizure 2006;15(6):366–75.

[34] Narechania AP, Garic II, Sen-Gupta I, Macken M, Gerard EE, Schuele SU. Assessment
of a quasi-piezoelectric mattress monitor as a detection system for generalized con-
vulsions. Epilepsy Behav 2013;28:172–6.

[35] de Bruijne GR, Sommen PCW, Aarts RM. Detection of epileptic seizures through
audio classiﬁcation. 4th European Conference of the International Federation
for Medical and Biological Engineering. Berlin Heidelberg: Springer; 2009.
p. 1450–4.

[36] Nashef L, So EL, Ryvlin P, Tomson T. Unifying the deﬁnitions of sudden unexpected

death in epilepsy. Epilepsia 2012;53(2):227–33.

[5] Shorvon S. The epidemiology and treatment of chronic and refractory epilepsy.

[37] Thurman DJ, Hesdorffer DC, French JA. Sudden unexpected death in epilepsy:

Epilepsia 1996;37(Suppl. 2):S1–3.

assessing the public health burden. Epilepsia 2014;55(10):1479–85.

[6] Jacoby A, Snape D, Baker GA. Determinants of quality of life in people with epilepsy.

[38] Tomson T, Nashef L, Ryvlin P. Sudden unexpected death in epilepsy: current knowl-

Neurol Clin 2009;27(4):843–63.

[7] Mormann F, Andrzejak RG, Elger CE, Lehnertz K. Seizure prediction: the long and

winding road. Brain 2007;130:314–33.

[8] Cook MJ, O'Brien TJ, Berkovic SF, Murphy M, Morokoff A, Fabinyi G, et al. Himes D
prediction of seizure likelihood with a long-term, implanted seizure advisory system
in patients with drug-resistant epilepsy: a ﬁrst-in-man study. Lancet Neurol 2013;
12(6):563–71.

edge and future directions. Lancet Neurol 2008;7(11):1021–31.

[39] Téllez-Zenteno JF, Hernández Ronquillo L, Wiebe S. Sudden unexpected death in
epilepsy: evidence-based analysis of incidence and risk factors. Epilepsy Res 2005;
65:101–15.

[40] Hesdorffer DC, Tomson T, Benn E, Sander JW, Nilsson L, Langan Y, et al. Do antiepi-
leptic drugs or generalized tonic–clonic seizure frequency increase SUDEP risk? A
combined analysis. Epilepsia 2012;53(2):249–52.

J. van Andel et al. / Epilepsy & Behavior 57 (2016) 82–89

89

[41] Lamberts RJ, Thijs RD, Laffan A, Langan Y, Sander JW. Sudden unexpected death in
epilepsy: people with nocturnal seizures may be at highest risk. Epilepsia 2012;
53(2):253–7.

[42] Langan Y, Nashef L, Sander JW. Case–control study of SUDEP. Neurology 2005;64(7):

1131–3.

[53] Johansen JR, Lindahl G, Sandstedt P. Home-video observation of seizures in children

with epilepsy-impact on quality of family life. Seizure 1999;8:356–7.

[54] Eisenman LN, Attarian H, Fessler AJ, Vahle VJ, Gilliam F. Self-reported seizure fre-
quency and time to ﬁrst event in the seizure monitoring unit. Epilepsia 2005;
46(5):664–8.

[43] Shorvon S, Tomson T. Sudden unexpected death in epilepsy. Lancet 2011;378:

[55] Elger CE, Burr W. Advances in telecommunications concerning epilepsy. Epilepsia

2028–38.

2000;41(Suppl. 5):S9–S12.

[44] Ryvlin P, Nashef L, Tomson T. Prevention of sudden unexpected death in epilepsy: a

[56] Vigevano F, Arzimanoglou A, Plouin P, Specchio N. Therapeutic approach to epileptic

realistic goal? Epilepsia 2013;54(S2):23–8.

encephalopathies. Epilepsia 2013;54(s8):45–50.

[45] Rosenow F, Hamer HM, Knake S. Epidemiology of convulsive and nonconvulsive

status epilepticus. Epilepsia 2007;48(S8):82–4.

[46] Knake S, Rosenow F, Vescove M, Oertel WH, Mueller H-H, Wirbatz A, Katsarou N,
Hamer HM. Incidence of status epilepticus in adults in Germany: a prospective,
population-based study. Epilepsia 2001;42(6):714–8.

[47] DeLorenzo RJ, Hauser WA, Towne AR, Boggs JG, Pellock JM, Penberthy L, et al. A pro-
spective, population-based epidemiologic study of status epilepticus in Richmond,
Virginia. Neurology 1996;46:1029–35.

[48] Neligan A, Shorvon SD. Prognostic factors, morbidity and mortality in tonic–clonic

status epilepticus: a review. Epilepsy Res 2010;93:1–10.

[49] Nguyen R, Téllez Zenteno JF. Injuries in epilepsy: a review of its prevalence, risk

factors, type of injuries and prevention. Neurol Int 2009;16(1):e20.

[50] Van Andel J, Zijlmans M, Fischer K. Leijten FSS quality of life of caregivers of patients

with intractable epilepsy. Epilepsia 2009;50(5):1294–6.

[51] Van Andel J, Westerhuis W, Zijlmans M, Fischer K, Leijten FSS. Coping style and
health-realted quality of life in caregivers of people with epilepsy. J Neurol 2011;
258:1788–94.

[52] Larson AM, Ryther RCC, Jennesson M, Geffrey AL, Bruno PL, Anagnos CJ, et al. Impact
of pediatric epilepsy on sleep patterns and behaviors in children and parents.
Epilepsia 2012;53(7):1162–9.

[57] Nijsen TME, Arends JBAM, Griep PAM, Cluitmans PJM. The potential value of three-
dimensional accelerometry for detection of motor seizures in severe epilepsy.
Epilepsy Behav 2005;7(1):74–84.

[58] Edworthy J. Medical audible alarms: a review. J Am Med Inform Assoc 2013;20(3):

584–9.

[59] Morton RW, Everard ML, Elphick HE. Adherence in childhood asthma: the elephant

in the room. Arch Dis Child 2014;99(10):949–53.

[60] Pinnock H, Hanley J, McCloughan L, Todd A, Krishan A, Lewis S, et al. Effectiveness of
telemonitoring integrated into existing clinical services on hospital admission
for exacerbation of chronic obstructive pulmonary disease: researcher blind,
multicentre, randomised controlled trial. BMJ 2013;17:347.

[61] Townsend D, Knoefel F, Goubran R. Privacy versus autonomy: a tradeoff model for
smart home monitoring technologies. Conf Proc IEEE Eng Med Biol Soc 2011:
4749–52.

[62] Ryvlin P, Nashef L, Lhatoo SD, Bateman LM, Bird J, Bleasel A, et al. Incidence and
in epilepsy monitoring units

mechanisms of
(MORTEMUS): a retrospective study. Lancet Neurol 2013;12:966–77.

cardiorespiratory arrests

[63] Cohn D, Atlas L, Ladner R. Improving generalization with active learning. Mach Learn

1994;15(2):201–21.
