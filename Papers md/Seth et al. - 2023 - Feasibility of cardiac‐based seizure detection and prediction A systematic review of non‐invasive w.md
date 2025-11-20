# Seth et al. - 2023 - Feasibility of cardiac‐based seizure detection and prediction A systematic review of non‐invasive w

Received: 17 May 2023 

DOI: 10.1002/epi4.12854  

|  Accepted: 21 October 2023

C R I T I C A L   R E V I E W

Feasibility of cardiac-based seizure detection and 
prediction: A systematic review of non-invasive wearable 
sensor-based studies

Eryse Amira Seth1,2
Hadri Hadi Md Yusof1,2
Amudha Kadirvelu2

|   Jessica Watterson2,3

|   Jue Xie3

|   Irma Wati Ngadimon1,2

|   Mohd Farooq Shaikh1,2,5

|   Alina Arulsamy1,2
|   

|   Ching Soong Khoo4

|   

1Neuropharmacology Research 
Laboratory, Jeffrey Cheah School of 
Medicine and Health Sciences, Monash 
University Malaysia, Bandar Sunway, 
Malaysia
2Jeffrey Cheah School of Medicine and 
Health Sciences, Monash University 
Malaysia, Bandar Sunway, Malaysia
3Department of Human-Centred 
Computing, Monash University, 
Melbourne, Victoria, Australia
4Neurology Unit, Department of 
Medicine, Universiti Kebangsaan 
Malaysia Medical Centre, Kuala Lumpur, 
Malaysia
5School of Dentistry and Medical 
Sciences, Charles Sturt University, 
Orange, New South Wales, Australia

Correspondence
Mohd Farooq Shaikh, School of Dentistry 
and Medical Sciences, Charles Sturt 
University, 346 Leeds Parade, Orange, 
NSW 2800, Australia.
Email: farooq.shaikh@monash.edu and 
mshaikh@csu.edu.au

Funding information
Monash University Malaysia NEED 
(NEtwork for Equity through Digital 
Health), Grant/Award Number: MED/
NEED/11-2020/002

Abstract
A reliable seizure detection or prediction device can potentially reduce the mor-

bidity and mortality associated with epileptic seizures. Previous findings indicat-

ing alterations in cardiac activity during seizures suggest the usefulness of cardiac 

parameters for seizure detection or prediction. This study aims to examine avail-

able  studies  on  seizure  detection  and  prediction  based  on  cardiac  parameters 

using  non-invasive  wearable  devices.  The  Embase,  PubMed,  and  Scopus  data-

bases  were  used  to  systematically  search  according  to  the  Preferred  Reporting 

Items for Systematic Reviews and Meta-Analysis guidelines. Human studies that 

evaluated seizure detection or prediction based on cardiac parameters collected 

using wearable devices were included. The QUADAS-2 tool and proposed stand-

ards for validation for seizure detection devices were used for quality assessment. 

Twenty-four articles were identified and included in the analysis. Twenty stud-

ies evaluated seizure detection algorithms, and four studies focused on seizure 

prediction. Most studies used either a wrist-worn or chest-worn device for data 

acquisition. Among the seizure detection studies, cardiac parameters utilized for 

the algorithms mainly included heart rate (HR) (n = 11) or a combination of HR 

and heart rate variability (HRV) (n = 6). HR-based seizure detection studies col-

lectively reported a sensitivity range of 56%-100% and a false alarm rate (FAR) 

of  0.02-8/h,  with  most  studies  performing  retrospective  validation  of  the  algo-

rithms. Three of the seizure prediction studies retrospectively validated multi-

modal algorithms, combining cardiac features with other physiological signals. 

Only one study prospectively validated their seizure prediction algorithm using 

HRV extracted from ECG data collected from a custom wearable device. These 

studies  have  demonstrated  the  feasibility  of  using  cardiac  parameters  for  sei-

zure detection and prediction with wearable devices, with varying algorithmic 

performance. Many studies are in the proof-of-principle stage, and evidence for 

This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any 
medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made.
© 2023 The Authors. Epilepsia Open published by Wiley Periodicals LLC on behalf of International League Against Epilepsy.

Epilepsia Open. 2024;9:41–59. 

wileyonlinelibrary.com/journal/epi4

|  41

  
  
 
 
 
 
 
 
 
 
42 

| 

real-time detection or prediction is currently limited. Future studies should pri-

oritize further refinement of the algorithm performance with prospective valida-

tion using large-scale longitudinal data.

Plain Language Summary
This systematic review highlights the potential use of wearable devices, like wrist-

bands, for detecting and predicting seizures via the measurement of heart activity. 

By reviewing 24 articles, it was found that most studies focused on using heart rate 

and changes in heart rate for seizure detection. There was a lack of studies look-

ing  at  seizure  prediction.  The  results  were  promising  but  most  studies  were  not 

conducted in real-time. Therefore, more real-time studies are needed to verify the 

usage of heart activity-related wearable devices to detect seizures and even predict 

them, which will be beneficial to people with epilepsy.

K E Y W O R D S

cardiac, heart rate, seizure detection, seizure prediction, wearable device

1 

|  INTRODU CT ION

Epileptic  seizures  are  associated  with  an  increased  risk  of 
depression,  anxiety,  seizure-related  injuries,  and  prema-
ture death, known as sudden unexpected death in epilepsy 
(SUDEP).1,2  The  lifetime  prevalence  of  epilepsy,  including 
cases in remission, is 7.60 per 1000 people overall.3 A signifi-
cant number of people with epilepsy (PWE) still experience 
inadequate  seizure  control,  despite  considerable  progress 
in  treatment  and  surgical  interventions.4  Due  to  the  un-
predictability of seizures, physicians are reliant on patients 
and caregivers to document seizure events.5 However, self-
reporting is often unreliable and inaccurate,6–8 posing chal-
lenges to timely and effective treatment, self-management, 
and the risk of seizure-related injuries and SUDEP.

Recent  technological  advancements  have  paved  the 
way  for  improved  treatment  and  management  strategies 
through  seizure  detection  and  prediction.  Seizure  detec-
tion is the identification of a seizure upon onset, providing 
objective seizure quantification,9 while seizure prediction 
involves  identifying  physiological  changes  preceding  a 
seizure  and  alerting  patients  and  caregivers  of  a  seizure 
risk  at  any  given  time.  An  online  survey  conducted  by 
the  Epilepsy  Innovation  Institute  (Ei2)  revealed  that  un-
predictability  was  the  most  hindering  aspect  for  PWE.10 
A reliable seizure prediction system may reduce anxiety, 
improve quality of life, and potentially eliminate the risk 
of injuries and SUDEP. It can also be used in the context 
of treatment, as medications could be titrated according to 
periods of high or low seizure likelihood, further improv-
ing patient adherence and side effects.11,12

Research  on  seizure  detection  or  prediction  based  on 
non-cerebral signals has grown significantly due to the ris-
ing prevalence of wearable devices that can non-invasively 

Key Points

•  There is promising evidence for seizure detec-
tion  and  prediction  based  on  cardiac  param-
eters using wearable devices.

•  Most  of  the  studies  aimed  to  develop  seizure 
detection  algorithms,  with  only  a  few  studies 
focusing on seizure prediction.

•  Cardiac  parameters  used  included  heart  rate, 
heart rate variability, or a combination of both, 
yielding diverse algorithm performance.

•  Future  studies  should  focus  on  prospectively 
validating algorithms with large-scale longitu-
dinal data to enhance algorithm performance.

measure  signals  such  as  accelerometer  (ACC),  electrocar-
diogram (ECG), electrodermal activity (EDA), and electro-
myography.13–16 By coupling these measurements with the 
application of machine learning tools, substantial progress 
has been made in generating new insights into seizure pat-
terns (Figure 1). Dysfunction in the autonomic nervous sys-
tem (ANS) has been particularly observed in focal seizures 
with a temporal lobe origin, as well as focal-to-bilateral and 
generalized  tonic-clonic  seizures.17  This  systematic  review 
mainly focuses on the cardiac changes associated with ep-
ileptic  seizures  as  an  indicator  of  seizure  onset,  given  the 
compelling  evidence  for  pre-ictal  and  ictal  cardiac  man-
ifestations.17,18 Alterations in heart rate (HR) are the most 
commonly observed ictal autonomic changes and could po-
tentially serve as the earliest clinical sign of an impending 
seizure.17 This includes ictal tachycardia19,20 or a decrease in 

SETH ET AL. 
 
|  43

Schematic diagram of a seizure detection/prediction system. Physiological signals collected from wearable devices undergo 
F I G U R E   1 
pre-processing, and biomarkers for seizure detection/prediction are extracted. Analysis of these biomarkers is followed by the classification 
step, which is used to make a decision, triggering an alert notifying users of an upcoming seizure.

heart rate variability (HRV),21 which is the variation in time 
intervals between successive heartbeats. HRV is a reflection 
of cardiac activity regulation by the ANS, suggesting its po-
tential value in the identification of an upcoming seizure.21
In this systematic review, we aim to examine currently 
available studies on seizure detection or prediction based 
on  cardiac  parameters  using  non-invasive  wearable  de-
vices and to compare the performance between different 
cardiac parameters.

2 

|  METHODS

2.1 

|  Search strategy

The  Scopus,  PubMed,  and  Embase  databases  were  used 
to  conduct  a  systematic  search  in  accordance  with  the 
Preferred  Reporting  Items  for  Systematic  Reviews  and 
Meta-Analysis  (PRISMA)  guidelines.  All  available  publi-
cations  up  to  August  2022  were  included,  although  it  is 
worth noting that the utilization of sensor technology has 
only  emerged  in  the  last  decade.22,23  Keywords  related 
to  [“epilepsy”  or  “seizure”]  were  combined  with  terms 
related  to  [“detection”  or  “prediction”],  [“heart  rate”  or 
“cardiac”]  and  [“wearable  device”].  Searches  in  all  data-
bases were conducted based on title and abstract.

2.2 

|  Study selection

All resulting articles were imported into Covidence software 
(Veritas Health Innovation), and duplicates were automati-
cally removed. One reviewer screened titles and abstracts 
to  identify  relevant  research  articles.  Two  independent 
reviewers screened the full-text articles for inclusion, and 
conflicts were resolved by a third reviewer. The following 
inclusion criteria were used: (a) written in English; (b) ob-
servational  studies  (prospective  or  retrospective  studies) 
involving  human  participants;  (c)  peer-reviewed  original 
research articles related to seizure detection or prediction 
using  wearable  devices  in  people  with  epilepsy;  (d)  ECG 
or cardiovascular parameters were used as a basis for sei-
zure  detection  or  prediction,  either  alone  or  with  other 

physiological  signals,  (e)  provided  at  least  one  algorithm 
performance  indicator  as  an  outcome.  We  also  included 
studies that analyzed blood volume pulse (BVP) obtained 
from  photoplethysmography  (PPG)  signals,  as  it  provides 
information  about  heart  rate.24  Studies  were  excluded 
based  on  the  following  criteria:  (a)  articles  identified  as 
conference papers, reviews, book chapters, commentaries, 
editorials, and case reports; (b) ECG or cardiovascular data 
not collected using a wearable device; (c) studies that did 
not use cardiac parameters as a basis for seizure detection 
or prediction; (d) studies involving neonates.

|  Data extraction and synthesis of  

2.3 
results

Data  from  the  included  studies  were  extracted  elec-
tronically  using  Covidence.  Data  were  extracted  in  the 
following  categories:  study  identifiers  (author,  year  of 
publication),  study  characteristics  (study  population, 
study  setting,  reference  standard,  total  participants 
recruited,  and  number  of  patients  analyzed),  wear-
able device (wearable device used, device location, and 
physiological  signal[s]  collected),  seizure  detection 
or  prediction  algorithm  (type  of  validation,  detection 
or  prediction,  modality,  cardiovascular  parameter[s] 
used),  and  results  (seizure  type[s]  and  algorithm  per-
formance).  Studies  on  seizure  detection  were  analyzed 
separately from those on seizure prediction, which also 
included seizure forecasting.

2.4 

|  Quality assessment

Two  reviewers  independently  conducted  the  quality  as-
sessment  for  all  included  studies,  and  conflicts  were  re-
solved by discussion. The QUADAS-2 tool, a risk of bias 
tool  that  can  be  applied  to  primary  diagnostic  accuracy 
studies,  was  used  to  assess  the  quality  of  the  studies  in-
cluded  in  the  review  using  Review  Manager  version  5.4 
(Cochrane  Collaboration).  The  risk  of  bias  was  assessed 
based  on  each  of  these  four  domains:  patient  selection, 
index  test,  reference  standard,  flow,  and  timing.  The 

SETH ET AL. 
   
44 

| 

patient  selection  domain  assesses  the  method  of  patient 
recruitment  and  the  patients  included  in  the  study.  The 
index  test  and  reference  standard  domains  assess  how 
they  were  conducted  and  interpreted,  where  interpre-
tation of the index test results may be influenced by the 
knowledge of the reference standard and thus introduces 
the potential for bias. Concerns regarding applicability to 
the review question were also assessed for the first three 
domains. The flow and timing domain assesses the inclu-
sion of all patients in the analysis and the interval between 
the index test and reference standard.25 All included stud-
ies  were  also evaluated  based on proposed  standards for 
clinical validation of seizure detection devices.26 The stud-
ies  were  categorized  into  five  different  phases  based  on 
key features, including subjects, recordings, analysis and 
alarms, and reference standard.

3 

|  RESULTS

The database searches yielded a total of 2394 articles, out 
of which 1537 were screened based on title and abstract 
and  136  articles  were  selected  for  full-text  review.  After 
reviewing the full text based on eligibility criteria, 24 arti-
cles were included for analysis. Twenty studies evaluated 

seizure  detection  algorithms,27–46  whereas  the  remain-
ing four studies focused on seizure prediction, including 
forecasting the likelihood of seizures (periods of high and 
low risk).24,47–49 The screening stages and results are out-
lined  in  more  detail  in  Figure  2.  Articles  were  excluded 
mainly due to being a conference abstract or review, the 
study design not involving the validation of an algorithm 
on  patients,  or  not  using  a  wearable  device  to  measure 
cardiovascular signals. Studies that recorded and analyzed 
cardiovascular signals before or during seizures but not in 
the context of validating a seizure detection or prediction 
algorithm were also excluded.

3.1 

|  Studies on seizure detection

