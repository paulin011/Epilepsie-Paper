# Ode et al. - 2023 - Development of an epileptic seizure prediction algorithm using R–R intervals with self-attentive aut

Artificial Life and Robotics (2023) 28:403–409 
https://doi.org/10.1007/s10015-022-00832-0

ORIGINAL ARTICLE

Development of an epileptic seizure prediction algorithm using R–R 
intervals with self‑attentive autoencoder

Rikumo Ode1,2 · Koichi Fujiwara1,2,4 · Miho Miyajima2 · Toshikata Yamakawa3 · Manabu Kano4 · Kazutaka Jin5 · 
Nobukazu Nakasato5 · Yasuko Sawai6 · Toru Hoshida6 · Masaki Iwasaki7 · Yoshiko Murata7 · Satsuki Watanabe7 · 
Yutaka Watanabe7 · Yoko Suzuki2 · Motoki Inaji2 · Naoto Kunii8 · Satoru Oshino9 · Hui Ming Khoo9 · 
Haruhiko Kishima9 · Taketoshi Maehara2

Received: 15 May 2022 / Accepted: 15 November 2022 / Published online: 27 November 2022 
© The Author(s) 2022

Abstract
Epilepsy is a neurological disorder that may affect the autonomic nervous system (ANS) from 15 to 20 min before seizure 
onset, and disturbances of ANS affect R–R intervals (RRI) on an electrocardiogram (ECG). This study aims to develop a 
machine learning algorithm for predicting focal epileptic seizures by monitoring R–R interval (RRI) data in real time. The 
developed algorithm adopts a self-attentive autoencoder (SA-AE), which is a neural network for time-series data.The results 
of applying the developed seizure prediction algorithm to clinical data demonstrated that it functioned well in most patients; 
however, false positives (FPs) occurred in specific participants. In a future work, we will investigate the causes of FPs and 
optimize the developing seizure prediction algorithm to further improve performance using newly added clinical data.

Keywords  Epilepsy · Electrocardiogram · Machine learning · Self-attentive autoencoder

This work was presented in part at the joint symposium of the 
27th International Symposium on Artificial Life and Robotics, 
the 7th International Symposium on BioComplexity, and the 5th 
International Symposium on Swarm Behavior and Bio-Inspired 
Robotics (Online, January 25–27, 2022).

 *  Koichi Fujiwara 

fujiwara.koichi@hps.material.nagoya-u.ac.jp

1  Department of Material Engineering, Nagoya University, 

Nagoya, Japan

2  Tokyo Medical and Dental University, Tokyo, Japan
3  Kumamoto University, Kumamoto, Japan
4  Kyoto University, Kyoto, Japan
5  Tohoku University, Sendai, Japan
6  National Hospital Organization Nara Medical Center, Nara, 

Japan

7  National Center of Neurology and Psychiatry, Kodaira, Japan
8  Tokyo University, Tokyo, Japan
9  Osaka University, Suita, Japan

1  Introduction

Epilepsy is a neurological disorder that causes recurrent 
seizures and affects about 1 % of the global population [1]. 
Although 70–80% of epilepsy patients can control seizures 
by taking appropriate medications, the remaining 20–30% of 
patients have intractable epilepsy that cannot be controlled 
with current therapies. In addition, women of childbearing 
potential may not be able to take antiepileptic drugs due to 
teratogenicity [2].

Epileptic seizures are caused by excessive electric dis-
charge in the cerebrum, which also may affect the autonomic 
nervous system (ANS) from 15 to 20 min before seizure 
onset [3]. The alteration in ANS affects heart rate variability 
(HRV), which is defined as fluctuations of R–R intervals 
(RRI) on an electrocardiogram (ECG). RRI is the temporal 
distance derived from the interval between two adjacent R 
waves, as shown in Fig. 1.

