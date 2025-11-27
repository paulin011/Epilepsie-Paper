# Håkansson - 2023 - Machine learning and big data for personalized epilepsy treatment

Machine learning and big data 
for personalized epilepsy 
treatment 

Samuel Håkansson 

Department of Clinical Neuroscience 
Institute of Neuroscience and Physiology 
Sahlgrenska Academy, University of Gothenburg 

Gothenburg 2023 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Cover illustration by DALL·E 2 

Machine learning and big data for personalized epilepsy treatment 
© Samuel Håkansson 2023 
samuel.hakansson@gu.se 

ISBN 978-91-8069-313-4 (PRINT)  
ISBN 978-91-8069-314-1 (PDF) 

Printed in Borås, Sweden 2023 
Printed by Stema Specialtryck AB 

SVANENMÄRKET
SVANENMÄRKET

Trycksak
Trycksak
3041 0234
3041 0234

-  But what is a girl addicted to fun supposed to do 

Maddy Bishop 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Cover illustration by DALL·E 2 

Machine learning and big data for personalized epilepsy treatment 

© Samuel Håkansson 2023 

samuel.hakansson@gu.se 

ISBN 978-91-8069-313-4 (PRINT)  

ISBN 978-91-8069-314-1 (PDF) 

Printed in Borås, Sweden 2023 

Printed by Stema Specialtryck AB 

-  But what is a girl addicted to fun supposed to do 
Maddy Bishop 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
ABSTRACT 

Finding an effective anti-seizure medication (ASM) with minimal side 

effects is a challenge. Patient characteristics are used to guide treatment 

selection, but about half of the patients with epilepsy do not achieve seizure 

freedom with their first ASM. While randomized controlled trials are the 

gold standard for estimating treatment efficacy, they may not always be 

clinically relevant, especially for rare conditions. Registers are valuable 

sources of data because they can contain many patients, are accessible, and 

are updated regularly. The aim of the present research is to evaluate 

registers and develop machine learning algorithms for personalized 

medicine in epilepsy.  

We used prescriptions, in- and outpatient data, and mortality data from 

national Swedish registers to model ASM use of patients. As a bundled 

estimation of efficacy and tolerability, retention rate was used as the 

measure of outcome.  

The results indicate that using register data to estimate retention of ASMs is 

feasible and personalized ASM selection can potentially improve patient 

outcomes. Retention rates from registers are similar to that of RCTs and 

meta-analyses of RCTs. In an analysis of patients with epilepsy and 

comorbidities, there was a potential improvement of 14-21% of the 5-year 

retention rate for the initial ASM (Paper I). Ranking of ASMs for patient 

cases based on retention rates from register data is similar to suggestions 

based on expert advice (Paper II). We also studied ASM use in children, a 

group with limited evidence (Paper III). Specialized machine learning 

algorithms can potentially be a useful source of information for doctors for 

selecting ASMs (Paper IV).  

In conclusion, this research highlights the potential of registers as a data 

source for personalized medicine. Machine learning trained on register data 

can be used to predict the efficacy of ASMs, but the methodology needs 

further development and clinical verification. 

Keywords: anti-seizure medication, personalized treatment, machine 

learning 

 
 
 
 
 
 
 
 
 
 
 
ABSTRACT 

Finding an effective anti-seizure medication (ASM) with minimal side 
effects is a challenge. Patient characteristics are used to guide treatment 
selection, but about half of the patients with epilepsy do not achieve seizure 
freedom with their first ASM. While randomized controlled trials are the 
gold standard for estimating treatment efficacy, they may not always be 
clinically relevant, especially for rare conditions. Registers are valuable 
sources of data because they can contain many patients, are accessible, and 
are updated regularly. The aim of the present research is to evaluate 
registers and develop machine learning algorithms for personalized 
medicine in epilepsy.  

We used prescriptions, in- and outpatient data, and mortality data from 
national Swedish registers to model ASM use of patients. As a bundled 
estimation of efficacy and tolerability, retention rate was used as the 
measure of outcome.  

The results indicate that using register data to estimate retention of ASMs is 
feasible and personalized ASM selection can potentially improve patient 
outcomes. Retention rates from registers are similar to that of RCTs and 
meta-analyses of RCTs. In an analysis of patients with epilepsy and 
comorbidities, there was a potential improvement of 14-21% of the 5-year 
retention rate for the initial ASM (Paper I). Ranking of ASMs for patient 
cases based on retention rates from register data is similar to suggestions 
based on expert advice (Paper II). We also studied ASM use in children, a 
group with limited evidence (Paper III). Specialized machine learning 
algorithms can potentially be a useful source of information for doctors for 
selecting ASMs (Paper IV).  

In conclusion, this research highlights the potential of registers as a data 
source for personalized medicine. Machine learning trained on register data 
can be used to predict the efficacy of ASMs, but the methodology needs 
further development and clinical verification. 

Keywords: anti-seizure medication, personalized treatment, machine 
learning 

 
 
 
 
 
 
 
 
 
 
 
SAMMANFATTNING PÅ SVENSKA 

Epilepsi behandlas oftast med antiepileptika. Men att hitta rätt medicin som 

minskar risken för anfall och samtidigt ger så få biverkningar som möjligt är 

svårt. Val av antiepileptikum grundas på bland annat ålder, kön, typ av 

epilepsi och samjuklighet, men trots det blir hälften av alla patienter inte 

anfallsfria av första testade antiepileptikum. Randomiserade kontrollerade 

studier (RCT) anses vara det bästa underlaget för att bedömma effekt av 

mediciner, men det är inte alltid de är kliniskt relevanta, speciellt för 

ovanliga tillstånd eller syndrom. Register är värdefulla datakällor eftersom 

att de har information om många patienter, är tillgängliga, och uppdateras 

regelbundet. Målet med denna forskning är att utvärdera register som 

datakälla och utveckla maskininlärningsalgoritmer för precisionsmedicin 

inom epilepsi. 

Vi har använt svenska nationella registerdata av recept, sluten- och 

öppenvård samt död för att modellera patienters användning av 

antiepileptika. Som ett aggregerat mått av effekt och tolerabilitet har vi 

använt retention som måttet på utfall av antiepileptika. 

Resultaten i denna avhandling indikerar att det är möjligt att använda 

registerdata för att uppskatta retention och att patientanpassat val av 

antiepileptika kan öka retentionen. Retentionsgrader uppskattade genom 

registerdata liknar de av RCTer samt meta-analyser av RCTer. I en analys 

med patienter med komorbiditeter fann vi en potentiell ökning av 

retentionsgraden med 14-21% efter 5 år för första antiepileptikum. Att 

rangordna antiepileptika efter retentionsgrad ger liknande resultat som 

förslag baserade på expertråd. Maskininlärningsalgoritmer som är 

specialiserade för observationell registerdata kan bli användbart som 

beslutsunderlag för att välja bästa möjliga medicin. 

Forskningen i denna avhandling belyser potentialen hos register som 

datakälla för precisionsmedicin. Maskininlärningsalgoritmer tränade på 

registerdata skulle kunna användas för att förutsäga utfallet av 

antiepileptika, men metodiken behöver vidareutvecklas och verifieras 

kliniskt.

 
 
 
 
 
 
 
SAMMANFATTNING PÅ SVENSKA 

Epilepsi behandlas oftast med antiepileptika. Men att hitta rätt medicin som 
minskar risken för anfall och samtidigt ger så få biverkningar som möjligt är 
svårt. Val av antiepileptikum grundas på bland annat ålder, kön, typ av 
epilepsi och samjuklighet, men trots det blir hälften av alla patienter inte 
anfallsfria av första testade antiepileptikum. Randomiserade kontrollerade 
studier (RCT) anses vara det bästa underlaget för att bedömma effekt av 
mediciner, men det är inte alltid de är kliniskt relevanta, speciellt för 
ovanliga tillstånd eller syndrom. Register är värdefulla datakällor eftersom 
att de har information om många patienter, är tillgängliga, och uppdateras 
regelbundet. Målet med denna forskning är att utvärdera register som 
datakälla och utveckla maskininlärningsalgoritmer för precisionsmedicin 
inom epilepsi. 

Vi har använt svenska nationella registerdata av recept, sluten- och 
öppenvård samt död för att modellera patienters användning av 
antiepileptika. Som ett aggregerat mått av effekt och tolerabilitet har vi 
använt retention som måttet på utfall av antiepileptika. 

Resultaten i denna avhandling indikerar att det är möjligt att använda 
registerdata för att uppskatta retention och att patientanpassat val av 
antiepileptika kan öka retentionen. Retentionsgrader uppskattade genom 
registerdata liknar de av RCTer samt meta-analyser av RCTer. I en analys 
med patienter med komorbiditeter fann vi en potentiell ökning av 
retentionsgraden med 14-21% efter 5 år för första antiepileptikum. Att 
rangordna antiepileptika efter retentionsgrad ger liknande resultat som 
förslag baserade på expertråd. Maskininlärningsalgoritmer som är 
specialiserade för observationell registerdata kan bli användbart som 
beslutsunderlag för att välja bästa möjliga medicin. 

Forskningen i denna avhandling belyser potentialen hos register som 
datakälla för precisionsmedicin. Maskininlärningsalgoritmer tränade på 
registerdata skulle kunna användas för att förutsäga utfallet av 
antiepileptika, men metodiken behöver vidareutvecklas och verifieras 
kliniskt.

 
 
 
 
 
 
 
LIST OF PAPERS  

Roman numerals. 

This thesis is based on the following studies, referred to in the text by their 

I. 

Samuel Håkansson, Markus Karlander, David Larsson, 

Zamzam Mahamud, Sara Garcia‐Ptacek, Aleksej Zelezniak, 

Johan Zelano.  

Potential for improved retention rate by personalized 

antiseizure medication selection: A register-based analysis 

Epilepsia 2021; 62(9): 2123-2132. 

https://doi.org/10.1111/epi.16987. 

II. 

Samuel Håkansson, Johan Zelano.  

Big data analysis of ASM retention rates and expert ASM 

algorithm: A comparative study 

Epilepsia 2022; 63(6): 1553-1562. 

https://doi.org/10.1111/epi.17235. 

III. 

Samuel Håkansson, Ronny Wickström, Johan Zelano. 

Selection and continuation of antiseizure medication in 

children with epilepsy in Sweden 2007-2020. 

Pediatric Neurology 2023; 144: 19-25. 

https://doi.org/10.1016/j.pediatrneurol.2023.03.016 

IV. 

Samuel Håkansson, Fredrik D. Johansson, Aleksej 

Zelezniak, Johan Zelano. 

Personalized anti-seizure medication selection using 

counterfactual time-to-event machine learning: a national 

retrospective study. 

Manuscript. 

i 

 
 
 
 
LIST OF PAPERS  
This thesis is based on the following studies, referred to in the text by their 
Roman numerals. 

I. 

II. 

III. 

IV. 

Samuel Håkansson, Markus Karlander, David Larsson, 
Zamzam Mahamud, Sara Garcia‐Ptacek, Aleksej Zelezniak, 
Johan Zelano.  
Potential for improved retention rate by personalized 
antiseizure medication selection: A register-based analysis 
Epilepsia 2021; 62(9): 2123-2132. 
https://doi.org/10.1111/epi.16987. 

Samuel Håkansson, Johan Zelano.  
Big data analysis of ASM retention rates and expert ASM 
algorithm: A comparative study 
Epilepsia 2022; 63(6): 1553-1562. 
https://doi.org/10.1111/epi.17235. 

Samuel Håkansson, Ronny Wickström, Johan Zelano. 
Selection and continuation of antiseizure medication in 
children with epilepsy in Sweden 2007-2020. 
Pediatric Neurology 2023; 144: 19-25. 
https://doi.org/10.1016/j.pediatrneurol.2023.03.016 

Samuel Håkansson, Fredrik D. Johansson, Aleksej 
Zelezniak, Johan Zelano. 
Personalized anti-seizure medication selection using 
counterfactual time-to-event machine learning: a national 
retrospective study. 
Manuscript. 

i 

 
 
 
 
ACKNOWLEDGEMENTS .................................................................................. 49 

REFERENCES .................................................................................................. 50 

CONTENT 
ABBREVIATIONS ............................................................................................. IV 

INTRODUCTION ................................................................................................ 5 

BACKGROUND ................................................................................................. 7 

Epilepsy and anti-seizure medications .......................................................... 7 

ASM selection and side effects ............................................................... 8 

Measuring efficacy of ASMs ................................................................... 9 

Clinical trials of ASMs .......................................................................... 10 

Observational studies of ASMs ............................................................. 14 

Time-to-event statistics ............................................................................... 15 

Estimating treatment effect from observational data .................................. 15 

Machine learning for personalized treatment selection .............................. 15 

Machine learning in epilepsy ...................................................................... 16 

AIM ................................................................................................................ 17 

METHODS ...................................................................................................... 18 

National registers ........................................................................................ 18 

National Patient Register (NPR) ............................................................ 18 

National Prescribed Drug Register (NPDR) .......................................... 18 

Cause of Death Register (CDR) ............................................................ 18 

Patient modeling ......................................................................................... 19 

Ethical considerations ................................................................................. 19 

RESULTS ........................................................................................................ 21 

Potential for improved ASM retention rate (Paper I) ................................. 21 

Comparison of retention rates and expert algorithm (Paper II) .................. 24 

Selection and continuation of ASM in children (Paper III) ........................ 27 

Personalized ASM selection using machine learning (Paper IV) ............... 31 

DISCUSSION ................................................................................................... 36 

STRENGTHS AND LIMITATIONS ...................................................................... 40 

FUTURE PERSPECTIVES .................................................................................. 46 

CONCLUSIONS ............................................................................................... 48 

ii 

iii 

 
 
 
ACKNOWLEDGEMENTS .................................................................................. 49 

REFERENCES .................................................................................................. 50 

CONTENT 

ABBREVIATIONS ............................................................................................. IV 

INTRODUCTION ................................................................................................ 5 

BACKGROUND ................................................................................................. 7 

Epilepsy and anti-seizure medications .......................................................... 7 

ASM selection and side effects ............................................................... 8 

Measuring efficacy of ASMs ................................................................... 9 

Clinical trials of ASMs .......................................................................... 10 

Observational studies of ASMs ............................................................. 14 

Time-to-event statistics ............................................................................... 15 

Estimating treatment effect from observational data .................................. 15 

Machine learning for personalized treatment selection .............................. 15 

Machine learning in epilepsy ...................................................................... 16 

AIM ................................................................................................................ 17 

METHODS ...................................................................................................... 18 

National registers ........................................................................................ 18 

National Patient Register (NPR) ............................................................ 18 

National Prescribed Drug Register (NPDR) .......................................... 18 

Cause of Death Register (CDR) ............................................................ 18 

Patient modeling ......................................................................................... 19 

Ethical considerations ................................................................................. 19 

RESULTS ........................................................................................................ 21 

Potential for improved ASM retention rate (Paper I) ................................. 21 

Comparison of retention rates and expert algorithm (Paper II) .................. 24 

Selection and continuation of ASM in children (Paper III) ........................ 27 

Personalized ASM selection using machine learning (Paper IV) ............... 31 

DISCUSSION ................................................................................................... 36 

STRENGTHS AND LIMITATIONS ...................................................................... 40 

FUTURE PERSPECTIVES .................................................................................. 46 

CONCLUSIONS ............................................................................................... 48 

ii 

iii 

 
 
 
ABBREVIATIONS 

ASM 

Anti-seizure medication 

CDAUC 

Cumulative/Dynamic Area Under Curve 

CDR 

Cause of Death Register 

CI 

Concordance index 

EEG 

Electroencephalography 

ICD 

International Classification of Diseases 

ILAE 

International League Against Epilepsy 

ML 

Machine learning 

MRI 

Magnetic resonance imaging 

MS 

Multiple sclerosis 

NPDR 

National Prescribed Drug Register 

NPR 

National Patient Register 

RCT 

Randomized Controlled Trial 

SUDEP 

Sudden unexpected death in epilepsy 

Samuel Håkansson 

INTRODUCTION 

Epilepsy is a neurological condition in which the affected has an enduring 

predisposition for seizures [1]. It is most often treated with anti-seizure 

medications (ASMs), with the goal of achieving seizure freedom with as few 

side effects as possible. Finding the right medication for patients with 

epilepsy is difficult. Approximately 50% of patients need to try more than 

one ASM and about 30% never achieve seizure freedom [2]. A common 

reason for ASM failure is side effects. When a new ASM regime is 

initialized, treatment evaluation can take time. One reason is that it can be 

difficult to determine the correct target dose; doses are usually increased after 

seizures, making titration an extended process if seizures are sparse. Another 

reason is that epilepsies can be selectively responsive to different ASMs. If 

patients could try an ASM with a high likelihood of success, they could 

conceptually become seizure-free faster, and experience fewer side effects 

during ASM tryouts. 

Seizures and ASM side effects are important contributors to the burden of 

epilepsy. The annual global cost of epilepsy is estimated at $119 billion [3]. 

In Sweden, the direct healthcare cost per person is estimated to be $2403 per 

year and indirect costs are estimated to be $13 632 per year [3]. Direct costs 

include drugs, hospitalizations, contact with physicians, time spent by 

patients and families in the process of care, and social and educational 

services [4]. Indirect costs are estimates of foregone earnings from lost work 

and lost value due to fewer years of life [4]. Loss of independence is another 

example of a risk for patients with recurrent seizures. In a study with 81 adult 

patients with moderately severe epilepsy from southern USA, the most 

important concern was the ability to drive [5]. A study on outcomes after 

surgery found that the ability to drive was a major factor influencing 

employment post-surgery [6]. 

Since epilepsy is very heterogenous and there are more than 30 ASMs, 

performing randomized controlled trials (RCT) to identify the relative 

treatment effects of one or more ASMs is difficult, and such trials rarely 

contain enough patients for stratification of e.g. etiology. Instead, the use of 

systematically collected data, such as register data, is an interesting 

iv 

5 

 
 
 
 
 
 
 
 
ABBREVIATIONS 

ASM 

Anti-seizure medication 

CDAUC 

Cumulative/Dynamic Area Under Curve 

CDR 

Cause of Death Register 

CI 

Concordance index 

EEG 

Electroencephalography 

ICD 

International Classification of Diseases 

ILAE 

International League Against Epilepsy 

ML 

Machine learning 

MRI 

Magnetic resonance imaging 

MS 

Multiple sclerosis 

NPDR 

National Prescribed Drug Register 

NPR 

National Patient Register 

RCT 

Randomized Controlled Trial 

SUDEP 

Sudden unexpected death in epilepsy 

Samuel Håkansson 

INTRODUCTION 

Epilepsy is a neurological condition in which the affected has an enduring 
predisposition for seizures [1]. It is most often treated with anti-seizure 
medications (ASMs), with the goal of achieving seizure freedom with as few 
side effects as possible. Finding the right medication for patients with 
epilepsy is difficult. Approximately 50% of patients need to try more than 
one ASM and about 30% never achieve seizure freedom [2]. A common 
reason for ASM failure is side effects. When a new ASM regime is 
initialized, treatment evaluation can take time. One reason is that it can be 
difficult to determine the correct target dose; doses are usually increased after 
seizures, making titration an extended process if seizures are sparse. Another 
reason is that epilepsies can be selectively responsive to different ASMs. If 
patients could try an ASM with a high likelihood of success, they could 
conceptually become seizure-free faster, and experience fewer side effects 
during ASM tryouts. 

Seizures and ASM side effects are important contributors to the burden of 
epilepsy. The annual global cost of epilepsy is estimated at $119 billion [3]. 
In Sweden, the direct healthcare cost per person is estimated to be $2403 per 
year and indirect costs are estimated to be $13 632 per year [3]. Direct costs 
include drugs, hospitalizations, contact with physicians, time spent by 
patients and families in the process of care, and social and educational 
services [4]. Indirect costs are estimates of foregone earnings from lost work 
and lost value due to fewer years of life [4]. Loss of independence is another 
example of a risk for patients with recurrent seizures. In a study with 81 adult 
patients with moderately severe epilepsy from southern USA, the most 
important concern was the ability to drive [5]. A study on outcomes after 
surgery found that the ability to drive was a major factor influencing 
employment post-surgery [6]. 

Since epilepsy is very heterogenous and there are more than 30 ASMs, 
performing randomized controlled trials (RCT) to identify the relative 
treatment effects of one or more ASMs is difficult, and such trials rarely 
contain enough patients for stratification of e.g. etiology. Instead, the use of 
systematically collected data, such as register data, is an interesting 

iv 

5 

 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

alternative or supplement. Registers are a potential data source with plenty of 
patients, are relatively easily accessible, follow patients for a long time, and 
are updated systematically.  

The hope for personalized medicine has increased in recent years owing to 
the development of machine learning (ML) methods in combination with an 
abundance of healthcare data. Two of the main advantages of using ML are 
the ability to obtain patient-specific recommendations, rather than stratified 
ones, and the ability to analyze complex and big data. 

The focus of this thesis is to (1) investigate the viability of registers as a data 
source for personalized ASM selection, and (2) develop and evaluate 
machine learning methods trained on register data to suggest an optimal 
ASM for patients. 

BACKGROUND 

EPILEPSY AND ANTI-SEIZURE MEDICATIONS 

Epilepsy is a common brain disorder, with a lifetime prevalence of 0.76% 

worldwide [7]. Epilepsy is usually diagnosed after two unprovoked seizures 

or after a single unprovoked seizure together with a high risk of experiencing 

more seizures [8]. The most common way to treat epilepsy is to use anti-

seizure medications (ASMs). There are approximately 30 different ASMs, 

each with a different mechanism of action and potential side effects. Epilepsy 

can start at any age, but the incidence is U-shaped with more onsets in youths 

and older individuals. Genetic causes are more common in younger ages, 

whereas certain acquired epilepsies after brain damage such as a stroke 

become more common with advancing age.  

There are two types of seizure onset: focal and generalised, and in some 

cases, unknown. Focal-onset refers to a seizure that starts within a single 

brain region and implies a focal disturbance of brain function that can be 

genetic or acquired. Awareness can be either retained or impaired during a 

seizure, even if the person is immobile [9]. Generalised onset refers to 

seizures that start in both hemispheres simultaneously. Focal-onset seizures 

may spread to other parts of the brain. For example, a seizure starting in a 

single part of the brain and then propagating to the other hemisphere, 

manifesting as a tonic-clonic seizure, can be classified as a focal to bilateral 

tonic-clonic seizure [9]. Seizure onset defines the type of epilepsy; focal 

seizures occur in focal epilepsies [10]. The type of epilepsy is important for 

ASM selection; some ASMs are selectively effective in focal epilepsies and 

may even aggravate generalised ones [11, 12].  Focal epilepsy can start at any 

age, whereas onset of generalised epilepsy is rare after age 25-30. 

It is important to find a suitable ASM early on to avoid seizures and their 

consequences such as head injuries, fractures, and drowning [13, 14]. Some 

