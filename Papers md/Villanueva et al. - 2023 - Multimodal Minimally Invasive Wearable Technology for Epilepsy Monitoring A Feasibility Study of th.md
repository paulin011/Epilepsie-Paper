# Villanueva et al. - 2023 - Multimodal Minimally Invasive Wearable Technology for Epilepsy Monitoring A Feasibility Study of th

26620

IEEE SENSORS JOURNAL, VOL. 23, NO. 21, 1 NOVEMBER 2023

Multimodal Minimally Invasive Wearable
Technology for Epilepsy Monitoring:
A Feasibility Study of the
Periauricular Area

Guillermo M. Besné Villanueva , Peio Lopez-Iturri

, Manuel Alegre Esteban ,

Julio Artieda González Granda , Jesús D. Trigo , Luis Serrano-Arriezu , Senior Member, IEEE,
Francisco Falcone , Senior Member, IEEE, and Miguel Valencia Ustarroz

Abstract—Ambulatory monitoring is of great interest in
both clinical and domestic environments. Despite the tech-
nological advances, few monitoring solutions are suitable for
medical application and diagnosis. Here, we investigate the
feasibility of targeting the periauricular area (ear pavilion, ear
canal, and the surrounding skin areas) to implement a mul-
timodal system that fulfills the requirements of ergonomics
and minimal obstructiveness in the context of epilepsy mon-
itoring. Six physiological signals are selected and explored for their integration in the area of interest and a
“proof-of-concept” prototype integrating the components in a single portable device targeting the selected location
is implemented. Results show mixed results where some parameters are highly reliable, and others are impractical
or require customized technology to provide clinically relevant information. To enable data acquisition, storage, and
processing within the Internet of Medical Things paradigms, wireless body area transceiver integration is also analyzed
in terms of coverage/capacity relations, showing feasibility for such device configuration.

Index Terms— Ambulatory monitoring, epilepsy, multimodal wearable, periauricular area.

I. INTRODUCTION

T HE chronification of some diseases and the increase

in technological knowledge by the general population
results on a higher number of medical experts, patients, and
relatives demanding a better use of technological innovations.

Manuscript

received 28 August 2023; accepted 6 September
2023. Date of publication 18 September 2023; date of current
version 31 October 2023. This work was supported in part by
the Government of
the Department of Economic Development of
Navarra under Grant GN 2019 PC078-079;
in part by the Carlos
III Health Institute through the project under Grant DTS19/00130
(co-financed by the European Regional Development Fund; “A way
to make Europe”); and in part by the Agencia Estatal de Investi-
gación, Fondo Europeo de Desarrollo Regional -FEDER-, European
Union under Grant PID2021-127409OB-C31 CONDOR. The work of
Guillermo M. Besné Villanueva was supported by the “Asociación de
Amigos de la Universidad de Navarra, ADA” during his Ph.D. The
associate editor coordinating the review of this article and approving
it
for publication was Dr. Edward Sazonov. (Corresponding author:
Miguel Valencia Ustarroz.)

This work involved human subjects or animals in its research.
Approval of all ethical and experimental procedures and protocols was
granted by the Local Ethical Committee of the University of Navarra
under Approval No. CEIC-2021.143.

Please see the Acknowledgment section of this article for the author

affiliations.

Digital Object Identifier 10.1109/JSEN.2023.3314190

Their claim is to ensure accurate diagnosis and provide
continuous monitoring and personalized treatments [1], [2],
[3], [4], [5].

In recent years, technological advances have made it possi-
ble to implement increasingly versatile sensors, smaller in size
and with lower consumption. These developments, together
with the possibility of transmitting, processing, and storing
a large amount of information, might represent a shift of
paradigm in the way we understand and use “data” for disease
management. Technology has improved consumer electronics
leading to a surge of wearable devices capable of moni-
toring physiological parameters, such as hear rate, calories
consumption, physical exercise intensity, or estimates of sleep
stages. However, very few of these solutions are suitable for
medical application and diagnosis [6]. This might be explained
by the fact that the process of adopting some technological
solution for monitoring diseases is not easy [7], [8], [9], [10].
Leaving aside concepts, such as privacy and clinical data
security, their success lies in the ability to implement features
such as: 1) portability; 2) ease of use; 3) robustness; 4) preci-
sion (compared to those provided by clinical and specialized
settings); and 5) coverage of parameters to provide (clini-
cally) relevant information. In addition, and depending on

1558-1748 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

BESNÉ VILLANUEVA et al.: MULTIMODAL MINIMALLY INVASIVE WEARABLE TECHNOLOGY

26621

the disease or monitoring circumstances, it is necessary to
identify, among others, the most suitable variables of interest,
location/optimization of the sensitization points, degree of
miniaturization,
level of obstruction, anatomic constraints,
or ergonomics needs.

Continuous monitoring and personalized follow-up is of
high interest in diseases, such as epilepsy: a chronic neu-
rologic condition marked by the recurrence of unprovoked
seizures [11], [12]. Seizures are paroxysmal events that result
from abnormal neuronal discharges and manifest in the form
of sudden, stereotyped episodes with accompanying changes
in motor activity, sensation, and behavior,
thus exposing
the patient to life-threatening situations [13], [14]. Seizures
result in increased injuries and mortality, including sudden
unexpected death in epilepsy (SUDEP). This scenario makes
constant supervision a requirement, even during night [15],
[16]. The need of chronic intake of antiepileptic drugs (AEDs)
also leads to potential side effects that require continuous
adjustment of the treatment. Despite handwritten diaries where
patients’ evolution is reflected, disease perception and patients’
mood have drastic effects on reports to neurologists and neu-
ropediatricians. Consequently, unnecessary or even inadequate
treatment adjustments are frequent [17].

All these scenarios justify the need for monitoring sys-
tems suitable for their operation on domestic or ambulatory
environments. Ideally, such developments should implement
multimodal, minimally obstructive monitoring systems capable
to provide information clinically relevant to assess the phys-
iological and neurological state of the subject. As critical as
the parameters to measure, it is also important to identify an
appropriate recording location. All parameters selected must
be susceptible to be measured, with little or nonintrusive
approximation, complying with structural stability capable of
supporting robust and prolonged monitoring periods of time.
The periauricular area (the external ear, the ear canal, and the
surrounding skin area) seems to be a good candidate; the
anatomical location and rigidity of the ear canal provide great
support to anchor potential devices, such as earphones or
hearing aids with low stigmatization. In addition, previous
reports have described the possibility of obtaining reliable,
long term, and clinically relevant measures of different biosig-
nals. Nevertheless, combining several signal modalities in
one single setup represents a big challenge and requires the
systematic assessment of their feasibility when being recorded
at the same time.

In the case of epilepsy patients, a number of such physio-
logical measurements can be of special relevance; parameters,
such as electroencephalogram (EEG), acceleration (Acc), elec-
trocardiogram (ECG), peripheral oximetry (SpO2), body core
temperature (Tª), and galvanic skin response (GSR), could pro-
vide an integral assessment of the general state of the patient.
The EEG is the register of electrical activity generated by
the brain [18], [19]. In the case of epilepsy, the EEG represents
one of the most important tools for diagnosis and follow-up. In
epileptic patients both during seizures and interictal periods,
the brain generates abnormal activities easily identified in
the EEG traces. In this context, EEG recordings in the ear
canal have been introduced recently [20] resulting in different
implementations that also include wireless capabilities [21],

[22], [23], [24], [25]. In the area of interest, the EEG can
be recorded through electrodes located within the ear canal
(in-earEEG) or disposed around the ear pavilion and provide
relevant information for the detection of seizures in patients
with focal and generalized epilepsies [26], [27].

Acceleration represents a straightforward method to quan-
tify the amount of movement. Measurements can refer to
dynamic acceleration, where speed changes of the monitored
object are quantified; or static acceleration with measurements
are due to gravity, thus making it possible to estimate the
object’s orientation relative to Earth’s surface. In the case of
epilepsy, acceleration has been successfully integrated into
warning systems to detect seizures [28], [29]. In addition,
it can be used for fall detection and head orientation assess-
ment [30], to quantify the amount of movement and identify
postural changes or the presence of abnormal movements [31].
As for placement, the acceleration measurement of the head
is less restrictive with its placement. As a rigid body, the
movement of the head can be monitored at any point, including
the periauricular area.

ECG records electrical activity from the heart myocardium
[32]. Polarization and depolarization sequences leading to
heart contraction result in a series of waveforms that can be
divided into P-wave, QRS complex, and T-wave. To obtain a
high-quality ECG suitable for cardiovascular diagnosis, a set
of nine electrodes are required [33]. However, for simpler
approaches, such as those aimed at estimating the heart rate
(HR) or their variations in time [heartrate variability (HRV)],
three or even two electrodes are sufficient. Variations on the
HR are used as surrogates of distress at multiple levels; in
the context of epilepsy, they have proved to be useful to
detect the occurrence and onset of epileptic seizures [34],
[35], [36], and SUDEP events. Nevertheless, and in the case of
periauricular area (under the constraint of unique and unilateral
placement of the electrodes), the geometry of the heart ver-
sus (one) ear could present some difficulties to provide reliable
ECG measurements.

