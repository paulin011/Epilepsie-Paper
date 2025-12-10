# Pordoy et al. - The Open Seizure Database Facilitating Research Into Non-EEG Seizure Detection

GENERIC COLORIZED JOURNAL, VOL. XX, NO. XX, XXXX 2017

1

The Open Seizure Database

Facilitating Research Into Non-EEG Seizure Detection

J. Pordoy, G. Jones, N. Matoorian, N. Dadashiserej and M. Zolgharni

Abstract— This research introduces the Open Seizure Database
and Toolkit as a novel, publicly accessible resource designed
to advance non-electroencephalogram seizure detection research.
This paper highlights the scarcity of resources in the non-
electroencephalogram domain and establishes the Open Seizure
Database as the ﬁrst openly accessible database containing
multimodal sensor data from 49 participants in real-world,
in-
home environments. The database is comprised of 494 events,
encompassing 146 epileptic seizures, collected over a duration
of 453 days, presenting the most extensive publicly available
non-electroencephalogram seizure data to date. Additionally, the
database has 348 labelled false alarms, including 302 common
human movements and activities. The Open Seizure Toolkit is
designed to facilitate machine and deep learning practices by
streamlining data from the Open Seizure Database. Utilising these
resources, researchers can rapidly develop and train seizure detec-
tion models before deploying them to the Open Seizure Detector
Android Application. Access to these resources is expected to
foster collaborative efforts, ultimately contributing to the establish-
ment of a non-electroencephalogram gold standard and advancing
the ﬁeld of seizure detection.

Index Terms— Seizure Detection, Epilepsy, Multimodal,
Open Seizure Detector, Deep Learning, Accelerometer, PPG

I. INTRODUCTION

Epilepsy is a chronic neurological disorder that affects an estimated
65 million people worldwide, characterised by recurring unprovoked
seizures due to an abnormal, hypersynchronous discharge between
communicating neurons [1]. Epidemiological studies suggest that
approximately 30% of patients with epilepsy (PWE) are refractory to
common therapeutic treatments, which increases the risk of a sudden
unexpected death in epilepsy (SUDEP). SUDEP is the leading cause
of premature death observed in patients diagnosed with refractory
epilepsy and is deﬁned as a death in epilepsy that is not attributable
to trauma, drowning or status epilepticus [2].

Although the underlying etiology behind SUDEP remains un-
known, studies show that in 67% of cases, there were indications of a
generalised seizure preceding the terminal event [3] [4]. Additionally,
there is evidence to indicate that seizure-induced perturbations in
respiratory, cardiac, and electrocerebral functions, along with several
potential predisposing risk factors, could contribute to SUDEP [5].
Lamberts et al found that 58% of SUDEP cases were associated
with sleep, and that 86% of instances occurred when the PWE was
alone and unsupervised [6]. Sveinsson et al’s analysis of 321 SUDEP
cases yielded similar ﬁndings, with most instances occurring at night
in the patient’s home whilst living alone (71%) [6]. While similar

J. Pordoy, Department of Computing, University of West London, St

Mary’s Rd, London W5 5RF, (e-mail:jamie.pordoy@uwl.ac.uk).

G. Jones, Open Seizure Detector, Hartlepool, UK, TS26 (e-

mail:graham@openseizuredetector.org.uk).

N. Matoorian, Dept of Computing, University of West London, St

Mary’s Rd, London W5 5RF, (e-mail:Nasser.matoorian@uwl.ac.uk).

N. Dadashiserej, Dept of Computing, University of West London, St

Mary’s Rd, London W5 5RF (e-mail:nassim.dadashiserej@uwl.ac.uk).

M. Zolgharni, Dept of Computing, University of West London, St

Mary’s Rd, London W5 5RF (e-mail:massoud.Zolgharni@uwl.ac.uk).

ﬁndings can be found in broader literature, closer examination reveals
that predisposed factors for SUDEP are primarily triggered when
the individual with epilepsy is at home. These ﬁndings indicate
that such factors signiﬁcantly increase the likelihood of SUDEP,
with studies concluding that up to 69% of cases could have been
left unattended at night. Despite
prevented if patients were not
little progress has been made in
an increase in clinical studies,
characterising SUDEP risk factors and the underlying mechanisms
leading to premature death in epilepsy [7] [8]. This has led numerous
studies to postulate that seizure detection could serve as a means to
deter terminal seizures pre-ictal, and reduce the incidence of SUDEP
cases through early intervention and prevention.

II. RELATED WORK

The electroencephalogram (EEG) represents the diagnostic gold
standard modality for capturing seizures within hospital settings,
employing continuous electrical brain wave monitoring over an
extended period. However, the EEG’s utility as an assistive diagnostic
tool is unsuitable outside of a hospital or epilepsy monitoring unit
(EMU) due to the need for a PWE to remain in a stationary
position with multiple scalp-based electrodes attached, and a full-
time neurodiagnostic technician to interpret real-time neurological
activity. To overcome the limitations associated with EEG, a new
sub-ﬁeld of research has emerged known as non-EEG detection.
This approach utilises non-invasive methods to detect seizures in
real-world environments. These methods include wearable devices
that measure physiological signals such as heart rate, movement and
electrodermal activity.

The accelerometer (ACM) has emerged as the most promising
non-EEG sensing modality, having been extensively explored in
non-EEG research for capturing changes in motion and velocity
displayed by PWE. Notably, these investigations have showcased
the ACMs potential for detecting rhythmic movements, particularly
those associated with a generalised tonic-clonic (GTC) seizures. By
leveraging ACM data, sophisticated algorithms have been developed
to identify the convulsive movements characteristic of a seizure’s
clonic phase. Seminal studies conducted by Conradsen et al. and
Lockman et al, serve as notable examples, demonstrating the practical
application of ACM-based detection with remarkable accuracies of
90% and 91% respectively [9] [10].

However, it is important to note that the ACM data utilised in
these studies did not originate from patients diagnosed with epilepsy;
rather, it was simulated by healthy participants in controlled short-
term studies. This prevailing trend is widespread in the ﬁeld of non-
EEG seizure detection, as a signiﬁcant portion of studies have relied
on small-scale, simulated, or synthetic datasets [16]. Two predominate
factors contribute to this observation. Firstly, the ﬁeld of research
in non-EEG detection is relatively new, and as such, there are no
established, publicly available datasets, which are more common in
other domains of healthcare research. Secondly, epileptic seizures
are infrequent, rare events, which makes it challenging to record
an extensive dataset of generalised seizure recordings from multiple
PWE.

2

GENERIC COLORIZED JOURNAL, VOL. XX, NO. XX, XXXX 2017

TABLE I: Summary of the publicly available datasets used for non- electroencephalogram seizure detection where the # symbol represents
the “number of”, Ref = Reference, Prt = Participants, Sz = Seizure, Ps = Per Sample, SR = Sample Rate and p/e = per event

Ref

[11]
[12]
[13]
[14]
[15]

Total

Dataset

Sensors

Type

#Prt

