# Najafi et al. - 2024 - VersaSens An Extendable Multimodal Platform for Next-Generation Edge-AI Wearables

IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS FOR ARTIFICIAL INTELLIGENCE, VOL. 1, NO. 1, SEPTEMBER 2024

83

VersaSens: An Extendable Multimodal Platform for
Next-Generation Edge-AI Wearables

Taraneh Aminosharieh Najaﬁ , José Angel Miranda Calero , Member, IEEE, Jérôme Thevenot

,

Benjamin Duc

, Stefano Albini

, Alireza Amirshahi

, Hossein Taji

, María José Belda Beneyto ,

Antonio Affanni

, and David Atienza

, Fellow, IEEE

Abstract—The transition of healthcare towards digitalization is
closely related to the advancement of health-related technologies,
including wearable sensors and edge computing. In this paper,
we present VersaSens, a versatile and customizable platform
concept and its real implementation as a tool to boost research in
wearable sensors. The platform embodies the core attributes of
the VersaSens concept: versatility, ﬂexibility, and extendability
across multiple aspects of hardware, software, and processing
components. It features a modular design, consisting of sensor,
processor, and co-processor modules, allowing for various con-
ﬁgurations. To evaluate the efﬁciency of the platform, we tested
three use cases: cough monitoring, heartbeat classiﬁcation and
epileptic seizure detection. In all cases, the results indicate that
the platform effectively executes the applications, achieving low
energy consumption. In particular, our ﬁndings indicates that the
integration of a domain-speciﬁc edge-AI co-processor [i.e., HEEP
ocrates (Machetti et al., 2024)] equipped with several hardware
accelerators further improved the overall execution time and
energy consumption of the system. These results demonstrate
the potential of VersaSens to effectively support a diverse range
of edge-AI applications and conﬁgurations, thereby providing a
robust foundation for the research and development of novel
smart wearable sensor systems.

Received 24 May 2024; revised 26 July 2024; accepted 25 August 2024.
Date of publication 9 September 2024; date of current version 8 November
2024. This research was supported in part by the Wyss Center for Bio and
Neuro Engineering: Lighthouse Noninvasive Neuromodulation of Subcortical
Structures, in part by the ACCESS – AI Chip Center for Emerging Smart
Systems, sponsored by InnoHK funding, Hong Kong SAR, and in part
by the Swiss NSF Sinergia under Grant 193813: “PEDESITE-Personalized
Detection of Epileptic Seizure in the Internet-of-Things Era”. The review of
this article was arranged by Associate Editor Qi Zhu. (Corresponding author:
Taraneh Aminosharieh Najaﬁ.)

Taraneh Aminosharieh Najaﬁ is with the Embedded Systems Labora-
tory (ESL), Institute of Electrical and Micro Engineering, École Polytech-
nique Fédérale de Lausanne (EPFL), 1015 Lausanne, Switzerland, and also
with the Polytechnic Department of Engineering and Architecture, 33100
Udine, Italy (e-mail: taraneh.aminoshariehnajaﬁ@epﬂ.ch, aminoshariehnajaﬁ.
taraneh@spes.uniud.it).

José Angel Miranda Calero, Jérôme Thevenot, Benjamin Duc, Stefano
Albini, Alireza Amirshahi, Hossein Taji, and David Atienza are with the
Embedded Systems Laboratory (ESL), Institute of Electrical and Micro
Engineering, École Polytechnique Fédérale de Lausanne (EPFL), 1015 Lau-
sanne, Switzerland (e-mail: jose.mirandacalero@epﬂ.ch; jerome.thevenot@
epﬂ.ch; benjamin.duc@epﬂ.ch; stefano.albini@epﬂ.ch; alireza.amirshahi@
epﬂ.ch; hossein.taji@epﬂ.ch; david.atienza@epﬂ.ch).

Antonio Affanni is with the Polytechnic Department of Engineering and

Architecture, 33100 Udine, Italy (e-mail: antonio.affanni@uniud.it).

María José Belda Beneyto is with the Computer Architecture and Automa-
tion Department, Universidad Complutense de Madrid, 28040 Madrid, Spain
(e-mail: mbelda@ucm.es).

Digital Object Identiﬁer 10.1109/TCASAI.2024.3453809

Index Terms—Modular platform, multimodal bio-signals, next
generation edge-AI, smart wearable sensors, deep learning,
HEEPocrates, heterogeneous processor.

I. INTRODUCTION

I N 2020, the World Health Organization (WHO) introduced

the global digital health strategy 2020-2025 [2], which advo-
cates the integration of digital information and communication
technologies into healthcare systems worldwide with the aim
of enhancing global health outcomes. The objective of this
strategy is to facilitate a transition in healthcare towards the
implementation of digital solutions that are accessible, afford-
able, and sustainable. Furthermore, the strategy emphasizes
the adoption of cutting-edge technologies such as the Internet
of Things (IoT), Artiﬁcial Intelligence (AI), and smart wear-
ables to improve medical diagnosis and treatment through data-
driven approaches. Currently, despite the WHO digital health
strategy, healthcare systems in most countries remain largely
traditional. In contrast, AI has experienced rapid growth. To
harness the beneﬁts of AI in healthcare and bridge this gap,
it is of paramount importance to conduct adequate research
and development of cutting-edge infrastructure and medical
instruments to enable the next-generation of smart and edge-AI
wearables. For example, the development of custom hardware
for smart sensors, capable of running sophisticated AI models,
can facilitate a range of digital healthcare needs, including the
processing of large amounts of data, the provision of virtual care
[3], and the monitoring of patients remotely. Such facilities can
ensure equitable access to healthcare for people of all sex, race
and community worldwide. In addition, the processing results
of medical data driven by AI and Machine Learning (ML)
approaches on the edge, accessible to individuals, can democra-
tize healthcare information. This empowers the user to actively
participate in personalized treatment and preventive measures.
Moreover, wearable edge-AI technologies have the potential to
optimize medical care by moving away from a one-size-ﬁts-all
approach to personalized [4] and precision [5] medicine.

However, in contrast to software, the development of hard-
ware is a time-consuming, less ﬂexible, and an expensive pro-
cess. While debugging software typically involves identifying
and correcting errors in the code, hardware errors often neces-
sitate signiﬁcant changes, such as redoing the printed circuit
board (PCB) or ordering new components. These changes can

2996-6647 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

84

IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS FOR ARTIFICIAL INTELLIGENCE, VOL. 1, NO. 1, SEPTEMBER 2024

take weeks or even months to implement. Consequently, for the
rapid advancement of research and development in the ﬁeld of
hardware, in particular edge-AI technologies, the implementa-
tion of ﬂexible and modular hardware can play an essential role.
This approach allows modules to be developed and upgraded
independently of one another, thereby reducing the risk of dis-
ruption to the rest of the system when a module is found to have
an issue or requires an upgrade.

In light of the evolution of wearable sensor technology and
the importance of their rapid advancement for digital health, in
addition to the considerations mentioned above, further chal-
lenges must be addressed. The design of wearable sensors must
take into account the need for compactness, safety, and comfort
of wear. The necessity of continuous health monitoring im-
plies prolonged contact between the sensor and the body. Thus,
comfort, robustness, and biocompatibility are requirements to
ensure the long-term use of the hardware.

In addition, wearable sensors should be energy efﬁcient while
maintaining high functionality. In the literature, it is common
to adopt different strategies in sleep and idle modes to reduce
system consumption during low-operation instances [6], [7].
However, in accordance with the purpose and the application
of the system, it is necessary to determine the optimal trade-off
between energy consumption and functionality. To identify such
trade-offs during the research and development of such devices,
it is essential to have the ﬂexibility to alter and assess key
parameters such as the supply range and execution frequency
[8]. Furthermore, integrating multiple bio-signal modalities en-
hances the robustness, reliability and accuracy of the derived
outcomes [9].

This paper introduces VersaSens, a novel versatile and ex-
tendable platform designed to build edge-AI wearable systems
in a wide range of multimodal applications. The platform ad-
dresses the aforementioned challenges by incorporating the
principles of modularity, ﬂexibility, and expandability at various
levels. This approach provides a solid foundation for adapting,
enhancing, and scaling hardware to keep up with advancements
in AI technology. On this basis, the VersaSens platform consists
of sensor and processing modules, each equipped with Flexible
Flat Cable (FFC) and USB-C connectors. Communication be-
tween modules occurs through a dedicated bus that supports
various standard interface protocols. The modules are compact
and can be stacked horizontally, vertically, or at varying dis-
tances from each other. The platform offers the ﬂexibility to
create singular and multimodal sensors using available acoustic,
bio-potential, bio-impedance, temperature, optical, and inertial
sensors. Additionally, unlike any other state-of-the-art platform,
VersaSens offers the possibility to be expanded with ultra-low-
power AI co-processor modules. This enables efﬁcient real-
time execution of complex AI models directly at the edge. To
illustrate this capability, three use cases are presented and their
results are evaluated.

