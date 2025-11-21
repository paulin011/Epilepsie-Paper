# Lu et al. - 2025 - UKF-Based Model Parameter Estimation to Localize the Seizure Onset Zone in ECoG

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 9, SEPTEMBER 2025

6613

UKF-Based Model Parameter Estimation to
Localize the Seizure Onset Zone in ECoG

Junfeng Lu , Donghui Zhang , Kunlin Guo , Kunying Meng, Denghai Wang , Kai Lu ,
, Rui Zhang , Hong Wan , and Mingming Chen

Renping Yu , Lifang Yang, Mengmeng Li

Abstract—Drug-resistant epilepsy (DRE) patients typ-
ically require surgical
intervention or neurostimulation.
Therefore, accurate localization of the seizure onset zone
(SOZ) is essential for effective clinical
intervention. Al-
though some physiologically meaningful parameters of
neural computational models show substantial differences
across brain regions during seizures, few studies pay at-
tention to applying these model parameters to SOZ local-
ization. To investigate whether the parameter can be used
for accurate SOZ localization, the unscented kalman ﬁlter
(UKF) is employed to estimate the excitatory-inhibitory bal-
ance parameter c from the Z6 neural computational model
using DRE patients’ electrocorticography (ECoG). The re-
sults indicate that this parameter follows a unimodal distri-
bution during the pre-ictal period and the post-ictal period,
while exhibiting a bimodal distribution during the ictal pe-
riod. Then, the distribution of this parameter is combined
with machine learning methods, and a bagged tree classi-
ﬁer is constructed to localize the SOZ. The classiﬁcation
results demonstrate that the classiﬁer based on parameter
distributions exhibits excellent performance, particularly
during the post-ictal period, with an average accuracy of
91.60% . Interestingly, SOZ localization is more accurate
when no lesions are detected on magnetic resonance imag-
ing (MRI) compared to when lesions are present. Finally,
the model parameter distributions of the SOZs are utilized
to predict the outcome of epilepsy surgery. Of note, the
results demonstrate that the parameter distribution accu-
rately predicts surgical outcomes with an average accu-
racy of 92.56% . These ﬁndings suggest that the distribu-
tion of neural computational model parameters may serve
as biomarkers for SOZ localization and epilepsy surgery
outcome prediction, providing valuable support and assis-
tance for clinical decision-making.

Received 14 September 2024; revised 23 January 2025; accepted
16 May 2025. Date of publication 21 May 2025; date of current version
9 September 2025. This work was supported in part by the National
Natural Science Foundation of China under Grant 62173310, in part by
MOST 2030 Brain Project under Project 2022ZD0208500, and in part by
the Technology Project of Henan Province under Grant 242102311015
and Grant 222102310031. (Corresponding authors: Hong Wan; Ming-
ming Chen.)

All ECoG data used in this article are acquired from the HUP iEEG
Epilepsy Dataset (https://openneuro.org/datasets/ds004100/versions/1.
1.3).

The authors are with the Henan Key Laboratory of Brain Science and
Brain–Computer Interface Technology, School of Electrical and Infor-
mation Engineering, Zhengzhou University, Zhengzhou 450001, China
(e-mail: wanhong@zzu.edu.cn; mmchen@zzu.edu.cn).
Digital Object Identiﬁer 10.1109/JBHI.2025.3572204

Index Terms—Drug-resistant epilepsy, ECoG, parameter
distribution, machine learning, seizure onset zone (SOZ)
localization.

I. INTRODUCTION

E PILEPSY is a chronic neurological disorder caused by

abnormal electrical discharges in brain neurons, charac-
terized by recurrent seizures [1]. The impact of epilepsy ex-
tends beyond the physical harm experienced during seizures,
encompassing long-term psychological and cognitive effects
as well [2], [3]. Currently, antiepileptic drugs are the most
commonly used treatment for epilepsy. However, approximately
30% of patients are unable to achieve effective seizure control
through medication alone, and this type of epilepsy is known
as drug-resistant epilepsy (DRE) [4]. With the deepening under-
standing of epilepsy, surgical interventions and neurostimulation
therapies have become feasible options for DRE patients [5], [6].
In the clinical diagnosis and treatment of epilepsy, particularly
in surgical interventions for DRE, accurately identifying the
seizure onset zone (SOZ) is crucial for developing a surgical
plan and preserving the patient’s neurological functions [7], [8].
Currently, researchers have proposed various strategies and
tools for localizing SOZ through analysis of electroencephalog-
raphy (EEG), including methods such as neural fragility [9],
cross-frequency coupling [10], high-frequency oscillations [11],
and dynamic networks [12], which have played a critical role in
clinical pre-surgical evaluations and treatment decision-making.
In recent years, as intracranial electroencephalography (iEEG)
offers higher spatial resolution, better signal quality, and cov-
erage of deep brain regions [13], researchers have increasingly
employed iEEG, or combined EEG with iEEG, to study epilepsy,
showing great potential for SOZ localization. iEEG encom-
passes two primary techniques: electrocorticography (ECoG)
and stereo-electroencephalography (SEEG) [14]. Speciﬁcally,
ECoG records brain activity by placing electrode grids or strips
directly on the cortical surface, while SEEG employs depth elec-
trodes implanted in the brain to capture electrical activity from
deep brain structures. Despite these advances, many of these
studies do not provide a clear and comprehensive representation
of the underlying excitatory and inhibitory processes occurring
in the brain during seizures, which are crucial for understanding
seizure dynamics and SOZ localization.

Beyond studies based on clinical experimental data,
researchers often explore the physiological mechanisms of neu-

2168-2194 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies.
Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html
for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:33 UTC from IEEE Xplore.  Restrictions apply. 

6614

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 9, SEPTEMBER 2025

rological disorders such as epilepsy from the perspective of
neural computational models. These models can dynamically
simulate the real-time changes in brain activity, with several
model parameters having electrophysiological signiﬁcance, and
their adjustment allows for ﬁtting complex electrophysiological
signals. Neurophysiologically, it has been well established that
signiﬁcant changes in both excitability and inhibition occur
during the epileptic evolution [15], [16]. Moreover, there are
distinct differences in the excitability of SOZs compared to other
brain regions [17], [18]. Hence, neural computational model
parameters reﬂecting physiological states, such as excitability,
hold potential as biomarkers for SOZ localization. Integrating
these computational models with clinically recorded EEG or
ECoG signals, and accurately estimating the model parameters
from neural signals, is crucial for SOZ localization.

In recent years, various methods have been applied to pa-
rameter estimation in differential models, such as the least
squares method [19], genetic algorithms [20], Bayesian opti-
mization [21], Kalman ﬁlter (KF) [22], and variational infer-
ence [23]. Compared to traditional Kalman ﬁltering methods,
the unscented kalman ﬁlter (UKF) is better suited for handling
highly nonlinear problems and can dynamically capture changes
in neural signals in real time. These characteristics make it par-
ticularly advantageous for neural computational models, such
as the JR model [24] and the Wendling model [25], especially
when managing complex dynamic parameters. The parameters
estimated by UKF in neural computational models have nu-
merous applications, such as detecting epileptic seizures [26],
developing control strategies for epilepsy [27], and exploring
the mechanisms of seizure onset and propagation [28]. How-
ever, despite the extensive use of model parameters in epilepsy
research, few studies have employed these parameters for the
localization of the SOZ.

