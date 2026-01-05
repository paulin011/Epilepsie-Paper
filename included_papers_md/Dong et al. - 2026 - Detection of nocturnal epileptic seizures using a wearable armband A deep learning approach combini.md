# Dong et al. - 2026 - Detection of nocturnal epileptic seizures using a wearable armband A deep learning approach combini

Computer Methods and Programs in Biomedicine 273 (2026) 109087 

Contents lists available at ScienceDirect

Computer Methods and Programs in Biomedicine
journal homepage: www.sciencedirect.com/journal/computer-methods- 
and-programs-in-biomedicine

Detection of nocturnal epileptic seizures using a wearable armband: A deep 
learning approach combining accelerometry and 
photoplethysmography signals

, Johannes P. van Dijk b,c, Ronald M. Aarts b, Yunfeng Wang d, Xi Long b,*

Chunjiao Dong a,b
a Department of Medical Imaging, Hebei Medical University, 050031 Shijiazhuang, Hebei, China
b Department of Electrical Engineering, Eindhoven University of Technology, 5612 AP Eindhoven, Netherlands
c The Kempenhaeghe Academic Center for Epileptology, 5591 VE Heeze, Netherlands
d The Institute of Microelectronics, Chinese Academy of Sciences, 100029 Beijing, China

A R T I C L E  I N F O

A B S T R A C T

Keywords:
seizure detection
Wearable sensor
Accelerometry
Photoplethysmography
Deep learning
Long-term monitoring

Background:  Epileptic  seizures  can  lead  to  severe  outcomes  including  sudden  unexpected  death  in  epilepsy 
(SUDEP).  Clinical  standard  for  seizure  diagnosis  and  detection  requires  electroencephalography  and  video 
monitoring, which is yet considered not suitable for home use, especially during nighttime sleep in a low-light 
condition. We proposed a deep learning (DL)-based approach to automatically detect nocturnal major seizures 
using a wearable armband that can potentially help reduce SUDEP risk through timely caregiver intervention.
Methods: In this prospective cohort study, 68 patients with major seizures were monitored for up to three months 
using a wearable armband (NightWatch®) capturing tri-axial accelerometry (ACM) and photoplethysmography 
(PPG) signals. A two-step approach was designed: (1) a pre-screening step using threshold-based algorithms to 
identify  suspected  seizure  events  (ACM  standard  deviation  >0.4  or  heart  rate  increase  >10%),  and  (2)  a  DL 
model (CNN-LSTM with attention mechanism) to recognize true seizures. Model performance was evaluated via a 
10-fold  cross-validation,  reporting  sensitivity  (SEN),  false  alarm  rate  (FAR),  and  area  under  the  ROC  curve 
(AUC).
Results:  In  788  overnight  recordings  (6304  hours),  a  total  of  1846  severe  seizures  were  identified.  The  pre- 
screening  step  achieved 0.940 sensitivity in pre-identifying or ‘preserving’  seizures, reducing data  volume by 
81% (from 6304 to 1201 hours). The DL model demonstrated a mean accuracy of 0.793 [95% CI: 0.745–0.841], a 
mean  sensitivity  of  0.762  [95%  CI:  0.704–0.821],  a  mean  positive  predictive  value  of  0.334  [95%  CI: 
0.229–0.356] and a mean false alarm rate of 0.165/hour [95% CI: 0.097–0.234]. These results exceeded those of 
single (signal) modality detection methods.
Conclusion: Our two-step approach enables accurate, long-term detection of severe nocturnal seizures in home 
settings. The wearable system provides a practical solution for continuous monitoring and real-time alerts, thus 
potentially reducing SUDEP risk and improving patient safety, fulfilling an urgent unmet need in epilepsy care. 
Furthermore,  by  enabling  long-term  home  monitoring,  this  system  may  help  assess  the  relationship  between 
seizure events and lifestyle-related triggers such as sleep deprivation, stress, physical exertion, or alcohol con-
sumption, thereby supporting the development of personalized preventive strategies.

1. Introduction

Epilepsy  is  a  chronic  neurological  disorder  characterized  by 
abnormal, excessive neuronal discharges, leading to recurrent seizures, 

requiring patients to do regular review and long-term treatment. Epi-
lepsy  has  a  high  incidence  rate  and  a  wide  range  of  affected  people, 
bothering patients of different ages, races, and classes around the world. 
A  systematic  review  and  meta-analysis  of  shows  that  the  global 

Abbreviations: ACM, accelerometry; AUC, area under the ROC curve; CNN, convolutional neural network; ECG, electrocardiography; EEG, electroencephalog-
raphy; FAR, false alarm rate; HR, heart rate; LSTM, long short-term memory; PPG, photoplethysmography; ROC, receiver operating characteristic; SD, standard 
deviation; SEN, sensitivity; SUDEP, sudden unexpected death in epilepsy; SVM, support vector machines.

* Corresponding author.

E-mail address: x.long@tue.nl (X. Long). 

https://doi.org/10.1016/j.cmpb.2025.109087
Received 17 May 2025; Received in revised form 8 September 2025; Accepted 24 September 2025  
Available online 29 September 2025 
0169-2607/© 2025 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ). 

C. Dong et al.                                                                                                                                                                                                                                    

Computer Methods and Programs in Biomedicine 273 (2026) 109087 

prevalence of epilepsy ranges from 5.8 % to 7.3 % [1]. It is estimated 
that there are currently about 50 million active epilepsy patients in the 
world (referring to patients with frequent epileptic seizures needing to 
maintain anti-epileptic treatment), and among them 30 % are refractory 
[2]. Epileptic seizures have many potential dangers, including injury, 
status  epilepticus,  and  sudden  unexpected  death  in  epilepsy  (SUDEP) 
[3]. The sudden death rate in epilepsy patients is 20 times higher than 
that in the general population [4]. Among people with refractory epi-
lepsy, the incidence rate of SUDEP is 1.1–5.9 per 1000 people per year, 
and the frequency of epilepsy patients with indications for surgery or 
epilepsy  patients  who  still  have  seizures  after  surgery  is  6.3–9.3  per 
1000 people per year [5]. They will face the risk of epilepsy attacks at 
any  time  for  a  long  time  or  even  throughout  their  lives.  Therefore, 
long-term  seizure  detection  methods  that  can  be  used  out-of-hospital 
would  greatly  improve  the  ability  of  people  with  epilepsy  to  live 
independently.

Studies have shown that before and during an epileptic seizure onset, 
there are several characteristics significantly different from other stages, 
such as headache, chest tightness, sleep disorders, and irritability [5]. 
These  symptoms  are  often  reflected  in  multiple  physiological  signals, 
and  timely  identification  is  crucial  for  detecting  seizures.  Pre-ictal 
symptoms may even be able to predict the onset of epilepsy. In 2017, 
the American Academy of Neurology and the American Epilepsy Society 
jointly issued a practice guideline about the incidence and risk factors of 
SUDEP,  which  pointed  out  that  if  monitoring  equipment  is  used,  the 
caregivers of the patients can be notified promptly when an epileptic 
seizure occurs [6]. If appropriate measures are taken, the chances of the 
occurrence of respiratory dysfunction and hypoxemia will be reduced.

SUDEP  usually  occurs  within  a  short  time  of  a  convulsive  seizure 
(2–17 minutes, average 10 minutes) and may result in a hypo ventilatory 
state  or  asphyxia,  accompanied  by  normal  arousal  dysfunction  [5]. 
Because of the uncertainty of the time and place of epileptic seizures, 
patients may have seizures at any time and harm themselves. Therefore, 
caregivers should provide constant supervision to ensure the safety of 
the patient. Especially at night, it is difficult for caregivers to be with 
patients all the time. In this context, wearable devices provide a more 
convenient option for both caregivers and patients, allowing for greater 
independence and safety in patients’ daily lives.

At present, the work of detecting epileptic seizures mainly focuses on 
identifying  abnormal  changes  in  patients’  electrocardiography  (EEG) 
[7–10],  clonus  [11,12],  tachycardia  [13,14],  and  other  abnormal 
symptoms  in  respiration  rate  and  sounds  [15].  Compared  with 
short-term episodic detection methods such as video-EEG used in clin-
ical practice, continuous detection is an approach for prolonged moni-
toring of epileptic patients, providing timely detection of seizures.