In summary, our main contributions can be listed as follows:
• The introduction of the novel concept of VersaSens, for
the advancement in the ﬁeld of edge-AI smart wearable
sensors, facilitating the integration of cutting-edge deep
learning (DL) models.

• The ﬁrst realization of the VersaSens concept is presented.
It showcases the modularity, ﬂexibility, and expandability
features of the VersaSens concept through the development
of modular processor and sensor units. These features
enable the creation of numerous wearable sensors tailored
to speciﬁc application needs with diverse compositions,
including both compact and distributed conﬁgurations. In
addition, the platform supports rapid prototyping and al-
lows for the integration of custom-designed modules.
• Enabling seamless integration of application-speciﬁc
edge-AI accelerator, as well as other sensing and storage
modules, within the VersaSens platform. This allows the
conception of advanced multi-layer SoCs equipped with
hardware accelerator units.

• Incorporating variable voltage and frequency features for
co-processor to facilitate research on functionality and
power consumption trade-offs.

The paper is structured as follows: Section II presents an
overview of other platforms in the literature, with a compar-
ison to VersaSens. Section III details the ﬁrst version of the
VersaSens platform hardware, software stack, and operating
modes. Section IV illustrates three distinct VersaSens conﬁg-
urations and presents analysis of their usability. In Section V,
we provide three case studies of cough frequency monitor-
ing, heartbeat classiﬁcation, and real-time epileptic seizure
detection using a VersaSens platform conﬁgurations. Finally,
Section VI offers our conclusions.

II. RELATED WORKS

Recent advances in wearable sensor platforms have led to
a signiﬁcant diversiﬁcation of their applications, ranging from
health monitoring to educational tools [10], [11], [12], [13],
[14], [15], [16], [17]. This section compares several leading
platforms in the state-of-the-art targeting a multimodal con-
cept and modular implementation. The unique contributions
and technological orientations within the healthcare ﬁeld are
highlighted and analyzed based on the comparison shown
in Table I.

A. Research-Based Platforms

Research-based platforms have been pivotal in the advance-
ment of the ﬁeld of wearable sensor technology, offering in-
novative solutions that address a wide variety of scientiﬁc and
medical applications. These platforms are usually designed to
enhance precision, ﬂexibility, and scalability in biomedical sig-
nal processing, enabling extensive research possibilities. Gen-
erally, there are two main types of platforms: those that target
a multimodal concept, which integrates many different sensors,
and those that target a unimodal concept, which focuses on a
speciﬁc type of modality. For instance, in the former category,
the authors in [18] introduced the Mobile Modular Multimodal
Biosignal Acquisition (M3BA) platform. It provided a highly
miniaturized design and integrated different sensors to acquire
distinct modalities such as biopotential, biooptical, and body
movement signals. Notable for its modularity, M3BA allowed

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

NAJAFI et al.: VERSASENS: AN EXTENDABLE MULTIMODAL PLATFORM FOR NEXT-GENERATION EDGE-AI WEARABLES

85

TABLE I
COMPARISON OF LEADING PLATFORMS IN MULTIMODAL AND MODULAR WEARABLE SENSOR TECHNOLOGY

Extendability Modular Design

User-Friendly

Low Cost Wide Sensor Support

AI Capabilities

Rapid Prototyping

Platform
M3BA
Amulet
MBioTracker
BioWolf
BITalino
Shimmer3
BioSignalsPlux(cid:2)R
BioHarness by Zephyr(cid:2)R
VersaSens

Type
Research-based
Research-based
Research-based
Research-based
Research-based
Commercial
Commercial
Commercial
Proposed system

ﬂexible integration into different mechanical setups and head-
and-body gears. Although M3BA was a novel highly customiz-
able mobile architecture, the system was module-centric, i.e.,
the main module was the one integrating the sensors in the same
PCB. Due to the latter fact, when it is desired to expand and
add additional modules or sensors, the main module had to be
replicated. Additionally, ensuring secure data transmission and
storage is a signiﬁcant concern for M3BA due to the variety of
sensitive biosignals it handles, which are not addressed in its
work. Note that the latter fact is mainly driven as this type of
platforms and devices handle sensitive personal data, necessitat-
ing robust security measures to protect user privacy and ensure
application integrity. Finally, no advanced AI co-processor is
present in this platform, hindering the implementation and ef-
ﬁcient deployment of any DL model.

In this context, the Amulet platform should also be mentioned
[6]. It offered an energy-efﬁcient, multi-application wearable
platform designed for long battery life and robust application
support. It included an ultra-low-power hardware architecture
and a companion software framework, enabling the develop-
ment of energy-efﬁcient applications. The platform supported
a variety of internal and external sensors and aimed to bal-
ance long battery life with the ﬂexibility and programmability
of a smartwatch. However, the need for strong security prop-
erties and app isolation in such a platform adds complexity
to its design and usage. Furthermore, the MBioTracker plat-
form [19] represents another signiﬁcant innovation in research-
based wearable systems. MBioTracker was designed for online
cognitive workload monitoring and integrated multiple physio-
logical signal acquisition channels, such as respiration cycles,
heart rate, skin temperature, and pulse waveform. It featured a
low-power processing platform and employed energy-sensitive
biosignal processing algorithms, demonstrating the potential for
extended battery life and efﬁcient data processing. However, the
complexity of the system and the need for careful calibration
of its self-aware monitoring approach may present challenges
to broader applicability and ease of use. Moreover, it presents
the same module-centric issues and lacks AI co-processor ca-
pabilities, similar to the M3BA.

In contrast to the multimodal concept followed by the latter
platforms, unimodal examples can be found. For example, the
authors in [10] presented BioWolf. This platform features a
nine-core processor optimized for ultra low power consump-
tion while maintaining high accuracy and reliability in elec-
troencephalogram (EEG) based monitoring systems. Although
they achieved a highly wearable system, their main focus was

solely on brain computer interfaces, which limited the range
of possible applications. In fact, the authors acknowledged this
latter fact and the platform was further improved in BioWolf16
[20]. The new version offered a 16-channel, 24-bit, 4kSPS ultra-
low power platform for wearable clinical-grade bio-potential
parallel processing and streaming. This advancement signiﬁ-
cantly enhanced its capabilities for clinical-grade applications,
maintaining ultra-low power consumption while increasing the
number of channels and improving data precision and streaming
capabilities. However, no further modiﬁcations were made to
include more modalities or even to attach external co-processors
to ofﬂoad AI workloads. Unlike the platforms previously dis-
cussed, security considerations for BioWolf and BioWolf16
include ensuring the integrity and conﬁdentiality of the EEG
data, which is critical for both clinical and research purposes.
Overall, these types of platform pose a valuable poten-
tial towards modularity and ﬂexibility; however, the complex-
ity of their setup and integration may imply challenges for
novice users. Moreover, their higher cost compared to simpler
research-educational platforms might be a limiting factor. For
example, BITalino is renowned for its accessibility and ﬂexibil-
ity, particularly within research and educational contexts [11].
It provides an entry point for students and novices to explore
biomedical signal processing. Although BITalino lacks the pro-
cessing power and specialized capabilities of more advanced
platforms, it remains a valuable tool for basic signal acquisition
purposes. This platform supports various types of biosignal,
making it a versatile option for a wearable proof-of-concept.
However, its capacity to interface seamlessly with external co-
processors is limited compared to more advanced platforms.

B. Commercial Platforms

Commercial platforms have also made signiﬁcant strides in
wearable sensor technology, focusing on providing robust and
reliable solutions for clinical and research applications. These
platforms are designed to offer high precision, user-friendly
interfaces, and extensive support for various sensor types, mak-
ing them suitable for practical, real-world applications. They
emphasize reliability, ease of use, and broad applicability, of-
ten providing comprehensive frameworks that facilitate data
acquisition and analysis. For instance, Shimmer3 [12] is widely
valued in clinical and sports science research for its precision
and reliability in biophysical and kinematic data capture. This
platform offers robust frameworks for biosignal processing,
making it ideal for clinical research applications. However,

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

✓
✓
✗
✗
✓
✗
✗
✓
✗
✗
✗
✓
✗
✗
✓
✓
✗
✗
✓
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✓
✓
✓
✓
✗
✓
✗
✓
✗
✗
✗
✗
✗
✗
✓
✓
✗
✓
✗
✗
✗
✗
✓
✗
✗
✗
✗
✓
✓
✓
✓
✓
✓
✓
86

IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS FOR ARTIFICIAL INTELLIGENCE, VOL. 1, NO. 1, SEPTEMBER 2024

TABLE II
CURRENT MODULES AND MODALITIES AVAILABLE IN VERSASENS

Module

Type

Main

Processor & Sensor

ExG

Sensor (8 channels)

EDA

Sensor (1 channel)

Heart

Sensor (1 channel)

HEEPO

Co-Processor

Modality
3-axis accelerometer
3-axis gyroscope
EEG
ECG
EMG
ECG
GSR/EDA
RSP
ECG
GSR/EDA
RSP
PPG
SKT
Acoustic sensor
-

Signal Range
± 8g
± 2000 (◦/s)

Resolution Bits
12
16

±4/Gain(4, 6, 8, 12)(V )

±1/Gain(20, 40, 80, 160)(mV )

0 - 2 (M Ω)
±100(mV )

0 - 100 (M Ω)

530 ,655 ,940 (Green, Red, Infrared) (nm)
0 - 70 (◦C)
27 − 27k(Hz)
-

24

18

20

18

20

20
16
-
-

while Shimmer3 offers substantial hardware ﬂexibility, it pri-
marily supports speciﬁc sensors designed for its ecosystem and
does not explicitly support seamless interfacing with external
co-processors, which limits its adaptability in some scenarios.
In addition, its higher cost and technical complexity may require
advanced technical skills for installation and operation. Simi-
larly, BioSignalsPlux(cid:2)R [21] provides a comprehensive frame-
work designed for versatility and ease of use in research and
development settings. Supporting a wide range of sensors,
the platform offers ﬂexibility in data acquisition and analy-
sis, making it a user-friendly option for research applications.
Another example in the commercial category is BioHarness by
Zephyr(cid:2)R [22]. This is a comprehensive wearable sensor plat-
form that monitors various physiological parameters, including
heart rate, respiration rate, posture, activity level, and skin tem-
perature. It is widely used in both sports science and clinical
research to monitor performance and health. The platform is
designed to provide real-time data, which is crucial for ap-
plications that require continuous monitoring of physiological
signals. However, as for the rest of the commercial available
platforms, the substantial hardware ﬂexibility in terms of the
physiological parameters it can monitor, is primarily optimized
for use with its own proprietary sensors.

The comparative analysis of these commercial platforms un-
derscores their contributions to the ﬁeld of wearable technology.
Additionally, being commercially oriented leads to ensuring
robust security measures, which is essential across all of them
to protect sensitive data and maintain the integrity and conﬁ-
dentiality of the collected information. However, they all share
common drawbacks. For instance, the reliance on proprietary
sensors and ecosystems or their cost. These can potentially pos-
ing a barrier for widespread adoption in resource-constrained
environments. Moreover, the complexity of the setup for some
of them can also be a challenge.

As a result of the previously discussed platforms found in
the literature, this work presents VersaSens, which emerges as
a particularly innovative platform trying to address the limita-
tions found in both research- and commercial-grade systems.
Designed with a focus on modularity and rapid customiza-
tion, which is crucial to explore various design spaces in the

integration of wearable technology. This platform allows for
easy integration of a diverse array of sensors and co-processors
through its modular design, facilitating efﬁcient real-time data
acquisition, processing and DL execution. In fact, the AI em-
powerment of VersaSens, attributable to its capacity to interface
with deeply heterogeneous co-processors, positions it uniquely
for applications demanding high computational power and real-
time responsiveness.

III. PLATFORM DESCRIPTION

This section outlines the VersaSens platform1 and de-
scribes the ﬁrst version of the realized hardware modules in
Section III-A, discusses the software stack including the
ﬁrmware architecture and operating system in Section III-B,
and operating modes in Section III-C.

A. Hardware

VersaSens is a platform for the development of wearable
sensors. It is modular and in its current representation con-
sists of ﬁve individual sensor and processing modules, namely:
Main, Heart, ExG, EDA, and HEEPO. The modalities included
in each module, along with their respective signal ranges and
resolutions, are detailed in Table II.

All sensor modules and the Main module are equipped with
FFC and USB-C connectors, allowing communication through
a dedicated bus called Sensor Bus (S-Bus). The co-processor
module, on the other hand, communicates exclusively with the
main module and is equipped only with FFC connectors. An-
other dedicated bus, the Processor Bus (P-Bus), facilitates com-
munication between the processors. S-Bus supports numerous
communication interfaces, including Serial Peripheral Interface
(SPI), Inter-Integrated Circuit (I2C), Pulse Density Modulation
(PDM), and General-Purpose Input/Output (GPIO) for digital
and analog signals, as well as a 3.3V power supply and ground.
Similarly, P-Bus includes SPI, I2C and GPIOs, along with 3.3V

1All information regarding the VersaSens platform can be found on its

website at: https://www.epﬂ.ch/labs/esl/research/smart-wearables/versasens/

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

NAJAFI et al.: VERSASENS: AN EXTENDABLE MULTIMODAL PLATFORM FOR NEXT-GENERATION EDGE-AI WEARABLES

87

Fig. 1. VersaSens platform overview.

Fig. 2. VersaSens modules stacked with FFC for a compact conﬁguration.

and ground connections. A block diagram of the platform is
provided in Fig. 1.

The inclusion of buses, FFC connectors, and USB-C connec-
tors allows modules to be arranged in various conﬁgurations.
Additionally, these features allow the platform to be extendable,
facilitating the integration of both off-the-shelf and custom-
designed sensor or co-processor modules. The add-on modules,
as illustrated in Fig. 1, can utilize any of the aforementioned
interfaces on the S-Bus or P-Bus to communicate with the main
module. Both busses are accessible through FFC connectors and
USB-C ports.

All modules are designed on a four-layer PCB system. The
Main module has a PCB dimensions of 30x55x0.8 mm3, while
all the other boards have a PCB dimensions of 25x45x0.8
mm3. The physical realization of all sensor, processor and

co-processor modules is illustrated in Fig. 2 demonstrating their
interconnectivity through FFC. The detail description of all
modules is provided in the subsequent sections.

1) Main Module: The Main module serves as the cen-
tral unit of the platform, housing the main System-on-Chip
(SoC) based on the nRF5340 from Nordic Semiconductor(cid:2)R .
This high-performance, low-power solution features a dual-core
Arm(cid:2)R Cortex-M33 architecture, comprising both application
and network processors. The application core has digital signal
processing (DSP) instructions and a ﬂoating point unit (FPU),
operating at up to 128 MHz with 1 MB of ﬂash memory and
512 kB of RAM. The network core is optimized for ultra-
low power consumption, running at a ﬁxed frequency of 64
MHz with 256 kB of ﬂash memory and 64 kB of RAM. The
SoC supports various interfaces, including SPI, I2C, Quad SPI,

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

88

IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS FOR ARTIFICIAL INTELLIGENCE, VOL. 1, NO. 1, SEPTEMBER 2024

PDM, and GPIOs, in addition to a wide range of wireless
protocols such as Bluetooth Low Energy (BLE), Near Field
Communication (NFC), and 2.4 GHz proprietary protocols.

In the current VersaSens setup, the SoC is responsible for
power management, sensor conﬁguration, signal acquisition,
data synchronization, and storage in local memory. In com-
munications with sensors and other auxiliary components, the
SoC consistently functions as the master, collecting data from
the slave devices. However, in communication with the co-
processor, the SoC operates as a slave, preparing data in a buffer
at the required time intervals for the co-processor.

The Main module incorporates a Power Management Inte-
grated Circuit (PMIC) utilizing the MAX77658B from Analog
Devices(cid:2)R . This circuit is responsible for charging the battery
and providing 1.8V and 3.3V power supplies from the battery.
The PMIC communicates with the main SoC via I2C and GPIO
interfaces.

The Main module also includes an Inertial Measurement Unit
(IMU) employing the BNO086 from CEVA(cid:2)R , which consists
of a three-axis accelerometer, gyroscope, and magnetometer.
Currently, the IMU is conﬁgured to measure accelerations (X,
Y, Z) and rotational angles (yaw, pitch, roll) thanks to the
manufacturer’s data fusion algorithms. The IMU communicates
with the main SoC through a universal asynchronous receiver-
transmitter (UART) interface.

For local storage, the board features an 8 G-bit ﬂash memory
utilizing the AS5F38G04SND from Alliance Memory(cid:2)R , and a
micro Secure Digital (SD) card slot supporting various capaci-
ties. The ﬂash memory and SD card communicate with the SoC
through quad-SPI and fast SPI interfaces, respectively.

