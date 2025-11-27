# Hamlin et al. - 2021 - Assessing the feasibility of detecting epileptic seizures using non-cerebral sensor data

Contents lists available at ScienceDirect 

Computers in Biology and Medicine 

journal homepage: http://www.elsevier.com/locate/compbiomed 

Assessing the feasibility of detecting epileptic seizures using non-cerebral 
sensor data 

Alexandra Hamlin a, Erik Kobylarz b, James H. Lever c, Susan Taylor c, Laura Ray a,* 
a Thayer School of Engineering, Dartmouth College, United States 
b Geisel School of Medicine, Dartmouth College, Thayer School of Engineering, Dartmouth College (adjunct Appointment); and Dartmouth-Hitchcock Medical Center, 
United States 
c Dartmouth College (adjunct Appointment) and U.S. Army ERDC, United States   

A R T I C L E  I N F O    

A B S T R A C T    

Keywords: 
Biomedical computing 
Decision-support systems 
Wearable sensors 
Machine learning 
Biomedical signal processing 

This paper investigates the feasibility of using non-cerebral, time-series data to detect epileptic seizures. Data 
were recorded from fifteen patients (7 male, 5 female, 3 not noted, mean age 36.17 yrs), five of whom had a total 
of seven seizures. Patients were monitored in an inpatient setting using standard video-electroencephalography 
(vEEG), while also wearing sensors monitoring electrocardiography, electrodermal activity, electromyography, 
accelerometry, and audio signals (vocalizations). A systematic and detailed study was conducted to identify the 
sensors and the features derived from the non-cerebral sensors that contribute most significantly to separability 
of  data  acquired  during  seizures  from  non-seizure  data.  Post-processing  of  the  data  using  linear  discriminant 
analysis (LDA) shows that seizure data are strongly separable from non-seizure data based on features derived 
from the signals recorded. The mean area under the receiver operator characteristic (ROC) curve for each in-
dividual patient that experienced a seizure during data collection, calculated using LDA, was 0.9682. The fea-
tures  that  contribute  most  significantly  to  seizure  detection  differ  for  each  patient.  The  results  show  that  a 
multimodal approach to seizure detection using the specified sensor suite is promising in detecting seizures with 
both sensitivity and specificity. Moreover, the study provides a means to quantify the contribution of each sensor 
and feature to separability. Development of a non-electroencephalography (EEG) based seizure detection device 
would give doctors a more accurate seizure count outside of the clinical setting, improving treatment and the 
quality of life of epilepsy patients.   

1. Introduction 

Around 65 million people worldwide have epilepsy, and about 3.4 
million of these people live in the U.S [1,2]. Of people with epilepsy, 
20–40% have refractory epilepsy, which means typical epilepsy medi-
cations do not control their seizures [3]. In order for doctors to prescribe 
the correct medication and gain an understanding of how epilepsy in-
terferes  with  a  patient’s  life,  they  rely  on  the  patient’s  self-reported 
accounts  of  seizures.  However,  a  study  by  Hoppe  et  al.  [4]  revealed 
that patients monitored in an Epilepsy Monitoring Unit (EMU) failed to 
report 55.5% of all seizures. When asked, 36 of the 91 patients (40%) 
believed  they  were  fully  aware  of  their  seizures,  yet  their  reporting 
showed that only 11 patients (12%) were able to accurately record all of 
their  seizures.  Experiments  such  as  this  have  been  reproduced  with 
similar conclusions drawn [5,6]. 

Currently, the gold standard for seizure monitoring and detection is 
combined  video  and  electroencephalography  (vEEG)  recording  con-
ducted in an EMU. While vEEG provides the most accurate results for 
seizure detection, it requires patients to wear numerous electrodes on 
their  scalp  (typically  at  least  25)  and  be  continuously  videotaped, 
making  it  unrealistic  for  everyday  use.  Furthermore,  trained  pro-
fessionals  need  to  review  the  EEG  data  to  identify  seizures.  Conse-
quently, a method is needed to accurately count seizures during day-to- 
day activity outside of a clinical setting. 

Epileptic seizures can present a wide range of observable behaviors 
that relate to the nature of their onset and propagation within the brain. 
Table  1  provides  brief  descriptions  of  common  seizure  types.  The 
observable changes in patient motion, vocalization, and physiological 
response during seizures offer non-cerebral signals that could be used to 
detect seizures. This paper presents a study whose aim is to determine 

* Corresponding author. 

E-mail address: lray@dartmouth.edu (L. Ray).  

https://doi.org/10.1016/j.compbiomed.2021.104232 
Received 6 September 2020; Received in revised form 13 January 2021; Accepted 17 January 2021   

ComputersinBiologyandMedicine130(2021)104232Availableonline21January20210010-4825/©2021ElsevierLtd.Allrightsreserved.A. Hamlin et al.                                                                                                                                                                                                                                 

Table 1 
Common Seizure Types and their Manifestation.  

Type 

Manifestation 

Tonic-Clonic 
Clonic 
Tonic 
Myoclonic 
Atonic 
Absence (Petit Mal) 
Simple Focal 
Complex Focal 
Secondary 

Generalized 

Muscle stiffening, jerking, shaking, loss of consciousness 
Rhythmic muscle spasms or jerking 
Muscle tensing 
Sudden muscle jerk as if shocked 
Loss of muscle tone 
Blank staring, lack of responsiveness 
Change in smell or taste, extremity twitching, sweating 
Loss of consciousness, repetitive motions, e.g., lip smacking 
Muscle shaking or loss of tone  

whether seizure activity of many types is separable from daily activities. 
Establishing  separability  is  the  first  step  towards  developing  a  body- 
worn  device  for  seizure  detection  using  non-cerebral  signals.  Sepa-
rating  seizure  behavior  from  long  intervals  of  normal,  non-seizure 
behavior  is  the  key  task  of  any  detection  scheme  and  is  critical  to 
avoiding  frequent  “nuisance”  alarms  from  false  detections.  Hence 
separability is the central focus of this study. 

To assess separability, we used linear discriminant analysis (LDA) on 
features  derived  from  data  recorded  from  inpatients  via  electrocardi-
ography, electrodermal activity, electromyography, accelerometry, and 
audio signal monitoring. The results presented in this paper will guide 
the design of a self-contained device comprised of sensors and a real- 
time machine learning algorithm. The goal is a device that accurately 
detects and counts seizures occurring outside of the clinical setting with 
minimal interference on normal life. Establishing separability is the first 
step in the design process. 

2. Prior research 

Several research teams have investigated the use of accelerometers 
placed on or under mattresses to detect a patient’s nocturnal seizures 
[7–10]. Other researchers have explored monitoring sleep through video 
and audio monitoring [11–14]. These studies have shown mixed results 
and are only useful for detecting convulsive seizures in a specific room. 
Wearable  devices  have  been  studied  to  detect  convulsive  seizures 
specifically,  which  are  associated  with  repeated,  jerking  motions  of 
various parts of the body and are dissimilar to motions that occur during 
day-to-day life. The movements of convulsive seizures are observable in 
several signals such as accelerometry and electromyography (EMG). 

In accelerometry signals, myoclonic, tonic clonic, and clonic seizures 
appear  distinct  from  each  other  and  from  normal  movements.  A 
myoclonic seizure is characterized by muscle jerks that frequently occur 
in clusters [15]. At the end of a myoclonic seizure the patient goes limp 
and falls to the nearest surface, which manifests as a sudden spike in 
accelerometry  data.  During  a  tonic  seizure,  a  person’s  body  becomes 
rigid  [16].  Tonic-clonic seizures are  tonic seizures  followed  by clonic 
seizure, characterized by rapid jerking or shaking [17]. These seizure 
types appear distinct from each other and from normal movements in 
accelerometry data. 

