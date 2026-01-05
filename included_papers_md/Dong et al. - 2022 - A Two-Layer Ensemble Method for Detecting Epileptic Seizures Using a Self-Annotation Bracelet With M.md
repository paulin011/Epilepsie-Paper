# Dong et al. - 2022 - A Two-Layer Ensemble Method for Detecting Epileptic Seizures Using a Self-Annotation Bracelet With M

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022

4005013

A Two-Layer Ensemble Method for Detecting
Epileptic Seizures Using a Self-Annotation
Bracelet With Motor Sensors

Chunjiao Dong , Tianchun Ye , Member, IEEE, Xi Long , Senior Member, IEEE,

Ronald M. Aarts

, Fellow, IEEE, Johannes P. van Dijk , Senior Member, IEEE, Chunheng Shang ,

Xiwen Liao , Wei Chen , Senior Member, IEEE, Wanlin Lai

, Lei Chen , and Yunfeng Wang

Abstract— Using monitoring devices could help avoid injuries
and even death. Currently, wearable sensors such as motion
sensors and other sensors are used to detect when the patient is
having a seizure and alarm their caregivers. However, the devel-
opment phase of these devices requires labor-intensive work on
labeling the collected data, resulting in difﬁculties in developing
wearable monitoring devices. Thus, a more automated auxiliary
method of labeling seizure data and a wearable device to detect
seizures for daily monitoring use are necessary. We collected
data from epileptics outside the hospital with our proposed
bracelet. The subjects were asked to press the mark button
after they had seizures. We also presented an automatically
extraction and annotation of moving segments (EAMS) algorithm
to exclude nonmoving segments. Then, we used a two-layer
ensemble model (TLEM) using machine learning methods to
classify seizures and non-seizure moving segments, which was
designed to deal with imbalanced dataset. Then, we build two
individual TLEM models separately for the overall (all day and
night) seizure detection case and the night seizure detection
case, owing to different imbalance of these datasets. The EAMS
algorithm exclude 93.9% raw inactive data. The TLEM model

Manuscript received November 11, 2021; revised March 29, 2022; accepted
April 13, 2022. Date of publication May 11, 2022; date of current ver-
sion May 19, 2022. The work was supported in part by the Alliance
of International Science Organization under Grant ANSO-CR-SP-2020-04
(2020000147) and in part by the Natural Science Foundation of China
under Grant 12026607. The Associate Editor coordinating the review process
was Dr. Fabricio Guimaraes Baptista. (Corresponding authors: Lei Chen;
Yunfeng Wang.)

Chunjiao Dong is with the Institute of Microelectronics of Chinese Acad-
emy of Sciences (IMECAS) and the Department of Electronic Electrical
and Communication Engineering, University of Chinese Academy of Sci-
ences (UCAS), Beijing 100049, China (e-mail: dongchunjiao@ime.ac.cn;
C.Dong95@hotmail.com).

Tianchun Ye, Xiwen Liao, and Yunfeng Wang are with the Institute of
Microelectronics of the Chinese Academy of Sciences (IMECAS), Bei-
liaoxiwen@ime.ac.cn;
jing 100029, China (e-mail: yetianchun@ime.ac.cn;
wangyunfeng@ime.ac.cn).

Xi Long, Ronald M. Aarts, and Johannes P. van Dijk are with the Depart-
ment of Electrical Engineering, Eindhoven University of Technology, 5612
AZ Eindhoven, The Netherlands (e-mail: X.Long@tue.nl; R.M.Aarts@tue.nl;
J.P.v.Dijk@tue.nl).

Chunheng Shang was with the Institute of Microelectronics of the Chi-
nese Academy of Sciences (IMECAS), Beijing 100029, China. She is now
with Beijing Shunyuan Kaihua Technology, Beijing 100036, China (e-mail:
shangchunheng@zepp.com).

Wei Chen is with the Center for Intelligent Medical Electronics, Department
of Electronic Engineering, School of Information Science and Technology,
Fudan University, Shanghai 200433, China (e-mail: w_chen@fudan.edu.cn).
Wanlin Lai and Lei Chen are with the Department of Neurology,
West China Hospital, Sichuan University, Chengdu 610041, China (e-mail:
laiwl93@163.com; leilei_25@126.com).

Digital Object Identiﬁer 10.1109/TIM.2022.3173270

achieved 76.84% sensitivity (SEN) and 97.28% accuracy (ACU)
for the overall case and achieved 94.57% SEN and 91.37% ACU
for the night case. These results indicate that this bracelet can
capture seizures efﬁciently, and our proposed TLEM has higher
SEN and ACU than single-layer machine learning models.

Index Terms— Accelerometer (ACM), epilepsy, gyroscope,
machine learning, motor sensor, seizure detection, signal process-
ing, wearable device.

I. INTRODUCTION

A CCORDING to the World Health Organization’s report,

there are around 50 million (7‰) epileptics worldwide,
based on which the population of epileptics in China would
be more than 9 million and is growing at the rate of 400 000
each year [1]. Epileptics are facing plenty of possible risks,
including injury, and even sudden unexpected death in epilepsy
(SUDEP), with sudden death rate two to four times higher than
those who are healthy [2]. They are at risk of random seizures
for a long time, even a lifetime.

it

To date, the pathogenesis of SUDEP is unclear, and SUDEP
has many possible related factors. Medication can help about
70% epileptics, but for the remaining 30% [3],
is not
effective. Most sudden deaths happened after generalized
tonic–clonic seizures (GTCS) [4]. In addition, the risk of
SUDEP increases with the frequency of GTCS in patients.
The American Academy of Neurology and American Epilepsy
Society published “Practice guideline summary: SUDEP inci-
dence rates and risk factors” in 2017, and they announced that
the use of monitoring equipment can alarm caregivers to take
proper measures, and this could help reduce respiratory dys-
function and hypoxemia [5] of the patient. Epileptic seizures,
especially seizures that happened at night, are at serious risk
of being missed by their caregivers. Wearable epileptic seizure
detection devices could help improve the patients’ quality
of life and independence, while also providing a means for
continuous patient recording treatment evaluation.

Video-electroencephalography monitoring (VEM)

is the
gold standard for epileptic seizure monitoring [6]. Lahmiri
and Shmuel [7] proposed a computer-aided diagnostic tool to
help support a decision in clinical applications. They extracted
Hurst exponents in different scales and built a K near-
est neighbors (KNN) model to automatically detect seizures
in electroencephalogram (EEG) signal. Kołodziej et al. [8]

1557-9662 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply. 

4005013

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022

developed a seizures and spikes detection algorithm based
on the duration and amplitude of the sought spikes. How-
ever, an device [7], [8] with wires would be required for
VEM, which is uncomfortable for epileptics. Using VEM also
requires trained personnel to position the electrodes on the
speciﬁc area. Consequently, VEM is not a suitable monitoring
method for daily care outside the hospital.

Besides the EEG and electrocorticography recording instru-
mentation and measurements, wearable non-EEG seizure
detection systems focus on the use of different sensing
modalities or methods, such as accelerometer (ACM) [9]–
[14], electromyography (EMG) [15], [16], photoplethysmog-
raphy (PPG) [17], [18], and electrocardiogram (ECG) [19],
[20]. The method or combination of methods most appro-
type of
seizure detection depends on the
priate
seizure [21]. For instance, combining ACM and electro-
dermal activity sensors could not only detect GTCS, but
also could quantify the autonomic dysfunction caused by
seizures [22].

for

As a preliminary study, we used an ACM to start our
research, because it is the most direct way to detect the severe
seizures. There are mainly two kinds of epileptic seizures:
convulsive seizures and non-convulsive seizures, of which
the ﬁrst one contributes to most seizure-associated accidents,
including injuries, asphyxia, and SUDEP [4]. Movements
are the most direct characters of detecting motor seizures,
and it is the ﬁrst choice of all non-EEG seizure detection
methods widely used in clinics [23]. ACM sensors mounted
on the arms and legs can detect these movements, which
are least invasive to patients compared with other non-EEG
seizure detection methods [23]. However, there is no single
detection device that can detect all kinds of seizures, and most
multisensor detection systems include motor sensors to avoid
severe convulsive seizures by monitoring abnormal movement
events [24].

