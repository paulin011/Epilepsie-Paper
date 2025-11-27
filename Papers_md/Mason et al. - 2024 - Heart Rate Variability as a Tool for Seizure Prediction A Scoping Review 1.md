# Mason et al. - 2024 - Heart Rate Variability as a Tool for Seizure Prediction A Scoping Review 1

Review
Heart Rate Variability as a Tool for Seizure Prediction:
A Scoping Review

Federico Mason 1
Luca Vignatelli 2,*

, Anna Scarabello 1, Lisa Taruffi 1, Elena Pasini 2

, Giovanna Calandra-Buonaura 1,2,

and Francesca Bisulli 1,2

1 Department of Biomedical and Neuromotor Sciences, University of Bologna, 40126 Bologna, Italy;

federico.mason@unibo.it (F.M.); anna.scarabello@studio.unibo.it (A.S.); lisa.taruffi@studio.unibo.it (L.T.);
giovanna.calandra@unibo.it (G.C.-B.); francesca.bisulli@unibo.it (F.B.)
IRCCS Institute of Neurological Sciences of Bologna, Full Member of the European Reference Network
EpiCARE, 40139 Bologna, Italy; elena.pasini@isnb.it

2

* Correspondence: l.vignatelli@ausl.bologna.it

Abstract: The most critical burden for People with Epilepsy (PwE) is represented by seizures, the
unpredictability of which severely impacts quality of life. The design of real-time warning systems
that can detect or even predict ictal events would enhance seizure management, leading to high
benefits for PwE and their caregivers. In the past, various research works highlighted that seizure
onset is anticipated by significant changes in autonomic cardiac control, which can be assessed
through heart rate variability (HRV). This manuscript conducted a scoping review of the literature
analyzing HRV-based methods for detecting or predicting ictal events. An initial search on the
PubMed database returned 402 papers, 72 of which met the inclusion criteria and were included in the
review. These results suggest that seizure detection is more accurate in neonatal and pediatric patients
due to more significant autonomic modifications during the ictal transitions. In addition, conventional
metrics are often incapable of capturing cardiac autonomic variations and should be replaced with
more advanced methodologies, considering non-linear HRV features and machine learning tools
for processing them. Finally, studies investigating wearable systems for heart monitoring denoted
how HRV constitutes an efficient biomarker for seizure detection in patients presenting significant
alterations in autonomic cardiac control during ictal events.

Keywords: seizure detection; seizure prediction; heart rate variability; epilepsy

1. Introduction

Epileptic seizures represent the main burden for People with Epilepsy (PwE), who,
because of ictal events, may suffer physical injuries, loss of consciousness, and, in the most
dangerous cases, status epilepticus and Sudden Unexpected Death in Epilepsy (SUDEP) [1].
The unpredictability of seizures leads PwE to experience anxiety and depression, signifi-
cantly affecting their quality of life (QoL) [2]. In this context, the implementation of real-time
warning systems that can detect or predict seizures would enhance the management of
these episodes, leading to high benefits to both PwE and their caregivers [3].

In the past decades, it has been recognized that PwE present a complex interaction
between brain and heart. Some studies have suggested alterations in autonomic activity
following focal seizures spreading into cortical structures such as the amygdala, insula,
and cingulate gyrus, with possible involvement of the thalamus and hypothalamus [4].
In Temporal Lobe Epilepsy (TLE), ictal events often correlate with tachycardia, which
may precede seizure onset by seconds to minutes [5]. At the same time, in some cases,
ictal bradycardia can also be observed [6]. In general, it remains challenging to assess the
role of cardiovascular dysregulation during the peri-ictal phase and its interaction with
sympathetic/parasympathetic balance.

Citation: Mason, F.; Scarabello,

A.; Taruffi, L.; Pasini, E.;

Calandra-Buonaura, G.; Vignatelli, L.;

Bisulli, F. Heart Rate Variability as

a Tool for Seizure Prediction: A

Scoping Review. J. Clin. Med. 2024, 13,

747. https://doi.org/10.3390/

jcm13030747

Received: 6 December 2023

Revised: 4 January 2024

Accepted: 22 January 2024

Published: 27 January 2024

Copyright: © 2024 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under

the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

J. Clin. Med. 2024, 13, 747. https://doi.org/10.3390/jcm13030747

https://www.mdpi.com/journal/jcm

Journal ofClinical MedicineJ. Clin. Med. 2024, 13, 747

2 of 17

Heart rate variability (HRV), defined as the variability of the intervals among con-
secutive heartbeats, is one of the most popular tools for estimating the balance between
sympathetic and parasympathetic tones [7,8]. Fluctuation in the inter-heartbeat intervals is
considered a protective mechanism to respond to sudden cardiovascular demands, and a
decreased HRV can be linked to an elevated risk of sudden cardiac death [9]. Differently
from other cardiovascular parameters, HRV can be recorded using a single-lead electro-
cardiogram (ECG), and, consequently, can be monitored through noninvasive wearable
devices, like wrist-worn smartwatches or chest-strap sensors [10,11].

In the literature, multiple studies have reported changes in cardiac autonomic control
before seizure onset, suggesting that the HRV could be a predictive biomarker of ictal
events [5,12–16]. Such evidence and the relative easiness of HRV recording have encouraged
the development of HRV-based seizure detectors, with the dual aim of improving QoL and
minimizing the risk of sudden death for PwE [17]. Despite presenting a lower accuracy
than more complex systems that integrate features of different natures, HRV-based systems
are associated with high usability and acceptability levels, enabling continuous health
monitoring even outside a clinical context [18]. To date, no detection systems have provided
accurate results over broad populations and there is no agreement on which HRV-based
features could better assess ictal events.

This manuscript consists of a scoping review of the literature analyzing HRV modifi-
cations during the peri-ictal phase and aims to provide new insights on how to develop
efficient systems for predicting seizures. Despite other reviews having been written in this
field [5,19–24], to the authors’ knowledge, these previous works did not focus on analyzing
how HRV changes during the ictal transitions but generally compared cardiac modifica-
tions between different populations or associated HRV modification with seizure severity.
The most similar work in the literature is [25], which presents significant methodological
limits since it does not follow systematic criteria for selecting the papers and comparing
their content.

2. Materials and Methods
2.1. Search Strategy

Our review followed the Preferred Reporting Items for Systematic Reviews and Meta-
Analyses (PRISMA) guidelines [26]. The PubMed database was systematically searched
for original studies investigating HRV changes during ictal periods, considering all the
works published from January 1980 to 30 June 2023. In carrying out the initial research, a
combination of synonyms of “Epilepsy” and “Heart Rate Variability” were considered as
search terms (see Table 1).

Table 1. Search strategy. If a word ended with an asterisk character, all the search terms starting with
that word were considered.

Index

Search

“Epilepsy” [Mesh] OR “Seizures” [Mesh] OR “Epilep*” [title/abstract]
OR “Seizure*” [title/abstract] OR “Ictal” [title/abstract] OR “Pre-ictal”
[title/abstract] OR “Post-ictal” [title/abstract] OR “Peri-ictal”
[title/abstract] OR “Inter-ictal” [title/abstract]

(“Time analysis” [title/abstract] OR “Power analysis” [title/abstract] OR
“Nonlinear” [title/abstract] OR “Non linear” [title/abstract] OR
“Non-linear” [title/abstract]) AND (“Electrocardiography” [Mesh] OR
“Electrocardiography” [title/abstract] OR “Electrocardiogram”
[title/abstract] OR “EKG” [title/abstract] OR “ECG” [title/abstract])

“Heart rate variability” [title/abstract] OR “HR variability”
[title/abstract]

#2 or #3

#1 and #4

1

2

3

4

5

Results

265,315

1847

23,489

24,610

402

J. Clin. Med. 2024, 13, 747

3 of 17

When selecting the papers to be included in the review, the following criteria were
considered: being written in English; considering PwE as the studied population; analyzing
HRV changes during the peri-ictal phase; and developing seizure detection tools taking
HRV measures as an input. A double-screening approach was followed where the abstract
of each record was independently analyzed by two authors (F.M. and A.S.). If there was no
concordance on discarding or including the record in the final selection, a third author (L.T.)
was asked to assess if the abstract complied with the review criteria. After the screening,
the full text of each record selected was reviewed by three authors (F.M., A.S., and L.T.)
to assess its eligibility for the final analysis. A flow chart of the full selection procedure is
given in Figure 1.

Figure 1. Flow chart of the selection procedure.

The following information was collected from each study: the heartbeat recording, the
types of HRV metrics analyzed, the algorithms implemented for classifying ictal periods,
the characteristics of the studied population, the clinical outcomes derived from the HRV
analysis (comparing different demographic groups or seizure types), and the performance
of the systems used for detecting or predicting seizures. The Supplementary Materials
provided a concise overview of key attributes found in all the scrutinized studies (see
Table S1). To synthesize the results of the review, the technical methodologies employed in
HRV processing and clinical outcomes associated with different age-stratified populations
were distinguished.

2.2. HRV Features

To estimate the HRV, it is first necessary to compute the normalized time intervals
between consecutive R peaks, denoted as Normal-to-Normal Intervals (NNIs) [27]. The
HRV can be derived from the entire NNI time series or, more commonly, a portion of
the series. In the latter scenario, the HRV depends on a subset of the NNI samples and,