Nijsen et al. [18] monitored 18 patients with severe epilepsy for 36 h 
each and observed a total of 897 seizures through a combination of vEEG 
and accelerometry monitoring. The researchers report that 78% of sei-
zures had a stereotypical tonic pattern, 74% a stereotypical myoclonic 
pattern, 14% a stereotypical clonic pattern, and 57% were preceded by a 
myoclonic seizure. Overall, they found that they were able to detect 48% 
of  all  seizures  that  occurred  using  accelerometry.  Other  studies  have 
shown  higher  convulsive  seizure  detection  rates  using  accelerometry 
alone [19–28]. Although accelerometry is useful for detecting convul-
sive seizures, it is not useful for detecting other types of seizures. 

EMG,  which  measures  muscle  activation,  is  also  used  to  detect 
convulsive seizures [21,29,30]. A myoclonic seizure, when a person’s 
body falls limp upon conclusion of the seizure, would also be visible in 

EMG signals as all muscle activation would end suddenly. Like accel-
erometry, EMG is most useful in detecting convulsive seizures, but does 
not detect all seizure types. 

To  detect  non-convulsive  seizures,  non-movement-based  signals 
must be recorded using other sensors. During seizures, the autonomic 
nervous system is frequently activated, leading to variations in several 
biosignals. One of the most common changes during an epileptic seizure 
is  an  increase  in  heart  rate  due  to  the  activation  of  the  sympathetic 
nervous system [31–39]. Sinus tachycardia, or when the heart rate rises 
above 100 beats per minute, has been reported to occur in as many as 
99%  of  seizures  and  frequently  precedes  the  seizure  onset  by  several 
seconds  [34].  More  importantly,  potentially  serious  changes,  such  as 
ST-depressions  and  T-wave  inversions  in  the  electrocardiogram,  were 
seen in 39% of seizures [37]. Heart rate variability also frequently in-
creases during seizures, allowing researchers to differentiate between an 
increase in heart rate due to seizures and other daily activity such as 
exercise  [38].  Still,  ECG  alone  is  not  adequate  for  accurate  seizure 
detection. 

Activation  of  the  autonomic  nervous  system  during  seizures  also 
increases sweating, which can be detected through electrodermal (EDA) 
sensors [40]. However, people sweat for various reasons, so EDA is most 
useful  when  combined  with  other  modalities.  Thus,  researchers  have 
generally tested devices using EDA in conjunction with other sensors. 

While many modalities are clearly useful in detecting seizures, none 
so far have been able to detect all types of seizures because of the wide 
variety of seizure manifestations. Several researchers have begun testing 
devices  that  use  multiple  modalities  with  mixed  outcomes  [41–46]. 
These studies relate most closely to the work presented in this paper. 

Miloˇsevi´c  et  al.  [41]  reports  results  using accelerometry,  but with 
added EMG sensors. They monitored 56 patients overnight, 7 of whom 
had a total of 22 seizures. Using a least-squares support vector machine 
(SVM),  they  were  able  to  detect  91%  of  short  and  non-stereotypical 
seizures.  Cogan  et  al.  [42]  presents  a  multimodal  seizure  detection 
system  that  uses  a  three-stage  detection  algorithm  with  photo-
plethysmography  (PPG)  to  monitor  heart  rhythm,  oxygen  saturation 
measurements to observe breathing, and electrodermal activity (EDA) to 
evaluate sweating. Stage I quantifies signal activities, compares them to 
previous epochs of data, and looks specifically for an increase in heart 
rate followed by a decrease in oxygenation and then an increase in EDA 
consecutively.  Stage  II  personalizes  the  algorithm  by  patient  using 
pattern  recognition  and  adjusting  parameter  levels.  Stage  III  in-
corporates  a  limited  suite  of  EEG  channels  into  the  detection.  Cogan 
et al. [42] found that 100% of seizures were detected using Stages I and 
II  alone  from  six  of  the  ten  patients  who  had  seizures.  Interestingly, 
Cogan et al. noted that their algorithm either detected all or none of an 
individual patient’s seizures, so they assessed accuracy by patient rather 
than total seizure detection count. They were able to detect generalized 
tonic-clonic seizures more reliably than other seizure types, as expected, 
due to their more convulsive presentation. Finally, after incorporating 
three-channel  EEG  data  into  their  analysis,  Cogan  et  al.  were  able  to 
detect 100% of seizures from eight of their ten patients [42]. Nonethe-
less, this would require placing electrodes on a patient’s head during 
daily life, which is intrusive. 

Becq  et  al.  [43]  used  magnetic  sensors  and  accelerometers  on  the 
arms and forehead to analyze 226 seizures in nine patients. Their goal 
was not to classify data as seizure or non-seizure, but to identify the type 
of seizure based on its motor manifestation. They artificially grew their 
dataset by duplicating each event 30 times and adding random noise. 
Then,  they  classified  motor  manifestation  using  an  artificial  neural 
network.  This  process  resulted  in  20%  error  between  machine  and 
standard vEEG analysis. 

Poh et al. [44] used a Smartband [40,46] to record over 4000 h of 
data from 80 patients in an EMU. Though the Smartband includes more 
signals, they consider the accelerometry and EDA data in Ref. [44]. They 
analyze 10-s epochs of data using a 19-feature SVM. Their cross vali-
and 
dation 

leave-one-patient-out 

considered 

analysis 

both 

ComputersinBiologyandMedicine130(2021)1042322A. Hamlin et al.                                                                                                                                                                                                                                 

Table 2 
Summary of Patients monitored during study and Seizures Recorded.  

Patient 

Gender 

Age 

Seizures 

Seizure Type 

Aa 
Ba 
Ca 
Da 

E 
F 
G 
H 
I 

J 
K 
L 

A 

M 
N 

F 
n.n 
n.n 
n.n 

M 
M 
F 
F 
M 

M 
F 
F 

F 

M 
M 

Length 
(h) 

21.01 
7.6 
19.87 
21.77 

44.88 
4.44 
19.43 
21.03 
75.85 

3.72 
2.65 
12.4 

42 
n.n 
n.n 
n.n 

51 
21 
36 
36 
41 

n.n 
47 
21 

42 

37.31 

27 
32 

16.44 
66.72 

0 
0 
0 
4 

0 
0 
0 
0 
2 

0 
0 
1 

2 

0 
1 

O 

M 

58 

7.67 

1 

TOTAL 

7 M 5F 

36.2 

382.8 

11 

N/A 
N/A 
N/A 
Complex partial, non- 
convulsive 
N/A 
N/A 
N/A 
N/A 
Complex partial originating 
in the left temporal lobe 
N/A 
N/A 
Psychogenic non-epileptic 
seizure (PNES) 
Complex partial originating 
in the left temporal lobe 
N/A 
Partial originating in the left 
temporal lobe with secondary 
generalization, showed tonic 
clonic activity 
Partial motor originating in 
the right frontal lobe with 
secondary generalization 
6 Complex Partial 
2 Partial with Secondary 
Generalization 
2 Partial Motor 
1 Psychogenic Non-Epileptic 

‘n,n,’ indicates that the information was not noted. 

a Recorded with first system. 

leave-one-seizure-out  metrics.  Overall,  they  detected  15  of  16  (94%) 
seizures. With this sensitivity, they also observed about one false posi-
tive per 24-h period, or a total of 28 false alarms. This gives a positive 
predictive value of 0.36. 

