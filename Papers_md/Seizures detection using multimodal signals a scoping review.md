# Seizures detection using multimodal signals a scoping review

Physiological Measurement     TOPICAL REVIEW • OPEN ACCESSSeizures detection using multimodal signals: ascoping reviewTo cite this article: Fangyi Chen et al 2022 Physiol. Meas. 43 07TR01 View the article online for updates and enhancements.You may also likeRisk of seizures induced by intracranialresearch stimulation: analysis of 770stimulation sessionsHannah E Goldstein, Elliot H Smith,Robert E Gross et al.-Non-invasive wearable seizure detectionusing long–short-term memory networkswith transfer learningMona Nasseri, Tal Pal Attia, Boney Josephet al.-Seizure forecasting using machinelearning models trained by seizure diariesEzequiel Gleichgerrcht, Mircea Dumitru,David A Hartmann et al.-This content was downloaded from IP address 158.46.181.81 on 23/01/2023 at 19:00OPEN ACCESS

RECEIVED
25 November 2021

REVISED
31 May 2022

ACCEPTED FOR PUBLICATION
20 June 2022

PUBLISHED
18 July 2022

Original content from this
work may be used under
the terms of the Creative
Commons Attribution 4.0
licence.

Any further distribution of
this work must maintain
attribution to the
author(s) and the title of
the work, journal citation
and DOI.

Physiol. Meas. 43 (2022) 07TR01

https://doi.org/10.1088/1361-6579/ac7a8d

TOPICAL REVIEW

Seizures detection using multimodal signals: a scoping review

, Ina Chen1

Fangyi Chen1,5,∗
1 Department of Biomedical Engineering, Duke University, Durham, NC, United States of America
2 Department of Paediatrics, Neurology, School of Medicine, Duke University, Durham, NC, United States of America
3 Duke Comprehensive Epilepsy Center, Department of Neurology, School of Medicine, Duke University, Durham, NC, United States of

, Muhammad Zafar2, Saurabh R Sinha3 and Xiao Hu4

America

4 Department of Biomedical Engineering, Biostatistics & Bioinformatics, School of Medicine, School of Nursing, Duke University,

Durham, NC, United States of America

5 Corresponding author
∗ Author to whom any correspondence should be addressed.

E-mail: fangyi.chen727@duke.edu

Keywords: seizure, epilepsy, ML, wearable, sensors, detection, prediction

Supplementary material for this article is available online

Abstract
Introduction. Epileptic seizures are common neurological disorders in the world, impacting 65 million
people globally. Around 30% of patients with seizures suffer from refractory epilepsy, where seizures
are not controlled by medications. The unpredictability of seizures makes it essential to have a
continuous seizure monitoring system outside clinical settings for the purpose of minimizing patients’
injuries and providing additional pathways for evaluation and treatment follow-up. Autonomic
changes related to seizure events have been extensively studied and attempts made to apply them for
seizure detection and prediction tasks. This scoping review aims to depict current research activities
associated with the implementation of portable, wearable devices for seizure detection or prediction
and inform future direction in continuous seizure tracking in ambulatory settings. Methods. Overall
methodology framework includes 5 essential stages: research questions identiﬁcation, relevant studies
identiﬁcation, selection of studies, data charting and summarizing the ﬁndings. A systematic searching
strategy guided by systematic reviews and meta-analysis (PRISMA) was implemented to identify
relevant records on two databases (PubMed, IEEE). Results. A total of 30 articles were included in our
ﬁnal analysis. Most of the studies were conducted off-line and employed consumer-graded wearable
device. ACM is the dominant modality to be used in seizure detection, and widely deployed algorithms
entail Support Vector Machine, Random Forest and threshold-based approach. The sensitivity ranged
−1.
from 33.2% to 100% for single modality with a false alarm rate (FAR) ranging from 0.096 to 14.8 d
−1.
Multimodality has a sensitivity ranging from 51% to 100% with FAR ranging from 0.12 to 17.7 d
Conclusion. The overall performance in seizure detection system based on non-cerebral physiological
signals is promising, especially for the detection of motor seizures and seizures accompanied with
intense ictal autonomic changes.

1. Introduction

An epileptic seizure is deﬁned as transient symptoms due to the occurrence of abnormal electrical activity within
the brain, and more than one unprovoked seizure occurring > 24 h apart or a single seizure with a high
probability of recurrence is considered as epilepsy (Fisher et al 2014). Epilepsy is one of the most prevalent
neurological disorders in the world, impacting around 65 million people of all ages globally (Mehndiratta and
Wadhai 2015). Around 70% of epileptic cases can be controlled by the proper diagnosis and treatment; the
remaining 30% of patients with epilepsy are medication refractory, a subset of whom may be controlled with
surgery. Their unpredictability makes seizures extremely dangerous or even fatal, especially in an unsupervised
environment. For example, the risk of sudden unexpected death in epilepsy (SUDEP), one of the common

© 2022 The Author(s). Published on behalf of Institute of Physics and Engineering in Medicine by IOP Publishing Ltd

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

causes of death among epileptic patients, is likely higher when there is a lack of attention and failure to provide
urgent medical care, which may well explain a high risk of SUDEP during sleep periods at night (Nashef et al
1998, Lamberts et al 2012). Accidental injury/fatality related to seizures and SUDEP would potentially be
reduced if caregivers and physicians could reliably know when a patient had a seizure. As a matter of fact, a
continuous seizure detection and monitoring device is necessary in assisting caregivers and physicians to provide
clinical support and diagnosis, thereby preventing severe seizure-related injuries and improving the quality of
life for patients. Current options for seizure detection and monitoring are limited; for example, via video-EEG or
ambulatory EEG, which are obtrusive and unsuitable for long-term continuous seizure monitoring outside
clinical settings. A wearable device capable of acquiring non-cerebral physiological signals (ECG, EDA, EMG,
acceleration, oxygen saturation etc) is an alternative method to overcome these barriers. Moreover, these non-
cerebral manifestations may even precede the seizure onset as detected by scalp-EEG to forecast seizure events to
allow for patients or caregivers to take early actions (Lacuey et al 2019).

Many studies have established the linkage between physiological signals obtainable in ambulatory settings
and the occurrence of seizures (Ansakorpi et al 2000, Baumgartner et al 2001, Opherk et al 2002, Devinsky 2004).
Seizures spreading to certain parts of central nervous system may alter normal autonomic function as they
mimic the afferent action of the autonomic nervous system (ANS) (Devinsky 2004, Thijs 2019). The ANS is
responsible for regulating involuntary physiological functions, such as heart rate, respiration, blood pressure,
digestion, temperature, etc. Typically, the ictal or postictal state activates sympathetic nervous system, perceived
as increased heart rate, blood pressure and breathing as well as facial ﬂushing, pupillary dilatation
(Devinsky 2004). It is also possible for parasympathetic system to be activated during ictal or preictal state, which
leads to increased salivation, gastric acid secretion, decreased heart rates and blood pressured (Devinsky 2004).
The systematic review conducted by Baumgartner’s group presents a comprehensive overview of predominant
ictal autonomic changes in cardiovascular, respiratory, gastrointestinal, cutaneous, pupillary and urinary
aspects (Baumgartner et al 2001). Autonomic manifestations are often perceived in partial seizures but may
sometimes remain unnoticed, resulting in a delayed or even missed diagnosis (Devinsky 2004). A potential high
association has been reported between ictal central apneas (ICA) and focal epilepsy particularly mesial temporal
lobe epilepsy (MTLE), and ICA can be the earliest clinical sign or even the sole manifestation of some seizures in
MTLE (Lacuey et al 2019). Other biomarkers include but are not limited to changes of electrodermal activities
(Vieluf et al 2020), inﬂammation-like responses (evaluated body temperature, white blood cell counts, or
C-reactive protein levels) (Hong Seok et al 2016). These and other ﬁndings demonstrate the links between
seizure and the ANS and have laid a solid foundation for developing algorithms to detect or predict seizure
events based on physiological signals that can reﬂect status changes of the ANS. In addition, it can be anticipated
that performance based on the single modality may not be optimal, but the integration of multimodalities would
allow for more accurate seizure detection or prediction (van Westrhenen et al 2019).

A recently published International League Against Epilepsy (ILAE) guideline (Beniczky et al 2021)
summarized wearable devices used for seizure detection as well as their performances, and seizure types
recorded. The guideline targets on a speciﬁc group of audience, with a goal to inform and assist clinicians to
utilize wearable devices for appropriate seizure type. In contrast, our paper has a wider audience targeting on
clinicians, engineers, and researchers interested in algorithms behind, which caters to readers with various
background and needs. Beyond that, we noticed that the guideline excluded some essential elements that are
directly associated with the detection performance, such as extracted feature characteristics and deployed
algorithms, which were captured and discussed by this scoping review. Another older and much shorter
review paper (Leijten and Dutch TeleEpilepsy Consortium 2018) in the ﬁeld selected 7 studies to summarize
key algorithms and performance for seizure detection, limiting their scope to motor seizures that occur
during nighttime and excluding the ones using single- modality signal, which also missed to document
feature extraction processes and characteristics as well as the speciﬁc types of models being implemented.
Instead, we included all relevant studies using wearable devices for routine seizure monitoring to better
appreciate the variations across different types of seizures and how unimodal or multimodal devices affect
performances. We believe that a more detailed description and analysis regarding the extracted features and
algorithms would generate a comprehensive image of the current research activities in the ﬁeld of
ambulatory seizure detection/prediction and particularly help researchers in developing and advancing
algorithms for seizure monitoring.

