# Wu et al. - 2023 - Software-Hardware Co-Design for Energy-Efficient Continuous Health Monitoring via Task-Aware Compres 1

180

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 17, NO. 2, APRIL 2023

Software-Hardware Co-Design for Energy-Efﬁcient
Continuous Health Monitoring via
Task-Aware Compression

Di Wu , Shiqi Zhao , Student Member, IEEE, Jie Yang , Member, IEEE, and Mohamad Sawan , Fellow, IEEE

Abstract—Low power consumption associated with data trans-
mission and processing of wearable/implantable devices is crucial
to ensure the usability of continuous health monitoring systems.
In this paper, we propose a novel health monitoring framework
where the signal acquired is compressed in a task-aware manner
to preserve task-relevant information at the sensor end with a
low computation cost. The resulting compressed signals can be
transmitted with signiﬁcantly lower bandwidth, analyzed directly
without a dedicated reconstruction process, or reconstructed with
high ﬁdelity. Also, we propose a dedicated hardware architecture
with sparse Booth encoding multiplication and the 1-D convolution
pipeline for the task-aware compression and the analysis modules,
respectively. Extensive experiments show that the proposed frame-
work is accurate, with a seizure prediction accuracy of 89.70 %
under a signal compression ratio of 1/16. The hardware architec-
ture is implemented on an Alveo U250 FPGA board, achieving a
power of 0.207 W at a clock frequency of 100 MHz.

Index Terms—Continuous health monitoring, energy-efﬁcient,

signal compression, on-device processing, deep neural networks.

I. INTRODUCTION

E ARLY detection and prediction of diseases are critical to

improving patient survival rate, however regular scheduled
screening tests from hospital visits provide only a snapshot of the
patient’s health condition and fail to reveal instant information
in a timely manner [1], [2]. For instance, the prediction of acute
myocardial infarction [3] and epileptic seizure [4] could not be
realized by counting on the result of the next scheduled screening
test. Precision health, which aims to prevent diseases by early
detection and follow-up treatment, relies on dynamic measure-
ment of health parameters from health monitoring systems that

Manuscript received 14 October 2022; revised 8 December 2022; accepted 12
January 2023. Date of publication 23 January 2023; date of current version 19
May 2023. This work was supported in part by Zhejiang Key R&D Program
under Project 2021C03002 and in part by the Zhejiang Leading Innovative
and Entrepreneur Team Introduction under Grant 2020R01005. This paper was
recommended by Associate Editor M. Kiani. (Di Wu and Shiqi Zhao contributed
equally to this work.)

The authors are with the Center of Excellence in Biomedical Re-
search on Advanced Integrated-on-chips Neurotechnologies (CenBRAIN
Neurotech), School of Engineering, Westlake University, Hangzhou
310024, China, and also with the Institute of Advanced Technology,
Westlake Institute for Advanced Study, Hangzhou 310024, China (e-mail:
wudi@westlake.edu.cn;
yangjie@westlake.
edu.cn; sawan@westlake.edu.cn).

zhaoshiqi@westlake.edu.cn;

Color versions of one or more ﬁgures in this article are available at

https://doi.org/10.1109/TBCAS.2023.3238719.

Digital Object Identiﬁer 10.1109/TBCAS.2023.3238719

Fig. 1. Examples of popular health monitoring devices and corresponding
applications.

are embedded into everyday life. Wearable and implantable
devices are thus gaining more popularity among consumers.
As seen from Fig. 1, a large variety of physiological signals
such as blood pressure, heart rate, electrocardiogram (ECG),
and electroencephalogram (EEG) are collected, transmitted or
processed via daily wearable or implantable devices.

The advancement of deep neural network (DNN) based
methodologies, which are capable of extracting discriminative
features made possible accurate and complex physiological
signal analysis in real-time, outperforming conventional ap-
proaches [4], [5], [6], [7]. However, power consumption in-
duced by computation and transmission remains an enormous
challenge for real-time health monitoring systems due to the
miniature and battery constraints of monitoring devices [7]. In
addition, the signal precision and transmission rate are limited
by the transmission bandwidth. In-sensor signal compression [8]
is a potential solution to reduce bandwidth requirements and re-
sulting power consumption in the condition that the compression
process can be implemented with low power and hardware cost.
However, conventional compression algorithms such as least
absolute shrinkage and selection operator (LASSO) [9], least

1932-4545 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 19,2025 at 14:04:35 UTC from IEEE Xplore.  Restrictions apply. 

WU et al.: SOFTWARE-HARDWARE CO-DESIGN FOR ENERGY-EFFICIENT CONTINUOUS HEALTH MONITORING

181

angle regression (LARS) [10], and Sparse Bayesian Learning
algorithms [11] rely on heavy computation and are hard to
implement in resource-constrained devices.

Compressive sensing (CS) provides a relatively new technique
that enables signal sampling and compression simultaneously at
a sub-Nyquist sampling rate. The compression procedure could
be deﬁned as a matrix multiplication between a sensing matrix
and the signal, which is hardware-friendly and computationally
lightweight [12]. The research of CS resolves around two points:
1) How to design the sensing matrix for informative and efﬁcient
signal compression and 2) How to develop a reconstruction
algorithm that best recovers the original signal from the cor-
responding measurements [13]. Current research endeavors are
mainly focused on signal reconstruction neglecting the relation-
ship between signal compression and downstream monitoring
tasks. More importantly, existing CS approaches [14], [15] take
the compression and reconstruction as two separate processes
and compress signals in a task-agnostic fashion failing to capture
informative features for various real-time health monitoring
tasks. Consequently, compressed signals (randomized CS mea-
surements) cannot be directly used for monitoring tasks analysis,
and thus a complex reconstruction process is required before
applying analysis to the signals. This, in turn, binds existing
frameworks to a ﬁxed paradigm where signals are compressed
at the sensor end only and then transmitted to the cloud and
reconstructed for further analysis.

To mitigate the aforementioned discussed limitations and to
provide reliable and energy-efﬁcient continuous health monitor-
ing systems, this work presents a novel end-to-end framework
for joint signal compressing, analysis, and reconstruction. Com-
pared to traditional CS approaches, the compression technique
proposed in our CHM monitoring framework is parametric and
is directly applicable to unseen data without the need to solve
an optimization problem on the new data. The sensing matrix
learned by our proposed framework captures health monitoring
task-relevant features and is optimal for both signal analysis
and signal reconstruction for potential expert visualization and
record keeping. The learned sensing matrix could be deployed
on wearable or implantable devices as a generic plug-and-play
solution to compress and transmit signals in a power-efﬁcient
manner. Moreover, the proposed framework is ﬂexible where
the monitoring task related analysis could act directly on the
compressed signal on the end monitoring devices where trans-
mission is unavailable.

(cid:2)

We summarize the main contributions of this paper as follows:
(cid:2)
A novel deep learning based energy-efﬁcient CHM frame-
work which jointly solves signal compression, analysis,
and reconstruction in a end-to-end manner.
A task-aware compression module which reduces trans-
mission and analysis energy consumption and enables task
analysis directly on the compressed signal; A monitor-
ing task analysis module that extracts features at various
granularity levels; A reconstruction network with adaptive
architecture based on different signal compression ratios.
A FPGA implementation with sparse Booth encoding mul-
tiplication to perform efﬁcient matrix multiplication and
the 1-D convolution pipeline to maximize data reuse.

