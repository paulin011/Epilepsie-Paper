# Elfaramawy et al. - 2019 - A Wireless Respiratory Monitoring System Using a Wearable Patch Sensor Network

650

IEEE SENSORS JOURNAL, VOL. 19, NO. 2, JANUARY 15, 2019

A Wireless Respiratory Monitoring System Using a
Wearable Patch Sensor Network

Tamer Elfaramawy, Cheikh Latyr Fall

, Soodeh Arab, Student Member, IEEE, Martin Morissette,

François Lellouche, and Benoit Gosselin , Member, IEEE

Abstract— Wireless body sensors are increasingly used by
clinicians and researchers in a wide range of applications, such
as sports, space engineering, and medicine. Monitoring vital
signs in real time can dramatically increase diagnosis accuracy
and enable automatic curing procedures, e.g., detect and stop
epilepsy or narcolepsy seizures. Breathing parameters are critical
in oxygen therapy, hospital, and ambulatory monitoring, while
the assessment of cough severity is essential when dealing with
several diseases, such as chronic obstructive pulmonary disease.
In this paper, a low-power wireless respiratory monitoring system
with cough detection is proposed to measure the breathing
rate and the frequency of coughing. This system uses wearable
wireless multimodal patch sensors, designed using off-the-shelf
components. These wearable sensors use a low-power nine-axis
inertial measurement unit to quantify the respiratory movement
and a MEMs microphone to record audio signals. Data processing
and fusion algorithms are used to calculate the respiratory
frequency and the coughing events. The architecture of each
wireless patch-sensor is presented. In fact, the results show that
the small 26.67 × 65.53 mm2 patch-sensor consumes around
12–16.2 mA and can last at least 6 h with a miniature 100-mA
lithium ion battery. The data processing algorithms, the acqui-
sition, and wireless communication units are described. The
proposed network performance is presented for experimental
tests with a freely behaving user in parallel with the gold standard
respiratory inductance plethysmography.

Index Terms— Breathing rate, coughing detection,

inertial
low-power, wearable,

measurement unit, wireless, real-time,
patch sensors network, data fusion.

I. INTRODUCTION

H EALTH care expenses are continuously increasing and

are taking a large part of a country’s budget. During
medical care, vital signs, such as heart and breathing rates,
are key parameters that are continuously monitored. Coughing
is a prominent indicator of several problems such as chronic
obstructive pulmonary disease (COPD), and it is also the

Manuscript received August 20, 2018; revised October 5, 2018; accepted
October 5, 2018. Date of publication October 23, 2018; date of current
version December 21, 2018. This work was supported in part by the Natural
Sciences and Engineering Research Council of Canada, in part by the Fonds
de recherche du Québec—Nature et technologies, in part by the Microsystems
Strategic Alliance of Quebec, and in part by Oxy’Nov Inc. This is an expanded
paper from the IEEE SENSORS 2017 Conference. The associate editor
coordinating the review of this paper and approving it for publication was
Dr. Rosario Morello. (Corresponding author: Tamer Elfaramawy.)

T. Elfaramawy, C. L. Fall, S. Arab, and B. Gosselin are with the
Department of Electrical and Computer Engineering, Université Laval,
Quebec, QC G1V 0A6, Canada (e-mail: tamer.elfaramawy.1@ulaval.ca).
M. Morissette is with Oxy’Nov Inc., Quebec, QC G2J 0C4, Canada.
F. Lellouche is with the Research Center of IUCPQ, Université Laval,

Quebec, QC G1V 0A6, Canada.

Digital Object Identiﬁer 10.1109/JSEN.2018.2877617

