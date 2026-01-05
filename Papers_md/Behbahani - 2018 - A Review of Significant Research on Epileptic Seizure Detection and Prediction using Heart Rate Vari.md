# Behbahani - 2018 - A Review of Significant Research on Epileptic Seizure Detection and Prediction using Heart Rate Vari

414

Turk Kardiyol Dern Ars 2018;46(5):414-421   doi: 10.5543/tkda.2018.64928

INVITED REVIEW / DAVETLİ DERLEME

A review of significant research on epileptic seizure detection
and prediction using heart rate variability

Kalp hızı değişkenliğini kullanarak epilepsi nöbetlerinin saptanması ve öngörüsü 
üzerine önemli bir araştırmanın gözden geçirilmesi

Department of Electrical Engineering, Garmsar Branch, Islamic Azad University, Garmsar, Iran

 Soroor Behbahani, PhD.

Summary– Epilepsy is a brain disorder that many people 
struggle with all over the world. Despite extensive research, 
epilepsy  is  still  an  important  challenge  without  a  clear  so-
lution. There  may  be  confusion  about  providing  a  specific 
approach  due  to  the  variety  of  epileptic  seizures  and  the 
effectiveness  in  different  environmental  conditions.  Some 
patients  with  epilepsy  undergo  treatment  through  medica-
tion or surgery. Epileptic patients suffer from unpredictable 
conditions that may occur at any moment. Given the origins 
of these seizures, researchers have focused on predicting 
epileptic seizures via electroencephalogram (EEG). The re-
sults indicate some success in this regard. This success led 
to a focus on optimizing these methods and the evaluation 
of  epilepsy  seizure  prediction  through  other  vital  signals. 
Both  sympathetic  and  parasympathetic  inhibitory  effects 
are  undeniable  during  epileptic  seizures.  This  conflict  is 
visible in the change in heart rate. In recent years several 
investigations have focused on a behavioral study of heart 
rate  changes  before  the  seizures. The  results  have  led  to 
the development of algorithms for classifying and predicting 
epileptic  seizures  using  the  electrocardiogram  (ECG)  and 
the  more  distinct  heart  rate  variability  (HRV).  This  article 
presents  an  overview  of  seizure  detection  and  prediction 
methods and discusses their potential to improve the quality 
of life of epileptic patients.

Özet– Epilepsi tüm  dünyada birçok kişinin mücadele ettiği 
bir beyin rahatsızlığıdır. Yaygın araştırmalara rağmen, kesin 
çözümü olmayan zor bir rahatsızlık olarak epilepsi önemini 
kaybetmemiştir.  Spesifik  bir  yaklaşım  sunmadaki  kafa  ka-
rışıklığı  epilepsi  nöbetlerinin  çeşitliliğine  ve  farklı  çevresel 
koşullardaki  etkinliğine  bağlı  olabilir.  Epilepsi  hastalarının 
bir bölümü ilaç veya ameliyat ile tedavi edilir. Ancak epilepsi 
hastaları her an oluşabilen öngörülemez durumlardan rahat-
sız olabilir. Bu nöbetlerin kökenleri belli olduğuna göre araş-
tırmacılar elektroensefalogramla (EEG) epilepsi nöbetlerinin 
öngörülmesine odaklanmıştır. Sonuçlar bu açıdan bazı ba-
şarılar da göstermektedir. Aynı başarı bu yöntemlerin optimi-
zasyonuna ve hatta diğer yaşamsal belirtiler yoluyla epilepsi 
öngörüsünün değerlendirilmesine odaklanmaya yol açmıştır. 
Diğer  taraftan  epilepsi  nöbetleri  sırasında  sempatik  ve  pa-
rasempatik  inhibitör  etkiler  yadsınamaz.  Bu  uyuşmazlığın 
ortaya  çıkışı  kalp  hızındaki  değişikliktir.  Son  yıllarda  birkaç 
araştırmada nöbetler öncesinde kalp hızındaki değişiklikleri 
davranışsal  açıdan  incelenmesine  başlanmıştır.  Kabul  edi-
lebilir  sonuçlar  elektrokardiyogram  (EKG)  ve  açıkçası  kalp 
hızındaki  değişkenliği  (KHD)  kullanarak  epilepsi  nöbetlerini 
sınıflandıran ve öngören algoritmaların oluşmasıyla netice-
lenmiştir.  Bu  makale  nöbetlerin  saptanması  ve  öngörülme-
sine ilişkin yöntemleri sunmakta ve onların epilepsi hastala-
rında yaşam kalitesini iyileştirme potansiyelini tartışmaktadır.

Epilepsy is a brain disorder that leads to abnormal 

messages  sent  by  neurons:  the  regular  patterns 
of  neuronal  activity  are  impaired,  which  can  cause 
strange  sensations,  seizures,  muscular  cramps,  and 
loss of consciousness. 

The International League Against Epilepsy (ILAE) 
has developed new terms for a better description and 
classification of seizure types.[1] The purpose of such a 

