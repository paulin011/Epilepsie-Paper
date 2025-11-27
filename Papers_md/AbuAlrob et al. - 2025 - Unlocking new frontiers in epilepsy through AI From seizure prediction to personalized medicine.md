# AbuAlrob et al. - 2025 - Unlocking new frontiers in epilepsy through AI From seizure prediction to personalized medicine

Epilepsy & Behavior 166 (2025) 110327 

Contents lists available at ScienceDirect

Epilepsy & Behavior

journal homepage: www.elsevier.com/locate/yebeh

Perspective

Unlocking new frontiers in epilepsy through AI: From seizure prediction to 
personalized medicine

Majd A. AbuAlrob a,*, Adham Itbaisha b, Boulenouar Mesraoua a,c
a Neurosciences Department, Hamad Medical Corporation, Doha, Qatar
b Faculty of Medicine, Al-Quds University, Jerusalem, Palestine
c Weill Cornell Medical College, Doha, Qatar

A R T I C L E  I N F O

A B S T R A C T

Keywords:
Artificial Intelligence
Epilepsy
Seizure Detection
Personalized Medicine
Machine Learning
Deep Learning
EEG Analysis
Ethical Considerations
Neurology
Clinical Integration

1. Introduction

Artificial intelligence (AI) is revolutionizing epilepsy care by advancing seizure detection, enhancing diagnostic 
precision,  and  enabling  personalized  treatment.  Machine  learning  and  deep  learning  technologies  improve 
seizure  monitoring, automate  EEG analysis, and facilitate tailored  therapeutic strategies,  addressing the  com-
plexities of epilepsy management. However, challenges remain, including issues of model accuracy, interpret-
ability, and applicability across diverse patient populations. Ethical considerations, such as safeguarding patient 
privacy, ensuring data security, and mitigating algorithmic bias, underscore the importance of responsible AI 
integration. Collaborative efforts among neurologists, data scientists, and regulatory authorities are critical to 
refining models, establishing ethical guidelines, and ensuring safe clinical adoption. This review examines AI’s 
transformative  potential,  its  current  limitations,  and  the  multidisciplinary  initiatives  driving  its  effective 
implementation in epilepsy care.

Epilepsy, affecting over 50 million people worldwide, is a complex 
neurological disorder characterized by recurrent, unprovoked seizures 
[1]. It presents significant diagnostic and treatment challenges due to 
the wide variability in seizure phenotype and etiologies. The disorder 
significantly  impacts  children  and  older  adults.  It  is  associated  with 
psychological, social, and economic hurdles, including stigma, reduced 
quality of life, and sudden unexpected death in epilepsy (SUDEP), which 
is notably higher in individuals with poorly controlled seizures [2,3].

Despite advanced medical technology, diagnosing epilepsy remains 
resource-intensive  and  complex  [4].  Accurate  diagnosis  requires  dis-
tinguishing between epileptic and non-epileptic events such as psycho-
genic  non-epileptic  seizures  (PNES)  or  syncope  [5].  Traditional 
diagnostic EEG and MRI often have limitations in sensitivity and spec-
ificity, particularly during the interictal phase when seizures are absent 
[6].  Approximately  one-third  of  epilepsy  is  drug-resistant,  limiting 
therapy with standard anti-seizure drugs requiring alternative strategies 
[12].

Artificial  Intelligence  (AI)  has  emerged  as  a  tool  to  address 
healthcare challenges [7]. AI refers to the simulation of human intelli-
gence  in  machines,  enabling  tasks  that  typically  require  human 

* Corresponding author.

E-mail address: majdaiabualrob72@gmail.com (M.A. AbuAlrob). 

cognition, such as reasoning, learning, and decision-making [12]. Using 
of  AI  in  healthcare  began  with  expert  systems  like  INTERNIST-1  and 
MYCIN in the 1970 s and 1980 s, which used rule-based logic to assist in 
diagnosis but lacked adaptability [20,21]. Machine Learning (ML), Deep 
Learning (DL), Natural Language Processing (NLP), and Robotic Process 
Automation (RPA) are key advance AI technologies that play a signifi-
cant role in epilepsy care [13]. ML employs algorithms to analyze data, 
identify patterns, and make predictions as shown in Fig. 1. In epilepsy 
management,  ML  algorithms  are  crucial  for  detecting  and  predicting 
seizure  activity  through  EEG  analysis,  enabling  the  development  of 
personalized seizure prediction models trained on patient-specific data 
[11].  While  larger  datasets  improve  ML  performance  by  capturing 
seizure pattern variability, smaller datasets can still be effectively uti-
lized through techniques like data augmentation and transfer learning 
[11]. DL, a more advanced subset of ML, leverages deep neural networks 
to process complex, high-dimensional data such as EEG recordings and 
neuroimaging scans (MRI, PET) [22]. Convolutional Neural Networks 
(CNNs) and Recurrent Neural Networks (RNNs) are commonly applied 
in  epilepsy  care  to  identify  epileptogenic  zones  and  enhance  seizure 
detection as shown in Fig. 2 [23]. However, NLP facilitates the inter-
pretation of unstructured clinical data, including electronic health re-
cords (EHRs), physician notes, and research articles, helping clinicians 

https://doi.org/10.1016/j.yebeh.2025.110327
Received 2 November 2024; Received in revised form 19 January 2025; Accepted 18 February 2025  
Available online 4 March 2025 
1525-5050/© 2025 The Author(s). Published by Elsevier Inc. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ). 

M.A. AbuAlrob et al.                                                                                                                                                                                                                           

Epilepsy & Behavior 166 (2025) 110327 

(caption on next page)

2 

M.A. AbuAlrob et al.                                                                                                                                                                                                                           

Epilepsy & Behavior 166 (2025) 110327 

