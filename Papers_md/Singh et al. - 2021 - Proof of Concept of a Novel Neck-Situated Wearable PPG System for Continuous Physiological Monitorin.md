# Singh et al. - 2021 - Proof of Concept of a Novel Neck-Situated Wearable PPG System for Continuous Physiological Monitorin

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 70, 2021

9509609

Proof of Concept of a Novel Neck-Situated
Wearable PPG System for Continuous
Physiological Monitoring

Sukhpreet Singh , Michał Kozłowski

, Irene García-López , Student Member, IEEE, Zhou Jiang ,

and Esther Rodriguez-Villegas

, Senior Member, IEEE

overnight

Abstract— Continuous

signs monitoring
vital
for patients suffering from epilepsy, where
would be ideal
life-threatening hypoxemias can occur during sleep. However,
the existing physiological monitoring systems suffer from limita-
tions in terms of usability factors and/or limited information of
the signals being acquired. The body location of the monitoring
system is a crucial consideration, seldom addressed by the wider
community. This article presents a proof-of-concept, neck-worn
photoplethysmography system, which was developed and tested to
assess the feasibility of the neck as a monitoring site for longitudi-
nal sensing of cardiac and respiratory responses during sleep. The
novel system was compared against a gold-standard commercial
multichannel cardiorespiratory polysomnography (PSG) system
during oxygen desaturation cycles, to assess its ability to measure
heart rate, respiratory rate (RR), and peripheral blood oxygen
saturation (SpO2) on 15 participants. The ﬁndings for heart rate
showed a marginal mean error of 0.47 beats/min with limits of
agreement (LOA) at 95% conﬁdence between −3.17 and 4 bpm.
RR comparisons had an overall mean error of 0.43 breaths/min,
with LOA at 95% conﬁdence between −2.73 and 3.3 bpm.
Lastly, the system accurately outputs SpO2 with an overall root-
mean-square error of 1.44% between 90 and 100% SpO2 using
a custom calibration method. Moreover, it was observed that
the neck made it possible for the system to detect desaturation
events on an average 12.6 s prior to the PSG system, which used
a peripheral ﬁnger-based PPG system. Ultimately, this proof-
of-concept study illustrates the viability of neck-based sensing for
minimally invasive monitoring of cardiac and respiratory vitals
during sleep.

Index Terms— Biomedical monitoring, epilepsy, photoplethys-

mography (PPG), pulse oximetry, wearable sensors.

I. INTRODUCTION

E PILEPSY is a neurological condition affecting the central

nervous system, resulting in bursts of electrical activity in
the brain, resulting in seizures with a variety of physical and/or
cognitive manifestations [1]. The disease affects more than
500 000 people in the U.K. and 50 million worldwide [2]. It is

Manuscript received February 19, 2021; revised April 11, 2021; accepted
April 26, 2021. Date of publication May 26, 2021; date of current version
June 10, 2021. This work was supported by the European Research Coun-
cil (ERC) under Grant 724334. The Associate Editor coordinating the review
process was Dr. Subhas Chandra Mukhopadhyay. (Corresponding author:
Sukhpreet Singh.)

The authors are with the Wearable Technologies Laboratory, Department
of Electrical and Electronic Engineering, Imperial College London, London
SW7 2BT, U.K. (e-mail: ss7719@ic.ac.uk).

Digital Object Identiﬁer 10.1109/TIM.2021.3083415

unclear, in most cases, as to what causes epilepsy—possible
causes include a stroke, severe head injury, or drug abuse [1].
Epileptic events during sleep, or nocturnal seizures, can
lead to hypoxemic events and potentially be accompanied
by central apneas in the ictal phase [3], [4]. This results in
nocturnal seizures having an increased risk of mortality caused
by sudden unexpected death in epilepsy (SUDEP) [5]–[7].
Although the exact mechanisms of SUDEP are uncertain,
cardiac and respiratory impairment and ictal phase hypoxemic
events have shown to be potentially relevant factors [3],
[8]–[10]. The risk of SUDEP affects people of all ages [11].
Hence, having easy-to-use, unobtrusive systems that allows for
long-term monitoring of epilepsy patients during sleep could
potentially help to reduce the risk of SUDEP.

Currently, the gold standard for epilepsy patient monitor-
ing involves a video-based electroencephalogram (EEG) or
multichannel cardiorespiratory polygraphy/polysomnography
(PSG) for epilepsy [12], [13]. A variety of physiological
channels are sensed, which might include electroencephalog-
raphy (EEG), photoplethysmography (PPG), electrocardiogra-
phy (ECG), electromyography (EMG), and respiratory effort.
Despite PSG and video-based EEG systems showing their
versatility in overnight diagnostic studies and/or in-clinic long-
term monitoring, these systems are designed with supervised
clinical use in mind. Thus,
ideal for long-
term, ideally unsupervised, monitoring of the cardiorespiratory
function of the patient [12], [13]. The potential wearable
technologies could offer in this context is hence becoming
increasingly apparent [14]–[18].

they are not

Over the last few decades, the increased commercialization
of PPG-based wearable devices has been evident, garnering
considerable market share and press coverage. The devices
for pervasive health and ﬁtness monitoring, such as the Fitbit
(Fitbit Inc., California, USA) or the Apple watch (Apple Inc.,
California, USA), make use of PPG as one of their main
physiological sensors due to its noninvasive nature, simplicity,
and small form factor [19].

Despite offering a high degree of convenience and usability
compared to conventional clinical health monitors, these sys-
tems are not regulated as medical devices for physiological
monitoring purposes. This is unlikely to change in the future,
due to, among other reasons, the limitations associated with
the signal acquisition in the chosen body location [20], [21].

This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

9509609

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 70, 2021