revision was to denominate seizures more accurately, 
making it less confusing and more descriptive. In this 
recent report, there are 3 criteria for deciding on the 
type of epileptic seizure. The first criterion is the on-
set  of  the  seizure. The  localization  of  the  seizure  in 
the brain might represent what will occur during the 
seizure,  and  the  symptoms  likely  to  be  seen  can  be 
predicted. The second criterion is the level of aware-

Received: March 02, 2018   Accepted: May 16, 2018

Correspondence: Dr. Soroor Behbahani.  Department of Electrical Engineering, Garmsar Branch,
Islamic Azad University, Garmsar, Iran.
Tel: 982177874289   e-mail: sor.behbahani@gmail.com
© 2018 Turkish Society of Cardiology

Epileptic seizure detection and prediction

415

Abbreviations:

ness of the patient, 
which  can  indicate 
the type of the sei-
zure.  Finally,  the 
third criterion is the 
presence  of  move-
ment  during 
the 
seizure.

Autonomic nervous system 
ANS 
Approximate entropy 
ApEn 
Complex partial 
CP 
Detrended	fluctuation	analysis	
DFA	
Electrocardiogram 
ECG 
Electroencephalogram 
EEG 
False positive per hour 
FP/h 
GTCS  Generalized tonic-clonic seizures 
HF 
HR 
HRV 
ILAE 
IT 
LF 
pNN50   Number of RR intervals differing by  
>50 milliseconds from the adjacent  
interval divided by the total number  
of all RR intervals 
Photoplethysmography 
Power spectral density 

High frequency
Heart rate
Heart rate variability
International League Against Epilepsy
Intervention time
Low frequency 

In the new clas-
based 
sification 
on  the  ILAE  crite-
ria,  there  are  some 
changes in the clus-
ters of epileptic sei-
zures; for example, 
partial  seizures  are 
now  known  as  fo-
cal  seizures.  The 
terms 
dyscogni-
tive, simple partial, 
partial 
complex 
(CP)  and  second-
arily 
generalized 
(SG)  have  been 
eliminated. Atonic, 
clonic, epileptic spasms, myoclonic and tonic seizure 
can be of either focal or generalized onset. The new 
classification does not make significant changes, but 
allows for greater flexibility in naming seizure types. 
Given that these changes were just made in 2017, in 
this article, we have to identify the types of epileptic 
seizures  discussed  based  on  the  previous  classifica-
tions. 

RRI 
SDANN  Standard deviation of mean NN  
intervals in 5-minute recordings 
Standard deviation of normal to  
normal RR intervals
Secondarily generalized
Seizure occurrence period 
Support vector machines 
Very low frequency

PPG 
PSD 
RMSSD  Root mean square of successive NN  

interval differences 
RR Interval 

SG 
SOP 
SVM 
VLF 

SDNN 

In many patients, seizures can only be controlled 
with  prescribed  medications.  Patients  with  uncon-
trolled seizures usually suffer from anxiety due to the 
unstable conditions. This fact should not be ignored: 
seizure prediction has excellent potential for improv-
ing  quality  of  life  in  such  patients. The  patient  with 
knowledge of the seizure occurrence period (SOP) can 
at least avoid hazardous situations that may endanger 
life, such as being on a busy street or in a swimming 
pool. Also, an awareness of seizure onset can provide 
the possibility of prescribing a variety of  treatments 
rather  than  simply  long-term  drug  treatment,  which 
has  neurological  and  peripheral  side  effects.  Treat-
ment may be necessary only in the interval before the 
seizure.

Research on predicting epileptic seizures using an 
electroencephalogram (EEG) has been underway for 
a long time. As the origin of epilepsy is the brain, dif-
ferent systems throughout the body can be affected. A 
large part of the basic research on predicting epileptic 
seizures has been dedicated to examining the effects 
of  epilepsy  on  central  nervous  system  function.[2–5] 
The results have demonstrated that heart rate variabil-
ity (HRV) is a good indicator of autonomic nervous 
system function and arousal.[6] It can be measured as 
fluctuation of the RR interval (RRI). 

Several reports of heart rate (HR) changes before 
seizures  drew  particular  attention  to  the  potential  of 
HRV  in  epileptic  seizure  prediction.  Moreover,  the 
drawbacks of daily EEG recordings and noise effects 
on this signal confirm that an alternative or a combi-
nation  method  is  needed.  Therefore,  in  recent  years, 
along with brain-based methods, means of predicting 
seizures using HRV were also initiated. In this manu-
script, the current detection and prediction algorithms 
for epileptic seizures based on HRV are described. An 
overview  of  these  algorithms  can  efficiently  identify 
their strengths and potential in solving the problems of 
epileptic patients and help provide individualized care. 

HRV Analysis

Various approaches, which include linear and non-lin-
ear methods, have been proposed in cardiac research 
for HRV processing. Sometimes the use of 1 method 
can be enough to help us recognize the phenomenon. 
However, there are other cases where it becomes nec-
essary to examine the subject from different aspects to 
extract the actual dynamics accurately. In essence, the 
complexity of the event leads us toward choosing the 
appropriate method.

Linear HRV Analysis

