# Yu and Hu - 2021 - Epilepsy SEEG Data Classification Based On Domain Adversarial Learning

Received May 9, 2021, accepted May 31, 2021, date of publication June 7, 2021, date of current version June 14, 2021.

Digital Object Identifier 10.1109/ACCESS.2021.3086885

Epilepsy SEEG Data Classification Based
On Domain Adversarial Learning

HAO YU AND MENGQI HU
Shanghai Key Laboratory of Trustworthy Computing, East China Normal University, Shanghai 200062, China

Corresponding author: Hao Yu (haoyu@stu.ecnu.edu.cn)

ABSTRACT Epilepsy is a neurological disorder characterized by recurrent epileptic seizures. Although an
increasingly intense research effort has focused on the use of brain signal data to predict or detect epileptic
seizures as early as possible, this problem is still computationally challenging. The main challenge is that the
patient’s brain signal has strong individual characteristics, and the classiﬁcation model is easily disturbed by
this, which may lead to false predictions, affecting the reliability of the model. Based on the development
of brain signal acquisition technology and deep learning, we propose a new type of deep learning model
called the Epilepsy Domain Adversarial Neural Network (EDANN) model, which is used to classify epileptic
pre-ictal signals. EDANN integrates multiple deep neural networks based on the idea of adversarial learning,
which can reduce the impact of the differences between patients on model prediction. The multi-network
design in EDANN effectively improves the model training stability and model generalizability. In addition,
a unique brain signal processing algorithm is developed to convert signals to data blocks that are ready for
pre-ictal classiﬁcation, and the model may provide an auxiliary diagnosis for early warning of epilepsy.
Experimental results on real patient data show that EDANN clearly improved the F1 score by approximately
7.2% compared with the existing models. On a real dataset, our model achieved state-of-the-art results.

INDEX TERMS Brain signals, epilepsy, deep learning, domain adversarial neural network, SEEG.

I. INTRODUCTION
Epilepsy is one of the most common neurological disor-
ders with signiﬁcant social and economic impact [1] and
has various underlying causes [2]. Epileptic seizure, a result
of excessive and abnormal neuronal activity in the cor-
tex of the brain, can be conﬁrmed by scalp electroen-
cephalogram (EEG) [3], electrocorticography (ECoG) [4],
or stereo-electroencephalography (SEEG) [5].

In the recent decades, researchers have become increas-
ingly interested in utilizing brain signal data, mostly scalp
EEG, for seizure prediction or early detection [6]–[8].

This effort is motivated by the critical need to provide
patients and clinicians with a reliable warning during the
time between the start of measurable ictal evolution in brain
signals and the onset of disabling symptoms for the patient
for timely intervention and to potentially alter seizure evo-
lution [6]. This research may also provide insights into the
understanding of the underlying mechanisms of seizure initi-
ation and propagation [8].

The associate editor coordinating the review of this manuscript and

approving it for publication was Nuno Garcia

.

Despite decades of progress in the development of devices
and algorithms, reliable seizure prediction or early detection
is still computationally challenging. First, while scalp EEG
recordings have been widely used in daily practice, they are
highly susceptible to various bioelectric noise sources, posing
signiﬁcant challenges in the analysis and interpretation of
brain activities [9]. SEEG is a long-established technique
for the direct capture of electrophysiological signals from
the brain and records electrical activities with signiﬁcantly
more information and less noise than scalp EEG. However,
the patient-to-patient variance of the SEEG signals may be
large because that SEEG electrodes are implanted based on
the potential epileptogenic zone, which varies among the
patients. The high patient-to-patient variance also arises from
the wide demographic distribution and various epilepsy types
of the patients. Second, how early a seizure can be detected
remains an open question. There is no standard deﬁnition of
the duration of the pre-ictal and inter-ictal periods, although
a trained neurologist can identify pre-ictal spikes 30-60 min-
utes prior to seizure onset [10]. The determination of the time
window depends on the ability to perceive the changes in the
brain signals and on the region of the seizure onset. Third,
compared to the scale of the EEG datasets, which can include

82000

This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

VOLUME 9, 2021

H. Yu, M. Hu: Epilepsy SEEG Data Classification

FIGURE 1. SEEG electrode locations for a patient.

as many as hundreds of patients in a single study [11], a lim-
ited number of patients have undergone the SEEG procedure
and have had their seizures recorded. It is difﬁcult to mobilize
the existing SEEG-based analysis for epileptic pre-ictal signal
classiﬁcation [12], [13].

