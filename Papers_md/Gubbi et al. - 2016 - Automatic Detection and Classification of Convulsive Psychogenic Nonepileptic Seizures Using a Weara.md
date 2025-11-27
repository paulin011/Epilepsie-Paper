# Gubbi et al. - 2016 - Automatic Detection and Classification of Convulsive Psychogenic Nonepileptic Seizures Using a Weara

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 20, NO. 4, JULY 2016

1061

Automatic Detection and Classiﬁcation of Convulsive
Psychogenic Nonepileptic Seizures
Using a Wearable Device

Jayavardhana Gubbi, Senior Member, IEEE, Shitanshu Kusmakar, Student Member, IEEE,
Aravinda S. Rao, Student Member, IEEE, Bernard Yan, Terence O’Brien, and Marimuthu Palaniswami, Fellow, IEEE

Abstract—Epilepsy is one of the most common neurological
disorders and patients suffer from unprovoked seizures. In con-
trast, psychogenic nonepileptic seizures (PNES) are another class
of seizures that are involuntary events not caused by abnormal elec-
trical discharges but are a manifestation of psychological distress.
The similarity of these two types of seizures poses diagnostic chal-
lenges that often leads in delayed diagnosis of PNES. Further, the
diagnosis of PNES involves high-cost hospital admission and mon-
itoring using video-electroencephalogram machines. A wearable
device that can monitor the patient in natural setting is a desired
solution for diagnosis of convulsive PNES. A wearable device with
an accelerometer sensor is proposed as a new solution in the de-
tection and diagnosis of PNES. The seizure detection algorithm
and PNES classiﬁcation algorithm are developed. The developed
algorithms are tested on data collected from convulsive epileptic
patients. A very high seizure detection rate is achieved with 100%
sensitivity and few false alarms. A leave-one-out error of 6.67%
is achieved in PNES classiﬁcation, demonstrating the usefulness of
wearable device in the diagnosis of PNES.

Index Terms—Accelerometry, epileptic seizure (ES), psy-
chogenic nonepileptic seizure (PNES), support vector machines
(SVMs), wavelets.

I. INTRODUCTION

S EVERAL neurological disorders affect the motor system in

the brain, resulting in deprivation of purposeful movement
and affecting normal interaction with the environment. Epilepsy
is one of the most common neurological disorders, affecting
about 50 million people worldwide [1]. Patients with epilepsy
suffer recurrent unprovoked seizures, which are a transient neu-
rological event caused by excessive or hypersynchronous neu-
ronal network activity in the brain. Seizures carry a signiﬁcant
risk of mortality and morbidity and may on occasions be pro-
longed and require emergency intervention. One of the great-
est disabilities associated with epilepsy is the unpredictability
of seizures—which can occur anywhere and anytime. Seizures
have been characterized by a variety of symptoms [2]. Another

Manuscript received November 20, 2014; revised April 03, 2015; accepted
June 09, 2015. Date of publication June 17, 2015; date of current version July
06, 2016.

J. Gubbi, S. Kusmakar, A. S. Rao, and M. Palaniswami are with the Depart-
ment of Electrical and Electronic Engineering, The University of Melbourne,
Parkville, Vic. 3010, Australia (e-mail: jgl@unimelb.edu; skusmakar@student.
unimelb.edu.au; aravinda@student.unimelb.edu.au; palani@unimelb.edu.au).

B. Yan and T. O’Brien are with the Melbourne Brain Centre, Royal Melbourne
Hospital, Department of Medicine, The University of Melbourne, Parkville, Vic.
3052, Australia (e-mail: bernard.yan@mh.org.au; obrientj@unimelb.edu.au).

Color versions of one or more of the ﬁgures in this paper are available online

at http://ieeexplore.ieee.org.

Digital Object Identiﬁer 10.1109/JBHI.2015.2446539

class of seizures known as psychogenic nonepileptic seizures
(PNES) are involuntary events that pose diagnostic challenges
due to the similarities with epileptic seizures (ES). PNES, com-
monly called pseudoseizures, are a relatively uncommon disor-
der with a prevalence of around 1 to 33 cases per 100 000 and
they account for 5–20% of patients thought to have epilepsy [3].
There is potential for severe harm from the adverse side effects
or teratogenicity of antiepileptic drugs prescribed to PNES pa-
tients [4], as well as morbidity and mortality from intubation
for prolonged seizures [5]. The inaccurate diagnosis may also
result in delayed psychological treatment for the issues under-
lying the attacks and social stigma associated with epilepsy.
Previous research has found that over 75% of patients who are
diagnosed as having PNES on VEM had been referred with
a presumed diagnosis of epilepsy by their Neurologist [6]. It
has been reported that on average, patients experiencing PNES
are not correctly diagnosed until 7.2 years after the manifesta-
tion of the seizures. Such a long delay prior to the diagnosis of
PNES clearly demonstrates the unsatisfactory nature of current
procedures for evaluating this important group of patients [6].

The diagnosis between PNES and ES is the electrical dis-
charge that can be monitored through a video electroencephalo-
gram monitoring (VEM). In-patient VEM is the gold standard
for distinguishing different types of seizures [7]. Although it
has a high yield in diagnosis and management, it is expensive,
time consuming and, labor and resource intensive [8]. It also re-
quires inpatient admission, which adds a further burden on the
healthcare system. Due to the widespread use of VEM machines
for seizure categorization, it is safe to assume that visual cues
(of motor seizures) captured by an expert observer give critical
information on diagnosis and treatment planning in addition to
EEG signals. The videos accompanying EEG clearly show the
manifestation of distinguishable feature in motor activity. Any
neurological problem affecting the motor neurons will result
in the manifestation of the problem in one of the body parts,
speciﬁcally in the limbs that can be captured by an accelerom-
eter sensor. Due to economic feasibility and the tediousness of
VEM, alternate methods are being researched to differentiate
PNES and ES. In our previous work, we have shown that mani-
festation of epileptic and nonepileptic seizures is quite different
in its motor activity [9]. Therefore, a motor activity monitoring
device should be able to distinguish between ES and PNES.

Unobtrusive and ambulatory monitoring get more important
in case of patients who suffer from nocturnal ES. These pa-
tients are highly susceptible to injury or even sudden death as

2168-2194 © 2015 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:20 UTC from IEEE Xplore.  Restrictions apply. 
See http://www.ieee.org/publications standards/publications/rights/index.html for more information.

1062

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 20, NO. 4, JULY 2016

the seizure goes unnoticed to the caregivers, hence making au-
tomated detection of seizures a pivotal and, in many cases, a
life-saving task. Clinical decision making is a hot area
in biomedical engineering, and for automated detection of
seizures, the ﬁrst and the foremost step is the identiﬁcation
of the seizure event and activities which can mimic seizure or
activities of daily living (referred to as normal activity in this
work). The use of accelerometer for the detection of ES has
been reported in [10]. It was found that it was possible to detect
the stereotypical patterns for myoclonic, clonic, and tonic ES
termed as simple motor seizures and distinguish them from nor-
mal movement using 3-D accelerometer attached to four limbs
and chest [10]. This work was extended further in [11], where
four different time-frequency and time-scale methods were in-
vestigated. Cuppens et al. [12] have focused on the identiﬁcation
of normal activity and activity that corresponds to seizure. Re-
sults from the work of Becq et al. [13] is promising, where they
have shown that a high sensitivity and speciﬁcity of 80% and
95%, respectively, can be achieved in the detection of gener-
alized tonic–clonic seizures from accelerometer data based on
a simple entropy feature obtained from the norm of accelera-
tion. However, it can be inferred from the results that there is
a slight overlap between the seizure activities and other motor
manifestations. This can be due to reasons attributed to patient
physiology, placement of the sensor for data collection, and the
type of the activity patient is doing. Another study shows that
the accelerometer can detect the nocturnal frontal lobe seizures
with a high level of sensitivity and speciﬁcity [14], and wearable
accelerometer-based kinematic sensors are successfully used as
a body sensor network for detection of the motor patterns of
ES [15].