Fig. 1. Workflow of machine learning in healthcare. Overview of the Machine Learning Workflow. The figure illustrates the iterative process involved in developing 
a machine learning model. The steps include: 1. Data Collection: Gathering relevant data from various sources. 2. Clean and Prepare the Data: Preprocessing the data 
to handle missing values, remove noise, and ensure quality for modeling. 3. Split the Data into Training, Validation, and Testing Sets: Dividing the data into subsets 
for training, tuning, and evaluating the model. 4. Train the Model: Using the training data to teach the machine learning algorithm. 5. Validate the Model: Fine-tuning 
the model using the validation set to ensure it generalizes well. 6. Test the Model: Evaluating the model’s performance on an unseen testing dataset to assess its 
accuracy and robustness. 7. Deploy into Real-World Uses: Applying the trained and tested model to practical applications. 8. Iterative Loop: Feedback from the 
deployment or testing phase is used to refine the model by revisiting earlier steps (e.g., improving data collection or retraining the model).

identify seizure trends, treatment responses, and adverse events [24]. 
Additionally,  NLP  supports  medical  coding  and  documentation,  opti-
mizing  administrative  workflows  [24].  Lastly,  RPA  automates  repeti-
tive,  rule-based  administrative  tasks  such  as  scheduling,  billing,  and 
data  entry,  reducing  clinicians’  workload  and  improving  healthcare 
system  efficiency  [25].  Although  RPA  does  not  directly  contribute  to 
epilepsy  diagnosis  or  treatment,  it  enhances  overall  patient  care  by 
streamlining  hospital  operations  and  improving  access  to  resources 
[26]. Together, these AI technologies contribute to more effective epi-
lepsy  management,  advancing  both  clinical  decision-making  and 
healthcare efficiency [10].

In the context of epilepsy, AI technologies enable more accurate 
detection,  prediction,  and  personalized  treatment  plans.  AI-driven 
seizure detection algorithms, for example, can analyze EEG patterns in 
real time, improving monitoring for patients who need continuous sur-
veillance [10]. In healthcare, ML is especially valuable for data analysis, 
such as predicting seizure occurrences and identifying patterns in EEG 
signals,  allowing  for  proactive  management  and  enhancing  patient 
safety [11]. Unlike traditional AI, which may rely on rule-based systems, 
ML  models  improve  their  accuracy  as  they  are  exposed  to  more  data 
[10]. DL can play a transformative role in personalized medicine; by 
using patient-specific data—including clinical profiles, genetic markers, 
and previous treatment responses—AI can tailor treatment plans more 
effectively  [9].  This  personalized  approach  can  reduce  the  trial-and- 
error  process  typically  associated  with  anti-seizure  medication  (ASM) 
selection,  especially  in  resistant  cases,  minimizing  side  effects  and 
improving patient outcomes [10].

This review explores the transformative potential of Artificial Intel-
ligence (AI) in epilepsy diagnosis, treatment, and management. It begins 
by examining AI’s role in seizure detection and prediction, where ma-
chine learning and deep learning algorithms improve the identification 
of seizure onset and patient monitoring. The review also highlights AI’s 
contribution to personalized treatment, tailoring plans based on patient 
data such as genetic markers, clinical history, and medication responses. 
It then addresses the ethical challenges of implementing AI in epilepsy 
care,  including  concerns  around  privacy,  data  security,  transparency, 
and algorithmic bias. These issues are crucial for maintaining trust in AI- 
driven decision-making. Lastly, the review discusses regulatory consid-
erations, particularly the role of the FDA and other bodies in ensuring AI 
tools  meet  safety  and  efficacy  standards.  Emphasizing  the  need  for 
collaboration  among  neurologists,  data  scientists,  and  regulators,  this 
review provides a comprehensive overview of AI’s potential, its current 
limitations, and the steps for responsible clinical integration in epilepsy 
care.

2. Epilepsy overview and clinical challenges

Epilepsy is a complex neurological disorder characterized by recur-
rent,  unprovoked  seizures  due  to  abnormal  electrical  activity  in  the 
brain  [12].  The  condition’s  pathophysiology  is  highly  heterogeneous, 
arising from diverse etiologies, including genetic, structural, metabolic, 
and  traumatic  factors,  leading  to  varied  clinical  manifestations  [13]. 
Seizures can be focal, generalized, or absent, presenting different chal-
lenges for accurate diagnosis and treatment [12]. For a more in-depth 
discussion  of  epilepsy’s  pathophysiology  and  epidemiology,  see  Sup-
plementary Materials.

Epilepsy affects approximately 1 % of the global population, with a 
higher prevalence in children and older adults [14]. The disease poses 

Fig. 2. Comparative workflows of CNNs and RNNs for epilepsy-related tasks. 
This figure compares the workflows of Recurrent Neural Networks (RNNs) and 
Convolutional  Neural  Networks  (CNNs).  RNNs  process  sequential  data  one 
element  at  a  time,  maintaining  memory  through  hidden  states  to  produce 
outputs based on temporal dependencies. In contrast, CNNs process pixel data 
by applying convolutional filters to detect spatial patterns, followed by pooling 
to reduce dimensionality and fully connected layers for classification.

3 

M.A. AbuAlrob et al.                                                                                                                                                                                                                           

Epilepsy & Behavior 166 (2025) 110327 

significant  clinical  challenges,  particularly  in  accurately  diagnosing 
epilepsy and distinguishing it from conditions with similar symptoms, 
such as psychogenic non-epileptic seizures (PNES), syncope, and certain 
types of migraines [16]. This difficulty is compounded by the limited 
sensitivity and specificity of traditional diagnostic tools like electroen-
cephalography (EEG), magnetic resonance imaging (MRI), and positron 
emission tomography (PET), especially when seizures are infrequent or 
absent  during  testing  [17].  Epilepsy  patients  are  considered  drug- 
resistant,  meaning  that  they  do  not  respond  to  conventional  antisei-
zure medications (ASMs) [15]. These patients often require alternative 
treatments  such  as  neurostimulation,  surgery,  or  dietary  therapies, 
which  may  not  be  universally  effective  or  suitable  for  all  individuals 
[18].  Despite  the  conventions,  they  often  involve  complex  decision- 
making and considerable risks. The trial-and-error approach for select-
ing the most effective ASM for patients remains a significant hurdle in 
epilepsy care [19].

