# Vieluf et al. - 2025 - Seizure monitoring by combined diary and wearable data

Received: 20 August 2024 Revised: 27 June 2025

Accepted: 27 June 2025

DOI: 10.1111/epi.18550

RESEARCH ARTICLE

Epilepsia

Seizure monitoring by combined diary and wearable data:
A multicenter, longitudinal, observational study

Solveig Vieluf'>*® | Sasagu Tomioka®’® | Bo Zhang® | Vaishnav Krishnan®
William J. Bosl”® | Todd Grinnell* | Tobias Loddenkemper'

IDivision of Epilepsy and Clinical Neurophysiology, Boston Children's Hospital, Harvard Medical School, Boston, Massachusetts, USA

2Deparlment of Medicine I, Ludwig Maximilian University Hospital, Ludwig Maximilian University Munich, Munich, Germany

*DZHK (German Centre for Cardiovascular Research), partner site, Munich Heart Alliance, Munich, Germany

4Sumitomo Pharma America, Inc., Marlborough, Massachusetts, USA

*Department of Neurology, Boston Children's Hospital, Harvard Medical School, Boston, Massachusetts, USA

°Departments of Neurology, Neuroscience, and Psychiatry & Behavioral Sciences, Baylor College of Medicine, Houston, Texas, USA

"Data Institute, Clinical Neuroinformatics & AI Laboratory, University of San Francisco, San Francisco, California, USA

8Computational Health Informatics Program, Boston Children's Hospital, Harvard Medical School, Boston, Massachusetts, USA

Correspondence

Sasagu Tomioka, Sumitomo Pharma
America, Inc. 84 Waterford Drive,
Marlborough, MA 01752, USA.
Email: sam.tomioka@us.sumitomo-
pharma.com

Funding information
Sumitomo Pharma America, Inc.

(formerly Sunovion Pharmaceuticals
Inc.); American Epilepsy Society,
Grant/Award Number: 932267;
Epilepsy Reserach Fund

Abstract

Objective: In patients with intractable epilepsy, accurate diaries of seizure occur-
rence and timing can substantially inform management. Wearable devices that
provide confirmation of seizure occurrence complement such diaries, which are
frequently incomplete and/or inaccurate. Here, we combined seizure diaries and
longitudinally deployed wrist-worn device recordings to evaluate whether wear-
able recordings contain information that can discriminate between days contain-
ing seizure-related activity and those without.

Methods: Patients with focal seizures were prospectively enrolled in a clinical trial
to test the effectiveness of eslicarbazepine acetate as an adjunct to levetiracetam
or lamotrigine (phase IV clinical trial NCT03116828). One hundred two patients
maintained a seizure diary and wore a biosensor for >30weeks. Based on diaries,
we labeled days as either “seizure” versus “no-seizure” or “preseizure” versus “no-
preseizure.” We compared patterns obtained by harmonic 24-h modeling between
conditions. Best-ranking wearable markers and seizure diary variables were fed
into a fully connected neural network, with several hidden layers and depth as
hyperparameters that classified between seizure day conditions.

Results: The final sample contained 70 patients (median age=42.5years, 43 fe-
male) with 5437 recorded patient-days, including 557 seizure days and 537 presei-
zure days. Twenty-four-hour patterns in electrodermal activity and accelerometry

Solveig Vieluf and Sasagu Tomioka contributed equally to this work.

Todd Grinnell and Tobias Loddenkemper jointly supervised this work.

© 2025 International League Against Epilepsy.

Epilepsia. 2025;66:4259-4271.

wileyonlinelibrary.com/journal/epi 4259

---

VIELUF ET AL.

= LEpilepsia

resolution.

KEYWORDS

1 | INTRODUCTION

Epilepsy is a neurological disorder that affects millions
of people worldwide, one third of whom experience per-
sistent seizures despite antiseizure medications (ASMs).
Accurately tracking seizure occurrence plays an essential
role in rigorously validating novel therapies and in the
management and selection of ASMs." To this date, seizure
diaries provide the main outcome measure for epilepsy,
but diaries lack accuracy, particularly over extended peri-
ods.? Both underreporting and overreporting complicate
the interpretation of diary information.’

Emerging technologies aim to provide improved ep-
ilepsy management. More reliable avenues for seizure
monitoring related to chronic intracranial or subscalp
electroencephalographic (EEG) recordings are avail-
able.*® However, these invasive strategies are not without
risk and often fail to discriminate between electroclinical
and pure electrographic events. Wearable technologies
have surfaced as an innovative and less invasive poten-
tial solution to complement traditional seizure diaries.”®
Wearables can capture seizure-related changes in auto-
nomic and actigraphic data before and after seizures and
enable seizure detection and prediction, respectively.”
Although prior studies demonstrate feasibility in inpa-
tient settings using EEG as the gold standard, challenges
remain in ambulatory or real-life settings where the best
data labeling comes from diaries, with a daily resolution
and potential limitations of self-reported seizures. Recent
research has shown that seizure occurrence is driven by
cycles of different period lengths in diaries, EEG, and
wearable, providing new avenues for improving seizure
tracking and likelihood calculations.*™'®

Our previous work identified potential biomarkers
from inpatient recordings that may enhance seizure

differentiated no-seizure versus seizure days, as well as no-preseizure versus
preseizure days (p<.01). Classification between no-seizure and seizure days
(weighted F1=.81, sensitivity=.82, specificity=.67) as well as between no-
preseizure and preseizure days (weighted F1=.82, sensitivity=.80, specific-
ity =.66) revealed good performance.

Significance: Wearable data capture seizure-related differences with daily
resolution, differentiating between days with lower and higher seizure suscep-
tibility. Combining diary-based clinical and wearable data bears the potential
for developing a dynamic seizure detection and prediction system with daily

24-h pattern, biosensors, eslicarbazepine acetate, seizure biomarker, seizure forecasting

Key points

« The analysis includes a robust dataset spanning
over 5000days from a retrospective observa-
tional cohort study.

« Seizure monitoring in outpatient settings can
be enhanced by integrating wearable data with
retrospective diary entries, as this approach of-
fers mutual benefits.

« Distinct patterns in seizure days before another
seizure day suggest the potential for defining a
novel seizure day category.

detection and prediction strategies. First, we modeled
24-h patterns to capture circadian rhythms and showed
that these patterns can distinguish between seizure and
nonseizure recordings.'”'® Second, ultradian rhythms,
with periods between 1 and 12 h, differ between record-
ings with and without seizures in specific frequencies."
Third, we discovered that short evening recordings
could forecast whether a seizure was likely to happen
the next day.*

Here, we aimed to test these three markers' potential
for seizure detection and prediction in a longitudinal real-
life outpatient dataset. We sought to determine whether
no-seizure days differed from seizure or preseizure days
regarding 24-h patterns, ultradian characteristics, and
short evening recordings of wearable data (aim 1). To test
the potential of the markers showing differences between
seizure conditions for seizure detection and prediction, we
aimed to classify between no-seizure and seizure or pre-
seizure days, respectively (aim 2).

