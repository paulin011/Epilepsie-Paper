# Zia et al. - 2021 - Detection of Generalized Tonic Clonic Seizures and Falls in Unconstraint Environment Using Smartphon

Received January 28, 2021, accepted February 28, 2021, date of publication March 4, 2021, date of current version March 16, 2021.

Digital Object Identifier 10.1109/ACCESS.2021.3063765

Detection of Generalized Tonic Clonic Seizures
and Falls in Unconstraint Environment Using
Smartphone Accelerometer

SHAFAQ ZIA , (Graduate Student Member, IEEE), ALI NAWAZ KHAN , (Member, IEEE),
KHURRAM SHABIH ZAIDI, AND SHAN E ALI
Department of Electrical and Computer Engineering, COMSATS University Islamabad, Lahore Campus, Lahore 54000, Pakistan

Corresponding author: Shafaq Zia (s.zia@ieee.org)

This work was supported by the Higher Education Commission Pakistan through the National Research Program for Universities under
Grant 8355/NRPU/R&D/HEC/2017.

ABSTRACT The detection of Generalized Tonic Clonic Seizures (GTCS) and Falls is of utmost importance
due to the increase in prevalence of epilepsy and Sudden Death in Epileptic Patients during CoVID-19
pandemic, and prevention of serious injuries in Fall risk groups such as elderly requiring continuous
monitoring for disease management and assisted living etc. Monitoring of Activities of Daily Living (ADLs)
can assist in the detection of symptoms and onset of neurological disorders such as Alzheimer’s, stroke, and
epileptic seizures. With a host of embedded sensors, improved memory, enhanced processing capabilities and
availability to masses, smartphones can be used for Human Activity Recognition (HAR) through continuous
monitoring of ADLs. This paper presents a tri-axial accelerometer-based approach to detect and classify
activities performed by individuals by applying machine learning algorithms including RF, J48, NB, LMT
and SVM to movement data. Movement data is collected in real-time from the embedded accelerometer of
a smartphone worn by individual on upper-left arm in unconstraint environment. It is pre-processed using
time and frequency domain analysis and spatial domain features are computed. Supervised machine learning
techniques are applied to classify ADLs into ﬁve classes based on the intensity of movements: Stationary,
Light Ambulatory, Intense Ambulatory, GTCS and Falls. We also used training data from MyNeuroHealth
dataset collected from 23 individuals including epilepsy patients. Based on gathered results, Random
Forest outperforms other classiﬁers with classiﬁcation accuracy of 99.6% for stationary, 81.5% for light
ambulatory, 99.8% for intense ambulatory and GTCS, and 97.2% for Falls corresponding to training data
of 14000 samples. To date, activity classiﬁcation in our system has been implemented on cloud instead
of mobile phone application as subjects are using smartphones with dissimilar software and hardware
speciﬁcations for assisted living applications.

INDEX TERMS Accelerometer, activity recognition, biomedical signal processing, assisted living, machine
learning.

I. INTRODUCTION
Human Activity Recognition (HAR) through wearable sen-
sors is gaining attention due to progress in automated fea-
ture extraction, classiﬁcation, mobile and cloud computing
for a number of applications [1], [2]. HAR is an ability to
interpret human body gesture or motion via sensors such
as accelerometer sensors, heart rate monitors and EEG etc.
to determine type of activity or action accordingly [3]. HAR

The associate editor coordinating the review of this manuscript and

approving it for publication was Jingchang Huang

.

is one of the most active research areas with its applica-
tions in human computer interaction, healthcare, and secu-
rity surveillance [4]–[6]. The accuracy of automated HAR
is enhanced by using data from environmental and body
worn sensors. In environmental sensing, sensors are placed
in the surrounding environment of the person. Therefore,
the detection of human activity depends on the person’s
interaction with the sensors. The sensor data can be collected
in a constraint environment where the patient is lying or
sitting in an idle state under controlled conditions or uncon-
straint environment i.e., without laboratory conditions, while

39432

This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

VOLUME 9, 2021

S. Zia et al.: Detection of GTCS and Falls in Unconstraint Environment

the body worn sensors are attached to the person who is
expected to perform different tasks [7]. Sensed data is used
to characterize the activities into different classes based on
ambulation, orientation, localization, and other appropriate
classiﬁcations depending on the type and frequency of the
activity being performed and recorded [8]. Furthermore, there
are different approaches to use body worn sensors, placed
in and on different parts of the individual’s body; including
waist, wrists, and thighs, to achieve a higher level of accuracy.
Recently, smartphones are being extensively used to detect
human behaviour using the inbuilt sensors like accelerometer,
gyroscopes, microphone, proximity, light intensity sensor,
and camera, etc. [5], [6].

The main goal of HAR is to have the ability to detect and
classify the basic Activities of Daily Living (ADLs) such
walking, running, eating, sedentary activities, ofﬁce work etc.
However, it offers a level of difﬁculty due to sensor motion,
its placement, background management, and variations in the
way activities are performed by an individual [9]. Monitoring
of various ADLs is employed in treating various neurolog-
ical disorders, detection of Falls and eventually helping to
improve quality of life of individuals with various health
issues [4], [5]. It is to be noted that several ADLs have com-
mon postures and levels of ambulation and it is very difﬁcult
to classify these activities correctly. For example, deskwork
and having breakfast both require a subject to be in stationary
sitting posture. In order to simplify the decision-making pro-
cess, activities can be grouped together on the basis of move-
ment into stationary class, light ambulatory class, intense
ambulatory class, and abnormal class [1]. Data of an individ-
ual’s body parameters can be extracted using wearables and
mobile devices and it can be further processed for the clas-
siﬁcation of ADLs using machine learning algorithms and
deep learning such as Convolutional Neural Network (CNN),
K-Nearest Neighbor (KNN), Decision Trees (DT), Pruned
Decision tree (J48), Random Forest (RF), Logistic Model
Trees (LMT), Bayesian Network (BN), Naïve Bayes (NB),
Multilayer Perception (MLP),
Instance Based Learning
(IBL), and Support Vector Machine Learning (SVM) [9].
Mentioned Machine Learning classiﬁers and deep learning
techniques can be used to improve the classiﬁcation and
detection accuracy of HAR, and abnormal activities including
seizure and Fall detection [2], [10].