(cid:2)

(cid:2)

We demonstrate the effectiveness of the proposed frame-
work and the FPGA implementation results on the moni-
toring task of seizure prediction on a popular open-source
dataset. Results show that the proposed framework outper-
forms state-of-the-art approaches under various compres-
sion ratios.

The remaining sections of this paper are organized as follows.
In Section II, we ﬁrst introduce previous research endeavors
from compressive sensing and continuous health monitoring
areas. We deﬁne and formalize our proposed framework in
Section III. Section IV provides a dedicated hardware design.
The effectiveness of our proposed framework is evaluated and
validated in Section V. Lastly, the paper is concluded in Sec-
tion VI.

II. RELATED WORK

A. Continuous Health Monitoring

Rapid advancement advancement in low-power biomedical
electronics and machine learning algorithms are revolution-
izing the healthcare industry [16], [17]. Early detection and
prevention of disease are considered promising solutions to
promoting wellness. In particular, Continuous Health Monitor-
ing (CHM), where wearable or implantable devices are utilized
to capture, analyze or transmit various physiological signals,
is envisioned as essential for proactive healthcare. Traditional
health monitoring systems such as Holter [18] are only used
for the long-term ECG recording [18] with signal processing
and analysis performed ofﬂine. In recent years, researchers are
stepping up the efforts to develop systems with real-time signal
processing and analysis capabilities [19], [20]. Accelerometers
are commonly used for physical activity detection associated
ﬁtness tracking [21]. Other vital signs such as oxygen saturation
and blood glucose present a basic health condition portray of the
user. ECG chest bands and EEG headsets enable some advance
functionalities such as sudden heart failure prediction [22],
seizure prediction [4] and emotion recognition [23].

However, the computation, storage, and transmission require-
ments for long-term CHM exceed the capabilities of existing
devices. Power consumption for CHM systems can be roughly
divided into signal acquisition, signal transmission, and signal
analysis, where wireless signal transmission usually consumes
the majority of the energy [24]. Battery recharging and re-
placement frequency are core factors for the usability of CHM
systems. Consequently, performing on-sensor computation for
signal processing and analysis without transmission or com-
pressing the signal before transmitting could help reduce energy
and storage consumption.

To this end, we propose a novel CHM framework that ap-
plies task-aware on-sensor signal compression, enabling energy-
efﬁcient signal transmission and analysis.

B. Compressive Sensing

Compressive Sensing (CS) is considered a breakthrough for
signal compression following the famous Shanon sampling the-
orem. In CS, we desire to acquire a signal x ∈ Rn with only

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 19,2025 at 14:04:35 UTC from IEEE Xplore.  Restrictions apply. 

182

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 17, NO. 2, APRIL 2023

m measurements where m (cid:3) n. To ensure unique recovery, CS
assumes that the underlying signal is approximately l-sparse in
some certain basis, meaning that the l largest entries dominate
others. The sparsity assumption holds naturally in many domains
such as video processing [25], face recognition [26], [27], mag-
netic resonance imaging (MRI) acquisition [28], etc. In contrast
to conventional sensing, CS adopts sensing matrices that are
based on random functions rather than Dirac delta functions.
Based on the available literature, the sensing matrix P hi can be
either Bernoulli [29] or Gaussian [30]. The CS acquisition of
CS can be mathematically expressed as:

z = Φx.

(1)

However, adopting random functions as sensing matrix fails to
capture task-speciﬁc features from the original signal leading
to deteriorated performance of downstream monitoring tasks
analysis.

The CS reconstruction process from limited measurements is
to solve the optimization task of an ill-posed inverse problem,
which can be formulated as:

arg min
x
where R(·) is a regularization prior term.

(cid:4)Φx − z(cid:4)2 + R(x),

(2)

Various algorithms have been developed to solve the under-
determined optimization problem for signal reconstruction. The
Greedy algorithm [31] minimizes the least square error in each
iteration to reconstruct the original signal in an iterative fashion.
Matching pursuit [32] and orthogonal matching pursuits [33]
are two popular algorithms due to their fast recovery speed.
However, they are computationally costly when the signal is
less sparse. Since the reconstruction objective is NP-hard, thus
it is common to consider a convex relaxation via linear program-
ming. Least angle regression (LARS), least absolute shrinkage
and selection operator (LASSO), and basis pursuit (BP) [34] are
some representative works.

To address the drawbacks of traditional CS methods, we
propose to construct the sensing matrix, which captures task-
relevant information during compression so that the compressed
signal can be directly used for analysis and reconstruction.

III. PROPOSED CHM FRAMEWORK

We formalize and propose an end-to-end CHM framework.
The principal objective of the proposed framework is to capture
task-aware information from the original physiological signals
and embed prior knowledge of the associated task into the
sampled measurement during the signal compression process.
The sampled measurement is then directly applicable to various
monitoring tasks to reduce power consumption with minimum
degradation in analysis performance for efﬁcient real-time con-
tinuous health monitoring systems. Besides signal analysis,
the proposed framework reconstructs the original signals from
sampled measurements for subject case recording for further
studying or expert visualization.

The proposed framework contains three modules, namely, a
compression module C(·), a reconstruction module R(·) and an
analysis module A(·). Let x ∈ RN ×C be physiological signals

of sequence length N and channel C, and y be its correspond-
ing desired monitoring task-related output. A training phase is
required to train all three modules for a speciﬁc monitoring task
before the deployment phase. As illustrated in Fig. 2, during
the training phase, the input signal x is ﬁrst compressed by the
compression module as follows:

z = C(x),

(3)

where z ∈ RM ×C represents the sampled measurement. The
signal compression ratio r is then naturally deﬁned as M
N with
M < N . The compressed signal z is then passed to the recon-
struction module, and the analysis module to give the recon-
structed signal ˆx and the analysis result ˆy, respectively. During
the actual deployment, the proposed framework also supports
multiple deployment strategies based on different monitoring
tasks and hardware requirements. One potential deployment
setting could be that the compression module and the analysis
module are deployed on the sensor. When a possible critical con-
dition is detected, the sensor raises an alarm and then transmits
the compressed signal to a cloud server for reconstruction and
further analysis by experts with the assumption that transmis-
sion is more power-consuming than signal analysis. Another
setting is that only the compression module is deployed on
the sensor for signal compression purposes. The analysis and
reconstruction modules are deployed on the cloud based on
the compressed signal received to reduce power consumption
further.

We implement all three modules with deep learning based
neural networks. It is worth noticing that we aim to propose
a generic framework and hence the structure of the neural
networks can be of arbitrary designs. In this work, we provide
a realization of these modules mainly with convolution-based
networks. Next, we describe the architectures of the NNs in
detail.

A. Compression Module