25U9I7 suowwoy aAneal) ajqealjdde ayy Aq pausanob aie sajoIle YO ‘@sn Jo sa|nJ Joy A1eiqr] aulug A3|iMm uo (suonipuod
-pue-suis)/wodAspmAseiqijauljuo//:sdiy) SUORIPUOD pue swia] 3y} 33S *[920Z/10/50] uo Aseiqrq aunuo Asjim ‘ujoy nz jenssanun Jap ‘|qig Ag ‘0558 L 1d3/L L L1 0 L/1op/wodAaim Atelqiauljuo//:sdny woiy papeojumoq ‘LL ‘SZ0Z ‘L9LL8ZSL

---

VIELUF ET AL.

2 | MATERIALS AND METHODS

21 | Study design

This is a retrospective, observational cohort study. Data
were collected during a 31-week, multicenter (39 sites in the
United States and one site in Canada), two-arm, prospective,
open-label, nonrandomized, phase 4 study in the United
States and Canada (phase IV clinical trial NCT03116828).
Details on the study design can be found online (see data
sharing section). Patients were enrolled in two study arms.
The underlying trial aimed to test the effectiveness of esli-
carbazepine acetate (ESL) as adjunctive therapy to leveti-
racetam or lamotrigine in adults with focal seizures over a
24-week maintenance period to replicate a traditional phase
3 study arm. To maximize the dataset, we merged both trial
arms, as the monitoring design, including wearable and
diary, were similar for both arms, and evaluated the dataset
as a single cohort. For this trial, wearable data were purely
exploratory endpoints and were not envisioned to influence
the results or the interpretation of primary endpoints. We
adhered to the STROBE checklist.

2.2 | Patients

We included ESL-naive patients with intractable focal
epilepsy (aged 18 and older) with a documented EEG sup-
porting the diagnosis, within the past 10years and at least
three focal seizures during the preceding 6 months. At the
time (2016) of the phase 4 open-label clinical trial design
from which these data were extracted, the most recent
version of the 2017 International League Against Epilepsy
(ILAE) Classification of Seizures had not yet been fully
implemented. The terminology used in the protocol de-
velopment reflected the existing accepted nomenclature
from the 2010 update to the 1981 ILAE classification sys-
tem. This was also the case with all previous clinical trials
of ESL. It was also consistent with the version of the clas-
sification system used in the approved US Food and Drug
Administration indication for the use of ESL. Because sei-
zures were identified and classified in this trial using the
older terminology, it would not be appropriate to assign
the newer terminology retrospectively. Neuromodulatory
devices (e.g., vagus nerve stimulator) had to be implanted
more than 6 months previously. Patients were excluded if
they had taken a medication that was prohibited in the
protocol of the clinical trial if they had seizures of gen-
eralized onset, exclusively focal seizures without motor
signs, a history of status epilepticus or cluster seizures, or
nonepileptic seizures. In addition, patients with other pro-
gressive physical or mental disorders were excluded. See
Figure 1 for inclusion tree and dataset overview.

Epilepsia--=*

2.3 | Procedures

Data were recorded and collected from 2017 to 2019. For
all included patients, age, sex, epilepsy duration, seizure
frequency, etiology, and worst seizure type were col-
lected based on medical records and patient self-report.
Additionally, medication intake history and seizure dia-
ries were obtained. The seizure diary included the seizure
date, estimated time, seizure type, and additional notes.
Patients received paper seizure diaries during screening,
titration, and every 4weeks during the 24-week main-
tenance phase. We retrospectively calculated prestudy
seizure frequency from historical patient diaries. Diaries
were collected and analyzed on the day of the next visit.
Patients indicated whether and how many seizures they
had with daily accuracy. Patients alternatingly wore two
Embrace (Empatica) sensors that recorded electrodermal
activity (EDA; sampling rate of approximately 4 Hz), wrist
temperature (TEMP; sampling rate of approximately 1 Hz),
and three-axis accelerometry (sampled at 32Hz). During
enrollment, defective devices were replaced. Wearable
data were analyzed with MATLAB 2023b (MathWorks).
For each patient, we concatenated all data. In overlapping
periods, we retained the recording with the higher tem-
perature, assuming the wrist temperature exceeded room
temperature. We removed data points in all three signals if
the TEMP was <24 or >37°C, and we removed EDA data
<.01 or >40 pS."”*! We included days with >8h of quality
recording that could be discontinuous. We converted con-
tinuous three-dimensional acceleration data into a single
acceleration vector (ACC) by calculating the root sum of
squares.” Based on diary entries, we divided time series
data into 24-h windows (midnight to midnight), annotat-
ing them as no-seizure versus seizure and no-preseizure
versus preseizure day. Preseizure and seizure days could
be the same and we labeled them as “both” for follow-up
analysis. See Figure 2 for a methods illustration.

2.4 | Wearable data analysis,
statistics, and machine learning

For group-based comparisons of 24-h patterns between no-
seizure and preseizure and seizure days, respectively, we
took the median of each 10-min window. We modeled 24-h
patterns with harmonic models, with two harmonic terms
for EDA and one harmonic term for ACC and TEMP per
patient, and saved model parameters.”” To compare the
seizure-day conditions among each other, we fit a nonlinear
mixed-effects harmonic model to either all days or a model
that included a group, that is, seizure-day condition indica-
tor. We decided on the better fitting model as determined by
the rejection decision parameter h and the p-value."”

3sudd|T suowiwo) aAneal) ajqeorjdde ayy Aq pausanob ale sajonIe YO ‘sn Jo sajni 1oy Aresqr auuo Aajim uo (suonipuod
-pue-suis)/wodAspmAseiqijauljuo//:sdiy) SUORIPUOD pue swia] 3y} 33S *[920Z/10/50] uo Aseiqrq aunuo Asjim ‘ujoy nz jenssanun Jap ‘|qig Ag ‘0558 L 1d3/L L L1 0 L/1op/wodAaim Atelqiauljuo//:sdny woiy papeojumoq ‘LL ‘SZ0Z ‘L9LL8ZSL

---

VIELUF ET AL.

= | Epilepsia
(A) ‘ \

