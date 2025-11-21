# Bonato - 2010 - Wearable Sensors and Systems

MIT Open Access Articles

Wearable Sensors and Systems

The MIT Faculty has made this article openly available. Please share
how this access benefits you. Your story matters.

Citation: Bonato, Paolo. “Wearable Sensors and Systems.” IEEE Engineering in Medicine and 
Biology Magazine 29.3 (2010): 25–36. Web. 30 Mar. 2012. © 2010 Institute of Electrical and 
Electronics Engineers

As Published: http://dx.doi.org/10.1109/MEMB.2010.936554

Publisher: Institute of Electrical and Electronics Engineers (IEEE)

Persistent URL: http://hdl.handle.net/1721.1/69890

Version: Final published version: final published article, as it appeared in a journal, conference 
proceedings, or other formally published context

Terms of Use: Article is made available in accordance with the publisher's policy and may be 
subject to US copyright law. Please refer to the publisher's site for terms of use.

From Enabling Technology to Clinical Applications

BY PAOLO BONATO

Over the past decade, wearable technology has

gained the interest of researchers and clinicians [1].
The motivation for the development of wearable
sensors and systems is due to the tremendous
benefits that could be associated with long-term monitor-
ing of individuals in the home and community settings.
For example, in Figure 1, an individual affected by a
balance disorder is monitored while at the gym or a
clinical center (e.g., undergoing balance training).
Here, exercise compliance and performance are
monitored via motion sensors attached to the
wrists and ankles: the interaction with a parallel-
bar setup is captured by sensorized gloves that
track hand movements, and physiological
responses to the exercise are gathered using a
chest strap that enables monitoring of heart
rate and respiratory rate. The subject carries
a cell phone in his/her pocket, which
serves as data logger (i.e., the cell phone
‘‘talks’’ to the sensors positioned on the
body) and as a gateway for remote
access to the subject’s data. Access to
the subject’s data is achieved via a
cell phone network or via a wireless
local area network. Data are then
relayed via the Internet to emer-
gency personnel (e.g., an ambu-
lance service), a family member
or caregiver, and clinical per-
sonnel
the subject’s
primary care physician) as
needed to respond to emer-
gency situations, assess
the subject’s status, and
plan clinical interventions.

