# Miron et al. - 2025 - Autonomic biosignals, seizure detection, and forecasting

Received: 4 March 2024 

DOI: 10.1111/epi.18034  

|  Revised: 17 May 2024 

|  Accepted: 22 May 2024

S P E C I A L   I S S U E   A R T I C L E

Autonomic biosignals, seizure detection, and forecasting

Gadi Miron1,2
Tobias Loddenkemper5  |   Christian Meisel1,2,6,7

  |   Mustafa Halimeh1,2  |   Jesper Jeppesen3,4

  |   

1Computational Neurology, 
Department of Neurology, Charité–
Universitätsmedizin Berlin, Berlin, 
Germany
2Berlin Institute of Health, Berlin, 
Germany
3Department of Clinical 
Neurophysiology, Aarhus University 
Hospital, Aarhus, Denmark
4Department of Clinical Medicine, 
Aarhus University, Aarhus, Denmark
5Department of Neurology, Boston 
Children's Hospital, Boston, 
Massachusetts, USA
6Bernstein Center for Computational 
Neuroscience, Berlin, Germany
7Center for Stroke Research Berlin, 
Berlin, Germany

Correspondence
Gadi Miron, Computational 
Neurology, Department of Neurology, 
Charité–Universitätsmedizin Berlin, 
Charitéplatz 1, 10117 Berlin, Germany.
Email: gadi.miron@charite.de

Abstract
Wearable devices have attracted significant attention in epilepsy research in re-

cent years for their potential to enhance patient care through improved seizure 

monitoring and forecasting. This narrative review presents a detailed overview of 

the current clinical state of the art while addressing how devices that assess auto-

nomic nervous system (ANS) function reflect seizures and central nervous system 

(CNS) state changes. This includes a description of the interactions between the 

CNS and the ANS, including physiological and epilepsy- related changes affect-

ing  their  dynamics.  We  first  discuss  technical  aspects  of  measuring  autonomic 

biosignals and considerations for using ANS sensors in clinical practice. We then 

review recent seizure detection and seizure forecasting studies, highlighting their 

performance  and  capability  for  seizure  detection  and  forecasting  using  devices 

measuring ANS biomarkers. Finally, we address the field's challenges and pro-

vide an outlook for future developments.

K E Y W O R D S

autonomic nervous system, epilepsy, seizure detection, seizure forecasting, wearables

|  INTERACTIO NS OF  T HE 
1 
CENTRAL AND  AUTON OMOU S 
NERVOU S SY ST EM S  IN  E PIL E PS Y

Epilepsy is a central nervous system (CNS) disorder charac-
terized by an enduring predisposition to generate epileptic 
seizures. A close relationship between the CNS and the au-
tonomic nervous system (ANS) has long been established in 
persons with epilepsy (PwE) through the semiological study 
of autonomic manifestations of seizures, such as epigastric 
sensations,  palpitations,  syncope,  pupillary  dilatation,  and 
facial flushing.1 Moreover, autonomic symptoms in epilepsy 

not only are clinical markers for seizure localization but also 
present significant risks. For example, autonomic dysfunc-
tions  can  lead  to  life- threatening  cardiac  arrhythmias  and 
are potentially associated with sudden unexpected death in 
epilepsy  (SUDEP),  contributing  to  the  increased  mortality 
observed in PwE.2 The central autonomic network (CAN), 
first  described  by  Claude  Bernard  >150 years  ago,  plays  a 
pivotal  role  in  this  interaction.3  The  CAN  is  highly  inter-
connected  and  encompasses  brain  regions  often  recruited 
by  the  epileptic  network,  such  as  the  insular  cortex,  ante-
rior  cingulate  cortex,  posterior  orbitofrontal  cortex,  and 
amygdala. These regions are connected to other cortical and 

This is an open access article under the terms of the Creative Commons Attribution-NonCommercial License, which permits use, distribution and reproduction in any 
medium, provided the original work is properly cited and is not used for commercial purposes.
© 2024 The Author(s). Epilepsia published by Wiley Periodicals LLC on behalf of International League Against Epilepsy.

Epilepsia. 2025;66(Suppl. 3):25–38. 

wileyonlinelibrary.com/journal/epi

|  25

  
  
26 

| 

subcortical areas within the hypothalamus, periaqueductal 
gray, parabrachial nucleus, nucleus of the solitary tract, ven-
trolateral reticular formation of the medulla, and medullary 
raphe. Thus, autonomic symptoms during preictal, ictal, or 
postictal phases are thought to result from either direct ac-
tivation of CAN brain areas or systemic effects mediated by 
autonomic activation, such as the release of catecholamines 
affecting the sympathetic response. Chronic effects due to 
long- term autonomic dysregulation may be a contributing 
factor to ANS- related disease, most notably increased rates 
of cardiac comorbidity in PwE,4,5 which in turn contribute 
to  increased  mortality  in  epilepsy.6  Importantly,  the  close 
interaction  between  CNS  and  ANS  suggests  means  to  de-
tect, characterize, and control epileptic seizures via the au-
tonomic subsystems.

|  IDENTIFY IN G  RE LEVA NT 

2 
AU TONOMIC B IOSIG NALS 
AND SENSOR S FOR  E PILE PSY 
MONITORIN G

The  ideal  autonomic  biosignals  should  accurately  rep-
resent  the  CNS  dynamic  state  and  afford  long- term  re-
cording  using  nonstigmatizing  and  noninvasive  sensors 
readily accepted by PwE. Within this framework, several 
subsystems  of  the  ANS  emerge  as  promising  candidates 
for  epilepsy  monitoring,  notably  the  cardiovascular  and 
thermoregulatory  systems  (Figure  1).  Across  these  auto-
nomic subsystems, different biosignals have been shown 
to directly reflect changes in CNS in healthy people and 
PwE.

In  the  cardiac  subsystem,  variables  related  to  heart 
rate  (HR)  represent  a  classical  measure  of  autonomic 
function, mediating the heart–brain connection. These in-
clude HR and HR variability (HRV), which is a measure 
of the variation between heartbeats, measured in both the 
time  and  frequency  domains,  including  power  in  differ-
ent frequency bands, as well as nonlinear measures such 
as  Poincaré  plots,  approximate  entropy,  and  detrended 
fluctuation  analysis,  which  quantify  the  nonstationarity 
and complexity of R- R interval series.7 Additional cardiac 
markers  are  based  on  the  electrocardiogram  (ECG)  and 
examine the morphology of QRS complexes, cardiac con-
duction abnormalities such as in QTc and PR intervals, or 
the interaction between respiration and HR.8 Functional 
neuroimaging studies have established the direct CNS link 
to  these  HR  features  in  healthy  individuals,  with  large- 
scale  meta- analyses  associating  HR  and  HRV  to  activity 
in the anterior cingulate, amygdala, insula, and prefron-
tal cortex, which are primary constituents of the CAN.9,10 
(EEG)  stimula-
Intracranial  electroencephalographic 
tion  and  surgical  studies  have  further  demonstrated  the 

Key points

•  ANS  patterns  of  ictal  and  peri- ictal  states  are 
modulated  by  distinct  influencing  factors  in-
cluding age, medications, and stress.

•  Multimodal  wearables  monitoring  ANS  func-
tion  have  demonstrated  capability  for  tonic–
clonic  (phase  4)  and  focal  (phase  2)  seizure 
detection.

•  Seizure  forecasting  uses  ANS  patterns  and 
rhythms  to  provide  multiday  risk  assessment 
and short- term predictions.

•  AI explainability methods can help identify the 
factors  influencing  performance  of  detection 
and forecasting models.

•  Considering  influencing  factors  is  crucial  for 
improving approaches and identifying optimal 
target populations.

influence  of  the  CNS  on  cardiac  function  in  PwE.  The 
insula,  for  example,  has  been  found  to  consistently  me-
diate  HR  responses  upon  stimulation,  with  increased 
HR often triggered by more posterior stimulation. Other 
CAN- related brain regions, including the cingulate gyrus, 
temporal–mesial structures, and orbitofrontal cortex, have 
also  shown  significant  mediating  effects  on  HRV,  often 
in  parallel  to  evoking  additional  emotional  or  visceral 
sensations.11,12

In  examining  the  thermoregulatory  system,  electro-
dermal  activity  (EDA),  which  reflects  the  modulation  of 
sweat  gland  activity  by  measuring  skin  conductance,  is 
often  investigated.  Unlike  HR  measures  that  are  influ-
enced by parasympathetic and sympathetic activity, EDA 
is predominantly modulated by the sympathetic nervous 
system. EDA's relationship to the CAN is evidenced from 
direct  electrical  stimulation  or  lesion  studies  of  several 
cortical  areas,  including  the  orbitofrontal,  ventromedial 
frontal,  and  anterior  cingulate  cortices.13  Indirect  tran-
scranial  magnetic  stimulation  of  the  CNS  has  also  been 
shown  to  affect  EDA,  for  example,  decreased  EDA  as-
sociated  with  stimulation  of  the  dorsolateral  prefrontal 
cortex.14 These areas exert both excitatory and inhibitory 
influences on EDA, highlighting the role of higher cortical 
areas in EDA regulation.

|   ANS CH ANGES IN RELATION 

3 
TO  SEIZUR ES

The  field  of  seizure  detection  and  forecasting  builds  on 
observations of ANS changes associated with seizures in 

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 
 
|  27

F I G U R E   1   The central autonomic 
network (CAN), autonomic nervous 
system (ANS), and wearable technology 
used for seizure detection and forecasting. 
The CAN is composed of cortical and 
subcortical brain regions that are affected 
by physiological and epilepsy- related 
factors. These dynamics influence 
the activity of the ANS. Wearable 
biosensors are particularly useful in 
measuring biosignals reflecting changes 
in the cardiac and thermoregulatory 
subsystems of the ANS, providing 
clinically useful information for seizure 
detection and forecasting. Noninvasive, 
nonstigmatizing, and easy- to- use solutions 
have been developed, and can be worn on 
the chest, arm, and wrist. Brain structures 
visualized using BrainPainter.106

PwE, which can occur in the preictal, postictal, and ictal 
states. In the cardiac subsystem, ictal HR increase is the 
most  common  phenomenon,  occurring  in  >80%  of  pa-
tients.15  The  increase  in  HR  may  happen  in  the  preictal 
period or within the first 30 s of the seizure. Of note, al-
though  preictal  HR  changes  occur  before  clinical  symp-
toms  or  scalp  EEG  changes,  they  may  reflect  cardiac 
effects  of  ictal  activity  in  deep- seated  brain  regions,  as 
studies of simultaneous scalp and intracranial EEG have 
demonstrated.16 Although it appears in both generalized 
and focal epilepsies, in focal epilepsy, it is most prevalent 
in temporal lobe epilepsy (TLE).17,18 Bradycardia or asys-
tole are rare events, reported only in focal onset seizures, 
and  in  the  vast  majority  of  cases  occur  in  patients  with 
drug- resistant  TLE.19  Cardiac  conduction  abnormalities 
are  also  commonly  reported,  particularly  involving  the 
QT segment. These abnormalities most often include pro-
longation  during  ictal  or  interictal  phases  but  may  also 
show ictal or postictal shortening, particularly after gen-
eralized seizures.20,21 ST- segment changes have also been 
observed, with T- wave inversion and ST- segment depres-
sion occurring more often during generalized seizures and 
sleep and interictally as T- wave alternans. These changes 
may  reflect  long- term  cardiac  conduction  abnormalities 
or cardiac damage or be secondary to medical treatment 
with  depolarization- blocking  antiseizure  medications 