The characteristics of the 20 seizure detection studies in-
cluded  in  the  review  are  listed  in  Table  1.  The  number 
of patients included in the analysis for seizure detection 
ranged between 3 and 94 participants (median = 15.5 par-
ticipants). Most studies took place in an inpatient setting 
(n = 17),  where  patients  with  a  diagnosis  of  epilepsy  ad-
mitted to an epilepsy monitoring unit (EMU) for presurgi-
cal evaluation, seizure assessment, or diagnostic purposes 
were recruited. Two studies were conducted in a residential 

F I G U R E   2  PRISMA (Preferred 
Reporting Items for Systematic Reviews 
and Meta-Analyses) flowchart for 
database search, screening, and selection 
of studies.

SETH ET AL. 
 
G
P
P

,

C
C
A

m
r
A

h
c
t
a
w
t
h
g
i
N

e
v
i
t
i
s
n
e
s
-
d
e
r
a
r
f
n
I

d
n
a
t
n
e
i
t
a
p
n
I

n
e
r
d
l
i

h
C

D

I
n
a
d
n
a
y
s
p
e
l
i
p
e
y
r
o
t
c
a
r
f
e
r
h
t
i

w

)
d
l
o
s
r
a
e
y
8
1
-
3
(
n
e
r
d
l
i

h
C

a
r
e
m
a
c
o
e
d
i
v

t
n
e
i
t
a
p
t
u
o

l
a
i
t
n
e
d
i
s
e
r

l
a
n
o
i
t
u
t
i
t
s
n

i
d
e
z
i
l
a
i
c
e
p
s
a
n

i

r
o
e
m
o
h
t
a
g
n
i
v
i
l

G
C
E

t
s
e
h
C

G
C
E
d
e
z
i
r
u
t
a
i
n
m
m
o
t
s
u
C

i

d
n
a
g
n
i
d
r
o
c
e
r
o
e
d
i
V

t
n
e
i
t
a
p
n
I

s
t
l
u
d
A

e
m
o
s
h
t
i

w

,
s
e
r
u
z
i
e
s

c
i
t
p
e
l
i
p
e
h
t
i

w
d
e
s
o
n
g
a
i
d
y
l
s
u
o
i
v
e
r
p
s
t
n
e
i
t
a
P

r
o
t
i
n
o
m

T
I
F
M
E

s
e
g
n
a
h
c
R
H

f
o
s

m
r
o
f

g
n
i
t
t
e
s

e
r
a
c

P
M
E
T

,

G
P
P

,

C
C
A

G
P
P

,

C
C
A

t
s
i
r

W

m
r
A

2

O
p
S

,

G
P
P

,

A
D
E

t
s
i
r

W

2
x
O
t
s
i
r

i

W
n
n
o
N

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

s
t
l
u
d
A

,
s
a
l
l
a
D

f
o
l
a
t
i
p
s
o
H
n
a
i
r
e
t
y
b
s
e
r
P
t
a
U
M
E
e
h
t
o
t
d
e
t
t
i

m
d
a
s
t
l
u
d
A

.
s
a
x
e
T

s
r
e
t
n
e
c
y
s
p
e
l
i
p
e
g
n
i
t
a
p
i
c
i
t
r
a
p
e
h
t

r
o
s
n
e
s

e
p
y
t
o
t
o
r
P

A
/
N

A
/
N

A
/
N

a
r
e
m
a
c
o
e
d
i
v

t
n
e
i
t
a
p
t
u
o

f
o
1
f
o
y
t
i
l
i
c
a
f

m
r
e
t
-
g
n
o
l
a
n

i
d
e
d
i
s
e
r
d
n
a
h
t
n
o
m

r
e
p
e
r
u
z
i
e
s

h
c
t
a
w
t
h
g
i
N

e
v
i
t
i
s
n
e
s
-
d
e
r
a
r
f
n
I

d
n
a
t
n
e
i
t
a
p
n
I

s
t
l
u
d
A

l
a
n
r
u
t
c
o
n
r
o
j
a
m
1
>

f
o
y
r
o
t
s
i
h
a
h
t
i

w
D

I
y
s
p
e
l
i
p
e
h
t
i

w
s
t
l
u
d
A

8
2

8
1
0
2
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

1
3

7
1
0
2
l
a

t
e
n
a
g
o
C

1
4

3
1
0
2
l
a

t
e

e
s
s
a
M

0
4

2
2
0
2
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

G
M
E
s

n
e
r
d
l
i

h
c

r
o
s
n
o
s
a
e
r

c
i
t
s
o
n
g
a
i
d
r
o
f

K
U
n
o
d
n
o
L

,
l
a
t
i
p
s
o
H
e
g
e
l
l
o
C

n
o
i
t
a
u
l
a
v
e

l
a
c
i
g
r
u
s
e
r
p

G
C
E

,

C
C
A

m
r
A

r
o
s
n
e
s

r
e
m
m
h
S

i

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

d
n
a
s
t
l
u
d
A

e
r
u
z
i
e
s

l
a
n
r
u
t
c
o
n
f
o
y
r
o
t
s
i
h
a
h
t
i

w

)
d
l
o
s
r
a
e
y
2
e
v
o
b
a
(

s
t
n
e
i
t
a
P

4
4

7
1
0
2
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

2

O
p
S

,

G
P
P

,

A
D
E

G
P
P

,

C
C
A

G
P
P

,

A
D
E

t
s
i
r

W

t
s
i
r

W

r
a
E

r
o
s
n
e
s

r
a
E
-
n
I

°
s
s
u
n
i
s
o
c

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
x
O
t
s
i
r

i

W
n
n
o
N

G
E
E
-
o
e
d
i
V

G
E
E
-
o
e
d
i
V

G
E
E

t
n
e
i
t
a
p
n
I

t
n
e
i
t
a
p
n
I

t
n
e
i
t
a
p
n
I

n
e
r
d
l
i

h
c

r
o
f

s
r
e
t
n
e
c

e
h
t

f
o
e
n
o
o
t
d
e
t
t
i

m
d
a
,

k
w
/
e
r
u
z
i
e
s
1
>
y
c
n
e
u
q
e
r
f

A
/
N

A
/
N

g
n
i
r
o
t
i
n
o
m
G
E
E
-
o
e
d
i
v
)
h
4
2
>

(

m
r
e
t
g
n
o
l

U
M
E
e
h
t
o
t
d
e
t
t
i

m
d
a
s
t
n
e
i
t
a
P

g
n
i
r
o
t
i
n
o
m
G
E
E
-
o
e
d
i
v
r
e
d
n
u
s
t
n
e
i
t
a
p
y
s
p
e
l
i
p
E

A
/
N

g
n
i
r
o
t
i
n
o
m
m
r
e
t
-
g
n
o
l

G
E
E
o
e
d
i
v
t
n
e
i
t
a
p
n

i
g
n
i
o
g
r
e
d
n
u
s
t
n
e
i
t
a
P

G
E
E

,

G
C
E

,

C
C
A

t
s
e
h
C

°
0
8
1
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

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

d
n
a
s
t
l
u
d
A

r
o
f

l
a
t
i
p
s
o
H
y
t
i
s
r
e
v
i
n
U
d
n
a
l
a
e
Z
t
a
U
M
E
e
h
t
o
t
d
e
t
t
i

m
d
a
s
t
n
e
i
t
a
P

n
e
r
d
l
i

h
c

n
o
i
t
a
u
l
a
v
e

c
i
t
s
o
n
g
a
i
d

2
4

2
2
0
2
l
a

t
e
n
e
s
l
e
i
N
h
c
n
u
M

)
V
R
H

(
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
H

2
3

5
1
0
2
l
a

t
e
n
a
g
o
C

5
3

1
2
0
2
l
a

t
e

e
z
n
e
H

6
4

9
1
0
2
l
a

t
e
m
o
s
Z

|  45

)
s
e
u
n
i
t
n
o
C
(

P
M
E
T

e
l
k
n
a

n
e
r
d
l
i

h
c

,

G
P
P

,

A
D
E

,

C
C
A

r
o
t
s
i
r

W

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

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

d
n
a
s
t
l
u
d
A

U
M
E

l
a
t
i
p
s
o
H
s
n
e
r
d
l
i

'

h
C
n
o
t
s
o
B
e
h
t
o
t
d
e
t
t
i

m
d
a
s
t
n
e
i
t
a
P

3
4

1
2
0
2
l
a

t
e
g
n
a
T

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
B

r
o
s
n
e
s

e
l
b
a
r
a
e
w

s
e
s
o
p
r
u
p
c
i
t
s
o
n
g
a
i
d
r
o
f

s
e
r
u
z
i
e
s

r
i
e
h
t

G
C
E

t
s
e
h
C

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

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

A
/
N

f
o
g
n
i
d
r
o
c
e
r

l
a
t
i
p
s
o
h
-
n

i

t
n
e
w
r
e
d
n
u
o
h
w
y
s
p
e
l
i
p
e
h
t
i

w
s
t
n
e
i
t
a
P

3
3

9
1
0
2
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

,

A
D
E

,

C
C
A

,

G
C
E

m
r
A

d
n
a
b
m
r
a
r
e
p
p
u
e
k
o
p
s
e
B

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

d
n
a
s
t
l
u
d
A

'

s
g
n
K

i

t
a
U
M
E
e
h
t
o
t
d
e
t
t
i

m
d
a
y
s
p
e
l
i
p
e

l
a
c
o
f
h
t
i

w
e
l
p
o
e
P

0
3

1
2
0
2
l
a

t
e
o
n
u
r
B

G
P
P

,

A
D
E

,

C
C
A

t
s
i
r

W

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

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

d
n
a
s
t
l
u
d
A

s
a
d
e
t
i
u
r
c
e
r
y
s
p
e
l
i
p
e

f
o
s
i
s
o
n
g
a
i
d
a
h
t
i

w

)
d
l
o
s
r
a
e
y
0
8
-
7
(

s
t
n
e
i
t
a
P

9
2

2
2
0
2
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
o
B

n
e
r
d
l
i

h
c

e
r
a
c
y
s
p
e
l
i
p
e

l
a
c
i
n

i
l
c
d
r
a
d
n
a
t
s

r
i
e
h
t

f
o
t
r
a
p

l
a
c
i
g
o
l
o
i
s
y
h
P

)
s
(
l
a
n
g
i
s

n
o
i
t
a
c
o
L

d
e
t
c
e
l
l
o
c

e
c
i
v
e
d
f
o

o
t
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

a
t
a
d
c
a
i
d
r
a
c
t
c
e
l
l
o
c

e
c
n
e
r
e
f
e
R

/
s
t
l
u
d
A

d
r
a
d
n
a
t
s

g
n
i
t
t
e
s
y
d
u
t
S

n
e
r
d
l
i
h
c

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
W

s
c
i
t
s
i
r
e
t
c
a
r
a
h
c
y
d
u
t
S

.
s
r
e
t
e
m
a
r
a
p
c
a
i
d
r
a
c
n
o
d
e
s
a
b
d
e
p
u
o
r
g
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
n
o
s
e
i
d
u
t
s

f
o
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
d
n
a
s
c
i
t
s
i
r
e
t
c
a
r
a
h
c
y
d
u
t
S

1

E
L
B
A
T

n
o
i
t
a
l
u
p
o
p
y
d
u
t
S

)
r
a
e
y

,
r
o
h
t
u
A
(
d
e
d
u
l
c
n
i

s
e
i
d
u
t
S

A
/
N

7
2

0
2
0
2
m
a
l
A
d
n
a
i
l

A

)
R
H

(

e
t
a
r

t
r
a
e
H

SETH ET AL. 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
46 

| 

l
a
c
i
g
o
l
o
i
s
y
h
P

)
s
(
l
a
n
g
i
s

n
o
i
t
a
c
o
L

d
e
t
c
e
l
l
o
c

e
c
i
v
e
d
f
o

o
t
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

a
t
a
d
c
a
i
d
r
a
c
t
c
e
l
l
o
c

e
c
n
e
r
e
f
e
R

/
s
t
l
u
d
A

d
r
a
d
n
a
t
s

g
n
i
t
t
e
s
y
d
u
t
S

n
e
r
d
l
i
h
c

n
o
i
t
a
l
u
p
o
p
y
d
u
t
S

)
r
a
e
y

,
r
o
h
t
u
A
(
d
e
d
u
l
c
n
i

s
e
i
d
u
t
S

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
d
n
a
e
t
a
r

t
r
a
e
H

A
D
E

,

C
C
A

,

G
C
E

t
s
e
h
C

e
v
o
M
g
c
E

-
n
o
n
(

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

s
t
l
u
d
A

y
s
p
e
l
i
p
e
y
r
o
t
c
a
r
f
e
r
h
t
i

w
r
e
d
l
o
r
o
s
r
a
e
y
8
1
d
e
g
a
s
t
n
e
i
t
a
p
t
l
u
d
A

6
3

1
2
0
2
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

)
s
g
n
i
d
r
o
c
e
r
G
E
E

-
p
l
a
c
s

e
v
i
s
a
v
n

i

g
n
i
r
o
t
i
n
o
m
G
E
E
-
o
e
d
i
v
t
n
e
w
r
e
d
n
u
o
h
w

G
C
E

,

C
C
A

t
s
e
h
C

d
n
a
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

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

n
e
r
d
l
i

h
C

m
a
r
g
o
l
a
h
p
e
c
n
e
o
r
t
c
e
l
e
-
o
e
d
i
v
g
n
i
o
g
r
e
d
n
u
)
y
7
1
-
2
(
n
e
r
d
l
i

h
C

4
3

1
2
0
2
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

t
s
i
r
w

)

G
P
P
(
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
d
n
a

g
r
e
b
s
i
u
h
t
s
a
G
n
e
v
u
e
L
Z
U

t
a
n
o
i
t
a
u
l
a
v
e

G
C
E

d
n
a
t
s
e
h
C

)