main reason for why patients seek medical advice [1]. In fact,
it is a pulmonary defense mechanism of the respiratory tract
that allows the expulsion of undesirable and irritating sub-
stances. Drugman et al. [2] studied the performance of several
automatic coughing detection sensors and concluded that the
best performances are achieved by systems that include an
audio microphone which can also be used to measure the
breathing activity [3]. In Sleep Disordered Breathing (SDB)
studies, the respiratory effort signal is estimated to help in
the detection of sleep apnoea [4], [5]. The average typical
healthy respiratory rate is around 12 to 20 breaths par minute.
In other words, a normal breathing frequency range is around
the 0.2 to 0.3 Hz. Several other methods have been used
to precisely monitor breathing activity. In-deed, contactless
methods exist, like with the Doppler Radar [6]–[8], the ultra-
wide band (UWB) radar [9], the laser method [10], using
WiFi signals [11], pyro-electric infrared (PIR) sensor [12],
a web-cam [13] or with depth images of a Kinect sensor [14],
but they aren’t suitable for dynamic environments since they
usually require a static setup. The respiratory inductance
plethysmography (RIP) is presented as the gold standard in
breathing surveillance especially for wearable measurement
systems [15]. It evaluates pulmonary ventilation by measuring
the induction in straps attached around the chest and abdomi-
nal wall. Another wearable method is the capacitive sensor
as described in [16]. It consists of integrating two textile-
based capacitive electrodes on the sides of a shirt which
can facilitate long-term monitoring. In [17], the capacitive
sensor can be even integrated in a shirt and in [18] six
Fiber Bragg grating (FBG) sensors are integrated in a smart
textile. Ono et al. [19] propose a small piezoelectric sensor
placed close to the nose or mouth. It monitors the breathing
ﬂow by measuring the temperature and pressure variations.
While these solutions can offer precise measurement results
with stationary users,
they fail with highly mobile users.
Additionally, for respiratory and sleep monitoring of freely
behaving users, more comfort and unobtrusiveness are needed.
Hence, in [20], a respiratory rate system for a stationary user
is developed using the three axes of an accelerometer, and
in [21], a dynamic respiration monitoring system is obtained
from the fusion of an accelerometer with a gyroscope and the
use of a Kalman ﬁlter, which yielded very compact systems.
In this paper, we present a real time low-power wireless
wearable measurement system based on a multimodal patch
sensor network that offers unlimited ﬂexibility and mobility

1558-1748 © 2018 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:54 UTC from IEEE Xplore.  Restrictions apply. 

ELFARAMAWY et al.: WIRELESS RESPIRATORY MONITORING SYSTEM USING A WEARABLE PATCH SENSOR NETWORK

651

two inertial measurement units (IMU) to measure both the
thoracic and abdominal cavity motions simultaneously. Data
from both accelerometers and gyroscopes are fused to obtain
the breathing rate and photoplethysmographic (PPG) signals in
real-time. When a problem arises with the respiratory system,
in a case of COPD for instance, the oxygen has difﬁculty get-
ting processed into the body. A common respiratory symptom
used to detect the COPD is coughing which is characterized
by a reﬂex contraction of the breathing muscles and a speciﬁc
sound. In that regard, a small MEMS microphone is used to
record the user’s coughing and airway sounds, and to detect
its frequency.

Fig. 1. Representation of the ventral body cavity, made up of the thoracic
and abdominal cavities, displacement during expiration (a) and inspiration (b).

III. SYSTEM DESIGN

A. System Architecture

for the user. It is designed with a respiratory monitoring system
with a coughing detection unit. It uses a complementary ﬁlter
to fuse the accelerometer and gyroscope data for efﬁcient
data processing, it also fuses the data coming from each
wireless node and is capable of detecting breathing data while
the patient is sitting and walking. In Section II, the system
design methodology is explained. In Section III and IV,
the hardware and software system design architectures are
presented. In Section V, the performance is reported for a
freely behaving user before concluding in Section VII.

II. SYSTEM OVERVIEW

While our system was ﬁrst shown in [22], an in-depth analy-
sis of the system is presented in this paper. The respiratory
system consists of all organs involved in breathing including
the lungs, all linked blood vessels, the airways such as the
nose, the mouth, the larynx, the trachea and the bronchial
tubes, and ﬁnally the muscles that enable breathing. This
system is vital for bringing oxygen into our body that is
vital for the survival of our cells and helps eliminating the
carbon dioxide, a waste gas, out of the body. The breathing
system uses the muscles near the lungs such as the diaphragm,
the intercostal, abdominal, neck and collarbone muscles for
breathing in a cyclic manner. Hence our methodology con-
sists of measuring the physical movements of the muscles.
There are two different types of physical movements during
a respiratory cycle, inspiration or breathing in, and expira-
tion or breathing out. The former starts with the intercostal
muscles contraction which raises the thoracic cavity and is
a joined with the diaphragm lowering. This increases the
thoracic intracavity space, decreases its pressure and lets air
enter the lungs. The latter continues on with the intercostal
muscles bringing the ribcage back in, lowering the thoracic
cavity, and with the abdominal muscles raising the diaphragm.
The expiration step decreases the thoracic intracavity space
while increasing its pressure and letting the air out of the lungs.
During this two step respiratory cycle, breathing is expressed
through an upper body activity with the thoracic cage, and with
a lower body activity with the abdominal cavity because of the
important role of the diaphragm and abdominals. Especially
during intense physical activities, the entire ventral cavity is
compressed and expanded, as seen in Fig. 1. Thus, we use