This scoping review is intended to provide a comprehensive mapping of current research activities

associated with continuous seizure detection and monitoring solutions in ambulatory settings using wearable or
implantable devices that are capable of recording physiological signals relevant to seizure detection. Several
research questions were proposed and investigated: (i) what is known from current literature regarding the
physiological signals used in ambulatory settings? (ii) what are the speciﬁcations of the devices used for recording
these signals? (iii) what are the computational algorithms applied in processing signals? (iv) what is the
performance of these algorithms?The anticipated outcome of the review is to inform the future direction in

2

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Table 1. Database and keywords used in literature search.

Electronic database

Searching keywords

PubMed/IEEE

‘(seizure

*

OR epileps

*) AND (predict

*

OR monitor

*

*
OR alert

OR detect

*) AND (device

*

OR wearable OR implant

*)’

continuous seizure detection or forecasting outside clinical settings and inspire further innovations in sustained
seizure tracking based on the discussed signals.

2. Method

The scoping review was guided by the methodology framework proposed by Arksey and O’Malley (Levac et al
2010). During this work, ﬁve essential stages were identiﬁed in conducting scoping reviews, which involve
identiﬁcation of research question, identifying relevant studies, study selection, data charting and lastly
summarizing and reporting the results.

2.1. Identify research question
To determine the applicable physiological signals and how they can be analyzed in seizure detection and
monitoring in ambulatory settings and to provide a comprehensive summary of the relevant studies, the review
was built upon four research questions:

(1)What is known from current literature regarding the physiological/motor signals used in ambulatory

settings?

(2)What are the speciﬁcations of the devices being used for recording these signals?

(3)What are the computational algorithms applied in the studies?

(4)What is the performance of these algorithms?

2.2. Identify relevant studies
Literature search was performed in two databases: PubMed and IEEE (Institute of Electrical and Electronics
Engineers). PubMed contains millions of published literatures in the ﬁeld of biomedical and life science. To
complement PubMed, IEEE is another source for identifying relevant studies with a focus on engineering and
technology research. The keywords used for searching relevant articles are listed in table 1.

2.3. Selection of eligible studies
The selection process was guided by Preferred Reporting Items for Systematic reviews and Meta-Analyses
(PRISMA) statement (Page et al 2021). Identiﬁed articles went through several stages to be included in the
scoping review. Two reviewers (FC and IC) performed double- blinded screening based on titles and abstracts to
ensure that included articles were related to our topic. Senior authors (SRS and XH) were consulted to resolve
any ambiguity or disagreement regarding whether to include speciﬁc articles. Articles were included if they
met all of the following inclusion criteria:

(cid:129) Related to seizure detection or prediction.

(cid:129) Published between year 2011 and year 2021.

(cid:129) Able to access full text.

(cid:129) Used at least one physiological signal listed in table 2.

(cid:129) Signals were collected using wearable or implantable devices.

(cid:129) Algorithms were described in sufﬁcient details.

(cid:129) Clinical studies of either prospective or retrospective nature.

2.4. Data charting
The relevant information from the included articles was captured electronically in Microsoft Excel. A list of data
elements that were extracted from each study is shown in table 3. We organized these elements into ﬁve

3

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Table 2. Explanation of the commonly employed physiological signals in seizure detection/prediction.

Physiological signals

Electroencephalography (EEG)
Electrocardiogram (ECG)
Accelerometry (ACM)
Electrodermal activity (EDA)
Electromyography (EMG)
Photoplethysmography (PPG)

Description

Measurement in the change of electrical impulses in brain
Measurement of electrical activity of heartbeat
Quantiﬁcation of movement changes in velocity and direction
Measurement of electrical conductance of skin in response to sweat
Measurement of muscle activity
Utilize a light-based approach to sense the rate of blood ﬂow

Table 3. Lists of essential data elements captured from articles,
organized in ﬁve categories.

Categories of data elements

Data elements

Study characteristics

Device characteristics

Signal characteristics

Algorithm characteristics

Performance

(cid:129) Study setting
(cid:129) Recorded status
(cid:129) Populations
(cid:129) Number of recruited and Number

of analyzed

(cid:129) Length of recording
(cid:129) Reference/Ground Truth
(cid:129) Seizure types
(cid:129) Forms of implantation
(cid:129) Wearability/Ergonomic
(cid:129) Device brand
(cid:129) Data storage
(cid:129) Capacity on device
(cid:129) Modality
(cid:129) Synchronization for multimodality
(cid:129) Sampling rate
(cid:129) Number of channels
(cid:129) Quality assessments and artifacts

removal

(cid:129) Expert annotation with seizure

onset/termination

(cid:129) Intention
(cid:129) Real-time?
(cid:129) Feature domain
(cid:129) Algorithm
(cid:129) Patient-speciﬁc?
(cid:129) Sensitivity
(cid:129) Accuracy
(cid:129) False alarm rate
(cid:129) Speciﬁcity
(cid:129) AUC
(cid:129) Positive predictive value

categories: study characteristics, device characteristics, signal characteristics, algorithm characteristics, and
algorithm performance. Most of the elements in the list are self-explanatory so we will focus on describing three
more nuanced data elements: seizure type, feature domains, and performance metrics. Even though for
ambulatory seizures detection/prediction tasks, the determination of seizure types is not the ultimate purpose,
rather providing timely alerts when a seizure strikes regardless of the type. However, we included this element as
to take the advantage of studies conducted at Epilepsy Monitoring Units (EMU)-based settings where seizure
types are readily available. Such information would be helpful for researchers to develop seizure-speciﬁc
algorithms as well as to provide insightful knowledge regarding the current choice of algorithms/modalities as
related to seizure types. Besides, it helps to identify the groups of individuals suitable for using wearable devices
for seizure monitoring, suggesting appropriate modalities and algorithms used for speciﬁc types of seizures.
Under the basic seizure classiﬁcation guidelines proposed by ILAE, seizures can be categorized into three

main groups based on onset: focal onset, generalized onset and unknown onset (Devinsky et al 2018). The

4

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Table 4. Descriptions of data elements captured in performance category.

Data elements

Description

Sensitivity
False alarm rate (FAR)
Positive predictive value
Speciﬁcity
AUC

The number of seizures detected divided by the number of physician-annotated seizures
The number of false detections (normal activity classiﬁed as a seizure) over a certain period of time
The proportion of seizure cases that are correctly identiﬁed
The proportion of actual non-seizure cases which are correctly identiﬁed
The area under the receiver operating characteristic (ROC) curve

essential distinction between focal and generalized seizures is that, at onset, focal seizures affect only a region of
the brain whereas generalized involve both hemispheres from the onset (Devinsky et al 2018). Focal onset
seizures may spread from the region of onset to involve both hemispheres, in which case they are said to have
become secondarily generalized. The category of unknown onset seizures is needed because it is not always
possible to classify a seizure precisely based on the available clinical data. Focal (and unknown) onset can be
further subdivided based on the presence or absence of impairment of awareness: focal with retained awareness
(previously called simple partial seizures) and focal with impaired awareness (previously called complex partial
seizures) (Devinsky et al 2018). All generalized onset seizures have impaired awareness. Depending on the type of
seizures and the speciﬁc brain regions involved, the symptoms of seizures can be highly varied and can include
motor (simple and complex), sensory, cognitive (confusion, loss of awareness), psychic and autonomic
phenomenon (Stafstrom and Carmant et al 2015). For clinical classiﬁcation purposes, the extent of motor
symptoms is an important feature in assessing patients’ conditions and examining potential treatment options
with better outcomes. In the context of this paper, the recorded seizures were grouped in accordance with the
classiﬁcation guidelines proposed by ILAE (Fisher et al 2014), but with minor adjustments. We placed focal to
bilateral tonic-clonic (FTBTC) into generalized-motor category, since the two types of seizure are highly similar
clinically and can be hard to differentiate using non-EEG modality.

The feature domains were divided into 4 different categories (time, spatial, frequency, and nonlinear) to
capture the feature characteristics being used for model construction. Time domain analysis depicts the changes
in a physiological signal with respect to time, whereas for frequency domain features, the signals are quantiﬁed in
given frequency bands. Spatial domain refers to the analysis in the variation for a signal across space. Lastly,
nonlinear domain features include entropy, laminarity, recurrence rate, determinism and so on that aim to
characterize dynamical evolution of the system that are presumably responsible for generating analyzed signals.
Different studies may choose to report different performance metrics. We therefore decided to capture all
reported performance metrics including sensitivity, accuracy, false alarm rate, positive predictive value. Their
corresponding deﬁnitions are given in table 4.

2.5. Collating, summarizing and reporting the results
Results collected from the data capture sheet were summarized in a narrative format along with data tabulation
and visualization. To answer the proposed four research questions, results were grouped by the following
categories (modality, device, applied algorithms, performance).

3. Results

The article selection procedure is depicted in ﬁgure 1. A total of 2927 records were initially identiﬁed. The initial
search was concluded at the end of february 2021. During manuscript writing, additional citations drawn from
related review articles and manual searching were screened to identify new articles to be included. We believe
this update was necessary to ensure the timeliness of this review because the research in this ﬁeld is accelerating.
We thus identiﬁed ﬁve additional articles and a total of 30 articles were included.

