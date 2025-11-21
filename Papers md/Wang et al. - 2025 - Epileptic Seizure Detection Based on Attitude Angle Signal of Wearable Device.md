# Wang et al. - 2025 - Epileptic Seizure Detection Based on Attitude Angle Signal of Wearable Device

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025

2505010

Epileptic Seizure Detection Based on Attitude
Angle Signal of Wearable Device

Jiabing Wang , Dinghan Hu , Member, IEEE, Xiaoping Lai

, Tao Jiang , Tiejia Jiang ,

Feng Gao , Pierre-Paul Vidal

, and Jiuwen Cao , Senior Member, IEEE

Abstract— Wearable wristband device-based epilepsy detection
has the merits of noninvasiveness, portability,
low costs, and
good environmental adaptability. However, attention has been
paid to exploring the attitude angle signals collected by wearable
devices for epilepsy detection. In this article, a systematic analysis
of whether the wearable device-based attitude angle signals,
particularly the PITCH and ROLL angles, can be applied to
epilepsy seizure detection, is studied. The relationship among
attitude angle signals, acceleration, and angular velocity signals
at the feature level is analyzed, and the detection effectiveness of
combining different attitude angle features for classifier training
and testing is presented and discussed. The long-term recorded
data were collected by wearable devices from 28 epileptic
patients, of which 11 were from the Fourth Affiliated Hospital
of Anhui Medical University and 17 from the Department of
Neurology, Children’s Hospital, Zhejiang University School of
Medicine. Each recording includes the measurement of three-axis
acceleration (ACC), three-axis gyroscope (GYR), ROLL, PITCH,
surface electromyography (SEMG), and electrodermal activity
(EDA), with at least one seizure recorded for each subject.
Experimental results show that ROLL and PITCH angles can be
utilized for epilepsy detection, with better performance than using
ACC and GYR. Moreover, the attitude angle feature training
by a long short-term memory (LSTM) network can achieve the
highest accuracy and efficiency.

Received 12 March 2024; revised 30 September 2024; accepted 24 October
2024. Date of current version 28 January 2025. This work was supported
in part by the Natural Science Key Foundation of Zhejiang Province
in part by the
under Grant LZ24F030010 and Grant LQN25F030013,
National Key Research and Development Program of China under Grant
2021YFE0100100 and Grant 2021YFE0205400,
in part by the Zhejiang
Provincial Natural Science Foundation under Grant LZ22F030002, and in
part by the National Natural Science Foundation of China under Grant
U1909209. The Associate Editor coordinating the review process was
Dr. Yunjie Yang. (Corresponding authors: Dinghan Hu; Jiuwen Cao.)

This work involved human subjects or animals in its research. Approval
of all ethical and experimental procedures and protocols was granted by
the Children’s Hospital, Zhejiang University School of Medicine under
Application No. 2020-IRB-124, and the Fourth Affiliated Hospital of Anhui
Medical University under Application No. PJ-YX2021-019.

Jiabing Wang, Dinghan Hu, Xiaoping Lai, and Jiuwen Cao are with
Machine Learning and I-health International Cooperation Base of Zhejiang
Province and the Artificial Intelligence Institute, Hangzhou Dianzi Uni-
versity, Hangzhou, Zhejiang 310018, China (e-mail: 1172598406@qq.com;
hdh@hdu.edu.cn; laixp@hdu.edu.cn; jwcao@hdu.edu.cn).

Tao Jiang is with the Department of Neurosurgery and Anhui Public Health
Clinical Center, First Affiliated Hospital of Anhui Medical University, Hefei,
Anhui 230002, China (e-mail: jiangtao@ahmu.edu.cn).

Tiejia Jiang and Feng Gao are with the Department of Neurology,
Children’s Hospital,
for Child
Health, Zhejiang University School of Medicine, Hangzhou 310003, China
(e-mail: jiangyouze@zju.edu.cn; epilepsy@zju.edu.cn).

the National Clinical Research Center

Pierre-Paul Vidal is with the Plateforme d’Etude de la Sensorimotricit ´e
(PES), BioMedTech Facilities, Universit ´e Paris Cit ´e, 75270 Paris, France
(e-mail: pierre-paul.vidal@parisdescartes.fr).

Digital Object Identifier 10.1109/TIM.2025.3529058

Index Terms— Acceleration, angular velocity signal, attitude
angle signal, long short-term memory (LSTM), multimodal signal
analysis, seizure detection, wearable device.

I. INTRODUCTION

E PILEPSY is a serious neurological disorder that affects

approximately 1% of the world’s population [1], [2]. Due
to the unpredictable and recurrent nature of epileptic seizures,
the loss of muscle control and consciousness that accom-
pany seizures can pose serious, even life-threatening risks
of injury for patients. People with epilepsy are two to three
times more likely to die than the general population [3], [4].
Video electroencephalography (EEG) in hospitalized patients
is currently considered the gold standard for epilepsy anal-
is only available in hospitals or specialized
ysis, but
it
epilepsy testing units,
is not portable, and is costly and
of limited duration [5], [6]. Wearable devices have better
environmental adaptability and portability compared to video
EEG, and comfort is ensured while the patient is wearing the
device.

Wearable devices have better environmental adaptability and
portability compared to video EEG, and comfort is ensured
while the patient is wearing the device. The wearable device
is widely used in various fields and plays an important role
in epileptic seizure detection. During seizures, there tends
to be more selectivity in the detection of seizure signals
due to significant changes in the associated physiological
signals. Various aspects of seizures can be assessed by non-
EEG biosignals, including acceleration (ACC), electrodermal
activity (EDA), body temperature, electromyography, or pho-
toplethysmography (PPG) [7], [8], which have been used to
detect epilepsy in either an unimodal or a multimodal form [9],
[10], [11].