(e.g.,

A Decade
of Development
of Wearable
Technology
Interest in monitoring
individuals in the home
and community settings

Digital Object Identifier 10.1109/MEMB.2010.936554

It could,

is not new and is in fact one of the factors that originated the
field of telemedicine (recently renamed as connected health to
emphasize the link between clinical personnel and patients that
has been made possible by communication technologies
such as the Internet). Researchers believe that long-term
monitoring of physiological data could lead to signif-
icant improvements in the diagnosis and treatment
for
of cardiovascular diseases [2].
instance, overcome shortcomings of currently
available technology (e.g., Holter monitoring),
such as the inability of capturing rarely occur-
ring events of diagnostic relevance. Home
monitoring of movement patterns in patients
with motor disorders also could have a
dramatic impact on the clinical management
of impairing symptoms. For example, moni-
toring the severity of parkinsonian symp-
toms could facilitate medication titration as
the disease progresses, thus minimizing
impairments associated with severe dyski-
nesia, bradykinesia, rigidity, and akinesia.
Researchers envisioned the potential ben-
efits of field monitoring of patients with
Parkinson’s disease since the early
1990s [3], [4]. However, technological
limitations prevented the immediate
clinical application of the method-

ologies proposed.

ble

Starting in the late 1990s, a
tremendous effort has been
made in the field of weara-
technology toward
closing the gap between
vision and reality. Re-
searchers have been
engaged in devel-
oping technolo-
gies to enable the
shared vision that
long-term home
monitoring could
revolutionize the
way medicine is
pra ct i ce d a nd
have focused on

© DIGITAL STOCK

IEEE ENGINEERING IN MEDICINE AND BIOLOGY MAGAZINE

0739-5175/10/$26.00©2010IEEE

MAY/JUNE 2010

25

ECG and Respiration

Location (GPS)
Communication Gateway

Cell Phone Network

Emergency

Cell

Internet

e-Textile
Data Glove

Motion

Bluetooth/WLAN

Family/Caregiver

Clinician

Fig. 1. Schematic representation of a system for patients’ monitoring in the home and community settings. A subject is shown
while exercising at the gym (e.g., undergoing balance therapy). Exercise compliance, exercise performance, and the associ-
ated physiological responses (i.e., heart rate and respiratory rate) are monitored via wearable sensors. A cell phone serves as
a data logger and gateway for communication with a remote location via a cell phone network and/or the Internet.

two major approaches to implement wearable systems. These
two distinct approaches leverage wireless technology and
e-textile solutions, respectively [5]. It could be argued that this
is purely a technology-based distinction and that future clinical
systems will most likely combine wireless and e-textile technol-
ogies according to the requirements of the application at hand.
However, hybrid systems integrating wireless and e-textile

Fig. 2. Schematic representation of a wearable system that
allows one to collect movement and physiological data
(i.e., heart rate and respiratory rate). Movement data are
gathered using the four nodes equipped with accelerome-
ters that are strapped around the ankles and wrists. Physio-
logical data are collected via a chest strap.

technologies still appear to be a futuristic possibility. Research
groups in the field of wearable technology are typically focused
on one technology or the other, since the technical expertise
necessary to develop systems leveraging both technologies
(i.e., wireless and e-textile) are very different and rarely found
in a single research group.

The development of wearable systems based on wireless
technology leverages the miniaturization of sensors, availabil-
ity of low-power radios, and development of dedicated operat-
ing systems (e.g., TinyOS) for small sensor units and networks
of sensor units. Such networks are referred to as body sensor
networks, and the sensor units are referred to as sensor nodes.
A schematic representation of a body sensor network is shown
in Figure 2. In the figure, a SHIMMER unit [6] is displayed as
an example of a sensor node. A subject is depicted with sensor
nodes attached to wrists and ankles, a setup suitable to monitor
major motor activities. A chest strap is used to monitor heart
rate and respiratory rate, thus capturing physiological responses
to motor activities and potential cardiovascular problems that
can be detected, for instance, via analysis of the heart rate and
its variability. The nodes communicate with a base station (not
shown in the figure) that could be either a data logger worn by
the subject or a computer located in the environment surround-
ing the subject.

Advances in sensor technology have been essential to the
implementation of body sensor networks. Researchers have
put a great deal of effort on developing ways to unobtrusively
monitor vital signs, with a particular emphasis on cardiac activ-
ity. Seminal work contributed by the group led by Asada and
coworkers [7], [8] resulted in the ring sensor, a ring-shaped
photoplethysmographic sensor capable of transmitting data
wirelessly to a base station, which provides the ability to moni-
tor heart rate and oxygen in the blood. More recently, Wang et
al. [9] developed an earpiece photoplethysmographic sensor
that has light-emitting diodes and photodiodes positioned

26

IEEE ENGINEERING IN MEDICINE AND BIOLOGY MAGAZINE

MAY/JUNE 2010

Home monitoring of movement patterns in
patients with motor disorders also have a

dramatic impact on the clinical management

of impairing symptoms.

around the outer ear—as opposed to being attached to the ear-
lobe as are commercially available photoplethysmographic
sensors—thus leading to improved comfort. Also, Vogel et al.
[10] developed an in-ear sensor suitable to record heart rate
and, in the future, oxygen in the blood. Unobtrusive blood pres-
sure monitoring has also been the focus of significant research
efforts. Wristwatch type monitors, such as the MediWatch
[11], were first developed by leveraging the miniaturization of
sensors based on traditional approaches to measure blood pres-
sure (i.e., via blood flow temporary obstruction). More
recently, researchers have focused their work in this field on
the pulse transit time technique [12], [13]. The technique lever-
ages the relationship between blood pressure and the time
between the R-peak of the electrocardiogram and a peak identi-
fied on the photoplethysmogram. Furthermore, researchers
interested in tracking patients’ movement patterns have been
relying on the advances that have marked the field of micro-
electromechanical systems over the past two decades. Thanks
to the progress in this field, sensors like accelerometers, gyro-
scopes, and magnetometers are now available that meet the
requirements (e.g., low power consumption) for use as part of a
body sensor network. Using this technology, researchers and
clinicians can currently monitor subjects’ movement patterns
and possibly even reconstruct movement trajectories [14].
Advances in sensor technology have been combined with
progress in short-range communication technologies such as
ultrawideband radio technology [15], Bluetooth [16], and
ZigBee [17] that have enabled the implementation of body sen-
sor networks. Seminal work in this field by Jovanov et al. [17]
has been followed by extensive work toward the development
of strategies aimed at optimizing the scarce resources available
on the nodes of body sensor networks [18]. This latter work has
required the development of operating systems specifically
designed for body sensor networks.

Advances in e-textile research have paralleled the vast
achievements in body sensor networks. Seminal work in this
area was performed at Georgia Tech, where researchers devel-
oped the Wearable Motherboard or Smart Shirt [19]–[21]. The
concept pursued by researchers at Georgia Tech, led by Jayara-
man, was one of transforming the clothing items into an equiva-
lent of a computer bus by attaching sensors, for example, to an
undergarment that could communicate with a data logger posi-
tioned on the subject (e.g., at waist level). This concept led to
different implementations and, eventually, commercially avail-
able products. An example of a research platform of this type is
shown in Figure 3(a), which is developed by Wade and Asada
[22]. In this implementation, traditional sensor technology is
embedded in special buttons that carry sensor technology and
that clip onto the fabric in a way that allows an electrical connec-
tion with a data logger positioned at waist level via the garment.
The layers of the garment provide electrical characteristics that

allow one to use the garment itself as a modem line, thus provid-
ing a means to send data from the sensors to the data logger.

Others have attempted the actual development and integration
of sensing elements into garments using new materials and tech-
niques to integrate sensors and fabric. De Rossi’s group has pro-
vided a unique contribution in this field [23], [24]. Figure 3(b)
shows an example of a technology developed in his laboratory.
Conductive elastomers are printed on a lycra shirt and provide a
means to monitor movements of shoulder and elbow. The
method leverages changes in resistance of the sensing elements
that occur as they are stretched or released during the movement
of body segments. Such changes are detected using a circuitry
that injects a small constant current into the sensing elements and
by means of a dedicated high-impedance amplification unit that
reads changes in voltage drop on the sensing elements that are
associated with changes in their resistance. Current research
focuses on the implementation of a new generation of textile sen-
sors [24]. These new technologies are expected to allow one to
seamlessly record electrocardiogram data, monitor respiratory
rate, track changes in blood oxygenation, and monitor sweat rate.
Wireless and e-textile technologies are now integrated into
wearable systems that fulfill the promise of subjects’ long-
term monitoring in the home and community settings.
Researchers are relying on data loggers with advanced com-
munication capabilities (such as Internet tablets and smart-
phones) to gather data from wearable sensors and relay
clinical information to a remote location [25]–[27]. Although
technical problems still hamper the deployment of these sys-
tems (e.g., difficulties managing the resources of smartphones
thus leading to rapidly depleting the phone battery), this is a
fast evolving field that has shown incredible transformations
over the past few years, and therefore, it is anticipated that
these issues will be soon addressed. Among others, the devel-
opment of open-source smartphone platforms promises to
make available to researchers and developers an array of tools
that will likely result into suitable solutions for an effective
integration of smartphones into wearable systems.

The body of work summarized earlier is by no means a com-
plete review of the advances that we have witnessed over the
past decade in the field of wearable sensors and systems. How-
ever, it provides an overview of the efforts and results achieved
by researchers in the field of wearable technology toward
developing systems that are suitable for clinical applications. In
the past, lack of suitable platforms for unobtrusive long-term
monitoring of individuals in the home and community settings
hindered the application of wearable technology to concrete
clinical problems. Advances achieved in this field over the past
decade have made available to researchers and clinicians the
tools needed to pursue clinical studies. As a consequence, we
are currently witnessing a flourishing of research efforts
focused on assessing the use of wearable sensors and systems to

IEEE ENGINEERING IN MEDICINE AND BIOLOGY MAGAZINE

MAY/JUNE 2010

27

Current research focuses on the
implementation of a new generation

of textile sensors.

prevent diseases, promptly respond to emergency situations,
and optimally manage chronic diseases. This is expected to be
the focus of the field for the next five to ten years. Preliminary
results summarized later suggest that major clinical applica-
tions of wearable technology are just around the corner.

Shifting the Focus on Clinical Applications
Clinical applications enabled by wearable systems can be
categorized according to how their design addresses the three
main challenges inherent in monitoring individuals in the
home and community settings. These challenges are captured
by the following three questions.
1) How critical

is the information to be gathered and

relayed by the wearable system?

2) How long will the subject wear the system and during

performance of what type of motor activities?

3) How quickly will it be necessary to relay the information

gathered by the wearable system to a remote site?

These questions work to define how applications of weara-
ble technologies have been pursued in the recent past and are
currently pursued with renewed effort, thanks to the advances
in wearable sensors and systems described earlier. Knowing
whether the information gathered via wearable systems is
critical to the management of emergency situations or to the
prevention and diagnosis of diseases has somewhat deter-
mined the level of comfort of researchers and developers in
the private sector in pursuing related applications. When criti-
cal information needs to be recorded and potentially processed
by the system, developers must use stringent criteria for the
assessment of the reliability of the data. They also need to con-
sider the liability of the company manufacturing the wearable
system. It follows that research and development activities
focused on these applications proceed slowly compared with
research and development activities that address applications
handling information that is not as critical. How long a subject
needs to wear the system to gather relevant information also

(a)

(b)

Fig. 3. Examples of e-textile technologies developed over the past ten years. (a) A system developed by Wade and Asada
[22] relying upon special buttons that carry sensor technology to record physiological and movement data. (b) A system
developed by De Rossi’s research team [23] for monitoring the movements of the shoulder and elbow via recordings of the
voltage drop on conductive elastomers that are printed on the garment. (Figures used with permission.)

28

IEEE ENGINEERING IN MEDICINE AND BIOLOGY MAGAZINE

MAY/JUNE 2010

The development of open-source smart phone
platforms promises to make available to

researchers and developers an array of tools

that will likely result into suitable solutions for an

effective integration of smart phones into

wearable systems.

