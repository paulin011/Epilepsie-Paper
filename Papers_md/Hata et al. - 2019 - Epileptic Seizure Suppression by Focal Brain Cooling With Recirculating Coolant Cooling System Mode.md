# Hata et al. - 2019 - Epileptic Seizure Suppression by Focal Brain Cooling With Recirculating Coolant Cooling System Mode

162

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 27, NO. 2, FEBRUARY 2019

Epileptic Seizure Suppression by Focal Brain
Cooling With Recirculating Coolant Cooling
System: Modeling and Simulation

Kei Hata, Koichi Fujiwara , Member,IEEE, Takao Inoue, Takuto Abe, Takatomi Kubo, Member,IEEE,
Toshitaka Yamakawa , Member,IEEE, Sadahiro Nomura, Hirochika Imoto, Michiyasu Suzuki,
and Manabu Kano , Member,IEEE

Abstract— A focal brain cooling system for treatment of
refractory epilepsy that is implantable and wearable may
permit patients with this condition to lead normal daily lives.
We have developed such a system for cooling of the epilep-
tic focus by delivery of cold saline to a cooling device that
is implanted cranially. The outﬂow is pumped for circulation
and cooled by a Peltier device. Here, we describe the design
of the system and evaluate its feasibility by simulation.
Mathematical models were constructed based on equations
of ﬂuid dynamics and data from a cat model. Computational
ﬂuid dynamics simulations gave the following results: 1) a
cooling device with a complex channel structure gives a
more uniform temperature in the brain; 2) a cooling period
of <10 min is required to reach an average temperature of
25.0◦C at 2 mm below the brain surface, which is the target
temperature for seizure suppression. This time is short
enough for cooling of the brain before seizure onset after
seizure prediction by an intracranial electroencephalogram-
based algorithm; and 3) battery charging would be required
once every several days for most patients. These results
suggest that the focal brain cooling system may be clinically
applicable.

Index Terms— Computational ﬂuid dynamics, epilepsy,

focal brain cooling, Pennes bioheat equation, titanium.

Manuscript received October 21, 2018; revised January 2, 2019;
accepted January 2, 2019. Date of publication January 7, 2019; date
of current version February 8, 2019. This work was supported in part by
JSPS KAKENHI under Grant JP15H05719 and in part by AMED SENTAN
under Grant 17934809. (Correspondingauthor:KoichiFujiwara.)

K. Hata, T. Abe, and M. Kano are with the Department of Systems

Science, Kyoto University, Kyoto 615-8085, Japan.

K. Fujiwara is with the Department of Systems Science, Kyoto
University, Kyoto 615-8085, Japan, and also with the Department of
Material Engineering, Nagoya University, Nagoya 464-8601, Japan
(e-mail: fujiwara.koichi@material.nagoya-u.ac.jp).

T. Inoue and M. Suzuki are with the Department of Neurosurgery,

School of Medicine, Yamaguchi University, Ube 753-8511, Japan.

T. Kubo is with the Department of Information Science, Nara Institute

of Science and Technology, Ikoma 630-0192, Japan.

T. Yamakawa is with the Department of Computer Science and Elec-
trical Engineering, Kumamoto University, Kumamoto 860-8555, Japan.
S. Nomura and H. Imoto are with the Department of Neurosurgery,
School of Medicine, Yamaguchi University, Ube 753-8511, Japan,
and also with the Epilepsy Center, Yamaguchi University Hospital,
Ube 755-0046, Japan.

Digital Object Identiﬁer 10.1109/TNSRE.2019.2891090

I. INTRODUCTION

E PILEPSY refers to a group of chronic disorders that are

associated with excessive neuronal activity in the cere-
brum and characterized by recurrent seizures that may man-
ifest as convulsion, consciousness disturbance, or an unusual
sensation. Epileptic seizures increase the risk of injury and
affect social activities of patients, including a limitation or pro-
hibition against acquiring a driving license in many countries.
Epileptic patients constitute about 1% of the population, and
in 25% current treatments do not relieve seizures [1], [2]. Anti-
epileptic drugs eliminate seizures in two-thirds of patients and
are generally the ﬁrst treatment option [3]. Surgery is used
for patients who do not respond to these drugs, but the only
surgical option is resection of the epileptic focus with high
neuronal activity. This cannot be achieved for an epileptic
focus located in the supeﬁcial cortical surface because of
the difﬁculty of surgery for neocortical epilepsy involving
a functional area [4]. Such cases are treated by palliative
surgical options such as callosotomy, vagus nerve stimulation,
and responsive neurostimulation, but these procedures do not
eliminate seizures. This background indicates the need for a
new approach to treatment of epilepsy.

Focal brain cooling involves application of hypothermia to
the epileptic focus. Evidence for the efﬁcacy of this method
includes the suppression of stimulation-evoked seizures in
intraoperative brain mapping within 5-10 s by pouring cold
Ringer’ s lactate solution over the surface of the stimulated
cortex [5]. In addition, interictal epileptiform activity can be
suppressed by treatment of the brain surface with cold saline
close to the epileptic focus [6].

Cooling of layers II and III in the gray matter underlies
the suppressive effect of focal brain cooling [7], with a
target temperature in this region of 25-30 ◦C [8]. This target
temperature was conﬁrmed in several clinical experiments in
patients with epilepsy. Therapeutic whole-body hypothermia
under 33◦ has a preventive effect on status epilepticus [9].
Fujii et al. [10] reported that epileptic discharges of EEG
diminished during cooling when the brain surface temperature

1534-4320 © 2019 IEEE. Translations and content mining are permitted for academic research only. Personal use is also permitted, but republication/
redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

HATA etal.: EPILEPTIC SEIZURE SUPPRESSION BY FOCAL BRAIN COOLING

163

reached less than 25◦C. Seizures in a patient with refractory
epilepsy were suppressed when the brain temperature was
cooled to 28◦C or 30◦C by focal brain cooling under an awake
condition [11]. Sourek and Travnicek [12] tested focal brain
cooling below 24◦C in 15 patients, and found that seizures
were reduced in 11 patients and unaltered in four.

To cool