the patient

The normal motor data-collection methods used in these
researches [9], [11], [12], [25], [26] are to collect data in
a hospital where the patient wears motor-detecting devices
and undergoes VEM meanwhile. Although the gold stan-
dard for epilepsy monitoring is VEM, it is not suitable for
daily monitoring, because the patient would be limited to be
equipped with the VEM all day long in the hospital, which
means that the collected data only contains the movements
is doing indoors inconspicuous activities.
that
On the other hand, labeling data of seizures according to EEG
recordings could be a costly and time-consuming work, and an
automatic monitoring data annotation method without medical
supervision could help with this situation [27]. Using motor
sensors along with video recordings could solve the problem
of collecting seizure counts, and this method is more accurate
than self-reporting by patients [28] by taking hand-write
notes. For patient privacy purposes, another form of electronic
recording besides video recording may help to record events,
such as adding patient-recorded seizure time to the moni-
tored acceleration (ACC) data in real time. In this research,
we illustrate a home-based movement-recording method by
adding a mark button (details will be introduced later) on our
bracelet. This mark button would help annotate each seizure

by the subject during/after having seizures. Such electronic
markers, which were recorded in the raw monitoring data,
could provide more reliable recordings of seizures’ times than
patients’ handwritten notebooks or mobile phone recordings.
We then designed an automatic method to extract the seizure
data segments according to these annotations.

Statistical methods and machine learning classiﬁcation
methods have been investigated in the epileptic seizure
detection ﬁeld, with potential clinical applications, such as
threshold value method, KNN [10] model, and support
vector machine (SVM) model [11]. Cuppens et al. [13],
Conradsen et al. [29], and Luca et al. [30] used the threshold
value method to classify seizures. They set
the threshold
value by observing the data. However, this is a labor-intensive
method, because it has to set different thresholds for different
subjects, and it is not an ideal method to be extended to widely
used by all convulsive epileptics. Borujeny et al. [10] used the
KNN model and artiﬁcial neural networks to detect seizures
from three patients, which achieved 85% sensitivity (SEN),
and the KNN model performed better. They also claimed that
if at least 50% of the dataset were seizure samples, the system
could detect the seizure more accurately, which illustrated
that the KNN model could not deal with this imbalanced
dataset seizure detection problem. Kusmakar et al. [11] used
kernalized SVM to detect convulsive seizures. Although they
detected 40 of 46 seizures, a false alarm rate (FAR) of
1.16/24 h occurred, and the system was developed and tested
on data collected in a hospital setting. Johansson et al. [31]
compared the performances of KNN, SVM, and random
forest (RF) models, and all models achieved high sensitivities
to detect tonic–clonic seizures. SVM and RF had an SEN of
90%, the KNN had 100% SEN, and RF had the lowest false
positive (FP) rate, which is owing to the ability of handling
imbalanced dataset.

However, these mentioned methods are all based upon the
assumption that the number of epileptic seizures is in balance
with the number of normal movements, which is not the case
in practice. Consequently, a technique that can overcome the
imbalance of the dataset would be more suitable for seizure
detection based on motor data. For instance, RF model’s
performance on imbalanced data was conﬁrmed in Khoshgof-
taar et al.’s [32] study. They used ten differently imbalanced
datasets to train and test the RF model and other models
(KNN, SVM, Naive Bayes, and so on) and compared the
performance of these models. The results showed that the
RF model had the best performance in accuracy (ACU) when
selecting proper the number of trees and features for each tree.
RF beneﬁts from randomness in each tree classiﬁer and for its
robustness.

In our previous work [33], we have presented a system
for detecting and classifying convulsive seizures and normal
movements using a single RF model, which could ignore the
effects of the imbalanced dataset. Though this system achieved
75.92% SEN for 24-h seizure detection and 88.01% SEN for
night seizure detection, it was still not completely trained well
due to the lack of enough seizure data.

In this latest study, the main innovations of this work are

as follows.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply. 

DONG et al.: TWO-LAYER ENSEMBLE METHOD FOR DETECTING EPILEPTIC SEIZURES USING A SELF-ANNOTATION BRACELET

4005013

Fig. 1.
algorithm, and a TLEM algorithm using machine learning methods. StdAcct/EgAcct = standard deviation/energy of the total ACC in a time window.

Protocol of our proposed research, including three main steps: collection of the raw data, extraction and annotation of moving segments (EAMS)

1) Provided a new method making it possible to collect
more data from daily life instead of in the hospital, and
this is realized by adding a mark button on the device.
2) Designed the EAMS algorithm to increase the efﬁciency
in the preprocessing step by automatically selecting
moving segments. The thresholds chosen in the EAMS
algorithm also could work on more subjects, because we
set them based on human activities, not only speciﬁc
subjects’ seizures included in this manuscript.

3) Presented the two-layer ensemble model (TLEM) algo-
rithm, which is the fusion of four simple and single
classiﬁers, which makes the computing not too complex
while increasing the performance.

II. MATERIALS AND METHODS

Fig. 1 shows the protocol of our proposed research. After
we designed the bracelet and collected enough data for our
there are mainly two
research in Sections II-A and II-B,
steps to analyze the data: 1) EAMS: thresholding to exclude
nonmoving segments and annotating seizure segments, which
would be illustrated in Section II-C. 2) TLEM: a two-layer
approach to classify seizure and non-seizure movements,
which would be illustrated in Sections II-D and II-E. In the
development phase, the subjects would use the mark button
to help annotate seizures. In the application phase in our
future study, the MARK button would have two functions; one
is to annotate missing seizures by pressing only once after
the seizure, and this would help the bracelet recognize the

Fig. 2. This wireless bracelet has a red mark button. (1) Front panel, the
red and green LEDs show the status of the bracelet, that is working/low bat-
tery/low storage/charging. (2) Electronics board, including a central processing
unit (CPU), an SD card, an ACM sensor, a gyroscope sensor, and a mark
button. (3) Chargeable lithium polymer battery, supporting over 24-h work.

movement before the press as a seizure; the other is to cancel
a false alarm by a double press.

A. Devices Design

We implemented the bracelet mainly focused on an afford-
able, lightweight, and wearable solution with improved com-
forts for patients. As shown in Fig. 2, we designed a bracelet
with built-in microelectromechanical systems including a 3-D

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply. 

4005013

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022

ACM and a 3-D gyroscope, and these two sensors are used
to capture the subject’s motion for seizures detection. This
battery-powered embedded electronic system consists of a
sensor interface, a power supply module, a secure digital (SD)
memory module, and a seizure mark module. The chargeable
800-mA battery could work for more than 24 h. The collected
data would be stored in an SD card temporarily, which could
store data of more than seven days. We recommended that
subjects (or their caregivers) upload the collected data every
night before they went to bed if they had seizures that day,
and others would upload data every week.

The self-annotation mark button, as shown in Fig. 2,
is designed to mark the seizure time by the patient or his/her
caregivers. In our future study, this self-annotation button
would help improve the ACU and SEN of the detection
system by marking the false alarmed normal activity and
failed detected seizure event. The 3-D ACM and 3-D gyro-
scope (ANG) signals were sampled at 100 Hz. The band is
made of elastic fabric and could be adjusted to the subject’s
wrist. The subjects were asked to place this bracelet on their
right or left wrist, depending on which side they have the more
serious symptom.

B. Data Acquisition

The data collection process was carried out together with
each subject’s daily life outside the hospital, and we selected
patients with GTCS who had been hospitalized for more than a
year. Selected patients were trained on how to use the bracelet
to collect data at home and how to annotate all seizure events
(by pressing the mark button).