MyNeuroHealth
Epilepsy Convulsion Recognition
Patient-Speciﬁc Dataset
Post-Ictal Heart Rate Oscillations
Gestures: MICCAI 2021

Smartphone tri-axial accelerometer
Tri-axial accelerometer
Electrocardiogram & electroencephalogram
Single-lead ECG
Video Capture & Image Capture

5

7

Real
Simulated
Real
Simulated
Real

2

23
6
15
5
68

Dur

30s p/e
30s p/e
-
15-110s p/e
approx 0.5s p/e

SR

15Hz
16Hz
512Hz
200 Hz
-

#Sz

3
10
38
11
183

210

Table I provides a comprehensive overview of the non-EEG
datasets currently accessible in the public domain, intended to drive
progress in the ﬁeld. However, upon closer examination, it becomes
evident that a signiﬁcant portion of the data is either simulated or
recorded using sub-optimal sensing modalities, such as smartphones
with embedded ACMs. Additionally,
the existing data lacks the
necessary depth to capture the complexities inherent in different types
of epilepsy. To address this, non-EEG data should be recorded from
real-world, in-home environments, as this is where most seizures
and SUDEP cases occur. By utilising real-world data, non-EEG
detection systems can be modelled to accurately reﬂect the real-world
complexities encountered by PWE in their day to day lives.

While publicly available non-EEG data remains limited, com-
mercial organisations and international consortiums have conducted
studies using several non-EEG detection techniques. Empatica’s
Embrace has been used in several studies to detect convulsive
seizures, demonstrating an average sensitivity of 92-100% and a
false alarm rate (FAR) between 0.2-1 per day [17] [18] [19] [20].
Another commercially available device, Seer Medical’s smartwatch
has yielded a mean area under curve (AUC), a sensitivity, and a
FAR per day of 0.98, 0.93, and 2.3, respectively for 19 motor
seizures from 10 in-hospital patients [21]. However, it should be
noted that the data used in these studies is not accessible to the
wider academic community, limiting the ability to replicate these
ﬁndings. Additionally, consideration should be given to the fact that
the data used in these commercial studies predominantly originates
from clinical trials conducted in EMUs, where the environmental
dynamics are closely regulated [22] .

The progress in non-EEG research is currently hindered by the
lack of publicly available data, impeding scientiﬁc advancements
and leading to slower progress compared to other ﬁelds utilising
Machine Learning/Deep Learning techniques in clinical practice [23].
Additionally, non-EEG literature often demonstrates high accuracy
scores but
is accompanied by a signiﬁcant occurrence of false
positives. The presence of false alarms poses challenges in real-
world seizure detection applications, as it can result in unnecessary
alerts, incorrectly indicating the presence of a seizure [24]. Reducing
false alarms is crucial to enhancing the reliability and effectiveness
of seizure detection models. The use of multimodal sensors shows
promise in achieving this goal. By combining data from different
sensors, a more accurate and robust dataset can be constructed for
the development of intelligent detection models. Several studies have
suggested that multimodal sensing could decrease the false positive
rate observed in literature and improve the accuracy and performance
of existing seizure detection models. To achieve these goals there is
a pressing need for a large-scale in-home study to record multimodal
sensor data. By recording individuals with epilepsy in their real-world
home environments using multiple sensors, a comprehensive dataset
could be created, offering sufﬁcient depth and breadth to tackle the
current challenges in non-EEG seizure detection research.

Large-scale data repositories and collaborative data sharing have
become integral to clinical progress. In epilepsy research, the Euro-
pean Epilepsy Database (EED) is the largest and most comprehensive
database for human surface and intracranial EEG recordings. It
contains clinically annotated pre-ictal, ictal, and post-ictal EEG data
from 278 patients suffering from pharmaco-resistant partial epilepsy
[25] [26]. Through collaborative sharing and centralised data access,
the EED has been cited in over 138 publications, facilitating research
progress in the ﬁeld of EEG detection [25]. However, the EED stores
data strictly for neurological research and does not store any non-EEG
resources.

A publicly available non-EEG database dedicated to storing sensor
data from patients with epilepsy in real-world conditions holds great
potential for transforming the ﬁeld of seizure detection research.
This approach would enable benchmark testing and comparative
analysis under reproducible conditions, facilitating the evaluation and
advancement of novel seizure detection techniques. Moreover, such
a database could advance epilepsy research through data sharing
and collaboration [27], enabling researchers to investigate innovative
concepts such as patient-speciﬁc and seizure-speciﬁc detection.

This paper is organised into the following sections: Section III
details the development of the Open Seizure Database. Section
IV outlines the Open Seizure Toolkit, highlighting its capacity to
rapidly develop algorithms compatible with Open Seizure Detector.
Section V presents the experimental results achieved using the the
Open Seizure Database and Toolkit. In Section VI, a comprehensive
discussion of this paper’s ﬁndings and ﬁnally, Section VII concludes
by highlighting the studies impact on the ﬁeld of non-EEG seizure
detection.

III. METHODOLOGY
This study introduces the Open Seizure Database (OSDB) and
Open Seizure Toolkit (OSTK) as novel contributions to the ﬁeld of
non-EEG seizure detection [28]. Developed in collaboration between
Open Seizure Detector (OSD) [29] and the University of West Lon-
don [30], the OSDB serves as the ﬁrst publicly accessible database
containing non-EEG epileptic seizure recordings from real-world, in-
home environments. OSD, established in 2013, is the largest open-
source seizure detection software package, distributed under the open-
source, GNU General Public License (GPL), boasting over 5000
downloads [31], and an estimated 300 daily users [29].

A comprehensive beta trial was conducted, utilising non-invasive
wearable sensing devices to capture non-EEG data from a diverse
cohort of participants diagnosed with various forms of epilepsy.
This beta trial, closely supervised by OSD, spanned from January
to June 2022. In adherence to ethical standards, all participants
provided informed consent [33], and voluntarily enrolled in the beta
trial through the Google Play Services Public Beta Program [32].
Furthermore, this research study obtained approval from the ethics
committee at the University of West London.

J PORDOY et al.: PREPARATION OF BRIEF PAPERS FOR IEEE TRANSACTIONS AND JOURNALS (FEBRUARY 2017)

3

Fig. 1: An illustration of the Open Seizure Detector architecture used to record participant data. The architecture consists of four main
components, Open Seizure Detector Android Application, Open Seizure Web Server, Open Seizure Database and the Open Seizure Toolkit

To uphold strict conﬁdentiality during the data collection process,
stringent measures were implemented, encompassing the removal
of personal identiﬁers to ensure anonymity. Subsequent to the beta
trial period, the opportunity to contribute data to the database was
extended to all OSD users who consented to the data safety statement.
Notably, data collection remains ongoing to the present day.

For the beta trial, individuals with partial-onset epilepsy, partic-
ularly those susceptible to absence or complex focal seizures, were
intentionally excluded during the initial phase of data collection. This
decision was predicated on the absence of tonic, atonic, myoclonic,
or clonic movements typically associated with generalised epilepsy.
Consequently, among the participants who signed up to the beta trial,
49 individuals met the required criteria concerning both technological
aspects, such as device and sensor compatibility, as well as physio-
logical requirements pertaining to the type of epilepsy.