Conventional CS approaches adopt random Bernoulli or
Gaussian matrices, while existing deep learning based CS meth-
ods mainly adopt a cascade of a few convolution layers as for
signal compression. Huang et al. [35] adopted convolution layers
with large stride without pooling layers stating that pooling
operation in the compression stage causes severe information
loss. Since the purpose of signal compression is to reduce the
computation and transmission cost on wearable or implantable
devices for continuous health monitoring systems, the com-
pression process itself should be energey-efﬁcient. Therefore,
we choose trainable matrix W ∈ RN ×M as the compression
network. Then signal xc is compressed to the sampled mea-
surement yc by applying matrix multiplication between the
raw signal and the compression matrix, yc = W cxc. The com-
pression matrix for each channel might vary if the underlying
modalities are different across channels or the signals from
each channel have a signiﬁcant difference. Else, if the signal
from different channels are expected to be similar and could
be compressed to acquire the same features, the compressed

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 19,2025 at 14:04:35 UTC from IEEE Xplore.  Restrictions apply. 

WU et al.: SOFTWARE-HARDWARE CO-DESIGN FOR ENERGY-EFFICIENT CONTINUOUS HEALTH MONITORING

183

Fig. 2. A conceptual illustration of the training process of the proposed CHM framework. Physiological signals of various modalities are collected by wearable
or implantable sensors and compressed via the compression module. The sampled measurements are then utilized for monitoring task analysis and signal
reconstruction by the analysis module and reconstruction module, respectively. The compression matrix, analysis network and the reconstruction network are
optimized simultaneously during training.

matrix could then be shared across channels to reduce memory
consumption.

B. Analysis Module

Physiological signals contain essential information about
human condition and behavioral activities and states and are
the primary signal source for continuous health monitoring
systems. To capture features of various granularity levels, the
model implicitly extracts patterns of different frequencies. For
instance, the alpha band of EEG signals is highly associated
with eye closing and relaxation. Consequently, patterns of such
frequency bands would be helpful for the sleep monitoring
system. Inspired by the famous ResNet [36], we propose a
strong baseline based on CNN with residual connections. 2-D
convolution is the commonly adopted operation of most exist-
ing CNN-based approaches for physiological signal analysis.
In other words, physiological signals from different channels
are seen as images where the temporal dimension and channel
dimension are considered as the height and width of an im-
age. However, 2-D convolution has been widely used in the
computer vision community due to the assumption that image
pixels of a local region have high semantic correspondence
and that convolution echoes this with different receptive ﬁeld
sizes. However, the aforementioned assumption does not hold
for multichannel physiological signals. Signals from different
channels might be collected from the same modality but from
different electrodes or even from different modalities since the
ordering of the channels, and the placement of electrodes are
random such that adjacent channels are not guaranteed to be
more functionally correlated than non-adjacent channels. 2-D
convolution is therefore a poor choice due to its failure to obtain
informative correlation among channels. In this work, we adopt
1-D convolution in lieu of 2-D convolution to maximally make
use of the interactions among different channels by setting the
kernel shape along the channel dimension to be the same as
the input signal or intermediate features. Intuitively speaking,
1-D convolution takes information from all channels as input

Fig. 3. Network architecture of the analysis module. The sampled measure-
ments are ﬁrst fed into the stem layer, which consists of a 1-D convolution layer
and a max-pooling layer. The output intermediate features are further processed
through 1-D convolution blocks. Each 1-D convolution block is composed of
convolution, batch normalization, and activation operations. The dotted red line
represents the residual connection. We use global average pooling and fully
connected layers to aggregate information and generate task-speciﬁc analysis
results.

and selects different channel correlation patterns with different
kernels via network trainable parameters.

Next, we describe the proposed analysis architecture in de-
tail. As shown in Fig. 3, the input raw signals are ﬁrst fed
to a stem layer consisting of a 1-D convolution layer and a
max-pooling layer. The kernel size and the stride size of the
convolution layer within the stem layer are set to relatively
larger to reduce the computational complexity of the following

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 19,2025 at 14:04:35 UTC from IEEE Xplore.  Restrictions apply. 

184

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 17, NO. 2, APRIL 2023

layers. The output from the stem layer is passed to a cascade of
1-D convolution blocks. Each 1-D convolution block contains
1-D convolution layers, with each followed by an activation
layer. A batch normalization layer is further placed in between
to avoid covariate shift and to ensure faster convergence. For
the activation function, we choose the Rectiﬁed Linear Unit
(ReLu). Deﬁne convl,k to be the 1-D convolution layer of the
lth convolution block, we obtain the corresponding intermediate
feature map:

fl,k = δ(BN (convl,k(fl,k−1))),

(4)

where fl,k denotes the intermediate feature map, δ and BN
represents the ReLu activation and batch normalization, recep-
tively. We set k = 2 and l = 4 in this work. The output fl of
each convolution block is deﬁned via residual connection:

fl = fl,0 + BottleNeck (fl,2),

(5)

where the BottleNeck operation reduces the channels of fl,2 to
be compatible with the number of channels of fl,0.

The analysis result ˆy is then provided as:

ˆy = σ(F C2(δ(F C1(GAP (f4))))),

(6)

where GAP stands for global average pooling and F Ci stands
for the ith fully connected layer. δ is the LeakyReLu function
and σ is the Softmax function.

Finally, we deﬁne the loss function for the analysis task:

Lanalysis = L(ˆy, y).

(7)

Ltask denotes the objective function used to access the perfor-
mance of the monitoring analysis task.

C. Reconstruction Module

In addition to monitoring analysis tasks, we also investigate
signal reconstruction for additional conceivable applications
which require the reconstruction of the original signal based on
the sampled measurement. For instance, a clinician might rely
on visualization of the original signal for diagnosis, or other
analysis tasks could be performed based on computation of the
original signal. Furthermore, we regard the task of the signal re-
construction as a regularizer to alleviate the overﬁtting problem
of DL models due to limited dataset size. The reconstruction
network is designed in an adaptive manner with ﬂexible archi-
tecture composed of different numbers of up-sampling modules
under various compression ratios to reduce reconstruction cost,
as shown in Fig. 4. The up-sampling module is deﬁned as:

ˆfl = δ(BN (convl(Up( ˆfl−1)))).
(8)
Up-sampling module l takes input feature vector ˆfl−1 as the
input and outputs the intermediate reconstructed feature vector
ˆfl where Up denotes linear interpolation. δ, BN and convl
denotes activation function, batch normalization layer and con-
volution layer respectively. Based on different lengths L of the
original signal and a compression ratio r, a total number of
r(cid:6) + 1 up-sampling modules are used in the reconstruction
(cid:5)log 1
network. Each module doubles the input signal length, except
that the last module maps the input signal to its original length.

2

Fig. 4. Network architecture of the reconstruction module for signal com-
pression ratio r. The reconstruction module is composed of (cid:5)log 1
r(cid:6) + 1 up-
2
sampling modules in total. Each up-sampling module upsamples the input signal
to twice the input signal length, with the exception that the last up-sampling
module is used to map the length of the output signal to the original signal
length. A BottleNeck operation is then adopted to map the number of channels
of the reconstructed signal to that of the original signal.