In total, 12 patients with convulsive seizures participated
were recruited in the hospital for this research, and 7 patients
(ﬁve males, two females; age among 6–35 years old, median
26 years old) had seizure events (overall 547 times, mean
78.1; at night 314 times, average 44.9) recorded during the
data collecting step. The total time of these seven subjects’
monitoring was 4152 h (range 120–1344, mean 461.3, median
336).

During the data collection period, all seizure events informa-
tion (start time, stop time, and symptoms) would be recorded
by the subjects through texts or by their caregivers through
phone cameras. These self-recordings would only be used to
check if the subjects pressed the mark button properly, and
if they forgot to press the mark button after a seizure, these
recordings would help us ﬁnd the seizure segment. The quality
of all collected data and self-annotated marks was checked by
hospital specialists by comparing it with the subjects’ records.
In this way, we can collect more daily activities, such as
brushing teeth, walking around, playing video games, and so
on, than the hospital data collection methods. Presumably,
the more types of everyday movements we collect, the more
practical the bracelet will be.

This data collection method allows collecting data from
patients with different daily activities, rather than in hospi-
tals with limited activities. Hospital experts reviewed all the
annotations and the moving segments extracted by EAMS.
If the patient pressed the button multiple times during/after the

Fig. 3. Distribution of the length of moving segments.

seizure, only one mark would be kept and other marks would
be removed, while if the subject forgot to press the button,
a new mark would be added by the expert. This research was
approved by the West China Hospital of Sichuan University
Biomedical Research Ethics Committee [No. 2018(590)], and
each patient (or his/her caregiver) provided written informed
consent.

C. Extraction and Annotation of Moving Segments

features, we

The original data contained two main categories of data:
moving segments (seizures and non-seizure movements) and
nonmoving segments. To increase the efﬁciency of data
processing, before the calculation of
pre-
processed the original data to exclude the segments that
do not contain valid information (i.e., no movement)
and kept only the moving segments of the patient. Sub-
sequently, moving segments would be further divided into
seizure movements and non-seizure movements and labeled
properly. The original monitoring data spans over 24 h. Man-
ual detection of moving events is a labor-intensive process.
To speed this up, we designed an automated selection method
of moving data, followed by a semiautomatic annotation in
terms of seizure and non-seizure movements according to the
subject’s marks, which needs a double check by experts if any
abnormal occurs.

The proposed EAMS method has four steps for extraction

and three steps for annotation.

As for the extraction phase, ﬁrst, the raw total ACC data
signal (acct = (ax 2 + ay2 + az2)1/2) is processed by the
eighth-order Butterworth low-pass ﬁlter with a cutoff fre-
the frequency of the
is known that
quency of 35 Hz. It
muscular contractions is lower than 20 Hz [23]. Second,
a sliding window with a duration of 2 s and an overlap of 1 s
between consecutive windows are used to estimate the stan-
dard deviation (StdAcct) and short-time energy (EgAcct) of
the ﬁltered total ACC signal. The standard deviation StdAcct
is calculated by

StdAcctn =

(cid:2)

(cid:3)

(cid:4)

L
i

(cid:5)
2

accti − acctn
L

(1)

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply. 

DONG et al.: TWO-LAYER ENSEMBLE METHOD FOR DETECTING EPILEPTIC SEIZURES USING A SELF-ANNOTATION BRACELET

4005013

Fig. 4. P values of the extracted features. The blue line shows P = 0.05. The features with P < 0.05 were kept in this study. The labels of the extracted
are named as: (sensor axis)_(feature).

where StdAcctn represents the standard deviation in the nth
window, and L represents the length of data in a sliding
window. L = Ws × Fs , where Ws is the window size (Ws =
2 s), Fs is the sampling frequency of the sensor, and acctn is
the average of ACC in the nth window. The short-term average
energy EgAcct in the nth window is computed, such that

EgAcctn

=

L(cid:6)

(w(L) ∗ acct(i ))2

i

(2)

where EgAcctn represents the short-time energy in the nth
window, and w(L) is a Hanning window used to smooth the
signal before calculating the short-term average energy. The
changes in standard deviation and short-time energy illustrate
the start and stop of each moving event. Third, two thresholds
of StdAcct and EgAcct are used to determine the start and stop
times of each moving event. These thresholds (i.e., 0.2 and 15)
are selected empirically for each subject to account for the
changes in the noise. At last, movement events lasting for less
than 15 s are excluded from further analysis. Two adjacent
segments with intervals less than 10 s are considered as a
whole segment.

As for annotation phase, after identifying all moving seg-
ments and excluding inactive data, all automatically selected
movement events would be labeled as “seizure” and “non-
seizure movement,” according to the subject’s marks when
using the bracelet. First, if the mark was not in a moving
segment, the moving segment right before the mark would be
annotated as a seizure event. Second, however, some marks
could occur during moving segments. If the mark was in the
last half of a moving segment, then this moving segment
would be annotated as a seizure event. Third, if the mark
was in the ﬁrst half of a moving segment, and it was close
(<20 s) to the end of the last moving segment, we would
annotate the last moving segment as a seizure event. However,
some abnormal could occur, such as two marks appeared
in a short time (<5 s), meaning the subject double pressed
the mark button, and we would discard the later duplicated
mark.

The moving segments range from 15 to 500 s, and the
distribution of the length of moving segments is shown in
Fig. 3. There are some moving segments lasting for more
than 20 s, because two adjacent segments with intervals less
than 10 s are considered as a whole seizure segment, which
means that we merged such consecutive segments of move-
ments. Those long moving segments usually happen in the
daytime.

D. Feature Extraction and Selection

Each moving segment’s raw data consist of ten channels,
including 3-D ACC (ax, ay, and az), 3-D ANG (gx, gy, and
gz), and 4-D quaternion (q0, q1, q2, and q3). We calculated
the total ACC (acct) and regarded it as the 11th channel. The
3-D ACC and 3-D ANG were directly collected from a six-axis
motion sensor. The quaternion could also be acquired from the
sensor, and it was calculated [34] from the raw signals of the
gyroscope by the following equations:
⎧
⎪⎪⎪⎨
⎪⎪⎪⎩

q0∗ = q0 + (−q1 ∗ gx − q2 ∗ gy − q3 ∗ gz) ∗ (T /2)
q1∗ = q1 + (q0 ∗ gx + q2 ∗ gz − q3 ∗ gy) ∗ (T /2)
q2∗ = q2 + (q0 ∗ gy − q1 ∗ gz + q3 ∗ gx) ∗ (T /2)
q3∗ = q3 + (q0 ∗ gz + q1 ∗ gy − q2 ∗ gx) ∗ (T /2)

(3)

where q0, q1, q2, and q3 are the four components of a 4-D
quaternion at time k, and gx, gy, and gz are the 3-D ANG
values at time k; then q0∗, q1∗, q2∗, and q3∗ would be the
updated quaternion components at time k + 1, and the time
window size is T .

Different statistical

features have been investigated for
classiﬁcation [10]. We selected a number of time-domain
features to describe each event and evaluated these features
to select
the most useful features to build the classiﬁca-
tion model. For each dimension of the entire 11-D data
(ax, ay, az, gx, gy, gz, q0, q1, q2, q3, and acct), we
calcu-
lated the minimum (min), maximum (max), mean, variance
(var), and interquartile range (iqr). In addition, we also
included the duration of each movement.

The best features are then selected through a ﬁltering feature
selection called analysis of variance. In this method, if a

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply. 

4005013

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022

The outputs of Layer 1 would be input to Layer2. Layer2 used
logistic regression (LR) as the ﬁnal classiﬁer. These two-layer
model’s parameters are shown in Table I. As Layer2 is an LR
model, the weights could be learned through model training,
which is [0.45, 2.33, 4.12, 6.76] for the four base learners
(GBDT, RF, ET, and ADB).