Random Forest (RF) is a supervised machine learning
algorithm employing a large ensemble of decision trees and
it can be used for classiﬁcation and regression problems.
Several trees are originated from bootstrapped original data
sets. It can easily handle a dataset with a large number of
dimensions, and it is suitable for feature selection as it assigns
an importance score to every feature based on the best binary
split. Accelerometer data with respect to time is highly vary-
ing and with reference to [6], [11], [12], a trend is observable
that RF is outperforming other classiﬁers and it is going to
perform well for the detection of HAR using accelerometer.
Epilepsy is a neurological disorder that directly affects the
nervous system. It is also known as seizure disorder which is

diagnosed when a subject experiences one or two unprovoked
seizure attacks within 24 hours. Seizures in epilepsy are
caused by irregular activity of the electrical pulses of brain or
disruption of communication between neurons [13]. It is third
most common neurological disease, and more than ﬁfty mil-
lion people are suffering from epilepsy around the world [14].
Sudden Unexpected Death in Epileptic Patients (SUDEP) is
the leading cause of death in patients suffering from epilepsy.
It inﬂuences individuals of all age groups generally causing
SUDEP fatalities (0.3-6) in every one of thousand individuals.
In addition, SUDEP is also responsible for 8-12% of deaths
in epileptic patients [15]. Epileptic seizures can be classiﬁed
into motor or non-motor seizures based on the movement
intensity such as Generalized Tonic-Clonic Seizures (GTCS)
seizures that occur when there is a disturbance in both sides of
the brain leading to unconsciousness and a series of jerking
movements. Frequency of the GTCS is the most important
risk factor for SUDEP [16].

There have been many causes of injuries among elderly
and Falls are one of those. Over 64 people suffer at least one
Fall per year out of 28% to 35% of the population [17], [18].
Fall incidents are becoming a major health care problem
for elderly people with the percentage constantly increas-
ing in the elderly population who live alone. Falls are also
the leading cause of deaths for the elderly people who are
over 65 years old and the annual incidence is approximately
35% [19], [20]. Falls may have serious consequences, but
mostly emergency situations are not directly caused by Falls
rather by lack of timely assistance and treatment [21]. Further
damage caused by Fall can be prevented by sending an imme-
diate alarm to the caregiver of an elderly person reducing
the treatment costs and increasing the recovery opportunities.
Therefore, it is of utmost importance and necessity to develop
a reliable, convenient, accurate, and automated Fall detection
system [22].

GTCS and Fall detection has gained considerable research
impetus recently due to prevalence and deployment of
e-health care solutions. This topic has become more relevant
in the prevailing COVID-19 pandemic as continuous lock-
down, monitory, social and societal losses, depression, and
anxiety associated with the uncertainty of the pandemic has
increased the number of reported emergency instances by
neurological patients many folds [23], [24].

It has also been evident that 18-38% COVID-19 sufferers
have neurological symptoms [25]. Clinicians do not know
how common these neurological effects are. As per a recent
report in nature [26], it is expected that 0.4 to 0.2% of the
people are to face neurological complications as a result of
COVID-19 and given that the current number of infections
are of the order of 100 million worldwide, we can expect
that between 200,000 and 400,000 people have experienced
neurological disorders as a consequence of the pandemic.

Existing research on the automated detection of GTCS and
Falls is hampered by lack of customized data sets and clas-
siﬁers pertaining to unconstraint environments. To the best
of our knowledge, no other data set exists in public domain

VOLUME 9, 2021

39433

TABLE 1. Available datasets collected using accelerometer.

S. Zia et al.: Detection of GTCS and Falls in Unconstraint Environment

which has been collected in an unconstraint environment
using wearable sensors to identify the anomalies in ADLs
and their long-term manifestation as neurological disorders.
In subsequent sections, we explain the basis and feasibility
of a method that uses 3D Accelerometer data collected in
an unconstraint environment from individuals performing
different ADLs. Collected Data is pre-processed using time
and frequency domain analysis for observing patterns in ADL
classes. Furthermore, the data is used to classify the activi-
ties into ﬁve categories: stationary, light ambulatory, intense
ambulatory, GTCS, and Fall using supervised machine learn-
ing classiﬁers such as J48, RF, LMT, NB, and SVM. These
classiﬁers are implemented and compared to identify the
most suitable classiﬁer detection of ADLs, GTCS and Falls.
Table 1 shows the summary of available datasets collected
using accelerometer, activities performed by the volunteers,
samples, number of subjects, and the environment in which
the dataset was collected.

II. RELATED WORK
An accelerometer is a device that can detect changes in
velocity and directions in x, y and z planes. Since seizures
and Fall manifest an abnormal movement of limbs and body
among subjects, 3-D accelerometers are used as motion
sensors in the detection of motor seizures and Falls. The
main challenge is to detect the difference between regular
ADLs and abnormal activities. Accelerometers can be used
to detect ongoing motor seizures but due to their inherent
dependency on the changes in movement, they might generate
false classiﬁcations in the absence of motor phenomena [7].
For example, a subject experiencing absence seizure might be
classiﬁed as someone performing stationary activities if the
decision is made solely on accelerometer data. A comparison
of relevant work done on HAR using wearable sensors based
on ADLs, type and placement of sensors, features, classiﬁers,
and classiﬁcation accuracy is presented in Table 2.

