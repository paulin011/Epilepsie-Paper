# Jafer et al. - 2020 - A Wireless Body Area Network for Remote Observation of Physiological Signals

Theme Article: Special Section on Implementable
Theme Article: Special Section on Implementable
Humanitarian Technology
Humanitarian Technology

A Wireless Body Area
Network for Remote
Observation of
Physiological Signals

Essa Jafer
Princess Sumaya University for Technology

Xavier Fernando
Ryerson University

Sattar Hussain
Centennial College

Abstract—The objective of this work is to describe the design process of a wireless body
area network (WBAN) for the remote observation of multiple physiological signals from a
patient. Various sensors such as temperature, heart rate monitor utilizing

electrocardiography, and accelerometer to detect fall and seizure conditions were
integrated in the WBAN. Sensed data is wirelessly transmitted to the central control unit
(CCU) that is associated with a remote base station. For benchmarking, medically
certiﬁed sensors were employed to validate wearable sensors data. The sensor

information can be ported in the cloud environment using CCU-based gateway with Global
System for Mobile communication (GSM) modem capability. This mechanism is facilitating
remote access to sensors information. To connect Radio Frequency (RF) units wirelessly,
Zigbee mesh topology was adopted. In this way, they can be remotely overseen, managed

and controlled by assigned staff. The presented prototype featuring the desired WBAN
system performance was evaluated with different human postures and moving scenarios.

& WIRELESS BODY AREA network (WBAN) plat-
forms have evolved signiﬁcantly over the last

Digital Object Identiﬁer 10.1109/MCE.2019.2953736

Date of current version 7 February 2020.

few years. These typically integrate sensing and
radio modules for remotely observing patient
health and physical parameters.1,2 With WBAN,
individuals can easily keep track of their beloved
ones in addition to healthcare professionals
while they are away. Continuous monitoring and

March/April 2020

Published by the IEEE Consumer Electronics Society

2162-2248 (cid:1) 2019 IEEE 103

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:29 UTC from IEEE Xplore.  Restrictions apply. 

Special Section on Implementable Humanitarian Technology

Figure 1. Presented system architecture.

data collection shown to signiﬁcantly reduce
medical complexities at later stages.

In the past few years, a number of topologies
has been developed for WBAN and remote
observation.3,4 However, most of these devel-
oped prototypes are not sizably compact to be
worn by patients. In the work done by Abiodun
et al.,5 an algorithm to reduce power consump-
tion in WBAN by dropping the non (and semi)-
urgent signals while transmitting only the urgent
data to the medical server was presented. How-
ever, only one node (a diabetic sensor) is consid-
ered. Also in the work done by Abiodun et al., 5
the testing was done using OMNETþþ simulator
without implementation.

This work aims to build a reliable multisensor
WBAN for personal health observation with
emphasis on monitoring vital physiological sig-
nals such as heart rate and muscles acceleration.
The proposed system uses accurate and com-
pact medical sensors selected carefully to
assure a robust low-cost system intended to
remote monitoring of
help and facilitate
patients’ physical health.

SYSTEM OVERVIEW

The work presented in this article can be
divided into two phases; selection of sensing
units and integration of wireless communication
modules. Figure 1 outlines the architecture of
the system framework including the two, sensing
and communication, phases.

The ﬁrst task was picking the appropriate
sensors. The heart rate sensor was the hard-
est to select since it supposed to overcome
artifacts due to body movements. Detection of
lonely patients is also
fall and seizure of

Figure 2. Wearable sensor units featuring the
developed WBAN.

important. Room and body temperatures were
also recorded estimate body activity levels
and fever condition.

In addition to these four sensors, more bio-
medical sensors can be incorporated in the pro-
posed system due to its modular architecture.

SENSOR INTERFACE

Since the microcontroller board would inﬂu-
ence the selection of sensors, Arduino Uno
is
board with ATmega328 microcontroller
selected. Polar Heart Rate Monitor Receiver
(HRMI) and Polar T31C wearable sensor were
identiﬁed to be suitable for measuring heart rate
signal.6 The receiver unit converts the received
heart rate information from the wearable sensor
to electrocardiography (ECG) data. This method
is convenient since the patient can wear a strap
at any time and in any position.