RF consists of a set of decision trees, and voting strategies
are used to make ﬁnal predictions. RF uses the bootstrap
method, namely, the resampling technique, to randomly select
N samples from N original training samples, and N samples
here can be repeated. If we repeat this operation for k times,
we will get k new training sets, and each new training set will
have N samples. In this study, here are mall = 59 features
in each sample, and the maximum number of features that
can be used in each leaf is set to mtry (mtry < mall). The
advantages of the RF classiﬁcation are that the model can
be trained with unbalanced datasets (most of the data are
normal movements, and very few are seizures), and the model
can be ﬂexibly adjusted as the volume of data increases.
ET is similar to RF, and the main differences, which tell ET
and RF apart, are that the ET uses all the sample, chooses
features randomly, and splits trees randomly. Each tree in
ET is grown from the original learning sample instead of
bootstrap, which increases the randomness of the model and
suppressed overﬁtting; however, this randomness could lead
to larger bias. In this case, its performance is good enough
to be a base learner in a two-layer stacking ensemble model.
GBDT is an iteration method, which is composed of multiple
decision trees, and it uses CART as base learners. GBDT
often shows good performance for linear inseparable data.
ADB is a method that combines the decision of individual
base classiﬁers. To get better performance, during the iteration
process, ADB increases the weights of samples that were
classiﬁed incorrectly and raises the weights of base classiﬁers
that have a lower error rate. ADB is also a strategy of
ensemble learning, which is originally proposed by Freund and
Schapire [35]. In general, ADB has shown fast and accurate
performance at classifying. Especially, we set the weight of
positive samples as four and the negative samples as one,
because we assume that false predicted positive events would
result in missing seizures, which is not acceptable for a seizure
detection model.

We used 70% samples to train our proposed model, which
is 7507 normal movements and 370 seizures for the over-
all model, and 562 normal movements and 222 seizures
for the night model. We proposed to establish two sep-
arate models to account for the different proportions of
normal movements and seizures that occur during the day
and at night. For both models’ training step, we used a
sixfold cross-validation approach to validate the temporary
performance. In this step, the training dataset was divided
into sixfold for cross validation, and in each iteration, ﬁve
folds were used to train the classiﬁer, and the remained
onefold was used for validation, and the results are shown
in Fig. 6.

To avoid overﬁtting during model training, model validation
is necessary. We used a Midscore value to describe the
average ACU score of training and validation during the model

Fig. 5. Extract features from each moving segment and label each feature
according to the marks. Next, use these features to train the two-layer
ensemble classiﬁcation.f

PARAMETERS OF THE BASE-LAYER MODELS AND META-LAYER MODEL

TABLE I

P value is less than 0.05, we acknowledge that extracted
eigenvalues differ signiﬁcantly between seizure and non-
seizure movements. All features with P < 0.05 were used for
multivariate modeling. At last, we excluded 16 not important
features, and kept 43 useful features among all 59 fea-
tures using Python 3.5 and sklearn module, as shown in
Fig. 4. The top ﬁve important features in our study are the
iqr of ax, var of ax,
iqr of gx, mean of acct, and iqr
of ay.

E. Model Estimation and Validation

In this step, we constructed a two-layer stacking ensemble
machine learning model, called TLEM, in which Layer1 is the
base layer and Layer2 is the meta layer. First, four classiﬁers
on Layer1 were trained individually, and each of them would
have a single output (seizure or normal movement). Second,
using outputs from the classiﬁers on Layer1 as the input
to Layer2’s classiﬁer to make the ﬁnal prediction to clas-
sify these two types of moving segments (seizure movement
and non-seizure movement). The framework is shown in the
right-hand side of Fig. 5. This ensemble framework could
provide advantages such as a reduction in FP rates and better
precision, because it would outperform every single model,
and overcome the shortcomings of each individual model and
improve the ﬁnal prediction results by adjusting the weights
of each base learners according to the performances of each
base learner.

Layer1 uses four base learners: RF, extra trees (ETs), gra-
dient boosting decision trees (GBDT), and AdaBoost (ADB).

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply. 

DONG et al.: TWO-LAYER ENSEMBLE METHOD FOR DETECTING EPILEPTIC SEIZURES USING A SELF-ANNOTATION BRACELET

4005013

depending on whether the model reaches the best performance
on the validation dataset. Having a too small n will reduce the
number of events in the training sets, leading to under-training
of the model, while having a too big n will likely have too few
events in the test set where computing performance metrics
will be difﬁcult in case no events are present. We have tried
to conﬁrm this using different folds, and the results suggested
the use of the current n = 6, and the amount of training
dataset in this case for the overall model and the night model
would be 6000 and 650. To be more speciﬁc, Fig. 6 illustrates
that the TLEM for overall data and night data reaches the best
performance at around 6500 ((5/6) of overall training samples)
samples and around 650 ((5/6) of night training samples)
samples individually, because the train score curve and the
validation score curve match at those number of samples.

To further compare our proposed TLEM with other models,
we include ACU, recall/SEN, precision/positive predictive
value (PPV), and Fβ score. These metrics are computed by

⎧

⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩

accuracy =

recall =

precision =

TP + TN
TP + TN + FP + FN
TP
TP + FN
TP
TP + FP
(cid:5)
(cid:4)
1 + β 2

Fβ score =

· precision · recall

β 2 · precision + recall

(5)

Fig. 6. Learning curves of the proposed TLEM for epileptic seizure detection.
The blue line with round dots represents the ACU of training, and the red
line with triangles represents the ACU of validation, while the shadow around
the line represents the ACU range of the sixfold cross validation. (a) Meta-
layer model performance on overall data. (b) Meta-layer model performance
on night data.

building step as

Midscore =

meantrain + stdtrain
meanvalidation − stdvalidation

(4)

where meantrain and meanvalidation are the mean ACU of training
and validation, respectively, while stdtrain and stdvalidation are
the standard deviation of training and validation ACU scores,
respectively. The Midscore reaches 97.31% for the overall
model and 91.19% for the night model. Both the overall
seizure detection model and the night seizure detection model
acquire acceptable training results in this model validation
step.

where TP = true positive, which is the number of correctly
classiﬁed positive samples; FP = false positive, incorrectly
classiﬁed negative samples; TN = true negative, correctly clas-
siﬁed negative samples, and FN = false negative, incorrectly
classiﬁed positive samples.

ACU describes how many samples are classiﬁed correctly
in total, whether the sample is positive or negative. SEN
describes the proportion of actually positive samples that are
correctly classiﬁed as positive. PPV describes the proportion of
classiﬁed positive samples that are actually positive. F score is
also called balanced F score, and it is designed as a harmonic
average of precision and recall. Fβ score could better describe
the model performance even for an imbalanced dataset. In this
case, we focused more on the TP rate and FP rate, and FP
could cause more severe damage than FP, because FN could
lead to ignorance of seizures happening and miss the chance
to alarm the patient’s caregivers to aid. We set β = 2, which
means the importance of SEN is as twice as PPV, and higher
Fβ score means better performance.

We trained and tested two individual models separately
for overall data and night data and used the abovementioned
metrics to evaluate the performance of these trained models.

III. RESULTS

F. Performance Evaluation Metrics

In the abovementioned model validation step, we investi-
gated n-fold cross validation (assume n = 5/6/10) to train the
model for different cases (overall/night), while the value of n

Fig. 7(a) represents an automated detected seizure event,
while the start and stop times were automatically detected
by the abovementioned algorithm, and the seizure mark was
annotated by the patient or his/her caregiver using the red
mark button on the bracelet. Fig. 7(b) shows how nonmoving

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply. 

4005013

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022

Fig. 7. Moving segment extraction and data annotation. (a) Example of
an automatically detected moving segment. The start and stop times of the
detected movement are shown in green and black. The blue line showed when
the patient or his/her caregiver used the mark button, indicating that this is a
seizure event. (b) Nonmoving segments are excluded in this step, and then,
moving segments are annotated according to the marks.

