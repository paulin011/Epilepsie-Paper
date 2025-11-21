# Chopannavaz and Ghaderi - 2025 - An Empirical Investigation of Reconstruction-Based Models for Seizure Prediction from ECG Signals

5
2
0
2

r
p
A
1
1

]
P
S
.
s
s
e
e
[

1
v
1
8
3
8
0
.
4
0
5
2
:
v
i
X
r
a

An Empirical Investigation of Reconstruction-Based Models for

Seizure Prediction from ECG Signals

Mohammad Reza Chopannavaz and Foad Ghaderi ∗

Human-Computer Interaction Lab., Faculty of Electrical and Computer Engineering, Tarbiat Modares

University, Tehran, Iran

Abstract

Epileptic seizures are sudden neurological disorders characterized by abnormal, excessive neuronal

activity in the brain, which is often associated with changes in cardiovascular activity. These dis-

ruptions can pose signiﬁcant physical and psychological challenges for patients. Therefore, accurate

seizure prediction can help mitigate these risks by enabling timely interventions, ultimately improv-

ing patients’ quality of life. Traditionally, EEG signals have been the primary standard for seizure

prediction due to their precision in capturing brain activity. However, their high cost, susceptibility

to noise, and logistical constraints limit their practicality, restricting their use to clinical settings. In

order to overcome these limitations, this study focuses on leveraging ECG signals as an alternative for

seizure prediction. In this paper, we present a novel method for predicting seizures based on detect-

ing anomalies in ECG signals during their reconstruction. By extracting time-frequency features and

leveraging various advanced deep learning architectures, the proposed method identiﬁes deviations

in heart rate dynamics associated with seizure onset. The proposed approach was evaluated using

the Siena database and could achieve speciﬁcity of 99.16%, accuracy of 76.05%, and false positive

rate (FPR) of 0.01/h, with an average prediction time of 45 minutes before seizure onset. These

results highlight the potential of ECG-based seizure prediction as a patient-friendly alternative to

traditional EEG-based methods.

Keywords Anomaly Detection; Autoencoders; Deep Learning; Electrocardiogram; Epilepsy; Seizure
Prediction.

1

Introduction

Epilepsy is a neurological disorder characterized by recurrent, unprovoked seizures caused by sudden

and excessive electrical discharges in the brain. Seizures have a wide range of characteristics, diﬀering

∗ Corresponding Author: fghaderi@modares.ac.ir (F. Ghaderi)

1

 
 
 
 
 
 
in form, frequency, and intensity, which can make the task of diagnosis and prediction challenging.

Despite advances in medical therapies, a signiﬁcant proportion of epileptic patients continue to expe-

rience seizures even after receiving medical treatment. This is known as drug-resistant or intractable

epilepsy [1]. As a result, many patients struggle to achieve full seizure control, which profoundly

impacts their quality of life by increasing the risk of injury, limiting daily activities, and exacerbating

mental health issues [2, 3].

Taking into account the uncontrollable nature of epilepsy, eﬀective seizure management and pre-

diction have become critical areas of research. Seizures typically progress through distinct phases,

including inter-ictal (between seizures), pre-ictal (before seizure onset), ictal (seizure onset), and

post-ictal (recovery) [4]. It should be noted that since the inter-ictal phase represents baseline physi-

ological conditions, data from this phase can be utilized as a normal reference for the identiﬁcation of

deviations from the pre-ictal phase. The ability to anticipate an impending seizure could enable early

intervention measures, signiﬁcantly enhancing safety, autonomy, and quality of life for epileptic pa-

tients. Traditionally, seizure prediction approaches relied on electroencephalogram (EEG) recordings

to detect abnormal brain activity [5, 6]; however, practical challenges with EEG, such as its limited

portability, discomfort in long-term use, and susceptibility to motion artifacts, have driven interest

in alternative, more accessible biomarkers like electrocardiogram (ECG) signals. Recent research

suggests that ECG-based approaches may provide valuable insights into pre-ictal states, oﬀering

a promising non-invasive option for seizure prediction [7]. Recent comprehensive reviews further

emphasize the potential of ECG-driven seizure prediction, highlighting the successful application of

machine learning techniques as a viable and scalable alternative to EEG-based approaches [8, 9].

This growing interest in ECG-based seizure prediction is rooted in physiological ﬁndings that demon-

strate how epileptic seizures interfere with autonomic nervous system (ANS) function, leading to

distinct and measurable changes in cardiac dynamics. During seizures, autonomic imbalances can

cause abrupt heart rate ﬂuctuations. This results in sudden tachycardia or bradycardia, irregular

rhythms, and even transient asystole in severe cases. Notably, these cardiac disturbances are not

limited to the seizure itself but can also occur in the pre-ictal phase, where subtle changes in heart

rate and other ECG-derived parameters have been observed as potential precursors to seizure onset

[10, 11]. These pre-ictal cardiac signatures oﬀer a promising non-invasive avenue for seizure predic-

tion, especially in cases where traditional EEG monitoring is impractical due to its limited mobility

and setup requirements.

Numerous studies have demonstrated the potential of analyzing heart rate ﬂuctuations to predict

epileptic seizures. These studies primarily focus on the analysis of Heart Rate Variability (HRV)

features as indicators of ANS dysregulation. The research studies such as [12–17] have highlighted

that HRV features in various domains—including time, frequency, and non-linear measures—can

reveal patterns indicative of upcoming seizure onset. These changes reﬂect physiological shifts within

the ANS, speciﬁcally sympathetic and parasympathetic activity, which are common during the pre-

ictal stage. Such ﬁndings underscore the promise of HRV-based analysis as a non-invasive method

for seizure prediction.

2

However, despite these promising ﬁndings, HRV-based approaches have limitations that impact their

applicability in real-time settings. One primary challenge is the requirement of a sustained data

window over a relatively long period of time—typically two to three minutes—to extract reliable

HRV metrics. This introduces a delay, making HRV-based methods less practical for immediate

seizure prediction. This limitation implies that patients must wait several minutes while features are

extracted and algorithms are ﬁne-tuned, causing delay in timely intervention in dynamic, real-world

environments.

Taking into account these timing constraints, Ode et al.

[18], developed a rapid-response model

using a Self-Attentive Autoencoder (SA-AE) designed for detecting anomalies in heart rate patterns

with minimal latency. By focusing on reconstruction error as an anomaly score, their SA-AE model

enables quick classiﬁcation of pre-ictal signals without the lengthy preprocessing typically required

for HRV analysis. Their results demonstrated that deep learning architectures like the SA-AE are

highly eﬀective at detecting early signs of seizures from physiological data, thereby enabling more

responsive seizure prediction.

Building on the work by Ode et al. [18], this study expands the analysis of ECG data beyond tradi-

tional HRV metrics through the utilization of time-frequency transformations. These transformations

allow for a more detailed examination of both temporal and spectral characteristics, capturing subtle

and transient variations in cardiac dynamics that are often overlooked by conventional HRV meth-

ods. By applying these domain transformations, we aim to develop a robust, near-real-time seizure

prediction model that overcomes the latency limitations of standard HRV methods and provides

timely warnings to patients, ultimately enhancing the safety and quality of life for epileptic patients.

In response to the critical challenges of seizure prediction, this study introduces the following signif-

icant contributions:

• The proposed model leverages Discrete Wavelet Transform (DWT), Continuous Wavelet Trans-

form (CWT), and Short-Time Fourier Transform (STFT) to extract time-frequency features

from ECG signals, enhancing the detection of transient anomalies linked to pre-ictal states.

• By employing deep learning models such as Autoencoders and Transformer-based architectures,

the framework reconstructs input signals and identiﬁes seizure precursors based on deviations

between input and reconstruction, enabling unsupervised anomaly detection.

• Taking into account the individual diﬀerences in ECG patterns, all models are trained using

patient-speciﬁc characteristics to ensure personalized seizure prediction.

• After training is completed, a moving average is used to smooth the reconstruction error,

improving the signal-to-noise ratio and reducing the number of false positives.

• Afterwards, we compute a statistical threshold based on the mean and standard deviation of

the training error distribution, which enables patient-speciﬁc prediction.

• Finally, the proposed methodology is evaluated on the Siena Scalp EEG database using clini-

3

cally relevant metrics to demonstrate its real-world eﬀectiveness.

2 Materials and Methods

The proposed seizure prediction framework, as illustrated in Fig. 1, follows a structured pipeline

that includes data acquisition, preprocessing, feature extraction, modeling, post-processing, and per-

formance evaluation. First, raw ECG signals are collected and preprocessed through noise ﬁltering

and segmentation to ensure consistency. Next, time-frequency transformation techniques—Discrete

Wavelet Transform (DWT), Continuous Wavelet Transform (CWT), and Short-Time Fourier Trans-

form (STFT)—are applied to extract transient and steady-state features crucial for identifying pre-

ictal patterns. These features are then analyzed using three deep learning models: LSTM Autoen-

coder (LSTM-AE), Multi-Head Convolutional LSTM Autoencoder (MH-C-LSTM-AE), and Trans-

former Encoder-Encoder (T-EE), which are designed for reconstruction-based anomaly detection.

Afterward, post-processing steps are applied to reﬁne predictions by mitigating noise and distin-

guishing normal segments from anomalous ones. Finally, the framework is evaluated using standard

performance metrics to ensure robustness across patient datasets.

Data
Preprocessing

Segmentation

Denoising and
Filtering

Modeling

LSTM-AE

Multi-Head
Conv-LSTM-AE

Transformer(cid:160)
(Enc-Enc)

Performance
Evaluation

Data
Acquisition

Siena(cid:160)
Database

Feature
Extraction

Discrete Wavelet
Transform

Continuous Wavelet
Transform

Short-Time Fourier
Transform

Post-Processing

Smoothing

Threshold
Selection

Figure 1: Overall components of the proposed approach for Epileptic Seizure Prediction.

2.1 Data Acquisition

In this study, the data were acquired from the Siena Scalp EEG Database [19], a comprehensive,

open-access dataset provided by the University of Siena, Italy. This dataset contains simultaneous

scalp EEG and ECG recordings from 14 epilepsy patients, primarily diagnosed with focal epilepsy

and with some cases exhibiting generalized tonic-clonic seizures. Each patient recording captures at

least one complete seizure event. A summary of the demographic data of the patients and a selection

of clinical characteristics are provided in Table 1.

The ECG signals in the Siena Database are recorded at a high sampling rate of 512 Hz, ensuring

4

suﬃcient temporal resolution to capture subtle cardiac rhythm variations that may indicate impend-

ing seizure onset. Furthermore, annotations are provided for each seizure event, marking the onset

and oﬀset times, which allows for accurate identiﬁcation of cardiac events associated with seizures

[20, 21].

Table 1: Characteristics of the patients included in the study.

Patient ID Age Gender Seizure Type Seizures # Recording (Min)

PN00

PN01

PN03

PN05

PN06

PN07

PN09

PN10

PN11

PN12

PN13

PN14

PN16

PN17

55

46

54

51

36

20

27

25

58

71

34

49

41

42

Male

Male

Male

Female

Male

Female

Female

IAS

IAS

IAS

IAS

IAS

IAS

IAS

5

2

2

3

5

1

3

Male

FBTC

10

Female

Male

Female

IAS

IAS

IAS

Male

WIAS

Female

Male

IAS

IAS

1

4

3

4

2

2

198

809

752

359

722

523

410

1002

145

246

519

1408

303

308

IAS is focal onset impaired awareness; WIAS is focal onset without impaired awareness; FBTC is

focal to bilateral tonic-clonic; T is temporal; F is frontal; R is right; L is left; and B is Bilateral.

2.2 Data Preprocessing

In the preprocessing stage of this study, the primary aim is to enhance the quality of ECG signals by

applying segmentation and denoising techniques to prepare the data for feature extraction and model

training. Therefore, the ECG signals are ﬁrst segmented into manageable time windows, and then,

denoising techniques are applied to minimize noise and artifacts present in ECG recordings. This

preprocessing steps enhances signal clarity and reliability, providing a cleaner input for downstream

feature extraction and model training.

2.2.1 Segmentation

In the segmentation phase, the ECG data is divided into well-deﬁned time windows to enable analysis

of temporal patterns leading up to seizure events. This segmentation strategy is critical for isolating

distinct segments within the continuous ECG signal. In this way, it is feasible to capture pre-ictal

and ictal characteristics that may signal impending seizures. In order to capture the dynamic nature

of ECG signals, we employed a range of window sizes—1, 5, and 10 seconds—each at diﬀerent

5

overlap levels, including 0 (no overlap) and partial overlaps of 1, 3 or 5 seconds. Through the

use of these varied conﬁgurations, we are able to examine the impact of window size and overlap

on prediction accuracy and feature stability. In analyzing a signal over a wider window, we may

be able to detect broader patterns, which might provide reliable information regarding changes in

heart rate. Conversely, smaller windows with partial overlaps can provide a higher level of temporal

resolution, which is crucial when detecting rapid, transient ﬂuctuations associated with pre-ictal

states. Additionally, the overlapping segments provide sequential continuity, which ensures that no

critical data is lost at the boundaries between segments.

2.2.2 Denoising and Filtering

In ECG signal processing, denoising plays a crucial role in accurate feature extraction and prediction

of medical conditions, including epileptic seizures. The primary artifacts in ECG signals include

power line interference, motion artifacts, and baseline wander. In seizure prediction, the baseline

wander artifact, which is often triggered by respiration or body movements, might provide valuable

information about the underlying physiological conditions related to the connection between the ANS

and the cardiovascular system during a seizure. Eliminating it completely can lead to the loss of subtle

seizure-related patterns embedded in low-frequency oscillations. Preserving this component allows

feature extraction methods to capture both high-frequency and low-frequency dynamics, enhancing

predictive performance.

Accordingly, a low-pass ﬁltering strategy was employed to keep slow-changing components like base-

line wander while suppressing high-frequency noise that can obscure signal interpretation. By main-

taining this balance, we are able to ensure that noise reduction does not compromise predictive

information, resulting in more reliable and accurate seizure forecasting models.

2.3 Feature Extraction

In order to accurately predict seizure onsets, reliable feature extraction is necessary to transform input

ECG signals into meaningful representations that capture signiﬁcant patterns, temporal trends, and

characteristics relevant to seizure prediction. The intricate and high-dimensional nature of ECG

data necessitates extracting features that capture subtle pre-ictal dynamics, as these are vital for

accurate and eﬀective seizure prediction. To address this complexity, several techniques have been

investigated. These include the set of features created by concatenating the coeﬃcients derived from

the discrete wavelet transform, the scalogram representation generated by the Continuous Wavelet

Transform, and the spectrogram representation produced by the Short-Time Fourier Transform. To

assess whether each method was eﬀective in improving signal representation and its impact on model

performance, each method was investigated independently. In the following, we provide a detailed

overview of each technique, the motivation behind the chosen parameters, and their signiﬁcance in

the context of seizure prediction.

6

2.3.1 Discrete Wavelet Transform

In the ﬁrst approach, DWT was used to decompose the ECG signal into time-frequency components,

enabling simultaneous analysis of transient and steady-state features. In contrast to Fourier Trans-

form, DWT provides both time and frequency information, making it eﬀective for ECG signals with
abrupt changes. The DWT of a signal x[n], sampled at discrete points, is computed using a mother
wavelet ψ(n), scaled and translated as follows:

(1)

(2)

Wj,k =

x[n]

·

ψj,k(n)

Xn

where:

ψj,k(n) = 2−j/2ψ

2−jn

k

−

(cid:1)

(cid:0)

Here, j denotes the scale index, k is the translation index, and ψ(n) is the mother wavelet. These
coeﬃcients Wj,k encapsulate both the temporal and spectral characteristics of the signal.

In this study, the sym4 wavelet was selected due to its symmetry and structural similarity to ECG

waveforms. This will help in minimizing distortion while eﬀectively capturing both rapid changes

(e.g., arrhythmias) and smooth trends (e.g., heart rate variability) [22, 23]. The decomposition was

performed up to level 3, balancing the preservation of high-frequency components, such as noise

and rapid ﬂuctuations, with low-frequency trends that reﬂect broader physiological changes [24].

The decomposition process at each level involved applying low-pass and high-pass ﬁlters, yielding
approximation (cAj ) and detail (cDj ) coeﬃcients:

cAj [n] =

h[k]

Xk

cDj [n] =

g[k]

Xk

cAj−1[2n

cAj−1[2n

k]

k]

−

−

·

·

(3)

where h[k] and g[k] denote the low-pass and high-pass ﬁlter coeﬃcients, respectively. After decompo-
sition, the coeﬃcients cA3, cD3, cD2, cD1 were normalized to mitigate diﬀerences in signal magnitude
across patients, ensuring comparability across datasets. Finally, the normalized coeﬃcients were

concatenated into a feature vector, creating a compact and robust representation of ECG signals for

subsequent analysis.

2.3.2 Continuous Wavelet Transform

In the second approach, the CWT was employed to analyze the energy distribution of the ECG

signal across both the time and frequency domains. Unlike traditional methods, CWT provides a

detailed time-frequency representation, making it highly eﬀective for detecting transient features in
non-stationary biomedical signals such as ECG. The CWT of a signal x(t) is deﬁned as:

where:

C(a, b) =

∞

Z

−∞

x(t)ψ∗

a,b(t) dt

ψ∗
a,b(t) =

1
√a

ψ

t

b
−
a (cid:19)

(cid:18)

7

(4)

(5)

Here, a > 0 indicates the scale parameter, controlling frequency variations, while b denotes the
translation parameter, governing time localization. The function ψ∗(t) is the complex conjugate of
the mother wavelet. This decomposition enables precise analysis of signal variations at diﬀerent time

instances and frequency bands.

In this study, the Mexican hat wavelet (mexh) was selected as the mother wavelet due to its strong

resemblance to QRS waves and excellent localization properties in both the time and frequency

domains. The mathematical deﬁnition of the Mexican hat wavelet is given by:

ψ(t) =

1

(cid:0)

t2

e−t2/2

(cid:1)

−

(6)

This wavelet is particularly well-suited for identifying transient energy shifts in ECG signals, which

are crucial for detecting pre-ictal activity preceding seizure events. Prior research has demonstrated

that mexh eﬀectively captures subtle energy variations in biomedical signals, making it a reliable

tool for analyzing rapid transitions in ECG signals [25].

To achieve an optimal balance between resolution and computational eﬃciency, we selected a scale
range of a = 128. This range enables capturing both low-frequency trends (e.g., heart rate variations)
and high-frequency changes (e.g., noise or sharp bursts). The scalogram, which represents the energy

distribution of the signal across diﬀerent scales and time instances, is computed as:

where E(a, b) denotes the energy at scale a and translation b. Following the decomposition, to
ensure consistency across datasets, scalogram energy was normalized, enhancing seizure prediction

E(a, b) =

C(a, b)

|

2

|

(7)

by identifying subtle pre-ictal patterns.

2.3.3 Short-Time Fourier Transform

In the third approach, the STFT was employed to analyze the time-frequency characteristics of ECG

signals, capturing both steady-state trends and transient variations in ECG signals. These variations

often include abrupt spectral energy shifts, which are critical indicators of pre-ictal states. The STFT
of a signal x(t) is deﬁned as:

X(t, f ) =

∞

Z

−∞

x(τ )w(τ

−

t)e−j2πf τ dτ

(8)

−

where w(τ
t) denotes a window function that selects a segment of the signal centered at time t,
and f indicates the analyzed frequency component. This equation demonstrates that the signal is
divided into short segments via the window function w, and the Fourier Transform is then applied
to each segment, providing a localized frequency analysis.

In this study, a window size of 512 samples was selected to balance temporal and spectral resolution,

ensuring the detection of both rapid transitions (e.g., arrhythmic events) and long-term variations

(e.g., heart rate trends). A smaller window improves temporal resolution at the cost of frequency

accuracy, while a larger window enhances frequency resolution but reduces time localization. This

8

window size aligns well with the typical ECG sampling rate, eﬀectively capturing both low and

high-frequency features [26].

Once the STFT coeﬃcients are obtained, the spectrogram is computed by computing the squared

magnitude of the STFT:

|
where S(t, f ) denotes the signal’s energy distribution across time and frequency. This spectrogram
provides a visual representation of how the power of diﬀerent frequency components varies over

|

S(t, f ) =

X(t, f )

2

(9)

time. Next, to ensure consistency across various patient datasets, the spectrogram energy was nor-

malized, reducing the impact of inter-ictal variability while preserving the most relevant pre-ictal

characteristics.

2.4 Modeling

In seizure prediction, the ability to detect anomalies in physiological signals is an essential component

of early warning systems. These anomalies often manifest as subtle deviations from normal patterns

during the pre-ictal phase, which precedes seizure onset. In this study, we present a reconstruction-

based anomaly detection approach that can be used to predict the onset of epileptic seizures in

an unsupervised manner. By analyzing signal representations produced through feature extraction,

the approach minimizes reliance on labeled data, thereby enhancing its adaptability and scalability

across diverse patient proﬁles.

The core idea of this study is based on the reconstruction error generated by models trained exclu-

sively on normal segments of ECG signals. These models learn to represent the baseline patterns

of the signal, capturing its inherent characteristics under typical, non-seizure conditions. However,

during the pre-ictal phase, subtle yet signiﬁcant deviations emerge in the signal’s characteristics as

the heart responds to physiological changes preceding a seizure event. These deviations, often un-

detectable through direct observation, lead to higher reconstruction errors when the signal is passed

through models. This phenomenon makes reconstruction error a reliable indicator for identifying

potential pre-ictal activity, serving as an indicator of imminent seizure onset.

In order to investigate these anomalies, three reconstruction-based models were used: the LSTM Au-

toencoder, the Multi-Head Convolutional LSTM Autoencoder, and the Transformer-Based Anomaly

Detection Model. Each model is meticulously crafted to address distinct challenges inherent in ECG

signal processing. These challenges include capturing long-term temporal dependencies, modeling

complex spatial relationships, and identifying sequential patterns with high ﬁdelity. By independently

evaluating these models, the study rigorously evaluates their individual contributions to anomaly de-

tection, providing insights into their eﬀectiveness in advancing seizure prediction.

2.4.1 Training and Testing Methodology

In order to develop a stable and personalized seizure prediction framework, a short segment is selected

from the initial portion of each patient’s ECG recording. This segment represents a typical, non-

9

seizure baseline signal, ensuring that the model is trained exclusively on normal patterns. By focusing

on these baseline characteristics, the models develop a comprehensive understanding of the patient’s

unique ECG dynamics. This enables them to identify subtle deviations from normality during the

prediction phase.

Once trained, the models are applied to the entire patient dataset (except the portion selected for

training) to identify anomalies indicative of seizure activities. This approach is particularly advan-

tageous for patient-speciﬁc analysis, as it inherently accounts for individual variations in ECG mor-

phology and rhythm. By tailoring the models to each patient’s data, the framework achieves a high

degree of personalization, which is critical for accommodating the diverse physiological characteris-

tics of epileptic patients. Furthermore, the reliance on patient-speciﬁc training segments eliminates

the need for generalized assumptions, enhancing the performance of anomaly detection [27, 28].

2.4.2 LSTM Autoencoder

The LSTM-AE is a neural network designed for sequential data, using an encoder-decoder structure.

The encoder, composed of stacked Long Short-Term Memory (LSTM) layers, generates a compact

latent representation, which captures long-term dependencies within the input data.

In order to

ensure robust training and to prevent overﬁtting, optimization layers—Batch Normalization and

Dropout—were applied. The decoder, mirroring the encoder, reconstructs the input signal to match

the original as closely as possible. Fig. 2 illustrates the LSTM-AE architecture, highlighting its

layers and structure.

LS

DO

BN

Input

Enc
LSTM

DO

BN

Output

Dec
LSTM

Figure 2: Schematic Diagram of LSTM-AE. Enc is Encoder; Dec is Decoder; BN is Batch Normal-

ization; DO is Dropout; LSTM is Long Short-Term Memory; and LS is Latent Space.

2.4.3 Multi-Head Convolutional LSTM Autoencoder

MH-C-LSTM-AE is a hybrid model that integrates convolutional layers, LSTM layers, and multi-head

attention mechanisms to eﬀectively capture both spatial and temporal complexity. In this model, the

encoder begins with 1D convolutional layers, which identify localized features such as QRS complexes

and waveform patterns. These layers use dilation factors to expand the receptive ﬁeld, allowing

the model to capture both ﬁne-grained and broader patterns. Next, LSTM layers model temporal

dependencies, tracking periodic trends and abrupt transitions. Additionally, in order to enhance the

10

eﬃciency of the encoder, multi-head attention mechanisms are integrated into the model, enabling the

model to dynamically focus on the most critical regions of the signal representations. This attention-

based feature enhances the detection of subtle, localized anomalies indicative of pre-ictal states, even

with complex background patterns. The decoder, mirroring the encoder, reconstructs both temporal

and spatial signal features, ensuring accurate anomaly detection. The architecture is motivated by

the need to comprehensively capture the multiscale nature of ECG-derived representations, which

often contain both localized events (e.g., QRS complexes) and long-term dependencies (e.g., heart

rate variability) [29]. The architecture of this model is illustrated in Fig. 3.

DO

BN

DO

BN

DO

BN

LS

DO

BN

DO

BN

Input Enc

CNN 1

Enc
CNN 2

Enc
CNN 3

MH
A

Enc
LSTM

MH
A

Dec
LSTM Dec

CNN 1

Dec
CNN 2

Output

Dec
CNN 3

Figure 3: Schematic Diagram of Multi-Head-Conv-LSTM-AE. Enc is Encoder; Dec is Decoder; BN

is Batch Normalization; DO is Dropout; CNN is Convolution Layer; LSTM is Long Short-Term

Memory; MH is Multi-Head Attention Layer; and LS is Latent Space.

2.4.4 Transformer-Based Anomaly Detection Model

Transformers are highly eﬀective for seizure prediction due to their ability to model long-range de-

pendencies in ECG signals. Unlike RNNs and LSTMs, which process data sequentially, transformers

operate in parallel, signiﬁcantly improving eﬃciency and scalability—critical for analyzing contin-

uous ECG recordings. The proposed transformer-based model leverages two transformer encoder

layers to process ECG signal representations. Each layer employs a multi-head self-attention mecha-

nism, allowing the model to capture key dependencies and relationships within the signal, regardless

of their position in the sequence. This capability enables the model to focus on diﬀerent signal

segments at various time steps, oﬀering a ﬂexible and adaptive approach to interpreting complex,

non-linear interactions. Following self-attention, a feedforward network reﬁnes the learned repre-

sentations by capturing higher-order feature relationships, further enhancing the model’s ability to

detect seizure-related patterns. The overall architecture is depicted in Fig. 4.

3 Post-Processing

3.1 Smoothing

In the post-processing stage of our seizure prediction framework, smoothing the reconstruction error

is a critical step that enhances the robustness and accuracy of predictions. Raw reconstruction error

11

DO

LN

FF

DO

LN

DO

LN

FF

DO

LN

Input EM

T
Enc

T
Enc

Output

Figure 4: Schematic Diagram of Transformer (Enc-Enc). EM is Embedding; T-Enc is Transformer

Encoder; LN is Layer Normalization; DO is Dropout; and FF is Feed-Forward Layer.

values, derived from comparing the model’s output with the original signal, often exhibit signiﬁcant

variability due to noise and transient ﬂuctuations in ECG data. Without adequate smoothing,

these variations could lead to false positives, reducing the predictive accuracy and reliability of the

model.

In order to resolve this, we apply a moving average technique with a ﬁxed window size,

where each point in the smoothed reconstruction error sequence is computed as the mean of its

surrounding values. This reduces noise while retaining signiﬁcant variations associated with seizure
events. Speciﬁcally, the smoothed reconstruction error Esmoothed(i) at index i is given by:

Esmoothed(i) =

1
n

min(N,i+ w
2 )

Xj=max(0,i− w
2 )

E(j),

(10)

where E(j) represents the raw reconstruction error at point j, w is the window size, and N is the
total number of points. This technique eﬀectively reduces short-term variability while preserving the

overall trend of the reconstruction error curve, which is essential for robust anomaly detection. In

order to maintain consistency, we apply smoothing to both the training and testing reconstruction

error sequences.

Importantly, the smoothed error distribution from the training set serves as the

foundation for threshold selection. By leveraging statistical properties of these smoothed errors, we

deﬁne an adaptive threshold for anomaly detection, ensuring that test samples are evaluated against

a stable and noise-ﬁltered baseline.

As a result of this post-processing step, the signal-to-noise ratio of the system is signiﬁcantly im-

proved, resulting in improved reliability and stability during the prediction phase. It helps to mitigate

the risk of false positives caused by transient spikes in error values, ensuring that the model only

ﬂags events that exceed a well-deﬁned and smoothed threshold. By integrating this smoothing pro-

cess, our approach achieves a more balanced performance, critical for real-time seizure prediction

applications.

3.2 Threshold Selection

The statistical thresholding method employed in this study provides a robust and dynamic mechanism

for identifying anomalies by leveraging statistical properties of reconstruction errors. Speciﬁcally, this

12

approach calculates the threshold based on the mean and standard deviation of the reconstruction er-

rors derived from the training dataset. This ensures adaptability to patient-speciﬁc data distributions

and robustness against noise.

The statistical threshold is mathematically deﬁned as follows:

µ =

1
N

N

Xi=1

ETrain(i),

1
N

N

Xi=1

σ = v
u
u
t

(ETrain(i)

µ)2

−

(11)

where µ represents the mean reconstruction error, and σ is the standard deviation of reconstruction
errors in the training data. Accordingly, τ denoted as the threshold is deﬁned as:

τ = µ + kσ

(12)

where k is a tunable parameter that determines the sensitivity of the anomaly detection system. A
higher k reduces false positives by requiring larger deviations to classify an event as anomalous, while
a lower k increases sensitivity but may result in more false positives.

In this study, k was conservatively set to 2, striking a balance between minimizing false positives and
ensuring the detection of meaningful anomalies.

This method oﬀers signiﬁcant advantages:

• The inclusion of the standard deviation ensures the method is resilient to outliers and irregu-

larities in the training data.

• The adjustable k-parameter allows ﬂexibility for diﬀerent application requirements, such as

prioritizing high speciﬁcity or sensitivity.

By employing this statistical thresholding technique, the study ensures that anomalies are detected

eﬀectively, providing a foundation for the development of reliable ECG-based seizure prediction

systems.

4 Performance Evaluation

Accurately assessing a seizure prediction model requires a comprehensive evaluation framework that

ensures reliability, robustness, and clinical viability. This section outlines the key performance metrics

used to quantify predictive accuracy, speciﬁcity, and false alarm rates. Additionally, to account for

seizure rarity, a class weighting mechanism is applied, preventing model bias toward non-seizure

intervals. Another critical aspect is the deﬁnition of the pre-ictal interval, which determines the

valid window for seizure predictions and ensures a fair assessment across diﬀerent datasets. By

incorporating these evaluation strategies, we establish a well-balanced and interpretable performance

analysis.

13

4.1 Evaluation Metrics

In order to fully assess the performance of seizure prediction models, a variety of evaluation metrics

should be used. These metrics are based on four fundamental components of a confusion matrix:

TP These are instances where the model correctly predicted seizures.

FP These are instances where the model incorrectly predicted a seizure.

TN These are the predictions where the model identiﬁed normal behavior correctly, avoiding false

alarms.

FN These are missed seizures, where the model failed to predict the seizure onset.

These components form the basis for key performance metrics such as speciﬁcity, accuracy, and FPR.

Seizure prediction models often face a signiﬁcant class imbalance between seizure intervals (positive

class) and normal intervals (negative class). Since seizures are relatively rare compared to normal

intervals, this imbalance can distort performance metrics. To address this challenge, a weighting

mechanism is employed to adjust the relative importance of each class. Therefore, the weight for the

negative class (normal intervals) is set to 1, while the positive class (seizure intervals) is assigned a

weight inversely proportional to its frequency. This ensures that the model is penalized more heavily

for missing seizures (FN) or falsely predicting seizures (FP), reﬂecting the critical nature of these

errors. Accordingly, the model becomes more sensitive to the minority class, improving its ability to

detect seizures without being overly biased by the abundance of normal intervals.

Another vital aspect of seizure prediction evaluation is deﬁning the pre-ictal interval—the period

preceding a seizure during which predictions are considered valid. This interval determines the

temporal window in which the model’s predictions are analyzed. In this study, the pre-ictal interval

is dynamically adapted based on the length of the dataset, so for a longer dataset, an hour-long

pre-ictal interval is used, while for shorter datasets, a proportionately shorter interval of 30 minutes

(half of the standard interval) is applied. Adjusting the pre-ictal interval dynamically ensures that

evaluation metrics remain clinically meaningful and consistent across datasets of varying durations.

Without this adaptation, models trained on shorter datasets might exhibit artiﬁcially high sensitivity,

while those trained on longer datasets might fail to detect shorter pre-seizure patterns. This approach

oﬀers multiple advantages:

• By adjusting the pre-ictal interval to the length of each record, the evaluation ensures that

longer or shorter records do not skew performance metrics.

• The model is better equipped to handle diverse ECG signal durations, leading to more reliable

predictions across varying scenarios.

As a consequence, in order to maintain consistency in evaluations, pre-ictal intervals must align with

the segmentation window size used in data processing. For instance, if the pre-ictal interval is deﬁned

as 3600 samples with a 1-second segmentation window, it must be reduced to 360 samples when a

14

10-second segmentation window is applied. This adjustment ensures that predictions remain precise

and consistent with the scaled data, preventing inaccuracies caused by mismatched intervals and

segmentation lengths. Allowing the above strategies, various evaluation metrics are computed to

assess the model’s performance:

• Accuracy: Represents the proportion of correct predictions (TP and TN) out of all predictions.

Accuracy =

TP + TN
TP + FP + TN + FN

(13)

• Speciﬁcity: Measures the model’s ability to correctly identify normal activities (non-seizures).

Speciﬁcity =

TN
TN + FP

(14)

• False Positive Rate (FPR): Indicates the proportion of normal activities incorrectly classiﬁed

as seizures, helping to assess the model’s false alarm rate.

FPR =

FP
FP + TN

(15)

5 Experimental Results

In this section, the results obtained through implementation of the proposed approach are presented

and analyzed using the evaluation metrics discussed previously. Based on the fundamental steps

of the proposed method, the results can be examined from three perspectives: the length of signal

segmentation windows, the type of extracted features and representations, and the architecture used

for modeling the seizure prediction process. Accordingly, the following analysis of the results is

conducted with these considerations in mind.

5.1 Seizure Prediction Performance

For a better understanding of the results, it is important to understand how the proposed approach

works and what are the preliminary steps to improve prediction performance.

The proposed approach is designed to predict seizures onset by monitoring and analyzing the recon-

struction loss of ECG signals, which serves as an indicator of abnormal patterns in the data. The

approach involves extracting meaningful features using time-frequency methods and analyzing them

through sequence-to-sequence models. These models are trained to reconstruct ECG signals from

normal, non-seizure segments. During this process, the reconstruction loss indicates how well the

model can predict the original signal based on its learned patterns. Higher reconstruction errors

typically correspond to anomalies, such as those occurring during the pre-ictal phase, which precedes

a seizure. However, as observed in the raw reconstruction error values (Fig. 5), the presence of noise

can lead to false positives, where the model identiﬁes certain points as anomalies, even when they

15

are not indicative of seizure activity. These noise-induced ﬂuctuations complicate the interpretation

of the data and decrease the trustworthiness of the predictions.

(cid:51)(cid:68)(cid:87)(cid:76)(cid:72)(cid:81)(cid:87)(cid:3)(cid:51)(cid:49)(cid:20)(cid:22)
(cid:20)(cid:86)(cid:3)(cid:54)(cid:72)(cid:74)(cid:80)(cid:72)(cid:81)(cid:87)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)(cid:15)(cid:3)(cid:54)(cid:83)(cid:72)(cid:70)(cid:87)(cid:85)(cid:82)(cid:74)(cid:85)(cid:68)(cid:80)(cid:15)(cid:3)(cid:47)(cid:54)(cid:55)(cid:48)(cid:16)(cid:36)(cid:40)(cid:15)(cid:3)(cid:53)(cid:68)(cid:90)(cid:3)(cid:50)(cid:88)(cid:87)(cid:83)(cid:88)(cid:87)

