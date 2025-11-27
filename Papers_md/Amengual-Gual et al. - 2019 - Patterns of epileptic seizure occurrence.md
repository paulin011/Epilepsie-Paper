# Amengual-Gual et al. - 2019 - Patterns of epileptic seizure occurrence

Brain Research 1703 (2019) 3–12

Contents lists available at ScienceDirect

Brain Research

j o u r n a l h o m e p a g e : w w w . e l s e v i e r . c o m / l o c a t e / b r e s

Review

Patterns of epileptic seizure occurrence
Marta Amengual-Gual a,b,1,⇑

, Iván Sánchez Fernández b,c,1, Tobias Loddenkemper b,1

a Pediatric Neurology Unit, Department of Pediatrics, Hospital Universitari Son Espases, Universitat de les Illes Balears, Palma, Spain
b Division of Epilepsy and Clinical Neurophysiology, Department of Neurology, Boston Children’s Hospital, Harvard Medical School, Boston, MA, USA
c Department of Child Neurology, Hospital Sant Joan de Déu, Universidad de Barcelona, Spain

a r t i c l e

i n f o

a b s t r a c t

Article history:
Received 23 July 2017
Received in revised form 3 December 2017
Accepted 20 February 2018
Available online 23 February 2018

Keywords:
Epilepsy
Closed-loop system
Differential antiepileptic dosing
Seizure
Machine learning

Background: The occurrence of epileptic seizures in seemingly random patterns takes a great toll on per-
sons with epilepsy and their families. Seizure prediction may markedly improve epilepsy management
and, therefore, the quality of life of persons with epilepsy.
Methods: Literature review.
Results: Seizures tend to occur following complex non-random patterns. Circadian oscillators may con-
tribute to the rhythmic patterns of seizure occurrence. Complex mathematical models based on chaos
theory try to explain and even predict seizure occurrence. There are several patterns of epileptic seizure
occurrence based on seizure location, seizure semiology, and hormonal factors, among others. These pat-
terns are most frequently described for large populations. Inter-individual variability and complex inter-
actions between the rhythmic generators continue to make it more difﬁcult to predict seizures in any
individual person. The increasing use of large databases and machine learning techniques may help bet-
ter deﬁne patterns of seizure occurrence in individual patients. Improvements in seizure detection –such
as wearable seizure detectors— and in seizure prediction –such as machine learning techniques and arti-
ﬁcial as well as neuronal networks— promise to provide further progress in the ﬁeld of epilepsy and are
being applied to closed-loop systems for the treatment of epilepsy.
Conclusions: Seizures tend to occur following complex and patient-speciﬁc patterns despite their appar-
ently random occurrence. A better understanding of these patterns and current technological advances
may allow the implementation of closed-loop detection, prediction, and treatment systems in routine
clinical practice.

(cid:1) 2018 Elsevier B.V. All rights reserved.

Contents