The overall block diagram of the wireless respiratory moni-
toring system, presented in Fig. 2, includes two different types
of acquisition nodes, one base station and a PC host for data
processing, data management and user interaction. The data
acquisition node 1, or thoracic node, is equipped with an
IMU sensor and a microphone while node 2, or abdominal
node, is only equipped with an IMU sensor. These acquisition
nodes are responsible for acquiring data from the different
sensors. They are placed on the body such as to obtain
the abdominal and thoracic breathing activities. Each one is
built around a MSP430 low-power microcontroller (MCU)
from Texas Instruments and use a LSM9DS0 IMU from
STMicroelectronics. Node 1 is also equipped with an analog
ADMP401 MEMS microphone from Analog Devices.

B. Microcontroller and Acquisition Nodes

The MSP-EXP430F5529LP, a development kit for the low
power MCU MSP430, is used for prototyping the acquisition
nodes that process the IMU’s and the microphone, as well
as for developing the wireless transceiver. As seen in Fig. 2,
the 16-bit MSP430F5529 MCU gathers data from the IMU
and the microphone before being sent wirelessly to the base-
station, using the low-power nRF24L01 radio module from
Nordic Semiconductor. In the case of acquisition node 1, after
that the analog audio data goes through an anti-aliasing ﬁlter at
5 kHz, see Fig. 3, it is sampled at a frequency of 10 kHz using
the 12-bit analog-to-digital converter (ADC), then buffered
using the direct memory access (DMA). Simultaneously, at a
rate of 32 Hz, a serial peripheral interface bus (SPI) is used to
transmit data from the IMU to the MCU where it is processed
to calculate the thoracic and abdominal displacement angles.
Finally, both data, the displacement angles and the audio data,
are relayed to the wireless transceiver using an SPI connection.

C. Wireless Transceiver

The low-power nRF24L01 radio module from Nordic Semi-
conductor, is used for all wireless transmission in the respira-
tory monitoring system. It transmits data from both acquisition
nodes to the base-station where acquired breathing and cough-
ing data are extracted. The RF IC can achieve up to 2 Mbps
on-air data rate, has transmission peaks less than 13 mA, offers
sub μA idle mode and is supplied on a 3.3 V supply voltage.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:54 UTC from IEEE Xplore.  Restrictions apply. 

652

IEEE SENSORS JOURNAL, VOL. 19, NO. 2, JANUARY 15, 2019

Fig. 2. Block diagram of the proposed wireless body sensor network including the data acquisition nodes, the base station, and, the data processing and
user interface.

Fig. 3. Circuit schematic of INMP401 analog MEMS microphone.

Fig. 5. Screenshot of the user interface showing the PPG (top) and the audio
signal showing speech (in black circles) and coughing (in red circles).

caption of the MATLAB interface that shows the displace-
ment of the ventral body cavity corresponding to PPG signal
(Fig. 5(a)), and the audio output of the microphone (Fig. 5(b)).
The respiratory frequency and the coughing occurrence are
depicted as well.

B. Abdominal and Thoracic Displacement Angles

Within the sensor nodes, the IMU provides the accelerom-
eter and gyroscope data to the MCU through an SPI interface
bus. To achieve a high speed transfer rate between the sensor
nodes and the base station, the amount of data to be transmitted
wirelessly is reduced through data processing in each node.
In fact, among the axes offered by the IMU, are 3 acceleration
axes and 3 rotational motion axes needed to calculate the
displacement angles. Instead of sending 6 data channels to the
base station, an interrupt routine is executed at a frequency
of 32 Hz within the nodes, where the abdominal and thoracic
displacement angles (or IMU rotation angles) are calculated
thanks to a ﬁrst order complementary ﬁlter as show in Fig. 6,
and then sent with the rest of data. Below, (1) and (2) are used
to calculate the angles when a user is standing or walking.
ωx is the rotational velocity along the x-vector, ay and ax
are the acceleration components along the y and x-vector,

Fig. 4. Block diagram of the signal processing unit including: the respiration
rate waveform unit, the respiration rate unit and the coughing detection unit.

IV. DATA PROCESSING AND ALGORITHMS

While the abdominal and thoracic displacement angles
processing are implemented directly within the sensor nodes
(in-situ),
the signal processing unit, depicted in Fig. 4,
is implemented ex-situ, inside the PC host. In fact, through this
unit is calculated the breathing frequency and the occurrence
of coughing, the details of which calculations are provided in
the next sections.

A. User Interface

The user interface as well as the digital signal processing are
both developed in MATLAB. The interface allows the user to
visualize the motion and the derived PPG and sound signals
acquired from the 2 sensor nodes in real-time. Fig. 5 is a

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:54 UTC from IEEE Xplore.  Restrictions apply. 

ELFARAMAWY et al.: WIRELESS RESPIRATORY MONITORING SYSTEM USING A WEARABLE PATCH SENSOR NETWORK

