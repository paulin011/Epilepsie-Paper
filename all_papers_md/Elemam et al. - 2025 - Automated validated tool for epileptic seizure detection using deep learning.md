# Elemam et al. - 2025 - Automated validated tool for epileptic seizure detection using deep learning

Journal of Intelligent Systems and Internet of Things 
Vol. 15, No. 01, PP. 74-90, 2025 
DOI: https://doi.org/10.54216/JISIoT.150107  

Automated validated tool for epileptic seizure detection using deep 
learning 

Mahy E. Elemam1,*, A. F. Elgamal1, I. Elmenshawi2, Hanan E. Abdelkader1 
1Computer Teacher Department, Faculty of Specific Education, Mansoura, Egypt 
2NeurologyDepartment, Faculty of medicine, Mansoura, Egypt 
Emails: mahy-ibrahim@mans.edu.eg; amany_elgamal@mans.edu.eg; menshawy@mans.edu.eg; hanan277@mans.edu.eg  

Abstract 

This paper explores an innovative approach for the automatic detection of epileptic seizures from audio recordings and Heart 
Rate Variability (HRV) using Convolutional Neural Networks (CNNs). In medical settings, accurately labeling seizure events 
is critical for patient monitoring. However, manual annotation by experts is not only time-intensive but also highly repetitive. 
To address this challenge, we developed a structured questionnaire for patients and eyewitnesses, concentrating on observable 
characteristics  during  typical  seizure  events.  This  questionnaire  was  used  to  prospectively  study  198  consecutive  adult 
patients with either Psychogenic Non-Epileptic Seizures (PNES) or Epileptic Seizures (ES). For each question, specific signs, 
symptoms,  and  risk  factors  were  extracted  as  variables.  The  results  showed  a  sensitivity  of  95.10%  and  a  specificity  of 
97.06%,  confirming  the  reliability  of  the  questionnaire.  Also,  the  method  proposed  in  the  study  categorizes  all  seizure 
vocalizations into a singular target event class, modeling the detection task as a binary classification problem target (seizure 
event) vs. non-target (non-seizure event). The CNN is trained to detect seizure events in short time frames. Experimental 
results indicate that the method achieves over 92.5% detection accuracy. Furthermore, the research leverages the correlation 
between pre-ictal epileptic states and HRV features. By addressing the noise interference commonly present during seizures, 
the proposed model can robustly train the CNN to identify pre-ictal states. The model's performance is promising, yielding 
an accuracy of over 91.5% for both positive and negative predictions. The proposed system underwent a human evaluation 
by a group of physicians at Mansoura University Hospital. The results were highly satisfactory, with the doctors expressing 
strong approval of the system's performance. 

Received: June 27, 2024 Revised: September 22, 2024 Accepted: December 23, 2024  

Keywords: Convolutional neural network (CNN); Epilepsy; Seizure detection; Epilepsy prediction; Sound event detection 

1.  Introduction 

Epilepsy  is  one  of  the  most  widespread  neurological  disorders  globally,  affecting  an  estimated  50-70  million  individuals. 
Approximately 2 to 4 million new cases are diagnosed each year [1]. The  World Health Organization (WHO) highlights that 
epilepsy is a treatable condition when accurately diagnosed, with around 70% of individuals potentially living seizure-free lives 
with appropriate care. Notably, approximately 80% of those affected live in low- and middle-income regions [2, 3]. 

While  medication  successfully  controls  seizures  in  about  70%  of  cases,  the  remaining  30%  remain  vulnerable  to  secondary 
physical  injuries. With about  1% of the global population  affected by epilepsy, developing  wearable technologies to  predict 
seizures and alert patients before their onset could lead to significant societal benefits [4]. 

Seizures are the hallmark of epilepsy, marked by abrupt, repetitive, and temporary dysfunctions of the central nervous system 
due  to  the  excessive  synchronization  of  neuronal  activity  in  the  brain  [5,  6].  Diagnosing  these  episodes  typically  involves  a 
comprehensive  assessment,  including  a  review  of  medical  history,  neurological  examination,  and  diagnostic  tests  such  as 
Electroencephalograms EEGs to monitor brain activity [7]. 

Many studies aimed at predicting seizures rely heavily on EEG data, limiting their use in everyday situations. Nocturnal seizures, 
which often go undetected, have been linked to  Sudden Unexpected Death in Epilepsy (SUDEP) [8]. Physical indicators like 
heart rate and movement [9] are commonly used to detect these seizures. Meanwhile, audio monitoring has gained traction in 
healthcare as it utilizes nonintrusive acoustic systems traditionally used for nighttime care. 

Some studies reveal statistical correlations between HRV  features  and the  preictal and postictal phases of epileptic seizures. 
Although  the  exact  physiological  mechanisms  remain  unclear,  this  opens  the  possibility  of  predicting  seizures  using 
Electrocardiogram (ECG) [10,11]. 

74 

 
 
 
 
 
 
 
 
Artificial Intelligence (AI) has played a pivotal role in telemedicine [12], enabling personalized diagnosis, treatment planning, 
and disease management [13]. In recent years, machine learning has been widely adopted for seizure detection and prediction 
[14]. Additionally, emerging research increasingly focuses on deep learning algorithms, which have shown remarkable success 
in areas like speech recognition and computer vision [15]. 

Some students in educational institutions are vulnerable to epileptic seizures and often fear experiencing these episodes in front 
of their peers. As a result, the primary focus of our research is on accurately identifying epileptic seizures through the patient's 
exhibited symptoms, followed by predicting upcoming seizures using either heart rate monitoring or the sounds the patient makes 
prior to the onset of a seizure. 

This paper presents an innovative method for detecting epileptic seizures through audio analysis by treating various vocalizations 
during seizures as a unified target class. It approaches the seizure detection problem by modeling it as a binary classification 
task—seizure (target) versus non-seizure (non-target). The system is built using a CNN, which learns the distinctive acoustic 
features from a large dataset of annotated patient data. During the detection phase, the method processes lengthy audio recordings 
(10-14 hours) by segmenting them into shorter intervals for real-time seizure detection. 

Furthermore, this paper emphasizes the use of supervised classification techniques to identify pre-ictal Heart Rate (HR) patterns 
for seizure prediction. A robust method is presented for processing ECG data, which efficiently handles the inherent noise of 
portable ECG devices and the severe noise that occurs during seizures. The heart rate features extracted from the processed HR 
data are then used to train the CNN, which performs the seizure prediction task. The term HR refers to the heart rate, while RR 
represents the interval between successive wave peaks in the cardiac cycle, illustrating heart rate regularity and speed. 

In addition, it detects the presence of seizures in patients by analyzing their responses to a questionnaire that includes a range of 
symptoms specific to epileptic episodes. The proposed technique was evaluated by a group of patients from Mansoura University 
Hospital. 

