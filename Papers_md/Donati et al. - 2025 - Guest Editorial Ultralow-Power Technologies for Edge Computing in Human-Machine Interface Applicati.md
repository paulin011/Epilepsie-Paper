# Donati et al. - 2025 - Guest Editorial Ultralow-Power Technologies for Edge Computing in Human-Machine Interface Applicati

2

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 19, NO. 1, FEBRUARY 2025

Guest Editorial: Ultralow-Power Technologies for
Edge Computing in Human-Machine Interface
Applications

W EARABLE healthcare devices are revolutionizing how

we monitor and manage health, offering real-time data
and personalized insights that empower both patients and clini-
cians. From tracking heart rhythms to detecting neurological disor-
ders and enhancing prosthetic control, these devices promise to
transform the delivery of healthcare. However, despite their
immense potential, wearable devices face persistent challenges,
including the need for ultralow power consumption to prolong bat-
tery life, computational limitations in resource-constrained envi-
ronments, and maintaining accuracy across diverse users and real-
world conditions. Addressing these hurdles requires a multidisci-
plinary approach, combining advances in biosignal processing,
innovative hardware-software co-integration, and energy-efﬁcient
architectures. The research articles presented in this Special Sec-
tion exemplify this synergy, showcasing state-of-the-art solutions
that push the boundaries of what wearable healthcare technology
can achieve.

This Special Section serves as a pivotal platform to propel
research in biomedical circuits and systems within the CAS
community, advancing the state-of-the-art in this rapidly evolv-
ing ﬁeld. It comprises 8 selected papers from a competitive pool
of 23 submissions, representing an acceptance rate of (cid:1)35%.
the latest breakthroughs in
These contributions highlight
ultralow-power technologies and provide a glimpse into the
future of wearable healthcare systems.

A recurring theme in this Special Section is the challenge of
handling variability in biosignals while maintaining low-power
consumption. In Loh et al. [1], the authors tackle domain gener-
alization (DG) for electrocardiography (ECG) signals, introduc-
ing correction layers that enhance robustness against domain
shifts without signiﬁcantly increasing computational complex-
ity. This novel approach improves classiﬁcation accuracy while
optimizing memory and energy use, making it highly suitable
for wearable edge devices. Lee et al. [2] addresses arrhythmia
detection, proposing a lightweight convolutional neural network
(CNN) combined with R-peak interval features to capture long-
term rhythm information. The resulting system, implemented in
custom hardware, achieves high classiﬁcation accuracy with
ultralow latency and power consumption, demonstrating the
effectiveness of hardware-software co-design for ECG analysis.
The need for continuous and real-time monitoring is particu-
larly evident in epilepsy management. Zhang et al. [3] presents a
distributed-aggregated classiﬁcation architecture that leverages
spiking neural networks (SNNs) for event-driven, energy-efﬁ-
cient seizure detection. By reusing hardware resources and

avoiding redundant standby systems, the architecture achieves
remarkable energy savings while maintaining high detection
accuracy. Similarly, in another study, Lee et al. [4], proposes a
RISC-V-based deep learning accelerator capable of real-time sei-
zure detection and model personalization. This programmable
architecture supports both inference and training directly on the
device, addressing the unique challenges of adapting to individual
patient needs in real-world settings.

Neuromorphic computing emerges as a powerful approach in
several studies, highlighting its potential for wearable healthcare.
In O’Leary et al. [5], the authors develop a brain-state classiﬁcation
processor that integrates resonate-and-ﬁre neurons and decision
forests to deliver high accuracy for electroencephalography
(EEG)-based closed-loop neuromodulation. With its multiplier-
less architecture and state-of-the-art energy efﬁciency, this work
showcases the potential of neuromorphic designs for low-power,
real-time brain monitoring. Another neuromorphic innovation,
from Scrugli et al. [6], leverages SNNs to process surface electro-
myography (sEMG) signals for prosthetic control. The proposed
FPGA-based system efﬁciently handles both discrete gesture rec-
ognition and continuous ﬁnger force modelling, offering a glimpse
into the future of low-power human-machine interfaces.

System-level innovations also feature prominently in this
Special Section, providing frameworks for optimizing edge
healthcare applications. The ACE methodology presented by
Wang et al. [7] introduces an iterative classiﬁcation framework
that adapts computational complexity during runtime, ensuring
efﬁciency without sacriﬁcing accuracy. By automating the opti-
mization and deployment of algorithms on edge platforms, this
work reduces runtime and energy costs signiﬁcantly, making it
accessible for a wide range of biomedical applications. In
another direction, a study on analog computing by Alimisis et al.
[8] highlights the resurgence of analog architectures in health-
care. By implementing a low-power voting classiﬁer for diabe-
tes prediction, the authors demonstrate how analog computing
can achieve exceptional accuracy while minimizing energy use,
offering a compelling alternative to purely digital systems.