Recently, Ungureanu et al. [16] have proposed the use of a
different sensor modality for detection of nocturnal ES, due to
ambiguity on the placement of the accelerometer on the patient
and to identify seizures that do not normally manifest as motor
seizures. However, for unobtrusive and ambulatory monitoring
of patients, the challenge is to have a device and a method
with a minimum number of sensors. This reduces the power
consumption and the patient endurance that multiple sensors
cause. In our work, we have focused only on motor seizures.
Patients with motor ES are under a higher risk of injury or harm
during an ES or PNES event. Therefore, requiring early and
correct diagnosis for directed treatment is essential.

The use of surface electromyography (sEMG) is also reported
in the literature as a viable method for the development of au-
tomated algorithm for detection of seizures. Patel et al. [17]
have shown the use of sEMG data collected in conjugation with
accelerometer data using a wearable sensor. They showed that
sEMG data aid in identiﬁcation and discrimination of activity
of daily living from seizure events. Correct identiﬁcation of
normal or activity of daily living is a critical step for the de-
velopment of an automated algorithm for seizure detection as
many activities of daily living contribute to false alarms. Further,
Conradsen et al. [18] have shown the efﬁcacy of sEMG in the
automated detection of general tonic–clonic seizures with a very
high sensitivity of 100% and a speciﬁcity of 1 false detection
per day.

Seizures can be broadly classiﬁed into two types: convulsive
and nonconvulsive. Convulsive seizures cause involuntary con-
traction of muscles and can be visually observed. Most of the
work reported in the literature as discussed in the above para-
graphs is targeted at detection and classiﬁcation of simple mo-
tor seizures. In our previous work [9], we proposed an approach
based on short-time Fourier transform of the accelerometer data.
The data were recorded using a wrist-worn wired accelerometer
device. It was observed that PNES displays a stable dominant
frequency during the course of a seizure event. However, ES
shows more variation in the evolution of dominant frequen-
cies. Motivated by the initial results, an ambulatory convulsive
seizure monitoring system has been reported in this paper. A
fully automated system for detection and diagnosis of PNES
has not yet been addressed in the literature. In this regard, the
system employs a wrist-worn accelerometer system that records
motor activity. A new algorithm for detection and classiﬁcation
of convulsive seizures is proposed. The novel system is imple-
mented using a commercially available hand-held device and
tested on patients undergoing VEM. The main contributions of
this study are summarized as follows.

1) Accurate detection of PNES based on the occurrence of
seizure is critical for avoiding unnecessary delay in treat-
ment. Correct diagnosis of PNES is reported to be delayed
by 7.2 years on average. An automated system has been
developed for identiﬁcation of PNES in convulsive pa-
tients using limb motion analysis.

2) Continuous and unobtrusive monitoring is a challeng-
ing task due to the amount of data that are collected.
A new method for accurately identifying seizures from
accelerometer signal is proposed. The algorithm has the
ability to detect seizure-like activity that is present hidden
inside vast amounts of normal data.

3) A new classiﬁcation algorithm has been proposed for clas-
sifying ES and PNES using time-frequency analysis. The
algorithm is tested with good results on patient data col-
lected in a hospital setting.

II. METHOD

The proposed system consists of two stages, seizure detection
and seizure classiﬁcation, as shown in Fig. 1. The wrist-worn
device is mounted on the patient continuously for several days
when the patient is under observation in the VEM system. The
movement data are collected uninterrupted over this period other
than during the device change over period that lasts a few min-
utes. Due to the large volume of data collected, an algorithm for
detecting seizures accurately is developed in the ﬁrst stage us-
ing time-domain features and k-means clustering. In the second
stage, seizure activities are classiﬁed into ES or PNES with the
help of discrete wavelet transform (DWT) and SVMs. In this
section, the details are presented.

A. Data Collection and Processing

An ambulatory wireless system has been proposed that al-
lows continuous monitoring and in the subject’s natural setting.
A smart-device application was developed for collecting the

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:20 UTC from IEEE Xplore.  Restrictions apply. 

GUBBI et al.: AUTOMATIC DETECTION AND CLASSIFICATION OF CONVULSIVE PSYCHOGENIC NONEPILEPTIC SEIZURES

1063

Fig. 1.
Flowchart of the proposed method. The method consists of four stages of processing. In the ﬁrst stage, data are collected from a wrist-worn accelerometer.
In the second stage, a ﬁlter that eliminates small movements has been implemented as on-device processing. Seizure detection is the third stage comprising of four
steps: activity ﬁlter, time ﬁlter, extraction of time-domain features, and clustering of detected features. In the ﬁnal stage, the seizure is classiﬁed as PNES or ES.
For classiﬁcation of events as PNES of ES, an initial preprocessing of the signals is performed on the signals from seizure detection stage, followed by extraction
of wavelet features (db3, db5, coif3, and sym4) and then classiﬁcation using k-means and SVMs.

TABLE I
OVERALL NUMBER OF PATIENTS WHO HAD SEIZURES DURING THE MONITORING DURATION WITH THE NUMBER OF ES, PNES, AND BOTH ES
AND PNES PATIENTS

Overall

ES

PNES

Both ES and PNES

Patients
Observed events
Age
Male
Female
Duration of events (sec)

27
85
34.44 ± 13.34
8(29.6% )
19(70.30% )
117 ± 123

10
21
32.80 ± 13.40
5(50.00% )
5(50.00% )
115 ± 111.6

3
13
39.33 ± 18.61
0.00
3 (100%)
224 ± 203.43

1
–
30.00 ± 0.00
0.00
1 (100%)
–

A total of 14 patients had convulsive events. Only patients with convulsive events are shown with patient age
and event duration represented as mean ± standard deviation. Number of males and female patients and their
respective percentages shown in brackets for each category.

movement data. Apple iPod Touch with an accelerometer sen-
sor was used for all our experiments. Two iPods (one for each
hand) were attached ﬁrmly to the patient’s wrists with elas-
tic armbands to prevent unintended movements. Each device
consisted of an MEMS accelerometer (±2.5 g). A simple ﬁl-
ter to detect activity was used in order to conserve energy. The
device was changed every 12 h due to battery drainage. The
raw accelerometer data were stored using ﬂash memory on the
device and later transferred to the computer for analysis. The
sampling frequency of the data collected was 50 Hz and each
packet contained values along three axes and a time stamp. The
data were collected during 2012 and 2013 among patients in
the epilepsy video telemetry unit at the Royal Melbourne Hos-
pital in Melbourne, Australia, who experienced motor seizures
during hospitalization. Human Research Ethics Committee ap-
proval was obtained from the Royal Melbourne Hospital (HREC
Project 300.259). The study was conducted in keeping with the
regulations established by the hospital. During the stay in the
hospital, the patients underwent VEM continuously for at least
three days, and at the same time, the patients had an accelerom-
eter device ﬁtted ﬁrmly to both their wrists. The devices were
time synchronized with VEM setup in order to ensure exact
comparison and analysis, by manually autoupdating the time on

both the devices from same network. A lag of few milliseconds
in registrations of VEM and accelerometer device is permis-
sible according to clinical experts. Moreover, the EEG techni-
cians manually annotate the accelerometer data for the different
seizure types. The EEG technicians performed the annotation
without any automated signal processing. The annotation was
performed by visual assessment of the accelerometer data using
MATLAB. The EEG technicians reported that similar clues of
seizure-like activity is present on accelerometer data as seen
on EEG during VEM. Patients were excluded from this study
for three reasons: 1) if the seizures were absent (i.e., no move-
ment); 2) if they suffered from signiﬁcant underlying psychoses
(preventing informed consent); and 3) the monitoring was in-
tracranial. Summary of the data collected is shown in Table I.
Out of a total 57 subjects recruited, 27 patients had seizures dur-
ing VEM recording. Using the VEM, 85 events were observed
that included 34 convulsive events (14 patients) and 51 noncon-
vulsive events (13 patients). This study focuses on convulsive
patients only as motor activity monitoring is possible only if it
manifests on a body part; hence, convulsive events are consid-
ered. Out of 14 convulsive patients, ten epileptic patients and
three nonepileptic patients were encountered. One patient had
both epileptic and nonepileptic seizure events. A total of 21 ES

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:20 UTC from IEEE Xplore.  Restrictions apply. 

1064

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 20, NO. 4, JULY 2016

Fig. 2. Example of k-means clustering using standard deviation, zero crossing,
and power of the resultant acceleration signal. ◦ indicates normal activities and
(cid:2) indicates seizure events for patient no. 1. From the ﬁgure, it is clear that
standard deviation, zero crossing, and power are sufﬁcient to cluster the events
as normal or seizure-like events.