To restore the signal to the original number of channels, we
perform a BottleNeck operation on the signal output of the last
up-sampling module. The reconstruction objective function is
then deﬁned as:

Lrecon = L(ˆx, x).

(9)

Mean squared error loss is chosen as the objective function
Lrecon to access the quality of the reconstructed signal ˆx.

D. Joint-Objective Optimization

We simultaneously solve the task of compression, analysis,
and reconstruction by optimizing the following joint objective:

Ljoint = Ltask + λ ∗ Lrecon,

(10)

where λ is a scalar to balance the two objective functions. The
sensing matrix is implicitly optimized during the joint-objective
optimization process since both the analysis module and the re-
construction module take the output of the compression module
as the input. The objectives of Ltask and Lrecon therefore en-
sures that the weights of the sensing matrix is optimized for both
analysis and reconstruction via backpropagation. Consequently,
the compressed signal is embedded with the prior knowledge of
both the reconstruction and monitoring analysis tasks.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 19,2025 at 14:04:35 UTC from IEEE Xplore.  Restrictions apply. 

WU et al.: SOFTWARE-HARDWARE CO-DESIGN FOR ENERGY-EFFICIENT CONTINUOUS HEALTH MONITORING

185

Fig. 5. Architecture of the proposed processor and the detailed architecture of the SMMU. BN: batch normalization module. ReLU: ReLU activation function
module. Pooling: max pooling module. Adder: 24-bits adder.

IV. HARDWARE IMPLEMENTATION

With the deep learning-based compression sensing frame-
work discussed in the previous session, we propose a dedicated
hardware architecture to efﬁciently support the compression
and analysis modules. We also verify the overall framework
with FPGA implementation. The main goal of this hardware
is to perform matrix multiplication and convolution operations
used in compression and analysis modules, respectively. The
proposed hardware utilizes Booth encoding multiplication with
sparsity exploitation to perform efﬁcient matrix multiplication
and takes advantage of the proposed dedicated 1-D convolu-
tion pipeline to maximize data reuse for power reduction. The
overall hardware architecture, detailed architecture of sparse
matrix multiplication unit (SMMU), and workload mapping for
different modules will be presented in this section.

A. Overall Hardware Architecture

The overall architecture of our proposed hardware is shown
in Fig. 5. The data ﬂow from memory to the analysis element
(AE) via the memory interface, and the operations of the AE are
controlled by the controller. Weight memory stores the weights,
and I/O memory stores intermediate results and data just before
or after external memory access. The memory interface is the
bridge between the AE and memory, providing ﬂexible memory
reorder modes. The AE consists of 128 SMMUs and connects
with the top controller for parameter conﬁguration and interacts
with the memory interface for memory access. Each SMMU
can either work independently or connect with neighboring
SMMUs to extend the accumulation pipeline. By changing the
control signals, the accumulation pipeline can be adapted to the
requirements of different matrix multiplications or convolution
kernels.

B. Detailed Architecture of SMMU

The SMMU performs energy-efﬁcient 8-bit matrix multipli-
cation operations in compression and analysis modules using

the Booth encoding algorithm with sparsity exploitation. Fig. 5
depicts the Booth encoding multiplication used in 8-bits com-
putations, which divides one 8-bit multiplier into four segments,
and each segment is encoded by Booth encoding to obtain the
corresponding value of the multiplicands. Then, one multipli-
cation operation is replaced by several add operations and shift
operations. Booth encoding logic encodes the multiplicand num-
bers by the four Booth multiplier numbers. The four encoded
Booth multiplicand numbers are sent to 4 SMMUs, respectively.
The multiplied numbers in each of the 4 SMMUs are shifted left
the speciﬁed number of bits and then added with the partial
results from the last SMMU. The multiplication results are
accumulated together with the previously obtained results from
the last four SMMUs.

There is native sparsity in matrix multiplication that a hard-
ware can exploit. The sparsity rate is further enlarged when
Booth multiplication is involved. This is due to the fact that
ﬁne-grained 3-bits encoding is utilized for encoding multipli-
cand numbers. In this work, we design the circuit for Booth-level
sparsity exploitation. When each SMMU receives the encoded
Booth multiplicand number, it ﬁrst determines whether the
number is zero. If the number is not zero, the 24-bit adder of
the current SMMU will perform the addition operation, and
the register will store the addition results. The addition result
in the register that is calculated in the previous cycle will be
passed to the next SMMU. If the receiving multiplicand number
is zero, the adder of the current SMMU will perform the addition
operation normally, but the register will be clock gated to remain
the original value. At the same time, the partial results from
memory or from the last SMMU will be passed directly to the
next SMMU in place of the values in the register. By exploiting
this Booth-level sparsity, the computational cycles and power
consumption can be saved simultaneously.

When the result of the last SMMU is the partial result of
the convolution operation, it will be sent to the next SMMU
directly. However, if the result is the ﬁnal result of the convo-
lution operation, it will be sent to the corresponding operation
modules based on the network architecture. The AE contains a

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 19,2025 at 14:04:35 UTC from IEEE Xplore.  Restrictions apply. 

186

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 17, NO. 2, APRIL 2023

ReLU module for linear activation, a pooling module to support
max pooling operation, and a quantizer module to quantize the
results. The computation of the batch normalization layer is
subsumed into the weights and biases of the convolution layer
to avoid the computation of ﬂoating point numbers. The ReLU
activation function is implemented by comparators combined
with other corresponding combinational logic. For the Pooling
module, we adopted additional pipeline registers combined with
comparators to implement max pooling operation. The quanti-
zation module quantizes 24-bit intermediate results to 8-bit with
conﬁgurable shifting module.

C. Workload Mapping

In order to map workloads to the hardware in both com-
pression and analysis modules, the proposed hardware exploits
two types of patterns. In this subsection, these two modes
will be described in detail. Before performing calculations, the
FPGA receives data from external DDR memory and stores
in a buffer. The data need to be organized based on the com-
putational paradigms of the two modules. Direct memory ac-
cess (DMA) controls the data ﬂow between the buffer and
the memories of the proposed hardware. To efﬁciently ex-
change data, the Ping-Pong memory mode is applied for I/O
memory.

1) Compression Module: The main operations in compres-
sion module is the multiplication of compression matrix W ∈
RN ×M and raw signal matrix x ∈ RN ×C. This matrix multi-
plication is composed of multiple matrix-vector products. We
split the two matrix multiplications into matrix W and multiple
channel vector xi ∈ RN ×1 products. Since the dimension N
of the matrix W and vector xi is larger than 32 (the value of
maximum computing capacity), it is not possible to calculate
the ﬁnal result with one loading. Therefore, it is feasible to load
a part of the matrix W and vector xi to obtain partial results and
then accumulate the overall partial results. The xi is stored in the
register of Booth encoding logic as multipliers. While the data
in matrix W c is encoded by the generated Booth multipliers. By
utilizing this mapping pattern, the raw signal vector xi can be
reused M times.