AI  offers  promising  solutions  by  improving  the  accuracy  and  effi-
ciency of epilepsy diagnosis and management. Machine learning (ML) 
and deep learning (DL) algorithms can assist in automating EEG anal-
ysis, predicting seizure onset, and personalizing treatment plans based 
on individual patient data. These advancements in AI are particularly 
crucial in epilepsy, where personalized treatment strategies may reduce 
the reliance on trial-and-error methods and improve patient outcomes.

3. AI applications in epilepsy diagnostics

3.1. Automated EEG analysis

Automated  EEG  analysis,  powered  by  AI,  has  brought  significant 
advancements to epilepsy diagnostics, enabling the detection of seizure 
patterns  with  improved  speed  and  accuracy.  Convolutional  neural 
networks  (CNNs)  and  support  vector  machines  (SVMs)  are  widely 
used in analyzing EEG data, each offering unique strengths in capturing 
the complex patterns associated with epileptic activity. CNNs are espe-
cially effective in identifying spatial patterns within EEG signals, while 
SVMs excel in handling high-dimensional data and are robust against 
overfitting, which is crucial for medical applications. These models aid 
clinicians  by  processing  vast  amounts  of  EEG  data  quickly,  which  re-
duces diagnostic times and improves seizure monitoring, especially in 
patients requiring long-term, real-time monitoring.[27].

Models such as SPaRCNet (Seizure Prediction and Reliable Con-
trol Network) and SCORE-AI (Standardized Computer-based Orga-
nized Reporting of EEG) are examples of advanced AI systems designed 
for epilepsy. SPaRCNet has shown potential in predicting seizure onset 
with high sensitivity, while SCORE-AI offers a standardized system for 
reporting  EEG  results,  improving  consistency  and  accuracy  across 
diagnostic  settings.  However,  these  models  have  limitations.  While 
SPaRCNet performs well in controlled environments, its sensitivity can 
drop in diverse, real-world clinical settings. SCORE-AI, despite its ben-
efits, may sometimes produce false positives, which can lead to unnec-
essary treatment adjustments.[28,29].

3.2. Sensitivity and specificity Metrics

Performance metrics like sensitivity (the model’s ability to correctly 
identify actual seizures) and specificity (its ability to avoid false alarms) 
are  essential  for  assessing  AI  effectiveness  in  epilepsy  diagnostics.  In 
recent  studies,  CNN-based  models  achieved  sensitivity  rates  up  to 
85–90 % and specificity rates around 80–85 % in controlled datasets, 
illustrating their accuracy in detecting seizures. [30]However, in real- 
world scenarios, where factors like signal noise and patient variability 
affect readings, these metrics often fluctuate, underscoring the need for 
continuous  refinement  and  validation.  SVM-based  models  also  show 
high sensitivity but may struggle with specificity, especially in complex 
cases with overlapping seizure-like symptoms.[31].

4 

3.3. AI for functional imaging (MRI, PET)

AI has also demonstrated considerable utility in analyzing functional 
imaging  data,  such  as  MRI  and  PET  scans,  to  identify  epileptogenic 
zones—the areas in the brain responsible for generating seizures. Deep 
learning models like CNNs and autoencoders are particularly effective 
in  processing  high-resolution  imaging  data,  capturing  subtle  abnor-
malities  that  can  be  difficult  for  clinicians  to  identify  manually.  For 
example, AI models trained on large sets of MRI data can identify hip-
pocampal  sclerosis,  cortical  dysplasia,  and  other  structural  brain 
anomalies  associated  with  epilepsy,  which  are  often  missed  by  tradi-
tional visual analysis.[32].

Compared to traditional imaging techniques, AI-driven approaches 
offer several advantages. Traditional methods rely on manual interpre-
tation  by  radiologists  and  neurologists,  which  can  be  subjective  and 
influenced by clinician experience. AI models, on the other hand, can 
process thousands of images quickly, providing consistent and objective 
assessments  that  aid  in  pinpointing  epileptogenic  zones  with  higher 
precision.  In  clinical  studies,  AI  models  analyzing  MRI  data  achieved 
diagnostic accuracy rates between 75 % and 90 %, significantly higher 
than  the  typical  accuracy  rates  of  manual  interpretation  alone.  [33]
However, AI’s reliance on large, high-quality datasets for training is a 
limitation, as variations in scanner quality, imaging protocols, and pa-
tient populations can affect model performance.[34].

3.4. Comparison with traditional diagnostic Methods

The integration of AI with traditional diagnostic methods like EEG, 
MRI, and PET improves diagnostic accuracy by combining the strengths 
of automated pattern recognition with conventional expert analysis. In 
traditional  methods,  the  accuracy  of  epilepsy  diagnosis  can  be  influ-
enced  by  various  factors,  including  clinician  experience,  the  duration 
and quality of EEG monitoring, and the availability of advanced imaging 
technologies. AI algorithms, by contrast, systematically analyze EEG and 
imaging  data,  identifying  patterns  that  may  escape  human  detection, 
thus enhancing the reliability of diagnostic results.[35].

Studies comparing AI-augmented EEG and imaging with traditional 
diagnostics reveal that AI improves overall diagnostic sensitivity, espe-
cially in cases with atypical presentations. For instance, AI-integrated 
systems can increase seizure detection rates by 20–30 % compared to 
conventional EEG analysis alone, making it a valuable tool for complex 
cases or when expert resources are limited [70–75]. Despite these ad-
vantages, AI models face challenges related to data generalization, as 
models  trained  on  one  dataset  may  not  perform  consistently  across 
different  patient  demographics  or  clinical  settings.  Additionally,  the 
“black box” nature of many AI models, where decision-making processes 
are not fully transparent, can hinder clinician trust and adoption.[36].

3.5. Limitations of AI diagnostics