appears to be a determinant factor in making a decision about
pursuing the applications of wearable technology. The longer
a subject has to be monitored, the more stringent will be the
specifications concerning unobtrusiveness of the system and
its wearability. Consequently, the first applications research-
ers have focused their attention on require only sporadic data
sampling. In other terms, the system is donned and doffed as
needed but not used for continuous monitoring 24 hours a day,
7 days a week.

Similarly, the type of activity individuals are engaged in
significantly affects the system requirements. For instance, if
subjects are monitored while exercising, the quality of physio-
logical data gathered by the wearable system will be a concern,
because movement artifacts so often negatively affect the qual-
ity of physiological signals. Finally, applications in which criti-
cal information must be gathered by the wearable system and
used to generate alarm messages for immediate response to a
life-threatening situation present challenges that only complex
systems that have undergone extensive testing can meet. The
full development of such systems is yet to come, as only
recently reliable technologies that meet the specifications of
this type of monitoring have been made available.

These considerations justify the initial focus of researchers
and developers in the field of wearable sensors and systems on
wellness [28]–[30] and activity monitoring [31]–[36]. Figure 4
schematically represents a common application of wearable
technology in this context. In the figure, a runner’s heart rate,
respiratory rate, and motion are monitored using wearable sen-
sors. A cell phone provides data-logging capability and connec-
tivity. Commercially available systems already provide the
capability shown in Figure 4, including the ability to locate the
subject via solutions based on a global positioning system. This
ability enables a runner to follow his/her position on a running
course via a display unit mounted on the wrist and to compare
performance from one day to another while running or after
completing the running course. Wearable solutions are also
used by runners to pace themselves by playing suitable music
using an MP3 device wirelessly connected to sensors embedded
in the subject’s shoes that also track his/her pace.

Wellness applications of the type described earlier should
not be dismissed as mere gizmos. They have, in fact, a great
potential to increase exercise compliance in populations at
risk. Obesity management is an example where application of
wearable systems that support wellness could be implemented
[37]–[40]. It is well known that we face an obesity epidemic
and that the weight management industry is a huge business
that delivers very limited results. More effective tools are
required in the fight against obesity, and wearable sensors and

systems have the potential to provide new tools to support and
encourage healthy choices. For example, smartphones and
software applications can be designed to display activity pro-
files comparing target levels and actual levels of activity as
assessed via processing data gathered using wearable sensors.
Subjects could then be encouraged to increase their activity
level via presentation of this type of information on the smart-
phone display. Furthermore, the use of a global positioning
system and contextual information (e.g., the time of the day
and the proximity to a cafeteria) would trigger positive mes-
sages about decreasing calorie intake by suggesting healthy
nutritional choices. The potential impact of tools of this type
on preventing diseases and chronic conditions such as diabetes
and cardiovascular diseases is significant, and current research
continues to make positive strides in this direction.

Paralleling the progress in wearable technology, applica-
tions gradually shifted their focus toward medical problems
that require enhanced reliability compared with systems
designed for wellness applications. Monitoring patients with
Parkinson’s disease to improve clinical management of symp-
toms is an example of one such type of application. Currently,
clinical visits are inadequate to sample the severity of parkin-
sonian symptoms, because symptoms vary in response to a
medication dosage with a time constant of hours, a time inter-
val that does not lend itself to direct patient observation by

ECG
Respiration

Motion
SpO2

Motion

Cell

Fig. 4. An important application of wearable technology
consists of monitoring individuals while they exercise. The
focus here is on wellness/fitness monitoring, with the poten-
tial development of methodologies to improve exercise
compliance. Wearable sensors allow one to monitor move-
ment, respiratory rate, and heart rate. ECG: electrocardio-
graphic recordings; SpO2: oxygen saturation.

IEEE ENGINEERING IN MEDICINE AND BIOLOGY MAGAZINE

MAY/JUNE 2010

29

Advances achieved in this field over the past
decade have made available to researchers

and clinicians the tools needed to pursue

clinical studies.

clinical personnel. Furthermore, patients do not have an objec-
tive perception of their own motor status, and thus they cannot
report reliably about the severity of their symptoms and their
response to a medication adjustment. Patients often mix up
symptoms (e.g., tremor and dyskinesia) that require opposite
adjustments in medication intake.

Wearable technology has the potential for addressing these
problems by providing a means of gathering objective
measures of the severity of symptoms over a period of time
sufficient, for instance, to reliably assess the effectiveness of
medication adjustments. Seminal work by Ghika et al. [3] and
Spieker et al. [4] exploring the use of sensor technology to
capture the severity of parkinsonian symptoms was followed
by the work by Keijsers et al. [41]–[43] aimed at assessing the

effectiveness of medications in attenuating the severity of
symptoms using wearable sensors. More recent research has
been focused on integrating and further developing these tech-
niques into complete wearable systems for home monitoring
of patients with Parkinson’s disease [44]–[46]. We anticipate
that home monitoring of patients with Parkinson’s disease will
be integrated in the near future with remote assessment tools
leveraging videoconferencing and remote access to sensor
data to facilitate clinical evaluation of the severity of parkinso-
nian symptoms. Figure 5 shows a software application recently
developed by Matt Welsh’s research team and my research
team (supported by the Michael J. Fox Foundation) as part of a
joint effort toward the development of Web-based applications
devoted to the collection of data from patients with Parkinson’s

Fig. 5. Home-monitoring applications would often benefit from technology for remote examination of patients. The screen cap-
ture presented shows the graphical interface of an application recently developed by Matt Welsh’s research team at Harvard
University to monitor patients with Parkinson’s disease in the home. The software application provides clinicians with access to
wearable sensor data and measures the severity of parkinsonian symptoms [45].

30

IEEE ENGINEERING IN MEDICINE AND BIOLOGY MAGAZINE

MAY/JUNE 2010

Obesity management is an example where
application of wearable systems that support

wellness could be implemented.

disease in a home environment. The system integrates wearable
technology and advanced signal processing algorithms to rele-
vant information gathered to determine whether a medication
adjustment is needed. The project has the overall objective of
facilitating clinical management of parkinsonian symptoms in
patients at the late stages of the disease.

The screenshot shown in Figure 5 is the software interface
for personnel overseeing the remote clinical evaluation of a
patient with Parkinson’s disease. The session in Figure 5 is
a simulation in which a subject posing as a clinician instructs a
subject posing as a patient to perform motor tasks associated
with the motor section of the Unified Parkinson’s Disease Rat-
ing Scale, a clinical scale designed to assess the severity of
parkinsonian symptoms [47]. Data gathered using a body sen-
sor network are collected by a laptop computer (the patient’s
workstation) and relayed to the clinical site via the Internet.
As the display of data on the clinician’s computer screen
occurs online, the clinician has the opportunity to spot-check
the quality of data gathered during the session.

Similar applications have been pursued to monitor cardio-
vascular diseases such as congestive heart failure, which
requires long-term monitoring of patients to detect worsening
of patient status, and to set in place prompt interventions that
might prevent hospitalization [48]–[50]. It is worth emphasiz-
ing that these applications can be seen as fulfilling the vision
that led to the proposal of Holter monitoring in the late 1940s
and its clinical adoption in the 1960s. Although Holter moni-
tors have provided an invaluable tool to diagnose cardiovascu-
lar diseases over the past 50 years it could be argued that only
by leveraging wearable technology can the vision that origi-
nated Holter monitoring be fully implemented.