SEEG is a long-established technique to directly capture
electrophysiological signals from the brain through deep
electrodes surgically implanted into brain tissue [5]. It can
record electrical activities with signiﬁcantly more informa-
tion and less noise than scalp EEG. Fig. 1 shows a 3D
schematic diagram of a 27-year-old male epilepsy patient
(Patient-1 of the paper). The patient has a 15-year history
of seizures. To detect the epilepsy lesion, the doctor places
some electrodes in the suspicious area. An SEEG electrode
(e.g., A-J in Fig. 1) inserted into the human brain usually
contains multiple recording contacts (typically 8-16 con-
tacts with a 3.5 mm center-to-center distance) along each
electrode’s shaft. SEEG signal recordings have high ampli-
tudes (50-1500µv) and produce changes across a wide range
of frequencies (up to 10kHz) [14]. Fig. 2 shows the brain
signals collected by some electrodes. According to Fig. 2,
the patient has a seizure at approximately 5 seconds. Lever-
aging high-quality SEEG data and recent advances in deep
learning, we propose a novel deep learning algorithm called
Epilepsy Domain Adversarial Neural Network (EDANN) that
can distinguish seizures from non-seizure using SEEG sig-
nals a certain time prior to seizure onset (see Fig. 3). SEEG
can record electrical activities with signiﬁcantly more infor-
mation and less noise than scalp EEG. In this paper, we con-
sider all SEEG data from the same person to have the same
domain. Because these data often have the same individual
characteristics, this domain information will mislead the clas-
siﬁer, resulting in weak model generalization ability. The
EDANN model is designed based on the idea of adversar-
ial learning. It is mainly composed of three parts, encoder,
domain discriminator, and label classiﬁer. The encoder is
responsible for dimensionality reduction and local feature
extraction. The domain discriminator guides the encoder
to remove the domain information, and the label classiﬁer
completes the classiﬁcation on this basis. In the process of

FIGURE 2. Raw SEEG data with time on the x-axis and channel name on
the y-axis, where the dotted line indicates seizure onset.

FIGURE 3. SEEG data segmentation where data for both pre-ictal
signals (red) and no-seizure (blue) can be separated into 2-15 second
segments.

mutual adversarial learning, the model can ﬁnally complete
the classiﬁcation task without being affected by domain infor-
mation, greatly enhancing the generalization ability of the
model. The Python-based code can be found here.1

The main contributions of our work can be summarized as

follows:

• To the best of our knowledge, this study is the ﬁrst
to conduct more systematic mining of SEEG epilepsy
signals using the deep learning method.

• This paper proposes a deep learning model based on
epilepsy domain adversarial learning, which can adap-
tively classify different SEEG signals and achieves state-
of-the-art results compared with the benchmark model
on a real dataset. Our model may be used in actual
epilepsy diagnosis in the future.

• We constructed a real epilepsy SEEG dataset and veri-

ﬁed the effectiveness of our model.

II. RELATED WORK
In recent years, tools have been developed to characterize
seizure patterns from brain signals. However, most of the
tools are focused on scalp EEG data. Boashash et al. [15]
extracted seizure characteristics from newborn EEG by repre-
senting the EEG signals in the time-frequency domain using
the Beta distribution. Schiff et al. [16] developed a modern
numerical approach based on singular value decomposition
that can be applied to search for dynamically distinct stages of

1https://github.com/danzhewuju/Epilepsy-Domain-Adversarial-Neural-

Network

VOLUME 9, 2021

82001

epileptic seizures in humans. Dorr et al. [17] identiﬁed simi-
larities in the spatio-temporal dynamics of epileptic seizures
based on EEG. The method determined the time-varying
degree of nonlinear correlations between the scalp elec-
the seizure onset and during seizure spread.
trodes at
Fan et al. [18] developed a multivariate seizure detection
approach by representing the EEG signals with a recurrence
network.

Deep neural networks have been increasingly used for
EEG signal analysis. Yao et al. [19] identiﬁed epileptic
seizures through the analysis of EEG data, and this method
later became the standard machine learning approach for
identifying seizures from EEG data. Abramovici et al. [20]
assessed the utility of simultaneous scalp EEG in patients
with focal epilepsy undergoing intracranial EEG evaluation
after detailed presurgical testing. Chang et al. [21] found
that the transition from normal to seizure is not a sudden
phenomenon. Instead, it is a slow process that can be charac-
terized by the progressive loss of neuronal network resilience.
Truong et al. [22] applied a CNN-based generalized ret-
rospective and patient-speciﬁc seizure classiﬁcation model
using intracranial and scalp EEG data.

Although the existing works have revealed the EEG
seizure patterns in great detail,
they cannot be directly
adopted to analyze SEEG data, mainly because: 1) the
EEG channel position is relatively ﬁxed, whereas the SEEG
electrodes are implanted based on detailed analysis of an
anato-electro-clinical study of the potential epileptogenic
zone of every patient; 2) the sampling frequency of EEG
is much lower than that of SEEG; and 3) manual param-
eter adjustment is still inevitable when applying a trained
model to new patients. To date, only a few studies have
attempted to identify seizure patterns in SEEG data. Brain-
storm [12] is a collaborative application with a rich and
intuitive graphic interface dedicated to the analysis of brain
recordings, including EEG, ECoG, and SEEG. MNE [13] is
a tool for exploring, visualizing, and analyzing neurophysi-
ological data. Sharma et al. [23] developed a tool to predict
seizure timing and identify epileptic areas from SEEG data.
Zhang et al. [24] developed an epileptic seizure classiﬁcation
tool to analyze the power spectrum of the SEEG signals.
However, the applicability of these tools remains limited due
to the high data complexity.

III. METHOD
We propose EDANN for epileptic pre-ictal signal classiﬁca-
tion, which will be beneﬁcial for research on epilepsy early
warning.

A. SEEG DATA PREPROCESSING
We expect the model to capture the SEEG features between
multiple channels in the data preprocessing stage and then
learn the global SEEG features. First, the channels of the
SEEG signal can be reordered, and the formal expression is
as follows: Let C = {c1, c2, c3 . . . cn} represent the set of
physical coordinates of all n channels in the SEEG signal.