Participants were instructed to install the OSD Android application
[31] and continually wear a wrist-worn sensor device (Fig. 3), except
when charging was required. Several Garmin devices (TABLE III)
were employed for data collection, in which sensor data was transmit-
ted to the participants Android device using a Bluetooth connection.
Sensor data is then stored temporally on the end users device where
it is analysed to detect seizure-like movement as described in Section
III-F. When seizure-like movement is detected, the associated data is
stored long term using the OSD web server (Fig. 1).

A. Dataset

During the 453 day data collection period, a total of 494 events
were recorded from 49 participants. 146 events were recorded as
epileptic seizures, while the remaining 348 were classiﬁed as false
alarms. Among the false alarms, 302 were associated with human/-
physical activities and were appropriately labelled as such (Fig. 2).
The remaining 46 events were categorised as false alarms where
the activity is unknown. Epileptic seizures were recorded from 18
participants, amounting to a cumulative duration of 5 hours and
51 minutes (TABLE II). A diverse range of epileptic seizures were
recorded with 50 GTC seizures, 27 aura/focal seizures, 22 atonic
seizures/falls and 47 seizures labelled as ”Other Seizure”. It
is
important to note that, for the purposes of this study, ”Other seizure”
are deﬁned as seizures that were labelled only by type (e.g. seizure
or false alarm). Participants did not provide further categorisation of
the events speciﬁc sub-types (e.g. atonic, aura, tonic-clonic).

Fig. 2: Summary of the different events recorded. Epileptic-related
events are highlighted in orange, while common human activities
responsible for triggering false alarms are indicated in blue.

B. Sensing Modalities

Recording epileptic seizures from a large group of participants
using multiple sensors is a signiﬁcant challenge. To overcome this, we
employed Garmin wearable devices, capable of measuring accelerom-
etry, photoplethysmography (PPG), and pulse-oximetry (Sp02) sig-
nals. The use of Garmin devices proved to be a cost-effective and
easily accessible solution to record sensor data (Fig. 4) from a
large cohort of participants with epilepsy in their real-world, home
environments. This section details the sensors used during the study.
Garmin wrist-worn devices are equipped with tri-axis ACM and
have a sensing range of ±2 g up to ±16 g, where ’g’ quantiﬁes
the gravitational forces along different device axes [34]. This range
signiﬁes the maximum acceleration value accurately measurable by a
Garmin device. The ±2 g range accommodates the broad spectrum of
human movements and activities, while the ±16 g range can facilitate
the detection of high intensity movements.

For heart rate monitoring, Garmin devices are equipped with an
embedded optical PPG sensor, located on the back, which utilises a
green light-emitting diode to emit light onto the skin, thereby mea-
suring volumetric variations in blood circulation [35]. The reﬂected
light from the red blood cells in the skin facilitates the measurement
of the participant’s heart rate in beats per minute (bpm).

4

GENERIC COLORIZED JOURNAL, VOL. XX, NO. XX, XXXX 2017

Fig. 3: The architecture of Open Seizure Detector, detailing the components utilised by each participant. (a) and (e) depict a participant
wearing a Garmin device on their dominant hand from front and side angles. (b) illustrates the Bluetooth inter-connectivity between the
Garmin wearable device and the participant’s Android device. (c) is an example of a Garmin (Garmin Venu SQ) device used during the trial
and (d) illustrates the Open Seizure Detector application Interface.

TABLE II: Summary of the seizure events that were recorded during
the beta trial where data is distributed by participant Id, seizure
type and duration. Epileptic seizures were recorded from 18/49
participants in which TC = Tonic-clonic and Oth Sz = Other Seizure

Participant Id

#TC #Aura

#Atonic/ Fall

#Oth Sz Recorded Duration

P45
P39
P53
P83
P8
P421
P236
P55
P470
P62
P389
P157
P465
P483
P80
P59
P132
P138

18

25
11
0
5
3
2
0
0
0
0
1
1
1
1
0
0
0
0

50

22
0
0
0
3
0
2
0
0
0
0
0
0
0
0
0
0
0

27

0
0
16
0
0
0
0
0
2
0
0
0
0
0
1
1
1
1

22

10
33
0
1
0
0
0
2
0
1
0
0
0
0
0
0
0
0

47

02:21:35
01:48:20
00:41:45
00:16:05
00:05:00
00:04:40
00:04:20
00:04:15
00:02:45
00:02:45
00:02:30
00:02:30
00:02:30
00:02:15
00:02:35
00:02:25
00:02:20
00:02:35

05:51:00

Fig. 4: Graphical plots detailing sensor data recorded for events in
the Open Seizure Database. In plot (a), acceleration is measured as
vector magnitude. Plot (b) visualises the acceleration data for the
event along the x, y, z axis. Plot (c) visualises heart rate and oxygen
saturation levels obtained from the photoplethysmography sensor and
oxygen saturation sensors. Plot (d) depicts the Rroi and sensitivity
threshold measurements that represents the sequence in which the
event was detected by Open Seizure Detector algorithm.

Newer Garmin devices are equipped with oxygen saturation sen-
sors (SpO2) to non-invasively measure blood oxygen levels. These
devices utilise two wavelengths of light, red and infrared, with
red light being absorbed by oxygenated blood and infrared light
by deoxygenated blood. By analysing the absorption ratio of these
wavelengths, oxygen saturation levels can be calculated [36].

C. Data Storage

To address the long-term data storage requirements, a mobile-
client, client-server architecture was implemented. Short-term data

J PORDOY et al.: PREPARATION OF BRIEF PAPERS FOR IEEE TRANSACTIONS AND JOURNALS (FEBRUARY 2017)

5

storage utilised an SQLite database on each participants Android
device, leveraging local storage capabilities. Mobile Sync ensured
efﬁcient and reliable data synchronisation between the mobile client
and the OSD web server.

Sensor data was transmitted using Bluetooth in 5 second timesteps
(intervals) to the on-device database, striking a balance between
capturing sufﬁcient information for seizure detection and minimis-
ing energy consumption. Furthermore, the periodic transmission of
locally stored data to the OSD Web Server was designed to prevent
potential bottlenecks during the upload.

The OSDB was designed to be ﬂexible and maintain backward
compatibility. Initially, it stored one-dimensional ACM data in the
form of vector magnitude and heart rate data. However, during the
beta trial, adjustments were made to accommodate the storage of
SpO2 and three-dimensional ACM data. By utilising an SQLite
database on the Android platform and integrating additional fea-
tures and sensors, the OSD project achieved scalability and ensured
compatibility. Design choices were driven by the goal of optimising
data storage, capturing relevant sensor data, and improving overall
performance.

D. Database Schema

