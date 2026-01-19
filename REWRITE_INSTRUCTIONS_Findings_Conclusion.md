# Systematic Rewrite Instructions: Findings and Conclusion Sections

## Overview

This document provides instructions for systematically rewriting the Findings (`Sections(tex)/05_Findings_and_Takeaways.tex`) and Conclusion (`Sections(tex)/06_Conclusion2.tex`) sections to reflect the corrected data from the verification process.

---

## Part 1: Critical Data Corrections (Must Apply)

### 1.1 Dong et al. 2026 - Detection Latency Correction

**ERROR IDENTIFIED:**
- The paper mentions "caregiver response times... range from 30 s to several minutes" (line 1217-1218)
- This refers to CAREGIVER response time, NOT system detection latency
- System detection latency is NOT explicitly reported in the paper

**CURRENT TEXT TO CORRECT:**

In `05_Findings_and_Takeaways.tex`:
- Line 59: `$<$30~s` for Dong et al. latency → **CHANGE TO: `--` or `not reported`**
- Line 7 (Executive Summary): Any mention of detection latency for Dong → **VERIFY SOURCE**

In `06_Conclusion2.tex`:
- Any claims about detection latency for Dong et al. → **REMOVE or CORRECT**

**ACTION REQUIRED:**
```
SEARCH: "Dong.*30.*s" or "Dong.*latency"
REPLACE: Remove unsupported latency claims or mark as "not reported"
```

---

### 1.2 Spahr et al. 2025 - HMS 92.6 Correction

**ERROR IDENTIFIED:**
- HMS (Harmonic Mean Score) 92.6 is NOT found anywhere in the paper
- The paper reports: sensitivity 96%, FAR <1/8 days, latency 26 s median
- HMS metric is not used in this paper

**CURRENT TEXT TO CORRECT:**

In Table 2 (`04_Study_Comparison.tex` line 95):
- Already corrected to `--` for Other Metrics

**ACTION REQUIRED:**
```
VERIFY: No claims in Findings/Conclusion about "HMS 92.6" for Spahr
IF FOUND: Remove or replace with actual reported metrics
```

---

### 1.3 Wang et al. 2025 - Hospital Count Correction

**ERROR IDENTIFIED:**
- Paper uses TWO hospitals, not one (lines 32-34)
- "11 were from the Fourth Affiliated Hospital of Anhui Medical University and 17 from the Department of Neurology, Children's Hospital"

**CURRENT TEXT TO CORRECT:**

In `05_Findings_and_Takeaways.tex`:
- Any mention of "single hospital" for Wang → **CHANGE TO "two hospitals"**

**ACTION REQUIRED:**
```
SEARCH: "Wang.*single.*hospital" or similar
REPLACE: "two hospitals"
```

---

### 1.4 Nasseri 2021 - Latency Unit Correction

**ERROR IDENTIFIED:**
- Line 226: "Seizure alerts occurred on average 33 **min** before the EEG-recorded seizure onset"
- NOT 33 seconds - wrong unit

**CURRENT TEXT TO CORRECT:**

In `04_Study_Comparison.tex`:
- Line 111: Already corrected to `33~min`

In `05_Findings_and_Takeaways.tex`:
- Any mention of "33 s" or "33 seconds" for Nasseri → **CHANGE TO "33 min"**

In `06_Conclusion2.tex`:
- Any mention of Nasseri forecasting horizon → **VERIFY unit is minutes**

**ACTION REQUIRED:**
```
SEARCH: "Nasseri.*33.*s" or "Nasseri.*33.*second"
REPLACE: "33 min" or "33 minutes"
```

---

### 1.5 Reintjes et al. 2025 - "Responders" Clarification

**ERROR IDENTIFIED:**
- "55.6% responders" is a SUBGROUP DEFINITION (patients with >50 BPM HR change during seizures)
- This is NOT a detection success rate or performance metric
- Line 302: "55.55% of patients met the responder criterion"

**CURRENT TEXT TO CORRECT:**

In `05_Findings_and_Takeaways.tex`:
- Lines 8-9: Claims about ECG sensitivity/FAR trade-off → **VERIFY these are still accurate**
- Line 21: Any characterization of "responders" → **CLARIFY as subgroup definition**