H. Yu, M. Hu: Epilepsy SEEG Data Classification

Here ci(i = 1 . . . N ) represents the physical coordinates of
the ith channel in C. We can deﬁne an undirected complete
graph G(V , E), where V represents a collection of channel
nodes. vi denotes the ith node in V , and its corresponding
physical coordinate is ci. E represents the set of edges, and
ei,j represents the edges that exist between nodes vi and vj.
For the edges, the weight value on any edge ei,j is deﬁned as
follows:

(cid:1)

w (cid:0)ei,j

(cid:1) = D (cid:0)vi, vj
where D(·) represents the Euclidean distance. In G(V , E),
there is a subset of T in E. The minimum spanning tree
can be constructed by minimizing the global weight value.
W (T ) is expressed as the sum of the weights of the edges
of the minimum spanning tree. The formal expression is as
follows:

(1)

W(T ) = min





(cid:88)

w (cid:0)ei,j


(cid:1)


ei,j∈T

(2)

The overall ﬂow chart is shown in Fig. 4. Fig. 4(a)
shows the distribution of channel contacts in the brain space;
Fig. 4(b) shows a deep search at any node in the constructed
minimum spanning tree; Fig. 4(c) is completed through a
deep search; and Fig. 4(d) shows that the original SEEG sig-
nals are reordered according to the sequence. From Fig. 4(d),
it is observed that there is a certain similarity between the
SEEG signals of adjacent channels, which helps the model
better encode SEEG signal features. On the one hand, adja-
cent channels have similar SEEG signals, and arranging sim-
ilar SEEG signals can make it easier for the model to learn
local features. On the other hand, this method can realize
personalized data preprocessing. The number and location
of each person’s channels are inconsistent. Through the data
preprocessing method, different sequences can be generated
for different people, providing more effective use of the
information contained in the SEEG data. Finally, due to the
long recording time of the SEEG data, the data are not easy
to process and analyze, so this article adopts a standard pro-
cessing method to slice the SEEG signal. The original SEEG
signal is represented as a matrix, where the abscissa of the
matrix represents time, and the ordinate represents the sorted
channel sequence, as shown in Fig. 4(d). Next, the SEEG
signal must be sliced, and the related processing procedure
can be formally expressed as follows:

(3)

X = win(ﬂt(sampl(Z , r), flow, fhigh), ω)
where sampl(.) is a resampling function with sampling rate r,
ﬂt(.) is a band passing function, where flow and fhigh are
the low- and high-frequency thresholds, and win(.) is a
window function for converting a long SEEG signal into
variable-length segments, with its length being ω, where ω
is not a ﬁxed value but rather a random value within a certain
range.

Overall, to approach the realistic case, we process the
original data into fragments of 2-15 seconds. For the model,

82002

VOLUME 9, 2021

H. Yu, M. Hu: Epilepsy SEEG Data Classification

FIGURE 4. Schematic diagram of the SEEG data preprocessing.

FIGURE 5. EDANN contains 3 modules. The structure of EDANN consists of an encoder, a label classifier, and a
domain discriminator. The encoder is a convolutional neural network (CNN) [25], which learns an embedding for
every 1 second of the SEEG segment. The label classifier is a Transformer [26] or LSTM model that is used to
discriminate the target SEEG data. The domain discriminator is a bidirectional long short-term memory (BiLSTM)
model [27] that determines whether a pair of data comes from the same patient. It can help the encoder reduce
the difference between individuals and learn the correct characteristics.

identiﬁcation of variable-length fragments is more complex
than the task of identifying ﬁxed-length fragments because
the variable length of the data segment requires the model to
be able to learn the critical features of the SEEG signal truly.
The difference in the segment length (minimum length 2 s,
maximum length 15 s) is particularly signiﬁcant. The setting
can help our model deal with more complex situations; these
fragments will serve as input to our model. At the same time,
it can also learn the possible associations between the SEEG
sequences.

B. PRE-ICTAL SIGNAL CLASSIFICATION
The EDANN model includes three main modules: encoder,
label classiﬁer, and domain discriminator. Its structure is
shown in Fig. 5. The encoder is mainly used to encode the
original raw SEEG data and can learn the relevant EEG
features from the SEEG signal and reduce the dimensionality
of the data. The domain discriminator is mainly used to
determine whether a pair of SEEG segments are different.
For the same patient, the domain discriminator can be opti-
mized adversarially through the gradient reversal layer (GRL)
module. This ensures that the network cannot classify based

on domain knowledge and reduces the interference of the
SEEG data in the model due to individual differences. The
class discriminator classiﬁes the target SEEG data.

The encoder can be represented as fe(X ; θe) and can extract
multi-channel EEG signals while reducing the dimensions of
the original SEEG signals. θe represents the parameters of
the encoder. The label classiﬁer can be expressed as fl(fe; θl),
which is an attempt to predict the label of input X , where θl
represents the parameters learned by the discriminator. The
domain discriminator can be expressed as fd (fe; θd ), which
aims to determine whether a pair of inputs X1 and X2 are from
the same patient. Here, X2 is based on random sampling. The
ﬁnal loss comes from two parts, where the ﬁrst component
is the prediction loss of the label classiﬁer Ll(fl(fe; θl)) and
the other component is the loss of the domain discriminator
Ld (fd (fe; θd )). For a pair of input X1 and X2, the loss is given
as follows:

L (X1, X2; θe, θl, θd )

= Ll (fl (fe (X1; θe) ; θl))

−γ Ld (fd (fe (X1; θe) ; θd ) , fd (fe (X2; θe) ; θd ))

(4)

VOLUME 9, 2021

82003

H. Yu, M. Hu: Epilepsy SEEG Data Classification

TABLE 1. SEEG dataset information.

where γ are hyperparameters. For convenience, we use
Z1 and Z2 to denote the hidden representations of X1 and X2
calculated from encoder fe(X ; θe). The loss of the label clas-
siﬁer Ll(fl(Z1; θl)) can be denoted with binary cross entropy:
Ll(fl(Z1; θl)) = −[y1 log fl(Z1) + (1 − y1) log(1 − fl(Z1))]

(5)

where y1 represents the label of input data X1, and fl(Z1)
denotes the value of the prediction by the label classiﬁer.

The constructive loss of the domain discriminator Ld can

be expressed as follows:

=

1
2

Ld (fd (Z1; θd ) , fd (Z2; θd ))
D (fd (Z1) , fd (Z2))2 I
1
2

+

(max {0, m − D (fd (Z1) , fd (Z2))})2 (1 − I ) (6)

where I can be either 0 or 1, with I = 1 indicating that the two
samples are from the same patient and I = 0 indicating the
opposite. D(.) is the Euclidean distance, and m is the margin
that indicates the prediction boundary. The loss of all samples,
Lt , is deﬁned as follows:

Lt =

N
(cid:88)

i,j

αL(Xi, Xj; θe, θl, θd )

(7)

where N represents the number of data pairs. Xi and Xj
represent the input data pair, α indicates the hyperparameters,
and θe, θl and θd are the parameters of the encoder, label
classiﬁer and domain discriminator, respectively.

The domain classiﬁer of the EDANN model is a BiLSTM
model. The working principle of BiLSTM is to ﬁrst extract
the local features of the SEEG signal space of the window
(window size = 1 s) through a convolutional neural network.
The CNN model encodes a 16-dimensional representation of
each second SEEG signal (1 s), so that the original SEEG
segment can be expressed as a matrix with a matrix size of
n × 16, where n represents the length of the SEEG segment
(n · s, n ∈ [2, 15]). Then, BiLSTM is used to capture the rela-
tionship between the representations of the two directions,
and then learn the global characteristics of the SEEG signal in
time. According to the global characteristics, it can be judged
whether two SEEG segments come from the same domain
(whether two SEEG segments come from the same patient.).
EDANN’s label classiﬁer is an LSTM or Transformer
model. According to the different selected models, EDANN
models can be divided into EDANN-LSTM and EDANN-
Transformer. The label classiﬁer can classify the SEEG
segment according to the representation learned by the
encoder.

IV. EXPERIMENTAL RESULTS
A. DATASET
We collect the SEEG data from multiple epilepsy patients (an
average of 130 channels per patient) from Huashan Hospital
afﬁliated with Fudan University in Shanghai. There are a total

TABLE 2. Number of SEEG segments.

of 24 patients’ SEEG information, for which pre-ictal SEEG
data (within an hour before the seizure) and no-seizure SEEG
data (more than 12 hours after epileptic seizures) are collected
from 5 patients, and only pre-epilepsy SEEG information is
collected from 19 patients. We record many times for each
patient. Limited by the incompleteness of the actual medical
data, there are cases where some patient data collection is
incomplete. All the information is shown in Table 1. For
patients-I-V, we sample 2000 and 6000 fragments of variable
length for the pre-ictal and no-seizure categories, respec-
tively. The fragment length ranges from 2 s to 15 s. For the
other patients, we use the following calculation formula to
calculate the number of samples:

count =

duration ∗ 2 ∗ k
max_window − min_window

(8)

where duration represents the total length of the record.
max_window and min_window represent the maximum and
minimum lengths of the SEEG segments, respectively, and k
denotes the number of resampling. Equation 8 can make full
use of each patient’s SEEG data and can also take into account
the large difference in the length of the data for each patient.
The speciﬁc fragment information is presented in Table 2.

82004

VOLUME 9, 2021

H. Yu, M. Hu: Epilepsy SEEG Data Classification

B. EVALUATION METRIC
The evaluation measurements, including accuracy, precision,
recall (sensitivity), f1 score, area under the curve (AUC) and
false alarm rate (FAR), are deﬁned as follows:

Accuracy =

TP + TN
TP + TN + FP + FN

Sensitivity = Recall =

TP
TP + FN

(9)

(10)

(12)

(11)

FAR =

F1 score =

Precision =

TP
TP + FP
2 × Precision × Recall
Precision + Recall
FP
FP + TN
where TP is the number of true pre-ictal (pre-seizure) SEEG
segments, FN is the number of false no-seizure SEEG seg-
ments, TN is the number of true no-seizure (normal) SEEG
segments, and FP is the number of false pre-ictal SEEG seg-
ments. The F1 score is often used to evaluate the performance
of a model under unbalanced data, and the FAR index is often
used to measure the misreporting of epilepsy by software in
the diagnosis of clinical epilepsy. The deﬁnition of AUC is
the area under the ROC [28] curve.