Heldberg  et  al.  [45]  also  studied  the  Smartband  and  also  only 
considered  EDA  and  accelerometry  signals.  Eight  patients  that  had  a 
total  of  55  seizures  over  the  540  h  of  data  recorded.  The  data  were 
processed using 10 s windows with 50% overlap as well as 5-min win-
dows with 80% overlap, then passed through a 1.5 Hz low-pass filter 
before  extracting 26  features.  A 10-tree random  forest and  kNN clus-
tering with k = 5 algorithm were both tested. An overall sensitivity of 
89.1% and a specificity of 93.1% were achieved. The precision was low 
at  7.5%,  indicating  a  high  rate  of  false  positives.  For  predominantly 
non-motor  seizures,  they  achieved  a  sensitivity  of  97.1%  with  9.6% 
precision and 92.9% specificity, also using kNN clustering. Overall, re-
sults from this study indicate that there is still a need for a more reliable 
seizure detection device. 

While  some  methods  are  able  to  detect  specific  types  of  seizures, 
none  are  able  to  detect  all  types  reliably.  Generally,  modalities  that 
monitor movement, such as accelerometry and electromyography, are 
useful  in  identifying  convulsive  seizures.  Other  modalities,  such  as 
electro-cardiography  and  electrodermal  activity,  have  proven  to  be 
useful in detecting non-convulsive seizures. Because some modalities are 
more  useful  in  detecting  specific  types  of  seizures,  combining  many 
modalities should enable a larger range of seizure type detection. Thus, 
we hypothesize that combining several non-cerebral sensing modalities, 
and carefully choosing features that characterize the signals, will allow 
us to detect many seizure types. Moreover, a detailed study of separa-
bility of seizure and non-seizure activity will aid in identifying the most 
important sensors and features for seizure detection. 

3. Methods 

3.1. Dataset 

The data for this study is recorded from fifteen patients in an epilepsy 
monitoring unit (EMU). Both male and female patients between ages 18 
and 70 years old scheduled for admission to the Dartmouth-Hitchcock 
Medical  Center  EMU  were  screened  for  potential  recruitment  to  the 
study. All patients or their legal guardians gave informed written con-
sent following an Institutional Review Board protocol. Inclusion criteria 
were broad; both patients with poorly controlled seizures of partial (e.g., 
motor) onset that may or may not secondarily generalize, and patients 
experiencing primary generalized seizures (e.g., myoclonic and atypical 
absence with or without automatisms such as stereotypical facial and/or 
limb movements) were included in the study. The study called for pa-
tients who experience seizures on a relatively frequent basis to provide 
sufficient data for analysis. While being monitored, however, the ma-
jority of patients experienced no seizures, some experienced only one or 
two seizures and  one patient experienced four seizures.  Table 2 sum-
marizes the main categories and manifestations of seizures experienced 
by each patient. 

While in an EMU, patients are monitored using both EEG and video. 
In standard monitoring, doctors examine a patient’s EEG and note when 
seizures occur. These seizures are then verified with the video record. 

In this study, patients were simultaneously monitored with standard 
vEEG  recording  as  well  as  with  electrocardiograph  (ECG), electromy-
ography  (EMG),  electrodermal  activity  sensors  (EDA),  photo-
plethysmography (PPG), accelerometer (ACC), and a microphone. The 
vEEG data are used to hand-label the non-cerebral sensor data, i.e., to 
determine what patients were doing at different times, and to define the 
time of seizure onset and conclusion. To synchronize recording times 
with  vEEG,  a  digital  clock  was  placed  in  view  of  the  EMU’s  video 
camera. 

Data were collected over two separate time periods using different 
hardware. The original data set acquired for analysis by Azad et al. [47] 
used two Biopac MP36 data acquisition systems to collect patient data. 
One Biopac MP36 sampled the three accelerometer axes and a micro-
phone at 50,000 Hz, while the other sampled ECG, EMG, and EDA sig-
nals at 5000 Hz. To protect patient privacy, the microphone recorded 
only the high portions of a 100 ms square wave using a 555 Timer cir-
cuit, i.e., these 50 ms snapshots of vocalizations prohibit recording and 
decoding of the patient’s conversations. 

The  second  system  used  a  single  Biopac  MP160  data  acquisition 
system to acquire patient data. The Biopac MP160 connects to Biopac 
amplifiers  for  EDA,  EMG,  ECG,  and  photoplethysmography  (PPG),  as 
well as a Biopac tri-axial accelerometer. A custom microphone circuit, 
recording only high portions of the microphone signal convolved with a 
100  ms  square  wave  was  recorded  using  an  analog  channel  on  the 
MP160.  The  microphone  is  sampled  at  10  kHz,  while  the  rest  of  the 
signals are sampled at 2.5 kHz. 

Recording ECG data requires three electrodes placed on the chest. 
EDA uses two electrodes placed on the inner wrist. EMG measurement 
requires three electrodes placed on the inner forearm, and the acceler-
ometer is attached to the wrist as well. The microphone as well as the 
Biopac  system  were  placed  on  patients’  bedside  tables.  The  MP160 
connects to a computer running Biopac AcqKnowledge 5.0 software to 
record the incoming data. Overall, 382.79 h of data were collected from 
fifteen  different  patients  (5  female,  7  male,  3  not  noted)  between 
February 2016 and 2018. 

3.2. Sample data 

Different types of seizures appear differently in the signals collected. 
Convulsive seizures are particularly visible in accelerometry and EMG 
signals. Both convulsive and non-convulsive seizures frequently present 
with increased heart rate and heart rate variability as well as an increase 

ComputersinBiologyandMedicine130(2021)1042323A. Hamlin et al.                                                                                                                                                                                                                                 

Table 3 
Sample seizure data annotations.  

Annotation 

Time (sec) 

Electrographic seizure onset, no clinical changes on video 
Patient wakes up 
Appears asleep again - might be moaning during this seizure 
Right hand automatism, legs move under blanket. 
Appears to sleep. Moaning? 
Left head turning 
Patient awake, vocalizes, picks up right arm 
Right head turning 
Whole body now rhythmically shaking 
Automated seizure alarm 
Less whole body shaking, RN at bedside 
Whole body stiffened, back arched 
RN: “Heart rate 92
“Facial movements” patient rhythmic back jerking 
Whole body rhythmic jerking slowing down, RN administers O2 

′′

mask 

36,184 
36,188 
36,190 
36,231 
36,235 
36,269 
36,272 
36,273 
36,278 
36,279 
36,290 
36,296 
36,300 
36,305 
36,325 

Patient twitching significantly less strong, has gagging sounds, not 

36,332 

breathing 

Now only left arm twitching 
Minor back jerking x3 
Gasping 
′′
RN “Heart rate 101
Seizure ends electrographically, per EEG reader 
Patient takes deep breath 
RN “69, heart rate 138” (I think that’s what he says) 
Deep breathing by patient 
′′
RN “Heart rate 124
Deep breathing turns to snoring 

36,336 
36,340 
36,342–36344 
36,345 
26,350 
36,353 
36,360 
36,364 
36,371 
36,420  