events and 13 PNES events were identiﬁed using VEM. Based
on the feedback from the specialists, a minimum event length
of 20 s is considered in this study as an event. This resulted
in a reduction of the number of events captured by the device,
and there are 14 ES events and ﬁve PNES events for detection
and classiﬁcation. Although the number of events is lesser, it
should be noted that the analysis is performed on events of dif-
ferent window lengths (5 s in classiﬁcation stage) resulting in a
sizeable number of samples. In effect, eight convulsive patients
are available for analysis with a total of nineteen events. The
mean duration of ES and PNES events were 115 and 224 s,
respectively. More details about the data can be seen in Table I.

B. Detection of Seizure Events

(cid:2)

Accurate detection of seizure events is the ﬁrst step in analysis
of the motor movement that comprises of vast amounts of data.
A simple time- and frequency-domain approach is proposed for
detection of seizure activity. There are three possibilities of out-
put at this stage: 1) no activity; 2) normal arm movements; and
3) seizure activity. The resultant signal used at the ﬁrst stage
x2 + y2 + z2. The resultant is then
is calculated using R =
preprocessed using a simple activity ﬁlter that declares all sig-
nals less than 0.2 g as no activity or normal activity. The value
of 0.2 g is empirically chosen and is based on the lower bound
of the collected seizure data. Although this value is heuristical,
logically it is fair to accept it due to the nature of the phys-
iology of seizures. Followed by the use of the threshold, the
signal of 20-s length with 50% overlap is ﬁltered using a sixth-
order Butterworth bandpass ﬁlter with 2 and 25 Hz as cutoff
frequencies. This will ﬁlter all spurious spikes and some of the
controlled arm movements, which is not the nature of ES. Cup-
pens et al. [14] have shown the use of such preprocessing steps,
where they have used low-pass ﬁlter with cutoff frequency of
47 Hz, whereas in our work, we have focused on a particular fre-
quency range based on our observations of dominant frequency
of typical seizure events from our previous work [9]. Seizure
activities of minimum length of 20 s are considered in this work,
and hence, the choice of 20 s windows is made. A fast Fourier

Fig. 3. Three-level Wavelet decomposition. S is the input signal. H is the
high-pass ﬁlter and L is the low-pass ﬁlter. ↓ 2 indicates downsampling by a
factor of 2. ai is the approximate coefﬁcient and di is the detailed coefﬁcient.
In the proposed work, six-level wavelet decomposition is performed, resulting
in an approximate coefﬁcient along with six detailed coefﬁcients.

transform (FFT) of the ﬁltered signal is calculated by dividing
the 20-s window into 20 blocks of 1 s each. The magnitude
of the dominant peak along with the corresponding frequen-
cies is calculated. A detailed analysis of the mean and standard
deviation of the magnitude and frequency is performed. It is
found that the normalized peak magnitude of the data during
the seizure has a lower bound of 0.009, and the upper bound
on the peak magnitude during normal activity is several order
lesser than 0.009. Hence, it is chosen as the threshold in our
activity ﬁlter. Further, it is observed that for at least 10 s, out
of the 20-s window, the activity is high in magnitude during the
seizure, which is not the case in majority of the normal activity.
This will ensure that all subtle movements are excluded from
seizure-like activities, hence the name activity ﬁlter. A simi-
lar observation has been made by Cuppens et al. [12] in their
very recent work, where they have reported that activities that
manifest for lesser than 10 s are most likely normal nocturnal
movements. After preprocessing, the ﬁltered data now contain
normal activity that has signiﬁcant acceleration in addition to
seizures. As mentioned earlier, only events that have a minimum
duration of 20 s are considered in our work. Followed by the
activity ﬁlter, we use the time ﬁltering to remove normal and
seizure events that have duration of less than 20 s. At the end
of time ﬁltering, we are left with arm movements that comprise
of normal events and seizure events with the number of nor-
mal activities signiﬁcantly higher than seizure activities. The
thresholds are justiﬁed as we are not eliminating any seizure-
like activity but only focus on removing very obvious normal
movements. In order to extract only seizure events from this
biased set, k-means clustering is employed on time-domain fea-
tures that are extracted. The 15 time-domain features extracted
include signal power, zero crossings, energy, measures of cen-
tral tendency (mean, median, mode), measures of dispersion
(interquartile range, standard deviation, amplitude), skewness,
kurtosis, and entropy (Shannon, log energy, norm, threshold).
Features were calculated for signals corresponding to x-, y-,
and z-axes of accelerometer and also for the resultant signal R.
In total, we had a feature set comprising of 60 features. Out of
the 60 time-domain features, signal power, zero crossing, and
standard deviation were selected as key features based on fea-
ture evaluation using variance as the criterion in agreement with
Cuppens et al. [14]. For each subject, the duration of events is
represented by time window T = {t1, t2, . . . , tn |tI = 1 s}. The
feature vector for a particular subject comprising of tn windows
is generated using the 60 features. Let U = [u1, u2, . . . , u60]

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:20 UTC from IEEE Xplore.  Restrictions apply. 

GUBBI et al.: AUTOMATIC DETECTION AND CLASSIFICATION OF CONVULSIVE PSYCHOGENIC NONEPILEPTIC SEIZURES

1065

Fig. 4.
Six levels of wavelet decomposition shown for (a) PNES and (b) ES
during respective events. In each of the graphs, the ﬁrst subgraph shows the in-
put acceleration signals corresponding to x-, y-, and z-axes and the subsequent
subgraph show the resultant axis derived from x-, y-, and z-axes. The subse-
quent graphs show the six levels of detailed coefﬁcients and an approximate
coefﬁcient. The results were obtained using the db5 coefﬁcient.

represent the feature vector for a particular subject and the cor-
responding event. This is reduced to V = [v1, v2, v3], where v1,
v2, and v3 correspond to the power, zero crossing, and standard
deviation of the resultant.

k-means [19] is an unsupervised clustering algorithm that
classiﬁes the multivariate data into k clusters, where the number
of clusters k is known a priori. The intuition is to identify k
centroids based on the input data. The k centroids then form
the centroid of each cluster. Ideally, the centroids must be far
apart from each other, and the data points are associated with
one of the nearest k centroids. The k-means clustering is an
iterative algorithm, and thus, the procedure of newly formed
clusters with k centroids is iterated until convergence (cluster
centroids become ﬁxed and data points associated also become
ﬁxed). This can be written as minimizing an objective function

Fig. 5. Resultant accelerometer signal and evolution of dominant frequency
during (a) PNES and (b) ES from [9].

as

Q = arg min

k

k(cid:3)

n(cid:3)

j =1

i=1

(cid:4)xi − cj (cid:4)2

(1)

where xi are the n data points and cj are the k cluster centroids.
In the present scenario, the data contain n observations for
a single subject. Each observation consists of three features.
These features must be divided into two clusters: normal events
and seizure events. The k-means clustering will divide the input
vectors into a larger group of normal events and another smaller
group of seizure events as shown in Fig. 2. In Fig. 2, ◦ represents
the normal activity and (cid:2) represents the seizure events. As can
be inferred from Fig. 2, the data are clearly divided into two
distinct clusters and all the seizure events correspond to outliers
in our data.

C. Classiﬁcation of Seizure Into Epileptic and Pseudo
Nonepileptic Events

Our initial work as a proof of principle [9] demonstrated the
feasibility of differentiating ES and PNES using a single-stage
frequency analysis. Using a wired accelerometer and contin-
uous collection of the data, the collected acceleration signals
were analyzed using a Fourier transform and the ﬁrst dominant
peak was analyzed. It was found that the variation of the ﬁrst

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:20 UTC from IEEE Xplore.  Restrictions apply. 

1066

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 20, NO. 4, JULY 2016

TABLE II
EVENT DETECTION RESULTS FOR EIGHT CONVULSIVE PATIENTS, FOR A TOTAL OF 19 EVENTS CAPTURED USING THE WRIST-WORN ACCELEROMETER DEVICE

Patient
Number

Event
Number

Observed start
time (hh:mm:ss)

Predicted start
time (hh:mm:ss)

Start time
error (sec)