(13)

C. EXPERIMENTAL SETTING
To make the model more suitable for the actual situa-
tion, we use the leave-one-out method to verify the perfor-
mance of the model. We select 5 patients who had both
pre-ictal SEEG data and no-seizure SEEG data as the test
set, and all of the remaining data are used as the training
set. We use the traditional machine learning method based
on convolutional support vector machine CNN-SVM [29]
and neural network-based methods such as VDCNN [30],
DPCNN [31], CNN-Voting [31], PIESD [32], LSTM [33]
and Transformer [34] for comparison. We use the same data
preprocessing and data input for all of the methods. In the
CNN-SVM method, we learn the hidden representation of
SEEG data for each window (window size = 1 s) through the
CNN model and ﬁnally use the SVM model for classiﬁcation.
In the CNN-Voting method, the model gives a prediction
result for each window (window size = 1 s) and ﬁnally
gives the ﬁnal prediction result through voting. VDCNN and
DPCNN are commonly used for sentence classiﬁcation, but
if the word embedding is replaced with a window data repre-
sentation (window size = 1 s), then the VDCNN and DPCNN
models can also be used for classiﬁcation of SEEG or EEG
signals. Patient-Independent Epileptic Seizure (PIESD) is
an EEG seizure classiﬁcation algorithm based on adversar-
ial learning, but PIESD is a classiﬁcation algorithm with a
ﬁxed length data input. In the experiment, we use the set-
ting reported by Zhang et al. to reduce the length of the
input data to 1 s [32]. At the same time, we compare the
experimental effects of replacing the category discrimina-
tor of the domain adversarial neural network with LSTM

(EDANN-LSTM) and Transformer (EDANN-Transformer).
The EDANN-Transformer and EDANN-LSTM models use
the same CNN encoder structure. The encoder includes four
convolutional layers, four max-pooling layers, four ReLu
regularization functions and a Dropout(0.5) layer. Finally,
the dimension of the hidden vector is 32. Both models use the
same BiLSTM domain discriminator, which contains 2 bidi-
rectional LSTM layers and 64 hidden units.

In the experiment,
the main difference between the
(EDANN-LSTM) model and the
EDANN-Transformer
Transformer (LSTM) model is that there is a domain dis-
criminator. They have the same encoder module and label
classiﬁer. The label classiﬁer Transformer of EDANN-
Transformer has the same structure as that used in paper [35].
The label classiﬁer Transformer of EDANN-LSTM includes
64 hidden units. All of the methods use the same data pre-
processing. The learning rate α of EDANN-* model is set to
0.0005, and hyperparameter γ is set to 0.3. EDANN models
are built on the Pytorch framework and are deployed on a
server with an Intel i9 CPU and NVIDIA GeForce RTX
2080Ti. On average, 14 h are required to complete the model
training.

D. EXPERIMENTAL RESULTS
Tables 3-7 show the performance of our model and the bench-
mark model on the SEEG data of 5 test patients. An exami-
nation of the results presented in the Tables shows that the
domain-based adversarial SEEG classiﬁcation method pro-
posed in this paper achieves the best results. In particular,
the method based on EDANN-Transformer achieves the best
results on all patients with respect to the F1 score. Tables 4
and 5 show that our model outperforms the benchmark model
by approximately 4.5% in terms of the F1 score. This is due to
the nature of the SEEG signal. Because the SEEG signal has
non-stationary characteristics, the epilepsy characteristics of
some people are more obvious, so even a relatively simple
model can perform well. According to Tables 3, 6 and 7,
the EDANN-Transformer model outperforms the baseline
model by approximately 9% in terms of the F1 score, which
also shows that the idea of using domain adversarial learning
can effectively reduce the interference of individual informa-
tion. At the same time, we can also see from Tables 3-7 that
the PIESD method based on adversarial learning performs
similarly to the general CNN-based method. However, they
are inferior to the time series model (LSTM and Transformer)
in processing variable-length data.

In terms of the FAR, our models, including EDANN-LSTM
and EDANN-Transformer, are generally stable with lower
FAR, which is important in clinical practical applications.
An examination of the data presented in Table 3 shows that
our model has the worst FAR index of 2.67%, which is still
a quarter of that of the best benchmark model performance.
Table 5 shows that our model EDANN-Transformer has the
best FAR index of 0.45%, which is also better than the
benchmark model.

VOLUME 9, 2021

82005

TABLE 3. Performance of EDANN and all of the compared methods on pre-ictal signal classification using SEEG data of patient-I.

H. Yu, M. Hu: Epilepsy SEEG Data Classification

TABLE 4. Performance of EDANN and all of the compared methods on pre-ictal signal classification using SEEG data of patient-II.

TABLE 5. Performance of EDANN and all of the compared methods on pre-ictal signal classification using SEEG data of patient-III.

TABLE 6. Performance of EDANN and all of the compared methods on pre-ictal signal classification using SEEG data of patient-IV.

TABLE 7. Performance of EDANN and all of the compared methods on pre-ictal signal classification using SEEG data of patient-V.

To verify the effect of reordering the SEEG segment rows
in the data preprocessing, we use the EDANN-Transformer
model to compare the performance with different channel

