# Mohan et al. - 2017 - Deep power Deep learning architectures for power quality disturbances classification

2017  IEEE  International  Conference  on  Technological  Advancements  in  Power  and  Energy  (TAP Energy)

Deep Power: Deep Learning Architectures for
Power Quality Disturbances Classiﬁcation

Neethu Mohan, Soman K.P, Vinayakumar R
Centre for Computational Engineering & Networking,
Amrita University, Coimbatore, India.
neethumohan.ndkm@gmail.com, kp soman@amrita.edu

Abstract—The  transformation  of  the  conventional  electric 
power  grid  to  modern  smart  grid  are  subjected  to  power  system 
quality  and  reliability  problems.  In  order  to  ensure  reliable, 
secure and quality supply of power, it is important to characterize 
and  classify  the  power  quality  disturbances.  Power  quality  (PQ) 
disturbance  classiﬁcation s chemes i mplicitly r elies o n feature 
engineering  to  extract  unique  and  accurate  features  such  as 
statistical information, spatio-temporal characteristics, stationary 
and  non-stationary  behavior  of  PQ  signals.  This  paper  explores 
the  potentiality  of  deep  learning  algorithms  to  characterize  and 
classify  various  PQ  disturbances  in  smart  grid.  Deep  learning 
algorithms  have  the  inherent  capability  to  automatically  learn 
optimal  features  from  raw  input  data  and  thus  to  avoid  time-
consuming  feature  engineering.  To understand  the  effectiveness 
of  various  deep  learning  mechanisms,  different  architectures 
namely  convolution  neural  network  (CNN),  recurrent  neural 
network (RNN), identity-recurrent neural network (I-RNN), long 
short-term  memory  (LSTM),  gated  recurrent  units  (GRU)  and 
convolutional  neural  network-long  short-term  memory  (CNN-
LSTM)  are  studied  in  this  paper.  Several  experiments  are 
conducted to propose an optimal deep learning architecture with 
speciﬁc n etwork p arameters a nd t opologies. T he p erformance of 
the  proposed  deep  learning  architecture  is  evaluated  on  a  set 
of  synthetic  single  and  combined  PQ  disturbances  and  real-time 
PQ  events.  The  proposed  architecture  is  found  to  be  accurate 
for  real-time  characterization  and  classiﬁcation o f p ower quality 
disturbances  in  smart  grid.

Index Terms—Smart grid, distributed generation system, deep 
power, power  quality  disturbances,  deep  learning,  classiﬁcation.

I.  INTRODUCTION

Micro  grid  or  distributed  generation  (DG)  system  with
variable  renewable  energy  sources  and  energy  conservation
technologies  are  integrated  in  modern  electric  grid  to  satisfy
growing  power  demand.  Introduction  of  DG  systems  with
multiple and non-linear load characteristics have brought great
challenges to governing power quality [1], [2]. Increasing use
of  solid  switching  state  devices,  power  electronic  devices,
use  of  non-linear  loads  with  several  environmental  factors,
and  unbalanced  power  systems  cause  power  quality  (PQ)
disturbances.  Presence  of  power  quality  disturbances  such
as  voltage  sag,  voltage  swell,  harmonics,  inter-harmonics,

transients, interruption, ﬂicker, notch and their combinations
result in deterioration of electric power quality. These dis-
turbances cause malfunctioning of end-user equipments and
enormous economic loss. Identiﬁcation of PQ disturbances is
fundamental to develop a compensation device for improving
power quality. Conventional power analyzers fails to give
sufﬁcient knowledge on the disturbances [3]. The monitoring
system must be able to detect and characterize PQ disturbances
for reliable, secure and quality supply of power.

