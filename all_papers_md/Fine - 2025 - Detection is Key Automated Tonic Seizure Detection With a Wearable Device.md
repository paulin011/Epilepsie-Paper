# Fine - 2025 - Detection is Key Automated Tonic Seizure Detection With a Wearable Device

Detection is Key: Automated Tonic Seizure
Detection With a Wearable Device

Current Literature
in Clinical Research

Epilepsy Currents
2025, Vol. 25(1) 36–38
© The Author(s) 2024
Article reuse guidelines:
sagepub.com/journals-permissions
DOI: 10.1177/15357597241293298
journals.sagepub.com/home/epi

Automated detection of tonic seizures using wearable movement sensor and artiﬁcial neural network
Larsen SA, Johansen DH, Beniczky S. Epilepsia. 2024 Jul 30. doi: 10.1111/epi.18077. Epub ahead of print. PMID: 39076045.

Although several validated wearable devices are available for the detection of generalized tonic-clonic seizures, automated
detection of tonic seizures is still a challenge. In this phase 1 study, we report the development and validation of an artiﬁcial
neural network (ANN) model for automated detection of tonic seizures with visible clinical manifestation using a wearable
wristband movement sensor (accelerometer and gyroscope). The dataset prospectively recorded for this study included 70
tonic seizures from 15 patients (7 males, age 3-46 years, median = 19 years). We trained an ANN model to detect tonic sei-
zures. The independent test dataset comprised nocturnal recordings, including 10 tonic seizures from 3 patients and additional
(distractor) data from 3 subjects without seizures. The ANN model detected nocturnal tonic seizures with visible clinical man-
ifestation with a sensitivity of 100% (95% conﬁdence interval = 69%-100%) and with an average false alarm rate of 0.16/night.
The mean detection latency was 14.1 s (median = 10 s), with a maximum of 47 s. These data suggest that nocturnal tonic
seizures can be reliably detected with movement sensors using ANN. Large-scale, multicenter prospective (phase 3) trials
are needed to provide compelling evidence for the clinical utility of this device and detection algorithm.

Commentary

trial

investigators,

Real-time seizure monitoring devices are appealing for many
reasons. For clinical
to track accurate
seizure counts during a study period rather than rely on
seizure diaries1,2; for providers, to know how frequently their
patient is truly having clinical seizures and if the current thera-
pies are efﬁcacious; for patients who live alone, to get a sense of
how frequently they are having unwitnessed seizures; and for
caregivers, to get alerts when their loved one is having sei-
zures.3,4 Several monitoring devices have been investigated
and assessed for validity. These have been most successful
for seizures with prominent motor features, speciﬁcally general-
ized tonic-clonic seizures or focal to bilateral tonic-clonic sei-
zures.5,6 One issue with commercially available devices and
previously investigated devices is a high false-positive rate
which can limit real-world applicability and lead to discontinu-
ation of use by patients and caregivers.7

Larsen et al. present the results of their phase 1 study on the
development and validation of an automated neural network
(ANN) model trained to detect tonic seizures using a wearable
wrist sensor.8 Their wristband sensor included an accelerometer
and gyroscope, which collected 6 continuous axis measure-
ments, with a threshold for feature extraction of a minimum
acceleration of 0.1 g. Features were extracted in 10-s intervals
with 1-s overlap, with 594 features, such as mean, variance, and

standard deviation, extracted for each of the six sensor readings.
Enrolled patients were monitored using the author’s epilepsy
center’s standard of care in the epilepsy monitoring unit, including
video-electroencephalography (vEEG) and surface electromy-
ography (sEMG) electrodes. Video-EEG recordings were inde-
pendently reviewed by 2 experts, blinded to the sensor data,
who assessed for tonic seizures during the recording periods
of 1 to 3 days for the subjects. Fifteen patients aged 3 to 46 years,
with tonic seizures detectable on both vEEG and sEMG, were
included. Data on tonic seizures was split for training of the
algorithm and for testing. Additional subjects with tonic sei-
zures were recruited for the test dataset which was compared
to nocturnal data for subjects without any history of seizures
for evaluation of speciﬁcity and the false alarm rate. The auto-
mated neural network was developed and validated using the
independent test data.