ordering methods on ﬁve patients. In Fig. 6, Reordering
means using our sorting method, and Random means using
the SEEG default channel order (the SEEG default order is

82006

VOLUME 9, 2021

H. Yu, M. Hu: Epilepsy SEEG Data Classification

FIGURE 6. Influence of different ordering of the channels on the
EDANN-Transformer model in data preprocessing.

FIGURE 8. Impact of hyperparameter γ on the accuracy for patient-I SEEG
data.

TABLE 8. Ablation experiment exploring the influence of the domain
discriminator on the experiment.

FIGURE 7. Impact of fragment length on accuracy.

sorted according to the channel ID). Experimental results
show that the performance of EDANN-Transformer on the
data after channel reordering is 5.33% better than the ran-
dom order on average, proving the effectiveness of data
preprocessing.

Since our model uses variable-length data for training,
we compare the accuracy for data with different lengths.
Fig. 7 shows how the accuracy of the model (EDANN-
Transformer) varies with different sizes of the fragment
length. It is observed from Fig. 7 that when the fragment
length is less than 5 s, the accuracy rate increases drastically
with increasing fragment length; when the fragment length
size is 5-11 s, as the fragment length increases, the accuracy
of the model increases slowly; and when the fragment length
is longer than 11 s, as the length increases, the accuracy
of the model remains basically unchanged. This shows that
the model requires a speciﬁc fragment length size to cap-
ture relevant signals. The amount of information obtained
by our model decreases with decreasing fragment length,

increasing the likelihood of wrong predictions. However, too
long fragments increase the noise in the data, which will
also reduce the model’s prediction accuracy. The experiment
shows that the optimal recognition fragment length size of the
model is approximately 11 s. In the clinic, the time required
by the doctors to recognize epilepsy characteristic signals
is approximately ten seconds, which is consistent with our
experimental results.

The parameter γ in the experiment has a signiﬁcant inﬂu-
ence on the accuracy. We explore the inﬂuence of parameter
γ from 0 to 0.5 on the EDANN-Transformer model for the
SEEG data of patient-I. It is observed from Fig. 8 that when
γ is less than 0.3, the accuracy of the model increases with
increasing γ . When γ = 0.3, the accuracy of the model
reaches the maximum value of approximately 95%, and as γ
increases, the accuracy of the model gradually decreases. This
trend is observed because when γ is small, the contribution
of the domain discriminator to the entire model is relatively
small, and the model can easily learn incorrect informa-
tion about the patient, leading to low performance of the
model. When γ is greater than 0.3, the domain discriminator
interferes with the learning of the label classiﬁer, and the
accuracy of the model decreases. This means that the domain
discriminator is important for the appropriate functioning of
the EDANN-* model.

To further study the inﬂuence of the domain discrimi-
nator and label classiﬁer on the experiment, we conduct
an ablation experiment, with the results shown in Table 8,

VOLUME 9, 2021

82007

in which -domain discriminator means that the domain dis-
criminator is removed, and +domain discriminator means to
that the domain discriminator is added. We use LSTM and
Transformer as the label classiﬁer to compare their experi-
mental F1 score results. It is observed from Table 8 that the
domain discriminator has a greater impact on the F1 score of
the experiment. In particular, the impact on the Transformer
model is more pronounced. Probably because the model
parameters of LSTM are fewer than those of the Transformer
model, the domain discriminator is not as helpful to the
LSTM model as it is to the Transformer model.

V. CONCLUSION
In this paper, we propose an SEEG classiﬁcation algorithm
based on domain adversarial learning. This method adopts the
idea of adversarial learning and uses the domain discriminator
to supervise the encoder to perform encoding by removing
individual information, and the label classiﬁer is used to
guide the encoder to extract the SEEG features. Through
the adversarial learning method, the encoder can not only
learn the relevant characteristics of SEEG but also remove the
interference of individual information. This algorithm shows
improved performance on a real epilepsy diagnosis dataset.
This has positive signiﬁcance for SEEG signal processing and
clinical medical treatment.

REFERENCES

[1] S.-J. Chang and B.-C. Yu, ‘‘Mitochondrial matters of the brain: Mito-
chondrial dysfunction and oxidative status in epilepsy,’’ J. Bioenergetics
Biomembranes, vol. 42, no. 6, pp. 457–459, Dec. 2010.

[2] S. D. Shorvon, ‘‘The causes of epilepsy: Changing concepts of etiology of
epilepsy over the past 150 years,’’ Epilepsia, vol. 52, no. 6, pp. 1033–1044,
Jun. 2011.

[3] M. Zhou, C. Tian, R. Cao, B. Wang, Y. Niu, T. Hu, H. Guo, and J. Xiang,
‘‘Epileptic seizure detection based on EEG signals and CNN,’’ Frontiers
Neuroinform., vol. 12, p. 95, Dec. 2018.

[4] N. Nakasatp, M. F. Levesque, D. S. Barth, C. Baumgartner, R. L. Rogers,
and W. W. Sutherling,
‘‘Comparisons of MEG, EEG, and ECoG
source localization in neocortical partial epilepsy in humans,’’ Electroen-
cephalogr. Clin. Neurophysiol., vol. 91, no. 3, pp. 171–178, Sep. 1994.
[5] O. David, T. Blauwblomme, A.-S. Job, S. Chabardès, D. Hoffmann,
L. Minotti, and P. Kahane, ‘‘Imaging the seizure onset zone with
stereo-electroencephalography,’’ Brain, vol. 134, no. 10, pp. 2898–2911,
Oct. 2011.