Observed
duration (sec)

Predicted
duration (sec)

Duration Error
(sec)

1

2
3

4

5

6
7
8

1
2
3
4
5
6
1
1
2
1
2
3
1
2
3
4
1
1
1

16:04:00
00:33:00
07:23:49
10:03:00
14:42:00
16:12:00
04:50:35
15:23:53
03:07:12
15:08:38
15:32:33
11:52:15
21:15:00
11:20:00
12:20:00
12:35:00
00:45:00
12:06:09
23:40:00

16:04:31
00:33:07
07:23:47
10:03:37
14:42:41
16:12:33
04:50:46
15:22:35
03:06:46
15:08:09
15:32:27
11:51:24
21:16:49
11:21:19
12:18:00
12:32:50
00:48:28
12:06:26
23:45:04

+31
+07
−02
+37
+41
+33
+11
−78
−26
−29
−05
−51
+109
+79
−120
+130
+208
+17
+304

66
66
58
68
52
51
105
83
60
156
115
68
434
495
660
363
500
70
85

60
48
49
59
51
47
44
32
42
34
58
32
307
498
269
369
64
59
58

−6 (9.1%)
−18 (27.2%)
−9 (15.5%)
−9 (13.2%)
−1 (1.9%)
−4 (7.8%)
−61 (58.1%)
−51 (61.4%)
−18 (30.0%)
−125 (78.2%)
−57 (49.5%)
−36 (52.9%)
−125 (29.2%)
+3 (0.8%)
−391 (59.2%)
−6 (1.6%)
−449 (89.8%)
−11 (15.7%)
−27 (31.7%)

The table highlights the observed start time (with respect to VEM), accelerometer capture start time, and error. Similarly, the event
duration observed (with respect to VEM), accelerometer data, and error are shown.

TABLE III
PERFORMANCE OF THE PROPOSED EVENT DETECTION ALGORITHM

Patient No.

Sensitivity

Speciﬁcity

Accuracy

1
2
3
4
5
6
7
8

100
100
100
100
100
100
100
100

96.15
58.82
93.94
91.30
100.00
73.33
72.62
100.00

96.88
59.22
94.12
92.30
100.00
75.00
72.94
100.00

The table shows the results of seizure event detection
approach for eight patients that comprised of 19 con-
vulsive events.

dominant frequency between patients with ES and PNES var-
ied considerably with high coefﬁcient of variation in dominant
frequency of ES events as compared to PNES events. In con-
trast to our earlier work, we use wireless accelerometer that can
be worn without any hindrance to normal activity. Further, due
to the nature of data preprocessing, the data collected are ac-
curate but sparse. As a result, the algorithm based on FFT [9]
proposed earlier is not robust. In order to gain convenience in
data collection, some sacriﬁce is necessary in the quality of the
data collected, but we attempt to compensate it by proposing
a new algorithm based on time-frequency analysis and SVM
classiﬁer. The classiﬁer is build using ﬁvefold cross-validation,
where four folds are used for training the classiﬁer and ﬁfth fold
is used to test the model. This approach results in a completely
automated system that can detect seizure events and diagnose
PNES accurately that is a step further to what has been reported
earlier [9].

1) Extraction of Wavelet Features: Analysis of nonstation-
ary functions can be performed using mathematical functions

that allow simultaneous localization of interesting patterns in
time and scale. Wavelets belong to this class of functions and
they decompose the data into different frequency bands. Each
component is analyzed with a resolution matched to its scale.
They also offer important properties such as linearity and or-
thogonality that can be used for implementing the algorithm on
wearable devices that are resource hungry and work in real time.
The DWT further enhances their use in DSP chips by operating
on input data vectors whose length is an integer power of two.
A DWT is calculated by ﬁltering followed by down sampling
by a factor of 2 as shown in Fig. 3. It is clear from Fig. 3 that
wavelets provide multiscale representation of the input signal.
In Fig. 3, the approximate coefﬁcient aj and detailed coefﬁcient
dj are calculated using (2) and (3), where h and l are high-pass
and low-pass ﬁlter coefﬁcients, respectively:

aj +1[p] =

dj +1[p] =

n =∞(cid:3)

n =−∞
n =∞(cid:3)

n =−∞

l[n − 2p]aj [n]

h[n − 2p]aj [n].

(2)

(3)

Several mother wavelets with different orders were analyzed.
Finally, a small subset of mother wavelets including daubechies
(db3, db5), coiﬂets (coif3), and symlet (sym4) were empiri-
cally chosen for detailed analysis and validation of the proposed
method. Fig. 4 shows the decomposed signal with six detailed
coefﬁcients and one approximate coefﬁcient. Using power as the
criterion, detailed coefﬁcients at level 2 (d2), 3 (d3), and 4 (d4)
were chosen for further analysis. In addition, the approximate
coefﬁcients (a6 ) after six-level wavelet decomposition was used.
The entropy and power of each 5-s window (with 50% overlap)
in a seizure were calculated for d2, d3, d4, and a6. The coef-
ﬁcient of variation of power and entropy for each event was

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:20 UTC from IEEE Xplore.  Restrictions apply. 

GUBBI et al.: AUTOMATIC DETECTION AND CLASSIFICATION OF CONVULSIVE PSYCHOGENIC NONEPILEPTIC SEIZURES

1067

work consistently and also the data characteristics are not efﬁ-
ciently utilized. Density-based multiscale condensation strategy
has been used in this work [20] by using a derived attribute of
mean and standard deviation of the data. CCIA generates ´k clus-
ters where ´k > k. The idea of the algorithm is to merge nearby
clusters from the pool of ´k clusters based on Euclidian distance
between cluster centers. The new cluster centers formed by this
procedure will be used as initial cluster centers for the k-means
algorithm. The same procedure is repeated for d2, d3, d4, and
a6.

3) Classiﬁcation Using SVMs: SVMs [21] are a class of
trained models used in data analysis and pattern recognition
for classiﬁcation and regression. The models are learned using
the supervised learning where the input data and output class
are labeled. Internally, the SVMs use the Kernel Methods [22],
[23], where the algorithm depends only on the inner-product
of the data. Consequently, the properties of the kernel func-
tion determines the dot product of the data. This inner-product
feature space is a high-dimensional space and SVMs can ef-
fectively generate nonlinear decision boundaries to generate
accurate classiﬁcation results. The kernel functions are also ad-
vantageous to handle data that do not have ﬁxed vector structure.
In this work, radial basis function (RBF) kernel is used. The RBF
kernel for two input data samples is given by

K(x, x(cid:6)) = exp

(cid:4)

−

(cid:5)

(cid:4)x − x(cid:6)(cid:4)2
2
2σ2

(4)

where x and x(cid:6) are input data points and σ is the bandwidth of the
RBF kernel. In this work, based on empirical evidence during
the training stage, the RBF kernel parameters (C, γ) were set
to C = 1 and γ = 0.25, where C is the penalty parameter and
γ = 1
2σ 2 . The parameter C is a penalty term used in optimization
of decision boundary and controls the classiﬁcation error [24].

III. RESULTS AND DISCUSSION

The mode of data collection and the device used in this work
is different as explained earlier. Hence, as a ﬁrst evaluation,
we verify our results with Bayly et al. [9] who have used ﬁrst
dominant frequency within 2.56-s windows for the length of the
event. In the context of this work, it should be noted that the
data collection is using a sensor with lower sensitivity and there
is a ﬁlter within the device that suppresses very low strength
signal. This will allow us to ensure that the basic characteristic
of the signal that is needed to classify ES and PNES is not lost.
The results of dominant frequency evolution during the events
are shown in Fig. 5. As can be seen, consistent with the earlier
result, we observe little change in the case of PNES and vast
change in the case of ES. Based on this, we employed more
sophisticated signal-processing techniques to extract features
with higher discriminating capability. As shown in Table IVc,
leave-one-out error (LOOE) of 6.67% and an overall accuracy
of 92% are achieved in PNES classiﬁcation using the approach
presented in this work, which shows a vast improvement over
the previous results [9].

The results of the event detection stage are summarized in
Table II. All events are detected out of the 19 analyzed events.