Photoplethysmography (PPG) measures volumetric varia-
tions of blood circulation though optical inexpensive methods.
By using different light sources and photodetectors at the
surface of skin, PPG allows to estimate HR, oxygen saturation
in peripheral blood (SpO2), and other parameters suitable for
assessing the state of the cardiovascular system [37], [38].
Green light (530 nm) sources are optimal to determine the
HR on continuous monitoring setups as it is more sensible
to small volume changes and results more robust against
movement artifacts [39]. Complementarily, red (650 nm) and
infrared (IR, 940 nm) sources are used to exploit absorption
differences of hemoglobin on its reduced (Hb) and oxyg-
enized (HbO2) state and permit
to extract SpO2 [40]. In
the context of epilepsy, PPG can serve to estimate HR and
HRV as an alternative to ECG measures. It allows to study
cardiorespiratory coupling changes and SpO2 levels can be
useful to predict/detect epileptic seizures, although it might
be problematic to implement for tonic–clonic seizures [41],
[42], [43]. Common placements for PPG sensors include
the earlobe that it is highly irrigated. Fingers are the most
usual, but other implementations with custom PPG sensors
on in-ear devices have been built and performed satisfactorily

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

26622

IEEE SENSORS JOURNAL, VOL. 23, NO. 21, 1 NOVEMBER 2023

acquiring the PPG signal on the concha or
canal [44].

in the ear

As endothermic animal, humans can generate their own
body temperature by means of metabolic rate, sweating, vaso-
constriction, and other physiological mechanism. The most
common alteration in temperature is fever, an abnormal rise
on core body temperature. The ability of thermoregulation
and being able to withstand external temperature varies at
different ages. Adults have larger bodies and greater volume-
to-surface ratio, and therefore, a higher resistance to external
temperatures affects their core body temperature. As such,
children are more susceptible to suffering hyperthermia and
hypothermia under the same circumstances [45]. Given this
condition, febrile seizures are more common among children,
making body temperature a critical parameter. This measure-
ment is even more critical among for some specific epileptic
patients, as they are far more sensitive to temperature changes
and frequently trigger seizures [46]. Measuring core body tem-
perature, more reliable than peripheral temperature, requires
placing sensors in specific locations [47]. The tympanum is
one of the best areas to estimate the core temperature along
with the anus or the armpit. Nevertheless, its applicability is
far more convenient and suitable for sustained monitoring.

GSR, also known as electrodermal activity (EDA), measures
the conductance or resistance of the skin. GSA is directly
related to sweat gland activity that is regulated by sympa-
thetic and parasympathetic nervous systems [48], [49]. Arousal
of emotional, sensorial, or physiological origin modulates
the balance between these two systems and modifies skin
conductance [50]. Application for epilepsy patients include
stress-level assessment that could serve to prevent the onset of
certain types of seizures; paired with accelerometers, it is used
to detect convulsive seizures [51] and SUDEP [52]. Previous
works performed GSR measurements on multiple areas to
confirm their validity [53]. Among them, the closest one to
the desired area is the neck: placing the electrodes on the
nape on both sides of the spine. These works combined with
the population of sweat glands on both areas could allow GSR
acquisition on this area [54].

Here, we explore the feasibility of integration of these six
selected measures in the periauricular area. Several efforts
have succeeded in implementing unimodal devices providing
a unique physiological modality of recording. Others have
proposed the combination of multiple devices to increase the
number of parameters measured, but at the cost of increasing
complexity (using several recording points across the body)
and decreasing ergonomics and ease of use. Integrating all
these measurements in a single device opens the possibility
to implement a multimodal monitoring system, minimally
obstructive, and ergonomic, with the capability to gather infor-
mation that could be crucial in the diagnosis and follow-up
of patients, including the capability of providing an SUDEP
and seizure warning system, but attending to principles of
ergonomics, robustness, and reliability.

Finally, and to enable the inclusion of the monitoring plat-
form within medical health systems following the paradigms
of smart health and the Internet of Medical Things (IoMT), the
integration of communication system appears as a key factor

in the development of such multimodal monitoring system.
The proposed approach, taking advantage of wearable devices,
requires user mobility as well to provide high ergonomic lev-
els, leading to the use of wireless communication technologies.
Among these, body area network (BAN) protocols are widely
employed, due to low form factor, low energy consumption,
moderate cost, and transmission rates in the 1–2-Mbps range.
In this sense, Bluetooth is commonplace in wearable connec-
tivity, tethering either to other wearable devices such as smart
watch and smartphones or to infrastructure gateways, enabling
user interaction as well as web/cloud connectivity inherently
[63]. The integration of wireless transceivers within the sen-
sor platform is conditioned by the characteristics of radio
propagation in BAN scenarios, which can consider on-body,
off-body, and in-body communication links. These specific
communication links exhibit losses and potential degradation
due to different effects, such as body impact (in terms of
penetration losses, shadowing, and scattering), human body
dynamics, modification of antenna operational characteristics
(e.g., operation frequency, bandwidth, input impedance, and
radiation diagram), and multipath propagation components
from the surrounding environment [64]. Coverage/capacity
requirements must be fulfilled to provide adequate quality of
service metrics, in terms of bit error, rate/block error, and
rate/latency thresholds. Small-scale statistics as well as path
loss approximations have been obtained to provide assessment
in relation to operational conditions of wireless transceivers
operating in BAN configurations [63], [64].

II. MATERIALS AND METHODS

The feasibility and validity of recording the proposed
parameters on the auricular area were performed by first
recording each modality individually and finally integrating
all of them in a former multimodal recording where a proof-
of-principle multimodal system is built. Recordings were
performed by ten volunteers. Recording equipment, protocols,
and paradigms were approved by the Local Ethical Committee
of the University of Navarra (Ref: CEIC-2021.143) following
international guidelines. Inclusion criteria for recruited sub-
jects were: 1) age ranging from 20 to 40 years old; 2) no
known cardiac; or 3) no neurological disease.

A. Electroencephalography

Feasibility and validity of

recording EEG activity in
the area of
interest were performed according to three
different paradigms previously explored [55]. Two electrodes
were placed in the periauricular area (above the ear:
EarSup and below the ear: EarInf). As a gold standard,
the activity of a third electrode on the occipital region (Oz
position following the 10:20 system) was also recorded.
All
the three electrodes were referred to the earlobe and
the ground electrode was placed on the mastoid. EEG
recordings were performed by using BrainAmp EEG
amplifiers (BrainProducts, https://brainvision.com/) connected
with an STIM2 system (Compumedics Neuroscan, https://
compumedicsneuroscan.com/product/stim2-precise-stimulus-
presentation/) to deliver visual stimuli.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

BESNÉ VILLANUEVA et al.: MULTIMODAL MINIMALLY INVASIVE WEARABLE TECHNOLOGY

26623

Under the α-band modulation paradigm, volunteers were
placed in a relaxed position, wake while keeping the eyes
open for 30 s. Afterward, they closed their eyes (without
falling asleep) for another 30 s. This was repeated at least
ten several times, modulating brain’s waves, and an increase
in the brain activity on the α band (8–12 Hz) is observed.
This modulation is compared between recording areas by
performing a power spectrum density (PSD) [56], [57] for
each state and then quantifying the modulation on the α-band
and the exact frequency of the peak.

Then, we recorded visual evoked potentials (VEPs): on
a relaxed position, volunteers were stimulated visually by
means of an alternating chessboard pattern that changed every
1.1667 s (∼0.854 Hz). The alternating pattern stimulates the
visual system and elicits prototypic brain responses locked to
the stimulus that show a series of positive and negative peaks
at very specific latencies [58]. Accordingly, we determined the
feasibility of obtaining such responses on the selected area and
compared their latencies with those recorded over the occipital
area.

Finally, we evaluated the visual steady-state responses
(VSSRs) on the periauricular region. To do that, we used
the same chessboard stimulus but increasing the frequency to
8.54 Hz. Responses were obtained by performing a PSD for
each area and comparing the power and frequency of the main
response.

B. Acceleration

Acceleration measurements were performed with the
linear accelerometer ADXL345 (Analog Devices,
triaxial
During
https://www.analog.com/en/products/adxl345.html).
the recordings, the accelerometer was firmly attached to the
side of the head close to the ear and volunteers perform three
different sets of movements: postural changes (roll, pitch, and
yaw), walking, and jumping.

To minimize the potential effects of the interindividual
differences both in the orientation of the sensor and in the
dynamics of the performed activities (e.g., velocities in the
execution of the jumping phase), a rotation on the XYZ-axis
of accelerometer followed by a dynamic time warping (DTW)
[59], [60] of the signals was computed. By doing so, we were
able to align the different time series across paradigms and
subjects.

C. Cardiovascular Monitoring

For this experiment, two modalities are ECG and PPG.
In our experiments, we used a BiosignalsPlux Explorer
system from Plux Biosignals (https://plux.info/34-kits) and
an Arduino-based fully integrated system for physiological
research. We evaluated several configurations: 1) chest ECG
as gold standard (following Plux indications); 2) ear ECG;
3) PPG on the fingertip as gold standard; and 4) PPG on
the ear canal. To place the PPG sensor on the ear canal and
generate some pressure against the tissue, the PPG sensor was
embedded in a viscoelastic earplug.