(cid:51)(cid:68)(cid:87)(cid:76)(cid:72)(cid:81)(cid:87)(cid:3)(cid:51)(cid:49)(cid:20)(cid:22)
(cid:20)(cid:86)(cid:3)(cid:54)(cid:72)(cid:74)(cid:80)(cid:72)(cid:81)(cid:87)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)(cid:15)(cid:3)(cid:54)(cid:83)(cid:72)(cid:70)(cid:87)(cid:85)(cid:82)(cid:74)(cid:85)(cid:68)(cid:80)(cid:15)(cid:3)(cid:47)(cid:54)(cid:55)(cid:48)(cid:16)(cid:36)(cid:40)(cid:15)(cid:3)(cid:54)(cid:80)(cid:82)(cid:82)(cid:87)(cid:75)(cid:72)(cid:71)(cid:3)(cid:50)(cid:88)(cid:87)(cid:83)(cid:88)(cid:87)

Figure 5: Comparison of Raw and Smoothed Reconstruction Loss (Patient PN13, 1s segmentation,

Scalogram, LSTM-AE). In the plots, the blue curve represents the reconstruction error, the red

horizontal line indicates the threshold, the red dashed lines mark the seizure onset points, and the

turquoise dash-dotted lines, highlight the pre-ictal period.