In  clinical  settings,  video-EEG  systems  are  employed  for  patient 
monitoring  [12],  which  is  the  gold  standard  for  epileptic  seizure 
monitoring. However, the placement of EEG devices on patients’ scalps 
may  induce  discomfort  and  allergic  reactions,  while  restricting  their 
activities.  Consequently,  video-EEG  monitoring  is  not  suitable  for 
long-term daily use. Considering that continuous monitoring of epilepsy 
patients must not affect patients’ normal life, using wearable sensors is 
considered  promising  because  of 
its  good  portability  and 
non-invasiveness.

Body movement is considered a preferred choice for analysis among 
all non-EEG modalities because clear and distinguishable features can be 
observed in movement signals during epileptic seizures characterized by 
the associated motor phenomena [16]. In motor seizures, the distinctive 
movements are often composed of patterns similar to those induced by 
electrical  stimulation  of  the  primary  motor  areas  of  the  brain.  Motor 
seizures  typically  consist  of  a  series  of  single  or  multiple  movement 
patterns, namely myoclonic jerks, clonic movements, and tonic move-
ments  [17].  Moreover,  the  most  straightforward  manifestation  of 
movement is reflected in the changes in the accelerometry (ACM) signal 
[18,19]. In addition to body movement, the ictal tachycardia is also an 
important physiological characteristic of convulsive seizures (including 

bilateral  tonic-clonic  seizures  and  generalized  tonic-clonic  seizures) 
which is particularly common in temporal lobe epilepsy. The incidence 
of ictal tachycardia is about one-third of epileptic seizures [20] and may 
even occur a few seconds before body movements. Abnormal changes in 
HR can be used for early seizure detection. Studies employing electro-
cardiography (ECG) for seizure detection have predominantly concen-
trated  on  patients  in  hospital  settings  [21–23].  The  data  analysis 
primarily focuses on the magnitude and duration of HR elevation, often 
involving the extraction of time- and frequency-domain features within 
each heartbeat cycle or a fixed-length sliding window. Jeppesen et al. 
[23] used wearable sensors to acquire ECG signals for seizure detection. 
They extracted a total of 20 features such as second-order central dif-
ference  of  HR  and  cardiac  sympathetic  index,  achieved  a  sensitivity 
(SEN) of 0.8 in detecting seizures using a thresholding classifier. How-
ever, since some seizures are not associated with HR changes but with 
solely body movement, these seizures would be missed when applying 
an  ECG-  or  HR-based  model.  Cooman  et  al.  [24]  designed  a  transfer 
learning algorithm using support vector machines (SVM) and ECG sig-
nals, and they found that the false detection rate was 1.9 times per hour 
and suggested that when combining ECG with other signal modalities 
such as ACM,  the false detection rate could decrease with a factor of 
5–10 compared to an ECG-only model. Vandecasteele et al. [22] moni-
tored patients’ seizures in a hospital environment using a bipolar ECG 
device.  They  achieved  promising  results  in  seizure  detection  by 
employing an SVM model based on features including the peak, mean, 
and standard deviation of HR, although the results were slightly worse 
than  the  use  of  ECG.  Moreover,  Mohammadpour  et  al.  [25]  and  El 
Atrache et al. [26] found that the frequency, amplitude, duration, slope, 
smoothness, and area under the curve of photoplethysmography (PPG) 
signals would all changed during seizures. This suggested the potential 
value  of  using  more  PPG  characteristics  rather  than  only  HR  for 
improving seizure detection. However, only using ECG or PPG signals to 
detect seizures seem not sufficient. In the case of epileptic seizures, HR 
related  measurements  may  be  combined  with  body  motion  related 
measurements to ensure greater accuracy [27].

Traditional  statistical  analyzing  methods  rely  on  manual  feature 
extraction, which demands significant human efforts. Moreover, hand- 
crafted feature extraction may not encapsulate all the pertinent infor-
mation necessary for effective seizure detection. DL methods offer the 
advantage of automatically processing data by learning and extracting 
features  directly  from  signals.  Moreover,  they  could  discern potential 
relationships  and  interactions  among  different  dimensions  within  the 
data. This capability enables DL models to capture complex patterns and 
dependencies that may not be readily apparent through manual feature 
extraction or traditional analysis techniques. In this study, we adopt a 
hybrid design: raw ACM and PPG signals are first transformed into a set 
of statistical and physiological features, which are then processed by a 
DL  model.  This  approach  combines  the  interpretability  and  computa-
tional  efficiency  of  feature  engineering  with  the  pattern  recognition 
capabilities of DL, potentially improving seizure detection performance 
by incorporating additional PPG characteristics alongside HR. Similar 
feature engineering and integration strategies have also demonstrated 
clinical value in other disease prediction domains [28].

Although  various  seizure  detection  methods  have  been  proposed 
using EEG, ECG, ACM signals, and others, most of them are limited to in- 
hospital settings or rely on single-modality inputs. Most previous studies 
were  also based  on short-term  datasets  collected over  a  few hours  or 
days, limiting their ability to reflect long-term usability and reliability. 
Furthermore,  few  studies  focus  on  continuous  monitoring  during 
nocturnal  sleep  for  a  long  period  in  real-world,  out-of-hospital  envi-
ronments.  Existing  methods  either  lack  generalizability,  impose 
discomfort  due  to  sensor  placement  (e.g.,  EEG),  or  demonstrate  high 
false alarm rates when deployed in wearable devices. These limitations 
highlight a significant gap in developing seizure detection systems that 
are not only accurate and multimodal, but also suitable for real-world, 
long-term use.

2 

C. Dong et al.                                                                                                                                                                                                                                    

Computer Methods and Programs in Biomedicine 273 (2026) 109087 

Kempenhaeghe Academic Center for Epileptology, the Netherlands. As 
shown  in  Fig.  1,  signals  were  collected  with  the  armband  and  trans-
mitted to a base station. The NightWatch system proved a sensitive and 
convenient monitoring method for epileptics with convulsive seizures, 
especially for those who had more seizures at night while releasing their 
caregivers from accompanying the patients all day long.

The collected raw ACM and PPG signals had a sampling rate of 11–12 
Hz and 100 Hz, respectively. To ensure signal quality and consistency, 
any nightly recording containing sampling dropouts was excluded from 
analysis.  This  quality  control  process  resulted  in  a  final  dataset 
comprising 788 validated nights, totaling approximately 6304 hours of 
recordings. Both ACM and PPG signals were subsequently resampled to 
20 Hz to unify the temporal resolution for downstream processing.

Seizure annotations were made by experienced clinicians and trained 
nurses  based  on  synchronized  video  and  audio  recordings.  The anno-
tated events were categorized into three clinically significantly severe 
types: (1) tonic-clonic seizures, (2) major hypermotor seizures, and (3) 
prolonged  tonic  seizures  exceeding  30  seconds.  Minor  seizures, 
including myoclonic or short tonic events, were not included as alarm 
targets in this study. To ensure labeling consistency, 10 % of the anno-
tations  were  randomly  selected  and  cross-reviewed  by  clinicians  for 
quality  assurance.  The  final  dataset  was  structured  for  supervised 
learning, with seizure and non-seizure segments labeled accordingly.

3. Methods

The  proposed  seizure  detection  framework  consists  of  two  steps. 
Fig. 2 presents the algorithmic structure and technical pipeline of the 
proposed two-stage seizure detection framework, including (A) the pre- 
screening module, (B) the feature extraction process, and (C) the deep 
learning  classifier  architecture.  The  first  step  is  a  lightweight  pre- 
screening step aiming at identifying suspected seizure events as many 
as possible with a simple thresholding algorithm, where a large part of 
recordings  corresponding  to  non-seizure  periods  can  be  excluded  for 
further  analysis.  This  can  prevent  feeding  all  data  into  deep  neural 
networks for model learning which is expected to be of high computa-
tional load. Instead, a subset of data after pre-screening remains to be 
used  for  DL.  Importantly,  the  pre-screening  should  be,  on  purpose, 
allowed  to  miss  no  or  only  a  small  number  of  actual  seizure  events. 
Among  the  suspected  severe  seizures,  there  could  be  severe  seizures, 
minor seizures, and other non-seizure activities such as turning over in 
the bed, sitting up or waking up. The second step is the seizure detection 
step, during which a DL model is trained on the data of the suspected 
events to detect severe seizure events from all other suspected events. In 
this paper, for seizure detection, seizures are referred to severe seizures 
excluding  minor  seizures,  and  non-seizure  events  are  referred  to  the 
remaining suspected events including non-seizures and minor seizures.