In addition, the module is equipped with reset and on-off
buttons, an operating mode selector, and JTAG programmer
connector pads. The on-off button controls the PMIC supply to
the system. A reset signal, traveling through the S-Bus and P-
Bus to all boards, can be initiated by the reset button, or the SoC.
To synchronize all sensors, the SoC provides a start signal to
initiate sensor setup and acquisition. Furthermore, a 32.768kHz
oscillator based on the SIT1533AI from SiTime(cid:2)R , provides a
low-frequency clock for the sensors, distributed via the S-Bus
to all peripheral modules.

2) ExG Module: The ExG is a sensor module that in-
corporates an eight-channel bio-potential analog front end
(AFE) based on the ADS1298 from Texas Instruments(cid:2)R . This
AFE can measure electrocardiogram (ECG), electromyogram
(EMG), and EEG signals. It communicates with the main SoC
via the SPI interface through the S-Bus. Additionally, the ExG
module features two dip switches for selecting and deactivating
channels. To acquire biopotential signals, the corresponding
electrodes can be connected directly to the USB-C connector
of the ExG module. For example, the spectrogram plot shown
in Fig. 3 illustrates the EEG signals acquired by the ExG module
from the location of the Fp1 electrode, according to the 10-
20 system [23]. The signals were collected while a volunteer
had their eyes open (exhibiting blinking) for the ﬁrst half of the
period, and then the eyes closed (showing Alpha waves) for the
second half.

Fig. 3.

EEG signal acquired from Fp1 channel during open and closed eyes.

Fig. 4.
chest, using one differential channel, during breathing and breath-holding.

Synchronized raw ECG and ﬁltered RSP signals, acquired from the

3) EDA Module: The EDA is a sensor module incorpo-
rating a bio-potential and bio-impedance AFE based on the
MAX30001G. This AFE is capable of measuring electroder-
mal activity (EDA), galvanic skin resistance (GSR), respiration
(RSP), and ECG signals using two leads. The module commu-
nicates with the main SoC via the SPI interface through the
S-Bus. To acquire biopotential and bioimpedance signals, the
corresponding electrodes can be directly connected to the USB-
C connector of the EDA module. For instance, Synchronized
ECG and RSP signals, acquired by the EDA module, are illus-
trated in Fig. 4. These signals were obtained from a volunteer
using a single differential channel. Electrodes were positioned
under the right clavicle and on the lower left abdomen to capture
biopotential and bioimpedance signals during the phases of
normal breathing and holding of breath.

4) Heart Module: The Heart module is a sensor mod-
ule comprising three primary components. First, it includes a
Microelectromechanical Systems (MEMS) microphone based
on the T5838 from TDK(cid:2)R . This sensor communicates with the
main SoC via the PDM interface through the S-Bus. Further-
more, the module has a contactless digital infrared thermometer
based on the MLX90632 from Melexis(cid:2)R , which communicates
with the main SoC using the I2C interface via the S-Bus.

the Heart module incorporates an AFE for
Moreover,
bio-impedance,
and photoplethysmography
(PPG) measurements, based on the MAX86178 from Analog
Devices(cid:2)R . This AFE is capable of measuring ECG, RSP, or

bio-potential,

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

NAJAFI et al.: VERSASENS: AN EXTENDABLE MULTIMODAL PLATFORM FOR NEXT-GENERATION EDGE-AI WEARABLES

89

User APP

VersaAPI

Sensor 1

Sensor 2

Sensor n

Timer

SPI

I2C

PMIC

Storage

VersaSDK

Zephyr 
RTOS

Nordic BLE

System Init

Nordic HAL

Nordic SDK

Fig. 6.
and layered architecture.

Software stack of the VersaSens platform, showcasing its modular

the main SoC. These features collectively offer signiﬁcant ﬂex-
ibility in optimizing voltage and frequency parameters, thereby
enhancing power efﬁciency across different operational states,
including data acquisition and idle modes.

HEEPocrates interfaces with the main SoC via SPI interface
through the P-Bus, operating as the SPI master. It receives
the necessary signals collected by the main SoC at speciﬁc
time intervals, facilitating higher-level processing tasks, includ-
ing complex machine and deep learning training and infer-
ence. This conﬁguration, coupled with the high-performance
attributes of HEEPocrates, enables it to function effectively as
a co-processor, thereby enhancing the AI capabilities of the
VersaSens system.

B. Software Stack

VersaSens, in addition to its hardware expandability features
a ﬂexible and easy-to-extend software stack architecture, Fig. 6.
The ﬁrmware design allows researchers and developers to seam-
lessly interface with different peripherals. Moreover, the upper
layers of the software stack enable the integration and execution
in real-time of advanced deep learning models through and by
the attached heterogeneous co-processor modules, facilitating
complex data analysis and real-time decision-making.

The ﬁrmware and operational framework of the VersaSens
platform are designed to emphasize its core attributes of ﬂex-
ibility, modularity, and efﬁcient performance, essential for
deploying effective wearable sensor platforms across various
applications. Speciﬁcally, VersaSens utilizes a robust ﬁrmware
architecture designed to accommodate a modular approach,
enabling seamless integration and interchangeability of sen-
sor modules. This architecture facilitates the plug-and-play
functionality of sensors, where adding or swapping sensors
can be done without disrupting the overall system operations.

Fig. 5.
ﬁnger, respectively.

Synchronized ECG and PPG signals, acquired from the chest, and

EDA using two leads. It also supports up to six LEDs and four
photodiodes for PPG measurements and communicates with
the SoC via the I2C interface through the S-Bus.

To provide ﬂexibility in the design and selection of LEDs
and photodiodes for PPG measurements without necessitating
alterations to the Heart module, an auxiliary module referred to
as the PPG module was developed. This module is mounted via
a stacking connector on the reverse side of the Heart module. In
the current version of VersaSens, the PPG module features PCB
dimensions of 8x11x0.8 mm3 and accommodates three LEDs
(Grees, Red, Infrared), and one photodiode.

To acquire biopotential, bioimpedance signals, the corre-
sponding electrodes can be connected directly to the USB-C
connector of the Heart module. For the acquisition of biooptical
signals the PPG module must be positioned in close proximity
to the body. As an illustration, Fig. 5 presents the synchronized
ECG and green LED PPG signals captured by the Heart mod-
ule. The ECG signals were acquired using two electrodes, one
positioned under the right clavicle and the other on the lower
left abdomen. The PPG signals, also illustrated in the ﬁgure,
were collected from the index ﬁnger.

5) HEEPO Module: The HEEPO is a co-processor module
that incorporates the HEEPocrates SoC [1], speciﬁcally de-
signed for ultra-low-power healthcare applications based on the
X-HEEP platform [24]. HEEPocrates integrates both a Coarse-
Grained Reconﬁgurable Array (CGRA) accelerator [25] and
an In-Memory Computing (IMC) accelerator [26], both recog-
nized for their efﬁciency in reducing overall energy consump-
tion in healthcare applications. HEEPocrates operates within a
high-frequency, low-voltage range, achieving 170 MHz at 0.8V
and 470 MHz at 1.2V. The SoC features the CV32E20 core,
eight SRAM banks, a fully connected bus, and a wide array of
peripherals, including SPI, I2C, UART, and GPIOs.

On the HEEPO module, the voltage of HEEPocrates can be
adjusted for various applications via an adjustable Low Dropout
Regulator (LDO) based on the TLV75801PDBV from Texas
Instruments(cid:2)R . This LDO provides a voltage range from 0.6V
to 1.2V, adjustable through a potentiometer. Additionally, an ex-
ternal clock generator with a frequency of 32.768 kHz feeds the
internal Frequency Locked Loop (FLL) of the SoC, facilitating
the generation of the system clock, which can be conﬁgured by

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

90

IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS FOR ARTIFICIAL INTELLIGENCE, VOL. 1, NO. 1, SEPTEMBER 2024

This structured approach ensures that VersaSens is highly
adaptable and capable of supporting a wide range of bio-signal
processing applications. The main layers in the architecture are
described as follows:

• User APP. This is where end-user applications are de-
veloped. This layer interacts directly with the second one,
the VersaAPI, to utilize the underlying functionalities pro-
vided by the ﬁrmware.