Two  principal  common  linear  analyses  of  HRV  in-
clude  time  domain  analysis,  representing  circula-
tion system activity, and frequency domain analysis, 
which reports the sympathovagal balance of the auto-
nomic nervous system (ANS).

Time Domain Analysis

The first step in this analysis is the detection of QRS 
complexes,  and  particularly  the  R  wave,  which  has 
the highest amplitude. The features related to changes 
in HRV over time are as follows:

 
 
 
 
 
 
416

Turk Kardiyol Dern Ars

The total number of heartbeats; mean of RRI; SDNN 
(standard deviation of normal to normal RR intervals); 
SDANN (standard deviation of mean NN intervals in 
5  min  recordings);  pNN50  (the  number  of  adjacent 
RR  intervals  which  differ  by  more  than  50  millisec-
onds divided by the total number of RR intervals); and 
RMSSD (root mean square of successive NN interval 
differences). It is obvious that the examination of time 
characteristics cannot reflect changes in the HRV sig-
nal adequately. Therefore, frequency domain analyses 
can be helpful in identifying additional changes.

Frequency Domain Analysis 

Along  with  the  observations  used  in  time  domain 
analysis, frequency domain analysis enables a precise 
assessment of autonomic function and spectral com-
position  of  temporal  variations  in  the  autonomically 
modulated cardiac rhythm. Frequency domain analy-
sis involves power spectral density (PSD) of HRV. The 
resulting spectrum is divided into 3 routine bands: the 
very low frequency (VLF) band from 0.003–0.04 Hz, 
the low frequency (LF) band from 0.04–0.15 Hz, and 
the  high  frequency  (HF)  band  between  0.15  Hz  and 
0.4 Hz.[7,8]

Previous  studies  have  reported  that VLF  spectral 
power is associated with long-term regulatory mecha-
nisms. LF spectral power is a marker of sympathetic 
modulation  on  the  heart  and  some  parasympathetic 
influences  related  to  the  respiratory  system,  HF  is 
related to parasympathetic activity mainly caused by 
respiratory  sinus  arrhythmia,  and  the  LF/HF  ratio  is 
an indication of the balance between sympathetic and 
parasympathetic systems.[9–12]

Non-linear Methods

Non-linear  indices  include  the  power  law  exponent, 
which  describes  the  nature  of  correlations  of  single 
frequencies  in  a  time  series,[12]  and  approximate  en-
tropy (ApEn), which reflects the degree of irregular-
ity in a series of data. Smaller values indicate greater 
regularity, while higher values convey more random-
ness and system complexity.[13] Detrended fluctuation 
analysis  (DFA),  which  makes  a  distinction  between 
the internal variations generated by complex systems 
and variations caused by environmental or other ex-
ternal stimuli.[14]

Another non-linear method for HRV analysis is the 
Poincaré plot, which used the ellipse-fitting technique. 

The minor ellipse axis is identical to the standard de-
viation SD1 and represents the short-term variability 
of  HRV.[15,16]  The  major  axis,  the  standard  deviation 
SD2, represents long-term variability. The SD1/SD2 
ratio represents heart activity.

Effects of Epilepsy On HRV

HRV  alteration  in  the  pre-ictal  period  has  been  re-
ported  before.  Depending  on  the  type  of  epilepsy, 
these  changes  may  include  tachycardia,  and  altera-
tion of lateralization and the location of the seizures. 
Novak et al.[17] investigated HRV before, during, and 
after  partial  seizures  using  time-frequency  mapping 
in  patients  with  temporal  lobe  epilepsy. They  found 
autonomic  imbalance  and  tachycardia  in  the  pre-ic-
tal  phase  of  CP  seizures.  Spectral  power  at  respira-
tory frequencies fell rapidly in the period 30 seconds 
before  the  seizure.  In  other  words,  parasympathetic 
withdrawal occurred approximately 30 seconds before 
the seizure and sympathetic activity peaks at seizure 
onset.  Delamont  et  al.[18]  investigated  a  continuous 
index of cardiac parasympathetic activity in patients 
with  CP  and  complex  partial  with  SG  seizures. The 
mean  cardiac  parasympathetic  activity  was  elevated 
in the pre-ictal phase, while CP seizures did not show 
any significant change. It seems that pre-ictal eleva-
tion of cardiac parasympathetic activity could be used 
as a marker for SG seizures. Di Gennaro et al.[19] re-
ported that the HR of patients with mesial and lateral 
temporal  lobe  epilepsy  increased  before  seizure  on-
set. Jeppesen et al.[20] used HRV spectrum analysis in 
patients  with  focal  epilepsy  and  demonstrated  sup-
pressed parasympathetic activity and vagal tone drop 
prior to and during epileptic seizures. Nilsen et al.[21] 
reported an elevated HR before partial seizure onset 
in SG seizures. Behbahani et al.[22] found significant 
changes  in  the  time-frequency  and  Poincaré  param-
eters of HRV in 5 minutes before the seizure. 