**ACTION REQUIRED:**
```
VERIFY: All ECG trade-off claims reference the correct interpretation of "responders"
IF NEEDED: Add footnote: "Responders defined as patients with >50 BPM HR increase during seizures"
```

---

## Part 2: Verification Checklist for All Claims

### 2.1 Claims Requiring Source Verification

For each claim in Findings/Conclusion, verify:

| Claim Type | Verify Against | Correct Source Required |
|------------|----------------|------------------------|
| Sensitivity values | Individual papers | Exact line number |
| FPR/FAR values | Individual papers | Exact line number |
| Detection latency | Individual papers | Exact line number |
| Patient success rates | Individual papers | Exact line number |
| Validation methodology | Individual papers | Exact line number |
| Study design (prospective/retro) | Individual papers | Exact line number |

### 2.2 Specific Claims to Verify

**In `05_Findings_and_Takeaways.tex`:**

1. **Line 8**: "ECG-only methods exhibit a severe sensitivity-FAR trade-off where high sensitivity (96-98%) requires 13-40 FA/h"
   - **VERIFY**: Source for these specific numbers
   - **CORRECT SOURCE**: Reintjes et al. 2025, Table 3

2. **Line 9**: "Only 43.5-83% of patients achieve better-than-chance performance"
   - **VERIFY**: 43.5% comes from Meisel et al. (line 1724)
   - **VERIFY**: 83% comes from Nasseri (5/6 patients)
   - **CORRECT**: These numbers are accurate

3. **Line 10**: "Only three of 13 studies use prospective validation"
   - **VERIFY**: Spahr 2025 (Phase 2), Dong 2026 (prospective), Elemam 2025 (cross-sectional)
   - **CORRECT**: This is accurate

4. **Line 14**: "Nighttime false alarm rates (1/61 nights)"
   - **VERIFY**: Source for this statistic
   - **ACTION**: FIND SOURCE or REMOVE if unsupported

5. **Line 19**: Spahr "required a 30-model ensemble CNN"
   - **VERIFY**: Does Spahr use 30 models? Check source
   - **ACTION**: Verify exact ensemble size

6. **Line 21**: Matrix Profile sensitivity/FAR values
   - **VERIFY**: Reintjes et al. 2025, Table 3
   - **VALUES**: 98.16% sens at 13.90 FA/h (sens-opt), 38.04% sens at 1.91 FA/h (FAR-opt)
   - **CORRECT**: These match Table 3

7. **Line 23**: "heart rate increases approximately 100 seconds before movement onset"
   - **VERIFY**: FIND SOURCE for this claim
   - **ACTION**: Locate exact paper and line number

8. **Line 29**: "only 43.5% of patients achieve better-than-chance performance"
   - **VERIFY**: Meisel et al. 2020, line 1724
   - **CORRECT**: Accurate

**In `06_Conclusion2.tex`:**

1. **Line 7**: "only two of nine detection studies approach the ILAE Phase 3 benchmark"
   - **VERIFY**: Which two studies? (Fine 2025, Dong 2026)
   - **CORRECT**: This is accurate

2. **Line 15**: "only 43.5% of patients achieve better-than-chance forecasting performance"
   - **VERIFY**: Meisel et al. 2020, line 1724
   - **CORRECT**: Accurate

3. **Line 21**: "monitoring durations vary widely across studies"
   - **VERIFY**: Check each study for monitoring duration
   - **ACTION**: Compile table of monitoring durations

---

## Part 3: Systematic Rewrite Procedure

### Step 1: Create Citation-Claim Mapping Table

For each citation in Findings/Conclusion, create a mapping:

```
| Citation | Claim Made | Verified? | Correct Source | Action Needed |
|----------|------------|-----------|----------------|---------------|
| @spahr2025 | 96% sensitivity, <1/8d FAR | Yes | Line 116, 117 | None |
| @dong2026 | <30 s latency | NO | Not reported | REMOVE |
| @wang2025 | Single hospital | NO | Lines 32-34 | CHANGE TO "Two hospitals" |
| ... | ... | ... | ... | ... |
```

### Step 2: Rewrite Executives Summary

**Current Executive Summary Issues:**
1. Dong latency claim (<30 s) - **REMOVE**
2. Nighttime FAR (1/61 nights) - **VERIFY SOURCE**
3. HR increase 100 s before movement - **VERIFY SOURCE**