This study aims to combine the excitatory-inhibitory bal-
ance parameter in a neural computational model estimated by
the UKF with machine learning algorithms to achieve high-
performance of SOZ localization, thereby to provide effec-
tive support for decision-making in clinical epilepsy surgery.
First, UKF is used to estimate the parameters of the simulated
epileptic-like signals. The estimated parameters exhibit a high
degree of consistency with the preset parameters, demonstrat-
ing the feasibility of utilizing UKF in neural signal parame-
ter estimation. Subsequently, UKF is applied to estimate the
model parameters with ECoG collected from DRE patients,
and the parameter distributions are used as features to build a
bagged tree classiﬁer model for SOZ localization. The results
indicate that the model performs well in the three periods,
with better classiﬁcation performance in the post-ictal period.
In the post-ictal period, the accuracy is 91.60%, and the area
under the curve (AUC) is 96.43% . Further analysis shows that
SOZ classiﬁcation improves signiﬁcantly in patients without
magnetic resonance imaging (MRI) lesion status compared to
those with lesions. More importantly, the model can successfully
predict surgical outcomes based on SOZ parameter distributions,
achieving an accuracy of 92.56% . These ﬁndings suggest that
the distribution of model parameters could serve as a potential
biomarker for SOZ localization, providing auxiliary support for
medical decision-making in epilepsy.

Fig. 1. Examples of selected and excluded ECoG channels. The light
blue, red, and dark blue curves represent the ECoG signals during the
pre-ictal, ictal, and post-ictal periods, respectively. The black dashed
lines indicate the boundaries between different seizure periods. A, a
selected channel. B, an excluded channel with obvious defects. C, an
excluded SOZ without signiﬁcant seizure characteristics.

II. MATERIALS AND METHODS

A. ECoG Data and Preprocessing

The ECoG data used in this work are acquired from
the HUP iEEG Epilepsy Dataset created by the Hospital of
the University of Pennsylvania (https://openneuro.org/datasets/
ds004100) [29]. This dataset includes preoperative intracranial
electroencephalography (iEEG) recordings from 58 DRE pa-
tients, comprising ECoG from 20 DRE patients and SEEG from
38 DRE patients. Speciﬁcally, the reference montage with a
reference electrode which is far away from the SOZ is employed
to record the ECoG, and the sampling rate is either 500 Hz
or 512 Hz. The dataset provides clinically-determined seizure
onset channels, as well as channels overlapping with the resec-
tion/ablation zone, which are strictly determined by segmenting
the resection cavity. In addition, the dataset includes detailed
patient information such as lesion status on MRI and Engel
surgical outcomes after surgery [30].

In this study, the ECoG data from 20 DRE patients are ana-
lyzed. To ensure the reliability of the data, two types of channels
are excluded, as shown in Fig. 1: (1) channels with obvious
defects in the data, or (2) SOZs that do not show signiﬁcant
seizure characteristics. Speciﬁcally, SOZs are excluded if the
mean absolute value of the ictal data is less than the mean
absolute value plus one standard deviation from the pre-ictal
(or post-ictal) period. Of note, if more than half of the SOZs
in a single seizure are excluded, that seizure is excluded from
the analysis. Ultimately, we selected 17 patients (a total of 47
seizures). The detailed clinical characteristics of these patients
are shown in Table I. Here, an Engel grade of 1 indicates a
successful epilepsy surgery outcome, whereas an Engel grade
greater than 2 indicates a failed outcome.

Subsequently, the selected raw ECoG data are preprocessed
using the EEGLAB toolbox [31]. First, the average reference

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:33 UTC from IEEE Xplore.  Restrictions apply. 

LU et al.: UKF-BASED MODEL PARAMETER ESTIMATION TO LOCALIZE THE SEIZURE ONSET ZONE IN ECOG

6615

TABLE I
THE CLINICAL CHARACTERISTICS OF DRE PATIENTS

TABLE II
PARAMETER VALUES OF Z6 MODEL

method is utilized to the raw ECoG to re-reference the data and
reduce noise interference. Then, the ECoG data are band-pass
ﬁltered in the range of 0.5-45 Hz. Next, the preprocessed ECoG
data are segmented based on the seizures marked by time labels.
Notably, the ﬁrst 10 seconds of data are discarded. To ensure
uniform data length across different periods, the data in the
pre-ictal and post-ictal periods are aligned with the data length
in the ictal period. Additionally, given the signiﬁcant imbalance
in ECoG data between SOZ and NSOZ, dimensionality reduc-
tion is applied to the parameter distribution characteristics, as
described in Section II-E. Feature dimensionality reduction is
performed using Python 3.11, while all other data analysis and
processing are performed in MATLAB 2021a.

It should be noted that the SOZs for all patients in this
dataset are determined and labeled by clinical professionals.
Additionally, channels marked as “n/a” in the dataset are deﬁned
as non-SOZs (NSOZs).

B. Neural Computational Model

It has been widely demonstrated that the Z6 model, a phenom-
enal oscillator model, can simulate neural activities observed in
the brain, especially, epileptic neural dynamics [32]. The Z6
model is a nonlinear dynamical system deﬁned by an ordinary
differential equation [33]:

d
dt

Z = a|Z|4Z + b|Z|2Z + cZ + iωZ + η(t),

(1)

Where Z = x + iy is a complex variable, corresponding to the
real and imaginary parts of Z, with the real part being used to
represent EEG signals. a, b, c, ω are real parameters and η(t) is
additive noise.

Although the model described by (1) does not involve speciﬁc
biological mechanisms or processes within neuronal popula-
tions, some parameters can be interpreted as “quasi-realistic
quantities” with electrophysiological signiﬁcance [34]. The pa-
rameter a < 0 prevents the system from inﬁnite activation, the
parameter b > 0 is related to the generation of action potentials
in neuronal populations, the parameter c represents the balance
of excitatory and inhibitory activities within neuronal popula-
tions, and the parameter ω > 0 indicates the angular velocity
of the rotator [32]. Of note, the parameter c is a very important

control parameter of the system, and its variation can reﬂect
changes in excitatory and inhibitory activities within a brain
region. As c varies, the system transitions between different
dynamical states, including stable states, bistability, and limit
cycles, exhibiting rich dynamical properties. In the current study,
the UKF is utilized to estimate parameter c. According to the
previous study that introduced the Z6 model, the default values
for parameters a, b, and η are −1, 2, and 0.1, respectively [33].
Notably, since the average peak frequency of ECoG signals
from all epilepsy patients is approximately 8 Hz, the parameter
ω is set to 2 × π × 8. The speciﬁc parameters are detailed in
Table II.

C. UKF Algorithm

The UKF is an enhanced Kalman ﬁlter algorithm designed
for state and parameter estimation in nonlinear systems [35].
By incorporating the Unscented Transformation (UT), the UKF
effectively handles the state updates for nonlinear systems [24].
Compared with traditional Kalman ﬁlter, UKF is better suited
to handle highly nonlinear problems and can capture changes in
neural signals in real-time, making it particularly advantageous
for neural computational models, especially when dealing with
complex dynamic parameters. Assuming the nonlinear dynamic
system is described as:

(cid:2)

xk = f (xk−1) + ωk
yk = h(xk) + vk

(2)

Where xk represents the system state vector at time k, yk
represents the system observation vector at time k, f is the state
function, h is the observation function, ωk is the process noise
at time k, and vk is the observation noise at time k. Both ω and
v are independent and follow zero-mean Gaussian distributions.

The speciﬁc ﬁltering steps are as follows:
1) Initialization:

(cid:2)

ˆx0 = E(x0)
P0 = E

(cid:3)

(x0 − ˆx0)(x0 − ˆx0)T

(cid:4)

(3)

Where ˆx0 is the initial estimate of the state vector and P0
represents the initial estimate covariance matrix.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:33 UTC from IEEE Xplore.  Restrictions apply. 

6616

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 9, SEPTEMBER 2025

2) Calculation of sigma points:

⎧

⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩

χ0
k−1 = ˆxk−1
χi
k−1 = ˆxk−1
(cid:9)(cid:10)
+
χi
k−1 = ˆxk−1
(cid:9)(cid:10)
−
W m
W c
W m

0 = λ
L+λ
0 = λ
i = W c

(n + λ)Pk−1

(n + λ)Pk−1

(cid:11)

(cid:11)