Behbahani et al.[23] analyzed HRV during 5-minute 
segments  in  age-matched  populations.  The  patients 
included  males  (n=12)  and  females  (n=12),  ranging 
from 41 to 65 years of age. HF and LF components 
of  HRV  and  Poincaré  parameters  of  HR  time  were 
considered. The mean HR markedly differed between 
gender  groups  in  both  right-  and  left-sided  seizures. 
The  HF  and  the  LF/HF  ratio  increased  in  the  pre-
ictal  phase  of  both  the  male  and  female  groups,  but 
the  men  demonstrated  a  greater  increase,  especially 

Epileptic seizure detection and prediction

417

in right-sided seizures. The SD2/SD1 ratio of the pre-
ictal phase was greater in males than in females. HF, 
which  is  an  indication  of  parasympathetic  activity, 
was  greater  in  females  with  both  right  and  left-sid-
ed seizures, while men showed a sudden increase in 
sympathetic activity in the pre-ictal phase. 

Detection of Epileptic Seizures Based On HRV

As  previously  stated,  epileptic  seizures  are  often  ac-
companied by changes in various autonomic functions, 
and particularly HR. In past decades, many researchers 
have  used  ECG  and  HRV  signals  to  detect  epileptic 
seizures. Although success in detecting seizures does 
not  guarantee  that  they  can  be  predicted,  it  confirms 
that  there  are  some  features  that  can  distinguish  sei-
zures. Regardless of the elements used in these algo-
rithms to detect seizures, they apparently have 2 main 
stages: feature extraction and classification (Fig. 1).

Jeppesen et al.[20] considered 6 seizures experienced 
by 6 patients with temporal lobe epilepsy (4 females 
and  2  males). Three  intervals  were  chosen  for  HRV 
analysis: 25 to 30 minutes pre-seizure, 30 seconds to 5 
minutes post seizure onset, and 30 minute non-seizure 
sessions. Frequency domain analysis includes LF, HF, 
LF/HF,  LF/(LF+HF)  and  reciprocal  HF-power  mea-
surements. The results show that reciprocal HF-power 
peaks between 10 seconds pre-seizure and 24 seconds 
post-seizure. A  significant  difference  between  a  sei-
zure and non-seizure session were not seen in the oth-
er features of the analysis. High reciprocal HF-power 
peaks  suggest  suppressed  parasympathetic  activity 
just around seizure-onset time. 

Evrengül et al.[24] analyzed both the frequency and 
time domain parameters of HRV in 43 patients with 
generalized tonic-clonic seizures (GTCS) and a sex-
matched  control  group  using  no  medications.  In  the 
time domain analysis, the SDNN, SDANN, and HRV 
triangular  index,  pNN50,  and  RMSSD  were  con-
sidered.  The  patients  demonstrated  higher  values  in 
the time domain features compared  with  the control 
group. In the frequency domain analysis, the spectral 
measures  of  HRV  showed  a  reduction  in  HF  values 

and an increase in low LF values. Moreover, a signifi-
cant increase was observed in the LF/HF. The results 
confirmed  an  increase  in  the  sympathetic  control  of 
HR in epilepsy patients with GTCS, which could lead 
to tachyarrhythmia in epileptic patients.

Ponnusamy  et  al.[25]  reported  their  results  of  a 
study  of  26  patients  with  medically  refractory  tem-
poral lobe epilepsy and 24 sex-matched patients with 
psychogenic  non-epileptic  seizures.  Time  and  fre-
quency domain parameters, including LF, HF, SDNN, 
and RMSSD were extracted. Moreover, the cardiova-
gal index, cardio-sympathetic index, and ApEn were 
calculated. The results showed a significant difference 
between  ictal  HRV  measures  during  epileptic  and 
non-epileptic seizures. The cardio-sympathetic index 
was higher in epileptic seizures. The RR interval, LF, 
HF, and RMSSD were significantly lower during epi-
leptic  seizures.  Furthermore,  a  significant  difference 
was recorded in the mean value of ApEn and LF in the 
ictal phase versus the interictal phase. This research 
confirms other results, which show greater ANS acti-
vation in epileptic seizures. 

Malarvili  et  al.[26]  assessed  the  HRV  of  6  seizure 
and 4 non-seizure events of 64 seconds in 5 newborns 
as a tool for seizure detection. The characteristics ex-
amined were LF, mid-frequency band (0.07–0.15 Hz), 
and HF. Based on the results, a conditional moment 
of  HRV,  the  mean/central  frequency  in  the  LF,  and 
the variance in the HF can be used to discriminate the 
neonatal seizure.

Malarvili et al.[27] also investigated the use of HRV 
for  automatic  newborn  seizure  detection.  A  set  of 
time-frequency  features  from  the  neonatal  HRV  of 
8  newborns  was  extracted.  The  algorithm  achieved 
85.7% sensitivity and 84.6% specificity. 

Leutmezer et al.[28] assessed ECG changes during 
145 seizures recorded with a scalp EEG in 58 patients 
who underwent video-EEG monitoring. Consecutive 
RRIs  were  analyzed  with  a  newly  developed  math-
ematical method for a total of 90 seconds.

Behbahani et al.[29] analyzed the effects of epilepsy 
on the autonomic control of the heart in the ictal phase 

Electrocardiogram
Recordings