Automatic detection of ADLs, epileptic seizures, and
Falls require systems which makes use of certain sen-
sors for the collection of data such as Accelerometer,

Electrocardiogram (ECG), Electroencephalogram (EEG),
Magnetometers, Photoplethysmography (PPG), etc. These
sensors are either employed in unimodal or multi-
modal approach for seizure and Fall detection. Video-
Electroencephalography technique is considered to be the
gold standard for detection of epilepsy and stroke. However,
it requires trained technicians to record video-EEG that is
reviewed by medical experts for conﬁrmation. Whereas,
monitoring systems which use wearable 3D Accelerometer
devices detect seizures and Falls efﬁciently with reasonable
accuracy [34], [35]. By analyzing the data with appropri-
ate machine learning classiﬁers, a seizure and Fall can be
detected timely to prevent injuries or sudden death. The
known classiﬁers for HAR and detection of ADLs using
3-axis accelerometer includes Rule-Based machine learning,
Decision Trees, Bayes Networks, and SVM [36], [37].

Pannurat et al. proposed in [36] that position of wearable
sensors does affect the classiﬁcation accuracy of e-health care
system used for the detection of neurological disorders and
Ambient Assisted Living (ALL). They investigated the clas-
siﬁcation accuracy by placing the sensors on ankles, wrist,
upper side of arm, thighs, head, chest, waist, waist front and
waist side. Furthermore, machine learning techniques such
BN, NB, J48, Partial Tree Rule Learning, MLP, IBL, KNN,
and SVM were explored. It was concluded that waist side,
waist front and chest are the best sensor positions by using NB
achieving an accuracy of more than 96% for three mentioned
optimal positions. While 1NN perform exceptionally for the
sensors placed at thigh and achieved an accuracy of 99%.

In [4],

tri-axial accelerometer data is collected from
35 healthy individuals performing ADLs including jumping,
lying down, sitting, walking, Falls, etc. Spatial frequency
domain features were extracted from the data and a ﬁnal
feature vector was generated as the concatenation of the
computed features. The extracted vector was used to train
machine learning model for the detection of ADLs and
Falls. The classiﬁcation methods were designed in two dif-
ferent ways; classiﬁcation into 7 activity classes and binary
classiﬁcation into Fall and No Fall. Supervised machine

39434

VOLUME 9, 2021

S. Zia et al.: Detection of GTCS and Falls in Unconstraint Environment

TABLE 2. Summary of related work.

learning techniques including KNN, SVM, Linear Discrim-
inant Analysis and DT used for the classiﬁcation of ADLs
and Falls led to a higher classiﬁcation F1-score of 98.41%
for the binary approach instead of multi-class classiﬁcation
approach. Whereas the multi-class approach was proven to be
slightly better for Fall detection with a sensitivity of 99.05%.
A trial to detect Tonic Clonic seizures was conducted
in [38], tri-axial accelerometers were attached to both wrists
of the patients who were undergoing Video-EEG. False Pos-
itive Rate (FPR) and sensitivity are used as a performance
parameter learned through the Linear Kernel Support Vector
Machine (LKSVM), Random Forest (RF) and K-Nearest
Neighbors (KNN). KNN performed best by attaining a sensi-
tivity of 100% and RF did well in terms of False Positive Rate
(FPR) and attained an FPR of 0.01 FPR/h. Jose R. Villar et al.
suggested a 3D-accelerometer based non-invasive seizure
detection system in [39]. A 3D-accelereometer was placed
on the wrist of an epileptic patient for the detection of
Myoclonic seizure stimulated movements of upper limb and
lower limb. Principal Component Analysis (PCA), Locally
Linear Embedding and a distance based PCA are used for
extracting features from the collected data. The extracted
features are used for training machine learning model using
KNN and DT to detect seizures accurately. PCA-based meth-
ods outperformed others by achieving the geometric mean
of 98.43 %. Table 2 gives a detailed summary of existing
methods for detection of ADLs, seizures and Falls.

III. METHODOLOGY
The proposed system uses 3D-accelerometer data collected
from the smartphone of the user in order to classify activities
into 5 different classes. The data gathered is pre-processed
to extract spatial domain features such as mean, variance and

standard deviation. The time and frequency domain features
help us analyze the trends of various ADLs, Seizures and
Falls for further classiﬁcation of the activities using Machine
Learning Classiﬁers. The proposed methodology for accurate
detection of ADLs is presented in Figure 1.

A. DATA COLLECTION
Proposed system includes the collection of data from the
user using MyNeuroHealth application. The architecture of
the application is presented in [8]. The application uses
accelerometer in the mobile device to collect data from the
patient’s body. It had been noted that as operating systems
tend to regulate the sampling rate of embedded accelerome-
ters and these results in nonuniformly sampled data. During
data collection we noticed that the operating system changed
the sampling rate from 8 samples/sec to 20 samples/sec based
on previously recorded acceleration values and the battery
power levels. So, the data is pre-processed in real-time to
maintain a uniform sampling rate of 15 samples/sec through
linear interpolation. The resulting data is stored in a remote
database alongside user’s mobile device. Using our devel-
oped application, we have collected the data for all activities
that are listed in the UCI dataset used in [44]. All recorded
activities were performed in an unconstraint environment and
data is collected by 11 volunteers suffering from neurological
disorders and 12 healthy individuals. Collected dataset is
available at IEEE DataPort [45] and the comparison of both
datasets is given in Table 3. The mobile device was worn
by the mentioned 11 patients for a long duration of time
and from that we segmented the accelerometer data of ictal
state. All volunteers were required to perform ADLs, and they
were also asked to simulate Falls while performing various
ADLs.

VOLUME 9, 2021

39435

S. Zia et al.: Detection of GTCS and Falls in Unconstraint Environment

