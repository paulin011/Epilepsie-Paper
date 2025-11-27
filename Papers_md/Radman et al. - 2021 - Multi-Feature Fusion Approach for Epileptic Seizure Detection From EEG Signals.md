# Radman et al. - 2021 - Multi-Feature Fusion Approach for Epileptic Seizure Detection From EEG Signals

IEEE SENSORS JOURNAL, VOL. 21, NO. 3, FEBRUARY 1, 2021

3533

Multi-Feature Fusion Approach for Epileptic
Seizure Detection From EEG Signals

Moein Radman, Milad Moradi

, Ali Chaibakhsh , Member,IEEE,

Mojtaba Kordestani

, SeniorMember,IEEE, and Mehrdad Saif

, SeniorMember,IEEE

Abstract—In this article, a new fusion scheme based on the
Dempster–Shafer Evidence Theory (DSET) is introduced for
Epileptic Seizure Detection (ESD) in brain disorders. Firstly,
various features in temporal, spectral, and temporal-spectral
domains are extracted from Electroencephalogram (EEG)
signals. Afterward, a Correlation analysis via the Pearson
Correlation Coefﬁcient (PCC) is conducted on the extracted
features to select and remove highly correlated features.
It leads to the second feature set with about half numbers
of the ﬁrst feature set. Next, three separate ﬁlter-type feature
selection techniques, including Relief-F (RF), Compensation
Distance Evaluation Technique (CDET), and Fisher Score (FS),
are conducted to this second feature set for ranking features.
Following that, a feature fusion is engaged by the DSET
through the individual feature ranking results to generate high
qualiﬁed feature sets. Indeed, the DSET-based feature fusion
is devoted to enhancing the feature selection conﬁdence
using the least superb ranked features. In the classiﬁcation
stage, an Ensemble Decision Tree (EDT) classiﬁer, along
with two common validation procedures, including hold out
and 10-fold cross-validation, is appropriated to classify the
selected features from the EEG signals as normal, pre-ictal
(epileptic background), and ictal (epileptic seizure) classes.
Finally, several test scenarios are investigated using experi-
mental data of Bonn University to evaluate the proposed ESD
performance. Moreover, a comparison with other research
works on the same dataset and classes is accomplished. The obtained results indicate the effectiveness of the proposed
feature fusion approach and superior accuracy compared to the traditional methods.

Index Terms— Epileptic seizure detection (ESD), electroencephalogram (EEG) signals, feature selection, fusion

approaches, ensemble-based classiﬁer.

I. INTRODUCTION

E PILEPSY is the most common neural disease, based

on the World Health Organization (WHO) estimation.
Each year, approximately 2.4 million new cases are identiﬁed,
while 50 percent of the cases incur the disease when they are

Manuscript received July 1, 2020; revised September 17, 2020;
accepted September 18, 2020. Date of publication September 23, 2020;
date of current version January 6, 2021. The work of Mehrdad Saif was
supported by the Natural Sciences and Engineering Research Coun-
cil (NSERC) of Canada under Grant 61873144. The associate editor
coordinating the review of this article and approving it for publication was
Dr. Ravibabu Mulaveesala. (Correspondingauthor:MojtabaKordestani.)
Moein Radman and Ali Chaibakhsh are with the Faculty of Mechanical
Iran (e-mail:

Engineering, University of Guilan, Rasht 4199613776,
moeinradman@phd.guilan.ac.ir; chaibakhsh@guilan.ac.ir).

Milad Moradi, Mojtaba Kordestani, and Mehrdad Saif are with the
Department of Electrical and Computer Engineering, University of Wind-
sor, Windsor, ON N9B 3P4, Canada (e-mail: moradih@uwindsor.ca;
kordest@uwindsor.ca; msaif@uwindsor.ca).

Digital Object Identiﬁer 10.1109/JSEN.2020.3026032

children or teenagers. Moreover, epilepsy disorders grow in
older adults [1]. Generally, over 50 million people worldwide
are affected by this neurological disorder [2]. The sick cases
are consistently faced with unnatural sicknesses outbreak due
to the brain’s electric discharge during a certain period.

Epilepsy is often known as seizure repetitions during a
time period. This chronic issue can happen from once a year
to several times a day. Epileptic disorders and seizures are
not identical. The epilepsy signs can be sudden attacks with
no reason due to the central neural system interfering. This
disease is as a result of a typical neural network procedure that
suddenly transforms into a highly irritable network, mostly in
the cerebrum region [3].

A. Motivation

The EEG directly records the brain activities through the
electrodes attached to the scalp skin [4]. Most of the disorders

1558-1748 © 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:48 UTC from IEEE Xplore.  Restrictions apply. 

3534

IEEE SENSORS JOURNAL, VOL. 21, NO. 3, FEBRUARY 1, 2021

related to the brain malfunction, including epilepsy diseases,
are examined using the EEG signals [5]. The EEG signals
show the patterns before and during the seizure in the case
of epilepsy, which is entirely different from the normal EEG
signals. Some proposed ESD schemes divide the EEG signals
as normal and abnormal classes (two classes) [6], [7], while
others categorize EEG signals as normal, pre-ictal, and ictal
conditions (three classes) [8]. Although various methods have
been developed for the ESD [9], the EEG attack classiﬁcation
is a relatively difﬁcult, yet challenging task due to overlap
between classes.

B. RelatedWorks

A typical procedure of EEG attack diagnosis often involves
the following steps: a) Splitting the dataset into train and
test sets with a speciﬁc portion, and applying EEG sig-
nal preprocessing techniques to exclude the noises and arti-
facts. b) Extracting signal’s features by various time or/and
frequency-domain methods. c) Selecting superb extracted fea-
tures with the highest description. d) Implementing a classiﬁer
to identify the classes. e) Evaluating the attack diagnosis
method using the test dataset [10].

[12]

[11],

Several works exist on publicly available benchmark
databases [8],
that classify epileptic seizures.
Alam et al. [13] develop a seizure and epilepsy detection
based on the Empirical Mode Decomposition (EMD). First,
higher-order statical moments such as variance, kurtosis, and
skewness are utilized to extract proper features. Following that,
the features are given to an Artiﬁcial Neural Network (ANN)
to identify seizures and epilepsy. Although this approach is
faster than the time-frequency-based techniques, the classiﬁca-
tion accuracy is 80%, which is obtained only by three features.
Niknazar et al. [14] examine a system identiﬁcation tool
based on the time-delay method for ESD. Recurrence Quan-
tiﬁcation Analysis (RQA)-based features are utilized by
Error-Correction Output Codes (ECOC) classiﬁer. The RQA
is adopted because there is no requirement to know about
signal properties, such as its length, noise, etc. Therefore,
the suggested ESD method does not need transformations
or preexisting models. Besides, the ability to work with sig-
nals, including different morphology and spectrum, is another
advantage. A hybrid ESD method is introduced in [15]. First,
a Dual-Tree Complex Wavelet Transformation (DTCWT) is
applied to reduce the data size and obtain features. Later,
the features are presented to Complex-Valued Neural Net-
works (CVANN) for the classiﬁcation task. Investigating the
signals at various levels using wavelet transformations is a
prominent part of this work.