In literature, a signiﬁcant amount of effort has been devoted
to PQ disturbance analysis and classiﬁcation [3]–[14]. Time-
domain approaches, Fourier based techniques, Prony analy-
sis, optimization algorithms such as Newton’s method, least-
transform (DWT) [4],
square approaches, discrete wavelet
empirical mode decomposition (EMD) [5], empirical wavelet
transform [3], and variational mode decomposition (VMD)
[6], [7] are studied to characterize PQ disturbances. The
performance and accuracy of these methods greatly rely on
the extracted features. The extracted, hand crafted features
is fed as input to a shallow structured, pattern recognition
technique, including hidden Markov model (HMM) [8], mul-
tilayer perceptron (MLP) [9], artiﬁcial neural network (ANN)
[10], decision tree (DT) [11], logistic regression (LR) [12],
support vector machine (SVM) [13] and extreme learning
machine (ELM) [14]. It is inferred from literature that, ac-
curate detection of PQ disturbances is dependant on signal
processing techniques with predeﬁned ﬁlter speciﬁcations,
selection of unique and novel features, and an accurate pattern
recognition method or classiﬁer. Identiﬁcation and extraction
of hand crafted features require substantial effort. Even though
aforementioned methods are successful, feature learning phase
makes them time-consuming.

Recently, deep learning has become an emerging ﬁeld,
which have been impacted a wide range of tasks in artiﬁcial
intelligence (AI) related to the ﬁeld of signal, image and
information processing [15]. Deep learning algorithms have
multiple levels of representation and abstraction that help to
make sense of data such as signals, images, and text. They have

978-1-5386-4021-0/17/$31.00  c(cid:13)2017  IEEE

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 04,2025 at 12:31:14 UTC from IEEE Xplore.  Restrictions apply. 

the immense capability to automatically learn optimal features
from raw input data and thus to avoid feature engineering.
Availability of large scale computing power such as general-
purpose graphical processing units (GP-GPUs), signiﬁcantly
reduced hardware cost and the modern research advances in
machine learning and related ﬁeld have enabled the paradigm
shift to deep learning techniques from conventional AI tech-
niques [15], [16]. Through deep learning algorithms, ma-
chine can now surpass human interference in research areas
of signal/information processing, pattern recognition, natural
language processing, audio and video perception etc.

This paper explores the potentiality of deep learning archi-
tectures to characterize and classify various single and mixed
PQ disturbances in modern smart grid. The proposed deep
learning architecture automatically learns the best features
without additional feature extraction stage and thus reduces
the computation effort. Experiments are done with various
network parameters and conﬁgurations to select an optimal
architecture for PQ disturbance classiﬁcation.

II. MATERIALS AND METHODS

A. Power Quality (PQ) Disturbances

Power quality disturbances comprise of short and long
duration voltage variations and waveform distortions. Volt-
age sag, swell and interruption belong to short duration PQ
disturbances. Over voltage and under voltage conditions are
termed as long duration voltage variations. Waveform distor-
tions include steady state variations such as harmonics, inter
harmonics, spikes, notches and noises. PQ disturbance signals
have time-varying amplitudes. The performance of proposed
deep learning architecture is validated on synthetic and real-
time power quality disturbance signals.

B. Deep Learning Algorithms

Deep learning has become an important approach in arti-
ﬁcial intelligence, signal/information processing and machine
learning. Conventional machine learning tasks greatly depen-
dent on extracted features, which need signiﬁcant effort to
ﬁnd the most suitable features. Feature learning phase is task-
speciﬁc or task-dependent while deep learning methods are
data dependent. As the amount of data and range of application
in AI tasks continues to grow, it becomes unavoidable to
automatically learn features [17]. In deep learning techniques,
the initial data fed into the deep network are sufﬁcient to learn
features and to classify the instances. A general deep learning
architecture has several deep layers to obtain rich features of
input data. The output from each previous layer is passed
as input to successor layer, and learn multiple levels of data
abstraction. A simple deep learning network has an input layer,
multiple hidden layers followed by an output layer. Recently,
a PQ signal classiﬁcation scheme using CNN is proposed in
[18]. This paper has reported an accuracy of 97% for classiﬁca-
tion of six different PQ classes. In [19], a stacked autoencoder
framework for PQ disturbance classiﬁcation is proposed. In
this work, particle swarm optimization is employed to assist
the classiﬁcation. Indeed, the use of optimization approaches

results additional computational complexity. Classiﬁcation by
using the image ﬁles of PQ events are proposed in [20].

To understand and evaluate various deep learning algorithms
for PQ disturbance classiﬁcation, different architectures such
as convolution neural network (CNN) [21], sequential data
modeling algorithms namely recurrent neural network (RNN)
long
identity-recurrent neural network (I-RNN) [23],
[22],
short-term memory (LSTM) [24], gated recurrent units (GRU)
[25] and a hybrid architecture of CNN-LSTM are used in this
paper.