Many anatomical positions have been suggested for PPG,
the beneﬁt of each of them being ultimately dependent on
the intended purpose of the device. The neck, however, has
conventionally not been chosen as a potential location for
PPG sensing since other positions in the body are anatom-
ically more suitable. However, those conventional locations
are unsuitable to sense airﬂow, which in the context of high-
risk intended uses is important to identify full central apneas.
The neck offers the possibility of potentially monitoring both
oxygen saturation levels and airﬂow [22].

Previous work using neck-based PPG has been very
limited, only demonstrating the feasibility of extracting
signals [23]–[25], characterizing the waveform [26], and
analyzing potential artifacts and exploring the optimal loca-
tion [24], [27]. This article advances the state of the art by
presenting for the ﬁrst time a proof of concept of a wearable
system for PPG signal acquisition,
together with analysis
algorithms for extraction of heart rate (HR), respiratory rate
(RR), and peripheral oxygen saturation (SpO2).

II. METHODS

A. Hardware

A custom PCB was designed to house an integrated PPG
sensor (MAX30102, MAXIM integrated), which emits red
(650–670 nm) and IR (870–900 nm) light, paired with a
photodiode to quantify light absorption. The MAX 30102 was
chosen due to its low-power capabilities; operating at 1.8 V
and 3.3 V for the LEDs [28]. Furthermore, the small form
factor (5.6 mm × 3.3 mm × 1.5 mm), programmable parame-
ters, and built-in ambient light rejection make it practical for
wearable applications [28]. A three-axis linear accelerometer
(LIS2DH12, ST Electronics) was included to evaluate the
activity and remove motion artifacts as necessary. The chosen
accelerometer (LISDH12) speciﬁcally is ideal for wearable
applications due to its low-power modes, high precision, and
small form factor [29]. An NRF5232 microcontroller (Nordic
Semiconductor) was used to acquire sensor data via a two-wire
interface (TWI). The microcontroller is based on a 64-MHz
Arm Cortex-M4 CPU, with 512-kb and 64-kb storage for
ﬂash and RAM, respectively [30]. Furthermore, this micro-
controller supports the Bluetooth low energy (BLE) protocol
for controlling wireless sensor data transmission. Data from
the NWPPGS were transmitted wirelessly using a 2.4-GHz
mini-antenna (2450AT18b100, Johanson Technology, Inc.).
A custom rechargeable 80 mAh, 3.8-V lithium ion polymer
battery supplied power to the system, and was chosen for its
capacity and small form factor (20 mm × 16 mm × 4 mm).
Voltage regulators were used to tune the voltage for each mod-
ule to match the datasheet requirements (3.3 V for the micro-
controller, accelerometer, and PPG sensor LED, and 1.8 V for
the PPG sensor integrated circuit). Furthermore, power man-
agement circuitry was included to allow the battery to charge
via a micro-USB cable. The custom PCB was housed in an
additive manufactured enclosure to interface the sensor system
with the suprasternal notch. In order to maximize the surface
contact area between the complete Neck Worn PPG System
(NWPPGS) and the suprasternal notch, a slight protruding

Fig. 1.
(a) A study participant equipped with the SOMNOScreen PSG
(respiratory bands and a ﬁnger PPG sensor) and the NWPPGS. (b) IR
camera image showing the venous system near the suprasternal notch. The
darker regions indicated by the red arrows show veins in the neck region.
(c) NWPPGS system is equipped on a test subject using a double-sided
adhesive.

feature was implemented in the bottom of the enclosure.
A 0.2-mm acrylic screen was placed above the PPG sensor
to fully enclose the inside circuitry. The overall dimensions
of the physical enclosure were 28 mm × 28 mm × 10 mm.
To allow for a more consistent pressure distribution across
participants, a double-sided adhesive was used to bond the
NWPPGS to the user.

B. Experimental Setup

Collecting PPG data with the NWPPGS was approved by
an institutional review board: Local Ethics Committee of
Imperial College London (ICREC ref.: 18IC4358). The study
involved 15 healthy participants (ten male and ﬁve female),
with an average age of 27 ± 2 years, an average body mass
index (BMI) of 23.80 ± 3.57 kg/m2, and a variety of skin
colors. Recordings were captured with participants lying down
in a dark room to mimic sleeping environments. This was car-
ried out to simulate the device’s aim of being utilized in bed at
night. An IR camera was used to identify venous presence near
the suprasternal notch, as shown in Fig. 1(b). If a heavy venous
presence near the suprasternal notch was evident, the PPG
sensor would be repositioned nearby to avoid venous architec-
ture. Fig. 1(c) shows the NWPPGS applied to the suprasternal
notch using a double-sided adhesive. Relevant channels of a
portable PSG (SOMNOScreen and SOMNOmedics) system
were used as a reference gold standard, namely transmission
ﬁnger-based oximeter and thorax and abdomen respiratory
bands. The complete setup of sensing devices can be seen
in Fig. 1(a).

Raw data from the NWPPGS were sampled at 75 Hz.
The SOMNOScreen system displayed HR and SpO2 using
four-beat averages. Data from the NWPPGS were transmitted
via Bluetooth 5 to an in-house developed iOS app, with the
minimum and maximum connection intervals between the
NWPPGS and the tablet to be 20 and 40 ms, respectively.
Lastly, data from the tablet were uploaded to a cloud-based

SINGH et al.: PROOF OF CONCEPT OF NOVEL NECK-SITUATED WEARABLE PPG SYSTEM

9509609

Fig. 2. Block diagram outlining the internal structure of the NWPPGS. Data
are then transmitted from the NWPPGS to a tablet via BLE at 75 Hz, and
then to a cloud-based repository for data analysis.