i

i

i = 1, . . . , L

i = n + 1, . . . , 2L

(4)

L+λ + (1 − α2 + β)

i = 1

2(L+λ)

i = n + 1, . . . , 2L

For a random variable x with dimension L, a matrix χ con-
taining (2L + 1) sigma vectors χi (with corresponding
weights W i) is generated. λ is a scaling parameter, cal-
culated as λ = α2(L + κ) − L. α determines the spread
of the sigma points around ˆx and is usually set to a small
positive value (e.g., 10−3). κ is a secondary scaling pa-
rameter, typically set to 0. β incorporates prior knowledge
of the distribution of x (for a Gaussian distribution, β = 2
is optimal).
3) State prediction:
⎧

k|k−1 = f (χi
χi
(cid:12)2n
ˆxk|k−1 =
Px,k|k−1 =
(cid:13)

k−1)
i χi
i=0 W m
(cid:13)
k|k−1
(cid:12)2n
i=0 W c
χi
k|k−1 − ˆxk|k−1
i
(cid:14)T

(cid:14)

(5)

χi
k|k−1 − ˆxk|k−1
+Qk
k|k−1 = h(γi
γi
(cid:12)2n
ˆyk|k−1 =

k−1)
i=0 W m

i γi

k|k−1

⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩

Where Qk represents the covariance of the process noise
ω at time k.

4) Measurement update:
⎧
(cid:12)2n

⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩

(cid:14)

(cid:14)

(cid:13)
γi
k|k−1 − ˆyk|k−1

Py,k =
(cid:13)
γi
k|k−1 − ˆyk|k−1

i=0 W c
i
(cid:14)T

(cid:12)2n

+ Rk
(cid:13)

χi
k|k−1 − ˆxk|k−1

i=0 W c
i
(cid:14)T

Pxy,k =
(cid:13)
γi
k|k−1 − ˆyk|k−1
K = Pxy,kP −1
y,k
ˆxk = ˆxk|k−1 + K
Px,k = Px,k|k−1 − KPy,kK T

yk − ˆyk|k−1

(cid:3)

(cid:4)

(6)

Where Rk represents the covariance of the observation
noise v at time k. K represents the Kalman gain in UKF.
Notably, ˆxk = [ ˆxxk, ˆxyk, ˆxck] is a 3× 1 vector, representing
the real part, imaginary part, and parameter c of the Z6 model’s
output at time k, respectively, while yk is the ECoG signal value
at time k. By inputting a vector Y = [y1, y2, . . ., yk, . . ., yT ]
(k = 1, 2, . . ., T ) into the UKF system, three output vectors are
obtained: ˆXx = [ ˆxx1, ˆxx2, . . ., ˆxxk, . . ., ˆxxT ](k = 1, 2, . . ., T
), ˆXy = [ ˆxy1, ˆxy2, . . ., ˆxyk, . . ., ˆxyT ](k = 1, 2, . . ., T ) and ˆXc
= [ ˆxc1, ˆxc2, . . ., ˆxck, . . ., ˆxcT ](k = 1, 2, . . ., T ), where the vec-
tor ˆXc represents the sequence of parameter c corresponding to
the ECoG signal over time period T .

In the current study, to remove external noise and ensure
the reliability of parameter estimation, the ﬁrst and last 5 sec-
onds of ECoG are excluded. Additionally, to minimize the root
mean square error (RMSE) between the true and output signals,
the process noise covariance in the UKF is empirically set to
Q = diag(0.06, 0.06, 0.02) and the observation noise covari-
ance is set to R = 0.5. Finally, to facilitate the analysis of model
parameters, the parameters for each channel during each seizure
are normalized to a range of -1 to 1.

D. Calculation of the Model Parameter Distribution

To quantify the distribution characteristics of the model pa-
rameters, the elements of a 1 × n parameter vector C are divided
into a distribution vector using a speciﬁed step size. The detailed
procedure is as follows:

1) Parameter vector deﬁnition: First, all elements of the
parameter vector C are restricted to the interval [−1, 1].
The parameter vector is deﬁned as:

C = [c1, c2, . . ., cn]

(7)

Where ci ∈ [−1, 1].

2) Interval edges deﬁnition: The range of vector C in [−1, 1]
is divided into 200 equally spaced intervals. The interval
edges are deﬁned as:

edges = [−1, −0.99, −0.98, . . ., 0.99, 1]

(8)

3) Calculation of the number of elements: Using the his-
togram counting method, calculate the number of ele-
ments in vector C that fall within each interval, resulting
in a vector H:

H = histcounts(C, edges)

(9)

The resulting vector H is a 1 × 200 vector that represents
the distribution of elements in the parameter vector C
across the interval [−1, 1].

E. SOZ Localization Based on Parameter Distribution

To localize the SOZ, the model parameter of epileptic signals
estimated by UKF is used as features for classifying SOZ and
NSOZ. Note that the data are collected from patients who un-
derwent successful epilepsy surgery, including ECoG from both
SOZ and NSOZ. To effectively extract features, the UKF is used
to estimate model parameters from these signals. For a segment
of ECoG signal with T sampling points, T parameters c can be es-
timated. These T parameters are then distributed into 200 equally
spaced intervals within the range [−1, 1], resulting in a 1× 200
parameter distribution vector, which is used as the input to the
classiﬁcation model. To classify SOZ and NSOZ, the bagged
trees classiﬁer is employed. Bagged trees is an ensemble learning
method that enhances classiﬁcation accuracy and robustness by
training multiple decision trees and aggregating their outputs.
The advantage of bagged trees lies in its ability to reduce the
variance of individual decision trees, thereby improving model
stability and generalization [36]. However, there is a signiﬁcant
imbalance in the ECoG data between SOZ and NSOZ, with

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:33 UTC from IEEE Xplore.  Restrictions apply. 

LU et al.: UKF-BASED MODEL PARAMETER ESTIMATION TO LOCALIZE THE SEIZURE ONSET ZONE IN ECOG

6617

248 and 2525 cases, respectively. Here,to address this imbal-
ance, we adopt the method proposed by Lemaitre Guillaume
et al. [37], which involves techniques such as under-sampling,
over-sampling, and generating synthetic samples to balance the
dataset across classes. This approach prevents the classiﬁer from
being biased towards the majority class. For the classiﬁcation
model training, the dataset is randomly split into training and
testing sets at an 8:2 ratio, and this process is repeated 100 times.
To comprehensively evaluate the performance of the classiﬁer,
four metrics are used: Accuracy, Sensitivity, Specif icity,
and the Area Under the ROC Curve (AUC) [38]. These metrics
are calculated as follows:

Accuracy =

T P + T N
T P + F P + T N + F N

Sensitivity =

Specif icity =

T P
T P + F N
T N
T N + F P

(10)

(11)

(12)

Where T P represents true positives, T N represents true neg-
atives, F P represents false positives, and F N represents false
negatives.

Next, to investigate the potential impact of different MRI
lesion states on SOZ localization, the parameter distributions
under various MRI lesion conditions are obtained. Speciﬁcally,
the patients are divided into two groups: one group with lesions
visible on MRI and another without visible lesions. Classiﬁca-
tion of SOZ and NSOZ is then performed separately for each
group.

F. Surgical Outcome Prediction Based on Parameter
Distribution

The current study further explores the potential of predicting
surgical outcomes by analyzing the distribution of model param-
eters derived from epilepsy patients. As mentioned above, the
data come from a cohort of postoperative epilepsy patients, with
some achieving successful outcomes and others experiencing
unsuccessful surgeries. Of note, model parameters are extracted
from the ECoG data in the SOZ, with the data segmented into
pre-ictal, ictal and post-ictal periods. The distribution of these
model parameters is used as a feature to classify and predict
whether the surgical outcome is successful or not.

