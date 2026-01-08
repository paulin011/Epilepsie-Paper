# Singh Rathore et al. - 2024 - Development of a Multimodal Machine Learning Model for Seizure Detection Using Wearable Devices

7
1
2
5
9
8
0
1
.
4
2
0
2
.
7
8
3
3
6
N
2
C
A
C

I
/
9
0
1
1
.
0
1
:
I

O
D

|

E
E
E
I

4
2
0
2
©
0
0

.

1
3
$
/
4
2
/
6
-
1
8
6
5
-
3
0
5
3
-
8
-
9
7
9

|

)

N
2
C
A
C

I
(

g
n
i
k
r
o
w
t
e
N
d
n
a

n
o
i
t
a
c
i
n
u
m
m
o
C

,
g
n
i
t
u
p
m
o
C
n
i

s
e
c
n
a
v
d
A
n
o

e
c
n
e
r
e
f
n
o
C

l
a
n
o
i
t
a
n
r
e
t
n
I

t
s
1

4
2
0
2

2024 1st International Conference on Advances in Computing, Communication & Networking (ICAC2N) 

Development of a Multimodal Machine Learning 
Model for Seizure Detection Using Wearable 
Devices 

Saurabh Pratap Singh Rathore 
Dept. of Management ICAPSR 
New Delhi, India 
rathoresaurabhsingh@gmail.com 

Sumedha Magotra 
Dept. of Computer Science Engineering 
Chandigarh  University Chandigarh, 
India 
sumedhamagotra21@gmail.com 

Sruthy K V 
Dept. of Computer Science & Engineering 
Dhanalakshmi Srinivasan  college 
Coimbatore, India 
kvsruthy1992@gmail.com 

Sharma Sonu Kumar 
Dept. of Comp. Eng & Applications 
Mangalayatan  University Aligarh, 
India 
sharma.kumar@mangalayatan.edu.in 

Gaganpreet kaur 
Lovely Professional  University 
Punjab, India 

Sailendra Singh 
Dept. of  Computer 
Science J.S. University 
Shikohabad, India 
ssjsuni88@gmail.com 

in  order 

to  uncover 

storing  physiological  signals  like  EDA  &  ACC,  which  can 
help  identify  the  occurrence  of  seizures.  A large dataset of 
labeled  seizure  and  non-seizures  should  be  used  to  train  the 
model 
the  complex  patterns  and 
characteristics  associated  with  seizures.  High  sensitivity  and 
specificity should be incorporated into the system to minimize 
false  alarms  and  missed  detections.  It  can  be  challenging  to 
accurately  differentiate  a  seizure  from  other  behaviors  that 
might  resemble  one,  such  as  moving,  sleeping,  or  exercising, 
when developing a machine learning model. In the conclusion 
of  the  article,  opinions  regarding  wearable  multifunctional 
sensing technology and its possible uses in precision medicine 
are discussed. 

Abstract—This research explores the transformative potential of 
wearable  devices  designed  to  automatically  detect  &   predict 
epileptic seizures, offering continuous monitoring & early detection 
capabilities.  The  study  focuses  on  developing  a  machine  learning 
model  tailored  for  seizure  detection  in  such  devices,  leveraging 
multimodal  sensors  such  as  Electrodermal  Activity  (EDA)  &  
Accelerometer (ACC).  By measuring skin resistance and identifying 
irregular  heartbeats,  which  are  signs  of  upcoming  seizures,  these 
sensors  allow  for  precise  seizure  detection.  The  study  intends  to 
demonstrate  the  effectiveness  of  this  machine  learning  model  in 
wearable technology with the goal of improving patient outcomes and 
seizure management. 

Index  Terms—Seizure,  Electrodermal  Activity 

(EDA), 

Accelerometer (ACC),  Classifiers, Electroencephalogram (EEG). 

I. INTRODUCTION 

tasks 

Identifying  a  seizure  and 

Approximately  50  million  people  worldwide  suffer  from 
epileptic  seizures. 
reacting 
appropriately to prevent harm and save lives is one of the most 
difficult 
in  epileptic  seizures.  Therefore,  a  key 
component  of  seizure  treatment  is  seizure  detection  and 
prediction.  However,  conventional  techniques  like  employing 
an EEG or video EEG to identify seizures are frequently costly 
and  impractical  for  daily  use.  Therefore,  creating  a  wearable 
gadget with a machine learning model could revolutionize the 
way  that  epilepsy  is  treated.  This  research  paper  seeks  to 
address  the  accurate  detection  of  an  onset  seizure  using  a 
machine  learning  model.  The  model  must  be  trained  using 
sensor  data  obtained  from  wearable  devices.  The  system 
should be capable of collecting and 

979-8-3503-5681-6/24/$31.00©2024 IEEE 

Fig. 1. Use Case Diagram 

1422 
Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on January 05,2026 at 11:18:41 UTC from IEEE Xplore.  Restrictions apply. 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
2024 1st International Conference on Advances in Computing, Communication & Networking (ICAC2N) 

II. LITERATURE SURVEY 

Alazzam et al. (2021) discuss a smart healthcare system that 
integrates  IoT  &  machine  learning  for  continuous  patient 
monitoring.  Their  work  contributes  to  the  growing  field  of 
remote  health  monitoring,  combining  real-time  data  with  AI- 
driven  analytics [1].  Sharma & Kaushik (2023)  explore senti- 
ment analysis techniques applied to  Twitter data, highlighting 
methods  for  uncovering  user  emotions  &  opinions,  contribut- 
ing  to  social  media  analytics  &  user  behavior  modeling  [2]. 
Rosales  et  al.  (2019)  propose  a  smart  stress  detection  system 
using  physiological  data  &  machine  learning,  advancing  re- 
search  on  emotion  sensing  &  stress  management in  wearable 
technology  applications  [3].  Rathore  et  al.  (2024)  present  an 
innovative  delivery  management  solution  utilizing  smart 
technologies,  contributing  to  the  logistics  &  e-commerce 
sectors  by  optimizing  delivery  efficiency  through  real-time 
tracking  &   data  analysis  [4].  Tang  et  al.  (2021)  establish a 
benchmark  for  seizure  detection  using  wearable  sensors  & 
learning,  marking  an  advancement  in  medical 
machine 
technology  for  epilepsy  management  through  non-invasive 
monitoring systems [5]. Halimeh et al. (2022) investigate how 
wearable devices can monitor antiseizure medication effects on 
physiological parameters, providing insights into personalized 
treatment  &  enhancing  patient  care  in  epilepsy  management 
[6]. Tabasum et al. (2022) explore microfluidic e-skin sensors 
for  real-time  health  monitoring,  contributing  to  the  field  of 
wearable  sensors  &  bioelectronics  for  continuous  health 
assessment, particularly for stress & hydration levels [7]. 

Farooq et al. (2022) review machine learning techniques for 
seizure  detection,  summarizing  various  algorithms  &  their 
applications,  providing  valuable  insights  for  researchers  & 
developers in the field of medical AI [15]. Chen et al. (2009) 
study the effects of seizures during pregnancy on women with 
epilepsy,  offering  important  clinical  insights  into  mater-  nal 
health  &  pregnancy  management  for  epileptic  patients  [16]. 
Beniczky  et  al.  (2021)  discuss  clinical  guidelines  for 
automated seizure detection using wearable devices, advancing 
epilepsy  care  through  continuous  monitoring  &  improving 
seizure  management  in  clinical  practice  [17].  Wang  et  al. 
(2024)  introduce  a  dual-stream  neural  network  for  epileptic 
seizure detection, advancing the use of multimodal data to en- 
hance  detection accuracy & real-time monitoring for  epilepsy 
patients [18]. Sikarwar et al. (2023) focus on IoT-driven solu- 
tions to optimize parking management in smart environments, 
contributing  to  the  development  of  smart  city  technologies 
&  urban  mobility  solutions  [19].  Rathore  et  al.  (2023)  apply 
Recurrent Neural Networks (RNN) for customer segmentation 
in  banking,  enhancing  personalized  marketing  &  customer 
service  strategies  through  advanced  machine  learning  tech- 
niques  [20].  Sharma  et  al.  (2023) propose  a  methodology for 
partitioning  customers  using  K-Means  clustering  &  the  RFM 
model,  contributing  to  customer-centric  revenue  strategies  & 
marketing optimization in  business  intelligence [21].  Kaushik 
et  al.  (2023)  tackle  hate  speech  detection  using  ensemble 
learning  &   Long  Short-Term  Memory  (LSTM)  networks, 
enhancing real-time content moderation in smart environments 
& digital platforms [22]. 

studies  by 

leveraging  hybrid  deep 

Munch  Nielsen  et  al.  (2022)  propose  a  multi-modal 
wearable  seizure  detection  system,  combining  various  sensor 
technologies  to  improve  accuracy  in  detecting  seizures  & 
enhancing  epilepsy  management  through  wearable  medical 
devices  [8].  Kaushik  et  al.  (2024)  present  a  deep  learning-
based  approach 
Indian  music, 
to  classify  &   predict 
contributing  to  the  intersection  of  AI,  music  theory,  &  
learning 
cultural 
techniques  [9].  Zeng  et  al.  (2022)  review  multi-functional 
wearable sensors used in healthcare, emphasizing their role in 
real-time  health  monitoring  &  the  integration  of  diverse 
sensing  technologies  for  improved  diagnosis  &  personalized 
care  [10].  Urbina  Fredes  et  al.  (2024)  propose  wavelet-based 
analysis  for  improving  seizure  detection  accuracy  through 
EEG  signal  processing,  advancing  the  use  of  computational 
in  epilepsy  monitoring  &   management  [11]. 
methods 
Majumder et  al.  (2019) design an  energy-efficient IoT  system 
to  predict  cardiac  arrest,  con- tributing  to  the  development  of 
smart  health  devices  focused on early detection & prevention 
of critical medical events [12].  Sarmast  et  al.  (2020)  provide 
an  overview  of  seizure & epilepsy  classification, addressing 
current 
for 
improving  diagnostic  accuracy  &  treatment  strategies  in 
neurology  [13].  Bornoiu  &  Grig-  ore  (2013)  explore  feature 
extraction 
techniques  for  stress  detection,  focusing  on 
physiological  signals,  &  contribute  to  the  development  of 
wearable systems for monitoring mental health [14]. 

limitations  &  offering 

recommendations 

III. PROPOSED SYSTEM 

The  proposed  solution  leverages  a  machine  learning  model  to 
accurately  detect  seizures  in  epileptic  patients.  This  system 
employs  wearable  sensors 
to  collect  physiological  data, 
including  skin  resistance,  mobility,  heart  rate,  and  other 
variables  [23].  The  main  goal  is  to  create  a  very  accurate  and 
sensitive  model  that  can  identify  seizures  in  real  time.  To  do 
this, a sizable labeled dataset comprising both seizure and non-
seizure  cases  must  be  used  to  train  the  model  in  order  to  find 
intricate  patterns  and  characteristics  linked  to  seizures.  A  key 
focus of the study is minimizing the false alarm rate  (FAR) to 
enhance the model’s accuracy [24]. 
Developing  a  wearable  seizure  detection  system  presents 
several technical challenges: 
Data  Collection:  Acquiring  high-quality  sensor  data  in  real-
world  scenarios  can  be  difficult,  as  sensors  must  be 
comfortable,  unobtrusive,  and  capable  of  accurately  capturing 
critical information. 
Data  Analysis:  Extracting  meaningful  features  to  identify 
seizure events requires advanced signal processing and machine 
learning techniques due to the complexity of seizure patterns. 
Classification:  Determining  whether  a  seizure  is  occurring 
based on extracted features is challenging due to the variability 
in  seizure  manifestations,  requiring  precise  and  reliable 
machine learning classifiers. 

1423 
Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on January 05,2026 at 11:18:41 UTC from IEEE Xplore.  Restrictions apply. 

 
 
 
 
 
 
2024 1st International Conference on Advances in Computing, Communication & Networking (ICAC2N) 
7.  Multi-Layer Perceptron (MLP) 

Real-Time Functionality: The system must operate in real-time, 
sending immediate alerts upon seizure detection. This demands 
highly  efficient  and  optimized  data  processing  algorithms  for 
both speed and accuracy [25]. 
This  approach  provides  a  foundation  for  creating  an  effective 
seizure detection system tailored for real-world use. 

MLP,  a  neural  network  with  multiple 
layers, 
transforms  input  dimensions  into  desired  outputs. 
Implemented using TensorFlow, it effectively handles 
complex datasets. 

This approach ensures accurate classification by leveraging 
diverse  machine  learning  techniques  tailored  to  the 
dataset’s characteristics. 

V. RESULT 

This  study  used  multimodal  data  gathered  from  wearable 
learning 
to  assess  how  well  various  machine 
devices 
algorithms  detected  seizures.  Logistic  Regression,  Support 
Vector  Machine,  K-Nearest  Neighbors,  Naive  Bayes,  and 
Multilayer  Perceptron  were  among  the  algorithms  evaluated. 
Metrics like accuracy, precision, recall, and F-score were used 
to  compare  performance.  The  dataset  consisted  of  raw, 
unlabeled  data  with  approximately  3.2  million  data  points 
recorded  over  six  hours  from  a  single  patient.  This  data  was 
divided  into  smaller  segments  of  25,000  data  points  and 
further split into training and testing modules. 

A significant challenge in this research was the data labeling 
process,  which  involved  identifying  erroneous  values  and 
analyzing sensor signal fluctuations. One notable issue was the 
presence  of  highly  correlated  features,  particularly  the  "acc 
magnitude"  feature.  To  mitigate  errors,  this  feature  was 
excluded  from  the  dataset.  After  its  removal,  the  remaining 
features were used to evaluate the models. Furthermore, tree-
based  classification  methods  were  tested  but  resulted  in 
overfitting  due  to  the  high  levels  of  noise  in  the  data.  These 
insights  emphasize  the  importance  of  data  preprocessing  and 
feature  selection  in  achieving  robust  performance  for  seizure 
detection using machine learning techniques. 

VI. CONCLUSION 
The  MLP  classifier  demonstrated  superior  performance, 
achieving  an  accuracy  of  97.4%,  precision  of  94.8%,  recall  of 
96.8%,  and  an  F-score  of  95.6%.  Logistic  Regression  also 
performed  well,  with  accuracy,  precision,  recall,  and  F-score 
values  of  97.2%,  94.8%,  95.9%,  and  95.3%,  respectively.  The 
Support  Vector  Machine  (SVM)  algorithm  achieved  high 
accuracy  (97.2%)  and  recall  (95.6%)  but  slightly  lower 
precision (94.7%), resulting in an F-score of 95.2%. In contrast, 
K-Nearest  Neighbors 
performed 
comparatively  worse,  with  accuracy  scores  of  96.3%  and 
96.6%, respectively, making them the least effective methods in 
this analysis. 

and  Naive  Bayes 

TABLE I 
PE R F O R M A N C E  ON  MU LT I M O DA L  DATA S E T 

Machine Learning Algorithms  Accuracy  Precision  Recall 
95.9% 
Logistic Regression 
95.6% 
Support Vector Machine 
92.3% 
K-Nearest Neighbors 
97.9% 
Naive Bayes 
96.5% 
Multilayer Perceptron 

94.8% 
94.7% 
94.6% 
92% 
94.8% 

97.2% 
97.2% 
96.3% 
96.6% 
97.4% 

F Score 
95.3% 
95.2% 
93.4% 
94.6% 
95.6% 

(HR),  blood  volume  pressure 

IV. METHODOLOGY 
Pandas,  NumPy,  Matplotlib,  and  Seaborn  were  among  the 
necessary  libraries  imported  in  order  to  analyze  the 
dataset. The dataset was taken out of a CSV file and put 
into  a  variable.  Twenty-five  thousand  rows  were  taken 
out  of  the  raw  dataset.  Features  including  heart  rate 
variability 
(BVP), 
electrodermal activity (EDA), and accelerometery (ACC: 
x,  y,  z,  magnitude)  were  included  in  the  multimodal 
dataset.  In  order  to  replace  or  fix  null  and  incorrect 
values, data cleaning was done. While trends in EDA and 
HR  were  displayed  graphically,  a  strong  correlation  was 
noted  in  the  ACC  values.  Rows  with  values  below  the 
thresholds were designated as 0, and the remaining rows 
were designated as 1. Training and testing sets were then 
created  from  the  dataset.  The  data  was  analyzed  using 
imported  machine  learning  algorithms,  which  produced 
performance  metrics  and  ROC  curves.  Classification 
Algorithms Used: 
1.  Logistic Regression 

Logistic  regression  predicts  categorical  dependent 
variables  based  on  independent  variables,  outputting 
probabilities  between  0  and  1.  The  regression  curve 
provides 
the 
likelihoods, 
occurrence of seizures. 
2.  Random Forest Classifier 

such  as  predicting 

Random Forest builds a forest by combining multiple 
decision  trees.  The  trees  are  constructed  using 
randomly  selected  subsets  of  training  data,  and 
predictions are made by aggregating outputs from all 
trees. 

3.  Gradient Boosting Classifier 

Gradient  Boosting  combines  weak  predictors  to 
create  a  stronger  model.  Each  predictor  corrects  the 
errors  of  its  predecessor,  enhancing  the  overall 
accuracy. 

4.  Support Vector Machine (SVM) 
identifies  a  hyperplane 

SVM 
to  separate  n-
dimensional  space  into  classes,  enabling  accurate 
classification of new datasets. Support vectors are the 
data points used to define this hyperplane. 

5.  K-Nearest Neighbors (KNN) 

KNN  assigns  new  data  points  to  the  most  similar 
category  based  on  the  proximity  of  K  nearest 
neighbors.  The  Euclidean  distance  is  calculated  to 
determine  similarity,  and  classification  is  based  on 
the majority of neighboring data points. 

6.  Gaussian Naïve Bayes (GNB) 

GNB  applies  Bayes'  Theorem  to  predict  an  object's 
likelihood.  It  calculates  probabilities  of  features, 
constructs  likelihood  tables,  and  computes  posterior 
probabilities to classify data points. 

1424 
Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on January 05,2026 at 11:18:41 UTC from IEEE Xplore.  Restrictions apply. 

 
 
 
 
 
 
 
 
 
 
2024 1st International Conference on Advances in Computing, Communication & Networking (ICAC2N) 

REFERENCES 

[1]  M.  B.  Alazzam,  F.  Alassery,  &  A.  Almulihi,  “[Retracted]  A  Novel 
Smart Healthcare Monitoring System Using Machine Learning & the 
Internet  of  Things,”  Wireless  Communications  &  Mobile 
Computing,  vol.  2021,  no.  1.  Wiley, 
Jan.  2021.  doi: 
10.1155/2021/5078799. 

[2]  Sharma  T.  &  Kaushik  P.(2023).  Leveraging  Sentiment  Analysis  for 
Twit- ter Data to Uncover User Opinions & Emotions. International 
in  Computing  & 
Journal  on  Recent  &  Innovation  Trends 
Communication 
162–169. 
https://doi.org/10.17762/ijritcc.v11i8s.7186 

11(8s) 

Fig. 2. ROC Curve of MLP 

Fig. 3. ROC Curve of Logistic Regression 

Fig. 4. Performance Metrics 

These  results  suggest  that  the  MLP  classifier  can  handle 
multimodal  datasets  and  outperforms  other  classifiers 
assessed  in  this  work.  The  MLP  classifier  performs  well  in 
classification  because  it  can  manage  non-linear  interactions 
between  the  target  variable  and  the  features,  which  are 
crucial  in  multimodal  datasets.  These  results  suggest  that 
machine  learning  algorithms  can  effectively  detect  seizures 
using  data  from  wearable  devices.  Wearable  seizure 
detection  systems  would  benefit  from 
the  Multilayer 
Perceptron  and  Logistic  Regression  algorithms,  which 
showed the best results. More research is needed to evaluate 
these  algorithms'  performance  on  bigger  and  more  diverse 
datasets  and  to  look  at  the  practicality  and  usability  of 
wearable 
real-time  seizure  detection 
systems in clinical settings. 

technology-based 

[3]  M.  A.  Rosales,  A.  A.  Bandala,  R.  R.  Vicerra  &  E.  P. 
Dadios,”Physiological-Based  Smart  Stress  Detector  using  Machine 
Learning Algorithms,” 2019 IEEE 11th International Conference on 
Humanoid, 
Technology, 
Communication  &  Control,  Environment,  &  Management  ( 
HNICEM 
doi: 
),  Laoag,  Philippines, 
10.1109/HNICEM48295.2019.9073355. 

Nanotechnology, 

Information 

2019, 

1-6, 

pp. 

[4] S. P. S. Rathore, P. Kaushik, M. Poonia, S. S. Sikarwar, D. Singh, and 
D.  Jain,  ’Ease  Delivery:  A  Next-Gen  Delivery  Management 
Solution,’ 

2024  IEEE  International  Conference  on  Interdisciplinary  Approaches  in 
Technology  &  Management  for  Social  Innovation  (IATMSI), 
Gwalior, 
doi: 
India, 
10.1109/IATMSI60426.2024.10503239. 

2024, 

1-6, 

pp. 

[5]  J.  Tang  et  al.,  “Seizure  detection  using  wearable  sensors  &  machine 

learning: Setting a benchmark,” Epilepsia, vol. 62, no. 8. Wiley, pp. 

1807–1819, Jul. 15, 2021. doi: 10.1111/epi.16967. 
[6]  M.  Halimeh  et  al.,  “Wearable  device  assessments  of  antiseizure 
medica-  tion  effects  on  diurnal  patterns  of  electrodermal  activity, 
heart rate, & heart rate variability,” Epilepsy & Behavior, vol. 129. 
Elsevier 
doi: 
108635, 
BV, 
10.1016/j.yebeh.2022.108635. 

2022. 

Apr. 

p. 

[7] H. Tabasum, N. Gill, R. Mishra, & S. Lone, “Wearable microfluidic- 
based e-skin sweat sensors,” RSC Advances, vol. 12, no. 14. Royal 
(RSC),  pp.  8691–8707,  2022.  doi: 
Society  of  Chemistry 
10.1039/d1ra07888g. 

[8] J. Munch Nielsen, I. C. Zibrandtsen, P. Masulli, T. Lykke Sørensen, T. 
S.  Andersen,  &  T.  Wesenberg  Kjær,  “Towards  a  wearable  multi- 
modal seizure detection system in epilepsy: A pilot study,” Clinical 
Neurophysiology, vol. 136. Elsevier BV, pp. 40–48, Apr. 2022. doi: 
10.1016/j.clinph.2022.01.005. 

[9]  P.  Kaushik,  S.  P.  Singh  Rathore,  K.  Chahal,  S.  Saraf,  G.  Singh 
Chauhan,  &  P.  Kumar,  ’RhythmQuest:  Unifying  Indian  Music 
Classification & Prediction with Hybrid Deep Learning Techniques,’ 
2024 IEEE International Conference on Interdisciplinary Approaches 
in  Technology  &  Management  for  Social  Innovation  (IATMSI), 
doi: 
India, 
Gwalior, 
10.1109/IATMSI60426.2024.10503056. 

2024, 

1-6, 

pp. 

[10]  X.  Zeng,  H.T.  Deng,  D.L.  Wen,  Y.Y.  Li,  L.  Xu,  &  X.S.  Zhang, 
“Wearable  Multi-Functional  Sensing  Technology  for  Healthcare 
Smart Detection,” Micromachines, vol. 13, no. 2. MDPI AG, p. 254, 
Feb. 02, 2022. doi: 10.3390/mi13020254. 

[11]  S.  Urbina  Fredes,  A.  Dehghan  Firoozabadi,  P.  Adasme,  D.  Zabala 
Blanco,  P.  Palacios  Ja´tiva,  &  C.  Azurdia-Meza,  “Enhanced 
Epileptic Seizure Detection through Wavelet-Based Analysis of EEG 
Signal Processing,” Applied Sciences, vol. 14, no. 13. MDPI AG, p. 
5783, Jul. 02, 2024. doi: 10.3390/app14135783. 

[12] A. J. A. Majumder, Y. A. ElSaadany, R. Young, & D. R. Ucci, “An 
Energy  Efficient  Wearable  Smart  IoT  System  to  Predict  Cardiac 
Arrest,”  Advances  in  Human-Computer  Interaction,  vol.  2019. 
Hindawi 
doi: 
1–21, 
10.1155/2019/1507465. 

Limited, 

2019. 

Feb. 

12, 

pp. 

[13] S. T. Sarmast, A. M. Abdullahi, & N. Jahan, “Current Classification 
of  Seizures  &  Epilepsies:  Scope,  Limitations  &  Recommendations 
for  Future  Action,”  Cureus.  Springer  Science  &  Business  Media 
LLC, Sep. 20, 2020. doi: 10.7759/cureus.10549. 

[14]  I.  V.  Bornoiu  &  O.  Grigore,  ”A  study  about  feature  extraction  for 
stress detection,” 2013 8TH INTERNATIONAL SYMPOSIUM ON 
ADVANCED TOPICS IN ELECTRICAL ENGINEERING (ATEE), 
Bucharest, 
doi: 
10.1109/ATEE.2013.6563421. 

Romania, 

2013, 

1-4, 

pp. 

[15] M. S. Farooq, A. Zulfiqar, & S. Riaz, “A review on Epileptic Seizure 
arXiv. 

using  Machine 

Learning,” 

2022, 

Detection 
doi:10.48550/ARXIV.2210.06292. 

1425 
Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on January 05,2026 at 11:18:41 UTC from IEEE Xplore.  Restrictions apply. 

[16]  Y.H.  Chen,  H.Y.  Chiou,  H.C.  Lin,  &  H.L.  Lin,  “Affect  of  Seizures 
in  Women  With 

During  Gestation  on  Pregnancy  Outcomes 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
2024 1st International Conference on Advances in Computing, Communication & Networking (ICAC2N) 

Epilepsy,” Archives of Neurology, vol. 66, no. 8. American Medical 
Association 
doi: 
Aug. 
10.1001/archneurol.2009.142. 

(AMA), 

2009. 

01, 

[17] S. Beniczky et al., “Automated seizure detection using wearable de- 
vices:  A  clinical  practice  guideline  of  the  International  League 
Against  Epilepsy  &  the  International  Federation  of  Clinical 
Neurophysiology,”  Clinical  Neurophysiology,  vol.  132,  no.  5. 
Elsevier 
doi: 
BV, 
10.1016/j.clinph.2020.12.009. 

1173–1184,  May 

2021. 

pp. 

[18] B. Wang, Y. Xu, S. Peng, H. Wang, & F. Li, “Detection Method of 
Epileptic  Seizures  Using  a  Neural  Network  Model  Based  on 
Multimodal Dual-Stream Networks,” Sensors, vol. 24, no. 11. MDPI 
AG, p. 3360, May 24, 2024. doi: 10.3390/s24113360. 

[19] S. Sikarwar, M. F. Afzal, S. Kumar, S. Kumar, S. P. S. Rathore & G. 
Kaur,  ”Improving  Parking  Management:  Leveraging  IoT 
to 
Empower  Smart  Environments,”  2023  International  Conference  on 
India,  2024,  pp.  1-7, 
(ICSD),  Dehradun, 
Smart  Devices 
doi:10.1109/ICSD60021.2024.10751449. 

[20] S. P. S. Rathore, N. Anute, H. Raje, D. S. Ubale, A. P. Narkhede & 
P.Kaushik,  ”Segmentation  Study  on  Bank  Customers  Based  on 
RNN,” 

2023 International Conference on Smart Devices (ICSD), Dehradun, India, 

2024, pp. 1-6, doi: 10.1109/ICSD60021.2024.10751183. 

[21] V. Sharma, P. Agarwal, H. Y. Shaikh, R. M. Lenka, S. K.Manjhi & 
R.  Rathore,  ”Smart  Next-Generation  Revenue  Growth:  A 
Methodology  for  Partitioning  Customers  Utilizing  the  K-Means 
Algorithm & RFM Model,” 2023 International Conference on Smart 
Devices (ICSD), Dehradun, India, 2024, pp. 1-6, doi: 

10.1109/ICSD60021.2024.10751627. 
[22] P. Kaushik, R. Rohilla, P. Walia, S. Shankar, M. M. Kaushik & T.S. 
Gupta,  ”Confronting  Hate  Speech  in  SMART  Environments:  An 
Approach 
that  Uses  Ensemble  Learning  &  LSTM,”  2023 
International Conference on Smart Devices (ICSD), Dehradun, India, 
2024, pp. 1-6, doi: 10.1109/ICSD60021.2024.10751441.  

[23] Kaushik, P., Rathore, S. P. S., Rathore, R., & Sikarwar, S. S. (2024). 
Big Data-Powered Analytics for Fortifying Virtualized Infrastructure 
Security  in  the  Cloud.  In  Communications  in  Computer  and 
Information  Science  (pp.  156–168).  Springer  Nature  Switzerland. 
https://doi.org/10.1007/978-3-031-80778-7_12 

[24] Kaushik, P., Rathore, S. P. S., Rathore, R., & Sikarwar, S. S. (2024). 
Data  Analytics  Augmented  by  AI  in  the  Realm  of  6G  Wireless 
Communication.  In  Communications  in  Computer  and  Information 
Science 
Switzerland. 
144–155). 
https://doi.org/10.1007/978-3-031-80778-7_11 

Springer  Nature 

(pp. 

[25] Rathore, S. P. S., Kaushik, P., Rathore, R., & Sikarwar, S. S. (2024). 
Predictive Analytics for Inventory Management in Multi-Vendor E-
Commerce.  In  Communications  in  Computer  and  Information 
Science 
Switzerland. 
132–143). 
https://doi.org/10.1007/978-3-031-80778-7_10 

Springer  Nature 

(pp. 

1426 
Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on January 05,2026 at 11:18:41 UTC from IEEE Xplore.  Restrictions apply.