The database schema for the OSDB was carefully anonymized
and preprocessed, and the data was converted into a series of JSON
scripts. The utilisation of JSON provided a structured representation
of the data, ensuring accessibility across different platforms and
programming languages. Version 1 of the OSDB is available upon
request through the OSDB GitHub repository. It can be accessed
either as a single JSON script containing data for all labelled events
or as a subset focusing on speciﬁc event types such as tonic-clonic
or false alarms. The datasets are organised hierarchically using a
one-to-many relationship, where each event has multiple sub-events.
Each sub-event corresponds to a 5-second timestep, and sensor data
for that timestep is stored as a JSON array called ”Datapoints.” The
complete JSON schema of the OSDB, including accurate attribute
names, arrays, and data types, is provided in Fig. 5 and TABLE IV.

E. Annotating Event Labels

As the beta trial had a diverse cohort of participants spread across
the globe, a self-annotation system was developed where participants
were able to label an event as it occurred using the OSD Android
application. When an event was detected, participants were instructed
to label the event by type (e.g., Seizure, false alarm) and then sub-type
(e.g., aura, tonic-clonic). Participants had the ﬂexibility to add custom
class labels for more accurate annotation or choose from a predeﬁned
set of labels commonly associated with false alarms. Additionally,
participants had the option to manually trigger an alarm and label an
event in cases where the algorithm failed to detect a seizure.

TABLE III: Summary of the different Garmin devices and sensor
conﬁgurations employed for this study. Grouped by Device

Device

Code

Sensors

Participants

Venu
Venu SQ
Venu 2
Forerunner
Vivoactive 4
Vivoactive HR

006-B3226-00
010-02427-10
010-02430-11
010-02120-11
006-B3225-00
006-B2337-00

ACM, PPG, Sp02
ACM, PPG, Sp02
ACM, PPG, Sp02
ACM, PPG
ACM, PPG, Sp02
ACM, PPG

16
10
13
5
6
7

OSD performed a second stage of annotation, involving expert
labelling the start and end of each seizures convulsive or seizure-like
movement. The duration of each seizure is stored as an array labelled
”seizureTimes”, denoting the start and end time of the seizure-like
movement. By leveraging self-annotation during the trial and expert
labelling afterwards, the resulting OSDB presents the most accurate,
publicly available set of fully annotated non-EEG recordings.

{

}

"eventId": 47000,
"type": "Seizure",
"subType": "Other",
"desc": "partial.
"userId": 39,
"dataSourceName": "Garmin",
"alarmFreqMax": 8,
"alarmFreqMin": 3,
"datapoints": [{

arm flapping",

"alarmPhrase": "OK",
"alarmState": 0,
"dataTime": "2023-05-15T06:45:56Z",
"hr": 87,
"o2Sat": 0,
"rawData": [x1, x2, x2, ... ,x125],
"rawData3D": [x1, y1, z1, ... ,z375],
"roiPower": 4,
"roiRatio": 40,
"simpleSpec": [s1, s2, ... , s10],
"specPower": 1

},
{...}, {...}],

"seizureTimes":[-20, 60],
"has3dData": true,
"hasHrData": true,
"hasO2SatData": false,
"hrThreshMax": 150,
"hrThreshMin": 40,
"hrAlarmActive": false,
"phoneAppVersion": "4.1.2",
"sampleFreq": 25,
"watchFwVersion": "2.4.9",
"watchPartNo": "006-B2337-00",
"watchSdName": "GarminSD"

Fig. 5: Open Seizure Database JSON schema. Events are stored by
eventID and sensor data is stored using the ”datapoints” array

TABLE IV: Summary of datapoints array. Datapoints are recorded for
each timestep and can be accessed using the following attributes

Id

Attribute #DP

Description

1
2
3
4
5
6
7
8

RawData 125
3dRawData 375

Hr
O2Sat

1
1

1D Vector magnitude signal in milli-g
3D (xyz) accelerometer signal in milli-g
Heart rate signal in bpm
Oxygen Saturation (Sp02 %)

SimpleSpec 10 Spectral power in 1 second wide frequency bins (0-10 Hz)

1
RoiRatio
RoiPower
1
SpecPower 1

Region of Interest Ratio for OSD algorithm
Region of Interest power
Power of Frequency Spectrum

6

GENERIC COLORIZED JOURNAL, VOL. XX, NO. XX, XXXX 2017

F. Open Seizure Detector Algorithm

For seizure detection during the beta trial, participants were in-
structed to use the OSD Android application which runs a deter-
ministic detection algorithm. Sensor data was transmitted from the
participants’ Garmin device to the OSD application in ﬁve second
timesteps at a sample frequency of 25 Hz, resulting in 125 measure-
ments per timestep. To optimise the battery capacity of participants
Android devices, acceleration was in measured as a unit of vector
magnitude instead of measuring three separate spatial dimensions
(x, y, z), thus reducing the computational requirements by a factor
2
of
3 . This decision was made to increase the data collection duration
without the need for frequent battery replacement or recharging.
Vector magnitude for the current timestep can be calculated as

y−t + a2

At = q(a2

x−t + a2
Where ax−t, ax−t and ax−t represent the moving acceleration of
each orthogonal axis for timestep (t). The algorithm then transforms
the vector magnitude signal from the time domain to the frequency
domain by utilising a Fast Fourier Transform (F F T ) to compute the
power in each frequency range.

z−t)

(1)

As stated by the Nyquist Theorem, the maximum frequency that
can faithfully represent the original signal is half of the sample
frequency [37]. Consequently,
the OSD algorithm running on a
Garmin device is capable of precisely reconstructing signals with
frequencies up to 12.5 Hz without experiencing aliasing. If the
algorithm detects a participant moving at a frequency exceeding
12.5 Hz, the resulting observation will manifest as an alias feature in
the spectrum. However previous studies have reported that common
human movement predominantly occur within a frequency range
between 0-12.5 Hz [38]. Given this observation, we posit that any
high-frequency movement beyond the 12.5 Hz threshold will exert
minimal inﬂuence on algorithmic performance, as it lies outside the
typical range of human movement. Furthermore, studies have shown
that during the clonic phase the body’s major muscle groups exhibit
repetitive convulsions at a frequency range between 3-8 Hz, which is
inside the algorithms detectable frequency range [39] [40].

The frequency resolution of the spectrum is then determined by di-
viding the sample frequency (25 Hz) by the number of measurements
(125) per timestep, resulting in a resolution of 0.2 Hz. This resolu-
tion allows for effective detection and differentiation of frequency
components with a precision of 0.2 Hz. These calculations indicate
that the algorithm can accurately identify frequency components that
are spaced at intervals of 0.2 Hz, however any frequency differences
smaller than this value may not be distinguishable [41].

To detect a ’seizure-like’ movement, the algorithm calculates the
average power for the whole spectrum (Ps) and then the average
power of the 3-8 Hz Region of Interest (Proi) for each timestep. To
reduce the FAR, (Ps) is checked against a threshold to ensure that
there is a sufﬁcient level of movement, thus avoiding spurious alarms
caused by measurement noise when there is minimal movement. If
the movement detected exceeds the movement threshold, then Rroi
is calculated as the ratio between (Proi) and (Ps) which can be
expressed as