Similar to the previous analysis, the data of patients with
successful surgeries greatly outnumber those with unsuccessful
outcomes. To address this imbalance, a previously mentioned
imbalanced learning method is employed [37]. The bagged trees
classiﬁer is used again, with the dataset randomly split into
training and testing sets at an 8:2 ratio, repeated 100 times.
To evaluate the ability of the model parameter distribution to
predict surgical outcomes, the mean and standard deviation
of the accuracy, sensitivity, speciﬁcity, and AUC from these
100 iterations are calculated and reported. Finally, rank-sum
tests are performed to evaluate the accuracy and other metrics
of SOZ localization results across different periods and MRI
lesion conditions, as well as surgical outcome predictions across
different periods. P<0.05 is considered statistically signiﬁcant.

Fig. 2. An example showing the distribution of model parameter. A,
original parameter. B, distribution of parameter values.

III. RESULTS

A. UKF-Based Model Parameter Estimation of
Simulated Epileptic-Like Signals

Theoretically, the parameter c in the Z6 model can represent
the relative balance between the excitability and inhibition of
neuron masses. Therefore, the value of the parameter c can
determine the state of the model’s output. To verify this, we set
the parameter c in the Z6 model with different values to observe
the effect of these changes on the model’s output. Note that
the other parameters in the Z6 model are ﬁxed at the following
values: a = −1, b = 2, ω = 2 × π × 8, and η is Gaussian white
noise with a mean of 1.

Obviously, when the other parameters remain unchanged,
different values of the parameter c lead to different model
outputs, as shown in Fig. 3. Intuitively, when c = −8, the
system is in a steady state, and the output signal represents
normal brain activity (Fig. 3(a)). When c = −0.9, the system
is in a bistable state, with both ﬁxed-point and limit-cycle states
observable (Fig. 3(b)). And when c = 8, the system corresponds
to a limit cycle, and the model output exhibits epileptic-like
signals (Fig. 3(c)). Theoretically, as the parameter c gradually
changes from negative to positive values, the model’s output sig-
nal transitions from spontaneous brain activity to epileptic-like
signals. Conversely, when c changes from positive to negative
values, the signal should transmit from epileptic-like signals
back to a normal state. Actually, these two processes correspond
to the onset and offset of epilepsy. Taken together, these results
indicate that the parameter c can determine the system’s state in
the Z6 model. Therefore, estimating the parameter c is crucial to
understand the excitability and inhibition within brain regions.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:33 UTC from IEEE Xplore.  Restrictions apply. 

6618

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 9, SEPTEMBER 2025

Fig. 3. Simulated signals of Z6 model with different c values. A, c=−8.
B, c=−0.9. C, c=8.

Fig. 5. Model parameters estimation and distribution of true epileptic
ECoG in patient HUP074. A, the epileptic ECoG of an SOZ. B, the
estimated parameters of all SOZs. C, the epileptic ECoG of an NSOZ.
D, the estimated parameters of all NSOZs. E, the mean parameter
distribution in the pre-ictal period. F, the mean parameter distribution
in the ictal period. G, the mean parameter distribution in the post-ictal
period. H-N, the epileptic ECoG, parameter estimation, and distribution
of another seizure in patient HUP074. The light blue, black, and dark
blue curves represent the ECoG and the mean of the estimated param-
eters in the pre-ictal, ictal, and post-ictal periods, respectively. The red
shading represents the standard deviation of the estimated parameters.

It is observed that as the simulated epileptic-like signal transi-
tion between normal and seizure states, the model output signal
estimated by the UKF closely matches the simulated signal,
with the residual between them remaining near zero during the
epileptic phases (Fig. 4). Importantly, the parameter c estimated
by the UKF ﬁrst increases and then decreases, exhibiting the
same trend as the true parameter c, and the estimated values con-
sistently remain close to the true values (Fig. 4(b)). Summarily,
these results demonstrate that the UKF method performs well
in estimating the state and parameters of neural computational
models for both normal and epileptic neural signals.

Fig. 4. Parameters estimation of simulated epileptic-like signal. A, the
simulated epileptic-like signal. B, the estimated parameter c. C, the
residual between simulated and output signals.

To validate the feasibility of the UKF method for estimating
model parameters of neural signals, the UKF method is ﬁrst em-
ployed to estimate the model parameters of simulated epileptic
signals in this study. Here, the model used is the Z6 model, the
neural signals are the simulated epileptic signals (Fig. 4(a)), and
the parameter estimated is the balance parameter c of the Z6
model.

B. Model Parameter Estimation of True Epileptic ECoG
Based on UKF

The feasibility of using UKF to estimate model parameters of
epileptic-like signals has already been demonstrated. Accord-
ingly, the UKF is further used to estimate the model parameter
from the true epileptic ECoG of DRE patients.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:33 UTC from IEEE Xplore.  Restrictions apply. 

LU et al.: UKF-BASED MODEL PARAMETER ESTIMATION TO LOCALIZE THE SEIZURE ONSET ZONE IN ECOG

6619

Fig. 6. Model parameters estimation and distribution of true epileptic
ECoG in patient HUP126. A, the epileptic ECoG of an SOZ. B, the
estimated parameters of all SOZs. C, the epileptic ECoG of an NSOZ.
D, the estimated parameters of all NSOZs. E, the mean parameter
distribution in the pre-ictal period. F, the mean parameter distribution
in the ictal period. G, the mean parameter distribution in the post-ictal
period. H-N, the epileptic ECoG, parameter estimation, and distribution
of another seizure in patient HUP126. The light blue, black, and dark
blue curves represent the ECoG and the mean of the estimated param-
eters in the pre-ictal, ictal, and post-ictal periods, respectively. The red
shading represents the standard deviation of the estimated parameters.

Subsequently, Figs. 5 and 6 show the estimated model parame-
ters and their distributions from two seizures in two DRE patients
who undergo successful surgery (HUP074 and HUP126).

As shown in Fig. 5, it can be easily observed that the estimated
model parameters initially increase and then decrease during the
epileptic evolution for both the SOZ and the NSOZ. Notably,
despite the similar overall dynamic trend, the parameter changes
in SOZ are signiﬁcantly larger than those in NSOZ (Fig. 5(b)
and (d)).

Further analysis of the parameter distributions indicates that
during the pre-ictal period (Fig. 5(e)), both SOZ and NSOZ
parameters exhibit a clear unimodal distribution, with the peak
parameter in SOZ being higher than that in NSOZ. In contrast,
during the ictal period (Fig. 5(f)), both SOZ and NSOZ parame-
ters show a clear bimodal distribution, with peaks in both the neg-
ative and positive ranges. Notably, in the negative range, the peak
of parameter distribution in NSOZ is higher than that in SOZ,
while in the positive range, the peak of parameter distribution in
SOZ exceeds that in NSOZ. Additionally, during the postictal

Fig. 7. Model parameters distribution of true epileptic ECoG in all
patients. A, the mean parameter distribution in the pre-ictal period. B, the
mean parameter distribution in the ictal period. C, the mean parameter
distribution in the post-ictal period.

period (Fig. 5(g)), the parameters of NSOZ exhibit a distinct
unimodal distribution, whereas the parameters of SOZ show a
more uniform distribution without a prominent peak. Moreover,
the dynamic changes and distribution of the estimated model
parameters exhibit the same pattern during another seizure in
the same patient (Fig. 5(h) to Fig. 5(n)).

The dynamic changes and distribution of model parame-
ters in patient HUP074 are not isolated cases, similar pat-
terns can also be observed in data from other patients, such
as patient HUP126 (Fig. 6). Interestingly, during the pre-
ictal period, the difference between the peak parameters of
SOZ and NSOZ in patient HUP126 is more pronounced com-
pared to patient HUP074. Moreover, during the ictal period,
the parameter distribution in SOZ in HUP126 tends to be
more unimodal, even concentrating around 1. And during
the post-ictal period, the SOZ parameters of HUP126 ex-
hibit a unimodal distribution, primarily concentrated around
0.