From the ECG, we detected heartbeats and estimated the
the Bland–Altman [61] analysis was used to

HR. Then,

compare the HR estimated from the chest ECG with those
obtained from the ear ECG, finger PPG, and ear PPG.

Next, we explored the possibility to integrate the MAX-
30102 PPG sensor
(https://www.maximintegrated.com/en/
products/interface/sensor-interface/MAX30102.html), which
provides capabilities to provide SpO2 information. Recordings
were performed on the following locations: two gold standard
areas: fingertip and ear lobe; and two alternative areas: the
ear canal and behind the ear (over the mastoid process).

D. Body Temperature

sensor

For body temperature assessment,

the MLX90615 IR
temperature
(https://www.melexis.com/en/product/
MLX90615) and the TMP112 thermocouple (https://www.ti.
com/product/TMP112) were explored. The MLX90615 is a
low power consumption IR temperature sensor with 0.5 ◦C
of precision and 0.02 ◦C of resolution. Despite its small
dimensions, it could be problematic for our aim, as it would
obstruct completely the ear canal, preventing any aeration and
obstructing sound from reaching to the tympanum. TMP112
is a miniaturized thermocouple-based sensor (1.6 × 1.6 mm),
with low consumption, 0.5 ◦C accuracy, and 0.0625 ◦C
resolution. Complimentarily, we also explored the possibility
to use the temperature sensor integrated into the MAX30102
PPG (used to internally calibrate the IR readings of the PPG
photodiode). Nevertheless, although MAX30102 would be
the best choice in terms of potential integration, it has the
lowest precision (1 ◦C).

To assess the suitability of these sensors for future imple-
mentations, we obtained their calibration curves. To do that,
sensors were faced to a hot body and the temperature was mea-
sured as the temperature dropped gradually; a commercial IR
thermometer Thermoval Baby was used as a reference. Then,
we evaluated the capability of the sensors to follow changes
in the temperature; sensors went through three temperature
stages: 1) room temperature (around 20 ◦C) for 30 min; 2) cold
room (around 2 ◦C) for 60 min; and 3) room temperature for
another 30 min.

From these analyses, we selected the TMP102 thermocouple
and proceeded with recording on the volunteers. The TMP102
was embedded in a viscoelastic earplug and inserted in the
ear canal, and subjects were asked to move across several
rooms with different temperatures: 2 min in an office (room
temperature ∼20 ◦C), 2 min in a ∼5 ◦C refrigerated room,
1 min in a ∼−15 ◦C refrigerated room, again back for 2 min
at the ∼5 ◦C room, and finally 2 min in the office. The exact
room temperature was recorded simultaneously with another
TMP102 thermocouple.

E. Galvanic Skin Response

The equipment used for GSR validation was again the
BiosignalsPlux Explorer with the EDA (electrodermal activity,
equivalent
to GSR) sensor. To modulate their autonomic
response, volunteers were asked to watch 6-min-long recom-
pilation of short suspense videos and then asked to perform
six consecutive Valsalva maneuvers. GSR sensors are placed
between: 1) index and middle finger as gold standard and

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

26624

IEEE SENSORS JOURNAL, VOL. 23, NO. 21, 1 NOVEMBER 2023

2) the tragus and the mastoid process ipsilaterally to the
previous configuration. After visual inspection of the recorded
data, analysis on the influence of the maneuvers was deter-
mined on frequency bands: 0.1–0.2, 0.2–0.3, 0.3–0.4, and
0.4–1.0 Hz [62].

F. Proof-of-Concept Prototype

Finally, and with a selection of the most suitable com-
ponents, we proceeded with their integration in a prototype
considering factors of: 1) modularity; 2) wearability; 3) reli-
ability; and 4) ease of use. This prototype is designed as
a “proof of concept” to test the possibility of performing a
simultaneous multimodal recoding of the selected variables
together with the ability of a simple microcontroller, such as
an Arduino Nano, to manage the components and broadcast
the recorded signals through wireless technology. Although in
terms of miniaturization, placement, and degree of integration,
the microcontroller specifications were not considered key
in this stage of the development, attention was focused on
the dimensions and placement of the sensors, which were
considered critical to fulfill with the volumetric restrictions
imposed by the area of interest (they must be small enough to
fit inside or around the ear canal of volunteers).

G. Body Area Network Wireless Connectivity

Different BAN topologies have been considered, employing
Bluetooth classic and Bluetooth Low Energy (BLE) sys-
tems following the path loss methodology described in [64],
which considers the receiver position at chest or hip and
the transmitter positions at chest, back, right wrist, and left
wrist. Different transceiver operation conditions have been
considered, in terms of parameters such as use of frequency
hopping, transmission power setting, or receiver sensitivity
thresholds. Further insight is obtained by performing full-wave
electromagnetic analysis of wireless intrabody propagation
links. These results will be further discussed in the following
section.

III. RESULTS

In this section, the results of the feasibility studies for each
individual modality are exemplified by showing the data from
a representative subject. Then, a quantitative analysis, includ-
ing all ten subjects, is presented. For the proof-of-concept
prototype, an implementation example with a representative
recording is provided. Finally, wireless connectivity modeling
results for a BAN are shown.

A. Electroencephalography

Fig. 1 shows the effect of closing the eyes on the modulation
of the alpha oscillations for the Oz, EarSup, and EarInf
locations. Although the amplitude over Oz is larger than that
recorded in the ear areas, the analysis of the prominence of
the peaks confirms the existence of a significant modulation
of the amplitude (but not the frequency) of the alpha rhythm
all over the three locations (see Fig. 2).

For the VEPs, the results confirm that the maximal response
is detected at Oz; nevertheless, latencies for N75, P100, and

Fig. 1. Power spectrum of the acquired signal during the α-attenuation
study of three representative subjects. Continuous lines correspond to
the eyes-closed condition and dotted lines to the eyes-open period on
the corresponding areas: occipital, above the ear, and below the ear (left
to right).

Fig. 2.
modulation during the closed–open eyes study.

Study of prominence and frequency of the alpha rhythm

N140 are maintained across the three locations, showing no
thus demonstrating that despite the
significant differences,
lower amplitude of the responses, it is possible to obtain VEP
responses in the periauricular area (see Fig. 3).

As for the case of the VEPs, the VSSR were also detected
on the three selected recording areas. Fig. 4 shows the VSSR
together with the
response from a representative subject

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

BESNÉ VILLANUEVA et al.: MULTIMODAL MINIMALLY INVASIVE WEARABLE TECHNOLOGY

26625

Fig. 3. VEP waveforms corresponding to three representative subjects
on the corresponding areas (occipital, above the ear, and below the
ear; top panel from left to right). Average VEP for all volunteers at each
recording location (bottom panel, left) and box-plot representation of the
latencies of the N75, P100, and N140 peaks (bottom panel, right).

analysis of the amplitude and frequency of the responses for
the ten subjects. Results show that although maximal responses
is possible to record VSSR in the
are detected at Oz,
periauricular area with a good SNR for their detection and
with no deviation of the frequency (that is expected to be
8.54 Hz).

it

B. Acceleration

Fig. 5 shows a 3-D representation of the linear acceleration
recorded for all subjects. After a coordinate axis rotation
(see methods), trajectories show a good concordance between
subjects and differences between the three different move-
ments tested (postural changes, walking, and jumping). Indeed,
a simple correlation analysis (see Fig. 6) suggests the suitabil-
ity of these measures to implement a detection algorithm to
identify them. Finally, it is worth noting that the information
provided by the static acceleration also allows differentiating
between postures within the postural changes test.

C. Cardiovascular Monitoring

Fig. 7 shows ECG recordings together with the detected
heartbeats for the three different configurations investigated.
Visual inspection shows that both chest and head–shoulder
recordings show recognizable QRS complexes. In contrast,

Fig. 4. VSSR of three representative subjects at the three selected
locations together with the analyses of the prominence and frequency
of such responses for the ten volunteers involved in the study.

the recording performed on auricular area does not show
recognizable QRS complexes. This makes it difficult to detect
the heartbeat and, thus, the estimation of the HR. Indeed, the
Bland–Altman analysis of HR estimated from head–shoulder
ECG and ear ECG with respect to chest ECG demonstrates
that the head–shoulder derivation provides a far better HR
estimation of the HR (using chest ECG as gold standard) than
that obtained from the auricular area (see Fig. 8 for Bland–
Altman plot of a representative subject).

In contrast, HR values derived from PPG signals both from
finger and auricular provide good estimates of the HR. Fig. 9
shows an example of a combined chest-ECG and in-ear PPG
recording together with Bland–Altman plots that demonstrate
that the estimation of the HR from the PPG obtained in both
regions is comparable to that obtained from the chest ECG.

Fig. 10 shows an example of

the
MAX30102 PPG sensor to provide PPG information and SpO2
information from the finger and three different points of the
periauricular area. For the SpO2 data, it should be noted:

the capability of

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

26626

IEEE SENSORS JOURNAL, VOL. 23, NO. 21, 1 NOVEMBER 2023

