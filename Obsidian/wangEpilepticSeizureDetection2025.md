---
title: "Epileptic Seizure Detection Based on Attitude Angle Signal of Wearable Device"
authors: Jiabing Wang, Dinghan Hu, Xiaoping Lai, Tao Jiang, Tiejia Jiang, Feng Gao, Pierre-Paul Vidal, Jiuwen Cao
zotero_citekey: wangEpilepticSeizureDetection2025
aliases: ["wangEpilepticSeizureDetection2025"]
tags: 
  - zotero 
---



- [Open in Zotero](zotero://select/library/items/GXZQKX57)
- url: https://ieeexplore.ieee.org/document/10857465/
- [Open PDF]([Full Text PDF](file:///home/paulin/Zotero/storage/5ZC5TRLU/Wang%20et%20al.%20-%202025%20-%20Epileptic%20Seizure%20Detection%20Based%20on%20Attitude%20Angle%20Signal%20of%20Wearable%20Device.pdf))
# Abstract
Wearable wristband device-based epilepsy detection has the merits of noninvasiveness, portability, low costs, and good environmental adaptability. However, attention has been paid to exploring the attitude angle signals collected by wearable devices for epilepsy detection. In this article, a systematic analysis of whether the wearable device-based attitude angle signals, particularly the PITCH and ROLL angles, can be applied to epilepsy seizure detection, is studied. The relationship among attitude angle signals, acceleration, and angular velocity signals at the feature level is analyzed, and the detection effectiveness of combining different attitude angle features for classifier training and testing is presented and discussed. The long-term recorded data were collected by wearable devices from 28 epileptic patients, of which 11 were from the Fourth Affiliated Hospital of Anhui Medical University and 17 from the Department of Neurology, Children’s Hospital, Zhejiang University School of Medicine. Each recording includes the measurement of three-axis acceleration (ACC), three-axis gyroscope (GYR), ROLL, PITCH, surface electromyography (SEMG), and electrodermal activity (EDA), with at least one seizure recorded for each subject. Experimental results show that ROLL and PITCH angles can be utilized for epilepsy detection, with better performance than using ACC and GYR. Moreover, the attitude angle feature training by a long short-term memory (LSTM) network can achieve the highest accuracy and efficiency.


# Highlights

## Introduction / Motivation


> [!cite]
> 28 epileptic patients, of which 11 were from the Fourth Affiliated Hospital of Anhui Medical University and 17 from the Department of Neurology, Children’s Hospital, Zhejiang University School of Medicine.
> [Page 2505010](zotero://open-pdf/library/items/5ZC5TRLU?page=2505010&annotation=5ZMZJSZP)
> > [!note]
> > study group hospital



> [!cite]
> hree-axis acceleration (ACC), three-axis gyroscope (GYR), ROLL, PITCH, surface electromyography (SEMG), and electrodermal activity (EDA), with at least one seizure recorded for each subject.
> [Page 2505010](zotero://open-pdf/library/items/5ZC5TRLU?page=2505010&annotation=YS8IAI5N)
> > [!note]
> > ACC gyro, S-EMG, EDA used



## Methodology


> [!cite]
> Combination 1 as ACC + GYR + SEMG + EDA, the signal types used in Combination 2 as ACC + GYR + PITCH + SEMG + EDA, the signal types used in Combination 3 as ACC + GYR + ROLL + SEMG + EDA, and the signal types used in Combination 4 as ACC + GYR + PITCH + ROLL + SEMG + EDA.
> [Page 2505015](zotero://open-pdf/library/items/5ZC5TRLU?page=2505015&annotation=XE6GX4S2)
> > [!note]
> > Combinations used



> [!cite]
> E. LSTM-Based Seizure Detection
> [Page 2505017](zotero://open-pdf/library/items/5ZC5TRLU?page=2505017&annotation=5IGLELX4)


> [!cite]
> model training comes from patient IDs 1–18 (3197 samples), in which 2558 samples were for tenfold cross-validation, and the long-term data from patient IDs 19–28 were reserved for testing
> [Page 2505017](zotero://open-pdf/library/items/5ZC5TRLU?page=2505017&annotation=68U5PANJ)
> > [!note]
> > good split on the patients to make it patient independant



## General Shortcomings


## Results of Study


> [!cite]
> Moreover, the attitude angle feature training by a long short-term memory (LSTM) network can achieve the highest accuracy and efficiency.
> [Page 2505010](zotero://open-pdf/library/items/5ZC5TRLU?page=2505010&annotation=ABCI7FEW)
> > [!note]
> > used LSTM



> [!cite]
> The PITCH-based trained LDA classifier achieved 78.20% accuracy, 83.20% precision, and 58.70% recall. Compared to ACC and GYR, it is 3.8% and 4.6% higher in accuracy, 4.7% and 7% higher in precision, and 7.1% and 7% higher in recall. The LDA classifier trained on ROLL achieved 78.70% accuracy, 87.10% precision, and 56.40% recall. Compared to ACC and GYR, it is 4.3% and 5.1% higher in accuracy, 8.6% and 10.9% higher in precision, and 4.8% and 4.7% higher in recall.
> [Page 2505014](zotero://open-pdf/library/items/5ZC5TRLU?page=2505014&annotation=ZVEF32MA)
> > [!note]
> > on the different combinations of signals



> [!cite]
> For classifier 1, four seizures were successfully detected with an overall classification accuracy of 80.1%, and a total of 11 false alarms occurred in the offline data with a cumulative length of 30.24 h, with the false alarm rate of 8.73/24 h. For classifier 2, five seizures were successfully detected with a classification accuracy of 83.4%, and a total of 10 false alarms occurred in the offline data with a cumulative length of 28.36 h, with the false alarm rate of 8.46/24 h. For classifier 3, seizures were successfully detected four times with an accuracy of 82.5%, and a total of 9 false alarms occurred in the offline signals with a cumulative length of 25.36 h, with the false alarm rate of 8.51/24 h.
> [Page 2505017](zotero://open-pdf/library/items/5ZC5TRLU?page=2505017&annotation=BICZ8M2Z)
> > [!note]
> > results are not perfect



> [!cite]
> have demonstrated that the attitude angle signal has the potential to replace GYR based on three metrics from three classifiers
> [Page 2505018](zotero://open-pdf/library/items/5ZC5TRLU?page=2505018&annotation=M6PTXS5J)


> [!cite]
> conclude that both PITCH and ROLL can also serve as substitutes for GYR in seizure detection for epilepsy
> [Page 2505018](zotero://open-pdf/library/items/5ZC5TRLU?page=2505018&annotation=HRUCVPTL)


> [!cite]
> In the epileptic seizure detection system, employing traditional features in time, frequency, and nonlinear domains for classifier training with a sliding window overlap rate of 0% leads to a significant increase in false alarm rates during actual performance. However, this issue can be mitigated by incorporating deep learning techniques and increasing the overlap rate.
> [Page 2505018](zotero://open-pdf/library/items/5ZC5TRLU?page=2505018&annotation=3TX9FLC7)
> > [!note]
> > no overlap leads to more false alarms



> [!cite]
> Through three classifiers (Tree, SVM, and LDA), it is proved that the attitude angle signal can be used for seizure detection and outperforms the commonly used ACC signal as well as the GYR signal in terms of the indicators of accuracy, precision, and recall.
> [Page 2505018](zotero://open-pdf/library/items/5ZC5TRLU?page=2505018&annotation=3APEAGCE)
> > [!note]
> > classifiers are better performant^



> [!cite]
> It is concluded that the attitude angle  signals (PITCH and ROLL) replace the ACC to realize the seizure detection of epilepsy by the two metrics of accuracy and false alarm rate.
> [Page 2505018](zotero://open-pdf/library/items/5ZC5TRLU?page=2505018&annotation=X3YY8WBB)


> [!cite]
> Since the attitude angle signal is a single-channel signal, while ACC and GYR are three-channel signals, the algorithmic processing of the attitude angle signal in the preprocessing step is more efficient in terms of preprocessing speed.
> [Page 2505018](zotero://open-pdf/library/items/5ZC5TRLU?page=2505018&annotation=VNJ6KJ2C)
> > [!note]
> > attitude angle is only one signal and  more efficient



## Other Studies Findings


> [!cite]
> f 8.51/24 h. In a study by Boon et al. [35], an ECG-based actionbased seizure detection system was developed with a final accuracy of 81.8% and a false alarm rate of 11.76/24 h.
> [Page 2505017](zotero://open-pdf/library/items/5ZC5TRLU?page=2505017&annotation=P5CLSUHN)


> [!cite]
> The study by van Andel et al. [36] used acceleration signals and electromyographic signals for action-based seizure detection with a final median accuracy of 79% and a median false alarm rate of 12/24 h.
> [Page 2505017](zotero://open-pdf/library/items/5ZC5TRLU?page=2505017&annotation=9YAIKT3Q)


> [!cite]
> In a study by Ge et al. [37], the ACC signal, angular velocity signal (GYR), SEMG signal, and EDA signal were used to detect epileptic seizures, and the sensitivity of the final classifier was 82.6%, with a false alarm rate of 8.63/24 h.
> [Page 2505017](zotero://open-pdf/library/items/5ZC5TRLU?page=2505017&annotation=A3QFUYT4)


## Constraints


## Other Annotations


# Notes
%% begin notes %%
%% end notes %%

%% Import Date: 2025-12-15T10:50:21.631+01:00 %%