The  effectiveness  of  AI  diagnostics  in  epilepsy  is  contingent  upon 
access to large, diverse datasets for training and validation. However, 
gathering such data is challenging due to differences in equipment, EEG 
and  imaging  protocols,  and  population  demographics  across  in-
stitutions. Additionally, the complexity of some AI models creates “black 
box” issues, where the internal decision-making processes of models are 
not fully interpretable. This lack of transparency can make it difficult for 
clinicians to validate AI recommendations and raises ethical questions 
about  responsibility  in  cases  of  misdiagnosis.  Finally,  generalizing  AI 
models across varied clinical settings remains a hurdle, as model per-
formance  may  drop  when  applied  to  patient  populations  or  environ-
ments different from those in the training data.[37].

M.A. AbuAlrob et al.                                                                                                                                                                                                                           

Epilepsy & Behavior 166 (2025) 110327 

4. AI in epilepsy treatment and management

4.1. Ai-driven personalized Treatments

Personalized  medicine  is  a  crucial area  where  AI  can significantly 
impact epilepsy treatment by customizing antiseizure medication (ASM) 
plans to individual patients’ needs. Traditional ASM selection often in-
volves a trial-and-error process, where  patients cycle through various 
drugs and dosages to find an effective regimen, which can be a lengthy 
and frustrating process. AI models analyze large sets of patient-specific 
data, including genetic information, seizure history, and treatment re-
sponses, to predict the most effective ASM regimen for a particular in-
dividual.  By  leveraging  this  data,  AI  can  help  clinicians  make  more 
informed  decisions,  reducing  the  need  for  repeated  trial-and-error 
treatments.[38,39].

In  this  context, predictive  models  have  shown promising  results. 
For instance, machine learning algorithms trained on genetic markers 
and clinical data have demonstrated accuracy rates of up to 70–80 % in 
predicting  ASM  efficacy  for specific  patient profiles.  However,  imple-
menting  these  models  in  clinical  practice  requires  robust  regulatory 
oversight to ensure that predictions are reliable and that models do not 
introduce biases based on incomplete or skewed datasets.[40].

4.2. Regulatory Guidelines

The FDA has introduced guidelines for AI and machine learning in 
healthcare,  specifically  regarding  tools  that  are  intended  for  direct 
clinical  use.  For  epilepsy,  the  FDA  requires  that  AI-based  treatment 
models  meet  rigorous  safety,  efficacy,  and  transparency  standards 
before  they  can  be  implemented  in  patient  care.  These  guidelines 
emphasize  the  importance  of  real-world  validation,  model  interpret-
ability, and patient safety, all of which are critical in high-stakes areas 
like  epilepsy  treatment.  Additionally,  continuous  monitoring  and 
updating of AI models are recommended to ensure that predictive tools 
remain accurate as new data becomes available.[41,42].

approach  aligns  with  precision  medicine,  as  it  customizes  treatment 
based on each patient’s unique biological and clinical profile.[45].

Challenges  in  predictive  modeling  for  ASM  response  include  data 
heterogeneity and the need for continuous validation as new genetic and 
clinical  data  emerge.  Patient  genetics,  for  instance,  play  a  significant 
role  in  drug  metabolism  and  efficacy,  but  current  datasets  may  not 
capture the full range of genetic variability across diverse populations.
[46] As a result, predictive models must be regularly updated to ensure 
that they remain relevant and accurate for broader patient populations. 
Additionally, differences in treatment protocols and drug formulations 
across institutions can further complicate model generalization, under-
scoring the need for adaptable models that can be fine-tuned to indi-
vidual healthcare settings.[47].

4.5. Challenges in predictive Modeling

While  predictive  modeling  holds  great  promise,  it  faces  several 
technical and logistical hurdles. Data heterogeneity, or the variation in 
data types and sources, is a primary challenge. AI models rely on diverse 
datasets that encompass genetic, clinical, and demographic information, 
but inconsistencies in these data points can limit model accuracy. For 
instance, genetic markers may vary across ethnicities, making it difficult 
for a single model to generalize across diverse populations. Similarly, 
models  trained  in  one  clinical  environment  may  not  perform  equally 
well in another, where treatment protocols and patient demographics 
differ.[48].

Another  challenge  is  the  need  for  continuous  validation  and 
recalibration. Predictive models are dynamic and must be frequently 
updated with new patient data to maintain their accuracy. This ongoing 
validation  is  resource-intensive  and  requires  collaborations  across  in-
stitutions  to  aggregate  high-quality  data.  Furthermore,  as  predictive 
models become more integral to treatment planning, there is a need for 
ethical oversight to ensure that decisions remain patient-centered and 
that AI predictions do not inadvertently reinforce biases or exacerbate 
healthcare disparities.[49].

4.3. Responsive neurostimulation (RNS)

5. Ethical and practical challenges

Responsive neurostimulation (RNS) systems represent an innovative 
application  of  AI  in  epilepsy  treatment,  particularly  for  patients  with 
drug-resistant epilepsy. RNS devices, such as the NeuroPace RNS Sys-
tem, are implantable devices that monitor brain activity in real-time and 
deliver electrical stimulation to interrupt seizure activity. AI enhances 
these systems by analyzing EEG data to identify seizure onset patterns, 
enabling the  device to  provide timely interventions that may  prevent 
seizure progression.[43].

Recent studies have demonstrated the effectiveness of RNS systems 
in reducing seizure frequency among patients with refractory epilepsy, 
with some patients achieving seizure reductions of up to 50 %. How-
ever,  the  efficacy  of  RNS  devices  can  be  limited  by  factors  such  as 
patient-specific  seizure  patterns  and  the  need  for  precise  device  pro-
gramming,  which  often  requires  continuous  adjustments.  Regulatory 
approvals for RNS devices highlight the importance of long-term safety 
data, particularly because these devices are invasive and require surgical 
implantation. Additionally, the cost and complexity of RNS systems can 
limit  their  accessibility,  creating  practical  barriers  to  widespread 
adoption.[44].