FIGURE 1. Overview of the proposed methodology for detection of activities.

TABLE 3. Summary of datasets [2].

FIGURE 2. Placement of mobile phone for recording of data from the
volunteers.

B. DATA PRE-PROCESSING
Abnormalities can be detected by monitoring different pat-
terns of daily activities, seizure attacks and Falls. According
to the Table 1, time and frequency domain analysis can be
used for pattern recognition and extracting respective features
for classiﬁcation. The recorded 3D accelerometer signal from
MyNeuroHealth consisted of a 3-dimensional vector with a
sampling frequency of 15Hz, each component corresponding
to each of the three axes x, y, and z respectively. The various
computed features for the trend detection of ADLs, GTCS
and Fall are deﬁned below. Where i is the corresponding x, y
and z of accelerometer, n are the samples of the time series
and N is 500 which represents the total number of samples of
a single ADL.

1) PLACEMENT OF THE MOBILE PHONE
The data is collected with the mobile phone placed at the
upper-left arm of the individual as represented in Figure 2.
The device is placed on upper left arm to avoid any discomfort
that may hinder the activity performance as the most stable
part of the body is upper torso [46]. The x, y and z acceleration
data for a particular activity can also be visualized in Figure 3.

39436

VOLUME 9, 2021

S. Zia et al.: Detection of GTCS and Falls in Unconstraint Environment

data is used for further processing and classiﬁcation. The
instances are further labelled according to four different
classes described in [1] and the idea of classiﬁcation is
already presented in [47]. The classiﬁcation of the activities
according to their classes are presented in the Table 4 based
on the patterns and intensity of movement involved in each
activity.

TABLE 4. Classification of activities [1] [47].

FIGURE 3. Transition of activity from walking to Falling, the red lines
represent the segment of Fall with a duration of 3 seconds.

1) MEAN
Mean (µ) of the tri-axial accelerometer is computed using the
following equation.

µ (Acci) =

1
N

N
(cid:88)

n=1

Acci,n

(1)

2) VARIANCE
Variance (σ 2) of the tri-axial accelerometer is computed
using (2).

σ 2 (Acci) =

1
N

N
(cid:88)

n=1

(Acci,n−µ (Acci))2

(2)

3) STANDARD DEVIATION
Standard deviation (σ ) of the tri-axial accelerometer is com-
puted using the following equation.

σ (Acci) =

(cid:118)
(cid:117)
(cid:117)
(cid:116)

1
N

N
(cid:88)

n=1

(Acci,n−µ (Acci))2

(3)

4) FREQUENCY ANALYSIS
The signal of each ADL contains some unique dominant
frequencies and a magnitude belonging to each frequency.
Based on the fundamental frequencies and their magnitudes
of a signal, ADLs can be recognized. The data acquired
using accelerometer is processed using Fast Fourier Trans-
form (FFT) and respective frequencies are observed.

The thresholds for different activity classes are based on
trend detection techniques. The classiﬁed activities along
with their calculated spatial domain parameters are stored in
the remote database and user’s mobile devices. The stored

5) TRANSITIONAL ACTIVITIES
Given the nature of Fall, it is likely that a subject may
encounter Falling while performing ADLs such as working,
walking, jogging, or driving etc. The activity will transit from
a regular ADL to a Fall as shown in Figure 3. It is necessary
to ﬁnd the epoch of the activity to be extracted and for this
purpose resolution of the sensory data can be improved by
subtracting data values from its previous index. This can be
achieved by using delta modulation [48].

C. MODEL TRAINING AND CLASSIFICATION
UCI dataset and the data collected using MyNeuroHealth is
used for model training and further collected activities using
MyNeuroHealth are used for real-time testing. As per the
sampling rate, each activity contains 500 data samples of x, y,
and z acceleration, respectively. The data after pre-processing
is used for training three models with increasing the number
of samples per activity in training data to achieve the best
possible accuracy of detection. The training models are then
validated using 10-fold cross validation and further the model
is tested against the ﬁve classes of activities. Accuracies of
training and testing of the data are compared against different
machine learning classiﬁers including RF, NB, LMT, J48 and
SVM. The breakdown of the training models is presented in
the Table 5.

IV. RESULTS
The data gathered is processed using time and frequency
domain analysis to identify a difference in trend between
the activity classes. Training models are tested in terms of
accuracy of classiﬁcation for ADLs through Machine Learn-
ing Classiﬁers and tested against each activity as discussed
below.

A. TREND DETECTION
Mean, Variance and Standard deviation of the collected data
is presented in Table 6. From the table it can be clearly seen

VOLUME 9, 2021

39437

TABLE 5. Breakdown of training datasets.

that Seizure exhibits signiﬁcant difference in the features with
respect to other ADLs. Whereas it is difﬁcult to distinguish
between activities that belong to the same class and exhibit

TABLE 6. Spatial domain features of activities.

S. Zia et al.: Detection of GTCS and Falls in Unconstraint Environment

similar movement intensity such as stationary class activities
of Watching TV and Having Meal have signiﬁcant correla-
tion. The difference in the trends of different ADLs, GTCs
and Falls can be observed by time and frequency domain
plots. The results can be observed in Figure 4, characterizing
sitting by frequencies between 0 to 1 Hz, Figure 5 shows
dominant frequencies of light ambulatory activity i.e., 1 to
2 Hz, Figure 6 shows intense ambulatory can be categorized
by the frequency between 2 to 3 Hz, GTCS is characterized
by frequencies between 4 Hz to 6 Hz as seen in Figure 7 and
Figure 8 shows the time and frequency domain results of Fall
with dominant frequencies between 0.5 and 1.5Hz.

B. MODEL TRAINING AND CLASSIFICATION
Data sets obtained from different ADLs are processed in
WEKA and machine learning algorithms are applied for
classiﬁcation of activities to achieve maximum accuracy.
For further validation of the training models, 10-fold cross