1) Convolutional Neural Network (CNN): CNN architec-
ture consists of a number of convolutional layers, subsampling
layers and fully connected layers. The ﬁlters in convolutional
layers produce an initial feature map of the input data. The
convolution is performed by sliding the ﬁlter over the input
data. Pooling layer or subsampling layer follows immediately
after convolutional layer helps to simplify the information
from convolutional layer. The feature map generated after
pooling operation is then given to a fully connected layer or
dense layer for classiﬁcation. In the dense layer, a sigmoid
non-linearity activation function is applied over the features
for predicting the output class labels [26].

2) Recurrent Neural Network (RNN): RNN are extensions
of feed-forward networks. In RNN, the output from one state is
taken back as an input/feedback to it through a loop structure.
RNN handles data in a sequential form and holds information
in the network as a short memory through feedback loop. Thus
in a given time instant, the hidden state holds information from
all its previous states. The feedback loop makes RNN as exten-
sions of feed-forward network which passes the information
only in one direction. The hidden states act as memory units in
the network, receives input from previous states and transfers
output to next state. The hidden state vector ht at a given
time t is dependent on the current input xt and previous state
output ht−1. That is,

ht = f (P xt + W ht−1)

(1)

where f represents the non-linear activation function like
sigmoid, tanh, ReLU (rectiﬁed linear units). The output state
vector yt at time t is calculated from the hidden states at time
t as,

yt = sof t max(Qht)

(2)

In RNN, the hidden states are initialized randomly or as zeros.
The main obstacle for RNN is the vanishing or exploding
gradient problem, where the gradient vector explodes or de-
cay over time steps. Hence, RNN fails to capture long-term
dependencies.

3) Identity-Recurrent Neural Network (I-RNN): I-RNN is
an extension to RNN architecture, where the initialization of
weight matrix differs from traditional RNN. The weight matrix
is initialized as identity matrix or its scaled versions. This
initialization trick helps to avoid addition of error-derivatives
during back propagation and thus enable long-term dependen-
cies. The non-linear activation function used is ReLU.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 04,2025 at 12:31:14 UTC from IEEE Xplore.  Restrictions apply. 

4) Long Short-Term Memory (LSTM): LSTM a variant of
RNN with a gating architecture, captures long-term temporal
dependencies and avoid vanishing/exploding gradient problem.
The LSTM blocks are known as memory cells with adaptive
multiplicative gates namely input, output and forget gates. The
input gate decides how much current information need to be
passed.

it = σ(P ixt + W iht−1)

(3)

The forget gate decides about the information need to be
passed from previous state and is deﬁned as,

ft = σ(P f xt + W f ht−1)

(4)

The output gate deﬁnes the internal state information need to
be passed.

ot = σ(P oxt + W oht−1)

(5)

The internal memory of the unit ct is updated using previous
memory ct−1 with forget gate and updated hidden state ˆh with
input gate.

ct = ct−1 ◦ ft + ˆh ◦ it

(6)

where ◦ denotes an element-wise multiplication operation, ˆh
is the candidate hidden state computed as,

ˆh = tanh(P hxt + W hht−1)

Now using the memory ct,
computed by multiplying with the output gate o

the output hidden state ht

ht = tanh(ct) ◦ ot

(7)

is

(8)

C. Proposed Architecture - Convolution Neural Network-Long
Short-Term Memory (CNN-LSTM)

In this paper, to improve the performance of PQ disturbance
classiﬁcation by learning additional features, a hybrid architec-
ture is proposed. Fig. 1 represents various stages involved in
the proposed hybrid architecture. The architecture contains an
initial layer of CNN followed by max pooling to extract low
level spatial dependencies among the data. To generate a more
abstracted feature map, the ﬁrst level extracted features are fed
into the second layer of CNN and max pooling layers. The ﬁrst
CNN layer has 64 ﬁlters with a ﬁlter length of 3 for convolving
with the input raw data. The second CNN layer contains
128 ﬁlters with the same ﬁlter length as in ﬁrst CNN layer.
The max pooling layer has used a standard size of 2, which
combines the features from previous layer. The consolidated
feature matrix generated from max pooling layer are then fed
to an LSTM layer containing memory blocks. The LSTM layer
extracts the long term temporal dependencies and generate a
more abstracted feature map. The LSTM layer used in the
proposed architecture has 50 memory blocks including several
gates and activation function. Finally, the output of LSTM
layer has passed to a fully connected layer or dense layer.
Generally, a normal ﬂat feed-forward neural network layer
acts as fully connected layer, which contains units corresponds
to the number of PQ classes. This layer has a non-linear
activation function namely softmax function to calculate the
probabilities of output class predictions. In this study, we have
used a batch size of 32 and the model was trained for 1000
epochs.

