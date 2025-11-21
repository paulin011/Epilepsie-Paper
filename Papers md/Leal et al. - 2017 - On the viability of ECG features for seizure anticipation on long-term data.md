# Leal et al. - 2017 - On the viability of ECG features for seizure anticipation on long-term data

On the viability of ECG features for seizure anticipation on long-term
data

Adriana Leal, Maria da Grac¸a Ruano, Jorge Henriques, Paulo de Carvalho and C´esar Teixeira
CISUC, Department of Informatics Engineering
Coimbra, Portugal
{aleal, mruano, jh, carvalho, cteixei}@dei.uc.pt

Abstract— Besides the evident brain state alterations present
in electroencephalogram (EEG), epileptic seizures are also
associated with changes in the cardiovascular status. In par-
ticular, heart rate (HR) has become an important autonomic
biomarker in seizure prediction. Based on that, a preliminary
study is here proposed in order to inspect the behaviour
of electrocardiogram (ECG) derived features in the period
preceding epileptic seizures. The study took place using data
from 1275 seizures collected from a set of 167 patients available
in EPILEPSIAE database. The analysis was conducted consid-
ering three different variables: seizure type, seizure hour onset
and vigilance state.

The results did not reveal a clear effect of any of the
three variables, assessed individually,
in entire seizure set.
Nevertheless, some evidence has been found that, for some
seizures, it was possible to detected a consistent pattern of
increase/decrease in feature magnitude before the onset. These
patterns were revealed using the mean of RR intervals and
the mean of the number of beats per minute.

Keywords—epilepsy;

seizure; anticipation;

electrocardio-

gram.

I. INTRODUCTION

The management of refractory epileptic patients requires
systems able to provide warning before seizures onset to the
patients during their everyday life.

The vast majority of epileptic seizure prediction studies
available in literature has been proposed using information
from electroencephalogram (EEG), which is composed of
a mixture of different cerebral activities. Due to EEG com-
plexity no mathematically sensible features to the pre-seizure
period were developed until now [1], [2]. In recent years,
however, a great focus has been put in other seizure extrac-
erebral manifestations including the often reported changes
in the cardiovascular status. In fact, the autonomic func-
tion is affected during seizures, subsequently triggering the
parasympathetic and sympathetic system responses which in
turn will be responsible for modulation of cardiac parameters
such as heart rate and blood pressure [3], [4], [5]. An increase
in heart rate (HR) and blood pressure, possible occurrence
of tachycardia, atrio-ventricular conduction and ventricular
excitability are the result of the sympathetic nervous activity.
On the other hand, the effect of the parasympathetic response
can be detected when there is a decrease in the heart rate and
blood pressure [4], [5], [6], [7], [8].

HR was reported to increase during seizures, being typi-
cally associated with high variability regarding its magnitude,

velocity and duration depending for example on the vigilance
state (sleep versus awake) [3]. In face of these observations,
new studies were proposed addressing the differences in HR
across the periods preceding, during and after the seizure
[4], [9]. Results from 30 refractory epilepsy patients have
shown statistically signiﬁcant differences among different
seizure stages [9]. Furthermore, HR variations related to the
occurrence of epileptic seizures, besides the vigilance state,
can also be inﬂuenced by other aspects such as the type of
epilepsy, location of seizure onset, seizure type, patients’ age
and gender and time to diagnosis [3], [10].

Apart from the refereed HR variations, the morphology
of the electrocardiogam (ECG) also depicts changes that
typically occur before the EEG onset, making the former
useful for seizure early detection [5], [11]. For example,
it was observed that the QT interval diminished during the
early post-ictal period in patients diagnosed with refractory
epilepsy whereas in the pre-ictal phase, a T wave inversion
and ST elevation or depression happened [5], [7], [11].

Varon et al. achieved a positive predictive value of 80%
in a 30s window near EEG onset using HRV and also the
changes in the ECG morphology, obtained from 37 patients
[11]. A sensitivity of 91% and false-positive rate (FPR) of
0.7 times per hour was obtained by Fujiwara et al. using HRV
features from 14 patients [12]. Behbahani et al. obtained
accuracies of 86.74% and 79.41% when classifying 86 left-
sided and 84 right-sided seizures, respectively, using HRV
collected from 16 patiets [13].