J. Clin. Med. 2024, 13, x FOR PEER REVIEW 3 of 17   analyzing HRV changes during the peri-ictal phase; and developing seizure detection tools taking HRV measures as an input. A double-screening approach was followed where the abstract of each record was independently analyzed by two authors (F.M. and A.S.). If there was no concordance on discarding or including the record in the ﬁnal selection, a third author (L.T.) was asked to assess if the abstract complied with the review criteria. After the screening, the full text of each record selected was reviewed by three authors (F.M., A.S., and L.T.) to assess its eligibility for the ﬁnal analysis. A ﬂow chart of the full selection procedure is given in Figure 1.  Figure 1. Flow chart of the selection procedure. The following information was collected from each study: the heartbeat recording, the types of HRV metrics analyzed, the algorithms implemented for classifying ictal peri-ods, the characteristics of the studied population, the clinical outcomes derived from the HRV analysis (comparing diﬀerent demographic groups or seizure types), and the perfor-mance of the systems used for detecting or predicting seizures. The supplementary mate-rials provided a concise overview of key attributes found in all the scrutinized studies (see Table S1). To synthesize the results of the review, the technical methodologies employed in HRV processing and clinical outcomes associated with diﬀerent age-stratiﬁed popula-tions were distinguished. 2.2. HRV Features To estimate the HRV, it is ﬁrst necessary to compute the normalized time intervals between consecutive R peaks, denoted as Normal-to-Normal Intervals (NNIs) [27]. The HRV can be derived from the entire NNI time series or, more commonly, a portion of the series. In the latter scenario, the HRV depends on a subset of the NNI samples and, con-sequently, becomes a time-dependent variable. For such a purpose, the common choice is to select a speciﬁc time window ∆t, so that any feature HRV(t, ∆t) is computed according to the NNIs measured within time t and t + ∆t. It has been shown that the selection of ∆t strongly aﬀects the results of the HRV analysis [20], trading oﬀ between estimation J. Clin. Med. 2024, 13, 747

4 of 17

consequently, becomes a time-dependent variable. For such a purpose, the common choice
is to select a specific time window ∆t, so that any feature HRV(t, ∆t) is computed according
to the NNIs measured within time t and t + ∆t. It has been shown that the selection of
∆t strongly affects the results of the HRV analysis [20], trading off between estimation
accuracy and time sensitivity. A schematic representation of the HRV extraction process is
given in Figure 2.

Figure 2. HRV extraction process. NNI = Normal-to-Normal Interval; LF = Low Frequency; HF = High
Frequency; AVNN = Average of the NNI series; SDNN = Standard Deviation of the NNI series;
AVSD = Average of the subsequent NNI difference series; SDSD = Standard Deviation of the subse-
quent NNI difference series; RMSSD = Root Mean Square of the subsequent NNI difference series;
ppNN50 = percentage of NNIs differing more than 50 ms.

HRV metrics include three broad families, namely the time-based features, directly
computed from the NNI series, the frequency-based features, computed from the spectrum
of the NNI series, and the non-linear features [28]. The most common time-based features
are the Average (AVNN) and the Standard Deviation (SDNN) of the NNI series. The latter
denotes the tendency of NNI to keep a constant value and represents a naïve estimate
for the HRV. From the NNI series, it is possible to extract the series SD of subsequent
NNI differences SDi = NN Ii+1 − NN Ii and compute the Average (AVSD), the Standard
Deviation (SDSD), and the Root Mean Square (RMSSD) of SD. Another time-based feature
is the percentage (ppNNτ) of NNIs differing more than τ milliseconds during a specific
interval, where τ is usually set to 50 ms or 20 ms. The RMSSD and ppNN50 are both
recognized as two biomarkers of the vagal tone. More advanced time-based features
include the width and the integral of the NNI distribution, where the latter is known as the
triangular index.

To compute HRV metrics in the frequency domain, it is first necessary to implement a
time-frequency transformation, using methods such as the Fast Fourier Transform (FFT)
and the discrete wavelet transform [29,30]. The latter enables higher flexibility in terms
of time-frequency accuracy and does not require the segmentation of the NNI series into
windows. After estimating the HRV spectrum, the naïve choice is to compute the energy of

J. Clin. Med. 2024, 13, x FOR PEER REVIEW 4 of 17   accuracy and time sensitivity. A schematic representation of the HRV extraction process is given in Figure 2.  Figure 2. HRV extraction process. NNI = Normal-to-Normal Interval; LF = Low Frequency; HF = High Frequency; AVNN = Average of the NNI series; SDNN = Standard Deviation of the NNI series; AVSD = Average of the subsequent NNI diﬀerence series; SDSD = Standard Deviation of the subse-quent NNI diﬀerence series; RMSSD = Root Mean Square of the subsequent NNI diﬀerence series; ppNN50 = percentage of NNIs diﬀering more than 50 ms. HRV metrics include three broad families, namely the time-based features, directly computed from the NNI series, the frequency-based features, computed from the spec-trum of the NNI series, and the non-linear features [28]. The most common time-based features are the Average (AVNN) and the Standard Deviation (SDNN) of the NNI series. The latter denotes the tendency of NNI to keep a constant value and represents a naïve estimate for the HRV. From the NNI series, it is possible to extract the series SD of subse-quent NNI diﬀerences 𝑆𝐷(cid:3036)=𝑁𝑁𝐼(cid:3036)(cid:2878)(cid:2869)−𝑁𝑁𝐼(cid:3036)  and compute the Average (AVSD), the Standard Deviation (SDSD), and the Root Mean Square (RMSSD) of SD. Another time-based feature is the percentage (ppNNτ) of NNIs diﬀering more than τ milliseconds dur-ing a speciﬁc interval, where τ is usually set to 50 ms or 20 ms. The RMSSD and ppNN50 are both recognized as two biomarkers of the vagal tone. More advanced time-based fea-tures include the width and the integral of the NNI distribution, where the latter is known as the triangular index. To compute HRV metrics in the frequency domain, it is ﬁrst necessary to implement a time-frequency transformation, using methods such as the Fast Fourier Transform (FFT) and the discrete wavelet transform [29,30]. The latter enables higher ﬂexibility in terms of time-frequency accuracy and does not require the segmentation of the NNI series into windows. After estimating the HRV spectrum, the naïve choice is to compute the energy of signiﬁcant frequency bands. According to the literature, the HRV’s low-frequency (LF) band reﬂects the combined sympathetic and parasympathetic inﬂuences on cardiac con-trol, while the high-frequency (HF) band reﬂects parasympathetic and respiratory activ-ity. Under these assumptions, the energy ratio between the LF and HF bands can be con-sidered a measure of the sympathetic–vagal balance [31]. J. Clin. Med. 2024, 13, 747

5 of 17

significant frequency bands. According to the literature, the HRV’s low-frequency (LF) band
reflects the combined sympathetic and parasympathetic influences on cardiac control, while
the high-frequency (HF) band reflects parasympathetic and respiratory activity. Under
these assumptions, the energy ratio between the LF and HF bands can be considered a
measure of the sympathetic–vagal balance [31].

In the context of non-linear measures, the most popular tool is the Poincaré plot, which
represents subsequent NNI values in a two-dimensional coordinate system where each
point is given by a couple (NN Ii+1, NN Ii) [32]. From the Poincaré plot, it is possible to
compute the Cardiac Sympathetic Index (CSI), the Cardiac Vagal Index (CVI), and the mod-
ified Cardiac Sympathetic Index (mCSI) [33]. As denoted by the name, the CSI and the CVI
are indicators of sympathetic and parasympathetic tones, while the mCSI is an extension of
the CSI proving to be more sensitive to HRV changes. The NNI series can be characterized
also via information-based metrics, such as entropy, which, in its original formulation,
denotes the amount of information contained in an event [34]. Other approaches include
the maximum Lyapunov exponent, a control theory’s measure denoting the predictability
of a dynamic system [35], the recurrence quantification analysis, the detrended fluctuation
analysis, and the correlation dimension, which all aim at characterizing the state space
occupied by a time series [36].

2.3. Detection Algorithms

To detect seizure events, the naïve approach involves the definition of an alarm
threshold over a specific HRV measure, considering a univariate analysis. A higher ac-
curacy is achieved by using multivariate approaches, where different HRV features, also
of different domains, are aggregated together. For this purpose, possible solutions in-
clude the naïve Bayes classifier, the linear or quadratic discriminant analysis, and the
generalized linear models [37]. More advanced approaches include the implementation
of supervised and unsupervised Machine Learning (ML) frameworks, where the first
is designed to operate with labeled datasets and the latter enables the detection of new
data patterns without human intervention [38,39]. Among the supervised ML tools, a
popular solution is the Supporting Vector Machines (SVMs), which makes it possible to
classify multivariate data into two or multiple classes by defining a hyperplane in the input
space [40].

Independently of the technique implemented, the performance of any seizure detection
framework can be described in terms of accuracy, sensitivity, and specificity. The accuracy
is the probability for a detection system to correctly associate the algorithm input with its
true class (seizure vs. non-seizure). Instead, the sensitivity and the specificity are defined as
the probability of correctly detecting positive (seizure) and negative (non-seizure) events,
respectively. Other performance metrics include the False Alarm Ratio (FAR), which is
given by the number of false events reported within a specific period and, in the case of
predictive systems, the anticipation time, which is the time shift between the alarm time
and the seizure onset.

3. Results

The first research returned N = 402 different records, which were reduced to N = 86
after the double-screening procedure. Most of the records excluded in this phase focused
on autonomic changes in animals, the probability of SUDEP, and the effects of vagus
nerve stimulation. The text assessment led to the exclusion of N = 10 studies consisting of
reviews of the literature and N = 4 studies that still did not comply with the review criteria.
The final analysis included 72 studies that analyzed HRV during the peri-ictal phase,
presented new seizure detection methods taking HRV measures as an input, or designed
new wearable systems for such a purpose. A summary of the overall results is reported
in Table 2.

J. Clin. Med. 2024, 13, 747

6 of 17

Table 2. Summary of the results. AUC = Area Under Curve; CS = Convulsive Seizure; EMU = Epilepsy Monitoring Unit; ES = Electrographic Seizures; F(A+) = Focal
seizures with autonomic changes; F(A−) = Focal seizures without autonomic changes; FAR = False Alarm Rate; IAS = Infantile Apneic Seizure; NA = Not Available;
NCS = Non-Convulsive Seizure; NICU = Neonatal Intensive Care Unit; Sens = Sensitivity; Spec = Specificity; ↑ = best result; ↓ = worst result; + = 0–50% of the
studies report the results; +++ = 75–100% of the studies report the results.