A data-driven method based on Multi-Layer Perceptron
Neural Network (MLPNN) is developed in [16] for EEG
classiﬁcation. First, a Discrete Wavelet Transform (DWT)
is adopted to decompose EEG signals into frequency sub-
bands. Afterward,
the K-means algorithm is employed to
cluster the wavelet coefﬁcients in each sub-band. Following
that, the probability distributions based on the distribution of
wavelet coefﬁcients are computed. Finally, these distributions
are applied as inputs to the MLPNN model. In this work,

a clustering approach based on the k-means algorithm is
allowed over the wavelet coefﬁcients instead of using the basic
statistics, which improves the performance.

Tiwari et al. [17] apply a Local Binary Pattern (LBP)
method for epilepsy detection from EEG signals. Firstly, some
ﬁltered signals are detected by a pyramid of the Difference of
Gaussian (DoG). Then, these signals are fed to a Support Vec-
tor Machine (SVM) classiﬁer. The computational simplicity of
LBP features, the ability to reach high detection accuracy with
a smaller portion of the EEG signals, suitability for online
epileptic detection with reduced computational burden are the
clinical signiﬁcance of this diagnosis method. In another work,
Acharya et al. [18] apply several entropy-based extracted fea-
tures to detect normal, pre-ictal, and ictal conditions. First, four
different Entropy, including Approximate Entropy (ApEn),
Sample Entropy (SampEn), Phase Entropy 1 (S1), and Phase
Entropy 2 (S2), are investigated. Following that, the features
are fed to seven different classiﬁers, which among them Fuzzy
Sugeno Classiﬁer (FSC), provides the best performance.

Tzallas et al. [19] develop an automatic ESD method
to classify the epileptic attacks into three classes. Several
extracted features from the time-frequency analysis are fed to
Artiﬁcial Neural Network (ANN). Next, it is shown that the
classiﬁer reaches to the best performance using 40 features.
Upadhyay et al. [20] apply integrated DWT-based features and
Least Square-Support Vector Machine (LS-SVM) to classify
the epilepsy attacks. First, utilizing the Maximum Energy to
Permutation Entropy ratio, the best basis wavelet is chosen for
feature extraction. Afterward, several feature ranking methods,
including RF, FS, and Information Gain (IG), are applied for
feature selection. Then, they are ranked and fed to the classiﬁer
for ESD. Simulation tests on the EEG signals indicate the high
performance of the suggested ESD.

Hassan et al. [21] utilize Complete Ensemble Empirical
Mode Decomposition with Adaptive Noise (CEEMDAN) for
epileptic seizure identiﬁcation. They extract intrinsic mode
functions through decomposing segments of EEG signals by
the CEEMDAN. Afterward, Normal Inverse Gaussian (NIG)
pdf parameters are utilized to model the extracted mode func-
tions. Besides, ten classiﬁers are investigated in this work that
Adaptive Boosting (AdaBoost) reaches the best classiﬁcation
performance. In another work, Li et al. [22] introduce a
hybrid method for ESD by using Fuzzy Entropy (FuzzyEn)-
based features which are obtained from EEG signals in a
Fractional Fourier Transform - Wavelet Packet decomposition
(FFT-WPT) domain. They also employ the Principal Com-
ponent Analysis (PCA) to reduce dimensionality and pro-
duce uncorrelated variables. Finally, three different classiﬁers,
including K-Nearest Neighbor (KNN), Linear Discriminant
Analysis (LDA) and SVM are applied for classiﬁcation.
In simulation, test results indicate that the SVM classiﬁer
produces the best performance.

An EEG classiﬁcation method is developed in [23] using
a combination of temporal and spectral features from EMD.
Then, by concatenating the obtained temporal and spectral
features of the EEG signals, the salient characteristics are
extracted fed to an SVM classiﬁer. Test results indicate an
overall accuracy of 82 %. Hassan and Haque [24] introduce a

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:48 UTC from IEEE Xplore.  Restrictions apply. 

RADMAN etal.: MULTI-FEATURE FUSION APPROACH FOR ESD FROM EEG SIGNALS

3535

CEEMDAN for ESD and EEG signal analysis that resolves the
mode mixing problem and gives better spectral separation of
the modes. Then, various extracted statistical features by the
CEEMDAN are fed to the ANN for ESD. Test results show an
accuracy of 86.37 %. A Short-Time Fourier Transform (STFT)
is utilized in [25] to extract features. Then, Four rule-based
classiﬁers, including a decision tree algorithm, a random forest
algorithm, an SVM-based decision tree algorithm, and an
SVM-based random forest algorithm, are applied to detect
seizures. Test results indicate that the random forest provides
the best performance among the other investigated classiﬁers.
Das et al. [26] developed an automated ESD for EEG classi-
ﬁcation. The ESD method utilizes statistical NIG parameters
computed in the DTCWT domain to extract features. Then,
an SVM is applied for the classiﬁcation task. The proper over-
all performance and computational speed have been mentioned
as two advantages of this work.

An integrated Variational Mode Decomposition (VMD) and
Auto-Regression (AR)-based feature extraction is introduced
in [27] for automated seizure detection. Then, the random
forest classiﬁer is implemented for the classiﬁcation. Excellent
robustness and adaptive adjustment of AR model parameters
are two advantages of the suggested seizure detection. Hassan
and Subasi [28] address the problem of automated ESD using
single-channel EEG signals. To reach this aim, a CEEMDAN
is employed to decompose segments of EEG signals. Then,
the obtained train and test matrices are fed to Linear Pro-
gramming Boost-ing (LPBoost) for classiﬁcation. A scheme
including Tunable-Q factor Wavelet Transform (TQWT), and
bootstrap aggregating (Bagging) is proposed in [29] for the
ESD problem. First,
is decomposed into
the EEG signal
subbands by utilizing the TQWT, and then, various spectral
features are extracted from the decomposed sub-bands. Finally,
bagging is used to perform the classiﬁcation task. The classi-
ﬁer reaches an accuracy of 98.40%.

C. TheProposedFailurePrognosisMethodandMain
Contributions

This article introduces a new fusion ESD scheme to isolate
various conditions, including normal, pre-ictal, and ictal. For
this aim, the various domains like temporal, spectral, and
temporal-spectral features are ﬁrstly extracted from the EEG
signals. Following that, a feature selection analysis based on
correlation analysis is applied to reduce the feature number
from eighty to forty-three. Following that, the extracted fea-
tures that are now in the new reduced feature space are ranked
using RF, CDET, and FS feature ranking techniques. Since
then, the DSET is utilized to combine the features ranking
methods and generate several new feature sets with the ranked
high qualiﬁed properties. Finally, EDT classiﬁer is employed
to isolate and distinguish various Epileptic seizures.

The main contributions of this work are summarized as

follows:

feature extraction meth-
• Applying a combination of
ods from various domains,
including temporal, spec-
tral, and temporal-spectral domains, assists in producing
rich feature sets. It helps to catch the epileptic seizure

characteristic and therefore improves the detection rate
and ESD’s performance.