This is where the post-processing step becomes critical. During this step, a smoothing technique

is applied to reduce high-frequency noise in order to allow the model to identify more meaningful

anomalies. As shown in the lower part of Fig. 5, after smoothing, the reconstruction error values are

signiﬁcantly more stable, with fewer false anomalies identiﬁed. This improves the model’s ability to

accurately detect the true pre-ictal phase, reducing the number of incorrect predictions and providing

a more reliable prediction method.

In the example shown in Fig. 5, three out of three seizures were correctly predicted. However, it

is important to note that this approach heavily depends on the patient’s ECG signal, and in some

cases, it may fail to accurately predict impending seizures, as demonstrated in Fig. 6. In this case,

the ﬁrst two seizure onsets were successfully predicted, while the third attack was missed.

5.2 Results Based on Segmentation Window Lengths

The length of segmentation windows is crucial in seizure prediction, directly impacting model perfor-

mance and reliability. Longer windows capture richer temporal dynamics, enhancing feature stability

and accuracy but increasing computational cost and response time. Conversely, shorter windows im-

prove eﬃciency but may lack suﬃcient data representation, limiting generalization. This study

analyzed segmentation windows of 1, 5, and 10 seconds with varying overlap levels (none, 1, 3, and

5 seconds).

16

(cid:51)(cid:68)(cid:87)(cid:76)(cid:72)(cid:81)(cid:87)(cid:3)(cid:51)(cid:49)(cid:19)(cid:24)
(cid:20)(cid:86)(cid:3)(cid:54)(cid:72)(cid:74)(cid:80)(cid:72)(cid:81)(cid:87)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)(cid:15)(cid:3)(cid:54)(cid:83)(cid:72)(cid:70)(cid:87)(cid:85)(cid:82)(cid:74)(cid:85)(cid:68)(cid:80)(cid:15)(cid:3)(cid:47)(cid:54)(cid:55)(cid:48)(cid:16)(cid:36)(cid:40)