Seizure Detection
Performance

Seizure
Prediction Time

Pre-Ictal

HRV Changes
Ictal

Post-Ictal

Seizure
Type

References

Population

Study
Number

Neonates
(0–1 month)

Infants
(2–12 months)

Children
(1–18 years)

Adults
(>18 years)

8

1

18

50

Population
Size

Total = 256
Min = 5
Max = 52

Clinical
Setting

NICU

↑ AUC = 87% [41]
↓ AUC = 62% [42]

7

EMU

NA

Total = 397
Min = 9
Max = 72

Total = 941
Min = 1
Max = 70

EMU

EMU

Wearable

ECG-Patch

↑ Sens = 89.06% and
FAR = 0.41/hour [50]
↓ Sens = 60.9% and
Spec = 82.6% [51]

↑ Sens = 100.0% and
FAR = 0.90/hour [67]
↓ Sens = 60.0% and
Spec = 84.62% [68]

↑ Sens = 93.10% and
FAR = 0.04/hour [91]
↓ Sens = 78.20% and
FAR = 0.03/hour [105]

Sens = 92.6% and
FAR = 0.11/hour [110]

NA

NA

+

+++

+

Not specified

[41–48]

+++

NA

+++

IAS

[49]

Min = 21.8 s [52]
Max = 25 min [50]

+++

+++

+++

CS > NCS > ES

[49–66]

Min = 5 min [69]
Max = 30 min [70]

+++

+++

+++ (CS >
NCS)

CS > F(A+) >
F(A−) > ES

[50,64–69,71–104]

NA

NA

+++

+++

+++

CS > F(A+) >
F(A−)

[73,91,105–111]

+++

+++

+++

F(A+)

[110]

J. Clin. Med. 2024, 13, 747

7 of 17

3.1. HRV Features

To estimate HRV from Normal-to-Normal Intervals (NNIs), most of the analyzed
works (N = 17) considered a time window ∆t lasting 5 min, which is recognized as a good
trade-off between accuracy and time sensitivity [20]. In other cases, the value of ∆t was
set to 4 min (N = 6), 3 min (N = 7), 2 min (N = 3), or 1 min (N = 5), better capturing rapid
HRV changes at the cost of a reduced sample size. Finally, N = 9 studies considered a time
window ∆t lasting even less than 60 s, maximizing the time sensitivity.

The Average (AVNN) and the Standard Deviation (SDNN) of the NNI series repre-
sented the most common HRV features and were exploited in N = 41 and N = 33 works
among those analyzed, respectively. The authors of [71] suggested normalizing SDNN by
instantaneous Heart Rate (HR) to reduce the bias of each patient on the analysis outcomes.
The Root Mean Square Differences (RMSSDs) of the Subsequent NNI Difference (SD) series
and the ppNN50, both recognized as indicators of vagal tone, were considered in N = 31
and N = 20 studies, respectively. Finally, a minority number of works estimated the HRV
by the triangular index (N = 8), the width of the NNI distribution (N = 5), the Average
of the SD series (AVSD) (N = 4), and the Standard Deviation of the SD series (SDSD)
(N = 10). Interestingly, Behbahani and colleagues suggested considering a different lag
index j for analyzing the SD series, so that the i-th element of the SD series is given by
SDi(j) = NN Ii+j − NN Ii. This latter approach allows us to investigate the HRV changes
in different time scales [72].

To analyze the HRV in the frequency domain, N = 19 of the analyzed works imple-
mented Fast Fourier Transform (FFT). Other time-frequency transformations used in the
review were the discrete wavelet transform (N = 6), the Wigner–Ville distribution (N = 5),
the autoregressive models (N = 5), and the Welch algorithm (N = 5). Given the HRV
spectrum, N = 46 studies quantified the energy of the LF and HF bands (and their ratio),
while N = 6 studies detected specific HRV components without making assumptions about
the band boundaries. Interestingly, a specific work was proposed to evaluate the HRV com-
ponents according to their phase distribution by estimating a phase-locked spectrum [53].
Moreover, two works investigated the possibility that the EEG and ECG signals guide each
other, estimating how the signal synchronization changes in time [54,55].

Focusing on the non-linear HRV metrics, a total of N = 22 works considered the
Poincaré plot. A single work extended the Poincaré analysis by comparing the points
(cid:1) for multiple lag indexes j [72]. A significant number of works (N = 10)
(cid:0)NN Ii+j, NN Ii
estimated the complexity of the NNI series in terms of entropy. Among those works,
N = 4 analyzed entropy in multiple time scales and two studies considered more specific
entropy formulation, including the generalized entropy, the fuzzy entropy, the permutation
entropy, the self-information, and the conditional entropy [43,51]. Finally, a limited number
of studies (N = 5) characterized the NNI series via the recurrence quantification and the
detrended fluctuation analysis, N = 4 studies considered the correlation dimension, and
N = 3 studies implemented the maximum Lyapunov exponent.

3.2. Detection Algorithms

Among the works analyzed, N = 9 studies considered univariate approaches for
seizure detection, while a single study implemented a heuristic classifier based on the
Poincaré plot [56]. A limited number of works considered naïve Bayes classifiers (N = 3),
linear or quadratic discriminant analysis (N = 6), and generalized linear models (N = 4) for
discerning ictal and inter-ictal periods. Considering the ML approaches, most of the studies
considered supervised models, including artificial neural networks (N = 2), the k-nearest
neighbors algorithm (N = 4), random forests (N = 3), and Support Vector Machines (SVMs).
This latter approach proved to be the most popular HRV-based solution for detecting
seizures and was used in N = 10 studies among those analyzed. Finally, N = 3 works
implemented unsupervised models, including different types of clustering techniques
and the local outlier factor algorithm. An approach not falling in the previous definitions

J. Clin. Med. 2024, 13, 747

8 of 17

is given in [73,74], where ictal events were monitored through a multivariate statistical
process control chart [112].

3.3. Neonatal Population

Among the reviewed studies, N = 8 works investigated HRV modifications during
neonatal seizures. A first effort to quantify ictal autonomic changes in newborns is reported
in [113], where the authors assessed a significant HR increase during neonatal seizures,
without finding any significant HRV alterations. Two subsequent studies considered the
energy in the HF and LF bands to discriminate ictal and non-ictal intervals [44,45], while
another work proposed a seizure detection framework reaching an accuracy of about
85% using HRV metrics in the frequency domain [46]. More advanced seizure detection
frameworks, considering information theory metrics for estimating the HRV, are reported
in [42,43,47]. Frassineti and colleagues reached a detection accuracy of about 87% when
using an SVM classifier taking multiscale entropy features as an input [41]. To further
improve the detection performance, a single work combined EEG and HRV features via
a data fusion approach, reaching a sensitivity and specificity of about 95% and 89%,
respectively [48].

3.4. Pediatric Population

A total of N = 18 studies investigating autonomic abnormalities during the seizures of
pediatric patients were reviewed. Two initial works, published in 2004 and 2005, analyzed
HR in children with different epilepsy types, assessing that ictal tachycardia is more
commonly associated with convulsive seizures [57,58]. Several studies (N = 6) denoted
a correlation between seizures and sympathetic dominance, considering HRV metrics
computed in both the time and the frequency domain [49,51,53,59–61]. A single study
suggested that electrical seizures do not involve any HRV modifications [62], while Okanari
and colleagues showed that children with post-ictal EEG suppression are associated with
stronger sympathetic dominance during the pre-ictal phase [63]. More specific results are
reported in [54,55], the authors of which jointly analyzed EEG and HRV signals, observing
a stronger synchronization between the LF band of HRV and the Delta band of EEG during
the peri-ictal periods. Moreover, two studies analyzed autonomic changes in a population
including both children and adults [64,65], considering HRV metrics computed in the
frequency domain. The results highlighted that the pediatric population is associated with
stronger vagal suppression after tonic-clonic seizures than adult patients.

Two independent studies devised seizure detection systems, examined within a cohort
including only children. Specifically, De Cooman and colleagues developed a detection
algorithm for nocturnal seizures featuring autonomous adaptation to individual patient
characteristics [56]. This system, tested on a group of 28 children, gained a sensitivity of
77.6% while keeping a False Alarm Ratio (FAR) of 2.56 events per night. Conversely, the
authors of [52] compared different ML algorithms for detecting the pre-ictal transition in
a sample of nine children. The best results were obtained with an SVM classifier with a
multivariate input, yielding an accuracy of 77.1%.

3.5. Adult Population

In the adult population, N = 7 studies analyzed HRV changes during tonic-clonic
seizures with Generalized (GTCS) or Focal to Bilateral (FBTCS) onset [75–80,114]. These
studies assessed sympathetic dominance during the post-ictal periods independently of
the seizure origin (temporal vs. extra-temporal) and highlighted how autonomic changes
last longer in the case of convulsive than non-convulsive ictal events. In this regard, N = 3
other studies analyzed HRV during subclinical seizures, denoting that localized discharges
are associated with minimal autonomic variation [81]. However, a stronger reduction in
the parasympathetic tone is observed in case of the epileptic discharge spread within the
network [66,82].

J. Clin. Med. 2024, 13, 747

9 of 17

More heterogeneous results are obtained when analyzing the relationship between
autonomic changes and seizure localization or lateralization, as performed in N = 12 studies
in this review. An initial work documented a higher HR during seizures originating from
the left temporal lobe [81], while another two studies suggested that ictal tachycardia
does not correlate with the seizure onset [54,83]. Most of the studies in the literature
suggested that stronger changes in autonomic cardiac control are associated with seizures of
temporal origins, considering HRV measures computed in both the time and the frequency
domains [84,85]. Two studies assessed an increase in the sympathetic tone during the
pre-ictal periods in patients with both TLE and Frontal Lobe Epilepsy (FLE) [86,87], even in
relation to motor events occurring during sleep.