patients never find an appropriate ASM. Drug-resistant epilepsy is defined as 

the failure of two appropriately chosen and adequately tried ASMs, either as 

monotherapy or in combination [15]. The mortality rate is 4-7 times higher 

for people with drug-resistant epilepsy, and injury rates range from one per 

20 to one per 3 person-years [16]. 

6 

7 

 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

alternative or supplement. Registers are a potential data source with plenty of 

patients, are relatively easily accessible, follow patients for a long time, and 

are updated systematically.  

The hope for personalized medicine has increased in recent years owing to 

the development of machine learning (ML) methods in combination with an 

abundance of healthcare data. Two of the main advantages of using ML are 

the ability to obtain patient-specific recommendations, rather than stratified 

ones, and the ability to analyze complex and big data. 

The focus of this thesis is to (1) investigate the viability of registers as a data 

source for personalized ASM selection, and (2) develop and evaluate 

machine learning methods trained on register data to suggest an optimal 

ASM for patients. 

BACKGROUND 

EPILEPSY AND ANTI-SEIZURE MEDICATIONS 

Epilepsy is a common brain disorder, with a lifetime prevalence of 0.76% 
worldwide [7]. Epilepsy is usually diagnosed after two unprovoked seizures 
or after a single unprovoked seizure together with a high risk of experiencing 
more seizures [8]. The most common way to treat epilepsy is to use anti-
seizure medications (ASMs). There are approximately 30 different ASMs, 
each with a different mechanism of action and potential side effects. Epilepsy 
can start at any age, but the incidence is U-shaped with more onsets in youths 
and older individuals. Genetic causes are more common in younger ages, 
whereas certain acquired epilepsies after brain damage such as a stroke 
become more common with advancing age.  

There are two types of seizure onset: focal and generalised, and in some 
cases, unknown. Focal-onset refers to a seizure that starts within a single 
brain region and implies a focal disturbance of brain function that can be 
genetic or acquired. Awareness can be either retained or impaired during a 
seizure, even if the person is immobile [9]. Generalised onset refers to 
seizures that start in both hemispheres simultaneously. Focal-onset seizures 
may spread to other parts of the brain. For example, a seizure starting in a 
single part of the brain and then propagating to the other hemisphere, 
manifesting as a tonic-clonic seizure, can be classified as a focal to bilateral 
tonic-clonic seizure [9]. Seizure onset defines the type of epilepsy; focal 
seizures occur in focal epilepsies [10]. The type of epilepsy is important for 
ASM selection; some ASMs are selectively effective in focal epilepsies and 
may even aggravate generalised ones [11, 12].  Focal epilepsy can start at any 
age, whereas onset of generalised epilepsy is rare after age 25-30. 

It is important to find a suitable ASM early on to avoid seizures and their 
consequences such as head injuries, fractures, and drowning [13, 14]. Some 
patients never find an appropriate ASM. Drug-resistant epilepsy is defined as 
the failure of two appropriately chosen and adequately tried ASMs, either as 
monotherapy or in combination [15]. The mortality rate is 4-7 times higher 
for people with drug-resistant epilepsy, and injury rates range from one per 
20 to one per 3 person-years [16]. 

6 

7 

 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

ASM SELECTION AND SIDE EFFECTS 
When selecting a suitable ASM, many factors may need to be considered. 
ILAE suggests taking into account epilepsy syndrome, age, gender, genetics, 
and comorbidities, to name a few [17]. It is also important to consider the 
patient’s preferences. 

ASMs may have long-term side effects [18] such as cardiac adverse effects 
[19] and valproic acid and pregnancy [20-22]. While it is important to treat 
seizures, misdiagnosing epilepsy, for example for cardiac arrest, and starting 
epilepsy treatment can be disastrous. Some medications are associated with 
side effects that are related to specific genes. Carbamazepine is the main 
cause of Stevens-Johnsons syndrome (SJS) and toxic epidermal necrolysis 
(TEN) in Southeast Asian countries [23]. SJS-TEN causes high fever, 
malaise, exanthema, and mucosal involvement. 

A modified version of the WHO classification of adverse effects has been 
used to describe side effects of ASMs (Table 1) [24]. Types A and C are 
more likely than the other types to be found during short clinical trials, 
whereas types B, D, and E sometimes require a longer follow-up time to be 
discovered and understood. 

Table 1 Classification of adverse effects of ASMs. Adapted from [24] 

Description of adverse effects 

Type A  Related to the known mechanism of action of the drug; 

common or very common; dose-dependent; acute; predictable; 
reversible 

Type B  Related to individual vulnerability; first few weeks of 

treatment; uncommon; high morbidity and mortality; reversible 

Type C  Related to the cumulative dose of the drug; common; chronic; 

mostly reversible 

Type D  Related to prenatal exposure to the drug; uncommon; delayed; 

dose-dependent; irreversible 

Type E  Adverse drug interactions; common; reversible 

ASMs often require slow titration to avoid severe side effects. The titration 
periods differ for ASMs (Table 2) [25]. The difference in titration time can 

make it challenging to compare ASMs since a longer time to maintenance 

means that patients stay on an ASM for a longer duration without it 

necessarily being a better medication. On the contrary, a longer titration 

might mean that a patient has seizures while on a low dose of the medication 

and thus change treatment even though the medication itself was not 

inadequate, but the dose was insufficient.  

Table 2 Time to maintenance dose for ASMs. Adapted from [25] 

Median time to the maintenance dose (weeks) 

ASM 

Carbamazepine 

Lacosamide 

Lamotrigine 

Levetiracetam 

Phenytoin 

Topiramate 

Valproate 

5.4 

5.1 

8.1 

4.7 

3.3 

6.1 

5.1 

While ASMs are the primary treatment for epilepsy, for patients with drug-

resistant epilepsy (13.7-36.3% of patients with epilepsy [7]), there are 

alternatives such as brain surgery [26], vagus nerve stimulation [27], and 

ketogenic diet [28]. 

MEASURING THE OUTCOME OF ASMS 

Several different outcomes can be evaluated for an ASM in clinical trials: 

percentage of seizure reduction, responder rate (>50% seizure reduction), 

quality of life [29], time to first seizure, adverse events, retention rate, and 

compliance [30]. Retention is the time to treatment failure for any reason and 

is an integrated measure of efficacy and tolerability (Figure 1). The European 

Medicines Agency encourages the use of retention rate as a secondary 

measure of outcome in monotherapy trials [31]. The main disadvantages of 

using retention rate as an outcome measure are that it requires a longer trial 

duration, a larger sample size, and has less historical data to compare to [30]. 

8 

9 

 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

ASM SELECTION AND SIDE EFFECTS 

When selecting a suitable ASM, many factors may need to be considered. 

ILAE suggests taking into account epilepsy syndrome, age, gender, genetics, 

and comorbidities, to name a few [17]. It is also important to consider the 

patient’s preferences. 

ASMs may have long-term side effects [18] such as cardiac adverse effects 

[19] and valproic acid and pregnancy [20-22]. While it is important to treat 

seizures, misdiagnosing epilepsy, for example for cardiac arrest, and starting 

epilepsy treatment can be disastrous. Some medications are associated with 

side effects that are related to specific genes. Carbamazepine is the main 

cause of Stevens-Johnsons syndrome (SJS) and toxic epidermal necrolysis 

(TEN) in Southeast Asian countries [23]. SJS-TEN causes high fever, 

malaise, exanthema, and mucosal involvement. 

A modified version of the WHO classification of adverse effects has been 

used to describe side effects of ASMs (Table 1) [24]. Types A and C are 

more likely than the other types to be found during short clinical trials, 

whereas types B, D, and E sometimes require a longer follow-up time to be 

discovered and understood. 

Table 1 Classification of adverse effects of ASMs. Adapted from [24] 

Description of adverse effects 

Type A  Related to the known mechanism of action of the drug; 

common or very common; dose-dependent; acute; predictable; 

reversible 

Type B  Related to individual vulnerability; first few weeks of 

treatment; uncommon; high morbidity and mortality; reversible 

Type C  Related to the cumulative dose of the drug; common; chronic; 

mostly reversible 

Type D  Related to prenatal exposure to the drug; uncommon; delayed; 

dose-dependent; irreversible 

Type E  Adverse drug interactions; common; reversible 

ASMs often require slow titration to avoid severe side effects. The titration 

periods differ for ASMs (Table 2) [25]. The difference in titration time can 

make it challenging to compare ASMs since a longer time to maintenance 
means that patients stay on an ASM for a longer duration without it 
necessarily being a better medication. On the contrary, a longer titration 
might mean that a patient has seizures while on a low dose of the medication 
and thus change treatment even though the medication itself was not 
inadequate, but the dose was insufficient.  

Table 2 Time to maintenance dose for ASMs. Adapted from [25] 

ASM 
Carbamazepine 
Lacosamide 
Lamotrigine 
Levetiracetam 
Phenytoin 
Topiramate 
Valproate 

Median time to the maintenance dose (weeks) 
5.4 
5.1 
8.1 
4.7 
3.3 
6.1 
5.1 

While ASMs are the primary treatment for epilepsy, for patients with drug-
resistant epilepsy (13.7-36.3% of patients with epilepsy [7]), there are 
alternatives such as brain surgery [26], vagus nerve stimulation [27], and 
ketogenic diet [28]. 

MEASURING THE OUTCOME OF ASMS 
Several different outcomes can be evaluated for an ASM in clinical trials: 
percentage of seizure reduction, responder rate (>50% seizure reduction), 
quality of life [29], time to first seizure, adverse events, retention rate, and 
compliance [30]. Retention is the time to treatment failure for any reason and 
is an integrated measure of efficacy and tolerability (Figure 1). The European 
Medicines Agency encourages the use of retention rate as a secondary 
measure of outcome in monotherapy trials [31]. The main disadvantages of 
using retention rate as an outcome measure are that it requires a longer trial 
duration, a larger sample size, and has less historical data to compare to [30]. 

8 

9 

 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Figure 1 Retention is an aggregated measure of efficacy and tolerability. Adapted from [30]. 
Created with BioRender.com 

CLINICAL TRIALS OF ASMS 
The current literature illustrates the difficulties in determining the relative 
efficacy of ASMs in a clinically meaningful manner. Traditional methods 
include RCTs, uncontrolled trials, and observational studies. The benefits and 
problems of these strategies and the limitations in answerable research 
questions of relevance for personalized medicine are discussed below. 

One suggestion of the hierarchy of evidence for selecting initial ASM for a 
patient is [32]: 

1.  Individual patient data meta-analysis 
2.  Systematic review and meta-analysis of large RCTs 
3.  Large RCTs 
4.  Systematic reviews of small RCTs 
5.  Small RCTs 
6.  The consensus of expert opinion 
7.  Individual expert opinion 
8.  Case series 
9.  Individual case report 

10 

11 

Randomized controlled trials (RCT) are the gold standard for evaluating 

epilepsy treatments. However, these trials are often conducted for regulatory 

reasons with placebo or a single comparator as reference [33]. The eligibility 

criteria in clinical trials can be very restrictive to avoid exposing groups such 

as elderly or pregnant patients to potential side effects [34], making it 

challenging to extrapolate the efficacy of treatments to all patients. 

Furthermore, regulatory study protocols leave little or no flexibility in dosing 

schemes, which may affect the generalizability of the study to clinical 

practice and the interpretation of drug efficacy.  

Trials may also be too short to determine the optimal dose for patients. For 

example, pregabalin was found to be inferior to lamotrigine, possibly because 

the initial maintenance dose of pregabalin was ineffective, and the duration of 

the trial did not allow for the comparison of effectiveness at higher doses 

[35]. Clinical trials with 3-6 months follow-up are of limited applicability to 

general practice because the effectiveness of the drug is difficult to determine 

in such a short time frame [30]. Controlled trials in epilepsy are difficult to 

implement due to high costs and ethical difficulties, whereas uncontrolled 

studies tend to provide misleading estimates of both efficacy and adverse 

effects due to confounders [33]. Non-regulatory trials are sometimes biased 

towards the sponsor’s product by choosing the eligibility criteria, choice of 

formulation, target doses, titration rates, or interpreting the results in a certain 

way [34, 36]. ASMs are often tested as adjunctive treatment in trials with 

patients with uncontrolled seizures [37, 38]. Oftentimes, these are the only 

data on efficacy available to clinicians when a new ASM is released to the 

market. Clinicians must then be cautious about the optimal use of the drug, 

especially if it is used as monotherapy.  

Few trials in epilepsy are regarded as high-quality evidence of treatment 

efficacy. In 2006, 33 eligible trials of adults with focal seizures were 

analyzed. Two of them were rated as class I (the highest rating in terms of 

quality of evidence), one as class II, and 30 as class III (the lowest rating). 

All the trials in adults with generalised tonic-clonic or other generalised 

seizure types achieved class III rating [17, 39]. In a systematic review of 

randomized placebo-controlled adjunctive therapy trials, only 3 of the 63 

trials conducted in adults with focal epilepsy reported the proportion of 

 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Figure 1 Retention is an aggregated measure of efficacy and tolerability. Adapted from [30]. 

Created with BioRender.com 

CLINICAL TRIALS OF ASMS 

The current literature illustrates the difficulties in determining the relative 

efficacy of ASMs in a clinically meaningful manner. Traditional methods 

include RCTs, uncontrolled trials, and observational studies. The benefits and 

problems of these strategies and the limitations in answerable research 

questions of relevance for personalized medicine are discussed below. 

One suggestion of the hierarchy of evidence for selecting initial ASM for a 

patient is [32]: 

1.  Individual patient data meta-analysis 

2.  Systematic review and meta-analysis of large RCTs 

3.  Large RCTs 

5.  Small RCTs 

4.  Systematic reviews of small RCTs 

6.  The consensus of expert opinion 

7.  Individual expert opinion 

8.  Case series 

9.  Individual case report 

Randomized controlled trials (RCT) are the gold standard for evaluating 
epilepsy treatments. However, these trials are often conducted for regulatory 
reasons with placebo or a single comparator as reference [33]. The eligibility 
criteria in clinical trials can be very restrictive to avoid exposing groups such 
as elderly or pregnant patients to potential side effects [34], making it 
challenging to extrapolate the efficacy of treatments to all patients. 
Furthermore, regulatory study protocols leave little or no flexibility in dosing 
schemes, which may affect the generalizability of the study to clinical 
practice and the interpretation of drug efficacy.  

Trials may also be too short to determine the optimal dose for patients. For 
example, pregabalin was found to be inferior to lamotrigine, possibly because 
the initial maintenance dose of pregabalin was ineffective, and the duration of 
the trial did not allow for the comparison of effectiveness at higher doses 
[35]. Clinical trials with 3-6 months follow-up are of limited applicability to 
general practice because the effectiveness of the drug is difficult to determine 
in such a short time frame [30]. Controlled trials in epilepsy are difficult to 
implement due to high costs and ethical difficulties, whereas uncontrolled 
studies tend to provide misleading estimates of both efficacy and adverse 
effects due to confounders [33]. Non-regulatory trials are sometimes biased 
towards the sponsor’s product by choosing the eligibility criteria, choice of 
formulation, target doses, titration rates, or interpreting the results in a certain 
way [34, 36]. ASMs are often tested as adjunctive treatment in trials with 
patients with uncontrolled seizures [37, 38]. Oftentimes, these are the only 
data on efficacy available to clinicians when a new ASM is released to the 
market. Clinicians must then be cautious about the optimal use of the drug, 
especially if it is used as monotherapy.  

Few trials in epilepsy are regarded as high-quality evidence of treatment 
efficacy. In 2006, 33 eligible trials of adults with focal seizures were 
analyzed. Two of them were rated as class I (the highest rating in terms of 
quality of evidence), one as class II, and 30 as class III (the lowest rating). 
All the trials in adults with generalised tonic-clonic or other generalised 
seizure types achieved class III rating [17, 39]. In a systematic review of 
randomized placebo-controlled adjunctive therapy trials, only 3 of the 63 
trials conducted in adults with focal epilepsy reported the proportion of 

10 

11 

 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

patients who completed the trial successfully, that is, those who had a >50% 
reduction in seizure frequency and were able to complete the trial [40]. 

32]. 

