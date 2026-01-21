#!/bin/bash

# Set the directory
cd /home/paulin/Documents/Epilepsie/all_papers_md

papers=(
    "Spahr et al. - 2025 - Deep learning-based detection of generalized convulsive seizures using a wrist-worn accelerometer.md"
    "Reintjes et al. - 2025 - ECG-Based Detection of Epileptic Seizures in Real-World Wearable Settings Insights from the SeizeIT.md"
    "Fine - 2025 - Detection is Key Automated Tonic Seizure Detection With a Wearable Device.md"
    "Dong et al. - 2026 - Detection of nocturnal epileptic seizures using a wearable armband A deep learning approach combini.md"
    "Wang et al. - 2025 - Epileptic Seizure Detection Based on Attitude Angle Signal of Wearable Device.md"
    "Singh Rathore et al. - 2024 - Development of a Multimodal Machine Learning Model for Seizure Detection Using Wearable Devices.md"
    "Elemam et al. - 2025 - Automated validated tool for epileptic seizure detection using deep learning.md"
    "Borujeny et al. - 2013 - Detection of Epileptic Seizure Using Wireless Sensor Networks.md"
    "Vieluf et al. - 2025 - Seizure monitoring by combined diary and wearable data A multicenter, longitudinal, observational s.md"
    "Meisel et al. - 2020 - Machine learning from wristband sensor data for wearable, noninvasive seizure forecasting.md"
    "Stirling et al. - 2021 - Forecasting Seizure Likelihood With Wearable Technology.md"
    "Nasseri et al. - 2021 - Ambulatory seizure forecasting with a wrist-worn device using long-short term memory deep learning.md"
    "Ode et al. - 2023 - Development of an epileptic seizure prediction algorithm using R–R intervals with self-attentive aut.md"
)

for paper in "${papers[@]}"; do
    echo "=== $paper ==="
    # Search for precision terms
    grep -n -i -E "precision|PPV|positive predictive value|PPR" "$paper" | head -10
    echo ""
done