**Rewrite Template:**
```latex
\item \textbf{Convulsive seizure detection achieves clinical viability:} Non-EEG biosignals, primarily accelerometry, detect convulsive seizures with [CORRECT RANGE]% sensitivity. [REVISED ECG CLAIM with source citations].

\item \textbf{Seizure forecasting remains immature:} Only [CORRECT RANGE]% of patients achieve better-than-chance performance [with correct citations].
...
```

### Step 3: Rewrite Detection Performance Section

**Key Actions:**
1. Remove unsupported Dong latency claim
2. Verify all ECG trade-off numbers with Reintjes Table 3
3. Add clarification about "responders" being a subgroup definition
4. Verify nighttime vs daytime FAR comparison source

### Step 4: Rewrite Forecasting Performance Section

**Key Actions:**
1. Verify Nasseri latency is "33 min" not "33 s"
2. Verify all patient success rate calculations
3. Clarify which studies use LOSO vs patient-specific tuning

### Step 5: Update Tables

**Table in Findings (lines 49-63):**
```
| Study | Seizure Type | Sens. | FAR | Latency | Validation |
|-------|-------------|-------|-----|---------|------------|
| Fine 2025 | Tonic | 100% | 0.023/h | 14 s | Phase 1 |
| Dong 2026 | Nocturnal severe | 71.6% | 0.165/h | -- | Prospective |
| Spahr 2025 | Convulsive | 96% | <1/8d | 26 s | Phase 2 |
```

**NOTE**: Dong latency changed from `<30 s` to `--` (not reported)

### Step 6: Rewrite Conclusion Section

**Key Actions:**
1. Remove or correct any mentions of Dong detection latency
2. Verify all aggregated statistics are correct
3. Ensure consistency with corrected tables

---

## Part 4: Priority Action Items

### High Priority (Errors That Change Meaning)

1. **DONG LATENCY**: Remove all mentions of "<30 s" detection latency
   - Files affected: `05_Findings_and_Takeaways.tex` line 59, any Conclusion mentions
   - Action: Change to "not reported" or remove claim

2. **NASSERI LATENCY**: Change "33 s" to "33 min"
   - Files affected: All mentions in Findings/Conclusion
   - Action: Global find/replace with verification

3. **WANG HOSPITALS**: Change "single hospital" to "two hospitals"
   - Files affected: All mentions in Findings/Conclusion
   - Action: Update with correct count

4. **REINTJES RESPONDERS**: Clarify this is a subgroup definition
   - Files affected: Any ECG trade-off discussion
   - Action: Add explanatory footnote

### Medium Priority (Claims Needing Verification)

5. **HR INCREASE TIMING**: "100 seconds before movement onset"
   - Action: FIND SOURCE or remove claim

6. **NIGHTTIME FAR**: "1/61 nights" vs "1/9 days"
   - Action: VERIFY SOURCE

7. **SPAHR 30-MODEL ENSEMBLE**: Verify ensemble size
   - Action: Check paper for exact number

### Low Priority (Consistency Checks)

8. **CITATION CONSISTENCY**: Ensure all citations match bibliography
9. **METRIC UNITS**: Ensure all time units are consistent (s, min, h, d)
10. **STUDY COUNTS**: Verify "X of 13 studies" claims are accurate

---

## Part 5: Verification Checklist Before Finalizing

### For Each Paragraph:

- [ ] Every numerical claim has a source citation
- [ ] Every citation matches the verified data from papers
- [ ] No unsupported claims about detection latency
- [ ] All time units are correct (s vs min, h vs d)
- [ ] Patient success rates are explicitly calculated or marked as "not reported"
- [ ] ECG "responders" are clarified as subgroup definition
- [ ] Study counts (e.g., "3 of 13 studies") are accurate
- [ ] Hospital/center counts are correct
- [ ] Validation methodology is correctly described

### For Tables:

- [ ] All numbers match the corrected source tables
- [ ] Latency column reflects actual reported values
- [ ] FAR/FPR units are consistent
- [ ] Patient success rates are accurately represented
- [ ] Validation labels are correct (Phase 1, Phase 2, LOSO, etc.)

---

## Part 6: Suggested Rewrites

### Suggested Rewrite for Executive Summary (Line 7-14)

