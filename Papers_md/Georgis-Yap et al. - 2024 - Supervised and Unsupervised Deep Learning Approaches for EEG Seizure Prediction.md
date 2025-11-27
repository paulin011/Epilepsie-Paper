
Journal of Healthcare Informatics Research (2024) 8:286–312
https://doi.org/10.1007/s41666-024-00160-x
RESEARCH ARTICLE
Supervised and Unsupervised Deep Learning Approaches
for EEG Seizure Prediction
Zakary Georgis-Yap
1,2
·Milos R. Popovic
1,2
·Shehroz S. Khan
1,2
Received: 24 April 2023 / Revised: 4 January 2024 / Accepted: 18 January 2024 /
Published online: 16 February 2024
© The Author(s), under exclusive licence to Springer Nature Switzerland AG 2024
Abstract
Epilepsy affects more than50million people worldwide, making it one of the world’s
most prevalent neurological diseases. The main symptom of epilepsy is seizures,
which occur abruptly and can cause serious injury or death. The ability to predict
the occurrence of an epileptic seizure could alleviate many risks and stresses people
with epilepsy face. We formulate the problem of detecting preictal (or pre-seizure) with
reference to normal EEG as a precursor to incoming seizure. To this end, we developed
several supervised deep learning approaches model to identify preictal EEG from nor-
mal EEG. We further develop novel unsupervised deep learning approaches to train the
models on only normal EEG, and detecting pre-seizure EEG as an anomalous event.
These deep learning models were trained and evaluated on two large EEG seizure
datasets in a person-specific manner. We found that both supervised and unsupervised
approaches are feasible; however, their performance varies depending on the patient,
approach and architecture. This new line of research has the potential to develop
therapeutic interventions and save human lives.
KeywordsDeep learning·Intracranial EEG·Seizure prediction·Signal processing
Zakary Georgis-Yap and Shehroz S. Khan contributed equally to this work
B
Shehroz S. Khan
shehroz.khan@uhn.ca
Zakary Georgis-Yap
ztcgy11@gmail.com
Milos R. Popovic
milos.popovic@uhn.ca
1
KITE Research Institute, Toronto Rehabilitation Institute - University Health Network, 550,
University Avenue, Toronto M5G 2A2, Ontario, Canada
2
Institute of Biomedical Engineering, University of Toronto, 64 College St., Toronto M5S 3G9,
Ontario, Canada
123
Journal of Healthcare Informatics Research (2024) 8:286–312287
1 Introduction
Epilepsy is one of the most prevalent neurological disorders in the world, affecting
approximately 1% of the world’s population [1–3]. Epilepsy is characterized by spon-
taneously occurring seizures, which could lead to bodily injuries, fractures, burns [4],
and death in many cases [5]. People with epilepsy are mostly concerned with the fear
of incoming seizures [6]. Therefore, there is a dire need to reduce the unpredictability
of seizures to reduce the risk of injuries and improve their quality of life.
Electroencephalography (EEG) is normally used to analyze brain activity pertain-
ing to seizures [7]. Brain activity in people with epilepsy can be separated into four
states: regular brain activity (interictal), brain activity before the seizure (preictal),
brain activity during the seizure (ictal), and brain activity immediately after a seizure
(postictal). The preictal state can contain observable physiological changes prior to
the onset of a seizure [8] that can be used to predict an incoming seizure. The capa-
bility to predict an epileptic seizure could alleviate the risks patients face [9]; it would
give patients the time to get help and greatly reduce the risk of injury. However, the
biggest challenge is designing seizure prediction approaches is that there is no univer-
sally agreed upon preictal period length (PPL). Bandarabadi et al. [10] investigated
the optimal PPL for seizure prediction using statistical analysis and found that the
optimal PPL varies for each patient and for seizure within each patient [10].
Most of the work in this area is around seizure detection [11], which involves
detecting a seizure after its occurrence. Although this is important, contemporary
work must aim to predict seizures before their onset, as it can save patients’ lives and
improvetheirqualityoflife.Ourmainhypothesisisthatthecorrectdetectionofpreictal
state against normal brain activity (through supervised or unsupervised approaches)
can be a strong indicator of an incoming epileptic seizure. In the supervised setting,
a binary classifier can be trained between interictal and preictal periods. Whereas, in
the unsupervised setting, a classifier can be trained on only normal EEG (interictal)
and preictal state can be identified as an anomaly. Our main contributions are:
•Presented supervised and new unsupervised deep learning approaches to predict
epileptic seizures.
•Experimentally determined the PPL and window size, as against heuristics or
domain knowledge.
•Performed leave-one-seizure-out cross-validation for better generalization of
results.
•All the experiments were performed in a patient-specific manner to avoid data
leakages, overestimation of results and emphasis on individualized outcomes.
Our results showed that the unsupervised approaches were able to obtain comparable
results to supervised seizure prediction in many patients. However, across all imple-
mentations there was not one clear best performing model. This paper is an extension
of our preliminary work [12] that introduced supervised convolution neural network
(CNN) on SWEC-ETHZ dataset [13]. In this paper, we present two new supervised
approaches: CNN-Long Short Term Memory (LSTM) and Temporal Convolution
Network (TCN), and three new unsupervised approaches (CNN, CNN-LSTM, TCN
123
288Journal of Healthcare Informatics Research (2024) 8:286–312
autoencoders). We developed new seizure prediction baselines for the SWEC-ETHZ
dataset [13] and included a new CHB-MIT dataset [14].
2 Related Work
Seizure prediction using supervised machine learning has been used to distinguish the
interictal and preictal states [15]. Typical supervised machine learning seizure pre-
diction approaches involve signal pre-processing, extracting and selecting features,
followed by a classifier [15]. Common signal processing techniques include high-pass,
low-pass, or band-pass filtering, as well as artifact removal techniques [15]. Feature
extraction is typically done by a bio-signals or epilepsy expert examining a patient’s
EEG and deciding appropriate features for separating the preictal and interictal states
[15]. These features are often patient-specific and include statistical, non-linear, fre-
quency domain, and time-frequency domain features [15,16]. Common classifier
choices include support vector machines (SVM), k-nearest neighbor and random for-
est [15].
Machine learning approaches may have limitations in terms of extracting hand-
crafted features, which could be suboptimal and time-consuming. Deep learning
approaches can overcome some of these challenges by able to learn features from
data with little to no pre-processing, generate high-level representations of data, and
learn complex functions [17]. However, deep learning approaches need vast amount
of data and computing resources to train and deploy the models, which can be time-
consuming and costly. Also, it requires a careful tuning of the hyperparameters to avoid
overfitting and under fitting. An overview of preictal-interictal classification seizure
prediction methods (on human subjects) using deep learning is shown in Table1.
Many reviewed deep learning methods performed some type of pre-processing the
EEG data before passing it on to the classifier, typically through filtering [1,21],
artifact removal [35], or time-frequency analysis [21,22]. Common deep learning
architectures used for seizure prediction include CNN [1,22], LSTM network [29,
32], and feed-forward multilayer perceptron (MLP) [18]. We observed that a majority
of the studies use CNNs, LSTMS and/or their combinations to benefit from learning
spatial and temporal features. The window size (fixed duration of data to analyze)
and PPL were kept fixed in most of the studies, and they varied even when working
on the same dataset and patients. This is an issue in building classifiers to predict
seizures because the optimal PPL varies across patients (as concluded by Bandarabadi
et al. [10]). Only four of the studies reported experimenting with the PPL [18,21,
29,35], while others did not present any rationale for their choices. Some of the
studies (e.g., [14]) also found different PPLs sizes, showing that the optimal PPL
varies depending on the method’s implementation. These studies show that it is better
to determine the PPL empirically at a patient-specific level, rather than using a generic
or pre-determined average over a population.
We extend the existing supervised methods by obtaining PPL and window size using
a leave-one-seizure-out (LOSO) evaluation and introduced a new supervised TCN
123
Journal of Healthcare Informatics Research (2024) 8:286–312289
Table 1
Overview of deep learning EEG seizure prediction methods
Citation
Window Size
PPL
Pre-processing
DL Architecture
(seconds)
(minutes)
Teixeira et al. [
18
]
5
10, 20, 30, 40
Various fixed features
MLP
Feietal.[
19
]
10
Unknown
Fractional FT
MLP
Mirowski et al. [
20
]
300
50
Handcrafted
CNN
Khan et al. [
21
]110CWTCNN
Truong et al. [
22
]3060STFTCNN
Eberlein et al. [
23
]
15
60
None
CNN
Zhang et al. [
24
]
5
30
Common spatial pattern
CNN
Liu et al. [
25
]
30
60
Fast FT
Multi-view CNN
Dissanayake et al. [
26
]
10
60
MFCC
CNN
Jana and Mukherjee [
27
]
1, 2, 3, 8
10
None
CNN
Georgis-Yap et al. [
12
]
5, 10, 15, 30, 60
30, 60, 120
STFT
CNN
Xu et al. [
28
]
20
30, 60
None
CNN
Tsiouris et al. [
29
]
5
15
Handcrafted
LSTM
Shahbazi and Aghajan [
1
]
10
30
STFT
CNN + LSTM
Abdelhameed and Bayoumi [
30
]
4
60
None
CNN-AE+BiLSTM
Daoud and Bayoumi [
31
]
5
60
None
MLP,CNN,CNN+LSTM
Weietal.[
32
]
10
30
Image conversion
CNN+LSTM
Usman et al. [
33
]
30
60
STFT
CNN+SVM
Hussein et al. [
34
]
30
30
None
1DCNN+GRU
Prathaban and Balasubramanian [
35
]
Unknown
60
Image conversion
3DCNN
Ozcan and Erturk [
36
]
4
30
Various fixed features
3DCNN
Truong et al. [
37
]
28
30
STFT
Convolutional GAN
123
290Journal of Healthcare Informatics Research (2024) 8:286–312
classifier for this task. Unsupervised deep learning approach has been used by Daoud et
al. [31]; in conjunction with classification approach to predict epileptic seizures. They
trained a deep autoencoder on unlabelled EEG segments (balanced data of preictal
and interictal segments) and replace the trained autoencoder in their classification
pipeline. Their intent to use autoencoder is to leverage the transfer learning abilities
of the model by allowing the training process to have a good start point instead of
random initialization of the parameters, which reduces the training time drastically.
We introduced three different autoencoder models in a total unsupervised manner
and separate from the classification approaches and studied their performance for this
problem.
3 Supervised Seizure Prediction
Preictal-interictal classification for seizure prediction is performed with three different
architectures: convolutional neural networks (CNN) (used in our previous work [12]),
and two new architectures, i.e., CNN-LSTM), and TCN. We briefly discuss them
below.
3.1 CNN
The CNN model takes in EEG samples that have been time-frequency transformed
usingaSTFT[22] (see Sect.5.3). This helps the model in extracting time and frequency
features and puts the data into a suitable format for 2D convolutions [22]. The CNN
architecture takes advantage of spatial information in data to learn relevant features.
Each sample was converted into a 2D matrixF×Tusing a STFT, whereFwas the
number of sample frequencies used andTwas the number of segment times used.
The matrix was then resized to a 128×128 “image” using bilinear interpolation so
that image sizes were consistent regardless of the window size. The time-frequency
transform was done independently for each channel, resulting in each sample being
of dimensionsC×128×128, whereCis the total number of channels. The samples
were then passed to the CNN model, which is made up of three convolutional blocks
(see Fig.1a and b), followed by three fully connected layers with ReLU activation
functions. Table2shows the model hyperparameters used for the CNN.
3.2 CNN-LSTM
The CNN-LSTM architecture takes advantage of both the spatial feature extraction
of the CNN along with the LSTM’s propensity to work well with temporal data. The
CNN-LSTM model takes in STFT images similar to the CNN model. The input is a
consecutive series of images as one sample. The input sequence is divided into smaller
sub-sequences, which are independently time-frequency transformed and resized into
64×64 images, leading to dimensionsC×n×64×64, wherenis the number of sub-
sequences in a sample and is equal to the sequence length divided by the sub-sequence
length. Each sub-window is passed into a CNN model with two convolutional blocks
123
Journal of Healthcare Informatics Research (2024) 8:286–312291
(a)
(a)
(b)
(b)
Fig. 1(a) Convolutional block, (b) CNN architecture with convolution blocks and fully connected (FC)
layers
that outputs a feature vector. Then, each feature vector is concatenated into a sequence
and passed into a 2-layer LSTM, whose outputs are passed to a fully connected layer
that outputs the final scores. An overview of the CNN-LSTM architecture and hyper-
parameters are shown in Fig.2and Table3. We did experiments with LSTM on raw
EEG data; however, the results were not satisfactory and not discussed in the paper.
Converting the EEG to STFT highlighted the frequencies and enabled CNN to learn
spatial information, while the LSTM was able to model the temporal dependencies
between there. The RNNs were not used because LSTM supports longer memory and
better handling of vanishing gradient problem [38]. On the flip side, LSTMs generally
require more parameters to train, making it computationally expensive and memory
intensive. We resolved this issue by training LSTM models on a high-performance
computation GPU cluster (see Sect.6).
Table 2CNN model
hyperparameters
CNN kernel size5
CNN filter sizes8, 16, 32
Fully connected sizes128, 64
Dropout0.5
123
292Journal of Healthcare Informatics Research (2024) 8:286–312
Fig. 2CNN-LSTM architecture showing time-frequency (TF) transform, CNN layers, LSTM and fully
connected (FC) layer
3.3 TCN
The TCN model takes in scaled sequences of sizeC×S/4, whereSis the sequence
length and the sequences were down-sampled by a factor of 4. The TCN model [39]
consisted of TCN blocks (see Fig.3). Each TCN block is two consecutive sub-blocks
that contain a causal 1D convolution layer with a dilation, a weight normalization
layer, a ReLU activation function, and a dropout layer [39]. The TCN blocks have
skip connections, where the input to the block is added to the output [39]. The model
contained 6 TCN blocks with 32 channels each, followed by a 1D convolution layer,
and a fully connected layer. The dilation factor of each block was 2
(n−1)
, wherenis the
layer number. Figure3and Table4shows the TCN architecture and hyperparameters.
123
Journal of Healthcare Informatics Research (2024) 8:286–312293
Table 3Hyperparameters of
CNN-LSTM model
CNN kernel size5
CNN filter sizes8, 16
LSTM feature vector size32
LSTM hidden size16
Fully connected size96
Dropout0.5
(a)(b)
Fig. 3(a) TCN block description. TCN: temporal convolutional network. ReLU: rectified linear unit. (b)
Supervised TCN architecture overview. TCN: temporal convolutional network. FC layer: fully connected
layer
Table 4Hyperparameters of
TCN model
TCN kernel size5
TCN filter sizes32, 32, 32, 32, 32, 32
Fully connected size64
Dropout0.2
123
294Journal of Healthcare Informatics Research (2024) 8:286–312
4 Unsupervised Seizure Prediction
The reliance on preictal data for supervised seizure prediction methods remains a
challenge. Preictal data is typically scarce, and deep learning methods require a consid-
erable amount of data from both classes to work well. Preictal-interictal classification
methods cannot be used effectively on patients with little preictal data, and class
imbalance still remains an impending problem. An unsupervised approach (anomaly
detection) to seizure prediction could remedy these problems. Anomaly detection for
seizure prediction would require only interictal (and no preictal data) to train, making
it easier to be more accessible to a larger population. Autoencoders (AEs) and its
variants are apt to be used within this framework, with reconstruction error used as an
anomaly score [40]. To our knowledge, this is one of the first seizure prediction work
that uses unsupervised deep learning approach for epileptic seizure prediction without
utilizing preictal data. We implemented the following autoencoder approaches for this
task.
•CNN autoencoder [41]. Similar to the supervised CNN, it takes STFT images as
input. The encoder is made up of three convolutional blocks followed by a fully
connected layer which generates an embedding state of size 64. The decoder is a
mirrored version of the encoder (see Fig.4a).
•CNN-LSTM autoencoder [42]. Similar to the supervised CNN-LSTM, the input
sequence was divided into smaller sub-sequences and then an STFT was performed
on each sub-sequence. The encoder consisted of an individual CNN encoder for
each sub-sequence, followed by an LSTM that generated an embedding state of
size 64. The decoder has the reverse architecture to the encoder (see Fig.4b).
•TCN autoencoder [43]. It takes in raw scaled sequences, as is the case with the
supervised TCN. The encoder was a TCN with three layers, each with 16 channels
followedbya1dconvolutionandafullyconnectedlayer.Thesizeoftheembedding
state was 64. The decoder was an exact mirror of the encoder (see Fig.4c).
5 Data Processing
5.1 Datasets
We used two EEG Epilepsy seizure datasets, the Sleep-Wake Epilepsy Centre ETH
Zurich (SWEC-ETHZ) dataset [13] and the Children’s Hospital Boston Massachusetts
Institute of Technology (CHB-MIT) dataset [14]. Both datasets are publicly available,
easy to access, and contain human raw EEG recordings, where no seizure states have
been pre-selected. This is important so we can define and experiment with different
preictal and interictal regions. The SWEC-ETHZ dataset is an iEEG dataset containing
over 2500 h of recordings across 18 patients with a sampling rate of either 512Hz or
1024Hz [13]. The CHB-MIT dataset contains scalp EEG recordings from 22 patients
sampled at 256Hz with at least 22 EEG electrodes [14]. Note that one patient had
their recordings taken on two separate occasions 1.5 years apart, and the two cases are
treated as two separate patients for the rest of this paper [14].
123
Journal of Healthcare Informatics Research (2024) 8:286–312295
Fig. 4Autoencoders comprising
of (a) Convolution layers only,
(b)CNN-LSTM, and (c) TCN
(a)
(b)
(c)
123
296Journal of Healthcare Informatics Research (2024) 8:286–312
We define a “lead seizure” as any seizure that occurs at least 30 min after a preceding
seizure [22]. Only preictal periods from lead seizures were considered because of the
lack of interictal and preictal data to train models. Patients that have less than three lead
seizures were withheld from the experiments because at least three lead seizures were
required to perform test partitioning combined with an internal leave-one-seizure-out
(LOSO) cross-validation step (see Fig.5b). Six out of the 18 patients in the SWEC-
ETHZ dataset were not considered for this work due to this condition. All patients
in the CHB-MIT dataset had at least three lead seizures. A description of dataset
attributes for all patients used from both the SWEC-ETHZ and CHB-MIT datasets is
shown in Tables5and6, respectively.
5.2 Data Pre-processing
The length and location of the preictal period is defined by the PPL and the intervention
time (IT). The IT is the time between the preictal state and the seizure onset. Interictal
data is defined as any data that is not preictal, ictal, and postictal, and isddistance
away from the preictal state, as shown in Fig.5a. The data was divided into samples
of a fixed window size, which were labelled as either interictal or preictal. We set
d=0 to evaluate the model’s ability to classify interictal and preictal samples in
close temporal proximity to actual seizures. The IT was set to 0, increasing it can be a
future experiment after generating a baseline. In the SWEC-ETHZ dataset, interictal
samples were randomly selected with a down-sampling factor of 8 because interictal
data were overly abundant, and the classes were significantly imbalanced (patients
ID04, ID09, and ID10 used a down-sampling factor of 2 instead because there was
less interictal data). The number of preictal samples was artificially increased by
using 50% overlapping windows. The size of each sample wassf×Cwhereswas
the window size,fwas the sampling rate, andCwas the number of EEG electrodes.
The dataset was partitioned into a training set and a testing set using LOSO par-
titioning. We used the last lead seizure’s preictal data as the test set, while all other
preictal data was part of the training set. As shown in Fig.5b, LOSO partitioning is a
(a)
(b)
Fig. 5(a) Labelling of the preictal and interictal periods with parameters. (b) Simplified visualization of
LOSO test partitioning by withholding the last seizure
123
Journal of Healthcare Informatics Research (2024) 8:286–312297
Table 5SWEC-ETHZ dataset patient description [13]
Patient IDHours of dataSeizuresLead seizuresElectrodes
ID031584464
ID0441141432
ID0511044128
ID061468832
ID07694475
ID081444461
ID0941231448
ID1042171532
ID121919956
ID131047764
ID161775534
ID182055542
Table 6CHB-MIT dataset patient description [14]
Patient IDHours of dataSeizuresLead seizuresElectrodes
141 77 22
235 33 22
338 77 22
41564322
539 55 22
667 107 22
767 33 22
820 55 22
968 43 22
10507722
11353322
1224401122
133312722
14268622
1540201422
161910522
17213322
18366522
19303322
20288622
21334422
22313322
23277322
123
298Journal of Healthcare Informatics Research (2024) 8:286–312
better way to evaluate a model’s ability to generalize to a new seizure’s preictal data.
Standard test partitioning where samples are randomly assigned to the training or test
set may be an overestimation of the actual performance of the classifier.
5.3 Time-Frequency Transform
We transformed the EEG data from a time-series input into the time-frequency domain
[44,45] using short-time Fourier transform (STFT). It converts a one-dimensional
time-series signal into a two-dimensional matrix of values with axes of time and
frequency [46]. The STFT splits the signal into a series of smaller sequences and
then performing Fourier transforms on each one individually, providing a way to see
changes in the frequency domain at various points in time [47]. In this work, the
sequence is split into segments of 128 samples before performing Fourier transforms.
In CNN-based models used in the work, an STFT was used to pre-process the input
before passing samples to the model. Other time-frequency analysis methods such
as the continuous wavelet transform [21] and phase-amplitude coupling [48]were
experimented with in our preliminary work but did not provide better results.
6 Experimental Setting and Results
A grid search was performed to find the optimal window size and PPL for each
patient. We ran the model with varying window size (5, 10, 15, 30, 60 s) and PPL
(30,60,120 min) values. We used an internal LOSO cross-validation to tune the
parameters without looking at test data. This was done by dividing the training set into
folds, where each fold was a different seizure’s preictal and interictal data. One fold
was the validation set, while the others were used for training. Each fold in the set
was used as the validation set once, and the performance across all runs in a patient
was averaged. An example of the cross-validation method used is shown in Fig.6.
The area under the Receiver Operating Characteristic curve (AUC ROC) [49]was
Fig. 6LOSO cross-validation example with four seizures. One seizure is used for validation, while the
others are used for model training
123
Journal of Healthcare Informatics Research (2024) 8:286–312299
used as a performance metric for hyperparameter tuning. The test set was completely
withheld from this process. All the models were trained using an NVIDIA V100S-
PCIe GPU with 32 GB memory. A class-weighted (class weights vary per patient)
cross-entropy loss function was used with the Adam optimizer and was trained for
100 epochs with a batch size of 128 and a learning rate of 0.0001. All implementations
were done in the PyTorch framework [50]. After the final parameters for a model were
set, it was evaluated on the test set using the AUC ROC and precision-recall curve
(AUC PR). AUC PR is more appropriate for imbalanced classification problems [51].
The reported performance metrics are AUC ROC and AUC PR. The calculation of
false positive, false negative and derived metrics, such as accuracy, specificity, and
sensitivity, depends on the choice of the threshold applied to the reconstruction error
or classification probabilities [21,31]. ROC and PR analysis is more thorough since
it does not depend on the threshold choice, and instead analyzes the specificities
and sensitivities at all possible thresholds and provides an overall summary metric in
terms of AUC ROC/AUC PR. For imbalanced datasets, AUC PR is a better metric as
it takes care of precision and recall at all thresholds and does not inflate the results.
Another important point to note is that in unsupervised deep learning models, there is
no validation set; therefore, calculating an operating threshold is non-trivial.
6.1 Supervised Prediction
Hyperparameter tuning results using the supervised CNN are shown in Tables7and
8for the SWEC-ETHZ and CHB-MIT datasets, respectively. The window size and
PPL obtained using cross-validations as well as AUC ROC vary considerably across
different patients in both datasets. More than half of the patients in each dataset show
AUC ROC values greater than 0.7. In the SWEC-ETHZ dataset, six of the patients
had a test AUC ROC at least 0.1 lower than their validation AUC ROC, while in the
CHB-MIT dataset it was eight patients. This is consistent with Bandarabadi et al. [10]
that the optimal preictal period for seizure prediction varies even on seizures within
the same patient. The best way to account for this problem is to train and test on as
many lead seizures’ preictal data as possible.
6.1.1 Comparison with Fixed Parameters
We implemented a preictal-interictal classification model with a fixed window size
of 30 s and PPL of 1 h to compare to our tuned hyperparameter model. The CNN
model architecture is identical to the optimized parameter implementation. This was
done to explore the benefits of optimizing hyperparameters for seizure prediction.
Figures7and8shows the comparison of the two methods on the SWEC-ETHZ and
CHB-MIT dataset. In general, for the SWEC-ETHZ dataset, the optimized hyperpa-
rameter implementation performed slightly better than the fixed parameter. In patient
ID09, the optimized hyperparameter implementation performed much better than the
fixed parameter implementation. For patient ID09, the hyperparameter tuning found
a window size of 30 s and a PPL of 2 h. It is likely that there was additional preictal
information in the extra hour of data not used in the fixed parameter implementation.
123
300Journal of Healthcare Informatics Research (2024) 8:286–312
Table 7Validation and test results for preictal-interictal classification with optimized hyperparameters on
the SWEC-ETHZ dataset
Patient ID Window Size PPL (seconds) Validation AUC ROC Test AUC ROC Test AUC PR
ID033018000.7930.9390.681
ID046036000.7080.5090.610
ID056072000.9530.9180.863
ID066072000.7040.9480.842
ID073072000.7220.7130.745
ID081572000.7220.4540.452
ID093072000.9010.9440.982
ID106036000.8070.5740.790
ID126018000.9810.7980.544
ID136018000.7210.4990.394
ID161018000.7190.4230.160
ID181518000.8320.8500.401
The bold numbers mean better than average models
Table 8Validation and test results for preictal-interictal classification with optimized hyperparameters on
the CHB-MIT dataset
Patient ID Window Size PPL (seconds) Validation AUC ROC Test AUC ROC Test AUC PR
16018000.9870.9970.991
2572000.7180.9820.869
31018000.8531.0001.000
4572000.3760.6490.037
5536000.8210.8280.555
61036000.6160.8580.796
7572000.7440.1330.113
81018000.9990.3790.378
91072000.7890.7880.471
10518000.7320.6860.185
113036000.8900.9780.803
126072000.9170.5490.974
13536000.9730.8980.394
14518000.8170.1390.151
153072000.8240.4700.806
166018000.6860.6880.294
17572000.9330.5650.221
186018000.7500.8200.100
193072001.0000.9660.930
20518000.9830.8980.497
21572000.8070.7210.200
22572000.7700.3970.059
233018001.0000.6140.662
The bold numbers mean better than average models
123
Journal of Healthcare Informatics Research (2024) 8:286–312301
Fig. 7AUC ROC Comparison of CNN models using optimized hyperparameters vs fixed hyperparameters
on the SWEC-ETHZ dataset
For the CHB-MIT dataset, most patients had similar results for both the fixed and
optimized hyperparameter implementations. There were a few patients (ID 5, 16, 17,
18) that had much better results with the optimized model. However, there were also
patients (ID 9, 22, 23) who performed better with a fixed hyperparameter implementa-
tion. For these patients, the last seizure’s optimal hyperparameters were likely different
from the optimal hyperparameters for the preceding seizures in the patient’s dataset.
Figures9and10show the comparison between the optimized and fixed hyperparame-
ter implementations for the SWEC-ETHZ and CHB-MIT datasets respectively using
Fig. 8AUC ROC Comparison of CNN models using optimized hyperparameters vs fixed hyperparameters
on the CHB-MIT dataset
123
302Journal of Healthcare Informatics Research (2024) 8:286–312
Fig. 9AUC PR Comparison of CNN models using optimized hyperparameters vs fixed hyperparameters
on the SWEC-ETHZ dataset
AUC PR instead. It can be observed that the optimized implementation generally per-
forms better on the SWEC-ETHZ dataset in both metrics, and that the difference is
marginal in the CHB-MIT dataset. These experiments indicate that hyperparameter
tuning can potentially improve the performance in comparison to fixed parameters.
6.1.2 Comparison with Other Architectures
Using a fixed hyperparameter implementation, CNN-LSTM and TCN models were
trained using a window size of 30 s and a PPL of 1 h. A comparison of the AUC PR
Fig. 10AUC PR Comparison of CNN models using optimized hyperparameters vs fixed hyperparameters
on the CHB-MIT dataset
123
Journal of Healthcare Informatics Research (2024) 8:286–312303
Fig. 11Comparison of CNN, CNN-LSTM, and TCN implementations for preictal-interictal classification
on the SWEC-ETHZ dataset
for all models is shown in Figs.11and12. In the SWEC-ETHZ dataset, the CNN,
CNN-LSTM and TCN were the best performing model for 3, 5 and 4 patients. The
CNN and CNN-LSTM performed comparably well, and in each patient, the results
were fairly similar. The TCN results were more variable, performing well on some
patients, while the other models performed poorly. In the CHB-MIT dataset, the CNN,
CNN-LSTM and TCN were the best performing model for 7, 6 and 10 patients. The
TCN model performed much better in the CHB-MIT dataset compared to the SWEC-
ETHZ dataset. Overall, the CHB-MIT results were very variable with AUC PR values,
varying considerably even within the same patient.
Fig. 12Comparison of CNN, CNN-LSTM, and TCN implementations for preictal-interictal classification
on the CHB-MIT dataset
123
304Journal of Healthcare Informatics Research (2024) 8:286–312
6.2 Unsupervised Prediction
In the unsupervised approach, the training set only contained interictal data. For these
experiments, the hyperparameters were fixed, with a window size of 30 s and a PPL
of 60 min. The models were trained for 500 epochs with a batch size of 128 and a
learning rate of 0.0005. After training, the models were evaluated on the test set that
contained both interictal and preictal samples. Both AUC ROC and AUC PR were
used to evaluate performance.
6.2.1 Comparison of Architectures
Figures13and14a and b show the anomaly detection-based seizure prediction AUC
PR results for the CNN, CNN-LSTM, and TCN AEs on the SWEC-ETHZ dataset
and CHB-MIT dataset, respectively. We also show the supervised CNN with fixed
hyperparameters for comparison. It can be observed that the performance varies sig-
nificantly across different architectures and patients. For the SWEC-ETHZ dataset, the
CNN AE performed the worst across most patients while the CNN-LSTM and TCN
AEs performed relatively better, and even surpassed the supervised implementation
in some patients. In the CHB-MIT dataset, the results vary even more, with no clear
winner.
6.3 Best Implementations
Tables9and10show the best performing implementation (from all experiments with
supervised and unsupervised approaches) for each patient in the SWEC-ETHZ and
CHB-MIT datasets and its corresponding AUC ROC and AUC PR. For SWEC-ETHZ
dataset, an unsupervised approach was the best performing implementation for 7 out of
12 patients. For the CHB-MIT dataset, for 16 out of 23 patients, supervised approaches
Fig. 13Comparison of unsupervised seizure prediction using different model architectures on the SWEC-
ETHZ dataset. U: unsupervised, S: supervised
123
Journal of Healthcare Informatics Research (2024) 8:286–312305
(a)
(b)
Fig. 14Comparison of unsupervised seizure prediction using different model architectures on the CHB-
MIT dataset (a) patients 1 to 11, (b) patients 12 to 23. U: unsupervised, S: supervised
performed better. In particular, the supervised CNN performed the best for 8 patients
— the most of any model. Figure15shows that using the CNN-LSTM was the most
effective for the most patients, with the best performance in 16 of the 35 patients.
123
306Journal of Healthcare Informatics Research (2024) 8:286–312
Table 9Best performing implementation for each patient in the SWEC-ETHZ dataset
Patient IDBest ImplementationAUC PRAUC ROC
ID03Supervised CNN0.7350.930
ID04Unsupervised CNN-LSTM0.7270.427
ID05Unsupervised CNN-LSTM0.9910.995
ID06Supervised CNN-LSTM0.5370.756
ID07Supervised CNN-LSTM0.7260.787
ID08Unsupervised TCN0.5010.778
ID09Unsupervised CNN-LSTM0.9180.734
ID10Unsupervised TCN0.9550.808
ID12Unsupervised CNN0.8170.910
ID13Supervised TCN0.5730.496
ID16Unsupervised CNN0.4300.737
ID18Supervised CNN0.7020.837
Table 10Best performing implementation for each patient in the CHB-MIT dataset
Patient IDBest ImplementationAUC PRROC AUC
1Supervised CNN0.9660.988
2Supervised CNN0.7370.968
3Supervised CNN1.0001.000
4Supervised TCN0.0640.751
5Unsupervised CNN-LSTM0.6120.891
6Supervised CNN0.8780.925
7Unsupervised CNN-LSTM0.1150.526
8Supervised TCN0.7040.773
9Supervised CNN0.6600.947
10Supervised CNN-LSTM0.7330.922
11Supervised CNN0.8780.989
12Unsupervised TCN0.9280.743
13Supervised CNN0.9790.994
14Supervised TCN0.7420.824
15Unsupervised CNN-LSTM0.7200.526
16Unsupervised CNN-LSTM0.3190.764
17Unsupervised CNN-LSTM0.4140.808
18Supervised CNN-LSTM0.1040.822
19Supervised CNN-LSTM0.7330.964
20Supervised CNN-LSTM0.7060.924
21Supervised CNN-LSTM0.4770.868
22Unsupervised CNN-LSTM0.3080.909
23Supervised TCN0.9530.975
123
Journal of Healthcare Informatics Research (2024) 8:286–312307
Fig. 15Number of times the best performing model was of each architecture type (CNN, CNN-LSTM,
TCN)
6.4 Discussion
We found that it is important to tune the window size and PPL to maximize per-
formance. Preictal-interictal classification performed slightly better in both datasets
when using an optimized hyperparameter implementation. However, in the CHB-
MIT dataset, this difference was marginal. This is likely because of the size of the
dataset. The CHB-MIT dataset has fewer data per patient compared to the SWEC-
ETHZ dataset, so it is harder to properly tune hyperparameters that will generalize to
new seizures. The CNN and CNN-LSTM architectures performed similarly in most
experiments. This is likely because both use time-frequency transforms followed by
two-dimensional convolutions for spatial feature extraction. Even though the archi-
tectures are not exactly the same, it is likely that both are capturing similar underlying
patterns in the data. The TCN performed fairly well and was able to get good results in
some patients when the other two models failed. Although there was not one consis-
tently high-performing model, it is encouraging that different architectures were able
to perform well for different patients in different datasets.
The prediction results vary considerably across datasets, patients, and implementa-
tions. This demonstrates the variable nature of preictal and interictal data. To account
for this, it is important to have as many lead seizures data in a patient as possible, since
preictal data is typically scarce. A limitation of our work is that a patient requires three
lead seizures in their data to work with this method. It may not always be feasible for a
patient’s data to have at least three lead seizures, especially considering the difficulty
of data acquisition.
Anomaly detection seizure prediction performance varied significantly across dif-
ferent architectures. Although supervised preictal-interictal classification performed
better overall, there were many patients where an unsupervised approach was the best
implementation. Additionally, in the SWEC-ETHZ dataset, an unsupervised approach
123
308Journal of Healthcare Informatics Research (2024) 8:286–312
was the best implementation for the majority of patients. This is likely because the
SWEC-ETHZ dataset had a much larger recording duration and interictal-preictal
ratio. In autoencoder-based unsupervised approaches, the model is trained on only
interictal (or normal) EEG data and reconstruction error is used to detect the onset of
seizures (or preictal events). If the interictal data is interfered with noise, it means that
the reconstruction error may be higher even for the interictal training data, which could
result in misidentifying pre-seizures (that may also have higher reconstruction error
because they were not seen before). Alternatively, if the interictal data is not diverse
enough, then a slight variation in test interictal data could lead to misclassifying it
as pre-seizure, which may lead to higher false alarms rate. Nevertheless, anomaly
detection seizure prediction shows promise, and it implies that with improved signal
processing and predictive modelling it may not be necessary to collect substantial
preictal data to predict a seizure.
Figure16shows the average performance in terms of AUC PR across all patients. It
can be observed that the supervised CNN and the supervised CNN-LSTM performed
the best on average. However, the difference in performance across models is not
large, and with a large standard deviation, it is impossible to make a statistical claim
on the best performing model. In general, it can be observed that the supervised
approaches performed better than the unsupervised approaches with results varying
across individual patients. Our results also showed the potential of using unsupervised
approaches for seizure prediction. A major advantage is that it only uses unlabelled
interictal EEG data, which is easier to acquire and is not dependent on an expert to
annotate.
Fig. 16Average performance of each implementation. S: supervised. U: unsupervised
123
Journal of Healthcare Informatics Research (2024) 8:286–312309
7 Conclusions and Future Directions
We developed several supervised approaches and introduced new unsupervised deep
learning approaches for predicting epileptic seizures. In each approach, the main goal
was to identify a preictal state (either as a binary class or anomaly) to predict the onset
of an incoming seizure. We accounted for the variability of EEG and the preictal period
by tuning the window size and PPL using a grid search. We trained personalized models
and tuned hyperparameter using LOSO approach for better generalization of results.
This method has achieved good results on more than half of the patients. We experi-
mented with different supervised and unsupervised deep learning architectures on two
large EEG datasets. Our results vary across different implementations depending on
the patient. The advantage of unsupervised methods is that they do not require preic-
tal data to train the models; thus, alleviating the challenges around data acquisition,
and effort and time spent in labelling. However, due to the absence of validation set
in unsupervised approaches (anomaly detection), it is non-trivial to obtain a thresh-
old to detect pre-seizure events. Previous work on creating proxy outliers from the
normal data can be extended to obtain an operating threshold for predicting seizures
[52,53]. We found that in many cases, an unsupervised approach was able to get
similar or even better performance than a supervised approach; however, there was no
single best performing model. Our extensive experiments show the feasibility of super-
vised and unsupervised deep learning approaches for seizure prediction. However, the
amount of preictal data per patient appears to be a crucial factor in training generalized
models.
A future extension would be to experiment with a larger range for the hyper-
parameters. These parameters can also vary across implementations, so optimized
hyperparameter implementations with the CNN-LSTM or TCN architecture as the
base could be valuable. Another direction is to obtain (person-specific) operating
threshold for deployment of these algorithms in a real-world setting. However, there
are several limiting factors, including data imbalance, and unequal (and potentially
unknown) costs of false positive and false negative in this application. These costs must
be informed by clinical practices and guidelines as it pertains to human life. Generative
adversarial networks [54] and autoencoders trained in adversarial manner [55] can be
another potential unsupervised deep learning approach to predict epileptic seizures.
Another extension would be to try different signal processing methods and advanced
CNN and sequential models, including Resnet and Transformers. A breakthrough in
reducing intervention time before the onset of seizure would lead to development of
therapeutic interventions that can empower epilepsy patients to live without the fear
or adversarial outcomes.
Author ContributionsZakary Georgis-Yap and Shehroz S. Khan contributed equally in terms of developing
algorithms,evaluationofresultsandmanuscriptpreparation.ShehrozS.Khanpreparedsubsequentrevisions
of the paper. Milos R. Popovic provided academic support and consultation throughout the study.
FundingThis work is supported by the Natural Sciences and Engineering Research Council of Canada and
Data Science Institute, University of Toronto.
Availability of Data and MaterialsThe datasets used in the paper are publicly available.
123
310Journal of Healthcare Informatics Research (2024) 8:286–312
Declarations
Ethics ApprovalTwo publicly available datasets were used in this work; therefore, ethics approvals were
not required to use them.
Informed ConsentAll the co-authors give their consent to publish this paper.
Conflict of InterestThe authors declare no competing interests.
References
1. Shahbazi M, Aghajan H (2018) A generalizable model for seizure prediction based on deep learning
using cnn-lstm architecture. In: 2018 IEEE Global conference on signal and information processing
(GlobalSIP), Anaheim, USA
2. Beghi E, Giussani G (2018) Aging and the epidemiology of epilepsy. Neuroepidemiology 51:216–223
3. Litt B, Echauz J (2002) Prediction of epileptic seizures. Neurology 1:22–30
4. Nguyen R, T’ellez Zenteno JF (2009) Injuries in epilepsy: a review of its prevalence, risk factors, type
of injuries and prevention. Neurol Int 1
5. Ridsdale L, Charlton J, Ashworth M, Richardson MP, Gulliford MC (2011) Epilepsy mortality and
risk factors for death in epilepsy: a population-based study. Br J Gen Pract 61:271–278
6. Fisher RS (2000) Epilepsy from the patient’s perspective: Review of results of a community-based
survey. Epilepsy Behav 1:9–14
7. Kuhlmann L, Lehnertz K, Richardson MP, Schelter B, Zaveri HP (2018) Seizure prediction — ready
for a new era. Nat Rev Neurol 14:618–630
8. Stacey W, Le Van Quyen M, Mormann F, Schulze-Bonhage A (2011) What is the present-day eeg
evidence for a preictal state? Epilepsy Res 97:243–251
9. Brinkamann BH, Wagenaar J, Abbot D, Adkins P, Bosshard SC, Chen M, Tieng QM, He J, Muñoz-
Almaraz FJ, Botella-Rocamora P, Pardo J, Zamora-Martinez F, Hills M, Wu W, Korshunova I, Cukierski
W, Vite C, Patterson EE, Litt B, Worrel GA (2016) Crowdsourcing reproducible seizure forecasting in
human and canine epilepsy. Brain 139:1713–1722
10. Bandarabadi M, Rasekhi J, Teixeira CA, Karami MR, Dourado A (2015) On the proper selection of
preictal period for seizure prediction. Epilepsy Behav 158–166:46
11. Giannakakis G, Sakkalis V, Pediaditis M, Tsiknakis M (2014) Methods for seizure detection and
prediction: An overview. Mod Electroencephalographic Assem Tech 91:131–157
12. Georgis-Yap Z, Popovic MR, Khan SS (2022) Preictal-interictal classification for seizure prediction.
In: The 35th Canadian conference on artificial intelligence
13. Burrello A, Cavigelli L, Schindler K, Benini L, Rahimi A (2019) Laelaps: An energy-efficient seizure
detection algorithm from long-term human ieeg recordings without false alarms. In: 2019 Design,
automation & test in Europe conference & exhibition (DATE). Florence, Italy
14. Shoeb AH (2009) Application of machine learning to epileptic seizure onset detection and treatment.
PhD thesis, Massachusetts Institute of Technology
15. Acharya UR, Hagiwara Y, Adeli H (2018) Automated seizure prediction. Epilepsy Behav 88:251–261
16. Natu M, Bachute M, Gite S, Kotecha K, Vidyarthi A (2022) Review on epileptic seizure prediction:
machine learning and deep learning approaches. Comput Math Methods Med 2022
17. LeCun Y, Bengio Y, Hinton G (2015) Deep learning. Nature 521:436–444
18. Teixeira CA, Direito B, Bandarabadi M, Le Van Quyen M, Valerrama M, Schelter B, Schulze-Bonhage
A, Navarro V, Sales F, Dourado A (2014) Epileptic seizure predictors based on computational intelli-
gence techniques: A comparative study with 278 patients. Comput Methods Prog Biomed 114:324–336
19. Fei K, Wang W, Yang Q, Tang S (2017) Chaos feature study in fractional fourier domain for preictal
prediction of epileptic seizure. Neurocomputing 249:290–298
20. Mirowski P, Madhavan D, LeCun Y, Kuzniecky R (2009) Classification of patterns of eeg synchro-
nization for seizure prediction. Clin Neurophysiol 120:1927–1940
21. Khan H, Marcuse L, Fields M, Swann K, Yener B (2018) Focal onset seizure prediction using convo-
lutional networks. IEEE Trans Biomed Eng 65:2109–2118
123
Journal of Healthcare Informatics Research (2024) 8:286–312311
22. Truong ND, Nguyen AD, Kuhlmann L, Bonyadi MR, Yang J, Ippolito S, Kavehei O (2018) Con-
volutional neural networks for seizure prediction using intracranial and scalp electroencephalogram.
Neural Netw 105:104–111
23. Eberlein M, Hildebrand R, Tetzlaff R, Hoffmann N, Kuhlmann L, Brinkmann B, M”uller J (2018)
Convolutional neural networks for epileptic seizure prediction. In: 2018 IEEE International conference
on bioinformatics and biomedicine (BIBM), Madrid
24. Zhang Y, Guo Y, Yang P, Chen W, Lo B (2020) Epilepsy seizure prediction on eeg using common
spatial pattern and convolutional neural network. IEEE J Biomed Health Informat 24:465–474
25. Liu Y, Sivathamboo S, Goodin P, Bonnington P, Kwan P, Kuhlmann L, O’Brien T, Perucca P, Ge Z
(2020) Epileptic seizure detection using convolutional neural network: A multi-biosignal study. In:
ACSW ’20: Proceedings of the Australasian computer science week multiconference, Melbourne,
Australia
26. Dissanayake T, Fernando T, Denman S, Sridharan S, Fookes C (2021) Deep learning for patient-
independent epileptic seizure prediction using scalp eeg signals. IEEE Sensors J 21:9377–9388
27. Jana R, Mukherjee I (2021) Deep learning based efficient epileptic seizure prediction with eeg channel
optimization. Biomed Signal Process Control 68
28. Xu Y, Yang J, Zhao S, Wu H, Sawan M (2020) An end-to-end deep learning approach for epileptic
seizure prediction. In: 2020 2nd IEEE International conference on artificial intelligence circuits and
systems (AICAS), Italy
29. Tsiouris KM, Pezoulas VC, Zervakis M, Konitsiotis S, Koutsouris DD, Fotiadis DI (2018) A long
short-term memory deep learning network for the prediction of epileptic seizures using eeg signals.
Comput Biol Med 99:24–37
30. Abdelhameed AM, Bayoumi M (2018) Semi-supervised deep learning system for epileptic seizures
onset prediction. In: 2018 17th IEEE International conference on machine learning and applications
(ICMLA), Orlando
31. Daoud H, Bayoumi MA (2019) Efficient epileptic seizure prediction based on deep learning. IEEE
Trans Biomed Circ Syst 13:804–813
32. Wei X, Zhou L, Zhang Z, Chen Z, Zhou Y (2019) Early prediction of epileptic seizures using a long-term
recurrent convolutional network. J Neurosci Methods 327
33. Usman SM, Khalid S, Aslam MH (2020) Epileptic seizures prediction using deep learning techniques.
IEEE Access 8:39998–40007
34. Hussein A, Djandji M, Mahmoud R, Dhaybi M, Hajj HM (2020) Augmenting dl with adversarial
training for robust prediction of epilepsy seizures. J ACM 1
35. Prathaban BP, Balasubramanian R (2021) Dynamic learning framework for epileptic seizure prediction
using sparsity based eeg reconstruction with optimized cnn classifier. Expert Syst Appl 170
36. Ozcan AR, Erturk S (2019) Seizure prediction in scalp eeg using 3d convolutional neural networks
with an image-based approach. IEEE Trans Neural Syst Rehab Eng 27:2284–2293
37. Truong ND, Zhou L, Kavehei O (2019) Semi-supervised seizure prediction with generative adversarial
networks. In: 2019 41st Annual international conference of the ieee engineering in medicine and
biology society (EMBC), Berlin
38. Sherstinsky A (2020) Fundamentals of recurrent neural network (rnn) and long short-term memory
(lstm) network. Physic D Nonlinear Phenom 404:132306
39. Thill M, Konen W, Wang H, B”ack T, (2021) Temporal convolutional autoencoder for unsupervised
anomaly detection in time series. Appl Soft Comput 112:107751
40. Stefan Denkovski SSK, Mihailidis A (2023) Temporal shift - multi-objective loss function for improved
anomaly fall detection. In: 15
th
Asian conference on machine learning
41. Khan SS, Khoshbakhtian F, Ashraf AB (2021) Anomaly detection approach to identify early cases in
a pandemic using chest x-rays. In: Canadian conference on AI
42. Jacob Nogas SSK, Mihailidis A (2018) Fall detection from thermal camera using convolutional lstm
autoencoder. In: Proceedings of the 2nd workshop on aging, rehabilitation and independent assisted
living, IJCAI workshop
43. Abedi A, Khan SS (2023) Detecting disengagement in virtual learning as an anomaly using temporal
convolutional network autoencoder. SIViP
44. Al-Fahoum AS, Al-Fraihat AA (2014) Methods of eeg signal features extraction using linear analysis
in frequency and time-frequency domains. Int Scholar Res Not 2014
45. Herrmann CS, Rach S, Vosskuhl J, Str”uber D (2014) Time–frequency analysis of event-related poten-
tials: A brief tutorial. Brain Topogr 27:438–450
123
312Journal of Healthcare Informatics Research (2024) 8:286–312
46. Herrmann CS, Rach S, Vosskuhl J, Str”uber D (2014) Time–frequency analysis of event-related poten-
tials: A brief tutorial. Brain Topogr 27:438–450
47. Fadzal CWNFCW, Mansor W, Khuan LY, Zabidi A (2012) Short-time fourier transform analysis of
eeg signal from writing. In: 2012 IEEE 8th International colloquium on signal processing and its
applications. Malacca, Malaysia
48. Edakawa K, Yanagisawa T, Kishima H, Fukuma R, Oshino S, Khoo HM, Kobayashi M, Tanaka M,
Yoshimine T (2016) Detection of epileptic seizures using phase–amplitude coupling in intracranial
electroencephalography. Sci Rep 6(1):1–8
49. Huang J, Ling CX (2005) Using auc and accuracy in evaluating learning algorithms. IEEE Trans Knowl
Data Eng 17:299–310
50. Paszke A, Gross S, Massa F, Lerer A, Bradbury J, Chanan G, Killeen T, Lin Z, Gimelshein N, Antiga
L, Desmaison A, Kopf A, Yang E, DeVito Z, Raison M, Tajani A, Chilamkurthy S, Steiner B, Fang
L, Bai J, Chintala S (2019) Pytorch: An imperative style, high-performance deep learning library. In:
Advances in neural information processing systems 32, Vancouver
51. Branco P, Torgo L, Ribeiro RR (2016) A survey of predictive modeling on imbalanced domains. ACM
Comput Surv (CSUR) 49:1–50
52. Khan SS, Karg ME, Kuli ́c D, Hoey J (2017) Detecting falls with x-factor hidden markov models. Appl
Soft Comput 55:168–177
53. Khan SS, Mishra PK, Ye B, Newman K, Iaboni A, Mihailidis A (2023) Empirical thresholding on
spatio-temporal autoencoders trained on surveillance videos in a dementia care unit. In: 2023 20th
Conference on robots and vision (CRV), pp 265–272. IEEE
54. Habashi AG, Azab AM, Eldawlatly S, Aly GM (2023) Generative adversarial networks in eeg analysis:
an overview. J NeuroEng Rehab 20(1):40
55. Khan SS, Nogas J, Mihailidis A (2021) Spatio-temporal adversarial learning for detecting unseen falls.
Pattern Anal Applic 24:381–391
Publisher’s NoteSpringer Nature remains neutral with regard to jurisdictional claims in published maps
and institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under
a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted
manuscriptversionofthisarticleissolelygovernedbythetermsofsuchpublishingagreementandapplicable
law.
123