repository for analysis, as shown in Fig. 2. Manual markers
were inputted on the SOMNOScreen and tablet for synchro-
nization at the start of each experiment. Participants were
ﬁrst asked to breathe normally for 2 min, then wear a com-
mercial respiratory modulating device designed to simulate
high altitude (Ultrabreathe [31]) for 30–180 s. The respiratory
modulating device safely limited air intake to allow for a
controlled SpO2 decrease. Each test involved four desaturation
intervals, and two tests were taken from each user, resulting in
eight total desaturation events. Manual markers were recorded
on the tablet to indicate the start and end of every desaturation
event to determine the delay in SpO2 readings observed from
both sensing modalities.

C. Signal Processing

The overall aim of the work was to quantify the feasibility to
extract HR, RR, and SpO2 from neck PPG signals, comparing
their accuracy with respect to the same ground-truth parame-
ters. The PPG signals acquired with the wearable system were
processed as shown in Fig. 3. This is further described in
subsequent sections.

1) Preprocessing: Data acquired from the SOMNOScreen
and the NWPPGS were synchronized in time to ensure com-
plete correspondence between samples. This was carried out
automatically using cross-correlation between the acceleration
reported from the NWPPGS accelerometer and chest band
data. This synchronization was validated by conﬁrming the
time difference between the manual marker input between the
SOMNOScreen and NWPPGS empirically. All data were sub-
sequently downsampled to 15 Hz before undergoing analysis.
Outlier data were removed by computing the magnitude of the
accelerometer signal. The signal was separated into “usable”
periods of relatively noise-free data and noisy time spans.
After normalizing the amplitude of x-, y-, and z-directions,
the magnitude of the acceleration was computed. Data seg-
ments were removed if the magnitude was larger than two
standard deviations from the mean. This is exempliﬁed in
Fig. 4—the black and red periods of the data are the “usable”
and “noisy” segments, after masking the data using accelerom-
eter data, respectively. The binary mask was smoothed to
produce homogeneous, nondiscontinuous data for analysis.

Flow diagram illustrating the signal processing methodology
Fig. 3.
undergone by both the red and IR PPG signals. The data underwent spline
interpolation to downsample the data to 15 Hz, and then next to an outlier
detection/removal stage. Lastly, distinct signal processing pipelines were
applied depending on whether RR, HR, or SpO2 were computed.

Fig. 4.
Example of data showing interference with motion artifacts.
Normalized accelerometer signal (above) and red LED signal (below). Black
lines illustrate y periods of the interference caused by the movement of
artifacts as determined by the masking step.

are difﬁcult to fully interpret in this signal due to the large
inﬂuence of respiratory-induced signal modulations during
breathing. To this end, unique ﬁltering techniques were used
depending on whether a respiratory or a cardiac marker was
being investigated.

Fig. 5 shows raw signals for both the red and IR lights
in the NWPPGS. Cardiac components of the PPG signals

2) RR Processing: To analyze the respiratory components
of the signal, a fourth-order Chebyshev ﬁlter was applied

9509609

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 70, 2021

Fig. 5. Example displaying the ac components of the PPG signals acquired
from the NWPPGS, including the larger respiratory waveforms, with the
smaller cardiac pulses embedded in the respiratory component of the signal
for both the red LED (blue) and IR LED (orange).

in order to isolate frequen-
across the raw PPG signals,
cies in the respiratory band (0.1–0.5 Hz, 6–30 breaths/min).
A third-order Savitzky–Golay ﬁlter was then used to smooth
the signal of any sharp/transient signal artifacts which were
in the signal after bandpass ﬁltering. The
still evident
SOMNOScreen system quantiﬁed respiratory effort, as the
thorax and abdomen contracted during breathing; how-
ever, RR was not provided by the SOMNOScreen system.
Fig. 6 shows the sum of the thoracic and abdominal signal
obtained from the SOMNOScreen, superimposed on the raw
red light PPG signal [Fig. 6(a)], and the ﬁltered respiratory
component of the signal [Fig. 6(b)]. Therefore, to determine
the RR, dominant frequencies of each signal were tracked
using the built-in MATLAB function tfridge(). This outputted
the largest energy ridge in the time-frequency spectrum, and
thus isolated the dominant frequency over time. This RR algo-
rithm was applied to both sensing modalities for comparison.
The total amount of respirations/breaths taken by each subject
was tallied to verify the ability of the NWPPGS to identify
respiration cycles to that of the SOMNOScreen respiratory
bands. This was carried out using the MATLAB function
ﬁndpeaks() with thresholding.

3) HR Processing: To remove any bias caused by respira-
tion and to isolate the cardiac band, a fourth-order Chebyshev
ﬁlter (0.5–3 Hz) was applied across the signal. A frequency
tracking-based HR algorithm was used for its low com-
putational complexity. This method estimated HR using an
oscillator-based adaptive notch ﬁlter algorithm which tracked
the dominant frequencies of the signal [32], [33].

4) Blood Oxygen Saturation Processing: As shown in
Fig. 3, to derive the SpO2 signal, the ac and dc components of
the signal needed to be isolated reliably ﬁrst. A bandstop was
applied between 0.1 and 0.5 Hz for both the red and IR PPG
signals to remove the respiratory component. Next, the signal
was processed through a third-order Savitzky–Golay ﬁlter to
construct the dc signal.

The ac component of the signal was determined by ﬁrst
localizing the peaks and valleys of the signal using the
ﬁndpeaks() MATLAB function. Due to the possibility of false
identiﬁcation of nearby peaks, a peak correction step was

Fig. 6.
(a) Unﬁltered red LED PPG signal from the NWPPGS (blue) and
the respiratory output from the SOMNOScreen respiratory bands (orange).
Both signals are synchronized in time. (b) Filtered red LED PPG signal
to isolate the respiratory component of the signal (blue) and the respiratory
output calculated from the SOMNOScreen system (orange).