HRV
Extraction

Linear & Non-linear
Analysis

Classification

Detection

Figure 1. Epileptic seizure detection algorithm based on heart rate variability (HRV).

418

Turk Kardiyol Dern Ars

of 2 types of epileptic seizures with SG and CP. A to-
tal  of  96  SG  and  110  complex  partial  seizures  were 
included. A  5-minute  period  of  HRV  was  randomly 
selected  to  represent  both  seizure-free  and  seizure 
activity in both groups. Time and frequency domain 
analysis and nonlinear parameters extracted from the 
HRV  data  showed  an  increase  in  sympathetic  activ-
ity in the ictal phase of both SG and CP seizures that 
significantly differed from seizure-free segments. The 
mean HR, LF/HF, and the SD2/SD1 ratio of SG had a 
higher value compared with CP. This research demon-
strated that there are significant differences between 
the  autonomic  behaviors  of  CP  and  SG  subjects.  In 
addition, SG seizures show more sympathetic activity 
in comparison with CP seizures. 

Behbahani et al.[30] proposed an algorithm to detect 
epileptic seizures based on HRV. They used time and 
frequency domain analysis, as well as nonlinear fea-
tures, such as the input of an artificial neural network. 
A multilayer perceptron neural network was used as a 
classifier. The results demonstrated a sensitivity, spec-
ificity, and accuracy of 88.66%, 90%, and 88.33%, re-
spectively, in SG seizures, and 83.33%, 86.11%, and 
84.72%, respectively, in CP events.

In addition, Behbahani et al.[31] assessed HRV with 
a 5-minute duration in 170 seizures that occurred in 16 
patients,  comprising  86  left-sided  and  84  right-sided 
focus seizures. Time and frequency domain indices and 
Poincaré parameters of HRV were computed. Support 
vector machines (SVMs) were used to classify epilep-
tic  and  non-epileptic  signals.  The  accuracy  rates  for 
right-sided and left-sided focus seizures were 86.74% 
and 79.41%, respectively. This research indicated that 
patients with right-sided focus epilepsy demonstrated 
a greater reduction in parasympathetic activity and a 
greater increase in sympathetic activity. Moreover, the 
results suggested that the lateralization of seizure onset 
might have different influences on HR changes. 

Shamim et al.[32] proposed a new technique to de-
tect seizures in epileptic patients using the ECG sig-
nal. Multiple domain parameters were used: mobility, 
complexity,  mean  of  absolute  deviation  of  fast  Fou-
rier  transform  coefficients,  and  spectral  entropy. An 
SVM classifier was used based on a linear threshold 
for  classification.  The  classification  result  revealed 
94.2% accuracy, 84.1% sensitivity, and 94.5% speci-
ficity; the proposed algorithm detected epileptic sei-
zures efficiently. 

Malarvili et al.[26] presented their results based on 
of  time  frequency  analysis  to  compare  the  perfor-
mance of various time frequency distributions applied 
to HRV to detect non-seizure and seizure activity in 
newborns. The time frequency distributions included 
the Wigner-Ville spectrogram, the Choi-Williams dis-
tribution  function,  and  the  Modified  B  distribution. 
The  results  showed  that  the  Modified  B  distribution 
outperformed  other  distributions  regarding  time  fre-
quency resolution, cross-term suppression and in the 
ability to represent the neonatal HRV signals of non-
seizure and seizure, which are closely spaced compo-
nents in the time frequency domain.

Moridani et al.[33] studied the HRV of 11 patients. 
Time and frequency domain parameters of RRI, mean 
HR,  HF,  LF,  and  LF/HF  were  considered.  Poincaré 
plot  features  were  examined.  HRV  signals  were  di-
vided into segments with a 5-minute duration. In each 
segment,  linear  and  nonlinear  features  were  extract-
ed. During the ictal phase, the mean HR, LF/HF, and 
SD2/SD1 ratio were significantly increased while the 
RR  intervals  were  significantly  decreased.  The  pro-
posed algorithm detected seizures with 88.3% sensi-
tivity and 86.2% specificity.

Prediction of Epileptic Seizures Based On HRV

Although the use of HRV to detect epileptic seizures 
has  emerged  among  EEG-based  methods,  the  algo-
rithms that use HRV to predict are limited. Hirotsugu 
et al.[34] proposed an HRV-based epileptic seizure pre-
diction algorithm utilizing multivariate statistical pro-
cess control technology. Various HRV features were 
derived from the RRI interictal and pre-ictal period. 
The result of applying the proposed method to clini-
cal data demonstrated that seizures could be detected 
at least 1 minute before the seizure occurred, which 
emphasized the possibility of realizing an HRV-based 
seizure prediction method.

Behbahani  et  al.[35]  analyzed  the  HRV  of  16  epi-
leptic patients and 170 seizures to predict the occur-
rence  of  seizures  based  on  the  dynamic  changes  of 
HRV during the pre-ictal period. Time and frequency 
domain features were computed for consecutive time 
windows with a length of 5 minutes. An adaptive de-
cision threshold method was used to raise alarms. Pre-
dictions were made when selected features exceeded 
the  decision  thresholds.  For  the  seizure  occurrence 
period  (SOP)  of  4:30  minutes  and  intervention  time 

