# Borujeny et al. - 2013 - Detection of Epileptic Seizure Using Wireless Sensor Networks

Original Article

www.jmss.mui.ac.ir

Detection of Epileptic Seizure Using Wireless Sensor Networks

Golshan Taheri Borujeny, Mehran Yazdi, Alireza Keshavarz‑Haddad, Arash Rafie Borujeny
Department of Communication and Electronic Engineering, School of Electrical and Computer Engineering, Shiraz University, Shiraz, Iran

Submission: 18‑11‑2012 

Accepted: 25‑03‑2013

A B S T R A C T

The monitoring of epileptic seizures is mainly done by means of electroencephalogram (EEG) monitoring. Although this method is 
accurate, it is not comfortable for the patient as the EEG‑electrodes have to be attached to the scalp which hampers the patient’s 
movement. This makes long‑term home monitoring not feasible. In this paper, the aim is to propose a seizure detection system based 
on accelerometry for the detection of epileptic seizure. The used sensors are wireless, which can improve quality of life for the patients. 
In this system, three 2D accelerometer sensors are positioned on the right arm, left arm, and left thigh of an epileptic patient. Datasets 
from three patients suffering from severe epilepsy are used in this paper for the development of an automatic detection algorithm. This 
monitoring system is based on Wireless Sensor Networks and can determine the location of the patient when a seizure is detected and 
then send an alarm to hospital staff or the patient’s relatives. Our wireless sensor nodes are MICAz Motes developed by Crossbow 
Technology. The proposed system can be used for patients living in a clinical environment or at their home, where they do only their 
daily routines. The analysis of the recorded data is done by an Artificial Neural Network and K Nearest‑Neighbor to recognize seizure 
movements from normal movements. The results show that K Nearest Neighbor performs better than Artificial Neural Network for 
detecting these seizures. The results also show that if at least 50% of the signal consists of seizure samples, we can detect the seizure 
accurately. In addition, there is no need for training the algorithm for each new patient.

Key words: 2D accelerometer, epilepsy seizure detection, K Nearest‑Neighbor, neural network, wireless sensor network

INTRODUCTION

Epilepsy is one of the most common neurological disorders, 
affecting almost 60 million people all over the world. Most 
of  the  affected  people  can  be  treated  successfully  with 
drug  therapy  (67%)  or  neurosurgical  procedures  (7%‑8%). 
Nevertheless 25% of the affected people cannot be treated 
by  any  available  therapy.[1]  For  refractory  patients  who 
continue to have frequent seizures, it has been shown that 
intensive monitoring with electroencephalogram (EEG) and 
video over a long period, contributes to the management 
of  daily  care  and  the  adjustment  of  drug  therapy.[2]  The 
long‑term  monitoring  with  EEG  and  video  can  be  very 
unpleasant  for  patients,  and  analyzing  large  amounts 
of  EEG/video‑data  is  very  labor  intensive  for  medical 
personnel. Furthermore, this method cannot yet be applied 
in real‑time procedures.

All the above‑mentioned factors have made it necessary to 
look for sensors that are patient friendly and can be used 
for  a  reliable  automatic  detection  of  epileptic  seizures. 
One of these sensors is the accelerometer. Accelerometers 
are  used  in  many  medical  research  areas  for  activity 
recognition.[3‑5] For instance, in Parkinson’s disease, studies 

aim at distinguishing pathological (periods of hypokinesia, 
bradykinesia and dyskinesia) and normal movements.[6,7]

signs 

focus  on  motor 