4.4. Predicting drug Responses

AI also has the potential to predict individual responses to ASMs, a 
critical  capability  given  that  approximately  one-third  of  epilepsy  pa-
tients are resistant to commonly used medications. By analyzing genetic 
data, clinical history, and seizure characteristics, AI models can estimate 
the  likelihood  of  a  patient’s  response  to  specific  ASMs,  potentially 
reducing the time and cost associated with ineffective treatments. This 

5.1. Interpretability of AI models

One of the critical ethical concerns in AI applications for epilepsy is 
the interpretability of AI models, especially in clinical neurology. Many 
AI  models,  particularly  deep  learning  algorithms,  function  as  “black 
boxes” with complex inner workings that even experts struggle to fully 
understand. While these models can offer highly accurate predictions, 
their opacity raises concerns in a clinical context where understanding 
the  rationale  behind  diagnostic  or  therapeutic  recommendations  is 
crucial. [50]Clinicians and patients alike require transparency to trust 
AI-driven outcomes, particularly in high-stakes conditions like epilepsy, 
where treatment decisions carry substantial risks. Transparent models 
allow  healthcare  providers  to  understand  the  reasoning  behind  AI- 
generated insights, fostering informed decision-making that is aligned 
with patient safety and ethical standards.[51].

To  improve  interpretability,  several  techniques  are  emerging, 
including  explainable  AI  (XAI),  which  aims  to  create  models  that 
provide clear  explanations for  their outputs. [51]XAI frameworks  use 
tools like heat maps, feature importance scores, and simplified surrogate 
models  that  approximate  complex  models  while  remaining  interpret-
able.  By  providing  clinicians  with  insights  into  how  AI  models  reach 
their conclusions, these methods  aim to bridge the gap between high 
performance  and  transparency,  ensuring  that  AI-enhanced  decision- 
making remains clinically and ethically sound.[52,53].

5.2. Algorithm bias and Equity

Bias in AI algorithms presents another significant ethical challenge, 

5 

M.A. AbuAlrob et al.                                                                                                                                                                                                                           

Epilepsy & Behavior 166 (2025) 110327 

with potential to exacerbate existing health disparities in epilepsy care. 
AI  models  are  highly  dependent  on  the  quality  and  diversity  of  their 
training data. When data from certain demographic groups are under-
represented, AI algorithms may develop biases that reduce the accuracy 
and reliability of predictions for those populations. [54]For instance, if 
an  AI  model  for  epilepsy  diagnosis  is  trained  primarily  on  data  from 
adults, its accuracy may decrease when applied to children, who exhibit 
different  seizure  characteristics.  Similarly,  ethnic  minorities  and  low- 
income patients are often underrepresented in clinical datasets, which 
can  lead  to  AI  models  that  are  less  effective  or  even  harmful  when 
applied to these groups.[55].

Mitigating  bias  requires  concerted  efforts  to  ensure  diverse  and 
representative  datasets.  Strategies  to  reduce  bias  include  data 
augmentation,  collecting  data  from  underrepresented  groups,  and 
employing  fairness-enhancing  algorithms  that  actively  counteract 
learned biases. Collaborative research efforts across institutions are also 
essential  to  create  large,  representative  datasets  that  capture  a  wide 
range  of  patient  characteristics.[56] Additionally,  algorithmic  audi-
ting—regular  evaluations  to  identify  and  correct  biases  in  AI  mod-
els—can help ensure that these technologies are equitable and do not 
contribute to systemic inequalities in healthcare.[57].

5.3. Data Privacy

Data privacy is paramount when implementing AI systems that use 
sensitive patient information, such as EEG recordings, genetic data, and 
clinical history. The large-scale data requirements of AI often necessitate 
pooling information from multiple sources, increasing the risk of data 
breaches  and  unauthorized  access.  Moreover,  the  sensitive  nature  of 
epilepsy-related data, which may include information on seizure history, 
treatment responses, and personal health behaviors, makes it essential to 
maintain robust privacy protections to safeguard patient trust.[58].

Guidelines  and  regulations  like  the  General  Data  Protection 
Regulation (GDPR) in Europe and the Health Insurance Portability 
and  Accountability  Act  (HIPAA)  in  the  United  States  outline  strict 
requirements for data security and patient privacy in healthcare. [59]
These regulations mandate data anonymization, controlled access, and 
encryption to protect patient information. Privacy-preserving AI tech-
niques,  such  as  federated  learning  and  differential  privacy,  are 
emerging  solutions  that  allow  AI  models  to  train  on  data  without 
directly  accessing  patient  information.  These  approaches  ensure  that 
sensitive data remains on local devices, and only aggregated insights are 
shared, minimizing privacy risks. For AI in epilepsy to gain widespread 
acceptance, it is essential to adopt these privacy-preserving technologies 
and  comply  with  established  guidelines  to  protect  patient  data  and 
maintain public trust.[60].

5.4. Regulatory and legal Concerns

The rapid integration of AI into healthcare has raised regulatory and 
legal challenges, particularly concerning the accountability and safety of 
AI-driven decisions. The U.S. Food and Drug Administration (FDA), 
along with similar regulatory bodies globally, has recognized the need to 
develop standards for AI applications in clinical settings. [61]The FDA’s 
framework for AI-based software in healthcare emphasizes the need for 
transparency,  real-world  validation,  and  continuous  monitoring  to 
ensure that AI systems perform safely and effectively. However, regu-
latory guidelines are still evolving, and inconsistencies between coun-
tries can complicate the deployment of AI models in epilepsy care.[62].
A major regulatory concern is the issue of accountability. In cases 
where  AI-driven  decisions  result  in  adverse  outcomes,  it  is  unclear 
whether  the  responsibility  lies  with  the  developers,  the  healthcare 
providers, or the institution. Establishing standardized guidelines that 
clarify accountability in such cases is critical to protect both patients and 
providers.  Additionally,  ensuring  that  AI  models  undergo  rigorous 
testing across diverse patient populations before clinical deployment is 