[ 50 100

days

150 200

patients
g & 8

3

70

FIGURE 1 Dataset overview with (A) inclusion diagram and (B) dataset overview showing the number of days covering the period of
diary entries by the patient (yellow indicates a seizure day, and purple represents a no-seizure day), before excluding days based on wearable

data availability and quality.

We calculated the power spectral density to reveal ul-
tradian patterns by plotting Lomb-Scargle periodograms
with period lengths from .125h to 12h in .125-h incre-
ments. We extracted peak power and peak period length
around 12-, 10-, 4-, 3-, and 2-h period lengths with a win-
dow of +.25h, when a difference was visually detected.
Power values were compared with the paired two-sample
t-test and period length with the Wilcoxon signed rank
test. For short recordings, in addition to a 10-min time
window at 9p.m. as previously reported,® we selected a
time window at 11:30 p.m. as the average adult bedtime.

A paired two-sample t-test was performed to compare pre-
seizure and no-seizure day recordings. For reporting and
inclusion into the next step of deep neural network train-
ing, we set the significance level to p <.05.

We used Python with Google TensorFlow version
2.8.2 and Keras®® with Keras-tuner,” as well as Scikit-
learn® to run a deep neural network algorithm for the
classifications. We included wearable markers that were
significant on a group level combined with demograph-
ics, clinical data, and the diary-based days since the last
seizure variable. Seizure detection and prediction were

3sudd|T suowiwo) aAneal) ajqeorjdde ayy Aq pausanob ale sajonIe YO ‘sn Jo sajni 1oy Aresqr auuo Aajim uo (suonipuod
-pue-suis)/wodAspmAseiqijauljuo//:sdiy) SUORIPUOD pue swia] 3y} 33S *[920Z/10/50] uo Aseiqrq aunuo Asjim ‘ujoy nz jenssanun Jap ‘|qig Ag ‘0558 L 1d3/L L L1 0 L/1op/wodAaim Atelqiauljuo//:sdny woiy papeojumoq ‘LL ‘SZ0Z ‘L9LL8ZSL

---

VIELUF ET AL.

5
g
:
H
H
g
§
H

8

Temperature (degrees C)

2

20 21

10000

EDA
PSD EDA

2z Jul23 Jul24 Jui25 Jui26 Jui2r
2018

o

EDA Level
~ >

. 0+
o 00 5 10 15 20

hour of the day

20 8000
15 6000
1.0 4000
0.5 2000
0 2 5 7 10

period length in hours

12 0

11:30
time

Layers Predicted label
* Age input densel densen output No seizure Seizure
* Sex
* Age at epilepsy onset g
* Etiology B False
* Baseline number of anti-seizure 3 positives
medications z

* Baseline seizure frequency
« Days since last seizure

True label

False
negatives

Seizure

dropout

FIGURE 2 Summary of the analysis pipeline, including data preparation and preprocessing, before biomarker validation by analyzing

24-h patterns, ultradian rhythms, and evening short recordings. Biomarkers showing significant differences between seizure-day conditions

(no-seizure and preseizure or seizure) are used as input features combined with demographic and clinical data for classifications between

seizure-day conditions by a fully connected neural net. EDA, electrodermal activity. PSD, pre-seizure day.

based solely on retrospective seizure diary entries, using
only information available up to the previous day, with-
out incorporating data from the day being evaluated.
We excluded etiology and worst seizure type due to sub-
groups of less than three patients and the EDA short re-
cording, as it highly correlated (p<.01) with the EDA
24-h level. sklearn.feature_selection.RFECV performs
recursive feature elimination with cross-validation,
systematically removing less important features and
evaluating model performance at each step to select
the optimal subset of features that maximizes predic-
tive accuracy. We performed sklearn.feature_selection.

RFECV on randomly oversampled data with 10 runs
and included a minimum of six features for each fold for
detection, prediction, and seizure activity type classifi-
cation separately. The feature selection was performed
for combined data and wearable data analysis only. See
Figure S1 for an illustration of the machine learning
pipeline.

For network training, we used random oversampling.
We performed stratified fivefold cross-validation, split-
ting the dataset into 80% training data and 20% test data.
The training data was further split (also stratified) into
90% actual training data and 10% validation data for

Epilepsia--*

[Im-Asesqijaurjuo//:sdiy wouy papeojumoq ‘LL ‘S20Z ‘LZ9LL8ZSL

3sudd|T suowiwo) aAneal) ajqeorjdde ayy Aq pausanob ale sajonIe YO ‘sn Jo sajni 1oy Aresqr auuo Aajim uo (suonipuod

-pue-suis)/wodAspmAseiqiiauljuo//:sdily) suonIpuog pue swua) 3y} 93s ‘[920Z/10/50] uo Aseiqiq aunuo Asjim ‘ujoy nz JenssaAun Jap *|qig Ag ‘0558 L 1d3/L L LL 0 L/IOp/WOD

---

VIELUF ET AL.

= | Epilepsia

the fit. We chose a per-day split approach for the gen-
eral model, which allows data from the same patient
to be included in the training, validation, and test sets.
Despite the potential risk of data leakage, this approach
was selected because the number of days per patient var-
ied significantly, making stratification impractical given
the 9:1 split in the inner loop and the 4:1 split in the
outer loop. Additionally, an entire patient was held out
for independent testing in the leave-one-out approach.
Although the per-day split does carry a risk of minor
information leakage due to shared patient data across
subsets, the observed robustness of the model's perfor-
mance suggests that it maximizes data usage and effec-
tively captures general patterns rather than overfitting
to patient-specific data. The similarity of the results be-
tween the per-day and leave-one-out approaches would
indicate that interpatient-specific data were not critical
for model performance.

We trained fully connected deep neural networks for
different objectives. Each neural net consisted of N dense
layers of width W, an optional dropout layer with an ad-
justable dropout rate, and a dense output layer using the
softmax activation function. We used the sigmoid activa-
tion function for the N hidden layers. We used the Adam
optimizer with a categorical cross-entropy loss function.
The number of layers, their width, the use of the dropout
layer, and its dropout rate, as well as the batch size and the
learning rate, were tunable parameters in this study. We
used keras_tuner and the BayesianOptimizer to perform a
hyperparameter scan based on a probabilistic model, opti-
mizing for the number of “true positives.” We used Keras'
early stopping function, with a “patience” of 50 epochs,
to terminate training when the validation loss reached its
minimum. The performance metrics were evaluated on
the test data for each fold and average. We report weighted
F1, weighted precision, weighted recall, and the area
under the precision-recall curve (AUC_PR), as well as
sensitivity and specificity as model performance parame-
ters. For seizure activity comparisons, we report weighted
F1, weighted precision, and weighted recall. For model
evaluation, we chose the weighted F1 score as an overall
performance metric and decided to consider weighted F1
of <.8 as poor performance, .8 up to .9 as good, and >.9 as
excellent.

3 | RESULTS

3.1 | Patients and recordings

One hundred twenty-seven patients were screened,
and 102 subjects were enrolled in the study. Of those,
wearable data and/or paper diaries were missing for 15

patients (for more details, see Figure 1). Seventy-seven
patients had at least one no-seizure and one seizure
day recorded and were screened for data quality. The
final sample comprised 70 patients, with a total of 5437
recorded days (out of an original 12137 patient-days
within the reporting period, resulting in a deficiency
time of 55%). Among these, 557 were seizure days, 537
were preseizure days, and 242 were classified as both
seizure and preseizure days (Figure 1). The average age
of the included patients was 42.5years, and 43 were
female (for demographics and clinical characteristics,
see Table 1).

3.2 | Daily autonomic nervous
system activity differences
between no-seizure and seizure or
preseizure days