Finally, to verify the generalizability of these observations,
a statistical analysis of the model parameter distributions is
conducted for all 13 successfully operated DRE patients, as
shown in Fig. 7. During the pre-ictal period, the parameter
generally follows a unimodal distribution, and the parameter
distribution in the SOZ is typically localized to the right of
the NSOZ parameter distribution. During the ictal period, the
parameter exhibits a bimodal distribution. Notably, the peak
in the negative range for SOZ is smaller than that for NSOZ,
while in the positive range, the peak for SOZ is greater than
that for NSOZ. Additionally, during the post-ictal period, the
parameter exhibits a unimodal distribution, peaking around the

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:33 UTC from IEEE Xplore.  Restrictions apply. 

6620

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 9, SEPTEMBER 2025

TABLE III
SOZ CLASSIFICATION PERFORMANCE BASED ON PARAMETER DISTRIBUTION

TABLE IV
SOZ CLASSIFICATION PERFORMANCE OF DIFFERENT LESION
STATUSES ON MRI

Fig. 8. SOZ classiﬁcation performance based on parameter distribu-
tion. A, Accuracy. B, Sensitivity. C, Speciﬁcity. D, AUC. ∗∗∗ indicates
P<0.001.

vicinity of 0, and the peak value of SOZ is higher than that
of NSOZ. This suggests that despite the heterogeneity among
different patients, the observed distribution patterns are valid on
a broader scale, providing a reliable basis for further clinical
applications.

C. SOZ Localization Based on Model Parameter
Distribution

By using the model parameter distributions estimated from
the ECoG of patients who undergo successful epilepsy surgery
as features, and employing bagged trees as the classiﬁer, clas-
siﬁcation of SOZs and NSOZs has been performed on 13 DRE
patients. The results indicate that the classiﬁcation performance
during the post-ictal period is generally better than that dur-
ing the pre-ictal and ictal periods, as shown in Tables III and
Fig. 8. Intuitively, during the post-ictal period, the classiﬁcation
model achieves signiﬁcantly higher accuracy (0.9160 ± 0.0208),
sensitivity (0.9554 ± 0.0293), and AUC (0.9643 ± 0.0158),
whereas during the ictal period, the model exhibits higher speci-
ﬁcity (0.9096 ± 0.0414). These ﬁndings suggest that combining
UKF-based model parameter estimation with machine learning
classiﬁcation algorithms can effectively localize SOZs from

Fig. 9. SOZ classiﬁcation performance of different lesion statuses on
MRI. A, Accuracy. B, Sensitivity. C, Speciﬁcity. D, AUC. The abbrevi-
ations for classiﬁcation groups are as follows: pr-l represents pre-ictal
and lesional, pr-nl represents pre-ictal and non-lesional, i-l represents
ictal and lesional, i-nl represents ictal and non-lesional, po-l represents
post-ictal and lesional, and po-nl represents post-ictal and non-lesional.
Statistical signiﬁcance is indicated as follows: ∗ for P<0.05, ∗∗ for
P<0.01, and ∗∗∗ for P<0.001.

the ECoG of epilepsy patients, especially during the post-ictal
period.

To further explore the potential impact of MRI lesion sta-
tus on SOZ localization, the 13 epilepsy patients are divided
into an MRI lesion group (9 patients) and a non-lesion group
then the SOZ localization analyses are con-
(4 patients),
ducted separately for each group. The results show that
during the pre-ictal and post-ictal periods, the classiﬁcation
accuracy in the non-lesion group (0.9643 ± 0.0416 and
0.9561 ± 0.0430) is signiﬁcantly higher than that in the lesion
group (0.8678 ± 0.0335 and 0.8493 ± 0.0399). Conversely,
during the ictal period, the classiﬁcation accuracy in the lesion
group (0.8603 ± 0.0354) is higher than that in the non-lesion
group (0.8230 ± 0.0683), as shown in Table IV and Fig. 9.
Overall, the classiﬁcation accuracy in the pre-ictal non-lesion
group and post-ictal non-lesion group is signiﬁcantly higher
than that in other conditions. Additionally, during the pre-
ictal and post-ictal periods, the non-lesion group also exhibits
higher sensitivity (0.9832 ± 0.0517 and 0.9723 ± 0.0586),

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:33 UTC from IEEE Xplore.  Restrictions apply. 

LU et al.: UKF-BASED MODEL PARAMETER ESTIMATION TO LOCALIZE THE SEIZURE ONSET ZONE IN ECOG

6621

TABLE V
SURGICAL OUTCOMES CLASSIFICATION PERFORMANCE BASED
ON SOZ PARAMETER DISTRIBUTION

Fig. 10. Surgical outcomes classiﬁcation performance based on SOZ
parameter distribution. A, Accuracy. B, Sensitivity. C, Speciﬁcity. D, AUC.
∗∗∗ indicates P<0.001.

speciﬁcity (0.9454 ± 0.0666 and 0.9399 ± 0.0673), and AUC
(0.9828 ± 0.0298 and 0.9872 ± 0.0213) compared to other
conditions. These suggest that the presence of MRI-detected
lesions may have inﬂuences on the SOZ localization.

Finally, to assess the ability of model parameter distribu-
tion to predict surgical outcomes, the SOZ model parameter
distributions of patients with successful (13 patients) and unsuc-
cessful (4 patients) surgeries are used as features to classify the
surgical outcomes. The results, as shown in Table V and Fig. 10,
indicate that all classiﬁcation metrics during the ictal period are
signiﬁcantly higher than those during the pre-ictal and post-ictal
periods, with the classiﬁcation accuracy of surgical outcomes
during the ictal period reaching as high as 0.9256 (± 0.0438).
These ﬁndings demonstrate the signiﬁcant potential of using
model parameter distribution as a feature for predicting surgical
outcomes.

IV. DISCUSSION

Neural computational models are considered essential for
simulating dynamic oscillations within the brain and studying
the mechanisms of seizure onset and propagation. However,
few studies have explored the application of model parameters
in SOZ localization. In this study, the excitatory-inhibitory

balance parameters of the Z6 model are estimated from the
ECoG data of DRE patients using the UKF algorithm, with
parameter distributions serving as classiﬁcation features. SOZ
localization is then performed using the bagging tree algorithm.
The parameter estimation results indicate that the parameters
generally follow a unimodal distribution during the pre-ictal
and post-ictal periods, while they exhibit a bimodal distribution
during the ictal period. Especially, differences can be easily
observed between the peak values and corresponding parameters
of SOZ and NSOZ distributions in three periods. The classiﬁ-
cation results demonstrate that the model based on parameter
distribution can achieve excellent performance, with an average
accuracy of 91.60% and an AUC of 96.43% . Furthermore,
SOZ localization has also been performed using the parameter
distribution in patients with and without MRI-detected lesions.
The results indicate that the classiﬁcation accuracy improves on
patients without MRI-detected lesions. Additionally, the esti-
mated parameter distributions have been used to predict epilepsy
surgery outcomes, achieving a maximum average accuracy of
92.56% and an AUC of 97.20% . These ﬁndings suggest that
the distribution of neural computational model parameters may
complement existing SOZ localization and epilepsy surgery
outcome prediction methods, providing a new perspective for
clinical decision-making in epilepsy treatment.