In contrast, our work leverages a long-term dataset spanning several 
months,  providing  real-world  evidence  for  system  performance  and 
robustness under daily-life conditions. To address these challenges, this 
study  aims  to  develop a  two-stage seizure  detection framework  using 
multichannel  or  multimodal  signals  (ACM  and  PPG)  collected  from  a 
wearable  armband.  The  proposed  system  includes  a  lightweight  pre- 
screening  module  to  reduce  computational  load  and  a  CNN-LSTM- 
based  classifier  with  attention  mechanism  for  accurate  seizure  recog-
nition. Our objective is to enable robust, low false-alarm, and real-time 
detection of severe nocturnal seizures in out-of-hospital settings, thereby 
supporting independent living for people with epilepsy.

Comparing with some related recent studies as shown in Table 1, the 

main contributions of this study are summarized as follows: 

• Multimodal Signal  Fusion: We integrate tri-axial ACM and  PPG  to 
capture both movement and cardiovascular changes during seizures, 
enabling richer feature representation.

• Two-Stage Detection Framework: A lightweight pre-screening algo-
rithm  filters  out  irrelevant  segments  with  94  %  sensitivity  while 
reducing data volume by 81 %, followed by a CNN-LSTM model with 
attention to classify seizure events.

• Improved Detection Performance: Our system achieves a sensitivity 
of 76.2 %, a false alarm rate of 0.165/hour, and an AUC of 0.793 on a 
real-world  dataset  spanning  6304  hours  from  68  patients,  out-
performing traditional single-modality methods.

• Scalable  Wearable  Application:  The  proposed  approach  supports 
continuous, unobtrusive seizure monitoring in home environments, 
demonstrating  the  feasibility  of  deploying  DL  models  in  real-time 
healthcare settings.

The paper is organized as follows. Section 2 describes the dataset and 
data  acquisition  protocol.  Section  3 presents  the  signal  preprocessing 
techniques, the pre-screening strategy, and the architecture of the DL 
model. Section 4 provides experimental results and comparative anal-
ysis. Discussions, conclusions, limitations, and future work are given in 
Section 5 and 6.

2. Data collection and annotation

In  this  prospective  study,  nocturnal  tri-axial  ACM  and  PPG  re-
cordings  were  continuously  collected  using  a  NightWatch®  armband 
(LivAssured,  Leiden,  The  Netherlands)  from  68  patients  during  the 
night.  Each  patient  was  monitored  for  two  to  three  months  in  the 

Table 1 
Related recent studies in seizure detection highlighting signal modalities, clin-
ical scenarios, and model types.

Study (Year)

Signal Modality

Scenario

Ahmad et al. 
(2024) [7]

Qiu et al. (2023) 

[8]

Yang et al. (2021) 

[11]

Johansson et al. 
(2019) [12]
Vandecasteele 
et al. (2017) 
[22]

Touserkani et al. 
(2020) [25]
Our proposed 

method

EEG (publicly 
accessible 
database)
EEG (publicly 
accessible 
database)
Video

3-axis ACM

ECG and PPG

PPG

ACM and PPG

In- 
hospital

In- 
hospital

In- 
hospital
In- 
hospital
In- 
hospital

In- 
hospital
Out-of- 
hospital

Seizure 
Type

Model Type

Not 
mentioned

DL 
classifiers

Not 
mentioned

DL 
classifiers

GTCS

TC

focal 
seizure

GTCS

Severe 
seizures

DL 
classifiers
Single ML 
classifier
Single ML 
classifier

Statistical 
analysis
DL 
classifiers

Note: DL = deep learning; ML = machine learning; TC = tonic-clonic; GTCS =
Generalized tonic-clonic seizure.

Fig.  1. The  NightWatch  wearable  armband  and  base  station  for  nocturnal 
seizure monitoring.

3 

C. Dong et al.                                                                                                                                                                                                                                    

Computer Methods and Programs in Biomedicine 273 (2026) 109087 

Fig. 2. Technical architecture of the proposed two-stage seizure detection framework. 
(A) Pre-screening module for extracting suspected seizure segments based on accelerometry and HR signals. (B) Feature extraction process for standardized 5-minute 
signal segments. (C) DL model architecture combining CNN, LSTM, and attention mechanism for final classification.

3.1. Pre-screening of suspected severe seizure events

To  reduce  computational  overhead  and  focus  model  training  on 
seizure-relevant segments, we implemented a rule-based pre-screening 
strategy  that  extracts  potential  seizure  episodes  based  on  changes  in 
motion  and  HR  signals.  For  PPG  signals,  a  second  order  Butterworth 
bandpass filter (0.5–3.5 Hz) was applied to reject noise and frequency 
components  outside  the  possible  HR  range.  The  choice  of  cutoff  fre-
quencies was to ensure the pass band corresponding to the human HR 
range  from  30  to  210  beats  per  minute  (BPM).  For  ACM  signals,  an 
eighth-order Butterworth lowpass filter with a 10 Hz cutoff was applied 
to remove high frequency interference. HR was estimated from the PPG 
signal by detecting the systolic peaks. Both ACM and HR signals were 
then resampled to 20 Hz to ensure temporal alignment.

In  our  previous  study  [29],  we  found  that  the  standard  deviation 
(SD)  of  the  ACM  signal  that  conveys  motion  artifacts  is  crucial  in 
assessing a subject’s body movement. In addition, we found that some 
TC  seizures  are  associated  with  increased  HR,  which  can  sometimes 
occur even before the body movements. Therefore, in the pre-screening 
step, to identify suspected events, we delved into quantifying both HR 
and motion changes.

In  this  study,  we  employed  a  dual-threshold  strategy  to  identify 
‘movement  active’  and  ‘HR  increased’  segments  from  the  resampled 
ACM and HR signals. As shown in Fig. 2. A, a sliding window of 10 s was 
used to calculate the SD of ACM signals, and a sliding window of 20 s 
was  used  to  calculate  the  HR’s  increasing  percentage  (IP),  compared 
with  the  HR  in  the  last  sliding  window,  as  shown  in  the  following 
equation:
IP (%) = HR(i) (cid:0) median HR

(1) 

,

median HR

where the HR(i) is the HR value at the time i [ranges from 0 to 1200 (in 
total 20 minutes)], and median_HR is the median value of the HR during 
the whole recording segment. If the SD is higher than 0.4 or if the IP is 
over  10  %,  we  considered  that  there  was  a  suspected  severe  seizure 
event,  and  we  combined  the  ‘motion  active’  events  and  the  ‘HR 
increased’  event together, as shown in Fig. 3. The dashed lines in the 
upper and lower graphs represent segments with ‘movement active’ and 
segments  with  ‘HR  increased’,  respectively.  If  there  is  partial overlap 

Fig. 3. Example of identifying suspected seizure segments based on ACM and 
HR signals. ‘accx, accy, accz’ are the ACM signal on x, y and z axis.

between the two types of segments, they will be merged into a complete 
segment, indicating a suspected epileptic seizure segment. Otherwise, 
they  will  constitute  separate  suspected  epileptic  seizure  segments. 
Therefore, the segments shown in this figure represent a segment that 
includes both ‘movement active’ and ‘HR increased’.

3.2. Seizure labeling and feature extraction

Each  suspected  severe  seizure  events  obtained  from  the  pre- 
screening step was assigned a binary label based on clinician-verified 
annotations. A segment was labeled as a ‘suspected severe seizure’ if a 
documented annotations occurred within or near its time window (±2 
minutes). Otherwise, the segment was considered a ‘non-seizure’ event. 

4 

C. Dong et al.                                                                                                                                                                                                                                    

Computer Methods and Programs in Biomedicine 273 (2026) 109087 

To maintain event-level consistency and avoid a real seizure event was 
divided into too many segments, when the time interval between two 
seizure segments was less than 100 s, we merged these two segments. 
When  multiple  seizure  events  occurred  within  a  four-minute  window 
around an annotation, we also labeled them all as one seizure event.