introduced by creating a sample window at the calculated
peak equal
to half the sampling frequency. This ensured
that the chosen peak was the maximum and the valley was
the minimum. In order to match the SOMNOScreen system,
a four-beat average window was implemented to calculate the
SpO2.

Calibration of the system was carried out

in line with
the PPG sensor manufacturer’s calibration guidelines [34].
Further analytical steps were required, since only a subset
of subjects experienced a desaturation event greater than 5%.
to apply equal weights to all SpO2(%) levels,
Therefore,
a k-nearest neighbor (knn) search algorithm was used. The
algorithm chose the k closest points to the mean of each
SpO2 percentage, to balance the number of observations. The
common number of neighbors used for all percentages was
equal to the number of samples received for the lowest SpO2
level of 90%. Fig. 7 shows a scatter plot displaying the formed
linear regression of the reference SpO2 values against the
corresponding processed R ratios for all subjects.

The observations falling within one standard deviation
(Robs ∈ μ ± σ ) are displayed in blue and the knn surrounding
the mean in yellow. A linear model was ﬁt to the data by
least-squares approximation, i.e., by minimizing the squared
distance between each observation and the regression line. The
resulting linear function for SpO2

= 107.07 − 9.42R.

(1)

SpO2
This provided the

neck

calibration coefﬁcients of
A = 107.07 (intercept of the regression line) and B = 9.42
(slope of the regression line). The coefﬁcient of determination
(r 2) demonstrated that
the proposed model signiﬁcantly
( p < 0.001) explained 90% of the SpO2 variance.

A. Evaluation Criteria

III. RESULTS

The Bland–Altman and scatter plots were used to assess
the agreement between the NWPPGS and SOMNOScreen for

SINGH et al.: PROOF OF CONCEPT OF NOVEL NECK-SITUATED WEARABLE PPG SYSTEM

9509609

Fig. 7. Custom regression curve to determine SpO2 from the NWPPGS.
The blue dots represent the R calculated values for each SpO2 level with a
set of transparency factors; therefore, regions with increased density of points
appear in dark blue. The yellow dots represent the knn closest points which
were used to inﬂuence the linear regression curve, and thus the equation.

HR, RR, and SpO2. Root-mean-square error (RMSE) was
calculated to quantify the absolute prediction error of RR, HR,
and SpO2 for each test subject j , given by

RMSE j =

(cid:2)

(cid:3)

N
i=1

(yi − ˆyi )2
N

(2)

where (yi −ybi )2 corresponds to the residuals and N represents
the total number of samples. The overall RMSE (ORMSE) was
then obtained by averaging individual RMSE j for all subjects
based on the sample size for each subject.

B. Respiratory Rate

the study,

Fig. 8(a) shows a sample RR response for both the
SOMNOScreen and NWPPGS. Due to the stable conditions
the range of RRs examined was between
of
10 and 18 breaths/min (bpm). The calculated ORMSE of RR
was 1.72 bpm when comparing the NWPPGS system and the
SOMNOScreen. Fig. 8(b) shows the Bland–Altman and
scatter plots for RR between the NWPPGS system and
SOMNOScreen. The value of μ was quantiﬁed by computing
the average of all HR discrepancies. The limits of agree-
ment (LOA) at a 95% conﬁdence showed a mean error of
±1.96 × σ . A mean bias of 0.43 bpm was obtained in the
Bland–Altman plot shown in Fig. 8, with the upper and lower
LOA being 3.3 and −2.7 bpm, respectively. A positive sloping
bias was observed in the Bland–Altman plot, indicating that
higher calculated RRs for the NWPPGS were overestimated,
and lower calculated RRs were underestimated. The coefﬁcient
of determination (r 2) for RR demonstrated that the proposed
model signiﬁcantly explained 68% of the RR variance between
SOMNOScreen and NWPPGS. The average cumulative respi-
ration count per user was estimated as 177.2 respirations with
a standard deviation of 48.9 respirations and 181.6 respira-
tions with a standard deviation of 49.4 respirations for the
PPG and SOMNOScreen system, respectively. The NWPPGS
recorded 97.6% of the total respirations recorded by the
SOMNOScreen.

C. Heart Rate

Fig. 9(a) shows a similar HR response between both
systems. The experimental HR range was between 43 and

Fig. 8.
(a) Calculated RRs from both the NWPPGS (blue) and the
SOMNOScreen (orange), both synchronized in time. (b) Linear regres-
sion (left) and Bland–Altman plot (right) showing the comparison between
RRs automatically extracted from the NWPPGS and the reference test,
SOMNOScreen. LOA of the Bland–Altman plot at 95% conﬁdence were
3.3 and −2.4 bpm for the upper and lower bound, respectively.

96 beats/min (bpm). Fig. 9(b) shows a scatter plot and a
Bland–Altman plot used to compare the measured HR of
the NWPPGS method with the ground-truth SOMNOScreen.
A mean bias of 0.47 bpm was obtained, with the upper and
lower LOA bounds being 4 and −3.1 bpm, respectively, at a
95% conﬁdence interval. The bias line shows that the error
is consistent between the HR levels, and is not adversely
affected by varying bpm levels. The scatter plot between both
modalities showed a high degree of agreement, with r 2 of 95%.
Finally, the NWPPGS yielded an ORMSE of 1.69 bpm.

D. Blood Oxygen Saturation

Once the PPG device was calibrated, the ability of this
device to estimate SpO2 could be evaluated. A leave-one-
subject-out cross-validation (LOSO-CV) strategy assessed the
performance of the proposed linear model. For that, one test
subject was removed from the whole set iteratively to repeat
the linear regression ﬁtting with the rest of the subject’s data.
The calculated R values of the test subjects were then inputted
in the calibrated model to derive the corresponding SpO2
levels. The RMSE and ORMSE were additionally calculated
to quantify the prediction error.