As summarized from the included studies, current wearable devices for seizure detection or prediction
heavily rely on ECG, ACM, EDA, EMG signals or various combinations of them. In 70% of studies, only a single
modality was used to detect seizures with ACM being the most prevalent one and EDA never being used alone.
Majority of recruited subjects were monitored on a continuous basis and around 83% of studies took place
entirely in an inpatient EMU. Among all the modalities (table 6), many of the articles applied consumer-graded
devices available in the market, analyzed data in an ofﬂine fashion, and focused on seizure detection. Many of
them used video EEG (vEEG) as a gold standard to validate the developed algorithms. A comprehensive
documentation for each article can be found in the supplementary materials (available online at stacks.iop.org/
PMEA/43/07TR01/mmedia).

5

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Figure 1. Flow chart for article selection process, modiﬁed from suggested template in PRISMA.

3.1. Study and device characteristics
table 7 shows ﬁndings according to the applied modalities and the target seizure types and device being used.
Motor seizures (accompanied by some degree of involuntary muscle movements) were investigated and

6

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Table 5. The mapping table for the 30 selected articles and the number ordering used in all tables in Results section, with respective
references.

Article
number

Article title

Reference

1

2

3

4
5

6
7

8

9

10
11
12

13
14

15
16
17

18
19

20

21

22
23

24

25
26
27

28

29

30

Automated epileptic seizure detection based on wearable ECG and PPG in a hospital

Vandecasteele et al (2017)

environment

Multimodal, automated detection of nocturnal motor seizures at home: Is a reliable seizure

van Andel et al (2017)

detector feasible?

Multimodal nocturnal seizure detection in a residential care setting: a long-term prospective

Arends et al (2018)

trial

Detection of seizure-like movements using a wrist accelerometer
Measurement and quantiﬁcation of generalized tonic-clonic seizures in epilepsy patients by

means of accelerometry—An explorative study

Automated real-time detection of tonic-clonic seizures using a wearable EMG device
Convulsive seizure detection using a wrist-worn electrodermal activity and accelerometry

Lockman et al (2011)
Schulc et al (2011)

Beniczky et al (2018)
Poh et al (2012)

biosensor

Using wearable sensors for semiology-independent seizure detection—towards ambulatory

Heldberg et al (2015)

monitoring of epilepsy

Multicenter clinical assessment of improved wearable multimodal convulsive seizure

Onorati et al (2017)

detectors

Multi-biosignal analysis for epileptic seizure monitoring
Seizure detection based on heart rate variability using a wearable electrocardiography device
Wearable epileptic seizure prediction system with machine-learning-based anomaly detec-

Cogan et al (2016)
Jeppesen et al (2019)
Yamakawa et al (2020)

tion of heart rate variability

Evaluation of novel algorithm embedded in a wearable sEMG device for seizure detection
Ear-EEG detects ictal and interictal abnormalities in focal and generalized epilepsy-a com-

parison with scalp EEG monitoring

Detection of generalized tonic-clonic seizures from ear-EEG based on EMG analysis
Detection of generalized tonic-clonic seizures using surface electromyographic monitoring
A prospective, multicenter study of cardiac-based seizure detection to activate vagus nerve

stimulation

Seizure detection using heart rate variability: a prospective validation study
Detection of generalized tonic-clonic seizures by a wireless wrist accelerometer: a pro-

spective, multicenter study

Accelerometry-based home monitoring for detection of nocturnal hypermotor seizures

based on novelty detection

Conradsen et al (2012)
Zibrandtsen et al (2017)

Zibrandtsen et al (2018)
Halford et al (2017)
Boon et al (2015)

Jeppesen et al (2020)
Beniczky et al (2013)

Cuppens et al (2014)

Tracking generalized tonic-clonic seizures with a wrist accelerometer linked to an online

Velez et al (2016)

database

Spectral analysis of acceleration data for detection of generalized tonic-clonic seizures
User-based evaluation of applicability and usability of a wearable accelerometer device for

Joo et al (2017)
Meritam et al (2018)

detecting bilateral tonic-clonic seizures: a ﬁeld study

Tonic-clonic seizure detection using accelerometry-based wearable sensors: a prospective,

Johansson et al (2019)

video-EEG controlled study

Automated detection of convulsive seizures using a wearable accelerometer device
Machine learning from wristband sensor data for wearable, noninvasive seizure forecasting
Computationally-efﬁcient Algorithm for Real-Time Absence Seizure Detection in Wearable

Kusmakar et al (2019)
Meisel et al (2020)
Dan et al (2020)

Electroencephalography

Detection of generalized tonic clonic seizures and falls in unconstraint environment using

Zia et al (2021)

smartphone accelerometer

Non-invasive wearable seizure detection using long-short-term memory networks with