• Another novelty is to utilize the DSET to generate several
new ranked feature sets by fusing the feature ranking
methods. It enhances the classiﬁcation performance com-
pared to situations in which the classiﬁer only applies
each of the RF, CDET, and FS feature ranking methods
individually.

• The proposed fusion ESD structure is appropriated well
for online implementation. The suggested feature ranking
based on DSET chooses the optimized features and
consequently reaches a higher accuracy compared to [20]
in a similar condition when it applies a holdout vali-
dation procedure. Therefore, this is suitable for online
implementation.

• According to our best knowledge, this proposed ESD
scheme has reached the best-achieved accuracy when data
has been split into 70% and 30% for training and test,
respectively.

D. ThePaperOrganization

The rest of this article is organized as follows. Section II
illustrates materials and methods. Simulation studies are
demonstrated in detail in Section III. Section IV provides
discussion and details about the proposed EDT classiﬁer using
the integrated high-qualiﬁed features. Moreover, a comparison
with other works in the literature is provided. Finally, a sum-
mary of the results is given in Section V.

II. MATERIALS AND METHODS

A. Dataset

The dataset studied in this work is obtained from Bonn Uni-
versity in Germany [8], which is accessible in the Epileptology
department of the university. This dataset consists of ﬁve sub-
sets of A, B, C, D, and E; each of them carries 100 pieces of
single-channel EEG signal with a length of 23.6 seconds. The
A and B sets comprise EEG pieces recorded from the scalp
skin of ﬁve healthy volunteers based on the 10 − 20 standard
electrode placement procedure. Volunteers in set A are awake
with their eyes open, while B’s volunteers are awake with their
eyes closed. Sets C, D, and E are collected from the patient’s
EEG archive before the surgery. Based on table 1, normal
signals are gathered from 5 healthy subjects, attack signals,
and signals between the attacks. Set D contains EEG recorded
from inside the brain, and C includes recorded EEG from the
brain’s hippocampus region. Set C and D restrain brain activity
between two epileptic attacks. Nevertheless, Set E holds
activity during the epileptic attack. All the EEG signals are
recorded by a 128-channel ampliﬁer system using an average
standard reference after 12-bit analog to digital transformation.
The sampling frequency of the datasets is 173.63 Hz. Datasets
are split into A and B as a normal condition, C and D as
pre-ictal, and ﬁnally E as ictal conditions.

B. FeatureExtraction

Processing the raw EEG information is very challenging due
to the encoded information in EEG signals. Therefore, some

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:48 UTC from IEEE Xplore.  Restrictions apply. 

3536

IEEE SENSORS JOURNAL, VOL. 21, NO. 3, FEBRUARY 1, 2021

TABLE I
FEATURE EXTRACTION METHODS

mathematical transformations are often practiced to the EEG
signals to extract their properties from a particular perspective.
The output, or in other words, the obtained coefﬁcients from
these transforms are called features [30].

The standard feature extraction methods for the EEG signals
are divided into three general categories: 1) temporal, 2) spec-
tral, and 3) spatial features [31]. The spatial features are
often employed in the Brain-Computer Interface (BCI) [4].
To extract features, ﬁrstly, the Butterworth ﬁlter is adopted
to decompose the brain signal into ﬁve frequency sub-bands
named delta, theta, alpha, beta, and gamma. It is noteworthy
that each band contains useful information. Later, the features
are extracted for each frequency band individually. Besides,
several various features in different domains like temporal,
spectral, and temporal-spectral are extracted to attain the high-
est distinct characteristics of the EEG signals. The extracted
features are summarized in Table I.

First, several EEG signal characteristics in the tempo-
ral domain, such as root mean square, variance, skewness,
kurtosis, and mean absolute value, are exercised to obtain
features for ﬁve frequency bands. Afterward,
the signals
are transformed into the spectral domain by the Fourier
Transform (FT). Then, particular spectral features, according
to Table I, are extracted. The spectral features manifest the
signal’s change rate in a speciﬁc frequency bound. Therefore,
they confer the intensity and quantity of the signal in each
frequency bound.

coefﬁcients

Temporal-spectral domain features are obtained by Wavelet
Transform (WT). Commonly, wavelet
are
employed to represent the signal in both time and spectral
domains. In the ﬁrst step of discrete WT, approximate coefﬁ-
cients are obtained by passing a signal from a low-pass ﬁlter.
Then, detailed coefﬁcients are acquired by passing from a
high-pass ﬁlter in the second step [34]. In the next level,
decomposition is recursively executed to the low-pass approx-
imate coefﬁcients to reach the desired decomposed level.

In this work, resampling is applied to acquire proper WT’s
coefﬁcients. WT’s coefﬁcients, including A4, D4, D3, D2,
and D1 are related to Delta, Theta, Alpha, Beta, and Gamma,
respectively. Following that, the statistical and entropy features
are extracted from these coefﬁcients.

C. FeatureReduction,Ranking,Selection

Choosing effective features is recognized as an essential
step for designing an appropriate ESD system. In general,
some appropriate features are often deﬁned and extracted
according to the chosen dominant variables for ESD. It is noted
that selecting weak or irrelative features may cause incorrect
judgments of the decision-maker system. Feature selection
removes irrelevant or redundant features to obtain a minimum
set of features (or classes) [35].

Feature selection techniques can be categorized into two
major groups, including ﬁlter-type and wrapper-type methods.
In ﬁlter-type methods, variable selection is accomplished by
setting an appropriate ranking criterion to score and ordering
the variables [36]. The optimal feature subset is obtained
in the wrapper-type method by evaluating each feature sub-
set’s performance, which generally achieves a higher perfor-
mance compared to ﬁlter-type methods. Regarding the feature
selection operating mechanism, it is clear that the ﬁlter-type
methods are faster than the wrapper-type methods. Despite
the lower accuracy of ﬁlter-type methods,
they are often
preferred due to their computational efﬁciency, especially for
high-dimensional feature spaces [37], [38].

In this section, four different ﬁlter-type approaches, includ-
ing the Pearson Correlation Coefﬁcient (PCC), RF, CDET,
and FS, are employed for feature selection purposes. In the
following, each method is brieﬂy described.

1) Pearson Correlation Coefﬁcient (PCC): Correlation
indicates a relationship among measured data values or
mathematical variables. The PCC is deﬁned by a static gain
in a range of −1 to +1 for vectors X and Y. The gain close
to one intimates that
two variables are highly correlated.
In contrast, the gain near zero implies a wealy relationship
among the variables. The PCC is calculated as follows [39]:

(cid:2)

r =

(cid:3)(cid:2)
n
i=1

(xi − ¯x)(yi − ¯y)
(cid:3)(cid:2)

n
i=1
(xi − ¯x)2

n
i=1

(yi − ¯y)2

(1)