The LOSO-CV method conﬁrmed the estimation of SpO2
values, with a very low absolute error of ORMSE = 1.44%.
Generic coefﬁcients given by the PPG sensor manufacturer
resulted in an ORMSE = 12.54%, which is much larger

9509609

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 70, 2021

Fig. 9.
(a) Sample HR response from both the NWPPGS (blue) and
SOMNOScreen (orange), both synchronized in time. (b) Linear regression
(left) and Bland–Altman plot (right) used to compare HR from the NWPPGS
and SOMNOScreen. LOA of the Bland–Altman plot were 3.3 and −4.6 bpm
for the upper and lower bounds, respectively, with a 95% conﬁdence interval.

than the obtained 1.44%, showing the need for custom cal-
ibration. Fig. 10(a) shows desaturation events occurring with
the SpO2 response of both systems synchronized. Clearly,
the NWPPGS responded appropriately to desaturation events.
Fig. 10(b) shows the Bland–Altman plot comparing the SpO2
calculated by the NWPPGS and the ground-truth SpO2 from
the SOMNOScreen system. The mean bias of 0.92% was
observed, with LOA of 3.3% and −2.4% for the lower and
higher bounds, respectively, at a 95% conﬁdence interval.
A negatively trending slope was evident, as the error margins
increased for lower SpO2 levels. It was understood that lower
SpO2 levels slightly overestimated SpO2 values. However,
the NWPPGS system produced very promising results for
resting-state SpO2 levels. Lower SpO2 had a far smaller
density of data points compared to higher SpO2 levels, as can
be seen in Fig. 7.

The BMI and age of each subject were tabulated along with
the RMSE for each test in Table I. No signiﬁcant correlation
was found between BMI of subjects and RMSE.

Lastly, the time lag between the SpO2 outputs with respect
to the manually marked start of events was also compared, for
both the NWPPGS method and the SOMNOScreen ground
truth. Fig. 11 shows the outline of the overall time delay
associated with both the NWPPGS and SOMNOScreen ability
to respond to desaturation events. The mean delay was 15.01
and 27.29 s, with standard deviations of 3.31 and 6.13 s for the
NWPPGS and SOMNOScreen system, respectively. Hence,
it was found that the NWPPGS responded to desaturation

Fig. 10.
(a) SpO2 output from the NWPPGS (blue) and SOMNOScreen
(red). (b) Bland–Altman plot (right) used to compare SpO2 with the NWPPGS
and SOMNOScreen. LOA of the Bland–Altman plot were 3.3% and −1.4%
for the upper and lower bounds, respectively, at a 95% conﬁdence interval.
A negative bias is visually noticeable in the plot with overestimated values at
lower SpO2 levels.

Fig. 11. Boxplots explaining the mean time for each sensing modality to
respond to a desaturation event per user. The error bars correspond to the
standard deviation.

changes on an average of 12.28 s prior to the ground-truth
SOMNOScreen system.

IV. DISCUSSION

This article demonstrates for the ﬁrst time that it is pos-
sible to extract SpO2 values from a neck-based wearable

SINGH et al.: PROOF OF CONCEPT OF NOVEL NECK-SITUATED WEARABLE PPG SYSTEM

9509609

TABLE I
SpO2 RMSE, AGE, AND BMI FOR EACH USER ACROSS BOTH TESTS

device with accuracies that could match acceptable regulatory
margins [35], while also having the possibility of obtain-
ing respiratory and heart rates from only the sensed PPG
signal. Furthermore, it was demonstrated that desaturations
manifested on the signal acquired with the novel wearable
system from the neck were 12.6 s faster, on average, than
when sensing the PPG signal with the ﬁnger. Although faster
responses have been reported from other anatomical positions
before [36], [37], the neck is still signiﬁcantly faster than
the ﬁnger. This response can be crucial when trying to
develop a monitoring system intended to be used in critical
applications—such as the prevention of SUDEP [3], [9].

The evaluation results, however, showed that

the SpO2
error increased at lower recorded SpO2 levels. This error can
be attributed to the difﬁculty of obtaining a homogeneous
distribution of SpO2 levels with the current experimental setup,
especially at lower SpO2 levels between 90% and 94%. The
SpO2 desaturation levels were not consistent across partici-
pants, as each participant equipped the respiratory modulating
device for an amount of time that they found comfortable.
The feasibility has been proven, prompting the need for future
controlled hypoxia experiments, involving a larger number
of subjects, a wider range of demographic characteristics,
lower desaturations, and less controlled conditions. Those will
allow for a more precise tuning of the custom calibration
parameters. Moreover, extraction of the ac and dc values
for estimation of the SpO2 was limited by the presence of
noise. Although this was mitigated using accelerometer-based
thresholding, bandpass ﬁltering, and outlier removal, ideally a
more elaborate automatic signal processing algorithms could
be developed in future work [38]–[41].

In terms of RR, the system was able to reliably identify
97.6% of the total respirations recorded by the ground-truth
system. This result can be presumed to be preliminary,

it

is likely that