Epileptic seizure detection and prediction

419

(IT) of 110 seconds, the presented algorithm achieved 
a sensitivity of 78.59% with a false positive per hour 
(FP/h)  rate  of  0.21,  which  indicated  that  the  system 
was superior to the random predictor.

Pavei  et  al.[36]  presented  a  new  methodology  for 
the  prediction  of  epileptic  seizures  using  HRV  sig-
nals. Eigendecomposition of HRV parameter covari-
ance matrices was used to create an input for the SVM 
classifier. A total of 34 seizures from 12 patients, in-
volving 55.2 hours of inter-ictal ECG recordings were 
analyzed.  Moreover,  123.6  hours  of  ECG  data  from 
healthy subjects were used to test the FP/h. The pro-
posed approach detected seizures from 5 minutes be-
fore to just before onset with a sensitivity of 94.1%. 
The FP/h was 0.49 in patients with epilepsy and 0.19 
in healthy subjects. 

Vandecasteele et al.[37] compared the performance 
of  2  wearable  devices  based  on  ECG  and  photople-
thysmography (PPG) to predict epileptic seizure. This 
algorithm classified seizures by HR features using the 
HR increase. The algorithm was applied to 11 patients 
suffering from temporal lobe seizures. The sensitivity 
of  the  wearable  ECG  device  and  the  wearable  PPG 
device was 70% and 32%, respectively, with a corre-
sponding FP/h of 2.11 and 1.80. The seizure detection 
performance using the PPG device was considerably 
lower than that of the wearable ECG device.

Conclusion

Experiencing  an  epileptic  seizure  is  frightening  for 
the patient and their relatives. Finding a way to pre-
dict and prognosticate these events for the patient has 
repeatedly been raised in epilepsy-related research. It 
should  be  noted  that  the  prediction  of  epileptic  sei-
zures should not terminate to the loss of privacy and 
lack of comfort at night. In addition to the effective-
ness  of  the  prediction  algorithm,  psychological  as-
pects must also be considered.

Psychological considerations can be viewed from 
a variety of perspectives. Patients with such diseases 
are often overwhelmed by these conditions that they 
may be unable to control at any moment. Insensitiv-
ity  can  contribute  to  undermining  the  confidence  of 
patients, which can lead to the patients withdrawing 
from  the  community.  Assuming  that  the  algorithms 
provided to predict epileptic seizures based on EEG 
were  working  successfully,  individuals  who  have 
been  confronted  with  their  particular  circumstances 

have been told to wear a predesigned cap with record-
ing  electrodes  for  online  EEG  monitoring.  Clearly, 
such  a  method  jeopardizes  the  privacy  of  epileptic 
individuals and people may ridicule them. Too many 
false alarms are another reason for patient reluctance 
to use such methods, as they lose their confidence. 

Addressing  these  issues  and  their  complexities 
will require the continuation of research to find an al-
gorithm that can provide a sufficient compromise of 
performance, reliability, and privacy. It seems that the 
prediction of epileptic seizures using HRV can signifi-
cantly resolve the problems of permanent recording, 
noise, and privacy. Anyone can use Holter monitoring 
and wearable sensors to measure long-term RRI with-
out special skills and with a cost of less than $100.[40] 
However, we should not forget that the brain is the ori-
gin of epileptic seizures. The heart is the second organ 
affected by seizures, and it cannot be expected that the 
predictive results with this method of the brain.

When  comparing  the  prediction  of  epileptic  sei-
zures using EEG and ECG signals, it is important to 
note that brain-based research started years ago and is 
now in the optimization phase. In other words, these 
investigations do not seek to establish the possibility of 
prediction based on EEG. Instead, they are exploring 
ways to optimize the main parameters for predicting 
epileptic seizures, including SOP, IT, sensitivity, and 
FP/h. What is considered a benchmark of for success 
in these studies is the ability of algorithms to increase 
the SOP, IT, and sensitivity, as well as decreasing the 
FP/h.  One  of  the  challenges  facing  the  HRV-based 
algorithms  is  to  distinguish  between  conditions  that 
lead to changes in HR. The features that are used to 
distinguish between modes, such as excitement, exer-
cising, walking, etc. can be very useful in increasing 
the accuracy and success of these algorithms.

HRV-based  research  on  epileptic  seizure  predic-
tion  is  not  synchronous  with  EEG-based  studies. 
Much of the research has been done to support the hy-
pothesis that epileptic seizures can be predicted using 
the HRV. Therefore, the results obtained in this field 
are  still  not  comparable  with  EEG-based  algorithms 
and still have great potential for optimization. Indeed, 
further studies are needed to increase the sensitivity 
of prediction as well as other mentioned parameters 
to acquire patient trust. The review of all these studies 
shows that the most critical point is to provide a suc-
cessful algorithm that can restore patient comfort. The 

420

Turk Kardiyol Dern Ars