The analysis of 24-h patterns revealed that the model dif-
ferentiating between groups (H1) was superior for EDA
(h=1, p<.01) and ACC (h=1, p<.01), whereas HO rep-
resents data better for TEMP (h=0, p=1; Figure 3). For
ultradian rhythm analysis, the overall power did not dif-
fer between seizure conditions (all p>.05). We observed
lower power at seizure than no-seizure days for EDA 4-h
and ACC 10-hcycles. Peak period lengths differed for EDA
12- and 4-h, ACC 4- and 2-h, and TEMP 12- and 3-hcy-
cles. Preseizure days had lower ACC power for 10-h, and
peak period lengths differed for EDA 12- and 4-h, ACC
4-h, and TEMP 12- and 3-hcycles (Table S1). Comparing
preseizure and no-seizure evening recordings did not dif-
fer at 9p.m. (t=1.08, p=.28), but EDA levels were higher
in preseizure compared to no-seizure nights at 11:30 p.m.
(t=2.29, p=.03).

3.3 | Classifications for seizure
detection and prediction

See Table S2 for feature ranking; all features with rank
1 are included in the fold analysis. Features selected
over folds always contained days since last seizure and
baseline seizure frequency as well as parameters of the
24-h EDA and ACC patterns. Performance characteris-
tics of the machine learning are summarized in Table 2.
For the classification between no-seizure and seizure
days relevant for seizure detection, the classification
performance was comparable for the combined feature
input (AUC_PC =.84) and stochastic diary-based input
(AUC_PC=.83), and did not allow distinguishing be-
tween seizure and nonseizure days based on wearable
data only (AUC_PC =.49).

3sudd|T suowiwo) aAneal) ajqeorjdde ayy Aq pausanob ale sajonIe YO ‘sn Jo sajni 1oy Aresqr auuo Aajim uo (suonipuod
-pue-suis)/wodAspmAseiqijauljuo//:sdiy) SUORIPUOD pue swia] 3y} 33S *[920Z/10/50] uo Aseiqrq aunuo Asjim ‘ujoy nz jenssanun Jap ‘|qig Ag ‘0558 L 1d3/L L L1 0 L/1op/wodAaim Atelqiauljuo//:sdny woiy papeojumoq ‘LL ‘SZ0Z ‘L9LL8ZSL

---

VIELUF ET AL.

TABLE 1 Demographic and clinical characteristics of 102 enrolled patients and 70 patients with wearable data and paper diaries

included in the analysis.

Age, years Median
Sex, n (%) Female
Male
Epilepsy duration, years Mean (SD)
n (%) >20years
<20years
Etiology, n (%) Hereditary
Trauma
Infection

Brain tumor
Temporal sclerosis
Febrile seizure
Cerebral
Brain malformation
Unknown
Other

Worst seizure type [baseline], n (%)  Simple partial

Complex partial

Partial evolving to secondary generalized

Unknown

Other
Baseline standardized seizure Mean (SD)
frequency [28 days] Range
Number of documented seizure Mean (SD)
days Range
AED use, count Mean (SD)

Note: This table reflects the data capture terminology used at the time of the trial.

Abbreviation: AED, antiepileptic drug.

For the classification between no-seizure and pre-
seizure days, the performance was similar for combined
wearable and clinical input data (AUC_PC=.87), and for
diary-based input, that is, the stochastic model (AUC_
PC=.83), and did not classify based on wearable data only
(AUC_PC=.68).

3.4 | Differentiability of seizure
activity types

As a follow-up analysis, we compared preseizure days, sei-
zure days, and days that are both preseizure and seizure
days. The classification performance was comparable for
combined wearable (AUC_PC=.48) and clinical input
and diary-based input (AUC_PC=.51) and did not classify
based on wearable data only (AUC_PC =.33).

Enrolled, n=102 Final analysis, n=70

40.5 425

60 (58.8%) 43 (61.4%)
42 (41.2%) 27 (38.6%)
15.1 (14.85) 17.1 (14.81)
29 (28.4%) 24 (34.3%)
73 (71.6%) 46 (65.7%)
6 (5.9%) 2(2.9%)

21 (20.6%) 16 (22.9%)
2(2.0%) 1(1.4%)
2(2.0%) 1(1.4%)
1(1.0%) 1(1.4%)
2(2.0%) 0(.0%)

6 (5.9%) 3(4.3%)
7(6.9%) 5(7.1%)

56 (54.9%) 40 (57.1%)
4(3.9%) 4(5.7%)

10 (9.8%) 8 (11.4%)
66 (64.7%) 47 (67.1%)
24 (23.5%) 14.0 (20.0%)
1(1.0%) 0(.0%)
1(1.0%) 1(1.4%)
11.9 (41.79) 10.2 (40.41)
3-337.5 3-337.5
19.6 (32.71) 17.9 (31.77)
1-188 1-188

1.4 (.60) 1.5(.63)

Classification results are summarized in Table 2 and
Figure 4 as well as Figure S2. Feature selection for wear-
able data only is presented in Table S2. Figure S3 and
Table S2 show the results for the leave-one-out analysis
that provided comparable results.

4 | DISCUSSION

We examined wearable data and confirmed differences
in recordings captured during seizure or preseizure days
compared to no-seizure days. Despite the group differ-
ences, the extracted wearable features lack discrimina-
tory power for daily classification; the resolution of the
diary data as the gold standard did not allow for finer
granularity. Contextualizing wearable data with diary
entries and clinical attributes significantly enhanced

Epilepsia--