[6] C. C. Jouny, P. J. Franaszczuk, and G. K. Bergey, ‘‘Improving early seizure

detection,’’ Epilepsy Behav., vol. 22, pp. S44–S48, Dec. 2011.

[7] M. K. Siddiqui, R. Morales-Menendez, X. Huang, and N. Hussain,
‘‘A review of epileptic seizure detection using machine learning classi-
ﬁers,’’ Brain Informat., vol. 7, no. 1, pp. 1–18, Dec. 2020.

[8] K. Schindler, H. Leung, C. E. Elger, and K. Lehnertz, ‘‘Assessing seizure
dynamics by analysing the correlation structure of multichannel intracra-
nial EEG,’’ Brain, vol. 130, no. 1, pp. 65–77, Nov. 2006.

[9] A. Puce and M. Hämäläinen, ‘‘A review of issues related to data acquisition
and analysis in EEG/MEG studies,’’ Brain Sci., vol. 7, no. 12, p. 58,
May 2017.

[10] E. J. Ngamga, S. Bialonski, N. Marwan, J. Kurths, C. Geier, and
K. Lehnertz, ‘‘Evaluation of selected recurrence measures in discriminat-
ing pre-ictal and inter-ictal periods from epileptic EEG data,’’ Phys. Lett.
A, vol. 380, no. 16, pp. 1419–1425, Apr. 2016.

[11] D. A. Dean, A. L. Goldberger, R. Mueller, M. Kim, M. Rueschman,
D. Mobley, S. S. Sahoo, C. P. Jayapandian, L. Cui, M. G. Morrical,
S. Surovec, G.-Q. Zhang, and S. Redline, ‘‘Scaling up scientiﬁc discovery
in sleep medicine: The national sleep research resource,’’ Sleep, vol. 39,
no. 5, pp. 1151–1164, May 2016.

H. Yu, M. Hu: Epilepsy SEEG Data Classification

[12] F. Tadel, S. Baillet, J. C. Mosher, D. Pantazis, and R. M. Leahy, ‘‘Brain-
storm: A user-friendly application for MEG/EEG analysis,’’ Comput.
Intell. Neurosci., vol. 2011, pp. 1–13, Oct. 2011.

[13] A. Gramfort, M. Luessi, E. Larson, D. A. Engemann, D. Strohmeier,
C. Brodbeck, L. Parkkonen, and M. S. Hämäläinen, ‘‘MNE software
for processing MEG and EEG data,’’ NeuroImage, vol. 86, pp. 446–460,
Feb. 2014.

[14] G. Li, S. Jiang, S. E. Paraskevopoulou, M. Wang, Y. Xu, Z. Wu,
L. Chen, D. Zhang, and G. Schalk, ‘‘Optimal referencing for stereo-
electroencephalographic (SEEG) recordings,’’ NeuroImage, vol. 183,
pp. 327–335, Dec. 2018.

[15] B. Boashash, M. Mesbah, and P. Colditz, ‘‘Newborn EEG seizure pattern
characterisation using time-frequency analysis,’’ in Proc. IEEE Int. Conf.
Acoust., Speech, Signal Process., vol. 2, May 2001, pp. 1041–1044.
[16] S. J. Schiff, T. Sauer, R. Kumar, and S. L. Weinstein, ‘‘Neuronal spa-
tiotemporal pattern discrimination: The dynamical evolution of seizures,’’
NeuroImage, vol. 28, no. 4, pp. 1043–1055, Dec. 2005.

[17] V. L. Dorr, M. Caparos, F. Wendling, J.-P. Vignal, and D. Wolf, ‘‘Extraction
of reproducible seizure patterns based on EEG scalp correlations,’’ Biomed.
Signal Process. Control, vol. 2, no. 3, pp. 154–162, Jul. 2007.

[18] M. Fan and C.-A. Chou, ‘‘Detecting abnormal pattern of epileptic seizures
via temporal synchronization of EEG signals,’’ IEEE Trans. Biomed. Eng.,
vol. 66, no. 3, pp. 601–608, Mar. 2019.

[19] X. Yao, X. Li, Q. Ye, Y. Huang, Q. Cheng, and G.-Q. Zhang,
‘‘A robust deep learning approach for automatic classiﬁcation of seizures
against non-seizures,’’ 2018, arXiv:1812.06562. [Online]. Available:
http://arxiv.org/abs/1812.06562

[20] S. Abramovici, A. Antony, M. E. Baldwin, A. Urban, G. Ghearing,
J. Pan, T. Sun, R. T. Krafty, R. M. Richardson, and A. Bagic, ‘‘Features
of simultaneous scalp and intracranial EEG that predict localization of
ictal onset zone,’’ Clin. EEG Neurosci., vol. 49, no. 3, pp. 206–212,
May 2018.