these layers to 25 ◦C, a device applied to
the brain surface needs to cool the surface temperature to
<25 ◦C. The temperature of the brain surface may need
to be 10-20◦C, depending on the individual and the target
region for cooling [8], [13], [14]. Application of penicillin
G solution or cobalt powder to the brain surface in rats,
followed by placement of a Peltier cooling device on the
application area, caused frequent seizures if the device was
not activated. Less frequent seizures occurred in rats with brain
surfaces cooled to 20 ◦C or 15 ◦C by the Peltier device, and
those with brain surfaces at 10 ◦C had no seizures [13]. An
epileptic electroencephalogram (EEG) discharge induced by
kainic acid was also suppressed by cooling the brain surface to
14.8 ± 1.5 ◦C with the Peltier device [8], and seizures induced
by injection of 4-aminopyridine solution were signﬁcantly
reduced in duration by cooling the brain surface to about
20 ◦C [14]. Contact of a cooling device with the brain surface
at 0-10 ◦C does not cause irreversible side effects. Among
rats in which the brain surface was maintained at 20, 15, 10,
5, 0, or −5 ◦C for an hour, only rats maintained at −5 ◦C
had a reversible decrease in motor function and irreversible
histological damage [15]. Long et al. [16] found that cooling
of the Broca region and the speech motor cortex in awake
neurosurgical patients affected speech timing and articulation.
Impairment in ﬁnger movements was observed when the brain
surface of a monkey was cooled to 10 ◦C by a Peltier device,
but
the ﬁngers were not completely paralyzed [17]. Two
human patients had apparent temporal disruption of motor
speech functions when focal hypothermia was applied to the
Broca region with a stainless-steel chamber in which saline
was circulating at 1-3 ◦C [18].

Several techniques for brain cooling have been proposed,
including injection of cold ﬂuid into blood vessels and cover-
ing patients with cooling blankets [19]. While these techniques
reduce the body core temperature, it is unrealistic to lower the
core temperature to 25 ◦C, even under anesthesia. Packing
the head with ice can also be used, such that the steady-state
brain surface temperature is about 20 ◦C; however, simulations
under this condition suggest that the temperature in layers II
and III would not be reduced to 25 ◦C [20].

A Peltier device provides one approach for cooling of the
brain. This device generates a temperature difference of several
tens of degrees Celsius between the hot and cold sides. Focal
brain cooling systems using the Peltier device have been
tested in clinical trials before resection of the epileptic focus,
as well as in animal experiments. Fujii et al. [13] found
that cooling the epileptic focus with an implantable Peltier
device in direct contact with the brain suppressed epileptic
seizures in a free-moving rat modelmodels. Nomura et al. [21]
used a Peltier device for cooling the epileptogenic cortex in
patients and found intraoperatively that epileptic discharges on
electrocorticography (ECoG) were eliminated in the cooling

Fig. 1. Focal brain cooling system with RCC.

period and reappeared upon rewarming. The cortical GABA
level also decreases signiﬁcantly from the control level during
cooling in patients [22]. Although the Peltier device can be
used in a focal brain cooling system, safety is a concern in
placing this device in direct contact with the brain because it
is not biocompatible and a large electrical current is required
for its function.

Recirculating coolant cooling (RCC) has been proposed to
avoid these problems. The coolant is cooled outside the body,
ﬂows into a cooling device attached to the brain, removes heat
from the brain, and is then cooled again outside the body. RCC
permits adequate cooling and provides a therapeutic effect,
based on studies by King et al [56]. using a RCC brain
cooling system in a traumatic brain injury monkey model,
and development by Inoue et al. [23] of a RCC titanium
cooling plate that covers the epileptic focus. Experiments in
cat and monkey models showed that the titanium cooling plate
cooled the focal cortical temperature sufﬁciently for seizure
suppression. These results suggest that brain cooling with RCC
is a promising therapy for epilepsy.

Our aim is clinical application of a RCC focal brain cooling
system so that patients with refractory epilepsy can lead nor-
mal daily lives. Patients who would beneﬁt from this system
are those with an epileptic focus in the gyrus because this
location is easy to cool with a device on the brain surface [4],
while surgical treatment of neocortical epilepsy in a functional
area (e.g., eloquent cortex) is difﬁcult.

To achieve focal brain cooling with RCC, its feasibility has
to be investigated through simulation before clinical trials with
patients. In the present work, we developed a mathematical
models for the whole brain cooling system. Based on the
developed model, an optimal cooling device was designed
from the perspectives of the pressure drop in the device and
cooling performance, because the pump size increases as the
pressure drop increases. The designed device was evaluated
using computational ﬂuid dynamics (CFD) simulations.

this report did not

A preliminary version of this work has been described [24],
but
include the experiment in the cat
model or the channel structure optimization in the cooling
device.

II. BRAIN COOLING SYSTEM

Our RCC brain cooling system is shown schematically in
Fig. 1. The patient wears a jacket with two chest pockets, one
of which contains a Peltier device in contact with a tank of
saline that is connected to a titanium cooling device implanted
just above the epileptic focus in the skull. The circulating

164

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 27, NO. 2, FEBRUARY 2019

saline is cooled by the Peltier device while in the tank, and
then ﬂows into the cooling device under pressure from a pump
attached to the chest. The cooled saline removes heat from
the brain and then ﬂows back into the tank. Heat sinks are in
contact with the cold and hot sides of the Peltier device, and
this device and the pump are powered by a mobile battery that
is also attached to the chest. The pump and battery are located
extracorporeally and there is a risk of infection, but this kind of
conﬁguration is not uncommon in medical devices. For exam-
ple, some types of ventricular assist devices have a pump and
battery in this location [32], [33]. Over 2500 FDA-approved
mechanical circulatory support devices (MCSs), including left
ventricular assist devices (LVADs), were implanted in 2016 in
the US [34], and the prevalence of infection was 19% at
12 months after implantation [35]. This shows that appropriate
infection risk control is also needed in a brain cooling system
with RCC.

Two cooling processes can be used: a seizure prediction-
based operation and an intermittent operation. Intracranial
EEG-based algorithms have been investigated for several
decades [36]. In the American Epilepsy Society Seizure
Prediction Challenge 2016, an area under the curve (AUC)
value of 0.81 for long-term human data was achieved by
the top algorithm [37]. In addition, a clinical trial of seizure
prediction by intracranial EEG had been accomplished [38].
These algorithms can predict epileptic seizures 89 ± 15 min
prior to their onset [39]–[41]; thus, the time for cooling the
brain must be less than that from seizure prediction to onset.
On the other hand, Yang et al. [42] proposed a method for
cooling the epileptic focus intermittently like VNS and deep
brain stimulation. Their experiments in a rat model showed
intermittent brain cooling reduces the frequency and
that
intensity of epileptic seizures.

III. SYSTEM MODEL