FIGURE 4. Time and Frequency domain representation of stationary activity (sitting).

39438

VOLUME 9, 2021

S. Zia et al.: Detection of GTCS and Falls in Unconstraint Environment

FIGURE 5. Time and Frequency domain representation of light ambulatory activity (stairs up and down).

FIGURE 6. Time and Frequency domain representation of intense ambulatory activity (jogging).

FIGURE 7. Time and Frequency domain representation of GTCS.

validation is applied, and accuracies of different classiﬁers
are compared. Test sets are supplied to the trained model
and accuracy of detection of each ADL, GTCs and Fall
is computed using different classiﬁers and a comparison is
presented in terms of accuracy of detection.

From Figure 9(a), we conclude that

training model
accuracy using Random Forest Classier results in 100%.
Figure 9(b) shows confusion matrix of 10-fold cross vali-
dation of the training data with Random forest classiﬁer,
it results in 80% of detection accuracy with a certain overlap

VOLUME 9, 2021

39439

S. Zia et al.: Detection of GTCS and Falls in Unconstraint Environment

FIGURE 8. Time and Frequency domain representation of Fall.

TABLE 7. Training model accuracies (%).

TABLE 9. Machine learning performance metrics (Weighted AVG.).

TABLE 8. 10-FOLD cross validation accuracies (%).

TABLE 10. Stationary activity test set.

of Intense Ambulatory ADL with Light Ambulatory and
GTCS has signiﬁcant overlapping data with Intense ambu-
latory. In Figure 9(c), we observe the classiﬁcation of Light
Ambulatory has signiﬁcant overlap with stationary as the
movement intensities of both activities are similar at certain
data points, this results in difﬁculty during detection of that
ADL and accuracy is affected.

Similarly, the accuracies of the training models presented
in Table 5 are computed using RF, J48, LMT, NB and SVM
and the summary of Training Models and 10-fold Cross Vali-
dation is presented in Table 7 and Table 8, respectively. From
the tables it can be observes that as we increase the samples
from 9000 to 14000 there is a less signiﬁcant difference in
the accuracies of training models and their validation. Table 9

shows the weighted average of the performance metrics for
training model with 14000 samples. The values of preci-
sion, recall, and F-measure shows that RF performs better in
comparison to other machine learning algorithms used as it
classiﬁed all instances correctly.

1) SINGLE ACTIVTITY TEST SETS
After validation of training model, each ADL, GTCS and Fall
is supplied as a test set to the training model and accuracies
are observed corresponding to RF, J48, NB, LMT and SVM.
The summary of stationary, light ambulatory, intense ambu-
latory, GTCS and Fall as a test set is presented in Table 10,
11, 12, 13, and 14 respectively. From the tables, it can be
concluded that RF is giving the best accuracy of detection

39440

VOLUME 9, 2021

S. Zia et al.: Detection of GTCS and Falls in Unconstraint Environment

TABLE 11. Light ambulatory test set.

TABLE 12. Intense ambulatory test set.

TABLE 13. GTCS Test set.

TABLE 14. Fall activity test set.

FIGURE 9. Confusion matrices for Random Forest Classifier for
classification of St. (Stationary), LA (Light Ambulatory), Intense
Ambulatory (IA), Falls and GTCS with training model 14000, (a) Training
Model, (b) 10-fold cross validation, (c) Test data of LA (walking).

for each of the respective activities and the model with
14000 data samples outperforms the other two in terms of
detection accuracy.
VOLUME 9, 2021

V. IMPLEMENTED MODEL
Figure 10 shows our implemented system to date. The data
is transferred to the cloud for classiﬁcation of the activities
and the results are sent back to the application as subjects
were using phones with dissimilar hardware and software
speciﬁcations as listed in Table 15.

With all

the evidence provided earlier regarding the
accuracies of classiﬁcation using various machine learning
algorithms, we conclude that a complete health care frame-
work for the detection and classiﬁcation of GTCS and Falls
may be implemented on the mobile phone which can perform
in app processing on the sensed accelerometry data with the
deployment of our trained model.

39441

S. Zia et al.: Detection of GTCS and Falls in Unconstraint Environment

[5] N. Hegde, M. Bries, T. Swibas, E. Melanson, and E. Sazonov, ‘‘Automatic
recognition of activities of daily living utilizing insole-based and wrist-
worn wearable sensors,’’ IEEE J. Biomed. Health Informat., vol. 22, no. 4,
pp. 979–988, Jul. 2018.

[6] Y. Chen and C. Shen, ‘‘Performance analysis of smartphone-sensor behav-
ior for human activity recognition,’’ IEEE Access, vol. 5, pp. 3095–3110,
2017.

[7] S. Ramgopal, S. Thome-Souza, M. Jackson, N. E. Kadish, I. Sánchez
Fernández, J. Klehm, W. Bosl, C. Reinsberger, S. Schachter, and
T. Loddenkemper, ‘‘Seizure detection, seizure prediction, and closed-loop
warning systems in epilepsy,’’ Epilepsy Behav., vol. 37, pp. 291–307,
Aug. 2014.

[8] S. Zia, A. N. Khan, M. Mukhtar, M. Ahmad, J. Shahid, and M. Sohail,
‘‘MyNeuroHealth: A healthcare application for the detection of motor
seizures,’’ in Proc. IEEE Consumer Commun. Netw. Conf., Las Vegas, NV,
USA, 2020, pp. 1–6.

[9] J. Rafferty, C. D. Nugent, J. Liu, and L. Chen, ‘‘From activity recognition to
intention recognition for assisted living within smart homes,’’ IEEE Trans.
Human-Machine Syst., vol. 47, no. 3, pp. 368–379, Jun. 2017.