Fig. 6. Results of event detection stage for patient no. 1. (a) Data with normal
activity and ES event (top most), result of activity ﬁltering (second subplot),
and result of time ﬁltering (third subplot). (b) Normal activity (enlarged view
of the left most activity from (a), third subplot). (c) Seizure-like event (enlarged
view of the right most activity from (a), third subplot).

calculated and used as a feature for classiﬁcation. This resulted
in a feature vector of length of eight made up of coefﬁcients of
variation in power (d2, d3, d4, a6) and entropy (d2, d3, d4, a6).
2) Classiﬁcation Using Unsupervised Learning: Based on
our earlier work [9], we hypothesize that the coefﬁcient of vari-
ation of power and entropy in different frequency bands should
provide the basis for classifying PNES from ES. As reported
by Bayly et al. [9], PNES exhibit stable dominant frequency
during the course of the event (leading to low coefﬁcient of
variation) as against evolving dominant frequency in ES (lead-
ing to the high coefﬁcient of variation). In order to achieve
this, k-means has been used with a cluster center initializa-
tion algorithm (CCIA) [20]. Due to the nature of k-means by
using the random centroid initialization, the algorithm fails to

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:20 UTC from IEEE Xplore.  Restrictions apply. 

1068

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 20, NO. 4, JULY 2016

TABLE IVA
RESULTS OF EVENT (PNES) CLASSIFICATION

Data

Mother
Wavelet

Accuracy

Sensitivity

Speciﬁcity

f-score

LOOE

db3

db5

coif3

sym3

Resultant
X
Y
Z
Resultant
X
Y
Z
Resultant
X
Y
Z
Resultant
X
Y
Z

84.00 ± 26.08
68.00 ± 22.80
76.00 ± 21.91
84.00 ± 16.73
92.00 ± 10.95
68.00 ± 17.89
84.00 ± 8.94
88.00 ± 10.95
76.00 ± 16.73
68.00 ± 10.95
92.00 ± 10.95
84.00 ± 8.94
84.00 ± 16.73
80.00 ± 14.14
88.00 ± 10.95
84.00 ± 8.94

80.00 ± 32.60
65.00 ± 28.50
70.00 ± 27.39
80.00 ± 20.92
90.00 ± 13.69
65.00 ± 22.36
80.00 ± 11.18
85.00 ± 13.69
75.00 ± 17.68
70.00 ± 11.18
90.00 ± 13.69
80.00 ± 11.18
85.00 ± 13.69
85.00 ± 13.69
85.00 ± 13.69
80.00 ± 11.18

100.00 ± 0.00
80.00 ± 44.72
100 ± 0.00
100.00 ± 0.00
100.00 ± 0.00
80.00 ± 44.72
100.00 ± 0.00
100.00 ± 0.00
80.00 ± 44.72
60.00 ± 54.77
100.00 ± 0.00
100.00 ± 0.00
80.00 ± 44.72
60.00 ± 54.77
100.00 ± 0.00
100.00 ± 0.00

0.85 ± 0.26
0.73 ± 0.22
0.79 ± 0.23
0.88 ± 0.14
0.94 ± 0.08
0.74 ± 0.20
0.89 ± 0.06
0.91 ± 0.08
0.83 ± 0.13
0.78 ± 0.08
0.94 ± 0.08
0.89 ± 0.06
0.89 ± 0.11
0.87 ± 0.09
0.91 ± 0.08
0.89 ± 0.06

13.33
23.33
16.66
13.33
6.66
30
13.33
10
20
26.66
6.66
16.66
13.33
20
13.33
16.66

k -means classiﬁer performance using sub-band power as the feature for different mother wavelets. LOOE
(Leave one out error).

TABLE IVB
RESULTS OF EVENT (PNES) CLASSIFICATION

Data

Mother
Wavelet

Accuracy

Sensitivity

Speciﬁcity

f-score

LOOE

db3

db5

coif3

sym3

Resultant
X
Y
Z
Resultant
X
Y
Z
Resultant
X
Y
Z
Resultant
X
Y
Z

76.00 ± 8.94
68.00 ± 17.89
88.00 ± 10.95
84.00 ± 16.73
80.00 ± 0.00
72.00 ± 10.95
76.00 ± 16.73
84.00 ± 8.94
76.00 ± 8.94
88.00 ± 10.95
80.00 ± 20.00
68.00 ± 10.95
72.00 ± 10.95
56.00 ± 21.91
92.00 ± 10.95
76.00 ± 8.94

75.00 ± 0.00
65.00 ± 22.36
85.00 ± 13.69
85.00 ± 22.36
75.00 ± 0.00
70.00 ± 11.18
70.00 ± 20.92
85.00 ± 13.69
70.00 ± 11.18
90.00 ± 13.69
80.00 ± 20.92
60.00 ± 13.69
65.00 ± 13.69
50.00 ± 17.68
90.00 ± 13.69
80.00 ± 11.18

80.00 ± 44.72
80.00 ± 44.72
100.00 ± 0.00
80.00 ± 44.72
100.00 ± 0.00
80.00 ± 44.72
100.00 ± 0.00
80.00 ± 44.72
100.00 ± 0.00
80.00 ± 44.72
80.00 ± 44.72
100.00 ± 0.00
100.00 ± 0.00
80.00 ± 44.72
100.00 ± 0.00
60.00 ± 54.77

0.84 ± 0.05
0.74 ± 0.20
0.91 ± 0.08
0.88 ± 0.14
0.86 ± 0.00
0.80 ± 0.09
0.81 ± 0.14
0.89 ± 0.06
0.82 ± 0.09
0.92 ± 0.07
0.85 ± 0.15
0.74 ± 0.10
0.78 ± 0.10
0.64 ± 0.19
0.94 ± 0.08
0.84 ± 0.05

20
30
13.33
23.33
16.66
23.33
20
13.33
20
13.33
23.33
30
20
70
13.33
23.33

k -means classiﬁer performance using subband entropy as the feature for different mother wavelets.

The predicted start time is also fairly accurate other than for
patient no. 6. In terms of the duration of prediction, a mixed set
of result is reported. The goal at this stage was to detect the event,
and the duration of the event is not a major hurdle. By designing
a simple extension ﬁlter, it is possible to get more accurate event
duration if required. Table III gives the accuracy, sensitivity, and
speciﬁcity obtained by the proposed event detection scheme. As
intended, the sensitivity of the proposed algorithm is excellent
with 100% results. Although some false alarms are detected in a
few patients, a closer analysis revealed very low intensity single
seizure as the primary reason for these patients. However, the
threshold chosen ensures that the events are not missed, which
is the original goal.

Fig. 6 shows stepwise result of event detection stage for pa-
tient no. 1. The top most plot in Fig. 6 show a section of the data
with normal activity and seizure-like activity. At this stage, the

algorithm should output only seizure like activity. As explained
in methodology, an activity ﬁltering is performed and the results
are shown in Fig. 6(a), middle. As can be seen, low intensity
activities that involve normal movement are ﬁltered. Time ﬁlter-
ing is performed and the output is shown in Fig. 6(a), bottom. It
is clear that only the event (on extreme right) and some high in-
tensity normal activity (extreme left) are remaining at this stage
that needs to be classiﬁed. Finally, k-means clustering is used
to detect events of interest that classiﬁes normal activity [see
Fig. 6(b)] and seizure events [see Fig. 6(c)].

Tables IVa–IVd summarize the results of event classiﬁcation
stages using different feature–classiﬁer combinations for vari-
ous mother wavelets and accelerometer axis. f -score and LOOE
are also reported. As can be seen from Table IVc, SVM using
db5 mother wavelet and subband power as the feature results
in the best f -score and lowest LOOE consistently than other

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:20 UTC from IEEE Xplore.  Restrictions apply. 

GUBBI et al.: AUTOMATIC DETECTION AND CLASSIFICATION OF CONVULSIVE PSYCHOGENIC NONEPILEPTIC SEIZURES

1069

TABLE IVC
RESULTS OF EVENT (PNES) CLASSIFICATION

Data

Mother
Wavelet

Accuracy

Sensitivity

Speciﬁcity

f-score

LOOE

db3

db5

coif3

sym3

Resultant
X
Y
Z
Resultant
X
Y
Z
Resultant
X
Y
Z
Resultant
X
Y
Z