Results were notable for accurate detection of tonic seizures
and a sensitivity of 100% using the independent dataset. The
false alarm rate was 0.023/h in the same dataset. For the com-
plete dataset, the sensitivity was 96% with a false alarm rate
of 0.23 per night. Looking at the entire dataset, which included
18 patients, the median false alarm rate per patient was 0 per
night, with expected triggers for false alarms for tonic seizures
including voluntary movements, arousals from sleep, and phys-
iologic movements during sleep. Overall, these results show
signiﬁcant promise in the future development of wearable

Creative Commons Non Commercial CC BY-NC: This article is distributed under the terms of the Creative Commons Attribution-NonCommercial 4.0 License
(https://creativecommons.org/licenses/by-nc/4.0/) which permits non-commercial use, reproduction and distribution of the work without further permission
provided the original work is attributed as speciﬁed on the SAGE and Open Access page (https://us.sagepub.com/en-us/nam/open-access-at-sage).

Commentary

37

technology which can accurately detect nocturnal tonic seizures
with a low false positive rate.

battery life or poor Wi-Fi signal, or other connectivity issues
also play a role in how successful a device can be.11

types

seizure

and many times

While the results of Larsen and colleagues show that
improvements in seizure detection devices are on the horizon,
the authors acknowledge several limitations. This study popula-
tion, particularly the independent test pool, was small and there-
fore, future phase 3 studies, with real-time seizure detection, are
needed for further validation of this model and determination of
the clinical applicability of this ANN. Another point was that
this algorithm and the data collected were complex, with the
ANN and analysis done ofﬂine (i.e., not in real-time) on a PC
and not through embedded software in the wristband device.
If additional complexity or further parameters are needed, would
this be something that can be translated to the wearable device and
still retain the same degree of accuracy? This also brings up one
of the authors’ other points—patients with nocturnal tonic seizures
a
typically have other
Lennox-Gastaut syndrome phenotype. Other algorithms, such as
one targeting generalized tonic-clonic or focal to bilateral tonic-clonic
seizures,9 would need to be run in parallel and would likely result in a
higher false positive rate. The study also excluded subtle tonic sei-
zures which did not have a clear motor component but was picked
up by sEMG, which did not account for many seizures in this cohort.
Currently, there continue to be challenges in translating arti-
ﬁcial intelligence into epilepsy clinical practice. We can look
individually at a wearable device, or detection of a single
seizure type, or a set of machine learning models, but this is
still just a fraction of the information needed compared to the
large amount of rigorously reviewed, high-quality, standardized
data necessary for true clinical translation into practice.10 As
with other epilepsy research, multicenter collaboration is impor-
tant for sharing data and algorithms to assist with the collection
of standardized data in the development stage and to test gener-
alizability later. In the current example of seizure detection, the
likelihood of accurately detecting seizures would be low and the
false positive rate high if the data quality and breadth were
insufﬁcient, and generalizability were not adequately tested.

Larsen et al.’s study was performed in their epilepsy moni-
toring unit under ideal settings. In a real-world environment,
would the studied detection algorithms perform as well?
Many potential confounders need to be considered, including
environmental factors, such as signal interference from the
abundant number of electronics that the patient will encounter
on a day-to-day basis; patient factors, like excess movements
due to physical activity effecting sEMG inputs; and device
factors, such as battery life and durability. Other real-world consid-
erations include the needs and resources of patients and caregivers.
Seizure monitoring devices can be cost-prohibitive for some
patients, as devices may or may not be covered by insurance
and there typically exist monthly subscriptions for service.
Wearable device users tend to skew toward higher-income patients
and caregivers.3 The requirements of a stable internet connection
for data uploading or Wi-Fi of Bluetooth, for communication of
the sensor with the control unit, may not be available in rural
areas, or those from lower income or underserved populations.
The comfort level of the wearable over time, annoyances with

Real-time seizure detection devices can be appealing to
patients and caregivers, by reducing anxiety about unwitnessed
seizures, providing a sense of safety, and potentially providing a
greater sense of independence for some.3,4 For clinicians,
having an accurate seizure count can be extremely helpful to
assess whether a current treatment regimen is successful or
not; for research, accurate seizure diaries can make or break a
study; however, for patients who live alone, do not recall
their seizures, have unreliable witnesses, or who do not accu-
rately record seizures, this can be a challenge.1,2

While far from ready for commercial use, the present study
certainly brings hope that there continues to be progress in the
landscape of seizure detection devices. This is certainly some-
thing that frequently is asked about in my clinic by families
and caregivers. From both the clinical and research perspec-
tives, I think that having accurate seizure counts and classiﬁca-
tion of seizures would be a great boon. From a parent or patient
perspective, I can also see how having an accurate wearable
device that has a low false alarm rate would reduce anxiety
and potentially improve health-related quality of life.

Anthony L. Fine, MD
Department of Neurology
Mayo Clinic
Rochester
MN
USA

ORCID iD

Anthony L. Fine

https://orcid.org/0000-0001-5256-8368

Declaration of Conﬂicting Interests
The author(s) declared no potential conﬂicts of interest with respect to
the research, authorship, and/or publication of this article.

Funding
The author(s) received no ﬁnancial support for the research, author-
ship, and/or publication of this article.

References

1. Akman CI, Montenegro MA, Jacob S, Eck K, Chiriboga C,
Gilliam F. Seizure frequency in children with epilepsy: factors
inﬂuencing
Seizure.
2009;18(7):524–529.

awareness.

accuracy

parental

and

2. Blachut B, Hoppe C, Surges R, Stahl J, Elger CE, Helmstaedter C.
Counting seizures: the primary outcome measure in epileptology
from the patients’ perspective. Seizure. 2015 Jul;29:97–103.
3. Chiang S, Moss R, Patel AD, Rao VR. Seizure detection devices
and health-related quality of life: a patient- and caregiver-centered
evaluation. Epilepsy Behav. 2020 Apr;105:106963. doi: 10.1016/j.
yebeh.2020.106963. Epub 2020 Feb 22. PMID: 32092459.

4. Thompson ME, Langer J, Kinfe M. Seizure detection watch improves
quality of life for adolescents and their families. Epilepsy Behav. 2019
Sep;98(Pt A):188–194. doi: 10.1016/j.yebeh.2019.07.028

38

Epilepsy Currents 25(1)

5. Patterson AL, Mudigoudar B, Fulton S, et al. Smartwatch by
SmartMonitor: assessment of seizure detection efﬁcacy for
various seizure types in children, a large prospective single-center
study. Pediatr Neurol. 2015 Oct;53(4):309–311. doi: 10.1016/j.
pediatrneurol.2015.07.002

6. Onorati F, Regalia G, Caborni C, et al. Multicenter clinical assess-
ment of improved wearable multimodal convulsive seizure detectors.
Epilepsia. 2017 Nov;58(11):1870–1879. doi: 10.1111/epi.13899
7. Brinkmann BH, Karoly PJ, Nurse ES, et al. Seizure diaries and
forecasting with wearables: epilepsy monitoring outside the
clinic. Front Neurol. 2021 Jul 13;12:690404. doi: 10.3389/fneur.
2021.690404

8. Larsen SA, Johansen DH, Beniczky S. Automated detection of
tonic seizures using wearable movement sensor and artiﬁcial

neural network. Epilepsia. 2024;65:e170-e174. doi: 10.1111/epi.
18077

9. Beniczky S, Polster T, Kjaer TW, Hjalgrim H. Detection of gen-
eralized tonic-clonic seizures by a wireless wrist accelerometer:
a prospective, multicenter study. Epilepsia. 2013;54(4):e58–e61.
doi: 10.1111/epi.12120

the international

10. Lhatoo SD, Bernasconi N, Blumcke I, et al. Big data in epilepsy:
clinical and research considerations. Report from the epilepsy big
data task force of
league against epilepsy.
Epilepsia. 2020;61(9):1869–1883. https://doi.org/10.1111/epi.16633
11. Meritam P, Ryvlin P, Beniczky S. User-based evaluation of
applicability and usability of a wearable accelerometer device
tonic-clonic seizures: a ﬁeld study.
for detecting bilateral
Epilepsia. 2018 Jun;59(Suppl 1):48–52. doi: 10.1111/epi.14051