653

Fig. 6.
Block diagram of the complementary ﬁlter used to calculate
the abdominal and thoracic displacement angles where ay and az are the
acceleration components on the y and z-vector, ωx the rotational velocity
along the x-vector, θa the accelerometer rotation angle and θg the gyroscope
rotation angle.

angle is the displacement angle, αgyro and αacc are the
complementary ﬁlter coefﬁcients. In Fig. 6, αgyro and αacc are
represented by low and high pass ﬁlters. In-deed, αacc.θa[n]
acts the low pass ﬁltering of the accelerometer rotation angle
while αgyro. θg[n] represents the high pass ﬁltering of the
gyroscope rotation angle. In other words, the complementary
ﬁlter calculates a rotation angle around a desired vector by
removing noise from the accelerometer, eliminating the gyro
drift and by fusion them.

with

angle[n] = αgyro.θg[n] + αacc.θa[n]

⎧
⎨⎨

⎨⎩

αgyro = 1 − αacc
θg[n] = angle[n − 1] + ωx [n].t
θa[n] = atan2(−ay, az)

(1)

(2)

When the user is laying down, different vectors are used. The
optimal vectors are decided by comparing them to the gravi-
tational vector such as no disruptions occur when calculating
the rotational angle during the respiration cycle since the angle
is limited to − π

2 and π
2 .

C. Breathing Activity

Breathing activity is expressed from the chest and abdomen.
Hence, after initial synchronization of data coming from each
node, a data fusion is performed by calculating the arithmetic
mean of both,
the abdominal and thoracic displacements
angles, to achieve a ventral body cavity angle. To obtain the
real-time PPG, only a few steps are needed. First the average
displacement angle is calculated over a 3-second window and
eliminated to remove the body movement, then a 20th order
low-pass FIR ﬁlter with a cut-off frequency at 2 Hz is used. For
the respiration rate, several steps are needed to ensure that all
high-frequency components are eliminated, but also all noise
artifacts coming from the body. Especially since the calculated
ventral cavity angle includes the breathing movement, but also
any rotation around the sensor node like body movements.
Hence,
the ventral cavity angle is decimated to 5 Hz to
eliminate all high frequency components and followed by a 1st
order high-pass ﬁlter at 0.01 Hz to remove the baseline wander.
A Savitzky-Golay smoothing ﬁlter, chosen for its easy and
efﬁcient implementation in many systems including in [21],
is used to smooth the signal before applying a peak detection
algorithm to detect the breathing peaks. In Fig. 7(a) and (b),

Fig. 7.
The ventral body cavity angle before (a) and after (b) signal
processing, and (c) the RIP signal as a reference, with a distortion circled
in black.

the signal is presented before and after its ﬁltering and peak
detection.

D. Cough Detection

To detect coughing, we propose a simple but efﬁcient
method. Audio data is usually sampled at a high frequency
of 10 kHz. In the MCU, to ensure that the data is transferred
without interrupting other tasks, a DMA is used. After data
two seconds of audio data is saved for
synchronization,
processing. The zero-crossing rate (ZCR), which is heavily
used in speech recognition, is taken as the sign change rate
along the recorded audio signal [23]. Here, it is used to detect
the strong important signal changes when coughing occurs.
Furthermore, to maximize the algorithm efﬁciency, noise ﬂoor
is eliminated by setting to zero all data smaller than a pre-
determined threshold coefﬁcient , as seen in (3).


S[n] =

S[n],
0,

if S[n] > 
if S[n] < 

(3)

The ZCR is then applied, as seen in (4), where S is the signal
of length T and 1<0 the indicator function.

zcr = 1

T − 1

T −1

t =1

1<0

(St St −1 < 0)

(4)

Hence, to differentiate coughing from speech, a peak detection
algorithm is applied following a Savitzky-Golay smoothing
ﬁlter to detect only events with a higher zero-crossing rate.

V. MEASURED PERFORMANCES

In this section, we look at the wireless monitoring wearable
sensor performances in terms of durability, autonomy, usability
and precision. The ﬁnal wireless respiration monitoring system
characteristics and measurements are shown in Table I.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:54 UTC from IEEE Xplore.  Restrictions apply. 

654

IEEE SENSORS JOURNAL, VOL. 19, NO. 2, JANUARY 15, 2019

TABLE I

SUMMARY OF SYSTEM CHARACTERISTICS

Fig. 9.
placed on user (left) and base station (right).

Picture of the 2 sensor nodes (node 1 in black and node 2 in red)

Fig. 8. Printed circuit board of the proposed multimodal patch sensor.

A. Multimodal Patch Sensor