Algorithm 1 Pseudo code for the OSD algorithm where At =
acceleration (vector magnitude) at timestep t, Ps = spectrum power,
Proi = Region of Interest power, Rroi = ROI Ratio, T h = threshold.
DoAnalysis takes At as an input parameter on a repeating loop every
5 seconds. The acceleration values are passed to a F F T to convert
values into the frequency domain. For each timestep t the average of
Ps and Proi are calculated to ﬁnd the ratio of Rroi. If Rroi ≥ T h,
’seizure-like’ movement is detected where SD = Seizure Detected
and AS = Alarm State. Variables SD and AS are initialised at 0
At = [x1, x2, x3, ..., x125]
T h= Threshold
function: DoAnalysis(At)
1. F F T ← FastFourierTransform(At)
2. Ps ← CalculateAveragePower(0 − 12.5Hz)
3. Proi ← CalculateAveragePower(3 − 8Hz)
4. Rroi ← Proi
Ps
Input: DoAnalysis(At)
Output: Alarm ’Seizure Detected’
if At = True then

for each 5-second timestep where SD = True do

if SD = True & AS = 0 then

update AS = 1
DoAnalysis(At)

else if SD = True & AS = 1 then

update AS = 2
DoAnalysis(At)

else if SD = True & AS = 2 then

update AS = 3
Alert ’Seizure Detected’
DoAnalysis(At)

else if SD = True & AS = 3 then

AS == AS
DoAnalysis(At)

end
for each 5-second timestep where SD = False do

if SD = False & AS = 0 then

AS == AS
DoAnalysis(At)

else if SD = False & AS = 1 then

update AS = 0
DoAnalysis(At)

else if SD = False & AS = 2 then

update AS = 1
Alert ’Seizure Detected’
DoAnalysis(At)

else if SD = False & AS = 3 then

update AS = 2
DoAnalysis(At)

Rroi =

Proi
Ps

(2)

end

else

A seizure is then detected if Rroi ≥ the algorithms sensitivity
threshold. If the sensitivity threshold is exceeded for three consecutive
timesteps, an alarm state is raised, and the data saved to the database.
Three consecutive timesteps (15 seconds) were utilised to give bal-
ance between reducing false alarms and ensuring prompt generation
of an alarm when a genuine seizure was detected. The above process
is detailed in Algorithm 1.

AS == AS
Alert ’Input not received’
DoAnalysis(At)

end

J PORDOY et al.: PREPARATION OF BRIEF PAPERS FOR IEEE TRANSACTIONS AND JOURNALS (FEBRUARY 2017)

7

TABLE V: Summary of the events recorded during the beta trial. Events are categorised by type and sub-type and ordered by frequency of
event. The average duration is a calculation of the average duration of events (145s) * number of events for each sub type.

Class ID

Type

Sub Type

Participants

Events

Sub Events

Average Duration (hh:mm:ss)

c21
c4
c18
c23
c10
c16
c20
c24
c7
c2
c6
c1
c3
c19
c13
c12
c5
c22
c9
c8
c15
c11
c17
c14

#

Seizure
Seizure
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
Seizure
False Alarm
Seizure
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm

Tonic-Clonic
Other Seizure
Sorting
Unknown
Motor Vehicle
Sleeping
Talking
Washing Up
Gaming
Aura/Focal
Fidgeting
Atonic/Fall
Brushing Teeth
Standing
Scratching
Pushing Pram
Cycling
Typing
Lying Down
Hammock
Shopping
Other
Sneezing
Shaving

2

24

9
5
5
18
8
7
9
4
8
3
3
6
8
3
3
1
1
1
2
1
1
1
1
1

49

50
47
47
46
44
39
33
28
28
27
23
22
18
16
5
5
4
4
2
2
1
1
1
1

494

1450
1363
1363
1334
1276
1092
957
812
784
899
667
464
504
464
145
116
116
116
58
48
29
28
28
24

-

02:01:50
01:53:35
01:53:35
01:51:10
01:46:20
01:31:00
01:20:30
01:07:40
01:05:35
01:15:55
00:55:35
00:39:40
00:42:00
00:37:20
00:12:05
00:09:40
00:09:40
00:09:40
00:05:50
00:04:50
00:02:25
00:02:20
00:02:20
00:02:00

19:42:35

(a) Event:5382 - Atonic/Fall

(b) Event:6884 - Aura/Focal

(c) Event:8875 - Tonic-Clonic

(d) Event:5610 - Other Seizure

(e) Event:5221 - Cycling

(f) Event:5470 - Brushing Teeth

(g) Event:8737 - Tonic-Clonic

(h) Event:5218 - Scratching

(i) Event:8800 - Other Seizure

Fig. 6: A representative subset from the Open Seizure Database that visualises acceleration and heart rate signals for different types of event

8

GENERIC COLORIZED JOURNAL, VOL. XX, NO. XX, XXXX 2017

Fig. 7: A hierarchical overview of the ﬁle structure and core compo-
nents of the Open Seizure Database and Open Seizure Toolkit

IV. THE OPEN SEIZURE TOOLKIT
The Open Seizure Toolkit is a software package developed by
OSD, serving to facilitate data access to the OSDB, enabling the
analysis and development of seizure detection models compatible
with the OSD Android application. Fig.7 depicts the hierarchical
structure of the OSTK, which encompasses three primary components
(NN Trainer, Test Runner, and Data Summariser) located in the
User Tools directory. To access the OSDB, users are required to
clone the OSTK repository from the ofﬁcial OSD GitHub Repository.
Additionally, data access requires user registration with OSD and
compliance with the guidelines speciﬁed in the OSDB licence [43].
The following section illustrates the functionality of the OSTK by
conducting a series of experiments to developing a basic seizure
detection model compatible with the OSD Android application. For
this experiment a subset of 190 events were selected from 16
participants diagnosed with different epilepsy types.

A. Preprocessing and Data Engineering

By utilising the OSTK WebApi connector, data was extracted
as a JSON string and subsequently transformed by ﬂattening the
hierarchical structure of the data’s nested objects and loaded as
a dataframe for manipulation. Data cleaning, analysis, and feature
engineering were conducted to prepare the data for classiﬁcation.
To address the issue of imbalanced data, random oversampling was
applied to the minority class. In order to mitigate the effects of
data duplication resulting from oversampling, Gaussian noise was
introduced to the ACM data as a form of data augmentation, thereby
enhancing the variability among samples.

B. Class Relabelling and One Hot Encoding

In this experiment, one-hot encoding was used to convert 24
class categorical class labels into a binary vector representation. The
resulting binary vectors contain all zero values except for the index
corresponding to the class label, which is set to 1. The nnTrainer.py
and processing pipeline.py scripts were then used to partition the
subset into a 75:25 split for the training and test sets, respectively.

C. Neural Network Trainer

In this experiment, a 1-dimensional Convolutional Neural Network
(1D CNN) was developed, featuring four convolutional blocks la-
belled as b1, b2, b3, b4, each with an associated ﬁlter size of 64,

Fig. 8: Architectural schematic of 1D Convolutional Neural Network