• VersaAPI. This speciﬁc layer serves as a crucial interface,
exposing the necessary functionalities to the User APP
layer. It provides a set of APIs to interact with sensors,
handle data processing, and manage system resources.
• VersaSDK. This is a key part of the architecture. It in-
cludes development tools and libraries speciﬁc to Ver-
saSens, enabling developers to build applications and
ﬁrmware optimized for the platform. This layer also im-
plements various peripherals and low-level functionalities,
including analog and digital interfaces with sensors and
co-processors. In addition, power supply orchestration for
the attached modules and ﬂash data storage and retrieval
are also managed in this layer.

• Nordic SDK. This last layer represents the hardware ab-
straction layer for the SoC of the Main Module. It includes
libraries, drivers, and tools necessary for developing appli-
cations on Nordic System on Chip (SoC). Key components
within this layer include, in particular, Bluetooth manage-
ment and System Init functionalities. Speciﬁcally, for the
ﬁrst VersaSens realization presented in this work, this layer
includes Nordic SDK and HAL related functions, provided
by Nordic Semiconductor.

• Zephyr RTOS. This cross-cutting layer is a real-time op-
erating system that provides foundational services for task
scheduling, interrupt handling, and resource management.
This layer deals with the entire ﬁrmware architecture and
ensures robust and efﬁcient system performance.

Moreover, recognizing the importance of security, especially
in handling sensitive health data, the current software stack
also employs stringent encryption protocols for data at rest
and in transit. It supports secure, over-the-air ﬁrmware updates,
allowing for seamless enhancements to its functionalities and
security features without compromising user data or device
integrity.

C. Operating Modes

VersaSens is designed to operate in three distinct modes:
idle, storage, and storage-stream. These modes are selectable
via a selector located on the Main board. In idle mode, the
main SoC minimizes power consumption by shutting down the
supply to peripheral modules and entering sleep mode, with
operations limited to battery charging. When storing mode is
selected, the SoC wakes up, powers peripheral modules, sends
a start signal to all sensor modules, and begins collecting sensor
data without real-time transmission. The collected signals are
stored locally on one of the available onboard storage devices.
The data throughput is contingent upon the number of sen-
sor modalities and the acquisition frequency, which can vary

depending on the application. For example, employing all the
modalities presented in the current version of VersaSens at
common acquisition frequencies results in a data throughput of
21,364 bytes per second. At this rate, it would take over 13 hours
of continuous data recording to ﬁll the 8 G-bit ﬂash memory
available on the main board.

In storage-stream mode, the system not only collects and
stores data locally but also enables real-time data transmission
via a BLE communication network. Although this mode in-
creases power consumption, it facilitates real-time monitoring
and immediate data access. These operating modes offer ﬂex-
ibility in resource usage, particularly in power management,
allowing the user to switch to a less active mode when certain
features are not needed. The battery life duration depends on
the selected operating mode, the number and types of sensor
modalities, and can vary depending on the application. For
example, utilizing all the presented modalities in the current
version of VersaSens and operating the sensor in storage-stream
mode, a 420mAh battery can last up to 10 hours, resulting in a
total average power consumption of approximately 42mA.

IV. SENSOR CONFIGURATIONS AND USABILITY ANALYSIS

The platform was designed to ensure that the sensors are
light, compact, and easy to use. Various sensor compositions
can be conﬁgured from the VersaSens platform, with different
battery size, depending on the application of interest. Thanks
to the FFC connectors and the dedicated buses, modules can
be stacked horizontally, vertically, or in a combination of both
within single or separate enclosures. In addition, USB-C con-
nectors allow modules to be placed at a distance from each other
in separate enclosures. Finally, the BLE capability of the plat-
form allows real-time communication with other devices (e.g.,
smartphones, tablets, laptops, or even other VersaSens units).
The aforementioned features offer ﬂexibility and ease in the
usage of the platform and provide an adequate tool for prototyp-
ing new generations of wearable sensors. Although numerous
conﬁgurations are possible, this section describes three exam-
ples of conﬁgurations: compact, shoulder-distributed, and wrist
conﬁgurations. The open-source repository of VersaSens can
be found at https://github.com/esl-epﬂ/VersaSens. It contains
all the ﬁles and information required to replicate the described
VersaSens platform. In particular, it includes the PCBs layout,
SoC software, and 3D models for the enclosures of all three
conﬁgurations.

1) Compact Conﬁguration: In the proposed compact conﬁg-
uration, illustrated in Fig. 7, an enclosure with dimensions of
40x60x30 mm3 can accommodate all modules and a 750 mAh
battery, weighing a total of 50 grams. After being intercon-
nected via FFC, all modules can be easily inserted into the
enclosure. The enclosure can be made of biocompatible poly-
mers (e.g., Polylactic acid or Polyamide 12) and coated with
skin-safe silicon rubber (e.g., Dragonskin™), ensuring optimal
safety and comfort during daily use and clinical trials. The
compact conﬁguration can be worn on various parts of the body,
including the chest, arm, shoulder, and neck, by using straps or
medical adhesive patches (e.g., 3M 1577 or 3M 1522).

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

NAJAFI et al.: VERSASENS: AN EXTENDABLE MULTIMODAL PLATFORM FOR NEXT-GENERATION EDGE-AI WEARABLES

91

Fig. 7. Compact conﬁguration.

Fig. 8. Distributed shoulder conﬁguration.

2) Distributed Conﬁguration: In the proposed shoulder dis-
tributed conﬁguration, shown in Fig. 8, three separate cases
are designed to accommodate the Main and ExG modules in
the red enclosure placed on the back of the neck, the Heart
module in the green enclosure positioned on the left side of the
chest, and the EDA module and the battery in the blue enclosure
located on the right side of the chest. In this conﬁguration, the
Main and ExG modules are interconnected via FFC due to their
shared enclosure, while the Heart and EDA modules, which
are placed at a distance, are connected to the Main and ExG
modules via USB-C cables. Furthermore, the ExG module is
connected via USB-C to a headband embedded with up to eight
electrodes to collect cortical brain activity. The dimensions
are 34x60x18 mm3 for the red casing and 27x50x13 mm3 for
both the green and blue casing. All cases are secured with a
U-shaped skin-safe silicone rubber (Dragonskin™) with in-
creased tackiness to minimize movement artifacts for various
sensors. as an alternative implementation option for rapid proto-
typing and testing, silicone can be replaced by adhesive patches.
3) Wrist Conﬁguration: In the proposed wrist conﬁguration,
shown in Fig. 9, a unique enclosure accommodates both vertical
and horizontal modules arrangements. The Main and HEEPO
modules are vertically stacked in the upper section of the wrist
within the red compartment of the case. The ExG module,
intended for measuring EMG signals from the arm, is housed
in the pink compartment behind the Main module, along with
the battery. The Heart module, intended for PPG measurements
from the wrist, is positioned on the inner side of the wrist in
the green compartment. In this conﬁguration, the Main and
Heart modules are interconnected via FFC, while the Heart and

Fig. 9. Wrist conﬁguration.

ExG modules are connected by a USB-C cable. The enclo-
sure is shaped as a bracelet and can be adjusted to ﬁt various
wrist sizes or placed on other body parts, such as the upper
arm or ankle.

V. EXPERIMENTAL SETUP AND RESULTS

This section presents the deployment of three different
health-related use cases on our platform with a speciﬁc conﬁg-
uration. First, a cough-frequency monitoring application [27]
to detect and identify cough events in real-time by relying on
the joint usage of two AI models. Second, a heartbeat classiﬁer
is evaluated, relying on a machine learning pipeline to accu-
rately identify and classify heartbeats [28]. Finally, a seizure
detection model is evaluated based on a complex deep learning
model designed to detect seizure events with high precision and
sensitivity [29], [30].

As already mentioned, the physiological acquisition is or-
chestrated by the Main module of VersaSens. For the initial ap-
plication, algorithmic computations are also conducted within
this Main module. For the subsequent two applications, the pro-
cessing workloads are entirely performed by the co-processor
SoC, i.e. the HEEPO module porting HEEPocrates in this case.
Regarding the VersaSens multi-board system conﬁguration,
the necessary modules per application were stacked vertically
and enclosed in a casing along with a battery. The cough fre-
quency monitoring case used the Main and Heart modules,
while the other two cases required the Main, Heepo, and ExG
modules. For these applications, high-tack skin-safe silicone
allows the frame to be placed directly on the chest and neck, as
illustrated in Figs. 10(a) and 10(b). In the heartbeat monitoring
scenario, the electrodes are in contact with the skin on each
side of the apparatus. For the seizure detection scenario, elec-
trodes are mounted on a headband. Speciﬁcally, a 1-lead ECG
is utilized for the heartbeat classiﬁcation application, while a
bipolar montage (F7, T7, F8, and T8) is employed for the
seizure detection use case.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

92

IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS FOR ARTIFICIAL INTELLIGENCE, VOL. 1, NO. 1, SEPTEMBER 2024

(a) Cough frequency monitoring and Heart beat classiﬁer conﬁgurations

(b) Seizure detection conﬁguration

Fig. 10.
Sensor conﬁgurations for the health-related use cases reported: (a) Cough frequency monitoring and heartbeat classiﬁer conﬁgurations, which relies
on machine learning algorithms to detect cough events and classify heartbeats respectively, and (b) Seizure detection conﬁguration, which uses a complex
deep learning model to detect seizure events.

Fig. 11. Cough frequency monitoring application ﬂow.

A. Cough Frequency Monitoring

The ﬁrst use case focuses on a cough-frequency monitor-
ing application, leveraging machine learning capabilities on
two distinct modalities, speciﬁcally audio and kinematic sig-
nals captured from a microphone and an inertial measurement
unit (IMU). Both sensors are placed on the chest. Two dis-
tinct XGB (eXtreme Gradient Boosting) models are used, one
per modality, to exploit the different information carried by
each signal. Both are trained to detect cough events from their
input data.

The training and testing were performed on a multimodal
dataset for cough detection [27]. Data were collected from 20
healthy subjects (10 males, 10 females; age 26.5 ± 6.5 years)
during sitting and walking activities while being exposed to
different environmental noises (silent, trafﬁc, music, and by-
stander cough), and while performing different sounds (cough-
ing, laughing, deep breathing, and throat clearing). This pro-
vides a wide variety of data to allow the ﬁnal models to be robust
for deployment in real-life scenarios.

Fig. 11 shows the main phases of the algorithm, namely the
detection and post-processing phases, and their ﬂow. The detec-
tion phase is based on the cooperation of the two classiﬁers. In
particular, the kinematic-based one will serve as a trigger for
the acoustic-based one, executed only when a cough event is

TABLE III
ENERGY CONSUMPTION OF THE MAIN PROCESSOR FOR ONE
CLASSIFICATION WINDOW OR IMU-BASED MODEL (0.5S) AND
AUDIO-BASED MODEL (0.8S) FOR COUGH FREQUENCY MONITORING

Parameter

Duration

Power consumption

Voltage
Frequency

Energy consumption

Total energy

IMU
Audio
IMU
Audio

IMU
Audio

Processing
11 ms
114 ms
27.7 mW
30.3 mW
3.3 V
128 MHz
0.30 mJ
3.45 mJ
IMU
Audio

Deep Sleep
489 ms
686 ms

9.05 μ W

3.3 V
32 KHz
4.42 μJ
6.2 μJ
0.31 mJ
3.51 mJ

identiﬁed. The switch from one model to the other will solely
depends on the output of the current classiﬁcation. For both
models, feature extraction and inference are executed. Different
sets of features are extracted from the audio signal from both
the time and frequency domains, yielding intense computations.
In contrast, for the IMU signals only time domain features are
computed. After the inference phase, a post-processing rou-
tine is implemented. This accumulates information about the

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

NAJAFI et al.: VERSASENS: AN EXTENDABLE MULTIMODAL PLATFORM FOR NEXT-GENERATION EDGE-AI WEARABLES

93

Fig. 12. HBC application phases.

identiﬁed cough positions to provide the ﬁnal frequency estima-
tion over a selected time frame. This application is a version of
the algorithm presented in [27], which was originally achieving
91% of sensitivity, 92% of speciﬁcity, and 80% of precision.

The processing of the classiﬁers of the application is executed
on the processor of the main module, running at 128 MHz.
In both cases, the processor is active only during execution
and enters deep sleep mode for the remaining of the win-
dow (0.5s and 0.8s for IMU and audio models, respectively).
Table III reports average power and energy consumption of
feature extraction and inference phases, measured during pro-
cessing and deep sleep. The computations required by the IMU-
based model can be terminated in 11ms over its window of
0.5s, allowing the processor to stay in deep sleep mode for
489ms. Given the average power consumption of 27.7 mW and
9.05 μW during processing and sleep phases, the resulting
energy consumption is 0.30 mJ and 4.42 μJ, respectively. Anal-
ogous behavior occurs for the audio-based classiﬁer, which
presents 114ms of execution time and 686ms of sleep time,
yielding 3.45 mJ and 6.2 μJ of consumed energy. In both cases,
the limited duty cycle and the energy-efﬁcient sleep mode of
the processor allow us to keep the total energy consumption at
low values (0.31 mJ and 3.51 mJ for IMU and audio models,
respectively). As for the peak identiﬁcation and post-processing
module, their measurements are not reported due to their negli-
gible impact on the total energy, given their low computational
complexity and the small amount of data they process.

B. Heart Beat Classiﬁer

As a second use case, we employed a comprehensive ap-
proach to heartbeat classiﬁcation (HBC) based on advanced sig-
nal processing and machine learning techniques [28], Fig. 12.
The algorithm pipeline leverages a modular design to optimize
both performance and energy efﬁciency on ultra low power
platforms. Speciﬁcally, ECG samples are captured during
12 seconds and then, the systems process them. The data pro-
cessing is divided into four phases: ﬁltering, enhancement, fea-
ture extraction, and inference. Once the ECG signal is acquired,
it is ﬁltered to remove unwanted noise using the morpholog-
ical ﬁlter (MF), a technique that extracts the signal baseline
based on the shape of the original signal and subsequently
subtracts it. Initially utilized in image processing, this method
has been adapted for use on single- or multi-lead ECGs in
embedded systems. [31]. Then, the Relative Energy (Rel-En)
[32] technique is used to extract the energy of speciﬁc windows
of analysis to amplify the R peaks. Subsequently, the ECG
delineation method is employed to extract features. A crucial
part of this process is R peak detection, accomplished using the

TABLE IV
ENERGY CONSUMPTION OF CO-PROCESSOR FOR ONE
CLASSIFICATION WINDOW (12S) FOR HBC

Parameter
Duration
Power Consumption
Voltage
Frequency
Energy Consumption

Processing
22 ms
8.68 mW
830 mV
170 MHz
0.19 mJ

Total Energy

Deep Sleep
11978 ms
0.29 mW
830 mV
32 KHz
3.47 mJ
3.66 mJ

REWARD [32] algorithm. And the remaining ﬁducial points are
delineated with a low-complexity method [33]. Finally, a neuro-
fuzzy classiﬁer [34] with 97% accuracy is employed to detect
the abnormal beats.

To train and test the heartbeat classiﬁcation model, we used
the MIT-BIH Arrhythmia Database (MITDB) [35]. It contains
48 half-hour excerpts of two-channel ambulatory ECG record-
ings from 47 subjects. The dataset includes a wide variety of
arrhythmias and provides a robust foundation for developing
and validating the classiﬁer.

The processing part of the application is executed on the
HEEPocrates co-processor. Given that in this case, the de-
scribed algorithms does not present a high complexity, no hard-
ware accelerator available in HEEPocrates were really needed
or employed. Furthermore, an optimal setting for voltage and
frequency was selected based on previous research results [36].
Speciﬁcally, the co-processor runs at 170 MHz with a voltage of
830 mV while processing. For the 12-second window duration,
the co-processor executes the application and enters deep sleep
mode for the remainder of the time. The latter mode is achieved
by power-gating the modules in the system and reducing the
system frequency to the lowest feasible level, 32 KHz, to mini-
mize both static and dynamic power consumption. The average
power and energy consumption, and the corresponding voltage
and frequency parameters for both processing and deep sleep
conditions are outlined in Table IV.

The results show how during the processing phase, which
lasts 22 milliseconds,
the average power consumption is
8.68 mW, resulting in an energy consumption of 0.19 mJ.
This brief duration of high activity ensures that computational
tasks are completed quickly and efﬁciently, minimizing the time
spent in the higher-power-consuming state. Once classiﬁcation
is complete, the co-processor transitions into a deep sleep state
for the remaining time of the 12-second window (1978 ms),
dramatically reducing power consumption to 0.29 mW. Despite
the longer duration in this state, the energy consumption is
kept low at 3.47 mJ, mainly due to the reduced power require-
ments. Summing up the energy consumption for both states, the

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

94

IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS FOR ARTIFICIAL INTELLIGENCE, VOL. 1, NO. 1, SEPTEMBER 2024

Fig. 13.

Transformer model used for seizure detection.