essential  to  prevent  unintended  consequences.  As  AI  continues  to 
advance, regulatory frameworks will need to evolve in tandem to ensure 
that AI applications in epilepsy are both effective and ethically sound.
[63].

6. Future Directions and research needs

6.1. Improving model accuracy and generalizability

To  enhance  the  clinical  utility  of  AI  in  epilepsy  care,  ongoing 
research must address the challenges of model accuracy and generaliz-
ability. Current AI models may perform well in controlled settings but 
often  struggle  with  the  variability  encountered  in  real-world  clinical 
environments. For instance, seizure detection models trained on specific 
patient  data  may  not  generalize  effectively  to  patients  with  different 
seizure  characteristics  or  comorbid  conditions.  To  improve  accuracy, 
future  research  should  focus  on  developing  more  robust  algorithms 
capable  of adapting  to  diverse patient  populations  and  handling data 
variability. Techniques such as transfer learning, which allows models 
to apply knowledge from one domain to another, could be instrumental 
in improving generalizability.[64].

Further, research into interpretability-focused AI, such as explain-
able models and transparent neural networks, can provide clinicians 
with insights into model reasoning. This is particularly relevant in epi-
lepsy,  where  understanding  the  basis  for  a  model’s  prediction  (e.g., 
seizure  prediction  or  drug  response)  is  crucial  for  clinical  decision- 
making.  Developing  models  that  are  both  accurate  and  interpretable 
will  be  key  to  fostering  trust  and  acceptance  among  healthcare  pro-
viders.[52].

6.2. Closed-Loop Systems

Closed-loop neurostimulation devices represent a promising future 
direction for epilepsy treatment, allowing real-time, adaptive interven-
tion based on AI-driven insights. Unlike open-loop systems, which pro-
vide continuous or intermittent stimulation without feedback,  closed- 
loop  systems  monitor  brain  activity  and  deliver  targeted  stimulation 
when  abnormal  patterns  are  detected.[65] AI  algorithms  embedded 
within these devices analyze EEG data in real-time to detect early signs 
of seizure onset, enabling immediate intervention that can potentially 
halt seizure progression.[66].

As AI-driven closed-loop systems evolve, they offer a high level of 
personalization, tailoring interventions to each patient’s unique brain 
activity  patterns.  Research  into  adaptive  algorithms  that  learn  from 
patient responses over time will be critical in enhancing these systems. 
Such systems could eventually revolutionize epilepsy care by providing 
a continuous, personalized approach to seizure management. However, 
challenges remain in refining these algorithms to ensure high accuracy, 
reliability, and regulatory approval, as real-time therapeutic decisions 
carry significant risks.[67].

6.3. AI in genomics and Wearables

The  integration  of  AI  with  genomics  and  wearable  devices  offers 
significant potential for enhancing epilepsy management. Genomic data 
can reveal insights into an individual’s predisposition to certain types of 
epilepsy, drug responses, and potential adverse reactions. AI algorithms 
can  analyze  genetic  markers  to  help  predict  epilepsy  onset  and 
customize  treatment  plans,  tailoring  interventions  to  each  patient’s 
unique  genetic  profile.  This  precision-medicine  approach  could prove 
invaluable  for  patients  with  drug-resistant  epilepsy,  where  standard 
treatments are often ineffective.[55].

Wearable devices, such as smartwatches equipped with EEG sensors, 
heart rate monitors, and accelerometers, provide a continuous stream of 
physiological data, enabling real-time seizure detection and monitoring. 
When  integrated  with  AI,  these  devices  can  predict  seizure  onset, 

6 

M.A. AbuAlrob et al.                                                                                                                                                                                                                           

Epilepsy & Behavior 166 (2025) 110327 

alerting patients and caregivers to take preventive action. As wearable 
technology becomes more advanced, research into combining genomic 
data with real-time physiological monitoring could allow AI to create 
comprehensive  patient  profiles,  resulting  in  even  more  precise  and 
responsive epilepsy management.[8].

Declaration of competing interest

The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.

6.4. Advancements in ethical and regulatory Frameworks

References

For AI to reach its full potential in epilepsy care, advancements in 
ethical  and  regulatory  standards  are  essential.  Current  frameworks, 
while foundational, often lack specific guidelines for the nuances of AI in 
neurology, such as interpretability, bias mitigation, and patient privacy 
in  epilepsy-related  data.  Developing  ethical  frameworks  that  address 
these issues will ensure that AI technologies are used responsibly and 
equitably.[68].

Further,  regulatory  bodies  need  to  establish  clear  guidelines  that 
address  the  accountability  and  transparency  of  AI  systems.  With  AI 
systems increasingly involved in clinical decision-making, it is crucial to 
ensure that these systems meet rigorous standards for safety, efficacy, 
and  equity.  Collaboration  between  regulatory  authorities,  healthcare 
professionals, and AI developers is key to creating adaptable standards 
that  can  keep  pace  with  technological  advancements.  By  establishing 
comprehensive ethical and regulatory frameworks, the field can foster 
an environment where AI technologies enhance patient care while up-
holding the highest standards of safety and ethics.[69].

7. Conclusion

Artificial intelligence is transforming the landscape of epilepsy care 
by enabling more accurate diagnosis, personalized treatment, and pro-
active  management  strategies.  Through  advanced  data  analytics  and 
machine learning algorithms, AI offers the potential to improve seizure 
detection,  automate  EEG  interpretation,  predict  patient-specific  drug 
responses, and support real-time intervention with closed-loop systems. 
These applications address many of the persistent challenges in epilepsy 
care, such as the complexity of accurate diagnosis, the trial-and-error 
approach of antiseizure medication selection, and the need for contin-
uous monitoring in drug-resistant cases.