The system is designed to diagnose seizures and predict forthcoming episodes, ultimately reducing the significant clinical burden 
on neurologists. Moreover, it aids medical students, less experienced doctors, patients, and caregivers in diagnosing epilepsy and 
predicting seizures, thereby shortening the time required for diagnosis. The key contributions of this study are as follows: 

  Using Rules to assist in analyzing diagnostic questionnaire data. 

  Using AI and teachable machine for audio dataset creation. 

  Advising smart telemedicine systems on an effective and secure epilepsy detection and diagnostic solution. 

  Developing  a  new  framework  for  reducing  the  dimensionality  of  HRV  waveform  representation  and  analyzing  patient 
sounds using TensorFlow (TF) and feeding the reduced data into a Convolutional CNN to enhance model efficiency and 
reduce training complexity. 

 

Investigating and testing the suggested system in terms of  accuracy. We used accuracy,  recall and precision to estimate 
performance. 

The remainder of this work is structured as follows. Section 2 provides an overview of related work on seizure detection and 
predictability.  Section  3  discusses  the  proposed  system,  including  the  dataset  used.  Section  4  presents  the  application  and 
experimental results. Finally, Section 5 outlines the conclusions drawn from this study. 

2. 

 Related Work 

It  is  difficult  to  distinguish  between  the  possibility  of  seizures  and  non-seizures.  This  requires  obtaining  and  identifying  the 
distinguishing factors from the heart rate pattern and the sounds emitted before the seizure. In this section, we will provide an 
overview  of  the  advanced  methods  involved  in  detecting  seizures  and  non-seizures  using  different  feature  extraction  and 
classification  algorithms.  Dohyun  Lee,  et.al  [16]  used  a  method  for  predicting  epileptic  seizures  a  pre-trained  model  with 
supervised contrastive learning and a hybrid ResNet-LSTM model. The approach involves three phases: preprocessing data into 
spectrograms using STFT, pre-training with augmented data and supervised contrastive loss, and training the hybrid model. This 
model combines ResNet and LSTM to capture both image and time features. Tested on CHB-MIT and Seoul National University 
Hospital (SNUH) datasets, the method achieved accuracies of 91.90% and 83.37%, respectively, and outperformed traditional 
methods. Sina Shafiezadeh, et.al [17] improved seizure forecasting for new patients using a calibration pipeline that fine-tunes 
deep learning models with just one epileptic event. Testing on two datasets showed over 20% increased accuracy and consistent 
improvement across patients. The method benefits both deep learning and feature-based machine learning models, requiring only 
one event per patient for calibration, making it useful for practical healthcare applications. Sona M. Al Younis, et.al [18] used 
machine learning models KNN, NN, SVM, and TREE to classify LVEF in HF patients based on 24-hour ECG recordings. Data 
from 303 HF patients were analyzed, with TREE and KNN showing the highest accuracy (91.2% and 90.9%, respectively) and 
AUROC (0.98 and 0.99). Optimal classification occurred during midnight-1 am, 8–9 am, and 10–11 pm. These results suggest 
a potential for automated CAD screening aligned with circadian rhythms. Nurul Absar, et al. [19] used four machine learning 
models  Random  Forest  (RF),  Decision  Tree  (DT),  AdaBoost  (AB),  and  K-nearest  Neighbor  (KNN)  to  detect  heart  disease. 
Evaluated  on  the  Cleveland,  Hungary,  Switzerland,  and  Long  Beach  (CHSLB)  datasets  from  Kaggle,  the  models  achieved 
accuracies of 99.03% (RF), 96.10% (DT), 100% (AB), and 100% (KNN). On the Cleveland dataset alone, RF and KNN achieved 

75 

 
accuracies of 93.44% and 97.83%, respectively. Kunpeng Song, et al. [20] proposed an intelligent epileptic prediction system 
used  Synchrosqueezed  Wavelet  Transform  (SWT)  and  Multi-Level  Feature  Convolutional  Neural  Network  (MLF-CNN).  It 
achieved 96.99% accuracy and 96.48% sensitivity on the CHB-MIT dataset, and 94.25% accuracy and 97.76% sensitivity on the 
ZJU4H  dataset,  with  false  positive  rates  of  0.031%  and  0.049%  FPR/h,  respectively.  Xiao  Wu,  et  al.  [21] developed  a  new 
method for predicting epileptic seizures used successive variational mode decomposition (SVMD) and transformers. The data 
were decomposed and denoised with SVMD, then input to a pre-trained BERT model. This approach achieved 0.86% sensitivity 
and 0.18% FPR on intracranial EEG data. Kuldeep Singh, et al. [22] developed a two-layer LSTM model predicted epileptic 
seizures using spectral features from 23-channel EEG data. Evaluated on 5-50 second EEG segments from 24 subjects, the model 
achieved 98.14% accuracy, 98.51% sensitivity, and 97.78% specificity. Jaehak  Yu, et  al.  [23] developed a stroke prediction 
system using real-time bio-signals and Artificial Intelligence (AI). Unlike costly image-based tools, this system utilized Random 
Forest and Long Short Term Memory (LSTM) algorithms. It achieved prediction accuracies of 90.38% with Random Forest and 
98.96% with LSTM. Toshitaka Yamakawa, et al. [24] developed an innovative telemeter measured R-R intervals from ECG, 
with a  smartphone app for calculating heart rate  variability in real-time. Tested on seven epilepsy patients, it showed 85.7% 
sensitivity in detecting heart rate variability changes before seizures. Al-Hammadi [25] analyzed whether the audio recordings 
of epileptic and psychogenic non-epileptic seizures (PNE) could be classified using linear, quadratic, or support vector machine 
(SVM) classifiers. In their study, the SVM classifier using four mel-frequency bands achieved an accuracy of 76% during cross-
validation. However, the sample size for this analysis was limited to 16 recordings of epileptic seizures and 20 recordings of 
PNE seizures, suggesting that further research with a larger dataset would be necessary to validate and improve the classifier's 
performance.  Arends et al [26] focused on epilepsy patients  with intellectual disabilities, researchers selected 10 adults  who 
exhibited  major  seizures  accompanied  by  recognizable  sounds  from  an  initial  group  of  17  individuals.  These  patients  were 
monitored  for  four  weeks  using  both  audio  and  video  recordings.  The  results  showed  that  audio  detection  was  effective  at 
identifying either the initial vocalization or noise during major seizures. However, since the sounds produced were specific to 
each patient, the system was only able to reliably detect major seizures in half of the participants. This indicates that while audio 
monitoring can be useful, the variability in seizure-related sounds between individuals limits its general applicability Bruijne et 
al [27] analyzed vocalization during seizures, researchers observed vocal sounds in 61 out of 95 seizures across 17 patients. The 
study employed basic audio statistics derived from 25-millisecond sliding windows, training classifiers to detect specific vocal 
patterns such as screams, lip smacking, moans, or heavy breathing. Their experimental results achieved precision rates between 
66% and 77% using 10-fold cross-validation. However, the precision quickly declined with the introduction of noise, and the 
classifiers were not tested on unseen data, raising concerns about their generalizability and robustness in real-world conditions.  