Taking this effect into account, Fujiwara et al. have devel-
oped an algorithm for predicting epileptic seizures by means 
of multivariate statistical process control (MSPC) using 
HRV features. MSPC is a well-known anomaly detection 
method used mainly in the process industry. Fujiwara et al 
reported that their algorithm could predict seizures with high 

Vol.:(0123456789)1 3 
404 

Artificial Life and Robotics (2023) 28:403–409

Fig. 1   ECG trace and RRI

sensitivity and a low false positive (FP) rate [4]. According 
to a guideline on HRV analysis [5], RRI data for at least two 
to three minutes are needed to extract HRV features, which 
means that patients must wait for a few minutes before Fuji-
wara’s algorithm can be utilized. This fact motivated us to 
develop a new epileptic seizure prediction algorithm with a 
short downtime before algorithm start, preferably less than 
one minute.

It has been reported that RRIs become shorter around 
the time of epileptic seizures, a fact that could be used as a 
simple method for assessing ANS of epileptic patients [6]. 
It may be possible to shorten the downtime before the algo-
rithm starts using raw RRI data for epileptic seizure predic-
tion, as compared with using HRV features, by means of 
an anomaly detection framework. Thus, this study aims to 
develop a new machine learning algorithm for predicting 
focal epileptic seizures using RRI directly.

2   Methods

2.1   Self‑attentive autoencoder

Autoencoder (AE) is a type of neural network model that is 
often used for unsupervised learning and in which outputs 
become close to inputs due to a latent function of hidden lay-
ers [7]. Figure 2 shows a network diagram of one example of 
AE. An objective function of the training is to minimize the 
following reconstruction error RE, RE as follows:

Fig. 2   Schematic diagram of AE

output. Figure 3 illustrates an SA-AE model with inputs of 
RRI data. The RRI data are designated as queries, keys, and 
values, each of which are divided by time windows. The atten-
tion weight of RRI is obtained by calculating dot products of 
the queries and the keys. Finally, the SA mechanism recon-
structs the RRI data by multiplying the values by the attention 
weights, which is expected to suitably take into account the 
time-dependency of the RRI data.

Attention(Q, K, V) =softmax

�

QKT

V,

dk �

(2)

√

The output of the SA mechanism is calculated in accordance 
with Eq. (2). Q, K, V are the matrixes of the queries, the 
keys, and the values, respectively, dk is the dimension of the 
query, and softmax
 indicates attention weight of the 
�
SA mechanism, which will take a larger value if the similar-
ity between the Q and K components is high, and a smaller 
dk , we can 
value if the similarity is low. By divide Q, K by 

QKT
dk

�

√

√

RE =

N

i=1
�

xi − x′

i

,

(1)

‖

‖

where xi is input features, N is the number of features, and 
x′
i is features restored by an AE model.

Self-attentive autoencoder (SA-AE) is an extension of 
the AE model with a self-attention (SA) mechanism in the 
hidden layer, which is usually used for time-series analysis.
An SA mechanism is a method for learning important 
dependence in the input time-series data for determining the 

Fig. 3   Schematic diagram of SA-AE

1 3Artificial Life and Robotics (2023) 28:403–409 

405

prevent the dot products becoming large and pushing the 
softmax function into regions where it has extremely small 
gradients [8].

2.2   Anomaly detection

Anomaly detection refers to a framework for finding pat-
terns in data that do not conform to expected patterns. 
This framework uses only normal data as training data to 
learn patterns in said data. This learning method can deter-
mine whether the input data are normal or have abnormal 
patterns even if it is difficult to collect data containing 
anomalies.

In the proposed epileptic seizure prediction algorithm, 
the  input  values  of  SA-AE  are  the  original  RRI  data, 
and the output values are the RRI data reconstructed by 
SA-AE.  Algorithm  1  was  adopted  to  train  the  SA-AE 
model before seizure prediction. In this algorithm, y[i]
 indi-