This section describes a mathematical model of the RCC
brain cooling system, which we refer to as the system model.
Nomenclature for all symbols is given after the Conclusion.

A. ChestDevices

The patient wears a jacket with chest devices: a battery,
fan, heat sinks, Peltier device, thermoregulator, and pump. The
speciﬁcations are shown in Table I. These devices weigh just
over 1 kg and occupy a volume of 120×100 ×70 mm on each
side of the chest. The two batteries are connected in series to
raise the voltage, and the capacity is assumed to be 10 Ah,
which is the standard capacity of mobile batteries in 2018 [25].

TABLE I
SPECIFICATION OF DEVICES ON PATIENT’S CHEST

Fig. 2. Geometrical representation of head model.

TABLE II
CHANNEL STRUCTURE IN COOLING DEVICE. THE BLUE AND RED

REGIONS REPRESENT THE INLET AND THE OUTLET OF

THE SALINE, RESPECTIVELY

top, middle, and bottom layers are 1, 5, and 1 mm thick,
respectively. Some types of epileptic lesions, such as focal
cortical dysplasia (FCD), are localized within limited regions,
and this device size is appropriate for FCD. Several kinds of
device sizes should be considered depending on brain lesions.
Three types of channel structure in the middle layer are
shown in Table II. The tubes for saline inﬂow and outﬂow are
implanted under the soft tissue layer. Models of the titanium
cooling device, saline ﬂow, and biological tissue are described
in sections III-C, III-D, and III-E, respectively.

B. ModelStructure

The main part of the system model is a hemispheric head
model (Fig. 2), which comprises a titanium cooling device,
saline, and biological tissue divided into soft tissue, skull,
cerebrospinal ﬂuid (CSF), and brain tissue [35]. The cooling
device has a three-layer structure: the top layer has an inlet
and an outlet for saline,
the middle layer has a channel,
and the bottom layer is a cooling panel in contact with the
brain. The cooling device measures 30 × 30 × 7 mm, and

C. TitaniumCoolingDevice

Temporal changes in the device temperature are calculated

by the following heat conduction equation.

cTi

∂ T
∂t

= kTi∇2T

(1)

D. SalineFlow

Temporal changes in the velocity, pressure, and temperature
of saline are modeled as follows, assuming the ﬂow to be

HATA etal.: EPILEPTIC SEIZURE SUPPRESSION BY FOCAL BRAIN COOLING

165

laminar:

ρs

∂ρs
∂t
∂u
∂t

+ ∇ · (ρsu) = 0

+ ρs(u · ∇)u = ∇ · [− pI + τ ]

ρscs(

∂ T
∂t

+ (u · ∇)T ) = − T
ρs

(cid:2)
(cid:2)
(cid:2)
(cid:2)

p

∂ρs
∂ T

(

∂ p
∂t

+ (u · ∇) p)

− (∇ · q) + τ : S

(2)

(3)

(4)

The temperature dependence of the material properties [43] is
described by

νs = 1.38 × 10

−6 − 2.12 × 10

−8T + 1.36 × 10

−10T 2

− 4.65 × 10

−13T 3 + 8.90 × 10

−16T 4

ρs = 839 + 1.40T − 3.01 × 10

−3T 2

+ 3.72 × 10

−7T 3

cs = 1.20 × 104 − 80.4T + 0.310 T 2

− 5.38 × 10

−4T 3 + 3.63 × 10

−7T 4

ks = −0.869 + 8.95 × 10

−3T − 1.58 × 10

−5T 2

+ 7.98 × 10

−9T 3.

(5)

(6)

(7)

(8)

E. BiologicalTissue

Temporal changes in the biological tissue temperature are
calculated with a modiﬁed bioheat equation, which is based on
the conventional bioheat equation proposed by Pennes [44]:

ρtisctis

∂ T
∂t

= ktis∇2 T − cbloodwtis(T − Tcore) + M.

(9)

This equation represents energy conservation. The three terms
on the right side represent the effects of heat conduction, heat
convection due to blood ﬂow, and metabolic heat production,
in order. The equation assumes that the heat convection rate
due to blood ﬂow is proportional to the temperature difference
between the tissue and the body core. Equation (9) has been
veriﬁed in several studies [45], [46].

We derived the modiﬁed Pennes bioheat equation,

ρtisctis

∂ T
∂t

= ktis∇2 T − cbloodWtis(T − Tcore),

(10)

with two modiﬁcations. The rate of production of metabolic
heat was disregarded because this is much smaller than that of
heat convection due to blood ﬂow [47]. In addition, the blood
perfusion rate wtis was replaced by Wtis. The value of Wtis
differs between the brain and other tissues (0 in CSF, skull,
and soft tissue). Wtis in the brain was determined in an animal
model to ﬁt the theoretical temperature distribution to the
experimental distribution. The details of this experiment are
described in section. IV.

Fig. 3. Peltier device. (a) Basic unit. (b) Typical structure.

F. InitialandBoundaryConditionsofHeadModel

The boundary condition deﬁnes the outer surface of the head
model as thermally insulated except for the saline inlet and
outlet. The boundary condition for a steady state simulation is
Tin,h = Tout,h − QC
Fcsρs

(11)

and that for an unsteady-state simulation is

⎧
⎨

Tin,h(t) =

⎩

Tcore,
Tout,h(t − τ ) − QC
Fcsρs

,

for t < τ
for t ≥ τ.

(12)

The term −QC/Fcsρs denotes the effect of heat absorption
by the Peltier device. The Peltier effect and Peltier device
are described in section III-G, and determination of the heat
absorption rate is discussed in section III-H. The initial con-
dition for the unsteady-state simulation is that the temperature
of the whole head model is Tcore.

G. PeltierEffectandPeltierDevice

The Peltier effect is a phenomenon in which heat is absorbed
or emitted at the contact surface of two materials through
which an electrical current ﬂows. When electrical current ﬂows
from material 1 to material 2, the heat absorption rate QC is
expressed as

QC = (S2 − S1)T1,2 I.

(13)

The Peltier device is a plate device for cooling by the
Peltier effect. The basic unit of the Peltier device is illustrated
in Figure 3(a). For S1 < S3 < S2 and electrical current
ﬂowing in the direction of the arrows, heat is absorbed on
the top (blue) surfaces and emitted from the bottom (red)
surfaces. A typical structure of the Peltier device is shown in
Figure 3(b). Multiple basic units are connected in series two-
dimensionally to increase the heat absorption rate. Materials
1 and 2 are thermoelectric chips, and material 3 is an electrode.
The electrodes are in contact with substrates for electrical
insulation. Heat absorption and emission caused by the Peltier
effect result in a temperature drop around the top (blue) sur-
faces and a temperature rise around the bottom (red) surfaces.
Hence, heat is conducted in the direction shown in Figure 3(b).