Here,  we 
since  epileptic 
seizures  are  often  accompanied  by  motor  signs.  With 
accelerometry (ACM), only seizures that express themselves 
in movements or disturb normal movement patterns can be 
detected.  The  results  in  reference[8]  demonstrate  that  3D 
ACM  is  a  valuable  sensing  method  for  seizure  detection. 
The authors in reference[9] propose an algorithm based on 
HMM for seizure detection. As in reference[9], in reference[10] 
the  patient  movements  are  modeled  with  Hidden  Markov 
Models  and  Bayesian  analysis  of  the  signal  is  performed. 
Algorithm  of  seizure  detection  in  reference[9]  is  without 
adaptation  to  patient  but  this  problem  is  overcome  in 
reference[10]. About nocturnal epileptic seizure, reference[11] 
focuses  on  the  distinction  between  seizure  moves  and 
nocturnal  moves.  Sensors  are  therefore  attached  on  a 
patient  and  the  authors  propose  to  detect  period  with 
motor activities.

Long‑term home monitoring can provide the neurologist an 
objective measure of the number of seizures that a patient 
can have during the day. Also in some of the heavy epileptic 

Address for correspondence: 
Golshan Taheri, School of Electrical and Computer Engineering, Shiraz University, Iran. Email: golshan.taheri@gmail.com

Vol 3  | Issue 2  |  Apr-Jun 2013

Journal of Medical Signals & Sensors

63

attacks the patient needs medical care after or during the 
seizure. Human body movement can be monitored through a 
wireless network composed of inertial sensors. Reference[12] 
presents 
(Wireless 
the  development  of  Wagyromag 
Accelerometer, GYROscope, and MAGnetometer), a wireless 
Inertial  Measurement  Unit  (IMU)  composed  of  a  triaxial 
accelerometer, gyroscope and magnetometer. The authors 
describe  a  seizure  detection  system  based  on  Wireless 
Sensor Network (WSN) that can determine the location of 
the patient when a seizure is detected and sends an alarm 
to hospital staff or the patient’s relatives.

Proposed System

In  this  paper,  we  introduce  a  system  based  on  WSN  that 
provides  a  continuous  monitoring  without  limiting  the 
freedom  and  privacy  of  the  patients.  The  main  goal  is 
to  distinguish  between  data  with  and  without  seizure 
movement.

The  general  constraints  and  characteristics  of  the  system 
are listed as follows:
•	

Flexibility: All external wirings can be removed to allow 
the subject under test move without restrictions

•	 Ease  of  use:  The  network  protocol  allows  the 
sensor  network  to  initialize  itself  in  a  highly  ad‑hoc, 
self‑organizing manner

•	 Reliability: While data reliability is always important, it 
becomes a critical requirement for many applications, 
for example, in medical monitoring

Low power consumption

•	 Biaxial acceleration measurement
•	 Rechargeable batteries
•	
•	 Comfortability:  The  device  has  small  size  and  low 
weight, and is able to be attached to different parts of 
patient’s body.

There are two kinds of nodes in the network:
•	 Mobile sensor nodes which are placed on the body of 

•	

patients
Static nodes which are sited on fixed specific locations 
at the building.

The static nodes transport the collected data from mobile 
sensor nodes to a base‑ station. The base‑ station sends data 
to computer server through a USB cable. Recorded data will 
be processed and when a seizure is detected, static nodes 
can determine approximately the location of the patient and 
sends an alarm to hospital staff or the patient’s relatives.

The  analysis  of  the  recorded  data  is  based  on  artificial 
neural  network  (ANN)  and  K  Nearest  Neighbor  (KNN)  to 
recognize  seizure  movements  from  normal  movements. 
Figure 1 shows the proposed system for epileptic seizure 
detection.

64

SEIZURE DETECTION METHOD

Data Collecting

Datasets  from  patients  suffering  from  heavy  epilepsy 
were used for the development of an automatic detection 
algorithm. In this system, three 2D accelerometer sensors 
were  positioned  on  the  right  arm,  left  arm  and  left  thigh 
of  epileptic  patients.  Datasets  were  acquired  from  three 
patients  suffering  from  severe  epilepsy.  The  datasets  of 
the  epileptic  patients  were  recorded  during  the  day.  We 
recorded 20 epileptic seizures.