2) Analysis Module: For workload mapping of the analysis
module, each four SMMUs can perform a 1 × 1 convolution
operation. Take 1 × 8 convolution as an example, every 32 SM-
MUs are conﬁgured to be connected together for partial results
accumulation. Every 32 SMMUs can complete the convolution
operations of one kernel, and the whole hardware can perform
the operation of four convolutional kernels simultaneously with
one weight loading. The weights are stored in the register of
Booth encoding logic as multipliers. While the input feature
maps are encoded by the generated Booth multipliers. We de-
sign the pipeline speciﬁcally for 1-D convolution to maximize
data reuse. Fig. 6 shows the data reuse in 1-D convolution
pipeline. Due to the reusability of weights, the Booth multipliers
are able to remain unchanged for different input feature maps
until the computation of one kernel is completed. In addition,
the input feature maps and partial sums are reused across
SMMUs.

Fig. 6. Data reuse in 1-D convolution pipeline.

Fig. 7. Deﬁnition demonstration of seizure prediction horizon (SPH) and
preictal interval length (PIL).

V. EXPERIMENTAL RESULTS

We showcase our proposed framework by designing a seizure
prediction system to demonstrate effectiveness. We ﬁrst provide
preliminaries on epilepsy seizures, deﬁne a seizure prediction
system, and introduce the dataset used.

A. Seizure Prediction System

As a widespread chronic brain disease, epilepsy afﬂicts
around 70 million individuals, of which approximately up to
[37], [38], [39]. Patients are
one-third are drug-refractory
highly dependent on family members and caregivers due to the
safety uncertainty caused by seizure onset. Patients lose control
over body parts experiencing unconsciousness and movement
disorders when seizures occur. A seizure prediction system is
expected to generate a warning to the patients before the seizure
onset to provide time for emergent preparation under risky
scenarios such as the operation of heavy machinery.

A seizure prediction system could be abstracted into a binary
classiﬁcation problem of recognizing whether the patient is
about to have a seizure within an upcoming time frame. The
effectiveness of a seizure prediction system is largely determined
by the deﬁnition of preictal interval length (PIL), lead seizure,
and the seizure prediction horizon (SPH). An illustration of PIL
and SPH is given in Fig. 7. PIL deﬁnes the length of the preictal
period, while SPH indicates the preparation time for patients
between the warning and seizure onset. The length of SPH is
a trade-off between feeling anxious caused by a long waiting
time or not having enough time for proper preparation. Since
multiple seizures tend to occur within a short period of time,
thus lead seizures are of more research signiﬁcance in clinical
scenarios [40]. The lead seizure is deﬁned as any seizure that
is preceded by a seizure-free period. In this work, the length

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 19,2025 at 14:04:35 UTC from IEEE Xplore.  Restrictions apply. 

WU et al.: SOFTWARE-HARDWARE CO-DESIGN FOR ENERGY-EFFICIENT CONTINUOUS HEALTH MONITORING

187

TABLE I
SUMMARY OF SELECTED PATIENTS

We train each model for maximum of 150 epochs with an
early stopping criterion of no improvement for ten consecutive
epochs. #f iltersstem, #f iltersstem, sizef c and batch size are
set to 32, 32, 100 and 64, respectively. The kernel size of the
convolution layer in the stem layer is set to eight, and the kernel
size of all other convolution layers is set to four in the analysis
module. The stride is set to 1 for all convolution layers. The
kernel and stride size of the for each convolution layer in the
reconstruction module is set to three and two, respectively. All
three modules are implemented with Pytorch framework and
trained on NVIDIA 2080Ti GPU for acceleration.

D. Comparison With State-of-the-Art

of SPH and PIL are set to ﬁve and thirty minutes, respectively,
while the seizure-free interval is set to four hours to deﬁne lead
seizure. We collect preictal states only before lead seizures.

B. Dataset and Pre-Processing

EEG, as an important indicator for tracking brain activities,
is the most commonly adopted physiological signal in a seizure
prediction system. CHB-MIT sEEG [41] is a publicly accessible
database that contains sEEG signals from 22 epileptic patients.
The database contains 637 recordings recorded by 22 bi-polar
electrodes placed based on the globally recognized 10-20 system
from 17 females and ﬁve males. Some cases have electrodes
added or removed during the EEG acquisition process. We
remove these cases’ data to avoid feature inconsistency caused
by the variable electrode setting during acquisition. Patients with
more than one lead seizure and at least one preictal period of one
hour are chosen in this work. A sliding window is adopted to
generate samples from continuous sEEG signals. To alleviate
data imbalance, interictal data points are sampled using a non-
overlapping sliding window of 20 seconds, and preictal data
points are sampled with the same window length but with 25%
overlapping between two consecutive windows. The sampled
data points are standardized before feeding into the framework.
A summary of patients which qualify the requirements are listed
in Table I.

C. Experimental Setting

We ﬁrst elaborate on the setting of three network structure
related hyper-parameters, namely, the convolution ﬁlter number
of the ﬁrst up-sampling module #f iltersrecon, the convolution
ﬁlter number of the ﬁrst 1-D convolution layer in the stem
layer #f iltersstem and the size of the linear layer of analysis
network sizef c. For simplicity, the number of ﬁlters used in each
up-sampling module doubles the ﬁlter number of the previous
module. Similarly, the number of ﬁlters used in each convolution
layer of lth 1-D convolution block is set to 2 ∗ l ∗ #f iltersstem.
Adam optimizer is adopted with an initial learning rate of 5e − 4.

The effectiveness of our proposed CHM framework, on the
test case of seizure prediction, is validated by reporting seizure
prediction accuracy, sensitivity, and false prediction rate (FPR).
We pick two methods that use the original signal as input,
together with two methods that use statistics as input for compar-
ison. All four state-of-the-art methods are deep learning based
and listed as follows:

(cid:2)

(cid:2)

(cid:2)

(cid:2)

End-to-End approach [44]: the network structure of End-
to-End approach is also based on CNN which only applies
temporal convolution operation in early-stage and applies
both temporal and spatial convolution (channel-wise con-
volution) in the late-stage.
EEGNet [42]: EEGNet adopts a compact network archi-
tecture based on CNN containing various types of convo-
lution operations such as pointwise convolution, temporal
convolution and separable convolution.
STFT CNN [45]: the STFT CNN takes the Short Time
Fourier Transform of the EEG signals as input to a 3-layer
CNN.
Light-weight approach [43]: the light-weight approach is
a CNN based network structure that takes the Pearson
Correlation Coefﬁcient (PCC) [47] which is seen as syn-
chronization features across all channels as input.

For a fair comparison, all baseline methods are implemented
using Pytorch, carefully following the setting described in the
original papers. We train and evaluate each baseline method fol-
lowing the same settings in Section V-C using data pre-processed
and split the same way as described in V-B. A random Gaussian
matrix is adopted to compress signals for other baseline ap-
proaches. In order to demonstrate the robustness of the proposed
framework, we evaluate and report the average value of the
metrics over selected patients under various compression ratios:
2 , 1
1
16 . The comparison result is given in Fig. 8. We also
provide numerical value comparisons with compression ratio
1/16 in Table II. As can be seen, the seizure prediction system
based on our proposed methodology demonstrates consistent
improvement over other baseline methods under various com-
pression ratios, indicating the effectiveness and robustness of
the proposed CHM framework. Furthermore, with compression
ratios varying from 1
16 , our method produces a minimum
accuracy degradation. We notice more performance degradation
on Xu et al. [44] and Lawhern et al. [42]’s methods under signal