Fig. 7. Raw ECG measured on (a) chest, (b) between the ear and the
contralateral shoulder, and (c) auricular area. The body sketches on the
left represent the location of the electrodes, the plots on the center 80-s
sample recorded on each area, and the plots on the right a 5-s sample
of the same signals.

Fig. 5. Triaxial linear acceleration measurements for the ten volunteers
under (a) postural changes, (b) walking, and (c) jumping (each color
corresponds to each of the subjects).

Fig. 8. Bland–Altman representation of the HR obtained from ECG from
(a) chest and head–shoulder and (b) chest and auricular area. Please
note the difference of scales in the two panels, as panel A scales are
[−15, 15] and [55, 100] bpm, and for panel B, they are [−1000, 900] and
[0, 1600] bpm.

contact and this causes at some points movement-related
artifacts in the SpO2 estimation.

D. Body Temperature

The comparative analysis of the three temperature sensors
showed that the performance of the thermistor integrated in the
MAX30102 PPG sensor was the lowest in terms of precision
and dynamics of the response to temperature changes. On
the other hand, and despite the good performance of the
MLX90615 IR temperature, this sensor was not considered
as it fully blocks the ear canal, thus precluding the aeration
and limiting the sound perception. As a result, we selected
the TMP112 to proceed with the validation study on the ten

Fig. 6. Correlation values obtained for all recorded activities organized
by subject and volunteer.

1) that these are noncalibrated estimates that serve to prove the
feasibility of the measurements and 2) that the dimensions of
the PCB hosting the PPG sensor difficulties the skin-sensor

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

BESNÉ VILLANUEVA et al.: MULTIMODAL MINIMALLY INVASIVE WEARABLE TECHNOLOGY

26627

Fig. 9. Top panels: simultaneous chest ECG and in-ear PPG recordings
in two representative subjects. Bottom panels: Bland–Altman analysis
for all subjects comparing the HR estimation on chest ECG against the
finger PPG and auricular area PPG.

volunteers. As shown in Fig. 11, the effect on the temperature
measured in the ear canal is barely affected by the changes in
the room temperature. In contrast, the ambient sensor shows
the effects of moving from room office to cold rooms at
−5 ◦C and −15 ◦C and back to the office. All these results
demonstrate the suitability of measuring the core temperature
in the era canal as opposed to the use of wrist-worn sensors.

E. Galvanic Skin Response

The GSR recordings in Fig. 12 illustrate the impossibility of
the selected hardware to capture the modulation of the GSR
in the periauricular region. Although it is capable to obtain
significant (and similar) GSR modulations in both hands,
no apparent modulation is observed when placing the elec-
trodes between the tragus and the mastoid. Further statistical
analysis on the four selected frequency bands ([0.1, 0.2], [0.2,
0.3], [0.3, 0.4], and [0.4, 1.0] Hz) confirms this observation,
both for the Valsalva and video watching conditions (see
Fig. 13).

F. Proof-of-Concept Prototype

The results presented above did not only serve the purpose
of validating the area for these measurements but also to
determine the suitability of the discrete electronic components

Fig. 10.
PPG recordings on all four defined areas where the blue
plot represents red LED PPG and orange IR LED PPEG. The dots
over each line represent the estimated location of a heartbeat. The
exact placement of the sensor is indicated on the picture at the left of
each graphic. Bottom panel: SpO2 estimated from PPG registers on the
corresponding PPG recordings. The different levels of each area are due
to noncalibrated estimation, and the severe artifacts on in-ear registers
are the results of an incompatible form factor of the sensor with ear
canal.

selected. At this point, we then proceeded with the design
and implementation of a “proof-of-concept” prototype aimed
at determining the feasibility of a simultaneous recording of
the selected measures through a unique microcontroller.

Fig. 14 shows this first prototype integrating: 1) TMP112
thermistor for in-ear temperature measurement; 2) TMP102
for ambient temperature measurement; 3) MLX90615 IR ther-
mometer for contactless tympanic temperature measurement;
4) MAX30102 for PPG recordings; and 5) ADXL345 for
acceleration recording. Schematics show the placement of the
different components. Both TMP102 and ADXL345 are not
placed directly on the periauricular area as the TMP102 is used
to measure ambient temperature (thus, it is placed far from
the area of recording) and the placement of the accelerometer
does not require to be exactly the periauricular area but some
convenient location on the head. All sensors include evaluation
boards compatible with Arduino microcontrollers, except the
TMP112. Therefore, a custom solution was generated to
be compatible with this initial prototype and periauricular
measurements. All sensors were controlled with an Arduino
Nano that included a Bluetooth 4.0 transceiver to wirelessly
broadcast
the signals. Power supply was implemented by
means of a 3.7-V lithium-ion battery and a TTL port for
manual event input or synchronization purposes was included.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

26628

IEEE SENSORS JOURNAL, VOL. 23, NO. 21, 1 NOVEMBER 2023

Fig. 11.
(a) Example of temperature recordings in three representative
volunteers during the temperature validation study with the TMP112
measuring the ear canal temperature (blue) and a TMP102 measur-
ing ambient temperature (orange). (b) Temperature drift study for ear
canal (blue) and ambient (orange) temperature through the different
stages of the study. (c) Table summarizing the mean and SD of the drifts
for each ambient temperature the volunteers are exposed to.

All mentioned components were attached (with Velcro or
screws) to a head harness with an adjustable fastening system
to fit with the different head sizes.

Finally,

the setup was completed with the addition of
an EEG signal recorded through a BrainVision system with
electrodes placed in the periauricular area (see above). In the
current version of the prototype, EEG data were not directly
recorded by the Arduino Nano but synchronized with the
BrainVision system by using the TTL port included. Thus,
the setup demonstrates the feasibility of implementing the
acquisition of the EEG, PPG, and core temperature from
the periauricular area, together with accelerometry and room
temperature signals simultaneously. Fig. 15 shows an example
of one recording during the α-band modulation study. The
EEG data coming from the EarSup electrode show a clear
modulation of the α rhythm when the subject was asked
to close his eyes and press the TTL marker. This marker
was recorded and presented in the BrainVision system, and
this picture has been filtered with a bandpass filter between
0.5 and 35 Hz, removing the high frequency and line noise and
accentuating the α-band modulation on the EarSup electrode.
The TTL channel shows the states of the volunteer: open (blue)
and close (green) eyes. As can be seen, there is an increment
on the activity of the EEG recording during the closed-eyes

Fig. 12.
Top panel: example of simultaneous GSR register in the
two hands of a representative subject. Bottom panel: example of
simultaneous recording of GSR in the hand (blue lines) and auricular
area (orange) of three representative subjects (baseline of each of the
recordings has been modified across subjects so recordings do not
overlap). These are continuous recording going through the different
Valsalva maneuvers.

Fig. 13. Study of the power of the signal on the selected four frequency
bands. The boxplots represent the power at the frequencies for the
stimulation with the video (blue) and the Valsalva maneuver (orange):
on the hand in the left and the auricular area on the left.

period, corresponding to ∼10 Hz. The remaining parameters
are correctly recorded: 1) the temperature shows the expected
stable parameters; 2) the red and IR PPG signals show the

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

BESNÉ VILLANUEVA et al.: MULTIMODAL MINIMALLY INVASIVE WEARABLE TECHNOLOGY

26629

Fig. 14.
Top panel: proof-of-concept prototype build around head
harness including the following sensors: TMP102 (orange), TMP112
(green), ADXL345 (yellow), MAX30102 (purple), and MLX90615 (red).
Blue indicated the remaining components for management, connec-
tion, and computing: Arduino Nano, lithium battery, Bluetooth 4.0, TTL
connector, and I2C hub. The head sketches presented represent the
placement of each component according to their color code. Bottom
panel: photograph with all sensors on a human.

waveform corresponding to each heartbeat synchronized for
both signals; and 3) the acceleration shows stable accelera-
tion measurements, despite some alterations due to subjects’
movements to accommodate on the chair.

G. Body Area Network Wireless Connectivity

In order to gain insight in relation to the feasibility of
employing BAN transceivers within the multimodal signal
platform, coverage/capacity estimations have been obtained
for Bluetooth Classic as well as for BLE. Different BAN
topologies have been considered, following the path loss
methodology described in [64], which considers the receiver
position at chest or hip and the transmitter positions at chest,
back, right wrist, and left wrist. The maximum data transmit
power has been fixed to 10 dBm for both types of transceivers,
considering that adaptive frequency hopping (AFH) is not
active or that there are less than 15 channels available (in
if
order to consider a more restrictive use case scenario;

Fig. 15. Sample of the recordings obtained from two representative
subjects with the presented proof-of-concept prototype and the BrainVi-
sion showing the four signal modalities and the TTL registers combined
on a single recording.

it has been set

AFH is active, then 20-dBm maximum transmission power
is feasible). Receiver sensitivity thresholds have been set to
−70 dBm for Bluetooth Classic and BLE 1M/2M, whereas
for the case of BLE coded (s = 2),
to
−78 dBm, and for BLE coded (s = 8), it has been set to
−85 dBm, following core Bluetooth specifications. The results
are presented in Fig. 16, and as it can be seen, received
power levels are in principle above sensitivity thresholds for
all the link types under consideration. Further tests, however,
are compulsory in order to evaluate wireless channel perfor-
mance as a function of noise floor variations (due to variable
interference conditions and considering different interference
sources, i.e., intrasystem, intersystem, and external sources)
and site-specific propagation conditions.