Parameter distributions of neural computational models es-
timated by UKF might offer a novel approach for SOZ lo-
calization. In the current study, for pre-ictal, ictal and post-
ictal periods, the SOZ classiﬁcations achieved a remarkable
accuracy, which indicates that the model parameter distribution
may contribute to accurately identifying SOZ. Furthermore,
although the ECoG signals used in this study encompass various
seizure onset patterns, the model parameters achieved good
performance as classiﬁcation features. This demonstrates the
robustness of the model parameter estimation algorithm used
in this study, highlighting its strong adaptability to different
seizure onset patterns. Previous SOZ localization methods based
on bioelectrical signals often focus more on analyzing and
processing the signals themselves. For example, Jacobs et al.
found that the rates of high-frequency oscillations (HFOs) are
signiﬁcantly higher in the SOZ, and the degree of post-spike
high-frequency (HF) power attenuation in the SOZ is noticeably
more severe compared to NSOZ regions [39]. Similarly, Du et
al. proposed an SOZ localization algorithm based on multivari-
ate HFO feature extraction and wavelet time-frequency maps,
ultimately determining the SOZ classiﬁcation results according
to the wavelet time-frequency maps [11]. Additionally, Conrad
et al. analyzed iEEG data from DRE patients and found that
functional connectivity is reduced in the SOZ [40]. Unlike
these previous studies, this study concentrates on the potential
physiological signiﬁcance of neural computational model pa-
rameters, which could more directly reﬂect the neurodynamic
changes in the brain, and provide a possible underlying mech-
anism of seizures. Theoretically, the excitatory-inhibitory ratio
is expected to be higher during the ictal period compared to the
non-ictal period. The observed increase in the model parameter
c during the ictal period is consistent with the theoretical expec-
tation, emphasizing the physiological relevance of the model.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:33 UTC from IEEE Xplore.  Restrictions apply. 

6622

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 9, SEPTEMBER 2025

Also, as demonstrated in the current study, UKF-based param-
eter estimation has a strong performance in SOZ localization
using pre-ictal, ictal and post-ictal data, which indicates that the
method can capture not only abnormal neural activity during
the ictal period but also potential alterations during the pre-ictal
period. This capability may lay the foundation for early warning
and intervention in epilepsy, highlighting its signiﬁcant clinical
application potential.

Theoretically, the core feature used for SOZ classiﬁcation in
this study is the parameter representing the balance between
excitatory and inhibitory activity within brain regions. Indeed,
extensive literature has demonstrated a close relationship be-
tween seizures and the imbalance between excitatory and in-
hibitory [41], [42].At the cellular and molecular levels, neurons
promote the generation of action potentials by releasing excita-
tory neurotransmitters, such as glutamate [43], while inhibiting
this process by releasing inhibitory neurotransmitters, such as
GABAergic [44]. In epilepsy patients, excitatory activity is often
excessively enhanced, while inhibitory function is weakened,
and this imbalance is considered a primary trigger of seizure
activity [45]. In the SOZ, this imbalance is particularly pro-
nounced. Studies have shown that neurons in the SOZ tend to
exhibit heightened excitatory activity, making them more prone
to synchronized ﬁring. This abnormal excitatory activity not
only propagates within the SOZs but also spreads to adjacent
NSOZs through axonal conduction, leading to the expansion of
the seizure [46]. Notably, at the onset of seizures, low-voltage
fast activity is commonly observed in neural signals, which
may be related to the activation of inhibitory interneurons prior
to excitatory neurons [47], [48]. Subsequently, as the overall
excitability in the brain increases and inhibitory mechanisms
weaken, ultimately resulting in a prolonged, large-amplitude
epileptiform discharge. Therefore, the signiﬁcant differences in
the intensity and dynamics of excitatory and inhibitory activities
between SOZs and NSOZs may underlie the effectiveness of
balance parameters in localizing the SOZ.

The potential impact of different MRI lesion states on SOZ
localization is explored in this study, and the results indicate that
SOZ localization performs well regardless of the presence of
MRI-detected lesions. However, higher classiﬁcation accuracy
is achieved when no lesions are observed on MRI. Unlikely,
certain perspectives suggest that when lesions appear on the
MRI of DRE patients, it generally aids in the localization of the
SOZ [49], [50], [51]. This idea stems from the fact that struc-
tural abnormalities visible on MRI indicate potential sources of
epileptic activity, making the SOZ more identiﬁable in clinical
settings. Nevertheless, other studies highlight additional factors.
For example, even though lesions are visible on MRI, only part of
the lesion may correspond to the SOZ, while other parts could be
areas adjacent to or connected with the SOZ within the epileptic
network and inﬂuenced by it [52], [53]. This may lead to the
incorrect identiﬁcation of non-SOZ regions as SOZ. Moreover,
not all SOZs present visible lesions on MRI, and some may
have characteristics similar to other brain regions, making them
harder to distinguish [54]. Despite ongoing debate regarding
how MRI lesions inﬂuence SOZ localization, the UKF-based
method relies mainly on the analysis of ECoG signals, showing

minimal dependence on the presence of MRI-detected lesions.
Thus, the presence or absence of MRI lesions has a limited
impact on classiﬁcation performance. Interestingly, the method
is more sensitive to non-lesional signals, achieving relatively
better SOZ localization in such cases.

Accurately predicting the outcome of epilepsy surgery holds
signiﬁcant importance in clinical practice for assessing surgical
risks, aiding medical decision-making, and developing person-
alized surgical plans. Current studies on predicting epilepsy
surgery outcomes utilize various approaches, including clinical
and demographic features [55], graph theory metrics extracted
from functional magnetic resonance imaging (fMRI) data [56],
[57], and biomarkers such as interictal epileptiform discharges
(IEDs) from EEG (or iEEG) signals [58]. Additionally, a combi-
nation of demographic, EEG, and MRI features has been applied
to improve prediction accuracy [59], [60]. Furthermore, some
studies employ physiological models ﬁtted to invasive EEG
recordings and adjust brain network models to simulate virtual
resections of speciﬁc brain regions or connections, and the
post-resection activity in these models is then analyzed to predict
surgical outcomes [61], [62]. The aforementioned studies, by
integrating various clinical information, biomarkers, and net-
work model approaches, provide powerful tools for predicting
epilepsy surgery outcomes. However, these methods still face
certain limitations in simultaneously considering both temporal
resolution and physiological interpretability. This study inte-
grates estimated neural computational model parameters from
the ECoG of DRE patients with machine learning techniques,
preserving the high temporal resolution of ECoG signals and
incorporating the physiological interpretability of neural mod-
els, demonstrating excellent predictive capabilities for surgical
outcomes. Notably, these model parameter features are derived
from ECoG signals recorded during epileptic periods prior to
surgery, including the pre-ictal period, highlighting the potential
of this method for clinical presurgical evaluation.

Despite the fact that the distributions of balance parame-
ters estimated from ECoG signals in a neural computational
model is ﬁrstly employed in the current study as classiﬁca-
tion features to localize the SOZs, several limitations must be
acknowledged. First, this study selects ECoG data from only
13 DRE patients who undergo successful surgery, which may
limit the generalizability of the results. Additionally, to maintain
consistency in data processing, only ECoG data are considered,
and SEEG data are not included. Despite that SEEG data also
hold signiﬁcant values, and future research on SOZ localization
would incorporate SEEG data to enhance the applicability of
the analysis and achieve better coverage of deep brain regions.
Although high-frequency features of ECoG signals have gar-
nered signiﬁcant attention from researchers, this study primar-
ily focuses on analyzing the frequency components within the
0.5–45 Hz range. Regarding the UKF algorithm, although it
performs well in parameter estimation, the setting of process
noise covariance and observation noise covariance may require
multiple attempts to stabilize the algorithm, indicating a degree
of dependence on experience. Finally, the Z6 model used in this
study is based on simpliﬁed assumptions, which may not fully
capture the complexity of biological systems. Therefore, future

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:33 UTC from IEEE Xplore.  Restrictions apply. 

LU et al.: UKF-BASED MODEL PARAMETER ESTIMATION TO LOCALIZE THE SEIZURE ONSET ZONE IN ECOG

6623

studies should test the model on larger and diverse multicenter
clinical datasets, consider employing models that better reﬂect
physiological foundations to more accurately capture changes
in brain neurodynamics, and explore methods for automating or
adaptively adjusting the process and observation noise covari-
ances in the UKF algorithm.