Based on the recent studies, most feature extraction algorithms are manually crafted and not tailored to the data. Deep Learning 
(DL) can enhance the accuracy and generalizability of epilepsy detection systems. Hence, we were motivated to leverage deep 
learning to create a deep model with minimal learnable parameters capable of predicting imminent epileptic seizures. 

3.  Proposed System 

The proposed system is divided into two sections: the first section elucidates the diagnosis of epilepsy, while the second section 
explains how to detect an upcoming seizure.  

3.1 Epilepsy diagnosis through the questionnaire 

Questionnaires  designed  to  assess  ES  and  PNES  are  predominantly  used  as  tools  to  facilitate  faster  referrals  to  specialized 
epilepsy centers, where diagnosis can be confirmed, rather than serving as standalone diagnostic alternatives. While video-EEG 
monitoring remains the gold standard for diagnosis, these questionnaires help streamline diagnosis when video-EEG is either 
unavailable or yields inconclusive results. There are many types of epileptic seizures that epilepsy patients suffer from, and each 
seizure contains a set of symptoms that indicate the presence of this seizure, such as generalized seizures and partial seizures. In 
the proposed system, epileptic seizures were dealt with in general. The questionnaire within the proposed system consists of  a 
set of questions that were created by a group of experts in the medical field. A total of 105 patients of varying ages, who were 
diagnosed with epilepsy by neurologists at Mansoura University Hospital based on established medical criteria, were selected. 
Additionally, 98 patients without epilepsy who regularly attended the outpatient clinics at Mansoura University Hospital were 
also included in the study. 

By conducting several personal interviews with experts in the medical field specializing in epilepsy patients, the most common 
symptoms in epilepsy patients were obtained, which included a group of symptoms that appear during epileptic seizures, and the 
following table 1 shows some of the most common symptoms during true and pseudo epileptic seizures. 

Table 1: Samples for symptoms of true and pseudo epileptic seizures 

No. 

Symptoms for true seizure 

Symptoms for pseudo seizure 

76 

 
 
 
 
Symptom 

1 

2 

3 

4 

5 

6 

7 

8 

9 

10 

11 

12 

13 

14 

15 

16 

17 

18 

19 

20 

21 

22 

23 

24 

Seizure take Briefer time 

Seizure take prolonged time 

Stereotypic  the  form  of  symptoms  that  occur 
during seizure 

Fluctuating the form of symptoms that occur during 
seizure 

Epileptic  seizure  may  occur 
wakefulness  

in  sleep  or 

Epileptic seizure usually during wakefulness 

Unaware of what is happening during seizure 

Aware of what is happening during seizure 

Convulsions occur at the time of seizure as abrupt  Convulsions occur at the time of seizure as gradually 

Movement of the head during the seizure as Side 
to side with staring 

Movement of the head during the seizure one way or 
fixed 

Movements  of  the  hands  and  feet  during  the 
seizure  organized movements 

Movements of the hands and feet during the seizure  
random movements 

Seizure occurs during sleep 

Seizure doesn't occur  during sleep 

Seizure doesn't occurs during pseudo sleep 

Seizure occurs during pseudo sleep 

Difficult to describe the beginning of the seizure 

Factual description the beginning of the seizure 

Synchronized the movements during the seizure 

Lack  of  synchronization  of  movements  during  the 
seizure. 

No response to any action during the seizure 

Defense any action during the seizure 

Tongue biting through lateral 

Tongue biting through apical 

Eyes open during the seizure 

Eyes close during the seizure 

Shape of the pupil of the eye is abnormal 

Shape of the pupil of the eye is normal 

Increasing in heart rate 

Normal heart rate 

Feeling a headache during the seizure 

Don't Feel a headache during the seizure 

clinch teeth 

No teeth clenching occurs. 

Doesn't make sounds during the seizure 

Make sounds during the seizure 

Make sounds at beginning of the seizure 

Make sounds during or after seizure 

Doesn't  remember  what  happened  during  the 
seizure 

remember what happened during the seizure 

Occur incontinence 

Rare incontinence 

Injuries occur during a seizure. 

Don't injuries occur during a seizure. 

Long time take to recover from a seizure 

Little time take to recover from a seizure 

According  to  the  human  expert  every  symptoms  has  weight  (-1  or 1)  for  pseudo-seizure  and  (1  or 24)  for  true  seizure. The 
knowledge base of epileptic seizure symptoms was built using rules to obtain the probabilities of different symptoms appearing 
together,  in  order  to  confirm  whether  it  is  a  true  or  pseudo  seizure.  A  specific  weight  was  assigned  to  each  symptom, 
distinguishing between real and pseudo-seizures. Ultimately, the cumulative weights were calculated, and the final result of the 
questionnaire was determined accordingly. Additionally, certain symptoms serve as definitive indicators of an epileptic seizure. 
If any of these symptoms are present, whether individually or in combination, they confirm the occurrence of a seizure. 

The results led to the identification of several key symptoms, which formed the foundation of the knowledge base. The table 2 
presents samples of this knowledge base, utilized for distinguishing true epileptic seizures from pseudo-seizures.  

Table 2: system knowledge base obtained from the symptoms of true and pseudo epileptic seizures 

Symptoms (No) 

Rules 

S(2) 

True epileptic seizures 

77 

 
 
 
S(4) 

S(5) 

S(8) 

S(12) 

S(13) 

S(14) 

S(17) 

S(22) 

S(23) 

S(2)^ S(8) 

S(2) ^ S(8)^ S(13) 

S(2)^ S(8)^ S(14) 

S(13)^ S(14) 

Pseudo epileptic seizures 

Pseudo epileptic seizures 

True epileptic seizures 

Pseudo epileptic seizures 

True epileptic seizures 

True epileptic seizures 

Pseudo epileptic seizures 

True epileptic seizures 

True epileptic seizures 

True epileptic seizures 

True epileptic seizures 

True epileptic seizures 

True epileptic seizures 

3.2 Epilepsy prediction through HRV 

In the proposed system, the  main purpose is to predict epileptic seizures  with tunable  parameters on the  measured  HR. The 
proposed system contains the modules to read and process the incoming HR data  as  well as to send the alarms as shown in 
figure1.  

Signal Acquisition 

Figure 1. Heart rate measurement architecture 

  Access  Camera:  an  Android  device's  camera  with  a  resolution  of  32  megapixels  and  an  aperture  of  F/2.2  support 