In the case of seizure lateralization, the results are often contradictory. Two studies
documented a reduction in the parasympathetic tone during the temporal seizures affecting
the left lobe [88,89], while a third study assessed higher HRV and HR during the post-ictal
phase of right-sided seizures [90]. Page and colleagues reported significant autonomic
cardiac changes in terms of both HR and HRV, during seizures affecting both the temporal
lobes [71]. Moreover, findings from N = 4 studies indicate that there is no significant
variance in HRV parameters across ictal events with different lateralization [65,83,85,91].
Notably, it has been suggested that autonomic changes may serve as a biomarker for
distinguishing between epileptic and psychogenic seizures [92,115]. Finally, Hödl and
colleagues considered a population with Vagus Nerve Stimulation (VNS), observing that
non-responding patients exhibit a stronger HRV reduction during the pre-ictal phase
compared to the patients benefiting from the therapy [93,94].

Among the analyzed papers, N = 7 studies proposed tools for detecting focal seizures
in the adult population. Jeppesen and colleagues designed a detection framework to
discern ictal and non-ictal periods by monitoring reduction in parasympathetic activ-
ity [76,83,95,96]. By using the modified Cardiac Sympathetic Index (mCSI) to estimate the
HRV, the designed system obtained a sensitivity of 100% in patients presenting signifi-
cant tachycardia during the ictal phase. Alternative detection frameworks were proposed
in [67,72,97], and the maximum performance (sensitivity of 100%) was obtained by Qaraqe
and colleagues, who combined EEG and HRV features in a unique system.

Other studies (N = 7) analyzed differences among inter-ictal and pre-ictal intervals,
suggesting that HRV changes are visible minutes before the seizure and, thus, enable an
early prediction of ictal events. A case report from 2004 observed an increase in the HRV’s
LF energy 12 min before seizures [98], while three studies found significant autonomic
modifications during the 5 min preceding the ictal onset [99–101]. The authors of [68] imple-
mented an SVM-based algorithm to identify the intervals (of 2 min duration) immediately
preceding the seizure, obtaining a detection accuracy of 73%. Leal and colleagues consid-
ered a longer time horizon for characterizing the ictal transition and observed pre-ictal
modifications up to 40 min before the seizure [102,103].

Taking advantage of the above evidence, N = 5 studies explicitly designed algorithms
to predict seizure events from autonomic modifications. In this context, performance is
assessed in terms of accuracy and anticipation time. Two studies designed prediction
algorithms that ensured an anticipation time of 5 min [69,104], obtaining a maximum
sensitivity of about 94% when using an SVM classifier taking multiple HRV features from
different domains in input. Improved results are given in [50,74], where it is shown that a
seizure can be predicted up to 15 min in advance without degrading the sensitivity levels.
A recent study confirmed the large variability in the anticipation time, which could range
from 3 to 30 min according to the target patient [70].

3.6. Wearable Systems

A total of N = 9 papers were reviewed analyzing seizure detection systems built with
wearable devices, facing challenges related to the online estimation of HRV. Three studies
analyzed systems to extract heartbeats in people with epilepsy automatically, without
providing results in terms of detection accuracy [106–108]. In three consecutive studies,

J. Clin. Med. 2024, 13, 747

10 of 17

Jeppesen designed and refined a wearable system for detecting seizures during the activities
of daily living [91,105,109]. The first version of the system led to a sensitivity of 87% with a
FAR of 0.04/hour in patients, which was associated with ictal tachycardia. The adoption of
a patient-adaptive algorithm further lowered the FAR by 31%, albeit with a slight decrease
in sensitivity (78.2%). Running the algorithm on the data collected via an ECG patch,
the authors obtained a sensitivity of about 92% and a FAR of about 0.1 events per hour
in patients with marked ictal autonomic changes [110]. Finally, a recent work designed
a system that integrates ECG, PPG, and EEG measures [111], leading to an accuracy of
beyond 91% when detecting ictal events and status epilepticus. However, all the above
solutions were tested offline and need further validation in phase III studies.

4. Discussion

This scoping review provides a comprehensive overview of the state-of-the-art role of
cardiac autonomic variations, expressed through HRV, in the detection and prediction of
ictal events. It is well known that numerous physiological phenomena related to immune,
endocrine, metabolic, neurological, and cardiovascular functions present daily and multi-
daily cycles. In individuals with epilepsy, seizure timing can be phase-locked to multi-day
cycles in temperature, electrodermal activity, and heart rate [116]. A deeper understanding
of the connections between seizures and the cardiovascular system could pave the way
for innovative approaches to mitigate seizure risk, adapting clinical interventions, such as
taking anti-seizure medication, to behavioral and sleep–wake patterns.

Undoubtedly, the detection of seizures is crucial for individuals with epilepsy (PwE),
with varying implications depending on their age (Table 3). In newborns, the early detec-
tion of seizures is essential for timely clinical intervention, as untreated events can have
significant and enduring impacts on the infant’s neurological development [19]. In older
populations, the implementation of real-time warning systems can strongly enhance the
QoL of both patients and their caregivers. From a practical perspective, seizure alarm sys-
tems would enable the caregiver to position the patient safely, protect them against injuries,
and seek help. Such systems are particularly effective for nocturnal seizure monitoring,
when ictal events are frequently unreported, and constitute a preventive measure against
SUDEP [78].

Table 3. Handy tips.

Neonates
(0–1 month)

Children
(1–18 years)

Adults
(>18 years)

Handy Tips

➢ Ictal sympathetic activity is greater in full-term than pre-term newborns

➢ Ictal sympathetic changes are greater in Convulsive (CS) than in

Non-Convulsive Seizure (NCS)

➢ Ictal HR and HRV modifications are greater in children than in adults
➢ Peri-ictal HRV modifications are greater in CS as compared to NCS,

particularly in the post-ictal phase

➢ Ictal HRV changes might help differentiate epileptic seizures from
non-epileptic episodes in individuals with PNES (Psychogenic
Non-Epileptic Seizure)

➢ Electrographic seizures are associated with minimal autonomic variations

Several devices using accelerometers (ACMs), surface electromyography (EMG), or
multimodal recordings have been clinically validated for the detection of tonic-clonic
seizures [21]. The detection of non-convulsive seizures remains challenging since it may
entail only low-profile clinical signs. It has been shown that cardiac autonomic changes,
assessed through HRV, could potentially serve as a useful biomarker for the detection
of ictal events associated with minimal muscle contractions, undetectable via ACM or
similar technologies [117]. Some studies have highlighted that cardiac autonomic changes

J. Clin. Med. 2024, 13, 747

11 of 17

anticipate the motor onset, thereby enabling the prediction of convulsive seizures, which
demand increased assistance and may lead to critical consequences such as sudden death.
Studies analyzing autonomic changes during neonatal seizures highlighted that new-
borns exhibit lower inter-ictal HRV values than both children and adults. While full-term
neonates exhibit an increase in vagal indexes of HRV during ictal events, the HRV does
not show significant variations in preterm newborns [45], an effect that could be attributed
to autonomic immaturity. To address such a limit, the computation of HRV features, both
in time and frequency domains, should be tailored to the gestational and postnatal age
of the newborns [19]. Because of the faster heart cycles in neonates, HRV dynamics can
be characterized by using shorter time windows than those used for older populations,
allowing a higher time sensitivity in assessing autonomic status. Particularly, a 2 min
period has been suggested as the optimal window length for analyzing the NNI series in
newborns, while, in the adult population, such a parameter is set to 5 min.

Several neonatal seizure detection methods have been designed and evaluated in
real scenarios, leading to promising results for everyday use in clinical settings [42]. The
affordability, non-invasiveness, and ease of use of ECG sensors make it possible to integrate
such approaches as pre-screening tools in Neonatal Intensive Care Units (NICUs) to rapidly
identify newborns at seizure risk, who may require further neurological investigation
through continuous or amplitude EEG. In the context of newborn seizures, the maximum
detection accuracy (87%) was obtained when using an SVM classifier taking multiple
HRV features, including multi-scale entropy, as an input [41]. This result suggested that
cardiac autonomic changes can be perceived only using advanced methodologies, including
non-linear features for describing HRV evolution and ML algorithms for aggregating and
processing the HRV measures.

In the context of the pediatric population, most studies observed that the peri-ictal
phase is characterized by sympathetic dominance, a phenomenon that can be underlined
using HRV measures in the frequency domain. This autonomic imbalance is more marked
in children than adults, suggesting that seizure detection could be more efficient in younger
populations. The heightened autonomic manifestations during seizures in children may
stem from a lower threshold for epileptogenic activation of the central autonomic system,
reflecting immature, less-established, subcortical seizure networks [65]. As occurred for
the neonatal population, the best detection results (sensitivity of 77%) were obtained when
implementing a multivariate SVM classifier taking multiple HRV features as inputs for
discerning between ictal and inter-ictal periods.

Considering the adult population, it was shown that subclinical seizures lead to mini-
mal autonomic variations [81], while convulsive seizures can be easily detectable from ECG
signals. Interestingly, none of the studies in this review reported differences between geri-
atric and adult populations, suggesting that the same results also hold for older classes of
people. In this regard, detecting convulsive seizures via HRV metrics could be non-relevant
since other tools, including ACMs, may be used. The main utility of monitoring HRV lies in
the possibility of predicting the motor onset, allowing the patient to gain a safe environment
and caregivers to take proper measures to mitigate the seizure impact [118]. Besides leading
to a strong enhancement in QoF, anticipating the ictal onset would make it possible to
personalize medical treatments to specific seizure patterns and triggers, reducing the need
for hospitalization and emergency care. The interval preceding seizure onset within which
prediction becomes feasible exhibits an extraordinary variability, spanning from 30 min
anticipation [70] to durations of about 5 min [69]. This considerable range in predictive time-
frames highlights the intricacies involved in anticipating seizure events and underscores
the need for meticulous investigation into the underlying physiological mechanisms.

Focal seizures have garnered increased attention in the field of HRV analysis, given the
well-established connection between the autonomic system and TLE. HRV-based detection
could prove to be a valuable tool for identifying and possibly predicting focal seizures that
involve, at least partially, the structures of the temporal lobe. Autonomic modifications
are not strictly related to TLE, since they may also occur in FLE and mostly rely on the