where X = {x1, . . . , xi , . . . , xn} and Y = {y1, . . . , yi , . . . , yn}
represent the two vectors with a length of n. Furthermore, ¯x
and ¯y denotes the mean values for the vectors, respectively.
2) Relief-F (RF): One of the common ﬁlter-type methods
that works based on ranking features is RF [40]. The RF
identiﬁes conditional dependency among attributes, and it is
classiﬁed as a supervised technique. The priority goal
in
this ranking approach is to determine the features’ weight
individually using target data. The rating mechanism is based
on feature maximum distance. It is worth mentioning that
handling the multi-class problem and proper robustness in
noisy datasets are some of its merits. In contrast, the require-
ment for selecting a threshold is its drawback [41]. In this
method, the feature quality W (A) for all attributes A based

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:48 UTC from IEEE Xplore.  Restrictions apply. 

RADMAN etal.: MULTI-FEATURE FUSION APPROACH FOR ESD FROM EEG SIGNALS

3537

on a speciﬁed instance I0 is computed as follows:
(cid:4)

W (A) =

a(cid:4)
[

[ P(B) × di f f (A, I0, IM )
i

i=1
B(cid:2)=class( A)
− di f f (A, I0, IM )
i

]

]

(2)

where IH indicates the nearest hit instance from the same
class, IM denotes the nearest miss instance from a different
class. Moreover, a presents the nearest neighbor from the
various classes. Besides, P(B) implies each class’s prior prob-
ability, which is predicted from the training set. Additionally,
the function di f f (A, I 0, I ) shows the difference between the
values of A for both instances of I0 and I [41].

3) Compensation Distance Evaluation Technique (CDET):
The CDET is a well-known feature ranking method, which
was introduced by Lei et al. (2008) [42]. In this ﬁlter type
approach, features are ordered using their CDET scores in a
range of [0, 1]. Following that, the ranked features with lower
signiﬁcance are neglected. A feature set of A condition is
assumed as follows:
{T k
j k

, q = 1, 2, . . . , Q j ; j = 1, 2, . . . , J ; k = 1, 2, . . . , K }

(3)

where T k
i j represents kth eigenvalue from qth sample under
the j th condition. Furthermore, K denotes the feature number
for each condition. Besides, Q j indicates the sample number
for j th condition. It is noted that the ranking mechanism is
accomplished based on the average distance of the same con-
dition samples, DSk , divided to the average distance between
different condition samples, D Dk , which are formulated in the
following [42]:

DSk = 1
J

J(cid:4)

j =1

1
Q j × (Q j − 1)

Q j(cid:4)

l,q=1

where l and q take values among 1, 2, . . . , Q j and l (cid:2)= q.

D Dk =

1
J × (J − 1)

J(cid:4)

j,e

|T k
e

− 1
Q j

Q j(cid:4)

i−1

|

T k
i j

(5)

where j and e hold values among 1, 2, . . . , J and j (cid:2)= e.

4) FisherScore(FS): Another standard feature ranking pro-
cedure is FS [20]. The main idea is to select a feature subset
in a dataset such that data points in the same classes hold
the smallest distances, whereas data points in different classes
possess the largest distances [43]. The FS is expressed as
follows:

(μxn − μyn)2

F S =

+ σ 2
yn

σ 2
xn
where for N features with class labels l = (l1, l2, . . . , ln), μxn
and μyn denote mean value in x and y classes, respectively.
Moreover, σxn and σyn indicate standard deviation in x and y
classes, respectively.

(6)

D. FeatureFusion

Feature fusion is an intermediate-level fusion that is utilized
to combine features to achieve an optimal feature set for
decision-making or classiﬁcation purposes [44]–[46].

1) Dempster-ShaferEvidenceTheory(DSET): The evidence
theory was developed by Dempster and Shafer (1976) [47].
This algorithm has a great ability to deal with uncertainty.
The DSET is acknowledged as the generalization of Bayesian
theory to handle uncertainty in datasets, and enhance conﬁ-
dence in data mining approaches such as classiﬁcation [48].
The DSET is formulated by the Basic Probability Assignment
(BPA or m) as follows:

m : (cid:3)(X) −→ [0 1]
m((cid:4)) = 0,

(cid:4)

m(A) = 1

(7)

A∈P
where (cid:3)(X) represents a power set of X. Moreover, A ∈ (cid:3)(X)
which indicates that A is a subset in the power set (cid:3)(X).
Furthermore, (cid:4) denotes a null set. Additionally, m(A) holds
a value in a range of [0 1] for the subset A. It is noted
that the DSET for several BPAs can be formulated using
the orthogonal property of the subsets and the belief rule as
follows [49]:

m = m1 ⊕ m2 ⊕ . . . ⊕ m P ⇒
r(cid:5)

(cid:4)

m(A) = 1

1 − K

m j (Ai )

m((cid:4)) = 0, K =

∀Ai ⇒∩ p

i=1 Ai =A
(cid:4)

j =1

r(cid:5)

m j (Ai )

(8)

∀Ai ⇒∩ p

i=1 Ai =(cid:4)

j =1

where mi denotes a belief value for subset Ai . Moreover, p and
r represents the number of classes and classiﬁers, respectively.
In addition, K measures the conﬂict degree, which shows a
probability mass, concerning the conﬂicts among the evidence
sources.

The Decision Tree (DT) classiﬁer is a famous algorithm in
machine learning methods due to its several advantages such
as ﬂexibility, easy understanding, and easy debugging [50].
It has a ﬂowchart like a tree structure that helps to build
a decision rule generation model. The DT is classiﬁed as a
non-parametric supervised learning model that works based on
the divide and conquer process. The mechanism is based on
the recursive partitioning of input features into many different
subspaces to classify unlabeled data [51].

In machine learning, the Ensemble algorithm is known as
a technique that leads to increasing the accuracy of classiﬁers
by combining several of them [52]. The ensemble methods
consist of bagging, boosting [52], and stacking methods [53].
An important characteristic of ensemble methods is their
frequent improvement in predictive performance [54]. In the
boosting methods, which are not easy to overﬁt, at the ﬁrst,
equal initial uniform weight allots to all instances. Then, at a
new learning stage, each instance that has correctly classiﬁed
obtains less weight in comparison with instances that wrongly
classiﬁed until the system can concentrate on misclassiﬁed
instances. It leads to classifying them correctly during the next
learning step. Finally, the classiﬁers’ results are combined to
ﬁnd the ﬁnal prediction through a majority voting [55], [56].
Figure 1 shows the boosted EDT classiﬁer structure.

|T k
i j

− T k
l j

|

(4)

E. EnsembleDecisionTree(EDT)Classiﬁer

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:48 UTC from IEEE Xplore.  Restrictions apply. 

3538

IEEE SENSORS JOURNAL, VOL. 21, NO. 3, FEBRUARY 1, 2021

Fig. 1. The boosted EDT classiﬁer structure.

Fig. 3. The heatmap of PCC analysis.

Fig. 4. The percentage of the features in the shrunk feature set.

sub-band. Hence, eighty features become available for all fre-
quency sub-bands. Theses features include temporal, spectral,
and temporal-spectral (wavelet) domains, and therefore, they
can represent all properties of the EEG signals.

B. FeatureReduction