PhotoPlethysmoGraphy (PPG) was utilized  ،which generally captures ECG signal for fifteen seconds from the thumbs at a 
sampling frequency of 250 Hz, which is done in sitting position with hands resting on a table.  

  Extract Signal: Transform the captured video frames into a PPG signal by analyzing light absorption variations associated 

with heartbeats. 

Signal Preprocessing 

  Filter Noise: Implement signal processing techniques, such as bandpass filtering, to eliminate noise and isolate relevant HRV 
components. This is a signal processing technique  that allows  frequencies  within a specific range to pass through  while 
attenuating  frequencies  outside  that  range.  It  is  commonly  used  in  ECG  signal  processing  to  isolate  the  frequency 
78 

 
 
 
 
components that are most relevant for heart rate and other physiological measurements, typically between 0.5 to 40 Hz. The 
general transfer function for a second-order bandpass filter can be expressed as [28]:  

                                               H(s) =

A⋅S⋅Q
ω0
𝑄

.𝑆+𝑊

𝑆2+

                                                     (1) 

2
0

Where: 

      H(s) is the transfer function. 

      S is the complex frequency variable. 

      A is the gain. 

     w0 is the center angular frequency. 

     Q is the quality factor, which determines the bandwidth of the filter. 

  Segment Signal: Partition the signal into specific time windows for detailed analysis. 

CNN Model Development 

  Design Model: Construct a CNN trained to identify patterns in HRV signals that suggest a forthcoming epileptic seizure. 

  Train Model: Train the model using a dataset of HRV signals annotated with normal and seizure-related events. 

Real-Time Signal Analysis 

  Analyze Signal: Input real-time HRV data from the camera into the trained CNN model for classification. 

  Measure HR: Determine the HR by detecting peaks and calculating the intervals between them. 

 Alert Triggering 

  Threshold Check: Continuously monitor HR, and if it surpasses 120 bpm depend on equation (new HR > last HR*0.2+last 

HR); treat it as a potential warning of an impending seizure. 

 

Issue an Alert: Activate an alert for the user or caregiver if the HR exceeds the set threshold. 

3.3 Epilepsy prediction through sound classification 

This section of the proposed system presents an innovative approach to epileptic seizure detection by leveraging audio data, 
where various seizure-related vocalizations are treated as a unified target event.  

The method employs a CNN to learn and differentiate the acoustic features, utilizing an extensive dataset of annotated patient 
recordings. During the detection phase, the system processes prolonged audio recordings (ranging from 10 to 14 hours) and 
identifies seizures by analyzing short time segments within these recordings. 

Sound event detection involves identifying the start and end of specific sound events by analyzing their acoustic characteristics. 
In the proposed system, an epileptic seizure is treated as a target sound event to be detected within an audio recording. To detect 
a seizure, the audio is segmented into short clips, and features are extracted from each segment. The CNN is trained on these 
features, and during the testing phase, it evaluates whether the target event is present in segments of the same duration as those 
used in training.  

For this study, a segment length of 10 seconds was chosen, as it provides sufficient audio content for effective training of  the 
neural network. This approach achieves detection with a temporal resolution of 10 seconds, rather than pinpointing the exact 
onset and offset of the seizure. Figure2 presents the block diagram for prediction seizure through sound, with training and testing 
branches illustrated separately. 

79 

 
 
Figure 2. block diagram for prediction seizure through sound 

The convolutional layers of the CNN are responsible for learning these features, with kernels extending across both the frequency 
and time axes to capture the relevant temporal characteristics of the target class.  

During training, the target output for each segment is set to >=0.65 when a seizure event is active and 0 when it is inactive, this 
percentage was chosen to provide a more accurate prediction of the upcoming seizure, following multiple applications. After 
each  CNN  layer,  a  max-pooling  operation  is  applied  along  both  axes  to  reduce  data  dimensionality.  Batch  normalization  is 
performed after each convolutional layer to normalize the layer inputs, and the Rectified Linear Unit (ReLU) activation function 
is employed.  

To  prevent  overfitting,  a  30%  dropout  is  implemented  after  each  layer.  The  output  layer  consists  of  a  single  sigmoid  unit, 
producing a binary result that indicates whether the target class is active or inactive. 

Once the CNN has processed the input and produced a binary output indicating whether the target class (seizure event) is active 
or inactive, the system proceeds to the alert stage. If the output of the CNN is >=0.65, signaling that a seizure event is detected, 
the system immediately triggers an alert. 

The alert is designed to be both rapid and reliable, ensuring that the patient and their caregivers can take appropriate action 
swiftly to mitigate the risks associated with the seizure. 

The pseudo code for some sections of this paper is presented in the following part. 

Algorithm1.Epilepsy diagnosis through the questionnaire 

Algorithm2.Epilepsy prediction through HRV 

Input: patient_id, P.S.V 

//P.S.V refer to patient symptoms vector 

Input: finger video 

Output: Decision 

Output: Decision 

// Decision will be alarm or normal 

// Decision will be true seizure or pseudo seizure 

Begin 

Begin 

Apply frompixels() for figure video to convert it into a tensor 

Define T.P.S array symptoms [24, 2] 

// a tensor is captured image data 

// T.P.S refer to seizure and pseudo symptoms 

Apply crop Image () for a tensor to crops and resizes it 

//  T.P.S  array  components  are  (id,  true  seizure  weight, 
pseudo seizure weight) 

I=0 

For each item in P.S.V 

If item="a" then total T.S +=W.T.S (i, 1) 

Apply a bandpass filter () for a tensor to remove noise  

Load TensorFlow js for pulse model 

Apply predictpulse() a tensor to calculate newHR 

Connect with database 

80 

 
 
 
// T.S refer to true seizure 

Select HR-day , HR for patient p 

// W.T.S refer to weight of true seizure 

If Hr-day is current day then 

Else total P.S += W.P.S (i, 2) 

// P.S refer to pseudo seizure 

     If (new HR>HR+(HR*0.2)) then give alarm 

    Else show "normal" 

// W.P.S refer to weight of pseudo seizure  

    End if 

Else insert new HR & current day in HR-day for patient p  

End if  

End if 

i+=1 

Next item 

If total T.S>total P.S then 

Decision= "true seizure" 

Else Decision= "pseudo seizure" 

End if 

4.  Implementation 

The proposed system is designed using PHP and JavaScript languages. The proposed system can be accessed through mobile 
application .As well you can access it through the World Wide Web. Finally it can be  used through Personal Computer (PC). 
Running the proposed system on PC requires the availability of the XAMPP software to convert the PC to server.  

The proposed system can be used by neurology students, nurses, patients, or anyone interested in the management of epilepsy. 
Graphical user interface of mobile application system will be illustrated in this section. 