(ASMs).22  Despite  these  findings,  it  is  important  to  note 
that the prevalence of ECG changes in PwE remains rela-
tively low, although higher than in healthy individuals.23 
Finally,  HRV  is  often  lower  in  PwE,  particularly  those 
with  TLE  and  drug  resistance,  suggesting  a  shift  toward 
sympathetic  dominance  in  autonomic  tone.  Notably,  in 
both the preictal and postictal phases, a further decrease 
in HRV measures was observed.24

In  the  thermoregulatory  subsystem,  increases  in  ictal 
temperature  and  EDA  have  been  shown  to  occur  both 
during and after seizures.25 EDA changes have been doc-
umented in multiple seizure types, including generalized, 
focal aware, and impaired awareness seizures, as well as 
motor  and  nonmotor  seizures.  However,  the  most  pro-
nounced response is consistently seen with major motor 
seizures,  particularly  tonic–clonic  seizures.  Chronic 
changes in EDA, such as increased sympathetic response 
latencies,  have  also  been  documented  in  PwE  compared 
to  controls.26  Importantly  for  seizure  forecasting,  auto-
nomic  changes  are  also  observed  during  the  times  pre-
ceding seizures, as epileptic networks in the CNS have a 
strong connection to CAN brain networks. The relevance 
of  autonomic  changes  during  the  preictal  state  was  spe-
cifically examined in studies focused on PwE undergoing 
simultaneous ECoG, scalp EEG, and ECG recordings.27,28 
In one study, the authors examined how noninvasive ECG 

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 
   
28 

| 

measurements compared to scalp EEG and invasive ECoG 
measurements in terms of identifying biomarkers distin-
guishing  the  preictal  and  interictal  states.  Using  a  deep 
learning approach, this study found that extracting power 
spectral  density  features  from  a  single  ECG  sensor  pro-
vided  preictal  information  comparable  to  a  21- electrode 
scalp  EEG  and  a  single  ECoG  channel,  underscoring 
the  efficacy  of  ANS  biosignals  in  reflecting  CNS  cortical 
dynamics.27

|  INFLUE N CE S O N  AUTONOM IC 

4 
FUNCTION:  AGE ,  ME DICAT I O N, 
AND OTHER  FACTOR S

Although seizures and peri- ictal periods may exhibit dis-
tinct  ANS  signatures  relevant  to  epilepsy  monitoring,  it 
is  important  to  carefully  consider  the  interplay  between 
autonomic  function  and  various  physiological  and  path-
ological  factors  to  accurately  utilize  ANS  changes  for 
monitoring  seizures.  Systematic  age- related  autonomic 
changes, as evidenced by HR or HRV fluctuations, are well 
documented.29 HRV increases until late adolescence and 
then declines progressively with age. One study quantified 
this trend as a reduction of approximately 3.6 ms per dec-
ade.30  Notably,  the  HRV  decline  correlates  with  cortical 
thickness thinning, particularly in regions associated with 
autonomic  control,  such  as  the  ventromedial  prefrontal 
cortex and lateral orbitofrontal cortex.31 Likewise, multi-
ple EDA measures are effected by age, for example, with 
increased  age  smaller  phasic  responses  are  observed.32 
Additionally,  distinct  differences  in  autonomic  function 
are observed across sexes and ethnic groups. For instance, 
female  adults  generally  have  higher  HRV  than  males, 
and  African  Americans  show  greater  HRV  compared  to 
European  Americans.33  Gender  and  ethnic  differences 
with  relation  to  EDA  have  also  been  reported;  however, 
patterns of change have not been consistent across differ-
ent studies.32 These inherent differences are significant in 
study design and interpretation, emphasizing that diverse 
cohorts are critical for generalizable findings.

Circadian  rhythms,  centrally  regulated  by  the  supra-
chiasmatic nucleus, also play a significant role in the ANS. 
These diurnal measures have been reported, for example, 
in  the  cardiac  subsystem,  with  HR  slowing  at  night  and 
lengthening of the QRS, PR, and QT intervals. Similar di-
urnal  changes  are  observed  in  the  thermal  and  vascular 
subsystems, evidenced by alterations in EDA and nightly 
blood pressure dips.34–36 Although less widely described, 
longer term rhythms are also known, with multiday and 
seasonal  effects  on  HR  and  blood  pressure.37–39  In  epi-
lepsy  patients,  recent  works  have  shown  that  the  use  of 
ASMs further modulates these effects. Although findings 

vary,  most  studies  report  that  ASM  treatment  reduces 
HRV overall, with higher ASM loads linked to lower HRV 
and  ASM  withdrawal  leading  to  increased  HRV.40–42  In 
contrast,  ASM  loads  have  been  found  not  to  effect  EDA 
activity.40

Finally,  an  intricate  connection  exists  between  emo-
tional  regulation,  cognition,  stress,  and  the  ANS,  as  re-
viewed  by  Critchley  et  al.,43  Thayer  and  Lane,44  and 
Gianaros and Wager.45 CAN regions mediate this interplay 
and  can  affect  autonomic  measurements.  For  instance, 
studies  reported  that  cognitively  demanding  activities 
demonstrated  simultaneous  increased  activation  of  the 
dorsal anterior cingulate or prefrontal medial cortex and 
higher  low- frequency  HRV  power  and  EDA  measure-
ments,  which  reflect  increased  sympathetic  cardiac  in-
fluence. Likewise, emotional states and stress are closely 
related to CAN areas, notably the amygdala and the insula, 
and  modulate  the  autonomic  responses.  Understanding 
these connections is essential, as emotional states, cogni-
tive load, and stress can significantly impact seizure activ-
ity and overall autonomic function in PwE.

|   CONSIDERATIO NS IN THE 

5 
USE OF  ANS  BIOSIGNALS IN 
CLINICAL PRACTICE

For  PwE,  the  critical  question  is  whether  ANS  biosig-
nals  reflect  CNS  changes  related  to  seizure  activity  and 
how  reliable  they  are  for  diagnosis  and  management. 
Traditional  methods  used  by  clinicians  to  assess  disease 
activity,  mainly  self- reported  seizure  diaries,  are  recog-
nized  to  be  highly  inaccurate,  providing  both  over-   and 
underestimations  of  actual  seizure  counts.46–48  This  as-
pect  limits  effective  treatment  response  assessment  and 
interpretation  of  clinical  trials  of  drugs  and  other  inter-
ventions, which often report outcomes in terms of seizure 
load reduction. In recent years, EEG solutions have been 
developed  to  address  this  issue,  including  long- term  im-
plantable intracranial, subscalp, subdermal, and auricular 
EEG recording devices. However, these may not be read-
ily available, require invasive procedures, or be associated 
with stigma.46,49–52

Knowledge  of  changes  in  ANS  features  in  epilepsy 
and technological advancements in the field of wearable 
biosensors  have  led  to  studies  with  two  main  aims:  im-
proved  methods  for  seizure  detection  and  seizure  fore-
casting. Following these developments, the International 
League  Against  Epilepsy  (ILAE)  has  established  testing 
and validation standards for these technologies, outlining 
best  practice  study  designs  for  artificial  intelligence  (AI) 
in this field.53,54 These standards classify studies into five 
phases, ranging from initial exploratory studies (phase 0) 

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 
 
to  large- scale  in- field  validation  studies  (phase  4),  based 
on  methodological  robustness  and  generalizability.  Key 
features  determining  the  study  phase  are  related  to  sub-
ject  selection,  recording  method,  analysis  approach,  and 
the reference standard used to determine the ground truth 
outcome. Based on these criteria, the ILAE issued a weak/
conditional recommendation for the use of clinically val-
idated wearable devices for the detection of tonic–clonic 
seizures. Additional work is needed to establish robust sei-
zure detection in focal seizures.

|  SEIZURE   DETECT ION  USING 

6 
ANS  BIOSIGNALS

Developments  in  wearable  device  use  for  seizure  detec-
tion  have  been  described  in  several  comprehensive  re-
views and a clinical practice guideline published by a joint 
working group of the International Federation of Clinical 
Neurophysiology  and  the  ILAE.54–64  Here,  we  focus  on 
studies relevant to seizure detection based on autonomic 
biosignals, reviewed according to the study phase to better 
contextualize  each  approach's  current  clinical  relevance 
(Table 1).

To date, two phase 4 studies have been reported, utiliz-
ing the Nightwatch system, an upper arm bracelet combin-
ing accelerometry and HR data to detect nocturnal motor 
seizures.65,66 The  first  of  these  studies  was  conducted  in 
the residential setting for adults with intellectual disabili-
ties, whereas the second was conducted in homes of pedi-
atric patients with motor seizures. The Nightwatch system 
showed good acceptability in adults, with a high median 
sensitivity of 86% and a low median false alarm rate (FAR) 
of .25 per night. However, FAR was >1 per night in several 
participants, suggesting further personalization is needed 
to improve overall performance. HR was the critical mo-
dality  for  both  true  and  false  positive  detections.  This 
study  was  followed  by  a  phase  3  study  aimed  at  testing 
whether the established detection algorithm developed for 
adults could be effectively applied for seizure detection in 
children.67 Using the adult detection model for a pediatric 
cohort, a reduced median sensitivity of 75% was reported, 
with a notably high FAR level of .2 per hour that neces-
sitated  midtrial  adjustments  to  the  detection  algorithm 
by modifying alarms to occur only when the child was in 
a  horizontal  position,  eliminating  out  of  bed  detections. 
Subsequently, an additional stage 4 Nightwatch pediatric 
study, conducted in the in- home setting and using a pedi-
atric specific detection model, reported a median sensitiv-
ity  for  detection  of  major  motor  seizures  per  participant 
of  100%  (range = 49%–100%),  with  the  best  performance 
overall  reported  for  tonic–clonic  seizures.  In  this  study, 
similarly to the adult Nightwatch trial, FAR per hour was 

|  29

low, with a median of .04 per participant. However, rather 
than HR, the accelerometry signal was more often respon-
sible for triggering alarms, emphasizing differences in re-
sponse to seizures between age groups.

An  additional  phase  3  multicenter  prospective  study 
assessed multimodal data using the Empatica wristwatch 
device,  utilizing  EDA  and  accelerometry  for  generalized 
tonic–clonic seizure detection among hospitalized adults 
and pediatric patients.68 Using a previously US Food and 
Drug  Administration- approved  machine  learning  algo-
rithm, the study reported high sensitivities for both groups 
(.92  for  pediatric  and  .94  for  adults)  but  noted  a  higher 
FAR in children (1.26 compared to .57 per 24 h). Similarly 
to the Nightwatch study,66 the high FAR was affected by 
a  few  children  having  many  false  alarms.  Seizure  detec-
tion latency was approximately 37 s, reflecting a time pe-
riod that is acceptable for interventions in life- threatening 
motor  seizures  to  prevent  aspirations  or  provide  oxygen 
therapy.