collaboration of engineers, doctors, and practitioners 
is useful in providing a proper strategy for detection, 
classification, and prediction of epileptic seizures. In 
the course of the prediction of seizures, we can find 
more  suitable  methods  for  controlling,  and  possibly 
treating patients.

This  article  was  a  presentation  of  the  significant 
and  most  recent  research  concerned  with  the  detec-
tion  and  prediction  of  epileptic  seizures  using  HRV 
signals. The primary goal of this review was to assist 
researchers  in  the  field  of  ECG  signal  processing  to 
understand the available methods and encourage their 
use as well as EEG-based algorithms in order to find a 
better approach to prediction.
Conflict-of-interest: None declared.

References

1.  Beniczky  S,  Rubboli  G,  Aurlien  H,  Hirsch  LJ,  Trinka  E, 
Schomer DL; Score consortium. The new ILAE seizure clas-
sification: 63 seizure types? Epilepsia 2017;58:1298–300. 
2.  Wannamaker  BB. Autonomic  nervous  system  and  epilepsy. 

Epilepsia 1985;26:S31–9. [CrossRef]

3.  Kanner AM. Epilepsy and Activity of the Autonomic Nervous 

System. Epilepsy Curr 2002;2:159–60. [CrossRef]

4.  Berilgen MS, Sari T, Bulut S, Mungen B. Effects of epilepsy 
on autonomic nervous system and respiratory function tests. 
Epilepsy Behav 2004;5:513–6. [CrossRef]

5.  Müngen  B,  Berilgen  MS,  Arikanoğlu  A.  Autonomic  ner-
vous  system  functions  in  interictal  and  postictal  periods  of 
nonepileptic  psychogenic  seizures  and  its  comparison  with 
epileptic seizures. Seizure 2010;19:269–73. [CrossRef]

6.  van der Kruijs SJ, Vonck KE, Langereis GR, Feijs LM, Bodde 
NM, Lazeron RH, et al. Autonomic nervous system function-
ing associated with psychogenic nonepileptic seizures: Anal-
ysis of heart rate variability. Epilepsy Behav 2016;54:14–9.
7.  Malliani A, Pagani M, Lombardi F, Cerutti S. Cardiovascular 
neural regulation explored in the frequency domain. Circula-
tion 1991;84:482–92. [CrossRef]

8.  Heart rate variability: standards of measurement, physiologi-
cal interpretation and clinical use. Task Force of the European 
Society  of  Cardiology  and  the  North  American  Society  of 
Pacing and Electrophysiology. Circulation 1996;93:1043–65.
9.  Saul JP, Rea RF, Eckberg DL, Berger RD, Cohen RJ. Heart rate 
and muscle sympathetic nerve variability during reflex changes 
of autonomic activity. Am J Physiol 1990;258:H713–21.
10. Shiomi T, Guilleminault C, Sasanabe R, Hirota I, Maekawa 
M, Kobayashi T. Augmented very low frequency component 
of heart rate variability during obstructive sleep apnea. Sleep 
1996;19:370–7. [CrossRef]

Biomed Eng 2006;53:485–96. [CrossRef]

12. Gisiger T.  Scale  invariance  in  biology:  coincidence  or  foot-
print of a universal mechanism? Biol Rev Camb Philos Soc 
2001;76:161–209. [CrossRef]

13. Pincus  SM.  Approximate  entropy  as  a  measure  of  system 
complexity. Proc Natl Acad Sci U S A 1991;88:2297–301.
14. Peng CK, Havlin S, Stanley HE, Goldberger AL. Quantifica-
tion of scaling exponents and crossover phenomena in nonsta-
tionary heartbeat time series. Chaos 1995;5:82–7. [CrossRef]
15. Brennan M, Palaniswami M, Kamen P. Do existing measures 
of Poincaré plot geometry reflect nonlinear features of heart 
rate variability? IEEE Trans Biomed Eng 2001;48:1342–7.
16. Karmakar CK, Gubbi J, Khandoker AH, Palaniswami M. An-
alyzing temporal variability of standard descriptors of Poin-
caré plots. J Electrocardiol 2010;43:719–24. [CrossRef]

17. Novak VV, Reeves LA, Novak P, Low AP, Sharbrough WF. 
Time-frequency  mapping  of  R-R  interval  during  complex 
partial  seizures  of  temporal  lobe  origin.  J Auton  Nerv  Syst 
1999;77:195–202. [CrossRef]

18. Delamont  RS,  Julu  PO,  Jamal  GA.  Changes  in  a  measure 
of  cardiac  vagal  activity  before  and  after  epileptic  seizures. 
Epilepsy Research 1999;35:87–94. [CrossRef]

19. Di  Gennaro  G,  Quarato  PP,  Sebastiano  F,  Esposito V,  Ono-
rati  P,  Grammaldo  LG,  et  al.  Ictal  heart  rate  increase  pre-
cedes EEG discharge in drug-resistant mesial temporal lobe 
seizures. Clin Neurophysiol 2004;115:1169–77. [CrossRef]
20. Jeppesen  J,  Beniczky  S,  Fuglsang-Frederiksen  A,  Sidenius 
P,  Jasemian  Y.  Detection  of  epileptic-seizures  by  means  of 
power spectrum analysis of heart rate variability: a pilot study. 
Technol Health Care 2010;18:417–26.