The user will be able to log into the system after loading the proposed system and will be able to traverse the system. To log in, 
the user must first enter his user name and password into the designated fields and then click the "Log in" button, as shown in 
Figure 3 ،assuming he is already registered in the proposed system. 

Figure 3. The Proposed System Graphical User Interface 

4.1 Diagnosing epilepsy through its symptoms 

Diagnosing epilepsy through questionnaire is performed according to the following steps: 

  Access the Diagnostic Questionnaire: Navigate to the section dedicated to the epilepsy diagnostic questionnaire. 

  Complete the Questionnaire: Answer all relevant questions regarding the patient's symptoms, medical history, and other 

pertinent details. 

  Submit the Responses: Review the completed questionnaire and submit it for analysis. 

  Review Diagnostic Results: Analyze the results generated from the questionnaire to assist in diagnosing epilepsy. 

This process helps in assessing the likelihood of epilepsy based on the patient's responses and medical history. Figure 4 (a, b, c) 
shows a sample of the questionnaire questions and their answers. 

81 

 
     
 
(a) 

(b) 

(c) 

Figure 4. samples of questionnaire questions and their answers. 

4.2 Predicting an epileptic seizure through heartbeat 

To predict an epileptic seizure through heart rate  monitoring, follow these steps as depicted in the  figure 5 displays the start 
screen, where heart rate (HR) is recorded. Figure 6 shows the recorded heart rate results, presenting various screens for a single 
patient at different times.  

  Collect  Heart  Rate  Data:  Begin  by  monitoring  and  recording  the  patient’s  heart  rate  using  the  application,  initiated  by 

pressing the "Start Camera" button. 

  System Data Upload: The system automatically inputs the recorded heart rate data into the application, where it is analyzed 
and stored in the patient’s database. If it is the first measurement of the day, the system records it directly as the baseline for 
that day. However, if it is not the first measurement, the system compares the current reading with the last recorded result 
taken on the same day to detect any significant changes or trends. 

  Generate Predictions: The system analyzes the heart rate patterns to assess the likelihood of an impending seizure and give 

alarm. 

Monitoring heart rate can offer crucial insights into potential seizure activity, thereby enhancing the ability to anticipate and 
manage epileptic events more effectively. 

Figure 5. Heart rate measurement 

(a) 

(b) 

(c) 

Figure 6. Heart rate measurement result for the same patient 

82 

 
 
 
 
 
 
 
 
4.3 Predicting an epileptic seizure patient's voices 

To predict epilepsy by analyzing the sounds a patient makes before a seizure, follow these steps as depicted in the figures 7 ،8 ،
9: 

  Acoustic data collection: Record the patient's sounds using the app, ensuring accurate capture of any vocal phenomena that 

may precede a seizure. 

  Upload audio data to the system: The recorded audio files are sent to the application for analysis, where they are processed. 

  Voice Pattern Analysis: The system examines voice data to identify patterns or anomalies associated with seizure activity. 

  Generate predictions: Based on the analysis, the system predicts the probability of an impending attack and give alarm. 

Analysis  of  pre-seizure  sounds  can  provide  valuable  insights  for  predicting  seizures,  and  improving  the  management  and 
prediction of epileptic events. 

Figure 7. recording the patient's voice 

(a) 

(b) 

Figure 8. predicting an impending seizure 

Figure 9. predicting the occurrence of a non-epileptic seizure 

83 

 
 
 
 
 
5.   Results  

5.1 Results for diagnosing epilepsy through questionnaire 

To validate the questionnaire a transversal observational study was carried out. The central question of the questionnaire was: 
“During the last 24 months, while you are stopping treatment, have you had convulsions or epileptic seizures, brief periods of 
loss of consciousness, involuntary spasms of the arms or legs, or have you appeared to be disconnected from reality or incapable 
of  responding?”  If  the  answer  was  negative  the  interview  was  concluded  and  the  patient  was  considered  not  to  suffer  from 
epilepsy. If the answer was positive, the patient was considered to be at risk of having seizures, and the interview proceeded to 
the following series of questions Table 3, whose objective was to establish the diagnosis of epilepsy. 

Table 3: Complementary questions to establish the diagnosis of epilepsy. 

No. question 

Question 

1 

2 

3 

4 

5 

6 

7 

8 

9 

10 

11 

12 

13 

14 

15 

16 

17 

18 

19 

20 

21 

22 

23 

How long does the seizure take? 

Talk about the form of symptoms that occur during the seizure? 

Are you aware of what is happening around you during a seizure? 

When do convulsions occur at the time of seizure? 

Describe the movement of the head during the seizure? 

Describe the movements of the hands and feet during the seizure? 

Does the seizure occur during sleep? 

Does the seizure occur during pseudo sleep? 

Describe the beginning of the seizure? 

Are the movements synchronized during the seizure? 

Talk about his response to a specific action such as holding hands? 

Where is the tongue biting? 

What is the condition of the eyes? 

Explain the shape of the pupil of the eye? 

Is there an increase in heart rate? 

Do you feel a headache during the seizure? 

Does clinch your teeth? 

Do you make sounds during the seizure? 

When do you make sounds at the time of the seizure? 

Do you remember what happened during the seizure? 

What about incontinence? 

Are there injuries caused by the seizure? 

How long does it take to recover from a seizure? 

84 

 
A total of 105 patients of varying ages, who were diagnosed with epilepsy by neurologists at Mansoura University Hospital 
based  on  established  medical  criteria,  were  selected.  Additionally,  98  patients  without  epilepsy  who  regularly  attended  the 
outpatient clinics at Mansoura University Hospital were also included in the study. 

In both instances, patient selection was conducted consecutively, adhering to the standard procedures set by the administrative 
staff during 2023. In all cases, valid consent was obtained from the patient or a relative. Patients were excluded if their relatives 
or representatives could not provide reliable information. 

A pilot test  was performed involving the  relatives of  five patients  with epilepsy and five non-epileptic patients to adjust the 
details and address any potential uncertainties that could emerge during the application of the questionnaire. 

For the study, no more than four individuals from each group, along with their relatives or representatives, were invited daily to 
the Neurology outpatient clinic at Mansoura University Hospital. The procedure was explained to them, and they were requested 
not to disclose the patient's diagnosis during the interview. The responses were then recorded in a database created using php 
My Admin. 

Additionally, the neurological doctors re-evaluated a sample composed of 20% of the patient of each group, with the objective 
of determine the diagnostic reliability of the questionnaire.  

The  validity  of  the  questionnaire  was  measured  by  means  of  its  sensitivity  (capacity  of  detecting  patients  with  epilepsy), 
specificity (capacity of not diagnosing an epilepsy-free patient as having epilepsy), and the prognostic value of a positive or 
negative result, which were calculated from the equations shown below .As referential criteria to calculate these measurements, 
the clinical diagnosis of epilepsy patients diagnosed by a neurologist was used to test the reliability of the questionnaire [29]. 