8 , and 1

2 to 1

4 , 1

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 19,2025 at 14:04:35 UTC from IEEE Xplore.  Restrictions apply. 

188

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 17, NO. 2, APRIL 2023

Fig. 8.
ratios. Higher accuracy, sensitivity and lower false positive rate indicate better performance.

Seizure prediction performance comparison between the system based on our proposed framework with state-of-the-art systems under various compression

TABLE II
SEIZURE PREDICTION PERFORMANCE COMPARISON UNDER THE COMPRESSION
RATIO OF 1/16

compression. These two methods take in raw signal as input
and compression by multiplication with a random Gaussian
matrix clearly captures no informative features for the under-
lying seizure prediction task. On the contrary, the other two
methods by Truong et al. [45] and Zhang et al. [43] which use
signal statistics as input show better stability under compression.
However, manually extracting statistics from signals as input
to the network discards potential task-relevant information and
limits the feature extraction ability of neural networks. Our
proposed framework jointly optimizes the sensing matrix for
signal compression and task analysis so that the neural network
extracts informative task-relevant features automatically. More-
over, we observe from Fig. 8 that setting λ = 1 (reconstruction
is optimized together with the analysis network) yields better
performance than setting λ = 0 (only the analysis network is
optimized during training). This agrees with our hypothesis
that the signal reconstruction task acts as regularization to the
analysis task to alleviate possible over-ﬁtting and lead to a more

generic learned representation. We evaluate the reconstruc-
tion performance with Peak Signal-to-noise Ratio (PSNR) and
Pearson’s Correlation Coefﬁcient (PCC). Let xc be the signal
of channel c and ˆxc be its corresponding reconstructed version,
PSNR is deﬁned as:

P SN R(x, ˆx) = 10 · log10 ·

(cid:3)

(cid:2)

max(x)
M SE(x, ˆx)

M SE(x, ˆx) =

1

C

·

C(cid:4)

c=0

(cid:4)xc − ˆxc(cid:4)2

,

(11)

(12)

where C stands for the number of channels in total.

PCC is deﬁned as:

P CC =

1

C

·

C(cid:4)

c=0

(cid:5)

(xc − μc)(ˆxc − ˆμc)
(cid:5)
(xc − μc)2

(ˆxc − ˆμc)2 ,

(13)

where μc and ˆμc denote the mean of the original signal and
the reconstructed signal at channel c, respectively. The average
PSNR and PCC values of all patients selected under various
compression ratios are reported in Table IV. Besides quantitative
results, a qualitative visual comparison of the reconstructed
signal against the original signal is provided in Fig. 9. It is seen
that the reconstructed signal recovers the visual characteristics
of the original signal to a large degree.

Table III compares clock frequency, the monitoring task, per-
formance, and FPGA resource utilization of our work with other
state-of-art implementations. We demonstrate 92.9% sensitivity
and 91.3% speciﬁcity in the more complicated task of seizure

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 19,2025 at 14:04:35 UTC from IEEE Xplore.  Restrictions apply. 

WU et al.: SOFTWARE-HARDWARE CO-DESIGN FOR ENERGY-EFFICIENT CONTINUOUS HEALTH MONITORING

189

TABLE III
FPGA IMPLEMENTATION RESULTS AND COMPARISON WITH PRIOR-ART PUBLICATIONS

TABLE IV
RECONSTRUCTION PERFORMANCE UNDER DIFFERENT COMPRESSION RATIOS

not provide complete information on hardware resources for
instance FF.

VI. CONCLUSION

We presented an energy-efﬁcient and reliable end-to-end
health monitoring system with a joint signal compression, anal-
ysis, and reconstruction framework. The proposed framework
compresses signals in a task-aware and power-efﬁcient manner.
The analysis and reconstruction modules are designed based on
the DNN algorithm with a ﬂexible architecture. The performance
of our proposed framework is validated by a seizure predic-
tion system. Results demonstrate that the proposed framework
outperforms state-of-the-art works under various compression
ratios. The hardware implementation on an Alveo U250 FPGA
board shows that our proposed CHM framework can operate at a
maximum clock frequency of 100 MHz with power consumption
of 0.207 W, which is a signiﬁcant improvement over the existing
DNN-based works.

REFERENCES

[1] R. Zhao, R. Yan, Z. Chen, K. Mao, P. Wang, and R. X. Gao, “Deep learning
and its applications to machine health monitoring,” Mech. Syst. Signal
Process., vol. 115, pp. 213–237, 2019. [Online]. Available: https://www.
sciencedirect.com/science/article/pii/S0888327018303108

[2] S. S. Gambhir, T. J. Ge, O. Vermesh, R. Spitler, and G. E. Gold, “Contin-
uous health monitoring: An opportunity for precision health,” Sci. Transl.
Med., vol. 13, no. 597, 2021, Art. no. eae5383.

[3] J. Kojuri, R. Boostani, P. Dehghani, F. Nowroozipour, and N. Saki, “Pre-
diction of acute myocardial infarction with artiﬁcial neural networks in
patients with nondiagnostic electrocardiogram,” J. Cardiovasc. Dis. Res.,
vol. 6, no. 2, 2015, Art. no. 51.

[4] D. Wu, J. Yang, and M. Sawan, “Bridging the gap between patient-speciﬁc
and patient-independent seizure prediction via knowledge distillation,” J.
Neural Eng., vol. 19, 2022, Art. no. 036035.

[5] D. Wu, S. Li, J. Yang, and M. Sawan, “neuro2vec: Masked Fourier
spectrum prediction for neurophysiological representation learning,” 2022,
arXiv:2204.12440.

[6] S. Zhao, J. Yang, and M. Sawan, “Energy-efﬁcient neural network for
epileptic seizure prediction,” IEEE Trans. Biomed. Eng., vol. 69, no. 1,
pp. 401–411, Jan. 2022.

[7] S. Zhao, J. Yang, Y. Xu, and M. Sawan, “Binary single-dimensional
convolutional neural network for seizure prediction,” in Proc. IEEE Int.
Symp. Circuits Syst., 2020, pp. 1–5.

Fig. 9. Visualization comparison plotting of the reconstructed and the corre-
sponding original signals.

prediction using the proposed CHM framework on the CHB-
MIT EEG dataset. The maximum operating frequency of the
proposed system is 100 MHz. We measured only 0.207 W overall
power consumption and 0.05 W dynamic power of proposed
framework on FPGA, and 1.2 W overall power consumption
and 0.756 W dynamic power combined proposed framework
with peripheral modules (DDR and XDMA). The proposed
implementation trades off the use of register resources to achieve
signiﬁcant power savings compared to the SNN-based imple-
mentations [20]. It is worth noticing that [16] and [46] did

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 19,2025 at 14:04:35 UTC from IEEE Xplore.  Restrictions apply. 

190

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 17, NO. 2, APRIL 2023