While applications described earlier have significant poten-
tial clinical impact, they still fall within a group of applica-
tions that do not require prompt interventions in response to
an emergency situation that would be detected based on the
analysis of data gathered using the wearable system. In other
these applications are designed around a clinical
words,
response with a relatively long time constant, namely, a few
days. However, a new set of clinical applications of wearable
systems is currently emerging that requires either a response
within a few hours or an immediate clinical response, as sen-
sor data gathered in such applications are meant to detect
emergency situations. Applications that fall in this category
include monitoring patients with chronic obstructive pulmo-
nary disease to achieve early detection of exacerbation epi-
the
sodes, monitoring patients with epilepsy to detect
occurrence of seizures, and monitoring individuals to detect
and potentially prevent sudden cardiac arrest. These are all
applications of great relevance because of the potential-related
improvement of patients’ quality of life and because of the
significant potential impact on the society at large.

In patients with chronic obstructive pulmonary disease,
early detection of exacerbation episodes would break the
downward spiral that characterizes these patients who worsen
every time they experience an exacerbation episode—a wor-
sening from which they never fully recover—leading to a
progressive decline of their clinical status. In patients with epi-
lepsy, the detection of seizure events could potentially prevent
severe accidents and even death if the patient falls uncon-
scious and clinical care is not provided promptly. In individu-
als at risk of sudden cardiac arrest, continuous monitoring of
heart rate could provide a means to guarantee that clinical care
is immediately provided if the heart suddenly stops beating.

The applications of wearable sensors and systems summar-
ized in this section demonstrate the potential of this technol-
ogy for achieving prevention and diagnosis of several diseases
and for optimally managing chronic conditions. Some of these
applications, specifically those related to wellness manage-
ment, have already led to commercially available systems.
More challenging clinical applications such as the use of
wearable sensors and systems to facilitate the titration of med-
ications in chronic conditions (e.g., Parkinson’s disease) are
bound to become clinical tools within a few years. The need
for high reliability of the system, as required by clinical appli-
cations with a focus on providing an alarm that guarantees
prompt interventions in response to emergency situations, still
requires both technology development and clinical testing.
New trends merging wearable technology and robotics appear
to have the potential for opening the way toward improved
home interventions and achieving higher reliability in the
detection of emergency situations.

New Trends: Integrating
Wearable Technology and Robots
The combination of wearable technology and robots is a very
recent development in the field of wearable sensors and sys-
tems [51], [52]. Interest in this approach originates from the
observation that subjects with chronic conditions (such as
hemiparesis following a stroke) could benefit from therapeutic
interventions that can be facilitated by robotic systems and
enhanced by wearable technology. Figure 6 provides an exam-
ple of how robotic and wearable technologies can be combined
to deliver therapeutic interventions. In the simulated clinical
session shown in Figure 6, a subject is posing as a patient with
hemiparesis undergoing therapy. An exoskeleton-type system
provides support to the hemiparetic arm, thus facilitating the
performance of movements. The position of the exoskeleton is
tracked using sensors embedded in the device. The output of
the tracking algorithm is used to play video games designed to
encourage the patient to perform motor tasks such as reaching
and grasping/retrieving objects. Performance of these motor
tasks is known to have positive therapeutic effects when

IEEE ENGINEERING IN MEDICINE AND BIOLOGY MAGAZINE

MAY/JUNE 2010

31

New trends merging wearable technology
and robotics appear to have the potential for

opening the way toward improved home

interventions and achieving higher reliability

in the detection of emergency situations.

subjects perform a high number of movement repetitions. A
sensorized glove is used to track hand grasp/release move-
ments, thus providing a platform for the implementation of
exercises focused on the recovery of hand function.

The aforementioned approach is expected to benefit sub-
jects undergoing physical therapy to recover arm and hand
functions. The combination of wearable technology (i.e., the
sensorized glove) and robotics allows one to improve the qual-
ity of the intervention. The robot alone does not lend itself to
the implementation of therapeutic exercises that focus on hand
function, an aspect of physical therapy that is known to be of
paramount importance when one aims at achieving recovery
of the subject’s functional capability. The sensorized glove is
therefore a key factor in improving the clinical intervention in
the presented application scenario. Patients that are candidates
for the use of these technologies include individuals who have
suffered a stroke, a traumatic brain injury, or experienced
other neurological problems leading to impairments and func-
tional limitations of the upper limbs.

It is important to note that traditional physical therapy tech-
niques could theoretically lead to similar results to the ones
expected from robotic therapy (although recent research sug-
gests that robotic therapy leveraging interactive games leads
to better results than therapeutic interventions simply based
on delivering a high number of repetitions of specific move-
ments [53]). However, the intensity of the exercise that has
been shown to benefit patients when robotics is relied upon
cannot be achieved in the current health-care system model
by means of traditional interventions based on manual ther-
apy administered by clinical personnel in a one-to-one ratio
with patients (i.e., with one therapist working with a single
patient at a time). This is because the number of physical ther-
apy sessions that are reimbursed by insurance companies is
limited. Also, it must be observed that a higher number of
movement repetitions can be achieved within a single session
using robotics compared with traditional therapeutic inter-
ventions. In this context, wearable technology provides a
means to enhance available rehabilitation robotic platforms

Fig. 6. Rehabilitation robotics is combined with wearable technology for the purpose of enhancing functions that are not pro-
vided by robotic systems [51]. Features provided by commercially available robotic systems like the one shown in this figure
(Armeo by Hocoma AG) can be augmented via the use of wearable sensors. In the example presented, a sensorized glove
provides the system with the ability to implement exercises targeting the recovery of hand function. This capability would not
be available if the robot were to be used alone.

32

IEEE ENGINEERING IN MEDICINE AND BIOLOGY MAGAZINE

MAY/JUNE 2010

The use of off-the-shelf interactive gaming
systems is very attractive in the context of

implementing home interventions, but

commercially available systems lack the ability

of monitoring movement patterns in a way

that is satisfactory from a rehabilitation

intervention standpoint.

that lack adequate focus on exercises devoted to the recovery
of hand function.

The future of these technologies is in the home. Home-care
services would oversee the use of systems like the one
described earlier implemented in a home setting. During their
visits, therapists would instruct patients on the correct ways to
perform therapeutic exercises using the robot and combined
wearable technology. Patients would exercise using interactive
games that rely on the hardware provided by the home-care
service. Data concerning exercise compliance and performance
would be logged by the system for later review by the therapist
and patient. The data would also be relayed to a clinical center
for monitoring purposes so that immediate action can be taken
if necessary (e.g., a telerehabilitation session could be set up if
inappropriate patterns of movement are observed via review of
data collected during performance of a home-exercise session).
In addition to improving the effectiveness of interventions
by combining rehabilitation robots and wearable technology,
one can think of a number of other applications that would
be facilitated by the deployment of robotic and wearable tech-
nologies in the home. Major changes could rapidly occur in
the field if home robots were combined with wearable technol-
ogy, as schematically represented in Figure 7. In this example,
a wearable sensor suit is used to monitor movement and physio-
logical data [Figure 7(a)], and the suit communicates wirelessly
with a home robot [Figure 7(b)]. The figure shows a picture of
the iRobot ConnectR (courtesy of iRobot). This system has fea-
tures including a Web camera and Internet capability. In this
way, leveraging wearable technology and home robots could
have a dramatic impact in the field of clinical home monitoring.
Additionally, Figure 8 shows a range of clinical applications
that could be pursued if one leveraged home robots and weara-
ble technology. The platform depicted in Figure 8 is complex
and relies upon a combination of wearable sensors, home robots,
interactive gaming, and other technologies (e.g., cell phone and
Internet tablet) to develop a connected health application for
patients with balance disorders. The system assesses fall risk via
monitoring stride variability, facilitates interventions delivered
using interactive gaming systems, and detects falls via the com-
bined use of wearable sensors and a home robot.