since the cohort of subjects and RRs were limited;
is
nevertheless encouraging, since it demonstrates the potential
of the approach for analyzing respiratory activity from the
neck-acquired PPG signal. In a clinical context, this may be of
use to further support decisions from additional sensing modal-
ities [22] when trying to identify potentially dangerous apneas,
or even apnea events in the ictal phase [4], [42]. Additional
work could be carried out to investigate the optimal shape
and location of the enclosure, potential customization for the
user, and/or even the creation of variants for typical anatomical
characteristics. This is because the shape of the suprasternal
notch varies between subjects, with some having a consider-
ably higher degree of curvature than others. For subjects with
more concave suprasternal notches, the wearable could beneﬁt
from having a smaller form factor or a more ergonomic shape
to increase the contacting surface area between the sensor and
the user. Additionally, it has been reported that the mechanism
for respiration involves two degrees of freedom, namely the
the NWPPGS
thorax and abdomen [43]. It
is more heavily inﬂuenced by the movement of the thorax
and it would be worth investigating if results from subjects
with abdomen-dominant breathing are as accurate using the
NWPPGS. Furthermore, the current experimental setup tested
RRs in a resting state. Further experimentation should consider
a wider range of RRs, introduce apneic events, and investigate
whether using PPG in combination with airﬂow sensing could
increase the accuracy of the latter in differentiating poten-
tially dangerous apneas/hypopneas, prior to developing a more
advanced prototype incorporating both sensing modalities to
be tested in patients. The range of HR measured from 40 to
100 bpm in healthy individuals showed a strong correlation
and low degree of error that are sufﬁciently encouraging to
support further investigation into the use of the PPG signal
sensed in the neck. A potential study could obtain HR at
real time to support other biomarkers in a variety of clinical
applications. The Bland–Altman plot showed that errors did
not increase with an increase or decrease in HR. This is shows
a potential of this system to detect unusual transitory cardiac
trends in the context of epilepsy during seizures and postictal
states [1]. HR information, together with SpO2 estimation, and
airﬂow [22] could help to increase the accuracy in the inter-
pretation of dangerous overnight apnea events [9]. However,
as with RR and SpO2, future work needs to be carried out
to conﬁrm the robustness of the approach in a larger cohort
of subjects with wider demographic characteristics and less
controlled conditions. We have used the real-time transmission
of all data with ofﬂine processing to demonstrate the proof of
concept. However, different architectures are possible depend-
ing on the chosen application. For example, in cases where
the recorded physiological parameters are only needed during
a consultation with a doctor, continuous transmission between
the NWPPGS and the tablet can be triggered for small periods
overnight, keeping the system in low power mode at other
times, thereby saving battery life. Additionally, the NWPPGS
could transmit data on request, which could be visualized and
assessed either on a tablet or a cloud-based system. This,
however, comes with the disadvantage of reduced battery
life. Alternatively, the parameters could be computed on the

9509609

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 70, 2021

NWPPGS itself, and transmission will be triggered only when
abnormal values are detected. An on-device alarm system in
the presence of abnormal values may be advantageous in future
iterations to decrease its monitoring reliance on the tablet in
the event connection is lost. Ultimately, the different modes
can be used together to optimize the power consumption of
the system depending on the use case. Therefore, further
investigation is required to assess the feasibility of which
parameters can be calculated on the NWPPGS itself, and to
adjust data transfer rates between the NWPPGS and the tablet
to optimize for battery life and parameter detection time.

An additional challenge to optimizing battery life for wear-
able applications is the time delay generated during data
transmission. The NWPPGS’s maximum connection interval
between the tablet and NWPPGS was set to 40 ms—it can
therefore be assumed that
this delay between the sensed
parameter from the NWPPGS being transmitted to the tablet
would be of little consequence for real-time continuous data
transfer and analysis.

V. CONCLUSION

Noninvasive real-time sleep monitoring of patients can be
beneﬁcial to aid in the fast identiﬁcation of potentially life-
threatening physiological states in certain clinical contexts,
such as for SUDEP prevention. In this article, we demonstrated
the viability of extracting typical cardiorespiratory parameters
using a wearable PPG-based approach on the neck. The feasi-
bility of extracting blood oxygen saturation, pulse, and respira-
tion rate is demonstrated in a pilot study evaluation comparing
the outputs of the developed custom algorithms applied to the
sensed signal when compared to the measurements obtained
using signals recorded with a typical commercial cardiorespi-
ratory multichannel device. It was also proven that the novel
wearable responded to desaturation events quicker than the
gold-standard ﬁnger oximetry approach. This would be an
important advantage when trying to develop an alarm device
for time-critical applications, such as SUDEP.

ACKNOWLEDGMENT

The authors kindly acknowledge Acurable for providing
the necessary hardware for the designed wearable system.
They declare no conﬂict of interest. They also acknowledge
Dr. Syed Anas Imtiaz for his troubleshooting and embedded
systems assistance.

REFERENCES

[1] WHO. (2019). Epilepsy. [Online]. Available: https: //www.who.int/en/

news-room/fact-sheets/detail/epilepsy

[2] WHO. (2019). WHO—Epilepsy: A Public Health Imperative. [Online].
Available: http://www.who.int/mental health/neurology/epilepsy/report
2019/en/

[3] V. Latreille et al., “Nocturnal seizures are associated with more severe
hypoxemia and increased risk of postictal generalized EEG suppression,”
Epilepsia, vol. 58, no. 9, pp. e127–e131, Sep. 2017.

[4] L. Nashef, F. Walker, P. Allen, J. W. Sander, S. D. Shorvon, and
D. R. Fish, “Apnoea and bradycardia during epileptic seizures: Relation
to sudden death in epilepsy,” J. Neurol., Neurosurg. Psychiatry, vol. 60,
no. 3, pp. 297–300, Mar. 1996.

[5] D. J. Thurman, D. C. Hesdorffer, and J. A. French, “Sudden unexpected
death in epilepsy: Assessing the public health burden,” Epilepsia, vol. 55,
no. 10, pp. 1479–1485, Oct. 2014.

[6] A. G. Holst et al., “Epilepsy and risk of death and sudden unexpected
death in the young: A nationwide study,” Epilepsia, vol. 54, no. 9,
pp. 1613–1620, Sep. 2013.

[7] D. M. Ficker et al., “Population-based study of the incidence of
sudden unexplained death in epilepsy,” Neurology, vol. 51, no. 5,
pp. 1270–1274, Nov. 1998.

[8] O. Devinsky, “Sudden, unexpected death in epilepsy,” New England

J. Med., vol. 365, no. 19, pp. 1801–1811, Nov. 2011.