Generally, highly correlated features create redundant input
data, which negatively affects classiﬁer performance. There-
fore, the PCC analysis applies to these eighty features to
identify similar ones. Figure 3 shows the heatmap of PCC
analysis for eighty features. It is noted from Eq. (1) that PCC’s
values more than +0.9 and less than −0.9 refer to highly
correlated features. These values in Figure 3 correspond to
the points with white and black colors, respectively. At this
stage, redundant features are eliminated to shrink the feature
space to a slimmer space with only forty-three members.
Figure 4 shows the percentages of the selected forty-three
features related to the various domains in which features are
extracted from them.

It is noted from Figure 4 that the temporal participates 44%,
which is the highest percentage. Notably, the temporal-spectral
domain features are in the second rank.

Fig. 2. Flowchart of the Proposed ESD method.

III. SIMULATION STUDIES AND DESIGN
IMPLEMENTATIONS

In this section, simulation tests and design implementa-
tions of the proposed fusion ESD method are demonstrated.
Figure 2 shows the proposed ESD block diagram. It is noted
from Figure 2 that the proposed ESD method includes feature
extraction, feature reduction, feature ranking, feature fusion,
and EDT classiﬁcation block. In the following, the design
implementation of each block is brieﬂy illustrated.

A. FeatureExtraction

As we mentioned, the Butterworth ﬁlter is applied to EEG
signals to obtain ﬁve frequency sub-bands. Then, sixteen fea-
tures, correspond to Table I, are extracted from each frequency

C. FeatureRanking

At the feature ranking block, all the forty-three remaining
features are fed to one of three feature ranking methods until

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:48 UTC from IEEE Xplore.  Restrictions apply. 

RADMAN etal.: MULTI-FEATURE FUSION APPROACH FOR ESD FROM EEG SIGNALS

3539

Fig. 5. Associated weights to features from feature ranking methods.

the feature’s weight and ranks are assigned based on the
corresponding ranking methods’ criteria. Indeed, through this
occurrence, it is tried to sort remaining features in the reduced
extracted feature sets based on their weights and eligibility for
better separation between classes. Each ﬁlter-based ranking
method allocates a weight to each feature that the weight is
obtained based on their inner operation.

It is noted that the weights can take values in different
ranges. For instance, the RF weights are between −1 and +1,
while the CDET weights are between 0 and +1. Therefore,
It is necessary to rescale the weights for the feature ranking
methods in a range of [0 1]. The rescaling mechanism is
straightforward. For each proposed feature ranking method,
the feature weight is divided into the sum of all features’
weights. At the end of this procedure, there will be three
feature sets in which the summation of all features’ weights
in each method is equal to 1. Figure 5 shows the weights of
the feature rankings methods.

It is indicated from Figure 5 that all three feature ranking
methods associate considerable weights to Features 20-25.
These features, which belong to spectral, are more likely to
be correlated with Epileptic seizures.

D. FeatureFusion

Feature fusion combines the feature ranking methods using
the DSET, and obtains the integrated features. The main goal is
to utilize the DSET to obtain high-qualiﬁed features with less
amount of uncertainty using individual feature ranking meth-
ods. There are three ranking methods available. Therefore,
four combinations can be made, which are shown in Figure 6
Similarly, It is noted from Figure 6 that Features 20-25 gain
more weights. Thus, these features must inﬂuence the EDT
classiﬁer.

E. EDTClassiﬁer

In this section, the design implementation of the EDT classi-
ﬁer is illustrated. As we mentioned before, the datasets include
the normal, pre-ictal, and ictal classes. First, the datasets are
divided into two parts with 70% for the training, and 30% for
the test. Following that, Two common validation procedures,
including hold-out and 10-fold cross-validation, are utilized to
evaluate classiﬁer performance. Boosting approach is applied
to design the classiﬁer in both validation techniques. Moreover,
487 and 426 trees are utilized in the hold-out and 10-fold

Fig. 6. Associated weights to features from feature fusion methods.

TABLE II
THE MOST IMPORTANT PARAMETERS OF PROPOSED ESD

approaches, respectively. All design characteristics and para-
meters are summarized in TableII.

To determine the best conﬁguration of the proposed EDT
classiﬁer, the ranked feature sets, built in the previous sections,
are fed into the classiﬁer inputs, and their accuracies are
monitored. There exist three feature sets (Figure 5) from the
feature ranking methods, and also four integrated feature sets
(Figure 6) from the DSET method. These seven feature spaces
can be utilized to feed to the EDT classiﬁer. Then, the per-
formance of the EDT classiﬁer is presented and compared to
select the best feature sets that can maximize the classiﬁcation
accuracy.

In this presentation, the weighing factors allocated to each
feature indicates the inﬂuence and participation of this fea-
ture in the ﬁnal classiﬁer decision. Therefore, the features
are sorted with respect to their importance in each feature
set to feed the EDT classiﬁer. Afterward, for each feature
set,
the ﬁrst superb feature is fed to the classiﬁer, and
the classiﬁcation accuracy is plotted. We continue to add
the features from the feature set to maximize the classiﬁer
accuracy. Figures 7 and 8 illustrate the classiﬁcation accuracy
concerning the numbers of the features added to the EDT
classiﬁer in training and test phases, respectively.

It is noted from Figures 7 and 8 that the EDT classiﬁer
has reached to the best performance with the ﬁrst 20 superb
features. For the integrated RF and FS method, the classiﬁer
accuracies are 100% and 99.33% for the training and test
phases, respectively. Among the three basic feature selection
methods, including RF, CDET, and FS, none of them could
reach this performance. This fact shows that the obtained

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:48 UTC from IEEE Xplore.  Restrictions apply. 

3540

IEEE SENSORS JOURNAL, VOL. 21, NO. 3, FEBRUARY 1, 2021

Fig. 7. The classiﬁcation accuracy with respect to the numbers of the
features added in training phase for the seven feature sets.

Fig. 10. The confusion matrix of the proposed EDT classiﬁer for the
training phase.

Fig. 8. The classiﬁcation accuracy with respect to the numbers of the
features added in test phase for the seven feature sets.

Fig. 9. The input-output structure of the proposed EDT classiﬁer using
the ﬁrst superb twenty features.

feature set by utilizing the feature fusion approach leads
to better performance of the classiﬁer for the ESD task.
Therefore, the proposed EDT classiﬁer is developed using
the integrated RF and FS feature set. Figures 9 depicts the
input-output structure of the proposed EDT classiﬁer using
the superb twenty features.

Fig. 11. The confusion matrix of the proposed EDT classiﬁer for the test
phase.

IV. CLASSIFICATION RESULTS AND DISCUSSIONS

In this section, test result discussions are provided using
the proposed EDT classiﬁer using the integrated RF and FS
feature set. Figures 10 and 11 show the confusion matrix of
the proposed EDT classiﬁer in the training and test phases,
respectively.

It is noted from Figures 10 that the proposed EDT classiﬁer
identiﬁes all samples correctly in the training phase. Regarding
Figures 11, only one sample from pre-ictal is not detected and
mis-classiﬁed into health class.

sensitivity,

Furthermore,

speciﬁcity, and accuracy are
deﬁned based on the number of True Positive (TP), False
Positive (FP), True Negative(TN), and False Negative (FN)
as follows:

Sensitivity =

Speciﬁcity =

T P
T P + F N
T N
T N + F P

× 100%

× 100%

(9)