Nasseri et al ((2021)

transfer learning. Journal of neural engineering

Seizure detection using wearable sensors and machine learning: setting a benchmark

Tang et al (2021)

analyzed in every chosen article, except for some using ECG and PPG-based modality. Motor seizures can be
further divided into focal-onset (originate in one hemisphere) and generalize-onset (originate on both sides).
Focal-onset category contains temporal lobe seizure (n=2) (please refer to table 5 [1], [15]), focal-impaired
awareness (n=3) (please refer to table 5 [10], [18], [25]), focal motor (hyper-motor, hyperkinetic) (please refer
to table 5 [2], [3], [8]). Generalized tonic-clonic (GTC) seizure fell under the subcategory of generalize-onset,
which was recognized as one prevalent seizure type investigated by 50% of the articles. For motor seizures,
perceived as intense body motion, accelerometry is one frequently used modality to quantify acceleration and
vibration of a subject’s actions. Currently, there are many devices available in the market for acquiring such

7

Physiol. Meas. 43 (2022) 07TR01

Table 6. Essential data elements sharded by the included studies.

Characteristics

In patients only
Mixed subjects: adults and pediatric
recording>24 h daily

Multiple seizure types analyzed

Reference: Video-EEG
Consumer graded device
Artifact removal
Detection purpose
Threshold-based algorithm
Other algorithms
Off-line processed
Non-patient speciﬁc

ECG

ACM

EDA

EMG

EEG

n

5
2

4

3
5
4
5
5
3
2
3
1

%

100
40

80

60
100
80
100
100
60
40
60
20

n

8
4

6

1
9
10
7
10
4
6
6
1

%

80
40

60

10
90
100
70
100
40
60
60
10

n

—
—

—

—
—
—
—
—
—
—
—
—

%

—
—

—

—
—
—
—
—
—
—
—
—

n

3
3

3

—

3
3
—

3
3
—

1
—

%

100
100

100

—

100
100
—

100
100
—

33
—

n

2
—

3

1
3
—

3
3
2
1
2
3

%

67
—

100

33
100
—

100
100
67
33
67
100

F Chen et al

Multi-
modality

n

6
4

7

7
7
9
6
8
2
7
9
7

%

67
44

78

78
78
100
67
89
22
78
100
78

*
Note: the percentage represents the ratio between number of articles in each modality with such characteristic and the total number of
studies utilized that modality, round up to the nearest integer.

accelerometer signals, such as SmartWatch developed by Smart Monitor Inc., Nintendo, Epic-Care Free and
Shimmer etc. Another common modality targeting generalized motor seizures is EMG. However, the
acquisition of EMG signals typically requires several electrodes inserting into the skin, which could be painful for
patients. We found 3 eligible studies (please refer to table 5 [6], [13], [16]) based on surface EMG (sEMG)
modality that enables noninvasive monitoring. ECG or PPG-based modality is favorable in detecting seizure
without accompanying intense motion, where the common acquisition device is Epatch, and wearable sensors
developed by Empatica. We also compared the differences in choice of devices among the studies grouped by
seizure types (non-motor, motor, mixtures), shown in table 9.

The average recording length for each brand of device is reported in table 8. The examination of user
experience and data transmissions, if mentioned by the studies, were also recorded. Most of average recording
length for the device were greater than 2 months, with the exception of three devices (Nintendo, AspireSR and
Cyberonics). Within the scope of these studies, 7 brands of device acquired the interested physiological signals for
more than 6 months. Majority of these wearable sensors are easy to implement without special training and
assistance, and a few devices (e.g. Shimmer, custom-built: designed and built for research purpose, not available
in commercial markets) reported connectivity issues during recording periods. Four studies (please refer to
table 5 [11], [14], [16], [23]) reported adverse effects and they include the following: skin irritation, ear-
discomfort (for wearable ear-EEG device), sweltering. Both ePatch , Brain Sentinel and Epic-Care Free were
reported to cause some mild to moderate skin irritation after using the device (please refer to table 5 [11], [16],
[23]). Zibrandsten et al constructed a wearable ear-EEG sensor that required an expert assistant to place within
the outer portion of the external meatus, where the majority of the patients complained of increasing tenderness
and soreness in the external ear.

3.2. Algorithm
Algorithm 1(a) and 1(b) summarize the main algorithms from the articles organized by the seizure types, along
with the corresponding modalities and feature domains. Time domain features derived from acquired signals
were widely deployed in model construction, followed by frequency domain features. Fewer studies (n = 4)
(please refer to table 5 [7], [8], [9], [20]) utilized nonlinear features (entropy, laminarity, deterministic and so on)
in their algorithms. For ECG, the common features are HR, average HR, various metrics based on heart rate
variability (HRV) analysis, cardiac sympathetic index (CSI), cardiac vagal index (CVI), laminarity, etc. Regarding
EDA modality, the calculated features normally capture the variation in skin conductance response and skin
conductance level between current and previous segments, which mostly reside in time domain category.
Conversely, classiﬁers based on EMG and ACM signals often used frequency domain features, such as amplitude
under high frequency (> 150 Hz). Half of these studies utilized threshold-based algorithms in which they
determined the optimal passing value and duration for a case to be considered as an epileptic seizure event. In

8

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Table 7. Summary of analyzed seizure types and employed devices in each study grouped by modality used, with article number and counts
speciﬁed.

Modality

Targeted seizures

Device brand

Studies

Single-modality

ECG

PPG
ACM

EDA
EMG

EEG

Multi-modality

ECG and ACM

PPG and ACM

ACM and EDA

EDA and HR and SPO2

and EEG

EDA and ACM and BVP

and TEMP

Seizure

Focal Onset
Generalized Onset

NCS
iTC
Focal Onset

Generalized Motor

Focal Onset

—

Generalized Motor

Generalized Motor
Focal Onset
Generalized Onset
Generalized Motor
Focal Motor
Clusters
Generalized Motor
Focal Motor
Clusters
Generalized Motor

Focal Motor
Focal Non-motor
Generalized motor

Focal Onset
Generalized Onset

Generalized Motor
All types

# of
Studies

2
3

1
1
1

9

1

—

3

2
1
1
1
1
1
1
1
1
2

1
1
1

1
1

1
2

Faros

[1, 11, 12, 17, 18]

Epatch (n = 2)
AspireSR
Cyberonics
Empatica
Smart Monitor (n = 3)
Nintendo
Epi-Care Free (n = 2)
Apple iPod Touch
RISE Acreo
Shimmer
Custom- built
—
IctalCare (n = 2)
Brain Sentinel (n = 1)

[1]
[4, 5, 19–22, 23a, 24],
[25, 28]a

—
[6, 13, 16]

Custom-built (n = 2)
Medatec (BrainWalker 3)

[14, 15, 27]a

[2]

[3] a

[7–9]

Shimmer

LivAssured BV

Custom- built (n = 1)
Empatica (n = 2)
iCalm from MIT Lab (n

= 1)

Nonin (WristOX2)

[10]

Affectiva (Q- Curve sensor)

Empatica (n = 3)

[26, 29a, 30]

a Study conducted under ambulatory settings: (please refer to table 5 [3, 23, 27. 28, 29]).
*
Focal-onset seizure: Temporal lobe seizure (TLE), Focal impaired awareness (FIA), Focal-motor: Hyper-motor (HM), Focal hyperkinetic
(HK).
*
Generalized-onset seizure: Idopathetic generalized epilepsy (IGE), Generalized-motor: Tonic-clonic seizure (TC), Generalized tonic-clonic
seizure (GTC), Focal to bilateral tonic-clonic (FTBTC), Generalized tonic (GT), Bilateral-tonic (BT).
*
Non-convulsive seizures (NCS), ictal tachycardia (iTC) seizure.

particular, the compared metrics involved the rise of HR, numbers of high amplitude and frequency oscillations
denoted as the number of zero crossing, duration for such increment and so on. Besides, 2/3 of the selected
articles performed off-line processing, and a large portion of the real-time classiﬁers fell under the threshold-
based algorithm that mostly targeted motor seizure events. In addition, a few articles (n=5) (please refer to
table 5 [10], [12], [14], [20], [27]) constructed patient-speciﬁc algorithms, where one of them was semi-patient
speciﬁc (Arends et al 2018) model which was trained not only by the individual’s data but others as well.
Traditional machine learning algorithms (support vector machine, random forest, k-nearest-neighbor, etc)

9

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Table 8. Comparison of durability and usability among all collected device branda.

a User- friendly: easy implementation of device without special trainings or assistance from experts.

appear to be dominant in the ﬁeld of seizure detection. Nevertheless, deep learning recently started to emerge in
performing seizure classiﬁcation tasks or prediction using the data acquired from wearable devices, where 1D
convolutional neural network and long short-term memory (LSTM) recurrent neural network were applied
frequently. One recent study by Nasseri et al implemented a LSTM model which was initially built from
intracranial EEG (iEEG) data from 7 patients and adaptively trained by data acquired from wearable sensors
developed by Empatica using a transfer learning approach This study addressed the issue of deﬁciency of seizure
data and minimized the amount of time in training LSTM model by taking the advantage of iEEG signal from
both EMU patients and outpatients and reusing it for multimodal signals (ACM, EDA, BVP, Temp). Apart from
that, visual inspection heavily relies on humans’ empirical judgement and knowledge to determine seizure
events, which were used in 2 articles using EEG and ear-EEG based modality (please refer to table 5 [14], [15]).
To establish and validate the feasibility and reliability of using ear-EEG as a seizure detection tool, Zibrandsten’s
group manually inspected the acquired data and performed spectral analysis to compare the gold-standard
vEEG and ear-EEG (Zibrandtsen et al 2017, Zibrandtsen et al 2018).

10

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Algorithm 1a. Summary of input signal modality, extracted feature domain, real-time compatibility and patient
speciﬁcity for each algorithm, speciﬁed by article number. Studies were motor seizure onlya.

a Study conducted under ambulatory settings: [23, 28, 29].

Algorithm 1b. Summary of input signal modality, extracted feature domain, real-time compatibility and patient
speciﬁcity for each algorithm, speciﬁed by article number. Study were focusing on mixed types seizuresa
.

a Study conducted under ambulatory settings: [3, 27, 29].

11

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Table 9. Summary of seizure types, modality, and wearable device.

Seizure type

Motor

Modality

ACM

ACM+EDA

Ear- EEG
EMG / sEMG

Non-Motor

ECG

Mixture

ACM
Ear -EEG
ECG

PPG
EEG
Multimodality

a Study conducted under ambulatory settings: [3, 23, 27]. [28, 29].

Device brand

Smart Monitor ( n=3)
Nintendo (n=1)
Epi-Care Free (n=2)
Shimmer (n = 1)
Other brands (n=1)
Custom-built (n = 1)
Empatica (n = 1)
iCalm (n = 1)
Custom-built
Ictal Care (n=2)
Brain Sentinel (n = 1)
AspireSR (n=1)
Cyberonics (n = 1)

Apple iPod touch (n = 1)
Custom-built (n = 1)
ePatch (n = 2)
Farps (n = 1)
Empatica (n = 1)
Medatec (BrainWalker 3)
Empatica (n=4)
Shimmer (n=1)
LivAssured BV (n = 1)
Nonin (WristOX2) (n = 1)

Studies

[4, 5, 19, 20, 21]
[22, 23]a, [24, 28]a

[7, 9]

[14]
[6, 13, 16]

[17]

[25]
[15]
[1, 11, 12]

[1]
[27]a
[2, 3a, 8, 10, 18, 26, 29a, 30]

3.3. Performance
Table 10(a) reports the distribution of motor seizure studies categorized by different algorithms used, and based
on three key performance metrics, sensitivity, FAR and PPV, whereas table 10b reports performances for
mixture seizure studies. Within the scope of these studies, all 30 of them reported sensitivity as one of the
performance metrics. In addition, 27 studies reported FAR and 15 studies reported PPV, with each study
reporting at least one of the two metrics. To compile results, if the study involved multiple models of the same
algorithm, the best performance is reported. If a model was tested on multiple patient groups, the average
performance is given.

−1, with a range of 0 to 17.7 d

−1 and a standard deviation of 5.41. The only

Across all studies, the range of sensitivity spans from 47% to 100%, FAR varies from 0 to 43.2 d

−1. Regarding threshold-based algorithms, 12 out of 14 studies achieved

−1, and PPV
ranges from 2.15% to 100%. Twenty-two out of the 30 studies achieved sensitivity above 80%, and 21 out of 27
studies reported FAR below 5 d
sensitivity higher than 85%, among which 1/3 reached 100% sensitivity. However, the lowest sensitivity of
threshold-based algorithm was 57.14% from a surface-EMG study which had a small sample size of 7 seizures
from ﬁve patients, resulting in a standard deviation of 0.125. Meanwhile, 8 of the 13 threshold-based studies
reported false alarm rate less than 1 d
threshold-based study (Zibrandtsen et al 2018) that did not use FAR as a metric reported a PPV value of 95%
instead. As for studies using SVM algorithm (please refer to table 5 [1], [7], [9], [20], [24], [25], [28]), ﬁve out of
the seven had sensitivities above 90%, and the other two had sensitivities between 70% and 80%, resulting in a
smaller standard deviation of 0.109. Among the seven studies using SVM as the classiﬁer , more than half
reported FAR less than 1 d
signal, so the standard deviation of FAR in SVM classiﬁers is 19.01. For Random Forests, all three studies (please
refer to table 5 [8], [24], [28]) achieved sensitivities above 80% and one of them scored 100% in both sensitivity
and PPV (Zia et al 2021). Heldberg et al’s study evaluated both Random Forest and kNN models on EDA and
ACM signals: kNN had 89.1% sensitivity and 93.1% speciﬁcity while Random Forest had 87.3% sensitivity and
95.2% speciﬁcity. Studies using event-searching algorithms and visual inspections mostly had low FAR below
1 d

−1 and low sensitivities below 80% (please refer to table 5 [10], [14]).
Figures 2(a) and (b) show the correlation between the two most commonly reported performance metrics
among all studies. The 25 studies that reported both sensitivity and FAR are plotted separately by seizure types
(motor and mixture seizure) as two scatterplots of respective article numbers positioned by both metrics.
Figure 2(a) has a much smaller range of FAR than ﬁgure 2(b), indicating that motor seizure studies tend to have

−1 from Vemdecasteele et al’s study based on PPG

−1, whereas highest FAR is 43.2 d

12

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Table 10a. Summary of three most reported performance metrics for motor seizure studies, categorized by algorithms useda.

Sensitivity

FAR

PPV

Algorithm

Below 80% 80%–95% Above 95%

Above
−1
10 d

1–10 d

−1

Below 1
−1
d

Below
10%

10%–90% Above 90%

Threshold-based

[13]

[6, 19, 21]

[5, 16, 23]a —

[16, 21]

[28]a
SVM
—
Random forest
—
kNN
—
Event searching
[14]
Visual inspection
—
MSPC
Spectral analysis —
—
LSTM

[7, 9, 24]
[24]
[8]
[4]
—
—
—
[29]a

[20]
[28]a
[24]
—
—
—
[22]
—

a Study conducted under ambulatory settings: [23, 28, 29].

—
—
—
—
—
—
—
—

[7]
—
[24]
[4]
—
—
[22]
[29]a

[6, 13,
19,
23]a
[9, 24]
[24]
—
—
[14]
—
—
—

[16]

—

[5]

—
—
—
—
—
—
—
—

[9, 20, 28]a —
—
—
—
—
—
[22]
—

[28]a
—
—
[14]
—
—
—

Table 10b. Summary of three most reported performance metrics for mixtures seizure studies, categorized by algorithms useda.

Algorithm

Sensitivity

FAR

Below 80% 80%–95% Above 95%

Above 10
−1
d

1–10 d

−1

Threshold-based

[2]

[3, 11, 18]a

[15, 27]a

[1]
SVM
—
Random forest
—
kNN
[10]
Event searching
Visual inspection —
—
MSPC
Spectral analysis —
[26]
CNN
[29]a
LSTM

—
[8]
—
—
—
[12]
—
[30]
—

[25]
—
—
—
—
—
—
—
—

[2]

[1]
—
—
—
—
[12]
—
[30]
—

a Study conducted under ambulatory settings: [3], [27], [29].

[11]

—
—
—
—
—
—
—
—
[29]a

Below 1
−1
d

[3a, 15, 18,
27]a

[25]
—
—
[10]
—
—
—
—
—

Below
10%

—

[1]
[8]
[8]
—
—
—
—
—
—

PPV

10%–
90%

[2, 3,
18a

[25]
—
—
—
—
—
—
—
—

Above
90%

—

—
—
—
—
—
—
—
—
—

lower FARs in comparison to mixture seizure studies. In addition, motor seizure studies also had higher
sensitivities (13 out of 15 studies reported sensitivity above 85% and FAR below 5 d
better performance.

−1), achieving an overall

−1. Vandecasteele et al’s study is the only study that used PPG signal alone, and it scored a
−1. There is no study using EDA signal alone for seizure detection yet.

table 11 summarizes the model performance metrics grouped by modality used by each study. Among
studies using single modality, ECG had the tightest sensitivity range of 85.7%–93.1% as well as largest FAR range
from 0.58 to 14.88 d
sensitivity of 33.2% and a FAR of 43.2 d
Studies using EMG and EEG reported sensitivities with a broad distribution from 50% to 100%, and FAR below
−1 on average. Among the 9 multi-modality studies (please refer to table 5 [2], [3], [7], [8], [9], [10], [26], [29],
2 d
[30]), 7 of them have reported sensitivity whereas 4 also reported FAR. Three studies (please refer to table 5 [7],
[8], [9]) used ACM and EDA combined signals and all achieved sensitivity between 85% and 95%, with FARs
below 1 d
and 0.12 d
reported speciﬁcity between 73% and 100%.

−1. The study
using ACM-PPG combined modality had similar performances, with 85% sensitivity
−1 FAR. Cogan et al’s study using EDA, HR, SPO2 and EEG was able to achieve 100% sensitivity and

[3]

Table 12 summarizes the model performance metrics for different seizure types and modalities. Among all
articles, 16 studies involved only motor seizures, including 13 GTCS (generalized tonic-clonic seizure) studies
(please refer to table 5 [4], [5], [6], [7], [9], [13], [14], [16], [19], [20], [21], [22], [28]) and 9 studies based on ACM
modality (please refer to table 5 [4], [5], [19], [20], [21], [22], [23], [24], [28]). These motor seizure studies overall
−1. Speciﬁcally, for studies detecting GTCS, the
achieved sensitivities above 73% and false alarm rates below 3.7 d
−1. The study (please refer to table 5 [17]) on
range of sensitivity is 83.64%–100% and the range of FAR is 0–1.8 d
cardiac-based seizure detection (Boon et al 2015) analyzed only non-motor types of seizure and achieved a
sensitivity of 80% and false positive rates from 0.5 to 7.2 h

−1 for all model settings, among which it reported best

13

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Figure 2. (a) Article distribution based on sensitivity and FAR trade-off for motor seizure studies , with article numbers speciﬁed. (b)
Article distribution based on sensitivity and FAR trade-off for mixture seizure studies, with article numbers speciﬁed.

−1 FAR for the ictal tachycardia (iTC) seizure type. The rest of studies

performance of 100% sensitivity and 0.49 h
(n = 14, listed in ‘Mixture’ section of table 4) tested models on a mixture of motor and non-motor seizures,
including TLE (temporal lobe epilepsy), focal seizures, dialeptic seizures, etc. The mixture studies reported
detection accuracies evaluated on all types of seizure, where the sensitivities ranged from 32% to 100% and the
FAR ranged from 0 to 50 d

−1.

Drawing from table 13 , no signiﬁcant difference in performance between ambulatory and EMU settings was

found. In addition, there seems to be no preference on the selection of feature characteristics and algorithms
under different study settings. However, it would require more evidence to corroborate the above ﬁnding, given
that a limited number of ambulatory studies (please refer to table 5 [3], [23], [27], [28], [29]) were included in this
analysis. Thus, we were ineligible to draw any conclusions in terms of the differences between studies under
ambulatory and EMU settings.

14

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Table 11. Summary of algorithm performance ranges, compared across different modalities.

Modality

Single Modality

Multi-
Modality

Sensitivity

False alarm rate

Speciﬁcity

PPV

ECG
PPG
ACM
EDA
EMG
EEG

ACM, PPG
ACM, EDA
ACM, ECG
EDA, ACC, BVP, EMP
EDA, HR, SPO2

[85.7%–93.1%]
[33.2%]
[87.5%–100%]
—
[50%–100%]
[56%–100%]

[85%]
[83.64%–94.55%]
[71%]
[51.2%]
[100%]

−1]
−1]