Among various non-EEG biosignals, ACC has been always
used to detect epileptic seizures with motor symptoms, such
as GTCS [12], [13]. An accelerometer is often considered
the standard or minimum sensor configuration required to
characterize human activity [14]. However, the acceleration
signal is susceptible to external disturbances and can gen-
erate large noise spikes. The attitude angle signal, as a
is more stable compared to the accel-
synthetic signal,
less sensitive to external disturbances, and
eration signal,
has a faster response to changes in posture, but the con-
tribution of the attitude angle signal
to the detection of
epileptic seizures has not been extensively investigated and
analyzed.

1557-9662 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence
and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:08 UTC from IEEE Xplore.  Restrictions apply. 

2505010

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025

Fig. 1. Signals of three-axis ACC, three-axis GYR, and attitude angle (PITCH
and ROLL).

Fig. 3.
velocity, and attitude angle (PITCH and ROLL).

Time–frequency plots of synthetic acceleration, synthetic angular

all four action classes have more spikes present during the
seizure, and the seizure event can be captured. However, for
ACC and GYR, the number of spikes present in the nonseizure
phase was significantly greater than for PITCH and ROLL,
which is more resistant
to interference in the nonseizure
phase of epilepsy than in ACC and GYR. The results of the
time–frequency plot analysis of Fig. 1 are shown in Fig. 3.
It can be seen that the attitude angle signal has a significant rise
in energy in the frequency range of 0–25 Hz during a seizure,
and the amplitude of the rise in energy is significantly higher
than ACC. When there is no seizure, the attitude angle signal
does not show a wide range of energy enhancement compared
to GYR because it has a better anti-interference ability. It can
be seen that the attitude angle signal is less sensitive to external
interference, has a faster response speed to attitude changes,
and has a greater application prospect in seizure detection.

This article is the first to investigate the role of attitude
angle signals for seizure detection, specifically focusing on
the ROLL and PITCH. The six-modal signals (ACC, GYR,
PITCH, ROLL, surface electromyography (SEMG), and EDA)
are filtered in different ways to remove interfering compo-
nents, and then relevant features are extracted and fused.
three traditional
Using unimodal and multimodal signals,
classifiers are trained and compared, and the possibility of
PITCH/ROLL replacing ACC/GYR for seizure detection is
discussed. Besides, the proposed epilepsy detection algorithm
based on multimodal signals and long short-term memory
(LSTM) shows high detection accuracy and low complexity.
The overall analysis flowchart is shown in Fig. 4.

II. METHODOLOGY

A. Data Acquisition

In this article,

the data of 28 epileptic patients were
researched, with 11 patients coming from the Fourth Affiliated
Hospital of Anhui Medical University and 17 patients com-
ing from the Department of Neurology, Children’s Hospital,
Zhejiang University School of Medicine. Informed consent
was obtained from all participants and their legal guardians.
Despite spending more time in a stationary state in the hospital
environment compared to their daily lives, patients were not

Fig. 2. Envelopes of synthetic acceleration, synthetic angular velocity, and
attitude angle (PITCH and ROLL).

The attitude angle signal has been widely used in the fields
of navigation, agriculture, and attitude detection [15], [16]
and holds a significant research value and medical investiga-
tion significance in epileptic seizure detection. Attitude angle
signals consist of the pitch angle signal (PITCH), yaw angle
signal (YAW), and roll angle signal (ROLL), which describe
the change in the rotation angle of the bracelet device around
the X -, Y -, and Z -axes, respectively [17], [18]. This article
mainly analyzed three-axis ACC, three-axis GYR, PITCH, and
ROLL for seizure detection, as shown in Fig. 1. The attitude
angle signal is derived from sensor fusion of a three-axis
gyroscope and a three-axis accelerometer [19], defined as


 − gy × △t.

PITCH = tan−1

ROLL = tan−1





q

−ax
y + a2
a2
z
(cid:19)
(cid:18) −ay
ax

− gx × △t

(1)

(2)

where ax , ay, and az are the accelerations in the X -, Y -, and
Z -axes, respectively; gx , gy, and gz are the angular velocities
in the X -, Y -, and Z -axes, respectively; and △t is the sampling
time interval.

The results of the envelope analysis of the four action
classes of Fig. 1 are shown in Fig. 2. It can be seen that

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:08 UTC from IEEE Xplore.  Restrictions apply. 

WANG et al.: EPILEPTIC SEIZURE DETECTION BASED ON ATTITUDE ANGLE SIGNAL OF WEARABLE DEVICE

2505010

Fig. 4. Overall analysis flowchart.

completely immobile. All patients were recorded using identi-
cal wearable devices in both hospitals, and video EEG signals
were simultaneously collected. Among 28 epileptic patients
included in the analysis, 22 patients exhibited at least one
seizure recorded, resulting in a cumulative total of 62 seizures.
Each patient wears a wristband called “Biovital-P1,” which
consists of an “EMP sensor” and an “OPPO watch2.” The
application running in the OPPO watch can collect a variety of
physiological signals from the wrist, including pulse, pulse rate
variability, and blood sample signals from the OPPO watch,
as well as nine modal physiological signals such as SEMG,
EDA, ACC, and GYR from the EMP sensor, and the wristband
also calculates the attitude angle signals from ACC and GYR.
Raw data is stored as files in the local memory of the OPPO
watch, while raw data can also be transferred in real time to
the mobile phone for viewing and analysis when connected to
Wi-Fi. The data stored in the wristband can be exported via
USB or transferred to the cloud.