1.
2.

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Results. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.1. Historical evolution of the concept of seizure non-randomness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Chaos theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.2.
Non-random patterns of seizures in the EEG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.3.
Pathophysiological basis of seizure rhythmicity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.4.
Non-random patterns of seizures based on seizure onset, semiology, and evolution. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.5.
Seizure location (Fig. 1 and Table 1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.5.1.
Seizure semiology (Loddenkemper et al., 2011b; Zarowski et al., 2011) (Table 2) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.5.2.
2.5.3.
Clinical evolution of seizures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Irregular patterns of seizure occurrence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Non-random patterns of status epilepticus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Perimenstrual non-random patterns and other triggers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
Practical implications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

2.6.
2.7.
2.8.
2.9.

⇑ Corresponding author.

E-mail addresses: marta.amengual.gual@gmail.com (M. Amengual-Gual), ivan.fernandez@childrens.harvard.edu (I. Sánchez Fernández), tobias.loddenkemper@ childrens.

harvard.edu (T. Loddenkemper).

1 300 Longwood Avenue, 02115, Boston, MA, USA.

https://doi.org/10.1016/j.brainres.2018.02.032
0006-8993/(cid:1) 2018 Elsevier B.V. All rights reserved.

4

3.

M. Amengual-Gual et al. / Brain Research 1703 (2019) 3–12

2.9.1.
2.9.2.

Differential antiepileptic dosing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
Big data, machine learning, and seizure prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.10.
Future directions: seizure detection and seizure prediction in the ambulatory setting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
ETHICS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
FUNDING . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
DECLARATION OF INTEREST . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
CONTRIBUTORS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

1. Introduction

2.2. Chaos theory

One of the most disabling features of epilepsy is that seizures
occur in a seemingly unpredictable pattern (Karoly et al., 2016).
The apparent unpredictability of seizure occurrence leads to a sen-
sation of loss of control and worsens the quality of life of patients
and families (Jacoby, 1992; Kotwas et al., 2016). However, a grow-
ing body of literature demonstrates that seizures tend to occur in
patterns (Karoly et al., 2016; Loddenkemper et al., 2011b; Quigg,
2000), making seizure prediction in the individual patient a poten-
tially attainable goal in the future. In this review article, we sum-
marize the evidence demonstrating a non-random pattern of
seizure occurrence, the potential mechanisms that explain these
cyclical patterns or rhythmicity, and the implications for seizure
prediction and seizure treatment.

2. Results

2.1. Historical evolution of the concept of seizure non-randomness

Ancient civilizations conceptualized and explained epilepsy in
various ways. Most recognized the inﬂuence of environmental fac-
tors and the cyclical nature of seizure occurrence (Chaudhary et al.,
2011). The translation of a cuneiform text on epilepsy shows that
Babylonians classiﬁed epilepsy into diurnal epilepsy or nocturnal
epilepsy (Wilson and Reynolds, 1990). Aristotle also emphasized
the relationship between sleep and epilepsy in his treatise ‘‘On sleep
and waking” stating that ‘‘sleep is similar to epilepsy and in some
way sleep is epilepsy” (Magiorkinis et al., 2010). Most ancient civi-
lizations emphasized the inﬂuence of environmental factors such
as food, physical exercise, or climate on seizure occurrence
(Chaudhary et al., 2011). Additionally, some ancient societies
suggested that menstruation or moon cycles had the power to disor-
der the mind (Eadie, 2012; Raison et al., 1999). In particular, full
moon was associated with bouts of ‘‘insanity” and epilepsy (Raison
et al., 1999). This association is still represented in the English lan-
guage by the word ‘‘lunatic” –from ‘‘luna”, the moon or the goddess
of the moon— which refers broadly to mental disorders (Raison et al.,
1999). Peaks of seizure occurrence during full moon are well docu-
mented in modern literature (Polychronopoulos et al., 2006),
although they may be explained by increased nocturnal luminance
and resultant decrease in sleep time (Baxendale and Fisher, 2008;
Raison et al., 1999). After Edward Sieveking presented a paper on
epilepsy and seizure clustering in women to the Royal Medical and
Chirurgical Society in 1857, Sir Locock, obstetrician to the Queen Vic-
toria, observed that potassium bromide successfully stopped epilep-
tic seizures in all but one (n = 14 or 15) women whose seizure
occurrence was exclusively during their menstruation period
(Eadie, 2012). This is considered one of the earliest documented rea-
sonably effective treatment of epilepsy as well as an early descrip-
tion of catamenial epilepsy. In summary, it is remarkable that the
inﬂuence of environmental factors and their association with seizure
cyclical patterns was recognized by most ancient cultures.

Seizure occurrence appears random because seizure patterns
are often too complex to be described by any simple intuitive
model. Chaos theory aims to explain with mathematical models
the behavior of systems that change or evolve with time –dynamic
systems— and that appear to be random, such as the double pen-
dulum trajectory, natural phenomena, or economy.

From a qualitative point of view, the two main characteristics of
chaotic systems are: high sensitivity to initial conditions and order
without periodicity depending on system stability. Due to high
sensitivity to initial conditions, small variations at onset cause
exponentially divergent outcomes, popularly known as the butter-
ﬂy effect. Due to order without periodicity, sudden turns from
order to chaos and vice versa happen often -for example, fractal
geometry in nature-. As a result, long-term behavior predictions
are challenging in chaotic systems.

To mathematically describe the sensitivity to initial conditions
in systems with limited initial information –the most common
situation- the Lyapunov exponent is used. This exponent measures
the divergence between two starting and inﬁnitesimally close con-
ditions in a dynamic system in which all possible states are repre-
sented. Lyapunov exponent is represented by k in the function
jdZðtÞj (cid:2) ektjdZ0j, where dZ0 is the initial separation and t is the time.
The number of Lyapunov exponents is equal to the number of
dimensions of the system, that is, the rate of divergence. The max-
imal Lyapunov exponent (MLE) determines the predictability of the
system, and a positive MLE indicates that the system is chaotic.

From a mathematical point of view, nonlinear systems follow sets
of differential equations – a differential equation is a mathematical
equation which connects a function with its derivatives-. To describe
order without periodicity, each speciﬁc differential equation models
speciﬁc systems –for instance, Navier-Stokes equations character-
izes ﬂuid dynamics; Lorentz laws, electromagnetics; Lorenz system,
the atmospheric convection, among others-. Given the chaotic nat-
ure of brain neuronal activity, it should be possible to describe
epileptic seizures through nonlinear differential equations, and then
ﬁnd a mathematical solution to seizure occurrence.

From a pragmatic point of view, brain neuronal activity could
exemplify a chaotic system. Therefore, long-term EEG recordings
could beneﬁt from nonlinear analysis and provide clinically useful
tools in the ﬁeld of epilepsy (Elger et al., 2000; Iasemidis and
Sackellares, 1996; Lehnertz, 1999). Three chaotic levels depending
on the epileptic state have been discovered using nonlinear EEG
analysis. The ictal state or seizure discharge corresponds to the
lowest chaotic level (order); the postictal state corresponds to
the highest chaotic level (chaos); and the pre-ictal state corre-
sponds to an intermediate chaotic level. The intermediate chaotic
level during the pre-ictal state reﬂects a spatiotemporal transition
from chaos to a more predictable state (seizure discharge), proba-
bly underlying a synchronous neuronal discharge. Moreover, dif-
ferent levels of chaos are registered from the epileptogenic areas
and non-epileptogenic areas during interictal states facilitating

M. Amengual-Gual et al. / Brain Research 1703 (2019) 3–12

5

the detection of seizure foci (Drury et al., 2003; Iasemidis and
Sackellares, 1996). As a result, seizure location and prediction facil-
itated by the use of chaos theory may simplify epilepsy diagnosis,
patient follow-up, treatment response monitoring and epilepsy
pre-surgical planning (i.e. by reduced seizure detection time and
accurate location) (Ferri et al., 2001; van der Heyden et al.,
1999). Some preventive future interventions aim to move a step
further from description and predict, warn, and treat patients prior
to seizure onset (e.g., real-time tailored therapy through implanted
devices capable of detecting pre-ictal state and delivering treat-
ment in response) (Cook et al., 2013; Venkataraman et al., 2014).

2.3. Non-random patterns of seizures in the EEG

The pattern of seizure occurrence is not random. There is a rela-
tionship between seizure onset and certain prior EEG features
which may permit seizure pattern predictions through mathemat-
ical models. For example, a cascade of electrophysiological events
(long-term energy bursts) was recorded hours before the clinical
seizure onset in a small number of patients with mesial temporal
lobe epilepsy (Litt et al., 2001). In another study, ‘forbidden ordinal
patterns’ during a peri-ictal stage (which are the missing ordinal
patterns in deterministic dynamics) were recorded in intracranial
EEG in a small number of patients with pharmaco-resistant focal
epilepsy (Schindler et al., 2011). Likewise, other authors found that
a reduction of sleep spindles could predict the occurrence of sei-
zures and propensity of seizure generalization in focal epilepsy
(Tezer et al., 2014). A relationship between changes in spike rate,
both increased and decreased rate, and seizures onset has also been
described in a study involving a small number of patients (Karoly
et al., 2016). These authors suggested that a high spike rate inhibits
seizures onset instead of promoting them or that a decreased spike
rate is a secondary symptom of the brain approaching a seizure.
They also concluded that patterns of spike and seizure occurrence
were highly subject-speciﬁc and follow diurnal and nocturnal
cycles with the same regulatory mechanisms. Recently, Cook et al.
(2016) have suggested that focal seizures could be characterized
by seizure groups of ﬁxed duration and interval which signiﬁes that
seizures follow a predetermined path (Cook et al., 2016). Regarding
the end of seizures, a study demonstrated that self-terminating sei-
zures end through a common dynamical mechanism via a critical
electrophysiological transition, in contrast to status epilepticus that
does not cross the critical transition despite repeated approaches
(Kramer et al., 2012). Concerning clinical applicability, a seizure
advisory system has already been implanted in several patients
with drug-resistant epilepsy and it demonstrated the ability to pre-
dict seizure likelihood (Cook et al., 2013). In conclusion, both onset
and end of seizures can potentially be predicted through EEG with
mathematical models.

2.4. Pathophysiological basis of seizure rhythmicity

The pathophysiological basis of seizure rhythmicity remains
incompletely understood. However, the 24-h periodicity of epi-
lepsy and its relation to sleep-wake cycles suggest that circadian
and diurnal body systems may contribute to seizure rhythmicity
(Hofstra and de Weerd, 2009; Kothare and Zarowski, 2011;
Loddenkemper et al., 2011a).

The circadian system is a biological rhythm with an approxi-
mately 24-h period composed by one or more oscillators which
receive inputs and provide outputs (Smolensky and Peppas,
2007). Components of the circadian system include:

Oscillator. An oscillator is a structure of an organism capable to
produce a rhythmic output. The main oscillator is called pace-
maker or biological clock since its rhythm is self-sustained in con-
trast to the peripheral oscillators, which require the pacemaker

activity to work. The suprachiasmatic nucleus (SCN) –the human
oscillator— is located inside the hypothalamus and each one of
the two nuclei contains 8000–10000 neurons. These neurons are
responsible for circadian periodicity in humans and other mam-
mals by generating rhythmic electrical activity and producing syn-
chronizing signals. The pacemaker activity may be explained due
to ’core circadian clock genes’, which generate auto-regulatory
transcriptional-translational feedback loops (Bell-Pedersen et al.,
2005). The SCN is connected with other brain areas – such as pineal
body, thalamus, other hypothalamic nuclei, limbic system and
retina- and it can be entrained by environmental inputs. Heart,
lung, liver, pineal gland, kidney, ﬁbroblast, testis and skeletal mus-
cle are some examples of human peripheral oscillators or periph-
eral clocks activated by the SCN. Mutations in clock genes or
irregularities in transcriptional-translational processes could cause
circadian system dysfunction and, consequently, produce diseases
related with circadian rhythmic disruption.

Inputs. An input is a signal coming from the external medium
that allows SCN to entrain with the environment. The main input
pathways to SCN are the retina, by the retino-hypothalamic tract,
and the intergeniculate leaﬂet, by the geniculo-hypothalamic tract.
The light-dark cycle is the main input signal coming from the
retina, concretely from rods, cones and ganglion cells which con-
tain rhodopsin, photopsin and melanopsin respectively, and all
three required for optimal light entrainment (Panda et al., 2002).
Many other input signals entrain the SCN, such as feeding, social
interactions, and temperature.

Outputs. An output is an SCN efferent or a result from the oscil-
lator’s activity. SNC has efferents to many hypothalamic nuclei. It
connects through ventral and dorsal subparaventricular zones
and dorsomedial nucleus with the medial preoptic area, ventrolat-
eral preoptic nucleus, paraventricular nucleus and lateral nucleus
(Saper et al., 2005). SNC also connects with other brain areas, such
as the pineal body, thalamus, and limbic system. These connec-
tions, together with cortico-thalamic connections, may represent
part of the pathophysiological basis of speciﬁc seizure rhythmicity
and epilepsy patterns, since these are involved in some epileptic
networks (Loddenkemper et al., 2011a). The SCN, through its con-
nections with different areas of the hypothalamus, regulates pro-
feeding, metabolism,
cesses
corticosteroids secretion, and corporal temperature (Saper et al.,
2005). Peripheral oscillators also modulate other physiological
and biochemical functions. For example, the pineal gland regulates
the melatonin release depending on the amount of darkness or
light. Low melatonin levels increase alertness, heart rate, body
temperature, and activate high-alpha frequency in the EEG.
Another example may be cardiac features, including modulation
of heart rate, blood pressure, vasodilation, and gene expression
(Bell-Pedersen et al., 2005). All of the 24-h periodicity biological
activity patterns are controlled through clock genes products
which orchestrate gene expression, protein modiﬁcations and hor-
mone secretion among others.

sleep, wakefulness,

such as

Another concept related to seizure rhythmicity is seizure clus-
tering. On the one hand, seizure rhythmicity draws non-random
cyclical patterns of seizure occurrence through the time -
temporal distribution of epileptic seizures-. On the other hand, sei-
zure clustering means acute and repetitive seizures during a
deﬁned period of time, despite the lack of consensus to deﬁne
the period and the number of seizures included in it -closely
grouped series of seizures- (Haut, 2015).

2.5. Non-random patterns of seizures based on seizure onset,
semiology, and evolution

Circadian patterns in epilepsy, which correspond to diurnal /
nocturnal cycles, have been well described (Quigg, 2000). Speciﬁ-

6

M. Amengual-Gual et al. / Brain Research 1703 (2019) 3–12

cally, patient wakefulness and sleep cycles have shown to be a bet-
ter predictor for seizures types than day / night cycling (Kaleyias
et al., 2011; Loddenkemper et al., 2011b). The literature on seizure
patterns is also summarized in Tables 1 and 2.

2.5.1. Seizure location (Fig. 1 and Table 1)
(cid:3) Frontal lobe epilepsy (FLE). Seizures related to frontal lobe epi-
lepsy occur more frequently during sleep (Herman et al., 2001;
Kaleyias et al., 2011; Loddenkemper et al., 2011b) and overnight

between 12 a.m.–6 a.m., with a peak in the very early morning
(Loddenkemper et al., 2011b). A later study added that these
results change depending on different age groups. Frontal lobe
seizures occur more frequently during wakefulness in infants,
but they happen more frequently during sleep in adolescents
(Ramgopal et al., 2014a). These results suggest that changes in
circadian rhythms might cause different seizure susceptibility
depending on age group. In terms of the sleep phase involved,
one study pointed out that focal seizures with onset during

Table 1
Distribution of seizure occurrence according to location of seizure onset in the brain. (See below-mentioned references for further information.)

N: number of patients (and seizures) in the series. FLE: frontal lobe epilepsy. OLE: occipital lobe epilepsy. PLE: parietal lobe epilepsy. TLE: temporal lobe epilepsy. MTLE:
mesial temporal lobe epilepsy. NCTLE: neocortical temporal lobe epilepsy. XTLE: extratemporal lobe epilepsy. GEN: generalized epilepsy. MTLOB: multilobar epilepsy. In:
infants. Ch: children. Ad: adolescents. DS: Dyscognitive seizures. TS: tonic seizures. TCS: tonic-clonic seizures. CS: clonic seizures. AuS: automotor seizures. HMS: hypermotor
seizures. AtS: atonic seizures. hmS: hypomotor seizures. MS: myoclonic seizures. ES: epileptic spasms. VS: versive seizures. GS: gelastic seizures. Abs: absence seizures.

Table 2
Distribution of seizure occurrence according to seizure semiology.

N: number of patients (and seizures) in the series. FLE: frontal lobe epilepsy. OLE: occipital lobe epilepsy. PLE: parietal lobe epilepsy. TLE: temporal lobe epilepsy. MTLE:
mesial temporal lobe epilepsy. NCTLE: neocortical temporal lobe epilepsy. XTLE: extratemporal lobe epilepsy. GEN: generalized epilepsy. MTLOB: multilobar epilepsy. In:
infants. Ch: children. Ad: adolescents. DS: Dyscognitive seizures. TS: tonic seizures. TCS: tonic-clonic seizures. CS: clonic seizures. AuS: automotor seizures. HMS: hypermotor
seizures. AtS: atonic seizures. hmS: hypomotor seizures. MS: myoclonic seizures. ES: epileptic spasms. VS: versive seizures. GS: gelastic seizures. Abs: absence seizures.

M. Amengual-Gual et al. / Brain Research 1703 (2019) 3–12

7

sleep often occur during NREM sleep, mainly in stage 2, and
essentially never in REM sleep, which suggested that hypersyn-
chrony of sleep could facilitate the onset of certain focal sei-
zures (Herman et al., 2001). That is, sleep has a synchronizing
effect on frontal lobe seizures.

(cid:3) Occipital lobe epilepsy (OLE). In contrast, occipital lobe sei-
zures occur more frequently during daytime, with peaks from
9 a.m. - noon and 3 p.m. – 6 p.m. (Loddenkemper et al.,
2011b) and during wakefulness (Kaleyias et al., 2011).

(cid:3) Parietal lobe epilepsy (PLE). Parietal lobe seizures occur more
frequently during sleep, with a peak between 6 a.m. – 9 a.m.
(Loddenkemper et al., 2011b).

(cid:3) Temporal lobe epilepsy (TLE). Temporal lobe seizures happen
mostly in wakefulness (Kaleyias et al., 2011; Loddenkemper
et al., 2011b; Ramgopal et al., 2014a) and at night between 9
p.m. (cid:4) 9 a.m., with an early morning seizure peak in some stud-
ies (Loddenkemper et al., 2011b), and during daytime in others
(Kaleyias et al., 2011).

(cid:3) Multilobar seizures. Multilobar seizures occur largely during

sleep (Loddenkemper et al., 2011b).

(cid:3) Generalized epilepsy (GEN). Generalized seizures happen
mostly in wakefulness and daytime with a peak between 6 a.
m. – 12 p.m. (Loddenkemper et al., 2011b; Ramgopal et al.,
2014a). A study points out that occurrence of seizures at night
increases in older patients (Ramgopal et al., 2014a). Idiopathic
generalized epilepsy syndromes are more frequent in wakeful-
ness, in contrast with symptomatic generalized syndromes,
which do not show differences in wakefulness/sleep cycle
(Zarowski et al., 2011).

2.5.2. Seizure semiology (Loddenkemper et al., 2011b; Zarowski et al.,
2011) (Table 2)
(cid:3) Atonic seizures, hypomotor seizures and myoclonic seizures.
All three happen mostly in wakefulness and during daytime.
(cid:3) Automotor seizures and hypermotor seizures. Both occur

mostly during sleep and at night.

(cid:3) Gelastic seizures, dyscognitive seizures and auras. All three
happen more frequently in wakefulness than in sleep, without
any clear differences in day or night cycle.

(cid:3) Epileptic spasms. Epileptic spasms are more frequent in
wakefulness than in sleep, without differences in day-night
cycle, with the exception of one study that demonstrated a
higher frequency during daytime (Ramgopal et al., 2012a). Fur-
thermore, this study shows differences in daytime depending
on patient age (younger patients have epileptic spasms mostly
between 9 a.m. - noon and 3 p.m.–6 p.m., and older patients
have epileptic spasms mostly during 6 a.m.–9 a.m.) (Ramgopal
et al., 2012a).

(cid:3) Tonic seizures and tonic-clonic seizures. Both happen mostly
during sleep, without differences in day/night cycle. Tonic sei-
zures show a peak around midnight and in the early morning
hours.

(cid:3) Clonic seizures. Clonic seizures occur mainly during daytime,

without differences in wakefulness/sleep cycle.

2.5.3. Clinical evolution of seizures

Several studies suggest that the clinical evolution of seizures
(speciﬁcally the clinical evolution from one semiological pattern
into the next phase) also follows non-random patterns, and occurs
at speciﬁc times, or at a particular time of the wakefulness/sleep
cycle, independent of potential confounding factors (Ramgopal
et al., 2012b; Sánchez Fernández et al., 2013). For example, a study
focusing on this topic has shown that evolution into tonic seizures
peaks between 9 p.m. - noon and during sleep; into automotor sei-
into clonic seizures peaks
zures peaks during wakefulness;

between 0–3 a.m. and 6–9 a.m. and during sleep, and into general-
ized tonic-clonic seizures (GTC) seizures peaks during sleep
(Sánchez Fernández et al., 2013). Another study focusing on the
evolution into GTC seizures has shown that evolution into GTC sei-
zures occurs more frequently between 12–3 a.m. and 6–9 a.m.
Patients with generalized EEG onset have more frequent tonic-
clonic evolution between 9 a.m. and 12 p.m., and patients with
extratemporal focal seizures are more likely to evolve into GTC
during sleep (Ramgopal et al., 2012b). In addition, this study sug-
gests that increasing patient age and sleep are the main predictors
of secondary generalization (Ramgopal et al., 2012b). Additionally,
frontal lobe seizures present with less frequent secondary general-
ization during sleep compared with other focal seizures (Herman
et al., 2001).
In conclusion, seizures may follow non-random
patterns.

2.6. Irregular patterns of seizure occurrence

The pattern of seizure occurrence is most often described over a
24 h period, and mainly inﬂuenced by time of day and sleep-wake
stage (Loddenkemper et al., 2011b; Quigg, 2000). Detailed data
from patients with intracranial monitoring devices show that the
pattern of seizure occurrence may be more irregular and complex
(Cook et al., 2016; Karoly et al., 2016). In a series of 15 patients
with refractory focal epilepsy and an implanted intracranial device,
the inter-seizure interval showed a cyclical pattern which was
more complex than a simple circadian pattern (Cook et al., 2016).
Furthermore,
seizure pattern occurrence was highly
individual-speciﬁc (Cook et al., 2016). This series showed that
patient-speciﬁc ultradian and infradian rhythms may also con-
tribute to the distribution of seizure occurrence (Karoly et al.,
2016). The mechanisms associated with ultradian and infradian
rhythms are currently unknown but may shed light on the patho-
physiology of seizure generation.

the

Studying complex distributions require numerous data points.
As seizures occur relatively rarely in any given patient, deciphering
the individual pattern of seizure occurrence might be challenging.
Additionally,
interictal epileptiform activity also follows a
rhythmic pattern (Anderson et al., 2015) and the distribution of
interictal epileptiform discharges often closely mimics that of the
distribution of seizures (Karoly et al., 2016). Therefore,
it is
possible that the analysis of interictal epileptiform discharges
may help elucidate patient-speciﬁc patterns of seizure occurrence
in the future.

2.7. Non-random patterns of status epilepticus

In contrast to the large body of literature showing that sei-
zures follow non-random patterns related to time of day and
sleep-wakefulness cycles, little is known about the diurnal and
nocturnal patterns of status epilepticus. The lack of literature on
the 24 h variation of status epilepticus might be related to the
population needed to address this question. Describing the 24 h
distribution of seizure onset is an attainable goal in a single large
epilepsy unit. In contrast, describing the 24 h distribution of sta-
tus epilepticus onset is only attainable if a very large number of
cases of status epilepticus are analyzed together. Large multicen-
ter networks studying status epilepticus (Cock et al., 2011;
Sánchez Fernández et al., 2014) or the use of large patient self-
reported databases (Goldenholz et al., 2015) might provide
answers in the near future. The distribution of status epilepticus
over time may simply reﬂect the distribution of seizures over
time or status epilepticus may have its individual 24 h distribu-
tion. Answering this question may provide insights into the
mechanisms
to status epilepticus
generation.

lead from seizures

that

8

M. Amengual-Gual et al. / Brain Research 1703 (2019) 3–12

2.8. Perimenstrual non-random patterns and other triggers

Catamenial epilepsy refers to seizures that occur in relation to
the menstrual cycle. This type of epilepsy follows an infradian
rhythm which may be entrained by environmental
infradian
rhythms, such as lunar cycle. The menstrual cycle is divided into
a follicular phase (day 1 to 14 of the cycle) and a luteal phase
(day 15 to 28 of the cycle), which are separated by ovulation
(day 14 or 15) and menstruation (which starts on day 1). These
cyclical phases are associated with changes in hormonal levels,
mainly an estradiol surge during the follicular phase followed by
a pre-ovulatory luteinizing hormone (LH) peak, and a premenstrual
decrease in progesterone levels. Based on the menstrual cycle,
three catamenial seizure patterns have been described: C1 or per-
imenstrual pattern (seizure occurrence around menstruation, from
three days before to three days later), C2 or peri-ovulatory pattern
(seizure occurrence around ovulation, from four or ﬁve days before
to one day later), and C3 pattern in anovulatory cycles (seizure
occurrence around luteal phase, from four or ﬁve days before to
three days later) (Herzog, 2015). The highest seizure likelihood
during the menstrual cycle corresponds to day 1 and the lowest
seizure likelihood corresponds to the mid-luteal day in ovulatory
cycles. Estimating the prevalence of catamenial epilepsy is chal-
lenging due to heterogeneous study inclusion and exclusion crite-
ria. A recent study estimates a prevalence of 44.2% among women
with epilepsy (Herzog, 2015).

The pathophysiology of catamenial epilepsy is based on men-
strual oscillations of the sexual hormones which have neuroactive
properties and effects on epileptic substrates (Scharfman and
MacLusky, 2006; Woolley and Schwartzkroin, 1998). Progesterone
effect may protect from seizures. In contrast, estrogen effects may
increase or decrease seizure susceptibility depending on estrogen
levels, regulation of gene expression, duration of estrogen exposi-
tion (acute or chronic), estrogen species, seizure type, neurotrans-
mitter system involved, and interaction with progesterone
(Velísková, 2006; Velísková et al., 2010). Progesterone works
mainly through its metabolite allopregnanolone, which is a potent
modulator of GABAA receptor, and through changes in GABAA
receptor subunit expression; on the other hand, estrogens are
related to many complex excitatory and inhibitory mechanisms,
involving both NMDA and non-NMDA receptors (Kalkbrenner
and Standley, 2003).

improving the effectiveness and reducing the toxicity of treat-
ments. This type of therapy may be used in the form of differential
dosing, as preparations designed to deliver sustained or pulsatile
drug at times of greatest susceptibility, or in the form of ‘zeitge-
bers’ that reset endogenous rhythms. Chronotherapy is success-
fully used in many diseases with periodic endogenous rhythms
in their pathogenesis, such as diabetes, cancer, cardiovascular dis-
eases, asthma, and arthritis (Youan, 2004).

Differential antiepileptic dosing has been shown to be useful

without increasing adverse effects in several series:

1. A study of 103 adults patients with more frequent tonic–clonic
seizures at night and previous use of sub-therapeutic doses of
phenytoin and carbamazepine found that administration of a
higher percentage of the total daily antiepileptic dose in the
evening improved seizure control and reduced side effects
(Yegnanarayan et al., 2006).

2. In a series of 17 children with nighttime seizures were treated
with differential dosing and it was found that 15 (88%) patients
responded to treatment with (cid:5) 50% seizure reduction, 11 (65%)
of these patients became seizure free, nine patients (53%)
received monotherapy after dose modiﬁcation, two patients
complained of transient side effects (fatigue / somnolence)
and none presented with worsening of seizures (Guilhoto
et al., 2011).

3. In a recent study, 27 patients with a high proportion of seizures
at nighttime (6 p.m. to 6 a.m.) were treated with clobazam dif-
ferential dosing (> 50% of the total daily dose after 6 p.m.).
Patients with differential dosing tolerated a higher median total
clobazam dose as compared to controls. Additionally, differen-
tial dose patients exhibited a median seizure reduction of 75%
as compared to 50% in controls, and patients with generalized
seizures beneﬁted the most (Thome-Souza et al., 2016).

4. Another study showed that patients tend to take their medica-
tion sooner or later than expected, which could mean that
patients adapt these times to their morning or evening pattern
(Hofstra et al., 2012).

Besides the perimenstrual non-random patterns, other non-
random patterns have been described. Many patients relate the
occurrence of their seizures to lack of sleep, higher self-reported
stress and anxiety levels, weather variation –such as changes in
temperature,
or
seasonality-, among others, and their perceptions are being pro-
gressively corroborated (Gunn and Baram, 2017; Haut et al.,
2007; Rakers et al., 2017; Rüegg et al., 2008).

humidity, wind

exposure,

force,

light

2.9. Practical implications

2.9.1. Differential antiepileptic dosing

Approximately one-third of epilepsy patients continue to have
seizures after two cycles of appropriately chosen and dosed
antiepileptic drugs (Kwan and Brodie, 2000). The availability of
multiple antiepileptic drug choices in the last years did not reduce
the proportion of medically refractory epilepsy. Chronotherapy,
based on the current understanding of chronobiology, seizure pat-
terns and sleep-wake patterns, may be a promising approach, since
seizure susceptibility patterns are often well deﬁned in epilepsy
(see previous sections) (Ramgopal et al., 2013). Chronotherapy
aims to synchronize treatment to biological rhythms and disease
patterns taking into account dynamic changes in both drug phar-
macology and disease-related processes, with the objective of

Fig. 1. Seizures patterns based on seizure onset. This ﬁgure represents seizures
patterns depending on seizure onset throughout a 24-h time period. Each type of
seizure reveals speciﬁc peaks. Generalized seizures peak at 6–12 h; temporal lobe
seizures, at 21–9 h; frontal lobe seizures, at 0–6 h; parietal lobe seizures, at 6–9 h;
and occipital lobe seizures, at 9–12 h and 15–18 h. (Reproduced with permission
from Neurology/Wolters Kluwer Health and Loddenkemper et al. (Loddenkemper
et al., 2011b)).

M. Amengual-Gual et al. / Brain Research 1703 (2019) 3–12

9

In terms of infradian rhythms, the ﬁrst large-scale study about
hormonal treatment in catamenial epilepsy supports beneﬁts from
adjuvant progesterone therapy during the luteal phase (cid:4)200 mg
TID from day 14 to 25 followed by decreasing dosage until ﬁnish
it on day 28- in women whose seizures follow a strong perimen-
strual exacerbation or C1 pattern -besides optimal antiepileptic
treatment- (Herzog, 2015).

2.9.2. Big data, machine learning, and seizure prediction

Seizures tend to occur following patient-speciﬁc patterns (Cook
et al., 2016; Karoly et al., 2016; Loddenkemper et al., 2011b). Sei-
zure prediction has been an area of intense research for decades
(Litt and Echauz, 2002; Mormann et al., 2007). Implanted intracra-

nial devices in patients with focal refractory epilepsy have pro-
vided detailed data on the pattern of clinical and subclinical
seizure occurrence (Cook et al., 2013; Morrell et al., 2011). The
analysis of these patterns suggests that seizures do not occur ran-
domly, but that they follow complex and patient-speciﬁc probabil-
ity distributions (Cook et al., 2016; Karoly et al., 2016). Implantable
intracranial devices have led the way towards seizure prediction
and closed-looped systems of seizure detection and seizure treat-
ment (Cook et al., 2013; Morrell et al., 2011). A series of 191 adults
with refractory focal epilepsy were implanted with a neurostimu-
lator
that detected abnormal electrocorticographic activity
(Morrell et al., 2011). Patients who were randomized to receive
stimulation in response to abnormal electrocorticographic activity

Fig. 2. Components of the closed-loop detection-treatment systems. The portable device has access to the patient’s health care data and contains a combination of seizures
detection modalities -accelerometer (ACM), electrocardiogram (EKG), surface electromyogram (sEMG), electroencephalogram (EEG), electrodermal activity (EDA) and video
monitoring-. When a seizure is detected, it is registered in the patient’s clinical chart – which gives information to the physician in order to improve the management of the
patient – and general registers –which allow the improvement of detection algorithms and medication management from cohort data -. Furthermore, when a seizure is
detected the caregiver is informed and this leads to a corrective response which could imply abortive pharmacotherapy, neurostimulation or a micro-pump that delivers
medication, and transport to an emergency room if needed. (Reproduced with permission from Seizure/Elsevier and Ulate-Campos et al. (Ulate-Campos et al., 2016)).

10

M. Amengual-Gual et al. / Brain Research 1703 (2019) 3–12

presented with a much higher reduction in seizure frequency than
patients randomized to no stimulation, with no difference in
adverse events (Morrell et al., 2011). A series of 15 patients with
focal refractory epilepsy demonstrated that seizure prediction is
feasible, with prediction of seizure occurrence better than chance
(Cook et al., 2013). However, two major aspects limit the applica-
tion of these methods to the wider population of epileptic patients.
First, the positive and negative predictive values of the detection
algorithms are still far from what would be considered appropriate
for clinically meaningful prediction. More importantly, prediction
based on intracranial EEG data is only applicable to a minority of
patients with epilepsy in whom the beneﬁts of detecting seizures
outweigh the risks of neurosurgery and of an implanted intracra-
nial device.

As many seizures tend to occur in predictable patterns, these
patterns may be amenable to detection based on the occurrence
of clinical seizures. The recent more widespread use of electronic
seizure diaries makes it feasible and relatively straightforward to
collect large amounts of information on patients with epilepsy.
Electronic seizure diaries provide the amount of data points that
might allow identiﬁcation of complex seizure patterns. The rapidly
increasing size of clinical databases allows for development of
more complex models that may improve treatment selection
(Devinsky et al., 2016) and may reﬁne seizure prediction models
developed in databases of limited size (Hall et al., 2009). When
the seizure number is sufﬁciently large, the possibility to predict
seizure occurrence (Cook et al., 2016) and seizure counts
(Tharayil et al., 2017) becomes more likely. The application of
machine learning algorithms on clinical data may allow prediction
of seizure occurrence (Sánchez Fernández et al., 2016). Simple
learning algorithms like robust linear regression and random for-
ests may be the building blocks of more complex approaches like
deep learning. Once developed, these algorithms may be integrated
in clinically applicable devices. Integration of learning algorithms
into wearable detection devices may lead to closed-loop systems
for seizure detection and prediction (Ulate-Campos et al., 2016).

2.10. Future directions: seizure detection and seizure prediction in the
ambulatory setting

The quality of life of patients with chronic diseases and their
caregivers is an often overlooked aspect in treatment. Patients with
epilepsy may be better managed remotely by closed-loop
detection-treatment systems and may beneﬁt from reducing hos-
pital appointments and EEG recordings. Patients with epilepsy,
especially patients with uncontrolled epilepsy, are in urgent need
of seizure susceptibility prediction devices (Schulze-Bonhage
et al., 2010).

Technology to detect seizures using devices other than EEG is
now available (Ramgopal et al., 2014b; van Andel et al., 2016).
These devices are based on extra-cerebral signals. For example,
accelerometers, gyroscopes, magnetometers and video recordings
have proven useful in detecting movement of patients during sei-
zures; electromyography may detect the tonic phase of seizures;
electrocardiography or breathing/saturation sensors may detect
changes in heart rate or respiration respectively, allowing seizure
detection; and electrodermal activity could change due to sweat-
ing, meaning activation of the sympathetic nervous system.
Depending on the seizure type, selected electrophysiological pat-
terns or combinations of signals may work better for individual
patients and seizure patterns (Ulate-Campos et al., 2016). Further-
more, this technology has already been integrated into portable
devices which may facilitate detection of seizures in ambulatory
settings (Fig. 2).

Some algorithms for detecting generalized tonic-clonic seizures
have proven to be useful in clinical settings (van Andel et al., 2016),

and work is ongoing to improve the detection of other seizure
types. However, some technical difﬁculties in home settings –such
as interferences and alarm fatigue, data privacy and high false pos-
itive rates – are aspects that leave room for future improvements
(van Andel et al., 2016). Despite these issues, in the near future
the development of these technologies in portable devices may
modify the ﬁeld of epilepsy, such as diagnostic methods, treatment
and follow-up. In addition to improving quality of life, portable
devices may also reduce morbidity and mortality in epilepsy due
to rapid seizure detection and instant tailored treatment (Van de
Vel et al., 2013).

In summary, implementing machine learning driven closed-
loop detection, prediction, and treatment systems in routine clini-
cal practice is the research prospect that promises to revolutionize
the ﬁeld of epilepsy.

3. Conclusion

Despite their apparently random occurrence, seizures tend to
occur following complex and patient-speciﬁc probability distribu-
tions. A better understanding of these patterns -thanks to machine
learning techniques and artiﬁcial as well as neuronal networks-
may allow the development of closed-loop detection, prediction,
and treatment systems that may change the ﬁeld of epilepsy and
drastically improve the quality of life of patients with epilepsy.

Acknowledgements

Marta Amengual-Gual is funded by a grant for the study of status
epilepticus from ‘‘Fundación Alfonso Martín Escudero”.

ETHICS

This
standards.

FUNDING

study

complied with

biomedical research ethical

This study was supported by the Epilepsy Research Fund.

DECLARATION OF INTEREST

Iván Sánchez Fernández was funded by a grant for the study of
Epileptic Encephalopathies from ‘‘Fundación Alfonso Martín Escud-
ero” and by the HHV6 Foundation.

Tobias Loddenkemper serves on the Laboratory Accreditation
Board for Long Term (Epilepsy and Intensive Care Unit) Monitoring,
on the Council (and as Vice President) of the American Clinical
Neurophysiology Society, on the American Board of Clinical Neuro-
physiology, as an Associate Editor for Seizure, and as an Associate
Editor for Wyllie’s Treatment of Epilepsy 6th edition. He is part of
pending patent applications to detect and predict seizures and to
diagnose epilepsy. He receives research support from the Epilepsy
Research Fund, the American Epilepsy Society, the Epilepsy Foun-
dation of America, the Epilepsy Therapy Project, PCORI, the Pedi-
atric Epilepsy Research Foundation, CURE, HHV-6 Foundation,
and received research grants from Lundbeck, Eisai, Upsher-Smith,
Acorda, and Pﬁzer. He serves as a consultant for Zogenix, Upsher
Smith and Lundbeck. He performs video electroencephalogram
long-term and ICU monitoring, electroencephalograms, and other
electrophysiological studies at Boston Children’s Hospital and afﬁl-
iated hospitals and bills for these procedures and he evaluates
pediatric neurology patients and bills for clinical care. He has
received speaker honorariums from national societies including
the AAN, AES and ACNS, and for grand rounds at various academic

M. Amengual-Gual et al. / Brain Research 1703 (2019) 3–12

11

centers. His wife, Dr. Karen Stannard, is a pediatric neurologist and
she performs video electroencephalogram long-term and ICU mon-
itoring, electroencephalograms, and other electrophysiological
studies and bills for these procedures and she evaluates pediatric
neurology patients and bills for clinical care.

The authors report no potential conﬂicts of interest.

CONTRIBUTORS

Marta Amengual-Gual participated in drafting and revising the
manuscript for content, including medical writing for content, in
study concept and design, and study supervision.

Iván Sánchez Fernández participated in including medical writ-
ing for content, in study concept and design, and study supervision
or coordination.

Tobias Loddenkemper participated in medical writing for con-
in study concept and design, and study supervision or

tent,
coordination.

References

Anderson, C.T., Tcheng, T.K., Sun, F.T., Morrell, M.J., 2015. Day-night patterns of
long-term ambulatory

epileptiform activity
electrocorticography. J. Clin. Neurophysiol. 32, 406–412.

patients with

65

in

Baxendale, S., Fisher, J., 2008. Moonstruck? The effect of the lunar cycle on seizures.

Epilepsy Behav. 13, 549–550.

Bell-Pedersen, D., Cassone, V.M., Earnest, D.J., Golden, S.S., Hardin, P.E., Thomas, T.L.,
Zoran, M.J., 2005. Circadian rhythms from multiple oscillators: lessons from
diverse organisms. Nat. Rev. Genet. 6, 544–556.

Chaudhary, U.J., Duncan, J.S., Lemieux, L., 2011. A dialogue with historical concepts
of epilepsy from the Babylonians to Hughlings Jackson: persistent beliefs.
Epilepsy Behav. 21, 109–114.

Cock, H.R., ESETT Group, 2011. Established status epilepticus treatment trial

(ESETT). Epilepsia 52 (Suppl 8), 50–52.

Cook, M.J., O’Brien, T.J., Berkovic, S.F., Murphy, M., Morokoff, A., Fabinyi, G., D’Souza,
W., Yerra, R., Archer, J., Litewka, L., Hosking, S., Lightfoot, P., Ruedebusch, V.,
Shefﬁeld, W.D., Snyder, D., Leyde, K., Himes, D., 2013. Prediction of seizure
likelihood with a long-term, implanted seizure advisory system in patients with
drug-resistant epilepsy: a ﬁrst-in-man study. Lancet Neurol. 12, 563–571.
Cook, M.J., Karoly, P.J., Freestone, D.R., Himes, D., Leyde, K., Berkovic, S., O’Brien, T.,
Grayden, D.B., Boston, R., 2016. Human focal seizures are characterized by
populations of ﬁxed duration and interval. Epilepsia 57, 359–368.

Devinsky, O., Dilley, C., Ozery-Flato, M., Aharonov, R., Goldschmidt, Y., Rosen-Zvi, M.,
Clark, C., Fritz, P., 2016. Changing the approach to treatment choice in epilepsy
using big data. Epilepsy Behav. 56, 32–37.

Drury,

I., Smith, B., Li, D., Savit, R., 2003. Seizure prediction using scalp

electroencephalogram. Exp. Neurol. 184 (Suppl 1), S9–S18.

Durazzo, T.S., Spencer, S.S., Duckrow, R.B., Novotny, E.J., Spencer, D.D., Zaveri, H.P.,
2008. Temporal distributions of seizure occurrence from various epileptogenic
regions. Neurology 70, 1265–1271.

Eadie, M.J., 2012. Sir Charles Locock and potassium bromide. J. R. Coll Phys. Edinb.

42, 274–279.

Elger, C.E., Widman, G., Andrzejak, R., Arnhold, J., David, P., Lehnertz, K., 2000.
Nonlinear EEG analysis and its potential role in epileptology. Epilepsia 41
(Suppl 3), S34–S38.

Ferri, R., Elia, M., Musumeci, S.A., Stam, C.J., 2001. Non-linear EEG analysis in
children with epilepsy and electrical status epilepticus during slow-wave sleep
(ESES). Clin. Neurophysiol. 112, 2274–2280.

Goldenholz, D.M., Moss, R., Scott, J., Auh, S., Theodore, W.H., 2015. Confusing
placebo effect with natural history in epilepsy: a big data approach. Ann.
Neurol. 78, 329–336.

Guilhoto, L.M., Loddenkemper, T., Vendrame, M., Bergin, A., Bourgeois, B.F., Kothare,
S.V., 2011. Higher evening antiepileptic drug dose for nocturnal and early-
morning seizures. Epilepsy Behav. 20, 334–337.

Gunn, B.G., Baram, T.Z., 2017. Stress and seizures: space, time and hippocampal

circuits. Trends Neurosci.

Hall, C.B., Lipton, R.B., Tennen, H., Haut, S.R., 2009. Early follow-up data from seizure
diaries can be used to predict subsequent seizures in same cohort by borrowing
strength across participants. Epilepsy Behav. 14, 472–475.

Haut, S.R., 2015. Seizure clusters: characteristics and treatment. Curr. Opin. Neurol.

28, 143–150.

Haut, S.R., Hall, C.B., Masur, J., Lipton, R.B., 2007. Seizure occurrence: precipitants

and prediction. Neurology 69, 1905–1910.

Herman, S.T., Walczak, T.S., Bazil, C.W., 2001. Distribution of partial seizures during
the sleep–wake cycle: differences by seizure onset site. Neurology 56, 1453–
1459.

Herzog, A.G., 2015. Catamenial epilepsy: update on prevalence, pathophysiology
and treatment from the ﬁndings of the NIH Progesterone Treatment Trial.
Seizure 28, 18–25.

Hofstra, W.A., de Weerd, A.W., 2009. The circadian rhythm and its interaction with

human epilepsy: a review of literature. Sleep Med. Rev. 13, 413–420.

Hofstra, W.A., Grootemarsink, B.E., Dieker, R., van der Palen, J., de Weerd, A.W., 2009.
Temporal distribution of clinical seizures over the 24-h day: a retrospective
observational study in a tertiary epilepsy clinic. Epilepsia 50, 2019–2026.

Hofstra, W.A., van der Palen,

J., de Weerd, A.W., 2012. Morningness and
eveningness: when do patients take their antiepileptic drugs? Epilepsy Behav.
23, 320–323.

Iasemidis, L.D., Sackellares,
Neuroscientist 2, 118–126.

J.C., 1996. Chaos Theory and Epilepsy. The

Jacoby, A., 1992. Epilepsy and the quality of everyday life. Findings from a study of

people with well-controlled epilepsy. Soc. Sci. Med. 34, 657–666.

Kaleyias, J., Loddenkemper, T., Vendrame, M., Das, R., Syed, T.U., Alexopoulos, A.V.,
Wyllie, E., Kothare, S.V., 2011. Sleep-wake patterns of seizures in children with
lesional epilepsy. Pediatr. Neurol. 45, 109–113.

Kalkbrenner, K.A., Standley, C.A., 2003. Estrogen modulation of NMDA-induced
seizures in ovariectomized and non-ovariectomized rats. Brain Res. 964, 244–
249.

Karoly, P.J., Freestone, D.R., Boston, R., Grayden, D.B., Himes, D., Leyde, K.,
Seneviratne, U., Berkovic, S., O’Brien, T., Cook, M.J., 2016. Interictal spikes and
epileptic seizures: their relationship and underlying rhythmicity. Brain 139,
1066–1078.

Kothare, S.V., Zarowski, M., 2011. Sleep and epilepsy: common bedfellows. J. Clin.

Neurophysiol. 28, 101–102.

Kotwas, I., McGonigal, A., Trebuchon, A., Bastien-Toniazzo, M., Nagai, Y., Bartolomei,
J.A., 2016. Self-control of epileptic seizures by

F., Micoulaud-Franchi,
nonpharmacological strategies. Epilepsy Behav. 55, 157–164.

Kramer, M.A., Truccolo, W., Eden, U.T., Lepage, K.Q., Hochberg, L.R., Eskandar, E.N.,
Madsen, J.R., Lee, J.W., Maheshwari, A., Halgren, E., Chu, C.J., Cash, S.S., 2012.
Human seizures self-terminate across spatial scales via a critical transition.
Proc. Natl. Acad. Sci. U.S.A. 109, 21116–21121.

Kwan, P., Brodie, M.J., 2000. Early identiﬁcation of refractory epilepsy. N. Engl. J.

Med. 342, 314–319.

Lehnertz, K., 1999. Non-linear time series analysis of intracranial EEG recordings in

patients with epilepsy–an overview. Int. J. Psychophysiol. 34, 45–52.

Litt, B., Echauz, J., 2002. Prediction of epileptic seizures. Lancet Neurol. 1, 22–30.
Litt, B., Esteller, R., Echauz, J., D’Alessandro, M., Shor, R., Henry, T., Pennell, P., Epstein,
C., Bakay, R., Dichter, M., Vachtsevanos, G., 2001. Epileptic seizures may begin
hours in advance of clinical onset: a report of ﬁve patients. Neuron 30, 51–64.
Loddenkemper, T., Lockley, S.W., Kaleyias, J., Kothare, S.V., 2011a. Chronobiology of
epilepsy: diagnostic and therapeutic implications of chrono-epileptology. J.
Clin. Neurophysiol. 28, 146–153.

Loddenkemper, T., Vendrame, M., Zarowski, M., Gregas, M., Alexopoulos, A.V.,
Wyllie, E., Kothare, S.V., 2011b. Circadian patterns of pediatric seizures.
Neurology 76, 145–153.

Magiorkinis, E., Sidiropoulou, K., Diamantis, A., 2010. Hallmarks in the history of

epilepsy: epilepsy in antiquity. Epilepsy Behav. 17, 103–108.

Mormann, F., Andrzejak, R.G., Elger, C.E., Lehnertz, K., 2007. Seizure prediction: the

long and winding road. Brain 130, 314–333.

Morrell, M.J., RNS System in Epilepsy Study Group, 2011. Responsive cortical
stimulation for the treatment of medically intractable partial epilepsy.
Neurology 77, 1295–1304.

Panda, S., Sato, T.K., Castrucci, A.M., Rollag, M.D., DeGrip, W.J., Hogenesch, J.B.,
Provencio, I., Kay, S.A., 2002. Melanopsin (Opn4) requirement for normal light-
induced circadian phase shifting. Science 298, 2213–2216.

Pavlova, M.K., Shea, S.A., Bromﬁeld, E.B., 2004. Day/night patterns of focal seizures.

Epilepsy Behav. 5, 44–49.

Polychronopoulos, P., Argyriou, A.A., Sirrou, V., Huliara, V., Aplada, M., Gourzis, P.,
Economou, A., Terzis, E., Chroni, E., 2006. Lunar phases and seizure occurrence:
just an ancient legend? Neurology 66, 1442–1443.

Quigg, M., 2000. Circadian rhythms: interactions with seizures and epilepsy.

Epilepsy Res. 42, 43–55.

Quigg, M., Straume, M., Menaker, M., Bertram, E.H., 1998. Temporal distribution of
partial seizures: comparison of an animal model with human partial epilepsy.
Ann. Neurol. 43, 748–755.

Raison, C.L., Klein, H.M., Steckler, M., 1999. The moon and madness reconsidered. J.

Affect Disord. 53, 99–106.

Rakers, F., Walther, M., Schiffner, R., Rupprecht, S., Rasche, M., Kockler, M., Witte, O.
W., Schlattmann, P., Schwab, M., 2017. Weather as a risk factor for epileptic
seizures: a case-crossover study. Epilepsia 58, 1287–1295.

Ramgopal, S., Vendrame, M., Shah, A., Gregas, M., Zarowski, M., Rotenberg, A.,
Alexopoulos, A.V., Wyllie, E., Kothare, S.V., Loddenkemper, T., 2012b. Circadian
patterns of generalized tonic-clonic evolutions in pediatric epilepsy patients.
Seizure 21, 535–539.

Ramgopal, S., Shah, A., Zarowski, M., Vendrame, M., Gregas, M., Alexopoulos, A.V.,
Loddenkemper, T., Kothare, S.V., 2012a. Diurnal and sleep/wake patterns of
epileptic spasms in different age groups. Epilepsia 53, 1170–1177.

Ramgopal, S., Thome-Souza, S., Loddenkemper, T., 2013. Chronopharmacology of

anti-convulsive therapy. Curr. Neurol. Neurosci. Rep. 13, 339.

Ramgopal, S., Powell, C., Zarowski, M., Alexopoulos, A.V., Kothare, S.V.,
Loddenkemper, T., 2014a. Predicting diurnal and sleep/wake seizure patterns
in paediatric patients of different ages. Epileptic Disord. 16, 56–66.

Ramgopal, S., Thome-Souza, S., Jackson, M., Kadish, N.E., Sánchez Fernández, I.,
Klehm, J., Bosl, W., Reinsberger, C., Schachter, S., Loddenkemper, T., 2014b.
Seizure detection, seizure prediction, and closed-loop warning systems in
epilepsy. Epilepsy Behav. 37, 291–307.

12

M. Amengual-Gual et al. / Brain Research 1703 (2019) 3–12

Rüegg, S., Hunziker, P., Marsch, S., Schindler, C., 2008. Association of environmental

factors with the onset of status epilepticus. Epilepsy Behav. 12, 66–73.

Sánchez Fernández, I., Abend, N.S., Agadi, S., An, S., Arya, R., Carpenter, J.L., Chapman,
K.E., Gaillard, W.D., Glauser, T.A., Goldstein, D.B., Goldstein, J.L., Goodkin, H.P.,
Hahn, C.D., Heinzen, E.L., Mikati, M.A., Peariso, K., Pestian, J.P., Ream, M., Riviello,
J.J., Tasker, R.C., Williams, K., Loddenkemper, T., (pSERG), P.S.E.R.G.,, 2014. Gaps
and opportunities in refractory status epilepticus research in children: a multi-
center approach by the Pediatric Status Epilepticus Research Group (pSERG).
Seizure. 23, 87–97.

Sánchez Fernández, I., Goldenholz, D.M., Gainza-Lein, M., Moss, R., Theodore, W.H.,
Loddenkemper, T., 2016. Prediction of time of occurrence and lenght of seizures
based on basic demographic and clinical data using machine learning
algorithms. In American Epilepsy Society Meeting. Houston, Tx. https://www.
aesnet.org/meetings_events/annual_meeting_abstracts/view/183197.

Sánchez Fernández, I., Ramgopal, S., Powell, C., Gregas, M., Zarowski, M., Shah, A.,
Vendrame, M., Alexopoulos, A.V., Kothare, S.V., Loddenkemper, T., 2013. Clinical
evolution of seizures: distribution across time of day and sleep/wakefulness
cycle. J. Neurol. 260, 549–557.

Thome-Souza, S., Klehm, J., Jackson, M., Kadish, N.E., Manganaro, S., Fernández, I.S.,
Loddenkemper, T., 2016. Clobazam higher-evening differential dosing as an
add-on therapy in refractory epilepsy. Seizure 40, 1–6.

Ulate-Campos, A., Coughlin, F., Gaínza-Lein, M., Fernández,

I.S., Pearl, P.L.,
Loddenkemper, T., 2016. Automated seizure detection systems and their
effectiveness for each type of seizure. Seizure 40, 88–101.

van Andel, J., Thijs, R.D., de Weerd, A., Arends, J., Leijten, F., 2016. Non-EEG based
ambulatory seizure detection designed for home use: what is available and how
will it inﬂuence epilepsy care? Epilepsy Behav. 57, 82–89.

Van de Vel, A., Cuppens, K., Bonroy, B., Milosevic, M., Jansen, K., Van Huffel, S.,
Vanrumste, B., Lagae, L., Ceulemans, B., 2013. Non-EEG seizure-detection
systems and potential SUDEP prevention: state of the art. Seizure 22, 345–355.
van der Heyden, M.J., Velis, D.N., Hoekstra, B.P., Pijn, J.P., van Emde Boas, W., van
Veelen, C.W., van Rijen, P.C., Lopes da Silva, F.H., DeGoede, J., 1999. Non-linear
analysis of
lobe epilepsy. Clin.
Neurophysiol. 110, 1726–1740.

intracranial human EEG in temporal

Velísková, J., 2006. The role of estrogens in seizures and epilepsy: the bad guys or

the good guys? Neuroscience 138, 837–844.

Saper, C.B., Scammell, T.E., Lu, J., 2005. Hypothalamic regulation of sleep and

Velísková, J., De Jesus, G., Kaur, R., Velísek, L., 2010. Females, their estrogens, and

circadian rhythms. Nature 437, 1257–1263.

seizures. Epilepsia 51 (Suppl 3), 141–144.

Scharfman, H.E., MacLusky, N.J., 2006. The inﬂuence of gonadal hormones on
neuronal excitability, seizures, and epilepsy in the female. Epilepsia 47, 1423–
1440.

Venkataraman, V., Vlachos, I., Faith, A., Krishnan, B., Tsakalis, K., Treiman, D.,
Iasemidis, L., 2014. Brain dynamics based automated epileptic seizure
detection. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2014, 946–949.

Schindler, K., Gast, H., Stieglitz, L., Stibal, A., Hauf, M., Wiest, R., Mariani, L., Rummel,
C., 2011. Forbidden ordinal patterns of periictal
intracranial EEG indicate
deterministic dynamics in human epileptic seizures. Epilepsia 52, 1771–1780.
Schulze-Bonhage, A., Sales, F., Wagner, K., Teotonio, R., Carius, A., Schelle, A., Ihle, M.,
2010. Views of patients with epilepsy on seizure prediction devices. Epilepsy
Behav. 18, 388–396.

Smolensky, M.H., Peppas, N.A., 2007. Chronobiology, drug delivery, and

chronotherapeutics. Adv. Drug Deliv. Rev. 59, 828–851.

Tezer, F.I., Rémi,

J., Erbil, N., Noachtar, S., Saygi, S., 2014. A reduction of
sleep spindles heralds seizures in focal epilepsy. Clin. Neurophysiol. 125,
2207–2211.

Tharayil, J.J., Chiang, S., Moss, R., Stern, J.M., Theodore, W.H., Goldenholz, D.M., 2017.
A big data approach to the development of mixed-effects models for seizure
count data. Epilepsia 58, 835–844.

Wilson, J.V., Reynolds, E.H., 1990. Texts and documents. Translation and analysis of
a cuneiform text forming part of a Babylonian treatise on epilepsy. Med. Hist.
34, 185–198.

Woolley, C.S., Schwartzkroin, P.A., 1998. Hormonal effects on the brain. Epilepsia 39

(Suppl 8), S2–S8.

Yegnanarayan, R., Mahesh, S.D., Sangle, S., 2006. Chronotherapeutic dose schedule
of phenytoin and carbamazepine in epileptic patients. Chronobiol. Int. 23,
1035–1046.

Youan, B.B., 2004. Chronopharmaceutics: gimmick or clinically relevant approach to

drug delivery? J. Control Release. 98, 337–353.

Zarowski, M., Loddenkemper, T., Vendrame, M., Alexopoulos, A.V., Wyllie, E.,
Kothare, S.V., 2011. Circadian distribution and sleep/wake patterns of
generalized seizures in children. Epilepsia 52, 1076–1083.