G
C
E
(

°
0
8
1
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

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

s
t
l
u
d
A

l
a
c
i
g
r
u
s
e
r
p
t
n
e
w
r
e
d
n
u
o
h
w
y
s
p
e
l
i
p
e
y
r
o
t
c
a
r
f
e
r
h
t
i

w
s
t
n
e
i
t
a
P

5
4

7
1
0
2
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

°
0
8
1
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

e
r
a
c

l
a
c
i
n

i
l
c

r
o
f
g
n
i
r
o
t
i
n
o
m

G
C
E

t
s
e
h
C

e
c
i
v
e
d
h
c
t
a
P
e

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

d
n
a
s
t
l
u
d
A

r
o
l
a
c
o
f

e
l
b
a
b
o
r
p
f
o
s
i
s
o
n
g
a
i
d
a
h
t
i

w

)
d
l
o
s
r
a
e
y
6
7
-
5
(

e
l
p
o
e
P

8
3

7
1
0
2
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

n
e
r
d
l
i

h
c

G
E
E
-
o
e
d
i
v
m
r
e
t
-
g
n
o
l
a
r
o
f
d
e
l
l
o
r
n
e

,
y
s
p
e
l
i
p
e
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

l
a
t
i
p
s
o
H
y
t
i
s
r
e
v
i
n
U
s
u
h
r
a
A
n

i
g
n
i
r
o
t
i
n
o
m

l
a
i
n
a
r
c
a
r
t
n

i

,

G
E
E

i

;
y
t
i
l
i
b
a
s
i
d
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

,

D

I

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
t
i
n
u
g
n
i
r
o
t
i
n
o
m
y
s
p
e
l
i
p
e

,

U
M
E

;

m
a
r
g
o
l
a
h
p
e
c
n
e
o
r
t
c
e
l
e

,

G
E
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

m
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

G
C
E

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

.
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

n
o
i
t
a
r
u
t
a
s
n
e
g
y
x
o
d
o
o
l
b

,
2

O
p
S

;
y
h
p
a
r
g
o
y
m
o
r
t
c
e
l
e

e
c
a
f
r
u
s

,

G
M
E
s

;
y
h
p
a
r
g
o
m
s
y
h
t
e
l
p
o
t
o
h
p

,

G
P
P

;
e
l
b
a
l
i
a
v
a
t
o
n
n
o
i
t
a
m
r
o
f
n

i

,

A
/
N

;
y
h
p
a
r
g
o
l
a
h
p
e
c
n
e
o
r
t
c
e
l
e

G
C
E

t
s
e
h
C

e
c
i
v
e
d
h
c
t
a
P
e

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

d
n
a
s
t
l
u
d
A

l
a
c
i
g
r
u
s
e
r
p
r
o
s
n
o
s
a
e
r

c
i
t
s
o
n
g
a
i
d
r
o
f
d
e
l
l
o
r
n
e

e
r
e
w
o
h
w
s
t
n
e
i
t
a
P

n
e
r
d
l
i

h
c

U
M
E
e
h
t
n

i

n
o
i
t
a
u
l
a
v
e

G
C
E

t
s
e
h
C

e
c
i
v
e
d
h
c
t
a
P
e

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

d
n
a
s
t
l
u
d
A

l
a
c
i
g
r
u
s
e
r
p
r
o
s
n
o
s
a
e
r

c
i
t
s
o
n
g
a
i
d
r
o
f
d
e
l
l
o
r
n
e

e
r
e
w
o
h
w
s
t
n
e
i
t
a
P

n
e
r
d
l
i

h
c

U
M
E
e
h
t
n

i

n
o
i
t
a
u
l
a
v
e

9
3

9
1
0
2
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

7
3

0
2
0
2
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

s
c
i
t
s
i
r
e
t
c
a
r
a
h
c
y
d
u
t
S

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

SETH ET AL. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
setting, where they validated seizure detection devices for 
detecting nocturnal seizures.28,40 In studies with inpatient 
monitoring, patients were allowed to move around freely 
and perform normal daily activities despite being confined 
to a hospital room.33,42 Fifteen studies used video-electro-
encephalography (EEG) as a reference to validate seizure 
events,29–31,33–39,42–46 where clinical experts annotated the 
electrographic  seizure  onset  and  offset.  The  other  stud-
ies used infrared-sensitive video cameras,28,40 EEG with-
out  video  recording,31  and  video  recording  with  EMFIT 
monitor41  as  the  reference  standard.  One  study  did  not 
report on the reference standard used.27 Some of the stud-
ies also reported incomplete data and that not all patients 
that enrolled in the study were included in the analysis, 
mainly  due  to  factors  such  as  poor  connection  or  signal 
quality,34,44  withdrawal  of  participants,28  insufficient  or 
unsuitable seizures,29,30,37,39,42,46 unusable data,31,32,34 par-
ticipant's non-compliance to study protocol.40

3.1.1 

|  Wearable devices

Information on wearable devices used in the seizure de-
tection studies is listed in Table 1. A wide range of non-
invasive wearable devices were used to collect the ECG 
or  HR  data.  Four  studies  used  Empatica  E4,29,43,45,46 
three  studies  used  the  ePatch  device,37–39  and  three 
studies  used  Bittium  Faros  180°.34,42,45  Other  wear-
able  devices  that  were  noted  include  Nightwatch,28,40 
Nonin  WristOx2,31,32  SmartCardia  INYU  wearable  sen-
sor,33  Zephyr  Biopatch,34  cosinuss°  In-Ear  sensor,35 
EcgMove,36  and  Shimmer  sensor.44  Interestingly,  two 
studies  developed  custom  wearable  devices  to  collect 
the  ECG  or  PPG  data.30,41  The  devices  were  primarily 
either  worn  on  the  chest  (n = 8)33,34,36–39,41,42  or  wrist 
(n = 5). 27,29,31,32,46 In the remaining studies, the wearable 
devices  were  worn  on  the  arm  (n = 4)28,30,40,44  and  ear 
(n = 1). 35  One  study  used  two  wearable  devices,  where 
one device was worn on the chest and the other on the 
wrist,45  while  another  study  allowed  their  participants 
to wear the device either on their wrists or ankles.43

3.1.2 

|  Seizure detection algorithms

Information  on  the  seizure  detection  algorithms  and 
their performance are listed in Table 2. Eleven studies ex-
tracted HR features for the seizure detection algorithms, 
with  a  combined  sensitivity  range  of  56%-100%  and  a 
false  alarm  rate  (FAR)  of  0.02-8/h.  Most  of  the  studies 
that used HR as a basis for their seizure detection algo-
rithm (eight out of 11 studies) validated their algorithm 
retrospectively  using  an  existing  dataset.27,29–32,35,41,46 

|  47

For  example,  data  analysis  and  algorithm  testing  were 
performed  after  the  recording  of  physiological  signals 
from  patients  (offline).  Of  the  11  seizure  detection 
studies  based  on  HR,  four  studies  involved  adult  par-
ticipants,27,28,31,41 three studies included both adult and 
child participants29,30,44 and one study involved children 
only.40 The remaining three studies did not report infor-
mation on the participants' ages.32,35,46

Studies  with  adult  participants  achieved  a  combined 
sensitivity range of 85%-100%. The first study used a un-
imodal  approach,  where  a  custom  miniaturized  wear-
able  ECG  monitor  was  developed  and  integrated  with  a 
beat-detection algorithm and a real-time epileptic seizure 
detection  algorithm  to  detect  seizures.  The  device  was 
validated  in  three  patients  with  epilepsy  who  had  HR 
changes. Tonic-clonic, generalized tonic, and hypermotor 
seizures were detected with a mean sensitivity of 75% and 
PPV  of  70%.41  The  remaining  three  studies  with  adults 
used  a  multimodal  algorithm  that  was  validated  either 
prospectively28  or  retrospectively.27,31  In  the  prospective 
study, the multimodal sensor detected a median of 14 sei-
zures, with a median sensitivity of 86%, median positive 
predictive  value  (PPV)  of  49%,  and  a  false  positive  (FP) 
rate  of  0.25  per  night.28  The  authors  also  demonstrated 
that HR is a critical modality, as it accounted for 92% of 
the detection of true positives, whereas the ACC modal-
ity accounted for only 8% of detections. One retrospective 
study developed a seizure detection algorithm by analyz-
ing HR, blood oxygen saturation (SpO2), and EDA biosig-
nals acquired with a wrist-worn device. The personalized 
algorithm was able to detect seizures with 100% sensitiv-
ity and a FAR of 0.00/h in six out of 10 patients.31

In  the  study  focused  on  HR-based  seizure  detection 
among children, an adapted algorithm was developed to 
reduce  false  alarms,  where  the  alarm  was  only  triggered 
when  the  participant  was  lying  in  a  horizontal  position. 
This algorithm detected 305 out of 384 seizures (median 
sensitivity:  93%),  with  a  median  PPV  of  58%  and  a  false 
negative alarm rate of 0.02/h.40 Studies that included both 
adults  and  children  did  not  provide  a  clear  distinction 
in  algorithm  performance  between  the  two  age  groups, 
although  one  retrospective  study  used  a  leave-one-sei-
zure-out method for evaluation across three patients and 
reported lower sensitivity and higher FAR in one pediatric 
patient  compared  to  the  other  two  adult  patients  (sensi-
tivity: 67% vs 100%, FAR24: 41.52 vs 0.85-17.69).29 In this 
study,  HR  features  were  extracted  from  the  BVP  signals 
and combined with ACC and EDA features. An optimized 
model was also developed, which could detect focal motor 
seizures  with  a  mean  sensitivity  of  75%,  a  mean  FAR  of 
13.4/24 h, and a PPV of 2.1%.29

Two  studies  have  used  HRV  as  a  parameter  for  sei-
zure  detection.33,42  One  retrospective  validation  study 

SETH ET AL. 
   
48 

| 

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
p
m
h
t
i
r
o
g
l
a
f
o
s
t
l
u
s
e
R

e
p
y
t
e
r
u
z
i
e
S

y
t
i
l
a
d
o
M

n
e
r
d
l
i
h
c

d
e
z
y
l
a
n
a

d
e
t
i
u
r
c
e
r

n
o
i
t
a
d
i
l
a
v

)
R
H

(

e
t
a
r

t
r
a
e
H

)
r
a
e
y

%
5
8

:
y
t
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
9
0
6
2

.

:

R
A
F

s
e
r
u
z
i
e
s

e
v
i
s
l
u
v
n
o
C

l
a
d
o
m

i
t
l
u
M

s
t
l
u
d
A

%
6
8

:
y
t
i
v
i
t
i
s
n
e
S

M
O

,

K
H

,

T
G

,

S
C
T

:
s
e
r
u
z
i
e
s

l
a
n
r
u
t
c
o
N

l
a
d
o
m

i
t
l
u
M

s
t
l
u
d
A

3

8
2

3

e
v
i
t
c
e
p
s
o
r
t
e
R

7
2

0
2
0
2
m
a
l
A
d
n
a
i
l

A

4
3

e
v
i
t
c
e
p
s
o
r
P

8
2

8
1
0
2
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

.
s
r
e
t
e
m
a
r
a
p
c
a
i
d
r
a
c
n
o
d
e
s
a
b
d
e
p
u
o
r
g
s

m
h
t
i
r
o
g
l
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
S

2

E
L
B
A
T

f
o
.
o
N

l
a
t
o
T

/
s
t
l
u
d
A

s
t
n
e
i
t
a
p

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
p

f
o
e
p
y
T