[10] C. Xu, D. Chai, J. He, X. Zhang, and S. Duan, ‘‘InnoHAR: A deep neural
network for complex human activity recognition,’’ IEEE Access, vol. 7,
pp. 9893–9902, 2019.

[11] M. Muzammal, R. Talat, A. H. Sodhro, and S. Pirbhulal, ‘‘A multi-sensor
data fusion enabled ensemble approach for medical data from body sensor
networks,’’ Inf. Fusion, vol. 53, pp. 155–164, Jan. 2020.

[12] S. Mehrang, J. Pietilä, and I. Korhonen, ‘‘An activity recognition frame-
work deploying the random forest classiﬁer and a single optical heart rate
monitoring and triaxial accelerometer wrist-band,’’ Sensors, vol. 18, no. 3,
p. 613, Feb. 2018.

[13] P. O. Shafer. (Feb. 27, 2020). About epilepsy: The basics. Epilepsy Founda-
tion and Epilepsy Together. Accessed: Oct. 11, 2020. [Online]. Available:
https://www.epilepsy.com/learn/about-epilepsy-basics

[14] A. W. C. Yuen, M. R. Keezer, and J. W. Sander, ‘‘Epilepsy is a neurological
and a systemic disorder,’’ Epilepsy Behav., vol. 78, pp. 57–61, Jan. 2018.
[15] T. A. Manolis, A. A. Manolis, H. Melita, and A. S. Manolis, ‘‘Sudden
unexpected death in epilepsy: The neuro-cardio-respiratory connection,’’
Seizure, vol. 64, pp. 65–73, Jan. 2019.

[16] T. Tomson, R. Surges, R. Delamont, S. Haywood, and D. C. Hesdorffer,
‘‘Who to target in sudden unexpected death in epilepsy prevention and
how? Risk factors, biomarkers, and intervention study designs,’’ Epilepsia,
vol. 57, pp. 4–16, Jan. 2016.

[17] World Health Organization. (2008). WHO Global Report on Falls Pre-
vention in Older Age. Accessed: Oct. 2, 2020. [Online]. Available:
https://www.who.int/ageing/projects/falls_prevention_older_age/en/
[18] E. Casilari, J. A. Santoyo-Ramón, and J. M. Cano-García, ‘‘UMAFall: A
multisensor dataset for the research on automatic fall detection,’’ Procedia
Comput. Sci., vol. 110, pp. 32–39, Jan. 2017.

[19] C.-Y. Hsieh, K.-C. Liu, C.-N. Huang, W.-C. Chu, and C.-T. Chan, ‘‘Novel
hierarchical fall detection algorithm using a multiphase fall model,’’ Sen-
sors, vol. 17, no. 2, p. 307, Feb. 2017.

[20] C. Taramasco, T. Rodenas, F. Martinez, P. Fuentes, R. Munoz, R. Olivares,
V. H. C. De Albuquerque, and J. Demongeot, ‘‘A novel monitoring system
for fall detection in older people,’’ IEEE Access, vol. 6, pp. 43563–43574,
2018.

[21] G. Baldewijns, G. Debard, G. Mertes, T. Croonenborghs, and
B. Vanrumste,
‘‘Improving the accuracy of existing camera based
fall detection algorithms through late fusion,’’ in Proc. 39th Annu. Int.
Conf. IEEE Eng. Med. Biol. Soc. (EMBC), Seogwipo, South Korea,
Jul. 2017, pp. 2667–2671.

[22] P. Jatesiktat and W. T. Ang, ‘‘An elderly fall detection using a wrist-
worn accelerometer and barometer,’’ in Proc. 39th Annu. Int. Conf.
IEEE Eng. Med. Biol. Soc. (EMBC), Seogwipo, South Korea, Jul. 2017,
pp. 125–130.

[23] L. Ferini-Strambi and M. Salsone, ‘‘COVID 19 and neurological disorders:
Are neurodegenerative or neuroimmunological diseases more vulnera-
ble?’’ J. Neurol., vol. 1, no. 11, pp. 1–20, 2020.

[24] S. L. Xiangliang Chen, O. A. Onur, N. N. Kleineberg, G. R. Fink,
F. Schweitzer, and C. Warnke, ‘‘A systematic review of neurological symp-
toms and complications of COVID-19,’’ J. Neurol., vol. 1, no. 11, pp. 1–20,
2020.

[25] A. Makda, S. Kumar, A. Kumar, V. Kumar, and A. Rizwan, ‘‘The frequency
of neurological symptoms in COVID-19 patients at a tertiary care hospital
in Pakistan,’’ Cureus, vol. 12, no. 9, p. 10360, Sep. 2020.

[26] M. Marshall, ‘‘How COVID-19 can damage the brain,’’ Nature, vol. 585,

no. 7825, pp. 342–343, Sep. 2020.

VOLUME 9, 2021

FIGURE 10. A Healthcare Framework for Automated Detection of GTCS
and Falls.

TABLE 15. Smartphones used for data collection.

VI. CONCLUSION
Smartphone accelerometer can be used for detection and
classiﬁcation of ADLs, GTCS and Falls to prevent any conse-
quences of Fall or seizures leading to death or serious injuries.
It is concluded that data from wearable sensors collected in
an unconstraint environment, can be used for accurate clas-
siﬁcation of ADLs and abnormalities leading to neurological
disorders. In the work presented, data from MyNeuroHealth
application is pre-processed and further classiﬁed based on
their movement trends. Based on the results of classiﬁcation
of different activities using RF, J48, LMT, NB and SVM
classiﬁers, it is shown that RF performs 16% better than other
classiﬁers for detection of GTCS and 22% in detecting Fall.
It is observed that there is a certain overlap between the data
points of light ambulatory and stationary activity, and the
detection accuracy of light ambulatory is therefore minimum
i.e. 81.5109% using RF classiﬁer. Future work includes the
integration of RF in MyNeuroHealth app and improvement
in the detection accuracies by inclusion of more sensors such
as heart rate, EEG, skin conductivity etc. in decision making
process and the release of stand-alone application to facilitate
patients suffering from neurological disorders.