To  prepare  the  input  for  model  training,  each  suspected  severe 
seizure  event  was  transformed  into  a  fixed-length  feature  representa-
tion.  Before  training  the  detection  model,  we  first  standardized  the 
length  of  suspected  events  because  most  suspected  events  were  in 
different  length.  As  shown in  Fig. 4,  most  suspected  events  were  less 
than 5 minutes, so all segments were standardized to a duration of 300 s 
(5 minutes). Segments shorter than this length were zero-padded, while 
longer segments were cut. This fixed-length standard ensures consistent 
temporal input across samples.

From  each  segment,  we  extracted  nine  statistical  and  frequency- 
domain  features  at  1  Hz  resolution  from  the  ACM  and  HR  signals, 
including  the  SD  value,  entropy,  short-time  energy,  mean  value,  the 
lowest and highest envelope values, and the dominant frequency of the 
total acceleration, as well as the mean value and SD value of HR. The 
resulting data structure was a two-dimensional feature matrix of shape 
(300,  9),  capturing  the  temporal  evolution  of  physiological  patterns 
within each segment. This matrix served as the input to the DL classifier 
described in the next section.

3.3. Deep learning for seizure detection

To  further  classify  real  seizure  and  non-seizure  events  within  the 
suspected severe seizure segments, we designed a hybrid DL model that 
combines convolutional and recurrent layers with an attention mecha-
nism.  This  architecture  leverages  both  spatial  and  temporal  de-
pendencies within the extracted feature sequences.

As shown in Fig. 2.B and Fig. 2.C, the input to the DL model is a 2D 
feature matrix of shape (300, 9), representing a 5-minute segment with 
1-second resolution and nine features per timestep. The input feature 
matrix of shape (300, 9) passes through two initial convolutional layers 
with 16 and 32 filters, respectively, followed by max-pooling to reduce 
the  temporal  dimension.  A  third  convolutional  layer  with  64  filters 
further extracts hierarchical features, and max pooling is applied again. 
An  attention  mechanism  is  then  introduced  by  generating  dynamic 

Fig.  4. Segment  length  distribution  for  movement-active  and  heart-rate- 
increase events.

weights through a dense layer, which are element-wise multiplied with 
the feature maps to emphasize significant channels [30]. The resulting 
attended feature sequence is fed into an LSTM layer with 32 units to 
capture  temporal  dependencies.  Subsequently,  three  additional  con-
volutional and max-pooling blocks refine the features. Global average 
pooling aggregates the feature maps into a fixed-length vector, which is 
passed  through  a  fully  connected  layer  to  produce  the  final  seizure 
probability prediction.

To prevent overfitting, dropout was applied to the LSTM and dense 
layers  during  training.  The  proposed  model  was  implemented  using 
TensorFlow  and  trained  using  the  Adam  optimizer,  with  an  initial 
learning rate of 0.001, determined through a preliminary search among 
values  0.01  to  0.0001,  and  a  batch  size  of  64.  Early  stopping  with  a 
patience  of  10  epochs  was  employed  to  prevent  overfitting  based  on 
validation loss monitoring. The binary cross-entropy loss function was 
used  to  optimize  the  model  parameters.  To  decrease  the  inherent 
imbalance between seizure and non-seizure segments in the dataset, we 
applied  class  weighting  during  training,  assigning  a  higher  weight  to 
seizure samples in the binary cross-entropy loss function. The weights 
were  determined  based  on  the  inverse  frequency  of  each  class  in  the 
training  set,  thereby  ensuring  that seizure  events  contributed  propor-
tionally  more  to  the  optimization  process.  The  model  was  compiled 
using TensorFlow, Keras, and Python 3.11. The detailed parameters of 
the DL model and experimental setup are summarized in Table 2.

3.4. Model training and evaluation

Due  to  significant  variations  in  the  number  of  seizures  observed 
among  patients,  a  subject-independent  stratified  split  strategy  for  10- 
fold cross validation was used to ensure as much as possible a similar 
number of seizures per fold. Firstly, we sorted the patients in descending 
order based on their seizure occurrences (i.e., number of seizure events) 
and separated them into seven groups, each group contained nine or ten 
patients. Then one patient from each group was taken to constitute a fold 
of data. At last, we got ten folds of data, and each fold contained six to 
seven patients.

As shown in Fig. 5, in each training iteration, we selected one-fold to 
form a testing dataset comprising data from six or seven patients. The 
remaining folds were then utilized for both training and validation. This 
stratified split strategy allowed the model to be trained as a patient in-
dependent classifier by using one patient’s data only for training or only 
for testing. The amount and some statistics of the seizure events and the 

Table 2 
Experimental setup and DL model parameters.

Component

Parameter

Value/Description

Input features

Input shape

Feature types

Conv layer 1–3 +
Max-pooling
Dropout
Attention module

LSTM
Conv layer 4–6 +
Max-pooling
Global Average 
Pooling
Fully connected layer
Optimizer
Learning rate
Batch size
Epochs
Loss function
Task

DL model 

architecture

Training settings

Output

5 

(300, 9), 5-min segment at 1 s 
resolution
SD, entropy, short-time energy, 
dominant frequency, etc.
filters: 16, 32, 64; kernel: 2, 20, 4

0.3
Dynamic weights via dense layer ×
feature maps
32 hidden units
32→16 filters, kernel=4

’sigmoid’ activation
Adam
0.001
64
Earl stopping, patience = 10
Binary cross-entropy
Binary classification (seizure vs. non- 
seizure)

​
​
​
​
​
​
​
​
​
​
​
​
C. Dong et al.                                                                                                                                                                                                                                    

Computer Methods and Programs in Biomedicine 273 (2026) 109087 

Fig. 5. Subject-independent stratified split strategy in the model training and evaluation step.

monitoring duration of each fold are shown in Table 3.

The results of the detection model in test data were evaluated using 
receiver operating characteristic (ROC) curves, SEN and false alarm rate 
(FAR). The ROC curve is a graphical representation used to evaluate the 
performance of a classifier, which shows the relationship between the 
true positive rate and the false positive rate at different thresholds. The 
ROC  curve  captures  the  performance  of  the  classifier  over  the  entire 
prediction range, independent of a particular threshold. The area under 
the  ROC  curve  (AUC)  is  a  commonly  used  metric  that  indicates  the 
magnitude of the classifier’s ability to discriminate between all positive 
and  negative  samples.  In  this  work,  seizure  events  were  considered 
positive samples while non-seizures events were negative samples.

4. Results

In this study, we collected 1963 annotations from 68 patients during 
788 nights and recorded the onset time annotation of each seizure event. 
All  the  annotations  were  determined  by  the  clinicians  according  to 
abnormal  body  movements,  HR  raises,  sounds,  and  observations.  We 
then  obtained  seizure  events  labeled  according  to  the  annotations 
combined with the proposed pre-screening method. The average amount 
of seizure events per patients was 27.14 ± 63.55 (range from 1 to 372). 
The average monitoring time was 11.79 ± 19.25 nights (range from 1 to 
115).

By using the proposed pre-screening method, a total of 14,417 sus-
pected  severe  seizure  events  from  68  patients  were  identified,  where 
1109  (7.69  %)  of  which  were  TC  seizure  events,  564  (3.91  %)  were 
major seizure events and 173 (1.20 %) were other tonic seizures. The 
SEN  of  identifying  seizure  events  during  the  pre-screening  step  was 
0.940 and the PPV was 0.128. To be more specific, in the pre-screening 
step, a total of 1846 severe seizure events were successfully identified, 
and 117 annotations were not presented.

To  illustrate  the  time  difference  between  HR  increases  and  body 
movements, we plotted the percentage of increase in HR and the starting 

Table 3 
Distribution of seizure counts and monitoring duration across 10-fold partitions.

Fold

Number of 
patients

Number of 
seizures

Average number of 
seizures per patient

Monitoring 
duration (day)

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

7
7
7
7
7
7
7
7
6
6

95
95
103
115
123
132
160
291
315
409

13.57
13.57
14.71
16.43
17.57
18.85
22.86
41.57
45.00
68.17

52
75
70
72
55
61
75
138
95
95