[8] J. Yang and M. Sawan, “From seizure detection to smart and fully embed-
ded seizure prediction engine: A review,” IEEE Trans. Biomed. Circuits
Syst., vol. 14, no. 5, pp. 1008–1023, Oct. 2020.

[9] S. Qaisar, R. M. Bilal, W. Iqbal, M. Naureen, and S. Lee, “Compressive
sensing: From theory to applications, a survey,” J. Commun. Netw., vol. 15,
no. 5, pp. 443–456, 2013.

[10] M. Rudelson and R. Vershynin, “Sparse reconstruction by convex relax-
ation: Fourier and gaussian measurements,” in Proc. 40th Annu. Conf. Inf.
Sci. Syst., 2006, pp. 207–212.

[11] L. Wang, K. Lu, P. Liu, R. Ranjan, and L. Chen, “IK-SVD: Dictionary
learning for spatial Big Data via incremental atom update,” Comput. Sci.
Eng., vol. 16, no. 4, pp. 41–52, 2014.

[12] H. Mamaghanian, N. Khaled, D. Atienza, and P. Vandergheynst, “Com-
pressed sensing for real-time energy-efﬁcient ecg compression on wire-
less body sensor nodes,” IEEE Trans. Biomed. Eng., vol. 58, no. 9,
pp. 2456–2466, Sep. 2011.

[13] D. L. Donoho, “Compressed sensing,” IEEE Trans. Inf. Theory, vol. 52,

no. 4, pp. 1289–1306, Apr. 2006.

[14] M. Shoaib, K. H. Lee, N. K. Jha, and N. Verma, “A 0.6–107 µw energy-
scalable processor for directly analyzing compressively-sensed EEG,”
IEEE Trans. Circuits Syst. I: Regular Papers, vol. 61, no. 4, pp. 1105–1118,
Apr. 2014.

[15] M. Shoaran, M. H. Kamal, C. Pollo, P. Vandergheynst, and A. Schmid,
“Compact low-power cortical recording architecture for compressive mul-
tichannel data acquisition,” IEEE Trans. Biomed. Circuits Syst., vol. 8,
no. 6, pp. 857–870, Dec. 2014.

[16] M. Sahani, S. K. Rout, and P. K. Dash, “Epileptic seizure recognition
using reduced deep convolutional stack autoencoder and improved kernel
RVFLN from EEG signals,” IEEE Trans. Biomed. Circuits Syst., vol. 15,
no. 3, pp. 595–605, Jun. 2021.

[17] H. Elhosary, M. H. Zakhari, M. A. Elgammal, M. A. A. E. Ghany, K.
N. Salama, and H. Mostafa, “Low-power hardware implementation of a
support vector machine training and classiﬁcation for neural seizure detec-
tion,” IEEE Trans. Biomed. Circuits Syst., vol. 13, no. 6, pp. 1324–1337,
Dec. 2019.

[18] N. J. Holter, “New method for heart studies,” Science, vol. 134, no. 3486,

pp. 1214–1220, 1961.

[19] L. S. Vidyaratne and K. M. Iftekharuddin, “Real-time epileptic seizure
detection using EEG,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 25,
no. 11, pp. 2146–2156, Nov. 2017.

[20] C. Fang, F. Tian, J. Yang, and M. Sawan, “A 217.8 MSOPs/W FPGA
FPGA-based online learning SNN processor using uniﬁed event-driven
structure and topology aware data reuse strategies,” in Proc. IEEE Asian
Solid-State Circuits Conf., 2022, pp. 1–3.

[21] A. Ignatov, “Real-time human activity recognition from accelerometer
data using convolutional neural networks,” Appl. Soft Comput., vol. 62,
pp. 915–922, 2018.

[22] D. Lai, Y. Zhang, X. Zhang, Y. Su, and M. B. B. Heyat, “An automated
strategy for early risk identiﬁcation of sudden cardiac death by using
machine learning approach on measurable arrhythmic risk markers,” IEEE
Access, vol. 7, pp. 94 701–94 716, 2019.

[23] Y.-P. Lin et al., “EEG-based emotion recognition in music listening,” IEEE

Trans. Biomed. Eng., vol. 57, no. 7, pp. 1798–1806, Jul. 2010.

[24] A. M. Nia, M. Mozaffari-Kermani, S. Sur-Kolay, A. Raghunathan, and
N. K. Jha, “Energy-efﬁcient long-term continuous personal health moni-
toring,” IEEE Trans. Multi-Scale Comput. Syst., vol. 1, no. 2, pp. 85–98,
Apr.–Jun. 2015.

[25] S. Mun and J. E. Fowler, “Residual reconstruction for block-based
compressed sensing of video,” in Proc. Data Compression Conf., 2011,
pp. 183–192.

[26] P. Nagesh and B. Li, “A compressive sensing approach for expression-
invariant face recognition,” in Proc. IEEE Conf. Comput. Vis. Pattern
Recognit., 2009, pp. 1518–1525.

[27] L. Qiao, S. Chen, and X. Tan, “Sparsity preserving projections with appli-
cations to face recognition,” Pattern Recognit., vol. 43, no. 1, pp. 331–341,
2010. [Online]. Available: https://www.sciencedirect.com/science/article/
pii/S0031320309001964

[28] C. M. Sandino, J. Y. Cheng, F. Chen, M. Mardani, J. M. Pauly, and S.
S. Vasanawala, “Compressed sensing: From research to clinical practice
with deep neural networks: Shortening scan times for magnetic reso-
nance imaging,” IEEE Signal Process. Mag., vol. 37, no. 1, pp. 117–127,
Jan. 2020.

[29] E. J. Candes and T. Tao, “Near-optimal signal recovery from random
projections: Universal encoding strategies?,” IEEE Trans. Inf. Theory,
vol. 52, no. 12, pp. 5406–5425, Dec. 2006.

[30] Z. Chen and J. J. Dongarra, “Condition numbers of Gaussian random
matrices,” SIAM J. Matrix Anal. Appl., vol. 27, no. 3, pp. 603–620, 2005.
[31] T. Blumensath and M. E. Davies, “Iterative hard thresholding for
compressed sensing,” Appl. Comput. Harmon. Anal., vol. 27, no. 3,
pp. 265–274, 2009. [Online]. Available: https://www.sciencedirect.com/
science/article/pii/S1063520309000384

[32] S. Mallat and Z. Zhang, “Matching pursuits with time-frequency dic-
tionaries,” IEEE Trans. Signal Process., vol. 41, no. 12, pp. 3397–3415,
Dec. 1993.

[33] J. A. Tropp and A. C. Gilbert, “Signal recovery from random measurements
via orthogonal matching pursuit,” IEEE Trans. Inf. Theory, vol. 53, no. 12,
pp. 4655–4666, Dec. 2007.

[34] S. S. Chen, D. L. Donoho, and M. A. Saunders, “Atomic decomposition

by basis pursuit,” SIAM Rev., vol. 43, no. 1, pp. 129–159, 2001.

[35] J.-S. Huang, Y. Li, B.-Q. Chen, C. Lin, and B. Yao, “An intelli-
gent eeg classiﬁcation methodology based on sparse representation
enhanced deep learning networks,” Front. Neurosci., vol. 14, 2020,
Art. no. 808.