84.00 ± 26.08
80.00 ± 24.49
88.00 ± 26.83
88.00 ± 17.89
92.00 ± 10.95
92.00 ± 10.95
92.00 ± 10.95
88.00 ± 17.89
84.00 ± 16.73
72.00 ± 17.89
92.00 ± 10.95
92.00 ± 10.95
84.00 ± 16.73
80.00 ± 14.14
92.00 ± 10.95
88.00 ± 10.95

80.00 ± 32.60
75.00 ± 30.62
85.00 ± 33.54
85.00 ± 22.36
90.00 ± 13.69
90.00 ± 13.69
90.00 ± 13.69
90.00 ± 13.69
85.00 ± 13.69
75.00 ± 17.68
90.00 ± 13.69
90.00 ± 13.69
85.00 ± 13.69
85.00 ± 13.69
90.00 ± 13.69
85.00 ± 13.69

100.00 ± 0.00
100.00 ± 0.00
100 ± 0.00
100 ± 0.00
100.00 ± 0.00
100.00 ± 0.00
100.00 ± 0.00
80.00 ± 44.72
80.00 ± 44.72
60.00 ± 54.77
100 ± 0.00
100.00 ± 0.00
80.00 ± 44.72
60.00 ± 54.77
100.00 ± 0.00
100 ± 0.00

0.85 ± 0.26
0.82 ± 0.25
0.88 ± 0.27
0.90 ± 0.15
0.94 ± 0.08
0.94 ± 0.08
0.94 ± 0.08
0.92 ± 0.11
0.89 ± 0.11
0.80 ± 0.13
0.94 ± 0.08
0.94 ± 0.08
0.89 ± 0.11
0.87 ± 0.09
0.94 ± 0.08
0.91 ± 0.08

13.33
16.66
10
10
6.66
6.66
6.66
10
13.33
23.33
6.66
10
13.33
23.33
10
13.33

SVM classiﬁer performance using subband power as the feature for different mother wavelets.

TABLE IVD
RESULTS OF EVENT (PNES) CLASSIFICATION

Data

Mother
Wavelet

Accuracy

Sensitivity

Speciﬁcity

f-score

LOOE

db3

db5

coif3

sym3

Resultant
X
Y
Z
Resultant
X
Y
Z
Resultant
X
Y
Z
Resultant
X
Y
Z

88.00 ± 17.89
84.00 ± 16.73
88.00 ± 10.95
92.00 ± 10.95
88.00 ± 10.95
96.00 ± 8.94
88.00 ± 17.89
88.00 ± 10.95
84.00 ± 8.94
84.00 ± 8.94
80.00 ± 20.00
80.00 ± 14.14
88.00 ± 10.95
76.00 ± 16.73
84.00 ± 16.73
92.00 ± 10.95

90.00 ± 13.69
85.00 ± 13.69
85.00 ±
90.00 ± 13.69
90.00 ± 13.69
95.00 ± 11.18
85.00 ± 22.36
90.00 ± 13.69
90.00 ± 13.69
90.00 ± 13.69
80.00 ± 20.92
80.00 ± 20.92
85.00 ± 13.69
70.00 ± 20.92
80.00 ± 20.92
90.00 ± 13.69

80.00 ± 44.72
80.00 ± 44.72
100 ± 0.00
100.00 ± 0.00
80.00 ± 44.72
100.00 ± 0.00
100.00 ± 0.00
80.00 ± 44.72
60.00 ± 54.77
60.00 ± 54.77
80.00 ± 44.72
80.00 ± 44.72
100.00 ± 0.00
100.00 ± 0.00
100.00 ± 0.00
100.00 ± 0.00

0.92 ± 0.11
0.89 ± 0.11
0.91 ± 0.08
0.94 ± 0.08
0.92 ± 0.07
0.97 ± 0.06
0.90 ± 0.15
0.92 ± 0.07
0.90 ± 0.06
0.90 ± 0.06
0.85 ± 0.15
0.85 ± 0.12
0.91 ± 0.08
0.81 ± 0.14
0.88 ± 0.14
0.94 ± 0.08

6.66
13.33
16.66
10
13.33
10
13.33
10
16.66
16.66
20
26.66
13.33
26.66
16.66
10

SVM classiﬁer performance using subband entropy as the feature for different mother wavelets.

feature–classiﬁer pair and mother wavelets. In the event classiﬁ-
cation stage, the training model was validated by a ﬁvefold cross-
validation. The results as shown in Tables IVc and IVd suggest
that ﬁfth-order Daubechies wavelet gives the best results, which
also correlates well with the ﬁndings of Nijsen et al. [11]. Similar
results can be inferred from Tables IVa and IVb, where classi-
ﬁcation has been done using k-means. Further, it is seen that
a high f -score is found for signal corresponding to z-axis and
the resultant signal, which suggests that most of the seizure-like
activities manifest in the direction of z-axis, and the resultant
signal shows better results as it is a combined effect of the sig-
nals in all three axes. However, it should be noted that there
happens to be no clear direction of movement corresponding to
the z-axis when the accelerometer recording is a fully free form.
As a result, there is no easy way to attribute the movement to
any speciﬁc arm muscle.

Fig. 7 shows the observed and predicted value for patient
no. 4 and exhibits both epileptic and nonepileptic seizures.
The data were collected during August 27, 2012 to August 30,
2012. Fig. 7(a) shows the observed data and Fig. 7(b) shows the
predicted data. The gap in raw data on August 29, 2012 indicate
that the device was not worn or the battery was drained out until
the following morning. Normal activity in Fig. 7(a) is absent as
the information was not available in VEM, but the prediction
shows normal activity that was signiﬁcant as declared by the
event detection stage of the proposed algorithm.

This study demonstrates the use of a wrist-worn accelerome-
ter for detecting convulsive seizure events and classifying them
as ES or PNES. Bayly et al. [9] used FFT transform and showed
that the PNES events featured a stable dominant frequency
and ES characterized an evolving dominant frequency and was
proven that an accelerometer device can be used as a diagnostic

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:20 UTC from IEEE Xplore.  Restrictions apply. 

1070

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 20, NO. 4, JULY 2016

Fig. 7.

(a) Observed and (b) predicted events for patient no. 4 collected over three days. The patient had both ES and PNES.

tool. In this work, wavelet features have been used; furthermore,
k-means and SVM have been used for detection and classiﬁca-
tion of PNES events. The localization of time and frequency
using wavelet provides a higher resolution frequency and scale
analysis of the accelerometer signals. In line with this, the win-
dow size of the wavelet decomposition is reduced from 2.56 to
1 s.

From Table III, it is clear that the algorithm has a sensitiv-
ity of 100% for all the patients, which clearly demonstrates the
strength of the proposed approach. For any seizure detection
algorithm, it is vitally important that no seizure goes undetected
but at the same time to minimize the number of false alarms. Our
efforts have been to incorporate these concepts into the develop-
ment of an automated algorithm and come up with an accurate
seizure detection and classiﬁcation system. Our algorithm per-
formed fairly well with a near perfect event detection sensitivity
of 100% and a speciﬁcity of 85.77% for the 19 convulsive events.
The stage 1 of the proposed methodology has shown promising
and motivating results for seizure event detection, clearly stating
the reliability of the wrist-worn accelerometer devices in detect-
ing seizure events. One of the patients (patient no. 2) had a lot
of false positives which contributed to the overall reduction of
speciﬁcity; otherwise, the algorithm was able to detect seizure
events with good accuracy as seen from Table III. For patient
no. 2, the VEM recording of the patient was monitored as there
were a high number of false positives. The possible reason can
be attributed to the improper placement of the device or loose
strap of the device. In these cases, even slight movement of
the hands will result in activity data with higher amplitude and
frequency.

Table II shows the observed time of the seizure (for all events),
which is the time of seizure on VEM and the predicted time of
the seizure, which is the time of the seizure on the wrist-worn ac-
celerometer device. The positive start time error denotes the la-
tency in motor manifestation of the seizure event. In accordance