In order to assess the behavior of interbody/intrabody
wireless links with the operating range of BT/BLE systems
(a center operating frequency of 2.4 GHz), deterministic
full-wave simulations have been performed with the aid
of CST Microwave Studio. The human body voxel model
“Gustav” has been employed, providing accurate frequency
dispersive material characteristics. The CST Voxel Family is
composed of different human body models, from eight persons
of different gender, age, and stature. The biological data of all
tissues present in human bodies are considered, as well as
their electric properties, such as permittivity and conductivity
[65]. In Fig. 17, the “Gustav” voxel model employed for the
simulations described in this work can be seen. The numbered
points represent the proposed location of the antennas for the

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

26630

IEEE SENSORS JOURNAL, VOL. 23, NO. 21, 1 NOVEMBER 2023

Fig. 16. Estimation of received power levels in relation to relative TX-RX
positions within a body area network configuration. The values consider
the use of Bluetooth as well as BLE transceivers.

Fig. 18.
pattern of the antenna.

(a) Antenna designed for the CST simulations. (b) Radiation

considering the encapsulation of the whole device. Fig. 18
shows the designed antenna. The substrate is FR4 (dielectric
constant = 4.37) and the metallic parts are copper.

This antenna has been included as transmitter and receiver
at different points on the human body model in the simulation
scenario presented in Fig. 17. Specifically, the transmitter has
been located at the left ear, and the receivers have been located
at the right ear, on the chest, both wrists, and both ankles.
Fig. 19 presents the electric field distribution obtained by the
CST Microwave Studio simulations. The employed human
body allows obtaining propagation estimations in the air, in the
body, and on the body.

The electric field propagation results and the inclusion of the
antennas at the mentioned locations lead to the analysis of the
wireless link in terms of the S21 parameter (i.e., transmission
parameter), which represents the energy from the transmitter
received by each receiver antenna (from the transmitter). The
values of received power levels obtained for each one of the
transceiver locations are given in Table I. The results show
that received power levels in this case are lower, which is
given, on one hand, in the difference in relation to the relative
position of the transmitter–receiver pairs and, on the other
hand, on a more precise consideration of human body impact
as well as on the performance degradation of the realistic
antenna model employed.

Fig. 17. Human body model employed for body area wireless link
simulations. The numbered green dot cs the transmitter location, and
the red dots represent the receiver locations.

wireless link analysis (the green dot represents the transmitter,
emulating our sensor device, and the red ones represent the
receivers). It is worth noting that, in this case, the transceiver
location is flexible and, hence, can be located in a more
convenient
the transmitter in the periauric-
ular area), compared to the previous wireless link model
employed.