Patients were asked to perform a sequence of everyday normal 
activities but were not told specially how to do them. Normal 
activities  that  we  recorded  included  static  activities  such  as 
reading, working with computer, brushing of teeth, and lying 
and  dynamic  activities  such  as  walking.  The  sampling 
frequency of the accelerometer is 3  Hz. Figure  2 shows the 
pure  output  of  accelerometers  when  sampling  frequency  is 
3 Hz.  It  shows  at  first  lying  and  then  seizure  signal.  In  this 
Figure the seizure has begun from 180 samples. Acceleration 
has been measured based on gravity  (

m s
/

= 9 8
.

).

g

2

For  analyzing  and  detecting  seizures  from  this  huge  data 
sequence, the best way is cutting the acceleration sequences 

Figure 1: Proposed system for epileptic seizure detection

Figure 2: The pure output of accelerometers

Journal of Medical Signals & SensorsBorujeny, et al.: Detection of epileptic seizure using wireless sensor networksVol 3  | Issue 2  |  Apr-Jun 2013into  many  overlapping  windows  (segments)  of  the  same 
length. For our data, the size of this window is considered 
50 samples and it is repeated for every 25 samples. Since 
the sampling frequency is 3 Hz, we cut the data sequence 
every 9 seconds and analyzed this window of the ACM data 
to detect seizure. Figure 3 shows the acceleration data and 
overlapping window that located the signal.

Preprocessing

The  output  of  an  accelerometer  attached  to  the  human 
body consists of different components:
•	 Noise from sensor and measurement system
•	 Noise sources from the environment: (a) accelerations 
vehicles; 
produced  by 
(b) accelerations due to bumping of the sensor or the 
body against other objects

external 

sources 

like 

Figure 3:  Acceleration data with overlapping windows

•	 Noise  sources  from  the  body:  (a)  Muscle  tremor; 

  Where  x

i

= { }  is the average of samples

E x

i

(b) Heart; (c) Respiration; (d) Blood flow

•	 Gravitational acceleration
•	 Acceleration due to movements of the body

In  comparison  to  body  movements,  the  noise  from  the 
sensor and measurement system can be neglected. All data 
used in this study were recorded while the patients were in 
their living environment, thus there were no accelerations 
produced by external sources.

When  there  is  no  movement,  physiological  perturbations, 
like respiration and heart rate and gravitational acceleration 
are visible in the signal. A preprocessing step is executed on 
the raw data for deleting these perturbations. To do that, we 
use a moving average filter. If the received signal is denoted 
as X(k), the filtered signal is given by following equation:

X k
s

( ) = ( ) −
X k

L

l

=−∑ (
X k
L
L
2
+

1

+

)1

j

j

i

i

ij

(

y

y

)

x

−

=

C

•	 Correlation is calculated between the two axes of each 
accelerometer. The correlation Cij between	x	and y axes 
is given by:
{
−(
E x

}
)
  Where xi and yj are ACM input signals of	x	and y axes, 
= { }  are its mean.
= { }  and  y
respectively, so  x
Energy  is  the  sum  of  the  squared  discrete  FFT  (Fast 
Furrier Transform) component magnitudes of the signal. 
If the length of window is N, discrete FFT component 
magnitudes  Xk  of  the  signal  and  its  energy  Es  are 
given by:

E y

E x

i

i

i

i

X

k

=

∑

N

−

1

n

=

0

( )
X n e

s

−

j

2

k
n

n
N

,

E

s

=

∑

n

−

1

k

=

1

X

2
k

Energy  parameter  is  used  to  discriminate  sedentary 
activities from other activities.

Choice of the Classifier

Where Xs(k) is the output of the filter. 2 L	+	1 is the size of 
the sliding window expressed in the number of samples, the 
filter length. We introduce a delay of LT in the flow of data. 
In practice T	=	1/3, so for L	=	2, the delay is 0.6 seconds.