𝑆𝑒𝑛𝑠𝑖𝑡𝑖𝑣𝑖𝑡𝑦 =

𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑠

𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑠+𝐹𝑎𝑙𝑠𝑒 𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒𝑠

                                                                  (2)                                                       𝑆𝑝𝑒𝑐𝑖𝑓𝑖𝑐𝑖𝑡𝑦 =

𝑇𝑟𝑢𝑒 𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒𝑠

𝑇𝑟𝑢𝑒 𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒𝑠+𝐹𝑎𝑙𝑠𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑠

                                                                  (3) 

𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒 𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑣𝑒 𝑉𝑎𝑙𝑢𝑒 =  

𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑠

𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑠+𝐹𝑎𝑙𝑠𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑠

                                  (4) 

                            𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒 𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑣𝑒 𝑉𝑎𝑙𝑢𝑒 =

𝑇𝑟𝑢𝑒 𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒𝑠
𝑇𝑟𝑢𝑒 𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒𝑠 + 𝐹𝑎𝑙𝑠𝑒 𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒𝑠

                 (5) 

𝐼𝑛𝑑𝑒𝑥 𝑜𝑓 𝑉𝑎𝑙𝑖𝑑𝑖𝑡𝑦 =

(𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑠+𝑇𝑟𝑢𝑒 𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒𝑠)

𝑇𝑜𝑡𝑎𝑙 𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝐶𝑎𝑠𝑒𝑠

                                               (6) 

5 of the 203 evaluated patient lacked complete or reliable information, so they were not taken into account for the analysis. At 
the end, the study groups consisted of 102 with epilepsy, according to the diagnosis of the neurologists, and 96 without epilepsy. 
Table 4 show that 100 patient (51%) were between 19 and 30 years of age, and 98 (49%) were between 31 and 60. 

Table 4: Composition of the study groups according to age 

Age group 

Epilepsy patients 

Patients without epilepsy 

Total 

19-30 

31-60 

Total 

50 

52 

102 

50 

46 

96 

100 

98 

198 

The  evaluated  questionnaire  accurately  diagnosed  97  individuals  with  epileptic  seizures,  resulting  in  3  false  positive  cases. 
Additionally, 93 individuals were correctly diagnosed as not having epileptic seizures, with 5 false negative cases, as detailed in 
Table 5. 

Table 5: Results of the application of the diagnostic questionnaire in patient with epilepsy and without epilepsy 

Diagnosis  according  to  the 
questionnaire 

Patient with epilepsy 

Patient without epilepsy 

Total 

Positive 

Negative 

Total 

97 

5 

102 

3 

93 

96 

100 

98 

198 

85 

 
 
The tests of validity of the diagnostic questionnaire demonstrated its satisfactory sensitivity 95.10% and specificity 97.06%. The 
index of validity was of 96.08%, and the prognostic value of a positive result of 97.00% and that of a negative result of 95.19% 
as shown in figure 10  

Results

98

97

96

95

94

97.06

97

96.08

95.1

95.19

Results

Figure 10. Results for the proposed system (Diagnosing epilepsy through questionnaire) 

5.2 Results for prediction epilepsy through ECG classification 

To evaluate the proposed application, it was implemented on 30 patients (20 men and 10 women) aged between 20 and 65 years, 
who were attending Mansoura University Hospital. Table 6 presents the number of patients who participated in the study and 
were subjected to the proposed application for predicting epileptic seizures. It serves as a foundation for comparing the results 
with those obtained using existing applications to ensure the validity and reliability of the proposed system. 

Table 6: numbers of patients who participated in the study 

Male 
20 

Female 
10 

Total 
30 

The application successfully captured heart rate data and identified significant increases in heart rate that preceded seizure events. 
On average, the heart rate increased by 30% before a seizure. 

To verify the reliability of the results, they were compared with those obtained from the same patients at the same time using 
some pre-existing applications available on app store. That are widely used and approved for similar purposes. The measurements 
were  also  compared  to  those  obtained  by  the  neurologist  using  the  Mansoura  University  hospital's  CADOO  device,  which 
measures patients' heart rates through electrocardiography. 

The following table 7 compares the results obtained from the proposed system with those other applications. We utilize several 
metrics: Accuracy, Precision, sensitivity and specificity. These metrics are calculated using equations (7, 8) and equations (2, 3). 
Also figure 11 shows the results [26]. 

𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 =

𝑇𝑟𝑢𝑒 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒 + 𝑇𝑟𝑢𝑒 𝑛𝑒𝑔𝑎𝑡𝑖𝑣𝑒
𝑇𝑜𝑡𝑎𝑙 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑠𝑎𝑚𝑝𝑙𝑒𝑠

𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 =

𝑇𝑟𝑢𝑒 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒
𝑇𝑟𝑢𝑒 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒 + 𝐹𝑎𝑙𝑠𝑒 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒

                                                       (7) 

                                                        (8) 

Table 7: comparing the results of the proposed system with other systems 

App 

Accuracy 

Precision 

sensitivity 

specificity 

Proposed system 

91.5% 

90.3% 

Instant Heart Rate 

88.5% 

87.4% 

Heart Rate Monitor 

91% 

89.4% 

Runtastic  Heart  Rate 
Monitor 

89.5% 

87.6% 

93% 

90% 

93% 

92% 

90% 

87% 

89% 

87% 

Heart Rate Plus 

84% 

83.3% 

85% 

83% 

86 

 
 
94.00%
92.00%
90.00%
88.00%
86.00%
84.00%
82.00%
80.00%
78.00%

Accuracy

Precision

sensitivity

specificity

Proposed
system

Instant
Heart Rate

Heart Rate
Monitor

Runtastic
Heart Rate
Monitor

Heart Rate
Plus

Figure 11. Results for the proposed system (prediction epilepsy through ECG classification) 

This comparison highlights the effectiveness of the proposed application in predicting epileptic seizures by monitoring heart 
rate, demonstrating its accuracy relative to other widely used applications available on app stores.  

Our application showed higher accuracy in predicting seizures, with a sensitivity of 93% and a specificity of 90%, outperforming 
other applications in comparison to the CADDO device located in Mansoura University Hospital. Also Patients reported ease of 
use and confidence in the application’s predictions. No adverse events or technical issues were encountered during the testing 
period. 

5.3 Results for prediction epilepsy through sound classification 

The  dataset  utilized  in  this  study  comprises  audio  recordings  from  20  patients  experiencing  seizures.  The  recordings  were 
captured during nighttime monitoring sessions at the patients' residences, with each session lasting approximately 10 to 14 hours. 
The  audio  data,  extracted  from  corresponding  video  recordings,  was  meticulously  annotated  by  certified  neurologists  at 
Mansoura University Hospital. A total of 50 seizure events were identified and  labeled based on visual cues observed in the 
video recordings. 