128, 128, and 256, respectively, providing varying levels of recep-
tivity (Fig.8). Each block contains a convolutional layer with ReLU
activation and batch normalisation to capture spatial dependencies.
Furthermore, a max pooling layer was added to each block to reduce
spatial dimensionality. The output vector from b4 is ﬂattened and fed
into the models classiﬁcation block which has three dense layers. The
ﬁrst two dense layers contain 128 fully connected neurons with ReLU
activation units, while the third layer incorporates a softmax activation
function to produce an output vector of multiple probabilities. Cate-
gorical cross-entropy loss was used to optimise the learning process
in conjunction with the Adam optimisation technique. To enhance
numerical stability, the optimiser’s epsilon score and learning rate
were reduced to 1e-05 and 0.0001, respectively. The toolkit can be
used to visualise the models learning rate by plotting accuracy and
loss scores for training and validation sets (Fig.9-10).

TABLE VI: Hyper parameter conﬁguration used for 1D CNN model

Id

1
2
3
5

Hyper Parameter

Train/Test split
Validation Set
Training Epochs
Batch Size

Optimisation Metric

75:25
0.1
50
24

Fig. 9: A visual representation of accuracy and validation accuracy
plotted by the Open Seizure Toolkit”

Fig. 10: A visual representation of loss and validation loss plotted
by the Open Seizure Toolkit”

J PORDOY et al.: PREPARATION OF BRIEF PAPERS FOR IEEE TRANSACTIONS AND JOURNALS (FEBRUARY 2017)

9

Fig. 11: Multi-class Confusion Matrix: Evaluating the models ground truth and predicted class labels.

Fig. 12: 1D Convolutional Neural Network detecting a ”tonic-clonic” event: A visualisation plot illustrating how the model classiﬁes a
tonic-clonic seizure. The upper x-axis plots the models predicted labels for each timestep where 0 = no seizure and 1 = tonic clonic seizure.

Fig. 13: 1D Convolutional Neural Network detecting an ”Other Seizure” event: A visualisation plot showcasing the model’s accurate
classiﬁcation of convulsive movement. The upper x-axis plots the models predicted labels for each 5 second timestep

10

GENERIC COLORIZED JOURNAL, VOL. XX, NO. XX, XXXX 2017

TABLE VII: Summary of the overall classiﬁcation results detailing
the performance of the 1D Convolutional Neural Network

TABLE VIII: Summary of 1D Convolutional Neural Network clas-
siﬁcation results, measuring precision, recall and f1-scores for each
class

Id

Classiﬁcation Metric

Abbreviation Classiﬁcation Result

True Positive Rate
False Positive Rate
Positive Predictive Value

1
2
3
4 Matthews Correlation Coefﬁcient
5
6
7
8
9
10
11
12
14

False Negative Rate
True Negative Rate
False Discovery Rate
Accuracy
Speciﬁcity
Prevalence
F1-Score
False Omission Rate
Informedness

TPR
FPR
PPV
MCC
FNR
TNR
FDR
ACC
SPC
PREV
F1
FOR
BM

0.998
0.071
0.941
0.933
0.002
0.929
0.059
0.966
0.929
0.532
0.969
0.003
0.927

V. EXPERIMENTS & RESULTS
This section presents the experiments conducted using the OSTK
and and the results achieved. The 1D CNN was trained for 50 epochs,
and recorded accuracy and loss scores of 0.959 and 0.1412 receptivity.
The model was then evaluated on an unseen test set, and recorded
an accuracy score of 92.75% with 0.298 loss. A full breakdown of
the models overall performance is detailed in TABLE VII.

The OSTK Data Summariser was utilised to plot a multi-class
confusion matrix, visualising the model’s predicted and ground truth
labels for the 24 classes used in these experiments. An analysis of
the confusion matrix demonstrated how well the model distinguishes
between the different classes.

For the ”O Seizure” class, 810 true positives (TP) were accurately
detected, however, 48 instances of ”Tonic-Clonic,” 15 ”Aura/focal,”
and 58 ”Atonic/fall” were misclassiﬁed. Additionally, 8 instances
were labelled as ”Sleeping” and 13 as ”Other”.

Further analysis of the ”Tonic-Clonic” class classiﬁed 743 TP in-
stances. However, 7 instances were misclassiﬁed as ”Other Seizure,”
7 as ”Aura/focal” and 18 as ”Atonic/fall”. Furthermore, 14 instances
were incorrectly labelled as common human movements, with 9
instances labelled as ”Sleeping” and 5 as ”Other”.

An analysis of the ”Atonic/fall” class revealed 734 TP instances,
with only 2 instances inaccurately classiﬁed as ”Aura/focal”. More-
over, a single instance each of ”Tonic-Clonic” and ”Unknown” were
misclassiﬁed, whilst there were no incorrect classiﬁcations associated
with the ”Other Seizure” class. These results demonstrate the model’s
ability to differentiate between ”Atonic/fall” and ”Other Seizure”
classes.

For the ”Aura/focal” class, the model accurately identiﬁed 897
TP instances. However, 56 instances were incorrectly labelled as
”Atonic/focal”, 25 as ”Other Seizure” and 115 as ”Tonic-Clonic”.
A further 13 labels were incorrectly classiﬁed as ”Unknown”, 27 as
”sleeping” and 60 as ”Other”. However, these ﬁndings were expected,
as a considerable proportion of GTC seizures exhibit an aura (pre-
ictal) phase. A further analysis shows that GTC seizures have an
average clonic phase lasting 25 to 35 seconds after generalisation.
Therefore a degree of similarity between these classes is to be
expected and highlights the importance of considering the dynamics
of each sub-event. Overall the model has demonstrated a clear ability
to differentiate between the ”Other Seizure” and ”Atonic/fall” classes,
as well as ”Aura/focal” and ”Atonic/fall”. However, there were chal-
lenges distinguishing between the ”Tonic-Clonic” and ”Aura/focal”
classes.

Class ID

Type

Sub Type

Precision

Recall

F1 Score

c1
c2
c3
c4
c5
c6
c7
c8
c9
c10
c11
c12
c13
c14
c15
c16
c17
c18
c19
c20
c21
c22
c23
c24

Other

Atonic/Fall
Seizure
Aura
Seizure
Brush Teeth
False Alarm
Other Seizure
Seizure
Cycling
False Alarm
Fidgeting
False Alarm
Gaming
False Alarm
Hammock
False Alarm
False Alarm
Lying Down
False Alarm Motor Vehicle
False Alarm
False Alarm Pushing Pram
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
False Alarm
Seizure
False Alarm
False Alarm
False Alarm Washing Up

Scratching
Shaving
Shopping
Sleeping
Sneezing
Sorting
Standing
Talking
Tonic-Clonic
Typing
Unknown

0.84
0.61
1.00
0.85
0.55
1.00
0.98
1.00
1.00
0.96
0.96
0.48
0.98
1.00
1.00
0.76
1.00
0.90
0.85
0.95
0.86
0.82
0.76
0.98