In our work, two classifiers were constructed to recognize 
seizure movements from daily activities. The first classifier 
is ANN and the second classifier is KNN.

Feature Extraction

The  selection  of  discriminative  features  is  the  basis  of 
almost  all  detection  algorithms.  The  choice  for  certain 
features is based on the physiological phenomena that need 
to be detected.[13] In this way we should extract the features 
that help us to detect seizures. We used three features as 
follows:
•	 Variance measures the magnitude of a varying quantity 
2  can 
in the signal. If xi	=	Xs(k), the variance of samples  σi
be calculated by:

2
σi

=

|
E{ x

−

x

i

i

2
| }

T

T

2

,

,

=

=

{

}

yh

…

,
…

,
y y
1

{
2,
u u
1

, (cid:28)   and  y
ur

ANN
The  structure  of  the  ANN  classifier  is  shown  in  Figure  4. 
It consists of an input layer, a hidden layer, and an output 
}
layer  u
(cid:28)   are  the 
input and output vectors, respectively, where r represents 
the  number  of  elements  in  the  input  feature  set  and  h  is 
the  number  of  classes.  Tangent  sigmoid  functions  are 
selected  as  the  activation  functions  f  in  the  hidden  and 
output neurons. In general, the back propagation learning 
algorithm (a gradient descent optimization method) is used 
to  train  the  ANN.  However,  it  is  known  that  the  gradient 
descent  learning  method  is  subject  to  slow  convergence 
and local minima.[14]

65

Journal of Medical Signals & SensorsBorujeny, et al.: Detection of epileptic seizure using wireless sensor networksVol 3  | Issue 2  |  Apr-Jun 2013 
 
 
 
 
Levenberg‑Marquardt  backpropagation  is  one  of  the  best 
solutions  for  neural  network  training.[14]  A  multilayer 
perceptron  with  a  hidden  layer  of  15  nodes  and  with 
Levenberg‑Marquardt  backpropagation  as  the  training 
algorithm was used in the ANN classifier.

KNN
This  rule  classifies  x  by  assigning  it  to  the  label  which  is 
the  most  frequently  represented  among  the  k  nearest 
samples; in other words, the KNN query starts at the test 
point  and  grows  a  spherical  region  until  it  encloses  k 
training  samples,  and  labels  the  test  point  by  a  majority 
vote  of  these  samples.  The  criterion  of  distance  in  KNN 
classification is the Euclidean distance that is given by the 
following equation.

CC2420, ZigBee ready radio frequency transceiver designed 
for low‑power and low‑voltage wireless communication in 
the 2.4 GHz unlicensed ISM band.[15]

For the purpose of seizure detection, we use MTS310 sensor 
board. MTS310 has a variety of sensing modalities including 
an accelerometer two‑axis device. Figure 6 shows an MICAz 
Mote and an MTS310 sensor board.[16]

Locating the Patient

As  mentioned  above,  the  static  nodes  have  an  interface 
role between mobile sensor nodes and base‑station. Also, 
location  of  each  mobile  node  can  be  determined  by  the 
closest static node. So the location of static nodes must be 

d
E

=

T
−(
)
(
x m x m
[
i

−

i

1

2

)]

where	x	is a test point and mi is a training sample.

Network Topology

There  are  several  architectures  that  can  be  used  to 
implement  WSN  applications, 
including  star,  mesh, 
and  star‑mesh  hybrid.  Each  topology  presents  its  own 
set  of  challenges,  advantages,  and  disadvantages.  The 
topology  refers  to  the  configuration  of  the  hardware 
components  and  how  the  data  are  transmitted  through 
that configuration.