time  of  body  movement  in  Fig.  6.  In  this  figure,  the  dark  blue  line 
showed  the  mean  HR  IP, and  the  light  blue  shadow area showed  the 
standard deviation. The red line corresponded to the movement starts of 
seizures recorded by the NightWatch. The red dashed line indicated that, 
on  average,  the  HR  increase  already  started  about  100  s  earlier  than 
seizure-related body movement. Interestingly, the moment when the HR 
increase reached its peak was close to the recorded start of movements.
In the seizure detection step, by using stratified split strategy and 10- 
fold cross validation to train and test the proposed attention-based CNN- 
LSTM algorithm, we obtained the ROC curve for each test fold, as shown 
in Fig. 7. It can be seen that the mean AUC over folds was 0.793 [95 % 
CI: 0.745–0.841], ranging from 0.647 to 0.902. To further examine the 
contribution  of  each  component,  we  conducted  a  simplified  ablation 
study  comparing  single-modality  inputs  and  the  full  proposed  frame-
work, with the results summarized in Table 4.

Furthermore, we calculated SEN and PPV for each fold of patients, 
and the results was presented in Fig. 8. The SEN and PPV varied among 
patients, so did the number of seizures that the patient had. The size of 
the shadow around the spot indicated the number of the sever seizure 
events that patient had. The best performance showed the SEN and PPV 
were  both  1.0,  and  the  worst  performance  showed  the  SEN  and  PPV 
were  both  0.0.  The  achieved  mean  SEN  was  0.762  [95  %  CI: 
0.704–0.821], and the mean PPV was 0.334 [95 % CI: 0.229–0.356]. In 
addition, the mean FAR per hour was 0.165 [95 % CI: 0.097–0.234]. 
Considering the SEN of 0.940 in the pre-screening step, the overall SEN 
of our proposed method in detecting severe seizure events for the entire 
dataset was 0.716 [95 % CI: 0.713–0.772].

Table 5 presented the results of the proposed method in this study in 
comparison  with  other  HR  related  sensors  for  seizure  detection  [24]. 
Notably, the SEN of single HR-based sensors, such as ECG and PPG, for 
seizure detection did not exceed 0.710. Specifically, when relying only 
on one wearable PPG sensor device, the SEN dropped to 0.320. How-
ever, this comparison is intended to provide a qualitative overview of 
the  sensing  approaches  and  application  settings,  rather  than  a  direct 
quantitative performance benchmarking.

Fig.  6. Temporal  alignment  of  HR  changes  and  movement  onset  dur-
ing seizures.

6 

C. Dong et al.                                                                                                                                                                                                                                    

Computer Methods and Programs in Biomedicine 273 (2026) 109087 

notable  performance  in  the  detection  step,  and  this  ensured  the  reli-
ability  of  using  it  in  the  real  scenario.  The  two-stage  strategy  was 
designed  to  reduce  false  positives  by  pre-screening  suspected  seizure 
segments  before  applying  the  DL  classifier.  The  multimodal  classifier 
design was chosen to leverage complementary physiological cues from 
accelerometry  and  photoplethysmography,  aiming  to  capture  both 
motor and cardiovascular changes during seizures.

The proposed two-stage seizure detection framework is intentionally 
designed  to  balance  modeling  complexity,  interpretability,  and 
deployment feasibility. The first pre-screening module employs simple 
statistical methods to rapidly exclude non-informative signal segments, 
reducing data volume by 81 % while preserving over 94 % of seizure 
events. The pre-screening module is lightweight and suitable for real- 
time  filtering  on  wearable  devices,  with  an  estimated  computational 
complexity of O(N), where N = T × D (time steps × signal dimensions). 
This indicates that the vast majority of clinically relevant seizures were 
retained for second-stage classification, and the computational cost was 
substantially alleviated. These results suggest that the pre-screening step 
introduces only a minimal trade-off in sensitivity while offering signif-
icant  gains  in  efficiency  and  feasibility  for  real-time  wearable 
deployment.

The  high  SEN  of  pre-screening  is  critical  in  clinical  applications 
where minimizing missed seizure events was paramount. However, the 
reasons for missing were varied. Importantly, the few cases marked as 
“missed”  during  pre-screening  were  primarily  due  to  annotation  dis-
crepancies, such as duplicate annotations of different phases of a single 
prolonged seizure or delayed manual records relative to the true onset, 
rather  than  the  inability  of  the  algorithm  to  capture  seizure-related 
physiological  changes.  In  the  pre-screening  step,  we  found  that  one 
seizure event could be originally annotated multiple times. These mul-
tiple  annotations  were  set  considering  separate  parts  of  a  single  long 
seizure event as several separate seizures by the nurses. Also, the an-
notations were acquired through different methods including the nurses’ 
diaries and the alarm of clinical devices according to increasing HR and 
abnormal  movements,  which  also  caused  duplicated  annotation.  In 
other  cases,  the  missed  annotations  recorded  by  clinicians  were  later 
than the  actual  time with body  movements  and/or HR  changes.  As  a 
result, the gap between the event and the annotation might exceed the 
threshold  we  have  set.  Our  pre-screening  algorithm  treated  these 
duplicated and late annotations as ‘missed’ events. Moreover, in the pre- 
screening  step,  we  only  considered  severe  seizure  annotations,  while 
some minor seizures that do not require alarms were present as well, and 
those  minor  seizures  might  be  screened  as  suspected  severe  seizures. 
This approach aimed to highlight the detection of clinically severe sei-
zures, thereby reducing the effects of alarms from minor events.

The second stage uses a hybrid CNN-LSTM network with attention, 
integrating convolutional layers for local pattern extraction. An LSTM 
layer for modeling long-range dependencies, and an attention mecha-
nism  for  dynamic  weighting  of  time  points.  While  this  introduces 
moderate  structural  complexity,  it  enables  the  model  to  capture  tem-
poral progression across HR and movement channels, which is essential 
to reveal our novel physiological observation that ictal HR changes often 
precede  motor  manifestations.  In  terms  of  computational  complexity, 
the CNN and attention components are both O(N), while the LSTM in-
troduces a higher cost of O(N²) due to its recurrent operations over time 
steps. However, the system remains feasible for deployment considering 
the data volume reduction from the first step and the moderate size of 
the input sequence. Before applying DL, we reduce the size of the dataset 
substantially (from 6304 hours to 1201 hours), which greatly cuts down 
the computational cost and makes our approach more suitable for real- 
time applications. The optimal average accuracy of the CNN DL model 
integrating  the  attention  and  LSTM  layers  was  0.794.  This  result  in-
dicates that our model reliably distinguishes between seizure and non- 
seizure events in most cases.

However, as shown in Fig. 8, the performance of the seizure detec-
tion model varied across patients. For patients with low PPV but high 

Fig.  7. Receiver  operating  characteristic  (ROC)  curves 
cross-validation.

from  10-fold 

Table 4 
Ablation  results  show  the  contribution  of  each  component  in  the  proposed 
framework.

Research

ACM-only

PPG-only

Proposed method 
(ACM+PPG)

AUC [95 % CI]

SEN [95 % CI]

PPV [95 % CI]

0.731 
[0.592–0.870]
0.595 
[0.481–0.708]
0.793 
[0.745–0.841]

0.634 
[0.510–0.757]
0.596 
[0.472–0.721]
0.716 
[0.713–0.772]

0.236 
[0.169–0.302]
0.160 
[0.113–0.206]
0.334 
[0.229–0.356]

Fig. 8. Sensitivity (SEN) and positive predictive value (PPV) distribution across 
patients. Dot size represents the number of seizure events per patient.

5. Discussion

In this study, we developed a two-step approach for detecting severe 
nocturnal epileptic seizures using a combination of ACM and PPG data 
from an armband, which showed high SEN in the pre-screening step and 

7 

C. Dong et al.                                                                                                                                                                                                                                    

Computer Methods and Programs in Biomedicine 273 (2026) 109087 

Table 5 
Performance comparison between the proposed multimodal method and single-modality (ECG- or PPG-based) seizure detection models.

Research

Device

Classifier

Patients

Monitoring duration

Seizures

SEN

FAR /hour

Proposed method
Cooman et al. [24]
Vandecasteele et al. [22]

ACM + PPG wearable armband
single-lead ECG
clinical ECG device
wearable ECG device
wearable PPG device

CNN+ LSTM with attention
SVM+ transfer learning
SVM
SVM
SVM

68
24
11
11
11

783 nights (>8000 hours)
2172 hours
701 hours
701 hours
701 hours