cates the ith RRI segment clipped from the original RRI 
data with a window having a size of W, T represents the 
measured time length, Pi represents ith patients, and Itrain 
is the number of patients. The interictal RRI segments of 
̃X in steps 1–4 and 
each patient are merged into one matrix 
are standardized into zero-means and a standard deviation 
of one in step 5. The SA-AE model is trained with X in 
step 6. Finally, in steps 7 and 8, the control limit of RE is 
determined for each patient and denoted as RE[i]
.

After training the SA-AE model and setting an appro-
priate control limit RE , epileptic seizure prediction is per-
formed based on Algorithm 2. C represents the patient’s 
condition ( N  : Normal, A : Abnormal), so that ¬N = A and 
vice versa. 𝜏 represents the time exceeding RE if C = N  , 
and the time below the control limit if C = A .  𝜏  is the 
time threshold, which is intended to reduce FPs, since even 
routine activities such as eating, walking, and turning can 
cause ECG artifacts and easily disrupt the RRI. Setting 𝜏 
larger than one is useful to suppress the influence of ECG 
artifacts and reduce FPs. In steps 3–5, the newly input RRI 
is standardized, and the RE is calculated using the trained 
SA-AE model. If RE continuously exceeds RE for more 
than 𝜏  when the patient’s status is  N  , the status of the 
patient is determined to be A , since persistence of a large 
RE means that there is some abnormality. On the other 
hand, if RE continuously stays below RE for more than 𝜏 
when the patient’s status is A , the status of the patient is 
determined to be N .

In steps 5–13, the patient’s status is determined to be 
normal N  or abnormal A . If Algorithm 2 can successfully 
detect abnormal changes in RRI before a seizure, the patient 
would be able know in advance that a seizure could occur 
and take appropriate actions to prevent injury or accidents 
caused by epileptic seizures.

In this study, the seizure prediction algorithm is stopped 
for 30 min to restore ANS to its normal state once a seizure 
is predicted.

2.3   Data description

We collected clinical RRI data from 39 patients with focal 
epilepsy  who  were  admitted  to  the  Medical  Hospital  of 
Tokyo Medical and Dental University (TMDU), the National 
Hospital  Organization  Nara  Medical  Center  (NMC), 
National Center of Neurology and Psychiatry (NCNP) Hos-
pital, Tohoku University Hospital (TUH), Osaka Univer-
sity Hospital Epilepsy Center (OUHEC), and University of 
Tokyo Hospital (UTH) to monitor clinical video-EEG. Sei-
zure onsets were identified by clinical epilepsy specialists, 
certified by the Japan Epilepsy Society, based on the video-
EEG monitoring data. Collection and analysis of the clini-
cal data were approved by the Ethics Committee of TMDU, 
NMC, NCNP, TUH, OUHEC, and UTH. In addition to our 
collected data, we also retrieved data of 27 European partial 

1 3406 

Artificial Life and Robotics (2023) 28:403–409

epileptic patients from the European epilepsy database [11] 
to evaluate ethnic differences.

Training data included 131 interictal episodes for 77.4 h 
and validation data consisted of 264 interictal and 85 preictal 
episodes for a total of 195 h. The type of partial epilepsy 
varied for each patient, including temporal lobe epilepsy 
(TLE), frontal lobe epilepsy (FLE), and parietal lobe epi-
lepsy (PLE). The mean age of patients was 36.4 ± 13.7. 45 
patients were male, and 21 were female.

3   Results

3.1   Condition for seizure prediction

We trained the SA-AE model in accordance with Algo-
rithm 1 with the training data and evaluated its performance 
in accordance with Algorithm 2 using the validation data. 
The hyperparameters such as the number of units in the hid-
den layer and the internal function of the SA mechanism 
were determined by Optune™, which is a type of a Bayesian 
optimization library implemented in Python [10].

In this study, the control limit of RE was determined 
based on the 99% confidence limit, and the time threshold 
was set to eight seconds. They were determined by means 
of grid search.

3.2   Seizure prediction performance