Despite these advancements, significant challenges remain in inte-
grating AI safely and effectively into clinical practice. Issues related to 
model interpretability, algorithmic bias, and data privacy highlight the 
need for transparent and equitable AI solutions. Furthermore, regulatory 
and ethical frameworks must evolve alongside AI technologies to ensure 
patient safety, accountability, and fairness. Regulatory bodies like the 
FDA  are  beginning  to  establish  guidelines  for  AI  applications  in 
healthcare,  but  ongoing  collaboration  between  neurologists,  data  sci-
entists,  and  policymakers  is  essential  to  develop  comprehensive  stan-
dards for AI in epilepsy.

Looking forward, future research should prioritize model generaliz-
ability, the development of interpretable AI systems, and the integration 
of  multimodal  data  from  genomics,  imaging,  and  wearables.  By 
advancing these areas and addressing ethical and regulatory consider-
ations, the field of epilepsy care can harness AI’s full potential to provide 
safer, more effective, and personalized patient care. Through a multi-
disciplinary  effort,  AI-driven  epilepsy  management  could  shift  from 
potential to practice, offering a profound impact on patient outcomes 
and quality of life.

CRediT authorship contribution statement

Majd  A.  AbuAlrob:  Writing  –  original  draft,  Conceptualization. 
Adham  Itbaisha:  Writing  –  original  draft,  Conceptualization.  Boule-
nouar Mesraoua: Writing – review & editing.

[1] “Global Epilepsy Report; 2019”.
[2] Assadsangabi R et al. Update on adult epilepsy: what neuroradiologists should 

know.

[3] Devinsky O, Friedman D, Cheng JY, Moffatt E, Kim A, Tseng ZH. Underestimation 

of sudden deaths among patients with seizures and epilepsy.

[4] Harris L, Angus-Leppan H. Epilepsy: diagnosis, classification and management.
[5] Atwood AC, Drees CN. Seizure detection devices.
[6] Benbadis SR et al. Putting it all together: options for intractable epilepsy.
[7] Tveit J et al. Automated interpretation of clinical electroencephalograms using 

artificial intelligence.

[8] Saeizadeh A et al. SeizNet: an AI-enabled implantable sensor network system for 

seizure prediction.

[9] M. I. Ahmed, B. Spooner, J. Isherwood, M. A. Lane, E. Orrock and A. R. Dennison, 

“A Systematic Review of the Barriers to the Implementation of Artificial 
Intelligence in Healthcare”.

[10] Alowais SA et al. Revolutionizing healthcare: the role of artificial intelligence in 

clinical practice.

[11] A. L. N. Al-hajjar and A. K. M. Al-Qurabat, “An overview of machine learning 

methods in enabling IoMT-based epileptic seizure detection”.

[12] Falco-Walter J. Epilepsy—definition, classification, pathophysiology, and 

epidemiology.

[13] Beghi E. The epidemiology of epilepsy.
[14] Sen A, Jett´e N, Husain M, Sander JW. Epilepsy in older people.
[15] M. M. Watila, S. A. Balarabe, O. Ojo, M. R. Keezer and J. W. Sander, “Overall and 

cause-specific premature mortality in epilepsy: A systematic review”.
[16] M. Zhou et al., “Epileptic Seizure Detection Based on EEG Signals and CNN”.
[17] K. Lee, H. Jeong, S. Kim, D. Yang, H. Kang and E. Choi, “Real-Time Seizure 

Detection using EEG: A Comprehensive Comparison of Recent Approaches under a 
Realistic Setting”.

[18] C. Santana-Gomez, J. Engel and R. J. Staba, “Drug-resistant epilepsy and the 
hypothesis of intrinsic severity: What about the high-frequency oscillations?”.
[19] D. Guery and S. Rheims, “Clinical Management of Drug Resistant Epilepsy: A 

Review on Current Strategies”.

[20] R. A. Miller, H. E. Pople and J. D. Myers, “Internist-I, an Experimental Computer- 

Based Diagnostic Consultant for General Internal Medicine”.

[21] V. L. Yu et al., “Evaluating the performance of a computer-based consultant”.
[22] F. Wei, J. Mo, Q. Zhang, H. Shen, S. S. Nagarajan and F. Jiang, “Nested Deep 

Learning Model Towards A Foundation Model for Brain Signal Data”.

[23] A. Saeizadeh et al., “SeizNet: An AI-enabled Implantable Sensor Network System 

for Seizure Prediction”.

[24] W. Ge et al., “Improving Neurology Clinical Care With Natural Language 

Processing Tools”.

[25] “Robotic Process Automation: An Overview and Comparison to Other Technology 

in Industry 4.0”.

[26] R. Swetha, P. Pavithra, S. Prathiksha and S. Selvakanmani, “Robotic Process 

Automation (RPA) in Healthcare”.

[27] R. C. Hogan et al., “Scaling convolutional neural networks achieves expert-level 

seizure detection in neonatal EEG”.

[28] J. Jing et al., “Development of Expert-Level Classification of Seizures and Rhythmic 

and Periodic Patterns During EEG Interpretation”.

[29] S. Beniczky et al., “Standardized Computer-based Organized Reporting of EEG: 

SCORE”.

[30] H. Albaqami, G. M. Hassan and A. Datta, “MP-SeizNet: A multi-path CNN Bi-LSTM 

Network for seizure-type classification using EEG”.

[31] Z. Wang, J. Yang, H. Wu, J. Zhu and M. Sawan, “Power efficient refined seizure 

prediction algorithm based on an enhanced benchmarking”.

[32] M. M. R. Siddiquee et al., “Brainomaly: Unsupervised Neurologic Disease Detection 

Utilizing Unannotated T1-weighted Brain MR Images”.

[33] C. A. J. R. R. B. E. R. T. K. S. S. D. D. L. G. R. E. W. J. A. A. C. V. K. I. K. E. W. B. M. 
C. G. E. B. Leonardo, “MRI-based deep learning can discriminate between temporal 
lobe epilepsy, Alzheimer’s disease, and healthy controls - Communications 
Medicine”.

[34] N. G. Nia, E. Kaplano˘glu and A. Nasab, “Evaluation of artificial intelligence 