1846
227
47
47
47

0.716
0.710
0.570
0.700
0.320

0.165
1.900
1.920
2.110
1.800

Note: SEN=sensitivity; FAR=false alarm rate; ACM=accelerometry; PPG=photoplethysmography; ECG=electrocardiography.

SEN, we found that they experienced more minor seizures compared to 
other patients. Our algorithm successfully detected these minor seizures 
but did not label them as severe seizure events, resulting in higher FAR. 
This  discrepancy  indicated  that  although  our  model  was  good  at 
detecting  seizure  events,  it  sometimes  overestimated  their  severity, 
resulting in more false positives. For the patient with a PPV of 0.0 and 
SEN of 0.0, reason for this result is that he/she had a very small number 
of seizures, only one or two in most cases. This limited number of events 
greatly affected the statistical reliability of performance metrics for this 
case,  suggesting  that  the  model’s  performance  metrics  might  be  less 
reliable for patients with extremely low seizure frequencies.

Our proposed method achieved a higher SEN while maintaining an 
acceptable  FAR  compared  to  existing  studies.  Most  studies  had  faced 
challenges in balancing SEN and specificity, especially in reducing FAR 
without  severely  compromising  the  detection  of  true  seizure  events. 
Although the system exhibits relatively lower PPV, it was intentionally 
optimized for high SEN to minimize the risk of missing nocturnal sei-
zures, given their potentially severe clinical consequences. In practical 
use, the detection threshold can be adapted to patient-specific needs and 
caregiver  tolerance  for  false  alarms,  allowing  customization  of  the 
SEN–PPV trade-off.

As shown in Table 5 , in the field of seizure detection, single ECG and 
HR-based sensors such as PPG had lower SEN and higher FAR. Specif-
ically, when relying on only one wearable PPG sensor device, the SEN 
dropped to 0.320. This drop was attributed to the instability of the PPG 
signal during a seizure, where movements such as clonus could intro-
duce instability and motion artifacts [31]. As a result, the PPG signal 
contained  a  lot  of  noise,  making  it  impractical  to  extract  reliable  HR 
information by digital filtering. This result suggested that adding body 
movements  as  a  supplement  to  the  seizure  detection  process  can 
significantly  reduce  FAR.  However,  this  table  presents  a  structured 
comparison of representative studies using different sensing modalities 
for seizure detection. As these studies vary in data sources and evalua-
tion standards, the comparison is qualitative rather than quantitative. 
We  fully  recognize  that  comparing  performance  across  studies  is 
inherently  difficult  due  to  differences  in  patient  populations,  sensor 
modalities,  recording  environments,  and  annotation  protocols.  In 
particular,  most  existing  studies  rely  on  hospital-grade  EEG  data  or 
short-term recordings under controlled conditions. These datasets often 
exclude  ambiguous  or  hard-to-annotate  cases,  resulting  in  relatively 
balanced  class  distributions  and  potentially  optimistic  performance 
estimates.

In contrast, our study is based on a long-term, real-world wearable 
dataset collected in natural home environments, where seizure preva-
lence is extremely low and motion artifacts are common. Such condi-
tions  pose  significant  challenges  for  both  detection  performance  and 
clinical applicability. To the best of our knowledge, there is currently no 
publicly available open-access dataset of long-term wearable recordings 
for seizure detection. This makes it impossible to perform standardized, 
cross-study model evaluation. Moreover, the algorithms developed for 
EEG-based detection may not generalize to wearable signals like PPG 
and ACM. Given these limitations, we aim to benchmark our framework 
specifically within the wearable sensor context, and we hope that this 
work can help promote the creation of open, continuous, and realistic 
seizure  datasets  collected  from  wearable  devices.  If  regulatory 

8 

conditions allow, such datasets would be crucial for enabling fair com-
parisons and accelerating advances in the field.

In  the  seizure  detection  step,  we  combined  HR  information  (from 
PPG) and movement information (from ACM). By including PPG and HR 
signals,  we  not  only  proposed  a  novel  DL-based  seizure  detection 
framework but also revealed a previously underexplored physiological 
insight: the onset of ictal HR changes typically precedes seizure-related 
motor  activity  during  severe  seizures.  This  temporal  relationship, 
observed  consistently  across  real-world  multimodal  recordings,  offers 
valuable  information  for  early  and  accurate  seizure  detection.  To 
leverage  this  phenomenon,  we  incorporated  a  hybrid  CNN-LSTM  ar-
chitecture  with  an  attention  mechanism,  allowing  the  model  to 
dynamically  focus  on  temporal  features  across  both  PPG  and  ACM 
channels. This design enables the system to prioritize early cardiac ab-
normalities  while  capturing  subsequent  movement  patterns,  thereby 
improving detection sensitivity and reducing latency. However, when 
the  PPG  signal  was  of  poor  quality,  the  attention  mechanism  in  the 
proposed  detection  model  was  expected  to  shift  focus  away  from  the 
PPG  signal.  In  such  cases,  the  model  reduced  the  weight  of  the  HR 
related  channels  when  the  ACM  signal  changed  drastically.  This 
adjustment  resulted  in  a  more  stable  detection  effect.  Therefore,  the 
method  proposed  in  this  paper  has  a  higher  SEN  and  lower  FAR  in 
seizure  detection.  Our  approach  proved  effective  in  facing  the  chal-
lenges posed by motion artifacts and noise, enhancing the overall reli-
ability of seizure detection.

In addition to the main evaluation, we conducted a simplified single- 
modality analysis to assess the contribution of each input channel. Using 
only  ACM  could  capture  most  convulsive  seizures  but  missed  cases 
where  ictal  HR  changes  occurred  prior  to  motor  activity.  Conversely, 
using only PPG was highly vulnerable to motion artifacts, leading to an 
increased number of false alarms. These limitations were mitigated by 
integrating both modalities, enabling the framework to leverage com-
plementary  physiological  information.  This  observation  provides  sup-
portive  evidence  for  the  rationale  of  multimodal  integration.  These 
findings confirm that both the two-step strategy and the use of multi-
modal  signals  are  essential  in  achieving  a  balance  between  accuracy, 
efficiency, and robustness in real-world wearable seizure detection. This 
work  demonstrated  a  feasible  multimodal,  two-stage  framework  for 
nocturnal  seizure  detection  in  real-world  wearable  recordings.  The 
development  of  more  advanced  fusion  algorithms  and  a  systematic 
quantification of multimodal advantages will be the focus of our future 
investigations.

Unlike many  high-performing EEG-based seizure  detection models 
evaluated  on  open-access  datasets,  our  dataset  consists  of  long-term, 
real-world recordings that are naturally imbalanced and noisy. Public 
datasets often contain carefully selected, well-annotated segments with 
relatively balanced seizure prevalence, which may not reflect the chal-
lenges  of  continuous  monitoring.  In  contrast,  real-world  data  may 
include only a few seizure events over several weeks, with significant 
motion artifacts and ambiguous signal patterns. These factors inherently 
limit model performance and increase the difficulty of achieving high 
PPV. Motion artifacts, transient signal dropouts, and PPG unreliability 
during movements could potentially affect the seizure detection. These 
effects  were  partially  mitigated  through  preprocessing  and  the  pre- 
segments. 
screening 

that  filters  out  non-informative 

stage 

​
​
C. Dong et al.                                                                                                                                                                                                                                    

Computer Methods and Programs in Biomedicine 273 (2026) 109087 

Furthermore, the attention mechanism embedded in the DL model helps 
dynamically focus on more informative temporal and channel features, 
thereby reducing the negative impact of noisy or unreliable PPG signals. 
Future  deployments  will  integrate  adaptive  noise  suppression  tech-
niques and redundant sensing modalities to enhance robustness under 
real-world conditions.

Despite  these  challenges,  our  method  maintains  acceptable  sensi-
tivity (SEN = 0.716) and a low false alarm rate (FAR = 0.165/h), which 
are clinically relevant for nocturnal seizure detection. In practice, while 
some false alarms are tolerable, especially for severe seizure detection, it 
remains important to continue optimizing the PPV to reduce caregiver 
burden. Therefore, we prioritize improving the FAR while retaining high 
sensitivity.