Methods for the assessment of fall risk based on the varia-
bility of gait that have been proposed in recent years [54], [55]
could be implemented using the platform shown in Figure 8.
Wearable sensors attached to the ankles would allow one to
detect foot strike events and estimate stride-to-stride varia-
tions in the duration of the gait cycle. The platform shown in

Figure 8 would also provide connectivity with interactive
gaming systems like the Nintendo Wii. Physical and occupa-
tional therapists have demonstrated a growing interest in the
use of off-the-shelf interactive gaming systems as a tool that
complements traditional clinical interventions. The use of off-
the-shelf interactive gaming systems is very attractive in the
context of implementing home interventions, but commer-
cially available systems lack the ability of monitoring move-
ment patterns in a way that is satisfactory from a rehabilitation
intervention standpoint. While using interactive gaming sys-
tems, subjects must be encouraged to use appropriate motor
control strategies (rather than compensatory mechanisms). In
the scenario shown in Figure 8, the system would provide
appropriate feedback during the performance of home exer-
cises, based on the analysis of data recorded using wearable
sensors. The sensors would be used to monitor movement pat-
terns, and a home robot would be relied upon to convey feed-
back to the individual. Finally, wearable sensors and home

(a)

(b)

Fig. 7. It is envisioned that combining (a) wearable technol-
ogy and (b) home robots will result in novel home-monitor-
ing applications. Wearable sensors will communicate
wirelessly with home robots (image courtesy of iRobot) that
will in turn respond to alarm messages using onboard capa-
bilities (i.e., image processing) to interact with the patient
and assess the severity of the situation.

IEEE ENGINEERING IN MEDICINE AND BIOLOGY MAGAZINE

MAY/JUNE 2010

33

robotics would be combined to achieve prompt detection of
falls in the home environment. A key factor in minimizing the
severity of fall-related injuries is to promptly detect the fall
event and alert clinical personnel. During the past decade, a
number of devices for fall detection have been developed by
researchers [56]–[60], and fall-detection devices have been
introduced on the market. These systems are typically based
on body-worn units (e.g., pendants and wrist straps) equipped
with an accelerometer. The units are programmed to detect
falls based on the analysis of accelerometer data and to send
an alarm message to a caregiver. Unfortunately, the potential
benefit of these systems is limited by poor compliance,
because subjects are overwhelmed by the large number of
false detections of falls (i.e., false positives) that mark existing
systems. This is somehow inevitable because fall-detection
systems have to be extremely sensitive to the occurrence of a
fall. To achieve high sensitivity, low specificity (i.e., high rate
of false detections) has to be tolerated. In the system shown in
Figure 8, a home robot is combined with the use of a body-
worn unit to minimize the number of false positives. The
body-worn unit sends a message to the robot when the unit
detects a fall. The robot responds by using a combination of
video processing and human–robot interaction techniques to
assess whether the subject actually fell. If the robot determines
that the subject fell or if it cannot determine whether the

individual fell, it alerts a caregiver. The caregiver has the abil-
ity of teleoperating the robot to determine if the individual fell,
and if so, how urgently is attention to the situation required.
This approach based on assessing potential fall events with a
home robot has the potential to significantly improve the
effectiveness of fall-detection systems. By autonomously
eliminating a large number of false positives and allowing for
a rapid assessment of the severity of true positives, the system
allows precious human care-giving resources to be deployed
in the most efficient and effective manner.

It is worth noting that the combination of home robots and
wearable technology is somewhat complementary to installing
sensing components in living environments [61]. Although
some applications might be better served by sensing compo-
nents installed in the home [62], [63], the use of home robots
has a significant potential for decreasing costs and mitigating
the level of obtrusiveness of the monitoring system. It is
known that robots are often perceived by people as pets.
Therefore, one would expect that a home robot would be more
easily accepted than a set of Web cameras positioned in all the
rooms of the home. Home robots are also easier to control, and
they provide the assurance that privacy is not violated. For
instance, the camera positioned on the robot can be easily
flipped so that the lens does not face the subject, thus reassur-
the privacy is not violated even by
ing individuals that

Alerts

Fig. 8. Complex systems under development will soon provide enhanced monitoring capability, the ability to facilitate clinical
interventions, and features that are suitable for detecting emergency situations, assess needs (e.g., via gathering images
and other information using a home robot), and alert a remote clinical center when necessary.

34

IEEE ENGINEERING IN MEDICINE AND BIOLOGY MAGAZINE

MAY/JUNE 2010

mistake. Besides, remote control of home robots provides a
flexibility of interaction with the monitored individual which
is virtually impossible to achieve using sensing components
(including Web cameras) installed in the home environment.
It follows that home robots, alone or in combination with a
limited set of sensors embedded in the home environment,
have the potential to achieve effective monitoring of individu-
als in a rather unobtrusive way and with very limited likeli-
hood of generating privacy concerns.

In summary, platforms combining home robots and wearable
systems could be used in a variety of home-monitoring applica-
tions ranging from the detection of seizures in patients with epi-
lepsy [64] to the detection of cardiac arrest in patients undergoing
cardiac monitoring [65]. Emergency situations would be detected
via online processing of data gathered by wearable sensors, and
an alarm message would be sent to the home robot. The robot
would wake up (if it is in standby mode at the time it receives the
alarm message) and check upon the patient’s condition. The sys-
tem would provide high detection sensitivity without the draw-
back of requiring human intervention every time a false-positive
detection occurs. Connected health software applications would
further enhance the platform by assuring that qualified clinical
personnel are promptly put in touch with the patient when he/she
needs it the most, i.e., during an emergency situation. Therefore,
this type of platform could have a significant impact on our abil-
ity to clinically manage long-term conditions associated with
impairments and functional limitations that compromise the indi-
viduals’ quality of life.

Conclusions
It is now more than 50 years since the time when clinical mon-
itoring of individuals in the home and community settings was
first envisioned. Until recently, technologies to enable such
vision were lacking. However, wearable sensors and systems
developed over the past decade have provided the tools to
finally implement and deploy technology with the capabilities
required by researchers in the field of patients’ home monitor-
ing. As discussed, potential applications of these technologies
include the early diagnosis of diseases such as congestive
heart failure, the prevention of chronic conditions such as dia-
betes, improved clinical management of neurodegenerative
conditions such as Parkinson’s disease, and the ability to
promptly respond to emergency situations such as seizures in
patients with epilepsy and cardiac arrest in subjects under-
going cardiovascular monitoring.