Each seizure event was identified and annotated by the neurologists based solely on visual cues observed in the video recordings. 
Subsequently,  these  annotations  were  directly  applied  to  the  extracted  audio  clips.  For  the  purpose  of  training  the  seizure 
detection model, the annotated seizure events were segmented from the audio recordings, with an additional 120-second non-
seizure segment included both before and after each seizure event. This padding served as an example of the non-target class, 
providing the model with necessary context information. Consequently, the final dataset comprised 50 seizure segments and 100 
non-seizure segments, ensuring a balanced representation for model training indicated in table 8. The training dataset was utilized 
to train the model's parameters, while the test dataset was used to evaluate the trained model. 

Table 8: numbers of sounds used for the CNN in the proposed system validation. 

Total  number  of 
sounds 

Number  of  sounds  used 
for training 

Number of sounds used for 
testing 

Actual Seizure 

Actual Normal 

50 

100 

45 

94 

5 

6 

Given that the seizure events are relatively short, typically lasting between 10 and 30 seconds, the inclusion of the 120-second 
padding resulted in a sufficient degree of data imbalance within the dataset. This structure ensured that each audio file contained 
a balanced mix of seizure and non-seizure data, which is essential for training the model effectively.  

The  proposed  Convolutional  Neural  Network  (CNN)  model  was  trained  and  evaluated  using  the  prepared  dataset  to  predict 
upcoming seizures based on pre-seizure audio signals. In order to validate the system and measure the classification results, we 
utilize several metrics: Accuracy, Precision, Recall, and F-measure, yielding the metrics which shown in figure 12. 

These results indicate in this section of study, the CNN model effectively distinguishes between seizure and non-seizure events 
based on pre-seizure audio cues. Achieving an impressive accuracy of approximately 92.5%%.  

87 

 
 
 
 
96.00%

94.00%

92.00%

90.00%

88.00%

86.00%

Accuracy

Recall

Specificity Precision

F1 Score

Figure 12. Results for the proposed system (Diagnosing epilepsy through EEG wave form) 

Upon  detection  of  a  seizure  event  by  the  CNN  model,  the  system  successfully  triggered  alerts  with  a  latency  of  less  than  2 
seconds in 95% of the cases, ensuring timely notifications to patients and their relatives. The alert system maintained a reliability 
rate of 93%, minimizing false alarms and ensuring that alerts were only issued when a true seizure event was predicted. 

The proposed system underwent a comprehensive evaluation by a team of eight physicians at Mansoura University Hospital, 
each possessing different levels of expertise in neurology and epilepsy care. This evaluation was conducted to assess the system's 
full functionality, including its diagnostic accuracy and ability to predict epileptic seizures. The feedback from the doctors was 
highly  positive,  as  they  found  the  system  to  be  reliable  and  valuable  across  varying  clinical  experiences.  The  inclusion  of 
physicians with diverse expertise ensured a well-rounded assessment, further validating the system's effectiveness in real-world 
medical settings. The following Table 9 presents the items of the arbitration form and the doctors’ evaluation of it. 

Table 9: percentage of responses for each question based on the evaluation results. 

Question 

Excellent 
(%) 

Good 
(%) 

Satisfactory 
(%) 

Needs 
(%) 

Improvement 

Clarity of the User Interface 

Ease of Use for Your Role (e.g., Patient, Nurse, 
etc.) 

Accessibility of the Application 

Efficiency in Diagnosing Epilepsy (e.g., through 
EEG or Questionnaire) 

50.0 

50.0 

50.0 

25.0 

37.5 

12.5 

25.0 

25.0 

25.0 

25.0 

37.5 

37.5 

Efficiency  in  Detection  Epilepsy  (e.g.,  through 
EEG or Questionnaire) 

25.0 

50.0 

25.0 

Accuracy 
Symptoms/Questionnaire 

in 

Epilepsy  Diagnosis 

via 

25.0 

50.0 

25.0 

Accuracy 
Analysis 

in  Epilepsy  Diagnosis  via  EEG 

0.0 

75.0 

25.0 

0.0 

0.0 

0.0 

0.0 

0.0 

0.0 

0.0 

Effectiveness  in  Predicting  Upcoming  Seizures 
(e.g., based on heart rate, sound analysis) 

12.5 

37.5 

25.0 

25.0 

Responsiveness  of 
System 

the  Application’s  Alert 

25.0 

37.5 

37.5 

Did  the  application  help  you  understand  your 
condition better? 

12.5 

50.0 

37.5 

0.0 

0.0 

88 

 
 
 
Did  the  application’s  predictive  alerts  improve 
your management of seizures? 

12.5 

62.5 

25.0 

Did the application assist in diagnosing epilepsy 
accurately? 

12.5 

62.5 

25.0 

Overall Rating of the Application: 

12.5 

50.0 

37.5 

0.0 

0.0 

0.0 

6. Conclusion   

This study successfully demonstrates that automatic detection of epileptic seizures using CNNs on audio recordings and HRV 
analysis is feasible and effective, addressing the limitations of time-intensive, manual annotations. The structured questionnaire 
developed  for  observable  seizure  characteristics  proved  highly  reliable,  achieving  an  impressive  sensitivity  of  95.10%  and 
specificity  of  97.06%.  The  binary  classification  approach  categorizing  seizure-related  sounds,  along  with  leveraging  HRV 
features to detect pre-ictal states, enabled the model to maintain robust accuracy, with detection accuracy exceeding 92.5% and 
predictive accuracy over 91.5% despite noise interference. The system’s strong performance, validated by physician feedback at 
Mansoura University Hospital, highlights its potential for clinical use in patient monitoring. 

References 

[1]  Scheffer, I. E., Berkovic, S., Capovilla, G., Connolly, M. B., French, J., et al., "ILAE classification of the epilepsies: 

Position paper of the ILAE Commission for Classification and Terminology," Epilepsia, 2017. 

[2]  Akyuz, E., Paudel, Y., Polat, A. K., Dundar, H. E., and Angelopoulou, E., "Enlightening the neuroprotective effect of 
quercetin in epilepsy: From mechanism to therapeutic opportunities," Epilepsy Behav., vol. 115, pp. 107701, 2021, 
DOI: 10.1016/j.yebeh.2020.107701. 

[3]  World 

Health 

Organization, 

"World 

health 

organization," 

[Online]. 

Available: 

http://www.who.int/mediacentre/factsheets/fs999/en/, Accessed on: Feb. 7, 2024. 

[4]  Nijsen, T. M. E., Cluitmans, P. J. M., Arends, J. B. A. M., and Griep, P. A. M., "Detection of subtle nocturnal motor 
activity from 3-d accelerometry recordings in epilepsy patients," IEEE Trans. Biomed. Eng., vol. 54, no. 11, pp. 2073–
2081, 2007. 