J. Clin. Med. 2024, 13, 747

12 of 17

involvement of the central autonomic network at seizure onset or propagation [119]. In
general, the class of patients who enable efficient seizure detection and prediction is not
well established [87]. Also, in this case, most works suggested modeling HRV according to
frequency-based or non-linear metrics since time-based HRV features are often incapable
of capturing the autonomic change in the peri-ictal phase [43].

In the last few years, increasing efforts have been directed at developing seizure
detection algorithms that can be built with wearable devices. In this context, one of the most
important performance parameters is the FAR. According to the ILAE recommendations,
high FAR constitutes one of the major concerns of establishing a reliable wearable seizure
detection device for non-convulsive seizures. While overlay-sensitive systems could erode
patient confidence and lead to withdrawal from social activities, too many false alarms
could discourage the patient adoption of these methods. To reduce FAR, it is important to
consider patient-specific solutions, which can adapt detection thresholds and parameters to
the HRV patterns of each patient, according to ML approaches [105]. Another critical point
for minimizing false detections is to discern between different types of HRV changes, which
might be related to trivial daily activities. In this context, it has been shown that advanced
HRV metrics, e.g., based on the Poincaré Plot, can distinguish between exercise-induced
ECG changes and the fast autonomic changes occurring during seizures [83].

In general, HRV-based algorithms, using ECG recorded with a wearable device,
achieved good accuracy for detecting seizures only in patients with prominent ictal auto-
nomic changes [91]. In the future, the individual pre-screening of HRV changes during
a seizure remains necessary for determining if any form of HRV-based seizure detection
system is feasible for the patient. Another limitation of the current literature is that it
predominantly includes phase 2 studies running algorithms offline [109]. The validation of
seizure detection tools in a real-life environment is still missing and should be the focus
of the scientific community in the next few years. Finally, evidence has emerged that the
combination of EEG and HRV features largely improves the seizure detection performance
in terms of accuracy, false alarm rate, and latency compared with other methods [111].
A non-invasive wearable system that integrates ECG and EEG could represent the most
promising tool for feasible seizure detection in the future. Following this path, the scientific
and industry communities should address the challenges of designing new tools to collect
multiple physiological signals, ensuring usability and acceptability in broad populations.
The main limitation of this scoping review is that it focuses on a single database
(PubMed), and research works in scientific areas other than medical ones could have
been missed. In addition, the research design led to the exclusion of papers not explicitly
analyzing HRV modifications during the peri-ictal phase. A more comprehensive work,
with less stringent review criteria, may identify other useful information, e.g., regarding
the relationship between autonomic changes and antiepileptic drugs, for designing new
methods for detecting and predicting seizure events.

5. Conclusions

The creation of tools aimed at anticipating ictal events represents a promising avenue
for enhancing seizure management and the quality of life of PwE. This scoping review
focuses on HRV analysis during the peri-ictal phase, emphasizing the potential of veg-
etative biomarkers for seizure control. Baseline HRV features in the time domain often
miss vegetative variations related to ictal events. Optimal detection results come from
leveraging advanced HRV features, such as energy in specific frequency bands or measures
from the Poincaré Plot, using ML algorithms capable of aggregating diverse data. Detection
performance is higher in neonatal and pediatric patients due to more significant cardiac
autonomic changes, especially during seizures. However, most studies use datasets from
clinical and controlled settings, with a limited exploration of HRV features from wearable
devices. Out-of-hospital seizure detection appears feasible only for patients with sub-
stantial autonomic changes during the ictal transition. Currently, there is no evidence on
clinical markers for accurately identifying patients and enabling reliable seizure detection.

J. Clin. Med. 2024, 13, 747

13 of 17

Establishing new guidelines to preemptively identify responsive patients is crucial for the
widespread adoption of HRV-based detectors.

Supplementary Materials: The following supporting information can be downloaded at https:
//www.mdpi.com/article/10.3390/jcm13030747/s1, Table S1: List of the reviewed articles.

Author Contributions: Conceptualization E.P., G.C.-B. and F.B.; methodology L.V.; data collection and
analysis F.M., A.S. and L.T.; writing—original draft preparation F.M., A.S. and L.T.; writing—review
and editing F.M., A.S., L.T., E.P., G.C.-B., E.P., L.V. and F.B.; supervision E.P., G.C.-B. and F.B. All
authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Conflicts of Interest: The authors declare no conflicts of interest.

References

1.
2.

3.

4.

5.
6.

7.

8.

9.

So, E.L. What is known about the mechanisms underlying SUDEP? Epilepsia 2008, 49, 93–98. [CrossRef]
Guekht, A.B.; Mitrokhina, T.V.; Lebedeva, A.V.; Dzugaeva, F.K.; Milchakova, L.E.; Lokshina, O.B.; Feygina, A.A.; Gusev, E.I.
Factors influencing on quality of life in people with epilepsy. Seizure 2007, 16, 128–133. [CrossRef]
Stirling, R.E.; Cook, M.J.; Grayden, D.B.; Karoly, P.J. Seizure forecasting and cyclic control of seizures. Epilepsia 2021, 62, S2–S14.
[CrossRef]
Schernthaner, C.; Lindinger, G.; Pötzelberger, K.; Zeiler, K.; Baumgartner, C. Autonomic epilepsy—The influence of epileptic
discharges on heart rate and rhythm. Wien. Klin. Wochenschr. 1999, 111, 392–401.
Sevcencu, C.; Struijk, J.J. Autonomic alterations and cardiac changes in epilepsy. Epilepsia 2010, 51, 725–737. [CrossRef] [PubMed]
Tinuper, P.; Bisulli, F.; Cerullo, A.; Carcangiu, R.; Marini, C.; Pierangeli, G.; Cortelli, P. Ictal bradycardia in partial epileptic
seizures: Autonomic investigation in three cases and literature review. Brain 2001, 124, 2361–2371. [CrossRef]
Stein, P.K.; Bosner, M.S.; Kleiger, R.E.; Conger, B.M. Heart rate variability: A measure of cardiac autonomic tone. Am. Heart J.
1994, 127, 1376–1381. [CrossRef]
Cheshire, W.P.; Freeman, R.; Gibbons, C.H.; Cortelli, P.; Wenning, G.K.; Hilz, M.J.; Spies, J.M.; Lipp, A.; Sandroni, P.; Wada, N.; et al.
Electrodiagnostic assessment of the autonomic nervous system: A consensus statement endorsed by the American Autonomic
Society, American Academy of Neurology, and the International Federation of Clinical Neurophysiology. Clin. Neurophysiol. 2021,
132, 666–682. [CrossRef] [PubMed]
Singer, D.H.; Martin, G.J.; Magid, N.; Weiss, J.S.; Schaad, J.W.; Kehoe, R.; Zheutlin, T.; Fintel, D.J.; Hsieh, A.M.; Lesch, M. Low
heart rate variability and sudden cardiac death. J. Electrocardiol. 1988, 21, S46–S55. [CrossRef]

10. Georgiou, K.; Larentzakis, A.V.; Khamis, N.N.; Alsuhaibani, G.I.; Alaska, Y.A.; Giallafos, E.J. Can wearable devices accurately

measure heart rate variability? A systematic review. Folia Medica 2018, 60, 7–20. [CrossRef] [PubMed]

11. Cosoli, G.; Spinsante, S.; Scalise, L. Wrist-worn and chest-strap wearable devices: Systematic review on accuracy and metrological

characteristics. Measurement 2020, 159, 107789. [CrossRef]

12. Massetani, R.; Strata, G.; Galli, R.; Gori, S.; Gneri, C.; Limbruno, U.; Di Santo, D.; Mariani, M.; Murri, L. Alteration of cardiac
function in patients with temporal lobe epilepsy: Different roles of EEG-ECG monitoring and spectral analysis of RR variability.
Epilepsia 1997, 38, 363–369. [CrossRef]

13. Tomson, T.; Ericson, M.; Ihrman, C.; Lindblad, L.E. Heart rate variability in patients with epilepsy. Epilepsy Res. 1998, 30, 77–83.

[CrossRef]

14. Zijlmans, M.; Flanagan, D.; Gotman, J. Heart rate changes and ECG abnormalities during epileptic seizures: Prevalence and

definition of an objective clinical sign. Epilepsia 2002, 43, 847–854. [CrossRef]

15. Opherk, C.; Coromilas, J.; Hirsch, L.J. Heart rate and EKG changes in 102 seizures: Analysis of influencing factors. Epilepsy Res.

2002, 52, 117–127. [CrossRef]

16. Devinsky, O. Effects of seizures on autonomic and cardiovascular function. Epilepsy Curr. 2004, 4, 43–46. [CrossRef]
17. Leijten, F.S.; Consortium, D.T.; van Andel, J.; Ungureanu, C.; Arends, J.; Tan, F.; van Dijk, J.; Petkov, G.; Kalitzin, S.; Gutter, T.

18.

19.

Multimodal seizure detection: A review. Epilepsia 2018, 59, 42–47. [CrossRef] [PubMed]
Simonnet, M.; Gourvennec, B. Heart rate sensors acceptability: Data reliability vs. ease of use. In Proceedings of the 2016 IEEE
13th International Conference on Wearable and Implantable Body Sensor Networks (BSN), San Francisco, CA, USA, 14–17 June
2016; pp. 94–98.
Statello, R.; Carnevali, L.; Sgoifo, A.; Miragoli, M.; Pisani, F. Heart rate variability in neonatal seizures: Investigation and
implications for management. Neurophysiol. Clin. 2021, 51, 483–492. [CrossRef] [PubMed]

20. Myers, K.A.; Sivathamboo, S.; Perucca, P. Heart rate variability measurement in epilepsy: How can we move from research to

clinical practice? Epilepsia 2018, 59, 2169–2178. [CrossRef] [PubMed]