Fig. 9. Confusion matrices of the base-layer classiﬁcations and the meta-layer
classiﬁcation. The results are acquired by applying each individual base-layer
classiﬁcation on the test dataset (ﬁrst to fourth confusion matrix) and applying
the ensemble two-layer classiﬁcation on the test dataset (ﬁfth confusion
matrix). Label 1: seizure and label 0: normal movement. (a) Confusion matrix
of overall model. (b) Confusion matrix of night model.

Fig. 8. Hours of recording data, 93.9% of which is nonmoving data, 5.9%
is non-seizure moving, and only 0.2% is seizure moving.

segments were excluded, and these nonmoving segments were
either totally excluded if it was too long (>10 s), or not
excluded if it was a short stop (<10 s) between long time
moving segments. The blue line highlighted the time when
the subject pressed the mark button. However, there might
be several seizures (less than twice in a day) that were not
properly annotated, mainly because the patient did not press
the mark button in time after the seizure, or there might
be some unstable movements before the button is pressed.
In these circumstances, the additional movement would be
recognized as a seizure, so we would check and remove
the incorrect labels and re-label the correct seizure event.
In this way, all seizure events and normal movement events are
preserved, and data without movement events (inactive data)
are excluded. As shown in Fig. 8, we excluded 93.9% inactive
data through this automated detection method and annotation
method.

In total, we have extracted 10 707 (lasting for 241.6 h) non-
seizure moving events and 547 (5.5 h) seizure events, among

which 806 non-seizure moving events (5.8 h) and 314 (2.4 h)
seizures happened at night.

The results showed that the TLEM model has better per-
formance in ACU, SEN, and Fβ score than using one-layer
models, which indicated that using our proposed ensemble
method could improve the performance. To compare using
a single model’s performance and our proposed ensemble
model’s performance, we trained every single model using the
same method as we trained the ensemble model. The trained
classiﬁers would make predictions on the testing dataset as
well. We used a confusion matrix describe the performances
of our proposed TLEM and other single models, as shown in
Fig. 9.

We used a total of 30% samples (3200 non-seizure events
and 177 seizures) to test the overall seizure detection of the
trained two-layer ensemble classiﬁcation model. At the same
time, we used 30% night samples (244 non-seizure events and
92 seizures) for night seizure model.

The test results for overall seizure detection show that a total
of 136 out of 177 seizure events (mean SEN 76.84%) seizure
events were detected, and 3149 (98.41%) of 3200 non-seizure
events were classiﬁed correctly with an FAR of 0.98/24 h (51
false alarm from seven patients), and the Fβ score reaches
0.7598. At night, the proposed model based on home-collected

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply. 

DONG et al.: TWO-LAYER ENSEMBLE METHOD FOR DETECTING EPILEPTIC SEIZURES USING A SELF-ANNOTATION BRACELET

4005013

PERFORMANCE OF EACH SINGLE CLASSIFIER AND THE PROPOSED TLEM
CLASSIFIER

TABLE II

data correctly identiﬁed 87 out of 92 night seizure events
(mean SEN 94.57%) and 220 out of 244 non-seizure events
(90.16%), with an FAR of 0.46/24 h (24 false alarm in seven
patients). The Fβ score is 0.9082, which further indicated the
effectiveness of the night epilepsy detection system.

The Fβ score of the night model is much higher than that of
the overall model, because movements that happened at night
are shorter and less complex than those that happened at the
daytime. According to the data we collected in this experiment,
normal movements that happened at night only contain turning
over in bed, go to the toilet, and other slight moves. Moreover,
the ratio of normal movements and seizures at night is 2:1, and
the proportion at daytime is 19:1, indicating a more severe
imbalance between these two classes at daytime. Thus, those
complex normal movements that happened in the daytime,
such as brushing teeth and exercising, could be misidentiﬁed
more often than simple normal movements that happened at
night. In the meanwhile, both our proposed TLEM reaches
highest Fβ score comparing with other single machine learning
models.

We compared our two-layer ensemble classiﬁcation model
with other single classiﬁers as we used in the ﬁrst layer, and
we found that our proposed ensemble model performed better
than GBDT, RF, ET, and ADB in most cases, especially for
ACU, SEN, and Fβ score. It is obvious that for both the overall
detection task and night detection task, our proposed two-layer
ensemble classiﬁcation model has kept the best performance.

IV. DISCUSSION

In this work, we designed a data collection method and
device used in the home, and the practicality of this method
was investigated and proved. Our proposed automated algo-
rithm EAMS could exclude nonmoving segments efﬁciently
while reducing the calculation quantity and accelerating the
operation efﬁciency in the following classify step. For the
exclusion step,
the thresholds were derived based on the
observation of our subjects, and it is detecting whether a
human being is moving or not. These thresholds are not
describing the typical seizures that our subjects are having, but
the normal daily movements and seizure-related movements,
therefore, we assume these thresholds could also be efﬁcient
in the application phase, which would be further validated in

our future study. However, there are several misannotations
during the marking step, which is mainly because the subjects
forgot to press the button after the seizure, or an exanimation
happened after the seizure. This situation happened less than
once a day, so such this will not cause a lot of errors of
annotation. In this case, we would recheck the data according
that moving
to the subject’s dairy recordings and relabel
segment as a seizure event. On the other hand, if duplicated
marks happened in a short time (<5 s), we would remove the
later mark manually.

The subjects included in this study are having convulsive
seizures lasting for 15 s, so we only kept segments lasting for
no less than 15 s in this manuscript, but this threshold could
be changed if we include different types of seizures in our
further study.

As shown in Fig. 4, we found that the iqrs of the 3-D
ACM, the 3-D gyroscopes, and the quaternions showed great
importance in this study, which means the ACC and angular
velocities that change in a large range during a period could
indicate a possible seizure in some way. When the subject
was having a seizure, his/her movement would change both
in the linear aspect and the rotational aspect. Moreover, the
variances of the 3-D ACM are also important in this study,
while the variances of the 3-D gyros showed less importance.
The variance reﬂects the mean degree of data dispersion,
so this result indicates that seizures could lead to random
changes in the linear motion, but not in the rotational motion.
The mean values of each axis (of the ACM and the gyroscope)
are not signiﬁcant to the detection. When the subject was
having seizures, the movement would result in changes of
both directions of an axis. Then, the minimum value would
change to a lower value (negative), and the maximum would
also change to a higher value (positive); therefore, the mean
value only changed slightly not too obvious. However, the
mean value of the total ACC (positive) is informative, which
is because the total ACC ignores the direction of moving and
only considers the ACC magnitude.

We proposed a TLEM approach to classify imbalanced
datasets of normal movement events and seizure events. More-
over, different types of normal movements were involved
in this study. Compared with the previous experiments [9]–
[13],
this dataset collecting procedure was mainly carried
outside the hospital account for the “real world” scenario.
Our proposed detecting method brings this study closer to a
real-life scenario for daily monitoring purposes. In this study,
features were extracted from each entire moving segment.
However, exploring other extraction methods, such as using
sliding window to extract features, will be interesting in the
future study, and this might be able to increase the feature
density, and this could be possibly a potential beneﬁt for the
future study.

The experimental results show that our proposed two-layer
ensemble method could effectively characterize epileptic over-
all and night seizures with the accuracies of 97.28% and
91.37%, and the SEN values of 76.84% and 94.57%, respec-
tively. Missed seizures might be caused by small amplitudes.
As the proportions of seizures are different during the day and
at night, it is necessary to establish a separate night seizure

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply. 

4005013

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022

COMPARISON OF OUR PROPOSED APPROACH WITH OTHER SINGLE-SENSOR-BASED SEIZURE DETECTION SYSTEM

TABLE III

detection model. We set the weight of seizure samples to
four that of the normal movement samples, and increasing
the weight of the seizure samples will lead to a higher TP rate
and, unfortunately, a higher FP rate.