(10)

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:48 UTC from IEEE Xplore.  Restrictions apply. 

RADMAN etal.: MULTI-FEATURE FUSION APPROACH FOR ESD FROM EEG SIGNALS

3541

TABLE III
EDT CLASSIFIER PERFORMANCE IN TERMS OF ACCURACY, SENSITIVITY, SPECIFICITY, COHEN’S KAPPA COEFFICIENT, AND AUC

TABLE IV
A COMPARISON WITH THE OTHER METHODS IN THE LITERATURE BASED ON THE SAME USED DATASET
AND CLASSES (NORMAL, PRE-ICTAL, AND ICTAL), IN TERM OF ACCURACY

Accuracy =

T P + T N
T P + F P + T N + F N

× 100% (11)

In addition, Cohen’s kappa metric, which is known as a
more robust measure than a regular percent agreement metric
due to considering coincidentally occurring agreements [21],
is used as another performance evaluation criterion. Indeed,
this criterion evaluates the agreement between human expert
and classiﬁer output. It is worth mentioning that AUC, which
is the area under Receiver Operating Characteristic (ROC),
is another classiﬁer performance criterion that ranges from
zero to one. In the AUC criterion, the value which is closer to
one indicates a better classiﬁer performance. Table III collects
the accuracy, sensitivity, speciﬁcity, Cohen’s kappa coefﬁcient,
and the Area Under Curve (AUC) for the proposed ESD
method.

Moreover, a comparison with other methods in the literature
is illustrated in Table IV. According to Table IV, our proposed
EDT classiﬁer has the best performance in comparison with all
the other methods in the literature. Particularly, the proposed
EDT classiﬁer reaches a better accuracy than [20] when
the holdout technique with a 70% to 30% ratio is chosen.
Moreover, the proposed EDT classiﬁer achieves the accuracy
of 100% for 10-fold cross-validation technique.

V. CONCLUSION

This article introduced a multi-level fusion strategy for
the ESD in brain disorders. For this aim, the Butterworth
ﬁlter is adopted to decompose the brain signal
into ﬁve
frequency sub-bands. Then, eighty features were extracted
from these frequency sub-bands in temporal, spectral, and

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:48 UTC from IEEE Xplore.  Restrictions apply. 

3542

IEEE SENSORS JOURNAL, VOL. 21, NO. 3, FEBRUARY 1, 2021

temporal-spectral domains. Following that,
the PCC-based
feature selection methods were utilized to remove highly
correlated redundant features and obtain a shrunk feature set
with only forty-three features. Afterward, three feature ranking
methods, including the RF, CDET, and RF, were applied to
rescale and sort the selected features. Later, the DSET was
adapted to integrate the feature ranking methods and obtain
seven high-quality feature sets. Finally, the seven high-quality
features were fed into the EDT classiﬁer to detect various types
of Epileptic seizures. The EDT classiﬁer using integrated RF
and FS methods reached the highest accuracy compared to
the EDT classiﬁer with the other feature ranking methods and
the ESD methods in the literature. This is due to eliminating
redundant features and choosing a few high-qualiﬁed features
in the proposed ESD structure.

The main contribution was to employ various temporal,
spectral, and temporal-spectral domains to extract rich fea-
tures. It helped to catch the seizure characteristics and con-
sequently enhanced the detection rate. Another novelty was
to utilize the DSET to produce high-quality feature sets.
It improved the classiﬁcation accuracy.

The main advantage of the proposed ESD is its optimized
feature selection. Therefore, a few features are required in the
classiﬁcation task, which is proper for online implementation.
However, the utilized data in this approach is artifact-free. This
means that before applying the proposed ESD scheme to the
EEG signals, all types of noise and artifacts must be removed
using a de-noising method.

REFERENCES

[1] F. Mormann, R. G. Andrzejak, C. E. Elger, and K. Lehnertz, “Seizure
prediction: The long and winding road,” Brain, vol. 130, no. 2,
pp. 314–333, Feb. 2007.

[2] E. Alickovic, J. Kevric, and A. Subasi, “Performance evaluation of
empirical mode decomposition, discrete wavelet transform, and wavelet
packed decomposition for automated epileptic seizure detection and
prediction,” Biomed. Signal Process. Control, vol. 39, pp. 94–102,
Jan. 2018.

[3] S. Chakrabarti, A. Swetapadma, and P. K. Pattnaik, “A review on epilep-
tic seizure detection and prediction using soft computing techniques,” in
Smart Techniques for a Smarter Planet. Cham, Switzerland: Springer,
2019, pp. 37–51.

[4] M. Radman, A. Chaibakhsh, N. Nariman-zadeh, and H. He, “Gen-
eralized sequential forward selection method for channel selection in
EEG signals for classiﬁcation of left or right hand movement in BCI,”
in Proc. 9th Int. Conf. Comput. Knowl. Eng. (ICCKE), Oct. 2019,
pp. 137–142.

[5] J. A. de la O Serna, M. R. A. Paternina, A. Zamora-Mendez,
R. K. Tripathy, and R. B. Pachori, “EEG-rhythm speciﬁc Taylor–Fourier
ﬁlter bank implemented with O-splines for the detection of epilepsy
using EEG signals,” IEEE Sensors J., vol. 20, no. 12, pp. 6542–6551,
Jun. 2020.

[6] A. Subasi and M. Ismail Gursoy, “EEG signal classiﬁcation using PCA,
ICA, LDA and support vector machines,” Expert Syst. Appl., vol. 37,
no. 12, pp. 8659–8666, Dec. 2010.

[7] A. Subasi, “EEG signal classiﬁcation using wavelet feature extraction
and a mixture of expert model,” Expert Syst. Appl., vol. 32, no. 4,
pp. 1084–1093, May 2007.

[8] R. G. Andrzejak, K. Lehnertz, F. Mormann, C. Rieke, P. David, and
C. E. Elger, “Indications of nonlinear deterministic and ﬁnite-
dimensional structures in time series of brain electrical activity: Depen-
dence on recording region and brain state,” Phys. Rev. E, Stat. Phys.
Plasmas Fluids Relat. Interdiscip. Top., vol. 64, no. 6, Nov. 2001,
Art. no. 061907.

[9] O. Hanosh, R. Ansari, K. Younis, and A. E. Cetin, “Real-time epileptic
seizure detection during sleep using passive infrared sensors,” IEEE
Sensors J., vol. 19, no. 15, pp. 6467–6476, Aug. 2019.

[10] P. Boonyakitanont, A. Lek-uthai, K. Chomtho, and J. Songsiri,
“A review of feature extraction and performance evaluation in epileptic
seizure detection using EEG,” Biomed. Signal Process. Control, vol. 57,
Mar. 2020, Art. no. 101702.

[11] J. Kevric and A. Subasi, “The effect of multiscale PCA de-noising
in epileptic seizure detection,” J. Med. Syst., vol. 38, no. 10, p. 131,
Oct. 2014.

[12] A. Subasi, J. Kevric, and M. Abdullah Canbaz, “Epileptic seizure
detection using hybrid machine learning methods,” Neural Comput.
Appl., vol. 31, no. 1, pp. 317–325, Jan. 2019.