H. HeatAbsorptionRatebyPeltierDevice

The Peltier device model calculates the heat absorption rate
QC from a speciﬁed voltage U . The equations for energy

166

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 27, NO. 2, FEBRUARY 2019

conservation of materials 1 and 2 (Fig. 3(b)) are as follows:

CH

dTH
dt

CC

dTC
dt

= −QH(t) + N STH(t)I (t)

− kchip A

∂ T
∂z

|

z= 1

2 Z

+ 1
2

r I (t)2

(14)

= QC(t) − N STC(t)I (t)

device (N S, r , and Akchip
equations [48].

Z

) are determined by the following

N S = Umax
TH
r = Umax(TH − (cid:6)Tmax)
ImaxTH
= ImaxUmax(TH − (cid:6)Tmax)
2 TH(cid:6)Tmax

Akchip
Z

(22)

(23)

(24)

+ kchip A

∂ T
∂z
terms on the right

|

z= 1

2 Z

+ 1
2

r I (t)2

The four
in each equation are the
effect of heat emission from the hot/cold side, heat emis-
sion/absorption by the Peltier effect, heat conduction inside
in order. There are
the Peltier device, and Joule heating,
two assumptions in Eqs. (14) and (15): the value of kchip
is the same for both thermoelectric chips, and the heat
accumulation rate in materials 1 and 2 can be approxi-
dTC
dt , respectively. The validity of
mated as CH
Eqs. (14) and (15) has been shown previously [48]. Since the
temperature gradient inside the thermoelectric chips is approx-
imately linear along the z-axis [49], the following equation
applies.

and CC

dTH
dt

(cid:2)
(cid:2)
(cid:2)
(cid:2)

∂ T
∂z

= TH(t) − TC(t)
Z

z= 1

2 Z

(15)

I. PressureDrop

To calculate the pressure drop during saline circulation,
the whole system needs to be simulated; however, this requires
heavy computation. A simple model of
the relationship
between the saline ﬂow rate and the pressure drop was built
to reduce the computational load.

The cooling device was divided into two parts: the inside
of the middle layer (channel) and the outside (tube), which
was approximated as cylindrical and of length 2 m. CFD sim-
ulations should be conducted with Eqs. (2)-(4) for calculating
the pressure drop in the channel, but the pressure drop in the
tube can be calculated as follows:

(cid:6)pout = f ·
(cid:6)

ρsu2 Lt
2dt
64Re−1
Re < 3000
0.0791Re−0.25 Re > 3000

(25)

(26)

(16)

f =

Substitution of Eq. (16) for Eqs. (14) and (15) results in

Use of the pressure drop model for the tube saves compu-

CH

dTH
dt

CC

dTC
dt

= −QH(t) + N STH(t)I (t)

−

kchip A
Z

(TH(t) − TC(t)) + 1
2

r I (t)2

(17)

= QC(t) − N STC(t)I (t)

+

kchip A
Z

(TH(t) − TC(t)) + 1
2

r I (t)2.

(18)

The Peltier device makes contact with heat sinks on the
hot and cold sides. Thermal grease is applied for maximizing
heat transfer between the device and the heat sinks. Equa-
tions (19) and (20) are satisﬁed based on the deﬁnition of
heat resistance of the heat sink.

RH QH(t) = TH(t) − Ta
RC QC(t) = Tout,h(t) − TC(t)

(19)

(20)

where RH and RC are overall heat resistances that express
the sum of heat resistance between the Peltier device and
the heat sinks, the heat resistance of the heat sinks them-
resistance between the heat sinks
selves, and the heat
and air or saline. In addition,
law
results in

the Kirchhoff circuit

U (t) = r I (t) + N STH(t) − N STC(t).

(21)

Eqs. (17)-(21) deﬁne the Peltier device model. The initial
conditions for the unsteady-state simulation are TH(0) =
Ta and TC(0) = Tcore. The physical properties of
the

tational time in the CFD simulation.

IV. PARAMETER DETERMINATION IN A CAT MODEL

The principles, methods, and results of the experiment
with a cat for determining the parameter Wtis in Eq. (10)
are described. The thickness of the gray matter does not
differ among animal species, but varies in different brain
regions, and is about 2-4 mm overall [50]. This indicates that
heat conduction in a cat’s brain is close to that in humans.
In addition, the body of a cat is large enough to prevent the
body temperature becoming hypothermic during brain cooling.
Thus, we used a cat for determining the parameter Wtis.

A. Principles

Let z be the coordinate perpendicular to the brain surface,
with z = 0 on the brain surface and z > 0 inside the brain.
Under the assumption that the brain temperature depends only
on z, Eq. (10) is transformed to
∂ 2 ˜T
∂z2
where ˜T = T − Tcore. The following equation is satisﬁed in
the steady state.

− cbloodWtis

ρtisctis

∂ ˜T
∂t

= ktis

(27)

˜T

d2 ˜T
dz2

= cbloodWtis
ktis

˜T

The boundary conditions of Eq. (28) are as follows.

˜T (0) = ˜Ts
˜T (z) = 0

lim
z→∞

(28)

(29)

(30)

HATA etal.: EPILEPTIC SEIZURE SUPPRESSION BY FOCAL BRAIN COOLING

167

TABLE III
AGENTS INJECTED TO CAT IN EXPERIMENT

The solution of Eqs. (28)-(30) is
(cid:8)

(cid:7)
˜T (z) = ˜Ts exp

−

(cid:9)

cbloodWtis
ktis

z

Fig. 4. Device implant area and actual cooling device. (a) Device implant
area. (b) Cooling device ﬁxed with resin.

(31)

if none of cblood, Wtis, and ktis depend on z. This equation
represents the steady-state temperature proﬁle in the brain. It is
transformed into

ln

˜T (z)
˜Ts

= az

where the constant a is expressed as

(cid:8)

a = −

cbloodWtis
ktis

.

(32)

(33)

The value of Wtis is obtained through the following procedure.
1) Conduct an animal experiment in which the brain is
cooled until reaching a steady state, and measure the
steady-state temperature in the cooling device and at
multiple depths in the brain.

Fig. 5. Devices used in experiment. (a) Temperature measuring device.
(b) Cooling device.

2) Derive

the