Figure 6: The Reconstruction Loss of Patient PN05 (Patient PN05, 1s segmentation, Scalogram,

LSTM-AE). In this case, two out of the three seizures were correctly predicted, while the third

attack was missed.

Results showed that a 1-second window without overlap achieved the best results, oﬀering high

accuracy and low variability across patients. This setup eﬀectively balances temporal information

capture with computational eﬃciency. In contrast, the 5-second segmentation window, when used

with partial overlaps (e.g., 1 or 3 seconds), showed moderate performance. Although the overlaps

enhanced temporal continuity, the results were less consistent than with the 1-second window, as

indicated by increased standard deviations. This suggests that while partial overlaps may provide

some advantages in terms of continuous data representation, they also introduce more variability,

leading to reduced robustness in comparison. Finally, the 10-second segmentation windows, whether

used with no overlap or partial overlap, exhibited the lowest performance and highest variability

across patients. This performance drop can be attributed to over-aggregation of data, which may

obscure the short-term patterns critical for accurate seizure prediction.

5.3 Results Based on Extracted Feature Types

The quality and diversity of extracted features are crucial for the success of seizure prediction models.

Transforming input ECG signals into meaningful representations enables better analysis of the under-

lying patterns. In this study, we used three feature extraction methods: Discrete Wavelet Transform