Collectively, these studies push the boundaries of what is pos-
sible in wearable healthcare technologies. By addressing chal-
lenges at every stage—biosignal acquisition, algorithm design,
hardware optimization, and system integration—they lay the
groundwork for devices that are not only energy-efﬁcient but
also capable of delivering real-time, personalized insights. This
Special Section celebrates the convergence of innovative engi-
neering and practical medical applications, heralding a future

1932-4545 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies.
Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS

3

where wearable devices seamlessly integrate into our lives to
enhance health and well-being.

, Member, IEEE

ELISA DONATI
Institute of Neuroinformatics, University of Zurich and
ETH Zurich, 8057 Zurich, Switzerland
e-mail: elisa@ini.uzh.ch

BO ZHAO , Senior Member, IEEE
Zhejiang University, Hangzhou 310027, China

SIMONE BENATTI
University of Modena and Reggio Emilia, 41121
Modena, Italy

, Member, IEEE

, Member, IEEE
ANDREA COSSETTINI
ETH Zurich, 8092 Z€urich, Switzerland

REFERENCES

[1] J. Loh, L. Dudchenko, J. Viga, and T. Gemmeke, “Towards hardware
supported domain generalization in DNN-based edge computing devices
for health monitoring,” IEEE Trans. Biomed. Circuits Syst., early
access, Jun. 24, 2024, doi: 10.1109/TBCAS.2024.3418085.

[2] S.-Y. Lee, M.-Y. Ku, W.-C. Tseng, and J.-Y. Chen, “AI accelerator
time-period CNN-based model for arrhythmia
with ultralight-weight
classiﬁcation,” IEEE Trans. Biomed. Circuits Syst., early access, Jul. 30,
2024, doi: 10.1109/TBCAS.2024.3435718.

[3] Q. Zhang, M. Cui, Y. Liu, W. Chen, and Z. Yu, “Low-power and low-cost
AI processor with distributed-aggregated classiﬁcation architecture for
wearable epilepsy seizure detection,” IEEE Trans. Biomed. Circuits Syst.,
early access, Aug. 28, 2024, doi: 10.1109/TBCAS.2024.3450896.

[4] S.-Y. Lee, M.-Y. Ku, Y.-H. Tsai, and C.-C. Lin, “RVDLAHA: An
RISC-V DLA hardware architecture for on-device real-time seizure
detection and personalization in wearable applications,” IEEE Trans.
Biomed. Circuits Syst., early access, Aug. 13, 2024, doi: 10.1109/
TBCAS.2024.3442250.

[5] G. O’Leary et al., “BrainForest: Neuromorphic multiplier-less bit-serial
classiﬁcation
weight-memory-optimized
1024-tree
processor,” IEEE Trans. Biomed. Circuits Syst., early access, Oct. 16,
2024, doi: 10.1109/TBCAS.2024.3481160.

brain-state

[6] M. A. Scrugli, G. Leone, P. Busia, L. Raffo, and P. Meloni, “Real-time
sEMG processing with spiking neural networks on a low-power
5K-LUT FPGA,” IEEE Trans. Biomed. Circuits Syst., early access, Sep.
9, 2024, doi: 10.1109/TBCAS.2024.3456552.

[7] Y. Wang, L. Orlandic, S. Machetti, G. Ansaloni, and D. Atienza, “ACE:
Automated optimization towards iterative classiﬁcation in edge health
monitors,” IEEE Trans. Biomed. Circuits Syst., early access, Sep. 25,
2024, doi: 10.1109/TBCAS.2024.3468160.

[8] V. Alimisis, C. Aletraris, N. P. Eleftheriou, E. A. Serlis, A. James, and
P. P. Sotiriadis, “Low-power analog integrated architecture of the voting
classiﬁcation algorithm for diabetes disease prediction,” IEEE Trans.
Biomed. Circuits Syst., early access, Jul. 2, 2024, doi: 10.1109/TBCAS.
2024.3421313.

4

IEEE TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS, VOL. 19, NO. 1, FEBRUARY 2025