V. CONCLUSION

The excitatory-inhibitory balance parameter of the Z6 neural
computational model is extracted from epileptic ECoG using
the UKF algorithm, and SOZs have been accurately localized
based on the distribution of this parameter. It is observed that the
parameters follow a unimodal distribution during the pre-ictal
and post-ictal periods, while the parameters exhibit a bimodal
distribution during the ictal period. The classiﬁcation model con-
structed using parameter distributions as features demonstrates
excellent classiﬁcation performance, with an average accuracy
of 91.60% . Of note, the absence of MRI-detected lesions
appears to contribute to improving classiﬁcation performance.
More importantly, the distribution of parameters signiﬁcantly
contributes to the prediction of epilepsy surgery outcomes,
achieving an average accuracy of 92.56% . In summary, these
ﬁndings suggest that the distribution of neural computational
model parameters may serve as a biomarker for SOZ localization
and epilepsy surgery outcome prediction, supporting medical
decision-making in epilepsy treatment.

REFERENCES

[1] J. Falco-Walter, “Epilepsy—Deﬁnition, classiﬁcation, pathophysiology,
and epidemiology,” in Seminars in Neurology, vol. 40. New York City,
NY, USA: Thieme Medical Publishers, Inc., 2020, pp. 617–623.

[2] R. Tsigebrhan et al., “Co-morbid mental health conditions in people with
epilepsy and association with quality of life in low-and middle-income
countries: A systematic review and meta-analysis,” Health Qual. Life
Outcomes, vol. 21, no. 1, 2023, Art. no. 5.

[3] N. M. Sayed, M. T. K. Aldin, S. E. Ali, and A. E. Hendi, “Cognitive
functions and epilepsy-related characteristics in patients with generalized
Tonic–Clonic epilepsy: A cross-sectional study,” Middle East Curr. Psy-
chiatry, vol. 30, no. 1, 2023, Art. no. 15.

[4] B. Mesraoua, F. Brigo, S. Lattanzi, B. Abou-Khalil, H. Al Hail, and A. A.
Asadi-Pooya, “Drug-resistant epilepsy: Deﬁnition, pathophysiology, and
management,” J. Neurological Sci., vol. 452, 2023, Art. no. 120766.
[5] H. Yan et al., “Deep brain stimulation for patients with refractory epilepsy:
Nuclei selection and surgical outcome,” Front. Neurol., vol. 14, 2023,
Art. no. 1169105.

[6] M. J. Morrell, “Responsive cortical stimulation for the treatment of
medically intractable partial epilepsy,” Neurology, vol. 77, no. 13,
pp. 1295–1304, 2011.

[7] J. M. Bernabei et al., “Quantitative approaches to guide epilepsy surgery
from intracranial eeg,” Brain, vol. 146, no. 6, pp. 2248–2258, 2023.
[8] F. Rosenow and H. Lüders, “Presurgical evaluation of epilepsy,” Brain,

vol. 124, no. 9, pp. 1683–1700, 2001.

[9] A. Li et al., “Neural fragility as an eeg marker of the seizure onset zone,”

Nature Neurosci., vol. 24, no. 10, pp. 1465–1474, 2021.

[10] H. Yu et al., “Variation of functional brain connectivity in epileptic
seizures: An eeg analysis with cross-frequency phase synchronization,”
Cogn. Neurodynamics, vol. 14, pp. 35–49, 2020.

[11] Y. Du and B. Sun, “Accurate localization of seizure onset zones based on
multi-feature extraction and wavelet time-frequency map,” in Proc. IEEE
37th Chin. Control Conf., 2018, pp. 4283–4288.

[12] W. Staljanssens et al., “Seizure onset zone localization from ictal
high-density EEG in refractory focal epilepsy,” Brain Topogr., vol. 30,
pp. 257–271, 2017.

[13] N. Rogers et al., “Correlation structure in micro-ECOG recordings is
described by spatially coherent components,” PLoS Comput. Biol., vol. 15,
no. 2, 2019, Art. no. e1006769.

[14] M. R. Mercier et al., “Advances in human intracranial electroencephalog-
raphy research guidelines good practices,” Neuroimage, vol. 260, 2022,
Art. no. 119438.

[15] C. Yang, Q. Luo, H. Shu, R. L. B. Jeannès, J. Li, and W. Xiang,
“Exploration of interictal to ictal transition in epileptic seizures using a
neural mass model,” Cogn. Neurodynamics, vol. 18, no. 3, pp. 1215–1225,
2024.

[16] Y. Shimoda et al., “Extracellular glutamate and gaba transients at the
transition from interictal spiking to seizures,” Brain, vol. 147, no. 3,
pp. 1011–1024, 2024.

[17] Y. Yang et al., “Dynamic evolution of the anterior cingulate-insula net-
work during seizures,” CNS Neurosci. Therapeutics, vol. 29, no. 12,
pp. 3901–3912, 2023.

[18] M. A. Hays et al., “Cortico-cortical evoked potentials in response to
varying stimulation intensity improves seizure localization,” Clin. Neu-
riophysiol., vol. 145, pp. 119–128, 2023.

[19] N. Wu and Y. Liu, “Least squares estimation of multifactor uncertain
differential equations with applications to the stock market,” Symmetry,
vol. 16, no. 7, 2024, Art. no. 904.

[20] A. G. Roy and N. Peyada, “Lateral aircraft parameter estimation using
neuro-fuzzy and genetic algorithm based method,” in Proc. 2017 IEEE
Aerosp. Conf., 2017, pp. 1–11.

[21] N. J. Linden, B. Kramer, and P. Rangamani, “Bayesian parameter esti-
mation for dynamical models in systems biology,” PLoS Comput. Biol.,
vol. 18, no. 10, 2022, Art. no. e1010651.

[22] X. Gao, X. Zhong, D. You, and S. Katayama, “Kalman ﬁltering com-
pensated by radial basis function neural network for seam tracking
of laser welding,” IEEE Trans. Control Syst. Technol., vol. 21, no. 5,
pp. 1916–1923, Sep. 2013.

[23] C.-H. Lee and J.-T. Chien, “Deep unfolding inference for supervised topic
model,” in Proc. 2016 IEEE Int. Conf. Acoust., Speech Signal Process.,
2016, pp. 2279–2283.

[24] X. Wen, D. Wang, L. Fan, Z. Lv, C. Zhang, and Z. Liang, “Tracking
propofol-related brain states with UKF-based neural mass model,” in Proc.
41st Chin. Control Conf., 2022, pp. 5962–5966.

[25] B. Shan, J. Wang, B. Deng, X. Wei, H. Yu, and H. Li, “UKF-based
closed loop iterative learning control of epileptiform wave in a neural
mass model,” Cogn. Neurodynamics, vol. 9, pp. 31–40, 2015.

[26] R. Fang, J. Wang, C. Liu, H. Yu, and Y. Qing, “Closed-loop control scheme
to control epileptic activity based on UKF,” in Proc. IEEE 37th Chin.
Control Conf., 2018, pp. 7980–7985.

[27] M. Çetin and S. Beyhan, “Adaptive stabilization of uncertain cortex dy-
namics under joint estimates and input constraints,” IEEE Trans. Circuits
Syst. II: Exp. Briefs, vol. 66, no. 4, pp. 627–631, Apr. 2019.

[28] A. Jafarian, D. R. Freestone, D. Neši´c, and D. B. Grayden, “Slow-fast
dufﬁng neural mass model,” in Proc. IEEE 41st Annu. Int. Conf. Eng.
Med. Biol. Soc., 2019, pp. 142–145.

[29] J. M. Bernabei et al., “Hup ieeg epilepsy dataset,” OpenNeuro, 2023,

doi: 10.18112/openneuro.ds004100.v1.1.3.