21. Beniczky, S.; Arbune, A.A.; Jeppesen, J.; Ryvlin, P. Biomarkers of seizure severity derived from wearable devices. Epilepsia 2020,

61, S61–S66. [CrossRef] [PubMed]
Jansen, K.; Lagae, L. Cardiac changes in epilepsy. Seizure 2010, 19, 455–460. [CrossRef]

22.

J. Clin. Med. 2024, 13, 747

14 of 17

23. Mazzola, L.; Rheims, S. Ictal and Interictal Cardiac Manifestations in Epilepsy. A Review of Their Relation with an Altered

Central Control of Autonomic Functions and With the Risk of SUDEP. Front. Neurol. 2021, 12, 642645. [CrossRef]

24. van Westrhenen, A.; De Cooman, T.; Lazeron, R.H.C.; Van Huffel, S.; Thijs, R.D. Ictal autonomic changes as a tool for seizure

detection: A systematic review. Clin. Auton. Res. Off. J. Clin. Auton. Res. Soc. 2019, 29, 161–181. [CrossRef]

25. Behbahani, S. A review of significant research on epileptic seizure detection and prediction using heart rate variability. Arch. Turk.

Soc. Cardiol. 2018, 46, 414–421. [CrossRef]

26. Tricco, A.C.; Lillie, E.; Zarin, W.; O’Brien, K.K.; Colquhoun, H.; Levac, D.; Moher, D.; Peters, M.D.J.; Horsley, T.; Weeks, L.;
et al. PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation. Ann. Intern. Med. 2018, 169, 467–473.
[CrossRef] [PubMed]

27. Malik, M.; Camm, A.J. Heart rate variability. Clin. Cardiol. 1990, 13, 570–576. [CrossRef] [PubMed]
28.

Shaffer, F.; Ginsberg, J.P. An overview of heart rate variability metrics and norms. Front. Public Health 2017, 5, 258. [CrossRef]
[PubMed]

29. Brigham, E.O. The Fast Fourier Transform and Its Applications; Prentice-Hall, Inc.: New York, NY, USA, 1988.
30. Bentley, P.M.; McDonnell, J. Wavelet transforms: An introduction. Electron. Commun. Eng. J. 1994, 6, 175–186. [CrossRef]
31. Reyes del Paso, G.A.; Langewitz, W.; Mulder, L.J.; Van Roon, A.; Duschek, S. The utility of low frequency heart rate variability as
an index of sympathetic cardiac tone: A review with emphasis on a reanalysis of previous studies. Psychophysiology 2013, 50,
477–487. [CrossRef] [PubMed]

32. Brennan, M.; Palaniswami, M.; Kamen, P. Do existing measures of Poincare plot geometry reflect nonlinear features of heart rate

variability? IEEE Trans. Biomed. Eng. 2001, 48, 1342–1347. [CrossRef] [PubMed]

33. Bravi, A.; Longtin, A.; Seely, A.J. Review and classification of variability analysis techniques with clinical applications. Biomed.

34.

Eng. Online 2011, 10, 90. [CrossRef]
Inouye, T.; Shinosaki, K.; Sakamoto, H.; Toi, S.; Ukai, S.; Iyama, A.; Katsuda, Y.; Hirano, M. Quantification of EEG irregularity by
use of the entropy of the power spectrum. Electroencephalogr. Clin. Neurophysiol. 1991, 79, 204–210. [CrossRef]

35. Cencini, M.; Vulpiani, A. Finite size Lyapunov exponent: Review on applications. J. Phys. A Math. Theor. 2013, 46, 254019.

[CrossRef]

36. Henriques, T.; Ribeiro, M.; Teixeira, A.; Castro, L.; Antunes, L.; Costa-Santos, C. Nonlinear methods most applied to heart-rate

time series: A review. Entropy 2020, 22, 309. [CrossRef] [PubMed]

37. Myers, R.H.; Montgomery, D.C. A tutorial on generalized linear models. J. Qual. Technol. 1997, 29, 274–291. [CrossRef]
38. Kotsiantis, S.B.; Zaharakis, I.; Pintelas, P. Supervised machine learning: A review of classification techniques. Emerg. Artif. Intell.

Appl. Comput. Eng. 2007, 160, 3–24.

39. Grira, N.; Crucianu, M.; Boujemaa, N. Unsupervised and semi-supervised clustering: A brief survey. A Rev. Mach. Learn. Tech.

Process. Multimed. Content 2004, 1, 9–16.

40. Byvatov, E.; Schneider, G. Support vector machine applications in bioinformatics. Appl. Bioinform. 2003, 2, 67–77.
41.

Frassineti, L.; Lanata, A.; Manfredi, C. HRV analysis: A non-invasive approach to discriminate between newborns with and
without seizures. In Proceedings of the 2021 43rd Annual International Conference of the IEEE Engineering in Medicine & Biology
Society (EMBC), Virtual Conference, 1–5 November 2021; Volume 2021, pp. 52–55.

42. Olmi, B.; Manfredi, C.; Frassineti, L.; Dani, C.; Lori, S.; Bertini, G.; Cossu, C.; Bastianelli, M.; Gabbanini, S.; Lanatà, A. Heart Rate

43.

Variability Analysis for Seizure Detection in Neonatal Intensive Care Units. Bioengineering 2022, 9, 165. [CrossRef] [PubMed]
Frassineti, L.; Lanata, A.; Olmi, B.; Manfredi, C. Multiscale Entropy Analysis of Heart Rate Variability in Neonatal Patients with
and without Seizures. Bioengineering 2021, 8, 122. [CrossRef]

44. Malarvili, M.B.; Mesbah, M.; Boashash, B. Time-frequency analysis of heart rate variability for neonatal seizure detection.

45.

Australas. Phys. Eng. Sci. Med. 2006, 29, 67–72. [CrossRef]
Statello, R.; Carnevali, L.; Alinovi, D.; Pisani, F.; Sgoifo, A. Heart rate variability in neonatal patients with seizures. Clin.
Neurophysiol. Off. J. Int. Fed. Clin. Neurophysiol. 2018, 129, 2534–2540. [CrossRef]

46. Malarvili, M.B.; Mesbah, M. Newborn seizure detection based on heart rate variability. IEEE Trans. Biomed. Eng. 2009, 56,

47.

2594–2603. [CrossRef] [PubMed]
Frassineti, L.; Manfredi, C.; Olmi, B.; Lanata, A. A Generalized Linear Model for an ECG-based Neonatal Seizure Detector. In
Proceedings of the 2021 43rd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC),
Virtual Conference, 1–5 November 2021; Volume 2021, pp. 471–474.

48. Malarvili, M.B.; Mesbah, M. Combining newborn EEG and HRV information for automatic seizure detection. In Proceedings of
the 2008 30th Annual International Conference of the IEEE Engineering in Medicine and Biology Society, Vancouver, BC, Canada,
20–25 August 2008; Volume 2008, pp. 4756–4759.

49. Maruyama, S.; Jain, P.; Parbhoo, K.; Go, C.; Shibata, T.; Otsubo, H. Prolonged Video-EEG and Heart Rate Variability can Elucidate

Autonomic Dysregulation in Infantile Apneic Seizures. Pediatr. Neurol. 2022, 127, 48–55. [CrossRef] [PubMed]

50. Billeci, L.; Marino, D.; Insana, L.; Vatti, G.; Varanini, M. Patient-specific seizure prediction based on heart rate variability and

recurrence quantification analysis. PLoS ONE 2018, 13, e0204339. [CrossRef] [PubMed]

51. Pernice, R.; Faes, L.; Kotiuchyi, I.; Stivala, S.; Busacca, A.; Popov, A.; Kharytonov, V. Time, frequency and information domain
analysis of short-term heart rate variability before and after focal and generalized seizures in epileptic children. Physiol. Meas.
2019, 40, 074003. [CrossRef] [PubMed]

J. Clin. Med. 2024, 13, 747

15 of 17

52. Giannakakis, G.; Tsiknakis, M.; Vorgia, P. Focal epileptic seizures anticipation based on patterns of heart rate variability parameters.

53.

Comput. Methods Programs Biomed. 2019, 178, 123–133. [CrossRef] [PubMed]
Schiecke, K.; Wacker, M.; Piper, D.; Benninger, F.; Feucht, M.; Witte, H. Time-variant, frequency-selective, linear and nonlinear
analysis of heart rate variability in children with temporal lobe epilepsy. IEEE Trans. Biomed. Eng. 2014, 61, 1798–1808. [CrossRef]
[PubMed]

54. Piper, D.; Schiecke, K.; Leistritz, L.; Pester, B.; Benninger, F.; Feucht, M.; Ungureanu, M.; Strungaru, R.; Witte, H. Synchronization
analysis between heart rate variability and EEG activity before, during, and after epileptic seizure. Biomed. Technik. Biomed. Eng.
2014, 59, 343–355. [CrossRef] [PubMed]
Schiecke, K.; Pester, B.; Piper, D.; Benninger, F.; Feucht, M.; Leistritz, L.; Witte, H. Nonlinear Directed Interactions Between HRV
and EEG Activity in Children with TLE. IEEE Trans. Biomed. Eng. 2016, 63, 2497–2504. [CrossRef]

55.

56. De Cooman, T.; Varon, C.; Van de Vel, A.; Jansen, K.; Ceulemans, B.; Lagae, L.; Van Huffel, S. Adaptive nocturnal seizure detection

using heart rate and low-complexity novelty detection. Seizure 2018, 59, 48–53. [CrossRef] [PubMed]

57. Mayer, H.; Benninger, F.; Urak, L.; Plattner, B.; Geldner, J.; Feucht, M. EKG abnormalities in children and adolescents with

symptomatic temporal lobe epilepsy. Neurology 2004, 63, 324–328. [CrossRef] [PubMed]

58. O’Regan, M.E.; Brown, J.K. Abnormalities in cardiac and respiratory function observed during seizures in childhood. Dev. Med.

Child Neurol. 2005, 47, 4–9. [CrossRef] [PubMed]