XMesh is a full featured multi‑hop, ad‑hoc, mesh networking 
protocol  developed  by  Crossbow,[15]  for  wireless  network. 
An  XMesh  network  consists  of  nodes  that  wirelessly 
communicate  to  each  other  and  are  capable  of  hopping 
radio  messages  to  a  base  station  where  they  are  passed 
to  a  central  server.  The  hopping  effectively  extends  radio 
communication  range  and  reduces  the  power  required  to 
transmit messages. By hopping data in this way, XMesh can 
provide two critical benefits: improved radio coverage and 
improved  reliability.  Two  nodes  do  not  need  to  be  within 
direct  radio  range  of  each  other  to  communicate.  Xmesh 
provides to support both Zigbee standards (802.15.4) and 
advanced  mesh  networking.  XMesh  provides  a  TrueMesh 
is  both  self‑organizing  and 
networking  service  that 
self‑healing. In Figure 5 is presented the diagram for XMesh 
network.

We  have  implemented  this  WSN  in  a  three‑floor  building 
that has 16 rooms in each floor.

Hardware Requirement

We have implemented this system with our wireless sensor 
nodes,  Motes,  developed  by  Crossbow  Technology.  The 
device is built upon the IEEE 802.15.4 standard and has an 
8‑bit  Atmel  ATmega  microcontroller.  It  uses  the  Chipcon 

66

Figure 4: structure of artificial neural network

Figure 5:  X Mesh network diagram

a

b

Figure 6: (a-b) MICAz mote, MTS310 sensor board

Journal of Medical Signals & SensorsBorujeny, et al.: Detection of epileptic seizure using wireless sensor networksVol 3  | Issue 2  |  Apr-Jun 2013Table 1: Performance of ANN classifier for seizure 
detection

Number of 
marked seizure

Number of 
detected seizure

Number of 
false alarm

Patient# 1
Patient# 2
Patient# 3

7
9
4

ANN – Artificial neural network

6
7
4

1
0
2

Table 2: Performance of KNN classifier for seizure 
detection

Number of 
marked seizure

Number of 
detected seizure

Number of 
false alarm

K=1
K=3
K=5

20
20
20

KNN – K Nearest Neighbor

18
20
20

3
2
0

chosen  such  that  at  any  time,  a  mobile  node  connects  to 
one  and  only  one  static  node,  since  each  mobile  node  is 
localized by the nearest static node. Although a large radio 
range for the nodes increases the power consumption and 
decreases  the  accuracy  for  localizing  the  mobile  nodes,  it 
helps  to  cover  a  building  with  fewer  static  nodes.  So,  we 
should  set  a  trade‑off  between  the  number  of  nodes  and 
radio range for them.

We  set  the  node’s  power  on  316  mW.  In  this  power,  the 
radio range of nodes is 30 m in a line of sight area and we 
can cover a building using eight static nodes.

EXPERIMENTAL RESULTS

The  proposed  system  in  this  research  can  be  used  for 
patients  living  in  a  clinical  environment  or  at  their  home, 
where  they  do  only  their  daily  routine.  We  could  detect 
seizures from normal activities such as walking. The analysis 
of  the  recorded  data  is  based  on  the  ANN  and  KNN  to 
recognize seizure movement from normal movement. When 
we classified datasets of the three patients by ANN to detect 
epileptic seizures, we obtained the results shown in Table 1.

As  can  be  seen  in  the  table,  three  seizures  have  not 
been  detected  and  we  have  obtained  three  false  alarms. 
Sensibility in this system is 85%.

Then  we  used  KNN  to  classify  the  datasets  and  detect 
seizures. The results of using this classifier with k	=	{1, 3, 5} 
are shown in Table 2.

Table  2  shows  that  for  k	= 	 1  two  seizures  have  not  been 
detected and three normal activities have been detected as 
seizures. For k	=	3 we have only two false alarms. But for 
k	= 	 5  no  seizure  has  been  missed  by  the  system  and  we 
have no false alarm. So KNN algorithm has produced better 
results than ANN.

DISCUSSION AND CONCLUSION