0.83
0.83
0.97
0.88
0.84
0.96
0.83
0.78
0.81
0.94
0.97
0.71
1.00
1.00
1.00
0.61
1.00
0.95
0.81
0.46
0.71
0.93
0.72
1.00

0.83
0.71
0.98
0.87
0.67
0.98
0.90
0.87
0.89
0.95
0.97
0.58
0.99
1.00
1.00
0.68
1.00
0.92
0.83
0.62
0.78
0.88
0.74
0.99

Table VIII summarises the classiﬁcation results for each class.
For the purpose of these experiments, the results will be focused
on the four classes of seizure. For the ”Tonic-Clonic” class denoted
in the results as c21, the model achieved a precision score of 0.94
and a recall of 0.77. These metrics signify that 86% of positive
predictions were correct, while the recall indicates that 23% of true
instances of c21 were incorrectly classiﬁed. For c2 (Aura), the model
demonstrated a precision of 0.75, indicating that 75% of the instances
predicted were correct. However the recall score of 0.93 highlights
the model’s ability to correctly identify 93% of actual instances of
c2. An analysis of c1 (Atonic/fall) recorded a precision score of
0.99, signifying that 99% of the instances predicted as c1 were true
instances. Nonetheless, a recall score of 0.76 suggests that the model
is overcompensating and classifying to many instances of c1, which
has lead to a trade-off between the precision and recall scores. For
c4 (Other Seizure), the model displayed a balanced performance,
recording a precision, recall, and F1-score of 0.84. A precision score
of 84% indicates a relatively low false positive rate and demonstrates
a high level of accuracy when classifying classifying TP instances of
c4. Furthermore, a recall score of 84% demonstrated the number of
true instances correctly classiﬁed by c4.

To provide a comprehensive assessment, an F1-score was computed
for each class type, resulting in values of 0.86, 0.83, 0.84, and 0.85 for
c1, c2, c4 and c21, respectively. F1-score results indicate a realistic
trade-off between correctly identifying positive instances (recall) and
minimising false positives (precision) for each class. In summary,
the model’s performance demonstrates a clear ability to accurately
classify seizure-related classes while maintaining a balance between
precision and recall.

J PORDOY et al.: PREPARATION OF BRIEF PAPERS FOR IEEE TRANSACTIONS AND JOURNALS (FEBRUARY 2017)

11

VI. DISCUSSION

This study introduces the Open Seizure Database and Toolkit, a
publicly available resource designed to facilitate scientiﬁc investi-
gation into non-EEG seizure detection. The primary objective of
this research is to address the scarcity of resources in the ﬁeld of
non-EEG seizure detection by establishing the OSDB as the ﬁrst
openly accessible database encompassing non-EEG sensor data from
multiple sensing modalities.

This study distinguishes itself by utilising real-world data, provid-
ing an accurate depiction of everyday life compared to controlled
EMU-based datasets. The beta trial’s success led to an indeﬁnite
extension of the data collection period, showcasing our commitment
to continually enriching the OSDB and contributing to non-EEG
seizure detection research.

The initial version of the OSDB is comprised of 494 events
collected over 453 days, with each event labelled and optimised for
machine/deep learning. Among these events, 146 epileptic seizures
were recorded; 50 GTC seizures, 47 Other seizures, 27 aura/focal,
and 22 atonic/falls. The cumulative duration of recorded epileptic
events amounts to 5 hours, 51 minutes, making it the most extensive
publicly available cohort of non-EEG seizure data to date.

Additionally, 302 common human movements that triggered false
alarms during the data collection period were recorded and labelled. A
further 46 events were classiﬁed as false alarms, where the triggering
activity remains unidentiﬁed. The inclusion of labelled false alarms
in the dataset offers a valuable resource to address the challenge of
false positives in non-EEG seizure detection.

A. Future Research

The introduction of the OSDB sets forth several possibilities for
future research. As the data collection process is extended indeﬁnitely,
individuals with epilepsy can continue to participate and contribute
data. As more data is collected, the exploration of novel techniques
such as patient-speciﬁc and seizure-speciﬁc detection becomes a
possibility. However, due to the dataset’s current size, dedicated
classiﬁcation models cannot be trained for these concepts yet. Nev-
ertheless, as more data accumulates over time, these concepts will
become feasible.

VII. CONCLUSION

In conclusion, the introduction of the OSDB and OSTK represents
a signiﬁcant milestone in non-EEG seizure detection research,
providing a valuable resource to overcome existing scarcity in this
domain. With real-world data collected from in-home environments,
researchers can explore diverse multimodal approaches for seizure
detection. The OSDBs extensive data on epileptic seizures and
labelled false alarms presents a unique opportunity to advance
the ﬁeld. With continued data collection and exploration of novel
techniques, the OSDB and OSTK has the promise of establishing a
non-EEG gold standard and ultimately improving seizure detection
techniques. Researchers investigating non-EEG detection can access
the dataset, code, and models through the ofﬁcial OSDB GitHub
repository.

Acknowledgements: A heartfelt thank you to all the participants.
Your invaluable contributions have been instrumental in advancing
non-EEG seizure detection research. Your commitment has paved
the way for exploring new possibilities and making a positive impact
on the lives of those affected by epilepsy. We are deeply grateful
for your support and dedication.

Open Seizure Database (OSDB):: See https://github.
com/OpenSeizureDetector/OpenSeizureDatabase for
instructions on how to access the Open Seizure Database.

Open Seizure Database Licence: A summary of the licence under
which the Open Seizure Database is released can be accessed
https://github.com/OpenSeizureDetector/
at
OpenSeizureDatabase/blob/main/documentation/
LICENCE.md

Informed Consent Statement: The users gave their consent
to publish the developed database by agreeing to the Privacy
Policy at https://github.com/OpenSeizureDetector/
OpenSeizureDatabase/blob/main/documentation/
Privacy_Policy.pdf

Data Collection and Data Sharing: Details of the beta trial,
data collection and data sharing can be viewed at https:
//www.openseizuredetector.org.uk/?page_id=1818

Conﬂicts of Interest: The authors declare that there is no conﬂict
of interest regarding the publication of this manuscript.

REFERENCES

[1] O. Devinsky et al., Epilepsy, Nature Reviews Disease Primers., vol. 4,

pp. 18024, May 2018.

[2] M. Sperling, Sudden Unexplained Death in Epilepsy, Epilepsy currents,

vol. 1(1), pp. 21-23, Sep 2001.

[3] O. Sveinsson et al., Clinical risk factors in SUDEP: A nationwide
population-based case-control study, Neurology, vol. 94(4), pp. e419-
e429, Dec 2019.

[4] T. Manolis et al., Sudden unexpected death in epilepsy: The Neuro

Cardio Respiratory Connection, Seizure, vol. 64, pp. 65-73, Jan 2019.

[5] R. Surges et al., Sudden unexpected death in epilepsy: risk factors and
potential pathomechanisms, Nat Rev Neurol, vol. 5(9), pp. 492-504, Sep
2009.

[6] R.J. Lamberts et al., Sudden unexpected death in epilepsy: People with
nocturnal seizures may be at highest risk, Epilepsia, vol. 53(2), pp. 253-
257, Feb 2012.