```latex
\subsection{Executive Summary}

\begin{itemize}
    \item \textbf{Convulsive seizure detection achieves clinical viability:} Non-EEG biosignals, primarily accelerometry, detect convulsive seizures with 71.6-100\% sensitivity. \parencite{fineDetectionKeyAutomated2025} achieved 100\% sensitivity at 0.023/h FAR for tonic seizures with 14-second mean latency. \parencite{dongDetectionNocturnalEpileptic2026} demonstrated 71.6\% sensitivity at 0.165/h FAR for nocturnal seizures. \parencite{spahrDeepLearningbasedDetection2025} achieved 96\% sensitivity for convulsive seizures at $<$1/8 nights FAR. ECG-based methods exhibit a severe sensitivity-FAR trade-off where high sensitivity (96.98\%) requires 13-40~FA/h, while low FAR (0.05-4.2/h) yields only 1.8-61\% sensitivity \parencite{reintjesECGBasedDetectionEpileptic2025}.

    \item \textbf{Seizure forecasting shows patient heterogeneity:} Only 43.5\% of patients achieve better-than-chance forecasting performance under LOSO validation \parencite{meiselMachineLearningWristband2020}. Patient success rates range from 43.5\% to 100\% across studies, with no reliable predictors of which patients will respond.

    \item \textbf{Validation rigor is insufficient:} Only three of 13 studies use prospective validation and only one employs LOSO cross-validation, raising concerns about model generalizability.
\end{itemize}
```

### Suggested Rewrite for Detection Performance Table

```latex
\begin{table}[htbp]
\centering
\small
\caption{Highest Performing Detection Studies by Metric}
\label{tab:detection-performance}
\begin{tabular}{llcccc}
\toprule
\textbf{Study} & \textbf{Seizure Type} & \textbf{Sens.} & \textbf{FAR} & \textbf{Latency} & \textbf{Validation} \\
\midrule
\parencite{fineDetectionKeyAutomated2025} & Tonic & 100\% & 0.023/h & 14~s & Phase 1 \\
\parencite{dongDetectionNocturnalEpileptic2026} & Nocturnal severe & 71.6\% & 0.165/h & -- & Prospective \\
\parencite{spahrDeepLearningbasedDetection2025} & Convulsive & 96\% & $<$1/8d & 26~s & Phase 2 \\
\bottomrule
\end{tabular}
\end{table}
```

**NOTE**: Dong latency changed from `<30 s` to `--` (system latency not reported, only caregiver response time mentioned)

---

## Part 7: Final Verification Commands

### LaTeX Compilation Check:
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Grep Commands for Verification:

```bash
# Find all mentions of detection latency
grep -n "latency\|30 s\|detection time" Sections(tex)/05_Findings_and_Takeaways.tex
grep -n "latency\|30 s\|detection time" Sections(tex)/06_Conclusion2.tex

# Find all mentions of "single hospital"
grep -n "single hospital" Sections(tex)/05_Findings_and_Takeaways.tex
grep -n "single hospital" Sections(tex)/06_Conclusion2.tex

# Find all mentions of "33 s" or "33 seconds" (Nasseri)
grep -n "33 s\|33 second" Sections(tex)/05_Findings_and_Takeaways.tex
grep -n "33 s\|33 second" Sections(tex)/06_Conclusion2.tex

# Find all numerical performance claims
grep -n "[0-9]\+%" Sections(tex)/05_Findings_and_Takeaways.tex
```

---

## Summary of Required Changes

| File | Line(s) | Change Required |
|------|---------|-----------------|
| `05_Findings_and_Takeaways.tex` | 59 | Dong latency: `<30~s` → `--` |
| `05_Findings_and_Takeaways.tex` | 8-9 | Verify ECG trade-off numbers |
| `05_Findings_and_Takeaways.tex` | 14 | Verify nighttime FAR source |
| `05_Findings_and_Takeaways.tex` | 23 | Verify HR increase timing source |
| `05_Findings_and_Takeaways.tex` | Any | Change "single hospital" → "two hospitals" for Wang |
| `06_Conclusion2.tex` | Any | Change "33 s" → "33 min" for Nasseri |
| Both files | Any | Remove unsupported Dong latency claims |
| Both files | Any | Verify all aggregated statistics |