The wireless respiratory monitoring and coughing detection
sensor network is composed of two nodes. Each node is
designed using a 4-layer printed circuit board, including 2 sig-
nal layers, 1 ground layer and 1 supply voltage layer, as seen
in Fig. 8. The boards measures 26.67 × 65.53 mm2 which is
big enough to enable a programming input port identiﬁed by
P9 and small enough to be carried easily and ﬂexibly by the
user. The minimum gap between tracks is 0.2 mm and the
holes minimum diameter is 0.4 mm. The printed circuit board
is composed of 5 main units including the microcontroller
unit (MCU), the power management unit (PMU), the inertial
measurement unit (IMU), the audio unit (AUDIO) and the
radio frequency module (RF), as seen in Fig. 8. The sensor is
powered with a 3.7-V 100-mAh Li-ion battery and its RF-link
allows up to 8 meters of transmission.

B. Experimentation Procedures

During the experimentation, a user had the two sensor nodes
placed on the thoracic and abdominal cage, see Fig. 9, and in
the same time, a medical respiratory inductance plethysmog-
raphy (RIP) belt was attached around the chest as a reference.
Firstly, several experimental tests were done to ﬁnd the optimal
sensors location. Secondly, a performance test was done while
the user was walking to demonstrate its robustness. Finally, the

Fig. 10. The ventral body cavity angle after signal processing, also named
Filtered Roll, for 2 different users when the sensors are both placed on the
thoracic cavity (or TC) and when 1 is placed on the thoracic cavity and the
other on the abdominal cavity (or AC).

proposed monitoring system’s performance is compared to the
RIP belt.

C. Respiration Signal Analysis

An experimental test was performed to study the difference
in breathing signal results when the sensor is placed on the
thoracic and the abdominal cage. In Fig. 10, a comparison of
the breathing signal coming from two users when the sensors
are both placed on the thoracic cage and when each is placed
on the abdominal and the thoracic cavity. It can clearly be
seen that when one of the sensors is placed on the abdominal
cavity, the amplitude of the signal is greatly enhanced. This is
due to the fact that when sitting the users breaths mostly from
the abdominal area whereas when the user is doing a physical
exercise, the breathing will be enhanced in the thoracic area.
In Fig. 11, the robustness was demonstrated by having the
user test the monitoring system while sitting and walking.
In fact, at the 25th second of the Angle Fusion while walking
signal, noise coming from the movement is ﬁltered to obtain
a breathing cycle as seen in the second signal Filtered Angle
During walking. During the third experimental test, the breath-
ing cycles obtained through the medical gold standard RIP
belt and from our wireless monitoring system were compared

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:54 UTC from IEEE Xplore.  Restrictions apply. 

ELFARAMAWY et al.: WIRELESS RESPIRATORY MONITORING SYSTEM USING A WEARABLE PATCH SENSOR NETWORK

655

Fig. 11.
processing when the user is sitting and walking.

The ventral body cavity angle before (a) and after (b) signal

Fig. 13. Power consumption breakdown of the sensor nodes in %.

Fig. 12. The spectrogram of a 60 second processed breathing signal sample
with the maximum PSD shown in black.

as shown in Fig. 7. In the latter, the angle before and after
ﬁltering, and the RIP signal are all shown while the user is
walking. The ﬁgure particularly shows the system functioning
correctly while the user is moving. Furthermore, it is able
to detect breathing patterns during heavy distortions as seen
circled in black at the 25th second in the three graphs, where
the user disrupts the signal by sneezing. Also, a signiﬁcant
synchronization time was needed for each new use when
setting the RIP belt up while data from the patch was obtained
almost instantaneously. Finally, the spectrogram of a processed
respiratory signal, presented in Fig. 12, shows its maximum
PSD during 60 seconds of breathing. In this ﬁgure, the signal
power is clearly concentrated between 0.2 and 0.4 Hz with the
maximum power at around 0.35 Hz. In fact, the PPG of this
signal shows around 23 breathing cycles during 60 seconds,
which corresponds to around 0.38 Hz. The signal analysis
through the spectrogram is an important tool in understanding
the breathing signal distribution through time as well as for
building the respiratory data processing algorithms.

D. Power Consumption

While the abdominal sensor node consumes only 12 mA,
the thoracic sensor node consumption goes up to 16.2 mA with

Fig. 14. The microphone audio signal spectrogram showing coughing events
with the audio microphone signal in blue, the ﬁltered ZCR of the signal in
green and maximum PSD of the ﬁltered signal in red.

a 3.7 V supply voltage because of a higher data transmission
the consumption
rate due to the microphone. In Fig. 13,
breakdown for the latter is shown.

E. Coughing Detection