in the PPG signal. Patient N woke up approximately 4 s into the seizure, 
and then appeared to be asleep again 2 s later. However, small changes 
were observed in the microphone signal during this time, indicating that 
the patient may have been moaning, but the video footage is unclear. At 
time 36,231 s (41 s into  the seizure),  N began having  right hand au-
tomatisms  and  leg  movement,  although  he  appeared  to  be  asleep.  At 
time 36,272 s (88 s into the seizure), N woke up, vocalized, picked up his 
right  arm,  and  began  rhythmically  turning  his  head.  This  change  in 
behavior, marked by the first significant spike of the microphone signal, 
corresponds with the sudden dramatic change in the ECG signal as well 
as the fluctuations in the accelerometers. Six seconds later, N’s whole 
body was observed to rhythmically shake, and the accelerometry and 
EMG signals both increased in magnitude. Approximately 12 s later the 
rhythmic shaking gradually abated. At time 36,296 s, N’s whole body 
became rigid. Nine seconds later, N’s back began jerking, evolving into a 
whole  body  rhythmical  shake,  leading  to  another  increase  in  the 
magnitude  of  both  the  EMG  and  the  accelerometry  signals.  At  time 
36,332 s, N’s twitching lessened significantly and he produced gagging 
sounds, reflected by the microphone signal’s increased magnitude. Four 
seconds later, only N’s left arm was twitching. Finally, patient N gasped 
for 3 s, and at time 36,350 s, the seizure ended electrographically. 

3.3. Filtering 

While  one  may  be  able  to  visibly  identify  the  difference  between 
seizure  and  non-seizure  time-series  data,  this  difference  needs  to  be 
defined  by  measurable  properties  to  be  automatically  detected.  To 
develop machine learning classifiers, properties  of the waveforms are 
defined  as  features,  and  these  features  are  extracted  (i.e.,  calculated) 
from the time-series data. Prior to extracting features, the raw data are 
processed to reduce noise. For processing, data are segmented into 5-s 
increments  or  epochs,  with  each  epoch  overlapping  the  preceding 
epoch by 2.5 s (50%). 

The Biopac ECG amplifier contains a built-in 0.005 Hz high pass filter 
and 150 Hz low pass filter. In Matlab, a forward-backward infinite im-
pulse response (IIR) notch filter removes 60 Hz powerline noise and its 
harmonics which compromise the signal’s integrity. The EMG signal is 

Fig. 1. Non-cerebral data for patient N’s seizure. Signals are labeled below the 
waveforms:  the  first  three  signals  from  left  to  right  show  accelerometry,  fol-
lowed by ECG, EDA, EMG, MIC, which represents audio, and PPG signals on the 
y-axis  and  time  on  the  x-axis.  The  seizure  commenced  at  time  36,184  s  and 
concluded at time 36,350 s. This figure shows a notable change in all signals 
during the patient’s seizure. 

in EDA. Aural automatisms may occur in either type of seizure and can 
be seen in audio signals. Thus, looking at the time-domain signals can 
provide insight into events during a seizure. 

Fig. 1 plots the waveforms capturing patient N’s seizure activity as an 
example  of  raw  data  manifestation  of  a  seizure,  including  the  64  s 
immediately preceding the seizure and the 22 s following it. The seizure 
began at time 36,184 s and continued until time 36,350 s. The following 
account  describes  occurrences  during  the  seizure,  full  annotations  of 
which are documented in Table 3. Prior to the onset of the seizure, pa-
tient N was asleep. The start of the seizure is seen in the form of small 
blips in the accelerometer and EMG signals, as well as the sudden change 

ComputersinBiologyandMedicine130(2021)1042324A. Hamlin et al.                                                                                                                                                                                                                                 

Table 4 
Features extracted from time series data.  

Feature Name 

Feature Description 

Sensor 

ECG 

EMG 

EDA 

Avg. R-R Length 
Standard Deviation 
of the R-R Length 
Mean Absolute Value 

Variance 
RMS 
Waveform Length 

Maximum 
Time High 

Mean Fourier 
Transform 
Spectral Centroid 

Maximum 
Minimum 
Average 
Standard Deviation 
Maximum Derivative 

Waveform Length 

Spectral Centroid 

Accelerometry 

Average Magnitude 

Standard Deviation 

Maximum 
Magnitude 
Average Fourier 
Transform 

Average XY 
Correlation 

Average XZ 
Correlation 

Average YZ 
Correlation 

Std. Dev. of XY 
Correlation 

Std. Dev. of XZ 
Correlation 

Std. Dev. of YZ 
Correlation 

Spectral Centroid 

Avg. Magnitude 
Standard Deviation 
Average Pitch 

Spectral Centroid 

Bronchial Secretion 
Index 
Linear Prediction 
Coefficient 

Microphone 

∑