and (e) the design, conduct, and analysis of the trials were by industry [17, 

As different drugs have different levels of evidence of efficacy in clinical 
trials, the International League Against Epilepsy (ILAE) has graded the 
medications according to the level of evidence of efficacy as initial 
monotherapy for focal-onset epilepsy (Table 3). Many ASMs lack high-
quality evidence of efficacy and none of the drugs obtained an increase in 
evidence level in the updated version. In summary, the ILAE finds evidence 
for the effectiveness of different ASMs, but this is of little use to clinicians 
contemplating which ASM to use first. 

Table 3 ILAE guidelines for adults with newly diagnosed or untreated focal-onset epilepsy. 
Level A suggests that the ASM is established as an efficacious initial monotherapy, B is 
probably efficacious, C is possibly efficacious, and D is potentially efficacious   

ASM 

Carbamazepine 
Gabapentin 
Lamotrigine 
Oxcarbazepine 
Phenobarbital 
Phenytoin 
Topiramate 
Valproic acid 
Vigabatrin 
Clonazepam 
Levetiracetam 
Primidone 
Zonisamide 

Effectiveness, evidence 
level 2006 [17] 
A 
C 
C 
C 
C 
A 
C 
B 
C 

Effectiveness, evidence 
level 2013 [41] 
A 
C 
C 
C 
C 
A 
C 
B 
C 
D 
A 
D 
A 

The ILAE guidelines concluded the following concerns: (a) trials were not 
designed and powered as noninferiority trials because the main goal of many 
trials is to get a medication approved for market; (b) they were too short to 
produce clinically relevant information; (c) titration schedules were fixed and 
forced, and could be biased favouring the sponsor’s product; (d) the trials had 
a heterogeneous patient group with multiple age groups and seizure types; 

Some RCTs have tried to use multiple arms. Two of the largest phase 4 

randomized controlled trials on ASM efficacy are the Standard and New 

Antiepileptic Drugs (SANAD) trials on focal epilepsy [42, 43]. The two trials 

included 1721 and 990 patients, respectively. Patients aged 5 years or older 

with at least two unprovoked seizures were eligible for recruitment and they 

were followed-up for 12 months. Patients were excluded if they had known 

progressive neurological diseases, had acute symptomatic seizures, or were 

currently taking an ASM. 

A few trials conducted in Europe have been designed to provide information 

comparing a new drug and previously established treatment options in terms 

of efficacy and tolerability [33]. Although they have been criticized with 

concerns of assay sensitivity [38, 44, 45], i.e. the ability to distinguish an 

effective treatment from a less effective one. The U.S. Food and Drug 

Administration (FDA) requires evidence of the efficacy of a drug to 

demonstrate its superiority over a comparator. This comparator cannot be a 

placebo administered to patients with active epilepsy due to ethical concerns, 

but it is also improbable for a new drug to show significantly superior 

efficacy compared to the best standard ASM [44]. This led to a trial design of 

conversion to monotherapy with a sub-optimally dosed comparator [38, 46]. 

This design is also problematic because it allocates patients with uncontrolled 

seizures to a deliberately suboptimal treatment. Patients included in the study 

are pharmacoresistant, which is different from the intended monotherapy 

population. Efficacy is established by demonstrating a reduced risk of 

seizures, not clinical improvement, and the full dose is typically higher than 

the optimal dosing range in the clinical setting [36, 38, 44, 47, 48]. 

Some trials use placebo as a baseline for epilepsy treatment. One way to 

make trials easier to perform would be to remove the placebo group, which 

would be a valid strategy if the magnitude of the placebo response would be 

consistent over time, across trials, and in any geographic setting [33]. 

However, the proportion of responders to placebo ranged from <5% to almost 

40% in a systematic review of all RCTs conducted in adults with focal 

epilepsy between 1960 and 2009 [40]. Most RCTs of ASMs are conducted 

12 

13 

 
 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

patients who completed the trial successfully, that is, those who had a >50% 

reduction in seizure frequency and were able to complete the trial [40]. 

and (e) the design, conduct, and analysis of the trials were by industry [17, 
32]. 

As different drugs have different levels of evidence of efficacy in clinical 

trials, the International League Against Epilepsy (ILAE) has graded the 

medications according to the level of evidence of efficacy as initial 

monotherapy for focal-onset epilepsy (Table 3). Many ASMs lack high-

quality evidence of efficacy and none of the drugs obtained an increase in 

evidence level in the updated version. In summary, the ILAE finds evidence 

for the effectiveness of different ASMs, but this is of little use to clinicians 

contemplating which ASM to use first. 

Table 3 ILAE guidelines for adults with newly diagnosed or untreated focal-onset epilepsy. 

Level A suggests that the ASM is established as an efficacious initial monotherapy, B is 

probably efficacious, C is possibly efficacious, and D is potentially efficacious   

ASM 

Effectiveness, evidence 

Effectiveness, evidence 

level 2006 [17] 

level 2013 [41] 

A 

C 

C 

C 

C 

A 

C 

B 

C 

Carbamazepine 

Gabapentin 

Lamotrigine 

Oxcarbazepine 

Phenobarbital 

Phenytoin 

Topiramate 

Valproic acid 

Vigabatrin 

Clonazepam 

Levetiracetam 

Primidone 

Zonisamide 

A 

C 

C 

C 

C 

A 

C 

B 

C 

D 

A 

D 

A 

The ILAE guidelines concluded the following concerns: (a) trials were not 

designed and powered as noninferiority trials because the main goal of many 

trials is to get a medication approved for market; (b) they were too short to 

produce clinically relevant information; (c) titration schedules were fixed and 

forced, and could be biased favouring the sponsor’s product; (d) the trials had 

a heterogeneous patient group with multiple age groups and seizure types; 

Some RCTs have tried to use multiple arms. Two of the largest phase 4 
randomized controlled trials on ASM efficacy are the Standard and New 
Antiepileptic Drugs (SANAD) trials on focal epilepsy [42, 43]. The two trials 
included 1721 and 990 patients, respectively. Patients aged 5 years or older 
with at least two unprovoked seizures were eligible for recruitment and they 
were followed-up for 12 months. Patients were excluded if they had known 
progressive neurological diseases, had acute symptomatic seizures, or were 
currently taking an ASM. 

A few trials conducted in Europe have been designed to provide information 
comparing a new drug and previously established treatment options in terms 
of efficacy and tolerability [33]. Although they have been criticized with 
concerns of assay sensitivity [38, 44, 45], i.e. the ability to distinguish an 
effective treatment from a less effective one. The U.S. Food and Drug 
Administration (FDA) requires evidence of the efficacy of a drug to 
demonstrate its superiority over a comparator. This comparator cannot be a 
placebo administered to patients with active epilepsy due to ethical concerns, 
but it is also improbable for a new drug to show significantly superior 
efficacy compared to the best standard ASM [44]. This led to a trial design of 
conversion to monotherapy with a sub-optimally dosed comparator [38, 46]. 
This design is also problematic because it allocates patients with uncontrolled 
seizures to a deliberately suboptimal treatment. Patients included in the study 
are pharmacoresistant, which is different from the intended monotherapy 
population. Efficacy is established by demonstrating a reduced risk of 
seizures, not clinical improvement, and the full dose is typically higher than 
the optimal dosing range in the clinical setting [36, 38, 44, 47, 48]. 

Some trials use placebo as a baseline for epilepsy treatment. One way to 
make trials easier to perform would be to remove the placebo group, which 
would be a valid strategy if the magnitude of the placebo response would be 
consistent over time, across trials, and in any geographic setting [33]. 
However, the proportion of responders to placebo ranged from <5% to almost 
40% in a systematic review of all RCTs conducted in adults with focal 
epilepsy between 1960 and 2009 [40]. Most RCTs of ASMs are conducted 

12 

13 

 
 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

for regulatory purposes, where a product is deemed efficacious and safe if it 
is “better than nothing” [44]. In contrast, for clinicians to make informed 
decisions about drug selection, they would need to know how the drugs 
compare to previously established treatment options, preferably on the same 
population, titration schedule, etc. To make matters worse, placebo has seen a 
rising response in the last few years, making it more difficult to compare 
studies [40]. Placebo has also been linked to a 6-fold increase in the risk of 
sudden unexpected death in epilepsy (SUDEP) [49], showing the potential 
danger of trials with placebo. Because it is problematic to compare trials, one 
could seek information from head-to-head trials. However, these may not be 
available for many years after release to the market, or in some cases not at 
all [34]. 

While the SANAD results suggest that drugs performing better than placebo 
for generalised and focal seizures should be considered broad-spectrum 
ASMs, another suggestion of the definition of broad-spectrum is to depend 
on the demonstration of equivalence or superiority of efficacy against the 
existing first-choice agents [32]. The SANAD studies were not sufficiently 
large to alloy much stratification regarding age, sex, and comorbidities. 

OBSERVATIONAL STUDIES OF ASMS 
Prescription data is important for understanding adverse effects and other 
drug-related problems. Use of ASMs in other disorders, changes in 
prescription patterns, and combination of drugs are examples of usages of 
prescription data from registers or electronic health records [50]. Registers 
have been used to study ASM use and its effect on pregnancy in Finland [51], 
the effect of ASMs on the risk of cancer in Denmark [52], general trends of 
ASM use in Germany [53], changes in ASM use in children and adolescents 
in Norway [54], epilepsy and ASMs, and the relationship to transport 
accidents in Sweden [55], and combined data from Nordic countries to study 
the risk of autism and intellectual disability from ASMs [56].  

Although RCTs are considered the best evidence of treatment efficacy, 
observational studies may be superior to clinical trials for some purposes. 
Observational studies provide better evidence than RCTs for serious 
idiosyncratic reactions, chronic adverse events, or teratogenicity [32]. 

TIME-TO-EVENT STATISTICS 

When the outcome of a data point has a fixed lower limit but no upper limit, 

the outcome is right-censored. For example, this often arises in studies where 

the survival of patients is of interest, hence, it is commonly referred to as 

survival analysis. Patients who lived longer than the study period will be 

censored; it is known that they lived at least until the end of the study. The 

data of the studies in this thesis were right-censored either because the patient 

used the ASM until the end of the study or until they were deceased. Left-

censoring was not dealt with in the studies of this thesis but could be 

incorporated if patients with unknown ASM start dates were included. The 

Kaplan-Meier estimator is a popular estimation method for right-censored 

data and it was used in all studies in this thesis.  

ESTIMATING TREATMENT EFFECT FROM 

OBSERVATIONAL DATA 

Regulatory-grade clinical trials for drugs are expensive, with a median cost of 

about $19 million in 2015-2016 [57]. They could also be difficult to perform, 

especially for ASMs where the patient would potentially have to give up 

another option, which at the time is considered a better choice. Real-world 

data, such as registers and electronic health records, are alternative data 

sources for drugs released on the market. However, estimating the causal 

effects of ASMs using register data is not straightforward, mainly because the 

assignment of drugs by a doctor is non-random [58]. The probability of an 

individual being assigned a treatment is called the propensity score [59]. The 

propensity score can be used to adjust the regression models to estimate the 

causal effect of a treatment on a subject.  

MACHINE LEARNING FOR PERSONALIZED 

TREATMENT SELECTION 

Using biomarkers to train machine learning models for personalized medicine 

has the potential advantages of better medication effectiveness, risk reduction 

of adverse events, lower healthcare costs, early diagnosis and prevention of 

disease, improved disease management, and smarter clinical trial designs 

14 

15 

 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

for regulatory purposes, where a product is deemed efficacious and safe if it 

is “better than nothing” [44]. In contrast, for clinicians to make informed 

decisions about drug selection, they would need to know how the drugs 

compare to previously established treatment options, preferably on the same 

population, titration schedule, etc. To make matters worse, placebo has seen a 

rising response in the last few years, making it more difficult to compare 

studies [40]. Placebo has also been linked to a 6-fold increase in the risk of 

sudden unexpected death in epilepsy (SUDEP) [49], showing the potential 

danger of trials with placebo. Because it is problematic to compare trials, one 

could seek information from head-to-head trials. However, these may not be 

available for many years after release to the market, or in some cases not at 

all [34]. 

While the SANAD results suggest that drugs performing better than placebo 

for generalised and focal seizures should be considered broad-spectrum 

ASMs, another suggestion of the definition of broad-spectrum is to depend 

on the demonstration of equivalence or superiority of efficacy against the 

existing first-choice agents [32]. The SANAD studies were not sufficiently 

large to alloy much stratification regarding age, sex, and comorbidities. 

OBSERVATIONAL STUDIES OF ASMS 

Prescription data is important for understanding adverse effects and other 

drug-related problems. Use of ASMs in other disorders, changes in 

prescription patterns, and combination of drugs are examples of usages of 

prescription data from registers or electronic health records [50]. Registers 

have been used to study ASM use and its effect on pregnancy in Finland [51], 

the effect of ASMs on the risk of cancer in Denmark [52], general trends of 

ASM use in Germany [53], changes in ASM use in children and adolescents 

in Norway [54], epilepsy and ASMs, and the relationship to transport 

accidents in Sweden [55], and combined data from Nordic countries to study 

the risk of autism and intellectual disability from ASMs [56].  

Although RCTs are considered the best evidence of treatment efficacy, 

observational studies may be superior to clinical trials for some purposes. 

Observational studies provide better evidence than RCTs for serious 

idiosyncratic reactions, chronic adverse events, or teratogenicity [32]. 

TIME-TO-EVENT STATISTICS 

When the outcome of a data point has a fixed lower limit but no upper limit, 
the outcome is right-censored. For example, this often arises in studies where 
the survival of patients is of interest, hence, it is commonly referred to as 
survival analysis. Patients who lived longer than the study period will be 
censored; it is known that they lived at least until the end of the study. The 
data of the studies in this thesis were right-censored either because the patient 
used the ASM until the end of the study or until they were deceased. Left-
censoring was not dealt with in the studies of this thesis but could be 
incorporated if patients with unknown ASM start dates were included. The 
Kaplan-Meier estimator is a popular estimation method for right-censored 
data and it was used in all studies in this thesis.  

ESTIMATING TREATMENT EFFECT FROM 

OBSERVATIONAL DATA 

Regulatory-grade clinical trials for drugs are expensive, with a median cost of 
about $19 million in 2015-2016 [57]. They could also be difficult to perform, 
especially for ASMs where the patient would potentially have to give up 
another option, which at the time is considered a better choice. Real-world 
data, such as registers and electronic health records, are alternative data 
sources for drugs released on the market. However, estimating the causal 
effects of ASMs using register data is not straightforward, mainly because the 
assignment of drugs by a doctor is non-random [58]. The probability of an 
individual being assigned a treatment is called the propensity score [59]. The 
propensity score can be used to adjust the regression models to estimate the 
causal effect of a treatment on a subject.  

MACHINE LEARNING FOR PERSONALIZED 

TREATMENT SELECTION 

Using biomarkers to train machine learning models for personalized medicine 
has the potential advantages of better medication effectiveness, risk reduction 
of adverse events, lower healthcare costs, early diagnosis and prevention of 
disease, improved disease management, and smarter clinical trial designs 

14 

15 

 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

[60]. Many different data sources are considered biomarkers, for example, 
electronic health records, biological high-throughput data, bio-images such as 
MRT and CT scans, and data from wearable sensors and mobile health 
applications [60]. 

In vanilla supervised machine learning, the labels of the input data are 
known. The performance of the model was estimated by splitting the dataset 
into a training set and a test set (possibly also into a validation set). However, 
when estimating the treatment effect, it is rare to know the outcomes of all 
treatments for all patients. This makes it more difficult to evaluate the trained 
models because the evaluation of the test set will show how well the model 
will perform on the treatments assigned to the patients. Instead, a policy 
evaluation method can be used [61]. The goal of policy evaluation is to 
compare different policies, such as the treatment choices of a doctor or a 
machine learning model. This is essentially done by weighing the data points 
in the test set based on how commonly the treatment is assigned to that type 
of patient. 

When estimating the effect of an action on an outcome, an assumption about 
the relationship between the features of the dataset is sometimes required. A 
simple example is the estimation of the effect of altitude on temperature. We 
know that the altitude of a place might affect the temperature, and we know 
that the temperature does not affect the altitude. However, if we have a 
dataset with place, altitude, and temperature, it is impossible from the data 
alone to determine the causal relationship between altitude and temperature 
without additional assumptions. Nonetheless, with assumptions or additional 
input data, it is possible to deduce the relation between the variables [62]. 

MACHINE LEARNING IN EPILEPSY 
Epilepsy is a disease with difficult and diverse challenges, some of which 
have been attempted to be untangled with ML. ML has been used in epilepsy 
for image analysis for the classification of epilepsies, detecting lesions, and 
predicting seizure outcomes [63], seizure detection in EEG [64], seizure 
forecasting [65], and identifying regions of interest for epilepsy surgery [66]. 

AIM 

The overall aim of this thesis is to deepen the knowledge about the use of 

ASMs, how the ASM retention rate is affected by patient characteristics and 

to investigate the possibility to use this data to train machine learning models 

to inform the decision of selecting a personalized ASM.  

Paper 

Aim 

Rationale 

I Potential for 

To estimate the 

Data on ASM efficacy 

improved retention rate 

retention and retention 

is sparse. Registers are 

by personalized ASM 

rate gap of ASMs 

potential sources of 

selection 

using registers.  

data. 

II Comparison of ASM 

To describe the 

retention rates and 

similarity in ASM 

expert ASM algorithm 

ranking of ASM 

Expert knowledge 

tools for selecting 

ASMs have been 

retention rates and an 

shown to be useful. 

ASM expert 

knowledge tool. 

How does it compare 

to real-world data? 

III Selection and 

To describe the use 

Evaluating ASM 

continuation of ASM 

and retention of ASMs 

efficacy for children is 

in children with 

for children in Sweden. 

challenging. 

IV Personalized ASM 

To develop and test 

Clinicians could 

epilepsy 

selection using 

machine learning 

novel machine learning 

potentially improve 

models for selecting 

patient outcome with a 

personalized ASMs. 

tool for personalized 

ASM treatment. 

16 

17 

 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

[60]. Many different data sources are considered biomarkers, for example, 

electronic health records, biological high-throughput data, bio-images such as 

MRT and CT scans, and data from wearable sensors and mobile health 

applications [60]. 

In vanilla supervised machine learning, the labels of the input data are 

known. The performance of the model was estimated by splitting the dataset 

into a training set and a test set (possibly also into a validation set). However, 

when estimating the treatment effect, it is rare to know the outcomes of all 

treatments for all patients. This makes it more difficult to evaluate the trained 

models because the evaluation of the test set will show how well the model 

will perform on the treatments assigned to the patients. Instead, a policy 

evaluation method can be used [61]. The goal of policy evaluation is to 

compare different policies, such as the treatment choices of a doctor or a 

machine learning model. This is essentially done by weighing the data points 

in the test set based on how commonly the treatment is assigned to that type 

of patient. 

When estimating the effect of an action on an outcome, an assumption about 

the relationship between the features of the dataset is sometimes required. A 

simple example is the estimation of the effect of altitude on temperature. We 

know that the altitude of a place might affect the temperature, and we know 

that the temperature does not affect the altitude. However, if we have a 

dataset with place, altitude, and temperature, it is impossible from the data 

alone to determine the causal relationship between altitude and temperature 

without additional assumptions. Nonetheless, with assumptions or additional 

input data, it is possible to deduce the relation between the variables [62]. 

MACHINE LEARNING IN EPILEPSY 

Epilepsy is a disease with difficult and diverse challenges, some of which 

have been attempted to be untangled with ML. ML has been used in epilepsy 

for image analysis for the classification of epilepsies, detecting lesions, and 

predicting seizure outcomes [63], seizure detection in EEG [64], seizure 

forecasting [65], and identifying regions of interest for epilepsy surgery [66]. 

AIM 
The overall aim of this thesis is to deepen the knowledge about the use of 
ASMs, how the ASM retention rate is affected by patient characteristics and 
to investigate the possibility to use this data to train machine learning models 
to inform the decision of selecting a personalized ASM.  

Paper 

Aim 

Rationale 

I Potential for 
improved retention rate 
by personalized ASM 
selection 

To estimate the 
retention and retention 
rate gap of ASMs 
using registers.  

Data on ASM efficacy 
is sparse. Registers are 
potential sources of 
data. 

II Comparison of ASM 
retention rates and 
expert ASM algorithm 

III Selection and 
continuation of ASM 
in children with 
epilepsy 

IV Personalized ASM 
selection using 
machine learning 

To describe the 
similarity in ASM 
ranking of ASM 
retention rates and an 
ASM expert 
knowledge tool. 

Expert knowledge 
tools for selecting 
ASMs have been 
shown to be useful. 
How does it compare 
to real-world data? 

To describe the use 
and retention of ASMs 
for children in Sweden. 

Evaluating ASM 
efficacy for children is 
challenging. 

To develop and test 
novel machine learning 
models for selecting 
personalized ASMs. 

Clinicians could 
potentially improve 
patient outcome with a 
tool for personalized 
ASM treatment. 

16 

17 

 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

METHODS 

NATIONAL REGISTERS 

The Swedish National Board of Health and Welfare maintains registers for 
in- and outpatient hospital visits, prescribed medications, and death dates. It 
is mandatory for caregivers to report cases to the registers. For this thesis, the 
National Patient Register (NPR), the National Prescribed Drug Register 
(NPDR), and the Cause of Death Register (CDR) were used in all studies 
while the Swedish Stroke register, the Swedish dementia register, and the 
Swedish MS register were used only in Paper I. 

NATIONAL PATIENT REGISTER (NPR) 
The NPR contains diagnose codes using the International Classification of 
Diseases (ICD) and dates for inpatient care since 1987 and specialized 
outpatient care since 2001 in Sweden [67]. An epilepsy diagnosis with the 
ICD code G40 has a positive predictive value of approximately 90% when 
compared to patient charts [68]. For comorbidities, the positive predictive 
values are stroke, 94% [69]; MS, 93% [70]; trauma (open tibial fracture), 
87% [71]; and dementia: 81.3% [72]. Brain tumours had a sensitivity of 78% 
compared to the Swedish Cancer Register [73]. There are no validated studies 
of traumatic brain injury (TBI) but a study on brain concussion found the 
PPV to be 100%, though with only 18 cases [67]. 

NATIONAL PRESCRIBED DRUG REGISTER (NPDR) 
The NPDR contains all prescriptions and dispensations by pharmacies in 
Sweden since the 1st of July 2005 [74]. Drugs are registered by their 
Anatomical Therapeutic Chemical code (ATC) with ASMs starting the ATC 
code with N03. The register has been shown to have negligible loss and 
measurement error [75]. 

CAUSE OF DEATH REGISTER (CDR) 
The CDR contains dates and ICD codes of the underlying causes of death 
since 1961 for all deceased Swedish residents. 

PATIENT MODELING 

All prescriptions of ASMs for a patient were collected with ATC codes. The 

start date for an ASM for a patient started at the initial dispensation date. The 

last date for an ASM was 3 months after the last dispensation. The last date 

for an ASM was set when there had been at least 12 months without a new 

dispensation (Figure 2). It is assumed that patients quit an ASM only because 

it was inadequate. 

Figure 2 Modeling of patient data. Patients retrieve prescriptions, when a new prescription is 

dispensed, 3 months of ASM use is added. If 12 months pass without a new dispensation, the 

medication was stopped 3 months after the last retrieval. Created with BioRender.com 

For Paper I, polytherapy was allowed, while in Paper II, III, and IV only 

monotherapy was allowed. This means that in Paper II, III and IV there is an 

additional stopping rule for the duration of the first ASM if another 

medication is initiated. A difference between these two approaches is if the 

optimization is for finding the best monotherapy, or the best monotherapy 

including the potential to add more drugs. These two goals will yield 

different choices of personalized ASM if, e.g., drug A is in general used for a 

long time as monotherapy while drug B is often started with and then used 

with add-on therapy. 

The duration of ASM use is censored if a patient uses the medication at the 

end of study, or if the patient dies while on the medication. If a patient starts 

a second medication, the duration of the first medication is not censored. 

ETHICAL CONSIDERATIONS 

All studies were approved by the Ethics Review Authority. Paper and 

approval numbers; Paper I: 2020–01829, Paper II and IV: 2020-04902, Paper 

18 

19 

 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

METHODS 

NATIONAL REGISTERS 

The Swedish National Board of Health and Welfare maintains registers for 

in- and outpatient hospital visits, prescribed medications, and death dates. It 

is mandatory for caregivers to report cases to the registers. For this thesis, the 

National Patient Register (NPR), the National Prescribed Drug Register 

(NPDR), and the Cause of Death Register (CDR) were used in all studies 

while the Swedish Stroke register, the Swedish dementia register, and the 

Swedish MS register were used only in Paper I. 

NATIONAL PATIENT REGISTER (NPR) 

The NPR contains diagnose codes using the International Classification of 

Diseases (ICD) and dates for inpatient care since 1987 and specialized 

outpatient care since 2001 in Sweden [67]. An epilepsy diagnosis with the 

ICD code G40 has a positive predictive value of approximately 90% when 

compared to patient charts [68]. For comorbidities, the positive predictive 

values are stroke, 94% [69]; MS, 93% [70]; trauma (open tibial fracture), 

87% [71]; and dementia: 81.3% [72]. Brain tumours had a sensitivity of 78% 

compared to the Swedish Cancer Register [73]. There are no validated studies 

of traumatic brain injury (TBI) but a study on brain concussion found the 

PPV to be 100%, though with only 18 cases [67]. 

NATIONAL PRESCRIBED DRUG REGISTER (NPDR) 

The NPDR contains all prescriptions and dispensations by pharmacies in 

Sweden since the 1st of July 2005 [74]. Drugs are registered by their 

Anatomical Therapeutic Chemical code (ATC) with ASMs starting the ATC 

code with N03. The register has been shown to have negligible loss and 

measurement error [75]. 

CAUSE OF DEATH REGISTER (CDR) 

The CDR contains dates and ICD codes of the underlying causes of death 

since 1961 for all deceased Swedish residents. 

PATIENT MODELING 

All prescriptions of ASMs for a patient were collected with ATC codes. The 
start date for an ASM for a patient started at the initial dispensation date. The 
last date for an ASM was 3 months after the last dispensation. The last date 
for an ASM was set when there had been at least 12 months without a new 
dispensation (Figure 2). It is assumed that patients quit an ASM only because 
it was inadequate. 

Figure 2 Modeling of patient data. Patients retrieve prescriptions, when a new prescription is 
dispensed, 3 months of ASM use is added. If 12 months pass without a new dispensation, the 
medication was stopped 3 months after the last retrieval. Created with BioRender.com 

For Paper I, polytherapy was allowed, while in Paper II, III, and IV only 
monotherapy was allowed. This means that in Paper II, III and IV there is an 
additional stopping rule for the duration of the first ASM if another 
medication is initiated. A difference between these two approaches is if the 
optimization is for finding the best monotherapy, or the best monotherapy 
including the potential to add more drugs. These two goals will yield 
different choices of personalized ASM if, e.g., drug A is in general used for a 
long time as monotherapy while drug B is often started with and then used 
with add-on therapy. 

The duration of ASM use is censored if a patient uses the medication at the 
end of study, or if the patient dies while on the medication. If a patient starts 
a second medication, the duration of the first medication is not censored. 

ETHICAL CONSIDERATIONS 

All studies were approved by the Ethics Review Authority. Paper and 
approval numbers; Paper I: 2020–01829, Paper II and IV: 2020-04902, Paper 

18 

19 

 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

III: 2020-04902/2022-00312. Register-based research does not impose any 
physical risks for patients, but precautions must be made such that data is 
securely stored. The data was anonymized before being given to the authors 
and the data was handled with confidentiality. 

POTENTIAL FOR IMPROVED ASM RETENTION 

RESULTS 

RATE (PAPER I) 

KEY POINTS  

Question Based on register data, is there room for improvement in the 

retention rate of an initial ASM? 

Findings The potential for improvement of 5-year retention of the first 

ASM was between 14-21% depending on the comorbidity. 

Implications Personalized ASM selection could improve the retention rate 

of the first ASM. 

A total of 6380 patients with acquired epilepsy after one of the comorbidities 

stroke (number of patients: 5024, 78.7%), dementia (699, 11.0%), trauma 

(265, 4.2%), brain infection (243, 3.8%), or MS (149. 2.3%) were collected 

using data from the NPR, NPDR, CDR, and the national stroke, dementia, 

and MS registers [76]. The usability of registers as a data source for 

calculating retention rates was explored by stratifying the cohort by 

demographics, comorbidities, and ASM history, as well as quantifying the 

potential improvement in retention rate for the initial ASM.  

Kaplan-Meier analysis of the 5-year retention rate showed a difference of 

20% for MS, 14% for dementia, 21% for trauma, and 14% for stroke between 

the best ASM per comorbidity, age and sex strata, and the rest of the ASMs 

(Figure 3). The optimal age and sex stratification for each comorbidity were 

calculated by finding the stratification that had the largest increase in 

retention rate while still having at least 10 patients per retention rate 

estimation.  

20 

21 

 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

III: 2020-04902/2022-00312. Register-based research does not impose any 

physical risks for patients, but precautions must be made such that data is 

securely stored. The data was anonymized before being given to the authors 

and the data was handled with confidentiality. 

RESULTS 

POTENTIAL FOR IMPROVED ASM RETENTION 

RATE (PAPER I) 

KEY POINTS  

Question Based on register data, is there room for improvement in the 
retention rate of an initial ASM? 

Findings The potential for improvement of 5-year retention of the first 
ASM was between 14-21% depending on the comorbidity. 

Implications Personalized ASM selection could improve the retention rate 
of the first ASM. 

A total of 6380 patients with acquired epilepsy after one of the comorbidities 
stroke (number of patients: 5024, 78.7%), dementia (699, 11.0%), trauma 
(265, 4.2%), brain infection (243, 3.8%), or MS (149. 2.3%) were collected 
using data from the NPR, NPDR, CDR, and the national stroke, dementia, 
and MS registers [76]. The usability of registers as a data source for 
calculating retention rates was explored by stratifying the cohort by 
demographics, comorbidities, and ASM history, as well as quantifying the 
potential improvement in retention rate for the initial ASM.  

Kaplan-Meier analysis of the 5-year retention rate showed a difference of 
20% for MS, 14% for dementia, 21% for trauma, and 14% for stroke between 
the best ASM per comorbidity, age and sex strata, and the rest of the ASMs 
(Figure 3). The optimal age and sex stratification for each comorbidity were 
calculated by finding the stratification that had the largest increase in 
retention rate while still having at least 10 patients per retention rate 
estimation.  

20 

21 

 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Figure 3 Potential improvement in retention rate (in percentage points) if each stratum had 
been assigned the ASM with the highest retention 

time was 1 year because it is the validity time for a prescription and the 

retention rates were more stable from that point. 

It was also found that the failed first ASM could provide useful information 

when deciding the subsequent treatment. For patients with poststroke 

epilepsy, lamotrigine had a higher 1-year retention rate, 84% (95% CI = 80–

87) than levetiracetam 78% (95% CI = 75–82), p = .03. However, for the 

patients who used valproic acid as their initial ASM, levetiracetam had a 

higher retention rate, 93% (95% CI = 86–97) than lamotrigine, 73% (95% CI 

= 61–82), p = .002. 

To validate the method, the retention rates of carbamazepine, lamotrigine, 
and topiramate were compared to a randomized trial (SANAD).  

Figure 4 Sensitivity analysis of the maximum allowed time between dispensations 

In a sensitivity analysis, we investigated how the retention rate is affected by 
changing the max time between two dispensations (Figure 4). The chosen 

22 

23 

 
 
 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Figure 3 Potential improvement in retention rate (in percentage points) if each stratum had 

been assigned the ASM with the highest retention 

time was 1 year because it is the validity time for a prescription and the 
retention rates were more stable from that point. 

It was also found that the failed first ASM could provide useful information 
when deciding the subsequent treatment. For patients with poststroke 
epilepsy, lamotrigine had a higher 1-year retention rate, 84% (95% CI = 80–
87) than levetiracetam 78% (95% CI = 75–82), p = .03. However, for the 
patients who used valproic acid as their initial ASM, levetiracetam had a 
higher retention rate, 93% (95% CI = 86–97) than lamotrigine, 73% (95% CI 
= 61–82), p = .002. 

To validate the method, the retention rates of carbamazepine, lamotrigine, 

and topiramate were compared to a randomized trial (SANAD).  

Figure 4 Sensitivity analysis of the maximum allowed time between dispensations 

In a sensitivity analysis, we investigated how the retention rate is affected by 

changing the max time between two dispensations (Figure 4). The chosen 

22 

23 

 
 
 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Table 4 Retention rates for all patients 30 years and older 

1-year retention rate, 

Number of 

% (95% CI) 

patients 

ASM 

Lamotrigine 

Levetiracetam 

Phenobarbital 

Valproic acid 

Lacosamide 

Carbamazepine 

Oxcarbazepine 

Phenytoin 

Gabapentin 

Pregabalin 

Clobazam 

Topiramate 

71 (69-72) 

68 (68-69) 

66 (49-75) 

62 (61-64) 

61 (51-68) 

58 (58-59) 

57 (52-61) 

53 (49-57) 

45 (41-48) 

40 (36-45) 

39 (30-46) 

38 (28-46) 

5641 

12974 

58 

4272 

134 

11844 

478 

619 

943 

528 

152 

115 

COMPARISON OF RETENTION RATES AND 
EXPERT ALGORITHM (PAPER II) 

KEY POINTS 

Question How do the retention rate statistics from national registers 
compare to an expert-based algorithm? 

Findings The ASM with the highest retention rate was recommended by 
the expert-based algorithm in all eight test cases if at least 50 patients were 
used to estimate the retention rate. 

Implications Clinical decision support systems could work and be 
implemented with both real-world retention rates and expert opinions. 

To further evaluate the applicability of registers as data sources for ASM 
efficacy we compared the ranking of ASMs based on their retention rates to 
the ranking according to an expert tool named EpiPick [77].  

The NPR, NPDR, and CDR were cross-referenced and patients over 30 years 
of age at epilepsy onset and a common ASM (confidence interval <50%) 
were included, resulting in a population of 37643 patients [78]. 

The retention rates for all individuals were calculated using the Kaplan-Meier 
statistic. Lamotrigine and levetiracetam had the highest retention rates, and 
levetiracetam and carbamazepine were the most common treatments (Table 
4). 

To verify that the retention rates and rankings were not confounded by 
different epilepsy diagnoses, a sensitivity analysis was performed where only 
patients with focal epilepsy were included. For the most common ASMs; 
levetiracetam, carbamazepine, lamotrigine, and valproate, the retention rates 
were almost exactly the same even though approximately 40% of patients had 
been removed from the cohort. 

24 

25 

 
 
 
 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Table 4 Retention rates for all patients 30 years and older 

ASM 

Lamotrigine 
Levetiracetam 
Phenobarbital 
Valproic acid 
Lacosamide 
Carbamazepine 
Oxcarbazepine 
Phenytoin 
Gabapentin 
Pregabalin 
Clobazam 
Topiramate 

1-year retention rate, 
% (95% CI) 
71 (69-72) 
68 (68-69) 
66 (49-75) 
62 (61-64) 
61 (51-68) 
58 (58-59) 
57 (52-61) 
53 (49-57) 
45 (41-48) 
40 (36-45) 
39 (30-46) 
38 (28-46) 

Number of 
patients 
5641 
12974 
58 
4272 
134 
11844 
478 
619 
943 
528 
152 
115 

COMPARISON OF RETENTION RATES AND 

EXPERT ALGORITHM (PAPER II) 

KEY POINTS 

Question How do the retention rate statistics from national registers 

compare to an expert-based algorithm? 

Findings The ASM with the highest retention rate was recommended by 

the expert-based algorithm in all eight test cases if at least 50 patients were 

used to estimate the retention rate. 

Implications Clinical decision support systems could work and be 

implemented with both real-world retention rates and expert opinions. 

To further evaluate the applicability of registers as data sources for ASM 

efficacy we compared the ranking of ASMs based on their retention rates to 

the ranking according to an expert tool named EpiPick [77].  

The NPR, NPDR, and CDR were cross-referenced and patients over 30 years 

of age at epilepsy onset and a common ASM (confidence interval <50%) 

were included, resulting in a population of 37643 patients [78]. 

The retention rates for all individuals were calculated using the Kaplan-Meier 

statistic. Lamotrigine and levetiracetam had the highest retention rates, and 

levetiracetam and carbamazepine were the most common treatments (Table 

4). 

To verify that the retention rates and rankings were not confounded by 

different epilepsy diagnoses, a sensitivity analysis was performed where only 

patients with focal epilepsy were included. For the most common ASMs; 

levetiracetam, carbamazepine, lamotrigine, and valproate, the retention rates 

were almost exactly the same even though approximately 40% of patients had 

been removed from the cohort. 

24 

25 

 
 
 
 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Eight patient cases were constructed to test the overlap between Kaplan-
Meier retention rates and EpiPick. When more than 50 patients were used per 
medication, the ASM with the highest retention rate was recommended by 
EpiPick in all cases (Figure 5). At least two ASMs with the highest retention 
rates were recommended by EpiPick in all cases.  

Figure 5 Comparison of ranking ASMs according to retention rate versus ranking according to 
EpiPick. Subfigures B and D show rankings of retention rates with at least 50 patients per 
ASM. Figures A and B show the EpiPick-ranking of the ASM with the highest retention rate. 
Figures C and D show the highest retention-based ranked ASM not recommended by EpiPick 

SELECTION AND CONTINUATION OF ASM IN 

CHILDREN (PAPER III) 

KEY POINTS 

Question Which ASMs are prescribed to children with epilepsy and what 

are the retention rates? 

Findings The most common treatments had high retention rates. Off-label 

use is common but does not seem to be associated with lower retention. 

Valproic acid is rarely prescribed to females of childbearing age since the 

implementation of restrictions. 

Implications Clinicians can be confident in following clinical practice 

rather than relying on formal registrations of ASMs. 

Children and adolescents are generally not included in clinical trials, which 

makes it more difficult to assess treatment efficacy for young patients [79]. 

Sweden has generous off-label rules, allowing doctors to prescribe 

medications outside strict regulatory approval. The retention of ASMs in 

children is also less affected by e.g. the cost of medications because of the 

universal coverage of healthcare costs in Sweden. A similar Swedish study 

investigated the prescription patterns of ASMs in children with epilepsy and 

other diagnoses [80]. The main contribution in this work beyond including 

more recent data is a retention rate analysis and a pathway analysis. 

Evaluating ASM efficacy for children using retention rate is presumably not 

as reliable as for adults since, e.g., children may have more difficulties 

conveying side effects, and the epilepsy may resolve. Nonetheless, studying 

the prescribing patterns of ASMs in pediatric patients is an important step to 

evaluate ASMs using routinely collected register data. 

One-year monotherapy retention rate analysis and pathway selection analysis 

of ASMs was performed to investigate prescription patterns. Patients were 

divided into strata of 1 month to 1 year, 1-5 years, 5-12 years, 12-18 years 

female, and 12-18 years male. Neonatal patients up to one month old were 

26 

27 

 
 
 
 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Eight patient cases were constructed to test the overlap between Kaplan-

Meier retention rates and EpiPick. When more than 50 patients were used per 

medication, the ASM with the highest retention rate was recommended by 

EpiPick in all cases (Figure 5). At least two ASMs with the highest retention 

rates were recommended by EpiPick in all cases.  

Figure 5 Comparison of ranking ASMs according to retention rate versus ranking according to 

EpiPick. Subfigures B and D show rankings of retention rates with at least 50 patients per 

ASM. Figures A and B show the EpiPick-ranking of the ASM with the highest retention rate. 

Figures C and D show the highest retention-based ranked ASM not recommended by EpiPick 

SELECTION AND CONTINUATION OF ASM IN 

CHILDREN (PAPER III) 

KEY POINTS 

Question Which ASMs are prescribed to children with epilepsy and what 
are the retention rates? 

Findings The most common treatments had high retention rates. Off-label 
use is common but does not seem to be associated with lower retention. 
Valproic acid is rarely prescribed to females of childbearing age since the 
implementation of restrictions. 

Implications Clinicians can be confident in following clinical practice 
rather than relying on formal registrations of ASMs. 

Children and adolescents are generally not included in clinical trials, which 
makes it more difficult to assess treatment efficacy for young patients [79]. 
Sweden has generous off-label rules, allowing doctors to prescribe 
medications outside strict regulatory approval. The retention of ASMs in 
children is also less affected by e.g. the cost of medications because of the 
universal coverage of healthcare costs in Sweden. A similar Swedish study 
investigated the prescription patterns of ASMs in children with epilepsy and 
other diagnoses [80]. The main contribution in this work beyond including 
more recent data is a retention rate analysis and a pathway analysis. 

Evaluating ASM efficacy for children using retention rate is presumably not 
as reliable as for adults since, e.g., children may have more difficulties 
conveying side effects, and the epilepsy may resolve. Nonetheless, studying 
the prescribing patterns of ASMs in pediatric patients is an important step to 
evaluate ASMs using routinely collected register data. 

One-year monotherapy retention rate analysis and pathway selection analysis 
of ASMs was performed to investigate prescription patterns. Patients were 
divided into strata of 1 month to 1 year, 1-5 years, 5-12 years, 12-18 years 
female, and 12-18 years male. Neonatal patients up to one month old were 

26 

27 

 
 
 
 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Figure 6 Retention rates of children of different age and sex groups (A-E) 

not included in the study because the group may contain both severe 
epilepsies and acute provoked neonatal seizures, variables not available in 
our dataset. 

For patients age 1 month to 1 year, oxcarbazepine and valproic acid had the 
highest retention rate at 60% and 51%, respectively (Figure 6). Patients aged 
1-5 years had oxcarbazepine, valproic acid, and levetiracetam at the highest 
retention rate at 62%, 61%, and 59%, respectively. Valproic acid is not 
indicated for this age group, suggesting that medications without pediatric 
indication are still retained by patients. For patients aged 5-12 years, 
lamotrigine, oxcarbazepine, and carbamazepine had the highest retention 
rates at 71%, 69%, and 68%, respectively. Males of age 12-18 had the highest 
retention rate with lamotrigine, valproic acid, and oxcarbazepine at 74%, 
73%, and 72%, respectively. For females, lamotrigine, ethosuximide, and 
levetiracetam had the highest retention rates at 68%, 64%, and 63%, 
respectively.  

28 

29 

 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Figure 6 Retention rates of children of different age and sex groups (A-E) 

not included in the study because the group may contain both severe 

epilepsies and acute provoked neonatal seizures, variables not available in 

our dataset. 

For patients age 1 month to 1 year, oxcarbazepine and valproic acid had the 

highest retention rate at 60% and 51%, respectively (Figure 6). Patients aged 

1-5 years had oxcarbazepine, valproic acid, and levetiracetam at the highest 

retention rate at 62%, 61%, and 59%, respectively. Valproic acid is not 

indicated for this age group, suggesting that medications without pediatric 

indication are still retained by patients. For patients aged 5-12 years, 

lamotrigine, oxcarbazepine, and carbamazepine had the highest retention 

rates at 71%, 69%, and 68%, respectively. Males of age 12-18 had the highest 

retention rate with lamotrigine, valproic acid, and oxcarbazepine at 74%, 

73%, and 72%, respectively. For females, lamotrigine, ethosuximide, and 

levetiracetam had the highest retention rates at 68%, 64%, and 63%, 

respectively.  

28 

29 

 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Figure 7 Pathways of ASMs for children for the four most common ASMs and the rest of the 
medications grouped as “other”. Abbreviations: CBZ, carbamazepine; CLN, clonazepam; CM, 
lacosamide; LTG, lamotrigine; LEV, levetiracetam; OXC, oxcarbazepine; PB, phenobarbital; 
TPM, topiramate; VPA, valproic acid; VGB, vigabatrin 

KEY POINTS 

The most common pathways for up to the third treatment were analyzed. The 
most common pathway per group was: 1 month to 1 year; phenobarbital 
followed by levetiracetam, 1-5 years, valproic acid followed by lamotrigine; 
5-12 years, valproic acid followed by lamotrigine; 12-18 years males, 
valproic acid followed by lamotrigine; 12-18 years females, lamotrigine 
followed by levetiracetam.  

30 

31 

PERSONALIZED ASM SELECTION USING 

MACHINE LEARNING (PAPER IV) 

Question Can registers be used to train specialized machine learning 

algorithms to predict a good ASM for a patient? 

Findings Our novel ML models performed better than the benchmark ML 

methods on the real data set. 

Implications The novel ML models show promising results, suggesting 

that they may be useful tools for clinicians. 

If doctors had a tool to help select ASMs, patients could have a higher 

likelihood of finding an adequate treatment. Using register data to train 

machine learning algorithms, we wanted to investigate if it could be a useful 

clinical support system for doctors. The register data has two major 

difficulties: (1) the duration of ASM use is sometimes censored and (2) the 

data is observational, meaning that estimations of treatment effect are 

subjected to confounding bias if confounding is not adjusted for. A model 

that handled confounding from observational data on multiple treatments 

with survival data was not available in the literature, and thus two existing 

models were further developed. 

The two models that were further built upon were [81] (CSA) and [82] 

(SurvCI). Both models are neural networks comprised of a base network 

connected to treatment arms (which also are neural networks). The idea is 

that the first layer constructs a representation of a patient such that it 

resembles a patient from an RCT, i.e. all patient groups having the same age, 

sex, and prevalence of the different comorbidities. This method is similar to 

that of using propensity score to weigh patients differently in an analysis. The 

resulting multi-armed version of the previous models were called Multi-CSA 

and Multi-SurvCI. 

 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Figure 7 Pathways of ASMs for children for the four most common ASMs and the rest of the 

medications grouped as “other”. Abbreviations: CBZ, carbamazepine; CLN, clonazepam; CM, 

lacosamide; LTG, lamotrigine; LEV, levetiracetam; OXC, oxcarbazepine; PB, phenobarbital; 

TPM, topiramate; VPA, valproic acid; VGB, vigabatrin 

The most common pathways for up to the third treatment were analyzed. The 

most common pathway per group was: 1 month to 1 year; phenobarbital 

followed by levetiracetam, 1-5 years, valproic acid followed by lamotrigine; 

5-12 years, valproic acid followed by lamotrigine; 12-18 years males, 

valproic acid followed by lamotrigine; 12-18 years females, lamotrigine 

followed by levetiracetam.  

PERSONALIZED ASM SELECTION USING 
MACHINE LEARNING (PAPER IV) 

KEY POINTS 

Question Can registers be used to train specialized machine learning 
algorithms to predict a good ASM for a patient? 

Findings Our novel ML models performed better than the benchmark ML 
methods on the real data set. 

Implications The novel ML models show promising results, suggesting 
that they may be useful tools for clinicians. 

If doctors had a tool to help select ASMs, patients could have a higher 
likelihood of finding an adequate treatment. Using register data to train 
machine learning algorithms, we wanted to investigate if it could be a useful 
clinical support system for doctors. The register data has two major 
difficulties: (1) the duration of ASM use is sometimes censored and (2) the 
data is observational, meaning that estimations of treatment effect are 
subjected to confounding bias if confounding is not adjusted for. A model 
that handled confounding from observational data on multiple treatments 
with survival data was not available in the literature, and thus two existing 
models were further developed. 

The two models that were further built upon were [81] (CSA) and [82] 
(SurvCI). Both models are neural networks comprised of a base network 
connected to treatment arms (which also are neural networks). The idea is 
that the first layer constructs a representation of a patient such that it 
resembles a patient from an RCT, i.e. all patient groups having the same age, 
sex, and prevalence of the different comorbidities. This method is similar to 
that of using propensity score to weigh patients differently in an analysis. The 
resulting multi-armed version of the previous models were called Multi-CSA 
and Multi-SurvCI. 

30 

31 

 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

A synthetic patient dataset was created to investigate the performance impact 
of training the ML model with observational data and then applying the 
model in the clinic. The synthetic dataset was created to resemble the real-
world dataset. A causal graph was created to visualize how the synthetic 
dataset was made (except for the unobserved confounding) (Figure 8).  

Figure 8 Causal graphs of the relation between variables. Created with BioRender.com 

The baseline model Componentwise Gradient Boosting Survival Analysis 
(CGB Survival) had the best performance both using the Concordance index 
(CI) metric and Cumulative/Dynamic Area Under Curve (CDAUC) (Table 
5). CGB Survival, Multi-CSA, and Multi-SurvCI all had small changes in 
performance from the observational dataset to the randomized one. The 

32 

33 

median retention rate had a lot lower performance than CGB Survival, Multi-

CSA, and Multi-SurvCI.  

Table 5 Performance of models on synthetic data 

Concordance index 

Area Under Curve 

Model 

Observational  Randomized 

Observational  Randomized 

Multi-CSA 

0.693 (0.003) 

0.702 (0.002) 

0.834 (0.002) 

0.793 (0.002) 

Multi-SurvCI 

0.698 (0.004) 

0.685 (0.003) 

0.804 (0.003) 

0.774 (0.004) 

CGB Survival 

0.714 (0.008) 

0.707 (0.010) 

0.844 (0.005) 

0.804 (0.009) 

Survival forest 

0.610 (0.017) 

0.570 (0.012) 

0.727 (0.013) 

0.632 (0.015) 

Median retention 

0.587 (0.027) 

0.637 (0.011) 

0.629 (0.036) 

0.676 (0.013) 

Multi-CSA had the highest performance, both with CI and CDAUC on the 

real-world dataset (Table 6). Note that this evaluation is of the observational 

dataset (Figure 8A) and not how it would be used in the clinic i.e. 

randomized dataset (Figure 8B). 

Table 6 Performance of models on real-world patient data 

Model 

Multi-CSA 

Multi-SurvCI 

CGB Survival 

CI 

0.706 (0.005) 

0.664 (0.005) 

0.651 (0.004) 

CDAUC 

0.750 (0.007) 

0.708 (0.007) 

0.614 (0.020) 

An estimation of the ML methods' performance compared to the current 

treatment regime was conducted using a doubly robust balanced policy 

evaluation [83]. The ML models were compared to clinicians, random policy, 

and single treatment policy (same ASM given to all patients). Three different 

versions of the policy evaluation were conducted. CGB Survival and Random 

Survival Forest (RSF) were used to estimate the duration for censored 

patients and a balanced method and a K-Nearest Neighbours (KNN) method 

was used to estimate the policy evaluation weights. In the balanced policy 

evaluation with CGB, oxcarbazepine single treatment policy had the highest 

value (1023.1, SD: 4.8) followed by Multi-SurvCI (976.2, SD: 15.0) and 

Multi-CSA (955.1, SD: 26.0) (Table 7). It is important to note that the 

 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

A synthetic patient dataset was created to investigate the performance impact 

of training the ML model with observational data and then applying the 

model in the clinic. The synthetic dataset was created to resemble the real-

world dataset. A causal graph was created to visualize how the synthetic 

dataset was made (except for the unobserved confounding) (Figure 8).  

Figure 8 Causal graphs of the relation between variables. Created with BioRender.com 

The baseline model Componentwise Gradient Boosting Survival Analysis 

(CGB Survival) had the best performance both using the Concordance index 

(CI) metric and Cumulative/Dynamic Area Under Curve (CDAUC) (Table 

5). CGB Survival, Multi-CSA, and Multi-SurvCI all had small changes in 

performance from the observational dataset to the randomized one. The 

median retention rate had a lot lower performance than CGB Survival, Multi-
CSA, and Multi-SurvCI.  

Table 5 Performance of models on synthetic data 

Concordance index 

Area Under Curve 

Model 

Observational  Randomized 

Observational  Randomized 

Multi-CSA 

0.693 (0.003) 

0.702 (0.002) 

0.834 (0.002) 

0.793 (0.002) 

Multi-SurvCI 

0.698 (0.004) 

0.685 (0.003) 

0.804 (0.003) 

0.774 (0.004) 

CGB Survival 

0.714 (0.008) 

0.707 (0.010) 

0.844 (0.005) 

0.804 (0.009) 

Survival forest 

0.610 (0.017) 

0.570 (0.012) 

0.727 (0.013) 

0.632 (0.015) 

Median retention  0.587 (0.027) 

0.637 (0.011) 

0.629 (0.036) 

0.676 (0.013) 

Multi-CSA had the highest performance, both with CI and CDAUC on the 
real-world dataset (Table 6). Note that this evaluation is of the observational 
dataset (Figure 8A) and not how it would be used in the clinic i.e. 
randomized dataset (Figure 8B). 

Table 6 Performance of models on real-world patient data 

Model 
Multi-CSA 
Multi-SurvCI 
CGB Survival 

CI 
0.706 (0.005) 
0.664 (0.005) 
0.651 (0.004) 

CDAUC 
0.750 (0.007) 
0.708 (0.007) 
0.614 (0.020) 

An estimation of the ML methods' performance compared to the current 
treatment regime was conducted using a doubly robust balanced policy 
evaluation [83]. The ML models were compared to clinicians, random policy, 
and single treatment policy (same ASM given to all patients). Three different 
versions of the policy evaluation were conducted. CGB Survival and Random 
Survival Forest (RSF) were used to estimate the duration for censored 
patients and a balanced method and a K-Nearest Neighbours (KNN) method 
was used to estimate the policy evaluation weights. In the balanced policy 
evaluation with CGB, oxcarbazepine single treatment policy had the highest 
value (1023.1, SD: 4.8) followed by Multi-SurvCI (976.2, SD: 15.0) and 
Multi-CSA (955.1, SD: 26.0) (Table 7). It is important to note that the 

32 

33 

 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

algorithms are trained for a slightly different target than the policy evaluation 
since censored patients must be estimated by a separate survival model. 

Figure 9 Comparison of clinician’s context averaged choice and the highest ranked ASM 

according to Multi-SurvCI 

Table 7 Policy evaluation of the novel ML algorithms, clinicians, random, and single-
treatment policy. In square brackets are details of the method; the first abbreviation is the 
method used to estimate the censored data points, and the second abbreviation describes how 
the weights are computed. CGB = Componentwise gradient boosting survival analysis, RSF = 
Random Survival Forest, balanced = doubly robust balanced policy evaluation, KNN = K-
nearest neighbours 

Policy 

Clinicians 

Value  
[CGB+Balanced] 
881.1 (4.6) 

Value  
[CGB+KNN] 
903.9 (60.6) 

Value  
[RSF+KNN] 
814.5 (32.6) 

Random policy 

824.7 (3.9) 

828.3 (9.2) 

854.8 (10.1) 

Multi-SurvCI 

976.2 (15.0) 

979.1 (21.4) 

1091.7 (25.3) 

Multi-CSA 

955.1 (26.0) 

963.2 (34.9) 

1007.5 (29.9) 

Carbamazepine 

875.8 (3.9) 

880.9 (24.3) 

814.9 (15.2) 

Oxcarbazepine 

1023.1 (4.8) 

1019.0 (23.7)  1152.2 (13.4) 

Valproic acid 

756.9 (2.3) 

767.5 (22.4) 

791.6 (15.3) 

Lamotrigine 

949.9 (2.3) 

959.3 (16.6) 

1000.7 (21.1) 

Gabapentin 

626.6 (8.0) 

632.4 (23.3) 

729.3 (15.1) 

Levetiracetam 

905.3 (3.1) 

909.1 (17.4) 

777.9 (9.6) 

Pregabalin 

628.7 (6.8) 

635.4 (16.8) 

697.3 (13.4) 

Another question that was asked in this study was: what if the suggestions 
from the ML algorithms could be used to improve the current treatment 
policy of clinicians? The current treatment policy was estimated by selecting 
the most common treatment for each of the 13 comorbidities and age +- 2 
years, e.g., the most common treatment for females aged 78-82 with a 
previous stroke is levetiracetam. The result is shown in Figure 9, where the 
ASM with highest retention according to Multi-SurvCI is compared to the 
Multi-SurvCI-estimation of the most common selection according to the 
current treatment policy of clinicans. 

34 

35 

 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

algorithms are trained for a slightly different target than the policy evaluation 

since censored patients must be estimated by a separate survival model. 

Figure 9 Comparison of clinician’s context averaged choice and the highest ranked ASM 
according to Multi-SurvCI 

Table 7 Policy evaluation of the novel ML algorithms, clinicians, random, and single-

treatment policy. In square brackets are details of the method; the first abbreviation is the 

method used to estimate the censored data points, and the second abbreviation describes how 

the weights are computed. CGB = Componentwise gradient boosting survival analysis, RSF = 

Random Survival Forest, balanced = doubly robust balanced policy evaluation, KNN = K-

nearest neighbours 

Policy 

Value  

Value  

Value  

Clinicians 

881.1 (4.6) 

903.9 (60.6) 

814.5 (32.6) 

[CGB+Balanced] 

[CGB+KNN] 

[RSF+KNN] 

Random policy 

824.7 (3.9) 

828.3 (9.2) 

854.8 (10.1) 

Multi-SurvCI 

976.2 (15.0) 

979.1 (21.4) 

1091.7 (25.3) 

Multi-CSA 

955.1 (26.0) 

963.2 (34.9) 

1007.5 (29.9) 

Carbamazepine 

875.8 (3.9) 

880.9 (24.3) 

814.9 (15.2) 

Oxcarbazepine 

1023.1 (4.8) 

1019.0 (23.7)  1152.2 (13.4) 

Valproic acid 

756.9 (2.3) 

767.5 (22.4) 

791.6 (15.3) 

Lamotrigine 

949.9 (2.3) 

959.3 (16.6) 

1000.7 (21.1) 

Gabapentin 

626.6 (8.0) 

632.4 (23.3) 

729.3 (15.1) 

Levetiracetam 

905.3 (3.1) 

909.1 (17.4) 

777.9 (9.6) 

Pregabalin 

628.7 (6.8) 

635.4 (16.8) 

697.3 (13.4) 

Another question that was asked in this study was: what if the suggestions 

from the ML algorithms could be used to improve the current treatment 

policy of clinicians? The current treatment policy was estimated by selecting 

the most common treatment for each of the 13 comorbidities and age +- 2 

years, e.g., the most common treatment for females aged 78-82 with a 

previous stroke is levetiracetam. The result is shown in Figure 9, where the 

ASM with highest retention according to Multi-SurvCI is compared to the 

Multi-SurvCI-estimation of the most common selection according to the 

current treatment policy of clinicans. 

34 

35 

 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

DISCUSSION 

This thesis has investigated the use and retention of ASMs in adults and 
children, explored the suitability of routinely collected register data as a data 
source for informing ASM selection, and developed machine learning 
methods to determine the optimal ASM.  

Conclusions of this thesis that will be discussed: 

1.  Register data approximate retention rates and relative 

retention of ASMs in manners that are similar to the results 
of previous clinical trials. 

2.  There is likely room for improvement in retention rate 
through personalized ASM selection based on patient 
features. 

3.  Prediction of personalized ASM based on register data 
resembles suggestions obtained through expert advice, 
showing potential clinical relevance. 

4.  Machine learning trained on register data might be a useful 

tool for selecting optimal ASM. 

1. In an analysis in Paper I, it was found that the Kaplan-Meier retention rates 
of register data showed similar 5-year retention rates as that of SANAD I 
[76]. Our study also yielded similar results as a meta-analysis of RCTs. The 
1-year retention of carbamazepine was 58% in our data. In a meta-analysis of 
30 RCTs with carbamazepine, the 1-year retention was 61% (95% CI:54-
68%) [84]. However, in contrast to our study, this meta-analysis included 
focal and generalized seizures of both children and adults. In a network meta-
analysis of RCTs with carbamazepine as the baseline, it was found that 
lamotrigine and levetiracetam were better than carbamazepine for treatment 
failures for any reason and due to adverse events [85]. Carbamazepine was 
better than gabapentin for treatment failures for any reason and lack of 
efficacy, but gabapentin was better for treatment failures due to adverse 
events.  

When ranking the ASMs according to the hazard ratio (HR) from the network 
analysis [85], the result shows similar tendencies to that of ranking according 
to retention rate from our data: lamotrigine and levetiracetam have higher 

retention, lacosamide, carbamazepine, oxcarbazepine, and valproic acid have 

medium retention, and phenytoin, topiramate, and gabapentin have low 

retention (Table 8). Phenobarbital stands out as the retention rate is high, but 

the HR is low. This is likely to be at least partly because of the low number 

of patients in the Kaplan-Meier retention rate estimation, 58. The network 

study included both children and adults while our study in Paper II only 

included adults >30 years of age. The difference in age in the two studies 

might be of significance because older populations often have higher 

retention rates, see for example [78]. 

Table 8 Comparison of ASM ranking according to retention rates (Paper II) and a network 

analysis [85]. Pregabalin and clobazam were not included in the network analysis. Light 

orange means few patients for estimation of retention rate (<200). HR=Hazard ratio 

ASM 

1-year 

retention 

Network analysis 

Network 

by Nevitt et. al.  

rate, % (CI) 

HR (95% CI) 

analysis 

ranking 

Lamotrigine 

71 (69-72) 

0.79 (0.69-0.91) 

Levetiracetam 

68 (68-69) 

0.80 (0.69-0.93) 

Phenobarbital 

66 (49-75) 

1.56 (1.18-2.07) 

10 

Valproic acid 

62 (61-64) 

1.08 (0.88-1.31) 

Lacosamide 

61 (51-68) 

0.95 (0.74-1.22) 

Carbamazepine 

58 (58-59) 

1.00 (-) 

Oxcarbazepine 

57 (52-61) 

1.03 (0.82-1.30) 

Phenytoin 

Gabapentin 

Pregabalin 

Clobazam 

Topiramate 

53 (49-57) 

1.14 (0.90-1.44) 

45 (41-48) 

1.21 (1.01 to 1.45) 

40 (36-45) 

39 (30-46) 

- 

- 

38 (28-46) 

1.19 (0.99-1.43) 

1 

2 

6 

3 

4 

5 

7 

9 

- 

- 

8 

The SANAD I and II trials have some of the most prominent evidence of 

ASM efficacy. In SANAD I, lamotrigine had a longer time to treatment 

failure than carbamazepine, gabapentin, and topiramate, with a non-

significant advantage over oxcarbazepine [42]. In SANAD II, the primary 

outcome was time to 12 month-remission divided into two analyses, an 

intention-to-treat (ITT) which included all patients, and a per-protocol (PP) 

36 

37 

 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

DISCUSSION 

This thesis has investigated the use and retention of ASMs in adults and 

children, explored the suitability of routinely collected register data as a data 

source for informing ASM selection, and developed machine learning 

methods to determine the optimal ASM.  

Conclusions of this thesis that will be discussed: 

1.  Register data approximate retention rates and relative 

retention of ASMs in manners that are similar to the results 

of previous clinical trials. 

2.  There is likely room for improvement in retention rate 

through personalized ASM selection based on patient 

features. 

3.  Prediction of personalized ASM based on register data 

resembles suggestions obtained through expert advice, 

showing potential clinical relevance. 

4.  Machine learning trained on register data might be a useful 

tool for selecting optimal ASM. 

1. In an analysis in Paper I, it was found that the Kaplan-Meier retention rates 

of register data showed similar 5-year retention rates as that of SANAD I 

[76]. Our study also yielded similar results as a meta-analysis of RCTs. The 

1-year retention of carbamazepine was 58% in our data. In a meta-analysis of 

30 RCTs with carbamazepine, the 1-year retention was 61% (95% CI:54-

68%) [84]. However, in contrast to our study, this meta-analysis included 

focal and generalized seizures of both children and adults. In a network meta-

analysis of RCTs with carbamazepine as the baseline, it was found that 

lamotrigine and levetiracetam were better than carbamazepine for treatment 

failures for any reason and due to adverse events [85]. Carbamazepine was 

better than gabapentin for treatment failures for any reason and lack of 

efficacy, but gabapentin was better for treatment failures due to adverse 

events.  

When ranking the ASMs according to the hazard ratio (HR) from the network 

analysis [85], the result shows similar tendencies to that of ranking according 

to retention rate from our data: lamotrigine and levetiracetam have higher 

retention, lacosamide, carbamazepine, oxcarbazepine, and valproic acid have 
medium retention, and phenytoin, topiramate, and gabapentin have low 
retention (Table 8). Phenobarbital stands out as the retention rate is high, but 
the HR is low. This is likely to be at least partly because of the low number 
of patients in the Kaplan-Meier retention rate estimation, 58. The network 
study included both children and adults while our study in Paper II only 
included adults >30 years of age. The difference in age in the two studies 
might be of significance because older populations often have higher 
retention rates, see for example [78]. 

Table 8 Comparison of ASM ranking according to retention rates (Paper II) and a network 
analysis [85]. Pregabalin and clobazam were not included in the network analysis. Light 
orange means few patients for estimation of retention rate (<200). HR=Hazard ratio 

ASM 

1-year 
retention 
rate, % (CI) 

Network analysis 
by Nevitt et. al.  
HR (95% CI) 

Network 
analysis 
ranking 

Lamotrigine 

71 (69-72) 

0.79 (0.69-0.91) 

Levetiracetam 

68 (68-69) 

0.80 (0.69-0.93) 

Phenobarbital 

66 (49-75) 

1.56 (1.18-2.07) 

Valproic acid 

62 (61-64) 

1.08 (0.88-1.31) 

Lacosamide 

61 (51-68) 

0.95 (0.74-1.22) 

Carbamazepine 

58 (58-59) 

1.00 (-) 

Oxcarbazepine 

57 (52-61) 

1.03 (0.82-1.30) 

Phenytoin 

Gabapentin 

Pregabalin 

Clobazam 

Topiramate 

53 (49-57) 

1.14 (0.90-1.44) 

45 (41-48) 

1.21 (1.01 to 1.45) 

40 (36-45) 

39 (30-46) 

- 

- 

38 (28-46) 

1.19 (0.99-1.43) 

1 

2 

10 

6 

3 

4 

5 

7 

9 

- 

- 

8 

The SANAD I and II trials have some of the most prominent evidence of 
ASM efficacy. In SANAD I, lamotrigine had a longer time to treatment 
failure than carbamazepine, gabapentin, and topiramate, with a non-
significant advantage over oxcarbazepine [42]. In SANAD II, the primary 
outcome was time to 12 month-remission divided into two analyses, an 
intention-to-treat (ITT) which included all patients, and a per-protocol (PP) 

36 

37 

 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

one which excluded patients with major protocol deviations and patients who 
subsequently were diagnosed as not having epilepsy [43]. The authors found 
that levetiracetam was inferior to lamotrigine in both the ITT and PP analyses 
while zonisamide was inferior only in the PP analysis. In Paper II, we also 
found that lamotrigine had the highest retention in adults with presumed focal 
epilepsy. 

There have been several studies utilizing prescription data to estimate 
retention of ASMs. A study conducted on focal epilepsy in Japan using a 
health insurance claims database found that lacosamide had a higher 1-year 
retention rate (73.0%, n=141 patients) than levetiracetam (58.3%, n=530), 
lamotrigine (57.5%, n=80), and perampanel (54.7%, n=75) [86]. As in Paper 
II, levetiracetam and lamotrigine showed similar retention, even though the 
number of patients was quite low in this study, especially for lamotrigine. 

2. In Paper I, the room for retention rate improvement was estimated to be 
14-21% depending on the comorbidity. In a similar analysis in Paper IV, a 
policy evaluation score was calculated for the novel machine learning 
methods as well as the current treatment policy by clinicians. While the 
policy evaluation showed unexpected results such as oxcarbazepine assigned 
to all patients got the highest score of the evaluated policies, it still might 
give a hint about the size of the treatment gap. Compared to clinicians, there 
was a 16.1% increase for oxcarbazepine, a 10.8% increase for Multi-SurvCI 
and an 8.4% increase for Multi-CSA (using the CGB+Balanced variant). 
Note that the two methods from Paper I and Paper IV differ in cohort, unit, 
and adjustment of confounding.   

A study using machine learning to predict the optimal ASM for patients 
based on electronic health records estimated a 22 percentage points (pp) 
increase (0.4 to 0.62, estimated from viewing the plot) in the probability of 
treatment-related survival (p<0.001) with the model-predicted regimen 
compared to the current treatment regime [87]. In a validation study of 
EpiPick, it was found that the 1-year retention rate could increase by 12 pp, 
from 67% to 79% (p=0.005) [42]. The validation study included 425 patients 
and evaluated retention rates, seizure freedom rates, and adverse effects 
leading to treatment discontinuation. A sensitivity analysis on a sub-cohort 
with propensity scoring yielded similar results. 

3. In Paper II, we found that there is a large agreement between retention 

rates and the expert-based algorithm tool EpiPick in all eight test cases. 

A validation study of EpiPick invited 24 experts to select the optimal ASM 

for 25 patient cases and compared it to the choice of the EpiPick app [88]. 

There was a fair agreement between the experts and the app, with 73% 

agreement on the highest ranked selections of the app and 95% of experts 

found that no incorrect ASMs were ranked highest by EpiPick [88]. Since 

experts support the suitability of EpiPick for use by healthcare providers [88] 

and EpiPick ranks and retention rate ranks are similar, it is likely that 

retention rates ranks are of clinical relevance. 

4. To evaluate the novel machine learning methods in Paper IV, they were 

compared to baseline methods, including a Kaplan-Meier median retention 

method. This KM method is based on the results in Paper II. For all test 

cases, the retention rates showed similar results as the tool EpiPick [89] if 50 

patients were used in the population to estimate the retention rate. The 

median retention rate method had a concordance index of 0.587 on the 

synthetic dataset while Multi-CSA and Multi-SurvCI had 0.693 and 0.698, 

respectively. If the median retention rate method is approximately equally as 

good as EpiPick, the novel machine learning methods may have equal or 

better performance than EpiPick.  

In the policy evaluation in Paper IV, oxcarbazepine had the highest score of 

all policies. It would be expected to have an ML method, optimized towards 

the target, to have the highest score. The policy evaluation and the training 

data have slightly different targets. This exposes a weakness in either the 

policy evaluation method, e.g. that estimation of time-to-events and weights 

are off, or that the novel ML methods do not optimize towards the correct 

goal (or possibly both). 

In a previous study using ML to predict ASM retention, the most common 

suggestions by the model were, in order of prevalence, levetiracetam, 

lamotrigine, pregabalin, and oxcarbazepine [87]. Levetiracetam was by far 

the most recommended ASM by the model, which is considerably different 

from the suggestions made by the ML models in this study, e.g. shown in 

Figure 9. Valproic acid was not included in this previous study. 

38 

39 

 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

one which excluded patients with major protocol deviations and patients who 

subsequently were diagnosed as not having epilepsy [43]. The authors found 

that levetiracetam was inferior to lamotrigine in both the ITT and PP analyses 

while zonisamide was inferior only in the PP analysis. In Paper II, we also 

found that lamotrigine had the highest retention in adults with presumed focal 

epilepsy. 

There have been several studies utilizing prescription data to estimate 

retention of ASMs. A study conducted on focal epilepsy in Japan using a 

health insurance claims database found that lacosamide had a higher 1-year 

retention rate (73.0%, n=141 patients) than levetiracetam (58.3%, n=530), 

lamotrigine (57.5%, n=80), and perampanel (54.7%, n=75) [86]. As in Paper 

II, levetiracetam and lamotrigine showed similar retention, even though the 

number of patients was quite low in this study, especially for lamotrigine. 

2. In Paper I, the room for retention rate improvement was estimated to be 

14-21% depending on the comorbidity. In a similar analysis in Paper IV, a 

policy evaluation score was calculated for the novel machine learning 

methods as well as the current treatment policy by clinicians. While the 

policy evaluation showed unexpected results such as oxcarbazepine assigned 

to all patients got the highest score of the evaluated policies, it still might 

give a hint about the size of the treatment gap. Compared to clinicians, there 

was a 16.1% increase for oxcarbazepine, a 10.8% increase for Multi-SurvCI 

and an 8.4% increase for Multi-CSA (using the CGB+Balanced variant). 

Note that the two methods from Paper I and Paper IV differ in cohort, unit, 

and adjustment of confounding.   

A study using machine learning to predict the optimal ASM for patients 

based on electronic health records estimated a 22 percentage points (pp) 

increase (0.4 to 0.62, estimated from viewing the plot) in the probability of 

treatment-related survival (p<0.001) with the model-predicted regimen 

compared to the current treatment regime [87]. In a validation study of 

EpiPick, it was found that the 1-year retention rate could increase by 12 pp, 

from 67% to 79% (p=0.005) [42]. The validation study included 425 patients 

and evaluated retention rates, seizure freedom rates, and adverse effects 

leading to treatment discontinuation. A sensitivity analysis on a sub-cohort 

with propensity scoring yielded similar results. 

3. In Paper II, we found that there is a large agreement between retention 
rates and the expert-based algorithm tool EpiPick in all eight test cases. 
A validation study of EpiPick invited 24 experts to select the optimal ASM 
for 25 patient cases and compared it to the choice of the EpiPick app [88]. 
There was a fair agreement between the experts and the app, with 73% 
agreement on the highest ranked selections of the app and 95% of experts 
found that no incorrect ASMs were ranked highest by EpiPick [88]. Since 
experts support the suitability of EpiPick for use by healthcare providers [88] 
and EpiPick ranks and retention rate ranks are similar, it is likely that 
retention rates ranks are of clinical relevance. 

4. To evaluate the novel machine learning methods in Paper IV, they were 
compared to baseline methods, including a Kaplan-Meier median retention 
method. This KM method is based on the results in Paper II. For all test 
cases, the retention rates showed similar results as the tool EpiPick [89] if 50 
patients were used in the population to estimate the retention rate. The 
median retention rate method had a concordance index of 0.587 on the 
synthetic dataset while Multi-CSA and Multi-SurvCI had 0.693 and 0.698, 
respectively. If the median retention rate method is approximately equally as 
good as EpiPick, the novel machine learning methods may have equal or 
better performance than EpiPick.  

In the policy evaluation in Paper IV, oxcarbazepine had the highest score of 
all policies. It would be expected to have an ML method, optimized towards 
the target, to have the highest score. The policy evaluation and the training 
data have slightly different targets. This exposes a weakness in either the 
policy evaluation method, e.g. that estimation of time-to-events and weights 
are off, or that the novel ML methods do not optimize towards the correct 
goal (or possibly both). 

In a previous study using ML to predict ASM retention, the most common 
suggestions by the model were, in order of prevalence, levetiracetam, 
lamotrigine, pregabalin, and oxcarbazepine [87]. Levetiracetam was by far 
the most recommended ASM by the model, which is considerably different 
from the suggestions made by the ML models in this study, e.g. shown in 
Figure 9. Valproic acid was not included in this previous study. 

38 

39 

 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

STRENGTHS AND LIMITATIONS 

Here, the methodology of the studies will be discussed with its advantages 
and potential points of improvement compared to similar studies. 

A potential flaw of modelling the drug used retrospectively, i.e. the 12 
months gap allowance, is that the treatment use length might be biased [90]. 
For example, if a drug is commonly used by old people who are more likely 
to decease i.e. the outcome is censored, then the censoring might happen 
without the possibility of a prescription. More concretely, if a patient decides 
to quit a medication and dies 10 months after their last prescription, we 
assume that the patient used the medication for all 10 months, while if the 
patient would have lived for at least 2 more months, the patient would not 
have retrieved new medication and the treatment use length would have 
stopped at 3 months after the last dispensation. This is only a potential 
problem for the decision-making of selecting ASM if some drugs are used 
more by patients who are more likely to die, meaning that the relative 
outcome between ASMs is changed. 

Drug adherence is another potential confounder. Patients might dispense the 
medication but not take it. However, it is seemingly unlikely that patients 
would retrieve medication and not use it. It is also unlikely that some 
medications more than others would be retrieved and not used, which would 
be a problem since the relative adherence would differ between the ASMs. 
Note that there is a strength in using dispensations, which are ASMs actually 
picked up by the patient, and not just a prescription by the doctor.  

Our data may be missing important variables for the optimal selection of 
ASM. The ILAE suggests considering, except age, sex, and comorbidities 
(which are available in our data) seizure syndrome, dose-dependent adverse 
effects, idiosyncratic reactions, chronic toxicities, teratogenicity, 
carcinogenicity, pharmacokinetics, interaction potential, formulations, 
genetics, comedications, and ability to swallow pills in the decision-making 
[17]. The guidelines also mention insurance coverage, relative wealth, and 
ASM cost as variables, which may be less important to consider in a Swedish 
context since the healthcare system is to a large extent funded by the 

government. Missing variables might cause dubious results due to 

unobserved confounding [91]. 

A systematic review of validation studies of administrative data to identify 

cases of epilepsy suggests that algorithms with the combination of ICD-10 

code G40 (epilepsy) and one or more ASMs can be used confidently to 

identify people with epilepsy [92]. The approach had the highest positive 

predictive value compared to alternative approaches of using the G40 code 

alone, ICD-code R568 (seizure) and the use of ASM, and the use of ASM 

alone. 

The titration time might affect the outcome of the ASMs. As shown in Table 

2, titration times differ for different drugs. ASMs with longer titration times 

need a longer time to be evaluated, which means that patients stay on those 

drugs for a longer time, and the duration of use is thus artificially increased. 

On the other hand, a patient might have seizures during the titration period, 

causing a switch of medication to a more fast-acting ASM. In this case, the 

drug was not necessarily bad, it was just not the right dose. Lamotrigine has 

the longest titration time, meaning that its retention might be more difficult to 

estimate. 

The quality of care differs between different hospitals and providers. If some 

healthcare providers have an insufficient clinical follow-up of patients and 

also prescribe some medications more than others, our analysis of the 

treatment effect might be skewed. An American study found that 

prescriptions for second-generation ASMs were more commonly prescribed 

by clinicians practising near an epilepsy centre [93]. Thus, training the ML 

models on only patients who e.g. received care from neurologists could be an 

alternative approach to achieve data points with higher quality. 

National registers have some advantages compared to medical claims when 

used as a data source. Medical claims have been used to retrieve a large 

cohort of patients with epilepsy for the use of machine learning to select 

ASM [87]. The data source was the IMS Health Surveillance Data 

Incorporated medical claims database (SDI) which aggregates patient 

information from multiple provider sources. A drawback with SDI is that all 

claims for an individual might not be obtained if providers not submitting to 

40 

41 

 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

STRENGTHS AND LIMITATIONS 

Here, the methodology of the studies will be discussed with its advantages 

and potential points of improvement compared to similar studies. 

A potential flaw of modelling the drug used retrospectively, i.e. the 12 

months gap allowance, is that the treatment use length might be biased [90]. 

For example, if a drug is commonly used by old people who are more likely 

to decease i.e. the outcome is censored, then the censoring might happen 

without the possibility of a prescription. More concretely, if a patient decides 

to quit a medication and dies 10 months after their last prescription, we 

assume that the patient used the medication for all 10 months, while if the 

patient would have lived for at least 2 more months, the patient would not 

have retrieved new medication and the treatment use length would have 

stopped at 3 months after the last dispensation. This is only a potential 

problem for the decision-making of selecting ASM if some drugs are used 

more by patients who are more likely to die, meaning that the relative 

outcome between ASMs is changed. 

Drug adherence is another potential confounder. Patients might dispense the 

medication but not take it. However, it is seemingly unlikely that patients 

would retrieve medication and not use it. It is also unlikely that some 

medications more than others would be retrieved and not used, which would 

be a problem since the relative adherence would differ between the ASMs. 

Note that there is a strength in using dispensations, which are ASMs actually 

picked up by the patient, and not just a prescription by the doctor.  

Our data may be missing important variables for the optimal selection of 

ASM. The ILAE suggests considering, except age, sex, and comorbidities 

(which are available in our data) seizure syndrome, dose-dependent adverse 

effects, idiosyncratic reactions, chronic toxicities, teratogenicity, 

carcinogenicity, pharmacokinetics, interaction potential, formulations, 

genetics, comedications, and ability to swallow pills in the decision-making 

[17]. The guidelines also mention insurance coverage, relative wealth, and 

ASM cost as variables, which may be less important to consider in a Swedish 

context since the healthcare system is to a large extent funded by the 

government. Missing variables might cause dubious results due to 
unobserved confounding [91]. 

A systematic review of validation studies of administrative data to identify 
cases of epilepsy suggests that algorithms with the combination of ICD-10 
code G40 (epilepsy) and one or more ASMs can be used confidently to 
identify people with epilepsy [92]. The approach had the highest positive 
predictive value compared to alternative approaches of using the G40 code 
alone, ICD-code R568 (seizure) and the use of ASM, and the use of ASM 
alone. 

The titration time might affect the outcome of the ASMs. As shown in Table 
2, titration times differ for different drugs. ASMs with longer titration times 
need a longer time to be evaluated, which means that patients stay on those 
drugs for a longer time, and the duration of use is thus artificially increased. 
On the other hand, a patient might have seizures during the titration period, 
causing a switch of medication to a more fast-acting ASM. In this case, the 
drug was not necessarily bad, it was just not the right dose. Lamotrigine has 
the longest titration time, meaning that its retention might be more difficult to 
estimate. 

The quality of care differs between different hospitals and providers. If some 
healthcare providers have an insufficient clinical follow-up of patients and 
also prescribe some medications more than others, our analysis of the 
treatment effect might be skewed. An American study found that 
prescriptions for second-generation ASMs were more commonly prescribed 
by clinicians practising near an epilepsy centre [93]. Thus, training the ML 
models on only patients who e.g. received care from neurologists could be an 
alternative approach to achieve data points with higher quality. 

National registers have some advantages compared to medical claims when 
used as a data source. Medical claims have been used to retrieve a large 
cohort of patients with epilepsy for the use of machine learning to select 
ASM [87]. The data source was the IMS Health Surveillance Data 
Incorporated medical claims database (SDI) which aggregates patient 
information from multiple provider sources. A drawback with SDI is that all 
claims for an individual might not be obtained if providers not submitting to 

40 

41 

 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Studies using machine learning to predict the outcome of ASMs similar to 

that of Paper IV have been conducted (Table 9). The advantage of the 

methodology in Paper IV compared to the other studies in Table 9 is the 

number of patients and the causal inference approach.  

SDI were used [87]. To control for potentially lost data, the authors required 
at least 80% continuous monthly eligibility, in 1-year windows, in any of the 
databases. At least 2 years of data were required for each patient. Excluding 
patients with lost information removes data points but could also introduce 
selection bias if, for example, young patients are more likely to have 
healthcare providers that do not report to SDI. In Swedish registers, all 
healthcare providers except primary care are obligated to report in- and 
outpatient visits, meaning that diagnoses for e.g. high blood pressure, 
diabetes type 2, and heart failure have relatively low sensitivity. 

Survival analysis is difficult to evaluate because of incomplete information 
from the censoring. In the work in this thesis, the duration of treatment has 
been used as the outcome. An alternative approach could have been to use a 
rule to define a binary outcome for each ASM that a patient used. For 
example: keeping medication for a year would suggest that the ASM was 
adequate, and conversely, if the medication is stopped earlier, it was 
inadequate. This approach is used in [87], where an ASM was assumed to be 
successful if a medication was used for more than 12 months, unsuccessful if 
used for 1-12 months, and invalid if used for less than 1 month. The results 
from the accuracy tests and policy evaluation in Paper IV could have been 
more reliable with this method because of the full information on the labels. 
However, if there is insight in e.g. if a patient used a medication for 3 months 
or 9 months in terms of how good the ASM was, a simplification of the 
outcome could potentially lead to worse performance on real patients if a 
machine learning model trained on the simplified data would be used in the 
clinic. One could also argue that the censoring could simply be ignored, and 
thus assume that patients quit a medication at the end of the study or at death, 
but this would likely skew outcomes of medications, and medications 
commonly prescribed at the end of the study would seem worse. Another 
question that could be asked is: what if patients with censored outcomes were 
removed from the cohort? That could possibly skew the outcomes as well 
since older patients and patients with epilepsy-onset close to the end of the 
study would more often be removed. Since patients would be removed non-
randomly from the study, not only would the number of patients decrease, but 
selection bias would also be introduced. 

42 

43 

 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

Studies using machine learning to predict the outcome of ASMs similar to 
that of Paper IV have been conducted (Table 9). The advantage of the 
methodology in Paper IV compared to the other studies in Table 9 is the 
number of patients and the causal inference approach.  

SDI were used [87]. To control for potentially lost data, the authors required 

at least 80% continuous monthly eligibility, in 1-year windows, in any of the 

databases. At least 2 years of data were required for each patient. Excluding 

patients with lost information removes data points but could also introduce 

selection bias if, for example, young patients are more likely to have 

healthcare providers that do not report to SDI. In Swedish registers, all 

healthcare providers except primary care are obligated to report in- and 

outpatient visits, meaning that diagnoses for e.g. high blood pressure, 

diabetes type 2, and heart failure have relatively low sensitivity. 

Survival analysis is difficult to evaluate because of incomplete information 

from the censoring. In the work in this thesis, the duration of treatment has 

been used as the outcome. An alternative approach could have been to use a 

rule to define a binary outcome for each ASM that a patient used. For 

example: keeping medication for a year would suggest that the ASM was 

adequate, and conversely, if the medication is stopped earlier, it was 

inadequate. This approach is used in [87], where an ASM was assumed to be 

successful if a medication was used for more than 12 months, unsuccessful if 

used for 1-12 months, and invalid if used for less than 1 month. The results 

from the accuracy tests and policy evaluation in Paper IV could have been 

more reliable with this method because of the full information on the labels. 

However, if there is insight in e.g. if a patient used a medication for 3 months 

or 9 months in terms of how good the ASM was, a simplification of the 

outcome could potentially lead to worse performance on real patients if a 

machine learning model trained on the simplified data would be used in the 

clinic. One could also argue that the censoring could simply be ignored, and 

thus assume that patients quit a medication at the end of the study or at death, 

but this would likely skew outcomes of medications, and medications 

commonly prescribed at the end of the study would seem worse. Another 

question that could be asked is: what if patients with censored outcomes were 

removed from the cohort? That could possibly skew the outcomes as well 

since older patients and patients with epilepsy-onset close to the end of the 

study would more often be removed. Since patients would be removed non-

randomly from the study, not only would the number of patients decrease, but 

selection bias would also be introduced. 

42 

43 

 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Table 9 Studies of machine learning for prediction of ASM efficacy 

Study  Number of 

patients 

38830 

Paper 
IV 

[94] 

1798 

[87] 

34990 

Number 
of ASMs 

Patient variables 

Age, sex, 13 
comorbidities 

Age, sex, 3 
comorbidities, 8 
clinical variables, 
type of epilepsy, 
EEG and MRI, and 
previous ASMs  

Age, sex, 
comorbidities, 
other drugs,  

7 

7 

10 and 
combinati
ons of 
ASMs (52 
regimens 
in total) 

[95] 

235 

1 

[96] 

287 

1, any 
monother
apy 

Age, sex, genetics, 
previous ASMs, 
EEG, seizures, 
epilepsy type, 
demographics, 
clinical variables 

Age, sex, seizure 
type, clinical 
variables, 
demographics, 
EEG, MRI 

Treatment 
outcome 

Length of ASM 
use 

Complete 
seizure 
freedom for the 
first year of 
ASM treatment 

No change in 
ASM regimen 
or withdrawal 
of any ASM in 
the subsequent 
1-12 months 
after change 

>50% seizure 
frequency 
reduction 12 
weeks after 
study baseline 

Early 
remission, late 
remission, and 
never 
remission 

[97] 

46 

[98] 

Mice 

1 

4 

Age, MRI, epilepsy 
type, clinical 
variables 

3 years of 
seizure 
freedom 

EEG features 

Binary 
response 

Samuel Håkansson 

In the ML for ASM studies [94] and [95], the previous ASMs of a patient are 

used as variables. While this might seem like a good idea, it might cause 

trouble. The reason is not because the variable is not informative. It is, as 

exemplified in Paper I, showing that lamotrigine had the highest retention 

rate as initial ASM, but for patients starting with valproic acid, levetiracetam 

had the highest retention. However, the reason it is a dubious variable is that 

the distribution of covariates might differ between the patients who had a 

previous ASM and those who did not. This stems from the doctor using the 

information of the previous treatment when the new medication was selected.  

Even though the developed machine learning models in Paper IV account for 

training on observational data, it is important to note that the causal effect 

estimation performed by the models is not the same as causal decision-

making [99]. The reason the models are optimized for effect estimation and 

not decision-making is because of the structure of the training data. To 

optimize for decision-making, we would have to know which medications 

worked for a patient. While this could have been estimated by a hard rule, it 

is probably difficult to specify a rule such that the decision-making error 

would be less than by using causal effect estimation. 

Another potentially improbable but not impossible scenario arises from the 

difficulty for the clinician to evaluate an ASM for a patient. If a particular 

ASM has the property that patients have fewer seizures but are more aware 

while having the seizures, they might think a new medication is worse even 

though they might have fewer seizures. A solution to this problem is to 

record seizures using devices such as EEG headsets, wearables, or cameras. 

44 

45 

 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Table 9 Studies of machine learning for prediction of ASM efficacy 

Study  Number of 

Number 

Patient variables 

Treatment 

patients 

of ASMs 

Paper 

38830 

IV 

[94] 

1798 

7 

7 

Age, sex, 13 

comorbidities 

outcome 

Length of ASM 

use 

Age, sex, 3 

Complete 

comorbidities, 8 

seizure 

clinical variables, 

freedom for the 

type of epilepsy, 

first year of 

EEG and MRI, and 

ASM treatment 

previous ASMs  

[87] 

34990 

10 and 

Age, sex, 

combinati

comorbidities, 

ons of 

other drugs,  

ASMs (52 

regimens 

in total) 

No change in 

ASM regimen 

or withdrawal 

of any ASM in 

the subsequent 

1-12 months 

after change 

[95] 

235 

1 

Age, sex, genetics, 

>50% seizure 

[96] 

287 

1, any 

Age, sex, seizure 

Early 

monother

type, clinical 

apy 

variables, 

remission, late 

remission, and 

previous ASMs, 

frequency 

EEG, seizures, 

epilepsy type, 

demographics, 

clinical variables 

reduction 12 

weeks after 

study baseline 

demographics, 

never 

EEG, MRI 

remission 

Age, MRI, epilepsy 

3 years of 

type, clinical 

variables 

EEG features 

seizure 

freedom 

Binary 

response 

[97] 

46 

[98] 

Mice 

1 

4 

Samuel Håkansson 

In the ML for ASM studies [94] and [95], the previous ASMs of a patient are 
used as variables. While this might seem like a good idea, it might cause 
trouble. The reason is not because the variable is not informative. It is, as 
exemplified in Paper I, showing that lamotrigine had the highest retention 
rate as initial ASM, but for patients starting with valproic acid, levetiracetam 
had the highest retention. However, the reason it is a dubious variable is that 
the distribution of covariates might differ between the patients who had a 
previous ASM and those who did not. This stems from the doctor using the 
information of the previous treatment when the new medication was selected.  

Even though the developed machine learning models in Paper IV account for 
training on observational data, it is important to note that the causal effect 
estimation performed by the models is not the same as causal decision-
making [99]. The reason the models are optimized for effect estimation and 
not decision-making is because of the structure of the training data. To 
optimize for decision-making, we would have to know which medications 
worked for a patient. While this could have been estimated by a hard rule, it 
is probably difficult to specify a rule such that the decision-making error 
would be less than by using causal effect estimation. 

Another potentially improbable but not impossible scenario arises from the 
difficulty for the clinician to evaluate an ASM for a patient. If a particular 
ASM has the property that patients have fewer seizures but are more aware 
while having the seizures, they might think a new medication is worse even 
though they might have fewer seizures. A solution to this problem is to 
record seizures using devices such as EEG headsets, wearables, or cameras. 

44 

45 

 
 
 
 
 
 
time corresponds to the outcome of the treatment, and the treatment is only 

stopped if it was bad (or only if it was good, if the problem is to find the 

treatment with the earliest time-to-event). 

Samuel Håkansson 

Machine learning and big data for personalized epilepsy treatment 

FUTURE PERSPECTIVES 

The underlying cause of epilepsy is heterogeneous among patients, and is 
complex to understand, which makes the disease process itself difficult to 
target when developing ASMs [100]. Prognostic models from e.g. the 
SANAD studies show that EEG and brain imaging, among other clinical 
measures, are informative when predicting the outcome after a first seizure or 
an epilepsy diagnosis. However, the precision of EEG and brain imaging has 
shown to be insufficient for use in drug development [101]. Cellular and 
molecular biomarkers such as RNA, microRNA, protein, and metabolites 
extracted from blood [102] and cerebrospinal fluid [103] could be used to 
understand and predict the outcome of treatment [104]. Gathering data on 
biological biomarkers and the outcome of ASMs and using machine learning 
to predict a suitable treatment would further help to decrease the number of 
patients with drug-resistant epilepsy. 

In a study using electronic health records from the US, the identification of 
patients with epilepsy was performed with ICD codes, ASMs, age, sex, and 
text features derived from doctors’ notes [105]. The model had a very high 
accuracy, misclassifying only 1.46% of the test cases. While age and sex did 
not increase the accuracy, using text features did. Thus, using doctors’ notes 
in addition to the ICD codes and ASMs could help identify patients with 
epilepsy and remove patients without. The same technique could also be used 
to better identify the specific type of epilepsy. 

Future research on personalized medicine should be focused on developing 
machine learning techniques and evaluation methods with the clinical setting 
in mind. While this may sound obvious, sometimes it may be tempting to 
model problems by simplifying them to fit an existing algorithm. The 
problem arises when the evaluation is simplified as well, and the resulting 
methodology loses clinical relevance. In addition, validating ML algorithms 
in clinical trials is important to verify the assumptions made in all steps of the 
procedure. 

The methodology discussed in this thesis applies to more areas than selecting 
a medication for epilepsy. It can be used in any setting with similar available 
data and assumptions i.e. users keep the treatment for a duration of time, the 

46 

47 

 
 
 
 
 
 
time corresponds to the outcome of the treatment, and the treatment is only 
stopped if it was bad (or only if it was good, if the problem is to find the 
treatment with the earliest time-to-event). 

Samuel Håkansson 

Machine learning and big data for personalized epilepsy treatment 

FUTURE PERSPECTIVES 

The underlying cause of epilepsy is heterogeneous among patients, and is 

complex to understand, which makes the disease process itself difficult to 

target when developing ASMs [100]. Prognostic models from e.g. the 

SANAD studies show that EEG and brain imaging, among other clinical 

measures, are informative when predicting the outcome after a first seizure or 

an epilepsy diagnosis. However, the precision of EEG and brain imaging has 

shown to be insufficient for use in drug development [101]. Cellular and 

molecular biomarkers such as RNA, microRNA, protein, and metabolites 

extracted from blood [102] and cerebrospinal fluid [103] could be used to 

understand and predict the outcome of treatment [104]. Gathering data on 

biological biomarkers and the outcome of ASMs and using machine learning 

to predict a suitable treatment would further help to decrease the number of 

patients with drug-resistant epilepsy. 

In a study using electronic health records from the US, the identification of 

patients with epilepsy was performed with ICD codes, ASMs, age, sex, and 

text features derived from doctors’ notes [105]. The model had a very high 

accuracy, misclassifying only 1.46% of the test cases. While age and sex did 

not increase the accuracy, using text features did. Thus, using doctors’ notes 

in addition to the ICD codes and ASMs could help identify patients with 

epilepsy and remove patients without. The same technique could also be used 

to better identify the specific type of epilepsy. 

Future research on personalized medicine should be focused on developing 

machine learning techniques and evaluation methods with the clinical setting 

in mind. While this may sound obvious, sometimes it may be tempting to 

model problems by simplifying them to fit an existing algorithm. The 

problem arises when the evaluation is simplified as well, and the resulting 

methodology loses clinical relevance. In addition, validating ML algorithms 

in clinical trials is important to verify the assumptions made in all steps of the 

procedure. 

The methodology discussed in this thesis applies to more areas than selecting 

a medication for epilepsy. It can be used in any setting with similar available 

data and assumptions i.e. users keep the treatment for a duration of time, the 

46 

47 

 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

CONCLUSIONS 

ACKNOWLEDGEMENTS 

This thesis investigated the viability of register data as a data source for 
evaluating and predicting ASM suitability for patients. Using statistical 
methods and machine learning to handle real-world big data, we have shown 
that it is possible to approximate retention and estimate treatment effect of 
ASMs. The machine learning methodology was developed and evaluated 
with a causal inference approach to increase the amount of information 
yielded from the data and improve the chance for clinical application. 

KEY POINTS 

  Register data is an interesting complement to clinical 

studies of ASM outcomes. 

  Treatment gap estimations suggest room for improvement 

in ASM selection.  

  The failure of a first specific ASM could provide 
information about which ASM to try next. 
  Kaplan-Meier retention rates of register data are 

comparable to EpiPick suggestions. 

  Off-label use of ASMs in children in Sweden is common 

but not associated with lower retention. 

  Specialized machine learning algorithms trained on 

register data are likely to provide useful information to 
clinicians, but further methodological development and 
evaluation are necessary. 

The goal of the research was to help patients to become seizure-free faster, 
potentially at all, and could especially aid those with rare syndromes and 
comorbidities. Ultimately, machine learning trained on registers has the 
potential to improve the lives of people living with epilepsy. 

There are many people whom I am thankful for making this journey the 

wonderful and educative adventure it became.  

First, I would like to express my deepest appreciation to Johan Zelano for 

your enthusiasm, guidance, ideas, and for always being available. Thank you 

for encouraging me to pursue experiences abroad. I really could not have 

wished for a better supervisor. 

To my co-supervisor, Aleksej Zelezniak, for your inspiration and for giving 

me advice on both science and career. 

I would also like to express my gratitude to Fredrik Johansson, who helped 

me immensely with questions about causal inference.  

To the Zelano research group and collaborators Rakesh Kumar Banote, 

David Larsson, Markus Karlander, Zamzam Mahamud, Hanna 

Eriksson, Klara Andersson, Sarah Akel, Joakim Strandberg, and Judith 

Klecki, for your help, support and enthusiasm. 

I would also like to thank Seer Medical in Melbourne for an amazing 

internship during my PhD. I am especially grateful to Ewan Nurse and Pip 

Karoly for being my supervisors during the project and to Mark Cook for 

giving me the opportunity to visit. Thank you also to Ashley Reynolds for a 

great collaboration. 

Thanks should also go to Ronny Wickström, for your invaluable 

contributions to the pediatrics project. 

Many thanks also to the Zelezniak research group and Fredrik Johansson’s 

group Healthy AI, and special thanks to Adam Breitholtz for many fruitful 

discussions. 

Last but not least, I would like to thank my friends and family, especially my 

parents Tobias and Lotta, for supporting me no matter what. 

48 

49 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

CONCLUSIONS 

ACKNOWLEDGEMENTS 

This thesis investigated the viability of register data as a data source for 

evaluating and predicting ASM suitability for patients. Using statistical 

methods and machine learning to handle real-world big data, we have shown 

that it is possible to approximate retention and estimate treatment effect of 

ASMs. The machine learning methodology was developed and evaluated 

with a causal inference approach to increase the amount of information 

yielded from the data and improve the chance for clinical application. 

KEY POINTS 

  Register data is an interesting complement to clinical 

studies of ASM outcomes. 

  Treatment gap estimations suggest room for improvement 

in ASM selection.  

  The failure of a first specific ASM could provide 

information about which ASM to try next. 

  Kaplan-Meier retention rates of register data are 

comparable to EpiPick suggestions. 

  Off-label use of ASMs in children in Sweden is common 

but not associated with lower retention. 

  Specialized machine learning algorithms trained on 

register data are likely to provide useful information to 

clinicians, but further methodological development and 

evaluation are necessary. 

The goal of the research was to help patients to become seizure-free faster, 

potentially at all, and could especially aid those with rare syndromes and 

comorbidities. Ultimately, machine learning trained on registers has the 

potential to improve the lives of people living with epilepsy. 

There are many people whom I am thankful for making this journey the 
wonderful and educative adventure it became.  

First, I would like to express my deepest appreciation to Johan Zelano for 
your enthusiasm, guidance, ideas, and for always being available. Thank you 
for encouraging me to pursue experiences abroad. I really could not have 
wished for a better supervisor. 

To my co-supervisor, Aleksej Zelezniak, for your inspiration and for giving 
me advice on both science and career. 

I would also like to express my gratitude to Fredrik Johansson, who helped 
me immensely with questions about causal inference.  

To the Zelano research group and collaborators Rakesh Kumar Banote, 
David Larsson, Markus Karlander, Zamzam Mahamud, Hanna 
Eriksson, Klara Andersson, Sarah Akel, Joakim Strandberg, and Judith 
Klecki, for your help, support and enthusiasm. 

I would also like to thank Seer Medical in Melbourne for an amazing 
internship during my PhD. I am especially grateful to Ewan Nurse and Pip 
Karoly for being my supervisors during the project and to Mark Cook for 
giving me the opportunity to visit. Thank you also to Ashley Reynolds for a 
great collaboration. 

Thanks should also go to Ronny Wickström, for your invaluable 
contributions to the pediatrics project. 

Many thanks also to the Zelezniak research group and Fredrik Johansson’s 
group Healthy AI, and special thanks to Adam Breitholtz for many fruitful 
discussions. 

Last but not least, I would like to thank my friends and family, especially my 
parents Tobias and Lotta, for supporting me no matter what. 

48 

49 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

REFERENCES 

1. 

2. 

3. 

4. 

5. 

6. 

7. 

8. 

9. 

10. 

11. 

12. 

Fisher, R.S., et al., Epileptic seizures and epilepsy: definitions 
proposed by the International League Against Epilepsy (ILAE) and 
the International Bureau for Epilepsy (IBE). Epilepsia, 2005. 46(4): 
p. 470-2. 
Chen, Z., et al., Treatment Outcomes in Patients With Newly 
Diagnosed Epilepsy Treated With Established and New Antiepileptic 
Drugs: A 30-Year Longitudinal Cohort Study. JAMA Neurol, 2018. 
75(3): p. 279-286. 
Begley, C., et al., The global cost of epilepsy: A systematic review 
and extrapolation. Epilepsia, 2022. 63(4): p. 892-903. 
Begley, C.E., et al., Estimating the cost of epilepsy. Epilepsia, 1999. 
40 Suppl 8: p. 8-13. 
Gilliam, F., et al., Patient-validated content of epilepsy-specific 
quality-of-life measurement. Epilepsia, 1997. 38(2): p. 233-6. 
Reeves, A.L., et al., Factors associated with work outcome after 
anterior temporal lobectomy for intractable epilepsy. Epilepsia, 
1997. 38(6): p. 689-95. 
Sultana, B., et al., Incidence and Prevalence of Drug-Resistant 
Epilepsy: A Systematic Review and Meta-analysis. Neurology, 2021. 
96(17): p. 805-817. 
Fisher, R.S., et al., ILAE official report: a practical clinical definition 
of epilepsy. Epilepsia, 2014. 55(4): p. 475-82. 
Fisher, R.S., et al., Operational classification of seizure types by the 
International League Against Epilepsy: Position Paper of the ILAE 
Commission for Classification and Terminology. Epilepsia, 2017. 
58(4): p. 522-530. 
Scheffer, I.E., et al., ILAE classification of the epilepsies: Position 
paper of the ILAE Commission for Classification and Terminology. 
Epilepsia, 2017. 58(4): p. 512-521. 
Loscher, W. and P. Klein, The Pharmacology and Clinical Efficacy 
of Antiseizure Medications: From Bromide Salts to Cenobamate and 
Beyond. CNS Drugs, 2021. 35(9): p. 935-963. 
Kanner, A.M. and M.M. Bicchi, Antiseizure Medications for Adults 
With Epilepsy: A Review. JAMA, 2022. 327(13): p. 1269-1281. 

13.  Wirrell, E.C., Epilepsy-related injuries. Epilepsia, 2006. 47 Suppl 1: 

p. 79-86. 

14.  Willems, L.M., et al., Incidence, Risk Factors and Consequences of 

Epilepsy-Related Injuries and Accidents: A Retrospective, Single 
Center Study. Front Neurol, 2018. 9: p. 414. 

15. 

Kwan, P., et al., Definition of drug resistant epilepsy: consensus 

proposal by the ad hoc Task Force of the ILAE Commission on 

Therapeutic Strategies. Epilepsia, 2010. 51(6): p. 1069-77. 

16. 

Sperling, M.R., The consequences of uncontrolled epilepsy. CNS 

Spectr, 2004. 9(2): p. 98-101, 106-9. 

17. 

Glauser, T., et al., ILAE treatment guidelines: evidence-based 

analysis of antiepileptic drug efficacy and effectiveness as initial 

monotherapy for epileptic seizures and syndromes. Epilepsia, 2006. 

47(7): p. 1094-120. 

18. 

Gaitatzis, A. and J.W. Sander, The long-term safety of antiepileptic 

drugs. CNS Drugs, 2013. 27(6): p. 435-55. 

19. 

Zaccara, G., S. Lattanzi, and F. Brigo, Cardiac adverse effects of 

antiseizure medications. Expert Opin Drug Saf, 2022. 21(5): p. 641-

652. 

33. 

20.  Meador, K.J., et al., Cognitive Function at 3 Years of Age after Fetal 

Exposure to Antiepileptic Drugs. New England Journal of Medicine, 

2009. 360(16): p. 1597-1605. 

21. 

Bromfield, E.B., et al., Valproate teratogenicity and epilepsy 

syndrome. Epilepsia, 2008. 49(12): p. 2122-4. 

22. 

Jentink, J., et al., Valproic acid monotherapy in pregnancy and major 

congenital malformations. N Engl J Med, 2010. 362(23): p. 2185-93. 

23. 

Chen, P., et al., Carbamazepine-induced toxic effects and HLA-

B*1502 screening in Taiwan. N Engl J Med, 2011. 364(12): p. 1126-

24. 

Perucca, P. and F.G. Gilliam, Adverse effects of antiepileptic drugs. 

Lancet Neurol, 2012. 11(9): p. 792-802. 

25. 

Fishman, J., et al., Antiepileptic Drug Titration and Related Health 

Care Resource Use and Costs. J Manag Care Spec Pharm, 2018. 

24(9): p. 929-938. 

26. 

Jobst, B.C. and G.D. Cascino, Resective epilepsy surgery for drug-

resistant focal epilepsy: a review. JAMA, 2015. 313(3): p. 285-93. 

27. 

Shan, M., et al., Vagus Nerve Stimulation for Drug Resistant 

Epilepsy: Clinical Outcome, Adverse Events, and Potential 

Prognostic Factors in a Single Center Experience. J Clin Med, 2022. 

28. 

Elia, M., et al., Ketogenic Diets in the Treatment of Epilepsy. Curr 

Pharm Des, 2017. 23(37): p. 5691-5701. 

29. 

Dwivedi, R., et al., Anti-seizure medications and quality of life in 

person with epilepsy. Heliyon, 2022. 8(10): p. e11073. 

30. 

Ben-Menachem, E., et al., Measuring outcomes of treatment with 

antiepileptic drugs in clinical trials. Epilepsy Behav, 2010. 18(1-2): 

11(24). 

p. 24-30. 

50 

51 

 
REFERENCES 

3. 

4. 

5. 

6. 

8. 

9. 

1. 

Fisher, R.S., et al., Epileptic seizures and epilepsy: definitions 

proposed by the International League Against Epilepsy (ILAE) and 

the International Bureau for Epilepsy (IBE). Epilepsia, 2005. 46(4): 

p. 470-2. 

2. 

Chen, Z., et al., Treatment Outcomes in Patients With Newly 

Diagnosed Epilepsy Treated With Established and New Antiepileptic 

Drugs: A 30-Year Longitudinal Cohort Study. JAMA Neurol, 2018. 

75(3): p. 279-286. 

Begley, C., et al., The global cost of epilepsy: A systematic review 

and extrapolation. Epilepsia, 2022. 63(4): p. 892-903. 

Begley, C.E., et al., Estimating the cost of epilepsy. Epilepsia, 1999. 

40 Suppl 8: p. 8-13. 

Gilliam, F., et al., Patient-validated content of epilepsy-specific 

quality-of-life measurement. Epilepsia, 1997. 38(2): p. 233-6. 

Reeves, A.L., et al., Factors associated with work outcome after 

anterior temporal lobectomy for intractable epilepsy. Epilepsia, 

1997. 38(6): p. 689-95. 

7. 

Sultana, B., et al., Incidence and Prevalence of Drug-Resistant 

Epilepsy: A Systematic Review and Meta-analysis. Neurology, 2021. 

96(17): p. 805-817. 

Fisher, R.S., et al., ILAE official report: a practical clinical definition 

of epilepsy. Epilepsia, 2014. 55(4): p. 475-82. 

Fisher, R.S., et al., Operational classification of seizure types by the 

International League Against Epilepsy: Position Paper of the ILAE 

Commission for Classification and Terminology. Epilepsia, 2017. 

58(4): p. 522-530. 

10. 

Scheffer, I.E., et al., ILAE classification of the epilepsies: Position 

paper of the ILAE Commission for Classification and Terminology. 

Epilepsia, 2017. 58(4): p. 512-521. 

11. 

Loscher, W. and P. Klein, The Pharmacology and Clinical Efficacy 

of Antiseizure Medications: From Bromide Salts to Cenobamate and 

Beyond. CNS Drugs, 2021. 35(9): p. 935-963. 

12. 

Kanner, A.M. and M.M. Bicchi, Antiseizure Medications for Adults 

With Epilepsy: A Review. JAMA, 2022. 327(13): p. 1269-1281. 

13.  Wirrell, E.C., Epilepsy-related injuries. Epilepsia, 2006. 47 Suppl 1: 

p. 79-86. 

14.  Willems, L.M., et al., Incidence, Risk Factors and Consequences of 

Epilepsy-Related Injuries and Accidents: A Retrospective, Single 

Center Study. Front Neurol, 2018. 9: p. 414. 

Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

15. 

16. 

17. 

18. 

19. 

Kwan, P., et al., Definition of drug resistant epilepsy: consensus 
proposal by the ad hoc Task Force of the ILAE Commission on 
Therapeutic Strategies. Epilepsia, 2010. 51(6): p. 1069-77. 
Sperling, M.R., The consequences of uncontrolled epilepsy. CNS 
Spectr, 2004. 9(2): p. 98-101, 106-9. 
Glauser, T., et al., ILAE treatment guidelines: evidence-based 
analysis of antiepileptic drug efficacy and effectiveness as initial 
monotherapy for epileptic seizures and syndromes. Epilepsia, 2006. 
47(7): p. 1094-120. 
Gaitatzis, A. and J.W. Sander, The long-term safety of antiepileptic 
drugs. CNS Drugs, 2013. 27(6): p. 435-55. 
Zaccara, G., S. Lattanzi, and F. Brigo, Cardiac adverse effects of 
antiseizure medications. Expert Opin Drug Saf, 2022. 21(5): p. 641-
652. 

21. 

22. 

25. 

24. 

23. 

20.  Meador, K.J., et al., Cognitive Function at 3 Years of Age after Fetal 
Exposure to Antiepileptic Drugs. New England Journal of Medicine, 
2009. 360(16): p. 1597-1605. 
Bromfield, E.B., et al., Valproate teratogenicity and epilepsy 
syndrome. Epilepsia, 2008. 49(12): p. 2122-4. 
Jentink, J., et al., Valproic acid monotherapy in pregnancy and major 
congenital malformations. N Engl J Med, 2010. 362(23): p. 2185-93. 
Chen, P., et al., Carbamazepine-induced toxic effects and HLA-
B*1502 screening in Taiwan. N Engl J Med, 2011. 364(12): p. 1126-
33. 
Perucca, P. and F.G. Gilliam, Adverse effects of antiepileptic drugs. 
Lancet Neurol, 2012. 11(9): p. 792-802. 
Fishman, J., et al., Antiepileptic Drug Titration and Related Health 
Care Resource Use and Costs. J Manag Care Spec Pharm, 2018. 
24(9): p. 929-938. 
Jobst, B.C. and G.D. Cascino, Resective epilepsy surgery for drug-
resistant focal epilepsy: a review. JAMA, 2015. 313(3): p. 285-93. 
Shan, M., et al., Vagus Nerve Stimulation for Drug Resistant 
Epilepsy: Clinical Outcome, Adverse Events, and Potential 
Prognostic Factors in a Single Center Experience. J Clin Med, 2022. 
11(24). 
Elia, M., et al., Ketogenic Diets in the Treatment of Epilepsy. Curr 
Pharm Des, 2017. 23(37): p. 5691-5701. 
Dwivedi, R., et al., Anti-seizure medications and quality of life in 
person with epilepsy. Heliyon, 2022. 8(10): p. e11073. 
Ben-Menachem, E., et al., Measuring outcomes of treatment with 
antiepileptic drugs in clinical trials. Epilepsy Behav, 2010. 18(1-2): 
p. 24-30. 

30. 

28. 

26. 

27. 

29. 

50 

51 

 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

34. 

33. 

35. 

31. 

32. 

Guideline on clinical investigation of medicinal products in the 
treatment of epileptic disorders. CHMP/EWP/566/98/Rev. 2. January 
2010. European Medicines Agency (EMEA), Committee for 
Medicinal Products for Human Use (CHMP). 
Chadwick, D. and T. Marson, Choosing a first drug treatment for 
epilepsy after SANAD: randomized controlled trials, systematic 
reviews, guidelines and treating patients. Epilepsia, 2007. 48(7): p. 
1259-63. 
Perucca, E. and S. Wiebe, Not all that glitters is gold: A guide to the 
critical interpretation of drug trials in epilepsy. Epilepsia Open, 
2016. 1(1-2): p. 9-21. 
Perucca, E., From clinical trials of antiepileptic drugs to treatment. 
Epilepsia Open, 2018. 3(Suppl Suppl 2): p. 220-230. 
Kwan, P., et al., Efficacy and safety of pregabalin versus lamotrigine 
in patients with newly diagnosed partial seizures: a phase 3, double-
blind, randomised, parallel-group trial. Lancet Neurol, 2011. 10(10): 
p. 881-90. 
Perucca, E. and T. Tomson, Monotherapy trials with the new 
antiepileptic drugs: study designs, practical relevance and ethical 
implications. Epilepsy Res, 1999. 33(2-3): p. 247-62. 
Perucca, E., What clinical trial designs have been used to test 
antiepileptic drugs and do we need to change them? Epileptic 
Disord, 2012. 14(2): p. 124-31. 
Perucca, E., Designing clinical trials to assess antiepileptic drugs as 
monotherapy : difficulties and solutions. CNS Drugs, 2008. 22(11): 
p. 917-38. 
Perucca, E. and T. Tomson, The pharmacological treatment of 
epilepsy in adults. Lancet Neurol, 2011. 10(5): p. 446-56. 
Rheims, S., et al., Factors determining response to antiepileptic 
drugs in randomized controlled trials. A systematic review and meta-
analysis. Epilepsia, 2011. 52(2): p. 219-33. 
Glauser, T., et al., Updated ILAE evidence review of antiepileptic 
drug efficacy and effectiveness as initial monotherapy for epileptic 
seizures and syndromes. Epilepsia, 2013. 54(3): p. 551-63. 
42.  Marson, A.G., et al., The SANAD study of effectiveness of 

41. 

37. 

40. 

36. 

39. 

38. 

carbamazepine, gabapentin, lamotrigine, oxcarbazepine, or 
topiramate for treatment of partial epilepsy: an unblinded 
randomised controlled trial. Lancet, 2007. 369(9566): p. 1000-15. 

43.  Marson, A., et al., The SANAD II study of the effectiveness and cost-
effectiveness of levetiracetam, zonisamide, or lamotrigine for newly 
diagnosed focal epilepsy: an open-label, non-inferiority, multicentre, 
phase 4, randomised controlled trial. Lancet, 2021. 397(10282): p. 
1363-1374. 

52 

53 

44. 

Franco, V., J.A. French, and E. Perucca, Challenges in the clinical 

development of new antiepileptic drugs. Pharmacol Res, 2016. 103: 

p. 95-104. 

45.  Mintzer, S., et al., Is a separate monotherapy indication warranted 

for antiepileptic drugs? Lancet Neurol, 2015. 14(12): p. 1229-40. 

46. 

Beydoun, A. and E. Kutluay, Conversion to monotherapy: clinical 

trials in patients with refractory partial seizures. Neurology, 2003. 

60(11 Suppl 4): p. S13-25. 

47. 

Friedman, D. and J.A. French, Clinical trials for therapeutic 

assessment of antiepileptic drugs in the 21st century: obstacles and 

solutions. Lancet Neurol, 2012. 11(9): p. 827-34. 

48. 

Chadwick, D. and M. Privitera, Placebo-controlled studies in 

neurology: where do they stop? Neurology, 1999. 52(4): p. 682-5. 

49. 

Ryvlin, P., M. Cucherat, and S. Rheims, Risk of sudden unexpected 

death in epilepsy in patients given adjunctive antiepileptic treatment 

for refractory seizures: a meta-analysis of placebo-controlled 

randomised trials. The Lancet Neurology, 2011. 10(11): p. 961-968. 

50. 

Landmark, C.J., et al., Prescription patterns of antiepileptic drugs in 

patients with epilepsy in a nation-wide population. Epilepsy Res, 

2011. 95(1-2): p. 51-9. 

51. 

Artama, M., et al., Nationwide register-based surveillance system on 

drugs and pregnancy in Finland 1996-2006. Pharmacoepidemiol 

Drug Saf, 2011. 20(7): p. 729-38. 

52. 

Kaae, J., et al., Epilepsy, anti-epileptic medication use and risk of 

cancer. Int J Cancer, 2014. 134(4): p. 932-8. 

53. 

Hochbaum, M., et al., Trends in antiseizure medication prescription 

patterns among all adults, women, and older adults with epilepsy: A 

German longitudinal analysis from 2008 to 2020. Epilepsy Behav, 

54. 

Heger, K., et al., Changes in the use of antiseizure medications in 

children and adolescents in Norway, 2009-2018. Epilepsy Res, 2022. 

2022. 130: p. 108666. 

181: p. 106872. 

55. 

Sundelin, H.E.K., et al., Epilepsy, antiepileptic drugs, and serious 

transport accidents: A nationwide cohort study. Neurology, 2018. 

90(13): p. e1111-e1118. 

56. 

Bjork, M.H., et al., Association of Prenatal Exposure to Antiseizure 

Medication With Risk of Autism and Intellectual Disability. JAMA 

Neurol, 2022. 79(7): p. 672-681. 

57.  Moore, T.J., et al., Estimated Costs of Pivotal Trials for Novel 

Therapeutic Agents Approved by the US Food and Drug 

Administration, 2015-2016. JAMA Intern Med, 2018. 178(11): p. 

1451-1457. 

Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

31. 

Guideline on clinical investigation of medicinal products in the 

treatment of epileptic disorders. CHMP/EWP/566/98/Rev. 2. January 

2010. European Medicines Agency (EMEA), Committee for 

Medicinal Products for Human Use (CHMP). 

32. 

Chadwick, D. and T. Marson, Choosing a first drug treatment for 

epilepsy after SANAD: randomized controlled trials, systematic 

reviews, guidelines and treating patients. Epilepsia, 2007. 48(7): p. 

33. 

Perucca, E. and S. Wiebe, Not all that glitters is gold: A guide to the 

critical interpretation of drug trials in epilepsy. Epilepsia Open, 

1259-63. 

2016. 1(1-2): p. 9-21. 

34. 

Perucca, E., From clinical trials of antiepileptic drugs to treatment. 

Epilepsia Open, 2018. 3(Suppl Suppl 2): p. 220-230. 

35. 

Kwan, P., et al., Efficacy and safety of pregabalin versus lamotrigine 

in patients with newly diagnosed partial seizures: a phase 3, double-

blind, randomised, parallel-group trial. Lancet Neurol, 2011. 10(10): 

p. 881-90. 

36. 

Perucca, E. and T. Tomson, Monotherapy trials with the new 

antiepileptic drugs: study designs, practical relevance and ethical 

implications. Epilepsy Res, 1999. 33(2-3): p. 247-62. 

37. 

Perucca, E., What clinical trial designs have been used to test 

antiepileptic drugs and do we need to change them? Epileptic 

Disord, 2012. 14(2): p. 124-31. 

38. 

Perucca, E., Designing clinical trials to assess antiepileptic drugs as 

monotherapy : difficulties and solutions. CNS Drugs, 2008. 22(11): 

p. 917-38. 

39. 

Perucca, E. and T. Tomson, The pharmacological treatment of 

epilepsy in adults. Lancet Neurol, 2011. 10(5): p. 446-56. 

40. 

Rheims, S., et al., Factors determining response to antiepileptic 

drugs in randomized controlled trials. A systematic review and meta-

analysis. Epilepsia, 2011. 52(2): p. 219-33. 

41. 

Glauser, T., et al., Updated ILAE evidence review of antiepileptic 

drug efficacy and effectiveness as initial monotherapy for epileptic 

seizures and syndromes. Epilepsia, 2013. 54(3): p. 551-63. 

42.  Marson, A.G., et al., The SANAD study of effectiveness of 

carbamazepine, gabapentin, lamotrigine, oxcarbazepine, or 

topiramate for treatment of partial epilepsy: an unblinded 

randomised controlled trial. Lancet, 2007. 369(9566): p. 1000-15. 

43.  Marson, A., et al., The SANAD II study of the effectiveness and cost-

effectiveness of levetiracetam, zonisamide, or lamotrigine for newly 

diagnosed focal epilepsy: an open-label, non-inferiority, multicentre, 

phase 4, randomised controlled trial. Lancet, 2021. 397(10282): p. 

1363-1374. 

44. 

Franco, V., J.A. French, and E. Perucca, Challenges in the clinical 
development of new antiepileptic drugs. Pharmacol Res, 2016. 103: 
p. 95-104. 

45.  Mintzer, S., et al., Is a separate monotherapy indication warranted 

46. 

47. 

48. 

49. 

50. 

51. 

52. 

53. 

54. 

55. 

56. 

for antiepileptic drugs? Lancet Neurol, 2015. 14(12): p. 1229-40. 
Beydoun, A. and E. Kutluay, Conversion to monotherapy: clinical 
trials in patients with refractory partial seizures. Neurology, 2003. 
60(11 Suppl 4): p. S13-25. 
Friedman, D. and J.A. French, Clinical trials for therapeutic 
assessment of antiepileptic drugs in the 21st century: obstacles and 
solutions. Lancet Neurol, 2012. 11(9): p. 827-34. 
Chadwick, D. and M. Privitera, Placebo-controlled studies in 
neurology: where do they stop? Neurology, 1999. 52(4): p. 682-5. 
Ryvlin, P., M. Cucherat, and S. Rheims, Risk of sudden unexpected 
death in epilepsy in patients given adjunctive antiepileptic treatment 
for refractory seizures: a meta-analysis of placebo-controlled 
randomised trials. The Lancet Neurology, 2011. 10(11): p. 961-968. 
Landmark, C.J., et al., Prescription patterns of antiepileptic drugs in 
patients with epilepsy in a nation-wide population. Epilepsy Res, 
2011. 95(1-2): p. 51-9. 
Artama, M., et al., Nationwide register-based surveillance system on 
drugs and pregnancy in Finland 1996-2006. Pharmacoepidemiol 
Drug Saf, 2011. 20(7): p. 729-38. 
Kaae, J., et al., Epilepsy, anti-epileptic medication use and risk of 
cancer. Int J Cancer, 2014. 134(4): p. 932-8. 
Hochbaum, M., et al., Trends in antiseizure medication prescription 
patterns among all adults, women, and older adults with epilepsy: A 
German longitudinal analysis from 2008 to 2020. Epilepsy Behav, 
2022. 130: p. 108666. 
Heger, K., et al., Changes in the use of antiseizure medications in 
children and adolescents in Norway, 2009-2018. Epilepsy Res, 2022. 
181: p. 106872. 
Sundelin, H.E.K., et al., Epilepsy, antiepileptic drugs, and serious 
transport accidents: A nationwide cohort study. Neurology, 2018. 
90(13): p. e1111-e1118. 
Bjork, M.H., et al., Association of Prenatal Exposure to Antiseizure 
Medication With Risk of Autism and Intellectual Disability. JAMA 
Neurol, 2022. 79(7): p. 672-681. 

57.  Moore, T.J., et al., Estimated Costs of Pivotal Trials for Novel 
Therapeutic Agents Approved by the US Food and Drug 
Administration, 2015-2016. JAMA Intern Med, 2018. 178(11): p. 
1451-1457. 

52 

53 

Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

63. 

62. 

61. 

60. 

59. 

58.  Winship, C. and S.L. Morgan, The estimation of causal effects from 
observational data. Annual Review of Sociology, 1999. 25: p. 659-
706. 
Rosenbaum, P.R. and D.B. Rubin, The Central Role of the 
Propensity Score in Observational Studies for Causal Effects. 
Biometrika, 1983. 70(1): p. 41-55. 
Frohlich, H., et al., From hype to reality: data science enabling 
personalized medicine. BMC Med, 2018. 16(1): p. 150. 
Precup, D., R.S. Sutton, and S.P. Singh, Eligibility Traces for Off-
Policy Policy Evaluation, in Proceedings of the Seventeenth 
International Conference on Machine Learning. 2000, Morgan 
Kaufmann Publishers Inc. p. 759–766. 
Schölkopf, B., et al., On causal and anticausal learning, in 
Proceedings of the 29th International Coference on International 
Conference on Machine Learning. 2012, Omnipress: Edinburgh, 
Scotland. p. 459–466. 
Cendes, F. and C.R. McDonald, Artificial Intelligence Applications 
in the Imaging of Epilepsy and Its Comorbidities: Present and 
Future. Epilepsy Curr, 2022. 22(2): p. 91-96. 
Rasheed, K., et al., Machine Learning for Predicting Epileptic 
Seizures Using EEG Signals: A Review. IEEE Reviews in 
Biomedical Engineering, 2021. 14: p. 139-155. 
Stirling, R.E., et al., Seizure forecasting and cyclic control of 
seizures. Epilepsia, 2021. 62 Suppl 1: p. S2-S14. 
Dian, J.A., et al., Identification of brain regions of interest for 
epilepsy surgery planning using support vector machines. Annu Int 
Conf IEEE Eng Med Biol Soc, 2015. 2015: p. 6590-3. 
Ludvigsson, J.F., et al., External review and validation of the 
Swedish national inpatient register. BMC Public Health, 2011. 11: p. 
450. 
Sveinsson, O., et al., The incidence of SUDEP: A nationwide 
population-based cohort study. Neurology, 2017. 89(2): p. 170-177. 
Koster, M., et al., Refinement of Swedish administrative registers to 
monitor stroke events on the national level. Neuroepidemiology, 
2013. 40(4): p. 240-6. 

69. 

67. 

68. 

64. 

66. 

65. 

70.  Murley, C., et al., Validation of multiple sclerosis diagnoses in the 

71. 

Swedish National Patient Register. Eur J Epidemiol, 2019. 34(12): p. 
1161-1169. 
Tampe, U., et al., Diagnosis of Open Tibial Fracture Showed High 
Positive Predictive Value in the Swedish National Patient Register. 
Clin Epidemiol, 2020. 12: p. 1113-1119. 

54 

55 

72. 

Rizzuto, D., et al., Detection of Dementia Cases in Two Swedish 

Health Registers: A Validation Study. J Alzheimers Dis, 2018. 61(4): 

p. 1301-1310. 

73. 

Tettamanti, G., et al., Central nervous system tumor registration in 

the Swedish Cancer Register and Inpatient Register between 1990 

and 2014. Clin Epidemiol, 2019. 11: p. 81-92. 

74.  Wettermark, B., et al., The new Swedish Prescribed Drug Register--

opportunities for pharmacoepidemiological research and experience 

from the first six months. Pharmacoepidemiol Drug Saf, 2007. 16(7): 

75. 

Ohlin, M. and P. Otterdal, Det statistiska registrets framställning och 

p. 726-35. 

kvalitet. 2021. 

76. 

Hakansson, S., et al., Potential for improved retention rate by 

personalized antiseizure medication selection: A register-based 

analysis. Epilepsia, 2021. 62(9): p. 2123-2132. 

77. 

Asadi-Pooya, A.A., et al., The EpiPick algorithm to select 

appropriate antiseizure medications in patients with epilepsy: 

Validation studies and updates. Epilepsia, 2022. 63(1): p. 254-255. 

78. 

Hakansson, S. and J. Zelano, Big data analysis of ASM retention 

rates and expert ASM algorithm: A comparative study. Epilepsia, 

2022. 

79. 

Perucca, E., Antiepileptic drugs: evolution of our knowledge and 

changes in drug trials. Epileptic Disord, 2019. 21(4): p. 319-329. 

80. 

Karlsson Lind, L., et al., Utilization of Antiepileptic Medicines in 

Swedish Children and Adolescents with Different Diagnoses. Basic 

Clin Pharmacol Toxicol, 2018. 123(1): p. 94-100. 

81. 

Chapfuwa, P., et al., Enabling counterfactual survival analysis with 

balanced representations, in Proceedings of the Conference on 

Health, Inference, and Learning. 2021, Association for Computing 

Machinery: Virtual Event, USA. p. 133–145. 

82.  Muskan Gupta, G.K., Ranjitha Prasad,  Garima Gupta, Learn to Live 

Longer: Counterfactual Inference using Balanced Representations 

for Parametric Deep Survival Analysis. 2022. 

83. 

Leete, O.E., et al., Balanced policy evaluation and learning for right 

censored data. arXiv preprint arXiv:1911.05728, 2019. 

84. 

Olaciregui-Dague, K., et al., Anti-seizure efficacy and retention rate 

of carbamazepine is highly variable in randomized controlled trials: 

A meta-analysis. Epilepsia Open, 2022. 7(4): p. 556-569. 

85. 

Nevitt, S.J., et al., Antiepileptic drug monotherapy for epilepsy: a 

network meta-analysis of individual participant data. Cochrane 

Database Syst Rev, 2022. 4(4): p. CD011412. 

86. 

Chen, S., et al., Adherence to and persistence with lacosamide, 

perampanel, lamotrigine, and levetiracetam in adult patients with 

Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

58.  Winship, C. and S.L. Morgan, The estimation of causal effects from 

observational data. Annual Review of Sociology, 1999. 25: p. 659-

706. 

59. 

Rosenbaum, P.R. and D.B. Rubin, The Central Role of the 

Propensity Score in Observational Studies for Causal Effects. 

Biometrika, 1983. 70(1): p. 41-55. 

60. 

Frohlich, H., et al., From hype to reality: data science enabling 

personalized medicine. BMC Med, 2018. 16(1): p. 150. 

61. 

Precup, D., R.S. Sutton, and S.P. Singh, Eligibility Traces for Off-

Policy Policy Evaluation, in Proceedings of the Seventeenth 

International Conference on Machine Learning. 2000, Morgan 

Kaufmann Publishers Inc. p. 759–766. 

62. 

Schölkopf, B., et al., On causal and anticausal learning, in 

Proceedings of the 29th International Coference on International 

Conference on Machine Learning. 2012, Omnipress: Edinburgh, 

Scotland. p. 459–466. 

63. 

Cendes, F. and C.R. McDonald, Artificial Intelligence Applications 

in the Imaging of Epilepsy and Its Comorbidities: Present and 

Future. Epilepsy Curr, 2022. 22(2): p. 91-96. 

64. 

Rasheed, K., et al., Machine Learning for Predicting Epileptic 

Seizures Using EEG Signals: A Review. IEEE Reviews in 

Biomedical Engineering, 2021. 14: p. 139-155. 

65. 

Stirling, R.E., et al., Seizure forecasting and cyclic control of 

seizures. Epilepsia, 2021. 62 Suppl 1: p. S2-S14. 

66. 

Dian, J.A., et al., Identification of brain regions of interest for 

epilepsy surgery planning using support vector machines. Annu Int 

Conf IEEE Eng Med Biol Soc, 2015. 2015: p. 6590-3. 

67. 

Ludvigsson, J.F., et al., External review and validation of the 

Swedish national inpatient register. BMC Public Health, 2011. 11: p. 

450. 

68. 

Sveinsson, O., et al., The incidence of SUDEP: A nationwide 

population-based cohort study. Neurology, 2017. 89(2): p. 170-177. 

69. 

Koster, M., et al., Refinement of Swedish administrative registers to 

monitor stroke events on the national level. Neuroepidemiology, 

70.  Murley, C., et al., Validation of multiple sclerosis diagnoses in the 

Swedish National Patient Register. Eur J Epidemiol, 2019. 34(12): p. 

2013. 40(4): p. 240-6. 

1161-1169. 

71. 

Tampe, U., et al., Diagnosis of Open Tibial Fracture Showed High 

Positive Predictive Value in the Swedish National Patient Register. 

Clin Epidemiol, 2020. 12: p. 1113-1119. 

72. 

73. 

Rizzuto, D., et al., Detection of Dementia Cases in Two Swedish 
Health Registers: A Validation Study. J Alzheimers Dis, 2018. 61(4): 
p. 1301-1310. 
Tettamanti, G., et al., Central nervous system tumor registration in 
the Swedish Cancer Register and Inpatient Register between 1990 
and 2014. Clin Epidemiol, 2019. 11: p. 81-92. 

74.  Wettermark, B., et al., The new Swedish Prescribed Drug Register--

75. 

76. 

77. 

78. 

79. 

80. 

81. 

opportunities for pharmacoepidemiological research and experience 
from the first six months. Pharmacoepidemiol Drug Saf, 2007. 16(7): 
p. 726-35. 
Ohlin, M. and P. Otterdal, Det statistiska registrets framställning och 
kvalitet. 2021. 
Hakansson, S., et al., Potential for improved retention rate by 
personalized antiseizure medication selection: A register-based 
analysis. Epilepsia, 2021. 62(9): p. 2123-2132. 
Asadi-Pooya, A.A., et al., The EpiPick algorithm to select 
appropriate antiseizure medications in patients with epilepsy: 
Validation studies and updates. Epilepsia, 2022. 63(1): p. 254-255. 
Hakansson, S. and J. Zelano, Big data analysis of ASM retention 
rates and expert ASM algorithm: A comparative study. Epilepsia, 
2022. 
Perucca, E., Antiepileptic drugs: evolution of our knowledge and 
changes in drug trials. Epileptic Disord, 2019. 21(4): p. 319-329. 
Karlsson Lind, L., et al., Utilization of Antiepileptic Medicines in 
Swedish Children and Adolescents with Different Diagnoses. Basic 
Clin Pharmacol Toxicol, 2018. 123(1): p. 94-100. 
Chapfuwa, P., et al., Enabling counterfactual survival analysis with 
balanced representations, in Proceedings of the Conference on 
Health, Inference, and Learning. 2021, Association for Computing 
Machinery: Virtual Event, USA. p. 133–145. 

82.  Muskan Gupta, G.K., Ranjitha Prasad,  Garima Gupta, Learn to Live 

Longer: Counterfactual Inference using Balanced Representations 
for Parametric Deep Survival Analysis. 2022. 
Leete, O.E., et al., Balanced policy evaluation and learning for right 
censored data. arXiv preprint arXiv:1911.05728, 2019. 
Olaciregui-Dague, K., et al., Anti-seizure efficacy and retention rate 
of carbamazepine is highly variable in randomized controlled trials: 
A meta-analysis. Epilepsia Open, 2022. 7(4): p. 556-569. 
Nevitt, S.J., et al., Antiepileptic drug monotherapy for epilepsy: a 
network meta-analysis of individual participant data. Cochrane 
Database Syst Rev, 2022. 4(4): p. CD011412. 
Chen, S., et al., Adherence to and persistence with lacosamide, 
perampanel, lamotrigine, and levetiracetam in adult patients with 

83. 

84. 

85. 

86. 

54 

55 

Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

87. 

88. 

89. 

90. 

91. 

focal epilepsy in Japan: A descriptive cohort study using a claims 
database. Heliyon, 2023. 9(4): p. e15017. 
Devinsky, O., et al., Changing the approach to treatment choice in 
epilepsy using big data. Epilepsy & Behavior, 2016. 56: p. 32-37. 
Beniczky, S., et al., Optimal choice of antiseizure medication: 
Agreement among experts and validation of a web‐based decision 
support application. Epilepsia, 2020. 
Asadi-Pooya, A.A., et al., A pragmatic algorithm to select 
appropriate antiseizure medications in patients with epilepsy. 
Epilepsia, 2020. 
Nielsen, L.H., et al., Using prescription registries to define 
continuous drug use: how to fill gaps between prescriptions. 
Pharmacoepidemiol Drug Saf, 2008. 17(4): p. 384-8. 
Liu, W., S.J. Kuramoto, and E.A. Stuart, An introduction to 
sensitivity analysis for unobserved confounding in nonexperimental 
prevention research. Prev Sci, 2013. 14(6): p. 570-80. 

92.  Mbizvo, G.K., et al., The accuracy of using administrative healthcare 

post-hoc, subgroup analyses of data from the SANAD trial. Lancet 

Neurol, 2012. 11(4): p. 331-40. 

102.  Banote, R.K., S. Akel, and J. Zelano, Blood biomarkers in epilepsy. 

Acta Neurol Scand, 2022. 146(4): p. 362-368. 

103.  Banote, R.K., et al., CSF biomarkers in patients with epilepsy in 

Alzheimer's disease: a nation-wide study. Brain Commun, 2022. 

4(4): p. fcac210. 

104.  Walker, L.E., et al., Personalized medicine approaches in epilepsy. J 

Intern Med, 2015. 277(2): p. 218-234. 

105. 

Fernandes, M., et al., Identification of patients with epilepsy using 

automated electronic health records phenotyping. Epilepsia, 2023. 

93. 

96. 

95. 

94. 

data to identify epilepsy cases: A systematic review of validation 
studies. Epilepsia, 2020. 61(7): p. 1319-1335. 
Faught, E., et al., Newer antiepileptic drug use and other factors 
decreasing hospital encounters. Epilepsy Behav, 2015. 45: p. 169-75. 
Hakeem, H., et al., Development and Validation of a Deep Learning 
Model for Predicting Treatment Response in Patients With Newly 
Diagnosed Epilepsy. JAMA Neurol, 2022. 79(10): p. 986-996. 
de Jong, J., et al., Towards realizing the vision of precision medicine: 
AI based prediction of clinical drug response. Brain, 2021. 144(6): p. 
1738-1750. 
Yao, L., et al., Prediction of antiepileptic drug treatment outcomes of 
patients with newly diagnosed epilepsy by machine learning. 
Epilepsy Behav, 2019. 96: p. 92-97. 
Zhang, J.H., et al., Personalized prediction model for seizure-free 
epilepsy with levetiracetam therapy: a retrospective data analysis 
using support vector machine. Br J Clin Pharmacol, 2018. 84(11): p. 
2615-2624. 
Colic, S., et al., Prediction of antiepileptic drug treatment outcomes 
using machine learning. J Neural Eng, 2017. 14(1): p. 016002. 
Fernández-Loría, C. and F. Provost, Causal Decision Making and 
Causal Effect Estimation Are Not the Same…and Why It Matters. 
INFORMS Journal on Data Science, 2022. 1(1): p. 4-16. 
100.  Walker, L.E., et al., Personalized medicine approaches in epilepsy. 

98. 

97. 

99. 

Journal of Internal Medicine, 2015. 277(2): p. 218-234. 
101.  Bonnett, L., et al., Prognostic factors for time to treatment failure 

and time to 12 months of remission for patients with focal epilepsy: 

56 

57 

 
Machine learning and big data for personalized epilepsy treatment 

Samuel Håkansson 

post-hoc, subgroup analyses of data from the SANAD trial. Lancet 
Neurol, 2012. 11(4): p. 331-40. 

102.  Banote, R.K., S. Akel, and J. Zelano, Blood biomarkers in epilepsy. 

Acta Neurol Scand, 2022. 146(4): p. 362-368. 

103.  Banote, R.K., et al., CSF biomarkers in patients with epilepsy in 
Alzheimer's disease: a nation-wide study. Brain Commun, 2022. 
4(4): p. fcac210. 

104.  Walker, L.E., et al., Personalized medicine approaches in epilepsy. J 

105. 

Intern Med, 2015. 277(2): p. 218-234. 
Fernandes, M., et al., Identification of patients with epilepsy using 
automated electronic health records phenotyping. Epilepsia, 2023. 

focal epilepsy in Japan: A descriptive cohort study using a claims 

database. Heliyon, 2023. 9(4): p. e15017. 

87. 

Devinsky, O., et al., Changing the approach to treatment choice in 

epilepsy using big data. Epilepsy & Behavior, 2016. 56: p. 32-37. 

88. 

Beniczky, S., et al., Optimal choice of antiseizure medication: 

Agreement among experts and validation of a web‐based decision 

support application. Epilepsia, 2020. 

89. 

Asadi-Pooya, A.A., et al., A pragmatic algorithm to select 

appropriate antiseizure medications in patients with epilepsy. 

Epilepsia, 2020. 

90. 

Nielsen, L.H., et al., Using prescription registries to define 

continuous drug use: how to fill gaps between prescriptions. 

Pharmacoepidemiol Drug Saf, 2008. 17(4): p. 384-8. 

91. 

Liu, W., S.J. Kuramoto, and E.A. Stuart, An introduction to 

sensitivity analysis for unobserved confounding in nonexperimental 

prevention research. Prev Sci, 2013. 14(6): p. 570-80. 

92.  Mbizvo, G.K., et al., The accuracy of using administrative healthcare 

data to identify epilepsy cases: A systematic review of validation 

studies. Epilepsia, 2020. 61(7): p. 1319-1335. 

93. 

Faught, E., et al., Newer antiepileptic drug use and other factors 

decreasing hospital encounters. Epilepsy Behav, 2015. 45: p. 169-75. 

94. 

Hakeem, H., et al., Development and Validation of a Deep Learning 

Model for Predicting Treatment Response in Patients With Newly 

Diagnosed Epilepsy. JAMA Neurol, 2022. 79(10): p. 986-996. 

95. 

de Jong, J., et al., Towards realizing the vision of precision medicine: 

AI based prediction of clinical drug response. Brain, 2021. 144(6): p. 

1738-1750. 

96. 

Yao, L., et al., Prediction of antiepileptic drug treatment outcomes of 

patients with newly diagnosed epilepsy by machine learning. 

Epilepsy Behav, 2019. 96: p. 92-97. 

97. 

Zhang, J.H., et al., Personalized prediction model for seizure-free 

epilepsy with levetiracetam therapy: a retrospective data analysis 

using support vector machine. Br J Clin Pharmacol, 2018. 84(11): p. 

2615-2624. 

98. 

Colic, S., et al., Prediction of antiepileptic drug treatment outcomes 

using machine learning. J Neural Eng, 2017. 14(1): p. 016002. 

99. 

Fernández-Loría, C. and F. Provost, Causal Decision Making and 

Causal Effect Estimation Are Not the Same…and Why It Matters. 

INFORMS Journal on Data Science, 2022. 1(1): p. 4-16. 

100.  Walker, L.E., et al., Personalized medicine approaches in epilepsy. 

Journal of Internal Medicine, 2015. 277(2): p. 218-234. 

101.  Bonnett, L., et al., Prognostic factors for time to treatment failure 

and time to 12 months of remission for patients with focal epilepsy: 

56 

57