In Fig. 5, an image of the interface showing the PPG signal
and the audio signal is given. In the latter, the coughing
events and the pronunciation of words can be discriminated
in the audio signal. Indeed, the ZCR was able to differentiate
between the different audio sounds and recognize a cough.
In Fig. 14, a spectrogram of the microphone audio signal
shows the correlation between the maximum PSD of the
audio signal, shown in red, and the zero-crossing rate, show
in green. In blue, the original audio signal is shown with
several signal peaks corresponding to coughing events. In fact,
these important signal variations that occur when the user
is coughing, distinct by a strong power spectral density, are
detected with a simple but efﬁcient algorithm. Thanks to a

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:54 UTC from IEEE Xplore.  Restrictions apply. 

656

IEEE SENSORS JOURNAL, VOL. 19, NO. 2, JANUARY 15, 2019

peak detection algorithm applied on the ﬁltered ZCR signal,
every coughing event can be easily identiﬁed.

VI. DISCUSSION

The breathing activity analysis including the respiratory
frequency, the photoplethysmogram with the detection of each
cough event are all important respiratory parameters that can
help in the development of a robust and reliable diagnosis and
monitoring technologies. Hence, the next step will consist of
fusing respiratory and coughing data for a complete modeling
and analysis of the respiratory system. Further studies would
also include its application in the clinical assessment of
breathing activities and of cough.

VII. CONCLUSION

A real-time wireless respiratory monitoring system with
coughing detection is presented for patient surveillance dur-
ing ambulatory, hospital and home care. It uses low-power
electronic building blocks and is designed to maximize the
movement and comfort for the user with its small size circuit,
see Table I. Its set-up is much quicker and easier to use
than the RIP used in hospitals since it doesn’t need any
synchronization. Results show that the system can acquire
breathing data while the patients is resting but also when
walking. While the system is able to detect the coughing
occurrence, more complex algorithms have been proposed
in speech recognition that can be used to improve its efﬁ-
ciency especially when talking [2], [23]. The MCU and RF
module power consumption can be greatly improved through
ASIC design. The system can also be expanded to include
cardiovascular, blood pressure and temperature monitoring
units to increase diagnostic reliability. Future work will also
include developing more robust algorithms to enable continu-
ous breathing surveillance during different sports activity.

REFERENCES

[1] S. M. Schappert and C. W. Burt, “Ambulatory care visits to physician
ofﬁces, hospital outpatient departments, and emergency departments:
United States, 2001–02,” Vital Health Statist. Ser. Data Nat. Health
Surv., vol. 159, pp. 1–66, Feb. 2006.

[2] T. Drugman et al., “Objective study of sensor relevance for automatic
cough detection,” IEEE J. Biomed. Health Inform., vol. 17, no. 3,
pp. 699–707, May 2013.

[3] Y. Nam, B. A. Reyes, and K. H. Chon, “Estimation of respiratory
rates using the built-in microphone of a smartphone or headset,” IEEE
J. Biomed. Health Inform., vol. 20, no. 6, pp. 1493–1501, Nov. 2016.

[4] M. Jayawardhana and P. de Chazal, “Enhanced detection of sleep apnoea
using heart-rate, respiration effort and oxygen saturation derived from
a photoplethysmography sensor,” in Proc. 39th Annu. Int. Conf. IEEE
Eng. Med. Biol. Soc. (EMBC), Jul. 2017, pp. 121–124.

[5] I. Sadek, E. Seet, J. Biswas, B. Abdulrazak, and M. Mokhtari, “Non-
intrusive vital signs monitoring for sleep apnea patients: A preliminary
study,” IEEE Access, vol. 6, pp. 2506–2514, 2018.

[6] X. Gao, A. Singh, E. Yavari, V. Lubecke, and O. Boric-Lubecke,
“Non-contact displacement estimation using Doppler radar,” in Proc.
Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. (EMBC), Aug./Sep. 2012,
pp. 1602–1605.

[7] W. Li, B. Tan, and R. J. Piechocki, “Non-contact breathing detec-
tion using passive radar,” in Proc. IEEE Int. Conf. Commun. (ICC),
May 2016, pp. 1–6.

[8] A. Üncü, “A 24-GHz Doppler sensor system for cardiorespiratory mon-
itoring,” in Proc. 42nd Annu. Conf. IEEE Ind. Electron. Soc. (IECON),
Oct. 2016, pp. 5161–5164.

[9] Q. Jian, J. Yang, Y. Yu, P. Björkholm, and T. McKelvey, “Detection
of breathing and heartbeat by using a simple UWB radar system,”
(EuCAP), Apr. 2014,
in Proc. 8th Eur. Conf. Antennas Propag.
pp. 3078–3081.