techniques in disease diagnosis and prediction”.

[35] K. Saab, S. Tang, M. Taha, C. Lee-Messer, C. R´e and D. L. Rubin, “Towards 

trustworthy seizure onset detection using workflow notes”.

[36] A. Aldoseri, K. Al-Khalifa and A. Hamouda, “Re-Thinking Data Strategy and 

Integration for Artificial Intelligence: Concepts, Opportunities, and Challenges”.

[37] M. A. AbuAlrob and B. Mesraoua, “Harnessing artificial intelligence for the 

diagnosis and treatment of neurological emergencies: a comprehensive review of 
recent advances and future directions”.

[38] I. G. Malone et al., “Machine Learning Methods Applied to Cortico-Cortical Evoked 

Potentials Aid in Localizing Seizure Onset Zones”.

[39] S. An, C. Kang and H. W. Lee, “Artificial Intelligence and Computational 

Approaches for Epilepsy”.

7 

M.A. AbuAlrob et al.                                                                                                                                                                                                                           

Epilepsy & Behavior 166 (2025) 110327 

[40] W. L. Cava et al., “A flexible symbolic regression method for constructing 

[57] M. D. Abr`amoff et al., “Considerations for addressing bias in artificial intelligence 

interpretable clinical prediction models”.

for health equity”.

[41] S. E. Labkoff et al., “Toward a responsible future: recommendations for AI-enabled 

[58] “Toward a 21st Century National Data Infrastructure: Managing Privacy and 

clinical decision support”.

Confidentiality Risks with Blended Data”.

[42] “Predetermined Change Control Plans for Machine Learning-Enabled Medical 

[59] J. W. T. M. D. Kok et al., “A guide to sharing open healthcare data under the 

Devices: Guiding Principles”.

General Data Protection Regulation”.

[43] M. Ronchini, Y. Rezaeiyan, M. Zamani, G. Panuccio and F. Moradi, “NET-TEN: a 
silicon neuromorphic network for low-latency detection of seizures in local field 
potentials”.

[44] B. Jarosiewicz and M. J. Morrell, “The RNS System: brain-responsive 

[60] H. Cho et al., “Privacy-Enhancing Technologies in Biomedical Data Science”.
[61] “Artificial Intelligence and Medical Products”.
[62] “WHO outlines considerations for regulation of artificial intelligence for health”.
[63] A. Saenz, Z. Harned, O. Banerjee, M. D. Abr`amoff and P. Rajpurkar, “Autonomous 

neurostimulation for the treatment of epilepsy”.

AI systems in the face of liability, regulations and costs”.

[45] V. Gawade, K. S. Apar, R. D. Mapari, H. S. Lahane and D. R. Pawar, “From Data to 
Drugs a Review: Harnessing AI for Accelerated Pharmaceutical Development”.

[46] K. Wong et al., “Towards a reference genome that captures global genetic 

[64] M. Moor et al., “Foundation models for generalist medical artificial intelligence”.
[65] L. F. H. Contreras et al., “Neuromorphic Neuromodulation: Towards the next 

generation of on-device AI-revolution in electroceuticals”.

diversity”.

[66] Tang J et al. Seizure detection using wearable sensors and machine learning: 

[47] J. Cohen et al., “Problems in the deployment of machine-learned models in health 

Setting a benchmark.

care”.

[67] Khambhati AN, Chang EF, Baud MO, Rao VR. Hippocampal network activity 

[48] Y. Yang, H. Zhang, J. W. Gichoya, D. Katabi and M. Ghassemi, “The limits of fair 

forecasts epileptic seizures.

medical imaging AI in real-world generalization”.

[68] “Ethics and governance of artificial intelligence for health: guidance on large multi- 

[49] D. A. Dorr, L. Adams and P. J. Embí, “Harnessing the Promise of Artificial 

modal models”.

Intelligence Responsibly”.

[69] Oniani D et al. Adopting and expanding ethical principles for generative artificial 

[50] X. Li et al., “Interpretable deep learning: interpretation, interpretability, 

intelligence from military to healthcare.

trustworthiness, and beyond”.

[51] E. Kyrimi et al., “Explainable AI: Definition and attributes of a good explanation for 

health AI”.

[52] S. Martin, F. J. Townend, F. Barkhof and J. H. Cole, “Interpretable machine 

learning for dementia: A systematic review”.

[53] X. Li, J. Gu, Z. Wang, Y. Yuan, B. Du and F. He, “XAI for In-hospital Mortality 

Prediction via Multimodal ICU Data”.

[54] “A toolbox for surfacing health equity harms and biases in large language models”.
[55] B. Singhal and F. Pooja, “Unveiling Intractable Epileptogenic Brain Networks with 
Deep Learning Algorithms: A Novel and Comprehensive Framework for Scalable 
Seizure Prediction with Unimodal Neuroimaging Data in Pediatric Patients”.
[56] A. Retzer et al., “A toolkit for capturing a representative and equitable sample in 

health research”.

[70] Artificial intelligence system, based on mjn-SERAS algorithm, for the early 

detection of seizures in patients with refractory focal epilepsy: A cross-sectional 
pilot study.

[71] Chen W, Wang Y, Ren Y, et al. An automated detection of epileptic seizures EEG 
using CNN classifier based on feature fusion with high accuracy. BMC Med Inform 
Decis Mak 2023;23:96.

[72] “Using Explainable Artificial Intelligence to Obtain Efficient Seizure-Detection 

Models Based on Electroencephalography Signals”.

[73] Cao X, Zheng S, Zhang J, et al. A hybrid CNN-Bi-LSTM model with feature fusion 
for accurate epilepsy seizure detection. BMC Med Inform Decis Mak 2025;25:6.

[74] “Generative AI with WGAN-GP for boosting seizure detection accuracy, https:// 

doi.org/10.3389/frai.2024.1437315”.

[75] Artificial intelligence-enhanced epileptic seizure detection by wearables, https:// 

doi.org/10.1111/epi.17774.

8