-
a
N
@
=
jery
o
N
]
1]
N
o
N
jury
o
-]
H
2
o
]
a
@
a
-
=t
]
3
=
=
<
a
=
)
2
5
o
g
]
2
=
o
<
S8
es
°
58
£3
oo
<o
o=
[
53
CR:]
=3
©
28
<8
3
@
S
<
£
a2
S a
)
=8
c
o3
o=
S5
o 8
I
el
o N
2 c
a
32
=1
o=
=3
=
'Y=
83
3
9o
g3
)
o2
]
83
=
58
]
o
g.
7]
ER
30
-
23
@ o
-
g2
53
o n
® o
3
a
<)
-]
3
2
=
)
=
L
=
=
<
a
=
)
EX
5
[
53
g
2
2
z
2
[=3
o
3
=
o
2
3
]
?
2
3
&

---

VIELUF ET AL.

= | Epilepsia

= = Ing
o wn o

electrodermal activity

o
n

0.0 T v - v
0 5 10 15 20

hour of the day

1.01

1.001

actigraphy
o
o
o

0.98 1

0.97

0 5 10 15 20
hour of the day

33.0

325

32.0

temperature at wrist

315

31.0 T y y v
0 5 10 15 20

hour of the day

FIGURE 3 Results for modeled 24-h patterns (blue =no-
seizure, purple = preseizure, red =seizure) for electrodermal
activity, actigraphy (acceleration vector), and temperature at
wrist data.

classification performance to a similar level as using
diary-based features alone. Classification based on his-
torical diary data, that is, days since last seizure and sei-
zure frequency, allowed discrimination between seizure
activity conditions and no-seizure days. Furthermore,

our analysis revealed distinctive patterns for combined
seizure and preseizure days, hinting at potential addi-
tive or multiplying effects of consecutive seizures. These
findings underscore the importance of integrating mul-
timodal data sources for comprehensive seizure man-
agement strategies.

4.1 | Seizure diaries contain predictive
information

Despite many shortcomings, seizure diaries are the
standard of care in epilepsy management and build a
valid source of information for clinical trial outcomes.
Epilepsy is characterized by cyclic dynamics comprising
phases with both high and low seizure likelihoods.***
Based on self-reported data from a mobile seizure diary,
circadian patterns and multiday seizure patterns were
extracted, and those contained personalized information
on seizure likelihood.**?° In line with this approach, we
extracted seizure frequency determined at the start of
the study and the daily changing variable of days since
the last seizure from the diary data and built a classi-
fication system. In line with the cyclic approaches,"*™*®
we obtained good performance. We achieved a similar
performance as a previously reported seizure diary alone
approach that aimed at estimating the predictability of
seizures by statistical and machine learning-based ap-
proaches.”” Due to the imbalance in the dataset, we
report weighted F1 and AUC_PR instead of the AUC_
ROC, reported in other studies, for model performance,
so a direct performance comparison is not feasible. The
advantage of the approach presented in this study is that
it can start from the first day of use of the system and it
can learn and adjust easily over time. However, it would
be of great interest to combine both approaches by add-
ing the cycles after a recording of approximately 30 days.
Here, we used paper-based diary data for labeling sei-
zure days. However, some seizures may be missed, and
reporting accuracy and reliability are low, as patients
may not recall seizures, and some seizures may not be
noted by caretakers.” The seizure diary used in this study
included the seizure date, estimated time, seizure type,
and additional notes. As the time of the seizures was
estimated, the timing presented with inaccuracies that
challenged the time-based seizure detection and predic-
tion approaches.’*® We attempted to overcome this chal-
lenge of the low temporal resolution of seizure diaries
with day-based resolution biomarkers. For future stud-
ies, electronic seizure diaries offer the advantage of fa-
cilitating real-time data collection and analysis and add
the importance of discriminating between seizure, no-
seizure, and not-filled days.

3sudd|T suowiwo) aAneal) ajqeorjdde ayy Aq pausanob ale sajonIe YO ‘sn Jo sajni 1oy Aresqr auuo Aajim uo (suonipuod
-pue-suis)/wodAspmAseiqijauljuo//:sdiy) SUORIPUOD pue swia] 3y} 33S *[920Z/10/50] uo Aseiqrq aunuo Asjim ‘ujoy nz jenssanun Jap ‘|qig Ag ‘0558 L 1d3/L L L1 0 L/1op/wodAaim Atelqiauljuo//:sdny woiy papeojumoq ‘LL ‘SZ0Z ‘L9LL8ZSL

---

VIELUF ET AL.

TABLE 2 Performance metrics of machine learning models.

Epilepsia--=*

Weighted
‘Weighted F1 precision Weighted recall AUC_PR Sensitivity Specificity
Mean 95%CI Mean 95%CI Mean 95%CI Mean 95%CI Mean 95%CI Mean 95% CI
Detection
Stochastic .83 .02 .89 .00 .80 .03 .83 .01 .82 .04 .67 .06
Allranked .81 .02 .88 .01 77 .03 .84 .02 .78 .03 .66 .06
Wearable .59 .19 .82 .01 .56 24 49 .03 .57 31 44 .32
Prediction
Stochastic .83 .02 .89 .00 .79 .03 .83 .02 .81 .03 .67 .06
Allranked .82 .02 .89 .00 .79 .04 .87 .02 .80 .04 .66 .06
Wearable .72 oIl .82 .01 .69 .16 .68 B[S §78) 21 .29 .23
Seizure activity types
Stochastic .42 .04 45 .04 45 .03 48 .04 N/A N/A N/A N/A
Allranked .42 .04 A4 .04 44 .04 .51 .04 N/A N/A N/A N/A
Wearable .30 .04 31 .06 32 .03 33 .02 N/A N/A N/A N/A

Note: Means and 95% Cls are reported for weighted F1, precision, recall, AUC_PR, sensitivity, and specificity.

Abbreviations: AUC_PR, area under the precision-recall curve; CI, confidence interval; N/A, not applicable.

4.2 | Seizures disrupt the rhythmic daily
activity of the autonomic nervous system

Various physiological processes in the human body are
governed by complex interplays of different rhythms.*
Human biological systems operate with precision
through complex interplays of various rhythms, and
polyrhythmicity is a distinguishing feature sensitive
to events like seizures affecting internal balance. The
potential seizure biomarkers, 24-h patterns, ultradian
patterns, and short recordings were developed in a pedi-
atric patient cohort who wore wearables during an in-
patient stay at the epilepsy monitoring unit, and seizure
patients had one or more tonic-clonic or focal impaired
awareness seizures.'”'® In this study, wearable markers
were tested on longitudinal outpatient data in an adult
population with partial onset (focal) seizures. Here, we
included peri-ictal data in the analysis, as the exact sei-
zure times are unknown. We confirmed distinct 24-h
patterns for electrodermal activity and showed patterns
in actigraphy.’”® The models' higher peaks for EDA
and ACC on seizure days might reflect seizure activity.
Ultradian patterns and short recordings differ between
seizure activity and no-seizure days on a group level but
did not contribute to the classification between condi-
tions, which might relate to high intra- and interpatient
variability.

Following moderate classifier performances for sei-
zure detection and prediction and taking similarities
of preseizure and seizure day polyrhythmic patterns
into account, we tested the classification performance

between seizure and preseizure days. Many seizure days
are followed by a seizure day, introducing a new seizure-
related class (both). This indicates the high likelihood
of acute repetitive seizures, that is, seizure patterns
with periods of more frequent serial seizures.* Results
showed a by-chance classification, indicating that days
share common activity trends and that seizure activity
builds up before the seizure happens. Additionally, the
days that are both preseizure and seizure days have a
higher likelihood of being deemed non-no-seizure days
in the four-class comparison. This suggests additive or
superimposed effects for our set of biomarkers and bears
the potential to identify the lead-day of a period of more
frequent serial seizures.

43 | Combining wearable with
diary-based clinical data has the potential
to make seizure monitoring more dynamic

Despite significant differences on a group level, the bio-
markers we extracted from the wearable recordings did
not differentiate between seizure-day conditions. Based
on the diary as the gold standard, we can only classify
with a daily resolution, making the results not directly
comparable to previous seizure detection and predic-
tion methods.**'* Seizure diaries may permit the deter-
mination of seizure patterns that occur in circadian and
multiday cycles, and seizure diary patterns may serve
as predictors of seizure occurrence.**?® Feature rank-
ing shows that diary-based clinical data, that is, seizure

3sudd|T suowiwo) aAneal) ajqeorjdde ayy Aq pausanob ale sajonIe YO ‘sn Jo sajni 1oy Aresqr auuo Aajim uo (suonipuod
-pue-suis)/wodAspmAseiqijauljuo//:sdiy) SUORIPUOD pue swia] 3y} 33S *[920Z/10/50] uo Aseiqrq aunuo Asjim ‘ujoy nz jenssanun Jap ‘|qig Ag ‘0558 L 1d3/L L L1 0 L/1op/wodAaim Atelqiauljuo//:sdny woiy papeojumoq ‘LL ‘SZ0Z ‘L9LL8ZSL