[7] O. Sveinsson et al., Clinical risk factors in SUDEP, Neurology, vol. 94,

pp. e419-e429, Jan 2020.

[8] M. Thom et al., Sudden and unexpected death in epilepsy (SUDEP):
evidence of acute neuronal injury using HSP-70 and c-Jun immunohis-
tochemistry, Neuropathol Appl Neurobiol, vol. 29(2), pp. 132-43, Apr
2003.

[9] I. Conradsen et al., Detection of generalised tonic-clonic seizures by a
wireless wrist accelerometer: a prospective, multicenter study, Epilepsia,
vol. 56, pp. e83-e87, Apr 2015.

[10] J. Lockman et al., Detection of seizure-like movements using a wrist

accelerometer, Epilepsy Behaviour, vol .22, pp. S64-S68, Apr 2011.

[11] S. Zia et al., Detection of Generalised Tonic Clonic Seizures and Falls
in Unconstraint Environment Using Smartphone Accelerometer, IEEE
Access, vol. 9, pp. 39432-39443, Dec 2021.

[12] J. Villar et al., Generalised Models for the Classiﬁcation of Abnormal
Movements in Daily Life and its Applicability to Epilepsy Convulsion
Recognition, Int J Neural Sys, vol. 26, pp. 1650037, Apr 2016.
[13] L. Billeci et al., Patient-speciﬁc seizure prediction based on heart rate
variability and recurrence quantiﬁcation analysis, PLOS ONE, vol. 13,
pp. e0204339, Sep 2018.

[14] I. Al-Aweel et al., Postictal heart rate oscillations in partial epilepsy,

Neurology, vol. 53, pp. 1590-1592, Oct 1999.

[15] F. P´erez-Garc´ıa et al., Transfer Learning of Deep Spatiotemporal Net-
works to Model Arbitrarily Long Videos of Seizures, Medical Image
Computing And Computer Assisted Intervention, MICCAI 2021, pp.
334-344, Jun 2021.

[16] J. Pordoy et al., Predicting Epileptic Seizures with a Stacked Long Short-
Term Memory Network, Int J Auto AI Mach Learn, vol. 1(1), pp. 93-108,
Oct 2020.

12

GENERIC COLORIZED JOURNAL, VOL. XX, NO. XX, XXXX 2017

[43] The Open Seizure Database Licence, Open Seizure Detec-
tor,Hartlepool, UK, 2022. [Online] Available: https://github.
com/OpenSeizureDetector/OpenSeizureDatabase/
blob/main/documentation/LICENCE.md

[17] G. Regalia et al., Multimodal wrist-worn devices for seizure detection
and advancing research: Focus on the Empatica wristbands,Epilepsy Res,
vol. 153, pp. 79-82, Feb 2019.

[18] F. Onorati et al., Performance of a wrist-worn multimodal seizure
detection system for more than a year in real-life settings,13th European
congress on Epileptology, Aug 2018.

[19] F. Onorati et al., Multicenter clinical assessment of improved wearable
multimodal convulsive seizure detectors, Epilepsia, vol. 58(11), pp.
1870-1879, Nov 2017.

[20] M.Z. Poh et al., Autonomic changes with seizures correlate with postictal
EEG suppression, Neurology, vol. 78(23), pp. 1868–1876, 2012.
[21] M. Nasseri et al., Non-invasive wearable seizure detection using
long–short-term memory networks with transfer learning, J. Neural Eng,
vol. 18, pp. 056017, Apr 2021.

[22] J. Nielsen et al., Out-of-hospital multimodal seizure detection: a pilot

study, BMJ Neurology Open, vol. 5, Aug 2023.

[23] A. Van de Velet al.,Non-EEG seizure detection systems and potential
SUDEP prevention: State of the art: Review and update, Seizure, vol.
41, pp. 141-153, 2016,

[24] D. Friedman and C. Kazl, Seizure Detection and SUDEP Prevention,

Practical Neurology. pp. 54-58 Nov 2018.

[25] M. Ihle et al., EPILEPSIAE – A European epilepsy database, Computer
Methods And Programs In Biomedicine, vol. 106(3), pp. 127-138, Sep
2012.

[26] A. Dourado et al., Giving hope to refractory epileptic patients, IST-Africa

Conference Proceedings, pp. 1-10, May 2014.

[27] P. Thompson et al., Data sharing in epilepsy research, Epilepsia, vol.

54, pp. 576-582, 2013.

[28] The Open Seizure Database (OSDB), Open Seizure Detector, Hartle-
[Online] Available: https://github.com/

pool, UK, 2022.
OpenSeizureDetector/OpenSeizureDatabase

[29] Open

Seizure Detector, Open

pool, UK,
2013.
openseizuredetector.org.uk

[Online] Available:

Seizure Detector, Hartle-
https://www.

[30] University of West London, University of West London, London,
UK, 2022. [Online] Available: https://www.uwl.ac.uk
[31] Open Seizure Detector, Open Seizure Detector, Hartlepool, UK,
2013. [Online]. Available: play.google.com/store/apps/
details/?id=uk.org.openseizuredetector

[32] Google Play Open Testing(Google Play Store), 2023. [Online]
Available: https://play.google.com/console/about/
opentesting/

[33] Informed Consent Statement, Open Seizure Detector, Hartlepool,
[Online] Available: https://github.com/

UK,
OpenSeizureDetector/OpenSeizureDatabase/blob/
main/documentation/Privacy_Policy.pdf

2022.

[34] Accelerometer Data, Garmin Ltd, 2022.

[Online] Available:

https://developer.garmin.com/connect-iq/
core-topics/sensors/

[35] Heart Rate Monitoring, Garmin Ltd, 2022. [Online] Available:

https://developer.garmin.com/connect-iq/
core-topics/sensors/
[36] Pulse Oximetry, Garmin

2022.

Ltd,

[Online] Available:

www.garmin.com/en-GB/garmin-technology/
health-science/pulse-ox

[37] A. Oppenheim and R. Schafer, Discrete-time signal processing,

Pearson, 2010.

[38] R. Khusainov et al., Real-time human ambulation, activity, and
physiological monitoring:
techniques, ap-
taxonomy of
plications, challenges and limitations, Sensors, pp. 13(10), pp.
12852–12902, 2013.

issues,

[39] H. Joo et al., Spectral Analysis of Acceleration Data for Detection
of Generalised Tonic-Clonic Seizures, Sensors, pp. 17(3), pp. 481,
Feb 2017.

[40] Garmin Seizure Detector Performance, Open Seizure Detec-
tor, Hartlepool, UK, 2019. [Online] Available: https://www.
openseizuredetector.org.uk/?pageid=1341

[41] A. Harvey and M. Cerna, The Fundamentals of FFT-Based Signal

Analysis and Measurement in LabVIEW and LabWindows, 1993.

[42] W. Yuan and K. Gao, EAdam Optimizer: How e Impact Adam,

ArXiv: Learning, pp. 2011.02150, 2020.