In  our  experimental  evaluation,  a  5-minute  analysis  window  was 
employed  to  ensure  sufficient  feature  extraction  from  ACM  and  PPG 
signals.  This  window  was  implemented  as  a  historical  (non-centered) 
window, meaning that seizure-related features at the beginning of the 
segment  could  trigger  early  detection  without  waiting  for  the  full 
duration to pass. To address potential concerns about detection latency, 
we  note  that  although  a  5-minute  analysis  window  was  used  in  this 
study,  the  intended  deployment  is  a  real-time  sliding-window  system 
with partial overlap, which is initiated only after the pre-screening stage 
flags a suspected seizure segment. Detection is then triggered as soon as 
seizure  activity  enters  the  window,  allowing  for  updates  every  few 
seconds  and  supporting  timely  nocturnal  alerts  in  practical  use.  This 
means that the alarm does not necessarily require the entire 5-minute 
segment  to  elapse  but  can  occur  earlier  depending  on  when  the 
seizure activity enters the analysis window. Moreover, clinical studies 
have  reported  that  caregiver  response  times  to  nocturnal  seizures  at 
home often range from 30 s to several minutes [32], suggesting that our 
framework’s latency is within a clinically acceptable range.

Furthermore,  our  proposed  framework  is  tailored  for  real-world 
deployment  in  wearable  devices.  By  utilizing  both  PPG  and  tri-axial 
ACM  signals,  which  were  commonly  available  in  commercial  arm-
bands, we ensure broad applicability without requiring EEG or complex 
clinical infrastructure. The two-step structure, including a lightweight 
pre-screening module and a deep classification model, reduces compu-
tational load by over 80 %, facilitating continuous long-term monitoring 
at home. These findings and architectural innovations demonstrate not 
only the scientific novelty but also the practical utility of our work in 
supporting  independent  living  and  proactive  care  for  people  with 
epilepsy.

However,  there  were  several  limitations  of  this  study.  First,  the 
dataset, while wide-ranging, was derived from specific patients and they 
had highly imbalanced number of seizures. This might limit the gener-
alizability of our findings. Additionally, the variability in seizure types 
among different patients suggested that a one-fits-all model might not be 
optimal.  Future  work  will  incorporate  more  diverse  patient  de-
mographics and seizure phenotypes to improve the generalizability of 
the proposed approach. Our future work would also explore personal-
ized models that are able to adapt to the characteristics of individual 
patients. It is also important to address data imbalances to improve the 
reliability  and  accuracy  of  models  across  all  patients.  Future  studies 
should  also  focus  on  improving  model  specificity  and  reducing  FAR 
without compromising SEN. Furthermore, data augmentation represents 
a promising direction for enhancing the robustness of seizure detection 
models. However, unlike in image domains, augmentation for physio-
logical signals such as PPG and ACM requires careful consideration to 
preserve clinical and temporal validity. More advanced techniques, such 
as using generative models to simulate realistic seizure-like events, also 
require thorough validation. Given these complexities, we consider data 
augmentation a non-trivial yet important research direction and plan to 
address it in future dedicated studies.

In  summary,  our  study  demonstrates the  feasibility of  a  two-stage 
multimodal  seizure  detection  framework  that  balances  computational 
efficiency and accuracy. By combining ACM and PPG/HR signals within 

9 

an  attention-enhanced  CNN–LSTM  model,  the  system  captures  com-
plementary physiological cues and the temporal precedence of ictal HR 
changes,  which  enhances  detection  reliability  and  is  an  important 
underexplored  physiological  phenomenon.  The  use  of  a  wearable 
armband further underscores the clinical value of enabling continuous, 
non-invasive nocturnal monitoring at home. This expands accessibility 
to  a  broader  patient  population,  reduces  caregiver  burden,  and  ad-
dresses the urgent need for SUDEP risk mitigation during unsupervised 
night-time  periods.  Nevertheless,  prospective  validation  in  larger  and 
more diverse patient cohorts will be essential to fully establish clinical 
effectiveness.

Beyond detection accuracy, the proposed method has the potential to 
contribute to understanding lifestyle-related seizure triggers. Commonly 
reported factors such as sleep deprivation, physical or emotional stress, 
hormonal  changes,  and  alcohol  or  drug  use  are  known  to  influence 
seizure  onset  in  many  patients.  By  enabling  continuous  home-based 
monitoring,  our  system  could  facilitate  the  identification  of  temporal 
patterns between lifestyle factors and seizure events. Integrating wear-
able data with self-reported behavioral logs in future studies may offer 
deeper insight into modifiable seizure risks and inform targeted inter-
vention strategies aimed at seizure prevention.

6. Conclusion

In conclusion, our study presented a practical and effective approach 
for the long-term detection of severe nocturnal epileptic seizures using a 
wearable  system  that  combines  motion  and  cardiac  signals.  The  pro-
posed two-step method, incorporating both pre-screening and DL, de-
livers  improved  sensitivity  and  reduced  false  alarms  compared  to 
existing  approaches.  Despite  certain  limitations,  the  results  indicated 
significant  potential  for  improving  patient  care  and  warrant  further 
investigation  and  refinement.  Importantly,  it  provides  new  opportu-
nities to investigate lifestyle-related seizure triggers in real-world set-
tings,  thereby  advancing  early  detection  and  prevention  strategies  in 
epilepsy management. This work provides a promising approach toward 
scalable,  accurate,  and  efficient  seizure  detection  systems,  advancing 
the  integration  of DL  methodologies  into  wearable  health  monitoring 
applications.

Data availability

The  data  that  support  the  findings  of  this  study  are  not  openly 
available due to reasons of sensitivity and are available from the cor-
responding author upon reasonable request.

Funding

This work was supported by the Natural Science Research Program of 
the Education Department of Hebei Province (No. QN2025378), Hebei 
Medical University Postdoctoral Fund. (No. 30705010045) and Hebei 
Yanzhao  Golden  Platform  Talent  Gathering  Plan  Backbone  Talent 
Project (Overseas Returnees Platform) of Hebei Provincial Department 
of Human Resources and Social Security (No. B2025012).

Ethics approval

This study has the formal ethical approval from the Ethics Committee 
of Kempenhaeghe Epilepsy Center in the Netherlands, all participants or 
their legal guardians provided written informed consent.

Consent to participate

Informed  consent  was  obtained  from  all  individual  participants 

included in the study.

C. Dong et al.                                                                                                                                                                                                                                    

Computer Methods and Programs in Biomedicine 273 (2026) 109087 

CRediT authorship contribution statement

Chunjiao  Dong:  Writing  –  original  draft,  Visualization,  Software, 
Methodology, Funding acquisition. Johannes P. van Dijk: Supervision, 
Data curation, Conceptualization. Ronald M. Aarts: Writing – review & 
editing,  Supervision, Conceptualization. Yunfeng  Wang: Supervision, 
Investigation. Xi Long: Writing – review & editing, Supervision, Project 
administration, Conceptualization.

Declaration of competing interest

The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.

References

[1] K.M. Fiest, K.M. Sauro, S. Wiebe, S.B. Patten, C.S. Kwon, J. Dykeman, et al., 

Prevalence and incidence of epilepsy: a systematic review and meta-analysis of 
international studies, Neurology 88 (3) (Jan. 17 2017) 296–303, https://doi.org/ 
10.1212/WNL.0000000000003509.

[2] V. Patil, M. Madgi, A. Kiran, Early prediction of Alzheimer’s disease using 

convolutional neural network: a review, Egypt. J. Neurol. Psychiatr. Neurosurg. 58 
(1) (2022) 130, https://doi.org/10.1186/s41983-022-00571-w.

[3] U. Kramer, S. Kipervasser, A. Shlitner, R. Kuzniecky, A novel portable seizure 
detection alarm system: preliminary results, J. Clin. Neurophysiol. Publ. Am. 
Electroencephalogr. Soc. 28 (1) (Feb 2011) 36–38.

[4] S. Shorvon, T. Tomson, Sudden unexpected death in epilepsy, Lancet 378 (9808) 

(Dec. 10 2011) 2028–2038.

[5] D.C.H. Devinsky, D.J. Thurman, S. Lhatoo, G. Richerson, Sudden unexpected death 