[9] O. Devinsky, D. C. Hesdorffer, D. J. Thurman, S. Lhatoo, and
G. Richerson, “Sudden unexpected death in epilepsy: Epidemiol-
ogy, mechanisms, and prevention,” Lancet Neurol., vol. 15, no. 10,
pp. 1075–1088, Sep. 2016.

[10] P. Ryvlin et al., “Incidence and mechanisms of cardiorespiratory arrests
in epilepsy monitoring units (MORTEMUS): A retrospective study,”
Lancet Neurol., vol. 12, no. 10, pp. 966–977, Oct. 2013.

[11] C. Jy, “Late-onset epilepsy associated with untreated obstructive sleep
apnea: A case report and literature review,” Neurol. Disorders Thera-
peutics, vol. 2, no. 2, pp. 1–5, Apr. 2018.

[12] S. V. Jain, T. Dye, and P. Kedia, “Value of combined video EEG and
polysomnography in clinical management of children with epilepsy and
daytime or nocturnal spells,” Seizure, vol. 65, pp. 1–5, Feb. 2019.
[13] M. A. Tork et al., “Sleep pattern in epilepsy patients: A polysomno-
graphic study,” Egyptian J. Neurol., Psychiatry Neurosurg., vol. 56,
no. 1, pp. 1–5, Dec. 2020.

[14] K. Vandecasteele et al., “Automated epileptic seizure detection based on
wearable ECG and PPG in a hospital environment,” Sensors, vol. 17,
no. 10, p. 2338, Oct. 2017.

[15] M. Ghamari, “A review on wearable photoplethysmography sensors and
their potential future applications in health care,” Int. J. Biosensors
Bioelectron., vol. 4, no. 4, p. 195, 2018.

[16] E. L’Her, Q.-T. N’Guyen, V. Pateau, L. Bodenes, and F. Lellouche,
“Photoplethysmographic determination of the respiratory rate in acutely
ill patients: Validation of a new algorithm and implementation into a
biomedical device,” Ann. Intensive Care, vol. 9, no. 1, p. 11, Dec. 2019.
[17] J. Allen, “Photoplethysmography and its application in clinical phys-
iological measurement,” Physiol. Meas., vol. 28, no. 3, pp. R1–R39,
Mar. 2007.

[18] I. García-López and E. Rodriguez-Villegas, “Extracting the jugular
venous pulse from anterior neck contact photoplethysmography,” Sci.
Rep., vol. 10, no. 1, pp. 1–12, Dec. 2020.

[19] T. Tamura, Y. Maeda, M. Sekine, and M. Yoshida, “Wearable photo-
plethysmographic sensors—Past and present,” Electronics, vol. 3, no. 2,
pp. 282–302, Apr. 2014.

[20] L. Cadmus-Bertram, R. Gangnon, E. J. Wirkus, K. M. Thraen-Borowski,
and J. Gorzelitz-Liebhauser, “The accuracy of heart rate monitoring by
some wrist-worn activity trackers,” Ann. Internal Med., vol. 166, no. 8,
p. 610, Apr. 2017.

[21] E. Jo, K. Lewis, D. Directo, M. J. Kim, and B. A. Dolezal, “Validation of
biofeedback wearables for photoplethysmographic heart rate tracking,”
J. Sports Sci. Med., vol. 15, no. 3, p. 540, 2016.

[22] E. Rodriguez-Villegas, G. Chen, J. Radcliffe, and J. Duncan, “A pilot
study of a wearable apnoea detection device,” Brit. Med. J. Open, vol. 4,
no. 10, p. 5299, 2014.

[23] I. Garcia-Lopez, P. Sharma, and E. Rodriguez-Villegas, “Heart rate
extraction from novel neck photoplethysmography signals,” in Proc.
41st Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. (EMBC), Jul. 2019,
pp. 6541–6544.

[24] I. Garcia-Lopez and E. Rodriguez-Villegas, “Characterization of artifact
signals in neck photoplethysmography,” IEEE Trans. Biomed. Eng.,
vol. 67, no. 10, pp. 2849–2861, Oct. 2020.

[25] M. Peng, S. A. Imtiaz, and E. Rodriguez-Villegas, “Pulse oximetry in
the neck—A proof of concept,” in Proc. 39th Annu. Int. Conf. IEEE
Eng. Med. Biol. Soc. (EMBC), Jul. 2017, pp. 877–880.

[26] I. Garcia-Lopez, S. A. Imtiaz, and E. Rodriguez-Villegas, “Characteri-
zation study of neck photoplethysmography,” in Proc. 40th Annu. Int.
Conf. IEEE Eng. Med. Biol. Soc. (EMBC), Jul. 2018, pp. 4355–4358.

[27] Y. Zhong, Y. Pan, L. Zhang, and K.-T. Cheng, “A wearable signal
acquisition system for physiological signs including throat PPG,” in
Proc. 38th Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. (EMBC),
Aug. 2016, pp. 603–606.

[28] High-Sensitivity Pulse Oximeter and Heart-Rate Sensor for Wearable
Health MAX 30102 Datasheet, Maxim Integr., San Jose, CA, USA,
Oct. 2018.

[29] LIS2DH12: MEMS Digital Output Motion Sensor Ultra-Low-Power
High-Performance 3-Axis Nano Accelerometer LIS2DH12 Datasheet, ST
Microelectron., Geneva, Switzerland, Jul. 2017.

SINGH et al.: PROOF OF CONCEPT OF NOVEL NECK-SITUATED WEARABLE PPG SYSTEM

9509609

[30] nRF52832 Product Speciﬁcation V1.3, nRF52832 Datasheet, Nordic

Semicond., Trondheim, Norway, Feb. 2017.

[31] Medical Information—Ultrabreathe. Accessed: Jan. 3, 2021. [Online].