REFERENCES

[1] C. A. Ronao and S.-B. Cho, ‘‘Human activity recognition with smartphone
sensors using deep learning neural networks,’’ Expert Syst. Appl., vol. 59,
pp. 235–244, Oct. 2016.

[2] S. Zia, A. N. Khan, M. Mukhtar, S. E. Ali, J. Shahid, and M. Sohail,
‘‘Detection of motor seizures and falls in mobile application using machine
learning classiﬁers,’’ in Proc. IEEE Int. Conf. Ind. 4.0, Artif. Intell., Com-
mun. Technol. (IAICT), Bali, Indonesia, Jul. 2020, pp. 62–68.

[3] O. Chin Ann and L. Bee Theng,

‘‘Human activity recognition:
A review,’’ in Proc. IEEE Int. Conf. Control Syst., Comput. Eng. (ICCSCE),
Batu Ferringhi, Malaysia, Nov. 2014, pp. 389–393.

[4] T. Althobaiti, S. Katsigiannis, and N. Ramzan, ‘‘Triaxial accelerometer-
based falls and activities of daily life detection using machine learning,’’
Sensors, vol. 13, no. 3777, p. 20, 2020.

39442

S. Zia et al.: Detection of GTCS and Falls in Unconstraint Environment

[27] M. Saleh, M. Abbas, and R. B. Le Jeannes, ‘‘FallAllD: An open dataset
of human falls and activities of daily living for classical and deep learning
applications,’’ IEEE Sensors J., vol. 21, no. 2, pp. 1849–1858, Jan. 2021.
[28] J. Gupta, M. Kumar, R. Duggal, and N. Gupta. (Nov. 12, 2020).
Dataset
IEEE
human
DataPort. Accessed: Feb. 12, 2020. [Online]. Available: https://ieee-
dataport.org/documents/dataset-iot-assisted-human-posture-recognition

IoT assisted

recognition.

posture

for

[29] P. Casale, O. Pujol, and P. Radeva, ‘‘Personalization and user veriﬁcation
in wearable systems using biometric walking patterns,’’ Pers. Ubiquitous
Comput., vol. 16, no. 5, pp. 563–580, Jun. 2012.

[30] G. M. Weiss, K. Yoneda, and T. Hayajneh, ‘‘Smartphone and smartwatch-
based biometrics using activities of daily living,’’ IEEE Access, vol. 7,
pp. 133190–133202, 2019.

[31] E. Casilari, J. A. Santoyo-Ramón, and J. M. Cano-García, ‘‘UMAFall: A
multisensor dataset for the research on automatic fall detection,’’ Procedia
Comput. Sci., vol. 110, pp. 32–39, Jan. 2017.

[32] M. Malekzadeh, R. G. Clegg, A. Cavallaro, and H. Haddadi.
(Nov. 14, 2019). MotionSense Dataset. GitHub. Accessed: Dec. 2, 2020.
[Online]. Available: https://github.com/mmalekzadeh/motion-sense
[33] B. Bruno, F. Mastrogiovanni, and A. Sgorbissa, ‘‘Dataset for ADL recog-
nition with wrist-worn accelerometer data set,’’ in Proc. IEEE Int. Conf.
Automat. Sci. Eng. (CASE), Karlsruhe, Germany, 2012, pp. 156–161.
[34] T. De Cooman, C. Varon, A. Van De Vel, K. Jansen, B. Ceulemans,
L. Lagae, and S. Van Huffel, ‘‘Adaptive nocturnal seizure detection
using heart rate and low-complexity novelty detection,’’ Seizure, vol. 59,
pp. 48–53, Jul. 2018.

[35] G. Santos, P. Endo, K. Monteiro, E. Rocha, I. Silva, and T. Lynn,
‘‘Accelerometer-based human fall detection using convolutional neural
networks,’’ Sensors, vol. 19, no. 7, p. 1644, Apr. 2019.

[36] N. Pannurat, S. Thiemjarus, E. Nantajeewarawat, and I. Anantavrasilp,
‘‘Analysis of optimal sensor positions for activity classiﬁcation and appli-
cation on a different data collection scenario,’’ Sensors, vol. 17, no. 4,
p. 774, Apr. 2017.

[37] A. Özdemir and B. Barshan, ‘‘Detecting falls with wearable sensors using
machine learning techniques,’’ Sensors, vol. 14, no. 6, pp. 10691–10708,
Jun. 2014.

[38] D. Johansson, F. Ohlsson, D. Krýsl, B. Rydenhag, M. Czarnecki,
N. Gustafsson, J. Wipenmyr, T. McKelvey, and K. Malmgren, ‘‘Tonic-
clonic seizure detection using accelerometry-based wearable sensors: A
prospective, video-EEG controlled study,’’ Seizure, vol. 65, pp. 48–54,
Feb. 2019.

[39] J. R. Villar, M. Menéndez, E. de la Cal, J. Sedano, and V. M. González,
‘‘Identiﬁcation of abnormal movements with 3D accelerometer sensors for
seizure recognition,’’ J. Appl. Log., vol. 24, pp. 54–61, Nov. 2017.
[40] M. M. Hassan, M. Z. Uddin, A. Mohamed, and A. Almogren, ‘‘A robust
human activity recognition system using smartphone sensors and deep
learning,’’ Future Gener. Comput. Syst., vol. 81, pp. 307–313, Apr. 2018.
[41] S. Kusmakar, C. K. Karmakar, B. Yan, T. J. O’Brien, R. Muthuganapathy,
and M. Palaniswami, ‘‘Automated detection of convulsive seizures using a
wearable accelerometer device,’’ IEEE Trans. Biomed. Eng., vol. 66, no. 2,
pp. 421–432, Feb. 2019.