[13] S. M. S. Alam and M. I. H. Bhuiyan, “Detection of seizure and epilepsy
using higher order statistics in the EMD domain,” IEEE J. Biomed.
Health Informat., vol. 17, no. 2, pp. 312–318, Mar. 2013.

[14] M. Niknazar, S. R. Mousavi, B. Vosoughi Vahdat, and M. Sayyah,
“A new framework based on recurrence quantiﬁcation analysis for
epileptic seizure detection,” IEEE J. Biomed. Health Informat., vol. 17,
no. 3, pp. 572–578, May 2013.

[15] M. Peker, B. Sen, and D. Delen, “A novel method for automated
diagnosis of epilepsy using complex-valued classiﬁers,” IEEE J. Biomed.
Health Informat., vol. 20, no. 1, pp. 108–118, Jan. 2016.

[16] U. Orhan, M. Hekim, and M. Ozer, “EEG signals classiﬁcation using the
k-means clustering and a multilayer perceptron neural network model,”
Expert Syst. Appl., vol. 38, no. 10, pp. 13475–13481, 2011.

[17] A. K. Tiwari, R. B. Pachori, V. Kanhangad, and B. K. Panigrahi,
“Automated diagnosis of epilepsy using key-point-based local binary
pattern of EEG signals,” IEEE J. Biomed. Health Informat., vol. 21,
no. 4, pp. 888–896, Jul. 2017.

[18] U. R. Acharya, F. Molinari, S. V. Sree, S. Chattopadhyay, K.-H. Ng,
and J. S. Suri, “Automated diagnosis of epileptic EEG using entropies,”
Biomed. Signal Process. Control, vol. 7, no. 4, pp. 401–408, Jul. 2012.
[19] A. T. Tzallas, M. G. Tsipouras, and D. I. Fotiadis, “Automatic seizure
detection based on time-frequency analysis and artiﬁcial neural net-
works,” Comput. Intell. Neurosci., vol. 2007, pp. 1–13, Aug. 2007.
[20] R. Upadhyay, P. K. Padhy, and P. K. Kankar, “A comparative study of
feature ranking techniques for epileptic seizure detection using wavelet
transform,” Comput. Electr. Eng., vol. 53, pp. 163–176, Jul. 2016.
[21] A. R. Hassan, A. Subasi, and Y. Zhang, “Epilepsy seizure detection
using complete ensemble empirical mode decomposition with adaptive
noise,” Knowl.-Based Syst., vol. 191, Mar. 2020, Art. no. 105333.
[22] M. Li, W. Chen, and T. Zhang, “FuzzyEn-based features in FrFT-WPT
domain for epileptic seizure detection,” Neural Comput. Appl., vol. 31,
no. 12, pp. 9335–9348, Dec. 2019.

[23] F. Riaz, A. Hassan, S. Rehman, I. K. Niazi, and K. Dremstrup, “EMD-
based temporal and spectral features for the classiﬁcation of EEG signals
using supervised learning,” IEEE Trans. Neural Syst. Rehabil. Eng.,
vol. 24, no. 1, pp. 28–35, Jan. 2016.

[24] A. R. Hassan and M. A. Haque, “Epilepsy and seizure detection
using statistical features in the complete ensemble empirical mode
decomposition domain,” in Proc. IEEE Region 10 Conf. (TENCON),
Nov. 2015, pp. 1–6.

[25] G. Wang, Z. Deng, and K.-S. Choi, “Detection of epilepsy with
electroencephalogram using rule-based classiﬁers,” Neurocomputing,
vol. 228, pp. 283–290, Mar. 2017.

[26] A. B. Das, M. I. H. Bhuiyan, and S. M. S. Alam, “Classiﬁcation of
EEG signals using normal inverse Gaussian parameters in the dual-tree
complex wavelet transform domain for seizure detection,” Signal, Image
Video Process., vol. 10, no. 2, pp. 259–266, Feb. 2016.

[27] T. Zhang, W. Chen, and M. Li, “AR based quadratic feature extraction
in the VMD domain for the automated seizure detection of EEG using
random forest classiﬁer,” Biomed. Signal Process. Control, vol. 31,
pp. 550–559, Jan. 2017.

[28] A. R. Hassan and A. Subasi, “Automatic identiﬁcation of epileptic
seizures from EEG signals using linear programming boosting,” Comput.
Methods Programs Biomed., vol. 136, pp. 65–77, Nov. 2016.

[29] A. R. Hassan, S. Siuly, and Y. Zhang, “Epileptic seizure detection
in EEG signals using tunable-Q factor wavelet transform and boot-
strap aggregating,” Comput. Methods Programs Biomed., vol. 137,
pp. 247–259, Dec. 2016.

[30] S. Sanei and J. A. Chambers, EEG Signal Processing. Hoboken, NJ,

USA: Wiley, 2013.

[31] A. Bashashati, M. Fatourechi, R. K. Ward, and G. E. Birch, “A survey
of signal processing algorithms in brain–computer interfaces based on
electrical brain signals,” J. Neural Eng., vol. 4, no. 2, p. R32, 2007.

[32] B. B. Mandelbrot, D. E. Passoja, and A. J. Paullay, “Fractal character of
fracture surfaces of metals,” Nature, vol. 308, no. 5961, pp. 721–722,
Apr. 1984.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:48 UTC from IEEE Xplore.  Restrictions apply. 

RADMAN etal.: MULTI-FEATURE FUSION APPROACH FOR ESD FROM EEG SIGNALS

3543

[33] J. S. Richman and J. R. Moorman, “Physiological time-series analysis
using approximate entropy and sample entropy,” Amer. J. Physiol.-Heart
Circulatory Physiol., vol. 278, no. 6, pp. H2039–H2049, Jun. 2000.
[34] D. Zhang, “Wavelet transform,” in Fundamentals Image Data Mining.

Cham, Switzerland: Springer, 2019, pp. 35–44.

[35] H. Liu and H. Motoda, Computational Methods of Feature Selection.

Boca Raton, FL, USA: CRC Press, 2007.

[36] G. Chandrashekar and F. Sahin, “A survey on feature selection methods,”

Comput. Electr. Eng., vol. 40, no. 1, pp. 16–28, Jan. 2014.

[37] H. Liu and L. Yu, “Toward integrating feature selection algorithms for
classiﬁcation and clustering,” IEEE Trans. Knowl. Data Eng., vol. 17,
no. 4, pp. 491–502, Apr. 2005.

[38] T. Zhang, T. Zhu, P. Xiong, H. Huo, Z. Tari, and W. Zhou, “Correlated
differential privacy: Feature selection in machine learning,” IEEE Trans.
Ind. Informat., vol. 16, no. 3, pp. 2115–2124, Mar. 2020.

[39] M. Kordestani, A. Chaibakhsh, and M. Saif, “SMS—A security manage-
ment system for steam turbines using a multisensor array,” IEEE Syst.
J., vol. 14, no. 3, pp. 3813–3824, Sep. 2020.