(DWT), Continuous Wavelet Transform (CWT), and Short-Time Fourier Transform (STFT), which

capture time, frequency, and scale-based features which are useful for predicting seizures.

The performance of each feature extraction method was assessed individually for each patient, and

the mean performance across all patients alongside the standard deviation was reported. The stan-

dard deviation provides a comprehensive view of the model’s robustness across diﬀerent patients,

highlighting variability in performance. The results are summarized in Tables 2, 3, and 4.

Table 2: Summarized results from the DWT representation

Models

Speciﬁcity

Accuracy

FPR (/h)

LSTM-AE

98.16 ± 0.009

75.48 ± 0.125

0.018 ± 0.009

MH-C-LSTM-AE 98.13 ± 0.009

75.46 ± 0.125

0.019 ± 0.009

T-EE

98.32 ± 0.01 75.54 ± 0.126 0.017 ± 0.01

17

Table 3: Summarized results from the Scalogram representation

Models

Speciﬁcity

Accuracy

FPR (/h)

LSTM-AE

98.8 ± 0.005

75.67 ± 0.13

0.012 ± 0.005

MH-C-LSTM-AE 98.98 ± 0.006 75.74 ± 0.129 0.01 ± 0.006

T-EE

98.72 ± 0.004

75.62 ± 0.13