D. Hyper Parameter Tuning

In general, deep learning architectures are parameterized
models. Therefore the superior predictive performance of the

The long-term learning of
through the gating mechanism in LSTM [27], [28].

temporal

features is achieved

5) Gated Recurrent Units (GRU): Similar to LSTM, GRU
has gating units to pass information inside the unit. This
architecture have two types of gates namely reset gate and
update gate. The reset gate deﬁnes combination of the new
input with memory from previous state and update gate
deﬁnes how much information from previous state need to be
preserved. At time instant t, these gate vectors are calculated
as,

• Reset gate:

• Update gate:

rt = σ(P rxt + W rht−1)

ut = σ(P uxt + W uht−1)

(9)

(10)

The GRU architecture does not possess internal memory unit
ct and output gate o as in LSTM. In real-time learning, GRU
architecture has fewer tuning parameters than LSTM.

Fig. 1. Brief view of the stages involved in proposed hybrid (CNN-LSTM)
architecture for PQ disturbance classiﬁcation

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 04,2025 at 12:31:14 UTC from IEEE Xplore.  Restrictions apply. 

models are dependant on the selection of optimal parameters
and is achieved through hyper parameter tuning. Deep network
parameters such as learning rate and number of memory blocks
or number of ﬁlters have to be selected optimally to achieve
the highest performance. In order to ﬁx the hyper parameters
a moderately sized RNN/LSTM/GRU/I-RNN/CNN networks
which contains an input layer, hidden recurrent layer and an
output layer is used. This initial network has an input layer
with 1280 neurons, a single hidden recurrent layer/convolution
layer followed by max-pooling and an output layer contains
11 neurons. The experiments are performed epoch-wise and
we ran every experiment till 100 epochs. To ﬁnd the suitable
learning rate, we performed two trails of experiment for all
deep learning architectures in the range of [0.01-0.5]. The
highest performance is achieved at a learning rate of 0.01,
after that the performance gradually decreased. Hence, in this
study, the learning rate is ﬁxed at 0.01. The performance of
sequential data modeling algorithms such as RNN, I-RNN,
LSTM and GRU depends on the number of memory blocks
or hidden units. To ﬁx the optimal number of memory blocks,
two trails of experiments are done with hidden units/memory
blocks as 32, 64, 128, 256, 512, 1024 and 2048. The highest
performance is achieved with 1024 hidden units. Hence, the
number of hidden units is taken as 1024 in this study. For
CNN, the performance is relied on the number of ﬁlters and
ﬁlter length. We performed two trails of experiment with CNN
and max-pooling layer by varying the number of ﬁlters as 32,
64, 128 and ﬁlter length as 2, 3 and 6. The CNN model with
number of ﬁlters as 64, each ﬁlter having a length of 3 has
attained the highest accuracy and hence these values are ﬁxed
throughout in this study. After ﬁxing the network parameters,
experiments are conducted to select the most suitable network
architecture for all deep learning models. Experiments are
conducted with the following network topologies.

• RNN/LSTM/GRU/I-RNN - 1 layer with 1024 hidden

units/memory blocks

• RNN/LSTM/GRU/I-RNN - 5 layer with 1024 hidden

units/memory blocks

• RNN/LSTM/GRU/I-RNN - 10 layer with 1024 hidden

units/memory blocks

• CNN - 1 layer
• CNN - 2 layer
• CNN - 1 layer followed by LSTM with 50 memory blocks
• CNN - 2 layer followed by LSTM with 50 memory blocks