Based on the aforementioned, the current work was de-
veloped in order to understand which variables, including
seizure type, lateralization, location, among others, can con-
tribute to discriminate between the different set of seizures
identiﬁed in a speciﬁc patient and for different patients.
Towards that end, information from ECG features will be
analysed and interpreted in light of the metadata available,
for each seizure and patient. Long-term continuous ECG
data and associated metadata are provided by the European
Epilepsy Database (EPILEPSIAE).

II. MATERIAL AND METHODS

A. Data

The study was conducted using ECG information from the
European Epilepsy Database, also known as the EPILEP-
SIAE database (http://epilepsy-database.eu). The database

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:02 UTC from IEEE Xplore.  Restrictions apply. 

Fig. 1: RRMean feature computed for a single patient. Days are separated by different colors. Seizures are indicated in red. Information is
provided regarding the seizure type (SP: simple partial seizure, UC: unclassiﬁed seizure) and the vigilance state (A: awake, 2: NonREM
stage II). Seizures that are not separated by at least 240 min from the preceding seizure are not analysed.

contains long-term (165 h on average per patient) and
simultaneous EEG and ECG recordings of 275 refractory
epilepsy patients acquired in the epilepsy centres of the
University Hospital of Freiburg, Germany, of the University
Hospital of Coimbra, Portugal, and of the Hˆopital de la
Piti´e-Salpˆetri`ere of Paris, France [14], [15]. The majority
of EEG data was acquired non-invasively (217 patients).
The number of seizures per patient can go from 3 up to
94. Information about the etiology of the epileptic patient,
seizure type (e.g., simple partial, complex partial, secon-
darily generalized), seizure localization (temporal, frontal,
occipital, parietal), seizure vigilance state, and medication,
among other variables is also available. Most of the recorded
seizures have been doubly annotated, which means that two
types of annotations are provided: electrographic changes in
EEG and clinical changes detected by video-EEG analysis
[14]. The results present in this work are provided by the
analysis of 1275 seizures from 167 patients (accounting for
1260 days of ECG signal) having information regarding
vigilance state, seizure type and seizure onset hour.

B. Methods

Time-domain features were obtained from the ECG
signals using a 5-min window and a 98% overlap. The
feature set comprises:

• The minimum, maximum, mean and variance of RR

intervals (RRMin, RRMax, RRMean and RRVar).

• HR statistics: minimum (BPMMin), maximum (BPM-
Max), mean (BPMMean) and variance (BPMVar) of the
number of beats per minute (BPM).

• A measure of complexity of a time series given by

approximate entropy (AppEn).

Another four features were obtained from the frequency
spectrum analysis of the ECG data and stand as frequency-
domain measures of HRV:

• The power in the very-low-frequency (VLF) range:

0.003–0.04 cycles/interval.

• The power in the low-frequency (LF) range: 0.04–0.15

cycles/interval.

• The power in the high-frequency (HF) range: 0.15–0.4

cycles/interval.

• The ratio of the low-frequency-range power to that in

the high-frequency range (LF/HF).

An example of the obtained features is depicted in Figure
1 for the RRMean, where it is possible to observe a recurrent
pattern deﬁned by an increase in average of the RR intervals
during the night, which manifestly corresponds to periods
when the patient is at rest.

In order to inspect the behaviour of the ECG features four
hours before the seizure happens, the correlation between
the ECG feature and the time sequence corresponding to that
period was obtained using the Pearson correlation coefﬁcient
(as can be seen in Figure 2) and named CorrCoef. According
to this procedure, a value of correlation is obtained for each
seizure and the idea was to analyse those correlation values
in light of the metadata characterizing each seizure (vigilance
state, seizure type and occurrence hour). An example is
depicted in Figure 3. For each seizure data, correlation is
performed ﬁrst for an increasing time vector and secondly
for a decreasing time vector. The ﬁnal value of correlation
considered for that seizure will correspond to the maximum
of the two correlation values. When maximum corresponds
to the correlation with the decreasing time vector, the ﬁnal
correlation value is deﬁned to have negative sign. in this
way, it is possible to distinguish between an increase or a
decreased in feature magnitude before seizure arising.

III. RESULTS AND DISCUSSION

The analysis of the plots of the correlation between the
features and the corresponding regression line for each of
the 1275 seizures (take the example of Figures 3, 4 and 5)
allowed us to conclude that, even though a high correlation

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:02 UTC from IEEE Xplore.  Restrictions apply. 

(a)

(b)

Fig. 2: (a) Example of high correlation between feature RRMean obtained from seizure 190 and the time vector, with CorrCoef = 0.88.
(b) Example of low correlation between feature RRMean obtained from seizure 193 and the time vector, with CorrCoef = 0.39.

Fig. 3: Results for RRMean feature regarding the vigilance state variable. A: awake state, 2: NonREM sleep stage II, 3: NonREM sleep
stage III, 4: NonREM sleep stage IV, R: REM sleep stage, ?: unknown. Results for the seizures (each point) referring to a given patient
are delimited by two vertical lines.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:02 UTC from IEEE Xplore.  Restrictions apply. 

20015010050Time(min)750800850900950RRMean(ms)Seizure20015010050Time(min)900950100010501100RRMean(ms)Seizure0100200300400500600-1-0.500.51CorrCoefRRMeanVigilancestate-1-0.500.51050100700800900100011001200seizure-1-0.500.51CorrCoefRRMeanA21R34?-1-0.500.51050100Fig. 4: Results for BPMMean feature regarding the seizure onset hour variable. Results for the seizures (each point) referring to a given
patient are delimited by two vertical lines.

Fig. 5: Results for RRMax feature regarding the seizure type variable. FOA: focal onset aware, FOIA: focal onset impaired awareness,
UC: unclassiﬁed, FBTC: focal to bilateral tonic-clonic. Results for the seizures (each point) referring to a given patient are delimited by
two vertical lines.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:02 UTC from IEEE Xplore.  Restrictions apply. 

0100200300400500600-1-0.500.51CorrCoefBPMMeanSeizureonsettime(hour)-1-0.500.51050100700800900100011001200seizure-1-0.500.51CorrCoefBPMMean12<=sh<180<=sh<618<=sh<246<=sh<12-1-0.500.510501000100200300400500600-1-0.500.51CorrCoefRRMaxSeizuretype-1-0.500.51050100150700800900100011001200seizure-1-0.500.51CorrCoefRRMaxFOAFOIAUCFBTC-1-0.500.51050100150has been obtained for some seizures that variation was not
associated with a particular vigilance state, seizure onset
hour or seizure type. In other words, a coherent incremental
evolution (sometimes increase other times decrease) of the
feature magnitude until
the seizure occurrence has been
noticed in only a few seizures not being associated to any
of the tested variables.

However, it was possible to observe that, in general, higher
values of correlation were obtained for features such as
RRMax, RRMean, BPMMean and BPMMin, indicating that
these features have more potential to exhibit a consistent
pattern of transition from normal to seizure state.

IV. CONCLUSIONS

The present study represents a preliminary study of the
potential of ECG features for seizure prediction. It was
possible to observe a coherent behaviour of increasing or
decreasing feature magnitude for some seizures whereas for
others such pattern was not present. The variables vigilance
state, seizure type and seizure occurrence hour were not
speciﬁcally associated to an increase or decrease in feature
magnitude as the temporal distance to the seizure diminishes.
Average of RR intervals and average of the number of beats
per minute were the ECG features that best described an
increment/decrement in magnitude before the seizure onset.
The period preceding the seizure must be extensively studied
taking into account the peculiarities of seizure occurrence in
a given patient and in a speciﬁc epilepsy population. To that
end, more studies regarding the circumstances characterizing
each seizure must be undertaken.

REFERENCES

[1] D. R. Freestone, P. J. Karoly, A. D. H. Peterson, L. Kuhlmann, A. Lai,
F. Goodarzy, and M. J. Cook, “Seizure Prediction: Science Fiction or
Soon to Become Reality?” p. 73, nov 2015.

[2] S. Ramgopal, S. Thome-Souza, M. Jackson, N. E. Kadish, I. S´anchez
Fern´andez, J. Klehm, W. Bosl, C. Reinsberger, S. Schachter, and
T. Loddenkemper, “Seizure detection, seizure prediction, and closed-
loop warning systems in epilepsy,” Epilepsy & Behavior, vol. 37, pp.
291–307, aug 2014.

[3] M. Bialer, S. I. Johannessen, R. H. Levy, E. Perucca, T. Tomson, H. S.
White, and M. J. Koepp, “Seizure detection and neuromodulation: A
summary of data presented at the XIII conference on new antiepileptic
drug and devices (EILAT XIII),” Epilepsy Research, vol. 130, pp. 27–
36, feb 2017.

[4] K. Jansen and L. Lagae, “Cardiac changes in epilepsy.” Seizure,

vol. 19, no. 8, pp. 455–60, oct 2010.

[5] O. Devinsky, “Effects of Seizures on Autonomic and Cardiovascular

Function,” Epilepsy Currents, vol. 4, no. 2, pp. 43–46, 2004.

[6] M. Nei, “Cardiac Effects of Seizures,” Epilepsy Currents, vol. 9, no. 4,

pp. 91–95, 2009.

[7] F. J. Rugg-Gunn and D. Holdright, “Epilepsy and the Heart,” British

Journal of Cardiology, pp. 223–229, 2010.

[8] D. Cogan, J. Birjandtalab, M. Nourani, J. Harvey, and V. Nagaraddi,
“Multi-Biosignal Analysis for Epileptic Seizure Monitoring,” Interna-
tional Journal of Neural Systems, vol. 27, no. 01, p. 1650031, feb
2017.

[9] M. Zare, M. Salari, M. Tajmirriahi, M. Saadatnia, and R. Norouzi,
“Electrocardiographic changes in patients with refractory epilepsy.”
Journal of research in medical sciences : the ofﬁcial journal of Isfahan
University of Medical Sciences, vol. 18, no. Suppl 1, pp. S32–4, mar
2013.

[10] I. Osorio and B. Manly, “Probability of detection of clinical seizures
using heart rate changes,” Seizure, vol. 30, pp. 120–123, 2015.
[11] C. Varon, K. Jansen, L. Lagae, and S. Van Huffel, “Can ECG
monitoring identify seizures?” in Journal of Electrocardiology, vol. 48,
no. 6, 2015, pp. 1069–1074.

[12] K. Fujiwara, M. Miyajima, T. Yamakawa, E. Abe, Y. Suzuki,
Y. Sawada, M. Kano, T. Maehara, K. Ohta, T. Sasai-Sakuma,
T. Sasano, M. Matsuura, and E. Matsushima, “Epileptic Seizure Pre-
diction Based on Multivariate Statistical Process Control of Heart Rate
Variability Features,” IEEE Transactions on Biomedical Engineering,
vol. 63, no. 6, pp. 1321–1332, jun 2016.

[13] S. Behbahani, N. J. Dabanloo, A. M. Nasrabadi, and A. Dourado,
“Prediction of epileptic seizures based on heart rate variability,”
Technology and Health Care, vol. 24, no. 6, pp. 795–810, nov 2016.

[14] J. Klatt, H. Feldwisch-Drentrup, M. Ihle, V. Navarro, M. Neufang,
C. Teixeira, C. Adam, M. Valderrama, C. Alvarado-Rojas, A. Witon,
M. Le Van Quyen, F. Sales, A. Dourado, J. Timmer, A. Schulze-
Bonhage, and B. Schelter, “The EPILEPSIAE database: An exten-
sive electroencephalography database of epilepsy patients,” Epilepsia,
vol. 53, no. 9, pp. 1669–1676, sep 2012.

[15] M. Ihle, H. Feldwisch-Drentrup, C. A. Teixeira, A. Witon, B. Schelter,
J. Timmer, and A. Schulze-Bonhage, “EPILEPSIAE A European
epilepsy database,” Computer Methods and Programs in Biomedicine,

vol. 106, no. 3, pp. 127–138, jun 2012.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:02 UTC from IEEE Xplore.  Restrictions apply.