To compensate for time drift between the different devices,
the clocks of both devices were synchronized before acquiring
the physiological signals with the wristband corrected for
time over a network. While acquiring the patient’s phys-
iological signals, both the wristband and EEG monitoring
device recorded scalp EEG signals, which were then visually
inspected by a clinical expert on EEG to mark seizure periods.
The types of signals used in this article and the associated
sampling frequencies are as follows: ACC at 50 Hz, GYR
at 50 Hz, ROLL at 50 Hz, PITCH at 50 Hz, SEMG at 200 Hz,
and EDA at 4 Hz. The details of the data are shown in Table I.
The ACC and GYR are obtained from the accelerometer and
gyroscope inside the wristband, referring to the linear accel-
eration situation in three spatial dimensions and the angular
velocity situation of the three spatial rotation axes of the wrist-
band device, respectively. The PITCH and ROLL are signals
obtained by sensor fusion with a three-axis gyroscope and a
three-axis accelerometer. During seizures, patients are prone
to some degree of limb jerking, and this motor phenomenon is
readily reflected in features such as the time–frequency domain
of action-like signals. SEMG refers to a signal that measures
muscle activity. During a seizure, muscles usually contract and

TABLE I
DETAILS OF DATA (F: FEMALE, M: MALE,
Y: YEAR, M: MONTH, H: HOUR)

relax involuntarily, and this abnormal muscle activity produces
noticeable changes in SEMG [20]. EDA refers to a signal that
measures the surface electrical activity of the skin. During a
seizure, skin conductance may change.

B. Signal Preprocessing

Since noise is mixed into the signal initially captured by the
wristband, this article adopts different ways to remove noise
for different types of signals, as follows.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:08 UTC from IEEE Xplore.  Restrictions apply. 

2505010

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025

1) ACC, GYR, PITCH, and ROLL: The noise is usu-
ally composed of regular human motion and artifacts.
The 0-Hz component is first removed to calibrate the
baseline, and then a median filter with a width of 10 Hz
is used to remove artifacts.

2) SEMG: For SEMG signals, we first used a 4-Hz
comb filter to remove noise from the device, and then
a 20–60-Hz bandpass filter was adopted to remove
low-frequency artifacts due to common movements.
3) EDA: Since galvanic skin activity is a slowly varying
signal and may contain motion artifacts, a median filter
was used to remove the interfering signal components
from the galvanic skin.

C. Feature Extraction and Selection

After data preprocessing, the data is sliced using a slid-
ing window approach [5], [6], [21]. However, the study by
Chung et al. [22] found that the size of the sliding window
may directly or indirectly affect the final recognition accuracy.
Considering the relevant factors such as time resolution and
accuracy, we used a sliding window with a length of 4 s
and an overlap rate of 50% and then calculated the features
of each modal signal from the sliding window. In terms of
feature selection, time-domain features are the best features
for detecting epileptic seizures using accelerometers. It has low
computational complexity and is suitable for real-time analy-
sis. SEMG contains a higher frequency domain ratio during
seizures compared to normal activity, and nonlinear features on
EDA can characterize the changes in skin conductance levels.
Therefore, time, frequency, and nonlinear domain features are
extracted from each signal in this article.

y + g2
z

x + a2

x + g2