From the experiments, the best performance is obtained for
RNN/LSTM/GRU/I-RNN - 10 layer with 1024 units/memory
blocks, CNN with 2 layers and CNN - 2 layer followed by
LSTM with 50 memory blocks. For classifying the PQ signals,
these best performed network topologies with optimal network
parameters are used.

III. RESULTS AND DISCUSSION

The platform chosen for performing the evaluation is
Googles open source data ﬂow engine TensorFlow [29] in
conjunction with Keras [30]. To accelerate the performance

and computations, the experiments are realized using back-
propogation through time (BPTT) with adam optimizer [31]
on GPU enabled TensorFlow in single NVidia GK110BGL
Tesla k40. The evaluations are performed on real and synthetic
PQ disturbances, for six deep learning architectures namely
CNN, RNN, I-RNN, LSTM, GRU and hybrid model. In order
to prevent overﬁtting and to improve the training a dropout
parameter is used. The performance of the trained model of
each deep learning architecture is evaluated using the test
samples on epoch-wise. All the models have trained with a
loss of categorical cross-entropy and with the hyper parameters
explained in the previous section. The evaluations of the
model are analyzed using metrics such as precision, recall, F1-
measure and accuracy. The synthetic PQ disturbance signals

Fig. 2. Visualization of active values in ﬁnal hidden layer using t-SNE

including waveform distortions and voltage ﬂuctuations are
generated in MATLAB using parametric equations [32]. These
signals belong to 11 classes with single PQ disturbances such
as voltage sag, voltage swell, harmonics, interruption, ﬂicker,
transients and combined PQ disturbances namely sag with
harmonics, swell with harmonics, harmonics with interrup-
tions, ﬂicker with sag and ﬂicker with swell. The signals are
generated for 200 ms with a sampling rate of 6.4 kHz and
each class have 250 signals. 60% of the data is randomly
taken for training and the remaining 40% has given for testing.
The raw PQ signals are passed through more than one hidden
layers. The activation function in each hidden layer facilitates
to distinguish the signals into different categories. Features
learned in each layers are passed to next layer and ﬁnally
the activation values in the last layer is able to separate the
data into different classes. Each hidden layer includes high
dimensional activation values. These high dimensional data
are transformed to lower dimensional using t-SNE [33], as
shown in Fig. 2. It is clear from Fig. 2, the deep learning
model has learnt the features accurately and able to separate
the classes efﬁciently. The results obtained for synthetic PQ
signals are tabulated in Table I. The RNN model has attained
an accuracy of 0.915 with a loss of 0.48. The I-RNN model
accelerate the performance of conventional RNN and hence

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 04,2025 at 12:31:14 UTC from IEEE Xplore.  Restrictions apply. 

TABLE I
THE PERFORMANCE OF DEEP LEARNING ALGORITHMS FOR PQ CLASSIFICATIONS

CNN

RNN

I-RNN

LSTM

GRU

TPR
1.0
0.92
1
0.96
1

FPR
0.002
0.002
0
0.008
0.002

TPR
1
0.8
0.96
1
1

0.94

0.002

0.92

1

0

0.96

0.98

0.004

0.98

1

0

1

FPR
0
0.012
0.028
0.016
0.006

0

0

0.006

0.008

0.98

0.002

0.78

0.014

TPR
1
0.9
1
1
1

0.9

0.96

0.98

0.98

0.8

FPR
0
0.01
0.018
0.012
0.004

0.002

TPR
1
0.92
0.98
1
1

0.9

0

1

0.01

0.008

0.006

0.98

0.98

0.96

0.92

FPR
0.002
0.002
0.004
0.01
0

0

0

0.01

0.004

0.004

TPR
1
0.9
1
1
1

FPR
0
0.002
0.004
0.012
0.002

CNN-LSTM
FPR
TPR
1
1
0.006
0.96
0
1
0.004
0.98
0
1

0.92

0.002

0.92

0.98

0.96

0.98

0.96

0

0.008

0.006

1

1

1

0.004

0.96

1

0

0.008

0

0

0

1

0

0.66

0.004

0.78

0

0

0.9

0

1

0.98
0.18
0.98
0.98
0.98

0.915
0.48
0.919
0.915
0.912

0.936
0.42
0.94
0.936
0.935

0.967
0.30
0.969
0.967
0.967