As shown in Table II and Fig. 9, compared with the
single-layer classiﬁcation model, ﬁrst, our designed ensemble
classiﬁcation model has an SEN of 76.84%, which raised
by at most 55.15% performance of single classiﬁcation for
overall model, and has an SEN of 94.57%, which raised by
at most 22.99% performance of single classiﬁcation for night
model. The performance of simply using single classiﬁers is
not as good as our proposed method, which had a low fusion
complexity and reached a better performance. There were only
ﬁve seizures failed to be detected due to the subject’s arm,
which wore the bracelet was held by themselves and could
not move freely. This illustrates that this two-layer ensemble
classiﬁcation model could detect more seizure events while
still keep a low FAR.

As shown in Table III, compared with other studies, we col-
lected more seizure events in a free-living home environment
compared with the study of, for example, Nijsen et al. [14]
conducted in a hospital with only 153 seizures included, while
other mentioned studies have even fewer recordings. In other
words, our study is expected to provide more convincing
results as trained and tested on a larger dataset with more
data modalities. However, this could also lead to lower SEN
in the daytime, because more daily activities are included
in the dataset. The SEN of our approach in the nighttime
is the highest among all studies (to the best of the authors’
knowledge), and the SEN in daytime would be lower, because
many other daily activities (for example, doing sports or
house working) were included in the dataset. This would lead
to increasing chance of challenges in distinguishing seizure
movements from all other daily movements. We consider
having a relatively low SEN could be acceptable (when we
took care of the tradeoff between FAR and SEN), because,
as consistently observed that SUDEP happens more during
the night and the very early morning than the daytime [36].
Nevertheless, future work should focus on the challenge of
classifying seizure movements and movements caused by other
daily activities.

One limitation of this study is that only convulsive seizures
can be detected by motor sensors, because some seizures are

not clearly visible in the ACM and ANG signals. Besides one
single type of epileptic seizure detection, the classiﬁcation of
seizure types is more challenging due to the limited number of
multiple types of seizure data and subjects. The measurement
of the EMG and other signals might be useful to include
more types of seizures. EMG does not measure any movement
directly, but it illustrates muscle tones in tonic contractions,
so using both ACM and EMG sensors could include tonic
seizure type [16] into our proposed seizure detection system.
Besides wearable devices, non-contact sensors allow the sub-
ject to be free from wearing any device while still under
detection, and our group has designed a radar-based respiratory
rate and heart rate detection device [37] to use at night while
the subject was sleep, aiming to avoid night SUDEP. Moreover,
this night radar was designed as a non-contact method, which
means the subject does not have to wear any device while
sleeping. In our future study, we would use this non-contact
radar to detect seizures at night. And in our further study,
we would use wearable PPG, EMG, and ECG monitoring
devices to promote more types of seizures, such as non-
convulsive seizures. The ﬁrst version of our proposed device
has only motor sensors, and the heart rate will be integrated
in the future, and we do plan to conduct a study integrating
heart rate data. The use of heart rate combining with motor
data (e.g., ACMs) can boost the detection performance [38].
Another limitation of this study is that most of the subjects
had different numbers of seizures including some having only
a few seizures. Therefore, “leave patients out” approach would
cause clear limitation in model training, which might likely
lead to biasing the model to patients dominating the number of
seizures. In the real application to adopt our model, we could
potentially ask the users to press buttons to mark their seizures
in an early phase, and those marked data can be used to train a
model using our proposed algorithm. Nevertheless, we should
include more patients with more seizure events in the future
to develop a “patient-independent” algorithm, where no data
from the same patient were used for both training and testing.

V. CONCLUSION

In this study, we designed a bracelet with motor sensors to
help to monitor epileptics at home, which helps save labor
costs. The self-annotation mark button could help improve

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply. 

DONG et al.: TWO-LAYER ENSEMBLE METHOD FOR DETECTING EPILEPTIC SEIZURES USING A SELF-ANNOTATION BRACELET

4005013

the efﬁciency of labeling data. To extend, this mark button
could be used to improve the ACU of the detecting algorithm.
This proposed device is capable of detecting convulsive type
seizures lasting for over 15 s.

We proposed two main algorithms in this study; one is
the automatic active data selection method, namely, EAMS
algorithm, and the other is the two-layer ensemble classiﬁca-
tion method, namely, TLEM algorithm. The proposed selection
method helps to discard over 90% inactive data to speed up the
following data analyzing and classifying step. We also found
the proper amount for the proposed model to get the best
performance. The proposed classiﬁcation method is trained
well on 6000 samples and 650 samples for overall and night
models individually, and it
is validated on collected data
from patients using the bracelets we designed. The proposed
two-layer classiﬁcation is capable to deal with the imbalanced
dataset while combining the ﬁrst-layer base learners’ beneﬁts
and reaching an improved performance. The model detected
136 (76.83%) of 177 seizures in total, in which 87 (94.57%)
of 92 night seizures are recognized. Compared with single
classiﬁcation models, the proposed two-layer ensemble classi-
ﬁcation model shows the feasibility of automated detection
of convulsive seizures. Both overall and night model have
reached the best performance based on the proposed approach
with the size of the dataset with 6500 and 650 samples
individually.

In conclusion, the results suggest that this study can be used
for the automated seizure detection based on home-collection
methods with ACM and ANG data and is expected to con-
tribute to a complete wearable multisensor seizure detection
system.

REFERENCES

[1] L. Chang, “Progress in epidemiological

investigation of epilepsy in

China,” J. Int. Neurol. Neurosurg., vol. 39, no. 2, pp. 161–164, 2012.

[2] A. Neligan, G. S. Bell, S. D. Shorvon, and J. W. Sander, “Temporal
trends in the mortality of people with epilepsy: A review,” Epilepsia,
vol. 51, no. 11, pp. 2241–2246, Nov. 2010.

[3] J. van Andel, R. D. Thijs, A. de Weerd, J. Arends, and F. Leijten, “Non-
EEG based ambulatory seizure detection designed for home use: What
is available and how will it inﬂuence epilepsy care?” Epilepsy Behav.,
vol. 57, pp. 82–89, Apr. 2016.

[4] T. Tomson, T. Walczak, M. Sillanpaa, and J. W. A. S. Sander, “Sudden
unexpected death in epilepsy: A review of incidence and risk factors,”
Epilepsia, vol. 46, no. 11, pp. 54–61, Dec. 2005.

[5] C. Harden et al., “Practice guideline summary: Sudden unexpected death
in epilepsy incidence rates and risk factors,” Neurology, vol. 88, no. 17,
pp. 1674–1680, Apr. 2017.
[6] G. D. Cascino, “Clinical

indications and diagnostic yield of video-
electroencephalographic monitoring in patients with seizures and spells,”
Mayo Clinic Proc., vol. 77, no. 10, pp. 1111–1120, Oct. 2002.

[7] S. Lahmiri and A. Shmuel, “Accurate classiﬁcation of seizure and
from epileptic
seizure-free intervals of
patients,” IEEE Trans. Instrum. Meas., vol. 68, no. 3, pp. 791–796,
Mar. 2019.

intracranial EEG signals

[8] M. Kolodziej, A. Majkowski, R. J. Rak, and A. Rysz, “Detection
of spikes with deﬁned parameters in the ECoG signal,” IEEE Trans.
Instrum. Meas., vol. 68, no. 4, pp. 1045–1052, Apr. 2019.

[9] S. Beniczky, T. Polster, T. W. Kjaer, and H. Hjalgrim, “Detection of
generalized tonic-clonic seizures by a wireless wrist accelerometer: A
prospective, multicenter study,” Epilepsia, vol. 54, no. 4, pp. e58–e61,
Apr. 2013.

[10] G. T. Borujeny, M. Yazdi, A. Keshavarz-Haddad, and A. R. Borujeny,
“Detection of epileptic seizure using wireless sensor networks,” J. Med.
signals sensors, vol. 3, no. 2, pp. 63–68, 2013.

[11] S. Kusmakar, C. K. Karmakar, B. Yan, T. J. O’Brien, R. Muthuganap-
athy, and M. Palaniswami, “Automated detection of convulsive seizures
using a wearable accelerometer device,” IEEE Trans. Biomed. Eng.,
vol. 66, no. 2, pp. 421–432, Feb. 2019.