A wearable accelerometer (ADXL345) was
used to record the falling and seizure events and
trigger an alert
if necessary. An onboard
HTU21D temperature sensor is used to monitor
the indoor temperature and humidity.6 The
HTU21D offers a precision of þ/– 0.3 (cid:2)C for tem-
perature and þ/– 2% for moisture which is ade-
quate. MLX90614 was used to log body
temperature.6 This infrared sensor reads skin
temperature with a precision of þ/– 0.5 (cid:2)C in the
extent of 0–60 (cid:2)C which is satisfactory.

The sensors were placed in chosen locations
deliberately, offering a high level of patient solace.
As shown in Figure 2, HTU21D and MLX90614
units are connected to the arm, where ADXL345

IEEE Consumer Electronics Magazine

104

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:29 UTC from IEEE Xplore.  Restrictions apply. 

Table 1. Results of the falling trials.

Trial test1

Trial test2

Trial test3

Forward falling

Detected

Detected

Detected

Backward falling

Detected

Detected

Detected

Sideway falling

Detected

Not Detected

Detected

Figure 3. It is obvious that the time delay is com-
parable for all ﬁve patients and it is fewer than 2
s for less than 10 m separation.

Temperature

The HTU21D and MLX90614 functionalities
were assessed to verify the precision and possi-
ble correlation. The tests were run for a roughly
17 h. The sensors were close to each other to
guarantee a reasonable estimating condition.
Tests run showed the comparable performance
of both sensors clearly in reading the tempera-
ture with a small maximum margin of approxi-
mately þ/– 0.75(cid:2)C.

Acceleration

incorporating

accelerometer

The fall recognition was studied by utilizing
Triaxial
falling
postures in various ways. Tests were performed
by falling onto a dozing cushion on the ﬂoor
from the deﬁned sites. Falling backward, for-
ward, and sideways were three tested possible
conditions.

Correct detection rate of 80% was set as the
threshold for accurate fall identiﬁcation. Table 1
exhibits the three-run tests coordinated at the
three falling conditions.

Just a single run sideway condition failed the
test, however, this can be clariﬁed due to non-
ideal settings of the equipment. Following the
design plan, the free fall hinder is activated
when the free fall limit setting is surpassed amid
the free-falling expected time. These settings
were suggested as empirical ﬁgures with the
goal that they would be touchier in identifying
the fall occasion.

Muscle acceleration signals can also be uti-
lized to detect different
types of seizure.
Accordingly, our sensors were placed on both
arms and lower legs to gauge the seizure mus-
cle activities utilizing the fused seizure discov-
ery calculation.7

Figure 3. Arrival times of data from patient.

and Polar HRMI units are appended to the belt. An
Xbee unit is used as the Radio Frequency (RF)
module to transmit the collected data.

WIRELESS SYSTEM CONFIGURATION
First, Xbee modules’ operation was evaluated
in a point to point arrangement. The coordinator
of the network (CCU) was conﬁgured in the
application programming interface mode to
administrate the system topology.

The ad hoc on-request distance vector
mesh routing approach6 was employed to con-
trol the information packets between different
wireless modules. The route identiﬁcation pro-
cess starts with the broadcasting request
command. When the destination module gets
the request,
it would perform a comparison
with previously received requests and send
back to that module if it has a better cost to
establish the link with the source point. All
intermediate nodes will receive and forward
data packets to the desired destination.
In
order to pass information to the cloud-based
administrative web,
thinkspeak server and
Xbee CCU were chosen to act as the middle
agent.6 This arrangement ﬂawlessly bridges
the Xbee modules with the Internet showing
all types of network interactions.

PERFORMANCE EVALUATION

One objective is to measure the time delay
that packets will take to be delivered to the ﬁnal
destination, by conducting tests on a number of
patients. This was done by recording the
received time at the CCU from each patient at dif-
ferent locations ranging from 1 to 20 m on tests
performed with 5 patients. These are shown in

March/April 2020

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:29 UTC from IEEE Xplore.  Restrictions apply. 

105

Special Section on Implementable Humanitarian Technology

Table 2. Pilot test results.

Age

Gender

Test timeframe
(minutes)

Level of
sensitivity