constant a
ln ( ˜T (z)/ ˜Ts) vs. z by using least squares.

from the measurements

3) Determine Wtis as

Wtis  ktis
cblood

a2.

(34)

Note that cblood = 4.2 × 103
0.51 J/(m · s · K) in the brain [51].

J/(kg · K) and ktis =

B. Methods

The experiment was performed on a cat weighing 4.0 kg.
All procedures were reviewed by the Graduate School of
Medicine Committee for Animal Experimentation at Yam-
aguchi University, and were performed based on the committee
guidelines. First, ﬁve agents (Table III) were injected for
general anesthesia, suppression of saliva, muscle relaxation,
and analgesia. Since general anesthesia suppresses thermoreg-
ulation and respiration, an electric blanket was placed on the
cat and a tube was inserted into the trachea. After tracheal
intubation, the cat was maintained with controlled mechanical
ventilation using anesthesia equipment (A.D.S. 1000, Engler
Engineering Corp.). The head was then ﬁxed with a stereotaxis
apparatus and the skin incised to expose the skull. The dura
was exposed by resecting part of the skull (Fig. 4 (a)).

The cooling device for measuring the brain temperature is
shown in Fig. 5 (a) and (b). This device has a needle with three
thermocouples. The needle was inserted into the brain perpen-
dicular to the brain surface as shown in Fig. 6. The cooling
device was pressed against the brain surface just above the
needle, accompanied by two thermocouples at the inlet and

Fig. 6. Placement of temperature measuring device and cooling device.

Fig. 7. Circulation of saline. There are two routes; only route A passed
through cooling device.

outlet, and ﬁxed to the skull with resin, after which the skin
was sutured using a stapler (Fig. 4 (b)).

The two circulation routes for saline are shown in Figure 7.
Both routes pass through a tank, a ﬂow meter (LM05ZZT-AR,
Horiba Stec), a thermoregulator (TTM-204, Toho Electronics
and PSC-02, TwinBird), and a pump (KE-162, Taiko Kikai
Industries), but only route A runs through the cooling device.
Since the wall of the tubes was not thermally insulated, heat
transfer between saline and air was not necessarily negligible.
After stopping the anesthesia equipment and waking the cat
from anesthesia, brain temperature in the awake and naturally
relaxed condition was recorded under the following conditions.
First, saline was circulated in route B. The set point values

168

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 27, NO. 2, FEBRUARY 2019

TABLE IV
COMPARISON OF CHANNEL STRUCTURES FOR PROBLEM 1

Fig. 8. Experimental results of cooling animal brain with saline of 10◦C
for 20 minutes.

TABLE V
COMPARISON OF CHANNEL STRUCTURES FOR PROBLEM 2

Fig. 9. The relationship between ln( ˜T(z)/ ˜Ts) and z. The measurement
data at three different depths are approximated by a straight line. A total
of three lines are drawn on the basis of three animal experiments.

of the saline ﬂow rate and the outlet
temperature of the
thermoregulator were 0.3 L/min and 8.5 ◦C, respectively,
and the inlet temperature in the cooling device was about
10 ◦C. After the outlet temperature of the thermoregulator was
decreased to the set point value, a cycle of 20 min cooling
and 15 min rewarming was repeated three times. Cooling and
rewarming correspond to use of routes A and B, respectively.

C. Results

Throughout the cooling period, the inlet temperature of the
cooling device was maintained almost within the range of
10 ± 1 ◦C, and Ts was set to 10 ◦C in Eq.(32). The results
of cooling for 20 min are shown in Figure 8. A time of
<10 min was required for the brain temperature to level off.
The steady-state brain temperature was approximated as the
average temperature in the interval from 10 to 20 min after
the start of cooling. Tcore was set to 39.6 ◦C, which was the
brain temperature at a depth of 6.7 mm after leveling off in
the rewarming period.

A plot of ln ( ˜T (z)/ ˜Ts) vs. z is shown in Fig. 9. The slopes
in the three cycles were −210, −207, and −204 m−1. Based
on
slope, Wtis was
be
5.2 kg/(m3 · s). The Wtis value was concluded to be valid
because of the similarity of the slopes in different cycles.

determined to

average

the

V. SIMULATION

Simulation results for the RCC brain cooling system using
the developed system model are described in this section.
COMSOL Multiphysics® 5.1 was used for the simulation.

A. ChannelStructureinCoolingDevice

The channel structure in the titanium cooling device requires
optimization because it affects cooling performance and the
pressure drop. Two types of optimization problems were
solved to deﬁne the optimal structure of the channel among
the candidates shown in Table II.

Problem 1: Minimize the difference between the highest
and lowest temperatures on planes 0 and 2 mm below
the cooling device at steady state. The constraints were
as follows.

– An average temperature of 25.0 ◦C at 2 mm below

the cooling device.

– A ﬂow rate of saline of 0.4 L/min.

Problem 2: Minimize the pressure drop during saline
circulation with the following constraints.

– An average temperature of 25.0 ◦C at 2 mm below

the cooling device.

– A difference of 2.3 ◦C between the highest and
lowest temperatures at the bottom of the cooling
device at steady state.

The simulation results are shown in Tables IV and V.
In problem 1, device C achieved the minimum difference
between the maximum and minimum temperatures at planes
0 and 2 mm below the cooling device. In problem 2, device C
also achieved the lowest pressure drop. Thus, device C has the
optimal channel structure among the three candidates. In these
simulations, a voltage of 2.0-2.1 V was required for Peltier
device supply at steady state, and the hot and cold sides of
the device had temperatures of <40 ◦C and >5 ◦C in both
problems and all devices.

The brain surface temperature distribution 10 min after the
start of cooling by device C is shown in Figure 10. The highest
temperature at 2 mm below the cooling device did not reach
the target temperature of 25 ◦C, even after cooling for 20 min.

HATA etal.: EPILEPTIC SEIZURE SUPPRESSION BY FOCAL BRAIN COOLING

169

Steady-state temperature distribution in brain for device C
Fig. 10.
10 minutes after beginning of cooling. (a) Bottom of cooling device.
(b) 2 mm below cooling device. (c) 3 mm below cooling device.

The highest temperature occurred in the peripheral area of the
device, which suggests that the cooling device should be larger
than the target cooling region.