Current research efforts are now focused on the development
of more complex systems for home monitoring of individuals
with a variety of preclinical and clinical conditions. Recent
research on the clinical assessment of wearable technology
promises to deliver methodologies that are expected to lead to
clinical adoption within the next five to ten years. In particular,
combining home robots and wearable technology is likely to be
a key step toward achieving the goal of effectively monitoring
patients in the home. These efforts to merge home robots and
wearable technology are expected to enable a new generation
of complex systems with the ability to monitor subjects’ status,
facilitate the administration of interventions, and provide an
invaluable tool to respond to emergency situations.

Acknowledgments
The author expresses his gratitude to his associates and col-
laborators for the discussions and collaborative work that

originated this manuscript. Special
thanks go to Fabrizio
Cutolo, Anthony Dalton, Todd Hester, Richard Hughes, Chiara
Mancinelli, Shyamal Patel, and Delsey Sherrill who worked on
projects focused on wearable technology in the author’s labora-
tory. Sincere thanks also go to Bryan Adams, Metin Akay,
Harrry Asada, Danilo De Rossi, John Growdon, Holly Jimison,
Nancy Huggins, Emil Jovanov, Rita Paradiso, Doug McClure,
Misha Pavel, Marilyn Moy, Steve Schachter, Ludy Shih, Joel
Stein, David Standaert, Alessandro Tognetti, Eric Wade, and
Matt Welsh who collaborated with the author on projects
related to the development and deployment of wearable
technology. The author also expresses his appreciation to Pat-
rick Kasi and Mel Meister for their technical support.