59. Pradhan, C.; Sinha, S.; Thennarasu, K.; Jagadisha, T. Quantitative analysis of heart rate variability in patients with absence

epilepsy. Neurol. India 2011, 59, 25–29. [PubMed]

60. Kolsal, E.; Serdaro ˘glu, A.; Cilsal, E.; Kula, S.; Soysal, A.¸S.; Kurt, A.N.; Arhan, E. Can heart rate variability in children with epilepsy

be used to predict seizures? Seizure 2014, 23, 357–362. [CrossRef] [PubMed]

61. Gong, X.; Mao, X.; Chen, Y.; Huang, L.; Liu, W.; Huang, X.; Tan, Z.; Wang, X.; Wu, W.; Chen, Q.; et al. The changes of HRV
in refractory epilepsy: The potential index to predict the onset of epilepsy in children. J. X-ray Sci. Technol. 2016, 24, 309–317.
[CrossRef]

62. Assaf, N.; Weller, B.; Deutsh-Castel, T.; Cohen, A.; Tirosh, E. The relationship between heart rate variability and epileptiform
activity among children–a controlled study. J. Clin. Neurophysiol. Off. Publ. Am. Electroencephalogr. Soc. 2008, 25, 317–320.
[CrossRef]

63. Okanari, K.; Maruyama, S.; Suzuki, H.; Shibata, T.; Pulcine, E.; Donner, E.J.; Otsubo, H. Autonomic dysregulation in children with
epilepsy with postictal generalized EEG suppression following generalized convulsive seizures. Epilepsy Behav. 2020, 102, 106688.
[CrossRef]
Sarkis, R.A.; Thome-Souza, S.; Poh, M.Z.; Llewellyn, N.; Klehm, J.; Madsen, J.R.; Picard, R.; Pennell, P.B.; Dworetzky, B.A.;
Loddenkemper, T.; et al. Autonomic changes following generalized tonic clonic seizures: An analysis of adult and pediatric
patients with epilepsy. Epilepsy Res. 2015, 115, 113–118. [CrossRef]

64.

65. Chen, W.; Zhang, X.T.; Guo, C.L.; Zhang, S.J.; Zeng, X.W.; Meng, F.G. Comparison of heart rate changes with ictal tachycardia

seizures in adults and children. Child’s Nerv. Syst. ChNS Off. J. Int. Soc. Pediatr. Neurosurg. 2016, 32, 689–695. [CrossRef]

66. Brotherstone, R.; McLellan, A. Parasympathetic alteration during sub-clinical seizures. Seizure 2012, 21, 391–398. [CrossRef]

[PubMed]

67. Qaraqe, M.; Ismail, M.; Serpedin, E.; Zulfi, H. Epileptic seizure onset detection based on EEG and ECG data fusion. Epilepsy Behav.

2016, 58, 48–60. [CrossRef] [PubMed]

68. Valenza, G.; Romigi, A.; Citi, L.; Placidi, F.; Izzi, F.; Albanese, M.; Scilingo, E.P.; Marciani, M.G.; Duggento, A.; Guerrisi, M.;
et al. Predicting seizures in untreated temporal lobe epilepsy using point-process nonlinear models of heartbeat dynamics. In
Proceedings of the 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC),
Orlando, FL, USA, 16–20 August 2016; Volume 2016, pp. 985–988.

69. Pavei, J.; Heinzen, R.G.; Novakova, B.; Walz, R.; Serra, A.J.; Reuber, M.; Ponnusamy, A.; Marques, J.L.B. Early Seizure Detection

Based on Cardiac Autonomic Regulation Dynamics. Front. Physiol. 2017, 8, 765. [CrossRef] [PubMed]

70. Karasmanoglou, A.; Antonakakis, M.; Zervakis, M. ECG-Based Semi-Supervised Anomaly Detection for Early Detection and

Monitoring of Epileptic Seizures. Int. J. Environ. Res. Public Health 2023, 20, 5000. [CrossRef]

71. Page, T.; Rugg-Gunn, F.J. Bitemporal seizure spread and its effect on autonomic dysfunction. Epilepsy Behav. 2018, 84, 166–172.

[CrossRef] [PubMed]

72. Behbahani, S.; Jafarnia Dabanloo, N.; Nasrabadi, A.M.; Dourado, A. Epileptic seizure prediction based on features extracted from

lagged Poincaré plots. Int. J. Neurosci. 2022, 2022, 2106435. [CrossRef] [PubMed]

74.

73. Yamakawa, T.; Miyajima, M.; Fujiwara, K.; Kano, M.; Suzuki, Y.; Watanabe, Y.; Watanabe, S.; Hoshida, T.; Inaji, M.; Maehara, T.
Wearable Epileptic Seizure Prediction System with Machine-Learning-Based Anomaly Detection of Heart Rate Variability. Sensor
2020, 20, 3987. [CrossRef]
Fujiwara, K.; Miyajima, M.; Yamakawa, T.; Abe, E.; Suzuki, Y.; Sawada, Y.; Kano, M.; Maehara, T.; Ohta, K.; Sasai-Sakuma, T.;
et al. Epileptic Seizure Prediction Based on Multivariate Statistical Process Control of Heart Rate Variability Features. IEEE Trans.
Biomed. Eng. 2016, 63, 1321–1332.
Surges, R.; Scott, C.A.; Walker, M.C. Enhanced QT shortening and persistent tachycardia after generalized seizures. Neurology
2010, 74, 421–426. [CrossRef]

75.

J. Clin. Med. 2024, 13, 747

16 of 17

76.

Jeppesen, J.; Fuglsang-Frederiksen, A.; Brugada, R.; Pedersen, B.; Rubboli, G.; Johansen, P.; Beniczky, S. Heart rate variability
analysis indicates preictal parasympathetic overdrive preceding seizure-induced cardiac dysrhythmias leading to sudden
unexpected death in a patient with epilepsy. Epilepsia 2014, 55, e67–e71. [CrossRef]

77. Gaspard, N. Heartbreakers-Cardiac Stress After Uncomplicated Generalized Convulsive Seizures. Epilepsy Curr. 2019, 19, 246–248.

[CrossRef]

78. Arbune, A.A.; Jeppesen, J.; Conradsen, I.; Ryvlin, P.; Beniczky, S. Peri-ictal heart rate variability parameters as surrogate markers

of seizure severity. Epilepsia 2020, 61, S55–S60. [CrossRef]

79. Toth, V.; Hejjel, L.; Fogarasi, A.; Gyimesi, C.; Orsi, G.; Szucs, A.; Kovacs, N.; Komoly, S.; Ebner, A.; Janszky, J. Periictal heart rate
variability analysis suggests long-term postictal autonomic disturbance in epilepsy. Eur. J. Neurol. 2010, 17, 780–787. [CrossRef]
[PubMed]
Sivathamboo, S.; Constantino, T.N.; Chen, Z.; Sparks, P.B.; Goldin, J.; Velakoulis, D.; Jones, N.C.; Kwan, P.; Macefield, V.G.;
O’Brien, T.J.; et al. Cardiorespiratory and autonomic function in epileptic seizures: A video-EEG monitoring study. Epilepsy Behav.
2020, 111, 107271. [CrossRef] [PubMed]

80.

81. Adjei, P.; Surges, R.; Scott, C.A.; Kallis, C.; Shorvon, S.; Walker, M.C. Do subclinical electrographic seizure patterns affect heart

82.

83.

84.

85.

rate and its variability? Epilepsy Res. 2009, 87, 281–285. [CrossRef] [PubMed]
Forti, A.; Falla, M.; Scquizzato, T.; Strapazzon, G. A New Approach to Detect Nonconvulsive Seizures in Patients in a Cardiac
Surgery Intensive Care Unit by Monitoring Heart Rate Variability. J. Cardiothorac. Vasc. Anesth. 2019, 33, 2770–2774. [CrossRef]
[PubMed]
Jeppesen, J.; Beniczky, S.; Johansen, P.; Sidenius, P.; Fuglsang-Frederiksen, A. Detection of epileptic seizures with a modified heart
rate variability algorithm based on Lorenz plot. Seizure 2015, 24, 1–7. [CrossRef] [PubMed]
Jaychandran, R.; Chaitanya, G.; Satishchandra, P.; Bharath, R.D.; Thennarasu, K.; Sinha, S. Monitoring peri-ictal changes in heart
rate variability, oxygen saturation and blood pressure in epilepsy monitoring unit. Epilepsy Res. 2016, 125, 10–18. [CrossRef]
[PubMed]
Faria, M.T.; Rodrigues, S.; Campelo, M.; Dias, D.; Rego, R.; Rocha, H.; Sá, F.; Tavares-Silva, M.; Pinto, R.; Pestana, G.; et al. Heart
rate variability in patients with refractory epilepsy: The influence of generalized convulsive seizures. Epilepsy Res. 2021, 178,
106796. [CrossRef] [PubMed]

86. Calandra-Buonaura, G.; Toschi, N.; Provini, F.; Corazza, I.; Bisulli, F.; Barletta, G.; Vandi, S.; Montagna, P.; Guerrisi, M.; Tinuper, P.;
et al. Physiologic autonomic arousal heralds motor manifestations of seizures in nocturnal frontal lobe epilepsy: Implications for
pathophysiology. Sleep Med. 2012, 13, 252–262. [CrossRef]

87. You, S.M.; Jo, H.J.; Cho, B.H.; Song, J.Y.; Kim, D.Y.; Hwang, Y.H.; Shon, Y.M.; Seo, D.W.; Kim, I.Y. Comparing Ictal Cardiac
Autonomic Changes in Patients with Frontal Lobe Epilepsy and Temporal Lobe Epilepsy by Ultra-Short-Term Heart Rate
Variability Analysis. Medicina 2021, 57, 666. [CrossRef]

88. Romigi, A.; Albanese, M.; Placidi, F.; Izzi, F.; Mercuri, N.B.; Marchi, A.; Liguori, C.; Campagna, N.; Duggento, A.; Canichella, A.;
et al. Heart rate variability in untreated newly diagnosed temporal lobe epilepsy: Evidence for ictal sympathetic dysregulation.
Epilepsia 2016, 57, 418–426. [CrossRef]