[40] V. Ablavsky and M. R. Stevens, “Automatic feature selection with
applications to script identiﬁcation of degraded documents,” in Proc.
7th Int. Conf. Document Anal. Recognit., Aug. 2003, pp. 750–754.
[41] M. Robnik-Šikonja and I. Kononenko, “Theoretical and empirical analy-
sis of ReliefF and RReliefF,” Mach. Learn., vol. 53, nos. 1–2, pp. 23–69,
Oct. 2003.

[42] Y. Lei, Z. He, Y. Zi, and X. Chen, “New clustering algorithm-based fault
diagnosis using compensation distance evaluation technique,” Mech.
Syst. Signal Process., vol. 22, no. 2, pp. 419–435, Feb. 2008.

[43] Q. Gu, Z. Li,

and J. Han,

“Generalized Fisher

for
[Online]. Available:

score

feature
selection,”
http://arxiv.org/abs/1202.3725

2012,

arXiv:1202.3725.

[44] F. Castanedo, “A review of data fusion techniques,” Sci. World J.,

vol. 2013, pp. 1–19, 2013.

[45] M. Moradi, A. Chaibakhsh, and M. Mohammadi, “Multi-sensor fea-
ture fusion and grey wolf optimizer-based support vector machine for
transient fault detection in a once-through power plant,” in Proc. 27th
Iranian Conf. Electr. Eng. (ICEE), Apr. 2019, pp. 2067–2073.

[46] M. Rezamand, M. Kordestani, R. Carriveau, D. S.-K. Ting, and
M. Saif, “An integrated feature-based failure prognosis method for wind
turbine bearings,” IEEE/ASME Trans. Mechatronics, vol. 25, no. 3,
pp. 1468–1478, Jun. 2020.

[47] G. Shafer, A Mathematical Theory of Evidence, vol. 42. Princeton, NJ,

USA: Princeton Univ. Press, 1976.

[48] M. Beynon, D. Cosker, and D. Marshall, “An expert system for multi-
criteria decision making using dempster shafer theory,” Expert Syst.
Appl., vol. 20, no. 4, pp. 357–367, May 2001.

[49] K. Sentz and S. Ferson, Combination of Evidence in Dempster-Shafer
Theory, vol. 4015. Albuquerque, NM, USA: Sandia National Laborato-
ries, 2002.

[50] X. Liu, Z. Liu, G. Wang, Z. Cai, and H. Zhang, “Ensemble transfer
learning algorithm,” IEEE Access, vol. 6, pp. 2389–2396, 2018.
[51] S. Huda, J. Yearwood, H. F. Jelinek, M. M. Hassan, G. Fortino, and
M. Buckland, “A hybrid feature selection with ensemble classiﬁcation
for imbalanced healthcare data: A case study for brain tumor diagnosis,”
IEEE Access, vol. 4, pp. 9145–9154, 2016.

[52] M. Galar, A. Fernandez, E. Barrenechea, H. Bustince, and F. Herrera,
“A review on ensembles for the class imbalance problem: Bagging-
, Boosting-, and hybrid-based approaches,” IEEE Trans. Syst., Man,
Cybern., C, Appl. Rev., vol. 42, no. 4, pp. 463–484, Jul. 2012.

[53] J. Yoon, W. R. Zame, and M. van der Schaar, “ToPs: Ensemble learning
with trees of predictors,” IEEE Trans. Signal Process., vol. 66, no. 8,
pp. 2141–2152, Apr. 2018.

[54] A. Verikas, Z. Kalsyte, M. Bacauskiene, and A. Gelzinis, “Hybrid and
ensemble-based soft computing techniques in bankruptcy prediction: A
survey,” Soft Comput., vol. 14, no. 9, pp. 995–1010, Jul. 2010.

[55] L. N. Eeti and K. M. Buddhiraju, “Comparison of AdaBoost.M2 and
perspective based model ensemble in multispectral image classiﬁcation,”
in Proc. IEEE Annu. India Conf. (INDICON), Dec. 2016, pp. 1–5.
[56] F. Li, L. Xu, P. Siva, A. Wong, and D. A. Clausi, “Hyperspectral image
classiﬁcation with limited labeled training samples using enhanced
ensemble learning and conditional random ﬁelds,” IEEE J. Sel. Top-
ics Appl. Earth Observ. Remote Sens., vol. 8, no. 6, pp. 2427–2438,
Jun. 2015.

Moein Radman received the bachelor’s degree
from the University of Guilan, Rasht,
Iran,
in 2012, and the master’s degree in mechanical
engineering from the K. N. Toosi University of
Technology, Tehran, Iran, in 2015, respectively.
He is currently pursuing the Ph.D. degree with
the University of Guilan. During the Ph.D. studies,
he is also a member of ISACLAB. His current
research interests include the brain–computer
interface, signal processing, data mining, and
machine learning, with applications to biomedical
and health monitoring.

Milad Moradi received the B.Sc. and M.Sc.
degrees from the University of Guilan, Rasht,
Iran, in 2013 and 2016, respectively. He is cur-
rently pursuing the Ph.D. degree with the Uni-
versity of Windsor. The selection as a brilliant
talent student during his B.Sc. course, winning a
prestigious prize from Iran’s National Elites Foun-
dation, and working as a Research Assistant
with ISACLAB, University of Guilan from 2016 to
2020 are his honors and research experiences.
His research interests include machine learning,
fault diagnosis, and application of these areas in biomedical engineering,
and other complex engineering systems areas.

Ali Chaibakhsh (Member, IEEE) received the
B.Sc. degree from the University of Guilan,
Rasht, Iran, in 2002, and the M.Sc. degree and
the Ph.D. degree in mechanical engineering from
the K. N. Toosi University of Technology, Tehran,
Iran, in 2004 and 2009, respectively. He is an
Associate Professor of Mechanical Engineering
with industrial and academic research back-
grounds in process control and instrumentation.
His main research interests include intelligent
systems design and their applications in indus-
trial process systems. His special expertise areas are within control
systems, modeling and simulation, and fault diagnosis.

Mojtaba Kordestani (Senior Member,
IEEE)
received the bachelor’s degree in electronic engi-
neering from Malek Ashtar University in 2002,
and the master’s degree in control engineering
from Tehran Azad University, Iran, in 2008, and
the Ph.D. degree in electrical engineering from
the University of Windsor, Canada,
in 2018.
He is a Postdoctoral Fellow with the University of
Windsor. His research interests include control,
estimation, fault diagnostics, and failure progno-
sis. He has published about 40 refereed journal

articles and conference papers in these areas.

Mehrdad Saif (Senior Member, IEEE) received
the B.S., M.S., and D.Eng. degrees in electri-
cal engineering from Cleveland State Univer-
sity, Cleveland, OH, USA, in 1982, 1984, and
1987, respectively. He has been the Dean of
the Faculty of Engineering, University of Wind-
sor, since July 2011. Dr. Saif’s research inter-
ests include systems and control, estimation and
observer theory, model-based fault diagnostics,
condition monitoring, diagnostics and prognostic,
and application of these areas to automotive,
power, autonomous systems, and other complex engineering systems.
He has published over 350 refereed journal article and conference papers
plus an edited book in these areas.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:48 UTC from IEEE Xplore.  Restrictions apply.