The device with the more complex structure achieved a
temperature distribution with a higher uniformity. Vortexes
occurred in the cooling device with a simple channel structure
due to the wide channel width, and this hinders achievement of
a uniform temperature distribution. In fact, as shown in Fig. 10,
the highest temperature occurred in the periphery of the device,
while the central region had the lowest temperature. Higher
temperature uniformity is achieved when heat conduction from
the periphery to the center is promoted. A channel structure
with more titanium ﬁns may be most effective, since titanium
has a much larger thermal conductivity than saline at 25 ◦C:
21.9 W/(m · K) vs. 0.56 W/(m · K) (Table VII, Eq. (8)).

B. CoolingPerformance

The cooling performance of device C was evaluated. The
period required for brain cooling was estimated by unsteady-
state simulation. The Wtis parameter in Eq. (10) was set to
5.2 kg/(m3 ·s) (determined in section IV) and 10.4 kg/(m3 ·s),
which is double the determined value to simulate a situation
in which the brain is more difﬁcult to cool. The voltage for
driving the Peltier device was ﬁxed at 5 V, and the initial saline
temperature was 38 ◦C.

As shown in Fig. 11, <10 min was required for the average
temperature at 2 mm below the cooling device to reach the
target of 25 ◦C for both values of Wtis. The hot and cold sides
of the Peltier device were <40 ◦C and >5 ◦C, respectively,
and the average electrical current over 20 min was 4.0 A.

Epileptic seizures can be predicted 89±15 min before onset
using an intracranial EEG-based algorithm that has a sensitiv-
ity of 91.3% and a false warning rate of 0.121 /h [39]–[41].
Thus, the time required for brain cooling is much shorter
than that from seizure prediction to onset. Also, the period
for brain cooling might be shorter than the calculated value if
the initial saline temperature is <38 ◦C. This result shows that
the cooling performance of the designed brain cooling device
is sufﬁcient for seizure suppression.

C. FrequencyofBatteryCharge

The frequency of battery charge is a key performance
indicator for the focal brain cooling system because fre-
quent charging or exchange of the battery is undesirable.
The frequency of battery charge g is calculated as follows:
g = b

(35)

¯I tcoolζ