from the VEM recordings of the patient, it is seen that the la-
tency is the result of the gradual increase in motor manifestations
which starts off as a subtle event and manifests gradually. These
subtle movements at the start of the events mostly get ﬁltered out
during the on-device processing of the data in event detection
stage, thus resulting in latency. For patient no. 8, a huge delay
was observed. The reasons were attributed to error introduced
due to the time synchronization between iPod touch and the PC.
Further reasons were attributed to the posture of the patient dur-
ing VEM recording, resulting in loosening of the device strap
affecting the duration and timing of the recorded event on de-
vice; however, the occurrence of such mishaps was observed to
be rare. Table II also shows the duration error, which is found
to be negative in all cases except for event no. 2 in patient no. 5,
where the predicted duration is greater by 3 s. This can be due
to the subsiding nature of the convulsive manifestations of the
seizure event as it terminates; however, the electrical activity
of the brain has completely subsided. The reason for shorter
predicted duration in most of the cases is ascribed to the fact
that when a typical convulsive seizure starts and subsides, it
is mostly followed by the subtle limb movements (the typical
observation made from the VEM data). Such subtle limb move-
ments are ﬁltered on the device during event detection stage and
thus rendering equivalent to no motor manifestations by the pro-
posed algorithm. Thus, the observed duration is higher in most
of the cases in comparison to the predicted seizure duration.

The future direction involves in investigating whether the
acceleration data from a single axis are sufﬁcient for seizure de-
tection. However, the seizure detection is a multifactorial prob-
lem in that the seizures involve complex motor manifestations
and the orientation of the accelerometer device is continuously
changing. In this direction, the motion analysis of the trajectory
of the patient’s arm during a typical seizure using a wrist-based
accelerometer coupled with another sensor and ﬁnding proxy
accelerometer coordinate system to aid accurate diagnosis is

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:20 UTC from IEEE Xplore.  Restrictions apply. 

GUBBI et al.: AUTOMATIC DETECTION AND CLASSIFICATION OF CONVULSIVE PSYCHOGENIC NONEPILEPTIC SEIZURES

1071

required. Beniczky et al. [25] have performed the analysis of
sEMG in ES and PNES. Motor seizure causes involuntary con-
traction of muscles and performing a study determining the
accelerometer axes responsible for those muscle activation will
further help in minimizing the false positives and increasing the
accuracy of the proposed method. This is achieved by consid-
ering the activity only in a particular accelerometer axis and
discarding the data with minimal activity in the corresponding
axis.

However, an ambulatory monitoring device for seizure detec-
tion based on accelerometery can have the following limitations.
1) The accuracy of seizure detection can vary with the place-
ment of the device on the arm, as the algorithm is devel-
oped for a wrist-worn device.

2) Since we have considered seizures of durations greater
than 20 s, any seizures of lesser duration will go unde-
tected.

3) Furthermore, the system is still to be validated in home
conditions. For now, the system is tested and developed
in hospital settings, where patients do not engage in lot
of activities, which will not be the case in real-home
situations.

IV. CONCLUSION

A wireless wearable device for detecting and diagnosing
pseudo nonepileptic seizure is proposed. A novel algorithm for
detection of seizures using time-domain features is developed.
The detected seizures are classiﬁed into epileptic and nonepilep-
tic seizures using wavelet features and SVM classiﬁer. The data
from patients undergoing video EEG monitoring are collected
using the wearable device and tested on convulsive patients with
excellent results. The results demonstrate the feasibility of using
an automated easy-to-wear device to detect and diagnose PNES
in primary clinical setting.

ACKNOWLEDGMENT

The authors would like to thank D. Fernando and C. Muller
for their feedback and help during data collection as part of their
honors thesis. The authors would also like to thank the staff of
Royal Melbourne Hospital and the patients who agreed to be a
part of this study.

Disclosure: None of the authors has any conﬂict of interest

to disclose.

REFERENCES

[1] World Health Organization. (2014, Feb.). What are neurological disorders?

[Online]. Available: http://www.who.int/features/qa/55/en/

[2] S. Noachtar and A. Peters, “Semiology of epileptic seizures: A critical

review,” Epilepsy Behaviour, vol. 15, no. 1, pp. 2–9, 2009.

[3] S. R. Benbadis, K. Johnson, K. Anthony, G. Caines, G. Hess, C. Jackson,
F. L. Vale, and W. O. Tatum, “Induction of psychogenic nonepileptic
seizures without placebo,” Neurology, vol. 55, no. 12, pp. 1904–1905,
2000.

[4] N. Bodde, J. Brooks, G. Baker, P. Boon, J. Hendriksen, and A. Aldenkamp,
“Psychogenic non-epileptic seizures diagnostic issues: A critical review,”
Clin. Neurol. Neurosurgery, vol. 111, no. 1, pp. 1–9, 2009.

[5] M. Reuber and C. E. Elger, “Psychogenic nonepileptic seizures: Review

and update,” Epilepsy Behavior, vol. 4, no. 3, pp. 205–216, 2003.

[6] R. C. Martin, F. G. Gilliam, M. Kilgore, E. Faught, and R. Kuzniecky, “Im-
proved health care resource utilization following video-EEG-conﬁrmed
diagnosis of nonepileptic psychogenic seizures,” Seizure, vol. 7, no. 5,
pp. 385–390, 1998.

[7] M. Reuber, G. Fernandez, J. Bauer, C. Helmstaedter, and C. Elger, “Di-
agnostic delay in psychogenic nonepileptic seizures,” Neurology, vol. 58,
no. 3, pp. 493–495, 2002.

[8] J. Alving and S. Beniczky, “Diagnostic usefulness and duration of the in-
patient long-term video-EEG monitoring: Findings in patients extensively
investigated before the monitoring,” Seizure, vol. 18, no. 7, pp. 470–473,
2009.

[9] J. Bayly, J. Carino, S. Petrovski, M. Smit, D. A. Fernando, A. Vinton,
B. Yan, J. R. Gubbi, M. S. Palaniswami, and T. J. O’Brien, “Time-
frequency mapping of the rhythmic limb movements distinguishes con-
vulsive epileptic from psychogenic nonepileptic seizures,” Epilepsia,
vol. 54, no. 8, pp. 1402–1408, 2013.

[10] T. M. Nijsen, J. B. Arends, P. A. Griep, and P. J. Cluitmans, “The po-
tential value of three-dimensional accelerometry for detection of motor
seizures in severe epilepsy,” Epilepsy Behavior, vol. 7, no. 1, pp. 74–84,
2005.

[11] T. M. Nijsen, R. M. Aarts, P. J. Cluitmans, and P. A. Griep,
“Time-frequency analysis of accelerometry data for detection of my-
oclonic seizures,” IEEE Trans. Inf. Technol. Biomed., vol. 14, no. 5,
pp. 1197–1203, Sep. 2010.

[12] K. Cuppens, P. Karsmakers, A. Van de Vel, B. Bonroy, M. Milosevic,
S. Luca, T. Croonenborghs, B. Ceulemans, L. Lagae, S. Huffel, and
B. Vanrumste, “Accelerometry-based home monitoring for detection
of nocturnal hypermotor seizures based on novelty detection,” IEEE
J. Biomed. Health Informat., vol. 18, no. 3, pp. 1026–1033, May
2014.

[13] G. Becq, P. Kahane, L. Minotti, S. Bonnet, and R. Guillemaud, “Classi-
ﬁcation of epileptic motor manifestations and detection of tonic–clonic
seizures with acceleration norm entropy,” IEEE Trans. Biomed. Eng.,
vol. 60, no. 8, pp. 2080–2088, Aug. 2013.

[14] K. Cuppens, L. Lagae, B. Ceulemans, S. Van Huffel, and B. Vanrumste,
“Detection of nocturnal frontal lobe seizures in pediatric patients by means
of accelerometers: A ﬁrst study,” in Proc. Annu. Int. Conf. IEEE Eng. Med.
Biol. Soc., 2009, pp. 6608–6611.

[15] A. Dalton, S. Patel, A. R. Chowdhury, M. Welsh, T. Pang, S. Schachter,
G. OLaighin, and P. Bonato, “Development of a body sensor network to
detect motor patterns of epileptic seizures,” IEEE Trans. Biomed. Eng.,
vol. 59, no. 11, pp. 3204–3211, Nov. 2012.

[16] C. Ungureanu, V. Bui, W. Roosmalen, R. Aarts, J. Arends, R. Verhoeven,
and J. Lukkien, “A wearable monitoring system for nocturnal epileptic
seizures,” in Proc. 8th Int. Symp. Med. Inform. Commun. Technol., Apr.
2014, pp. 1–5.