[36] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
recognition,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2016,
pp. 770–778.

[37] R. Fisher et al., “ILAE ofﬁcial report: A practical clinical deﬁnition of

epilepsy,” Epilepsia, vol. 55, pp. 475–482, 2014.

[38] H. Zhang, D. Lai, C. Xie, H. Zhang, and W. Chen, “Directed-transfer-
function based analysis for epileptic prediction,” in Proc. 9th Int. Congr.
Image Signal Process. Biomed. Eng. Inf., 2016, pp. 1487–1491.

[39] W. H. Organization, Neurological Disorders: Public Health Challenges.

Geneva, Switzerland: World Health Organization, 2006.

[40] H.-H. Chen and V. Cherkassky, “Performance metrics for online seizure
prediction,” Neural Netw., vol. 128, pp. 22–32, 2020. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0893608020301428

[41] A. Shoeb and J. Guttag, “Application of machine learning to epilep-
tic seizure detection,” in Proc. 27th Int. Conf. Mach. Learn., 2010,
pp. 975–982.

[42] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and
B. J. Lance, “EEGNet: A compact convolutional neural network for eeg-
based brain–computer interfaces,” J. Neural Eng., vol. 15, no. 5, Jul. 2018,
Art. no. 056013, doi: 10.1088/1741-2552/aace8c.

[43] Z. Shasha, D. Chen, R. Ranjan, K. Y. H.Tang, and A. Zomaya,
“A lightweight solution to epileptic seizure prediction based on eeg
synchronization measurement,” J. Supercomputing, vol. 77, pp. 1–19,
04 2021.

[44] Y. Xu, J. Yang, S. Zhao, H. Wu, and M. Sawan, “An end-to-end deep
learning approach for epileptic seizure prediction,” in Proc. 2nd IEEE Int.
Conf. Artif. Intell. Circuits Syst., 2020, pp. 266–270.

[45] N. Truong et al., “Convolutional neural networks for seizure prediction us-
ing intracranial and scalp electroencephalogram,” Neural Netw., vol. 105,
pp. 104–111, 2018.

[46] C. Shea, A. Page, and T. Mohsenin, “SCALENet: A scalable low power
accelerator for real-time embedded deep neural networks,” in Proc. Great
Lakes Symp. VLSI, 2018, pp. 129–134.

[47] P. Schober, C. Boer, and L. A. Schwarte, “Correlation coefﬁcients:
Appropriate use and interpretation,” Anesth. Analg., vol. 126, no. 5,
pp. 1763–1768, 2018.

Di Wu received the B.S. degree from the Department
of Computer Science, Harbin Institute of Technol-
ogy, Harbin, China, and the M.S. degree in elec-
trical and computer engineering from Boston Uni-
versity, Boston, MA, USA. He is currently work-
ing toward the Ph.D. degree with the Center of
Excellence in Biomedical Research on Advanced
Integrated-on-chips Neurotechnologies, School of
Engineering, Westlake University, Hangzhou, China.
His research interests include self-supervised learn-
ing and efﬁcient deep learning for neurophysiological

applications.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 19,2025 at 14:04:35 UTC from IEEE Xplore.  Restrictions apply. 

WU et al.: SOFTWARE-HARDWARE CO-DESIGN FOR ENERGY-EFFICIENT CONTINUOUS HEALTH MONITORING

191

Shiqi Zhao (Student Member, IEEE) received the
B.S. degree in applied physics from Xi’an Polytech-
nic University, Xi’an, China, in 2016, and the M.S.
degree in integrated circuits and intelligent systems
from Peking University, Beijing, China, in 2019. In
2019, he joined the Center of Excellence in Biomed-
ical Research on Advanced Integrated-on-chips Neu-
rotechnologies (CenBRAIN Neurotech), School of
Engineering, Westlake University, Hangzhou, China,
where he is currently working toward the Ph.D. de-
gree. His research interests include brain machine
interface, energy-efﬁcient deep learning algorithm, customized computer ar-
chitecture design and hardware implementation for bio-medical deep learning
processors.

Jie Yang (Member, IEEE) received the B.S. degree
in electronic science and technology from Tianjin
University, Tianjin, China, in 2010, and the Ph.D.
degree in microelectronics from the Institute of Semi-
conductors, Chinese Academy of Sciences, Beijing,
China, in 2015. He is currently a Research Associate
Professor with the School of Engineering, Westlake
University, Hangzhou, China. From 2015 to 2019,
he was a Postdoctoral Fellow with the I2Sense Lab,
Department of Electrical and Computer Engineer-
ing, University of Calgary, Calgary, AB, Canada.
In 2019, he joined Westlake University, Hangzhou. His research interests in-
clude circuits and systems for intelligent biomedical applications, mixed-signal
SoC for brain-machine interface, energy-efﬁcient AI algorithms, and VLSI
architecture.

Mohamad Sawan (Fellow, IEEE) received the Ph.D.
degree from the University of Sherbrooke, Sher-
brooke, QC, Canada. He is currently the Chair Profes-
sor with Westlake University, Hangzhou, China, and
a Emeritus Professor with Polytechnique Montreal,
Montr, QC, Canada. He is the Founder and Director
of the Center of Excellence in Biomedical Research
on Advances-on-Chips Neurotechnologies, Westlake
University, and of the Polystim Neurotech Lab in
Polytechnique Montreal. He is the Co-Founder, As-
sociate Editor and was the Editor-in-Chief of IEEE
TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS (2016–2019). He
is the Founder of the ﬂagship IEEE International NEWCAS conference and
co-founder of the International IEEE-BioCAS and IEEE-AICAS Conferences.
He was the General Chair hosting both the 2016 IEEE International Symposium
on Circuits and Systems (ISCAS) and the 2020 IEEE International Medicine,
Biology and Engineering Conference (EMBC). He was awarded the Canada
Research Chair in Smart Medical Devices (2001–2015), and was leading the
Microsystems Strategic Alliance of Quebec (ReSMiQ), Canada (1999–2018).
He has authored or coauthored more than 1000 peer-reviewed papers, one Hand-
book, three books, 13 book chapters, 12 patents, and 20 other patents are pending.
He was the recipient of several awards, among them the Barbara Turnbull Award
from the Canadian Institutes of Health Research (CIHR), the J.A. Bombardier
and Jacques-Rousseau Awards from the ACFAS, the Queen Elizabeth II Golden
Jubilee Medal, the Medal of Merit from the President of Lebanon, the Shanghai
International Collaboration Award, the Chinese Government Friendship Award,
and the Hangzhou Outstanding Talent Award. Dr. Sawan is a Fellow of the
Royal Society of Sciences of Canada, a Fellow of the Canadian Academy of
Engineering, a Fellow of the Engineering Institutes of Canada, a Fellow of the
IEEE, a Fellow of the Asia-Paciﬁc Artiﬁcial Intelligence Association, and an
Ofﬁcer of the National Order of Quebec.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on December 19,2025 at 14:04:35 UTC from IEEE Xplore.  Restrictions apply.