[12] K. Cuppens et al., “Accelerometry-based home monitoring for detection
of nocturnal hypermotor seizures based on novelty detection,” IEEE
J. Biomed. Health Informat., vol. 18, no. 3, pp. 33–1026, 2014.
[13] K. Cuppens, L. Lagae, B. Ceulemans, S. Van Huffel, and B. Vanrumste,
“Detection of nocturnal frontal lobe seizures in pediatric patients by
means of accelerometers: A ﬁrst study,” in Proc. Annu. Int. Conf.
IEEE Eng. Med. Biol. Soc., Minneapolis, MIN, USA, Sep. 2009,
pp. 6608–6611.

[14] T. M. E. Nijsen, R. M. Aarts,

and
P. A. M. Griep, “Time-frequency analysis of accelerometry data for
detection of myoclonic seizures,” IEEE Trans. Inf. Technol. Biomed.,
vol. 14, no. 5, pp. 1197–1203, Sep. 2010.

J. Cluitmans,

P.

[15] S. Beniczky, I. Conradsen, and P. Wolf, “Detection of convulsive
seizures using surface electromyography,” Epilepsia, vol. 59, pp. 23–29,
Jun. 2018.

[16] I. Conradsen, S. Beniczky, P. Wolf, J. Henriksen, T. Sams, and
H. B. D. Sorensen, “Seizure onset detection based on a uni-or multi-
modal intelligent seizure acquisition (UISA/MISA) system,” in Proc.
Annu. Int. Conf. IEEE Eng. Med. Biol., Aug. 2010.

[17] J. van Andel, C. Ungureanu, R. Aarts, F. Leijten, and J. Arends,
“Using photoplethysmography in heart rate monitoring of patients with
epilepsy,” Epilepsy Behav., vol. 45, pp. 142–145, Apr. 2015.

[18] S.

Singh, M. Kozlowski,

and
E. Rodriguez-Villegas, “Proof of concept of a novel neck-situated
wearable PPG system for continuous physiological monitoring,” IEEE
Trans. Instrum. Meas., vol. 70, pp. 1–9, 2021.

I. Garcia-Lopez, Z.

Jiang,

[19] A. van Westrhenen, T. De Cooman, R. H. C. Lazeron, S. Van Huffel, and
R. D. Thijs, “Ictal autonomic changes as a tool for seizure detection: A
systematic review,” Clin. Autonomic Res., vol. 29, no. 2, pp. 161–181,
Apr. 2019.

[20] J. Jeppesen et al., “Seizure detection based on heart rate variability
using a wearable electrocardiography device,” Epilepsia, vol. 60, no. 10,
pp. 2105–2113, Oct. 2019.

[21] K. Vandecasteele et al., “Automated epileptic seizure detection based on
wearable ECG and PPG in a hospital environment,” Sensors, vol. 17,
no. 10, p. 2338, Oct. 2017.

[22] G. Regalia, F. Onorati, M. Lai, C. Caborni, and R. W. Picard, “Multi-
modal wrist-worn devices for seizure detection and advancing research:
Focus on the empatica wristbands,” Epilepsy Res., vol. 153, pp. 79–82,
Jul. 2019.

[23] J. B. A. M. Arends, “Movement-based seizure detection,” Epilepsia,

vol. 59, pp. 30–35, Jun. 2018.

[24] J. Arends et al., “Multimodal nocturnal seizure detection in a residential
care setting,” Neurology, vol. 91, no. 21, pp. e2010–e2019, Nov. 2018.
[25] U. Kramer, S. Kipervasser, A. Shlitner, and R. Kuzniecky, “A novel
portable seizure detection alarm system: Preliminary results,” J. Clin.
Neurophysiol., vol. 28, no. 1, pp. 8–36, 2011.

[26] J. Lockman, R. S. Fisher, and D. M. Olson, “Detection of seizure-like
movements using a wrist accelerometer,” Epilepsy Behav., vol. 20, no. 4,
pp. 638–641, Apr. 2011.

[27] D. Pascual, A. Aminifar, and D. Atienza, “A self-learning methodology
for epileptic seizure detection with minimally-supervised edge labeling,”
in Proc. Design, Autom. Test Eur. Conf. Exhib. (DATE), Mar. 2019,
pp. 764–769.

[28] J. Bidwell, T. Khuwatsamrit, B. Askew, J. A. Ehrenberg, and S. Helmers,
“Seizure reporting technologies for epilepsy treatment: A review of
clinical information needs and supporting technologies,” Seizure, vol. 32,
pp. 109–117, Nov. 2015.

[29] I. Conradsen, P. Wolf, T. Sams, H. B. D. Sorensen, and S. Beniczky,
“Patterns of muscle activation during generalized tonic and tonic-clonic
epileptic seizures,” Epilepsia, vol. 52, no. 11, pp. 2125–2132, Nov. 2011.
[30] S. Luca et al., “Detecting rare events using extreme value statistics
applied to epileptic convulsions in children,” Artif. Intell. Med., vol. 60,
no. 2, pp. 89–96, Feb. 2014.

[31] D. Johansson et al., “Tonic-clonic seizure detection using accelerometry-
based wearable sensors: A prospective, video-EEG controlled study,”
Seizure, vol. 65, pp. 48–54, Feb. 2019.

[32] T. M. Khoshgoftaar, M. Golawala, and J. V. Hulse, “An empirical study
of learning from imbalanced data using random forest,” in Proc. 19th
IEEE Int. Conf. Tools Artif. Intell. (ICTAI), Oct. 2007, pp. 310–317.

[33] C. Dong et al., “Home-based detection of epileptic seizures using a
bracelet with motor sensors,” in Proc. 10th Int. IEEE/EMBS Conf. Neural
Eng. (NER), May 2021, pp. 854–857.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply. 

4005013

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 71, 2022

[34] A.

Sjøberg,

Sveier, A. M.

“Applied
Runge–Kutta–Munthe-Kaas integration for the quaternion kinematics,”
J. Guid., Control, Dyn., vol. 42, no. 12, pp. 2747–2754, Dec. 2019.
[35] Y. Freund and R. E. Schapire, “Experiments with a new boosting
algorithm,” in Proc. 13th Int. Conf. Mach. Learn., Bari, Italy, Jul. 1996,
pp. 148–156.

and O.

Egeland,

[36] B. S. Purnell, R. D. Thijs, and G. F. Buchanan, “Dead in the night:
Sleep-wake and time-of-day inﬂuences on sudden unexpected death in
epilepsy,” Frontiers Neurol., vol. 9, p. 1079, Dec. 2018.

[37] W. Hu, Z. Zhao, Y. Wang, H. Zhang, and F. Lin, “Noncontact accurate
measurement of cardiopulmonary activity using a compact quadrature
Doppler radar sensor,” IEEE Trans. Biomed. Eng., vol. 61, no. 3,
pp. 725–735, Mar. 2014.

[38] J. van Andel et al., “Multimodal, automated detection of nocturnal motor
seizures at home: Is a reliable seizure detector feasible?” Epilepsia Open,
vol. 2, no. 4, pp. 424–431, Dec. 2017.

Chunjiao Dong received the B.S. degree from
the Department of Electronic Science and Technol-
ogy, Harbin Institute of Technology, Harbin, China,
in 2017. She is currently pursuing the Ph.D. degree
with the Institute of Microelectronics of the Chinese
Academy of Sciences (IMECAS), University of Chi-
nese Academy of Sciences, Beijing, China.

She is a visiting Ph.D. with the Eindhoven Uni-
versity of Technology, Eindhoven, The Netherlands.
Her research interests include biosensor and multi-
modal biological signal process and analysis.

Tianchun Ye (Member, IEEE) received the B.S.
from
degree in semiconductor microelectronics
Fudan University, Shanghai, China, in 1986.