,
r
o
h
t
u
A
(
d
e
d
u
l
c
n
i

s
e
i
d
u
t
S

)
P
(

%
0
0
1

,

%
0
0
1

:
y
t
i
v
i
t
i
s
n
e
S

)
P
(
h
/
0
0
0
0

.

,

h
/
5
1
0
0

.

:

R
A
F

)
P
(

%
0
0
1

,

%
6
8

:

V
P
P

t
h
g
i
n
/
3
0
0

.

:

R
A
N
F

t
h
g
i
n
/
5
2
0

.

:

R
A
P
F

%
9
4

:

V
P
P

:
)
6
=
n
(

s
r
o
s
n
e
S
3

S
C
T
G

,

S
C
T
B
F

,

I

A
O
F

l
a
d
o
m

i
t
l
u
M

s
t
l
u
d
A

0
1

0
2

e
v
i
t
c
e
p
s
o
r
t
e
R

1
3

7
1
0
2
l
a

t
e
n
a
g
o
C

.

.

)
2
1
0
-
3
0
0
0
e
g
n
a
r
(
h
/
2
0
0

.

:

R
A
N
F

I
C
%
5
9
[
%
0
0
1
-
%
4
7
4
e
g
n
a
r

.

,

.

%
9
5
8
n
a
e
m

]
%
0
0
1
-
%
9
9
5

.

(

%
2
3
9

.

:
y
t
i
v
i
t
i
s
n
e
S

M
O

,

K
H

,

T
G

,

S
C
T

:
s
e
r
u
z
i
e
s

l
a
n
r
u
t
c
o
N

l
a
d
o
m

i
t
l
u
M

n
e
r
d
l
i

h
C

%
4
0
7

.

:

V
P
P

%
5
7

:
y
t
i
v
i
t
i
s
n
e
S

r
o
t
o
m
r
e
p
y
h
d
n
a
c
i
n
o
t
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

S
C
T

l
a
d
o
m
n
U

i

s
t
l
u
d
A

)

.

%
6
6
8
-
%
2
1
e
g
n
a
r

.

,

.

%
5
5
5
n
a
e
m

(

%
1
8
5

.

:

V
P
P
n
a
i
d
e
M

%
5
7

:
y
t
i
v
i
t
i
s
n
e
S

.

4
3
1

:

4
2
R
A
F

%
1
2

.

:

V
P
P

S
C
T
G

,

S
C
T
B
F

l
a
d
o
m

i
t
l
u
M

d
n
a
s
t
l
u
d
A

n
e
r
d
l
i

h
c

.

1
9
0
-
6
5
8
0

.

:
y
t
i
v
i
t
i
s
n
e
S

6
1
0
0

.

:

V
P
P

d
e
t
a
i
c
o
s
s
a
s
n
o
i
t
a
t
s
e
f
i
n
a
m

A
D
E
r
o
G
C
E
d
a
h
s
e
r
u
z
i
e
s

e
r
a
w
a
r
o
t
o
m

f
o
e
n
o
N

•

s
e
r
u
z
i
e
s

%
5
7

:
)
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

e
r
u
z
i
e
s

r
o
t
o
m

(
y
t
i
v
i
t
i
s
n
e
S

•

d
e
r
i
a
p
m

i

h
t
i

w
s
e
r
u
z
i
e
s

r
o
t
o
m

l
a
c
o
F

l
a
d
o
m

i
t
l
u
M

d
n
a
s
t
l
u
d
A

)

A
D
E
r
o
C
C
A
r
o
G
M
E
s

r
o
G
C
E
(

%
2
9

,
)
y
l
n
o
G
C
E
(

e
r
a
w
a
r
o
t
o
m

l
a
c
o
f
d
n
a
s
s
e
n
e
r
a
w
a

n
e
r
d
l
i

h
c

.

t
h
g
i
n
/
3
2
=
R
A
F

;

%
1
7
-
%
6
5
=
y
t
i
v
i
t
i
s
n
e
S

:
y
l
n
o
R
H

,
r
o
t
o
m
r
e
p
y
h

,

C
T
G

:
s
e
r
u
z
i
e
s

l
a
n
r
u
t
c
o
N

l
a
d
o
m

i
t
l
u
M

d
n
a
s
t
l
u
d
A

.

t
h
g
i
n
/
3
6
-
9
5
=
R
A
F

.

;

%
7
8
-
%
1
7
=
y
t
i
v
i
t
i
s
n
e
S

:
t
v
M
+
R
H

s
e
r
u
z
i
e
s

r
e
t
s
u
l
c

,

T
G

n
e
r
d
l
i

h
c

)
P
(

%
0
0
1

,

%
0
0
1

:
y
t
i
v
i
t
i
s
n
e
S

x
e
l
p
m
o
c
d
n
a
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
y
l
i
r
a
d
n
o
c
e
S

l
a
d
o
m

i
t
l
u
M

A
/
N

s
3
1

:
y
c
n
e
t
a
l

n
o
i
t
c
e
t
e
d
n
a
e
M

h
4
2
/
2
9
1

:

R
A
F

)
P
(

%
0
0
1

,

%
3
8

:
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
S

)
P
(

%
0
0
1

,

%
2
9

:
y
c
a
r
u
c
c
A

s
e
r
u
z
i
e
s

l
a
i
t
r
a
p

S
C
T

l
a
d
o
m

i
t
l
u
M

A
/
N

3

3
2

6

2
1

3
2

3

7
1

3

e
v
i
t
c
e
p
s
o
r
t
e
R

1
4

3
1
0
2
l
a

t
e

e
s
s
a
M

5
2

e
v
i
t
c
e
p
s
o
r
P

0
4

2
2
0
2
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

3
4
2

e
v
i
t
c
e
p
s
o
r
t
e
R

9
2

2
2
0
2
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
o
B

1
5

e
v
i
t
c
e
p
s
o
r
t
e
R

0
3

1
2
0
2
l
a

t
e
o
n
u
r
B

5
9

e
v
i
t
c
e
p
s
o
r
t
e
R

4
4

7
1
0
2
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

5

e
v
i
t
c
e
p
s
o
r
t
e
R

2
3

5
1
0
2
l
a

t
e
n
a
g
o
C

A
/
N

e
v
i
t
c
e
p
s
o
r
t
e
R

5
3

1
2
0
2
l
a

t
e

e
z
n
e
H

e
v
i
s
l
u
v
n
o
c
-
n
o
n

%
8
7

:
y
c
a
r
u
c
c
A

d
n
a
e
v
i
s
l
u
v
n
o
c

,

S
E
N
P

,
s
e
r
u
z
i
e
s

c
i
t
p
e
l
i
p
E

l
a
d
o
m

i
t
l
u
M

A
/
N

8
1

0
3

e
v
i
t
c
e
p
s
o
r
t
e
R

6
4

9
1
0
2
l
a

t
e
m
o
s
Z

SETH ET AL. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
r
u
z
i
e
s

l
l
a
o
t
d
e
i
l
p
p
a
2
5
7
0
f
o
C
O
R
C
U
A

-

.

l
l
a
r
e
v
o
t
s
e
h
g
i
h

s

m
s
a
p
s

c
i
t
p
e
l
i
p
e

.

2
3
9
0
d
n
a
)
s
S
C
T
G

.

(
6
7
9
0
f
o
C
O
R
C
U
A

-

:

1
m
h
t
i
r
o
g
l
A

•

,
t
s
e
r
r
a
r
o
i
v
a
h
e
b
l
a
c
o
f

,
s

m

s
i
t
a
m
o
t
u
a

)
s
S
C
T
B
F
(

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
s
e
r
u
z
i
e
s

c
i
n
o
l
c

l
a
c
o
f

e
h
t
d
e
h
c
a
e
r
n
o
i
s
u
f
a
t
a
d
P
V
B
+
C
C
A

:

2
m
h
t
i
r
o
g
l
A

•

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
d
n
a
,
s
e
r
u
z
i
e
s

c
i
n
o
t

h
4
2
/
3
1
=
R
A
F

,

%
0
0
1
=
y
t
i
v
i
t
i
s
n
e
S

:
s
e
r
u
z
i
e
s

r
o
t
o
m
n
o
n

l
a
c
o
F

n
e
r
d
l
i

h
c

h
4
2
/
8
=
R
A
F

,

%
4
8
=
y
t
i
v
i
t
i
s
n
e
S

:
c
i
n
o
t

l
a
c
o
F

s
e
r
u
z
i
e
s

r
o
t
o
m
n
o
n

l
a
c
o
f
d
n
a
c
i
n
o
t

l
a
c
o
F

l
a
d
o
m

i
t
l
u
M

d
n
a
s
t
l
u
d
A

4
2
/
5
d
n
a

%
7
8
8

.

:
y
t
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
7
5
8

.

:
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
S

s
e
r
u
z
i
e
s

l
a
c
o
F

l
a
d
o
m
n
U

i

A
/
N

d
e
g
a
r
e
v
a
t
s
e
b
e
h
t
d
e
d
i
v
o
r
p
n
o
i
s
u
f
a
t
a
d
P
V
B
+
C
C
A

•

,
s
e
r
u
z
i
e
s

c
i
n
o
t

l
a
c
o
f

,
s
S
C
T
G

,
s
S
C
T
B
F

l
a
d
o
m

i
t
l
u
M

d
n
a
s
t
l
u
d
A

e
g
a
r
e
v
a
n
o
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
p
C
O
R
C
U
A

-

l
a
c
o
f

,
s
e
r
u
z
i
e
s

l
a
c
i
n

i
l
c
b
u
s

l
a
c
o
f

n
e
r
d
l
i

h
c

s
e
p
y
t

e
r
u
z
i
e
s

l
l
a
s
s
o
r
c
a
r
e
h
t
e
g
o
t
d
e
p
m
u

l

s
e
l
p
m
a
s

)

%
0
7

:
l
l
a
r
e
v
o
(

%
4
6

:
y
t
i
v
i
t
i
s
n
e
S

I

A
O
F

l
a
d
o
m
n
U

i

s
t
l
u
d
A

%
7
6

:
y
t
i
v
i
t
i
s
n
e
S

h
/
3
0
0

.

:
e
t
a
r
P
F

S
C
T
B
F

,

I

A
O
F

,

S
M
N
A
F

,

S
C
T
G

l
a
d
o
m

i
t
l
u
M

s
t
l
u
d
A

)

%
5
1
2

.

:
l
l
a
r
e
v
o
(

%
3
0
2

.

:

V
P
P

)
h
/
1
1
2

.

:
l
l
a
r
e
v
o
(
h
/
5
3
2

.

:

R
A
F

%
9
7
9
9
9

.

:
y
t
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
6
7
9
9
9

.

:

V
P
P

%
2
7

:
y
t
i
v
i
t
i
s
n
e
S

h
/
4
0
0

.

:
e
t
a
r
P
F

%
1
3
9

.

:
y
t
i
v
i
t
i
s
n
e
S

h
/
4
0
0

.

:
e
t
a
r
P
F

%
0
7
8

.

:
y
t
i
v
i
t
i
s
n
e
S

h
/
8
3
0

.

:
e
t
a
r
P
F

S
A
F

,

I

A
O
F

,

S
C
T
G

,

S
C
T
B
F

l
a
d
o
m
n
U

i

d
n
a
s
t
l
u
d
A

n
e
r
d
l
i

h
c

S
A
F

,

I

A
O
F

,

S
C
T
G

,

S
C
T
B
F

l
a
d
o
m
n
U

i

d
n
a
s
t
l
u
d
A

n
e
r
d
l
i

h
c

A
/
N

l
a
d
o
m
n
U

i

d
n
a
s
t
l
u
d
A

n
e
r
d
l
i

h
c

s
e
r
u
z
i
e
s

l
a
c
o
f
d
n
a
S
C
T

l
a
d
o
m

i
t
l
u
M

n
e
r
d
l
i

h
C

3

8
1

4
9

5
3

1
1

8
1

4
1

3
4

1
1

0
3

e
v
i
t
c
e
p
s
o
r
t
e
R

2
4

2
2
0
2
l
a

t
e
n
e
s
l
e
i
N
h
c
n
u
M

)
V
R
H

(
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
H

A
/
N

e
v
i
t
c
e
p
s
o
r
t
e
R

3
3

9
1
0
2
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

A
/
N

e
v
i
t
c
e
p
s
o
r
t
e
R

3
4

1
2
0
2
l
a

t
e
g
n
a
T

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
B

A
/
N

e
v
i
t
c
e
p
s
o
r
t
e
R

6
3

1
2
0
2
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
d
n
a
e
t
a
r

t
r
a
e
H

A
/
N

e
v
i
t
c
e
p
s
o
r
t
e
R

5
4

7
1
0
2
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

2
6

e
v
i
t
c
e
p
s
o
r
t
e
R

4
3

1
2
0
2
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

4
1

e
v
i
t
c
e
p
s
o
r
t
e
R

8
3

7
1
0
2
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

0
0
1

e
v
i
t
c
e
p
s
o
r
t
e
R

9
3

9
1
0
2
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

7
4

e
v
i
t
c
e
p
s
o
r
t
e
R

7
3

0
2
0
2
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
p
m
h
t
i
r
o
g
l
a
f
o
s
t
l
u
s
e
R

e
p
y
t
e
r
u
z
i
e
S

y
t
i
l
a
d
o
M

n
e
r
d
l
i
h
c

d
e
z
y
l
a
n
a

d
e
t
i
u
r
c
e
r

n
o
i
t
a
d
i
l
a
v

)
r
a
e
y

f
o
.
o
N

l
a
t
o
T

/
s
t
l
u
d
A

s
t
n
e
i
t
a
p

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
p

f
o
e
p
y
T

,
r
o
h
t
u
A
(
d
e
d
u
l
c
n
i

s
e
i
d
u
t
S

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

2

E
L
B
A
T

|  49

,

P
F

;
s
e
r
u
z
i
e
s

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

I

A
O
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
v
i
t
a
g
e
n
e
s
l
a
f

,

R
A
N
F

;
s
e
r
u
z
i
e
s

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

S
C
T
B
F

;
s
e
r
u
z
i
e
s

r
o
t
o
m
-
n
o
n
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

S
M
N
A
F

;
s
e
r
u
z
i
e
s

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

S
A
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
t
v
M

;
e
c
n
a
h
c

r
e
v
o
t
n
e
m
e
v
o
r
p
m

i

,

C
o
I

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
s
e
r
u
z
i
e
s

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

,

K
H

;
s
e
r
u
z
i
e
s

c
i
n
o
l
c
-
c
i
n
o
t
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

S
C
T
G

;
c
i
n
o
t
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

T
G

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
A
P
F

;
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

c
i
n
o
t

,

S
C
T

;
y
h
p
a
r
g
o
y
m
o
r
t
c
e
l
e

e
c
a
f
r
u
s

,

G
M
E
s

;
e
u
l
a
v
e
v
i
t
c
i
d
e
r
p
e
v
i
t
i
s
o
p

,

V
P
P

;
s
e
r
u
z
i
e
s

c
i
t
p
e
l
i
p
e
-
n
o
n
c
i
n
e
g
o
h
c
y
s
p

,

S
E
N
P

;

m
h
t
i
r
o
g
l
a
d
e
z
i
l
a
n
o
s
r
e
p

,

P

;
s
e
r
u
z
i
e
s

r
o
j
a
m

r
e
h
t
o

,

M
O

;
e
l
b
a
l
i
a
v
a
t
o
n
n
o
i
t
a
m
r
o
f
n

i

,

A
/
N

;
t
n
e
m
e
v
o
m

,

R
A
F

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

m
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

G
C
E

;
l
a
v
r
e
t
n

i

e
c
n
e
d
i
f
n
o
c

,
I
C

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

c
i
t
s
i
r
e
t
c
a
r
a
h
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

-

C
O
R
C
U
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
s
e
r
u
z
i
e
s

c
i
n
o
l
c

SETH ET AL. 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
50 

| 

collected  ECG,  ACC,  and  behind-the-ear  EEG  signals 
from  both  adults  and  children  using  separate  devices 
and extracted HRV measures such as Modified Cardiac 
Sympathetic  Index  (ModCSI)  and  Modified  Cardiac 
Sympathetic Index with Slope (ModCSISlope) from the 
R peaks of the ECG signal.42 A support vector machine 
(SVM)  algorithm,  another  machine  learning  tool,  was 
used to classify seizure or non-seizure events based on 
the  multimodal  signal  features  extracted.  This  study 
reported  the  detection  of  focal  tonic  (sensitivity:  84%, 
FAR:  8  per  24 h)  and  focal  non-motor  seizures  (sensi-
tivity: 100%, FAR: 13 per 24 h) in three patients. In an-
other retrospective study, the ECG signal collected using 
the chest-worn SmartCardia INYU wearable sensor was 
used to extract the R-R interval (RRI) and ECG-Derived 
Respiration  (EDR)  time  series.  For  HRV  analysis,  time 
domain, frequency domain, Lorenz plot, and multifrac-
tality  features  were  extracted  from  the  RRI  to  assess 
changes  in  cardiac  function.  The  random  forest  classi-
fier, a machine learning tool, was applied to classify sei-
zure and non-seizure segments. The algorithm was able 
to detect focal seizures with a sensitivity of 88.7% and a 
specificity of 85.7%.33

Six  studies  evaluated  seizure  detection  based  on  both 
HR and HRV parameters.34,36–39,45 Three of these studies 
included both adult and child participants, two involved 
adults only, while the remaining study included children 
only. Among the studies with adult participants, one uni-
modal algorithm study analyzed and compared ECG and 
PPG  wearable  devices  for  seizure  detection  in  patients 
with  temporal  lobe  epilepsy  (TLE).45  The  seizure  detec-
tion algorithm in this study utilized HRV and pulse rate 
variability  extracted  from  ECG  and  PPG  signals,  respec-
tively,  and  identified  an  HR  increase  before  performing 
classification  using  a  SVM  classifier.  The  wearable  ECG 
achieved  the  highest  sensitivity  (70%)  compared  to  the 
hospital ECG and wearable PPG, with a comparable FAR 
of  2.11/h. The  other  study  with  adult  participants  retro-
spectively  validated  a  multimodal  algorithm  combining 
HRV and HR with ACC and EDA, achieving a sensitivity 
of 67% and an FP rate of 0.03/h.36

In the study with children, a multimodal seizure detec-
tion algorithm based on ECG and ACC signals was eval-
uated.34  The  authors  also  developed  a  custom  prototype 
unit to employ the algorithm and allow for real-time sei-
zure detection. The cardiac algorithm, where both HR and 
HRV  were  analyzed,  was  able  to  detect  tonic-clonic  and 
focal  seizures  without  focal  to  bilateral  tonic-clonic  fea-
tures with an overall sensitivity of 72% and FAR or 0.04/h. 
Interestingly, when ECG and ACC parameters were com-
bined,  four  seizures  were  detected  faster,  but  the  overall 
sensitivity did not improve.34 Studies that evaluated HRV 
and  HR-based  algorithms  in  both  adults  and  children 

(n = 3) were all retrospective studies evaluating unimodal 
algorithms that achieved a combined sensitivity range of 
87%-100%. However, differences in performance between 
adults and children were not reported.37–39

3.2 

|  Studies on seizure prediction

Characteristics  and  wearable  devices  of  studies  on  sei-
zure prediction are listed in Table 3, and information on 
their  algorithms  is  summarized  in  Table  4.  Three  stud-
ies  employed  multimodal  seizure  prediction  algorithms 
and  conducted  retrospective  validation.24,47,48  The  first 
retrospective  study  evaluated  a  multimodal  algorithm 
combining  EDA,  HR,  and  skin  temperature  collected 
with  the  wrist-worn  Empatica  E4  in  three  patients  with 
refractory  epilepsy.  A  naïve  Bayes  classifier  was  trained 
on a set of sample data and then evaluated using five-fold 
cross-validation  for  preictal  and  interictal  classification 
during wakefulness, achieving a sensitivity of 78% and a 
specificity  of  80%.47  The  second  retrospective  study  also 
used Empatica E4 to acquire ACC, EDA, PPG, and tem-
perature  data  in  adults  and  children  with  epilepsy.  Out 
of  69  patients  included  in  the  analysis,  seizure  forecast-
ing  was  significantly  better  than  chance  for  43.5%,  of 
which achieved a mean improvement of chance (IoC) of 
28.5 ± 2.6%, a mean sensitivity of 75.6 ± 3.8%, and a mean 
percentage of time spent in warning (TiW) of 47.2 ± 3.4% 
(mean ± SEM). The same study also assessed the effect of 
reducing the training dataset on seizure forecasting algo-
rithm  performance  and  reported  improvements  in  IoC 
with  larger  datasets.24  Another  retrospective  study  uti-
lized a smartwatch to acquire PPG, sleep, and step count 
data, and a smartphone seizure diary app to monitor sei-
zures  in  adults  with  refractory  epilepsy.  HR,  HR  cycles, 
and HRV features were extracted from the PPG signal for 
the algorithm to forecast periods of high and low risk of 
seizures. The hourly forecasts achieved a median accuracy 
of 86%, and the average time spent in high-risk (prediction 
time) prior to a seizure onset was 37 minutes. Meanwhile, 
the daily forecast achieved 83% median accuracy, and the 
average prediction time before a seizure was 3 days.48

Only  one  study  prospectively  validated  their  seizure 
prediction algorithm and extracted both time-domain and 
frequency-domain  HRV  features.49  A  custom  wearable 
ECG  device  for  seizure  prediction  was  developed  in  this 
study,  which  consists  of  an  RR  interval  telemeter  con-
nected to a custom smartphone app via Bluetooth connec-
tion. The  smartphone  app  is  able  to  receive  and  analyze 
RRI,  which  is  used  to  extract  HRV  features.  A  machine 
learning  tool  known  as  multivariate  statistical  process 
control  for  seizure  prediction  was  employed,  where  a 
successful  prediction  was  defined  as  a  seizure  identified 

SETH ET AL. 
 
s
t
n
u
o
c
p
e
t
s

p
p
a
y
r
a
i
d
e
n
o
h
p
t
r
a
m
S

a
n

i
d
e
t
r
o
p
e
r

l
a
c
i
g
o
l
o
i
s
y
h
P

e
l
b
a
r
a
e
W

)
s
(
l
a
n
g
i
s

n
o
i
t
a
c
o
L

t
c
e
l
l
o
c
o
t
e
c
i
v
e
d

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
W

d
e
t
c
e
l
l
o
c

e
c
i
v
e
d
f
o

a
t
a
d
c
a
i
d
r
a
c

d
r
a
d
n
a
t
s
e
c
n
e
r
e
f
e
R

g
n
i
t
t
e
s

y
d
u
t
S

/
s
t
l
u
d
A

n
e
r
d
l
i
h
c

s
c
i
t
s
i
r
e
t
c
a
r
a
h
c
y
d
u
t
S

n
o
i
t
a
l
u
p
o
p
y
d
u
t
S

,

p
e
e
l
s

,

G
P
P

t
s
i
r

W

t
i
B
t
i
F

y
l
l
a
u
n
a
m

s
t
n
e
v
e

e
r
u
z
i
e
S

t
n
e
i
t
a
p
t
u
O

s
t
l
u
d
A

s
i
s
o
n
g
a
i
d
y
s
p
e
l
i
p
e
d
e
m

r
i
f
n
o
c
a
h
t
i

w

)
r
e
v
o
d
n
a
y
8
1
(

s
t
l
u
d
A

d
e
d
u
l
c
n
i

s
e
i
d
u
t
S

)
r
a
e
y
,
r
o
h
t
u
A
(

8
4

1
2
0
2
l
a

t
e
g
n

i
l
r
i
t
S

P
M
E
T

,

G
P
P

n
e
r
d
l
i

h
c

g
n
i
r
o
t
i
n
o
m
G
E
E
-
o
e
d
i
v
m
r
e
t

,

A
D
E

,

C
C
A

t
s
i
r

W

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

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

d
n
a
s
t
l
u
d
A

-
g
n
o
l

e
h
t
o
t
d
e
t
t
i

m
d
a
y
s
p
e
l
i
p
e
h
t
i

w

)
d
l
o
s
r
a
e
y
2
2
-
2
(

s
t
n
e
i
t
a
P

4
2

0
2
0
2
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

G
C
E

t
s
e
h
C

e
l
b
a
r
a
e
w
m
o
t
s
u
C

G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

d
n
a
s
t
l
u
d
A

t
n
e
w
r
e
d
n
u
d
n
a
d
e
t
t
i

m
d
a
y
s
p
e
l
i
p
e
y
r
o
t
c
a
r
f
e
r
h
t
i

w
s
t
n
e
i
t
a
P

9
4

0
2
0
2
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

e
c
i
v
e
d
G
C
E

n
e
r
d
l
i

h
c

n
o
i
t
a
u
l
a
v
e

l
a
c
i
g
r
u
s
e
r
p
r
o
f
g
n
i
r
o
t
i
n
o
m
G
E
E
-
o
e
d
i
v
l
a
c
i
n

i
l
c

t
n
e
m

s
s
e
s
s
a
e
r
u
z
i
e
s

r
o

P
M
E
T

r
e
t
n
e
C

l
a
c
i
d
e
M
y
k
c
u
t
n
e
K

f
o
y
t
i
s
r
e
v
i
n
U

,

G
P
P

,

A
D
E

t
s
i
r

W

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

G
E
E

i
d
n
a
G
E
E
-
o
e
d
i
V

t
n
e
i
t
a
p
n
I

A
/
N

e
h
t

t
a
n
o
i
t
a
u
l
a
v
e

l
a
c
i
g
r
u
s
e
r
p
e
v
i
s
a
v
n

i

r
o
f
d
e
t
t
i

m
d
a
s
t
n
e
i
t
a
P

7
4

8
1
0
2
l
a

t
e

i
r
k
a
B
-
l

A

,

G
P
P

,
e
l
b
a
l
i
a
v
a
t
o
n
n
o
i
t
a
m
r
o
f
n

i

,

A
/
N

,

m
a
r
g
o
l
a
h
p
e
c
n
e
o
r
t
c
e
l
e

l
a
i
n
a
r
c
a
r
t
n

i

,

G
E
E

i

,

m
a
r
g
o
l
a
h
p
e
c
n
e
o
r
t
c
e
l
e

,

G
E
E

,
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

,

m
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

G
C
E

,
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

.
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

,
y
h
p
a
r
g
o
m
s
y
h
t
e
l
p
o
t
o
h
p

.

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
e
r
u
z
i
e
s
n
o
s
e
i
d
u
t
s

f
o
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
d
n
a
s
c
i
t
s
i
r
e
t
c
a
r
a
h
c
y
d
u
t
S

3

E
L
B
A
T

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
p
m
h
t
i
r
o
g
l
a
f
o
s
t
l
u
s
e
R

e
p
y
t
e
r
u
z
i
e
S

m
h
t
i
r
o
g
l
a

y
t
i
l
a
d
o
M

n
e
r
d
l
i
h
c

d
e
z
y
l
a
n
a

d
e
t
i
u
r
c
e
r

n
o
i
t
a
d
i
l
a
v

)
r
a
e
y
,
r
o
h
t
u
A
(

r
e
t
e
m
a
r
a
p

r
o
f
d
e
s
u

c
a
i
d
r
a
C

f
o
.
o
N

l
a
t
o
T

/
s
t
l
u
d
A

s
t
n
e
i
t
a
p

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
p

f
o
e
p
y
T

d
e
d
u
l
c
n
i

s
e
i
d
u
t
S

.
s

m
h
t
i
r
o
g
l
a
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
e
r
u
z
i
e
S

4

E
L
B
A
T

)

M
E
S
±
n
a
e
m

(

.

%
4
3
±
2
7
4
=

.

i

)
g
n
n
r
a
w
n

i

t
n
e
p
s

e
m

i
t

f
o
e
g
a
t
n
e
c
r
e
p
e
h
t

,
e
i
(

i

W
T
n
a
e
M

.

.

%
8
3
±
6
5
7
=
y
t
i
v
i
t
i
s
n
e
s
n
a
e
M

.

.

%
6
2
±
5
8
2
=
C
o
I
n
a
e
M

y
r
a
d
n
o
c
e
s
d
n
a
y
r
a
m

i
r
P

P
V
B

l
a
d
o
m

i
t
l
u
M

d
n
a
s
t
l
u
d
A

d
n
a
,

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

s
e
r
u
z
i
e
s

l
a
c
o
f

n
e
r
d
l
i

h
c

%
6
8

:
)
t
s
a
c
e
r
o
f
y
l
r
u
o
h
(
y
c
a
r
u
c
c
a
n
a
i
d
e
M

%
3
8

:
)
t
s
a
c
e
r
o
f
y
l
i
a
d
(
y
c
a
r
u
c
c
a
n
a
i
d
e
M

R
H

,

V
R
H

A
/
N

,
s
e
l
c
y
c
R
H

l
a
d
o
m

i
t
l
u
M

s
t
l
u
d
A

%
5
5
=
a
p
p
a
k
s
n
e
h
o
C

'

%
8
7
=
y
t
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
0
8
=
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
S

h
/
2
6
0

.

:
e
t
a
r
P
F

A
/
N

R
H

l
a
d
o
m

i
t
l
u
M

A
/
N

n
e
r
d
l
i

h
c

%
7
5
8

.

:
y
t
i
v
i
t
i
s
n
e
S

S
A
F

,

S
C
T
B
F

,

S
A
I
F

V
R
H

l
a
d
o
m
n
U

i

d
n
a
s
t
l
u
d
A

1
1

9
6

7

3

9
3

e
v
i
t
c
e
p
s
o
r
t
e
R

8
4

1
2
0
2
l
a

t
e
g
n

i
l
r
i
t
S

7
1
3

e
v
i
t
c
e
p
s
o
r
t
e
R

4
2

0
2
0
2
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

4
1

e
v
i
t
c
e
p
s
o
r
P

9
4

0
2
0
2
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

3

e
v
i
t
c
e
p
s
o
r
t
e
R

7
4

8
1
0
2
l
a

t
e

i
r
k
a
B
-
l

A

|  51

t
r
a
e
h

,

R
H

,
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
A
P
F

,
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

P
F

,
s
e
r
u
z
i
e
s

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

S
A
I
F

,
s
e
r
u
z
i
e
s

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

S
C
T
B
F

,
s
e
r
u
z
i
e
s

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

S
A
F

,
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

,

n
a
e
m

f
o
r
o
r
r
e
d
r
a
d
n
a
t
s

,

M
E
S

,
e
l
b
a
l
i
a
v
a
t
o
n
n
o
i
t
a
m
r
o
f
n

i

,

A
/
N

,
e
c
n
a
h
c

r
e
v
o
t
n
e
m
e
v
o
r
p
m

i

,

C
o
I

,
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

,
e
t
a
r

SETH ET AL. 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
52 

| 

between 15 minutes and immediately before seizure onset. 
The  custom  seizure  prediction  system  demonstrated  the 
ability to predict focal impaired awareness seizures, focal 
to bilateral tonic-clonic seizures, and focal aware seizures 
in  both  adults  and  children  (sensitivity:  85.75%,  FAR: 
0.62/h).49

3.3 

|  Quality assessment

The  studies  included  in  this  review  are  of  mixed  quality 
(Table 5). Some studies did not provide a clear description 
of  the  recruitment  process  or  reference  standard;  there-
fore, it was difficult to assess the limitations and quality of 
these studies. Although a majority of the studies used EEG 
or video-EEG as the reference standard (n = 19), only five 
studies28,37,39,44,45 explicitly reported blinded annotation of 
seizures. It was unclear in the remaining studies whether 
the reference standard was reviewed without knowledge 
of the cardiac data. In the flow and timing domain, studies 
mostly had a low risk of bias as the data from the reference 
standard was collected concurrently with the cardiac data, 
and all patients received the same reference standard. Due 
to  the  heterogeneity  in  study  design  and  algorithm  per-
formance indicators reported in the studies, we could not 
conduct a meta-analysis in this present study.

Most of the studies are categorized as phase 1 (n = 19) 
according  to  the  proposed  standards  by  Beniczky  and 
Ryvlin  (Table  6).  Three  studies  are  categorized  as  phase 
2,28,37,39  while  the  remaining  two  studies  are  phase  0.30,48 
Although all studies used a dedicated device and a majority 
used video recording or video-EEG (n = 22) as the reference 
standard,  some  studies  could  not  be  classified  as  phase  2 
due  to  an  inadequate  number  of  patients  or  because  the 
safety  of  the  device  was  not  addressed.  Thirteen  studies 
trained and tested their algorithms on the dataset, and 10 
studies used predefined algorithms and cutoff values. Only 
four studies evaluated their algorithms in real time.28,40,41,49

4 

|  DISCUSSIO N

The findings from this systematic review highlighted both 
the  promise  and  challenges  of  the  feasibility  of  cardiac-
based seizure detection and prediction using non-invasive 
wearable devices. There is a clear feasibility with utilizing 
cardiac-based  algorithms  in  non-invasive  wearable  de-
vices for seizure detection, especially in adult populations 
of  epilepsy  with  generally  good  cardiovascular  health; 
however,  the  feasibility  of  them  for  seizure  prediction, 
whether in adults or children, may be too soon to conclude 
given the lack of data/clinical studies on their real-world 
prospective usage. Moreover, the reliability, validity, and 

sensitivity of these devices when taking into account the 
effect of cardiovascular abnormalities, such as a history of 
bradycardia  or  tachycardia,  among  people  with  epilepsy 
have  not  been  investigated.  The  findings  were  based  on 
articles that were either in phase 1 (proof-of-principle) or 
phase  2  (safety  of  device  addressed)  of  their  study,  with 
none  being  in  phase  3  (confirmation  of  safety  and  accu-
racy)  or  phase  4  (in-field,  usability  aspects),  suggesting 
that  the  feasibility  of  these  cardiac-based  seizure  detec-
tion  and  prediction  devices  is  still  in  the  early  stages  of 
development and validation, mainly in a controlled envi-
ronment. Real-world effectiveness accounting for patient 
clinical  heterogeneity  in  not  only  seizure  development 
but also general health, as well as patient usability in their 
daily  lives,  still  requires  further  research.  Since  the  risk 
of  bias  was  found  to  be  mostly  unclear  for  a  number  of 
the studies due to a lack of information in the reference 
standards used, the conclusions from these studies could 
be  potentially  biased.  Although  a  dedicated  device  was 
used  in  all  studies,  most  of  them  lack  an  assessment  of 
device safety and even have low sample sizes, contributing 
to a lack of feasibility information and data interpretation 
biasness.  Nevertheless,  findings  from  these  studies  may 
still contribute as an important stepping stone toward the 
epilepsy diagnostic and possibly therapeutic avenue upon 
further validation.

Some  of  the  studies  have  trained  and  validated  their 
own  machine  learning  algorithms  to  detect  changes  in 
physiological signals that indicate seizure events,43 while 
others have also used pre-trained algorithms. It is unclear 
at this point in time whether there are any confounding 
variables  to  be  considered  with  either  one  style  of  algo-
rithm  but  a  recent  paper  stated  that  while  pre-trained 
models may speed up optimization of the algorithm, they 
may have biased notions from previous machine learning 
training that will lead to inaccuracies in current data inter-
pretation.50  Moreover,  multiple  different  machine  learn-
ing techniques have been employed for seizure detection 
and  prediction  across  the  studies,  resulting  in  diverse 
performance results, thereby creating a more convoluted 
conclusion.  However,  the  diversity  in  machine  learning 
techniques used may bring to light the limitations and ad-
vantages of each technique, thereby providing future stud-
ies  with  a  better  idea  of  which  technique  would  be  best 
suited for further testing.

In  addition,  diverse  algorithmic  performance  was 
also  reported  when  comparing  seizure  detection  be-
tween adults and children. Among studies that use HR 
as an input for the seizure detection algorithm, a gener-
ally higher FAR was observed in children. However, one 
prospective  study  involving  children  only  achieved  an 
improvement  in  FAR  by  using  an  adapted  algorithm.40 
In  studies  that  used  HRV  and  HR,  higher  detection 

SETH ET AL. 
 
|  53

d
r
a
d
n
a
t
s
e
c
n
e
r
e
f
e
R

t
s
e
t
x
e
d
n
I

n
o
i
t
c
e
l
e
s

t
n
e
i
t
a
P

s
n
r
e
c
n
o
c
y
t
i
l
i
b
a
c
i
l
p
p
A

g
n
i
m

i
t
d
n
a
w
o
l
F

d
r
a
d
n
a
t
s
e
c
n
e
r
e
f
e
R

t
s
e
t
x
e
d
n
I

s
a
i
b
f
o
k
s
i
R

n
o
i
t
c
e
l
e
s

t
n
e
i
t
a
P

)
r
a
e
y
,
r
o
h
t
u
A
(
d
e
d
u
l
c
n
i

s
e
i
d
u
t
S

.
l
o
o
t
2
-
S
A
D
A
U
Q
g
n
i
s
u
d
e
d
u
l
c
n

i

s
e
i
d
u
t
s

e
h
t

f
o
t
n
e
m

s
s
e
s
s
a
y
t
i
l
a
u
Q

5

E
L
B
A
T

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

♦

7
2

0
2
0
2
m
a
l
A
d
n
a
i
l

A

8
2

8
1
0
2
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

9
2

2
2
0
2
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
o
B

0
3

1
2
0
2
l
a

t
e
o
n
u
r
B

2
3

1
3

5
1
0
2
l
a

t
e
n
a
g
o
C

7
1
0
2
l
a

t
e
n
a
g
o
C

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
3

1
2
0
2
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

3
3

9
1
0
2
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

6
3

1
2
0
2
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

5
3

1
2
0
2
l
a

t
e

e
z
n
e
H

8
3

9
3

7
3

7
1
0
2
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

9
1
0
2
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

0
2
0
2
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

0
4

2
2
0
2
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

1
4

3
1
0
2
l
a

t
e

e
s
s
a
M

2
4

2
2
0
2
l
a

t
e
n
e
s
l
e
i
N
h
c
n
u
M

5
4

7
1
0
2
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

4
4

7
1
0
2
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

3
4

1
2
0
2
l
a

t
e
g
n
a
T

7
4

8
1
0
2
l
a

t
e

i
r
k
a
B
-
l

A

4
2

0
2
0
2
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

8
4

1
2
0
2
l
a

t
e
g
n

i
l
r
i
t
S

9
4

0
2
0
2
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

6
4

9
1
0
2
l
a

t
e
m
o
s
Z

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
e
r
u
z
i
e
S

.
s
a
i
b
f
o
k
s
i
r
w
o
L
=
♦

;
s
a
i
b
f
o
k
s
i
r

r
a
e
l
c
n
U
=
♦

;
s
a
i
b
f
o
k
s
i
r
h
g
i
H
=
♦

SETH ET AL. 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
n
o
i
t
a
m
r
o
f
n
I

r
o
o
e
d
i
V

d
n
a
t
p
m
o
r
f

G
E
E
-
o
e
d
i
v

l
a
e
R

f
f
o
t
u
c
d
n
a

e
h
t
g
n
i
s
u

/
e
n
i
l
f
f

O

d
e
t
a
c
i
d
e
D

l
a
n
o
i
t
n
e
v
n
o
C

f
o
.
o
N

h
t
i

w
s
t
p

d
e
n
i
f
e
d
e
r
P

g
n
i
n
i
a
r
T

m
h
t
i
r
o
g
l
a

g
n
i
t
s
e
t
&

f
o
.
o
N

/
n
o
i
t
a
l
u
m
i
S

d
r
a
d
n
a
t
s
e
c
n
e
r
e
f
e
R

s

m
r
a
l
a
d
n
a
s
i
s
y
l
a
n
A

s
g
n
i
d
r
o
c
e
R

s
t
c
e
j
b
u
S

54 

| 

.

n

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
y
b
s
d
r
a
d
n
a
t
s
d
e
s
o
p
o
r
p
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
s
e
i
d
u
t
s
d
e
d
u
l
c
n

i

f
o
t
n
e
m

s
s
e
s
s
A

6

E
L
B
A
T

s
r
e
v
i
g
-
e
r
a
c

s
g
n
i
d
r
o
c
e
r

d
e
d
n
i
l

B

e
m

i
t

s
e
u
l
a
v

t
e
s
a
t
a
d

e
v
i
t
c
e
p
s
o
r
t
e
R

e
r
t
n
e
C
i
t
l
u
M

s
u
o
u
n
i
t
n
o
C

e
c
i
v
e
d

s
d
o
h
t
e
m

s
e
r
u
z
i
e
s

s
e
r
u
z
i
e
s

−

−

−

−

−

−

−

−

−

−

−

−

−

+

−

−

−

−

−

−

−

−

+

−

−

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

−

+

−

+

−

−

−

−

−

−

−

−

−

+

+

−

−

−

−

+

+

−

−

−

−

−

−

+

−

−

−

−

−

−

−

−

−

−

−

+

+

−

−

−

−

−

−

−

−

+

+

+

−

−

−

−

−

+

−

−

−

+

+

+

+

−

−

+

+

−

−

−

−

+

−

−

+

−

+

+

+

−

+

+

+

−

−

−

−

+

+

−

−

+

+

+

+

−

+

−

+

−

+

+

+

+

+

+

+

+

+

−

+

+

+

+

+

+

+

+

+

−

−

+

+

+

−

−

−

−

−

−

−

+

+

+

−

−

−

+

−

−

−

−

−

+

−

−

+

+

+

+

+

+

+

+

+

+

+

−

−

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

+

−

−

−

+

−

−

+

−

−

−

−

−

−

−

−

−

−

−

+

−

+

−

−

+

0
3
-
5
1

5
7
≥

0
3
-
5
1

5
7
-
0
3

5
1
-
1

5
1
-
1

5
7
≥

0
1
-
1

0
5
-
0
2

0
1
-
1

0
2
-
0
1

0
1
-
1

0
1
-
1

0
2
-
0
1

0
3
-
5
1

0
2
-
0
1

0
3
-
5
1

5
7
-
0
3

5
7
-
0
3

5
7
≥

0
3
-
5
1

5
7
-
0
3

5
7
≥

5
7
≥

5
7
≥

5
7
-
0
3

0
2
-
0
1

0
5
-
0
2

0
2
-
0
1

0
5
-
0
2

0
2
-
0
1

0
5
-
0
2

0
1
-
1

0
1
-
1

0
5
-
0
2

0
2
-
0
1

0
5
≥

5
7
-
0
3

0
2
-
0
1

A
/
N

5
7
≥

5
7
≥

5
1
-
1

0
1
-
1

0
5
≥

0
2
-
0
1

0
1
-
1

y
h
t
l
a
e
h

s
t
c
e
j
b
u
s

a

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

d
e
d
u
l
c
n
i

s
e
i
d
u
t
S

)
r
a
e
y
,
r
o
h
t
u
A
(

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

+

−

−

−

−

−

−

−

−

−

−

−

−

−

+

−

−

−

−

−

−

−

−

+

1

2

1

0

1

1

1

1

1

1

1

2

2

1

1

1

1

1

1

1

1

1

0

1

7
2

0
2
0
2
m
a
l
A
d
n
a
i
l

A

8
2

8
1
0
2
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

9
2

2
2
0
2
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
o
B

0
3

1
2
0
2
l
a

t
e
o
n
u
r
B

2
3

1
3

5
1
0
2
l
a

t
e
n
a
g
o
C

7
1
0
2
l
a

t
e
n
a
g
o
C

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

3
3

9
1
0
2

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

4
3

1
2
0
2

5
3

1
2
0
2
l
a

t
e

e
z
n
e
H

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

6
3

1
2
0
2

8
3

9
3

7
3

7
1
0
2
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

9
1
0
2
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

0
2
0
2
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

0
4

2
2
0
2
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

1
4

3
1
0
2
l
a

t
e

e
s
s
a
M

l
a

t
e
n
e
s
l
e
i
N
h
c
n
u
M

2
4

2
2
0
2

4
4

7
1
0
2
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

3
4

1
2
0
2
l
a

t
e
g
n
a
T

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

5
4

7
1
0
2

6
4

9
1
0
2
l
a

t
e
m
o
s
Z

7
4

8
1
0
2
l
a

t
e

i
r
k
a
B
-
l

A

4
2

0
2
0
2
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

8
4

1
2
0
2
l
a

t
e
g
n

i
l
r
i
t
S

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

9
4

0
2
0
2

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
e
r
u
z
i
e
S

h
t
i

w
e
c
i
v
e
d
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
d
e
t
a
c
i
d
e
d
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
s

:

2
e
s
a
h
P

.
s
e
i
d
u
t
s

e
l
p
i
c
n
i
r
p
-
f
o
-
f
o
o
r
p

:

1
e
s
a
h
P

.

d
o
h
t
e
m

l
e
v
o
n
a
g
n
i
p
o
l
e
v
e
d
r
o
g
n
i
t
r
a
t
s

r
o
f

s
e
i
d
u
t
s

l
a
i
t
i
n

i

:

0
e
s
a
h
P

:
s
e
s
a
h
p
g
n
w
o
l
l
o
f

i

e
h
t
o
t
n

i
d
e
z
i
r
o
g
e
t
a
c

e
r
a
s
e
i
d
u
t
S

a

.
s
t
c
e
p
s
a
y
t
i
l
i
b
a
s
u
g
n
i
s
s
e
r
d
d
a
,
s
t
n
e
m
n
o
r
i
v
n
e

e
m
o
h
s
t
n
e
i
t
a
p
s
e
c
i
v
e
d
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

f
o
s
e
i
d
u
t
s
d
l
e
i
f
-
n

i

:

4
e
s
a
h
P

.
y
c
a
r
u
c
c
a
d
n
a
y
t
e
f
a
s

f
o
n
o
i
t
a
m

r
i
f
n
o
c

l
a
n
i
f
n
o
s
e
i
d
u
t
s

:

3
e
s
a
h
P

.

d
e
s
s
e
r
d
d
a
e
c
i
v
e
d
e
h
t

f
o
y
t
e
f
a
s

.
t
n
e
i
t
a
p

,
t
p

;
r
e
b
m
u
n

,
.

o
N

;
e
l
b
a
l
i
a
v
a
t
o
n
n
o
i
t
a
m
r
o
f
n

i

,

A
/
N

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

SETH ET AL. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
sensitivity was reported among children compared to the 
studies involving adults, possibly due to the utilization 
of a patient-dependent algorithm in the study with chil-
dren. It is difficult to compare the performance between 
adults and children among the studies that reported on 
both, as they did not provide a clear difference between 
the  two  age  groups.  Resting  HR  was  found  to  increase 
with  age51  and  a  pre-ictal  decrease  in  HR  has  been  re-
ported  exclusively  in  studies  on  pediatric  population,18 
therefore, the large variation in HR among different age 
groups  may  contribute  to  diverse  performance  results. 
While  training  and  testing  algorithms  on  one  specific 
age  group  at  a  time  could  potentially  improve  the  de-
tection  or  prediction  performance  of  the  cardiac-based 
devices, it should also be noted that adults and children 
have  distinct  seizure  profiles  and  requirements  and 
therefore  should  always  be  treated  as  separate  subject 
groups  in  future  studies,  unlike  some  studies  reviewed 
in this manuscript.24,29,30,43,44,49

In  regards  to  the  cardiac  parameters  utilized,  it  was 
found  that  HR  was  most  commonly  extracted  and  an-
alyzed  for  seizure  detection,  with  a  few  studies  report-
ing the use of HRV or the combination of HRV and HR. 
There is a high incidence of pre-ictal HR increase more 
specifically  in  studies  involving  TLE  patients,  adults, 
or  patients  receiving  antiseizure  medications  (ASM).18 
However,  there  may  be  limitations,  as  not  all  seizures 
have changes in HR52 and may be prone to fluctuations 
contributed by medication, stress, age, sleep quality, and 
exercise.53  Some  studies  have  provided  a  possible  solu-
tion to this by using a multimodal algorithm and com-
paring  it  with  a  unimodal  algorithm,24,30,44  and  others 
have also asked patients to perform an exercise or stress 
test  to  sample  real-life  situations.37,39  Another  mean-
ingful  cardiac  measurement  is  the  HRV,  and  studies 
that used this parameter as a basis for seizure detection 
achieved a slightly higher sensitivity compared to those 
using HR only. HRV is regulated by the balance between 
the sympathetic and parasympathetic nervous systems; 
therefore,  changes  in  HRV  serve  as  an  indicator  of  the 
ANS  function.  Studies  investigating  the  correlation  be-
tween  interictal  HRV  and  epileptic  seizures  reported  a 
lower  HRV,  suggesting  an  imbalance  that  shifts  more 
toward  sympathetic  activity.54  This  is  in  line  with  an-
other study, which also reported an increase in peri-ictal 
(pre-ictal  and  post-ictal)  sympathetic  activity  in  gener-
alized tonic-clonic seizures.55 Taken together, it is clear 
that  both  HR  and  HRV  cardiac  parameters  should  be 
included  in  the  device  algorithm  to  improve  the  sensi-
tivity and specificity of seizure detection and prediction, 
which  could  also  greatly  improve  with  the  addition  of 
other physiological parameters such as skin temperature 
and electrodermal activity. The combination of cardiac 

|  55

and other physiological parameters may also reduce the 
chances  of  false  alarms,  which  will  encourage  greater 
patient compliance and usability.

Unfortunately,  detection  of  seizures  was  more  fre-
quently assessed and reported among the studies compared 
to seizure prediction. Since the latter is more aimed at no-
tifying patients and caregivers of an imminent seizure,56 
it  is  imperative  to  accurately  determine  pre-ictal  periods 
when training the algorithm.24 Accurate prediction of sei-
zures will allow patients and caregivers to take the neces-
sary precautions (medications or safe space) prior to their 
seizures,  thus  eliminating  possible  scenarios  that  may 
reduce their quality of life. Among the seizure prediction 
studies, there were variations in the performance metrics 
reported, maybe due to the different forms of prediction 
evaluated. Some studies provided a binary prediction (yes 
or no), while others forecast periods of high or low seizure 
likelihood, which could present more benefits as it allows 
users to plan activities and manage treatment according to 
the different periods of seizure likelihood.11,12 At present, 
it is difficult to compare prediction performance between 
age groups as we did not find any studies that evaluated 
seizure  prediction  exclusively  in  pediatric  patients.  The 
studies  included  either  adults  only  or  both  adults  and 
children. In the studies that included both adults and chil-
dren, they did not provide separate performance metrics 
for either population. Similar to seizure detection studies, 
multimodal algorithms or patient-specific algorithms may 
help to improve prediction rates, especially since there is 
no one-size-fits-all approach to developing a seizure pre-
diction algorithm.57 Billeci et al58 developed a patient-spe-
cific  algorithm  for  seizure  prediction  and  found  that 
optimal performance was achieved in patients with more 
conventional seizures. A considerable number of studies 
have  also  used  multiple  modalities,  combining  cardiac 
parameters  with  other  physiological  data  in  an  effort  to 
improve algorithm performance. Nevertheless, one or two 
modalities  could  be  sufficient,  depending  on  the  type  of 
seizures or the presence of ictal tachychardia.42

Wearable technology has made a remarkable impact 
in  healthcare  by  allowing  non-invasive  monitoring  of 
patients'  health  status  and  providing  easier  access  to 
information for physicians. The studies included in the 
analysis have used a wide range of wearable devices, col-
lecting  multiple  physiological  signals  that  are  utilized 
for  seizure  detection  or  prediction  algorithms.  Most 
studies  used  devices  that  are  currently  available  in  the 
market,  and  studies  that  have  developed  custom  wear-
able  devices  are  currently  at  the  prototype  stage  and 
have  reported  preliminary  data.  Further  clinical  test-
ing, particularly on validity and reliability, as well as an 
evaluation of user acceptance, may still be needed. For 
instance, a study investigating signal quality in wearable 

SETH ET AL. 
   
56 

| 

devices  used  for  epilepsy  management  and  monitoring 
has evaluated the patient experience and revealed their 
significant  preference  for  using  wrist-worn  devices.59 
Despite the ease and convenience associated with wear-
able devices, motion artifacts caused by normal daily ac-
tivities  should  also  be  taken  into  consideration.  Signal 
quality may also differ between individuals due to device 
or  battery  failures,  consequently  resulting  in  a  lack  of 
usable data for analysis. Yamakawa and colleagues have 
suggested  that  an  ECG  that  can  be  worn  like  clothing 
may be an option to improve signal and reduce motion 
artifacts.49 Nevertheless, most of the currently available 
studies  were  conducted  in  an  inpatient  setting,  where 
data  from  wearable  sensors  was  collected  either  pro-
spectively  or  from  an  existing  dataset,  and  algorithms 
were  validated  retrospectively.  Hence,  the  real-world 
factors such as motion artifacts and battery failures (loss 
of signal) that could influence the sensitivity of the sei-
zure prediction still lack clarity.

This systematic review is limited by the lack of statis-
tical analysis or meta-analysis to objectively compare the 
different cardiac parameters used in the seizure detection 
and prediction algorithms. This is due to the large hetero-
geneity  in  study  design,  setting,  and  population  among 
the included studies, representing a challenge that may be 
overcome  in  the  future  by  following  guidelines  for  con-
ducting and reporting seizure detection or prediction stud-
ies.26,60,61  Developing  studies  using  these  guidelines  will 
ensure that studies are comparable and data can be shared 
across  different  seizure  detection  or  prediction  research 
groups, subsequently improving the quality of evidence.

Based  on  current  advancements  in  technology  and 
digital  health,  there  is  a  possibility  that  patient-specific 
algorithms  with  an  integration  of  multiple  physiological 
parameters that enhance the accuracy and reliability of car-
diac-based seizure detection and prediction devices may be 
available in the near future. Indeed, real-time validation is 
first required, especially for the seizure prediction device, 
to ensure patient compliance and acceptance do not con-
found the validity and reliability of the seizure prediction. 
Moreover,  with  real-time  clinical  studies,  preferably  long-
term  studies,  the  safety,  cost-effectiveness,  logistics,  and 
practical utility of the devices can be assessed as well. Large-
scale  and  long-term  patient  data  are  required  to  develop 
and refine patient-specific algorithms. In addition, prospec-
tive validation of the algorithms in a real-world setting and 
assessment  of  signal  quality  would  also  be  useful,  taking 
into account any artifacts and noise that could be contrib-
uted by normal daily activities. A recent systematic review 
discovered that performance, design, comfort, and cost are 
crucial factors that determine the acceptance of wearable 
devices in real-world settings although this was not specific 
to  seizure  detection  or  prediction.62  Additionally,  people 

with  epilepsy  highly  prefer  non-stigmatizing  devices  that 
can be seamlessly integrated into their daily lives thereby 
justifying the need for real-world usability studies for these 
cardiac-based seizure detection and prediction devices.61

Once validated, the cardiac-based seizure device, partic-
ularly the seizure prediction device, will be a game-changer 
in epilepsy management, as treatment against seizures can 
be utilized more efficiently in a proactive manner than the 
current  reactive  seizure  management  strategies,  thereby 
ensuring  timely  prevention  of  seizures  and  reducing  the 
occurrence of drug adverse effects and resistance caused by 
overloading of current ASMs. In fact, by utilizing the car-
diac-based  seizure  detection  and  prediction  device,  treat-
ment against seizures could also become more automated, 
leaving children with epilepsy to be more independent in 
managing their condition and adults to have better adher-
ence to their treatment plan. Thus, successful implementa-
tion of these cardiac-based tools into clinical practice may 
improve current methods of epilepsy management, possi-
bly preventing seizures before their manifestation, thereby 
ensuring the preservation of quality of life among people 
with epilepsy.

5 

|  CONCLUSION

Altogether, the studies analyzed in this systematic review 
have  collectively  demonstrated  the  feasibility  of  utiliz-
ing  cardiac  parameters  as  a  tool  for  seizure  detection  or 
prediction. The integration of machine learning tools and 
non-invasive  wearable  devices  signifies  a  promising  ad-
vancement  in  epilepsy  care  and  management.  However, 
future research should focus on refining the detection or 
prediction performance and providing stronger evidence 
with  more  large-scale,  multicenter  studies  conducted  in 
an outpatient, real-life setting. Evaluation of user experi-
ence and feedback would be equally important to provide 
more insight into the clinical value of seizure detection or 
prediction using non-invasive wearable devices.

AUT HOR CON TRIBUT IONS
All  authors  have  contributed  to  the  preparation  of  this 
manuscript.  EAS  performed  the  literature  search,  criti-
cal  analysis  of  the  articles,  and  drafted  the  manuscript; 
HHMY and MFS performed the literature screening and 
selection;  IWN  performed  the  quality  analysis  of  the  lit-
erature; JW, JX, AA, CSK, AK, and MFS conceptualized, 
reviewed, edited, and approved the final manuscript.

ACKNOWLEDGMENT S
Open access publishing facilitated by Monash University, 
as  part  of  the  Wiley  -  Monash  University  agreement  via 
the Council of Australian University Librarians.

SETH ET AL. 
 
FUNDI NG  IN FORMATION
This  project  is  funded  by  Monash  University  Malaysia 
NEED (NEtwork for Equity through Digital Health) Grant 
Scheme 2020 (MED/NEED/11-2020/002). EAS, IWN and 
HHMY  are  supported  by  Monash  University  Malaysia 
Graduate Research Excellence Scholarship.

CO NFLI CT OF INTEREST STATEME N T
None  of  the  authors  have  any  conflict  of  interest  to 
disclose.

DATA  AVAILABIL ITY STAT EME N T
Data sharing is not applicable to this article as no new data 
were created or analyzed in this study.

ETHIC S STATEMENT
We  confirm  that  we  have  read  the  Journal's  position  on 
issues involved in ethical publication and affirm that this 
report is consistent with those guidelines.

 https://orcid.org/0000-0003-4549-1627 

 https://orcid.org/0000-0003-0993-5622 

 https://orcid.

 https://orcid.

ORC ID
Eryse Amira Seth 
org/0000-0002-7827-0807 
Jessica Watterson 
org/0000-0003-0619-0661 
Jue Xie 
Alina Arulsamy 
Hadri Hadi Md Yusof 
org/0000-0002-6702-1952 
Irma Wati Ngadimon 
org/0000-0002-0914-8058 
Ching Soong Khoo 
org/0000-0002-6756-0411 
Amudha Kadirvelu 
org/0000-0001-5646-294X 
Mohd Farooq Shaikh 
org/0000-0001-9865-6224 

 https://orcid.

 https://orcid.

 https://orcid.

 https://orcid.

 https://orcid.

R E F E R E N C E S
  1.  Nguyen R, Tellez Zenteno JF. Injuries in epilepsy: a review of its 
prevalence, risk factors, type of injuries and prevention. Neurol 
Int. 2009;1(1):e20.

  2.  Stafstrom CE, Carmant L. Seizures and epilepsy: an overview for 

neuroscientists. Cold Spring Harb Perspect Med. 2015;5(6):1–19.

  3.  Fiest KM, Sauro KM, Wiebe S, Patten SB, Kwon CS, Dykeman 
J, et al. Prevalence and incidence of epilepsy: a systematic re-
view  and  meta-analysis  of  international  studies.  Neurology. 
2017;88(3):296–303.

  4.  Ryvlin P, Cross JH, Rheims S. Epilepsy surgery in children and 

adults. Lancet Neurol. 2014;13(11):1114–26.

  5.  Brinkmann  BH,  Karoly  PJ,  Nurse  ES,  Dumanis  SB,  Nasseri 
M, Viana  PF,  et  al.  Seizure  diaries  and  forecasting  with  wear-
ables:  epilepsy  monitoring  outside  the  clinic.  Front  Neurol. 
2021;12:690404.

|  57

  6.  Erba G, Bianchi E, Giussani G, Langfitt J, Juersivich A, Beghi 
E. Patients' and caregivers' contributions for differentiating ep-
ileptic from psychogenic nonepileptic seizures. Value and lim-
itations of self-reporting questionnaires: a pilot study. Seizure. 
2017;53:66–71.

  7.  Hoppe C, Poepel A, Elger CE. Epilepsy: accuracy of patient sei-

zure counts. Arch Neurol. 2007;64(11):1595–9.

  8.  Nickels KC, Zaccariello MJ, Hamiwka LD, Wirrell EC. Cognitive 
and  neurodevelopmental  comorbidities  in  paediatric  epilepsy. 
Nat Rev Neurol. 2016;12(8):465–76.

  9.  Ramgopal S, Thome-Souza S, Jackson M, Kadish NE, Sánchez 
Fernández I, Klehm J, et al. Seizure detection, seizure predic-
tion,  and  closed-loop  warning  systems  in  epilepsy.  Epilepsy 
Behav. 2014;37:291–307.

 10.  Dumanis SB, French JA, Bernard C, Worrell GA, Fureman BE. 
Seizure  forecasting  from  idea  to  reality.  Outcomes  of  the  my 
seizure gauge epilepsy innovation institute workshop. eNeuro. 
2017;4(6):ENEURO.0349-17.2017.

 11.  Baud  MO,  Rao  VR.  Gauging  seizure  risk.  Neurology. 

2018;91(21):967–73.

 12.  Stirling  RE,  Cook  MJ,  Grayden  DB,  Karoly  PJ.  Seizure  fore-
casting and cyclic control of seizures. Epilepsia. 2021;62(Suppl 
1):S2–S14.

 13.  Beniczky S, Polster T, Kjaer TW, Hjalgrim H. Detection of gen-
eralized tonic-clonic seizures by a wireless wrist accelerometer: 
a prospective, multicenter study. Epilepsia. 2013;54(4):e58–61.

 14.  Milosevic  M,  van  de  Vel  A,  Bonroy  B,  Ceulemans  B,  Lagae 
L,  Vanrumste  B,  et  al.  Automated  detection  of  tonic-clonic 
seizures  using  3-D  accelerometry  and  surface  electromyog-
raphy  in  pediatric  patients.  IEEE  J  Biomed  Health  Inform. 
2016;20(5):1333–41.

 15.  Patterson AL, Mudigoudar B, Fulton S, McGregor A, Poppel KV, 
Wheless MC, et al. SmartWatch by SmartMonitor: assessment 
of  seizure  detection  efficacy  for  various  seizure  types  in  chil-
dren,  a  large  prospective  single-center  study.  Pediatr  Neurol. 
2015;53(4):309–11.

 16.  Bottcher  S,  Bruno  E,  Manyakov  NV,  Epitashvili  N,  Claes  K, 
Glasstetter  M,  et  al.  Detecting  tonic-clonic  seizures  in  multi-
modal biosignal data from wearables: methodology design and 
validation. JMIR Mhealth Uhealth. 2021;9(11):e27674.

 17.  Thijs RD, Ryvlin P, Surges R. Autonomic manifestations of ep-
ilepsy:  emerging  pathways  to  sudden  death?  Nat  Rev  Neurol. 
2021;17(12):774–88.

 18.  Bruno E, Biondi A, Richardson MP, Consortium R-C. Pre-ictal 
heart  rate  changes:  a  systematic  review  and  meta-analysis. 
Seizure. 2018;55:48–56.

 19.  Eggleston KS, Olin BD, Fisher RS. Ictal tachycardia: the head-

heart connection. Seizure. 2014;23(7):496–505.

 20.  Sivathamboo S, Constantino TN, Chen Z, Sparks PB, Goldin J, 
Velakoulis D, et al. Cardiorespiratory and autonomic function 
in  epileptic  seizures:  a  video-EEG  monitoring  study.  Epilepsy 
Behav. 2020;111:107271.

 21.  Pavei J, Heinzen RG, Novakova B, Walz R, Serra AJ, Reuber M, 
et al. Early seizure detection based on cardiac autonomic regu-
lation dynamics. Front Physiol. 2017;8:765.

 22.  Bruno  E,  Simblett  S,  Lang  A,  Biondi  A,  Odoi  C,  Schulze-
Bonhage  A,  et  al.  Wearable  technology  in  epilepsy:  the  views 
of  patients,  caregivers,  and  healthcare  professionals.  Epilepsy 
Behav. 2018;85:141–9.

SETH ET AL. 
   
58 

| 

 23.  Vegesna  A, Tran  M,  Angelaccio  M,  Arcona  S.  Remote  patient 
monitoring  via  non-invasive  digital  technologies:  a  systematic 
review. Telemed J E Health. 2017;23(1):3–17.

algorithm  for  patients  with  epilepsy  using  a  portable  electro-
cardiogram recorder. Annu Int Conf IEEE Eng Med  Biol Soc. 
2017;2017:4082–5.

 24.  Meisel C, El Atrache R, Jackson M, Schubach S, Ufongene C, 
Loddenkemper  T.  Machine  learning  from  wristband  sensor 
data  for  wearable,  noninvasive  seizure  forecasting.  Epilepsia. 
2020;61(12):2653–66.

 39.  Jeppesen  J,  Fuglsang-Frederiksen  A,  Johansen  P,  Christensen 
J, Wustenhagen S, Tankisi H, et al. Seizure detection based on 
heart rate variability using a wearable electrocardiography de-
vice. Epilepsia. 2019;60(10):2105–13.

 25.  Whiting  PF,  Rutjes  AW,  Westwood  ME,  Mallett  S,  Deeks  JJ, 
Reitsma  JB,  et  al.  QUADAS-2:  a  revised  tool  for  the  quality 
assessment  of  diagnostic  accuracy  studies.  Ann  Intern  Med. 
2011;155(8):529–36.

 40.  Lazeron  RHC,  Thijs  RD,  Arends  J,  Gutter  T,  Cluitmans  P, 
van  Dijk  J,  et  al.  Multimodal  nocturnal  seizure  detection:  do 
we  need  to  adapt  algorithms  for  children?  Epilepsia  Open. 
2022;7(3):406–13.

 26.  Beniczky  S,  Ryvlin  P.  Standards  for  testing  and  clinical  vali-
dation  of  seizure  detection  devices.  Epilepsia.  2018;59(Suppl 
1):9–13.

 27.  Ali SN, Alam MJ. editorsDevelopment of a wearable 3-risk fac-
tor  accumulated  epileptic  seizure  detection  system  with  IoT 
based warning alarm. 2020 IEEE 5th International Conference 
on Computing Communication and Automation (ICCCA) 2020 
30–31 Oct. 2020.

 28.  Arends J, Thijs RD, Gutter T, Ungureanu C, Cluitmans P, van 
Dijk  J,  et  al.  Multimodal  nocturnal  seizure  detection  in  a  res-
idential  care  setting:  a  long-term  prospective  trial.  Neurology. 
2018;91(21):e2010–9.

 29.  Bottcher  S,  Bruno  E,  Epitashvili  N,  Dumpelmann  M,  Zabler 
N, Glasstetter M, et al. Intra- and inter-subject perspectives on 
the detection of focal onset motor seizures in epilepsy patients. 
Sensors. 2022;22(9):1–20.

 30.  Bruno E, Biondi A, Richardson MP, Consortium O. Digital se-
miology and time-evolution pattern of bio-signals in focal onset 
motor seizures. Seizure. 2021;87:114–20.

 31.  Cogan  D,  Birjandtalab  J,  Nourani  M,  Harvey  J,  Nagaraddi  V. 
Multi-biosignal analysis for epileptic seizure monitoring. Int J 
Neural Syst. 2017;27(1):1650031.

 32.  Cogan D, Nourani M, Harvey J, Nagaraddi V. Epileptic seizure 
detection using wristworn biosensors. Annu Int Conf IEEE Eng 
Med Biol Soc. 2015;2015:5086–9.

 33.  Forooghifar F, Aminifar A, Cammoun L, Wisniewski I, Ciumas 
C, Ryvlin P, et al. A self-aware epilepsy monitoring system for 
real-time  epileptic  seizure  detection.  Mobile  Networks  Appl. 
2019;27(2):677–90.

 34.  Hegarty-Craver M, Kroner BL, Bumbut A, DeFilipp SJ, Gaillard 
WD, Gilchrist KH. Cardiac-based detection of seizures in chil-
dren with epilepsy. Epilepsy Behav. 2021;122:108129.

 35.  Henze  J,  Houta  S,  Surges  R,  Kreuzer  J,  Bisgin  P.  editorsMul-
timodal  detection  of  tonic–clonic  seizures  based  on  3D  ac-
celeration  and  heart  rate  data  from  an  in-ear  sensor.  Pattern 
recognition  ICPR  international  workshops  and  challenges. 
Cham:  Springer  Science  and  Business  Media  Deutschland 
GmbH; 2021.

 36.  Jahanbekam  A,  Baumann  J,  Nass  RD,  Bauckhage  C,  Hill  H, 
Elger  CE,  et  al.  Performance  of  ECG-based  seizure  detection 
algorithms  strongly  depends  on  training  and  test  conditions. 
Epilepsia Open. 2021;6(3):597–606.

 37.  Jeppesen  J,  Fuglsang-Frederiksen  A,  Johansen  P,  Christensen 
J,  Wustenhagen  S,  Tankisi  H,  et  al.  Seizure  detection  using 
heart rate variability: a prospective validation study. Epilepsia. 
2020;61(Suppl 1):S41–6.

 38.  Jeppesen  J,  Beniczky  S,  Fuglsang  Frederiksen  A,  Sidenius 
Johansen  P.  Modified  automatic  R-peak  detection 

P, 

 41.  Massé F, Bussel MV, Serteyn A, Arends J, Penders J. Miniaturized 
wireless  ECG  monitor  for  real-time  detection  of  epileptic  sei-
zures. ACM Trans Embedded Comput Syst. 2013;12(4):1–21.
 42.  Munch  Nielsen  J,  Zibrandtsen  IC,  Masulli  P,  Lykke  Sørensen 
T,  Andersen  TS,  Wesenberg  KT.  Towards  a  wearable  multi-
modal seizure detection system in epilepsy: a pilot study. Clin 
Neurophysiol. 2022;136:40–8.

 43.  Tang  J,  El  Atrache  R,  Yu  S,  Asif  U,  Jackson  M,  Roy  S,  et  al. 
Seizure  detection  using  wearable  sensors  and  machine  learn-
ing: setting a benchmark. Epilepsia. 2021;62(8):1807–19.

 44.  van Andel J, Ungureanu C, Arends J, Tan F, Van Dijk J, Petkov G, 
et al. Multimodal, automated detection of nocturnal motor sei-
zures at home: is a reliable seizure detector feasible? Epilepsia 
Open. 2017;2(4):424–31.

 45.  Vandecasteele  K,  De  Cooman  T,  Gu  Y,  Cleeren  E,  Claes  K, 
Paesschen  WV,  et  al.  Automated  epileptic  seizure  detection 
based  on  wearable  ECG  and  PPG  in  a  hospital  environment. 
Sensors. 2017;17(10):1–12.

 46.  Zsom A, Lafrance WC, Blum AS, Li P, La W, Shaikh MA, et al. 
Ictal  autonomic  activity  recorded  via  wearable-sensors  plus 
machine  learning  can  discriminate  epileptic  and  psychogenic 
nonepileptic  seizures.  Annu  Int  Conf  IEEE  Eng  Med  Biol 
Soc.  2019;2019:3502–6.  https:// doi. org/ 10. 1109/ EMBC. 2019. 
8857552

 47.  Al-Bakri  AF,  Villamar  MF,  Haddix  C,  Bensalem-Owen  M, 
Sunderam  S.  Noninvasive  seizure  prediction  using  autonomic 
measurements  in  patients  with  refractory  epilepsy.  Annu  Int 
Conf IEEE Eng Med Biol Soc. 2018;2018:2422–5.

 48.  Stirling  RE,  Grayden  DB,  D'Souza  W,  Cook  MJ,  Nurse  E, 
Freestone DR, et al. Forecasting seizure likelihood with wear-
able technology. Front Neurol. 2021;12:704060.

 49.  Yamakawa  T,  Miyajima  M,  Fujiwara  K,  Kano  M,  Suzuki  Y, 
Watanabe Y, et al. Wearable epileptic seizure prediction system 
with  machine-learning-based  anomaly  detection  of  heart  rate 
variability. Sensors. 2020;20(14):1–16.

 50.  Iman  M,  Arabnia  HR,  Rasheed  K.  A  review  of  deep  transfer 
learning  and  recent  advancements.  Dent  Tech.  2023;11(2):40. 
https:// doi. org/ 10. 3390/ techn ologi es110 20040 

 51.  Fleming S, Thompson M, Stevens R, Heneghan C, Plüddemann 
A,  Maconochie  I,  et  al.  Normal  ranges  of  heart  rate  and  re-
spiratory  rate  in  children  from  birth  to  18 years  of  age: 
a  systematic  review  of  observational  studies.  Lancet. 
2011;377(9770):1011–8.

 52.  van  Elmpt  WJ,  Nijsen  TM,  Griep  PA,  Arends  JB.  A  model  of 
heart rate changes to detect seizures in severe epilepsy. Seizure. 
2006;15(6):366–75.

 53.  Atwood  AC,  Drees  CN.  Seizure  detection  devices:  five  new 

things. Neurol Clin Pract. 2021;11(5):367–71.

SETH ET AL. 
 
 54.  Myers  KA,  Sivathamboo  S,  Perucca  P.  Heart  rate  variability 
measurement in epilepsy: how can we move from research to 
clinical practice? Epilepsia. 2018;59(12):2169–78.

 55.  Arbune AA, Jeppesen J, Conradsen I, Ryvlin P, Beniczky S. Peri-
ictal  heart  rate  variability  parameters  as  surrogate  markers  of 
seizure severity. Epilepsia. 2020;61(Suppl 1):S55–60.

 56.  Acharya UR, Hagiwara Y, Adeli H. Automated seizure predic-

tion. Epilepsy Behav. 2018;88:251–61.

 57.  Bosl WJ, Leviton A, Loddenkemper T. Prediction of seizure re-
currence. A note of caution. Front Neurol. 2021;12:675728.
 58.  Billeci  L,  Marino  D,  Insana  L,  Vatti  G,  Varanini  M.  Patient-
specific  seizure  prediction  based  on  heart  rate  variability  and 
recurrence  quantification  analysis.  PloS  One.  2018;13(9): 
e0204339.

 59.  Nasseri M, Nurse E, Glasstetter M, Bottcher S, Gregg NM, Laks 
Nandakumar  A,  et  al.  Signal  quality  and  patient  experience 
with  wearable  devices  for  epilepsy  management.  Epilepsia. 
2020;61(Suppl 1):S25–35.

 60.  Beniczky S, Wiebe S, Jeppesen J, Tatum WO, Brazdil M, Wang 
Y,  et  al.  Automated  seizure  detection  using  wearable  de-
vices:  a  clinical  practice  guideline  of  the  international  league 

|  59

against  epilepsy  and  the  International  Federation  of  Clinical 
Neurophysiology. Clin Neurophysiol. 2021;132(5):1173–84.
 61.  Bruno  E,  Böttcher  S,  Viana  PF,  Amengual-Gual  M,  Joseph  B, 
Epitashvili N, et al. Wearable devices for seizure detection: prac-
tical  experiences  and  recommendations  from  the  wearables 
for  epilepsy  and  research  (WEAR)  international  study  group. 
Epilepsia: John Wiley and Sons Inc; 2021. p. 2307–21.

 62.  Sivathamboo S, Nhu D, Piccenna L, Yang A, Antonic-Baker A, 
Vishwanath S, et al. Preferences and user experiences of wear-
able devices in epilepsy: a systematic review and mixed-meth-
ods synthesis. Neurology. 2022;99(13):e1380–92.

How to cite this article: Seth EA, Watterson J, 
Xie J, Arulsamy A, Md Yusof HH, Ngadimon IW, 
et al. Feasibility of cardiac-based seizure detection 
and prediction: A systematic review of non-invasive 
wearable sensor-based studies. Epilepsia Open. 
2024;9:41–59. https://doi.org/10.1002/epi4.12854

SETH ET AL.