The average interval between R-waves 
The standard deviation of the interval 
between R-waves 
The average of the absolute value of the 
signal, MeanAbs = mean (|x|) 
The variance of the signal 
Root mean square value of the signal 
Sum of the absolute value of the 
difference between N adjacent data 
points, n = 1..N,WL =
|xn+1- xn| 
The maximum value of the signal 
Percent of data points above 75% of the 
signal’s maximum 
Average Fourier transform, AvgFT = mean 
(fft(x)) 
Center of mass of the EMG frequency 
spectrum 
The maximum of the signal 
The minimum of the signal 
The average of the signal 
The standard deviation of the signal 
The maximum derivative of the signal, 
MaxDeriv = max (|diff(x)|) 
Sum of the absolute value of the 
difference between N adjacent data 
points, n = 1..N, WL =
|xn+1- xn| 
Center of mass of the EDA frequency 
spectrum 
Average of the square root of the sum of 
squares of each axis, AvgMag = mean 
((x2+ y2+ y2)1/2) 
Standard deviation of the magnitude, 
STDV = std ((x2+ y2+ y2)1/2 
MaxMag = max ((x2+ y2+ y2)1/2 

∑

The average of the Fourier transform of 
the magnitude. AvgFT = mean (fft ((x2+
y2+ y2)1/2 
The average of the correlation between 
the x and y axes, AvgXYCorr = mean (corr 
(x,y)) 
The average of the correlation between 
the x and z axes, AvgXZCorr = mean (corr 
(x,z)) 
The average of the correlation between 
the y and z axes, AvgYZCorr = mean (corr 
(y,z)) 
The standard deviation of the correlation 
between the x & y axes, StdvXYCorr = std 
(corr (x,y)) 
The standard deviation of the correlation 
between the x & z axes, StdvXZCorr = std 
(corr (x,z)) 
The standard deviation of the correlation 
between the y & z axes StdvYZCorr = std 
(corr (y,z)) 
Center of mass of the acceleration 
magnitude frequency spectrum 
The average magnitude of the signal 
The standard deviation of the signal 
The average Fourier transform of the 
signal, Pitch = mean (fft(x)) 
Center of mass of the microphone 
frequency spectrum 
The sum of the Fourier transform 
between 2.2 and 2.6 Hz 
The linear prediction coefficient of the 
signal using N = 2, LPC = lpc (x,2)  

filtered using the Biopac EMG amplifier’s built-in bandpass filter with 1 
Hz high pass corner frequency and 500 Hz low pass corner frequency. 
Notch filtering in Matlab removes powerline noise in the same way as 
with ECG data. EDA signals have a bandwidth below 3 Hz. There is al-
ways  some  DC  component  to  the  signal  because  skin  has  a  baseline 

conductance,  so,  the  Biopac  amplifier’s  built-in  10  Hz  low  pass  filter 
removes this baseline signal. A 40 Hz corner frequency low pass digital 
filter  designed  in  Matlab  removes  noise  higher  than  10  Hz.  Accel-
erometry also includes a very low frequency component from gravity 
that shifts its distribution between the three axes as the patient moves. 
Thus, accelerometry and EDA are filtered in the same way. The same 
notch filtering used on ECG and EMG data also removes powerline noise 
in the microphone signal. The device records audio data convolved with 
a 100 ms square wave. We wrote Matlab code to remove the low periods 
of the square wave retaining only the positive 50 ms of the convolved 
signal  to  protect  patient  privacy,  i.e.,  to  assure  that  we  were  not 
recording patient conversations. PPG data are filtered with the Biopac 
built-in 0.05 Hz high pass filter and 10 Hz low pass filter. 

3.4. Feature extraction and determination of separability 

A review of the literature identified possible features to extract from 
filtered  data  [14,19,29,47,48].  From  these  studies,  a  broad  range  of 
features  were  selected  so  that  their  utility  in  differentiating  between 
seizure  and  non-seizure  data  could  be  evaluated.  The  34  features 
extracted are detailed in Table 4. 

To evaluate the use of machine learning for detecting seizures from 
non-cerebral  data  we  must  first  quantify  the  separability  between 
seizure and non-seizure data, which is the primary purpose of this study. 
To do so, neurologists at the Dartmouth-Hitchcock Medical Center an-
notated vEEG data, labeling time segments of some of the data by what 
the patients were doing. Features were extracted from epochs of seizure 
and non-seizure data, and separability was evaluated using discriminant 
analysis. 

We chose to look at four normal activities to compare individually 
and collectively to seizures – eating, sleeping, talking, and using tech-
nology (such as a typing on a phone or computer) using a binary clas-
sifier.  We  hypothesized  that  activities  form  clusters  of  data  points  as 
each  has  their  own  distinct  signature  in  the  various  signals  being 
recorded. Furthermore, we hypothesized that seizure activity is distinct 
from other  daily  activities  allowing  it  to  be detected.  We explore  the 
separability  of  seizure  and  non-seizure  data  using  linear  discriminant 
analysis (LDA) –  a batch processing approach –  before progressing to 
other approaches. LDA identifies a linear combination of features that 
separates two classes of data [49], in this case, seizure activity from the 
four  normal  activities.  While  LDA  can  be  formulated  as  a  non-binary 
classifier, in the result presented in Section 4, we only consider binary 
classification. 

We implemented LDA on data for each individual patient as well as 
for multiple patients combined. LDA applied to data for an individual 
patient assesses the degree to which a linear decision boundary in multi- 
dimensional feature space (34 dimensions) separates seizure from non- 
seizure data for that individual, while applying LDA to data from mul-
tiple patients is a measure of whether a linear decision boundary can 
generalize. We use the area under the receiver operator characteristic 
(ROC) curve to quantify separability, where the ROC curve shows 1 – 
specificity or FP/(FP + TN) on the x-axis and sensitivity or TP/(TP + FN) 
on  the  y-axis.  This  study  informs  methods  for  training  subsequent, 
recursive machine learning classifiers. 

4. Results 

Because  the  patients  we  monitored  had  seizures  relatively  infre-
quently, we recorded significantly more non-seizure data than seizure 
data.  Thus,  we  selected  varying  set  amounts  of  non-seizure  data  for 
analysis. If N represents the number of epochs we recorded from a pa-
tient during a seizure, we carried out analyses with N, Nx2, Nx5, Nx10 
non-seizure epochs, as well as with all non-seizure data for that patient. 
N varies patient-to-patient as the number and length of seizures varies. 
Each analysis that does not include the full set of non-seizure data was 
executed 10,000 times, selecting a new random set of epochs within the 

ComputersinBiologyandMedicine130(2021)1042325A. Hamlin et al.                                                                                                                                                                                                                                 

Table 5 
Area  under  ROC  mean  and  standard  deviations  by  patient  and  non-seizure 
epochs used.  

Patient 

A 

D 

I 

N 

O 

N Seizure 
Epochs, N 
Non- 
Seizure 
Epochs 

0.957 ±
0.0112 
0.9381 ±
0.0292 
0.9615 ±
0.0251 
0.9793 ±
0.0095 
0.9998 ±
8.59E-04 

N Seizure 
Epochs, 
Nx2 Non- 
Seizure 
Epochs 

0.95806 ±
0.00821 
0.93475 ±
0.02096 
0.95125 ±
0.01924 
0.97825 ±
0.00661 
0.99962 ±
0.00115 

N Seizure 
Epochs, 
Nx5 Non- 
Seizure 
Epochs 

0.96140 ±
0.00508 
0.94022 ±
0.01268 
0.94322 ±
0.01365 
0.97922 ±
0.00379 
0.99973 ±
0.00059 

N Seizure 
Epochs, 
Nx10 Non- 
Seizure 
Epochs 

0.96480 ±
0.00354 
0.94588 ±
0.00856 
0.94063 ±
0.00975 
0.98072 ±
0.00251 
0.99991 ±
0.00016 

N Seizure 
Epochs, All 
Non- 
Seizure 
Epochs 

0.9695 

0.9549 

0.938 

0.9785 

1  

Table 6 
Number of seizure epochs collected for each patient.  

Patient 

Number of Seizure Epochs by Patient, N 

A 
D 
I 
N 
O 

82 
24 
30 
32 
26  

Fig. 2. Area under the ROC curve for individual patients as a function of N, or 
the number of non-seizure epochs that were included in analysis. This shows 
that the area under the ROC curve does not depend strongly on the amount of 
non-seizure data used. 

non-seizure  data  for  each  iteration.  This  selection  was  conducted  in 
order to ensure a representative sample set. For creating figures shown 
in this section, all 34 features described in Section 3 are used in LDA 
analysis. 

The means and standard deviations over 10,000 trials for each set of 
analyses for individual patients are reported in Table 5. N is used in the 
title of each column as a variable representing the number of seizure 

epochs recorded, which varies by patient and is provided in Table 6. No 
standard  deviation  is  reported  when  all  non-seizure  data  are  used  as 
there is no variation when this analysis is repeated. Generally, values 
greater than 0.95 are considered good. 

Fig. 2 shows a plot of the means in Table 6 for the five patients who 
experienced  at  least  one  seizure.  The  datapoint  “All”  denotes  that  all 
available non-seizure epochs were used to calculate the ROC for each 
patient. While values vary slightly based on how much non-seizure data 
are included, all values are greater than 0.9. It is interesting to note that 
while the curves for other patients either increase or remain relatively 
constant, the area under the ROC curve for patient I decreases as more 
non-seizure data are included. One possible explanation for this is that 
during his seizures, patient I simply stared ahead and was unresponsive; 
these  behaviors are  less distinct  from non-seizure behaviors. As  more 
non-seizure  data  are  added,  the  presence  of  false  positives  and  true 
negatives  increases.  By  the  same  logic,  the  presence  of  true  positives 
remains constant as no more seizure data are being added. Still, when all 
seizure and non-seizure data are included, the area under the ROC curve 
is 0.938 for patient I. In addition, patient D’s seizures were also non- 
movement  based  and  achieved  an  area  under  the  ROC  curve  of 
0.9549, demonstrating that non-movement seizures are separable from 
normal behavior. 

Fig. 3 shows the histograms for visualization of separability derived 
from LDA analysis and provides the area under the ROC curves in the 
title for each patient that had at least one epileptic seizure, as well as for 
all five patients who had seizures combined. Each subfigure provides a 
normalized distance from the axis of maximal separation (AMS) on the 
horizontal  axis  vs.  the  frequency  of  occurrence  of  epochs  within  the 
seizure and non-seizure data. Plots 1 through 5 in Fig. 3 use the same 
number of seizure and non-seizure epochs for each individual patient, 
and plot 6 uses all seizure and non-seizure data from the five patients 
who experienced seizures. 

All observations from the data support the same conclusion: while 
there is some overlap, seizure and non-seizure data are separable using 
the sensor suite and features described in section 3. We calculated the 
separation between the seizure data of all patients combined and all of 
the  non-seizure  data  of  all  of  the  patients  to  explore  how  data  from 
various patients generalize to others. The analysis presented uses all of 
the seizure data and all epochs of non-seizure data, and the area under 
the ROC curve is 0.9144. The area under this ROC curve is lower than for 
each individual patient. We hypothesize that one reason for this lower 
value  is  because  we  are  including  different  types  of  seizures  in  the 
analysis. When more seizure data are available, classifiers can be tested 
on multiple occurrences of the same type of seizure to determine if they 
need to be patient-specific or not. 

When using LDA, the separation between datasets is quantified by 
the magnitude of features along the AMS. Ranking features in order of 
their contribution to the AMS gives a metric of how useful they are in 
classifying  activities.  Thus,  we  can  assess  which  features  provide  the 
most  information  by  patient.  Table  7  lists  the  first  10  features  by 
importance for each patient. Table 7 also shows a combined feature set 
that  was  created  by  normalizing  the  means  of  each  feature  for  each 
patient individually, taking the average for each feature across patients, 
and  then  re-sorting  by  magnitude  to  determine  which  features  were 
overall the most important. To differentiate which features come from 
which sensors, the features are color-coded. Green represents a micro-
phone feature, orange an EMG feature, blue an EDA feature, red an ECG 
feature, and purple represents an accelerometry feature. This shows that 
the  most  valuable  sensors  do  vary  by  patient,  even  when  patients 
experience similar seizure types. For example, the ten most important 
features  for  detecting  the  non-convulsive  seizures  of  patients  D  and  I 
share two common features, while convulsive patients N and O share 
three of the 10 most important features. EMG, microphone, EDA, and 
accelerometry  features  generally  appear  higher  on  the  list  than  ECG 
features. Collecting more data and evaluating feature rank for additional 
patients and seizure types will provide further insight into which, if any, 

ComputersinBiologyandMedicine130(2021)1042326A. Hamlin et al.                                                                                                                                                                                                                                 

Fig. 3. Histograms showing separation of seizure and non-seizure epochs for each patient (a–e) and for all patients (f). Each count is an epoch, and separation values 
are the normalized value of the distance from the axis of maximal separation in 34-dimensional feature space. 

Table 7 
Ranking of most significant features for each patient and for all patients combined. 

Color code: Pink – accelerometer; Green: EMG; Blue: EDA; Grey: Microphone; Orange: ECG. 

sensors and features can be eliminated. 

Likewise, the analysis of separability using LDA sheds insight on and 
can  be  compared  to  the  results  previously  reported  for  detection  of 
seizures using a subset of the body-worn sensors considered here. For 

example, both Poh et al. [44] and Heldberg et al. [45] uses solely ac-
celerometers and EDA to detect seizures. Poh et al. [44] reports detec-
tion  of  15  out  of  16  generalized  tonic-clonic  (motion)  seizures  from 
seven patients and a false alarm rate of 0.74 every 24 h. Heldberg et al. 

ComputersinBiologyandMedicine130(2021)1042327A. Hamlin et al.                                                                                                                                                                                                                                 

Table 8 
ROC values for individual sensors only, pairs of sensors compared to the full sensor suite. 

[45]  includes  results  from  both  motion  and  non-motion  seizures 
reporting a lower overall sensitivity of 89.1% relative to Poh et al. and 
overall specificity of 93.1% for eight patients and 21 separate motion 
seizures. The sensitivity and specificity for seizures with no motor ac-
tivity  were  97.1%  and  92.9%,  respectively  over  34  seizures.  Table  8 
shows a heat-map coded ROC values for the five patients who experi-
enced seizures from our study, with motion classified in Table 2, and 
both single sensors and combinations of two sensors. These results are 
presented alongside the ROC for the full suite of sensors. These results 
show that no single sensor is adequate for seizure detection. Addition-
ally, while for some patients (patients N and O) accelerometry combined 
with EDA provides ROC values over 0.95, for others, ROC value for these 
two sensors is unacceptably low. If only two sensors could be chosen for 
a device, Table 7 shows that accelerometry and microphone provide a 
ROC value above 0.86 for all but one patient. The full sensor suite retains 
ROC  values  above  0.93  for  all  patients  individually,  with  an  overall 
value on 0.9144. 

5. Conclusion 

Epilepsy  is  one  of  the  most  common  neurological  disorders,  and 
accurate  seizure  tracking  is  crucial  for  effective  epilepsy  treatment. 
Currently, patients are expected to keep accurate records of their sei-
zures. However, the majority of patients do not remember their seizures. 
Thus,  a  device  to  detect  and  track  seizures  is  necessary.  While  some 
devices have shown positive results for specific types of seizures, none 
have  been  able  to  accurately  detect  all  types.  This  work  serves  to 
improve seizure detection by combining modalities and systematically 
investigating separability of seizures from normal activity as a first step 
in developing a device that can detect all types of seizures. 

We  use  electrocardiography,  electrodermal  activity,  electromyog-
raphy,  accelerometry,  and  audio  signals.  Using  linear  discriminant 
analysis, we establish that seizure and non-seizure data from this sensor 
set are separable. When using all seizure and non-seizure data, the areas 
under the ROC curves for most patients are greater than 0.95, indicating 
strong  separability.  The  area  under  the  ROC  curve  for  one  patient  is 
0.938 Although the latter’s seizures did not involve movement, another 
patient’s seizures also did not include movement, but had an area under 
the ROC curve of 0.9549, suggesting that non-movement seizures are 
still  separable  from  normal  activity.  Audio  signal  features,  which  are 
absent in other studies, prove to be among the top ten features estab-
lishing separability in four of five patients. 

Strong separability of seizure and non-seizure data suggests that it 
should be possible to detect seizures in real time during normal routine. 
We moved towards real-time classification by implementing a support 
vector machine in Ref. [50]; preliminary results suggest that, with more 
data, a discriminative approach, such as a Support Vector Machine, may 
enable  real-time  classification,  although  additional  data  are  needed 
[50]. 

Moving  forward,  we  need  to  collect  more  patient  data  to  develop 
multi-modal  classifiers  and  to  determine  which  features  generalize 
across patients or across patients with similar seizure types and which 
features  are  specific  to  facilitating  seizure  detection  in  individual  pa-
tients. With new data, various real-time machine learning classifiers can 
be explored. Overall, this research strongly suggests that non-cerebral 

sensing  modalities  provide  data  that  can  be  accurately  classified  as 
seizure  or  non-seizure  data  using  a  discriminative  machine  learning 
method. 

Declaration of competing interest 

The authors have no conflicts of interests to declare. 

Acknowledgements 

This  research  was  funded  by  the  Hitchcock  Foundation,  a  Reeves 
Pilot Project award and the Dept. of Defense Army Medical Research and 
Materiel Command, Award No. W81XWH18-1-0712. 

References 

[1] Institute of Medicine (US), Committee on the public health dimensions of the 
epilepsies, Washington D.C., in: M.J. England, C.T. Liverman, A.M. Schultz, L. 
M. Strawbridge (Eds.), “Introduction,” in Epilepsy Across the Spectrum, first ed., 
National Academies Press (US), Washington D.C.), US, 2012, p. 27. ch. 1, sec. 2 
[2] M.M. Zack, R. Kobau, “National and state estimates of the numbers of adults and 
children with active epilepsy – United States, 2015, Aug, 2017, MMWR Morb. 
Mortal. Wkly. Rep. 66 (31) (2017) 821–825, https://doi.org/10.15585/mmwr. 
mm6631a1 [Online]. 

[3] J.A. French, Refractory epilepsy: clinical overview, Epilepsia 48 (1) (Feb. 2007) 

3–7, https://doi.org/10.1111/j.1528-1167.2007.00992.x [Online]. 

[4] C. Hoppe, A. Poepel, C. E. Elger, “Epilepsy: accuracy of patient seizure counts,” 
Epilepsia, vol. 64, no. 11, pp. 1595-1599, DOI: 10.1001/archneur/64.11.1595, 
[Online]. 

[5] D. E. Blum, J. Eskola, J. J. Bortz, R. S. Fisher, “Patient awareness of seizures,” 
Neurology, vol. 47, no. 1, 260-264, DOI: 10.1212/WNL.47.1.260, ([Online]). 
[6] F. Kerling, S. Mueller, E. Pauli, H. Stefan, When do patients forget their seizures? 
An electroclinical study, Epilepsy Behav. 9 (2) (Sep. 2006) 281–285, https://doi. 
org/10.1016/j.yebeh.2006.05.050 ([Online]). 

[7] A.P. Narechania, I.I. Garic, I. Sen-Gupta, M.P. Macken, E.E. Gerard, S.U. Schuele, 
Assesment of quasi-piezoelectric mattress monitor as a detection system for 
generalized convulsions, Epilepsy Behav. 28 (2) (Aug. 2013) 172–176, https://doi. 
org/10.1016/j.yebeh.2013.04.017 ([Online]). 

[8] S. Fulton, K. Van Poppel, A. McGregor, M. Ellis, A. Patters, J. Wheless, Prospective 
study of 2 bed alarms for detection of nocturnal seizures, J. Child Neurol. 28 (11) 
(Oct. 2012) 1430–1433, https://doi.org/10.1177/0883073812462064 [Online]. 

[9] K. Van Poppel, S.P. Fulton, A. McGregor, M. Ellis, A. Patters, J. Wheless, 

Prospective study of the Emfit movement monitor, J. Child Neurol. 11 (11) (Jan. 
2013) 1434–1436, https://doi.org/10.1177/0883073812471858 [Online]. C. 
Carlson, V. Arnedo, M. Cahill, O. Devinsky, “Detecting nocturnal convulsions: 
efficacy of the MP5 monitor,” Seizure, vol. 18, no. 3, pp. 225–227, Apr. 2009. DOI: 
10.1016/j.seizure.2008.08.007, [Online]. 

[10] H. Lu, Y. Pan, B. Mandal, H.L. Eng, C. Guan, D.W.S. Chan, Quantifying limb 

movements in epileptic seizures through color-based video analysis, IEEE Trans. 
Biomed. Eng. 60 (2) (Nov. 2012) 461–469, https://doi.org/10.1109/ 
TBME.2012.2228649 ([Online]). 

[11] S. Kalitzin, G. Petkov, D. Velis, B. Vledder, F. Lopes da Silva, Automatic 

segmentation of episodes containing epileptic clonic seizures in video sequences, 
IEEE Trans. Biomed. Eng. 59 (12) (Aug. 2012) 3379–3385, https://doi.org/ 
10.1109/TBME.2012.2215609 [Online]. 

[12] L.L.C. Hipass Design, Sami: the sleep activity monitor [Online]. Available: www.sa 

mialert.com/details. 

[13] G.R. de Bruijne, P.C.W. Sommen, R.M. Aarts, Detection of epileptic seizures 

through audio classification, in: 4th European Conf. Of the Int. Fed. For Med. And 
Biomed. Eng., Antwerp, Switzerland, 2008, pp. 23–27. 

[14] Epilepsy Foundation, Myclonic seizures [Online]. Available: www.epilepsy.com/le 

arn/types-seizures/myoclonic-seizures. 

[15] Epilepsy Foundation, Tonic seizures [Online]. Available: www.epilepsy.com/ 

learn/types-seizures/tonic-seizures. 

[16] Epilepsy Foundation, Tonic-clonic seizures [Online]. Available, www.epilepsy.co 

m/learn/types-seizures/tonic-clonic-seizures. 

ComputersinBiologyandMedicine130(2021)1042328A. Hamlin et al.                                                                                                                                                                                                                                 

[17] T.M.E. Nijsen, R.M. Aarts, J.B.A.M. Arends, P.J.M. Cluitmans, Automated detection 
of tonic seizures using 3-D accelerometry, in: 4th  European Conf. Of the Int. Fed. 
For Med. And Biomed. Eng., Antwerp, Switzerland, 2008, pp. 188–191. 
[18] T.M.E. Nijsen, J.B.A.M. Arends, P.A.M. Griep, P.J.M. Cluitmans, The potential 

[33] C. Opherk, J. Coromilas, L.J. Hirsch, Heart rate and EKG changes in 102 seizures: 
analysis of influencing factors, Epilepsy Res. 52 (2) (Dec. 2002) 117–127, https:// 
doi.org/10.1016/S0920-1211(02)00215-2 [Online]. 

[34] C. Baumgartner, S. Lurger, F. Leutmezer, Autonomic symptoms during epileptic 

value of three-dimensional accelerometry for detection of motor seizures in severe 
epilepsy, Epilepsy Behav. 7 (1) (Aug. 2005) 74–84, https://doi.org/10.1016/j. 
yebeh.2005.04.011 [Online]. 

[19] S. Luca, P. Karsmakers, K. Cuppens, T. Croonenborghs, A. Van de Vel, 

B. Ceulemans, L. Lagae, S.V. Huffel, B. Vanrumste, Detecting rare events using 
extreme value statistics applied to epileptic convulsions in children, Artif. Intell. 
Med. 60 (2) (Feb. 2014) 89–96, https://doi.org/10.1016/j.artmed.2013.11007 
[Online]. 

[20] A. Van de Vel, K. Cuppens, B. Bonroy, M. Milosevic, S. Van Huffel, B. Vanrumste, 

L. Lagae, B. Ceulemans, Long-term home monitoring of hypermotor seizures by 
patient-worn accelerometers, Epilepsy Behav. 26 (1) (Jan. 2013) 118–125, https:// 
doi.org/10.1016/j.yebeh.2012.10.006 [Online]. 

[21] K. Cuppens, “reportDetection of Epileptic Seizures Based on Video and 

Accelerometer Readings,” Ph.D. dissertation, E. E., Katholieke Univ. Leuven., 
Leuven, Belgium. 

[22] G.T. Borujeny, M. Yazdi, A. Keshavarz-Haddad, A.R. Borujeny, Detection of 

epileptic seizure using wireless sensor networks, J. Med. Signals and Sens. 3 (2) 
(Apr. 2013) 63–68 ([Online]). 

[23] A. Dalton, S. Patel, A.R. Chowdhury, M. Welsh, T. Pang, S. Schachter, G. OLaighin, 
P. Bonato, Development of a body sensor network to detect motor patterns of 
epileptic seizures, IEEE Trans. Biomed. Eng. 59 (11) (June 2012) 3204–3211, 
https://doi.org/10.1109/TBME.2012.2204990 [Online]. 

[24] J. Lockman, R.S. Fisher, D.M. Olson, Detection of seizure-like movements using a 
wrist accelerometer, Epilepsy Behav. 20 (4) (Apr. 2011) 638–641, https://doi.org/ 
10.1016/j.yebeh.2011.01.019 ([Online]). 

[25] A.L. Patterson, B. Mudigoudar, S. Fulton, A. McGregor, K. Van Poppel, M. 

C. Wheless, L. Brooks, J.W. Wheless, SmartWatch by SmartMonitor: assessment of 
seizure detection efficacy for various seizure types in children, a large prospective 
single-center study, Pediatr. Neurol. 53 (4) (Oct. 2015) 309–311, https://doi.org/ 
10.1016/j.pediatrneurol.2015.07.002 [Online]. 

[26] S. Beniczky, T. Polster, T.W. Kjaer, W. Hjalgrim, Detection of generalized tonic- 

clonic seizures by a wireless wrist accelerometer: a prospective, multicenter study, 
Epilepsia 54 (4) (Apr. 2013), https://doi.org/10.1111/epi.12120 [Online]. 
[27] U. Kramer, S. Kipervasser, A. Schlitner, R. Kuzniecky, A novel portable seizure 
detection alarm system: preliminary results, J. Clin. Neurophysiol. 28 (1) (Feb. 
2011) 36–38, https://doi.org/10.1097/WNP.0b013e3182051320 [Online]. 
[28] I. Conradsen, P. Wolf, T. Sams, H.B.D. Sorensen, S. Beniczky, Patterns of muscle 

activation during generalized tonic and tonic-clonic epileptic seizures, Epilepsia 52 
(11) (Nov. 2011) 2125–2132, https://doi.org/10.1111/j.1528-1167.2011.03286.x 
[Online]. 

[29] I. Conradsen, S. Beniczky, K. Hoppe, P. Wolf, H.B.D. Sorensen, Automated 

algorithm for generalized tonic-clonic epileptic seizure onset detection based on 
sEMG zero-crossing rate, IEEE Trans. Biomed. Eng. 59 (2) (Dec. 2011) 579–585, 
https://doi.org/10.1109/TBME.2011.2178094 [Online]. 

[30] F. Leutmezer, C. Schernthaner, S. Lurger, K. P¨otzelberger, C. Baumgartner, 

seizures, Epileptic Disord. 3 (3) (Sep. 2001) 103–116 [Online]. 

[35] O. Devinsky, Effects of seizures on autonomic and cardiovascular function, 
Epilepsy Current 4 (2) (Mar. 2004) 43–46, https://doi.org/10.1111/j.1535- 
7597.2004.42001.x [Online]. 

[36] M. Nei, R.T. Ho, M.R. Sperling, EKG abnormalities during partial seizures in 

refractory epilepsy, Epilepsia 41 (5) (May 2000) 542–548, https://doi.org/ 
10.1111/j.1528-1157.2000.tb00207.x [Online]. 

[37] J. Jeppesen, S. Beniczky, P. Johansen, P. Sidenius, A. Fuglsang-Frederiksen, 

Detection of epileptic seizures with a modified heart rate variability algorithm 
based on Lorenz plot, Seizure 24 (Jan. 2015) 1–7, https://doi.org/10.1016/j. 
seizure.2014.11.004 [Online]. 

[38] I. Osorio, Automated seizure detection using EKG, Int. J. Neural Syst. 24 (2) (Mar. 

2014) 1450001, https://doi.org/10.1142/S0129075614500014 [Online]. 

[39] W.J.C. van Elmpt, T.M.E. Nijsen, P.A.M. Griep, J.B.A.M. Arends, A model of heart 
rate changes to detect seizures in severe epilepsy, Seizure 15 (6) (Sep. 2006) 
366–375, https://doi.org/10.1016/j.seizure.2006.03.005 [Online]. 

[40] M.Z. Poh, Continuous assessment of epileptic seizures with wrist-worn biosensors, 

Ph.D. dissertation, in: Harvard-MIT Div. Of Health Sci. and Tech., M.I.T., 
Cambridge, M.A., 2011. 

[41] M. Miloˇsevi´c, A. Van de Vel, B. Bonroy, B. Ceulemans, L. Lagae, B. Vanrumste, 

S. Van Huffel, Automated detection of tonic-clonic seizures using 3-D 
accelerometry and surface electromyography in pediatric patients, J. Biomed. 
Health Inform. 20 (5) (Sep. 2016) 1333–1341, https://doi.org/10.1109/ 
JBHI.2015.2462079 ([Online]). 

[42] D. Cogan, J. Birjandtalab, M. Nourani, J. Harvey, V. Nagaraddi, Multi-biosignal 
analysis for epileptic seizure monitoring, Int. J. Neural Syst. 27 (1) (2017) 
1650031, https://doi.org/10.1142/S0129065716500313 [Online]. 
[43] G. Becq, S. Bonnet, L. Minotti, M. Antonakios, R. Guillemaud, P. Kahane, 

Classification of epileptic motor manifestations using inertial and magnetic 
sensors, Comput. Biol. Med. 41 (1) (Jan. 2011) 46–55, https://doi.org/10.1016/j. 
compbiomed.2010.11.005 [Online]. 

[44] M.Z. Poh, T. Loddenkemper, C. Reinsberger, N.C. Swenson, S. Goyal, M.C. Sabtala, 
J.R. Madsen, R.W. Picard, Convulsive seizure detection using a wrist-worn 
electrodermal activity and accelerometry biosensor, Epilepsia 53 (5) (Mar. 2012) 
e93–e97, https://doi.org/10.1111/j.1528-1167.2012.0344.x ([Online]). 

[45] B.E. Heldberg, T. Kautz, H. Leutheuser, R. Hopfeng¨artner, B.S. Kasper, B. 

M. Eskofier, Using wearable sensors for semiology-independent seizure detection 
–towards ambulatory monitoring of epilepsy, in: Presented at 37th  Ann. Int. Conf. 
IEEE Eng. In Med. And Bio. Society, 2015, Aug. 

[46] F. Oronati, G. Regalia, C. Caborni, M. Migliorini, D. Bender, M.Z. Poh, C. Frazier, 

E. Kovitch Thropp, E.E. Mynatt, J. Bidwell, R. Mai, W. C Jr., A.S. Blum, 
D. Friedman, T. Loddenkemper, F. Mohammadpour-Touserkani, C. Reinsberger, 
S. Tognetti, R.W. Picard, Multicenter clinical assessment of improved wearable 
multimodal convulsive seizure detectors, Epilepsia 58 (11) (Nov. 2017) 
1870–1879, https://doi.org/10.1111/epi.13899 [Online]. 

Electrocardiographic changes at the onset of epileptic seizures, Epilepsia 44 (3) 
(Mar. 2003) 348–354, https://doi.org/10.1046/j.1528-1157.2003.34702.x 
([Online]). 

[47] E. Azad, D. Bajpai, R. Butler, L. Sridhar, Final Design Review: A Device to Detect 
and Quantify Seizures, Thayer School of Engineering, Hanover, N.H., U.S., 2016. 

[48] G.M. Azmal, A. Al-Jumaily, M. Al-Jaafreh, Continuous measurement of oxygen 

[31] V. Novak, A. Reeves, P. Novak, P.A. Low, F.W. Sharbrough, Time-frequency 

mapping of R-R interval during complex partial seizures of temporal lobe origin, 
J. Auton. Nerv. Syst. 77 (2–3) (Sep. 1999) 195–202, https://doi.org/10.1016/ 
S0165-1838(99)00044-2 ([Online]). 

[32] I. Osorio, B.F. Manly, Is seizure detection based on EKG clinically relevant? Clin. 
Neurophysiol. 125 (10) (Oct. 2014) 1946–1951, https://doi.org/10.1016/j. 
clinph.2014.01.026 [Online]. 

saturation level using photoplethysmography signal, in: Presented at Int. Conf. On 
Biom. And Pharm. Eng., 2006, 2007, Jan [Online]. Available: www.ieeeexplore. 
ieee.org/stamp/stamp.jsp?arnumber=4155955. 

[49] S. Balakrishnama, A. Ganapathiraju, Linear discriminant analysis - a brief tutorial, 

Institute for Signal and information Processing 18 (1998). No. 1998. 

[50] A. Hamlin, Epileptic Seizure Detection Using Multimodal Sensor Data and Machine 

Learning, Master of Science Thesis, Dartmouth College, 2019. 

ComputersinBiologyandMedicine130(2021)1042329