---

VIELUF ET AL.

= | Epilepsia

Stochastic All Ranked Wearable Ranked
no-sz SZ no-sz SZ no-sz Sz
N N N
g 82% + 4% 18% + 4% g 78% + 3% [IPPAIEICE g 57% = 31 % ERIEECIN
c c c [
o
2
O
]
-t
a
o SRR/ IR 67 % £ 6% USRI 66 % + 6 % N1 56% + 32% RUT NP/
no-pre-sz pre-sz no-pre-sz pre-sz no-pre-sz pre-sz
N N N
i o ol
£181% +3% [CRAEICE L1 80% +4% [PLROEREA £173% +21%
=) ° o
e = < <
S
iel
[
S
a 3 b
EEL AN 67 % + 6% o ELY AN 66% + 6%  {NAS6EEN281%6
o Q

both pre-sz

28% % 12%

pre-sz
pre-sz

142% = 9% 22% + 9% 36% * 7%

sz

Activity Types
74

both

q6%+3% 5
Q

predicted label

sz both

32% = 9% EINERERA 22% + 7%

CRCPLEEWERA 63 % + 9%

predicted label

both

LR URNPLER WA 50 % + 13 %)
11% 31% * 6%

a47% * 7%

F=4
Fog 24 % = 14 % 29 % + 14 % ELRER VAL
Q

predicted label

FIGURE 4 Summary of classification results by seizure activity-specific classifications for the feature combinations diary-based

(stochastic), all features ranked, and wearable features ranked (from left to right). Validation results are averaged over five folds and

normalized per row. sz, seizure.

frequency and days since the last seizure, are the two fea-
tures with the highest importance. In line with the seizure
cycle approaches, using a combination of patient-specific
seizure frequency with the information of days since the
last seizure derived from the historical seizure reporting
revealed good accuracy. We conclude that seizure moni-
toring in outpatient settings can be enhanced by integrat-
ing wearable data with retrospective diary entries, as this
approach offers mutual benefits; diary entries provide

context for wearable data, helping to identify patterns re-
lated to stress and other factors, and wearable data add
real-time precision and flexibility to diary-based seizure
tracking, capturing fluctuations in events and moods
throughout the day. Our findings might serve as a basis
for a prospective study, where multiday cycles based on
wearable and diary data are added to the presented analy-
sis.'*!*** The prospective study could evaluate the corre-
spondence between seizure-day labeling between diaries

-
a
N
@
2
oy
o
N
N
o
N
&
N
pry
o
S
H
2
o
o
o
o
Q.
-
=
°
3
=
=
b1
a
=
o
2
S
o
=
g
o
2
£
o
<
Sa
39
2:
S o
£3
a°
<o
o=
32
53
23
=4
0
FRA]
<8
Y
:2
cw
3
S a
S
52
c
o3
os
> 8
o 2
25
5%
o N
2c
3%
° 5
't
$s
32
a9
o=
< 35
~x1
=
o O
88
LR
§‘<
°
®
=2
o o
58
]
93
=N
59
]
oS
g
»
(]
33
S =
23
@ o
g |
22
23
® g
=]
a
(=]
-]
=
2
=
S
=
»
=
=
=
<
@
2
°
EX
5
[
=
g
o
s
=
z
2
[+]
°
3
2
=
]
1
3
@
o
3
e

---

VIELUF ET AL.

and wearables. Incorporating a human-in-the-loop ap-
proach, where wearable devices prompt participants to re-
port whether they experienced a seizure based on device
predictions, could significantly enhance the accuracy of
self-reported data. We believe that utilizing wearables to
supplement traditional paper or app-based diaries could
improve participant adherence and provide valuable real-
time support for documentation. Future studies should
explore this integration, as it holds promise for optimizing
seizure monitoring and enhancing the quality of collected
data. Also, future studies could explore the relationship
between circadian patterns of seizures and the characteri-
zation of patients' chronotypes in relation to 24-h patterns
in wearable data. This investigation would be of signifi-
cant interest, as understanding these interdependencies
could reveal how individual biological rhythms influence
seizure occurrence, potentially leading to more person-
alized management strategies for epilepsy. Researchers
may uncover critical temporal factors that impact seizure
frequency and severity by integrating wearable data with
chronobiological insights. The next step would be to test
the clinical impact of an increased accuracy in seizure re-
porting. The clinical impact of improved seizure monitor-
ing has not yet been tested in long-term prospective trials.
Simulated data suggest that increased accuracy in seizure
reporting does not directly affect ASM burden or seizure
freedom rates®'; however, the long-term impact may arise
from better treatment adjustments enabled by higher ac-
curacy, ultimately leading to improved outcomes. Beyond
ASM burden, psychological factors such as quality of life
and patient empowerment are critical aspects of clinical
care, as enhanced seizure reporting accuracy may foster
more informed patient-physician communication and en-
able more personalized treatment strategies.

4.4 | Limitations

Retrospective and partly exploratory analysis of wear-
able data collected during a clinical pharmaceutical trial
presents several inherent limitations. First, the quality
of the wearable data and patient compliance in wearing
the device introduce noise and bias into the data. We ex-
cluded days with low-quality data, but we had no means to
monitor compliance or how well the device was worn. The
resolution of the diary was daily. Therefore, we restricted
our analysis to seizure days due to the resolution of the
seizure diary data. A follow-up study utilizing real-time
seizure reporting, such as through an app, would enable
more detailed, time-specific analysis. Additionally, we did
not take other influencing factors, such as sleep, stress,
or other temporal factors that were shown to impact sei-
zure likelihood, into account.*” Using labels derived from

Epilepsia--=*

retrospective diary data can introduce recall bias, as par-
ticipants may inaccurately report the timing or frequency
of events like seizures, potentially skewing the results
and weakening the predictive model's validity. This reli-
ance on self-reported data may also miss subtle patterns
or more minor seizures that participants do not notice. A
future study could mitigate these issues by using objec-
tive, real-time data collection methods, such as continu-
ous monitoring through wearable devices, implantable
EEGs, or automated video analysis (at least for nighttime),
providing an alternative and potentially more reliable gold
standard for seizure detection. This approach would cap-
ture more precise, continuous data, allowing for a more
accurate evaluation of predictive algorithms.