[10] T. Kondo, T. Uhlig, P. Pemberton, and P. D. Sly, “Laser monitor-
ing of chest wall displacement,” Eur. Respirat. J., vol. 10, no. 8,
pp. 1865–1869, 1997.

[11] S. Lee, Y.-D. Park, Y.-J. Suh, and S. Jeon, “Design and implementa-
tion of monitoring system for breathing and heart rate pattern using
WiFi signals,” in Proc. 15th IEEE Annu. Consum. Commun. Netw.
Conf. (CCNC), Jan. 2018, pp. 1–7.

[12] F. Erden and A. E. Cetin, “Breathing detection based on the topological
features of IR sensor and accelerometer signals,” in Proc. 50th Asilomar
Conf. Signals, Syst. Comput., Nov. 2016, pp. 1763–1767.

[13] T. Nochino, Y. Ohno, and S. Okada, “Development of noncontact
respiration monitoring method with Web-camera during sleep,” in
Proc. IEEE 6th Global Conf. Consum. Electron. (GCCE), Oct. 2017,
pp. 1–2.

[14] T. Ushijima and J. Satake, “Development of a breathing detection robot
for a monitoring system,” in Proc. Joint 8th Int. Conf. Soft Comput.
Intell. Syst. (SCIS), 17th Int. Symp. Adv. Intell. Syst. (ISIS), Aug. 2016,
pp. 790–795.

[15] A. Hart, K. Tallevi, D. Wickland, R. E. Kearney, and J. A. Cafazzo,
“A contact-free respiration monitor for smart bed and ambulatory
monitoring applications,” in Proc. Annu. Int. Conf. IEEE Eng. Med.
Biol., Aug./Sep. 2010, pp. 927–930.

[16] S. K. Kundu, S. Kumagai, and M. Sasaki, “A wearable capacitive sensor
for monitoring human respiratory rate,” Jpn. J. Appl. Phys., vol. 52,
no. 4S, p. 04CL05, 2013. [Online]. Available: http://stacks.iop.org/1347-
4065/52/i=4S/a=04CL05

[17] S. W. Park, P. S. Das, A. Chhetry, and J. Y. Park, “A ﬂexible capacitive
pressure sensor for wearable respiration monitoring system,” IEEE
Sensors J., vol. 17, no. 20, pp. 6558–6564, Oct. 2017.

[18] D. L. Presti et al., “Respiratory and cardiac rates monitoring during MR
examination by a sensorized smart textile,” in Proc. IEEE Int. Instrum.
Meas. Technol. Conf. (I2MTC), May 2017, pp. 1–6.

[19] Y. Ono, D. Mohamed, M. Kobayashi, and C.-K. Jen, “Piezoelectric
membrane sensor and technique for breathing monitoring,” in Proc.
IEEE Ultrason. Symp., Nov. 2008, pp. 795–798.

[20] A. Bates, M. J. Ling, J. Mann, and D. K. Arvind, “Respiratory rate and
ﬂow waveform estimation from tri-axial accelerometer data,” in Proc.
Int. Conf. Body Sensor Netw., Jun. 2010, pp. 144–150.

[21] J.-W. Yoon, Y.-S. Noh, Y.-S. Kwon, W.-K. Kim, and H.-R. Yoon,
“Improvement of dynamic respiration monitoring through sensor fusion
of accelerometer and gyro-sensor,” J. Elect. Eng. Technol., vol. 9, no. 1,
pp. 334–343, Jan. 2014, doi: 10.5370/JEET.2014.9.1.334.

[22] T. Elfaramawy, C. L. Fall, M. Morissette, F. Lellouche, and B. Gosselin,
“Wireless respiratory monitoring and coughing detection using a wear-
able patch sensor network,” in Proc. 15th IEEE Int. New Circuits Syst.
Conf. (NEWCAS), Jun. 2017, pp. 197–200.

[23] B. Ferdousi, S. M. F. Ahsanullah, K. Abdullah-Al-Mamun, and
M. N. Huda, “Cough detection using speech analysis,” in Proc. 18th
Int. Conf. Comput. Inf. Technol. (ICCIT), Dec. 2015, pp. 60–64.

Tamer Elfaramawy received the B.Sc. degree in
electronics engineering, specialized in radio and
telecommunication systems,
from the Bordeaux
Institute of Technology, Bordeaux, France, in 2014,
and the M.Sc. degree in electrical engineering from
Université Laval, Quebec, QC, Canada, in 2018. His
project was the design of a respiratory and vital signs
monitoring system. His main research interests are
digital and analog circuit design, intelligent wireless
biomedical sensors, and low-power body-implanted
microsystems.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:54 UTC from IEEE Xplore.  Restrictions apply. 