He is currently the Director of the Institute of
Microelectronics of the Chinese Academy of Sci-
ences, Beijing, China, where he is involved in studies
on IC fabrication technology, novel devices, and
microfabrication. As a subject principal and key
backbone, he has completed a dozen of research sub-
jects, which are supported by the 7th-10th Five-Year
National Key Technologies Research and Develop-
ment Program, the National Climbing Project, “863” Project, “973 Program,”
and the Project of Knowledge Innovation Program, Chinese Academy of
Sciences. His research interests include IC design and application, nano-
fabrication, and novel devices.

Xi Long (Senior Member, IEEE) was born in China,
in 1983. He received the B.Eng. degree in electronic
information engineering from Zhejiang University,
Hangzhou, China, in 2006, and the M.Sc. and Ph.D.
(cum laude) degrees in electrical engineering from
the Eindhoven University of Technology (TU Eind-
hoven), Eindhoven, The Netherlands, in 2009 and
2015, respectively.

From 2010 to 2011, he was with Tencent, Shen-
zhen, China, where he was involved in data mining
and user research. He has ten years of research
and development experience in healthcare industry, with Philips Research,
Eindhoven, where he is currently a Senior Scientist and the Full Contract
Scan (FCS) Artiﬁcial Intelligence (AI) Lead with the Department of Personal
and Preventive Care. He is also an Assistant Professor with TU Eindhoven
and an Associate Professor with the Department of Electrical Engineering,
TU Eindhoven. His research interests include signal processing and machine
learning in healthcare and biomedicine applications. He has published more
than 80 articles and reports in these ﬁelds, and his inventions led to more
than ten patent applications.

Dr. Long received the Best Student Paper Award from the IEEE Bioinfor-
matics and Bioengineering (BIBE) Conference and the First Runner-Up Paper
Award from the IEEE Biomedical and Health Informatics (BHI) Conference
in 2012.

Ronald M. Aarts (Fellow,
IEEE) received the
B.S. degree in electrical engineering, and the Ph.D.
degree in physics from the Delft University of Tech-
nology, Delft, The Netherlands, in 1977 and 1995,
respectively.

He joined the Optics Group, Philips Research
Laboratories (formerly known as the NatLab), Eind-
hoven, The Netherlands, in 1977 and initially inves-
tigated servos and signal processing for use in both
video long play players and compact disc players.
He has been a part-time Full-Professor with the
Eindhoven University of Technology (TU Eindhoven), Eindhoven, since 2006,
where he is mainly involved in supervising the master and Ph.D. students.
He has been the President of Aarts Consultancy (Adviesbureau Aarts) since
1990. He is currently a Professor with the Department of Electrical Engineer-
ing, TU Eindhoven. His research interests include acoustics and engineering
to medicine and biology in particular sensors, signal processing, and systems
for ambulatory and unobtrusive-monitoring, sleep, cardiology, perinatal, drugs
response monitoring (DRM), and epilepsy detection.

Johannes P. van Dijk (Senior Member, IEEE)
the Department of
is currently the Head of
the Sleep and Epilepsy Centre,
Clinical Physics,
Kempenhaeghe, Heeze, The Netherlands, a Senior
Researcher with the Department of Orthodontics,
University of Ulm, Ulm, Germany, and a Senior
Guest Researcher with the Eindhoven University
of Technology, Eindhoven, The Netherlands. His
research interests include the ﬁeld of clinical neuro-
physiology using (high density) electromyography,
electroencephalogram, and application of (unobtru-

sive) sensors in epilepsy and sleep disorders.

Chunheng Shang was an Assistant Researcher with the Institute of Micro-
electronics of the Chinese Academy of Science, Beijing, China. She is cur-
rently with Beijing Shunyuan Kaihua Technology Company Ltd., Beijing. She
is also a Senior Algorithm Engineer with Zepp Health, Hefei, China, where
she is involved in working on algorithm development for various wearable
devices, including smart watches, smart sleep monitor, and non-contact radar
monitor in the past seven years. Her research interests include sensor data
analysis and processing, machine learning, and deep learning algorithms in
wearable devices.

Xiwen Liao is currently an Assistant Researcher
with the Institute of the Chinese Academy of Sci-
ence, Beijing, China, where he is mainly involved in
the development of wearable medical electronics and
medical information management, and so on. He had
developed non-contact sign monitors, epilepsy mon-
itoring wristbands based on multiple physiological
parameters. He had published papers six papers and
more than ten patent applications.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply. 

DONG et al.: TWO-LAYER ENSEMBLE METHOD FOR DETECTING EPILEPTIC SEIZURES USING A SELF-ANNOTATION BRACELET

4005013

Lei Chen is currently a Neurologist and a Pro-
fessor with the Neurology Department, West China
Hospital, Sichuan University, Chengdu, China. She
has published more than 100 articles. Her research
interests include etiology, mechanisms, and diagno-
sis of epilepsy. This work has included studies of
the medical therapy to epilepsy, role of noncoding
RNA in refractory epilepsy, brain imaging studies of
epilepsy, and metabolic mechanisms of epilepsy.

Prof. Chen has received several

international
awards including the American Academy of Neurol-
ogy (AAN) International Scholarship Award (2015), the American Federation
for Medical Research (AFMR) Henry Christian Award (2015), and the
Japanese Epilepsy Society International Scholarship Award (2009).

Wei Chen (Senior Member, IEEE) received the
B.Eng. and M.Eng. degrees in telecommunication
systems and smart sensor systems from the School of
Electrics and Information Engineering, Xi’an Jiao-
tong University, Xi’an, China, in 1999 and 2002,
respectively, and the Ph.D. degree in performance
monitoring and impairment mitigation for optical
communication systems from the Department of
Electrical and Electronics Engineering, The Uni-
versity of Melbourne, Melbourne, VIC, Australia,
in 2007.

She worked as an Intern with Bell Laboratories, Munich, Germany, and
Alcatel-Lucent, Stuttgart, Germany, in 2005. From 2007 to 2015, she was an
Assistant Professor with the Eindhoven University of Technology, Eindhoven,
The Netherlands. Since 2015, she has been a Full Professor and the Director
of the Center for Intelligent Medical Electronics (CIME), Department of
Electronic Engineering, School of Information Science and Technology, Fudan
University, Shangai, China. Her research interests include the multidisciplinary
areas of wireless sensor systems, patient health monitoring, ambient intelligent
system design, and digital signal processing for performance optimization. The
application areas include neonatal monitoring, elderly care, smart rehabilita-
tion, interactive, and cognitive environments.

Dr. Chen is the Managing Editor of the IEEE Reviews in Biomedical
Engineering (R-BME). She is an Associate Editor of the IEEE JOURNAL OF
BIOMEDICAL HEALTH INFORMATICS (JBHI) and the IEEE TRANSACTIONS
ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING (TNSRE).

Wanlin Lai received the B.S. degree in clinical
medicine and the M.S. degree in neurology from the
West China Hospital, Sichuan University, Chengdu,
China, in 2017 and 2020, respectively, where she is
currently pursuing the Ph.D. degree. She received
her doctor qualiﬁcation in 2018 and her medical
doctor practicing license in 2020.

Her research interests include clinical and scien-
tiﬁc aspects of epilepsy, particularly the interaction
between female epilepsy and sex hormones and
seizure attack warning.

Yunfeng Wang received the B.S. degree in micro-
electronics from Xidian University, Xi’an, China,
in 2004, and the Ph.D. degree in microelectron-
ics and solid-state electronics from the Institute of
Microelectronics of the Chinese Academy of Sci-
ences, Beijing, China, in 2009.

He is currently an Associate Professor with the
Institute of Microelectronics of the Chinese Acad-
research interests
emy of Sciences. His current
include analog and RF circuit design for low-power
wireless communications, biomedical circuits and
systems, and wearable healthcare and its enabling ultra-low-power design and
technology.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:16:05 UTC from IEEE Xplore.  Restrictions apply.