20–32

33–47

48–65

F

M

F

M

F

M

114

158

357

272

73

95

0.614

0.685

0.722

0.776

0.652

0.653

False
rate

0.307

0.364

0.363

0.379

0.401

0.395

Pilot trials were performed to gauge the per-
formance of our seizure measuring system in
comparison with video based clinical EEG test-
ing. Table 2 shows the information gathered
from the seizure observations during the pilot
tests. 65% was set as an acceptable sensitivity
factor. The platform tests were satisfactory with
less than 40% a negative false rate and around
11% a positive false rate.

Heart Rate

The observed heart rate information was
compared with the data read by the polar watch
and a bicycle grasp heart rate activity screen.
This was done under four conditions. These
were, while the patient was 1) resting, 2) with
light movement, 3) in direct action, and 4) in
energetic action. The heart rate information
acquired from the sensors clearly indicated the
associated behavior under each condition.

For benchmarking, medically certiﬁed sen-
sors were employed to validate wearable sen-
sors data.
Initially some discrepancies were
found, however, after increasing the sampling
rate to 10 samples/second seems to improve the
performance signiﬁcantly.

The relationship between false alarms and
missed detection depends on the characteristics
of the decision making process. The ideal scenario
would be for both probabilities to be extremely
small.
In the real world this is not possible,
because a reduction in false alarms often leads to
an increase in missed detection and vice-versa.
But we can get close by using an appropriate deci-
sion making rule and the threshold value algo-
rithms according to Neyman–Pearson lemma. The
outcome, however, depends on the probability
density functions of the events under concern.

CONCLUSIONS

In this article, a new WBAN platform utilizing
multiple biomedical sensors was developed for
recording physiological signals to medicinal
applications. The presented WBAN architecture
can be useful in remote patient care.

& REFERENCES

1. E. Jovanov, A. Milenkovic, C. Otto, and P. Groen, “A

wireless body area network of intelligent motion

sensors for computer assisted physical rehabilitation,”

J. Neuro-Eng. Rehabil. vol. 2, no. 6, 2005, Art. no. 6.

2. Wireless Body Area Networks (WBAN) Standard

Group, Mar. 2009, [Online]. Available: http://www.

ieee802.org/15/pub/TG6.html.

3. C. K. Ho and M. R. Yuce, “Low data rate ultra

wideband ECG monitoring system,” in Proc. IEEE Eng.

Med. Biol. Soc. Conf., Aug. 2008, pp. 3413–3416.

4. T. Gao, D. Greenspan, M. Welsh, R. R. Juang, and

A. Alm, “Vital signs monitoring and patient tracking over

a wireless network,” in Proc. IEEE-EMBS 27th Annu. Int.

Conf. Eng. Med. Biol., Sep. 2005, pp. 102–105.

5. A. S. Abiodun, M. Anisi, I. Ali, A. Akhunzada, and

M. Khan, “Reducing power consumption in wireless

body area networks,” IEEE Consum. Electron. Mag.,

vol. 6, no. 10, pp. 38–47, Oct. 2017.

6. E. Jafer, A. S. Mahmoud, S. Hussain, and X. Fernando,

“Wireless body area network development for

connected health care applications,” in Proc. IEEE Int.

Humanitarian Conf., Jul. 2017, pp. 26–31.

7. J. Lockman, R. S. Fisher, and D. M. Olson,

“Detection of seizure-like movements using a

wrist accelerometer,” Epilepsy Behav., vol. 20,

pp. 638–641, 2011.

Essa Jafer is currently a faculty member with the
Department of Electrical Engineering, Princess
Sumaya University for Technology, Amman, Jordan.
Contact him at essajh@gmail.com.

Sattar Hussain is currently a faculty member with
the Department of Information and Communications
Engineering Technology, Centennial College, Scar-
borough, ON, Canada. Contact him at shussa98@my.
centennialcollege.ca.

Xavier Fernando is currently a Professor and
Director of Communications Laboratory, Ryerson
University, Toronto, ON, Canada. Contact him at
fernando@ee.ryerson.ca.

IEEE Consumer Electronics Magazine

106

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:14:29 UTC from IEEE Xplore.  Restrictions apply.