One of the most interesting applications of WSN is health 
monitoring. In this paper we introduced a monitoring system 
based on WSN for detection of epilepsy seizures. This system 
can be used for patients living in a clinical environment or 
at their home, where they do only their daily routine. Our 
system  can  determine  the  location  of  the  patient  when  a 
seizure  is  detected  and  sends  an  alarm  to  hospital  staff 
or  the  patient’s  relatives.  Since  our  sensors  are  wireless, 
the  subject  under  test  can  move  without  restrictions.  In 
addition, because of the small size of the sensor nodes, they 
are wearable for patients. Our experimental results showed 
that  5  Nearest  Neighbors  provides  better  results  than  the 
ANN  classifier.  Furthermore,  there  is  no  need  for  training 
the algorithm for each new patient.

REFERENCES

1.  Witte  H,  Iasemidis  LD,  Litt  B.  Special  issue  on  epileptic  seizure 

2. 

prediction. IEEE Trans Biomed Eng 2005;50:537‑9.
Binnie CD, Aarts JH, Van Bentum‑De Boer PT, Wisman T. Monitoring at 
the institute for epilepsy fight in Bosch..Electroencephalogr and Clin 
Neurophysiol Suppl 1985;37:341‑55.

3.  Mathie  MJ,  Celler  BG,  Lovell  NH,  Coster  AC.  Classification  of  basic 
daily movements using a triaxial accelerometer. Med Biol Eng Comput 
2004;42:679‑87.

4.  Veltink  P,  Bussmann  HB,  de  Vries  W,  Martens  WL,  Van  Lummel  RC. 
Detection  of  static  and  dynamic  activities  using  uniaxial 
accelerometers. IEEE Trans Rehabil Eng 1996;4:375‑85.

5.  Najafi  B,  Aminian  K,  Paraschiv‑Ionescu  A,  Loew  F,  Bula  C,  Robert  P. 
Ambulatory  system  for  human  motion  analysis  using  a  kinematic 
sensor: Monitoring of daily physical activity in the elderly. IEEE Trans 
on Biomed Eng 2003;50:711‑23.

6.  Dunnewold RJ, Hoff JI, Pelt HC, Fredrikze PQ, Wagemans EA, Hilten BJ. 
Ambulatory quantitative assessment of body position, bradykinesia, 
and  hypokinesia 
J  Clin  Neurophysiol 
1998;15:235‑42.
Thielgen  T,  Foerster  F,  Fuchs  G,  Hornig  A,  Fahrenberg  J.  Tremor  in 
parkinson’s disease: 24‑hr monitoring with calibrated accelerometry. 
Electromyogr Clin Neurophysiol 2004;44:137‑46.

in  parkinson’s  disease. 

7. 

9. 

8.  Nijsen TM, Arends JB, Griep PA, Cluitmans PJ. The potential value of 
three‑dimensional accelerometry for detection of motor seizures in 
severe epilepsy. Epilepsy and Behav 2005;7:74‑ 84.
Jallon  P,  Bonnet  S,  Antonakios  M,  Guillemaud  R.  Detection  system 
of  motor  epileptic  seizures  through  motion  analysis  with  3D 
accelerometers. Conf Proc IEEE Eng Med Biol Soc 2009; p. 2466‑9.
Jallon  P.  A  Bayesian  approach  for  epileptic  seizures  detection 
with  3D  accelerometers  sensors.  Conf  IEEE  Eng  Med  Biol  Soc 
2010;2010:6325‑8.

10. 

11.  Nijsen  TM,  Cluitmans  PJ,  Arends  JB,  Griep  PA.  Detection  of  subtle 
nocturnal motor activity from 3d accelerometry recordings in epilepsy 
patients. IEEE Trans Biomed Eng 2007;54:2073‑ 81.

12.  Olivares  A,  Olivares  G,  Mula  F,  Górriz  JM,  Ramírez  J.  Wagyromag: 
Wireless sensor network for monitoring and processing human body 
movement in healthcare applications. J Sys Arch 2011;57:905‑15.

13.  Bao  L, 