Compared  to  phase  3  and  4  studies,  phase  2  studies 
have been reported more frequently in recent years, pro-
viding valuable insights into initial experiences and novel 
methodologies. These studies, however, are generally not 
validated  on  large  cohorts  or  in- field  settings  and  often 
lack  real- time,  predetermined  detection  algorithms.  One 
significant  application  involves  the  vagal  nerve  stimula-
tion  (VNS)  device,  a  closed- loop  stimulation  system  de-
signed to detect seizures and provide treatment based on 
the detection of increased HR.69,70 Two studies, including 
a  combined  51  adult  and  pediatric  patients,  compared  a 
foreground HR of 10 s against a background HR from the 
previous  5 min.  Different  thresholds  of  increase  in  HR 
were used to detect seizures and trigger VNS stimulation. 
Despite  achieving  sensitivity  of  >80%  for  multiple  HR 
thresholds, a positive correlation between sensitivity and 
FAR was observed, ranging from .5 to 7.2 alarms per hour. 
Nevertheless,  this  approach  successfully  aborted  31%  of 
seizures in the two studies combined and showed a posi-
tive 12- month benefit on seizure reduction. However, the 
broad  applicability  of  this  approach  is  limited  by  the  re-
quirement for an invasive implantation procedure.

Another focus of phase 2 studies has been on expand-
ing seizure detection capabilities to encompass a broader 
range of focal impaired seizures, beyond major motor sei-
zures.  Two  such  studies  using  the  Empatica  wristwatch 
were  conducted  on  a  pediatric  population  hospitalized 
in  epilepsy  monitoring  units.71,72  Employing  deep  learn-
ing techniques, these studies sought to establish detection 
benchmarks across various seizure types. The first study, 
including 94 patients and 548 seizures across nine differ-
ent seizure types, achieved an area under the receiver op-
erating curve (AUC) of .75.71 Subsequently, a larger study 
with 166 patients and 900 seizures reported improvement 

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 
   
30 

| 

y
d
u
t
S

e
s
a
h
p

s
e
r
u
z
i
e
S

R
A
F

y
i
v
i
t
i
s
n
e
S

s
t
n
a
p
i
c
i
t
r
a
P

s
l
a
n
g
i
s
o
i
b

e
c
i
v
e
d
e
l
b
a
r
a
e
W

y
d
u
t
S

S
N
A

.
e
c
n
e
d
i
v
e

f
o
w
e
i
v
e
R

1

E
L
B
A
T

s
e
i
t
i
l
i
b
a
s
i
d

)
n
a
i
d
e
m

(

%
6
8

l
a
u
t
c
e
l
l
e
t
n

i

h
t
i

w
s
t
l
u
d
a
8
2

R
H

,

C
C
A

h
c
t
a
W
t
h
g
i
N

5
6

)
8
1
0
2
(

.
l
a

t
e

s
d
n
e
r
A

n
o
i
t
c
e
t
e
d
e
r
u
z
i
e
S

4

4

3

3

2

2

2

2

2

2

2

2

,

C
T
B
F

,

C
T
G
9
0
8

r
e
h
t
o

,

K
H

,

M
G

r
o
t
o
m

r
o
j
a
m

,

C
T
B
F

,

C
T
G
2
5
5

r
e
h
t
o

,

K
H

,

M
G

r
o
t
o
m

r
o
j
a
m

,

C
T
B
F

,

C
T
G
4
8
3

r
e
h
t
o

,

K
H

,

M
G

r
o
t
o
m

r
o
j
a
m

C
T
B
F

,

C
T
G
5
3

C
T
B
F

,

C
T
G
1
3

t
h
g
i
n
/
5
2

.

)
n
a
i
d
e
m