[5]  Stafstrom, C. E., and Carmant, L., "Seizures and Epilepsy: An Overview for Neuroscientists,"  Cold Spring Harb. 

Perspect. Med., 2015. 

[6]  Zhang,  L., Wang, X., Jiang, J., Xiao, N., Guo, J., Zhuang,  K., et al., "Automatic interictal epileptiform discharge 
(IED)  detection  based  on  convolutional  neural  network  (CNN),"  Front.  Mol.  Biosci.,  2023,  DOI: 
10.3389/fmolb.2023.1146606. 

[7]  Sharmila,  Raj, A.,  Pandey,  S.,  and  Mahalakshmi,  P.,  "Epileptic  seizure  detection  using  DWT-based  approximate 
entropy, Shannon entropy and support vector machine: a case study," J. Med. Eng. Technol., vol. 42, pp. 1–8, 2018. 

[8]  Kurada, A. V., Srinivasan, T., Hammond, S., Ulate-Campos, A., Bidwell, J., "Seizure detection devices  for use in 
antiseizure  medication  clinical  trials:  A  systematic  review,"  Seizure,  vol.  66,  pp.  61–69,  2019,  DOI: 
10.1016/j.seizure.2019.02.007. 

[9]  Xiaoyan,  W.,  Zhang,  Z.,  and  Zhou,  Y.,  "Epileptic  seizure  detection  from  multivariate  sequential  signals  using 

multidimensional convolution network," Res. Square, 2022, DOI: 10.21203. 

[10]  Moridani, M. K., and Farhadi, H., "Heart rate variability as a biomarker for epilepsy seizure prediction," Bratisl. Med. 

J., vol. 118, no. 1, pp. 21–25, Jan. 2017, DOI: 10.4149/BLL_2017_001. 

[11]  Zambrana-Vinaroz,  D.,  Vicente-Samper,  J.  M.,  Manrique-Cordoba,  J.,  and  Sabater-Navarro,  J.  M.,  "Wearable 
epileptic  seizure  prediction  system  based  on  machine  learning  techniques  using  ECG,  PPG  and  EEG  signals," 
Sensors, vol. 22, no. 23, pp. 9372, 2022, DOI: 10.3390/s22239372. 

[12]  Saminu, S., Xu, G., Zhang, S., Ab El Kader, I., Aliyu, H. A., Jabire, A. H., et al., "Applications of artificial intelligence 
in automatic detection of epileptic seizures using EEG signals: A review," Artif. Intell. Appl., vol. 1, pp. 11–25, 2022. 

[13]  Ryu, S., and Joe, I., "A hybrid DenseNet-LSTM model for epileptic seizure prediction," Appl. Sci., vol. 11, no. 7661, 

2021. 

[14]  Lourenço, C. da S., Tjepkema-Cloostermans, M. C., and van Putten, M. J. A. M., "Machine learning for detection of 
epileptiform  discharges,"  Clin.  Neurophysiol.,  vol.  132,  pp.  1433–1443,  2021,  DOI: 

interictal 
10.1016/j.clinph.2021.02.403. 

[15]  Zhengdao, L., Hwang, K.,  Li, K., and Wu, J., "Graph generative  neural  network  for EEG based epileptic seizure 

detection via discovery of dynamic brain functional connectivity," Sci. Rep., vol. 12, no. 18998, 2023. 

89 

 
[16]  Lee, D., Kim, B., Kim, T., Joe, I., Chong, J., Min, K., and Jung, K., "A ResNet-LSTM hybrid model for predicting 
epileptic seizures using a pretrained model with supervised contrastive learning," Sci. Rep., vol. 14, no. 1319, 2024, 
DOI: 10.1038/s41598-023-43328-y. 

[17]  Srivastava, S., Manjunath, R. K., and Shanthi, P., "Design, simulation and fabrication of a microstrip bandpass filter," 

Int. J. Sci. Eng. Appl., vol. 3, no. 5, pp. 45–58, 2014, ISSN 2319-7560. 

[18]  Al Younis, S. M., Hadjileontiadis, L. J., Khandoker, A. H., Stefanini, C., Soulaidopoulos, S., et al., "Prediction of 
heart failure patients with distinct left ventricular ejection fraction levels using circadian ECG features and machine 
learning," PLOS ONE, vol. 13, May 2024, DOI: 10.1371/journal.pone.0302639. 

[19]  Absar, N., et al., "The efficacy of machine-learning-supported smart system for heart disease prediction," Healthcare, 

vol. 10, no. 6, 2022. 

[20]  Song, K., et al., "An intelligent epileptic prediction system based on synchrosqueezed wavelet transform and multi-

level feature CNN for smart healthcare IoT," Sensors, vol. 22, no. 27, Aug. 2022. 

[21]  Wu, X., et al., "Epileptic seizure prediction using successive variational mode decomposition and transformers deep 

learning network," Front. Neurosci, vol. 26, Sept. 2022. 

[22]  Singh,  K.,  et  al.,  "Two-layer  LSTM  network-based  prediction  of  epileptic  seizures  using  EEG  spectral  features," 

Complex & Intell. Syst., 2022. 

[23]  Yu, J., et al., "AI-based stroke disease prediction system using real-time electromyography signals," Appl. Sci., vol. 

28, Sept. 2020. 

[24]  Yamakawa, T., et al., "Wearable epileptic seizure prediction system with machine-learning-based anomaly detection 

of heart rate variability," Sensors, vol. 20, no. 17, July 2020. 

[25]  Al-Hammadi,  F.  M.,  "The  impact  of  audio  classification  on  detecting  seizures  and  psychogenic  non-epileptic 

seizures," 2015. 

[26]  Arends, J., van Dorp, J., van Hoek, D., Kramer, N., van Mierlo, P., van der Vorst, D., and Tan, F. I. Y., "Diagnostic 
accuracy of audio-based seizure detection in patients with severe epilepsy and an intellectual disability,"  Epilepsy 
Behav., vol. 62, pp. 180–185, 2016. 

[27]  de Bruijne, G. R., Sommen, P. C. W., and Aarts, R. M., "Detection of epileptic seizures through audio classification," 
in 4th Eur. Conf. Int. Fed. Med. Biol. Eng., J. Vander Sloten, P. Verdonck, M. Nyssen, and J. Haueisen, Eds. Berlin, 
Germany: Springer, 2009, pp. 1450–1454. 

[28]  Srivastava, S., Manjunath, R. K., and Shanthi, P., "Design, simulation and fabrication of a microstrip bandpass filter," 

Int. J. Sci. Eng. Appl., vol. 3, no. 5, pp. 45–58, 2014. 

[29]  West, R., "Understanding the accuracy of diagnostic and serology tests: Sensitivity and specificity," Johns Hopkins 

Center for Health Security, Dec. 2020. 

90