The retrospective nature of the analysis limits control
and standardization of the conditions under which the
data were collected. Also, the overall aim of the clini-
cal trial was to test an early adjunctive therapy in adults
with focal seizures. To maximize the dataset, we did not
take the medication groups into account but used sei-
zure frequency. Patients had comparably low residual
baseline seizure frequency, and patients with generalized
EEG-seizure onset were excluded. Both aspects might
diminish the strength of the seizure-related signature in
the wearable signal and increase the relevance of watch
placement. Also, this selection bias impacts the general-
izability to other patient populations. Here, most patients
had multiple seizure subtypes, which increases the vari-
ability within patients. Due to variability in the dataset,
we performed the feature selection as a preprocessing
step based on the entire dataset, which incorporates in-
formation from the validation set during feature selec-
tion. Although this approach was chosen to ensure robust
feature identification given the dataset's complexity and
limited size, we acknowledge that it may impact the gen-
eralizability of the results and recommend that future
studies validate the findings using independent test sets
or cross-validation techniques if their dataset is larger and
therefore the impact of individual patients on feature se-
lection is minimized. All these aspects influence the gen-
eralizability of the models. One limitation of our study
is the inability to compare the Embrace device to other
seizure detection systems, as only retrospective data from
this well-established and widely accepted device were
available for analysis. To our knowledge, no established
algorithms exist for seizure monitoring at the daily reso-
lution we used, making direct comparisons with other ap-
proaches difficult. Furthermore, the wearable device did
not record cardiac activity, which could greatly improve
seizure monitoring.*>**

Taken together, the retrospective analysis of wearable
data offers valuable insights into real-world data; follow-up
research must address various limitations to ensure the

25U9I7 suowwoy aAneal) ajqealjdde ayy Aq pausanob aie sajoIle YO ‘@sn Jo sa|nJ Joy A1eiqr] aulug A3|iMm uo (suonipuod
-pue-suis)/wodAspmAseiqijauljuo//:sdiy) SUORIPUOD pue swia] 3y} 33S *[920Z/10/50] uo Aseiqrq aunuo Asjim ‘ujoy nz jenssanun Jap ‘|qig Ag ‘0558 L 1d3/L L L1 0 L/1op/wodAaim Atelqiauljuo//:sdny woiy papeojumoq ‘LL ‘SZ0Z ‘L9LL8ZSL

---

VIELUF ET AL.

= | Epilepsia

validity and applicability of the findings, generated with
this uniquely large dataset.

5 | CONCLUSIONS

Integrating diary-based, clinical, and wearable data shows
differentiation between no-seizure and seizure/presei-
zure days, demonstrating the promising potential for im-
proved seizure detection and prediction in the outpatient
setting with the potential to contribute to better epilepsy
management.

AUTHOR CONTRIBUTIONS

Solveig Vieluf, Sasagu Tomioka, Todd Grinnell, and Tobias
Loddenkemper conceptualized and designed the study.
Todd Grinnell and Sasagu Tomioka were involved in the
data acquisition. All coauthors designed analysis methods
used. Solveig Vieluf and Sasagu Tomioka performed data
analysis. Solveig Vieluf wrote the initial manuscript draft.
All coauthors drafted parts of the manuscript, edited the
manuscript, and approved the final version.

ACKNOWLEDGMENTS
We thank Joanne Rahmati for her support.

FUNDING INFORMATION

The study was supported by the American Epilepsy Society
under award number 932267, the Epilepsy Research Fund,
and Sumitomo Pharma America, Inc. (formerly Sunovion
Pharmaceuticals; phase IV clinical trial NCT03116828).

CONFLICT OF INTEREST STATEMENT

T.L. is part of patent applications to detect and predict
clinical outcomes and to manage, diagnose, and treat
neurological conditions, epilepsy, and seizures. T.L. has
received past device donations from various companies, in-
cluding Empatica, and has received research support from
Empatica in the past. S.V., B.Z., and T.L. are part of a pat-
ent application covering technology for seizure forecasting.
VK. serves on the scientific advisory board of Enliten AI
and is a paid consultant for the Digital In Vivo Alliance.
S.T. is an employee of Sumitomo Pharma America, Inc.
(formerly Sunovion Pharmaceuticals). Neither of the other
authors has any conflict of interest to disclose. We confirm
that we have read the Journal's position on issues involved
in ethical publication and affirm that this report is consist-
ent with those guidelines.

DATA AVAILABILITY STATEMENT

Deidentified data that support the findings of this study
are available upon reasonable request, and approval
pending intent of use. Study protocol is available at

https://classic.clinicaltrials.gov/ct2/show/NCT03116828
and can be accessed by anyone for any purpose.

ORCID

Solveig Vieluf ® https://orcid.org/0000-0002-5532-8690
Sasagu Tomioka ® https://orcid.
0rg/0000-0001-6927-2096

REFERENCES

1.

10.

11.

12.

13.

14.

Stirling RE, Maturana MI, Karoly PJ, Nurse ES, McCutcheon
K, Grayden DB, et al. Seizure forecasting using a novel sub-
scalp ultra-long term EEG monitoring system. Front Neurol.
2021;12:713794. https://doi.org/10.3389/fneur.2021.713794
Fisher RS, Blum DE, DiVentura B, Vannest J, Hixson JD, Moss
R, et al. Seizure diaries for clinical research and practice: limita-
tions and future prospects. Epilepsy Behav. 2012;24(3):304-10.
Hannon T, Fernandes KM, Wong V, Nurse ES, Cook MJ.
Over- and underreporting of seizures: how big is the problem?
Epilepsia. 2024;65(5):1406-14.

Kuhlmann L, Karoly P, Freestone DR, Brinkmann BH, Temko
A, Barachant A, et al. Epilepsyecosystem.Org: crowd-sourcing
reproducible seizure prediction with long-term human intra-
cranial EEG. Brain. 2018;141(9):2619-30.

Cook MJ, O'Brien TJ, Berkovic SF, Murphy M, Morokoff A,
Fabinyi G, et al. Prediction of seizure likelihood with a long-
term, implanted seizure advisory system in patients with
drug-resistant epilepsy: a first-in-man study. Lancet Neurol.
2013;12(6):563-71.

Haneef Z, Yang K, Sheth SA, Aloor FZ, Aazhang B, Krishnan
V, et al. Sub-scalp electroencephalography: a next-generation
technique to study human neurophysiology. Clin Neurophysiol.
2022;141:77-87.

Stirling RE, Cook MJ, Grayden DB, Karoly PJ. Seizure forecast-
ing and cyclic control of seizures. Epilepsia. 2021;62:52-S14.
Brinkmann BH, Karoly PJ, Nurse ES, Dumanis SB, Nasseri
M, Viana PF, et al. Seizure diaries and forecasting with wear-
ables: epilepsy monitoring outside the clinic. Front Neurol.
2021;12:690404.

Meisel C, El Atrache R, Jackson M, Schubach S, Ufongene C,
Loddenkemper T. Machine learning from wristband sensor
data for wearable, noninvasive seizure forecasting. Epilepsia.
2020;61(12):2653-66.

Tang J, El Atrache R, Yu S, Asif U, Jackson M, Roy S, et al.
Seizure detection using wearable sensors and machine learn-
ing: setting a benchmark. Epilepsia. 2021;62(8):1807-19.
Vieluf S, Reinsberger C, El Atrache R, Jackson M, Schubach S,
Ufongene C, et al. Autonomic nervous system changes detected
with peripheral sensors in the setting of epileptic seizures. Sci
Rep. 2020;10(1):1-8.

Poh M-Z, Loddenkemper T, Reinsberger C, Swenson NC, Goyal
S, Sabtala MC, et al. Convulsive seizure detection using a wrist-
worn electrodermal activity and accelerometry biosensor.
Epilepsia. 2012;53(5):e93-e97.