0.964
0.34
0.965
0.964
0.964

0.984
0.15
0.984
0.984
0.984

Classes

Normal
Sag
Swell
Interruption
Harmonics
Sag+
Harmonics
Swell+
Harmonics
Interruption+
Harmonics
Flicker
Flicker+
Sag
Flicker+
Swell
Accuracy
Loss
Precision
Recall
F1-score

achieved an accuracy of 0.936. The recurrent LSTM and GRU
has a higher performance with an accuracy of 0.967 and 0.964
respectively. The CNN architecture has got an accuracy 0.98
with a loss of 0.18. Hence, to improve the accuracy, in the
proposed architecture, the features from CNN are given to a
recurrent LSTM layer and achieved the highest accuracy of
0.984. The loss in classiﬁcation is only 0.15.

The conventional PQ disturbance classiﬁcation methods are
time consuming mainly because of extraction of features.
While the deep learning models has avoided the feature ex-
traction stage and hence the processing time is comparatively
smaller than conventional machine learning techniques. Addi-
tionally, the accuracy obtained for deep learning models are
higher than conventional techniques. In [34], statistical feature
based PQ classiﬁcation scheme using support vector machine
(SVM) and random kitchen sink (RKS) is discussed. The
highest accuracy achieved for six PQ classes is only 94.44%
with RKS classiﬁer. On comparing with the results reported
in [34], proposed deep learning architecture has obtained an
accuracy of 98.4% with more PQ disturbances classes. This, in
turn, highlight the scalability of deep learning models. That is,
the deep learning models are efﬁcient to learn distinguishable
features across classes for accurate separation. In conventional
approaches, as the number of classes increases, more sophis-
ticated features are needed for efﬁcient classiﬁcation.

The real-time data samples taken from [35] containing
three PQ disturbances namely voltage sag, transients and non-
harmonic waveform distortions. A total of 1031 signals are
taken for evaluation, from which 30% data are randomly taken
for testing the model. The classiﬁcation of real-time power
quality events is performed using the hybrid architecture. The
results of evaluation are tabulated in Table II. The CNN-LSTM
architecture has achieved an accuracy of 0.919 with 0.47 loss.

TABLE II
THE PERFORMANCE OF CNN-LSTM HYBRID MODEL ON PQ SIGNALS
FROM [35]

Classes
Class 1
Class 2
Class 3
Accuracy
Loss
Precision
Recall
F1-score

TPR
0.686
0.983
0.950

FPR
0.007
0.047
0.931

0.919
0.47
0.920
0.919
0.916

The decreased performance of the algorithm is mainly due to
the deﬁciency of data events for training the model. From the
evaluation it is inferred that the performance of deep learning
algorithms is proportional to the volume of data. To achieve
a good separation between the PQ classes, a more abstracted,
and higher level feature map is required.

A. Conclusion

This paper investigates the effectiveness of various deep
learning architectures for PQ disturbances characterization and
classiﬁcation. The inherent mechanism of deep learning algo-
rithms to automatically extract the best and unique features
is utilized for the efﬁcient and accurate classiﬁcation. Deep
learning models have scalability among data and are computa-
tionally efﬁcient. To improve the performance of classiﬁcation
by learning additional features, this paper has proposed a
hybrid architecture combining CNN with LSTM. In this hybrid
architecture, initial two CNN layers are used for learning
spatial information followed by a recurrent LSTM layer to
learn the temporal characteristics. The features generated from
maxpooling layer of CNN are fed to LSTM layer, followed
by a dense layer with softmax activation function. The CNN-

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 04,2025 at 12:31:14 UTC from IEEE Xplore.  Restrictions apply. 

[15] L. Deng, D. Yu, et al., “Deep learning: methods and applications,” Foun-
dations and Trends R(cid:13) in Signal Processing, vol. 7, no. 3–4, pp. 197–387,
2014.

[16] L. Deng, “A tutorial survey of architectures, algorithms, and applications
for deep learning,” APSIPA Transactions on Signal and Information
Processing, vol. 3, 2014.

[17] Y. Bengio et al., “Learning deep architectures for ai,” Foundations and

trends R(cid:13) in Machine Learning, vol. 2, no. 1, pp. 1–127, 2009.