0.013 ± 0.004

Table 4: Summarized results from the Spectrogram representation

Models

Speciﬁcity

Accuracy

FPR (/h)

LSTM-AE

98.76 ± 0.008

75.95 ± 0.128

0.011 ± 0.006

MH-C-LSTM-AE 99.16 ± 0.006 76.05 ± 0.127 0.01 ± 0.005

T-EE

98.76 ± 0.008

75.62 ± 0.126

0.016 ± 0.009

Analysis shows that the STFT-derived spectrogram slightly outperforms other methods, suggesting

that frequency-domain information oﬀers more discriminative features for seizure prediction. How-

ever, as illustrated in Fig. 7, scalogram and spectrogram, displayed similar trends, indicating that

pre-seizure anomalies occurred at consistent intervals. These points could potentially aid in early

seizure detection, though further clinical validation is needed.

In conclusion, while all feature extraction methods show potential, the STFT-based spectrogram

oﬀers the most promising results for seizure prediction, guiding future research in selecting the most

eﬀective techniques.

5.4 Results Based on Designed Models

In the ﬁnal step, architectures play a crucial role in transforming the extracted features into actionable

predictions. In this study, a wide range of neural network architectures were employed, including

feedforward networks, convolutional networks, recurrent networks, autoencoders, and transformer

models. The results of these models are presented cumulatively in Table 5.

Table 5: Final Results

Models

Speciﬁcity

Accuracy

FPR (/h)

LSTM-AE

98.76 ± 0.008

75.95 ± 0.128

0.011 ± 0.006

MH-C-LSTM-AE 99.16 ± 0.006 76.05 ± 0.127 0.01 ± 0.005

T-EE

98.76 ± 0.008

75.62 ± 0.126

0.016 ± 0.009

Based on the data shown in Table 5, it is evident that among the proposed architectures, the MH-

C-LSTM-AE model achieved the highest performance, successfully predicting 45 out of 47 seizures

with speciﬁcity of 99.16%, accuracy of 76.05%, and FPR of 0.01/h. Following closely, the T-EE

model also demonstrated high performance, predicting 44 seizures, and ﬁnally, the LSTM-AE model

18

(cid:51)(cid:68)(cid:87)(cid:76)(cid:72)(cid:81)(cid:87)(cid:3)(cid:51)(cid:49)(cid:19)(cid:24)
(cid:20)(cid:86)(cid:3)(cid:54)(cid:72)(cid:74)(cid:80)(cid:72)(cid:81)(cid:87)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)(cid:15)(cid:3)(cid:39)(cid:58)(cid:55)(cid:3)(cid:38)(cid:82)(cid:72)(cid:73)(cid:73)(cid:76)(cid:70)(cid:76)(cid:72)(cid:81)(cid:87)(cid:86)(cid:15)(cid:3)(cid:47)(cid:54)(cid:55)(cid:48)(cid:16)(cid:36)(cid:40)

(cid:51)(cid:68)(cid:87)(cid:76)(cid:72)(cid:81)(cid:87)(cid:3)(cid:51)(cid:49)(cid:19)(cid:24)
(cid:20)(cid:86)(cid:3)(cid:54)(cid:72)(cid:74)(cid:80)(cid:72)(cid:81)(cid:87)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)(cid:15)(cid:3)(cid:54)(cid:70)(cid:68)(cid:79)(cid:82)(cid:74)(cid:85)(cid:68)(cid:80)(cid:15)(cid:3)(cid:47)(cid:54)(cid:55)(cid:48)(cid:16)(cid:36)(cid:40)

(cid:51)(cid:68)(cid:87)(cid:76)(cid:72)(cid:81)(cid:87)(cid:3)(cid:51)(cid:49)(cid:19)(cid:24)
(cid:20)(cid:86)(cid:3)(cid:54)(cid:72)(cid:74)(cid:80)(cid:72)(cid:81)(cid:87)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)(cid:15)(cid:3)(cid:54)(cid:83)(cid:72)(cid:70)(cid:87)(cid:85)(cid:82)(cid:74)(cid:85)(cid:68)(cid:80)(cid:15)(cid:3)(cid:47)(cid:54)(cid:55)(cid:48)(cid:16)(cid:36)(cid:40)

Figure 7: Results of reconstruction loss for seizure prediction (Patient PN05, 1s segmentation, LSTM-

AE). The ﬁrst plot shows the reconstruction loss using combined coeﬃcients from the DWT, the

second plot displays results from the scalogram representation derived from the CWT, and the ﬁnal

plot presents the reconstruction loss based on the spectrogram representation from the STFT.

predicted 43 seizures. Additionally, it can be observed that all three models were able to predict

seizures approximately 40 minutes in advance, indicating their potential for early seizure prediction.

6 Comparison with Previous Studies

Seizure prediction using ECG signals has been extensively explored in biological signal processing

and machine learning. This section brieﬂy reviews related studies and compares their results with

the proposed approach.

In prior work, Billeci et al. [30] applied a classiﬁcation-based approach to the Siena Database, report-

ing an accuracy of 88.86%, speciﬁcity of 89.32%, and FPR of 0.41/h. While these results represent

an advancement over earlier eﬀorts, the reliance on linear features and conventional classiﬁcation

methods may limit the ability to capture the non-linear dynamics presented in pre-seizure patterns,

potentially hindering seizure prediction performance in real-world settings.

As previously mentioned, the proposed method builds upon the work of Ode et al. [18], who utilized

19

an attention-based autoencoder (SA-AE) model for seizure prediction based on RR interval (RRI)

features. However, given the unavailability of their original dataset, we decided to ensure a fair and di-

rect comparison by re-implementing their methodology using the publicly accessible Siena database.

In our re-implementation, we trained the SA-AE model on RRI features, achieving speciﬁcity of