Paolo Bonato received his M.S. degree in
electrical engineering from Politecnico di
Torino, Turin, Italy, in 1989 and Ph.D.
degree from the Universita` di Roma La
Sapienza in 1995. He is an assistant profes-
sor in the Department of Physical Medi-
cine and Rehabilitation, Harvard Medical
School, Boston, Massachusetts, and a
member of the affiliated faculty of Harvard–Massachusetts
Institute of Technology Division of Health Sciences and
Technology, Cambridge, Massachusetts. He serves as a direc-
tor of Motion Analysis Laboratory, Spaulding Rehabilitation
Hospital, Boston, Massachusetts. He is an elected member of
the IEEE Engineering in Medicine and Biology Society
(EMBS) Administrative Committee and president of the
International Society of Electrophysiology and Kinesiology.
He served as a chair of the IEEE EMBS Technical Committee
on Wearable Biomedical Sensors and Systems in 2008 and
has been a member of this committee since its inception in
2006. He is the founding and current editor-in-chief of Jour-
nal on NeuroEngineering and Rehabilitation and associate
editor of IEEE Transactions on Information Technology in
Biomedicine. He is a Senior Member of the IEEE. His
research interests focus on rehabilitation technology, with an
emphasis on wearable technology and robotics.

Address for Correspondence: Paolo Bonato, Department of
Physical Medicine and Rehabilitation, Harvard Medical
School, Spaulding Rehabilitation Hospital, 125 Nashua Street,
Boston, MA 02144 USA. E-mail: pbonato@partners.org.

References
[1] P. Bonato, ‘‘Wearable sensors/systems and their impact on biomedical engi-
neering,’’ IEEE Eng. Med. Biol. Mag., vol. 22, pp. 18–20, May–June 2003.
[2] P. F. Binkley, ‘‘The next era of examination and management of the patient with car-
diovascular disease,’’ IEEE Eng. Med. Biol. Mag., vol. 22, pp. 23–24, May–June 2003.
[3] J. Ghika, A. W. Wiegner, J. J. Fang, L. Davies, R. R. Young, and J.
H. Growdon, ‘‘Portable system for quantifying motor abnormalities in Parkinson’s
disease,’’ IEEE Trans. Biomed. Eng., vol. 40, pp. 276–283, Mar. 1993.
[4] S. Spieker, C. Jentgens, A. Boose, and J. Dichgans, ‘‘Reliability, specificity
and sensitivity of long-term tremor recordings,’’ Electroencephalogr. Clin. Neuro-
physiol., vol. 97, pp. 326–331, Dec. 1995.
[5] X.-F. Teng, Y.-T. Zhang, C. C. Y. Poon, and P. Bonato, ‘‘Wearable medical
systems for p-Health,’’ IEEE Rev. Biomed. Eng., vol. 1, pp. 62–74, 2008.
[6] SHIMMER [Online]. Available: http://docs.tinyos.net/index.php/SHIMMER
[7] S. Rhee, B. H. Yang, and H. H. Asada, ‘‘Artifact-resistant power-efficient
design of finger-ring plethysmographic sensors,’’ IEEE Trans. Biomed. Eng.,
vol. 48, pp. 795–805, July 2001.
[8] H. H. Asada, P. Shaltis, A. Reisner, S. Rhee, and R. C. Hutchinson, ‘‘Mobile
monitoring with wearable photoplethysmographic biosensors,’’ IEEE Eng. Med.
Biol. Mag., vol. 22, pp. 28–40, May–June 2003.
[9] L. Wang, B. P. L. Lo, and G. Z. Yang, ‘‘Multichannel reflective PPG earpiece
sensor with passive motion cancellation,’’ IEEE Trans. Biomed. Circuits Syst.,
vol. 1, no. 4, pp. 235–241, 2007.

IEEE ENGINEERING IN MEDICINE AND BIOLOGY MAGAZINE

MAY/JUNE 2010

35

[10] S. Vogel, M. Hulsbusch, T. Hennig, V. Blazek, and S. Leonhardt, ‘‘In-ear
vital signs monitoring using a novel microoptic reflective sensor,’’ IEEE Trans.
Inf. Technol. Biomed., vol. 13, no. 6, pp. 882–889, 2009.
[11] K. G. Ng, C. M. Ting, J. H. Yeo, K. W. Sim, W. L. Peh, N. H. Chua,
N. K. Chua, and F. Kwong, ‘‘Progress on the development of the MediWatch
ambulatory blood pressure monitor and related devices,’’ Blood Press. Monit.,
vol. 9, pp. 149–165, June 2004.
[12] C. C. Poon and Y. T. Zhang, ‘‘Cuff-less and noninvasive measurements of
arterial blood pressure by pulse transit time,’’ Conf. Proc. IEEE Eng. Med. Biol.
Soc., vol. 6, pp. 5877–5880, 2005.
[13] M. Y. Wong, C. C. Poon, and Y. T. Zhang, ‘‘An evaluation of the cuffless
blood pressure estimation based on pulse transit time technique: A half-year study
on normotensive subjects,’’ Cardiovasc. Eng., vol. 9, pp. 32–38, Mar. 2009.
[14] D. Roetenberg, H. J. Luinge, C. T. Baten, and P. H. Veltink, ‘‘Compensation
of magnetic disturbances improves inertial and magnetic sensing of human body
segment orientation,’’ IEEE Trans. Neural Syst. Rehabil. Eng., vol. 13, pp. 395–
405, Sept. 2005.
[15] W. Hirt, ‘‘Ultra-wideband radio technology: Overview and future research,’’
Comput. Commun., vol. 26, no. 1, pp. 46–52, 2003.
[16] M. F. Rasid and B. Woodward, ‘‘Bluetooth telemedicine processor for multi-
transmission via mobile cellular networks,’’ IEEE
channel biomedical signal
Trans. Inf. Technol. Biomed., vol. 9, pp. 35–43, Mar. 2005.
[17] E. Jovanov, A. Milenkovic, C. Otto, and P. C. De Groen, ‘‘A wireless body
area network of intelligent motion sensors for computer-assisted physical rehabili-
tation,’’ J. Neuroeng. Rehabil., vol. 2, p. 6, Mar. 1, 2005.
[18] K. Lorincz, B. R. Chen, G. W. Challen, A. R. Chowdhury, S. Patel,
P. Bonato, and M. Welsh, ‘‘Mercury: A wearable sensor network platform for
high-fidelity motion analysis,’’ in Proc. 7th ACM Conf. Embedded Networked
Sensor Systems (SenSys’09), Berkeley, CA, 2009, pp. 183–196.
[19] S. Park, C. Gopalsamy, R. Rajamanickam, and S. Jayaraman, ‘‘The Wearable
Motherboard: A flexible information infrastructure or sensate liner for medical
applications,’’ Stud. Health Technol. Inform., vol. 62, pp. 252–258, 1999.
[20] S. Park and S. Jayaraman, ‘‘Enhancing the quality of life through wearable
technology,’’ IEEE Eng. Med. Biol. Mag., vol. 22, pp. 41–48, May–June 2003.
[21] S. Park and S. Jayaraman, ‘‘e-Health and quality of life: The role of the Weara-
ble Motherboard,’’ Stud. Health Technol. Inform., vol. 108, pp. 239–252, 2004.
[22] E. Wade and H. Asada, ‘‘Cable-free body area network using conductive fab-
ric sheets for advanced human–robot interaction,’’ Conf. Proc. IEEE Eng. Med.
Biol. Soc., vol. 4, pp. 3530–3533, 2005.
[23] A. Tognetti, F. Lorussi, R. Bartalesi, S. Quaglini, M. Tesconi, G. Zupone,
and D. De Rossi, ‘‘Wearable kinesthetic system for capturing and classifying
upper limb gesture in post-stroke rehabilitation,’’ J. Neuroeng. Rehab., vol. 2,
no. 8, pp. 1–16, 2005.
[24] S. Coyle, K. T. Lau, N. Moyna, D. Diamond, F. Di Francesco, D. Constanzo,
P. Salvo, M. G. Trivella, D. De Rossi, N. Taccini, R. Paradiso, J. A. Porchet,
J. Luprano, A. Ridolfi, C. Chuzel, T. Lanier, F. Revol-Cavalier, S. Schoumacker,
V. Mourier, R. Convert, I. Chartier, H. De-Moncuit, and C. Bini, ‘‘BIOTEX: Bio-
sensing textiles for personalised healthcare management,’’ IEEE Trans. Inf. Tech-
nol. Biomed., to be published.
[25] H. A. Kayyali, S. Weimer, C. Frederick, C. Martin, D. Basa, J. A. Juguilon,
and F. Jugilioni, ‘‘Remotely attended home monitoring of sleep disorders,’’ Tel-
emed J E Health, vol. 14, pp. 371–374, May 2008.
[26] K. Patrick, W. G. Griswold, F. Raab, and S. S. Intille, ‘‘Health and the
mobile phone,’’ Amer. J. Prev. Med., vol. 35, pp. 177–181, Aug. 2008.
[27] A. Sagahyroon, H. Raddy, A. Ghazy, and U. Suleman, ‘‘Design and imple-
mentation of a wearable healthcare monitoring system,’’ Int. J. Electron. Healthc.,
vol. 5, no. 1, pp. 68–86, 2009.
[28] Z. Wang, T. Kiryu, and N. Tamura, ‘‘Personal customizing exercise with a
wearable measurement and control unit,’’ J. Neuroeng. Rehabil., vol. 2, p. 14, 2005.
[29] D. Giansanti, G. Maccioni, V. Macellari, E. Mattei, M. Triventi, F. Censi,
G. Calcagnini, and P. Bartolini, ‘‘A novel, user-friendly step counter for home telemo-
nitoring of physical activity,’’ J. Telemed. Telecare, vol. 14, no. 7, pp. 345–348, 2008.
[30] F. Buttussi and L. Chittaro, ‘‘MOPET: A context-aware and user-adaptive weara-
ble system for fitness training,’’ Artif. Intell. Med., vol. 42, pp. 153–163, Feb. 2008.
[31] J. Fahrenberg, F. Foerster, M. Smeja, and W. Muller, ‘‘Assessment of pos-
ture and motion by multichannel piezoresistive accelerometer recordings,’’ Psy-
chophysiology, vol. 34, pp. 607–612, Sept. 1997.
[32] P. Bonato, P. J. Mork, D. M. Sherrill, and R. H. Westgaard, ‘‘Data mining of
motor patterns recorded with wearable technology,’’ IEEE Eng. Med. Biol. Mag.,
vol. 22, pp. 110–119, May–June 2003.
[33] M. J. Mathie, A. C. Coster, N. H. Lovell, and B. G. Celler, ‘‘Detection of
daily physical activities using a triaxial accelerometer,’’ Med. Biol. Eng. Comput.,
vol. 41, pp. 296–301, May 2003.
[34] M. J. Mathie, A. C. Coster, N. H. Lovell, B. G. Celler, S. R. Lord, and
A. Tiedemann, ‘‘A pilot study of long-term monitoring of human movements in the
home using accelerometry,’’ J. Telemed. Telecare, vol. 10, no. 3, pp. 144–151, 2004.
[35] J. Parkka, M. Ermes, P. Korpipaa, J. Mantyjarvi, J. Peltola, and I. Korhonen,
‘‘Activity classification using realistic data from wearable sensors,’’ IEEE Trans.
Inf. Technol. Biomed., vol. 10, pp. 119–128, Jan. 2006.
[36] M. Ermes, J. Parkka, J. Mantyjarvi, and I. Korhonen, ‘‘Detection of daily
activities and sports with wearable sensors in controlled and uncontrolled condi-
tions,’’ IEEE Trans. Inf. Technol. Biomed., vol. 12, pp. 20–26, Jan. 2008.
[37] O. Amft and G. Troster, ‘‘Recognition of dietary activity events using on-
body sensors,’’ Artif. Intell. Med., vol. 42, pp. 121–136, Feb. 2008.

[38] O. Amft, M. Kusserow, and G. Troster, ‘‘Bite weight prediction from acous-
tic recognition of chewing,’’ IEEE Trans. Biomed. Eng., vol. 56, pp. 1663–1672,
June 2009.
[39] E. S. Sazonov, S. A. Schuckers, P. Lopez-Meyer, O. Makeyev, E. L. Melanson,
M. R. Neuman, and J. O. Hill, ‘‘Toward objective monitoring of ingestive behavior
in free-living population,’’ Obesity, vol. 17, pp. 1971–1975, Oct. 2009.
[40] M. G. Benedetti, A. Di Gioia, L. Conti, L. Berti, L. D. Esposti, G. Tarrini,
N. Melchionda, and S. Giannini, ‘‘Physical activity monitoring in obese people in
the real life environment,’’ J. Neuroeng. Rehabil., vol. 6, p. 47, 2009.
[41] N. L. Keijsers, M. W. Horstink, J. J. Van Hilten, J. I. Hoff, and C. C. Gielen,
‘‘Detection and assessment of the severity of levodopa-induced dyskinesia in
patients with Parkinson’s disease by neural networks,’’ Mov. Disord., vol. 15,
pp. 1104–1111, Nov. 2000.
[42] N. L. Keijsers, M. W. Horstink, and S. C. Gielen, ‘‘Automatic assessment of
levodopa-induced dyskinesias in daily life by neural networks,’’ Mov. Disord.,
vol. 18, pp. 70–80, Jan. 2003.
[43] N. L. Keijsers, M. W. Horstink, and S. C. Gielen, ‘‘Ambulatory motor
assessment in Parkinson’s disease,’’ Mov. Disord., vol. 21, pp. 34–44, Jan. 2006.
[44] D. Giansanti, G. Maccioni, and S. Morelli, ‘‘An experience of health technology
assessment in new models of care for subjects with Parkinson’s disease by means of
a new wearable device,’’ Telemed. J. E. Health, vol. 14, pp. 467–472, June 2008.
[45] S. Patel, K. Lorincz, R. Hughes, N. Huggins, J. Growdon, D. Standaert,
M. Akay, J. Dy, M. Welsh, and P. Bonato, ‘‘Monitoring motor fluctuations in
patients with Parkinson’s disease using wearable sensors,’’ IEEE Trans. Inf. Tech-
nol. Biomed., vol. 13, pp. 864–873, Nov. 2009.
[46] M. Baechlin, M. Plotnik, D. Roggen, I. Meidan, J. Hausdorff, N. Giladi, and
G. Troester, ‘‘Assistive cueing, context awareness, freezing of gait, Parkinson’s dis-
ease, personal health assistant,’’ IEEE Trans. Inf. Technol. Biomed., to be published.
[47] S. Fahn and R. L. Elton, ‘‘Unified Parkinson’s Disease Rating Scale,’’ Recent
Developments in Parkinson’s Disease, S. Fahn, Ed. New York, NY: MacMillan
Healthcare Information, 1987, pp. 153–163.
[48] U. Anliker, J. A. Ward, P. Lukowicz, G. Troster, F. Dolveck, M. Baer,
F. Keita, E. B. Schenker, F. Catarsi, L. Coluccini, A. Belardinelli, D. Shklarski,
M. Alon, E. Hirt, R. Schmid, and M. Vuskovic, ‘‘AMON: A wearable multipara-
meter medical monitoring and alert system,’’ IEEE Trans. Inf. Technol. Biomed.,
vol. 8, pp. 415–427, Dec. 2004.
[49] V. Thulasi Bai and S. K. Srivatsa, ‘‘Design of wearable cardiac telemedicine
system,’’ Int. J. Electron. Healthc., vol. 3, no. 3, pp. 303–316, 2007.
[50] E. Villalba, D. Salvi, M. Ottaviano, I. Peinado, M. T. Arredondo, and
A. Akay, ‘‘Wearable and mobile system to manage remotely heart failure,’’ IEEE
Trans. Inf. Technol. Biomed., vol. 13, pp. 990–996, Nov. 2009.
[51] P. Bonato, F. Cutolo, D. De Rossi, R. Hughes, S. Patel, M. Schmid, J. Stein,
and A. Tognetti, ‘‘Wearable technologies to monitor motor recovery and facilitate
home therapy in individuals post stroke,’’ in Proc. 17th Congress Int. Society of
Electrophysiology and Kinesiology, Niagara Falls, Canada, 2008.
[52] P. Bonato, ‘‘Advances in wearable technology for rehabilitation,’’ Stud.
Health Technol. Inform., vol. 145, pp. 145–159, 2009.
[53] A. Mirelman, P. Bonato, and J. E. Deutsch, ‘‘Effects of training with a
robot-virtual reality system compared with a robot alone on the gait of individuals
after stroke,’’ Stroke, vol. 40, pp. 169–174, Jan. 2009.
[54] J. M. Hausdorff,
J. Neuroeng. Rehabil., vol. 2, p. 19, 2005.
[55] J. M. Hausdorff, ‘‘Gait dynamics, fractals and falls: Finding meaning in the
stride-to-stride fluctuations of human walking,’’ Hum. Mov. Sci., vol. 26, pp. 555–
589, Aug. 2007.
[56] A. K. Bourke, J. V. O’brien, and G. M. Lyons, ‘‘Evaluation of a threshold-
based tri-axial accelerometer fall detection algorithm,’’ Gait Posture, vol. 26,
pp. 194–199, July 2007.
[57] A. K. Bourke and G. M. Lyons, ‘‘A threshold-based fall-detection algorithm
using a bi-axial gyroscope sensor,’’ Med. Eng. Phys., vol. 30, pp. 84–90, Jan. 2008.
[58] G. Wu and S. Xue, ‘‘Portable preimpact fall detector with inertial sensors,’’
IEEE Trans. Neural Syst. Rehabil. Eng., vol. 16, pp. 178–183, Apr. 2008.
[59] D. Giansanti, G. Maccioni, S. Cesinaro, F. Benvenuti, and V. Macellari,
‘‘Assessment of fall-risk by means of a neural network based on parameters
assessed by a wearable device during posturography,’’ Med. Eng. Phys., vol. 30,
pp. 367–372, Apr. 2008.
[60] M. A. Estudillo-Valderrama, L. M. Roa, J. Reina-Tosina, and D. Naranjo-Her-
nandez, ‘‘Design and implementation of a distributed fall detection system–personal
server,’’ IEEE Trans. Inf. Technol. Biomed., vol. 13, pp. 874–881, Nov. 2009.
[61] S. Hagler, D. Austin, T. Hayes, J. Kaye, and M. Pavel, ‘‘Unobtrusive and
ubiquitous in-home monitoring: A methodology for continuous assessment of gait
velocity in elders,’’ IEEE Trans. Biomed. Eng., to be published.
[62] T. L. Hayes, F. Abendroth, A. Adami, M. Pavel, T. A. Zitzelberger, and J.
A. Kaye, ‘‘Unobtrusive assessment of activity patterns associated with mild cogni-
tive impairment,’’ Alzheimers Dement., vol. 4, pp. 395–405, Nov. 2008.
[63] A. Adami, M. Pavel, T. Hayes, and C. Singer, ‘‘Detection of movement in
bed with unobtrusive load cell sensors,’’ IEEE Trans. Inf. Technol. Biomed., to be
published.
[64] S. Patel, C. Mancinelli, B. L. Patritti, T. Pang, S. Schachter, and P. Bonato,
‘‘Detecting epileptic seizures using wearable sensors,’’ presented at
the 35th
Annual Northeast Bioengineering Conf., Cambridge, MA, 2009.
[65] B. K. Lee and J. E. Olgin, ‘‘Role of wearable and automatic external defibril-
lators in improving survival in patients at risk for sudden cardiac death,’’ Curr.
Treat. Options Cardiovasc. Med., vol. 11, pp. 360–365, Oct. 2009.

‘‘Gait variability: Methods, modeling and meaning,’’

36

IEEE ENGINEERING IN MEDICINE AND BIOLOGY MAGAZINE

MAY/JUNE 2010