location (e.g.,

An antenna has been designed for the CST Microwave
simulation, following the criteria of operating at 2.4 GHz and
being as small as possible. Note that this antenna has been
designed and simplified for the wireless link analysis, and the
antenna integrated into the sensor device will be different after

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

BESNÉ VILLANUEVA et al.: MULTIMODAL MINIMALLY INVASIVE WEARABLE TECHNOLOGY

26631

simulation and other approaches, such as deterministic bases
modeling (e.g., geometric-stochastic models).

IV. CONCLUSION

The measurement of the purposed parameters has been
fulfilled with mixed results. On one hand, the selected setup
on the auricular area for PPG, acceleration temperature, and
EEG shows an adequate behavior for the application purpose.
The ADX345 is capable of recording distinctive acceleration
patterns corresponding to each activity tested, enabling the
quantification of their similarities, and allowing future applica-
tions of motion classification. All temperature sensors provide
adequate response to the different testing, being the TMP112
thermistor the selected sensor for both integration and val-
idation studies given its behavior, robustness, and reduced
dimensions. The drop-in temperature of 5.4 ◦C measured
during the very cold environment exposure (where the user is
exposed to 31.8 ◦C drop) shows that the area has the potential
to provide adequate temperature measurements once the sensor
placement and isolation are better approached. Nevertheless,
this deviation of the measurements can be easily avoided by
the use of protective clothing. In terms of PPG, the performed
test showed that the behavior of this measurement on the
auricular area is equivalent to its measurement on the gold
standard on the finger. The HR and PTT studies showed the
adequacy of the auricular area to acquire this signal modality.
Moreover, the MAX30102 sensor can record the signal in the
area of interest with enough quality to assess properly SpO2-
and HR-related parameters. In the case of EEG, the results
show that it is possible to detect the α-modulation during an
opened/closed eyes test as well as VEP and VSSRs. However,
the equipment used does not admit integration with the rest
of devices, and thus, a discrete device capable of similar (or
better) recordings has to be selected.

In contrast to these four parameters, both ECG and GSR are
discarded. Even with the restrictive electrode configuration,
auricular area ECG records some cardiac activity with very
low amplitude and inconsistent presence among subjects.
However, as mentioned before, the PPG recordings show high
signal quality and temporal coherence with the ECG being
a great substitute for temporal characterization. In a similar
manner, the GSR requires skin areas with enough separation
between them to create some resistance to the applied current
and active enough sweat glands during sympathetic arousal.
Fortunately, multiple studies show that, despite being related
to different physiological phenomena, both HRV and GSR can
be used to assess the same type of emotional and sympathetic
arousal. Thus, with the appropriate analysis tools, GSR can
be substituted by the PPG. Nevertheless, GSR and ECG
quality issues might be overcome with hardware modification,
searching more adequate hardware or customized devices.

For the validation of four of the parameters, a wearable
device has been developed integrating multiple temperature
sensors, acceleration, and PPG devices. The current state of
this prototype lacks a proper EEG integration to be considered
complete. Despite this limitation being solved by synchro-
nization through the TTL port, the volunteers wearing this
system reported minor inconvenience in its use and sensor

Fig. 19. CST Microwave Studio results: electric field distribution (both
through the air, in and on the human body) generated by the transmitter,
located at the left ear.

TABLE I
RECEIVER POWER LEVELS—FULL-WAVE RESULTS

As it can be seen, the interaction with the human body
as well as with the surrounding environment
results in
degradation in quality, mainly by signal power loss (given
by shadowing, diffraction, and scattering) and/or time-domain
distortion, mainly given by multipath propagation. The topol-
ogy of the human body as well as the existence of elements
such as types of clothing can also be relevant,
in terms
of changes in losses as well as in terms of reflection and
transmission coefficients given by the application of Fresnel’s
laws. In this sense, it is compulsory to perform the detailed
wireless channel analysis, in order to fully consider the impact
both on the human body as well as on the surrounding
environment, aided by tools such as full-wave electromagnetic

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

26632

IEEE SENSORS JOURNAL, VOL. 23, NO. 21, 1 NOVEMBER 2023

placement on the auricular area. This and the quality of the
recording, further validate the implementation and serve as a
basis for future more ambitious implementations miniaturizing
this device and upgrading its functionalities.

Even with the restrictiveness of the selected area for physio-
logical signal recording, here, we have shown that it is feasible
to obtain physiological data from the selected region. By doing
so, we consider that it is possible to implement a wearable
solution to determine the subject’s state in an ergonomic and
reliable way. In addition, body area network wireless connec-
tivity analyses demonstrate the feasibility and limitations in
terms of coverage/capacity conditions, as well as the detailed
impact of human body presence intrabody/interbody links.

A device built for this purpose would not only be of great
aid to epileptic patients and their relatives but would also
be capable of detecting fever, motility disturbances, and low
oxygen saturation; all of them very convenient for COVID-19
monitoring and early detection. Future work is also fore-
seen in the integration of wireless communication capabilities
with BAN protocols as well as exploring further alternatives,
such as low-power wide area network protocols, 5G NR
FR1 (below 6-GHz bands, machine-type communications),
or IEEE 802.11ah (sub-1-GHz IoT purpose specific connec-
tivity). Moreover, security considerations within wearables
must also be analyzed, playing a key role in overall user
adoption [66].

it

The proposed system envisages a platform that is scalable,
as a function of the microcontroller unit employed, as well as
on the potential limitations given in terms of form factor as
well as energy requirements. In this way and thinking on future
evolutions,
is feasible to consider multiple alternatives,
such as distributed computing nodes within the BAN, aggre-
gated/multiplexed signal processing, and/or the increase in the
unit size, which can be achieved supported by an external
element that can be connected to the periauricular area. In this
way, the system can span to tens of signals gathered. In terms
of energy consumption, there are also multiple alternatives,
also scalable in terms of energy consumption capabilities.
This includes the use of elements, such as batteries and
supercapacitors, with wireless power transfer mechanisms and
hence the possibility of easily recharging the battery unit.

In relation to the system architecture, more extensive
distributed computing schemes can be employed and are
compatible with the proposed solution described in this work.
Fog/cloud computing schemes can be indeed employed and
can be beneficial for future system upgrades, in terms of
data analysis/inference capabilities. The potential limitations
of these network architectures are mainly derived in terms of
latency, which for this specific application can have a lower
impact for nonreal-time tasks, such as those aforementioned
in relation to data analysis/processing/inference capabilities.

ACKNOWLEDGMENT

Guillermo M. Besné Villanueva, Julio Artieda González Granda, and
Miguel Valencia Ustarroz are with the Biomedical Engineering Program,
CIMA, Universidad de Navarra, 31080 Pamplona, Spain, and also with the
Instituto de Investigación Sanitaria de Navarra (IdiSNA), 31008 Pamplona,
Spain (e-mail: mvustarroz@unav.es).

Peio Lopez-Iturri, Jesús D. Trigo, and Luis Serrano-Arriezu are with the
Institute of Smart Cities, Public University of Navarre, 31006 Pamplona,
Spain, and also with the Instituto de Investigación Sanitaria de Navarra
(IdiSNA), 31008 Pamplona, Spain.

Manuel Alegre Esteban is with the Biomedical Engineering Program,
CIMA, Universidad de Navarra, 31080 Pamplona, Spain, and also with the
Clínica Universidad de Navarra (CUN), 31008 Pamplona, Spain.

Francisco Falcone is with the Institute of Smart Cities, Public University
of Navarre, 31006 Pamplona, Spain, also with the Instituto de Investigación
Sanitaria de Navarra (IdiSNA), 31008 Pamplona, Spain, and also with the
School of Engineering and Sciences, Tecnologico de Monterrey, Monterrey
64849, Mexico (e-mail: francisco.falcone@unavarra.es).

REFERENCES

[1] M. W. J. Huygens et al., “Self-monitoring of health data by patients with
a chronic disease: Does disease controllability matter?” BMC Family
Pract., vol. 18, no. 1, p. 40, Mar. 2017.

[2] M. W. J. Huygens, J. Vermeulen, I. C. S. Swinkels, R. D. Friele,
O. C. P. van Schayck, and L. P. de Witte, “Expectations and needs of
patients with a chronic disease toward self-management and eHealth for
self-management purposes,” BMC Health Services Res., vol. 16, no. 1,
p. 232, Dec. 2016.

[3] R. V. Milani, R. M. Bober, and C. J. Lavie, “The role of technology
in chronic disease care,” Prog. Cardiovascular Diseases, vol. 58, no. 6,
pp. 579–583, 2016.

[4] D. V. Gunasekeran, “Technology and chronic disease management,”

lancet. Diabetes Endocrinol., vol. 6, no. 2, p. 91, Feb. 2018.

[5] K. Lancaster et al., “The use and effects of electronic health tools for
patient self-monitoring and reporting of outcomes following medication
use: Systematic review,” J. Med. Internet Res., vol. 20, no. 12, p. e294,
2018. [Online]. Available: https//www.jmir.org/2018/12/

[6] J. M. Peake, G. Kerr, and J. P. Sullivan, “A critical review of consumer
wearables, mobile applications, and equipment for providing biofeed-
back, monitoring stress, and sleep in physically active populations,”
Frontiers Physiol., vol. 9, p. 743, Jun. 2018.

[7] M. Zhang, M. Luo, R. Nie, and Y. Zhang, “Technical attributes, health
attribute, consumer attributes and their roles in adoption intention
of healthcare wearable technology,” Int. J. Med. Informat., vol. 108,
pp. 97–109, Dec. 2017.

[8] J.-M. Tsai, M.-J. Cheng, H.-H. Tsai, S.-W. Hung, and Y.-L. Chen,
“Acceptance and resistance of telehealth: The perspective of dual-
factor concepts in technology adoption,” Int. J. Inf. Manage., vol. 49,
pp. 34–44, Dec. 2019.

[9] M. S. Rahman, “Does privacy matters when we are sick? An extended
privacy calculus model for healthcare technology adoption behavior,” in
Proc. 10th Int. Conf. Inf. Commun. Syst. (ICICS), Jun. 2019, pp. 41–46.
[10] L. Hogaboam and T. Daim, “Technology adoption potential of medical
devices: The case of wearable sensor products for pervasive care in
neurosurgery and orthopedics,” Health Policy Technol., vol. 7, no. 4,
pp. 409–419, Dec. 2018.

[11] E. Bruno, P. F. Viana, M. R. Sperling, and M. P. Richardson, “Seizure
detection at home: Do devices on the market match the needs of people
living with epilepsy and their caregivers?” Epilepsia, vol. 61, no. S1,
pp. S11–S24, Nov. 2020.

[12] T. Rukasha, S. I. Woolley, T. Kyriacou, and T. Collins, “Evaluation
of wearable electronics for epilepsy: A systematic review,” Electronics,
vol. 9, no. 6, p. 968, Jun. 2020.

[13] C. E. Stafstrom and L. Carmant, “Seizures and epilepsy: An overview
for neuroscientists,” Cold Spring Harbor Perspect. Med., vol. 5, no. 6,
pp. a022426–a022426, Jun. 2015.

[14] O. Devinsky et al., “Epilepsy,” Nature Rev. Disease Primers, vol. 4,

no. 1, pp. 1–24, May 2018.

[15] L. Lagae, J. Irwin, E. Gibson, and A. Battersby, “Caregiver impact
and health service use in high and low severity Dravet syndrome:
A multinational cohort study,” Seizure, vol. 65, pp. 72–79, Feb. 2019.
[16] J. Pimentel, “The epileptic multifactorial patient’s burden. Review of the

topic,” J. Epileptol., vol. 24, no. 2, pp. 167–172, Dec. 2016.

[17] G.-H. Kim, J. H. Byeon, S.-H. Eun, and B.-L. Eun, “Parents’ subjective
assessment of effects of antiepileptic drug discontinuation,” J. Epilepsy
Res., vol. 5, no. 1, pp. 9–12, Jun. 2015.

[18] M. Teplan, “Fundamentals of EEG measurement,” Meas. Sci. Rev.,

vol. 2, no. 2, pp. 1–10, 2002.

[19] S. Noachtar and J. Rémi, “The role of EEG in epilepsy: A critical
review,” Epilepsy Behav., vol. 15, no. 1, pp. 22–33, May 2009.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

BESNÉ VILLANUEVA et al.: MULTIMODAL MINIMALLY INVASIVE WEARABLE TECHNOLOGY

26633

[20] K. B. Mikkelsen, S. L. Kappel, D. P. Mandic, and P. Kidmose, “EEG
recorded from the ear: Characterizing the ear-EEG method,” Frontiers
Neurosci., vol. 9, pp. 1–8, Nov. 2015.

[42] C. Varon, K. Jansen, L. Lagae, L. Faes, and S. Van Huffel, “Transient
behavior of cardiorespiratory interactions towards the onset of epileptic
seizures,” Comput. Cardiol., vol. 41, pp. 917–920, Jan. 2014.

[21] A. Paul, S. R. Deiss, D. Tourtelotte, M. Kleffner, T. Zhang, and
G. Cauwenberghs, “Electrode-skin impedance characterization of in-ear
electrophysiology accounting for cerumen and electrodermal response,”
in Proc. 9th Int. IEEE/EMBS Conf. Neural Eng. (NER), Mar. 2019,
pp. 855–858.

[22] M. Eickenscheidt, P. Schäfer, Y. Baslan, C. Schwarz, and T. Stieglitz,
“Highly porous platinum electrodes for dry ear-EEG measurements,”
Sensors, vol. 20, no. 11, pp. 1–12, Jun. 2020.

[23] C. Athavipach, S. Pan-Ngum, and P. Israsena, “A wearable in-ear EEG
device for emotion monitoring,” Sensors, vol. 19, no. 18, p. 4014,
Sep. 2019.

[24] V. Goverdovsky et al., “Hearables: Multimodal physiological

in-ear

sensing,” Sci. Rep., vol. 7, no. 1, pp. 1–10, Jul. 2017.

[25] M. G. Bleichner and S. Debener, “Concealed, unobtrusive ear-centered
EEG acquisition: CEEGrids for transparent EEG,” Frontiers Hum.
Neurosci., vol. 11, p. 163, Apr. 2017.

[26] Y. Gu et al., “Comparison between scalp EEG and behind-the-ear EEG
for development of a wearable seizure detection system for patients with
focal epilepsy,” Sensors, vol. 18, no. 2, p. 29, Dec. 2017.

[27] I. C. Zibrandtsen, P. Kidmose, C. B. Christensen, and T. W. Kjaer, “Ear-
EEG detects ictal and interictal abnormalities in focal and generalized
epilepsy—A comparison with scalp EEG monitoring,” Clin. Neurophys-
iol., vol. 128, no. 12, pp. 2454–2461, Dec. 2017.

[28] S. M. Rissanen et al., “Wearable monitoring of positive and negative
myoclonus in progressive myoclonic epilepsy type 1,” Clin. Neurophys-
iol., vol. 132, no. 10, pp. 2464–2472, Oct. 2021.

[29] M. Ghamari, “A review on wearable photoplethysmography sensors and
their potential future applications in health care,” Int. J. Biosensors
Bioelectron., vol. 4, no. 4, pp. 195–202, 2018.

[30] G.-J. Horng and K.-H. Chen, “The smart fall detection mechanism
for healthcare under free-living conditions,” Wireless Pers. Commun.,
vol. 118, no. 1, pp. 715–753, Jan. 2021.

[31] J. P. Wolff, F. Grützmacher, A. Wellnitz, and C. Haubelt, “Activity
recognition using head Worn inertial sensors,” in Proc. 5th Int. Workshop
Sensor-based Activity Recognit. Interact., Sep. 2018, pp. 1–7.

[32] M. Alghatrif and J. Lindsay, “A brief review: History to under-
stand fundamentals of electrocardiography,” J. Community Hospital
Internal Med. Perspect., vol. 2, no. 1, p. 14383, Apr. 2012, doi:
10.3402/JCHIMP.V2I1.14383.

[33] K. Khunti, “Accurate interpretation of the 12-lead ECG electrode place-
ment: A systematic review,” Health Educ. J., vol. 73, no. 5, pp. 610–623,
Sep. 2014.

[34] L. Billeci, A. Tonacci, D. Marino, L. Insana, G. Vatti, and M. Varanini,
“A machine learning approach for epileptic seizure prediction and early
intervention,” in Converging Clinical and Engineering Research on
Neurorehabilitation III (Biosystems & Biorobotics), vol. 21. Cham,
Switzerland: Springer, 2019, pp. 972–976.

[35] A. van Westrhenen, T. De Cooman, R. H. C. Lazeron, S. Van Huffel,
and R. D. Thijs, “Ictal autonomic changes as a tool for seizure detection:
A systematic review,” Clin. Autonomic Res., vol. 29, no. 2, pp. 161–181,
Apr. 2019.

[36] G. Giannakakis, M. Tsiknakis, and P. Vorgia, “Focal epileptic seizures
anticipation based on patterns of heart rate variability parameters,”
Comput. Methods Programs Biomed., vol. 178, pp. 123–133, Sep. 2019.
[37] Y. Sun and N. Thakor, “Photoplethysmography revisited: From contact
to imaging,” IEEE Trans. Biomed. Eng.,

to noncontact, from point
vol. 63, no. 3, pp. 463–477, Mar. 2016.

[38] J. Allen, “Photoplethysmography and its application in clinical physi-
ological measurement,” Physiolog. Meas., vol. 28, no. 3, pp. R1–R39,
Mar. 2007.

[39] Y. Maeda, M. Sekine, and T. Tamura, “Relationship between measure-
ment site and motion artifacts in wearable reflected photoplethysmog-
raphy,” J. Med. Syst., vol. 35, no. 5, pp. 969–976, May 2010.

[40] S. Bagha, S. Hills, P. Bhubaneswar, and L. Shaw, “A real time analysis
of PPG signal for measurement of SpO2 and pulse rate,” Int. J. Comput.
Appl., vol. 36, no. 11, pp. 40–50, 2011.

[41] R. J. Thomas, J. E. Mietus, C.-K. Peng, and A. L. Goldberger,
“An electrocardiogram-based technique to assess cardiopulmonary
coupling during sleep,” Sleep, vol. 28, no. 9, pp. 1151–1161,
Sep. 2005.

[43] C. Varon et al., “Interictal cardiorespiratory variability in temporal lobe
and absence epilepsy in childhood,” Physiolog. Meas., vol. 36, no. 4,
pp. 845–856, Apr. 2015.

[44] S. Passler, N. Müller, and V. Senner, “In-ear pulse rate measurement:
A valid alternative to heart rate derived from electrocardiography?”
Sensors, vol. 19, no. 17, p. 3641, Aug. 2019.

[45] V. Bach, F. Telliez, and J. P. Libert, “The interaction between sleep and
thermoregulation in adults and neonates,” Sleep Med. Rev., vol. 6, no. 6,
pp. 481–492, Dec. 2002.

[46] A. K. Leung, K. L. Hon, and T. N. Leung, “Febrile seizures: An

overview,” Drugs Context, vol. 7, pp. 1–12, Jul. 2018.

[47] M. Sund-Levander, C. Forsberg, and L. K. Wahren, “Normal oral, rectal,
tympanic and axillary body temperature in adult men and women:
A systematic literature review,” Scandin. J. Caring Sci., vol. 16, no. 2,
pp. 122–128, Jun. 2002.

[48] R. Norman, L. Mendolicchio, and C. Mordeniz, “Galvanic skin response
& its neurological correlates,” J. Consciousness Explor. Res., vol. 7,
no. 7, pp. 553–572, 2016.

[49] R. L. Bailey, “Electrodermal activity (EDA),” in The International
Encyclopedia of Communication Research Method. Chicago, IL, USA:
Wiley, 2017, pp. 1–15.

[50] R. Martinez, A. Salazar-Ramirez, A. Arruti, E. Irigoyen, J. I. Martin,
and J. Muguerza, “A self-paced relaxation response detection sys-
tem based on galvanic skin response analysis,” IEEE Access, vol. 7,
pp. 43730–43741, 2019.

[51] M.-Z. Poh et al., “Convulsive seizure detection using a wrist-worn
electrodermal activity and accelerometry biosensor,” Epilepsia, vol. 53,
no. 5, pp. e93–e97, May 2012.

[52] R. W. Picard et al., “Wrist sensor reveals sympathetic hyperactivity and
hypoventilation before probable SUDEP,” Neurology, vol. 89, no. 6,
pp. 633–635, Aug. 2017.

[53] M. van Dooren, J. J. G.-J. de Vries, and J. H. Janssen, “Emotional
sweating across the body: Comparing 16 different skin conductance
measurement locations,” Physiol. Behav., vol. 106, no. 2, pp. 298–304,
May 2012.

[54] C. J. Smith and G. Havenith, “Body mapping of sweating patterns
in male athletes in mild exercise-induced hyperthermia,” Eur. J. Appl.
Physiol., vol. 111, no. 7, pp. 1391–1404, Jul. 2011.

[55] S. L. Kappel, M. L. Rank, H. O. Toft, M. Andersen, and P. Kidmose,
“Dry-contact electrode ear-EEG,” IEEE Trans. Biomed. Eng., vol. 66,
no. 1, pp. 150–158, Jan. 2019.

[56] P. Stoica and R. Moses, Spectral Analysis Of Signals. Upper Saddle

River, NJ, USA: Prentice-Hall, 2005.

[57] B. Porat, Digital Processing of Random Signals: Theory and Methods,

2008.

[58] D. J. Creel, “Visually evoked potentials,” Handb. Clin. Neurol., vol. 160,

pp. 501–522, Jan. 2019.

[59] M. Müller, “Dynamic time warping,” in Information Retrieval for Music

and Motion. Berlin, Germany: Springer, 2007, pp. 69–84.

[60] R. Muscillo, S. Conforto, M. Schmid, P. Caselli, and T. D’Alessio,
“Classification of motor activities through derivative dynamic time
warping applied on accelerometer data,” in Proc. 29th Annu. Int. Conf.
IEEE Eng. Med. Biol. Soc., Aug. 2007, pp. 4930–4933.

[61] N. Ö. Do˘gan, “Bland-Altman analysis: A paradigm to understand
correlation and agreement,” Turkish J. Emergency Med., vol. 18, no. 4,
pp. 139–141, Dec. 2018.

[62] R. Zangróniz, A. Martínez-Rodrigo, J. M. Pastor, M. T. López, and
A. Fernández-Caballero, “Electrodermal activity sensor for classification
of calm/distress condition,” Sensors, vol. 17, no. 10, pp. 1–14, 2017.

[63] D. B. Smith, D. Miniutti, T. A. Lamahewa, and L. W. Hanlen, “Propaga-
tion models for body-area networks: A survey and new outlook,” IEEE
Antennas Propag. Mag., vol. 55, no. 5, pp. 97–117, Oct. 2013.
[64] D. Smith, D. Miniutti, L. Hanlen, A. Zhang, D. Lewis, and D. Rodda,
Power Delay Profiles for Dynamic Narrowband Body Area Network
Channels, document 802.15-09-0187-01-0006, Mar. 2009.

[65] CST Human Body Model. Accessed: Nov. 25, 2022. [Online]. Available:
https://space.mit.edu/RADIO/CST_online/mergedProjects/3D/common_
tools/common_tools_biomodels.htm

[66] H. Amintoosi et al., “Secure and authenticated data access and shar-
ing model for smart wearable systems,” IEEE Internet Things J.,
vol. 9, no. 7, pp. 5368–5379, Apr. 2022, doi: 10.1109/JIOT.2021.
3109274.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

26634

IEEE SENSORS JOURNAL, VOL. 23, NO. 21, 1 NOVEMBER 2023

Guillermo M. Besné Villanueva received the
B.E. and M.E. degrees in biomedical engi-
neering from TECNUN, University of Navarra,
Donostia-San Sebastián, Spain,
in 2015 and
2017, respectively, and the Ph.D. degree in
biomedicine and applied medicine from the Pro-
gram of Neurosciences of CIMA, University of
Navarra, Pamplona, Spain, in 2022, under the
supervision of M. Valencia Ustarroz.

His research interests include biomedical and
healthcare device development, patient monitor-
ing, and data science applications on physiological recordings with
special interest in neuropathologies, such as epilepsy.

Julio Artieda González Granda received the
bachelor’s degree in medicine and Ph.D. degree
in medicine from the University of Navarra
(UNAV), Pamplona, Spain, in 1978 and 1979,
respectively.

He is a specialist in neurophysiology and neu-
rology. He completed his studies at the Hôpital
de Sainte Anne, Université Cochine-Port Royal,
Paris, France. He is currently an Emeritus Pro-
fessor of Neurology at UNAV. He has been
Director of the Neurology Department and Head
of the Clinical Neurophysiology Service, Clínica Universidad de Navarra,
(CUN), Pamplona; Director of the Doctoral Program in Neuroscience
and Cognition and Coordinator of the Neuroscience Area of the Center
for Applied Medical Research (CIMA) and Navarra Health Research
Institute (IdisNA), Pamplona. He is the author of more than 150 peer-
reviewed publications and 20 books. In recent years, he has been
interested in the role of brain oscillatory activity in information processing
at the brain level and its role in different neurological diseases, such as
Parkinson’s disease or psychiatric diseases such as schizophrenia.

received the bachelor’s
Peio Lopez-Iturri
degree in telecommunications engineering, the
master’s degree in communications, and the
Ph.D. degree in communication engineering
from the Public University of Navarre (UPNA),
Pamplona, Spain,
in 2011, 2012, and 2017,
respectively.

He has worked in 18 different public and
privately funded research projects.
In 2019,
he partly worked as a Researcher for Tafco
Metawireless, Ansoáin, Spain. He has over
200 contributions in indexed international journals, book chapters, and
conference contributions. He is affiliated with the Institute for Smart
Cities (ISC), UPNA. His research interests include radio propagation,
wireless sensor networks, electromagnetic dosimetry, modeling of radio
interference sources, mobile radio systems, wireless power transfer, IoT
networks and devices, 5G communication systems, and electromagnetic
compatibility (EMC)/electromagnetic interference (EMI).

Dr. Lopez-Iturri was a recipient of the ECSA 2014 Best Paper Award,
the IISA 2015 Best Paper Award, the ISSI 2019 Best Paper Award, and
the EAI Industrial IoT 2020 Best Paper Award. He received the 2018
Best Spanish Ph.D. Thesis in Smart Cities in CAEPIA 2018 (3rd prize),
sponsored by the Spanish network on research for Smart Cities CI-RTI
and Sensors.

Jesús D. Trigo was born in Zaragoza,
Spain, in 1981. He received the M.S. degree
in telecommunication engineering and the
Ph.D. (Hons.) degree from the University of
Zaragoza, Zaragoza, Spain, in 2005 and 2011,
respectively.

He is currently an Assistant Professor with the
Department of Electrical, Electronic and Com-
munications Engineering, Public University of
Navarre, Pamplona, Spain. He has undergone
research stages at the Biomedical Informatics
Laboratory, Foundation for Research and Technology-Hellas, Heraklion,
Crete, Greece, and the Institute of Medical Biometry and Informat-
ics, Heidelberg University, Heidelberg, Germany. He is the author of
17 articles, five book chapters, and over 50 publications in national and
international conference proceedings. He has participated in over ten
research projects with both public and private funding and has advised
one Ph.D. thesis. His research interests include eHealth applications
and architectures, biomedical informatics or medical device interoper-
ability, and standardization among others.

Manuel Alegre Esteban received the bachelor’s
and Ph.D. degrees in medicine and surgery from
the University of Navarra, Pamplona, Spain, in
1994 and 2002, respectively.

He is a Specialist in Neurology and Clinical
Neurophysiology and currently heads the Neuro-
physiology Service of the Clínica Universidad de
Navarra, Pamplona. His main field of research
interest is brain oscillatory activity in relation to
physiological motor control and its alterations
(movement disorders). His other fields of interest
are the physiology of the auditory pathway and the relationship between
oscillatory activity and cognition.

Dr. Alegre Esteban has received several awards, including the Extraor-
dinary Degree Award in 1994 and the Extraordinary Doctorate Award in
2002. He belongs to the Spanish Society of Neurophysiology, Spanish
Society of Neurology, Movement Disorders Society, and Society for Neu-
roscience. He has been member of the Editorial Committee of Clinical
Neurophysiology and Editorial Assistant of Movement Disorders.

Luis Serrano-Arriezu (Senior Member, IEEE)
was born in Andosilla, Spain,
in 1966. He
received the M.Sc. degree in physics from
the University of Zaragoza, Zaragoza, Spain,
in 1989, and the Ph.D. degree in electrical engi-
neering from the Public University of Navarra,
Pamplona, Spain, in 1995.

He has been involved in the design and manu-
facture of medical devices for vital sign measure-
ments (BP, SpO2, optical, and bioelectronics),
the development of interoperability standards for
medical devices, strategies for the deployment of new ICT-based elec-
tronic health services, the Internet of Medical Things (IoMT), startup
entrepreneurship, as well as the elaboration of study plans (bachelor,
master, and Ph.D.) in this field. During this time, he has published
more than 90 articles in indexed international
journals as well as in
national and international congresses, several book chapters, as well
as the publication of a national patent. He has also managed numerous
research projects, collaborative projects, and technology transfer with
private companies, as well as innovation and development contracts and
six doctoral theses.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply. 

BESNÉ VILLANUEVA et al.: MULTIMODAL MINIMALLY INVASIVE WEARABLE TECHNOLOGY

26635

Francisco Falcone (Senior Member,
IEEE)
received the degree in telecommunication engi-
neering and the Ph.D. degree in communica-
tion engineering from the Public University of
Navarre (UPNA), Pamplona, Spain, in 1999 and
2005, respectively.

From 1999 to 2000, he was a Microwave
Network Engineer at Siemens-Italtel, Málaga,
Spain. From 2000 to 2008, he was a Mobile
Access Network Engineer at Telefónica Móviles,
In 2009, he co-founded Tafco
Pamplona.
Metawireless, a spin-off of UPNA (with EIBT national label), of which
he was its first manager. In parallel, from 2003 to 2009, he was an
Assistant Lecturer with the Department of Electrical and Electronic Engi-
neering, UPNA, where he became an Associate Professor in June 2009.
From 2011 to 2012, he was a Secretary at the Department of Electrical,
Electronic and Communication Engineering, UPNA, where he was the
Head of the Department of Electrical, Electronic and Communication
Engineering from January 2012 to July 2018 and from July 2019 to
November 2021. In 2018, he was a Visiting Professor at the Kuwait Col-
lege of Science and Technology, Doha, Kuwait, for three months. He has
also been with the Smart Cities Institute, Public University of Navarra,
a multidisciplinary research institute with over 100 researchers, being
the Head of the Institute, since May 2021, working on contextual and
interactive environments solutions, through the integration of heteroge-
neous wireless communications networks, based on HetNet and the IoT.
Since June 2022, he has been a Distinguished Visiting Professor with
the Telecommunications School of Engineering and Science, Tecno-
logico de Monterrey, Monterrey, Mexico. Since September 2022, he has
also been a Full Professor with the Department of Electrical, Electronic
and Communication Engineering, UPNA. He has over 600 contributions
in indexed international journals, book chapters, and conference contri-
butions. His research interests include computational electromagnetics
applied to the analysis of complex electromagnetic scenarios, with a
focus on the analysis, design, and implementation of heterogeneous
wireless networks to enable context-aware environments.

Dr. Falcone received several research awards, such as the CST Best
Paper Award in 2003 and 2005, the Prize of the Official Association of
Telecommunications Engineers for the Best Doctoral Thesis in 2005, the
UPNA Ph.D. Award in Experimental Sciences from 2004 to 2006, the 1st
Prize Juan López de Peñalver to the Best Young Researcher in 2010,
the Real Academia de Ingeniería de España, the XII Talgo Foundation
Award for Technological Innovation with the proposal “Implementation
of an Environment for the Railway Ecosystem,” the ECSA-2 Best Paper
Award in 2015, the Best Paper Award IISA in 2015, the ECSA Award-3
Best Paper Award in 2016, the ECSA-4 Best Paper Award in 2018, the
Best Paper Award ISSI in 2019, and the IIoT 2020 Best Paper Award.

Miguel Valencia Ustarroz received the B.E.
degree in telecommunications engineering from
the Public University of Navarra (UPNA),
Pamplona, Spain, in 2001, followed by an expert
in biomedical engineering, and the Ph.D. degree
in applied physics and mathematics from UPNA
in 2006.

From 2003 to 2006, he participated in the
establishment of the Laboratory of Clinic Neuro-
physiology, Center for Applied Medical Research
(CIMA), during his Ph.D. From 2007 to 2009,
he worked with CNRS on the LENA Laboratory located at the Pitié-
Salpêtrière Hospital, Paris, France. Afterward, he was reincorporated
on CIMA as a Junior Researcher and now leads the Physiological
Monitoring and Control Laboratory, CIMA. He is the author of over
50 publications, two book chapters, and 120 scientific communications.
Dr. Valencia Ustarroz is a member of the Spanish Society for Neuro-

science and the Spanish Society of Biomedical Engineering.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:12:19 UTC from IEEE Xplore.  Restrictions apply.