Available: https: //www.ultrabreathe.com/medical-information/

[32] J. Shin and J. Cho, “Noise-robust heart rate estimation algorithm
from photoplethysmography signal with low computational complexity,”
J. Healthcare Eng., vol. 2019, pp. 1–7, May 2019.

[33] H.-E. Liao, “Two discrete oscillator based adaptive notch ﬁlters (OSC
ANFs) for noisy sinusoids,” IEEE Trans. Signal Process., vol. 53, no. 2,
pp. 528–538, Feb. 2005.

[34] Application Note 6845 Guidelines for SPO2 Measurement Using the
Maxim? MAX32664 Sensor hub, M. I. Products, San Jose, CA, USA,
2019.

[35] Pulse Oximeters Premarket Notiﬁcation Submissions [510(k)s]: Guid-
ance for Industry and Food and Drug Administration Staff, US Food
and D. A. (FDA), Silver Spring, MD, USA, 2013.

[36] H. J. Davies, I. Williams, N. S. Peters, and D. P. Mandic, “In-ear
SpO2: A tool for wearable, unobtrusive monitoring of core blood oxygen
saturation,” Sensors, vol. 20, no. 17, p. 4879, Aug. 2020.

[37] B. Bradke and B. Everman, “Investigation of photoplethysmography
behind the ear for pulse oximetry in hypoxic conditions with a novel
device (SPYDR),” Biosensors, vol. 10, no. 4, p. 34, Apr. 2020.
[38] Y. Zhang et al., “Motion artifact reduction for wrist-worn photoplethys-
mograph sensors based on different wavelengths,” Sensors, vol. 19, no. 3,
p. 673, Feb. 2019.

[39] J. Lee, M. Kim, H. K. Park, and I. Y. Kim, “Motion artifact reduction
in wearable photoplethysmography based on multi-channel sensors with
multiple wavelengths,” Sensors, vol. 20, no. 5, p. 1493, 2020.

[40] J.-J. Liao, S.-Y. Chuang, C.-C. Chou, C.-C. Chang, and W.-C. Fang,
“An effective photoplethysmography signal processing system based
on EEMD method,” in Proc. VLSI Design, Automat. Test (VLSI-DAT),
Apr. 2015, pp. 1–4.

[41] P. Thamarai and K. Adalarasu, “Denoising of EEG, ECG and PPG
signals using Wavelet Transform,” J. Pharmaceutical Sci. Res., vol. 10,
no. 1, pp. 156–161, 2018.

[42] Toolkit for Commissioning and Planning Local NHS Services in the
U.K. Obstructive Sleep Apnoea (OSA), Brit. Lung Found., London, U.K.,
2015.

[43] M. Chu et al., “Respiration rate and volume measurements using
wearable strain sensors,” Npj Digit. Med., vol. 2, no. 1, pp. 1–9, 2019.

Sukhpreet Singh received the B.Eng. degree in biomedical engineering from
the University of Victoria, Victoria, BC, Canada, in 2011.

His past experiences have included the development of upper limb prosthe-
ses and wearable device development for medical applications. He is currently
a Research Assistant with the Wearable Technologies Laboratory, Imperial
College London, London, U.K. His current
interests include low-power
electronics and optomechanical design optimization.

Michał Kozłowski
received the M.Eng. and Ph.D. degrees from the
University of Bristol, Bristol, U.K., in 2015 and 2020, respectively. His
doctoral thesis addressed robust and efﬁcient algorithms for indoor localization
in healthcare applications.

He is currently a Research Associate with Imperial College London,
London, U.K. His work spans the areas of machine learning, signal processing,
robotics, wireless communications, and wearable sensor design. His current
research interests include active learning, robustiﬁcation of personal sensing
systems, as well as efﬁcient and practical data collection techniques.

Irene García-López (Student Member, IEEE) received the B.Eng. degree in
biomedical engineering from the University Carlos III Madrid, Spain, in 2015,
and the M.Sc. degree in neurotechnology from Imperial College London,
London, U.K., in 2016, where she is currently pursuing the Ph.D. degree,
focusing on signal processing of photoplethysmography signals.

Zhou Jiang received the B.Eng. degree in electrical and electronic engineering
from the University of Bristol, Bristol, U.K., in 2011, the M.Sc. degree
in integrated circuit design from Imperial College London, London, U.K.,
in 2012, and the Ph.D. degree from the Circuit sand Systems Group, Imperial
College London, in 2017.

His current research interests include analog and digital integrated circuit
designs for miniature wireless neuronal activity recording systems, ultralow
power analogs, RF integrated circuit designs for wireless applications, and
system level design with wireless wearable devices for recording vital physi-
ological signals and health monitoring.

Esther Rodriguez-Villegas (Senior Member, IEEE) received the Ph.D. degree
from the University of Seville, Seville, Spain, in 2002.

Since 2002, she has been a Faculty Member with the Imperial College
London, London, U.K. Since 2015, she holds the Chair of low-power
electronics with the Department of Electrical and Electronic Engineering. She
is also the Director of the Wearable Technologies Laboratory. She has trained
over 700 engineers from all over the world at the M.S. or Ph.D. levels in
ultralow-power electronic design. She is also the Chief Scientiﬁc Ofﬁcer of
TaniTec, Ltd., London, and the Co-Chief Executive Ofﬁcer of Acurable, Ltd.,
London, which she founded.

Dr. Rodriguez-Villegas has received a number of awards and honors,
including being recognized as the Top Young Scientist/Engineer in Spain,
in 2009 (the Complutense Award); the Institution of Engineering and Tech-
nology (U.K.) Innovation Award, in 2009; being recognized twice by the
European Research Council as a Research Leader in Europe (Starting and
Consolidator Awards, in 2010 and 2016); and the XPRIZE (USA) Award,
in 2014.