(

h
/
7
0

.

h
/
8
0

.

h
4
2
/
6
2
1

.

h
4
2
/
7
5

.

%
9
8

%
4
9
7

.

%
2
9

%
4
9

A
F

,

A
I
F

,

C
T
B
F
6
6

.

h
/
2
7
–
5

.

R
H
e
l
p
i
t
l
u
m

r
o
f

%
0
8
>

s
d
l
o
h
s
e
r
h
t

A
I
F

,

A
F

,

C
T
B
F
9
8

d
e
t
r
o
p
e
r

t
o
N

R
H
e
l
p
i
t
l
u
m

r
o
f

%
0
8
>

&
d
e
z
i
l
a
r
e
n
e
g

e
l
p
i
t
l
u
m
8
4
5

t
e
s
n
o
l
a
c
o
f

&
d
e
z
i
l
a
r
e
n
e
g

e
l
p
i
t
l
u
m
0
0
9

t
e
s
n
o
l
a
c
o
f

,

C
T
B
F

,

C
T
G
3
3

,

M
G

,

C
T
G
5
5
2

A
F

,

A
I
F

,

C
T
B
F

A
F

,

A
I
F

,

C
T
B
F

,

M
G

,

C
T
G
1
5

A
F

,

A
I
F

R
P
F
%
3
5
3

.

h
4
2
/
7

.

h
4
2
/
4

.

h
4
2
/
2
1

.

s
d
l
o
h
s
e
r
h
t

C
U
A
2
5
7

.

%
9
3
8

.

%
9
6
6

.

%
9
3

%
4
1
3

.

,

C
T
B
F

,

C
T
G
6
2
1

h
4
2
/
0
1

.

%
1
3
9

.

)
s
r
e
d
n
o
p
s
e
r
%
5
3
5
(

.

s
t
l
u
d
a
3
4

,

C
T
B
F

,

C
T
G
3
2

A
F

,

A
I
F

A
F

,

A
I
F

h
4
2
/
9

.

A
F

,

A
I
F

,

C
T
B
F

,

C
T
G
4
7
1

h
4
2
/
2
6

.

%
7
8

%
2
8
7

.

s
t
l
u
d
a
1
1

s
t
l
u
d
a
2
6

c
i
r
t
a
i
d
e
p
3
5

R
H

,

C
C
A

h
c
t
a
W
t
h
g
i
N

.
l
a

t
e
n
e
n
e
h
r
t
s
e

W
n
a
V

6
6

)
3
2
0
2
(

c
i
r
t
a
i
d
e
p
3
2

R
H

,

C
C
A

h
c
t
a
W
t
h
g
i
N

7
6

)
2
2
0
2
(

.
l
a

t
e
n
o
r
e
z
a
L

c
i
r
t
a
i
d
e
p
5
8

C
C
A

,

A
D
E

4
E
a
c
i
t
a
p
m
E

8
6

)
1
2
0
2
(

.
l
a

t
e

i
t
a
r
o
n
O

s
t
l
u
d
a
7
6

s
t
l
u
d
a
6
1

s
t
l
u
d
a
0
2

R
H

R
H

R
S
e
r
i
p
s
A

9
6

)
5
1
0
2
(

.
l
a

t
e
n
o
o
B

R
S
e
r
i
p
s
A

0
7

)
6
1
0
2
(

.
l
a

t
e

r
e
h
s
i
F

C
C
A

t
r
o
h
o
c
d
e
x
i
m
4
9

,

P
V
B

,

A
D
E

4
E
a
c
i
t
a
p
m
E

1
7

)
1
2
0
2
(

.
l
a

t
e
g
n
a
T

t
r
o
h
o
c
d
e
x
i
m
6
6
1

,

P
V
B

,

A
D
E

4
E
a
c
i
t
a
p
m
E

2
7

)
3
2
0
2
(

.
l
a

t
e
u
Y

s
t
l
u
d
a
5
3

s
t
l
u
d
a
7
9

s
t
l
u
d
a
0
3

C
C
A

V
R
H

V
R
H

V
R
H

V
R
H

s
n
e
S
i
v
o
M

.
l
a

t
e
m
a
k
e
b
n
a
h
a
J

4
7

)
1
2
0
2
(

h
c
t
a
P
e

6
7

)
9
1
0
2
(

.
l
a

t
e
n
e
s
e
p
p
e
J

h
c
t
a
P
e

7
7

)
0
2
0
2
(

.
l
a

t
e
n
e
s
e
p
p
e
J

h
c
t
a
P
e

8
7

)
3
2
0
2
(

.
l
a

t
e
n
e
s
e
p
p
e
J

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
y
d
u
t
S

e
s
a
h
p

2

1

2

2

2

2

2

2

2

2

2

2

2

1

A
F

,

A
I
F

,

C
T
B
F
4
5

,

C
T
B
F

,

C
T
G
9
5

A
F

,

A
I
F

l
a
c
o
f
4
5
1

s
e
r
u
z
i
e
S

&
d
e
z
i
l
a
r
e
n
e
g

e
l
p
i
t
l
u
m
5
2

t
e
s
n
o
l
a
c
o
f

A
I
F
7
4

K
H

,

M
G

,

C
T
G
6
8

C
T
G
6
1

C
T
B
F
9
4

C
T
F
6

h
4
2
/
5
2

.

R
A
F

y
t
i
c
i
f
i
c
e
p
s

%
5
6
5
8

.

h
4
2
/
3
0
1

.

h
4
2
/
7
2

.

h
/
0
8
1

.

h
/
1
1
2

.

t
h
g
i
n
/
7
5
–
3
2

.

.

h
4
2
/
4
7

.

h
4
2
/
2

.

C
T
B
F

,

C
T
G
1
2

h
4
2
/
9
1

.

y
i
v
i
t
i
s
n
e
S

%
8
4
8

.

%
6
2
9

.

%
6
6
8
8

.

%
2
7

%
2
3

%
0
7

%
7
8
–
1
7

%
5
5
4
9

.

%
4
9

%
9
0
9

.

6
7
f
o
n
a
e
M

s
e
r
u
z
i
e
s

&
d
e
z
i
l
a
r
e
n
e
g

e
l
p
i
t
l
u
m
2
5
4

t
e
s
n
o
l
a
c
o
f

d
e
t
r
o
p
e
r

t
o
N

d
e
t
r
o
p
e
r

t
o
N

d
e
t
r
o
p
e
r

t
o
N

i

W
T
%
2
7
4

.

h
4
2
/
8
9
4

.

%
6
5
7

.

%
4
6
6

.

A
F

,

A
I
F

,

C
T
B
F
4
1

h
/
2
6

.

%
7
5
8

.

s
e
r
u
z
i
e
s

.

4
2
7
f
o
n
a
e
M

d
e
t
r
o
p
e
r

t
o
N

d
e
t
r
o
p
e
r

t
o
N

S
N
A

s
t
n
a
p
i
c
i
t
r
a
P

s
l
a
n
g
i
s
o
i
b

e
c
i
v
e
d
e
l
b
a
r
a
e
W

y
d
u
t
S

s
t
l
u
d
a
2
2

s
t
l
u
d
a
6

V
R
H

V
R
H

x
R
m

r
i
f
n
o
C

0
8

)
3
2
0
2
(

.
l
a

t
e
n
e
s
e
p
p
e
J

h
c
t
a
P
e

9
7

)
4
2
0
2
(

.
l
a

t
e
n
e
s
e
p
p
e
J

s
t
l
u
d
a
8
1

R
D
E

,

V
R
H

U
Y
N

I
a
i
d
r
a
C
t
r
a
m
S

1
8

)
9
1
0
2
(

.
l
a

t
e

r
a
f
i
h
g
o
o
r
o
F

c
i
r
t
a
i
d
e
p
8
1

,

V
R
H

,

R
H

h
c
t
a
p
o
i
B
r
y
h
p
e
Z

.
l
a

t
e

r
e
v
a
r
 C
-
y
t
r
a
g
e
H

C
C
A

s
o
r
a
F
m
u
i
t
t
i
B

5
0
1

)
1
2
0
2
(

)
d
e
u
n
i
t
n
o
C
(

1

E
L
B
A
T

3
4

0
8

9
6

8
3

0
1

s
t
l
u
d
a
1
1

R
H

C
C
A

,

A
D
E

C
C
A

,

A
D
E

C
C
A

,

R
H

m
l
a
C

i

s
o
a
r
F
n
o
i
t
o
M
e

4
E
a
c
i
t
a
p
m
E

.
l
a

t
e

e
l
e
e
t
s
a
c
e
d
n
a
V

3
8

)
7
1
0
2
(

t
l
i
u
 b
-
m
o
t
s
u
C

5
8

2
1
0
2

.
l
a

t
e
h
o
P

r
e
m
m
h
S

i

4
8

)
7
1
0
2
(

.
l
a

t
e

l
e
d
n
A
n
a
v

4
E

,
3
E
a
c
i
t
a
p
m
E

6
8

)
7
1
0
2
(

.
l
a

t
e

i
t
a
r
o
n
O

9
6

,

P
M
E
T

,

A
D
E

4
E
a
c
i
t
a
p
m
E

0
0
1

)
0
2
0
2
(

.
l
a

t
e

l
e
s
i
e
M

6

6
4

7

C
C
A

,

P
V
B

,

P
V
B

,

P
M
E
T

,

R
H

,

A
D
E

C
C
A

R
H

4
E
a
c
i
t
a
p
m
E

1
0
1

)
1
2
0
2
(

.
l
a

t
e

i
r
e
s
s
a
N

t
i
b
t
i
F

2
0
1

)
1
2
0
2
(

.
l
a

t
e
y
l
o
r
a
K

V
R
H

r
e
t
e
m
e
l
e
t
d
e
t
a
c
i
r
b
a
F

4
0
1

)
0
2
0
2
(

.
l
a

t
e
a
w
a
k
a
m
a
Y

C
C
A

,

A
D
E

4
E
a
c
i
t
a
p
m
E

7
8

)
1
2
0
2
(

.
l
a

t
e

r
e
h
c
t
t
ö
B

,

P
M
E
T

,

V
R
H

,

R
H

,

A
D
E

C
C
A

4
E
a
c
i
t
a
p
m
E

9
9

)
3
2
0
2
(

.
l
a

t
e
g
g
e
r
G

n
o
i
t
c
i
d
e
r
p
d
n
a
g
n
i
t
s
a
c
e
r
o
f

e
r
u
z
i
e
S

|  31

i

d
e
n
m
r
e
t
e
d
s
i

e
s
a
h
p
y
d
u
t
S

.

d
e
t
o
n
e
s
i
w
r
e
h
t
o
s
s
e
l
n
u

,
s
n
a
e
m

s
a
d
e
t
r
o
p
e
r

e
r
a
s
c
i
r
t
e
m
e
c
n
a
m
r
o
f
r
e
P

.
s
l
a
n
g
i
s
o
i
b
m
e
t
s
y
s

s
u
o
v
r
e
n
c
i
m
o
n
o
t
u
a
n
o
d
e
s
a
b
g
n
i
t
s
a
c
e
r
o
f
d
n
a
n
o
i
t
c
e
t
e
d
e
r
u
z
i
e
s

r
o
f

s
e
c
i
v
e
d
e
l
b
a
r
a
e
w
g
n
i
s
u
s
e
i
d
u
t
S
:
e
t
o
N

3
5
n

.

i
l
v
y
R
d
n
a
y
k
z
c
i
n
e
B
o
t
g
n
i
d
r
o
c
c
a

,

K
H

;
c
i
n
o
l
c
–
c
i
n
o
t

t
e
s
n
o
d
e
z
i
l
a
r
e
n
e
g
,

C
T
G

;
r
o
t
o
m

t
e
s
n
o
d
e
z
i
l
a
r
e
n
e
g
,

M
G

;
e
t
a
r

e
v
i
t
i
s
o
p
e
s
l
a
f

,

R
P
F

;
s
s
e
n
e
r
a
w
a
d
e
r
i
a
p
m

i

l
a
c
o
f

,

A
I
F

;
c
i
n
o
l
c
–
c
i
n
o
t

l
a
r
e
t
a
l
i
b
o
t

l
a
c
o
f

,

C
T
B
F

;
e
t
a
r

m
r
a
l
a
e
s
l
a
f

,

R
A
F

;
e
r
a
w
a
l
a
c
o
f

,

A
F

;

n
o
i
t
a
r
i
p
s
e
r

d
e
v
i
r
e
 d
-
y
h
p
a
r
g
o
i
d
r
a
c
o
r
t
c
e
l
e

,

R
D
E

;
y
t
i
v
i
t
c
a
l
a
m
r
e
d
o
r
t
c
e
l
e

,

A
D
E

;
e
s
l
u
p
e
m
u
l
o
v
d
o
o
l
b

,

P
V
B

;
e
v
r
u
c
g
n
i
t
a
r
e
p
o
r
e
v
i
e
c
e
r

e
h
t

r
e
d
n
u
a
e
r
a
,

C
U
A

;

m
e
t
s
y
s

s
u
o
v
r
e
n
c
i
m
o
n
o
t
u
a
,

S
N
A

;
y
r
t
e
m
o
r
e
l
e
c
c
a
,

C
C
A

:
s
n
o
i
t
a
i
v
e
r
b
b
A

i

.
g
n
n
r
a
w
n

i

e
m

i
t

,

W
T

i

;
e
r
u
t
a
r
e
p
m
e
t

,

P
M
E
T

;
y
t
i
l
i
b
a
i
r
a
v
e
t
a
r

t
r
a
e
h

,

V
R
H

;
e
t
a
r

t
r
a
e
h

,

R
H

;
c
i
t
e
n
i
k
r
e
p
y
h

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
32 

| 

with AUC > .8 for 19 of 28 seizure types, raising the overall 
detection AUC to .79. Although these studies show prom-
ise for wider application of seizure detection, some seizure 
types were characterized by low overall seizure numbers 
and high variability in false positives (range = 15%–46%). 
An  additional  retrospective  study  examining  76  pediat-
ric patients further reported that poorly detected seizures 
were associated with shorter seizure durations, lower age, 
and higher ASM dose, pointing to additional factors that 
affect  the  performance  of  deep  learning  approaches.73 
These caveats may limit the use of the currently developed 
models for an alarm system. However, they may still have 
value as a seizure- monitoring and diary adjunct tool or as 
a  basis  for  future  development  as  larger  patient  datasets 
become available.72

Other phase 2 studies have investigated seizure detec-
tion by exploring a broader range of cardiac features. One 
such study included 162 adult PwE undergoing simulta-
neous  recordings  with  chest-   and  wrist- based  wearable 
devices in the video- EEG monitoring unit. It focused on 
105  HR-   and  HRV- related  metrics.74  The  authors  devel-
oped  and  tested  unique  seizure  detection  models  across 
three  patient  groups  in  distinct  conditions  (either  mo-
bile or mostly in bed). When comparing separate patient 
groups  for  validation,  the  outcomes  illustrated  a  broad 
spectrum  of  detection  sensitivities  (4%–62.8%)  and  false 
detection rates (.08–5.1 per 24 h). These results underscore 
the  cardiac  variability  related  to  seizure  type,  the  influ-
ence  of  patient  conditions  on  detection  efficacy,  and  the 
need  to  rigorously  test  for  generalizability  in  developing 
cardiac- based  seizure  detection  devices.  Two  additional 
studies  used  a  wearable  patch  to  extract  a  modified  car-
diac  sympathetic  index  determined  from  100  successive 
R- R peaks, an approach the same study group developed 
for real- time HRV analysis.75 These studies demonstrated 
that 83.3%–90.5% detection sensitivities were reached in a 
subset of patients with ictal HR increase, with an FAR of 
approximately 1 per 24 h.76,77 Notably, ictal HR increase of 
>50 beats per minute was identified as a predictor of good 
performance. A subsequent study on the same dataset fur-
ther reduced the FAR to approximately .6 per 24 h through 
a logistic regression machine learning approach aimed at 
adaptive  patient- specific  detection  thresholding  for  sei-
zure alarms.78 The patient adaptive threshold method was 
recently also validated in a dataset consisting of different 
demography  from  Brazilian  patients  with  reproducible 
sensitivity and even lower FAR of .25 per 24 h. However, 
these  investigators  collected  data  retrospectively,  and 
therefore,  discontinuous  data  were  used  from  standard 
wired  ECG  recording  during  long- term  monitoring.79 To 
allow for longer term recordings and alleviate the need for 
changing ECG wearable patch adhesives, a phase 1 proof 
of  concept  study  examined  the  use  of  a  subcutaneously 

implantable  cardiac  monitor  for  seizure  detection  in  six 
patients and up to 8 months of recording, reporting a high 
sensitivity  of  92.6%  and  a  24- h  FAR  of  2.7.80  HRV  fea-
tures were also explored in an additional study, including 
18  patients  and  211 h  of  recording  using  the  chest- worn 
SmartCardia INYU sensor, which also took respiration in 
relation to the R- R interval into account. Although FARs 
are not reported, seizures were detected with a sensitivity 
of 88.7% and a specificity of 85.7% while employing a re-
duced energy consumption that allowed for a battery life 
of 137 days.81

Although  these  studies  demonstrate  the  potential  of 
cardiac  features  for  seizure  detection,  they  also  under-
score  the  challenges  posed  by  data  quality  and  artifacts 
from  daily  activities.  One  investigation  into  28  patients 
with  62  focal  seizures  examined  photoplethysmographic 
(PPG)  measurements  from  the  Empatica  wristwatch, 
compared against ECG recordings, to assess the impact of 
seizures and spontaneous movements on signal quality.82 
This study reported that spontaneous and epileptic move-
ments hinder the ability of the biosensor to obtain good- 
quality data. However, in 60% of motor seizures, ictal HR 
increase could still be identified, as it occurred before the 
motor symptoms. Furthermore, the PPG signal was well 
correlated temporally to both the ECG and EEG ictal re-
cordings,  making  it  a  valuable  biomarker,  especially  at 
rest. The issue of motion artifacts impairing HR detection, 
particularly  with  ictal  HR  increase,  was  highlighted  in 
another study.83 This study found that in a dataset of 11 
patients and 47 temporal lobe seizures, PPG- based seizure 
detection provided a sensitivity of 32%, considerably lower 
than an additional wearable ECG device (70%) and a hos-
pital ECG system (57%). This discrepancy underscores the 
influence of patient movement on the reliability of wear-
able  device  readings.  Another  multicenter  prospective 
study used a different system for measuring accelerome-
try and HR, the Shimmer device, and also reported major 
recording issues, with data analysis only possible for 43 of 
95 patients recruited. This study also reported high FARs 
(2.3–5.7  per  night),  resulting  in  low  positive  predictive 
values.84  Together,  these  studies  emphasize  the  need  for 
improved methodologies to mitigate these issues in real- 
world settings.

In  addition  to  the  phase  3  study  described  above,68 
EDA has been employed in several phase 2 studies for sei-
zure  detection.  The  Empatica  wristwatch,  incorporating 
accelerometry and EDA signals, was used in a multicenter 
study including 45 adult and 24 pediatric patients with 55 
tonic–clonic seizures. This study achieved a sensitivity of 
94.5% with an FAR of .2, improving on a previously pub-
lished  algorithm  that  was  trained  on  a  smaller  and  less 
heterogeneous cohort.85,86 These findings were reinforced 
in an additional relatively small two- center study with 10 

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 
 
patients  using  the  same  wearable  device  but  with  a  dif-
ferent, openly available detection algorithm. In this study, 
10 of 11 tonic–clonic seizures were detected with an FAR 
of .19 per day.87 These outcomes indicate that employing 
various algorithms can yield consistent detection results. 
However, it is important to note that all detections in these 
phase 2 studies were conducted within hospital settings, 
potentially obscuring the FARs in everyday environments.
One potential of using autonomic markers is not only 
for  detecting  seizure  occurrence  but  also  to  predict  sei-
zure severity and determine predictive biomarkers for an 
adverse seizure outcome, such as SUDEP. Biomarkers of 
seizure severity derived from wearables have been previ-
ously reviewed64 and include cardiac markers such as ictal 
and  postictal  bradycardia  and  asystole,  interictal  HRV 
dysregulation  (both  increased  and  decreased  HRV),  and 
a postictal decrease in parasympathetic activity. Likewise, 
increased  postictal  EDA,  reflecting  abnormally  height-
ened sympathetic activity, is particularly marked in post-
ictal generalized EEG suppression cases and SUDEP.88

|  SEIZURE   FOR ECA ST IN G 

7 
USING  ANS BI OSIG NA LS

Whereas seizure detection aims to accurately quantify sei-
zure counts and implement alarm systems to prevent in-
jury, seizure prediction or forecasting may enable patients 
to  take  preventive  measures  during  periods  of  increased 
risk,  such  as  taking  additional  medication  or  avoiding 
dangerous  settings.  Unlike  the  deterministic  nature  of 
seizure  detection,  which  confirms  the  presence  or  ab-
sence of seizures, forecasting adopts a more probabilistic 
approach,  assessing  the  likelihood  of  a  seizure  within  a 
specific  time  period.  Clinical  recognition  of  cyclical  pat-
terns  in  seizure  occurrences—similar  to  other  biological 
rhythms observed in immune, endocrine, and cardiovas-
cular  functions—has  provided  further  opportunity  for 
seizure forecasting.38,89 More recently, studies leveraging 
long- term intracranial EEG recordings from people with 
drug- resistant  epilepsy  have  indicated  that  both  seizure 
risk  and  interictal  epileptic  activity  fluctuate  with  circa-
dian and multiday rhythms.90–93 Based on these observa-
tions and novel theoretical insights into the dynamics of 
seizure onset mechanisms and precursors,92,94 the seizure 
prediction and forecasting field has recently seen consid-
erable  attention,  as  evidenced  by  several  comprehensive 
reviews  published.95–98  Including  autonomic  biosignals 
for  forecasting  offers  a  promising  avenue  for  providing 
seizure prediction without invasive procedures, making it 
more widely applicable in clinical settings.

One study exploring the cyclical patterns in intracranial 
EEG and autonomous biosignals compared simultaneous 

|  33

recordings from both modalities in 10 PwE (seven subjects 
had  an  average  of  76  seizures  each)  over  an  average  re-
cording duration of 232 days.99 This study identified that, 
in  parallel  to  multiday  patterns  of  elevated  seizure  risk 
associated with intracranial EEG recordings, cyclical pat-
terns were seen in temperature in five patients, in HR in 
six patients (after adjusting for the confounding effects of 
physical activity), and in the phasic component of EDA in 
four patients. Furthermore, there was a strong coherence 
between intracranial and autonomous circadian patterns, 
suggesting that the latter could be used as a surrogate mea-
sure.  However,  notably,  no  such  significant  association 
was  found  concerning  multiday  patterns.  Importantly, 
this study reinforced prior works that focused exclusively 
on autonomic biosignals concerning patterns of increased 
seizure  risk.50,100–102  Another  study  included  31  PwE 
using  wearable  wristwatches  and  examining  circadian 
and  multiday  cardiac  patterns  associated  with  increased 
seizure risk, as documented by seizure diaries.102 In this 
study, the authors found that multiday HR cycles in most 
patients correlated to approximately weekly and monthly 
frequencies.  In  10  of  19  patients  who  recorded  seizures, 
an increased risk aligning with these patterns was found.

Several  studies  were  aimed  not  only  at  examining 
heightened  risk  periodicities  but  also  at  establishing 
shorter term, clinically relevant prediction horizons. One 
phase  2  study  used  a  deep  learning  approach  to  analyze 
HR,  EDA,  temperature,  and  accelerometry  from  wear-
able wristwatches in a cohort of 69 pediatric patients with 
452  seizures  during  video- EEG  monitoring.100  Findings 
revealed that for 30 of the 69 patients, seizures could be 
predicted  at  better- than- chance  level  with  an  average 
improvement  over  chance  of  28.5%  and  a  31- min  pre-
diction  horizon  on  average.  Prediction  performance  was 
highest  when  combining  multiple  autonomous  biosig-
nals. Although the study was constrained by a relatively 
brief  average  recording  duration  per  patient,  it  did  not 
require patient- specific fine- tuning of prediction models. 
It provided evidence that performance may improve with 
increased  training  data  size.  Other  studies  have  focused 
solely on cardiac measures. One phase 2 study examining 
15 patients during video- EEG monitoring reported a sen-
sitivity of 89% for prediction of seizures within a horizon 
of  15 min.  This  study,  however,  required  a  model  to  be 
trained  specifically  for  each  patient  and  still  had  a  high 
FAR of almost 10 per day.103 Another study similarly re-
ported  a  prediction  horizon  of  15 min,  using  a  real- time 
wearable HRV measurement device, with a sensitivity of 
85% and an FAR of 14 per day.104

Other  studies  have  focused  on  examining  in- field, 
long- term data to evaluate feasibility of seizure forecasting 
in home environments. A notable study included six PwE 
using the RNS implantable device as a seizure reference, 

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 
   
34 

| 

thus predicting electrophysiological rather than just clini-
cal seizures.101 This study analyzed multiple signals mea-
sured using the Empatica device, including temperature, 
EDA, HR, and accelerometry. In five of six PwE, seizure 
forecasts  were  significantly  above  chance  level,  with  a 
mean AUC of .75. Alerts occurred on average 33 min be-
fore seizures. Another study in a retrospective and pseu-
doprospective setting with 11 patients also demonstrated 
that forecasting is feasible, achieving above chance hourly 
and daily predictions in all patients, compared to seizure 
diary  self- reports.50  Notably,  in  this  latter  study,  models 
were  retrained  weekly  on  personalized  data.  Thus,  this 
study  does  not  provide  an  out- of- the- box  solution  that 
would be immediately available for a prospective new pa-
tient but highlights the utility of personalized retraining. 
Despite the small cohorts, both works are important to es-
tablish the clinical feasibility of long- term in- field seizure 
forecasting.

|  CHALLE NG ES A ND  FUT U RE 

8 
DIRECTIONS

Although  significant  progress  has  been  made  in  sei-
zure  detection  and  forecasting,  several  challenges  re-
main. One primary concern is the relatively low number 
of  patients  and  seizures  included  in  studies,  coupled 
with  brief  durations  of  data  recording.  Classification 
algorithms,  particularly  those  based  on  deep  learning, 
require substantial data to refine their accuracy and re-
liability.100 Although computational techniques such as 
data augmentation are employed to expand datasets arti-
ficially, larger, more diverse data collections are critical 
to enhance these approaches' generalizability and prac-
tical applicability. Further compounding this challenge 
are  the  training  conditions  under  which  many  models 
are  developed.  The  majority  of  studies  are  currently 
conducted in the hospital setting, where PwE are often 
confined  to  bed  and  patterns  of  autonomic  activity  do 
not reflect those of daily life activities, as demonstrated 
by  Jahanbekam  and  colleagues.74  Training  and  testing 
conditions must be expanded to improve generalizabil-
ity and robustness of models in out- of- hospital settings. 
Another  complex  issue  involves  the  evaluation  of  pre-
diction  algorithms,  which  must  account  for  a  variety 
of  factors,  including  a  baseline  chance  level  for  mean-
ingful  comparison,  the  specific  periods  being  assessed 
(e.g., interictal vs. preictal, sleep vs. wake states), defini-
tions of seizures, and the decision to include or exclude 
clusters of seizures. The introduction of testing and re-
porting  standards  marks  progress  toward  harmonizing 
the  field,53  yet  a  comprehensive  benchmark  dataset  is 
essential  for  effectively  comparing  the  performance  of 

diverse methodologies. Ideally, such a dataset would fa-
cilitate cross- center comparisons, increase sample sizes, 
and enable out- of- sample validation, contributing to de-
veloping  detection  models  that  demonstrate  enhanced 
performance across different patient demographics and 
clinical settings.

In addition to these methodological challenges, several 
critical  clinical  aspects  must  be  considered.  First,  seizure 
detection and forecasting need to be further developed for 
multiple seizure types and vigilance states. So far, clinical 
applicability  of  seizure  detection  has  only  been  demon-
strated  on  major  motor  seizures,  and  although  other  sei-
zure  types  have  been  investigated,  these  should  be  more 
rigorously  studied.  Likewise,  many  studies  have  reported 
high  detection  rates  during  sleep,  with  limited  and  clini-
cally  insufficient  performance  during  wake.  Age  also  sig-
nificantly  affects  model  efficacy,  with  younger  PwE  often 
showing  decreased  performance.73  This  highlights  the 
need  for  further  research  into  age- adaptive  models,  espe-
cially considering the mixed pediatric and adult cohorts in 
many studies. Methods from explainable AI will be crucial 
in further identifying these data constraints.73 Third, ASM 
regimes have been shown to modulate autonomic biomark-
ers and affect detection performance, with decreased ASM 
load associated with improved sensitivities and decreased 
FAR.73  The  impact  of  nonepilepsy  medications,  such  as 
beta- blockers  and  carbonic  anhydrase  inhibitors,  on  au-
tonomic  signals  like  HR  and  EDA  remains  unexplored. 
Fourth,  algorithms  have  been  trained  on  drug- resistant 
PwE.  However,  special  populations,  including  those  with 
epileptic encephalopathies or syndromic diseases, may re-
quire tailoring of devices. Moreover, in older populations, 
the presence of comorbidities—particularly cardiovascular 
conditions—may interfere with the accuracy of autonomic 
measures,  necessitating  models  that  can  differentiate 
between  epilepsy- related  changes  and  those  stemming 
from other health issues. Fifth, the influence of biological 
rhythms, including circadian and multiday patterns, on au-
tonomic signals warrants further investigation. These nat-
ural fluctuations can impact the manifestation of seizures 
and the efficacy of forecasting models. Finally, conducting 
additional studies in patients' home environments is essen-
tial. The majority of current research has been conducted 
in controlled hospital settings, which do not fully replicate 
the  home  environment,  where  behavior  is  less  restricted 
and different stressors may trigger seizures.

9 

|   CONCLUSI ONS

We  here  provided  a  narrative  review  about  the  progress 
made and the challenges that remain in seizure detection 
and forecasting using autonomic biosignals. Although this 

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 
 
field is rapidly growing, the success of this endeavor will 
rely on the community's ability to expand datasets and es-
tablish robust testing and benchmarking methodologies, 
share  knowledge  and  technology,  and  integrate  patient- 
specific  requirements.  Future  research  needs  to  develop 
scientifically  robust  and  practical  methodologies,  ensur-
ing  that  technological  advancements  improve  outcomes 
for individuals with epilepsy.

AUTHOR  CONTRIBUTIONS
Gadi Miron: Writing–original draft; writing–review and 
editing;  conceptualization  of  study.  Mustafa  Halimeh, 
Jesper  Jeppesen,  Tobias  Loddenkemper:  Writing–re-
view  and  editing.  Christian  Meisel:  Conceptualization 
of study; writing–review and editing.

ACKNOWLEDGMENTS
The study was supported by the NeuroCure Clinical Research 
Center,  funded  by  the  Deutsche  Forschungsgemeinschaft 
(German  Research  Foundation)  under  Germany's 
Excellence  Strategy  EXC  2049- 390688087.  T.L.  was  sup-
ported by the Epilepsy Research Fund. Open Access fund-
ing enabled and organized by Projekt DEAL.

CONFLICT  OF INTEREST STATEME N T
T.L. is part of patents and patent applications to detect 
and predict clinical outcomes, and to detect, manage, di-
agnose, and treat neurological conditions, epilepsy, and 
seizures,  but  none  of  these  has  been  licensed.  He  has 
received device donations to Boston Children's Hospital 
for research purposes from various companies, including 
Empatica. In the past, he has received research support 
paid  to  Boston  Children's  Hospital  from  Empatica  for 
research  unrelated  to  this  study.  C.M.  is  part  of  patent 
applications to detect and predict clinical outcomes and 
to manage, diagnose, and treat neurological conditions. 
C.M. has received speaker and/or consultation fees from 
UNEEG  and  Bristol- Myers  Squibb,  all  outside  the  sub-
mitted  work.  The  remaining  authors  have  no  conflicts 
of interest. We confirm that we have read the Journal's 
position on issues involved in ethical publication and af-
firm that this report is consistent with those guidelines.

DATA  AVA ILABILITY  STAT EME N T
Data  sharing  is  not  applicable  to  this  article,  as  no  new 
data were created or analyzed in this study.

ORCID
Gadi Miron 
Jesper Jeppesen 
Christian Meisel 

 https://orcid.org/0000-0003-0842-1806 

 https://orcid.org/0000-0002-3095-2040 
 https://orcid.org/0000-0003-2984-5480 

|  35

R E F E R E N C E S
  1.  Baumgartner C, Koren J, Britto- Arias M, Schmidt S, Pirker S. 
Epidemiology  and  pathophysiology  of  autonomic  seizures:  a 
systematic review. Clin Auton Res. 2019;29(2):137–50.

  2.  Barot  N,  Nei  M.  Autonomic  aspects  of  sudden  unexpected 
death in epilepsy (SUDEP). Clin Auton Res. 2019;29(2):151–60.
  3.  Conti F. Claude Bernard's des Fonctions du Cerveau: an ante 
litteram  manifesto  of  the  neurosciences?  Nat  Rev  Neurosci. 
2002;3(12):979–85.

  4.  Sevcencu  C,  Struijk  JJ.  Autonomic  alterations  and  cardiac 

changes in epilepsy. Epilepsia. 2010;51(5):725–37.

  5.  Shmuely  S,  van  der  Lende  M,  Lamberts  RJ,  Sander  JW, Thijs 
RD. The heart of epilepsy: current views and future concepts. 
Seizure. 2017;44:176–83.

  6.  Gaitatzis  A,  Sisodiya  SM,  Sander  JW.  The  somatic  comor-
bidity  of  epilepsy:  a  weighty  but  often  unrecognized  burden. 
Epilepsia. 2012;53(8):1282–93.

  7.  Shaffer  F,  Ginsberg  JP.  An  overview  of  heart  rate  variability 

metrics and norms. Front Public Health. 2017;5:258.

  8.  Goldenholz DM, Kuhn A, Austermuehle A, Bachler M, Mayer 
C,  Wassertheurer  S,  et  al.  Long- term  monitoring  of  cardio-
respiratory  patterns  in  drug- resistant  epilepsy.  Epilepsia. 
2017;58(1):77–84.

  9.  Ruiz  Vargas  E,  Sörös  P,  Shoemaker  JK,  Hachinski  V.  Human 
cerebral  circuitry  related  to  cardiac  control:  a  neuroimaging 
meta- analysis. Ann Neurol. 2016;79(5):709–16.

 10.  Thayer JF, Ahs F, Fredrikson M, Sollers JJ, Wager TD. A meta- 
analysis  of  heart  rate  variability  and  neuroimaging  studies: 
implications for heart rate variability as a marker of stress and 
health. Neurosci Biobehav Rev. 2012;36(2):747–56.

 11.  Soulier  H,  Mauguière  F,  Catenoix  H,  Montavont  A,  Isnard  J, 
Hermier  M,  et  al.  Visceral  and  emotional  responses  to  direct 
electrical  stimulations  of  the  cortex.  Ann  Clin Transl  Neurol. 
2023;10(1):5–17.

 12.  Chouchou  F,  Mauguière  F,  Vallayer  O,  Catenoix  H,  Isnard  J, 
Montavont A, et al. How the insula speaks to the heart: cardiac 
responses to insular stimulation in humans. Hum Brain Mapp. 
2019;40(9):2611–22.

 13.  Mangina CA, Beuzeron- Mangina JH. Direct electrical stimula-
tion of specific human brain structures and bilateral electroder-
mal activity. Int J Psychophysiol. 1996;22(1–2):1–8.

 14.  Cox  OD,  Munjal  A,  McCall  WV,  Miller  BJ,  Baeken  C, 
Rosenquist  PB.  A  review  of  clinical  studies  of  electrodermal 
activity and transcranial magnetic stimulation. Psychiatry Res. 
2023;329:115535.

 15.  Eggleston KS, Olin BD, Fisher RS. Ictal tachycardia: the head- 

heart connection. Seizure. 2014;23(7):496–505.

 16.  Hirsch  M,  Altenmüller  D- M,  Schulze- Bonhage  A.  Latencies 
from intracranial seizure onset to ictal tachycardia: a compari-
son to surface EEG patterns and other clinical signs. Epilepsia. 
2015;56(10):1639–47.

 17.  Leutmezer  F,  Schernthaner  C,  Lurger  S,  Pötzelberger  K, 
Baumgartner  C.  Electrocardiographic  changes  at  the  onset  of 
epileptic seizures. Epilepsia. 2003;44(3):348–54.

 18.  Blumhardt  LD,  Smith  PE,  Owen  L.  Electrocardiographic  ac-
companiments  of  temporal  lobe  epileptic  seizures.  Lancet. 
1986;1(8489):1051–6.

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 
   
36 

| 

 19.  van der Lende M, Surges R, Sander JW, Thijs RD. Cardiac ar-
rhythmias during or after epileptic seizures. J Neurol Neurosurg 
Psychiatry. 2016;87(1):69–74.

 20.  Ufongene  C,  El  Atrache  R,  Loddenkemper  T,  Meisel  C. 
Electrocardiographic changes associated with epilepsy beyond 
heart rate and their utilization in future seizure detection and 
forecasting methods. Clin Neurophysiol. 2020;131(4):866–79.

 21.  Surges R, Scott CA, Walker MC. Enhanced QT shortening and 
persistent  tachycardia  after  generalized  seizures.  Neurology. 
2010;74(5):421–6.

 22.  Stollberger C, Finsterer J. Evidence of cardiac ischemia during 
seizures  in  drug  refractory  epilepsy  patients.  Neurology. 
2004;62(7):1238–9; author reply 1239.

 23.  Lamberts  RJ,  Blom  MT,  Novy  J,  Belluzzo  M,  Seldenrijk  A, 
Penninx  BW,  et  al.  Increased  prevalence  of  ECG  markers  for 
sudden cardiac arrest in refractory epilepsy. J Neurol Neurosurg 
Psychiatry. 2015;86(3):309–13.

 24.  Myers  KA,  Sivathamboo  S,  Perucca  P.  Heart  rate  variability 
measurement in epilepsy: how can we move from research to 
clinical practice? Epilepsia. 2018;59(12):2169–78.

 25.  Poh M- Z, Loddenkemper T, Swenson NC, Goyal S, Madsen JR, 
Picard  RW.  Continuous  monitoring  of  electrodermal  activity 
during  epileptic  seizures  using  a  wearable  sensor.  Annu  Int 
Conf IEEE Eng Med Biol Soc. 2010;2010:4415–8.

 26.  Müngen  B,  Berilgen  MS,  Arikanoğlu  A.  Autonomic  nervous 
system  functions  in  interictal  and  postictal  periods  of  nonep-
ileptic psychogenic seizures and its comparison with epileptic 
seizures. Seizure. 2010;19(5):269–73.

 27.  Meisel C, Bailey KA. Identifying signal- dependent information 
about the preictal state: a comparison across ECoG, EEG and 
EKG using deep learning. EBioMedicine. 2019;45:422–31.
 28.  Gagliano  L,  Assi  EB,  Toffa  DH,  Nguyen  DK,  Sawan  M. 
Unsupervised  clustering  of  HRV  features  reveals  preictal 
changes in human epilepsy. Annu Int Conf IEEE Eng Med Biol 
Soc. 2020;2020:698–701.

 29.  Zulfiqar  U,  Jurivich  DA,  Gao W,  Singer  DH.  Relation  of  high 
heart  rate  variability  to  healthy  longevity.  Am  J  Cardiol. 
2010;105(8):1181–5.

 30.  Koenig  J.  Neurovisceral  regulatory  circuits  of  affective  resil-
ience  in  youth:  principal  outline  of  a  dynamic  model  of  neu-
rovisceral 
in  development.  Psychophysiology. 
2020;57(5):e13568.

integration 

 36.  Vieluf S, Amengual- Gual M, Zhang B, El Atrache R, Ufongene 
C, Jackson MC, et al. Twenty- four- hour patterns in electroder-
mal activity recordings of patients with and without epileptic 
seizures. Epilepsia. 2021;62(4):960–72.

 37.  Reinberg AE, Dejardin L, Smolensky MH, Touitou Y. Seven- day 
human biological rhythms: an expedition in search of their ori-
gin, synchronization, functional advantage, adaptive value and 
clinical relevance. Chronobiol Int. 2017;34(2):162–91.

 38.  Foster  RG,  Roenneberg  T.  Human  responses  to  the  geo-
lunar  cycles.  Curr  Biol. 

physical  daily,  annual  and 
2008;18(17):R784–R794.

 39.  Siegelová  J,  Cornélissen  G,  Havelková  A,  Dusek  J,  Vank  P, 
Dobsak  P.  Seven- day  ambulatory  blood  pressure  monitor-
ing:  circadian  and  circaseptan  rhythm  in  adults.  Brno,  Czech 
Republic:  Noninvasive  Methods  of  Cardiology,  Masaryk 
University; 2014. p. 109–24.

 40.  Halimeh  M,  Yang  Y,  Sheehan  T,  Vieluf  S,  Jackson  M, 
Loddenkemper  T,  et  al.  Wearable  device  assessments  of  anti-
seizure medication effects on diurnal patterns of electrodermal 
activity,  heart  rate,  and  heart  rate  variability.  Epilepsy  Behav. 
2022;129:108635.

 41.  Hennessy MJ, Tighe MG, Binnie CD, Nashef L. Sudden with-
drawal of carbamazepine increases cardiac sympathetic activity 
in sleep. Neurology. 2001;57(9):1650–4.

 42.  Lossius MI, Erikssen JE, Mowinckel P, Gulbrandsen P, Gjerstad 
L. Changes in autonomic cardiac control in patients with epi-
lepsy after discontinuation of antiepileptic drugs: a randomized 
controlled withdrawal study. Eur J Neurol. 2007;14(9):1022–8.
 43.  Critchley HD, Eccles J, Garfinkel SN. Interaction between cog-
nition,  emotion,  and  the  autonomic  nervous  system.  Handb 
Clin Neurol. 2013;117:59–77.

 44.  Thayer  JF,  Lane  RD.  A  model  of  neurovisceral  integration 
in  emotion  regulation  and  dysregulation.  J  Affect  Disord. 
2000;61(3):201–16.

 45.  Gianaros  PJ,  Wager  TD.  Brain- body  pathways  linking  psy-
chological  stress  and  physical  health.  Curr  Dir  Psychol  Sci. 
2015;24(4):313–21.

 46.  Cook  MJ,  O'Brien  TJ,  Berkovic  SF,  Murphy  M,  Morokoff  A, 
Fabinyi  G,  et  al.  Prediction  of  seizure  likelihood  with  a  long- 
term,  implanted  seizure  advisory  system  in  patients  with 
drug- resistant  epilepsy:  a  first- in- man  study.  Lancet  Neurol. 
2013;12(6):563–71.

 31.  Koenig  J,  Abler  B,  Agartz  I,  Åkerstedt  T,  Andreassen  OA, 
Anthony M, et al. Cortical thickness and resting- state cardiac 
function  across  the  lifespan:  a  cross- sectional  pooled  mega- 
analysis. Psychophysiology. 2021;58(7):e13688.

 47.  Blachut  B,  Hoppe  C,  Surges  R,  Elger  C,  Helmstaedter  C. 
Subjective seizure counts by epilepsy clinical drug trial partici-
pants are not reliable. Epilepsy Behav. 2017;67:122–7.

 48.  Fisher  RS.  Bad  information  in  epilepsy  care.  Epilepsy  Behav. 

 32.  Boucsein W, Fowles DC, Grimnes S, Ben- Shakhar G, Roth W, 
Dawson  ME,  et  al.  Publication  recommendations  for  electro-
dermal measurements. Psychophysiology. 2012;49(8):1017–34.
 33.  Hill LK, Hu DD, Koenig J, Sollers JJ, Kapuku G, Wang X, et al. 
Ethnic differences in resting heart rate variability: a systematic 
review and meta- analysis. Psychosom Med. 2015;77(1):16–25.

 34.  Vandewalle  G,  Middleton  B,  Rajaratnam  SMW,  Stone  BM, 
Thorleifsdottir  B,  Arendt  J,  et  al.  Robust  circadian  rhythm  in 
heart rate and its variability: influence of exogenous melatonin 
and photoperiod. J Sleep Res. 2007;16(2):148–55.

 35.  Black N, D'Souza A, Wang Y, Piggins H, Dobrzynski H, Morris 
G, et al. Circadian rhythm of cardiac electrophysiology, arrhyth-
mogenesis,  and  the  underlying  mechanisms.  Heart  Rhythm. 
2019;16(2):298–307.

2017;67:133–4.

 49.  Bergey  GK,  Morrell  MJ,  Mizrahi  EM,  Goldman  A,  King- 
Stephens  D,  Nair  D,  et  al.  Long- term  treatment  with  respon-
sive brain stimulation in adults with refractory partial seizures. 
Neurology. 2015;84(8):810–7.

 50.  Stirling  RE,  Grayden  DB,  D'Souza  W,  Cook  MJ,  Nurse  E, 
Freestone DR, et al. Forecasting seizure likelihood with wear-
able technology. Front Neurol. 2021;12:704060.

 51.  Weisdorf  S,  Duun- Henriksen  J,  Kjeldsen  MJ,  Poulsen  FR, 
Gangstad  SW,  Kjaer TW.  Ultra- long- term  subcutaneous  home 
monitoring  of  epilepsy- 490 days  of  EEG  from  nine  patients. 
Epilepsia. 2019;60(11):2204–14.

 52.  Kaongoen N, Choi J, Woo Choi J, Kwon H, Hwang C, Hwang 
G,  et  al.  The  future  of  wearable  EEG:  a  review  of  ear- EEG 

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 
 
|  37

technology  and  its  applications.  J  Neural  Eng.  2023;20(5). 
051002. https:// doi. org/ 10. 1088/ 1741- 2552/ acfcda

adult  patients  in  the  epilepsy  monitoring  unit.  Front  Neurol. 
2021;12:724904.

 53.  Beniczky  S,  Ryvlin  P.  Standards  for  testing  and  clinical  vali-
dation  of  seizure  detection  devices.  Epilepsia.  2018;59(Suppl 
1):9–13.

 54.  Beniczky S, Wiebe S, Jeppesen J, Tatum WO, Brazdil M, Wang 
Y,  et  al.  Automated  seizure  detection  using  wearable  devices: 
a  clinical  practice  guideline  of  the  International  League 
Against Epilepsy and the International Federation of Clinical 
Neurophysiology. Clin Neurophysiol. 2021;132(5):1173–84.
 55.  Ryvlin P, Cammoun L, Hubbard I, Ravey F, Beniczky S, Atienza 
D.  Noninvasive  detection  of  focal  seizures  in  ambulatory  pa-
tients. Epilepsia. 2020;61(Suppl 1):S47–S54.

 56.  Hubbard I, Beniczky S, Ryvlin P. The challenging path to devel-
oping a mobile health device for epilepsy: the current landscape 
and where we go from here. Front Neurol. 2021;12:740743.
 57.  Naganur  V,  Sivathamboo  S,  Chen  Z,  Kusmakar  S,  Antonic- 
Baker  A,  O'Brien  TJ,  et  al.  Automated  seizure  detection  with 
noninvasive  wearable  devices:  a  systematic  review  and  meta- 
analysis. Epilepsia. 2022;63(8):1930–41.

 58.  Li W, Wang G, Lei X, Sheng D, Yu T, Wang G. Seizure detection 
based on wearable devices: a review of device, mechanism, and 
algorithm. Acta Neurol Scand. 2022;146(6):723–31.

 59.  Esmaeili  B,  Vieluf  S,  Dworetzky  BA,  Reinsberger  C.  The  po-
tential  of  wearable  devices  and  mobile  health  applications 
in  the  evaluation  and  treatment  of  epilepsy.  Neurol  Clin. 
2022;40(4):729–39.

 60.  Beniczky  S,  Karoly  P,  Nurse  E,  Ryvlin  P,  Cook  M.  Machine 
learning  and  wearable  devices  of  the  future.  Epilepsia. 
2021;62(Suppl 2):S116–S124.

 61.  Seth  EA,  Watterson  J,  Xie  J,  Arulsamy  A,  Md  Yusof  HH, 
Ngadimon IW, et al. Feasibility of cardiac- based seizure detec-
tion and prediction: a systematic review of non- invasive wear-
able sensor- based studies. Epilepsia Open. 2023;9:41–59.
 62.  Meritam  Larsen  P,  Beniczky  S.  Non- electroencephalogram- 
based seizure detection devices: state of the art and future per-
spectives. Epilepsy Behav. 2023;148:109486.

 69.  Boon  P,  Vonck  K,  van  Rijckevorsel  K,  El  Tahry  R,  Elger  CE, 
Mullatti  N,  et  al.  A  prospective,  multicenter  study  of  cardiac- 
based  seizure  detection  to  activate  vagus  nerve  stimulation. 
Seizure. 2015;32:52–61.

 70.  Fisher RS, Afra P, Macken M, Minecan DN, Bagić A, Benbadis 
SR, et al. Automatic Vagus nerve stimulation triggered by ictal 
tachycardia:  clinical  outcomes  and  device  performance–the 
U.S. E- 37 trial. Neuromodulation. 2016;19(2):188–95.

 71.  Tang  J,  El  Atrache  R,  Yu  S,  Asif  U,  Jackson  M,  Roy  S,  et  al. 
Seizure  detection  using  wearable  sensors  and  machine  learn-
ing: setting a benchmark. Epilepsia. 2021;62(8):1807–19.
 72.  Yu S, El Atrache R, Tang J, Jackson M, Makarucha A, Cantley 
S, et al. Artificial intelligence- enhanced epileptic seizure detec-
tion by wearables. Epilepsia. 2023;64(12):3213–26.

 73.  Halimeh M, Jackson M, Vieluf S, Loddenkemper T, Meisel C. 
Explainable  AI  for  wearable  seizure  logging:  impact  of  data 
quality,  patient  age,  and  antiseizure  medication  on  perfor-
mance. Seizure. 2023;110:99–108.

 74.  Jahanbekam  A,  Baumann  J,  Nass  RD,  Bauckhage  C,  Hill  H, 
Elger  CE,  et  al.  Performance  of  ECG- based  seizure  detection 
algorithms  strongly  depends  on  training  and  test  conditions. 
Epilepsia Open. 2021;6(3):597–606.

 75.  Jeppesen  J,  Beniczky  S,  Fuglsang  Frederiksen  A,  Sidenius 
P,  Johansen  P.  Modified  automatic  R- peak  detection  algo-
rithm  for  patients  with  epilepsy  using  a  portable  electrocar-
diogram  recorder.  Annu  Int  Conf  IEEE  Eng  Med  Biol  Soc. 
2017;2017:4082–5.

 76.  Jeppesen  J,  Fuglsang- Frederiksen  A,  Johansen  P,  Christensen 
J, Wüstenhagen S, Tankisi H, et al. Seizure detection based on 
heart rate variability using a wearable electrocardiography de-
vice. Epilepsia. 2019;60(10):2105–13.

 77.  Jeppesen  J,  Fuglsang- Frederiksen  A,  Johansen  P,  Christensen 
J,  Wüstenhagen  S,  Tankisi  H,  et  al.  Seizure  detection  using 
heart rate variability: a prospective validation study. Epilepsia. 
2020;61(Suppl 1):S41–S46.

 63.  Vieluf  S,  El  Atrache  R,  Hammond  S,  Touserkani  FM, 
Loddenkemper T, Reinsberger C. Peripheral multimodal mon-
itoring  of  ANS  changes  related  to  epilepsy.  Epilepsy  Behav. 
2019;96:69–79.

 78.  Jeppesen J, Christensen J, Johansen P, Beniczky S. Personalized 
seizure  detection  using  logistic  regression  machine  learn-
ing  based  on  wearable  ECG- monitoring  device.  Seizure. 
2023;107:155–61.

 64.  Beniczky  S,  Arbune  AA,  Jeppesen  J,  Ryvlin  P.  Biomarkers  of 
seizure  severity  derived  from  wearable  devices.  Epilepsia. 
2020;61(Suppl 1):S61–S66.

 65.  Arends J, Thijs RD, Gutter T, Ungureanu C, Cluitmans P, Van 
Dijk J, et al. Multimodal nocturnal seizure detection in a res-
idential  care  setting:  a  long- term  prospective  trial.  Neurology. 
2018;91(21):e2010–e2019.

 66.  Van  Westrhenen  A,  Lazeron  RHC,  van  Dijk  JP,  Leijten  FSS, 
Thijs  RD,  Dutch  TeleEpilepsy  Consortium.  Multimodal  noc-
turnal  seizure  detection  in  children  with  epilepsy:  a  pro-
spective,  multicenter,  long- term,  in- home  trial.  Epilepsia. 
2023;64(8):2137–52.

 67.  Lazeron  RHC,  Thijs  RD,  Arends  J,  Gutter  T,  Cluitmans  P, 
Van  Dijk  J,  et  al.  Multimodal  nocturnal  seizure  detection:  do 
we  need  to  adapt  algorithms  for  children?  Epilepsia  Open. 
2022;7(3):406–13.

 68.  Onorati  F,  Regalia  G,  Caborni  C,  LaFrance  WC,  Blum  AS, 
Bidwell  J,  et  al.  Prospective  study  of  a  multimodal  convul-
sive  seizure  detection  wearable  system  on  pediatric  and 

 79.  Jeppesen J, Lin K, Melo HM, Pavei J, Marques JLB, Beniczky S, 
et al. Detection of seizures with ictal tachycardia, using heart 
rate variability and patient adaptive logistic regression machine 
learning methods: a hospital- based validation study. Epileptic 
Disord. 2024;26:199–208.

 80.  Jeppesen J, Christensen J, Mølgaard H, Beniczky S. Automated 
detection  of  focal  seizures  using  subcutaneously  implanted 
electrocardiographic device: a proof- of- concept study. Epilepsia. 
2023;64(Suppl 4):S59–S64.

 81.  Forooghifar F, Aminifar A, Cammoun L, Wisniewski I, Ciumas 
C,  Ryvlin  P,  et  al.  A  self- aware  epilepsy  monitoring  system 
for  real- time  epileptic  seizure  detection.  Mob  Netw  Appl. 
2019;27:677–90.

 82.  Glasstetter M, Böttcher S, Zabler N, Epitashvili N, Dümpelmann 
M, Richardson MP, et al. Identification of ictal tachycardia in 
focal  motor-   and  non- motor  seizures  by  means  of  a  wearable 
PPG sensor. Sensors (Basel). 2021;21(18):6017.

 83.  Vandecasteele  K,  De  Cooman  T,  Gu  Y,  Cleeren  E,  Claes  K, 
Paesschen  WV,  et  al.  Automated  epileptic  seizure  detection 

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License 
   
38 

| 

based  on  wearable  ECG  and  PPG  in  a  hospital  environment. 
Sensors (Basel). 2017;17(10):2338.

wearables: epilepsy monitoring outside the clinic. Front Neurol. 
2021;12:690404.

 84.  van  Andel  J,  Ungureanu  C,  Arends  J,  Tan  F,  Van  Dijk  J, 
Petkov G, et al. Multimodal, automated detection of nocturnal 
motor seizures at home: is a reliable seizure detector feasible? 
Epilepsia Open. 2017;2(4):424–31.

 85.  Poh M- Z, Loddenkemper T, Reinsberger C, Swenson NC, Goyal 
S, Sabtala MC, et al. Convulsive seizure detection using a wrist- 
worn  electrodermal  activity  and  accelerometry  biosensor. 
Epilepsia. 2012;53(5):e93–e97.

 97.  Baud MO, Proix T, Gregg NM, Brinkmann BH, Nurse ES, Cook 
MJ, et al. Seizure forecasting: bifurcations in the long and wind-
ing road. Epilepsia. 2023;64(Suppl 4):S78–S98.

 98.  Meisel  C,  Loddenkemper  T.  Seizure  prediction  and  interven-

tion. Neuropharmacology. 2020;172:107898.

 99.  Gregg  NM,  Pal  Attia T,  Nasseri  M,  Joseph  B,  Karoly  P,  Cui  J, 
et al. Seizure occurrence is linked to multiday cycles in diverse 
physiological signals. Epilepsia. 2023;64(6):1627–39.

 86.  Onorati  F,  Regalia  G,  Caborni  C,  Migliorini  M,  Bender  D, 
Poh  M- Z,  et  al.  Multicenter  clinical  assessment  of  improved 
wearable  multimodal  convulsive  seizure  detectors.  Epilepsia. 
2017;58(11):1870–9.

 100.  Meisel C, El Atrache R, Jackson M, Schubach S, Ufongene C, 
Loddenkemper  T.  Machine  learning  from  wristband  sensor 
data  for  wearable,  noninvasive  seizure  forecasting.  Epilepsia. 
2020;61(12):2653–66.

 87.  Böttcher  S,  Bruno  E,  Manyakov  NV,  Epitashvili  N,  Claes  K, 
Glasstetter  M,  et  al.  Detecting  tonic- clonic  seizures  in  multi-
modal biosignal data from wearables: methodology design and 
validation. JMIR Mhealth Uhealth. 2021;9(11):e27674.

 101.  Nasseri M, Pal Attia T, Joseph B, Gregg NM, Nurse ES, Viana 
PF,  et  al.  Ambulatory  seizure  forecasting  with  a  wrist- worn 
device  using  long- short  term  memory  deep  learning.  Sci  Rep. 
2021;11(1):21935.

 88.  Poh  M- Z,  Loddenkemper  T,  Reinsberger  C,  Swenson  NC, 
Goyal  S,  Madsen  JR,  et  al.  Autonomic  changes  with  sei-
zures  correlate  with  postictal  EEG  suppression.  Neurology. 
2012;78(23):1868–76.

 102.  Karoly  PJ,  Stirling  RE,  Freestone  DR,  Nurse  ES,  Maturana 
MI,  Halliday  AJ,  et  al.  Multiday  cycles  of  heart  rate  are  asso-
ciated  with  seizure  likelihood:  an  observational  cohort  study. 
EBioMedicine. 2021;72:103619.

 89.  Karoly  PJ,  Rao VR,  Gregg  NM, Worrell  GA,  Bernard  C,  Cook 
MJ, et al. Cycles in epilepsy. Nat Rev Neurol. 2021;17(5):267–84.
 90.  Karoly  PJ,  Freestone  DR,  Boston  R,  Grayden  DB,  Himes  D, 
Leyde  K,  et  al.  Interictal  spikes  and  epileptic  seizures:  their 
relationship  and  underlying  rhythmicity.  Brain.  2016;139(Pt 
4):1066–78.

 91.  Baud MO, Kleen JK, Mirro EA, Andrechak JC, King- Stephens 
D, Chang EF, et al. Multi- day rhythms modulate seizure risk in 
epilepsy. Nat Commun. 2018;9(1):88.

 92.  Maturana MI, Meisel C, Dell K, Karoly PJ, D'Souza W, Grayden 
DB, et al. Critical slowing down as a biomarker for seizure sus-
ceptibility. Nat Commun. 2020;11(1):2172.

 93.  Meisel  C,  Schulze- Bonhage  A,  Freestone  D,  Cook  MJ, 
Achermann  P,  Plenz  D.  Intrinsic  excitability  measures  track 
antiepileptic  drug  action  and  uncover  increasing/decreasing 
excitability over the wake/sleep cycle. Proc Natl Acad Sci USA. 
2015;112(47):14694–99.

 94.  Meisel  C,  Kuehn  C.  Scaling  effects  and  spatio- temporal 
in  epileptic  seizures.  PLoS  One. 

multilevel  dynamics 
2012;7(2):e30371.

 95.  Kuhlmann  L,  Lehnertz  K,  Richardson  MP,  Schelter  B,  Zaveri 
HP. Seizure prediction – ready for a new era. Nat Rev Neurol. 
2018;14(10):618–30.

 96.  Brinkmann  BH,  Karoly  PJ,  Nurse  ES,  Dumanis  SB,  Nasseri 
M,  Viana  PF,  et  al.  Seizure  diaries  and  forecasting  with 

 103.  Billeci  L,  Marino  D,  Insana  L,  Vatti  G,  Varanini  M.  Patient- 
specific  seizure  prediction  based  on  heart  rate  variabil-
ity  and  recurrence  quantification  analysis.  PLoS  One. 
2018;13(9):e0204339.

 104.  Yamakawa  T,  Miyajima  M,  Fujiwara  K,  Kano  M,  Suzuki  Y, 
Watanabe Y, et al. Wearable epileptic seizure prediction system 
with machine- learning- based anomaly detection of heart rate 
variability. Sensors (Basel). 2020;20(14):3987.

 105.  Hegarty- Craver M, Kroner BL, Bumbut A, DeFilipp SJ, Gaillard 
WD, Gilchrist KH. Cardiac- based detection of seizures in chil-
dren with epilepsy. Epilepsy Behav. 2021;122:108129.

 106.  Marinescu  RV,  Eshaghi  A,  Alexander  DC,  Golland  P. 
BrainPainter:  a  software  for  the  visualisation  of  brain  struc-
tures,  biomarkers  and  associated  pathological  processes. 
Multimodal  Brain  Image  Anal  Math  Found  Comput  Anat 
(2019). 2019;11846:112–20.

How to cite this article: Miron G, Halimeh M, 
Jeppesen J, Loddenkemper T, Meisel C. Autonomic 
biosignals, seizure detection, and forecasting. 
Epilepsia. 2025;66(Suppl. 3):25–38. https://doi.
org/10.1111/epi.18034

MIRON et al. 15281167, 2025, S3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/epi.18034 by Bibl. der Universitat zu Koln, Wiley Online Library on [21/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