[0.58–14.88 d
[43.2 d
[0.2–2 d
—
[0.096–2.25 d
−1]
[0.5–2.25 d

−1]

−1]

−1]
−1]
−1]

[0.12 d
[0.29 d
[17.7 d
—
—

—
—
[99%]
—
[11%–20%]
[87%–100%]

—
[93.1%–95.2%]
—
—
[73%–100%]

[2.15%]
[1.12%]
[40%–100%]
—
—
—

[56%]
[7.5%–8.2%]
—
—
—

Table 12. Summary of algorithm performance group by seizure type.

Seizure Type

Modality

Performance

Sensitivity

False alarm rate

PPV

Article

Motor

Non-motor
Mixture

ACM
EMG
EEG
ACM, EDA
ACM, EDA, BVP, TEMP
ECG

[87.5%–100%]
[76%–100%]
[73.6%–92%]
[83.64%–94.55%]
[93%]
[81.8%–100%]

ACM
ECG
EEG
PPG
ACM, ECG
ACM, PPG
ACM, EDA
EDA, HR, SPO2, EEG
ACM, EDA, BVP, TEMP

[95.23%]
[38.9%–87%]
[95%–100%]
[32%]
[71%]
[86%]
[89.1%]
[57%]
[47%–80%]

a Study conducted under ambulatory settings: [3, 23, 27]. [28, 29].

4. Discussion

−1]
−1]

[0.2–3.7 d
[0–2.24 d
−1]
[0.1 d
[0.2–1.5 d
−1]
[2.3 d
[11.76–172.8 d

−1]

[60.04%–100%]
[11%–20%]
[92.59%]
[39%–51%]
—
−1] —

[4, 5, 19, 20, 21, 22, 23a, 24, 28]a
[6, 13, 16]
[14]
[7, 9]
[29]a
[17]

−1]

−1]
[0.64 d
[0.58–50 d
−1]
[0–0.5 d
−1]
[43.2 d
−1]
[17.7 d
−1]
[0.75 d
—
[0.64 d
[7.3–13.63 d

−1]

−1]

[40%]
[2.15%–86.2%]
—
[1.12%]
[50%]
[49%]
[7.5%]
—
—

[25]
[1, 11, 12, 18]
[15, 27]a
[1]
[2]
[3]a
[8]
[10]
[26, 29a, 30]

Typically, deﬁnitive diagnoses and detection of epileptic seizures, along with some clinical interventions and
treatments, require continuous long-term EEG monitoring of patients, which could be quite expensive,
cumbersome, and signiﬁcantly restrain the mobility of patients, making it infeasible for use outside clinical
settings. Given the fact that the association between physiological signals related to the ANS and certain seizure
manifestations has been well established (Ansakorpi et al 2000, Baumgartner et al 2001, Opherk et al 2002,
Devinsky, 2004), more approachable signals were suggested to address the issues. This scoping review intended
to investigate four research questions we proposed to guide a scoping review of this nascent but active ﬁeld. Our
research questions are answered by collecting, analyzing, and synthesizing data elements that are organized into
ﬁve categories (study, device, signal, algorithm and performance characteristics) and we designed an easy-to-use
data capture form to allow multiple reviewers collect data. Overall ﬁndings from this scoping review show that it
is promising to use non-EEG signals acquired from wearable sensors to detect or even anticipate seizure events
in ambulatory settings. However, we also identiﬁed large variations among reviewed studies in terms of
describing types of seizures and choices of performance metrics to evaluate algorithms. These variations have
made it difﬁcult to compare and synthesize results from different studies. Therefore, our scoping review is best
considered as a snapshot of a ﬁeld of studies that is rapidly advancing and can be used to inform directions of
future research. In the following, we discuss our ﬁndings for each research question, present some
recommendations of essential data elements for future studies to include in their reports, and summarize the
limitation of this scoping review.

15

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Table 13. Performance grouped by study settings (ambulatory, non-ambulatory).

Settings

Sensitivity

Below
80%

80%–95%

Above
95%

Above 10
−1
d

FAR

1–10
−1
d

Below 1
−1
d

Below 10%

PPV

10%–
90%

Above
90%

Ambulatory

[28, 29]

[3, 29]

Non-Ambulatory

[1, 2,
10,
13,
14,
26]

[4, 6], [7–9],
[11, 12],
[18, 19],
[21,
24], [30]

[23,

27, 28]

[5, 15],

[16, 17,
20, 22],
[24,
25]

—

[29]

[3, 23, 27] —

[3, 28]

[28]

[1][2]
[12]
[17]
[30]

[4, 7, 11,
16,
21,
22,
24]

[6, 9, 10,
13, 14],
[15, 18],
[19,
24],
[25]

[1] [8] [16]

[5, 14]

[2, 9],
[18,
20,
22,
25]

4.1. Physiological and mobility signals
Most of the articles focused on GTCS, where the most frequently used signal modalities are ACM and EMG.
Convulsive seizures are accompanied by dramatic motor activity, which have been identiﬁed as the high-risk
factor for physical injury and sudden unexpected death in epilepsy (SUDEP) (Kanner 2011). SUDEP is a
common cause of death in epilepsy, which may be attributed by cardiac and respiratory alternations related with
GTCS (Kanner 2011). One study investigating witnessed cases of SUDEP found out that 12 out of 15 SUDEP
cases followed after a GTCS (Langan et al 2000). This association with SUDEP along with risk of accidental injury
makes a compelling case that convulsive seizures are more critical to detect than non-convulsive seizures (NCS).
NCS may cause less immediate harm to patients but their detection and prompt intervention may prevent any
ensuing injury. Furthermore, NCSs often go undetected, which greatly delays the identiﬁcation and treatment
process. Correspondingly, a wider coverage of the seizure types is critical for seizure management in ambulatory
settings. Based on results from this scoping review, detection of a wide category of seizure types would be best
approached by integrating multiple signal modalities.

4.2. Device characteristics
With respect to the device used among the studies, all wearable devices, except for some custom-made devices
(wearable ear-EEG device), are consumer-graded and easy to access the data via Bluetooth transmission towards
mobile devices or local stations. A stable data transmission is essential for data collection, processing, and model
construction, enabling for implementing real-time detection or prediction systems. Among all the examined
papers, 3 types of devices (Shimmer, SmartWatch, custom-built) were reported to experience disconnections
during the recording stages due to sensor failures or poor connection to base station. Consequently, a more
robust sensor design along with the transmission system warrants further exploration. Regarding the side effect
found in the device, mild to moderate skin irritations are the most frequently reported adverse effects but appear
to be transient. Both research studies (Zibrandtsen et al 2017, Zibrandtsen et al 2018) implementing custom
built wearable ear-EEG device found that one of the major drawbacks was the increasing discomfort on the
external ears when continuously wearing the device. Besides, even though its performance appears identical to
EEG, the burden for specialists in correcting the electrode gels and wearing the device remains unsolved. A softer
earpiece material was suggested to enhance the user experience, but its actual effect remains unknown until
conducting further studies.

None of studies we collected reported any assessment of the wearable devices in terms of their signal quality.

Instead, they documented the encountered data transmission issues and user-experiences of using such
wearable devices. However, quantiﬁcation of signal quality is essential in constructing accurate and realizable
seizure detection models that would reject low quality signal segments. Nasseri et al (Nasseri et al 2020) evaluated
several commercial wearable devices (Empatica E4, Biovotion Everion, Byteﬂies Sensor Dots, Activinsights
GENEActiv watch) regarding their signal quality by calculating respective signal quality indexes. According to
their ﬁndings, the aforementioned commercial devices could generate high-quality signals and the recruited
patients showed strong preferences in wearing wrist-worn devices as opposed to the ones worn on upper arm
during the study period. As mentioned by the study, although the reliability of these devices was established, the
potential for continuous long-term clinical usage remains unknown. In future studies, the integration of
automated signal quality measurements may be helpful in enhancing the performance of real-time detection
models.

16

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

4.3. Algorithm characteristics
Algorithms used to classify signals in the collected studies can be divided into traditional machine learning
(SVM, kNN, random forest, decision tree etc), deep learning (1D CNN, LSTM), and others (threshold-based,
event searching, visual inspection etc). Despite the fact that most of them were implemented off-line with a goal
of differentiating seizure events, some potential was shown for seizure prediction if the signals capture ANS
changes that precede the EEG discharges (Leutmezer et al 2003, Thijs 2019). Mesile al etc constructed 1D CNN
and LSTM based on multimodal signals (EDA, ACM, BVP and temperature) acquired from E4 wristbands to
predict seizure events, demonstrating signiﬁcantly better than chance in 43% of the patients where among them,
mean sensitivity was around 75%. At the same time, the results looked less promising across all the recruited
subjects, with a mean sensitivity around 51%. There certainly exist opportunities for further enhancement in
prediction tasks. Conversely, algorithms designed purely for detection purpose generated much better
performance (sensitivity above 90% with less than 1 FAR/day). Regardless of the success in seizure detection
using non-EEG signals, a large portion of them conducted off-line signal processing and the outcome may differ
when applied in real-time scenarios. Toshitaka’s team developed multivariate statistical process control for
anomaly detection to recognize tonic-clonic and non-convulsive seizures in real-time. HRV features are
extracted from the raw data, and control limits (detection threshold) are determined individually and adjusted
off-line prior to real time implementation. Overall, they reported a high sensitivity (95%) but with high false
−1). Many studies found in this scoping review captured the signals in settings where patients’
alarm rates (14 d
mobility was often restricted. To minimize the FAR and better differentiate seizure events from seizure mimic
events in free-living settings, Jeppesen et al instructed patients to perform exercise tests (biking, cognitive stress
tests), if possible, to mimic the activities which would cause dramatic autonomic changes. In the end, they
reported a sensitivity of 93.1% and FAR of 1 per day. During recording stages, special instructions like requesting
patients to perform physical exercises or allowing patients to engage in their typical activities under careful
supervision could be beneﬁcial in building a more robust classiﬁer with low FAR.

4.4. Performance characteristics
In selection of comparable performance metrics, accuracy is not a valid measure of model performance when
the dataset is imbalanced. Sensitivity, which is the ratio of correct seizure predictions to total seizure
occurrences, provides information about a model’s performance on false negatives (incorrect prediction of
seizure as non-seizure). On the other hand, PPV or precision gives a model’s performance on false positives
(incorrect prediction of non-seizure as seizure) and directly characterizes seizure alert burdens. In the
circumstances of seizure detection, the false negatives are more detrimental. Therefore, the performance
measure of sensitivity is relatively more important. However, reducing false positives is also desirable in
ambulatory seizure detection devices, especially for everyday use, so this feature is captured by FAR in
performance metrics. Some articles also reported speciﬁcity, which is the proportion of actual non-seizure cases
that are correctly identiﬁed, as reﬂected in table 11. Often, sensitivity is found to be closely related to false alarm
rates. Many studies (Poh et al 2012, van Andel et al 2017) have reported higher false alarm rate if a model was
tuned to achieve higher sensitivity. The trade-off between these two metrics needs to be considered based on
context, including seizure types and severity and the anticipated actions to respond to the seizure detection. For
example, higher sensitivity with a compromise in FAR is acceptable in seizures that are easily ignored, whereas
high FAR of low-risk seizures overnight is not desirable in commercial-graded seizure monitoring devices.

−1. The few studies using Random Forests (n = 3) (please refer to table 5 [8],

Among all collect studies, threshold-based algorithms are not only the most widely used, but also the most
common algorithm to have high performance, featuring 12 out of 14 threshold-based models having above 80%
−1 FAR. Among traditional machine learning algorithms, SVM was
sensitivity and 8 out of 13 having below 1 d
the most commonly used, and it also had the best performance, with 71% SVM studies having sensitivity over
90% and 60% having FAR under 1 d
[24], [28]) and kNN (n = 2) (please refer to table 5 [8], [24]) generally achieved good performance (sensitivity
−1), whereas the two studies (please refer to table 5 [26], [29]) using CNN and
above 85% and FAR under 1.2 d
−1) tested
LSTM neural networks had relatively poor performance (sensitivity below 80% and FAR around 10 d
at all types of seizures. Although one study (please refer to table 5 [30]) did achieve sensitivity around 80%, it
failed to retain a low FAR (around 13.63 d
algorithms may not necessarily reﬂect the impertinence of these algorithms in seizure detection/prediction task.
The results may not be representative due to the limited number of studies that have tested these techniques and
the limited number of training samples used to train these neural networks. Besides, the study implementing
LSTM transfer learning algorithm (Nasseri et al 2021) was trained on motor seizure data and reported the
performance separately on motor seizure dataset and on all types of seizures. Its performance on motor seizures
had a much higher sensitivity of 90% with lower FAR 2.45 per day, as compared with the model tested on all
types of seizures which reported a sensitivity of 47% and FAR 7.2 per day. The performance variation was also

−1). However, relatively poor results generated by deep learning

17

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

aligned with the ﬁndings from previous literature (Beniczky et al 2021). The large variation in the performance
may partially be explained by the different extent of manifestations associated with seizure types.

As reﬂected in table 12, more than half of the studies focused on detecting motor seizures and reported an

−1]. Among the 16 motor seizure studies, 13 of
overall high sensitivity of [73.6%–100%] and low FAR of [0–3.7 d
them involved the detection of GTCS and reported even higher sensitivities above 80% and lower FARs below 2
per day. The most common modality used to detect motor seizures is ACM. The 12 studies that included ACM
as single or in multi-modal signals reported many of the highest sensitivities and lowest FARs. Such high
performance of ACM is related to its nature of capturing well motions and activities, and motor seizures are
characterized mainly by motor symptoms in semiological seizure classiﬁcations (Lüders et al 1998). However,
the studies involving detection of both motor and non-motor seizures had a much larger range of sensitivities
and FARs, spanning from 30% to 100% and 0–50 per day respectively. Seven of the 14 mixture studies used
single modality and the other 7 used multi-modalities, but there is no signiﬁcant difference in performance
observed across the different modalities. There is only one study (please refer to table 5 [17]) involving only non-
motor seizures. The study reported high sensitivity above 80% as well as high FAR between 0.5 and 7.2 per hour,
but this result may not be representative due to the limited number of performance metrics included for non-
motor seizures. Based on the included articles, motor seizures are generally more likely to be detected with a
higher sensitivity and lower false alarm rate, especially for GTCS, which indicates that detections for motor
seizure are relatively more mature and well-studied, whereas models for non-motor and mixture seizures
detection requires more research to achieve higher performance.

In addition, studies using different modalities varied in performance as well. Generally, studies based on
modality such as ECG and ACM tend to have higher sensitivity and low FAR, probably due to the reliability of
ECG signals and the close relation between movement and motor seizures. The sensitivity and FAR of studies
using EMG and non-invasive EEG signals alone had very wide ranges, indicating that their performances are
probably more related to the algorithms used to process these signals. PPG signals are usually used in
combination with other modalities such as ACM to achieve best performance. The study that used PPG signal
alone (Vandecasteele et al 2017) had worse-than-chance sensitivity and high FAR, whereas performance got
greatly improved in Arends, et al’s multimodality study using both ACM and PPG. Another commonly used
multimodality pair is ACM and EDA. All three studies based on ACM-EDA combined signals had sensitivity
above 80% and either FAR below 1 d
as single modality, EDA was commonly used in multimodality studies: 7 out of the 9 multimodality studies
included EDA as one of the bio-signals. Some modalities are more applicable to certain types of seizures and the
above data may be confounded by fact where some seizures are easier to detect. For instance, ACM might
outperform other signals, potentially attributed by the fact that it is commonly applied for detecting motor
seizures which intrinsically are easier to detect than non-motor seizures.

−1 or speciﬁcity above 90%. Although no study was included that used EDA

4.5. Recommendations
There exists some variability across different studies in terms of classifying seizure types. The ambiguity and
inconsistency in naming convention and seizure classiﬁcation make it difﬁcult to group the studies by its
targeted seizures and learn about the common modality being used for a speciﬁc seizure type. For instance, some
studies may choose to divide the recorded seizures as convulsive and non-convulsive, while others categorize the
seizures based on its onset, focal versus generalized or even brain region (e.g. temporal lobe epilepsy). The two
different dichotomy systems impose complexity in developing seizure speciﬁc classiﬁers. In addition, we also
noticed some inconsistency among these studies in reporting performance metrics. One study may choose to
report only accuracy of their algorithm, others may use AUC, FAR, making it infeasible to generate a reliable,
comprehensive evaluations towards these algorithms. One guideline (Luo et al 2016) for employing machine
learning models in biomedical data helps to avoid the above issues by listing out minimum performance metrics
required to report: sensitivity, speciﬁcity, positive predictive value, negative predictive value, AUC for
classiﬁcation task. A more standardized seizure types and performance metrics used by the studies would be
useful in assessing and validating the models’ performances for a particular seizure type. Finally, increasing use
of machine learning techniques to detect seizure in ambulatory settings also calls for the research community to
jointly invest in developing a common dataset that can be used to benchmark different algorithms, ensure
reproducibility, and advance the ﬁeld in a measurable and transparent way. Given the potential number of
patients the technology will touch, it is imperative that future studies follow a rigorous approach to develop
algorithms and report results.

4.6. Limitation
This scoping review presents a systematic mapping of the current feasible systems (device+algorithm) for
seizure monitoring in an ambulatory environment. The essential information was extracted from the selected

18

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

articles and recorded in table format to answer the proposed research questions. One limitation of this study is
the lack of critical evaluation of results in the collected articles as the scoping review does not perform any quality
appraisal instead provides comprehensive knowledge for the current ﬁeld. Despite that, we performed
systematic search strategy based on the keywords and utilized the related review papers to identify any pertinent
records, there is still a potential omission of relevant studies. Studies published in other languages were excluded,
and only the peer-reviewed articles were considered in our case, which may limit our understanding in what has
been achieved in this area and conﬁne our analysis only in those scientiﬁc reported journals.

5. Conclusion

To the best of our knowledge, this scoping review is the ﬁrst to summarize research activities regarding wearable
devices for seizure monitoring purpose by capturing a comprehensive list of data elements covering device
brands and modalities, extracted feature characteristics, algorithms, and performances. Based on the studies we
reviewed, non-cerebral physiological signals acquired by wearable devices have exhibited promising results in
detecting or even forecasting seizure occurrences, especially for detecting motor seizures (GTCS, FTBTC).
However, further research is needed to reﬁne the signal analysis techniques and decision algorithms for
accurately detecting non-convulsive seizures and reducing FAR for motor seizures. With the emerging trend of
using various deep learning algorithms to process data from wearable devices, peformance that has been
achieved using traditional machine learning methods is poised to be further boosted. Ultimately, the integration
of machine learning and wearable devices offers a great alternative option of long-term continuous seizure
monitoring under ambulatory settings. Towards such a goal, we anticipate a growing number of studies in
this ﬁeld.

Acknowledgments

We would like to express our gratitude to Dr Syed Bashar for his help in identifying the latest relevant articles
during the scoping review process.

ORCID iDs

Fangyi Chen
Ina Chen
Xiao Hu

https://orcid.org/0000-0003-2926-1063

https://orcid.org/0000-0003-1357-5092
https://orcid.org/0000-0001-9478-5571

References

Ansakorpi H, Korpelainen J T, Suominen K, Tolonen U, Myllylä V V and Isojärvi J I 2000 Interictal cardiovascular autonomic responses in

patients with temporal lobe epilepsy Epilepsia 41 42–7

Arends Jthe Dutch Tele-Epilepsy, C. et al 2018 Multimodal nocturnal seizure detection in a residential care setting Neurology 91 e2010
Baumgartner C, Lurger S and Leutmezer F 2001 Autonomic symptoms during epileptic seizures Epileptic Disord 3 103–16 (https://pubmed.

ncbi.nlm.nih.gov/11679301)

Beniczky S, Conradsen I, Henning O, Fabricius M and Wolf P 2018 Automated real-time detection of tonic-clonic seizures using a wearable

EMG device Neurology 90 e428–34

Beniczky S, Polster T, Kjaer T W and Hjalgrim H 2013 Detection of generalized tonic–clonic seizures by a wireless wrist accelerometer: a

prospective, multicenter study Epilepsia 54 e58–61

Beniczky S, Wiebe S, Jeppesen J, Tatum W O, Brazdil M, Wang Y, Herman S T and Ryvlin P 2021 Automated seizure detection using

wearable devices: a clinical practice guideline of the international league against epilepsy and the international federation of clinical
neurophysiology Clin. Neurophysiol. 132 1173–84

Boon P et al 2015 A prospective, multicenter study of cardiac-based seizure detection to activate vagus nerve stimulation Seizure-Eur. J.

Epilepsy 32 52–61

Cogan D, Birjandtalab J, Nourani M, Harvey J and Nagaraddi V 2016 Multi-biosignal analysis for epileptic seizure monitoring Int. J. Neural

Syst. 27 1650031

Conradsen I, Beniczky S, Wolf P, Jennum P and Sorensen H B 2012 Evaluation of novel algorithm embedded in a wearable sEMG device for

seizure detection Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. 2012 2048–51

Cuppens K et al 2014 Accelerometry-based home monitoring for detection of nocturnal hypermotor seizures based on novelty detection

IEEE J. Biomed. Health Inform. 18 1026–33

Dan J, Vandendriessche B, Paesschen W V, Weckhuysen D and Bertrand A 2020 Computationally-efﬁcient algorithm for real-time absence

seizure detection in wearable electroencephalography Int. J. Neural Syst. 30 2050035
Devinsky O 2004 Effects of seizures on autonomic and cardiovascular function Epilepsy Curr. 4 43–6
Devinsky O, Vezzani A, O’Brien T J, Jette N, Scheffer I E, de Curtis M and Perucca P 2018 Epilepsy Nat. Rev. Dis. Primers 4 18024
Fisher R S et al 2014 ILAE ofﬁcial report: a practical clinical deﬁnition of epilepsy Epilepsia 55 475–82
Halford J J et al 2017 Detection of generalized tonic-clonic seizures using surface electromyographic monitoring Epilepsia 58 1861–9

19

Physiol. Meas. 43 (2022) 07TR01

F Chen et al

Heldberg B E, Kautz T, Leutheuser H, Hopfengärtner R, Kasper B S and Eskoﬁer B M 2015 Using wearable sensors for semiology-

independent seizure detection - towards ambulatory monitoring of epilepsy 2015 37th Annual Int. Conf. of the IEEE Eng. in Medicine
and Biology Society (EMBC)

Hong Seok S, Sung Keun K and Seo-Young L 2016 Inﬂammatory markers associated with seizures Epileptic Disorders 18 51–7
Jeppesen J, Fuglsang-Frederiksen A, Johansen P, Christensen J, Wüstenhagen S, Tankisi H, Qerama E and Beniczky S 2020 Seizure detection

using heart rate variability: a prospective validation study Epilepsia 61 S41–6

Jeppesen J, Fuglsang-Frederiksen A, Johansen P, Christensen J, Wüstenhagen S, Tankisi H, Qerama E, Hess A and Beniczky S 2019 Seizure

detection based on heart rate variability using a wearable electrocardiography device Epilepsia 60 2105–13

Johansson D, Ohlsson F, Krýsl D, Rydenhag B, Czarnecki M, Gustafsson N, Wipenmyr J, McKelvey T and Malmgren K 2019 Tonic-clonic
seizure detection using accelerometry-based wearable sensors: a prospective, video-EEG controlled study Seizure 65 48–54
Joo H S, Han S-H, Lee J, Jang D P, Kang J K and Woo J 2017 Spectral analysis of acceleration data for detection of generalized tonic-clonic

seizures Sensors 17

Kanner A M 2011 Peri-ictal cardiac and respiratory disturbances in epilepsy: incidental ﬁnding or culprit of SUDEP?: peri-ictal cardiac and

respiratory disturbances in epilepsy Epilepsy Curr. 11 16–8

Kusmakar S, Karmakar C K, Yan B, O’Brien T J, Muthuganapathy R and Palaniswami M 2019 Automated detection of convulsive seizures

using a wearable accelerometer device IEEE Trans. Biomed. Eng. 66 421–32

Lacuey N, Hupp N J, Hampson J and Lhatoo S 2019 Ictal central apnea (ICA) may be a useful semiological sign in invasive epilepsy surgery

evaluations Epilepsy Res. 156 106164

Lamberts R J, Thijs R D, Laffan A, Langan Y and Sander J W 2012 Sudden unexpected death in epilepsy: people with nocturnal seizures may

be at highest risk Epilepsia 53 253–7

Langan Y, Nashef L and Sander J W 2000 Sudden unexpected death in epilepsy: a series of witnessed deaths J. Neurol. Neurosurg. Psychiatry

68 211–3

Leijten F and Dutch teleepilepsy consortium 2018 Multimodal seizure detection: a review Epilepsia 59 42–7
Leutmezer F, Schernthaner C, Lurger S, Pötzelberger K and Baumgartner C 2003 Electrocardiographic changes at the onset of epileptic

seizures Epilepsia 44 348–54

Levac D, Colquhoun H and O’Brien K K 2010 Scoping studies: advancing the methodology Implementation Sci. 5 69–69
Lockman J, Fisher R S and Olson D M 2011 Detection of seizure-like movements using a wrist accelerometer Epilepsy Behav. 20 638–41
Lüders H et al 1998 Semiological seizure classiﬁcation Epilepsia 39 1006–13
Luo W et al 2016 Guidelines for developing and reporting machine learning predictive models in biomedical research: a multidisciplinary

view J. Med. Internet Res. 18 e323

Mehndiratta MM and Wadhai SA 2015 Feb International Epilepsy Day - A day notiﬁed for global public education & awareness The Indian

journal of medical research 141 143–133

Meisel C, El Atrache R, Jackson M, Schubach S, Ufongene C and Loddenkemper T 2020 Machine learning from wristband sensor data for

wearable, noninvasive seizure forecasting Epilepsia 61 2653–66

Meritam P, Ryvlin P and Beniczky S 2018 User-based evaluation of applicability and usability of a wearable accelerometer device for

detecting bilateral tonic–clonic seizures: a ﬁeld study Epilepsia 59 48–52

Nashef L, Garner S, Sander L, Fish R and Shorvon S 1998 Circumstances of death in sudden death in epilepsy: Interviews of bereaved relatives

J. Neurol., Neurosurg. Psychiatry 64 349–52

Nasseri M 2020 Signal quality and patient experience with wearable devices for epilepsy management Epilepsia 61 S25–35
Nasseri M et al 2021 Non-invasive wearable seizure detection using long-short-term memory networks with transfer learning J. Neural Eng.

18 056017

Onorati F et al 2017 Multicenter clinical assessment of improved wearable multimodal convulsive seizure detectors Epilepsia 58 1870–9
Opherk C, Coromilas J and Hirsch L J 2002 Heart rate and EKG changes in 102 seizures: analysis of inﬂuencing factors Epilepsy Res. 52

117–27

Page M J et al 2021 The PRISMA 2020 statement: an updated guideline for reporting systematic reviews Bmj 372 n71
Poh M-Z, Loddenkemper T, Reinsberger C, Swenson N C, Goyal S, Sabtala M C, Madsen J R and Picard R W 2012 Convulsive seizure

detection using a wrist-worn electrodermal activity and accelerometry biosensor Epilepsia 53 e93–7

Stafstrom CE and Carmant L 2021 Jun Seizures and epilepsy: an overview for neuroscientists Cold Spring Harb Perspect Med 5 a022426
Schulc E, Unterberger I, Saboor S, Hilbe J, Ertl M, Ammenwerth E, Trinka E and Them C 2011 Measurement and quantiﬁcation of
generalized tonic–clonic seizures in epilepsy patients by means of accelerometry-an explorative study Epilepsy Res. 95 173–83

Tang J et al 2021 Seizure detection using wearable sensors and machine learning: Setting a benchmark Epilepsia 62 1807–19
Thijs R D 2019 The autonomic signatures of epilepsy: diagnostic clues and novel treatment avenues Clin. Autonomic Res. 29 131–3
van Andel J et al 2017 Multimodal, automated detection of nocturnal motor seizures at home: Is a reliable seizure detector feasible? Epilepsia

Open 2 424–31

Vandecasteele K, De Cooman T, Gu Y, Cleeren E, Claes K, Paesschen W V, Huffel S V and Hunyadi B 2017 Automated epileptic seizure

detection based on wearable ECG and PPG in a hospital environment Sensors 17 2338

Velez M, Fisher R S, Bartlett V and Le S 2016 Tracking generalized tonic-clonic seizures with a wrist accelerometer linked to an online

database Seizure 39 13–8

Vieluf S, Reinsberger C, El Atrache R, Jackson M, Schubach S, Ufongene C, Loddenkemper T and Meisel C 2020 Autonomic nervous system

changes detected with peripheral sensors in the setting of epileptic seizures Sci. Rep. 10 11560

van Westrhenen A, De Cooman T, Lazeron R H C, Van Huffel S and Thijs R D 2019 Ictal autonomic changes as a tool for seizure detection: a

systematic review Clin. Autonomic Res. 29 161–81

Yamakawa T, Miyajima M, Fujiwara K, Kano M, Suzuki Y, Watanabe Y, Watanabe S, Hoshida T, Inaji M and Maehara T 2020 Wearable
epileptic seizure prediction system with machine-learning-based anomaly detection of heart rate variability Sensors 20(14) 3987
Zia S, Khan A N, Zaidi K S and Ali S E 2021 Detection of generalized tonic clonic seizures and falls in unconstraint environment using

smartphone accelerometer IEEE Access 9 39432–43

Zibrandtsen I C, Kidmose P, Christensen C B and Kjaer T W 2017 Ear-EEG detects ictal and interictal abnormalities in focal and generalized

epilepsy–a comparison with scalp EEG monitoring Clin. Neurophysiol. 128 2454–61

Zibrandtsen I C, Kidmose P and Kjaer T W 2018 Detection of generalized tonic-clonic seizures from ear-EEG based on EMG analysis

Seizure-Eur. J. Epilepsy 59 54–9

20