[30] J. Engel Jr, “Surgery for seizures,” New England J. Med., vol. 334, no. 10,

pp. 647–653, 1996.

[31] A. Delorme and S. Makeig, “Eeglab: An open source toolbox for analysis
of single-trial eeg dynamics including independent component analysis,”
J. Neurosci. Methods, vol. 134, no. 1, pp. 9–21, 2004.

[32] M. Koppert, S. Kalitzin, D. Velis, F. L. D. Silva, and M. A. Viergever, “Pre-
ventive and abortive strategies for stimulation based control of epilepsy:
A computational model study,” Int. J. neural Syst., vol. 26, no. 08, 2016,
Art. no. 1650028.

[33] S. Kalitzin, M. Koppert, G. Petkov, and F. L. D. Silva, “Multiple oscillatory
states in models of collective neuronal dynamics,” Int. J. Neural Syst.,
vol. 24, no. 6, 2014, Art. no. 1450020.

[34] P. R. Bauer et al., “Dynamics of convulsive seizure termination and
postictal generalized eeg suppression,” Brain, vol. 140, no. 3, pp. 655–668,
2017.

[35] S. Julier, J. Uhlmann, and H. F. Durrant-Whyte, “A new method for
the nonlinear transformation of means and covariances in ﬁlters and
estimators,” IEEE Trans. Autom. Control, vol. 45, no. 3, pp. 477–482,
Mar. 2000.

[36] W.-Y. Loh, “Fifty years of classiﬁcation and regression trees,” Int. Stat.

Rev., vol. 82, no. 3, pp. 329–348, 2014.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:33 UTC from IEEE Xplore.  Restrictions apply. 

6624

IEEE JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, VOL. 29, NO. 9, SEPTEMBER 2025

[37] G. LemaÃŽtre, F. Nogueira, and C. K. Aridas, “Imbalanced-learn: A
python toolbox to tackle the curse of imbalanced datasets in machine
learning,” J. Mach. Learn. Res., vol. 18, no. 17, pp. 1–5, 2017.

[38] J. Huang and C. X. Ling, “Using AUC and accuracy in evaluating learning
algorithms,” IEEE Trans. Knowl. Data Eng., vol. 17, no. 3, pp. 299–310,
Mar. 2005.

[39] J. Jacobs, C. Vogt, P. L.Van, R. Zelmann, J. Gotman, and K. Kobayashi,
“The identiﬁcation of distinct high-frequency oscillations during spikes
delineates the seizure onset zone better than high-frequency spectral
power changes,” Clin. Neuriophysiol., vol. 127, no. 1, pp. 129–142,
2016.

[40] E. C. Conrad et al., “Addressing spatial bias in intracranial eeg functional
connectivity analyses for epilepsy surgical planning,” J. Neural Eng.,
vol. 19, no. 5, 2022, Art. no. 056019.

[41] E. J. V. V. Hugte, D. Schubert, and N. N. Kasri, “Excitatory/inhibitory
balance in epilepsies and neurodevelopmental disorders: Depolarizing γ-
aminobutyric acid as a common mechanism,” Epilepsia, vol. 64, no. 8,
pp. 1975–1990, 2023.

[42] J. E. Niemeyer et al., “Seizures initiate in zones of relative hyperexcitation
in a zebraﬁsh epilepsy model,” Brain, vol. 145, no. 7, pp. 2347–2360,
2022.

[43] H. I. Needs et al., “Changes in excitatory and inhibitory receptor expression
and network activity during induction and establishment of epilepsy in the
rat reduced intensity status epilepticus (rise) model,” Neuropharmacology,
vol. 158, 2019, Art. no. 107728.

[44] S. M. Sears and S. J. Hewett, “Inﬂuence of glutamate and GABA transport
on brain excitatory/inhibitory balance,” Exp. Biol. Med., vol. 246, no. 9,
pp. 1069–1083, 2021.

[45] Y. Wang, B. Tan, Y. Wang, and Z. Chen, “Cholinergic signaling, neural
excitability, and epilepsy,” Molecules, vol. 26, no. 8, 2021, Art. no. 2258.
[46] H. G. Meijer et al., “Modeling focal epileptic activity in the wilson–cowan
model with depolarization block,” J. Math. Neurosci., vol. 5, pp. 1–17,
2015.

[47] F. Capitano et al., “Preictal dysfunctions of inhibitory interneurons para-
doxically lead to their rebound hyperactivity and to low- voltage- fast onset
seizures in Dravet syndrome,” Proc. Nat. Acad. Sci. USA, vol. 121, no. 23,
2024, Art. no. e2316364121.

[48] M. de Curtis and M. Avoli, “Gabaergic networks jump-start focal seizures,”

Epilepsia, vol. 57, no. 5, pp. 679–687, 2016.

[49] Y. Tang et al., “Individual localization value of resting-state fmri in
epilepsy presurgical evaluation: A combined study with stereo-EEG,” Clin.
Neuriophysiol., vol. 132, no. 12, pp. 3197–3206, 2021.

[50] A. Berger et al., “Preoperative localization of seizure onset zones by
magnetic source imaging, EEG-correlated functional MRI, and their com-
bination,” J. Neurosurgery, vol. 134, no. 4, pp. 1037–1043, 2020.
[51] J.-W. Jeong et al., “Multi-scale deep learning of clinically acquired multi-
modal mri improves the localization of seizure onset zone in children with
drug-resistant epilepsy,” IEEE J. Biomed. Health Informat., vol. 26, no. 11,
pp. 5529–5539, Nov. 2022.

[52] A. A. Asadi-Pooya, F. Brigo, S. Lattanzi, and I. Blumcke, “Adult epilepsy,”

Lancet, vol. 402, no. 10399, pp. 412–424, 2023.

[53] R. Shah, A. Botre, and V. Udani, “Trends in pediatric epilepsy surgery,”

Indian J. Pediatrics, vol. 82, pp. 277–285, 2015.

[54] L. Andrade-Valença et al., “Interictal high frequency oscillations (HFOS)
in patients with focal epilepsy and normal MRI,” Clin. Neuriophysiol.,
vol. 123, no. 1, pp. 100–105, 2012.

[55] Z. Jourahmad et al., “Machine learning techniques for predicting the short-
term outcome of resective surgery in lesional-drug resistance epilepsy,”
2023, arXiv:2302.10901.

[56] S. Baxendale, “What are we really predicting with fMRI in epilepsy

surgery?,” Epilepsy Behav., vol. 145, 2023, Art. no. 109298.

[57] B. C. Jobst and G. D. Cascino, “Thalamus as a ‘hub’ to predict outcome
after epilepsy surgery,” Neurology, vol. 88, no. 24, pp. 2246–2247, 2017.
[58] B. A. Dworetzky and C. Reinsberger, “The role of the interictal eeg
in selecting candidates for resective epilepsy surgery,” Epilepsy Behav.,
vol. 20, no. 2, pp. 167–171, 2011.

[59] Z. Fitzgerald et al., “Improving the prediction of epilepsy surgery outcomes
using basic scalp eeg ﬁndings,” Epilepsia, vol. 62, no. 10, pp. 2439–2450,
2021.

[60] C. Tonini et al., “Predictors of epilepsy surgery outcome: A meta-analysis,”

Epilepsy Res., vol. 62, no. 1, pp. 75–87, 2004.

[61] A. P. Millán et al., “Epidemic models characterize seizure propagation
and the effects of epilepsy surgery in individualized brain networks based
on MEG and invasive EEG recordings,” Sci. Rep., vol. 12, no. 1, 2022,
Art. no. 4086.

[62] A. P. Millán et al., “Individualized epidemic spreading models predict
epilepsy surgery outcomes: A pseudo-prospective study,” Netw. Neurosci.,
vol. 8, no. 2, pp. 437–465, 2024.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:33 UTC from IEEE Xplore.  Restrictions apply.