Fig. 11. Temporal change of temperature in brain and Peltier device
3 · s). (b) Wtis
when ambient temperature is 25 ◦C. (a) Wtis is 5.2 kg/(m
is 10.4 kg/(m

3 · s).

TABLE VI
VALUES OF CONSTANTS ON HEAD MODEL [51]

where b, ¯I , tcool, and ζ represent the battery capacity, the aver-
age electrical current, the time required for cooling per seizure,
and the number of seizures per day, respectively. b was
assumed to be 10 Ah. ¯I is the sum of the electrical current
supplied to the Peltier device, the pump, and the fan. The
current for the Peltier device was 4.0 A based on section V-B,
and those for the pump and fan were 0.2 and 0.3 A,
respectively [26], [31]. Using these assumptions, the estimated
average electrical current was approximately 5 A.

The cooling time for seizure suppression is estimated as
the total time required for lowering and maintaining the brain
surface temperature. In section V-B, the cooling period was
determined to be ≤10 min, and maintenance of brain cooling
should occur for about 10 min based on clinical experience
at Yamaguchi University School of Medicine. That is, our
system requires about 20 min of brain cooling for seizure
suppression and consumes 1.5 Ah per cooling cycle. From this,
we conclude that battery charging would be required every
two or three seizures. The quartile frequencies of seizures with
awareness impairment in temporal lobe epilepsy are 0.10, 0.16,
and 0.47 /day [52], which indicates that charging or exchange
of the battery would usually be required every few days. This
frequency of required battery charging does not detract from
the usability of the brain cooling system.

The

intermittent brain cooling proﬁle proposed by
Yang et al. [42] has cooling for 30 s at intervals of 2 min.

170

IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 27, NO. 2, FEBRUARY 2019

temporal changes of the average temperature at 2 mm below
the cooling device at ambient temperatures of 15, 20, 25, 30,
and 35 ◦C. The voltage for driving the Peltier device was ﬁxed
at 5 V and the initial saline temperature was 38 ◦C.

For Wtis = 5.2 kg/(m3 · s), the average temperature at
2 mm below the cooling device reached the target of 25 ◦C
within 15 min, even when the ambient temperature was 35 ◦C.
This cooling is sufﬁcient for seizure suppression. In contrast,
with Wtis = 10.4 kg/(m3 · s), the average temperature at
2 mm below the cooling device did not reach 25 ◦C after
30 min when the ambient temperature was 30 or 35 ◦C. This
result indicates that it is difﬁcult to suppress seizures when the
ambient temperature is very high. Suppression of seizures at
high ambient temperature requires an increased heat removal
performance of the Peltier device, but this setting may require
frequent battery exchanges.

VI. CONCLUSIONS

In this work, we developed mathematical models for a focal
brain cooling system with recirculating coolant cooling (RCC)
to achieve an optimal design. The model system consists of the
head model, basic ﬂuid dynamics equations, and a modiﬁed
Pennes bioheat equation. To determine a parameter in the
bioheat equation, an experiment was performed in a cat model.
In addition, a pressure drop model of the relationship between
the saline ﬂow rate and pressure drop was constructed to
reduce the computational burden of the CFD simulation.

The simulation results showed that a complex channel
structure in the cooling device is desirable since it gives higher
brain surface temperature uniformity and a lower pressure drop
compared to a simple channel structure. A time <10 min was
required for the average temperature at 2 mm below the cool-
ing device to reach the target temperature of 25.0 ◦C, which is
a short enough period for brain cooling after seizure prediction
by an intracranial EEG-based algorithm. In addition, the fre-
quency of battery charge in our system was calculated to be
once every few days for most patients. Therefore, the focal
brain cooling system under development is feasible for future
treatment of epilepsy.

it

We plan to manufacture a prototype of the focal brain
in ani-
cooling system designed in this work and test
mal experiments before clinical application.
In addition,
we will simulate various device sizes. A new seizure predic-
tion algorithm will be constructed for determination of the
timing for activation and deactivation of the cooling system,
using EEG, brain temperature, intracranial pressure, and oxy-
gen saturation and concentration of oxyhemoglobin in cerebral
blood measured by skull-implanted multimodal sensors [53].

REFERENCES

Fig. 12. Temporal change of average temperature at 2 mm below cooling
3 · s).
device with different ambient temperatures. (a) Wtis is 5.2 kg/(m
(b) Wtis is 10.4 kg/(m

3 · s).

TABLE VII
VALUES OF CONSTANTS

This proﬁle consumes 1.0 Ah per hour and the battery life is
about 10 h. Thus, patients would need to charge or exchange
the battery once or twice each day.

D. EffectofAmbientTemperature

The ambient temperature affects the cooling performance of
the focal brain cooling system because the heat stored in the
circulating saline is removed to the ambient air by the Peltier
device. To evaluate the effect of the ambient temperature on the
cooling performance, we simulated changes of the brain tem-
perature with different ambient temperatures. Figure 12 shows

[1] J. W. Sander, “The epidemiology of epilepsy revisited,” Current Opinion

Neurol., vol. 16, no. 2, pp. 165–170, 2003.

[2] A. K. Ngugi, C. Bottomley,

I. Kleinschmidt, J. W. Sander, and
C. R. Newton, “Estimation of the burden of active and life-time epilepsy:
A meta-analytic approach,” Epilepsia, vol. 51, no. 5, pp. 883–890, 2010.
[3] B. Litt and J. Echauz, “Prediction of epileptic seizures,” Lancet Neurol.,

vol. 1, no. 1, pp. 22–30, 2002.

[4] S. M. Rothman, M. D. Smyth, X.-F. Yang, and G. P. Peterson, “Focal
cooling for epilepsy: An alternative therapy that might actually work,”
Epilepsy Behav., vol. 7, pp. 214–221, Sep. 2005.

HATA etal.: EPILEPTIC SEIZURE SUPPRESSION BY FOCAL BRAIN COOLING

171

[5] C. J. Sartorius and M. S. Berger, “Rapid termination of intraoperative
stimulation-evoked seizures with application of cold ringer’s lactate to
the cortex,” J. Neurosurg., vol. 88, no. 2, pp. 349–351, 1998.

[6] K. M. Karkar, P. A. Garcia, L. M. Bateman, M. D. Smyth,
N. M. Barbaro, and M. Berger, “Focal cooling suppresses spontaneous
epileptiform activity without changing the cortical motor threshold,”
Epilepsia, vol. 43, no. 8, pp. 932–935, 2002.

[7] T. Hiraishi et al., “Signiﬁcance of horizontal propagation of synchro-
nized activities in human epileptic neocortex investigated by opti-
cal imaging and immunohistological study,” Epilepsy Res., vol. 104,
pp. 59–67, Mar. 2013.

[8] H. Imoto et al., “Use of a peltier chip with a newly devised local
brain-cooling system for neocortical seizures in the rat,” J. Neurosurg.,
vol. 104, no. 1, pp. 150–156, 2006.

[9] A. E. Bennett, R. E. Hoesch, L. D. DeWitt, P. Afra, and S. A. Ansari,
“Therapeutic hypothermia for status epilepticus: A report, historical per-
spective, and review,” Clin. Neurol. Neurosurg., vol. 126, pp. 103–109,
Nov. 2014.

[10] M. Fujii et al., “Application of focal cerebral cooling for the treatment
of intractable epilepsy,” Neurologia Med.-Chirurgica, vol. 50, no. 9,
pp. 839–844, 2010.

[11] A. K. Ommaya and M. Baldwin, “Extravascular local cooling of the

brain in man,” J. Neurosurg., vol. 20, no. 1, pp. 8–20, 1963.

[12] K. Šourek and V. Trávníˇcek, “General and local hypothermia of the
brain in the treatment of intractable epilepsy,” J. Neurosurg., vol. 33,
no. 3, pp. 253–259, 1970.

[13] M. Fujii et al., “Cooling of the epileptic focus suppresses seizures with
minimal inﬂuence on neurologic functions,” Epilepsia, vol. 53, no. 3,
pp. 485–493, 2012.

[14] X.-F. Yang and S. M. Rothman, “Focal cooling rapidly terminates
experimental neocortical seizures,” Ann. Neurol., vol. 49, pp. 721–726,
Jun. 2001.

[15] T. Oku et al., “The inﬂuence of focal brain cooling on neurophys-
iopathology: Validation for clinical application,” J. Neurosurg., vol. 110,
no. 6, pp. 1209–1217, 2009.

[16] M. A. Long et al., “Functional segregation of cortical regions underlying
speech timing and articulation,” Neuron, vol. 89, no. 6, pp. 1187–1193,
2016.

[17] S. M. Rothman, “The therapeutic potential of

focal cooling for
neocortical epilepsy,” Neurotherapeutics, vol. 6, no. 2, pp. 251–257,
2009.

[18] H. E. Bakken, H. Kawasaki, H. Oya,

and
M. A. Howard, III, “A device for cooling localized regions of human
cerebral cortex,” J. Neurosurg., vol. 99, no. 3, pp. 604–608, 2003.
[19] K. H. Polderman and I. Herold, “Therapeutic hypothermia and con-
trolled normothermia in the intensive care unit: Practical considerations,
side effects, and cooling methods,” Crit. Care Med., vol. 37, no. 3,
pp. 1101–1120, 2009.

J. D. Greenlee,

[20] C. Diao, L. Zhu, and H. Wang, “Cooling and rewarming for brain
ischemia or injury: Theoretical analysis,” Ann. Biomed. Eng., vol. 31,
no. 3, pp. 346–353, 2003.

[21] S. Nomura et al., “Changes in glutamate concentration, glucose
metabolism, and cerebral blood ﬂow during focal brain cooling of the
epileptogenic cortex in humans,” Epilepsia, vol. 55, no. 5, pp. 770–776,
2014.

[22] S. Nomura et al., “Effects of focal brain cooling on extracellular
concentrations of neurotransmitters in patients with epilepsy,” Epilepsia,
vol. 58, no. 4, pp. 627–634, 2017.

[23] T. Inoue et al., “Epidural focal brain cooling abolishes neocortical
seizures in cats and non-human primates,” Neurosci. Res., vol. 122,
pp. 35–44, Sep. 2017.

[24] K. Hata et al., “Design of focal brain cooling system for suppressing
epileptic seizures,” in Proc. EMBC, Jeju, Korea, Jul. 2017, pp. 283–286.
[Online]. Available: http://www.maxell.jp/consumer/

[25] (2018). Maxell.

mpc-cw10000.html

[26] (2017). Nippon Keiki Works.

[Online]. Available:

http://www.

nipponkeiki.co.jp/products/IngresProtection/HY60W/HY60W-spec.pdf

[27] (2017). Mizutani Electric Industry. [Online]. Available: http://www.

mizuden.com/web/pdf/EAB.pdf

[32] T. A. Snyder et al., “Preclinical biocompatibility assessment of the
EVAHEART ventricular assist device: Coating comparison and platelet
activation,” J. Biomed. Mater. Res. A, vol. 81, no. 1, pp. 85–92, 2007.
[33] M. E. Stone, A. Pawale, H. Ramakrishna, and M. M. Weiner,
“Implantable left ventricular assist device therapy—Recent advances
and outcomes,” J. Cardiothoracic Vascular Anesthesia, vol. 32, no. 4,
pp. 2019–2028, 2018.

[34] J. K. Kirklin et al., “Eighth annual INTERMACS report: Special focus
on framing the impact of adverse events,” J. Heart Lung Transplantation,
vol. 36, no. 10, pp. 1080–1086, 2017.

[35] D. J. Goldstein et al., “Continuous-ﬂow devices and percutaneous site
infections: Clinical outcomes,” J. Heart Lung Transplantation, vol. 31,
no. 11, pp. 1151–1157, 2012.

[36] L. Kuhlmann, K. Lehnertz, M. P. Richardson, B. Schelter, and
H. P. Zaveri, “Seizure prediction—Ready for a new era,” Nature Rev.
Neurol., vol. 14, no. 10, pp. 618–630, 2018.

[37] L. Kuhlmann et al., “Epilepsyecosystem.org: Crowd-sourcing repro-
ducible seizure prediction with long-term human intracranial EEG,”
Brain, vol. 141, no. 9, pp. 2619–2630, 2018.

[38] M. J. Cook et al., “Prediction of seizure likelihood with a long-
term, implanted seizure advisory system in patients with drug-resistant
epilepsy: A ﬁrst-in-man study,” Lancet Neurol., vol. 12, no. 6,
pp. 563–571, 2013.

[39] L. D. Iasemidis et al., “Long-term prospective on-line real-time seizure
prediction,” Clin. Neurophysiol., vol. 116, pp. 532–544, Mar. 2005.

[40] M. E.Weinand, L. P. Carter, W. F. El-Saadany, P.

J. Sioutos,
D. M. Labiner, and K. J. Oommen, “Cerebral blood ﬂow and temporal
lobe epileptogenicity,” J. Neurosurg., vol. 86, no. 2, pp. 226–232, 1997.
[41] D. Sone et al., “Noninvasive evaluation of the correlation between
regional cerebral blood ﬂow and intraventricular brain temperature
Imag., vol. 34, no. 4,
in temporal
pp. 451–454, 2016.

lobe epilepsy,” Magn. Reson.

[42] X.-F. Yang, J. H. Chang, S. M. Rothman, “Long-lasting anticonvulsant
effect of focal cooling on experimental neocortical seizures,” Epilepsia,
vol. 44, no. 12, pp. 1500–1505, 2003.

[43] COMSOL Multiphysics 5.1 Material Library, COMSOL Incorporated,

2016.

[44] H. H. Pennes, “Analysis of tissue and arterial blood temperatures in the
resting human forearm,” J. Appl. Physiol., vol. 1, no. 2, pp. 93–122,
1948.

[45] D. A. Nelson and S. A. Nunneley, “Brain temperature and limits on
transcranial cooling in humans: Quantitative modeling results,” Eur.
J. Appl. Physiol. Occupat. Physiol., vol. 78, pp. 353–359, Aug. 1998.

[46] J. P. Abraham and B. D. Plourde, “Validation of numerically simulated
tissue temperatures during transcutaneous recharge of neurostimula-
tion systems,” Neuromodulation, Technol. Neural Interface, vol. 19,
pp. 161–170, Feb. 2016.

[47] C.-S. Orr and R. C. Eberhart, “Bioheat transfer in blood perfused tissues
and clinical applications of hypothermia,” Annu. Rev. Heat Transf.,
vol. 9, pp. 1–78, 1998.

[48] S. Lineykin and S. Ben-Yaakov, “Modeling and analysis of thermo-
electric modules,” IEEE Trans. Ind. Appl., vol. 43, no. 2, pp. 505–512,
Mar./Apr. 2007.

[49] A. Montecucco, J. R. Buckle, and A. R. Knox, “Solution to the 1-D
unsteady heat conduction equation with internal joule heat generation for
thermoelectric devices,” Appl. Therm. Eng., vol. 35, pp. 177–184, 2012.
[50] M. A. Hofman, “Size and shape of the cerebral cortex in mammals.
I. The cortical surface,” Brain Behav. Evol., vol. 27, no. 1, pp. 28–40,
1985.

[51] (2015).

IT’IS Foundation.

[Online]. Available:

http://www.itis.

ethz.ch/virtual-population/tissue-properties/downloads/database-v3-0/

[52] S. Wiebe, W. T. Blume, J. P. Girvin, and M. Eliasziw, “A randomized,
controlled trial of surgery for temporal-lobe epilepsy,” New England
J. Med., vol. 345, no. 5, pp. 311–318, 2001.

[53] T. Yamakawa, T. Inoue, Y. He, M. Fujii, M. Suzuki, and M. Niwayama,
“Development of an implantable ﬂexible probe for simultaneous near-
infrared spectroscopy and electrocorticography,” IEEE Trans. Biomed.
Eng., vol. 61, no. 2, pp. 388–395, Feb. 2014.

[54] W. M. Haynes and D. R. Lide, Eds., CRC Handbook of Chemistry and

[28] (2017). Mizutani Electric Industry. [Online]. Available: http://www.

Physics, 92nd ed. New York, NY, USA: CRC Press, 2011.

mizuden.com/web/pdf/PIF.pdf

[29] (2017). Z-MAX.

[Online]. Available:

http://www.z-max.jp/peltier_

en/peltier/products/pdf_speciﬁcations/12708AC.pdf

[30] Kurag Electronics.

[Online]. Available: http://kurag.o.oo7.jp/kurag-

el/english/sPLC-10/support/sPLC-10_Brochure(E).pdf

[31] (2017). Enomoto Micro Pump. [Online]. Available: http://www.emp.

co.jp/en/products/direct-current_air/cm-15-24.html

[55] X. Xu, P. Tikuisis, and G. Giesbrecht, “A mathematical model for
human brain cooling during cold-water near-drowning,” J. Appl.
Physiol., vol. 86, no. 1, pp. 265–272, 1999.

[56] C. King et al., “Brain temperature proﬁles during epidural cooling
with the ChillerPad in a monkey model of traumatic brain injury,”
J. Neurotrauma, vol. 27, no. 10, pp. 1895–903, Oct. 2010. [Online].
Available: https://www.ncbi.nlm.nih.gov/pubmed/20684677