21. Nilsen  KB,  Haram  M, Tangedal  S,  Sand T,  Brodtkorb  E.  Is 
elevated pre-ictal heart rate associated with secondary gener-
alization in partial epilepsy? Seizure 2010;19:291–5. [CrossRef]
22. Behbahani  S,  Dabanloo  NJ,  Nasrabadi  AM,  Teixeira  CA, 
Dourado  A.  Pre-ictal  heart  rate  variability  assessment  of 
epileptic seizures by means of linear and non-linear analyses. 
Anadolu Kardiyol Derg 2013;13:797–803. [CrossRef]

23. Behbahani  S,  Jafarnia  Dabanloo  N,  Motie  Nasrabadi  A, 
Dourado A. Gender-Related Differences in Heart Rate Vari-
ability of Epileptic Patients. Am J Mens Health 2018;12:117–
25. [CrossRef]

24. Evrengül  H,  Tanriverdi  H,  Dursunoglu  D,  Kaftan  A,  Kuru 
O,  Unlu  U,  et  al.  Time  and  frequency  domain  analyses  of 
heart rate variability in patients with epilepsy. Epilepsy Res 
2005;63:131–9. [CrossRef]

25. Ponnusamy A,  Marques  JL,  Reuber  M.  Comparison  of  heart 
rate variability parameters during complex partial seizures and 
psychogenic nonepileptic seizures. Epilepsia 2012;53:1314–21.
26. Malarvili MB, Mesbah M, Boashash B. Time-frequency anal-
ysis  of  heart  rate  variability  for  neonatal  seizure  detection. 
Australas Phys Eng Sci Med 2006;29:67–72.

11.  Redmond  SJ,  Heneghan  C.  Cardiorespiratory-based  sleep 
staging in subjects with obstructive sleep apnea. IEEE Trans 

27. Malarvili  MB,  Mesbah  M.  Newborn  seizure  detection 
based  on  heart  rate  variability.  IEEE  Trans  Biomed  Eng 

Epileptic seizure detection and prediction

421

2009;56:2594–603. [CrossRef]

28. Leutmezer  F,  Schernthaner  C,  Lurger  S,  Pötzelberger  K, 
Baumgartner C. Electrocardiographic changes at the onset of 
epileptic seizures. Epilepsia 2003;44:348–54. [CrossRef]

29. Behbahani  S,  Dabanloo  NJ,  Nasrabadi  AM.  Ictal  heart  rate 
variability assessment with focus on secondary generalized and 
complex partial epileptic seizures. Adv Biores 2012;4:50–8.
30. Behbahani S, Jafarnia Dabanloo N, Motie Nasrabadi A, Teix-
eira CA, Dourado A. A new algorithm for detection of epilep-
tic seizures based on HRV signal. Journal of Experimental & 
Theoretical Artificial Intelligence 2014;26:251–65. [CrossRef]

31. Behbahani S, Dabanloo NJ, Nasrabadi AM, Dourado A. Clas-
sification of ictal and seizure-free HRV signals with focus on 
lateralization of epilepsy. Technol Health Care 2016;24:43–56.
32. Shamim G, Khan YU, Sarfraz M, Farooq O. Epileptic seizure 
detection using heart rate variability. 2016 International Con-
ference  on  Signal  Processing  and  Communication  (ICSC); 
2016 Dec 26-28; Noida, India: IEEE; 2017. [CrossRef]

34. Fujiwara  K,  Miyajima  M,  Yamakawa  T,  Abe  E,  Suzuki  Y, 
Sawada Y,  et  al.  Epileptic  Seizure  Prediction  Based  on  Mul-
tivariate  Statistical  Process  Control  of  Heart  Rate  Variability 
Features. IEEE Trans Biomed Eng 2016;63:1321–32. [CrossRef]
35. Behbahani S, Dabanloo NJ, Nasrabadi AM, Dourado A. Pre-
diction  of  epileptic  seizures  based  on  heart  rate  variability. 
Technol Health Care 2016;24:795–810. [CrossRef]

36. Pavei J, Heinzen RG, Novakova B, Walz R, Serra AJ, Reu-
ber M, et al. Early Seizure Detection Based on Cardiac Auto-
nomic Regulation Dynamics. Front Physiol 2017;8:765.
37. Vandecasteele K, De Cooman T, Gu Y, Cleeren E, Claes K, 
Paesschen WV, et al. Automated Epileptic Seizure Detection 
Based on Wearable ECG and PPG in a Hospital Environment. 
Sensors (Basel) 2017;17.pii:E2338. [CrossRef]

Keywords:  Detection;  electrocardiogram;  epilepsy;  heart  rate  vari-
ability; prediction.

33. Moridani MK, Farhadi H. Heart rate variability as a biomarker 
for epilepsy seizure prediction. Bratisl Lek Listy 2017;118:3–8.

Anahtar  sözcükler:  Elektrokardiyogram;  epilepsi;  kalp  hızı  değiş-
kenliği; tespit; öngörü.