in epilepsy: epidemiology, mechanisms, and prevention, Lancet Neurol. 15 (10) 
(Sep. 2016) 1075–1088, https://doi.org/10.1016/S1474-4422(16)30158-2.
[6] C. Harden, T. Tomson, D. Gloss, J. Buchhalter, J.H. Cross, E. Donner, et al., Practice 
guideline summary: sudden unexpected death in epilepsy incidence rates and risk 
factors: report of the guideline development, dissemination, and implementation 
subcommittee of the American Academy of Neurology and the American Epilepsy 
Society, Neurology. 88 (17) (Apr. 25 2017) 1674–1680.

[7] X.W. Ahmad, D. Javeed, P. Kumar, O.W. Samuel, S. Chen, A hybrid deep learning 
approach for epileptic seizure detection in EEG signals, IEEE J. Biomed. Health Inf. 
PP (Apr. 10 2023) 1–12.

[8] X. Qiu, F. Yan, H. Liu, A difference attention ResNet-LSTM network for epileptic 

seizure detection using EEG signal, Biomed. Signal. Process. Control 83 (2023) 
104652.

[9] Y. Sun, W. Jin, X. Si, X. Zhang, J. Cao, L. Wang, et al., Continuous seizure detection 
based on transformer and long-term iEEG, IEEE J. Biomed. Health Inf. 26 (11) 
(Nov. 2022) 5418–5427, https://doi.org/10.1109/JBHI.2022.3199206.
[10] Y.R. Aldana, B. Hunyadi, E.J.M. Reyes, V.R. Rodriguez, S. Van Huffel, 

Nonconvulsive epileptic seizure detection in scalp EEG using multiway data 
analysis, IEEE J. Biomed. Health Inf. 23 (2) (Mar. 2019) 660–671, https://doi.org/ 
10.1109/JBHI.2018.2829877.

[11] Y. Yang, R.A. Sarkis, R.E. Atrache, T. Loddenkemper, C. Meisel, Video-based 

detection of generalized tonic-clonic seizures using deep learning, IEEE J. Biomed. 
Health Inf. 25 (8) (Aug. 2021) 2997–3008, https://doi.org/10.1109/ 
JBHI.2021.3049649.

[12] D. Johansson, F. Ohlsson, D. Krýsl, B. Rydenhag, M. Czarnecki, N. Gustafsson, et 
al., Tonic-clonic seizure detection using accelerometry-based wearable sensors: a 
prospective, video-EEG controlled study, Seizure 65 (Feb. 2019) 48–54, https:// 
doi.org/10.1016/j.seizure.2018.12.024.

[13] M. Lucchesi, J.B. Silverman, K. Sundaram, R. Kollmar, M. Stewart, Proposed 

mechanism-based risk stratification and algorithm to prevent sudden death in 

epilepsy, Front. Neurol. 11 (Jan. 25 2021) 618859, https://doi.org/10.3389/ 
fneur.2020.618859.

[14] S. Behbahani, N.J. Dabanloo, A.M. Nasrabadi, A. Dourado, Prediction of epileptic 
seizures based on heart rate variability, Technol. Health Care 24 (6) (Nov. 14 
2016) 795–810, https://doi.org/10.3233/THC-161225.

[15] J. Arends, R.D. Thijs, T. Gutter, C. Ungureanu, P. Cluitmans, J. Van Dijk, et al., 
Multimodal nocturnal seizure detection in a residential care setting: a long-term 
prospective trial, Neurology. 91 (21) (2018) e2010–e2019, https://doi.org/ 
10.1212/WNL.0000000000006545. Nov. 20.

[16] J.B.A.M. Arends, Movement-based seizure detection, Epilepsia 59 (S1) (Jun. 2018) 

30–35, https://doi.org/10.1111/epi.14053. Suppl. 1.

[17] J. van Andel, C. Ungureanu, J. Arends, F. Tan, J. Van Dijk, G. Petkov, et al., 

Multimodal, automated detection of nocturnal motor seizures at home: is a reliable 
seizure detector feasible? Epilepsia Open. 2 (4) (Sep. 6 2017) 424–431, https://doi. 
org/10.1002/epi4.12076.

[18] C. Dong, et al., Home-based detection of epileptic seizures using a bracelet with 

motor sensors, in: 10th International IEEE EMBS Conference on Neural 
Engineering, Virtually, May 6, 2021.

[19] T.M.E. Nijsen, R.M. Aarts, P.J.M. Cluitmans, P.A.M. Griep, Time-frequency analysis 
of accelerometry data for detection of myoclonic seizures, IEEE Trans. Inf. Technol. 
Biomed. 14 (5) (Sep. 2010) 1197–1203, https://doi.org/10.1109/ 
TITB.2010.2058123.

[20] E. Bruno, A. Biondi, M.P. Richardson, Pre-ictal heart rate changes: a systematic 

review and meta-analysis, Seizure 55 (Feb. 2018) 48–56, https://doi.org/10.1016/ 
j.seizure.2018.01.003.

[21] U. Satija, B. Ramkumar, M.S. Manikandan, A new automated signal quality-aware 
ecg beat classification method for unsupervised ECG diagnosis environments, IEEE 
Sens. J. 19 (1) (2019) 277–286, https://doi.org/10.1109/JSEN.2018.2877055.
[22] K. Vandecasteele, T. De Cooman, Y. Gu, E. Cleeren, K. Claes, W.V. Paesschen, et al., 
Automated epileptic seizure detection based on wearable ECG and PPG in a 
hospital environment, Sensors 17 (10) (Oct. 13 2017) 2338, https://doi.org/ 
10.3390/s17102338.

[23] J. Jeppesen, A. Fuglsang-Frederiksen, P. Johansen, J. Christensen, S. Wüstenhagen, 
H. Tankisi, et al., Seizure detection based on heart rate variability using a wearable 
electrocardiography device, Epilepsia 60 (10) (Oct. 2019) 2105–2113, https://doi. 
org/10.1111/epi.16343.

[24] T. De Cooman, et al., Personalizing heart rate-based seizure detection using 

supervised SVM transfer learning, Front. Neurol. 11 (2020).

[25] F.M. Touserkani, E. Tamilia, F. Coughlin, S. Hammond, R. El Atrache, M. Jackson, 
et al., Photoplethysmographic evaluation of generalized tonic-clonic seizures, 
Epilepsia 61 (8) (Aug. 2020) 1606–1616, https://doi.org/10.1111/epi.16590.

[26] R. El Atrache, E. Tamilia, F. Mohammadpour Touserkani, S. Hammond, 

C. Papadelis, K. Kapur, et al., Photoplethysmography: a measure for the function of 
the autonomic nervous system in focal impaired awareness seizures, Epilepsia 61 
(8) (Aug. 2020) 1617–1626, https://doi.org/10.1111/epi.16621.

[27] R.M. Aarts, Device for Detecting and Warning of Medical Condition, Koninklijke 

Philips NV United States Patent, 2008. US12/158,375 Patent Appl. US 2008- 
0319281 A1.

[28] L. G, R. H, M. S, S.P. Raja, Enhancing diabetic retinopathy and macular edema 

detection through multi scale feature fusion using deep learning model, Graefes. 
Arch. Clin. Exp. Ophthalmol. 263 (4) (May. 2024) 935–956, https://doi.org/ 
10.1007/s00417-024-06687-4.

[29] C. Dong, T. Ye, X. Long, R.M. Aarts, J.P. van Dijk, C. Shang, et al., A two-layer 

ensemble method for detecting epileptic seizures using a self-annotation bracelet 
with motor sensors, IEEE Trans. Instrum. Meas. 71 (2022) 1–13, https://doi.org/ 
10.1109/TIM.2022.3173270.

[30] A. Vaswani, et al., Attention is all you need, Adv. Neural Inf. Process. Syst. 30 

(2017).

[31] J. van Andel, C. Ungureanu, R. Aarts, F. Leijten, J. Arends, Using 

photoplethysmography in heart rate monitoring of patients with epilepsy, Epilepsy 
Behav. 45 (Apr. 2015) 142–145, https://doi.org/10.1016/j.yebeh.2015.02.018.

[32] K. Malloy, D. Cardenas, A. Blackburn, L. Whitmire, J.E. Cavazos, Time to response 
and patient visibility during tonic–clonic seizures in the epilepsy monitoring unit, 
Epilepsy Behav. 89 (Dec. 2018) 84–88, https://doi.org/10.1016/j. 
yebeh.2018.09.012.

10