93.85%, accuracy of 67.13%, and FPR of 0.067/h, with a prediction time of 1 minute. This allowed

us to validate their approach under consistent and controlled conditions. Despite these results, the

exclusive reliance on RRI features may not fully capture the intricate pre-seizure dynamics, which

are critical for accurate seizure prediction. Furthermore, the relatively high FPR observed in this

model poses signiﬁcant challenges for clinical applicability, as false alarms can lead to alarm fatigue

and reduced trust in automated systems. In order to overcome these limitations, we explored the

potential beneﬁts of incorporating our proposed time-frequency features into the model. By training

the re-implemented SA-AE model with these enhanced features, we observed notable improvements

in speciﬁcity and accuracy. These ﬁndings suggest that time-frequency representations oﬀer a more

comprehensive view of the underlying ECG patterns, capturing temporal and frequency-domain in-

formation that RRI features alone may miss. However, despite these improvements, the performance

of the time-frequency enhanced model still did not match the robustness of our proposed MH-C-

LSTM-AE model. This diﬀerence could be attributed to diﬀerences in model architecture, extracted

feature representations, and the level of optimization during the training process, which all inﬂuence

the ﬁnal performance.

Compared to Ode et al. [18], as shown in Table 6, the proposed method achieves substantially lower

FPR, enhancing its reliability for clinical applications. By addressing these limitations, the proposed

framework improves prediction while ensuring a better balance between accuracy and real-world

applicability.

Table 6: Comparison with previous studies.

Previous Studies

Dataset

Speciﬁcity Accuracy

FPR

Predicted

(/h)

Time (Min)

Billeci et al. [30]

Ode et al. [18]

DWT Coeﬃcients

SA-AE

Scalogram

Spectrogram

LSTM-AE

MH-C-LSTM-AE

T-EE

Proposed

Methods

Siena

Database

Siena

Database

Siena

Database

Siena

Database

89.34 % 88.86 % 0.41

13.7

93.85 %

67.13 % 0.067

98.05 %

75.38 % 0.019

91.94 %

74.09 % 0.081

95.73 %

74.51 % 0.043

98.76 %

75.95 % 0.011

99.16 % 76.05 % 0.010

98.76 %

75.62 % 0.016

1

10

21

22

43

45

44

20

7 Discussion

Seizure prediction remains a critical challenge in neurology, with signiﬁcant implications for patient

safety and quality of life. The ﬁndings of this study provide strong evidence for the eﬀectiveness of an

ECG-based anomaly detection framework for seizure prediction, with high accuracy and temporal

sensitivity. The framework, grounded in time-frequency domain feature extraction and advanced

sequence modeling coupled with reconstruction error analysis, enables the proposed approach to not

only detect seizures accurately but also provide a dynamic, patient-speciﬁc solution using adaptive

statistical thresholds. This is critical for real-world clinical applications, where individual variability

in ECG signals often challenges the use of universal thresholds.

One of the critical elements contributing to the model’s success was the smoothing of reconstruction

errors using moving average ﬁltering. This step was pivotal in enhancing the reliability of the model

by eﬀectively reducing transient ﬂuctuations often inherent in ECG signals. By reducing these ﬂuc-

tuations, the model is able to maintain accuracy while decreasing false alarms, which is essential for

clinical systems. Furthermore, the use of an adaptive statistical thresholding method, derived from

the training set’s distribution parameters, enables the creation of patient-speciﬁc decision boundaries.

This method accounts for inter-patient variability in physiological signals, ensuring that the model

can eﬀectively adapt to the individual characteristics of each patient. Next, the choice of segmenta-

tion window length also played a crucial role in model performance. In particular, a 1-second window

without overlap provided superior results, striking a balance between temporal granularity and com-

putational eﬃciency. This setup allowed the model to capture ﬁne-grained temporal features, which

are essential for detecting the pre-ictal state. Longer windows, conversely, resulted in decreased

performance, due to over-smoothing and the loss of temporal resolution, which is critical for identi-

fying early pathological changes. The feature extraction methodology also inﬂuenced the system’s

accuracy. Among the methods evaluated, STFT demonstrated the highest discriminative capability,

highlighting the importance of frequency-domain features in identifying pre-seizure ECG patterns.

However, the relatively slight performance margin between STFT, CWT, and DWT suggests that

a multi-representation ensemble could be a promising avenue for future research. Combining these

techniques may enhance the model’s ability to detect diverse pre-seizure signatures, potentially im-

proving prediction accuracy. Finally, among the investigated models, the MH-C-LSTM-AE model

achieved the best performance. It successfully identiﬁed 45 out of 47 seizures, exhibiting high speci-

ﬁcity and FPR of only 0.01/h. The architecture’s ability to integrate temporal dependencies (via

LSTM layers), spatial hierarchies (via convolutional layers), and contextual attention (via multi-

head attention) was crucial for capturing the complex ECG dynamics associated with seizure onset.

Notably, the approach predicted seizure onset with an average prediction time of approximately 40

minutes, suggesting its potential for real-time, anticipatory intervention in clinical settings.

However, despite these successes, the model’s sensitivity to inter-individual variability remains a limi-

tation. This is a well-known challenge in biological signal-based prediction systems, where variability

in individual data can impact the consistency and generalizability of predictions. This highlights the

21

need for patient-speciﬁc calibration or the incorporation of transfer learning strategies in future iter-

ations. Additionally, while the system demonstrated promising results during retrospective analysis,

its true potential will only be fully realized through prospective real-time deployment in clinical en-

vironments, which will help assess its robustness under actual clinical constraints. Furthermore, the

methodology proposed in this study has signiﬁcant potential for broader clinical applications. Given

the reliance on ECG signals and reconstruction error-based anomaly detection, the framework could

be adapted for the early detection or ongoing monitoring of various cardiovascular and neurological

conditions. For example, this system could be adapted for arrhythmia classiﬁcation [31], sleep apnea

detection [32], and other cardiovascular or neurological conditions, with minimal modiﬁcations due

to their similar temporal patterns in ECG and related signals.

8 Conclusion

In this study, we developed a comprehensive framework for seizure prediction using ECG signals.

Through careful selection of time-frequency representations and the design of robust deep learning

architectures, we identiﬁed key factors—such as a 1-second time-window, low-pass ﬁltering, and

Fourier-based spectrograms—that contributed to the best performance. However, challenges such as

limited patient-speciﬁc data and the inability to accurately identify seizure phases pose signiﬁcant

barriers to improving both the accuracy and generalizability of the model. Moving forward, future

research should focus on reﬁning the framework to improve accuracy, particularly in scenarios with

limited data.

22

References

[1] Linda Dalic and Mark J Cook. Managing drug-resistant epilepsy: challenges and solutions.

Neuropsychiatric disease and treatment, pages 2605–2616, 2016.

[2] Robert S Fisher, Carlos Acevedo, Alexis Arzimanoglou, Alicia Bogacz, J Helen Cross, Chris-

tian E Elger, Jerome Engel Jr, Lars Forsgren, Jacqueline A French, Mike Glynn, et al. Ilae

oﬃcial report: a practical clinical deﬁnition of epilepsy. Epilepsia, 55(4):475–482, 2014.

[3] Hanneke M De Boer, Marco Mula, and Josemir W Sander. The global burden and stigma of

epilepsy. Epilepsy & behavior, 12(4):540–546, 2008.

[4] Claire Ufongene, Rima El Atrache, Tobias Loddenkemper, and Christian Meisel. Electrocar-

diographic changes associated with epilepsy beyond heart rate and their utilization in future

seizure detection and forecasting methods. Clinical Neurophysiology, 131(4):866–879, 2020.

[5] B Jaishankar, AM Ashwini, D Vidyabharathi, and L Raja. A novel epilepsy seizure prediction

model using deep learning and classiﬁcation. Healthcare Analytics, 4:100222, 2023.

[6] Nazanin Mohammadkhani Ghiasvand and Foad Ghaderi. Epileptic seizure prediction from spec-

tral, temporal, and spatial features of eeg signals using deep learning algorithms. The Neuro-

science Journal of Shefaye Khatam, 9(1):110–119, 2020.