[18] A. S. Binsha P., Sachin Kumar S. and K. Soman, “Power quality signal
classiﬁcation using convolutional neural network,” IJCTA, International
Science Press, pp. 8033–8042, 2016.

[19] J. Ma, J. Zhang, L. Xiao, K. Chen, and J. Wu, “Classiﬁcation of power
quality disturbances via deep learning,” IETE Technical Review, vol. 34,
no. 4, pp. 408–415, 2017.

[20] E. Balouji and O. Salor, “Classiﬁcation of power quality events using
deep learning on event images,” in Pattern Recognition and Image
Analysis (IPRIA), 2017 3rd International Conference on, pp. 216–221,
IEEE, 2017.

[21] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classiﬁcation
with deep convolutional neural networks,” in Advances in neural infor-
mation processing systems, pp. 1097–1105, 2012.

[22] Y. Gal and Z. Ghahramani, “A theoretically grounded application of
dropout in recurrent neural networks,” in Advances in neural information
processing systems, pp. 1019–1027, 2016.

[23] Q. V. Le, N. Jaitly, and G. E. Hinton, “A simple way to initialize recur-
rent networks of rectiﬁed linear units,” arXiv preprint arXiv:1504.00941,
2015.

[24] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural

computation, vol. 9, no. 8, pp. 1735–1780, 1997.

[25] J. Chung, C. Gulcehre, K. Cho, and Y. Bengio, “Empirical evaluation of
gated recurrent neural networks on sequence modeling,” arXiv preprint
arXiv:1412.3555, 2014.

[26] V. R, K. Soman, and S. Kumar, “Evaluating deep learning approaches
to characterize and classify the dgas at scale,” Journal of Intelligent and
Fuzzy Systems (JIFS), IOS Press, in Press.

[27] S. S. Kumar, M. A. Kumar, and K. Soman, “Sentiment analysis of tweets
in malayalam using long short-term memory units and convolutional
neural nets,” in International Conference on Mining Intelligence and
Knowledge Exploration (MIKE 2017), Springer LNAI Series, in Press.
[28] V. R, P. Poornachandran, and K. Soman, Scalable Framework for Cyber
Threat Situational Awareness based on Domain Name Systems Data
Analysis. Big data in Engineering Applications (Springer), in Press.
[29] M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, M. Devin,
S. Ghemawat, G. Irving, M. Isard, et al., “Tensorﬂow: A system for
large-scale machine learning.,” in OSDI, vol. 16, pp. 265–283, 2016.

[30] F. Chollet, “Keras.” https://github.com/fchollet/keras, accessed 2017-10-

08.

[31] P. J. Werbos, “Backpropagation through time: what it does and how to
do it,” Proceedings of the IEEE, vol. 78, no. 10, pp. 1550–1560, 1990.
[32] S. Khokhar, A. A. M. Zin, A. P. Memon, and A. S. Mokhtar, “A new
optimal feature selection algorithm for classiﬁcation of power quality
disturbances using discrete wavelet transform and probabilistic neural
network,” Measurement, vol. 95, pp. 246–259, 2017.

[33] L. v. d. Maaten and G. Hinton, “Visualizing data using t-sne,” Journal
of Machine Learning Research, vol. 9, no. Nov, pp. 2579–2605, 2008.
[34] C. Aneesh, P. Hisham, S. Kumar, P. Maya, and K. Soman, “Variance
based ofﬂine power disturbance signal classiﬁcation using support vector
machine and random kitchen sink,” Procedia Technology, vol. 21,
pp. 163–170, 2015.

[35] “Power Quality Events Data Collection,Instituto de Telecomunicaes.”

http://www.gim.lx.it.pt/fct57708/data/, accessed 2017-7-25.

LSTM hybrid architecture has obtained an accuracy of 0.984
on synthetic and 0.919 on real PQ signals. In addition, the per-
formance of various deep learning architectures namely CNN,
RNN, I-RNN, LSTM and GRU are studied. The efﬁciency of
each algorithm is tested on synthetically generated and real-
time PQ disturbance signals. This study serves as a bottom
level system to understand the effectiveness of various deep
learning approaches for PQ classiﬁcation. Development of an
intelligent deep learning PQ disturbance classiﬁcation system
by including more PQ disturbance classes is devised as a future
scope of this work.