(anorm = (a2

Since ACC and GYR are three-channel signals, the syn-
)1/2)
y + a2
thesized acceleration signal
z
(gnorm =
and the synthesized angular velocity signal
)1/2) are first calculated from the three accel-
(g2
eration signals (ax , ay, az) and the three angular velocity
signals (gx , gy, gz) after the filtering operation. The rele-
vant features for anorm and gnorm are then computed using a
sliding window approach. In addition to extracting the time,
frequency, and nonlinear domain features, we also extracted
the mean diagonal
length feature, which was computed
from the acceleration time series using recurrence plots by
Böttcher et al. [5] and successfully applied to detect focal
seizure motor epilepsy with tonic or clonic movements. For
the attitude angle signals (PITCH and ROLL), since they
belong to the action class of signals like ACC and GYR,
we use the same types of features as for ACC and GYR
(time domain, frequency domain, nonlinear domain, and mean
diagonal length features). For SEMG, in addition to the time,
frequency, and nonlinear domain features, the over-zero rate
feature was also computed. Conradsen et al. [20] found that
the over-zero rate feature was also useful in detecting epileptic
seizures for SEMG signals. The final features used in this
article are shown in the first column of Table II.

The use of multimodal signals will result in higher accuracy
in detecting seizures compared to unimodal signals because
multimodal signals provide more comprehensive information.

TABLE II
p-VALUES OF DIFFERENT FEATURES ON SIX-MODAL SIGNALS

The fusion methods of multimode signals generally include
early fusion and late fusion. The early fusion method is
employed in this article, where relevant features are first
extracted from each modal signal, and then all the features
are combined to construct a new feature vector. The combined
feature vector is subsequently used for training the relevant
classifier [23].

To enhance the accuracy of subsequent model classification,
it is necessary to conduct a feature screening operation to iden-
tify the most crucial features for constructing an appropriate
feature set. The t-test was first used to analyze the degree
of difference between the features of different signals during
seizure and nonseizure epilepsy, with the significance levels
expressed as p-values. Table II shows the p-values of different
features on six-modal signals. p < 0.05 indicates that the
feature is significant and retained in this article. These features
are analyzed by correlation analysis to remove the redundant
features with high correlation. The importance of features is
subsequently ranked using the forward search method (SFS) to
retain only the top-ranked important features, thereby reducing
unnecessary features and mitigating overfitting caused by high
dimensionality. This approach ensures efficient classification
performance of the classifier. At least 20 features are retained
for each modal signal in this article to train the classifier.

D. LSTM Classifier

Recurrent neural networks (RNNs) are better at learning
the fundamental representation of time-varying signals [24].
A multitude of extensions and variations of RNNs have
been reported in the relevant academic literature, such as
the Skip RNN [25], LSTM, gated recurrent units [26], and
so on. A stochastic recurrent network that considers the
long-term dependencies inherent in the data has been proposed
by Goyal et al. [27]. Besides, LSTM networks have been

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:08 UTC from IEEE Xplore.  Restrictions apply. 

WANG et al.: EPILEPTIC SEIZURE DETECTION BASED ON ATTITUDE ANGLE SIGNAL OF WEARABLE DEVICE

2505010

TABLE III

COMPARISON RESULTS OF TRADITIONAL CLASSIFIERS
BASED ON UNIMODAL SIGNALS

Fig. 5. LSTM-based seizure detection algorithm on the real-time monitoring
component.

employed in various research, such as the modifier LSTM [28],
external memory-based networks [29], and attention-based
models [30]. After evaluating the benefits of each classification
method, LSTM was adopted for seizure detection to further
investigate the efficiency and feasibility of attitude angle
signals in the real-time detection process, with the proposed
LSTM-based seizure detection algorithm’s workflow diagram
shown in Fig. 5.

III. SIGNAL ANALYSIS

A. Analysis of Features

In this section, we focus on the analysis between the attitude
angle, ACC, and GYR in terms of characterization to further
explore the correlation among these signals. Here, we analyze
the case of correlation between ACC, GYR, PITCH, and
ROLL. The correlation heat maps on PITCH and ACC, PITCH
and GYR, ROLL and ACC, and ROLL and GYR are drawn
in Fig. 6. From the analysis of signal correlation among
these four groups, it can be observed that the majority of
time-domain features exhibit significant correlation, while a
small portion of frequency-domain features also demonstrate
noticeable correlation. Overall, there is a strong correlation
between PITCH and ACC, as well as PITCH and GRY, with
the same conclusion drawn for ROLL and ACC and ROLL
and GRY. Fig. 7 shows the distribution of five representative
features of the four action signals during the seizure and
nonseizure phases. Since most of the features have a similar
distribution, standard deviation and root mean square selected
from the time-domain features, mean frequency and centroid
frequency selected from the frequency-domain features, and
fuzzy entropy features selected from the nonlinear features
are chosen. The distribution of four types of action signals
during different stages of epilepsy was elucidated through
the examination of these five features. It is evident that the
range of the feature distribution for the attitude angle signal is
narrower compared to that of ACC and GYR. However, a more
noticeable difference still exists between the features in the
seizure and nonseizure phases. In terms of feature distribution
across time, frequency, and nonlinear domains, the distribution
of the attitude angle signal is very similar to that of ACC
and GYR.

B. Unimodal Signals-Based Machine Learning

To investigate whether attitude angle signals (PITCH and
ROLL) have the same effect as ACC and GYR in detecting

epileptic seizures, physiological signal data from a total of
18 epileptic patients with patient ID 1–18 were used. Conven-
tional classifiers based on unimodal signals, including Tree,
SVM, and linear discriminant (LDA), were constructed and
compared. Experiments were conducted on patient IDs 1–18,
with a total of 3197 samples. The dataset was divided
into a training set
(2558 samples) and a testing set
(639 samples) with a ratio of 8:2. And tenfold cross-validation
was applied to the training set for the most optimal model
selection, resulting in 256 samples for validation in each
round. Three main indicators of accuracy, precision, and
recall were used to judge the performance of the model.
The comparisons of performance results of the three different
classifiers are shown in Table III. The PITCH-based trained
LDA classifier achieved 78.20% accuracy, 83.20% precision,
and 58.70% recall. Compared to ACC and GYR, it is 3.8% and
4.6% higher in accuracy, 4.7% and 7% higher in precision,
and 7.1% and 7% higher in recall. The LDA classifier trained
on ROLL achieved 78.70% accuracy, 87.10% precision, and
56.40% recall. Compared to ACC and GYR, it is 4.3% and
5.1% higher in accuracy, 8.6% and 10.9% higher in precision,
and 4.8% and 4.7% higher in recall.

It can be seen that PITCH and ROLL outperform ACC and
GYR in terms of accuracy, precision, and recall of Tree, SVM,
and LDA, which is also because the attitude angle signal
is a signal obtained by fusing the sensors of a three-axis
gyroscope and a three-axis accelerometer. Therefore, it has
the same characteristics as ACC and GYR. The above results
demonstrate that the attitude angle signals (PITCH and ROLL)
can be used for seizure detection and are superior to ACC or
GYR in the unimodal signals-based traditional classification
model.

C. Multimodal Signals-Based Machine Learning

In Section III-C, we found that PITCH and ROLL signifi-
cantly outperform ACC and GYR when the unimodal signal is
used to train the classifier. Given that the majority of epilepsy
detection systems currently in use leverage multimodal signals
for seizure detection, our study aims to examine the effects of
incorporating PITCH and ROLL data into the combination of
ACC and GYR multimodal signals on the overall performance
of classifiers.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:08 UTC from IEEE Xplore.  Restrictions apply. 

2505010

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025

Fig. 6. Correlation heat map on PITCH and ACC, PITCH and GYR, ROLL and ACC, and ROLL and GYR.

Fig. 7. Box plot of feature distribution on ACC, GYR, PITCH, and ROLL.

We define the signal types used in Combination 1 as ACC +
GYR + SEMG + EDA, the signal types used in Combina-
tion 2 as ACC + GYR + PITCH + SEMG + EDA, the signal
types used in Combination 3 as ACC + GYR + ROLL +
SEMG + EDA, and the signal types used in Combination 4
as ACC + GYR + PITCH + ROLL + SEMG + EDA.
The comparison results of traditional classifiers based on
multimodal signals are shown in Table IV. It is clear that for

all three classifiers (Tree, SVM, and LDA), when the PITCH
is added alone (Combination 2) or the ROLL is added alone
(Combination 3), the classifiers outperform Combination 1 on
accuracy, precision, and recall. When both PITCH and ROLL
are added to Combination 1 (Combination 4), some of the
classifiers do not perform as well as Combination 2 or
Combination 3, but the overall performance is still better than
Combination 1 (without the PITCH or ROLL).

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:08 UTC from IEEE Xplore.  Restrictions apply. 

WANG et al.: EPILEPTIC SEIZURE DETECTION BASED ON ATTITUDE ANGLE SIGNAL OF WEARABLE DEVICE

2505010

TABLE IV

TABLE V

COMPARISON RESULTS OF TRADITIONAL CLASSIFIERS
BASED ON MULTIMODAL SIGNALS

COMPARISON RESULTS OF TRADITIONAL CLASSIFIERS
WITH THE PITCH REPLACING ACC/GYR

Taking the SVM classifier as an example, the SVM classifier
trained based on Combination 2 achieved 95.5% accuracy,
95.8% precision, and 95.3% recall, which is 2.1% higher in
accuracy, 2.9% higher in precision, and 2.4% higher in recall
than the SVM classifier trained based on Combination 1. The
SVM classifier trained based on Combination 3 achieved 95%
accuracy, 95.3% precision, and 92.2% recall, which provides
1.6% higher accuracy, 2.4% higher precision, and 1.3% higher
recall than the SVM classifier trained based on Combination 1.
The SVM classifier trained based on Combination 4 achieved
95.1% accuracy, 95.3% precision, and 92.7% recall, which
is 1.7% higher in accuracy, 2.4% higher in precision, and
1.8% higher in recall than the SVM classifier trained based on
Combination 1. Similar results were seen for Tree and LDA,
where the classifiers trained with Combination 2, Combina-
tion 3, and Combination 4 outperformed the classifier trained
with Combination 1 in all three metrics. It can be concluded
that the introduction of the PITCH and ROLL has a certain
improvement on the classification effect of the classifier.

D. Analysis of the Possibility of Attitude Angle Signals
Replacing ACC and GYR

By observing and analyzing the results of the performance
of different modal signal combinations in the three classifiers,
experimental results in the previous section prove that the
PITCH and ROLL outperform the ACC and GYR in seizure
detection. This section provides an in-depth analysis of the
PITCH and ROLL and investigates the possibility of replacing
the ACC and GYR with the PITCH and ROLL.

the signal

To research whether the attitude angle signal can replace
ACC and GYR for seizure detection analysis in epilepsy, here
the modal signal types used in Combination 1 are defined as
ACC, GYR, SEMG, and EDA; the signal types used in Combi-
nation 2 are PITCH, GYR, SEMG, and EDA (PITCH replaces
ACC);
types used in Combination 3 are ACC,
PITCH, SEMG, and EDA (PITCH replaces GYR); Combina-
tion 4 uses PITCH, SEMG, and EDA (PITCH replaces ACC
and GYR); Combination 5 uses ROLL, GYR, SEMG, and
EDA (ROLL replaces ACC); Combination 6 uses ACC, ROLL,
SEMG, and EDA (ROLL replaces GYR); Combination 7 uses
ROLL, SEMG, and EDA (ROLL replaces ACC and GYR).

TABLE VI

COMPARISON RESULTS OF TRADITIONAL CLASSIFIERS
WITH THE ROLL REPLACING ACC/GYR

The results of each signal combination approach trained in
tree classification, SVM, and linear discrimination are shown
in Tables V and VI.

From the results, we can see that in Combination 2 (PITCH
instead of ACC), Combination 3 (PITCH instead of GYR),
Combination 5 (ROLL instead of ACC), and Combination 6
(ROLL instead of GYR), the three metrics of accuracy, pre-
cision, and recall are significantly higher than the results in
Combination 1, and there is a significant improvement in
the classification efficiency of the classifiers. Combination 4
(PITCH replaces ACC and GYR) does not show a significant
improvement in tree classification compared to Combination 1,
and SVM shows an improvement of about 1%–2%, but there
is a more significant decrease in linear discrimination instead.
Combination 7 (ROLL replaces ACC and GYR) does not show
a large gap in the metrics of the three classifiers compared to
Combination 1.

In the study by Conradsen et al., the features extracted
from the ACC, GYR, and SEMG were used to train the SVM
classifier model, and the final classifier was 91% accurate [31].
In the study by Zsom et al. [32], features extracted from
ACC, EDA, body temperature, and heart rate signals were
used to train the XGBoost model, and the model achieved a
classification performance of 78% accuracy. In the study by
Vieluf et al. [33], features extracted from EDA, body tem-
perature, and heart rate signals were used to train a machine
learning model, and the cross-validated machine learning
model had an accuracy of 0.69, a sensitivity of 0.68, and

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:08 UTC from IEEE Xplore.  Restrictions apply. 

2505010

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025

a specificity of 0.75. In a study by Heldberg et al. [12],
using ACC and EDA to detect epileptic seizures with motor
symptoms, the final KNN classifier had a sensitivity of 89.1%
and a specificity of 93.1%. It can be seen that the attitude
angle signal instead of the ACC and GYR signal combination
approach leads to better training results as well as higher
training metrics for the classifier.

E. LSTM-Based Seizure Detection

In this section, a wearable device-based algorithm for
detecting epileptic seizures using LSTM is proposed. The
proposed model consists of four layers: signal input layer,
feature extraction layer, early fusion layer, and classifier layer.
In the feature extraction layer, traditional features of the
signal including time-domain features, frequency-domain fea-
tures, and nonlinear domain features are extracted. In the early
fusion layer, the features of each modality are combined into
a feature vector. Since the training and testing set features
are normalized using the 0–1 normalization method, and the
normalization parameters are stored before the LSTM classi-
fier is trained. Hence, the feature vectors must be normalized
using the previously stored normalization parameters from
the training step after the feature vectors are collated in the
early fusion layer. In the classifier layer, LSTM was adopted,
consisting of one LSTM layer (40 hidden units), one Relu
activation layer, one fully connected layer, and one softmax
layer. During the training process, the dataset is randomly
divided into a training set and a testing set, where the testing
set is 20% of the total data, and tenfold cross-validation is used
to train the classifier to prevent overfitting of the classifier. The
ADAM optimizer with binary cross-entropy loss function is
used to ensure the classification efficiency of the classifier as
much as possible [34]. To further demonstrate the effectiveness
of the proposed method, we collected 500 samples from
each of patient IDs 19–28, resulting in an additional testing
set comprising 5000 samples (including both seizure and
nonseizure). The performance is measured by the mean square
error, which is given by the following equation:

MSE =

1
n

n
X

(xi − yi )2

i=1

where n is the number of samples in the testing set, xi is the
true label of the sample, and yi is the label predicted by the
classifier. To optimize the performance of the classifier and to
prevent the classifier from overfitting, the internal hyperparam-
eters of the LSTM classifier are adjusted by grid search. The
smaller the MSE, the better the model performance. When
the number of LSTM layers is 1 with 40 hidden units and
the learning rate is set to 0.01, the MSE is 0.08674, which
achieves the best performance.

Three LSTM classifiers using different signal combinations
are trained, with the specification as follows: classifier 1 for
the signal types ACC, GYR, SEMG, and EDA; classifier 2
for the signal types PITCH, GYR, SEMG, and EDA; and
classifier 3 for the signal types ROLL, GYR, SEMG, and
EDA. The model evaluation metrics are the number of seizures
detected, false alarm rate, and accuracy. The data used for

TEST RESULTS ON DIFFERENT MULTIMODAL SIGNAL COMBINATION

TABLE VII

model training comes from patient IDs 1–18 (3197 samples),
in which 2558 samples were for tenfold cross-validation, and
the long-term data from patient IDs 19–28 were reserved for
testing. Table VII shows the test results by these three LSTM
classifiers on the data with seven labeled seizure events. For
classifier 1, four seizures were successfully detected with an
overall classification accuracy of 80.1%, and a total of 11 false
alarms occurred in the offline data with a cumulative length of
30.24 h, with the false alarm rate of 8.73/24 h. For classifier 2,
five seizures were successfully detected with a classification
accuracy of 83.4%, and a total of 10 false alarms occurred in
the offline data with a cumulative length of 28.36 h, with the
false alarm rate of 8.46/24 h. For classifier 3, seizures were
successfully detected four times with an accuracy of 82.5%,
and a total of 9 false alarms occurred in the offline signals
with a cumulative length of 25.36 h, with the false alarm rate
of 8.51/24 h.

In a study by Boon et al. [35], an ECG-based action-
based seizure detection system was developed with a final
accuracy of 81.8% and a false alarm rate of 11.76/24 h. The
study by van Andel et al. [36] used acceleration signals and
electromyographic signals for action-based seizure detection
with a final median accuracy of 79% and a median false
alarm rate of 12/24 h. In a study by Ge et al. [37], the
ACC signal, angular velocity signal (GYR), SEMG signal,
and EDA signal were used to detect epileptic seizures, and
the sensitivity of the final classifier was 82.6%, with a false
alarm rate of 8.63/24 h. The comparison with the results of
others shows that the proposed LSTM-based seizure detection
algorithm, using attitude angle signals instead of ACC and
GYR signals, has a final false alarm rate index in a reasonable
range and achieves better accuracy.

The detection efficiency results shown in Table VII indicate
that when PITCH and ROLL replace ACC, the accuracy is
improved to some extent and the false alarm rate does not
change much, which shows that PITCH and ROLL can indeed
be used for seizure detection and that PITCH and ROLL can
be used in place of ACC. Since there are not many studies
using GYR, a real-time monitoring model that replaces GYR
with attitude angle signaling was not developed here. However,
due to the high correlation among the four signals ACC,
GYR, PITCH, and ROLL in terms of features, as illustrated in

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:08 UTC from IEEE Xplore.  Restrictions apply. 

WANG et al.: EPILEPTIC SEIZURE DETECTION BASED ON ATTITUDE ANGLE SIGNAL OF WEARABLE DEVICE

2505010

TABLE VIII

TEST RESULTS FOR PATIENT IDS 19–28

the previous sections, we have demonstrated that the attitude
angle signal has the potential to replace GYR based on three
metrics from three classifiers. Combining these results with the
findings presented in this section, we can conclude that both
PITCH and ROLL can also serve as substitutes for GYR in
seizure detection for epilepsy. In the long term, attitude angle
signals have a greater potential for epileptic seizure detection,
and attitude angle signals characterized by both ACC and GYR
signals remain open for more in-depth study in the future.

In the epileptic seizure detection system, employing tra-
ditional features in time, frequency, and nonlinear domains
for classifier training with a sliding window overlap rate of
0% leads to a significant increase in false alarm rates during
actual performance. However,
this issue can be mitigated
by incorporating deep learning techniques and increasing the
overlap rate.

Patient-specific testing experiments are conducted on each
of patient IDs 19–28, where the number of LSTM layers
is 1 with 40 hidden units and the learning rate is set to 0.01.
For each patient, 500 samples are used to test, with the results
shown in Table VIII. The proposed method achieves the best
performance with 97.8% accuracy for patient ID 26. Among
patient IDs 19–28, four patients achieved the test accuracy
exceeding 90%. These results demonstrate the superior classi-
fication performance and generalization ability of the proposed
method.

IV. CONCLUSION

This article explores the usability of attitude angle signals
(PITCH and ACC) for epileptic seizure monitoring and con-
ducts an in-depth analysis of the feature level of the signals.
Through three classifiers (Tree, SVM, and LDA), it is proved
that the attitude angle signal can be used for seizure detection
and outperforms the commonly used ACC signal as well as
the GYR signal in terms of the indicators of accuracy, preci-
sion, and recall. Besides, the proposed LSTM-based seizure
monitoring algorithm using multimodal signals collected from
wearable devices and a multigroup comparison experiment
also demonstrates the usability of attitude angle signals. In the
LSTM-based seizure detection system, three different signal
combination methods are selected and three different LSTM
classifiers are trained. It is concluded that the attitude angle

signals (PITCH and ROLL) replace the ACC to realize the
seizure detection of epilepsy by the two metrics of accuracy
and false alarm rate.

Since the attitude angle signal is a single-channel signal,
while ACC and GYR are three-channel signals, the algorithmic
processing of the attitude angle signal
in the preprocess-
ing step is more efficient in terms of preprocessing speed.
Consequently, there remains untapped potential for further
exploration of attitude angle signals in seizure detection for
epilepsy. This article demonstrates the viability of utilizing
attitude angle signaling for seizure detection and offers addi-
tional options for future research in epilepsy by expanding the
range of available detection signals.

ACKNOWLEDGMENT

All the patients provided informed consent before inclusion

in the study.

REFERENCES

[1] M. Miloševic et al., “Automated detection of tonic–clonic seizures using
3-D accelerometry and surface electromyography in pediatric patients,”
IEEE J. Biomed. Health Informat., vol. 20, no. 5, pp. 1333–1341,
Sep. 2016.

[2] L. Dong, G. Li, C. Tian, L. Lin, Y. Gao, and Y. Zheng, “Design
of submillimeter magnetic stimulation instrumentation and its targeted
inhibitory effect on rat model of epilepsy,” IEEE Trans. Instrum. Meas.,
vol. 70, pp. 1–8, 2021.

[3] A. A. Kabanov and A. I. Shchelkanov, “Development of a wearable
inertial system for motor epileptic seizure detection,” in Proc. 14th
Int. Sci.-Tech. Conf. Actual Problems Electron. Instrum. Eng. (APEIE),
Novosibirsk, Russia, Oct. 2018, pp. 339–342.

[4] M. N. A. Tawhid, S. Siuly, and T. Li, “A convolutional long short-term
memory-based neural network for epilepsy detection from EEG,” IEEE
Trans. Instrum. Meas., vol. 71, pp. 1–11, 2022.

[5] S. Böttcher et al., “Intra- and inter-subject perspectives on the detection
of focal onset motor seizures in epilepsy patients,” Sensors, vol. 22,
no. 9, p. 3318, Apr. 2022.

[6] M. Nasseri et al., “Ambulatory seizure forecasting with a wrist-worn
device using long-short term memory deep learning,” Sci. Rep., vol. 11,
no. 1, p. 21935, Nov. 2021.

[7] M. Glasstetter et al., “Identification of ictal tachycardia in focal motor-
and non-motor seizures by means of a wearable PPG sensor,” Sensors,
vol. 21, no. 18, p. 6017, Sep. 2021.

[8] M.-Z. Poh, T. Loddenkemper, N. C. Swenson, S. Goyal, J. R. Madsen,
and R. W. Picard, “Continuous monitoring of electrodermal activity
during epileptic seizures using a wearable sensor,” in Proc. Annu. Int.
Conf. IEEE Eng. Med. Biol., Aug. 2010, pp. 4415–4418.

[9] A. Ulate-Campos, F. Coughlin, M. Gaínza-Lein, I. S. Fernández,
P. L. Pearl, and T. Loddenkemper, “Automated seizure detection systems
and their effectiveness for each type of seizure,” Seizure, vol. 40,
pp. 88–101, Aug. 2016.

[10] A. Van De Vel et al., “Non-EEG seizure detection systems and potential
SUDEP prevention: State of the art,” Seizure, vol. 41, pp. 141–153,
Oct. 2016.

[11] F. Chen, I. Chen, M. Zafar, S. R. Sinha, and X. Hu, “Seizures detection
using multimodal signals: A scoping review,” Physiological Meas.,
vol. 43, no. 7, Jul. 2022, Art. no. 07TR01.

[12] B. E. Heldberg, T. Kautz, H. Leutheuser, R. Hopfengärtner, B. S. Kasper,
and B. M. Eskofier, “Using wearable sensors for semiology-independent
seizure detection–towards ambulatory monitoring of epilepsy,” in Proc.
37th Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. (EMBC), Aug. 2015,
pp. 5593–5596.

[13] C. Dong et al., “A two-layer ensemble method for detecting epileptic
seizures using a self-annotation bracelet with motor sensors,” IEEE
Trans. Instrum. Meas., vol. 71, pp. 1–13, 2022.

[14] C. Ma et al., “Quantitative assessment of essential tremor based on
machine learning methods using wearable device,” Biomed. Signal
Process. Control, vol. 71, Jan. 2022, Art. no. 103244.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:08 UTC from IEEE Xplore.  Restrictions apply. 

2505010

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025

[15] Y. Dong, Y. Zhang, and J. Ai, “Full-altitude attitude angles enve-
lope and model predictive control-based attitude angles protection
for civil aircraft,” Aerosp. Sci. Technol., vol. 55, pp. 292–306,
Aug. 2016.

[16] H. Tian, Y. Liu, J. Zhou, Y. Wang, J. Wang, and W. Zhang, “Attitude
angle compensation for a synchronous acquisition method based on an
MEMS sensor,” Sensors, vol. 19, no. 3, p. 483, Jan. 2019.

[17] J. L. Ackerman, W. R. Proffit, D. M. Sarver, M. B. Ackerman, and
M. R. Kean, “Pitch, roll, and yaw: Describing the spatial orientation
of dentofacial traits,” Amer. J. Orthodontics Dentofacial Orthopedics,
vol. 131, no. 3, pp. 305–310, Mar. 2007.

[18] K. D. Kumar and K. Kumar, “Satellite pitch and roll attitude maneuvers
tethers,” Acta Astronautica, vol. 44, nos. 5–6,

through very short
pp. 257–265, Mar. 1999.

[19] Y. Liu, N. Noguchi, and K. Ishii, “Development of a low-cost IMU by
using sensor fusion for attitude angle estimation,” IFAC Proc. Volumes,
vol. 47, no. 3, pp. 4435–4440, 2014.

[20] I. Conradsen, S. Beniczky, K. Hoppe, P. Wolf, and H. B. D. Sorensen,
“Automated algorithm for generalized tonic–clonic epileptic seizure
onset detection based on sEMG zero-crossing rate,” IEEE Trans.
Biomed. Eng., vol. 59, no. 2, pp. 579–585, Feb. 2012.

[21] N. Pradhan, S. Rajan, A. Adler, and C. Redpath, “Classification
of the quality of wristband-based photoplethysmography signals,” in
Proc.
(MeMeA), May 2017,
pp. 269–274.

IEEE Int. Symp. Med. Meas. Appl.

[22] S. Chung, J. Lim, K. J. Noh, G. Kim, and H. Jeong, “Sensor
data acquisition and multimodal sensor fusion for human activity
recognition using deep learning,” Sensors, vol. 19, no. 7, p. 1716,
Apr. 2019.

[23] B. Nakisa, M. N. Rastgoo, A. Rakotonirainy, F. Maire, and V. Chandran,
“Automatic emotion recognition using temporal multimodal deep learn-
ing,” IEEE Access, vol. 8, pp. 225463–225474, 2020.

[24] D. Jyotishi and S. Dandapat, “An LSTM-based model for person
identification using ECG signal,” IEEE Sensors Lett., vol. 4, no. 8,
pp. 1–4, Aug. 2020.

[25] V. Campos, B. Jou, X. Giro-I-Nieto, J. Torres, and S.-F. Chang, “Skip
RNN: Learning to skip state updates in recurrent neural networks,” 2017,
arXiv:1708.06834.

[26] K. Greff, R. K. Srivastava, J. Koutník, B. R. Steunebrink, and
J. Schmidhuber, “LSTM: A search space Odyssey,” IEEE Trans. Neural
Netw. Learn. Syst., vol. 28, no. 10, pp. 2222–2232, Oct. 2016.

[27] A. Goyal, A. Sordoni, M.-A. Côté, N. R. Ke, and Y. Bengio,
“Z-forcing: Training stochastic recurrent networks,” in Proc. Adv. Neural
Inf. Process. Syst., vol. 30, Nov. 2017, pp. 6713–6723.

[28] G. Melis, T. Koˇcisk`y, and P. Blunsom, “Mogrifier LSTM,” 2019,

arXiv:1909.01792.

[29] S. Sukhbaatar, A. Szlam, J. Weston, and R. Fergus, “End-to-end memory
networks,” in Proc. Adv. Neural Inf. Process. Syst., vol. 28, Dec. 2015,
pp. 2440–2448.

[30] D. Bahdanau, K. Cho, and Y. Bengio, “Neural machine translation by

jointly learning to align and translate,” 2014, arXiv:1409.0473.

[31] I. Conradsen, S. Beniczky, P. Wolf, J. Henriksen, T. Sams, and
H. B. D. Sorensen, “Seizure onset detection based on a uni- or
intelligent seizure acquisition (UISA/MISA) system,”
multi-modal
in Proc. Annu.
IEEE Eng. Med. Biol., Aug. 2010,
pp. 3269–3272.

Int. Conf.

[32] A. Zsom et al., “Ictal autonomic activity recorded via wearable-sensors
plus machine learning can discriminate epileptic and psychogenic
nonepileptic seizures,” in Proc. 41st Annu. Int. Conf. IEEE Eng. Med.
Biol. Soc. (EMBC), Jul. 2019, pp. 3502–3506.

[33] S. Vieluf et al., “Seizure-related differences in biosignal 24-h modulation

patterns,” Sci. Rep., vol. 12, no. 1, p. 15070, Sep. 2022.

[34] C. Meisel, R. El Atrache, M. Jackson, S. Schubach, C. Ufongene, and
T. Loddenkemper, “Machine learning from wristband sensor data for
wearable, noninvasive seizure forecasting,” Epilepsia, vol. 61, no. 12,
pp. 2653–2666, Dec. 2020.

[35] P. Boon et al., “A prospective, multicenter study of cardiac-based
seizure detection to activate vagus nerve stimulation,” Seizure, vol. 32,
pp. 52–61, Nov. 2015.

[36] J. van Andel et al., “Multimodal, automated detection of nocturnal motor
seizures at home: Is a reliable seizure detector feasible?” Epilepsia Open,
vol. 2, no. 4, pp. 424–431, Dec. 2017.

[37] Y. Ge et al., “Multimodal wearable device signal based epilepsy detec-
tion with multi-scale convolutional neural network,” in Proc. Int. Conf.
Cogn. Syst. Signal Process. Cham, Switzerland: Springer, Nov. 2023,
pp. 70–80.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:08 UTC from IEEE Xplore.  Restrictions apply.