[7] Raﬀaele Manni, Gianpaolo Toscano, and Michele Terzaghi. Epilepsy and cardiovascular function:

Seizures and antiepileptic drugs eﬀects. Brain and heart dynamics, pages 507–515, 2020.

[8] Mohammad Reza Chopannavaz and Foad Ghaderi. Advances in machine learning for epileptic

seizure prediction: A review of ecg-based approaches. Preprints, April 2025.

[9] Federico Mason, Anna Scarabello, Lisa Taruﬃ, Elena Pasini, Giovanna Calandra-Buonaura,

Luca Vignatelli, and Francesca Bisulli. Heart rate variability as a tool for seizure prediction: a

scoping review. Journal of clinical medicine, 13(3):747, 2024.

[10] M-Z Poh, T Loddenkemper, C Reinsberger, NC Swenson, S Goyal, JR Madsen, and Rosalind W

Picard. Autonomic changes with seizures correlate with postictal eeg suppression. Neurology,

78(23):1868–1876, 2012.

[11] Maeike Zijlmans, Danny Flanagan, and Jean Gotman. Heart rate changes and ecg abnormalities

during epileptic seizures: prevalence and deﬁnition of an objective clinical sign. Epilepsia, 43

(8):847–854, 2002.

[12] Hirotsugu Hashimoto, Koichi Fujiwara, Yoko Suzuki, Miho Miyajima, Toshitaka Yamakawa,

Manabu Kano, Taketoshi Maehara, Katsuya Ohta, Tetsuo Sasano, Masato Matsuura, and Eisuke

Matsushima. Epileptic seizure monitoring by using multivariate statistical process control. IFAC

Proceedings Volumes, 46(31):249–254, 2013.

23

[13] Hirotsugu Hashimoto, Koichi Fujiwara, Yoko Suzuki, Miho Miyajima, Toshitaka Yamakawa,

Manabu Kano, Taketoshi Maehara, Katsuya Ohta, Tetsuo Sasano, Masato Matsuura, et al.

Heart rate variability features for epilepsy seizure prediction. In 2013 Asia-Paciﬁc Signal and

Information Processing Association Annual Summit and Conference, pages 1–4. IEEE, 2013.

[14] Koichi Fujiwara, Erika Abe, Yoko Suzuki, Miho Miyajima, Toshitaka Yamakawa, Manabu Kano,

Taketoshi Maehara, Katsuya Ohta, and Tetsuo Sasano. Epileptic seizure monitoring by one-class

support vector machine. In Signal and Information Processing Association Annual Summit and

Conference (APSIPA), 2014 Asia-Paciﬁc, pages 1–4. IEEE, 2014.

[15] Soroor Behbahani, Nader Jafarnia Dabanloo, Ali Motie Nasrabadi, and Antonio Dourado. Pre-

diction of epileptic seizures based on heart rate variability. Technology and Health Care, 24(6):

795–810, 2016.

[16] Laura Gagliano, E Bou Assi, Dènahin Hinnoutondji Toﬀa, Dang Khoa Nguyen, and Mohamad

Sawan. Unsupervised clustering of hrv features reveals preictal changes in human epilepsy. In

2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology

Society (EMBC), pages 698–701. IEEE, 2020.

[17] Adriana Leal, Mauro F. Pinto, Fábio Lopes, Anna M. Bianchi, Jorge Henriques, Maria G.

Ruano, Paulo de Carvalho, António Dourado, and César A. Teixeira. Heart rate variability

analysis for the identiﬁcation of the preictal interval in patients with drug-resistant epilepsy.

Scientiﬁc Reports, 11(1):5987, 2021.

[18] Rikumo Ode, Koichi Fujiwara, Miho Miyajima, Toshikata Yamakawa, Manabu Kano, Kazutaka

Jin, Nobukazu Nakasato, Yasuko Sawai, Toru Hoshida, Masaki Iwasaki, Yoshiko Murata, Satsuki

Watanabe, Yutaka Watanabe, Yoko Suzuki, Motoki Inaji, Naoto Kunii, Satoru Oshino, Hui Ming

Khoo, Haruhiko Kishima, and Taketoshi Maehara. Development of an epileptic seizure prediction

algorithm using r-r intervals with self-attentive autoencoder. Artiﬁcial Life and Robotics, pages

1–7, 2022.

[19] Paolo Detti. Siena scalp eeg database. PhysioNet, 10:493, 2020.

[20] Paolo Detti, Giampaolo Vatti, and Garazi Zabalo Manrique de Lara. Eeg synchronization

analysis for seizure prediction: A study on data of noninvasive recordings. Processes, 8(7):846,

2020.

[21] Ary L. Goldberger, Luis an Amaral, Leon Glass, Jeﬀrey M. Hausdorﬀ, Plamen Ch Ivanov,

Roger G. Mark, Joseph E. Mietus, George B. Moody, Chung-Kang Peng, and H. Eugene Stanley.

Physiobank, physiotoolkit, and physionet: Components of a new research resource for complex

physiologic signals. circulation, 101(23):e215–e220, 2000.

[22] Kiran Kumar Patro and P Rajesh Kumar. A novel frequency-time based approach for the detec-

tion of characteristic waves in electrocardiogram signal. In Microelectronics, Electromagnetics

and Telecommunications: Proceedings of ICMEET 2015, pages 57–67. Springer, 2016.

24

[23] Akkachai Phuphanin, Metha Tasakorn, and Jeerapong Srivichai. Electrocardiogram signal pro-

cessing algorithm on microcontroller using wavelet transform method. International Journal of

Electrical & Computer Engineering (2088-8708), 14(2), 2024.

[24] Amir Hatamian, Farzad Farshidi, Changiz Ghobadi, Javad Nourinia, and Ehsan Mostafapour.

Improving the quality of ecg signal using wavelet transform and adaptive ﬁlters. Journal of

Applied Research in Electrical Engineering, 2(1):45–53, 2023.

[25] MJ Burke and M Nasor. Wavelet based analysis and characterization of the ecg signal. Journal

of Medical Engineering & Technology, 28(2):47–55, 2004.

[26] Jingshan Huang, Binqiang Chen, Bin Yao, and Wangpeng He. Ecg arrhythmia classiﬁcation

using stft-based spectrogram and convolutional neural network. IEEE access, 7:92871–92880,

2019.

[27] Andrea V Perez-Sanchez, Carlos A Perez-Ramirez, Martin Valtierra-Rodriguez, Aurelio

Dominguez-Gonzalez, and Juan P Amezquita-Sanchez. Wavelet transform-statistical time

features-based methodology for epileptic seizure prediction using electrocardiogram signals.

Mathematics, 8(12):2125, 2020.

[28] Andrea V Perez-Sanchez, Juan P Amezquita-Sanchez, Martin Valtierra-Rodriguez, and Hojjat

Adeli. A new epileptic seizure prediction model based on maximal overlap discrete wavelet

packet transform, homogeneity index, and machine learning using ecg signals. Biomedical Signal

Processing and Control, 88:105659, 2024.

[29] Mikel Canizo, Isaac Triguero, Angel Conde, and Enrique Onieva. Multi-head cnn–rnn for multi-

time series anomaly detection: An industrial case study. Neurocomputing, 363:246–260, 2019.

[30] Lucia Billeci, Daniela Marino, Laura Insana, Giampaolo Vatti, and Maurizio Varanini. Patient-

Speciﬁc Seizure Prediction Based on Heart Rate Variability and Recurrence Quantiﬁcation Anal-

ysis. PLOS ONE, 13(9):e0204339, 2018.

[31] Ameet Shah, Dhanpratap Singh, Heba G Mohamed, Salil Bharany, Ateeq Ur Rehman, and

Seada Hussen. Electrocardiogram analysis for cardiac arrhythmia classiﬁcation and prediction

through self attention based auto encoder. Scientiﬁc Reports, 15(1):9230, 2025.

[32] Yongrui Chen, Yurui Zheng, Adam Worrall, Sam Johnson, Richard Wiﬀen, and Bin Yang.

Detecting sleep anomalies from spo2 data using autoencoder-based neural networks. Biomedical

Engineering Advances, page 100150, 2025.

25