Intille  SS.  Activity  Recognition 

from  User‑Annotated 
Acceleration Data. New York: Springer‑Verlag Berlin Heidelberg 2004;  
p. 1‑17.

14.  Looney  CG.  Pattern  recognition  using  neural  networks,  theory  and 
algorithms  for  engineers  and  scientists.  Oxford:  Oxford  University 

67

Journal of Medical Signals & SensorsBorujeny, et al.: Detection of epileptic seizure using wireless sensor networksVol 3  | Issue 2  |  Apr-Jun 2013Press; 1997.

15.  Available  from:  http://www.xbow.comIProducts/productdetails.aspx? 

sid=l64 [Last accessed on 2012 Nov 03].

16.  Available 

from:  http://www.tinyos.millennium.berkeley.edul 

[Last 

accessed on 2012 Nov 03].

How to cite this article: Borujeny GT, Yazdi M, Keshavarz‑Haddad A,  
Borujeny AR. Detection of epileptic seizure using wireless sensor 
networks. J Med Sign Sens 2012;3:63‑8.

Source of Support: Nil, Conflict of Interest: None declared

BIOGRAPHIES

Golshan Taheri Borujeny was born in 1985. 
She received the B.Sc. degree in Biomedical 
engineering  from  the  Isfahan  University, 
in 
Isfahan 
the 
communication 
and 
Department  of 
electronic  engineering,  Shiraz  University,  Shiraz,  Iran,  in 
2007 and 2013, respectively. Her research interests include 
image  processing,  biomedical  signal  processing  and 
movement analysis.

systems 
from 
communication 

the  M.Sc.  degree 

and 

Alireza  Keshavarz‑Haddad  received  his  B.Eng.  degree 
in  2001  from  the  Department  of  Electrical  Engineering 
of  Sharif  University,  Tehran,  Iran,  and  his  M.S.  and  Ph.D. 
degrees in 2003 and 2007 from the Department Electrical 
and  Computer  Engineering  of  Rice  University,  Houston, 
Texas. Since 2008, he has been with the School of Electrical 
and Computer Engineering at Shiraz University, Shiraz, Iran, 
where  he  is  currently  an  Assistant  Professor.  His  research 
interests  are  in  Wireless  Ad  Hoc  and  Sensor  networks, 
Network Coding, and Network Security.

E‑mail: golshan.taheri@gmail.com

E‑mail: keshavarz@shirazu.ac.ir

from 

Arash Rafie Borujeny was born in 1985. He 
received  the  B.Sc.  degree  in  electrical 
engineering 
the  Shahid  Rajaee 
Teacher training University, Tehran, Iran, in 
2008.  He  is  currently  pursuing  the  M.Sc. 
of 
degree 
communication 
and  electronic  engineering,  Shiraz 
University,  Shiraz,  Iran.  His  research  interests  are  pattern 
recognition, neural network and numerical methods.

Department 

the 

in 

E‑mail: arash.rafie@gmail.com

from 

Mehran Yazdi received his B.Sc. degree in 
Digital  Communication  Systems  from  the 
Department  of  Electrical  Engineering, 
Shiraz  University,  in  1992  and  M.Sc.  and 
Ph.D. degrees in Digital Vision and Image 
the  Department  of 
Processing 
Electrical Engineering, Laval University, Canada, in 1996 and 
2003 respectively. He is currently Associate Professor at the 
Department of Communication and Electronic Engineering, 
Shiraz University, Iran. He conducted several projects in the 
area of hyperspectral image compression and denoising, CT 
metal artifact reduction and video compression. His major 
research interests are in the field of Image/video processing, 
remote  sensing,  Multidimentional  signal  processing  and 
medical image analysis.

E‑mail: yazdi@shirazu.ac.ir

68

Journal of Medical Signals & SensorsBorujeny, et al.: Detection of epileptic seizure using wireless sensor networksVol 3  | Issue 2  |  Apr-Jun 2013