ELFARAMAWY et al.: WIRELESS RESPIRATORY MONITORING SYSTEM USING A WEARABLE PATCH SENSOR NETWORK

657

Cheikh Latyr Fall received the master’s degree in
automatic control and electrical engineering from the
Institut National des Sciences Appliquées, Toulouse,
France, in 2013. He is currently pursuing the Ph.D.
degree in electrical engineering with the Biomedical
Microsystems Laboratory, Laval University, Quebec,
QC, Canada. His main research interests are assis-
tive technologies, rehabilitation robotics, human–
machine interfaces, wireless body sensor networks,
and biomedical instrumentation.

in
Soodeh Arab received the B.Sc. degree
engineering from Shariati University,
electrical
Tehran, Iran, in 2006, the M.Sc. degree in opto-
electronic engineering from the Shiraz University of
Technology, Shiraz, Iran, in 2010, and her project
was the design and simulation of a mixer
for
2.4-GHZ communication standard using 0.18 μm
CMOS technology, and the master’s degree in
bio-electrical engineering from Laval University
in 2017, and her project was the implementing of
a low-power wireless system for real-time health
monitoring applications. In 2014, she started her research at Laval University
as a Research Assistant. Her main research interests include design of analog
CMOS integrated circuits (design, optimization, and modeling), RF micro-
electronics, wireless implantable biomedical systems, biomedical VLSI circuit
design, wireless sensor interfaces, wireless power and data transmission, and
circuit modeling/simulation/numerical analysis/computational techniques.

Martin Morissette received the bachelor’s degree
in electrical engineering. He has over 20 years of
experience in research and development of inno-
vative technologies in the telecommunications and
medical devices sector. He is currently the Research
and Development Director of OxyNov, a company
specialized in the conception of medical devices for
oxygen therapy.

François Lellouche received the M.D. degree in
internal medicine in 2001 and critical care medicine
in 2004 from the Pierre et Marie Curie University
(Paris VI) and the Ph.D. degree in science and
engineering: materials–modeling–environment from
the University of Paris XII, under the supervision of
Pr. L. Brochard. He was an INSERM–CIHR Post-
Doctoral Fellow with the Saint-Michael Hospital
Laboratory (Pr. Sinderby and A. Slutsky). He is
currently a Critical Care Physician with the Quebec
Heart and Lung University Institute and an Associate
Professor with the Department of Medicine, Laval University. His research
interests include humidiﬁcation of gas during mechanical ventilation, nonin-
vasive mechanical ventilation, high-ﬂow oxygen therapy, and new modes of
mechanical ventilation, focusing on automated modes of respiratory support
and closed-loop oxygen supplementation.

He conducts at the research center of the Quebec Heart and Lung Institute
bench studies, physiological studies focusing on breathing physiology and
clinical trials to evaluate the clinical impact based on preliminary studies. His
laboratory develops several innovative devices in the ﬁeld of respiratory and
oxygen support, including the FreeO2 device, a new breakthrough closed-loop
device that titrates oxygen ﬂow based on patient’s needs. He co-founded with
Pr. E. L’Her the Oxynov company that manufactures and commercializes the
FreeO2 device.

Benoit Gosselin (S’02–M’08) received the Ph.D.
degree in electrical engineering from the École Poly-
technique de Montréal in 2009. In 2010, he was
an NSERC Post-Doctoral Fellow with the Georgia
Institute of Technology. He is currently an Associate
Professor with the Department of ECE, Univer-
sité Laval, where he is also leading the Biomed-
ical Microsystems Laboratory. His research interests
include wireless microsystems for brain–computer
interfaces, analog-/mixed-mode and RF integrated
circuits for neural engineering, interface circuits of
implantable sensors/actuators, and point-of-care diagnostic microsystems for
personalized healthcare.

Dr. Gosselin has received several awards, including the Mitacs Award for
Outstanding Innovation and the NSERC Brockhouse Canada Prize for Inter-
disciplinary Research in Science and Engineering. He is currently the Chair
and the Founder of the IEEE CAS/EMB Quebec Chapter (2015 Best New
Chapter Award). He is also an Associate Editor of the IEEE TRANSACTIONS
ON BIOMEDICAL CIRCUITS AND SYSTEMS. He served on the committees of
several international conferences, such as IEEE BIOCAS, IEEE NEWCAS,
IEEE EMBC, IEEE LSC, and IEEE ISCAS. His signiﬁcant contribution to
biomedical microsystems research led to the commercialization of the ﬁrst
wireless microelectronic platform for optogenetics and electrophysiology with
live animals by Doric Lenses Inc.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:15:54 UTC from IEEE Xplore.  Restrictions apply.