The overall results showed that sensitivity, precision, FP 
rate, and Area Under Curve (AUC) of the trained SA-AE 
model were 74%, 0.35, 0.85 times/h, and 0.97, respectively. 
A sensitivity of 100% was achieved in 29 patients, eight of 
whom had no FP.

Figure 4 shows an example of a seizure prediction result 
for patient A (male, 41 years old, right TLE). The top and 
bottom figures show the preictal and interictal episodes, 
respectively. The green area is the period that the algorithm 
determined as abnormal, and the blue area is the period dur-
ing which seizure prediction was stopped.

The abnormal condition was detected before seizure onset 
in the preictal episode, while RE was monotonic and stayed 
below the control limits in the interictal episode. It indicates 
that seizure prediction with the proposed algorithm func-
tioned well for patient A.

4   Discussion

In this study, the RRI-based epileptic seizure prediction 
model was trained utilizing SA-AE, which achieved a sen-
sitivity of 74% and an FP rate of 0.85 times/h. To confirm the 
validity of the trained model, we compared its performance 

Fig. 4   Seizure  prediction  results  of  patient  A  for  preictal  data  (top) 
and interictal period data (bottom)

Table 1   The result of seizure prediction of each model

Algorithm

Sensitivity

SA-AE
AE
LSTM-AE

74
74
81

FP rate 
[times/h]

0.85
1.30
1.50

Precision

AUC 

0.35
0.28
0.26

0.97
0.93
0.90

with other models using only the RRI as input. The com-
pared models were an AE model without the SA mechanism 
and a long short-term memory (LSTM) network with a hid-
den layer of AE.

Table 1 shows the comparison results. The SA-AE model 
was  able  to  predict  seizures  with  the  highest  precision 
among the three models. In particular, the result suggests 
that the SA mechanism helps reduce FPs since the sensitiv-
ity of SA-AE was the same as that of AE while the FP rate 
was the lowest.

The  seizure  prediction  performance  varied  for  each 
patient. Figure 5 shows histograms and a box plot of FP 
rates per patient, which indicate that only six patients had 
an FP rate of more than 2.5 times/h.

We checked the profile of patient B (male, 46 years old, 
localization-related  epilepsy,  Rt  temporal  lobe  epilepsy 
s/o), whose FP rate was 2.6 times/h. As shown in Fig. 6, 
the change in RE in patient B was more intense than in 
patient A. Although there were no significant findings in 
the video monitoring data or complications, the brain struc-
ture in localization-related epilepsy is problematic, and its 
epileptic focus is difficult to identify. Thus, the effect on 
ANS before seizures may be different from other types of 
epilepsy. Lehtimäki et al. suggested that a single seizure 
triggers  inflammatory  signals  in  patients  with  chronic 

1 3Artificial Life and Robotics (2023) 28:403–409 

407

Fig. 5   Histograms of FP rates per patient for seizure prediction

Fig. 7   Seizure prediction results of patient C for preictal data (upper) 
and interictal period data (lower)

significant autonomic dysregulation compared to nontem-
poral ictal activity [13]. Repetitive stimulation of the cen-
tral autonomic network by epileptic discharges may result in 
interictal dysfunction of the autonomic nervous system [14]. 
It is possible that the interictal RRI of patient C deviated 
from those of other patients included in the training data, 
due to pathological cardiac autonomic activity caused by 
chronic BTLE. This could be the rationale for setting a large 
control limit for patient C.

Poor seizure prediction performance of other patients may 
have been caused by motion artifacts contaminating the RRI 
data. In addition, alteration of ANS may induce FPs. It is 
well known that there is a close relationship between the 
activities of ANS and epileptic seizures [3]. In addition, it 
has been reported that ANS activities tend to be impaired 
in patients with anxiety disorders. Thus, poor mental condi-
tions like anxiety may affect ANS, and such alterations of 
ANS may be detected by the SA-AE model as FPs. It is also 
possible that the SA-AE model could not capture changes in 
RRI well, because the characteristics of the RRI data used 
as training data were different from those of such patients. 
Thus, it is necessary to individually tune hyperparameters 
of the seizure prediction algorithm to cover typical causes 
of FP.