[21] W.-C. Chang, J. Kudlacek, J. Hlinka, J. Chvojka, M. Hadrava, V. Kumpost,
A. D. Powell, R. Janca, M. I. Maturana, P. J. Karoly, D. R. Freestone,
M. J. Cook, M. Palus, J. Otahal, J. G. R. Jefferys, and P. Jiruska, ‘‘Loss of
neuronal network resilience precedes seizures and determines the ictogenic
nature of interictal synaptic perturbations,’’ Nature Neurosci., vol. 21,
no. 12, pp. 1742–1752, Dec. 2018.

[22] N. D. Truong, A. D. Nguyen, L. Kuhlmann, M. R. Bonyadi, J. Yang,
S. Ippolito, and O. Kavehei, ‘‘Convolutional neural networks for seizure
prediction using intracranial and scalp electroencephalogram,’’ Neural
Netw., vol. 105, pp. 104–111, Sep. 2018.

[23] A. Sharma, J. K. Rai, and R. P. Tewari, ‘‘Scalp electroencephalography
(sEEG) based advanced prediction of epileptic seizure time and identiﬁ-
cation of epileptogenic region,’’ Biomed. Eng./Biomedizinische Technik,
vol. 65, no. 6, pp. 705–720, Nov. 2020.

[24] Z. Zhang and K. K. Parhi, ‘‘Low-complexity seizure prediction from
iEEG/sEEG using spectral power and ratios of spectral power,’’
IEEE Trans. Biomed. Circuits Syst., vol. 10, no. 3, pp. 693–706,
Jun. 2016.

[25] A. S. Razavian, H. Azizpour, J. Sullivan, and S. Carlsson, ‘‘CNN features
off-the-shelf: An astounding baseline for recognition,’’ in Proc. IEEE Conf.
Comput. Vis. Pattern Recognit. Workshops, Jun. 2014, pp. 806–813.
[26] Q. Wang, B. Li, T. Xiao, J. Zhu, C. Li, D. F. Wong, and L. S. Chao,
‘‘Learning deep transformer models for machine translation,’’ 2019,
arXiv:1906.01787. [Online]. Available: http://arxiv.org/abs/1906.01787

[27] G. Liu and J. Guo, ‘‘Bidirectional LSTM with attention mechanism and
convolutional layer for text classiﬁcation,’’ Neurocomputing, vol. 337,
pp. 325–338, Apr. 2019.

[28] A. I. Bandos, H. E. Rockette, T. Song, and D. Gur, ‘‘Area under the free-
response ROC curve (FROC) and a related summary index,’’ Biometrics,
vol. 65, no. 1, pp. 247–256, Mar. 2009.

[29] P. Agarwal, H.-C. Wang, and K. Srinivasan, ‘‘Epileptic seizure prediction
over eeg data using hybrid CNN-SVM model with edge computing ser-
vices,’’ in Proc. MATEC Web Conf., vol. 210, 2018, p. 03016.

[30] Y. Qian and P. C. Woodland, ‘‘Very deep convolutional neural networks
for robust speech recognition,’’ in Proc. IEEE Spoken Lang. Technol.
Workshop (SLT), Dec. 2016, pp. 481–488.

[31] Y. Zhan, M. I. Vai, S. Barma, S. H. Pun, J. W. Li, and P. U. Mak,
‘‘A computation resource friendly convolutional neural network engine
for EEG-based emotion recognition,’’ in Proc. IEEE Int. Conf. Com-
put. Intell. Virtual Environ. Meas. Syst. Appl. (CIVEMSA), Jun. 2019,
pp. 1–6.

82008

VOLUME 9, 2021

MENGQI HU was born in Shanghai, China,
in 1997. He received the B.S. degree in software
engineering from East China Normal University,
Shanghai, in 2020, where he is currently pursuing
the M.S. degree in software engineering. Since
2018, he has been engaged in research on brain
signal processing, data mining, and deep learning.

H. Yu, M. Hu: Epilepsy SEEG Data Classification

[32] X. Zhang, L. Yao, M. Dong, Z. Liu, Y. Zhang, and Y. Li, ‘‘Adversarial rep-
resentation learning for robust patient-independent epileptic seizure detec-
tion,’’ IEEE J. Biomed. Health Informat., vol. 24, no. 10, pp. 2852–2859,
Oct. 2020.

[33] S. Alhagry, A. Aly, and R. A. El-Khoribi, ‘‘Emotion recognition based
on EEG using LSTM recurrent neural network,’’ Int. J. Adv. Comput. Sci.
Appl., vol. 8, no. 10, pp. 355–358, 2017.

[34] G. Krishna, C. Tran, M. Carnahan, and A. H. Tewﬁk, ‘‘EEG based con-
tinuous speech recognition using transformers,’’ 2019, arXiv:2001.00501.
[Online]. Available: http://arxiv.org/abs/2001.00501

[35] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
‘‘Attention is all you need,’’ 2017,

L. Kaiser, and I. Polosukhin,
arXiv:1706.03762. [Online]. Available: http://arxiv.org/abs/1706.03762

HAO YU was born in Hubei, China, in 1997.
He received the B.S. degree in software engineer-
ing from the University of Shanghai for Science
and Technology, Shanghai, China, in 2018. He is
currently pursuing the master’s degree in software
engineering from East China Normal University.
Since 2018, he has been engaged in research on
brain signal processing and analysis, data mining,
and machine learning.

VOLUME 9, 2021

82009