89. Behbahani, S.; Dabanloo, N.J.; Nasrabadi, A.M.; Dourado, A. Classification of ictal and seizure-free HRV signals with focus on

90.

91.

lateralization of epilepsy. Technol. Health Care Off. J. Eur. Soc. Eng. Med. 2016, 24, 43–56. [CrossRef]
Shimmura, M.; Uehara, T.; Ogata, K.; Shigeto, H.; Maeda, T.; Sakata, A.; Yamasaki, R.; Kira, J.I. Higher postictal parasympathetic
activity following greater ictal heart rate increase in right- than left-sided seizures. Epilepsy Behav. 2019, 97, 161–168. [CrossRef]
Jeppesen, J.; Fuglsang-Frederiksen, A.; Johansen, P.; Christensen, J.; Wüstenhagen, S.; Tankisi, H.; Qerama, E.; Hess, A.; Beniczky,
S. Seizure detection based on heart rate variability using a wearable electrocardiography device. Epilepsia 2019, 60, 2105–2113.
[CrossRef]

92. Ponnusamy, A.; Marques, J.L.; Reuber, M. Comparison of heart rate variability parameters during complex partial seizures and

psychogenic nonepileptic seizures. Epilepsia 2012, 53, 1314–1321. [CrossRef]

93. Hödl, S.; Olbert, E.; Mahringer, C.; Struhal, W.; Carrette, E.; Meurs, A.; Gadeyne, S.; Dauwe, I.; Goossens, L.; Raedt, R.; et al.
Pre-ictal heart rate variability alterations in focal onset seizures and response to vagus nerve stimulation. Seizure 2021, 86, 175–180.
[CrossRef]

95.

94. Hödl, S.; Olbert, E.; Mahringer, C.; Carrette, E.; Meurs, A.; Gadeyne, S.; Dauwe, I.; Goossens, L.; Raedt, R.; Boon, P.; et al. Severe
autonomic nervous system imbalance in Lennox-Gastaut syndrome patients demonstrated by heart rate variability recordings.
Epilepsy Res. 2021, 177, 106783. [CrossRef] [PubMed]
Jeppesen, J.; Beniczky, S.; Fuglsang-Frederiksen, A.; Sidenius, P.; Jasemian, Y. Detection of epileptic-seizures by means of power
spectrum analysis of heart rate variability: A pilot study. Technol. Health Care Off. J. Eur. Soc. Eng. Med. 2010, 18, 417–426.
[CrossRef] [PubMed]
Jeppesen, J.; Beniczky, S.; Johansen, P.; Sidenius, P.; Fuglsang-Frederiksen, A. Using Lorenz plot and Cardiac Sympathetic Index
of heart rate variability for detecting seizures for patients with epilepsy. In Proceedings of the 2014 36th Annual International
Conference of the IEEE Engineering in Medicine and Biology Society, Chicago, IL, USA, 26–30 August 2014; Volume 2014,
pp. 4563–4566.

96.

97. Behbahani, S.; Dabanloo, N.J.; Nasrabadi, A.M.; Dourado, A. Prediction of epileptic seizures based on heart rate variability.

Technol. Health Care Off. J. Eur. Soc. Eng. Med. 2016, 24, 795–810. [CrossRef] [PubMed]

J. Clin. Med. 2024, 13, 747

17 of 17

98.

Faber, R.; Stepan, H.; Baumert, M.; Voss, A.; Walther, T. Changes of blood pressure and heart rate variability precede a grand mal
seizure in a pregnant woman. J. Perinat. Med. 2004, 32, 538–540. [CrossRef] [PubMed]

99. Behbahani, S.; Dabanloo, N.J.; Nasrabadi, A.M.; Teixeira, C.A.; Dourado, A. Pre-ictal heart rate variability assessment of epileptic

seizures by means of linear and non-linear analyses. Anadolu Kardiyol. Derg. 2013, 13, 797–803. [CrossRef] [PubMed]

100. Behbahani, S.; Dabanloo, N.J.; Motie Nasrabadi, A.; Dourado, A. Gender-Related Differences in Heart Rate Variability of Epileptic

Patients. Am. J. Men’s Health 2018, 12, 117–125. [CrossRef] [PubMed]

101. Gagliano, L.; Assi, E.B.; Toffa, D.H.; Nguyen, D.K.; Sawan, M. Unsupervised Clustering of HRV Features Reveals Preictal Changes
in Human Epilepsy. In Proceedings of the 2020 42nd Annual International Conference of the IEEE Engineering in Medicine &
Biology Society (EMBC), Montreal, QC, Canada, 20–24 July 2020; Volume 2020, pp. 698–701.

102. Leal, A.; Pinto, M.; Henriques, J.; Graca Ruano, M.D.; de Carvalho, P.; Teixeira, C. Preictal Time Assessment using Heart Rate
Variability Features in Drug-resistant Epilepsy Patients. In Proceedings of the 2019 41st Annual International Conference of the
IEEE Engineering in Medicine and Biology Society (EMBC), Berlin, Germany, 23–27 July 2019; Volume 2019, pp. 6776–6779.
103. Leal, A.; Pinto, M.F.; Lopes, F.; Bianchi, A.M.; Henriques, J.; Ruano, M.G.; de Carvalho, P.; Dourado, A.; Teixeira, C.A. Heart rate
variability analysis for the identification of the preictal interval in patients with drug-resistant epilepsy. Sci. Rep. 2021, 11, 5987.
[CrossRef] [PubMed]

104. Moridani, M.K.; Farhadi, H. Heart rate variability as a biomarker for epilepsy seizure prediction. Bratisl. Lek. Listy 2017, 118, 3–8.

[CrossRef] [PubMed]

105. Jeppesen, J.; Christensen, J.; Johansen, P.; Beniczky, S. Personalized seizure detection using logistic regression machine learning

based on wearable ECG-monitoring device. Seizure 2023, 107, 155–161. [CrossRef] [PubMed]

106. Jeppesen, J.; Beniczky, S.; Fuglsang Frederiksen, A.; Sidenius, P.; Johansen, P. Modified automatic R-peak detection algorithm
for patients with epilepsy using a portable electrocardiogram recorder. In Proceedings of the 2017 39th Annual International
Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), Jeju, Republic of Korea, 11–15 July 2017; Volume
2017, pp. 4082–4085.

107. Kołodziej, M.; Majkowski, A.; Rak, R.J.; ´Swiderski, B.; Rysz, A. System for automatic heart rate calculation in epileptic seizures.

Australas. Phys. Eng. Sci. Med. 2017, 40, 555–564. [CrossRef]

108. Zambrana-Vinaroz, D.; Vicente-Samper, J.M.; Sabater-Navarro, J.M. Validation of Continuous Monitoring System for Epileptic

Users in Outpatient Settings. Sensors 2022, 22, 2900. [CrossRef]

109. Jeppesen, J.; Fuglsang-Frederiksen, A.; Johansen, P.; Christensen, J.; Wüstenhagen, S.; Tankisi, H.; Qerama, E.; Beniczky, S. Seizure

detection using heart rate variability: A prospective validation study. Epilepsia 2020, 61, S41–S46. [CrossRef]

110. Jeppesen, J.; Christensen, J.; Mølgaard, H.; Beniczky, S. Automated detection of focal seizures using subcutaneously implanted

electrocardiographic device: A proof-of-concept study. Epilepsia 2023, 64, S59–S64. [CrossRef]

111. Zambrana-Vinaroz, D.; Vicente-Samper, J.M.; Manrique-Cordoba, J.; Sabater-Navarro, J.M. Wearable Epileptic Seizure Prediction
System Based on Machine Learning Techniques Using ECG, PPG and EEG Signals. Sensors 2022, 22, 9372. [CrossRef] [PubMed]
112. Bersimis, S.; Psarakis, S.; Panaretos, J. Multivariate statistical process control charts: An overview. Qual. Reliab. Eng. Int. 2007, 23,

517–543. [CrossRef]

113. Greene, B.R.; de Chazal, P.; Boylan, G.; Reilly, R.B.; O’Brien, C.; Connolly, S. Heart and respiration rate changes in the neonate

during electroencephalographic seizure. Med. Biol. Eng. Comput. 2006, 44, 27–34. [CrossRef]

114. Faria, M.T.; Rodrigues, S.; Campelo, M.; Dias, D.; Rego, R.; Rocha, H.; Sá, F.; Tavares-Silva, M.; Pinto, R.; Pestana, G.; et al. Does

the type of seizure influence heart rate variability changes? Epilepsy Behav. 2022, 126, 108453. [CrossRef]

115. Au Yong, H.M.; Minato, E.; Paul, E.; Seneviratne, U. Can seizure-related heart rate differentiate epileptic from psychogenic

nonepileptic seizures? Epilepsy Behav. 2020, 112, 107353. [CrossRef] [PubMed]

116. Gregg, N.M.; Pal Attia, T.; Nasseri, M.; Joseph, B.; Karoly, P.; Cui, J.; Stirling, R.E.; Viana, P.F.; Richner, T.J.; Nurse, E.S.; et al.
Seizure occurrence is linked to multiday cycles in diverse physiological signals. Epilepsia 2023, 64, 1627–1639. [CrossRef]
117. Elger, C.E.; Hoppe, C. Diagnostic challenges in epilepsy: Seizure under-reporting and seizure detection. Lancet Neurol. 2018, 17,

279–288. [CrossRef]

118. Kuhlmann, L.; Lehnertz, K.; Richardson, M.P.; Schelter, B.; Zaveri, H.P. Seizure prediction—Ready for a new era. Nat. Rev. Neurol.

2018, 14, 618–630. [CrossRef]

119. Benarroch, E.E. The central autonomic network: Functional organization, dysfunction, and perspective. Mayo Clin. Proc. 1993, 68,

988–1001. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