[42] V. Bojanovsky, S. Byrne, P. Kirwan, I. Cleland, and C. Nugent, ‘‘Evaluation
of fall and seizure detection with smartphone and smartwatch devices,’’
in Proc. Int. Conf. Ubiquitous Comput. Ambient Intell., Philadelphia, PA,
USA, 2017, pp. 275–286.

[43] A. Gumaei, M. M. Hassan, A. Alelaiwi, and H. Alsalman, ‘‘A hybrid
deep learning model for human activity recognition using multimodal body
sensing data,’’ IEEE Access, vol. 7, pp. 99152–99160, 2019.

[44] M. Daniela, M. Marco, and P. Napoletano, ‘‘UniMiB SHAR: A new dataset
for human activity recognition using acceleration data from smartphones,’’
Appl. Sci., vol. 7, no. 10, p. 1101, 2017.

[45] S. Zia, A. N. Khan, S. E. Ali, M. Mukhtar, J. Shahid, and M. Sohail.
(May 23, 2020). Myneurohealth dataset: Activities of daily living, simu-
lated falls and seizure attacks. IEEE DataPort. Accessed: May 23, 2020.
[Online]. Available: https://ieee-dataport.org/documents/myneurohealth-
dataset-activities-daily-living-simulated-falls-and-seizure-attacks

[46] N. Amini, M. Sarrafzadeh, A. Vahdatpour, and W. Xu, ‘‘Accelerometer-
based on-body sensor localization for health and medical monitoring appli-
cations,’’ Pervas. Mobile Comput., vol. 7, no. 6, pp. 746–760, Dec. 2011.
[47] S. E. Ali, A. N. Khan, S. Zia, and M. Mukhtar, ‘‘Human activity recognition
system using smart phone based accelerometer and machine learning,’’ in
Proc. IEEE Int. Conf. Ind. 4.0, Artif. Intell., Commun. Technol. (IAICT),
Bali, Indonesia, Jul. 2020, pp. 69–74.

[48] A. Pilloni, M. Franceschelli, A. Pisano, and E. Usai, ‘‘Delta modulation
((cid:49)-M) via second-order sliding-mode control technique,’’ Control Eng.
Pract., vol. 92, Nov. 2019, Art. no. 104129.

VOLUME 9, 2021

SHAFAQ ZIA (Graduate Student Member, IEEE)
received the B.S. degree in Electrical (Telecommu-
nication) Engineering from COMSATS Univer-
sity Islamabad (CUI), Lahore Campus, Pakistan,
collaboration with Lancaster University, U.K.,
in 2018, where she is currently pursuing the M.Sc.
degree in Electrical Engineering. She has worked
as a Research Assistant on a funded project by
Higher Education Commission Pakistan under the
National Research Program for Universities with
the Department of Electrical and Computer Engineering, CUI Lahore. Her
research interests include signal processing, human activity recognition,
machine learning, and e-health.

ALI NAWAZ KHAN (Member, IEEE) received
the B.S. degree in Electrical Engineering from
the University of Engineering and Technology,
Lahore, Pakistan, in 2003, and the Ph.D. degree
in Information and Communication Engineering
from the Harbin Institute of Technology, Harbin,
in 2008. He is currently an Assistant
China,
Professor with the Department of Electrical and
Computer Engineering, COMSATS University
Islamabad, Pakistan. He is also the Head of the
Wireless Sensor Networks Research Group and supervises graduate and post
graduate research in the areas of mobile networks, mobile healthcare appli-
cations, wireless sensor networks, and energy efﬁcient mac protocols. He
is an Active Reviewer of several internationally abstracted journals and a
Program Committee Member of Frontiers of IT Conference (2009 onwards).

in 2000,

KHURRAM SHABIH ZAIDI received the B.Sc.
degree in Electrical Engineering from the Uni-
versity of Engineering and Technology, Lahore,
Pakistan,
the M.Sc. degree in Infor-
mation and Communication Engineering from
the University of Leicester, U.K., in 2008, and
the Ph.D. degree from the Universiti Teknologi
Petronas (UTP), Malaysia, in 2018. He is cur-
rently a Research Ofﬁcer with UTP. He is currently
working as an Assistant Professor with the Electri-
cal and Computer Engineering Department, COMSATS University Islam-
abad, Lahore Campus, Pakistan. He has done a number of experiments
and projects related to over the horizon maritime wireless communication.
His research interests include IoT devices, backhaul communication, data
analytics, wireless communication and data communication networks, non-
intrusive load monitoring, electric circuits and electronic devices, and wire-
less network security. His expertise includes the availability and capacity
prediction and calculations for data communication. He has provided con-
sultancy to a RF and baseband design house called Plextek, Cambridgeshire,
U.K., for two months, in 2016. He also owns a Patent on ‘‘Trans-horizon
wireless communication system using the tropospheric evaporation duct.’’
US20190296801A1 - 2019-09-26.

received the bachelor’s degree
SHAN E ALI
(Computer) Engineering from
in Electrical
the COMSATS University Islamabad, Pakistan,
in 2015, where he is currently pursuing the M.Sc.
degree in Electrical Engineering. At COMSATS
University Islamabad, Lahore, he worked as a
Research Assistant under Higher Education Com-
mission (HEC) research program on a project for
one year and is a part of the Wireless Sensor
Networks Research Group. He conducted research
on biosensors and electrode fabrication at Svenska Cellulosa AB (SCA),
Gothenburg, Sweden. His research interests include artiﬁcial intelligence,
deep learning, biosensors, electrode fabrication, and the Internet of Things.

39443