[17] S. Patel, C. Mancinelli, A. Dalton, B. Patritti, T. Pang, S. Schachter, and
P. Bonato, “Detecting epileptic seizures using wearable sensors,” in Proc.
IEEE 35th Annu. Northeast Bioeng. Conf., 2009, pp. 1–2.

[18] I. Conradsen, S. Beniczky, K. Hoppe, P. Wolf, and H. B. Sorensen, “Au-
tomated algorithm for generalized tonic–clonic epileptic seizure onset
detection based on sEMG zero-crossing rate,” IEEE Trans. Biomed. Eng.,
vol. 59, no. 2, pp. 579–585, Feb. 2012.

[19] J. MacQueen, “Some methods for classiﬁcation and analysis of multivari-
ate observations,” in Proc. 5th Berkeley Symp. Math. Statistics Probab.,
California, CA, USA, 1967, vol. 1, pp. 281–297.

[20] S. S. Khan and A. Ahmad, “Cluster center initialization algorithm for
k-means clustering,” Pattern Recog. Lett., vol. 25, no. 11, pp. 1293–1302,
2004.

[21] B. E. Boser, I. M. Guyon, and V. N. Vapnik, “A training algorithm for op-
timal margin classiﬁers,” in Proc. 5th Annu. Workshop Comput. Learning
Theory, 1992, pp. 144–152.

[22] B. Scholkopf and A. J. Smola, Learning with Kernels: Support Vector
Machines, Regularization, Optimization, and Beyond. Cambridge, MA,
USA: MIT Press, 2001.

[23] J. Shawe-Taylor and N. Cristianini, Kernel Methods for Pattern Analysis.

Cambridge, U.K.: Cambridge Univ. Press, 2004.

[24] K.-P. Wu and S.-D. Wang, “Choosing the kernel parameters for support
vector machines by the inter-cluster distance in the feature space,” Pattern
Recog., vol. 42, no. 5, pp. 710–717, 2009.

[25] S. Beniczky, I. Conradsen, M. Moldovan, P. Jennum, M. Fabricius,
K. Benedek, N. Andersen, H. Hjalgrim, and P. Wolf, “Quantitative analysis
of surface electromyography during epileptic and nonepileptic convulsive
seizures,” Epilepsia, vol. 55, pp. 1128–1134, 2014.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:20 UTC from IEEE Xplore.  Restrictions apply. 

1072

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 20, NO. 4, JULY 2016

Jayavardhana Gubbi (SM’15) received the Bach-
elor of Engineering degree from Bangalore Univer-
sity, Bengaluru, India, in 2000, the Ph.D. degree from
the University of Melbourne, Parkville, Australia, in
2007.

For three years, he was a Research Assistant at the
Indian Institute of Science, where he was involved in
speech technology for Indian languages. He is cur-
rently a Research Fellow in the Department of Elec-
trical and Electronic Engineering, The University of
Melbourne. From 2010 to 2014, he was an ARC
Australian Postdoctoral Fellow Industry working on an industry linkage grant
in video processing. His current research interests include video processing,
Internet of Things, and ubiquitous healthcare devices. He has coauthored more
than 40 papers in peer-reviewed journals, conferences, and book chapters over
the last ten years. He has served as conference secretary and publications chair
in several international conferences in the area of wireless sensor networks,
signal processing, and pattern recognition.

Bernard Yan received F.R.A.C.P. degree from Col-
lege of Physicians, in 2003 and M.B.B.S. degree from
the University of Melbourne, Parkville, Australia, in
1994.

He is an Assistant Professor in the Department of
Medicine, The University of Melbourne, and the De-
partment of Neurology, Royal Melbourne Hospital
since 2005. He has published 106 academic papers
in peer-reviewed medical journals. He is actively in-
volved in investigator-driven and industry-sponsored
multicenter clinical trials. He is the Principal Inves-
tigator of several international studies in cerebrovascular diseases. He pursued
his academic interest in cerebrovascular disease research. One of his key re-
search interests is in the development of portable mobile wireless sensors for
the monitoring of patients with neurological diseases.

Shitanshu Kusmakar (S’14) received the B.Tech.
degree from Thapar University, Punjab, India, in
2010, and the M.Tech. degree in clinical engineer-
ing from the Indian Institute of Technology Madras,
Chennai, India, in 2012. He has been working to-
ward the Ph.D. degree in the Department of Electrical
and Electronic Engineering, The University of Mel-
bourne, Parkville, Australia, since December 2013.
For a year, he was a Clinical Applications Engineer
at R&D Centre HTIC, set up by the Indian Institute
of Technology Madras and Department of Biotech-
nology (DBT), Government of India. His research interests include ubiquitous
health monitoring devices, biomedical signal processing, epilepsy, classiﬁca-
tion, and pattern recognition.

Aravinda S. Rao (S’09) received the B.E. degree
in electronics and communications engineering from
Visveswaraya Technological University, Belgaum,
India, in 2006, and the M.E. degree in electron-
ics and telecommunications from Deakin University,
Geelong, Australia, in 2010. He is currently working
toward the Ph.D. degree at the University of Mel-
bourne, Parkville, Australia, working on video-based
monitoring crowd and understanding behavior.

He was a Deputy Engineer in the Development and
Engineering division of Naval Systems/Sonar Sys-
tems, focusing on designing and developing hardware for submarine sonar sys-
tems, at Bharat Electronics Limited, Bangalore, India, during 2006–2007. He
commenced his research studies at the Department of Electrical and Electronic
Engineering, The University of Melbourne, in 2011. His research interests in-
clude computer vision, crowd behavior analysis, manifold learning, wireless
sensor networks, and embedded systems design.

Terence O’Brien (M.B.B.S. Melb., M.D. Melb.,
F.R.A.C.P.) is The James Stewart Chair of Medicine,
The Department of Medicine, The Royal Melbourne
Hospitals, and consultant neurologist at The Royal
Melbourne Hospital, Victoria, Australia. He leads a
large translational research team undertaking both
basic studies, involving animal models, and clinical
studies. He is a specialist in neurology and clinical
pharmacology, with particular expertise in epilepsy,
anti-epileptic drugs and in-vivo imaging in animal
models and humans. He did his clinical and research
training at St. Vincent’s and Royal Melbourne Hospitals in Melbourne, and
then the Mayo Clinic, Rochester, Minnesota, USA (1995–1998). His research
is broad based, covering both basic and clinical studies related to epilepsy,
traumatic brain injury and other neurodegenerative conditions. The work has
had two primary goals: First to better understand the determinants of treatment
response, identify biomarkers for treatment outcomes–imaging, electrophysio-
logical, genomic and clinical, and develop new treatment approaches. Second
to investigate the fundamental neurobiological basis, and inter-relationship, of
the neuropsychiatric co-morbidities present in many patients with epilepsy and
neurodegenerative conditions. He has published over 275 peer-reviewed origi-
nal papers in leading scientiﬁc and medical journals, and 20 other publication.

Marimuthu Palaniswami (F’12) received the B.E.
(Hons.) from the University of Madras, Chennai, In-
dia, the M.E. degree from the Indian Institute of Sci-
ence, Bengaluru, India, and the Ph.D. degree from
the University of Newcastle, Callaghan, Australia.

He then joined the University of Melbourne,
Parkville, Australia, where he is currently a Professor
of electrical engineering and Director/Convener of a
large ARC Research Network on Intelligent Sensors,
Sensor Networks and Information Processing with
about 200 researchers and interdisciplinary themes
as focus for the center. He has coauthored more than 340 refereed journal and
conference papers, including a number of books, edited volumes, and book
chapters. His research interests include smart sensors and sensor networks, ma-
chine learning, neural networks, support vector machines, signal processing,
biomedical engineering, and control.

Dr. Palaniswami has served international boards and advisory committees
including a panel member for National Science Foundation, as an Associate
Editor for Journals/transactions including IEEE TRANSACTIONS ON NEURAL
NETWORKS and Computational Intelligence for Finance. He is the Subject Edi-
tor for the International Journal on Distributed Sensor Networks. He was given
a Foreign Specialist Award by the Ministry of Education, Japan, in recognition
of his contributions to the ﬁeld of machine learning.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:20 UTC from IEEE Xplore.  Restrictions apply.