REFERENCES

[1] L. An, X. Qianming, M. Fujun, and C. Yandong, “Overview of power
quality analysis and control technology for the smart grid,” Journal of
Modern Power Systems and Clean Energy, vol. 4, no. 1, pp. 1–9, 2016.
[2] S. R. Mohanty, N. Kishor, P. K. Ray, and J. P. Catalo, “Comparative
study of advanced signal processing techniques for islanding detection
in a hybrid distributed generation system,” IEEE Transactions on sus-
tainable Energy, vol. 6, no. 1, pp. 122–131, 2015.

[3] K. Thirumala, A. C. Umarikar, and T. Jain, “A generalized empirical
wavelet
transform for classiﬁcation of power quality disturbances,”
in Power System Technology (POWERCON), 2016 IEEE International
Conference on, pp. 1–5, IEEE, 2016.

[4] M. Uyar, S. Yildirim, and M. T. Gencoglu, “An effective wavelet-based
feature extraction method for classiﬁcation of power quality disturbance
signals,” Electric Power Systems Research, vol. 78, no. 10, pp. 1747–
1755, 2008.

[5] S. Shukla, S. Mishra, and B. Singh, “Empirical-mode decomposition
with hilbert transform for power-quality assessment,” IEEE transactions
on power delivery, vol. 24, no. 4, pp. 2159–2165, 2009.

[6] S. Samantaray, P. Achlerkar, and M. Manikandan, “Variational mode
decomposition and decision tree based detection and classiﬁcation of
power quality disturbances in grid-connected distributed generation
system,” IEEE Trans. Smart Grid, 2016.

[7] C. Aneesh, S. Kumar, P. Hisham, and K. Soman, “Performance compari-
son of variational mode decomposition over empirical wavelet transform
for the classiﬁcation of power quality disturbances using support vector
machine,” Procedia Computer Science, vol. 46, pp. 372–380, 2015.
[8] H. Dehghani, B. Vahidi, R. Naghizadeh, and S. H. Hosseinian, “Power
quality disturbance classiﬁcation using a statistical and wavelet-based
hidden markov model with dempster–shafer algorithm,” International
Journal of Electrical Power & Energy Systems, vol. 47, pp. 368–377,
2013.

[9] M. Uyar, S. Yildirim, and M. T. Gencoglu, “An effective wavelet-based
feature extraction method for classiﬁcation of power quality disturbance
signals,” Electric Power Systems Research, vol. 78, no. 10, pp. 1747–
1755, 2008.

[10] B. Perunicic, M. Mallini, Z. Wang, and Y. Liu, “Power quality distur-
bance detection and classiﬁcation using wavelets and artiﬁcial neural
networks,” in Harmonics and Quality of Power Proceedings, 1998.
Proceedings. 8th International Conference On, vol. 1, pp. 77–82, IEEE,
1998.

[11] P. K. Ray, S. R. Mohanty, N. Kishor, and J. P. Catalao, “Optimal feature
and decision tree-based classiﬁcation of power quality disturbances
in distributed generation systems,” IEEE Transactions on Sustainable
Energy, vol. 5, no. 1, pp. 200–208, 2014.

[12] L. Xu and M.-Y. Chow, “A classiﬁcation approach for power distribu-
tion systems fault cause identiﬁcation,” IEEE Transactions on Power
Systems, vol. 21, no. 1, pp. 53–60, 2006.

[13] D. Granados-Lieberman, R. Romero-Troncoso, R. Osornio-Rios,
A. Garcia-Perez, and E. Cabal-Yepez, “Techniques and methodologies
for power quality analysis and disturbances classiﬁcation in power
systems: a review,” IET Generation, Transmission & Distribution, vol. 5,
no. 4, pp. 519–529, 2011.

[14] H. Eris¸ti, ¨O. Yıldırım, B. Eris¸ti, and Y. Demir, “Automatic recognition
system of underlying causes of power quality disturbances based on
s-transform and extreme learning machine,” International Journal of
Electrical Power & Energy Systems, vol. 61, pp. 553–562, 2014.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 04,2025 at 12:31:14 UTC from IEEE Xplore.  Restrictions apply.