total energy expenditure for the 12-second window amounts to
3.66 mJ. This demonstrates a highly efﬁcient energy proﬁle as
most of the time is spent in a low-power state. The power-gating
strategy and the possibility of selecting optimal voltage and
frequency settings in the VersaSens platform play crucial roles
in achieving this efﬁciency. Thus, in this case, by minimizing
both static and dynamic power consumption, the co-processor is
able to maintain prolonged operation without frequent recharg-
ing or battery replacement, which is critical for wearable health
monitoring devices.

C. Seizure Detection With Transformer

For this use case, a modiﬁed 4-layer VisionTransformer
[37] speciﬁcally adapted for epileptic seizure detection [29],
[30] serves as the core model. The transformation of each
12-seconds EEG segment through the Short-time Fourier Trans-
form (STFT) extracts time-frequency features from each EEG
channel, which are then treated as input images for the trans-
former encoder. A fully connected layer in the decoder com-
presses the output of the encoder to the necessary class
dimensions. The preprocessing steps and the architecture of the
model, key to understanding epilepsy detection, are illustrated
in Fig. 13.

To train and test

the model, we used the publicly
available Temple University Hospital EEG Seizure Corpus
(TUSZ)-v2.0.0 [38], which includes recordings from 675
individuals totaling 1476 hours. The dataset exhibits hetero-
geneity in sampling frequency. Thus, to achieve consistency,
we resampled all
following the
recommended practices [39].

recordings to 256 Hz,

TABLE V
ENERGY CONSUMPTION OF CO-PROCESSOR FOR ONE CLASSIFICATION
WINDOW (12S) WITH AND WITHOUT CGRA

Parameter
Processing time
Power Consumption
Voltage
Frequency
Energy Consumption
Total Energy

With CGRA Without CGRA

53 ms
8.86 mW
830 mV
160 MHz
0.47 mJ
3.93 mJ

79 ms
8.83 mW
830 mV
160 MHz
0.70 mJ
4.16 mJ

Deep Sleep
11947 ms
0.29 mW
830 mV
32 KHz
3.46 mJ

detection [40]. In our work, an AUC value of 0.84 is achieved
using the transformer model and the previously mentioned four
electrodes, indicating the ability of the model to distinguish
between seizure and non-seizure classes. The processing time,
average power, and energy consumption for the transformer
model are detailed in Table V. The preprocessing steps (STFT,
patch ﬂattening and embedding) are not taken into account for
this use case. Additionally, to show the potential of having
such a deeply hetereogenous SoC in VersaSens when dealing
with this type of complex applications, a comparison between
processing some parts of the transformer on the CGRA or on
the CPU is also shown. For both scenarios and to get a fair
comparison, we set the same voltage and frequency settings.

Results presented in Table V verify that using the CGRA
implies a reduction of energy consumed during the processing
period. Furthermore, a speedup of up to 1.5 in the processing
time is achieved, giving a minimum execution time of 53ms
suitable for a real-time system, since it is lower than the 12s of
the acquiring data window.

As for the previous application,

the Transformer archi-
tecture is executed on the HEEPocrates co-processor. While
16-bit ﬁxed-point arithmetic is used for linear operations within
the transformer, non-linear functions such as Softmax, Nor-
malization, and GELU activation utilize a 32-bit ﬂoating-point
unit. Moreover, we selected an optimal setting for the voltage
and frequency as described in [36]. Speciﬁcally, the chosen
conﬁguration operates the co-processor at the highest frequency
supported at the lowest voltage, i.e. 160 MHz with a voltage
of 830 mV while processing. Similar to the HBC, once the
classiﬁcation is complete, the system transitions to the deep
sleep mode until the next classiﬁcation.

Finally, the performance of the model is evaluated using
the AUC (Area Under the Curve) metric, which is recognized
for its efﬁcacy in binary classiﬁcation tasks such as seizure

VI. CONCLUSION

This paper has introduced VersaSens, an innovative and new
versatile wearable multi-sensing platform concept to advance
research in edge-AI based wearable technologies. VersaSens
addresses key challenges in the ﬁeld by offering a tool to pro-
mote the development and enhancement of the next generation
wearable sensor systems. The architecture design and physical
realization of the platform, as detailed in this paper, exempliﬁes
its core attributes of versatility, ﬂexibility, and extendability
with various hardware, software, and processing components.
To demonstrate the platform’s capabilities, three edge-AI
use cases of medical wearables have been tested with notable
results. First, in the cough-frequency monitoring case, Ver-
saSens was able to process two modalities at different frequency

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

NAJAFI et al.: VERSASENS: AN EXTENDABLE MULTIMODAL PLATFORM FOR NEXT-GENERATION EDGE-AI WEARABLES

95

within their respective short windows to reach the desired out-
come. The processing was fast enough to allow an efﬁcient
switch to idle mode, thus achieving optimized energy consump-
tion. Second, in the heartbeats classiﬁcation, the system efﬁ-
ciently processed ECG data while achieving a very low energy
consumption of 3.66 mJ for a 12-second classiﬁcation window.
In the last case of seizure detection using transformers, the
integration of hardware accelerators seamlessly (a key feature
of VersaSens extendability) signiﬁcantly reduced energy con-
sumption and processing time in comparison to the latest SoC
designs. Thus, a total energy reduction is obtained from 4.16 mJ
to 3.93 mJ (approximately 8% less), and, more importantly
in the context of real-time operation of the next-generation of
edge-AI wearables, a much lower execution time (33% less) is
achieved (from 79 ms to 53 ms).

Finally, the presented VersaSens platform concept can be
modiﬁed to meet various requirements. For instance, the Main
module can incorporate different SoCs, sensor modules can
integrate various types of AFEs or custom-designed AFEs, and
the co-processor unit can utilize alternative SoCs with advanced
hardware accelerators. Additionally, multiple co-processors can
concurrently manage different applications on physiological
signals in real-time. The software and operating modes of the
system are also customizable. Furthermore, several VersaSens
sensors can collaborate via a wireless network, enabling the
execution of more complex deep learning models, such as
federated learning models. This extendability, combined with
the platform’s modular architecture and advanced edge-AI pro-
cessing capabilities, ensures that VersaSens can support a wide
range of wearable applications in digital health, wellness, and
complex multi-modal edge-AI medical applications. For future
research, we will use the current version of the VersaSens
platform in a series of studies on medical and wearable systems
in multiple applications. These studies will involve comprehen-
sive experiments to evaluate the usability of the platform and
to assess its capabilities for continuous real-time training and
inference.

REFERENCES

[1] S. Machetti, P. D. Schiavone, C. T. Müller, A. S. J. Levisse, M. Peon
Quiros, and D. Atienza Alonso, “HEEPocrates: An ultra-low-power
RISC-V microcontroller for edge-computing healthcare applications,”
in Europractice, 2024.

[2] WHO, Global Strategy on Digital Health 2020-2025. Geneva, Switzer-
land: World Health Organization, Licence: CC BY-NC-SA 3.0
IGO, 2021.

[3] B. A. Jnr, “Use of telemedicine and virtual care for remote treatment in
response to COVID-19 pandemic,” J. Med. Syst., vol. 44, no. 7, 2020,
Art. no. 132.

[4] A. M. Vicente, W. Ballensiefen, and J.-I. Jönsson, “How personalised
medicine will transform healthcare by 2030: The icpermed vision,”
J. Translational Med., vol. 18, no. 1, pp. 1–4, Apr. 2020.

[5] M. A. Hamburg and F. S. Collins, “The path to personalized medicine,”

New England J. Med., vol. 363, no. 4, pp. 301–304, 2010.

[6] J. Hester et al., “Amulet: An energy-efﬁcient, multi-application wearable
platform,” in Proc. 14th ACM Conf. Embedded Netw. Sensor Syst.
CD-ROM, 2016, pp. 216–229.

[7] J. Wittmann, F. Cannillo, D. Ciomaga, M. Jefremow, and F. Rigoni,
Highly Efﬁcient Power Management
in Wearables and IoT De-
vices. Cham, Switzerland: Springer International Publishing, 2020,
pp. 125–142.

[8] S. Ki, G. Byun, K. Cho, and H. Bahn, “Co-optimizing cpu voltage,
memory placement, and task ofﬂoading for energy-efﬁcient mobile
systems,” IEEE Internet Things J., vol. 10, no. 10, pp. 9177–9192,
May 2023.

[9] T. Aminosharieh Najaﬁ, A. Affanni, R. Rinaldo, and P. Zontone,
“Drivers’ mental engagement analysis using multi-sensor fusion ap-
proaches based on deep convolutional neural networks,” Sensors,
vol. 23, no. 17, Art. no. 7346, 2023.