The attention mechanism adopted in SA-AE is a method 
for  identifying  which  parts  of  the  input  data  contribute 
to output calculation. In natural language processing, for 
instance, the attention mechanism identifies important words 
for sentence understanding, which is capable of interpreta-
tion even for humans [15]. However, in the proposed epilep-
tic seizure prediction model, it is difficult to understand the 
meaning of important RRIs. Instead of interpretations about 
each RRI, we focus on co-occurrence information about 
important RRIs for seizure prediction in the SA-AE model. 

Fig. 6   Seizure prediction results of patient B for preictal data (upper) 
and interictal period data (lower)

localization-related epilepsy, which may lead to structural 
changes in neural tissue [12].

The AUC exceeded 0.9 in almost all patients; however, 
the AUC of patient C [male, 50 years old, bitemporal lobe 
epilepsy (BTLE)] was 0.56. Figure 7 shows his seizure pre-
diction results, in which changes in RE were different from 
those of patients A and B for whom no significant changes 
were observed even in the preictal period. Patient C may 
have problems other than epilepsy since his seizures could 
not be predicted with any model, but a detailed profile of 
him is unknown. In addition, his control limit was much 
larger than those of other patients.

Page et al. reported that bitemporal ictal activity detected 
by  intracranial  depth  EEG  monitoring  induced  more 

1 3408 

Artificial Life and Robotics (2023) 28:403–409

patients. In future works, we aim to further improve the sei-
zure prediction performance by optimizing the parameters 
of the model or developing a new seizure prediction model. 
In addition, we will collect more clinical data to investigate 
typical causes of FPs in epileptic seizure prediction.

Acknowledgements  This work was supported in part by the research 
project for medical-engineering collaboration and implementation of 
artificial intelligence from Japan Agency for Medical Research and 
Development (AMED) Grant Number 21445838.

Open Access  This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, 
provide a link to the Creative Commons licence, and indicate if changes 
were made. The images or other third party material in this article are 
included in the article's Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in 
the article's Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will 
need to obtain permission directly from the copyright holder. To view a 
copy of this licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.

Fig. 8   Heatmaps  of  the  correlation  matrix  of  attention  weights  of 
Patient  A  (top)  and  Patient  C  (bottom);  left  and  right  figures  are  in 
inter- and peri-ictal periods, respectively

References

Figure 8 shows a correlation matrix of the attention weights 
in the attention layer of the trained SA-AE model. The size 
of the correlation matrix was 45× 45 because the length of 
the time window of the input RRI data for the trained SA-AE 
model was 45 seconds.

The correlation matrixes of the attention weights in inter-
ictal and preictal periods of Patient A who had a high sensi-
tivity and a low FP rate as shown in Fig. 8a, b. These figures 
indicate that RRIs close to each other contributed to the 
prediction in Patient A. On the other hand, in Patient C, as 
shown in Fig. 8c, d, RRIs wider than those in Patient A were 
used. That is, the SA-AE model might not find important 
information for seizure prediction in the input RRI data. This 
characteristic in the attention weights was common among 
some patients with poor seizure prediction performance. 
Therefore, it may be possible to identify participants for 
whom seizure prediction is effective by checking the atten-
tion weights.

5   Conclusion

In this study, we proposed an anomaly detection algorithm 
for epileptic seizure prediction based on an SA-AE model. 
The  results  of  applying  the  proposed  algorithm  to  the 
clinical data demonstrated that it functioned well in some 
patients; however, further improvements in prediction per-
formance are needed to clinically apply it to more epilepsy 

  1.  Thurman David J, Ettore Beghi, Begley Charles E, Berg Anne 