Elisa Donati (Member, IEEE) received the B.Sc. and M.Sc. degrees in biomedical engineering
from the University of Pisa, Pisa, Italy, and the Ph.D. degree in biorobotics from Sant’Anna
School of Advanced Studies, Pisa. Currently, she is a Research Fellow with the Institute of Neuro-
informatics, University of Z€urich and ETH Z€urich, and a Group Leader with the ZNZ Center
where her research lies at the intersection of neuroscience, neuromorphic engineering, and biomed-
ical applications. Her research includes developing closed-loop systems for neural interfaces, creat-
ing neuromorphic sensors and algorithms for processing biomedical signals, and exploring spiking
neural networks for real-time sensory encoding. She served as the Co-Coordinator of the H2020
EU CSA Project NEUROTECH, she was also awarded a Prestigious Marie Curie IF on EMG sig-
nal processing using neuromorphic approaches. Additionally, she has received other Swiss and
European Grants to advance research in signal processing and embedded systems. She is dedicated
to pushing the boundaries of neuromorphic technologies for real-world applications.

Bo Zhao (Senior Member, IEEE) received the Ph.D. degree in electrical engineering from the
Department of Electronic Engineering, Tsinghua University, Beijing, China, in 2011. From 2013
to 2015, he was a Research Fellow with the National University of Singapore. From 2015 to
2018, he was an Assistant Project Scientist with Berkeley Wireless Research Center (BWRC),
Department of Electrical Engineering and Computer Sciences, University of California, Berkeley,
CA, USA. Since 2018, he has been a Professor with the Institute of VLSI Design, Zhejiang Uni-
versity, Hangzhou, China. He has authored or co-authored more than 60 articles and book chap-
ters, and he holds more than 30 Chinese patents. His research interests include IoT radios,
wireless power transfer, and wearable/implantable radios. He was a recipient of the 2017 IEEE
TRANSACTIONS ON CIRCUITS AND SYSTEMS I: REGULAR PAPERS Darlington Best Paper Award
and the Design Contest Award of the 2013 IEEE ISLPED. He is an Associate Editor for IEEE
TRANSACTIONS ON BIOMEDICAL CIRCUITS AND SYSTEMS and an Associate Editor for IEEE
TRANSACTIONS ON CIRCUITS AND SYSTEMS I: REGULAR PAPERS. He is also a Committee Member
of IEEE/C/SM. He was the Publication Chair of the 2016 IEEE BioCAS. In 2022, he was elected to be the Chair-Elect of IEEE
Biomedical and Life Science Circuits and Systems Technical Committee.

Simone Benatti (Member, IEEE) received the Ph.D. degree in electronics, telecommunications,
and information technologies from the University of Bologna under the supervision of Prof. Luca
Benini. During his Ph.D., he was a Visiting Fellow with the BWRC–University of California,
Berkeley (Supervisor: Prof. Jan Rabaey). In 2023, he was appointed as a Visiting Professor with
the EFCL-ETHZ. Currently, he serves as an Associate Professor with the University of Modena e
Reggio Emilia, while pursuing his collaboration with IIS-ETH in Zurich. His research interests
include energy-efﬁcient embedded systems for IoT and biomedical applications. This includes
hardware/software codesign to efﬁciently address performance, as well as advanced algorithms. He
works on designing and optimizing energy-efﬁcient embedded systems for biopotential (ExG)
acquisition and processing, and biosignal-based HMIs. In this ﬁeld, he has published more than 100
papers in international peer-reviewed conferences and journals. He has ongoing collaborations with
several international research institutes, such as ETHZ-EFCL, EPFL, TU Graz, FBK, and Politec-
nico di Torino. He is the recipient of the GHAIA Grant (H2020-MSCA-RISE-2017, G.A. 777822).

Andrea Cossettini (Member, IEEE) received the Ph.D. degree in electronic engineering from the
University of Udine, Udine, Italy, in 2019, with a focus on nanoelectrode array biosensors. Previ-
ously, he was with Acreo Swedish ICT AB (Kista, Sweden), designing waveguide-to-chip transi-
tions at sub-mm waves, and with Inﬁneon Technologies (Villach, Austria), working on signal
integrity for high-speed serial interfaces. Currently, he is with ETH Z€urich, Z€urich, Switzerland,
serving as a Research Cooperation Manager of the ETH Future Computing Laboratory (EFCL), a
Project Leader with the Integrated Systems Laboratory (IIS), and a Lecturer. His research interests
are in biomedical circuits and systems, with a special focus on wearable/high-speed ultrasound
and wearable EEG.