Gregg NM, Attia TP, Nasseri M, Joseph B, Karoly P, Cui J, et al.
Seizure occurrence is linked to multiday cycles in diverse phys-
iological signals. Epilepsia. 2023;64:1627-39.

Karoly PJ, Stirling RE, Freestone DR, Nurse ES, Maturana
MI, Halliday AJ, et al. Multiday cycles of heart rate are

9SUD2IT suowwog aaneas) ajqedljdde ayy Aq pausanob aie sajoie YO @SN Jo sa|nJ Joy Aseiqr suljuQ Asjim uo (suol
-pue-swia)/wodKspimAlelqijauljuo//:sdiy) SUOCRIPUOY pue SWLIR] 31 39S *[9Z0Z/L0/50] Uo Ateiqr aulug A3)im ‘ujoy Nz JeusiaAlun Jap °|qig Ag "0558 1 1da/L L L1 0L/10p/wodkepm Aieiqijauljuo//:sdny woiy papeojumoq ‘L1 ‘SZ0Z ‘£9LL8ZSL

---

VIELUF ET AL.

15.

16.

17.

18.

19.

20.

21.

22.

23.

24.

25.

26.

27.

associated with seizure likelihood: an observational cohort
study. EBioMedicine. 2021;72:103619.

Vieluf S, El Atrache R, Hammond S, Touserkani FM,
Loddenkemper T, Reinsberger C. Peripheral multimodal mon-
itoring of ANS changes related to epilepsy. Epilepsy Behav.
2019;96:69-79.

Proix T, Truccolo W, Leguia MG, Tcheng TK, King-Stephens
D, Rao VR, et al. Forecasting seizure risk in adults with focal
epilepsy: a development and validation study. Lancet Neurol.
2021;20(2):127-35.

Vieluf S, Amengual-Gual M, Zhang B, El Atrache R, Ufongene
C, Jackson MC, et al. Twenty-four-hour patterns in electroder-
mal activity recordings of patients with and without epileptic
seizures. Epilepsia. 2021;62(4):960-72.

Vieluf S, El Atrache R, Cantley S, Jackson M, Clark J, Sheehan
T, et al. Seizure-related differences in biosignal 24-h modula-
tion patterns. Sci Rep. 2022;12(1):15070.

Vieluf S, Cantley S, Krishnan V, Loddenkemper T. Ultradian
rhythms in accelerometric and autonomic data vary based
on seizure occurrence in paediatric epilepsy patients. Brain
Commun. 2024;6(2):fcae034.

Vieluf S, Cantley S, Jackson M, Zhang B, Bosl WI,
Loddenkemper T. Development of a multivariable seizure like-
lihood assessment based on clinical information and short au-
tonomic activity recordings for children with epilepsy. Pediatr
Neurol. 2023;148:118-27.

Bottcher S, Vieluf S, Bruno E, Joseph B, Epitashvili N, Biondi A,
et al. Data quality evaluation in wearable monitoring. Sci Rep.
2022;12(1):21412.

Chollet F. Keras. 2015. GitHub. https://github.com/fchollet/
keras

O'Malley T, Bursztein E, Long J, Chollet F, Jin H, Invernizzi
L, et al. Keras Tuner. 2019. https://github.com/keras-team/
keras-tuner

Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B,
Grisel O, et al. Scikit-learn: machine learning in python. J Mach
Learn Res. 2011;12:2825-30.

Karoly PJ, Ung H, Grayden DB, Kuhlmann L, Leyde K, Cook
MJ, et al. The circadian profile of epilepsy improves seizure
forecasting. Brain. 2017;140(8):2169-82.

Karoly PJ, Eden D, Nurse ES, Cook MJ, Taylor J, Dumanis S, et al.
Cycles of self-reported seizure likelihood correspond to yield of
diagnostic epilepsy monitoring. Epilepsia. 2021;62(2):416-25.
Gleichgerrcht E, Dumitru M, Hartmann DA, Munsell BC,
Kuzniecky R, Bonilha L, et al. Seizure forecasting using ma-
chine learning models trained by seizure diaries. Physiol Meas.
2022;43(12):124003.

28.

29.

30.

31.

32.

33.

34.

Epilepsia--~
Al-Bakri AF, Villamar MF, Haddix C, Bensalem-Owen M,
Sunderam S. Noninvasive seizure prediction using autonomic
measurements in patients with refractory epilepsy. In: 2018
40th annual international conference of the IEEE engineer-
ing in medicine and biology society (EMBC). IEEE, pp. 2422-5
2018.

Vieluf S, Hasija T, Schreier PJ, El Atrache R, Hammond S,
Touserkani FM, et al. Generalized tonic-clonic seizures are ac-
companied by changes of interrelations within the autonomic
nervous system. Epilepsy Behav. 2021;124:108321.

Cereghino JJ. Identification and treatment of acute repetitive
seizures in children and adults. Curr Treat Options Neurol.
2007;9(4):249-55.

Goldenholz D, Brinkmann BH, Westover MB. How accurate
do self-reported seizures need to be for effective medication
management in epilepsy? Epilepsia. 2024;65(7):e104-e112.
doi:10.1111/epi.18019

Payne DE, Dell KL, Karoly PJ, Kremen V, Gerla V, Kuhlmann
L, et al. Identifying seizure risk factors: a comparison of sleep,
weather, and temporal features using a Bayesian forecast.
Epilepsia. 2021;62(2):371-82.

Seth EA, Watterson J, Xie J, Arulsamy A, Md Yusof HH,
Ngadimon IW, et al. Feasibility of cardiac-based seizure detec-
tion and prediction: a systematic review of non-invasive wear-
able sensor-based studies. Epilepsia Open. 2024;9(1):41-59.
Miron G, Halimeh M, Jeppesen J, Loddenkemper T, Meisel
C. Autonomic biosignals, seizure detection, and forecasting.
Epilepsia. 2024;1-14. https://doi.org/10.1111/epi.18034

SUPPORTING INFORMATION
Additional supporting information can be found online

in

the Supporting Information section at the end of this

article.

How to cite this article: Vieluf S, Tomioka S,
Zhang B, Krishnan V, Bosl WJ, Grinnell T, et al.
Seizure monitoring by combined diary and wearable
data: A multicenter, longitudinal, observational
study. Epilepsia. 2025;66:4259-4271. https://doi.

org/10.1111/epi.18550

Im°Ateiqijauljuo//:sdny wouy papeojumoq ‘L1 ‘SZ0Z ‘L9L182ZSL

3sudd|T suowiwo) aAneal) ajqeorjdde ayy Aq pausanob ale sajonIe YO ‘sn Jo sajni 1oy Aresqr auuo Aajim uo (suonipuod

-pue-suis)/wodAspmAseiqiiauljuo//:sdily) suonIpuog pue swua) 3y} 93s ‘[920Z/10/50] uo Aseiqiq aunuo Asjim ‘ujoy nz JenssaAun Jap *|qig Ag ‘0558 L 1d3/L L LL 0 L/IOp/WOD