T, Buchhalter Jeffrey R, Ding Ding, Hesdorffer Dale C, Allen 
Hauser W, Lewis Kazis, Rosemarie Kobau et al (2011) Standards 
for epidemiologic studies and surveillance of epilepsy. Epilepsia 
52:2–26

  2.  Jansen  Katrien  (2013)  Peri-ictal  ECG  changes  in  childhood 
epilepsy: implications for detection systems. Epilepsy Behav 
29(1):72–76

  3.  Sevcencu C, Struijk JJ (2010) Autonomic alterations and cardiac 

changes in epilepsy. Epilepsia 51:725–737

  4.  Fujiwara Koichi, Miyajima Miho, Yamakawa Toshitaka, Abe 
Erika, Suzuki Yoko, Sawada Yuriko, Kano Manabu, Maehara 
Taketoshi, Ohta Katsuya, Sasai-Sakuma Taeko et al (2015) Epi-
leptic seizure prediction based on multivariate statistical process 
control of heart rate variability features. IEEE Trans Biomed Eng 
63(6):1321–1332

  5.  Malik Marek, Bigger J Thomas, Camm A John, Kleiger Robert E, 
Malliani Alberto, Moss Arthur J, Schwartz Peter J (1996) Heart 
rate variability: standards of measurement, physiological interpre-
tation, and clinical use. Eur Heart J 17(3):345–381

  6.  Zijlmans Maeike, Flanagan Danny, Gotman Jean (2002) Heart 
rate changes and ECG abnormalities during epileptic seizures: 
prevalence and definition of an objective clinical sign. Epilepsia 
43(8):847–854

  7.  An Jinwon, Cho Sungzoon (2015) Variational autoencoder based 
anomaly detection using reconstruction probability. Spec Lect IE 
2(1):1–18

  8.  Vaswani Ashish, Shazeer Noam, Parmar Niki, Uszkoreit Jakob, 
Jones Llion, Gomez Aidan N, Kaiser Łukasz, Polosukhin Illia 
(2017) Attention is all you need. Advances in neural information 
processing systems 30:5998–6008

  9.  Fujiwara Koichi, Miyatani Shota, Goda Asuka, Miyajima Miho, 
Sasano Tetsuo, Kano Manabu (2021) Autoencoder-based extra-
systole detection and modification of RRI data for precise heart 
rate variability analysis. Sensors 21(9):3252

 10.  Akiba T, Sano S, Yanase T, Ohta T, Koyama M (2019) Optuna: 
a  next-generation  hyperparameter  optimization  framework. 

1 3Artificial Life and Robotics (2023) 28:403–409 

409

Proceedings of the 25th ACM SIGKDD international conference 
on knowledge discovery & data mining, pp 2623–2631

 11.  Ihle M, Feldwisch-Drentrup H, Teixeira CA, Witon A, Schel-
ter B, Timmer J, Schulze-Bonhage A (2012) EPILEPSIAE - a 
European epilepsy database. Comput Methods Programs Biomed 
106(3):127–138

 12.  Lehtimäki KA, Keränen T, Palmio J, Mäkinen R, Hurme M, Hon-
kaniemi J, Peltola J (2007) Increased plasma levels of cytokines 
after seizures in localization-related epilepsy. Acta Neurol Scand 
116(4):226–230

 13.  Page Thomas, Rugg-Gunn Fergus J (2018) Bitemporal seizure 
spread and its effect on autonomic dysfunction. Epilepsy Behav 
84:166–172

 14.  Mazzola L, Rheims S (2021) Ictal and interictal cardiac manifesta-
tions in epilepsy. A review of their relation with an altered central 
control of autonomic functions and with the risk of SUDEP. Front 
Neurol 12:642645

 15.  Vig J (2019) A multiscale visualization of attention in the trans-

former model, arXiv preprint arXiv: 1906. 05714

Publisher's  Note  Springer  Nature  remains  neutral  with  regard  to 
jurisdictional claims in published maps and institutional affiliations.

1 3