[10] V. Kartsch, G. Tagliavini, M. Guermandi, S. Benatti, D. Rossi, and L.
Benini, “BioWolf: A sub-10-mW 8-channel advanced brain–computer
interface platform with a nine-core processor and ble connectivity,” IEEE
Trans. Biomed. Circuits Syst., vol. 13, no. 5, pp. 893–906, Oct. 2019.

[11] H. P. Da Silva, J. Guerreiro, A. Lourenço, A. Fred, and R. Martins,
“BITalino: A novel hardware framework for physiological computing,”
in Proc. Int. Conf. Physiol. Comput. Syst., vol. 2, Rijeka, Croatia:
SciTech, 2014, pp. 246–253.

[12] H. J. Han, S. Labbaf, J. L. Borelli, N. Dutt, and A. M. Rahmani,
“Objective stress monitoring based on wearable sensors in everyday
settings,” J. Med. Eng. & Technol., vol. 44, no. 4, pp. 177–189, 2020.
[13] D. R. Seshadri et al., “Wearable sensors for monitoring the physiological
and biochemical proﬁle of the athlete,” NPJ Digit. Med., vol. 2, no. 1,
2019, Art. no. 72.

[14] A. N. Patel, T.-P. Jung, and T. J. Sejnowski, “A wearable multi-
modal bio-sensing system towards real-world applications,” IEEE Trans.
Biomed. Eng., vol. 66, no. 4, pp. 1137–1147, Apr. 2019.

[15] C.-T. Lin, C.-Y. Wang, K.-C. Huang, S.-J. Horng, and L.-D. Liao,
“Wearable, multimodal, biosignal acquisition system for potential critical
and emergency applications,” Emergency Med. Int., vol. 2021, Jun. 2021,
Art. no. 9954669.

[16] A. von Lühmann, H. Wabnitz, T. Sander, and K.-R. Müller, “M3BA:
A mobile, modular, multimodal biosignal acquisition architecture for
miniaturized EEG-NIRS-based hybrid BCI and monitoring,” IEEE
Trans. Biomed. Eng., vol. 64, no. 6, pp. 1199–1210, Jun. 2017.
[17] A. S. Carmo, M. Abreu, A. L. N. Fred, and H. P. da Silva, “EpiBOX:
An automated platform for long-term biosignal collection,” Frontiers
Neuroinformatics, vol. 16, 2022, Art. no. 837278.

[18] A. von Luhmann, H. Wabnitz, T. Sander, and K.-R. Muller,
“M3baM3BA: A mobile, modular, multimodal biosignal acquisition
architecture for miniaturized EEG-NIRS-based hybrid BCI and mon-
itoring,” IEEE Trans. Biomed. Eng., vol. 64, no. 6, pp. 1199–1210,
Jun. 2017.

[19] F. Dell’Agnola, U. Pale, R. Marino, A. Arza, and D. Atienza,
“MBioTracker: Multimodal self-aware bio-monitoring wearable system
for online workload detection,” IEEE Trans. Biomed. Circuits Syst.,
vol. 15, no. 5, pp. 994–1007, Oct. 2021.

[20] R. Donati, V. Kartsch, L. Benini, and S. Benatti, “BioWolf16: A
16-channel, 24-bit, 4kSPS ultra-low power platform for wearable
clinical-grade bio-potential parallel processing and streaming,” in Proc.
44th Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. (EMBC), 2022,
pp. 2518–2522.

[21] V. Toral et al., “A versatile wearable based on reconﬁgurable hard-
ware for biomedical measurements,” Measurement, vol. 201, 2022,
Art. no. 111744. [Online]. Available: https://www.sciencedirect.com/
science/article/pii/S0263224122009484

[22] G. Nazari, P. Bobos, J. C. MacDermid, K. E. Sinden, J. Richardson,
and A. Tang, “Psychometric properties of the Zephyr bioharness device:
A systematic review,” BMC Sports Sci., Med. Rehabil., vol. 10, pp. 1–
8, Feb. 2018.

[23] H. H. Jasper, “The ten-twenty electrode system of the International
Federation,” Electroencephalogr. Clin. Neurophysiol., vol. 52, pp. 3–
6, 1999.

[24] P. D. Schiavone et al., “X-HEEP: An open-source, conﬁgurable and
extendible RISC-V microcontroller,” in Proc. 20th ACM Int. Conf.
Comput. Frontiers, 2023, pp. 379–380.

[25] R. R. Álvarez, B. Denkinger, J. Sapriza, J. M. Calero, G. Ansaloni, and
D. A. Alonso, “An open-hardware coarse-grained reconﬁgurable array
for edge computing,” in Proc. 20th ACM Int. Conf. Comput. Frontiers,
2023, pp. 391–392.

[26] W. A. Simon, Y. M. Qureshi, A. Levisse, M. Zapater, and D. Atienza,
“BLADE: A bitline accelerator for devices on the edge,” in Proc. Great
Lakes Symp. VLSI, 2019, pp. 207–212.

[27] L. Orlandic, J. Thevenot, T. Teijeiro, and D. Atienza, “A multimodal
dataset for automatic edge-AI cough detection,” in Proc. 45th Annu.
Int. Conf. IEEE Eng. Med. & Biol. Soc. (EMBC), Piscataway, NJ, USA:
IEEE Press, 2023, pp. 1–7.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply. 

96

IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS FOR ARTIFICIAL INTELLIGENCE, VOL. 1, NO. 1, SEPTEMBER 2024

[28] E. De Giovanni et al., “Modular design and optimization of biomedical
applications for ultralow power heterogeneous platforms,” IEEE Trans.
Comput.-Aided Des. Integr. Circuits Syst., vol. 39, no. 11, pp. 3821–
3832, Nov. 2020.

[29] Y. Ma et al., “TSD: Transformers for seizure detection,” bioRxiv,

pp. 2023–01, 2023.

[30] A. Amirshahi, J. Dan, J. A. Miranda Calero, A. Aminifar, and D. Atienza
Alonso, “FETCH: A fast and efﬁcient technique for channel selection
in EEG wearable systems,” in Proc. Conf. Health, Inf., Learn., 2024.

[31] D. A. R. Braojos, G. Ansaloni and F. Rincon, “Embedded realtime ECG
delineation methods: A comparative evaluation,” in Proc. IEEE Int. Conf.
Bioinformat. Bioeng. (BIBE), 2012, pp. 00–104.

[32] L. Orlandic, E. De Giovanni, A. Arza, S. Yazdani, J.-M. Vesin, and
D. Atienza, “REWARD: Design, optimization, and evaluation of a real-
time relative-energy wearable r-peak detection algorithm,” in Proc. 41st
Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. (EMBC), Piscataway, NJ,
USA: IEEE Press, 2019, pp. 3341–3347.

[33] E. De Giovanni, A. Aminifar, A. Luca, S. Yazdani, J.-M. Vesin, and
D. Atienza, “A patient-speciﬁc methodology for prediction of parox-
ysmal atrial ﬁbrillation onset,” in Proc. Comput. Cardiol. (CinC),
Piscataway, NJ, USA: IEEE Press, 2017, pp. 1–4.

[34] R. Braojos, G. Ansaloni, and D. Atienza, “A methodology for embedded
classiﬁcation of heartbeats using random projections,” in Proc. Des.,
Automat. & Test Europe Conf. & Exhib. (DATE), Piscataway, NJ, USA:
IEEE Press, 2013, pp. 899–904.

[35] G. Moody and R. Mark, “The impact of the MIT-BIH arrhythmia
database,” IEEE Eng. in Med. Biol. Mag., vol. 20, no. 3, pp. 45–50,
May/Jun. 2001.

[36] H. Taji, J. Miranda, M. Pe’on-Quir’os, and D. Atienza, “Energy-
efﬁcient frequency selection method for bio-signal acquisition in AI/ML
wearables,” in Proc. ACM/IEEE Int. Symp. Low Power Electron. Des.,
2024, pp. 1–6.

[37] A. Dosovitskiy et al., “An image is worth 16x16 words: Transformers

for image recognition at scale,” 2020, arXiv:2010.11929.

[38] I. Obeid and J. Picone, “The temple university hospital EEG data

corpus,” Frontiers Neurosci., vol. 10, 2016, Art. no. 196.

[39] J. Dan et al., “SzCORE: A seizure community open-source research
evaluation framework for the validation of EEG-based automated seizure
detection algorithms,” 2024, arXiv:2402.13005.

[40] S. Tang et al., “Self-supervised graph neural networks for

im-
proved electroencephalographic seizure analysis,” 2021, arXiv:2104.
08336.

Authorized licensed use limited to: Universität zu Köln USB Köln. Downloaded on November 21,2025 at 14:13:14 UTC from IEEE Xplore.  Restrictions apply.
