# ILAE Framework Integration Plan
## Comprehensive Plan for Integrating Essential Definitions Without Restoring Full Background Section

**Date:** 2026-01-26
**Purpose:** Address critique finding that ILAE framework and related clinical definitions are referenced but not defined, while avoiding full Background section restoration

---

## Problem Analysis

### Definitions Currently Missing (from Background section 3.4, lines 65-97)

| Term/Concept | Where Used (Undefined) | Impact |
|--------------|------------------------|--------|
| **ILAE Phases 0-4** | Abstract, Results 06/07/08/09, Discussion d1/d4, Conclusion | Readers cannot understand validation framework |
| **GTCS/FBTCS** | Abstract, Background, Results | Seizure types never explained |
| **Prospective/Pseudo-prospective/Retrospective** | Methods, Abstract | Study design terminology unclear |
| **FPR 0.05-0.1/h clinical significance** | Throughout | Why this threshold matters unclear |
| **Clinical tolerance for FAR** | Discussion d1 | User vs clinician expectations not established |

### Content Source: `02_background2.tex` Section 3.4 (lines 65-97)

This section contains all essential definitions:
- ILAE framework (Phases 0-4)
- Retrospective vs pseudo-prospective vs prospective
- Phase 3 benchmark (0.008-0.028/h FPR for GTCS/FBTCS)
- Clinical tolerance for false alarms
- ILAE recommendations for device use

---

## Proposed Solution: Add "Clinical Evaluation Frameworks" Subsection to Introduction

### Rationale

1. **Introduction is the logical place** for defining frameworks that guide the entire review
2. **Minimal structural change** - single new subsection, no new top-level section
3. **Early positioning** - defines terms before they're used in Methods and Results
4. **Natural flow** - follows "Key Research Question" and precedes "Methods"

### Location

Insert as **1.3** in `01_introduction3.tex` (after "Key Research Question")

---

## Detailed Content Plan

### New Subsection: "Clinical Evaluation Frameworks"

**Structure:**

```
1.3 Clinical Evaluation Frameworks
  1.3.1 ILAE Phased Validation Framework
  1.3.2 Study Design Classifications
  1.3.3 Clinical Performance Benchmarks
```

**Content to Include (extracted and condensed from Background 3.4):**

#### 1.3.1 ILAE Phased Validation Framework

```
The clinical validity of seizure detection algorithms is assessed through
the International League Against Epilepsy (ILAE) phased framework,
which classifies studies into five validation phases:

- Phase 0: Proof of concept
- Phase 1: Retrospective analysis with small sample
- Phase 2: Minimum 10 patients with seizures, 15 recorded seizures
- Phase 3: Prospective, multicenter, >=30 seizures from >=20 patients,
           real-time detection in intended use environment
- Phase 4: Real-world home validation

Prospective trials (Phase 3) represent the clinical gold standard,
requiring locked algorithms, video-EEG reference, and testing on
unseen data from multiple centers.
```

#### 1.3.2 Study Design Classifications

```
This review distinguishes three study design types:

- Retrospective: Analysis of historical data with potential data leakage
  if non-chronological splits allow future information to inform training

- Pseudo-prospective: Chronologically ordered splits training only on
  past seizures to test on subsequent ones, providing more realistic
  performance estimates

- Prospective: Real-time testing on new patients with locked algorithms,
  representing the highest validation rigor
```

#### 1.3.3 Clinical Performance Benchmarks

```
The ILAE systematic review established performance benchmarks for
generalized tonic-clonic seizures (GTCS) and focal-to-bilateral
tonic-clonic seizures (FBTCS): 90-96% sensitivity with false alarm
rates of 0.2-0.67 per 24 hours (approximately 0.008-0.028/h).

For ambulatory use, acceptable false alarm rates depend on user
perspective. Patients and caregivers typically require 100% sensitivity
and accept approximately one false alarm per week. Clinicians consider
90% sensitivity adequate and tolerate two false alarms per week to
one per month.

Based on these benchmarks, an FPR below 0.05-0.1/h is considered
clinically acceptable for home monitoring devices.

Currently, the ILAE recommends wearable devices only for GTCS/FBTCS
detection in unsupervised patients, with weak/conditional recommendation
based on moderate evidence.
```

---

## Alternative Options (If User Prefers Different Approach)

### Option B: Separate Short Section Before Methods
- Create `02_Clinical_Framework.tex` as Section 2
- Move Methods to Section 3
- **Pros:** Dedicated section, easier to reference
- **Cons:** Adds another section to document, affects section numbering

### Option C: Integrate into Methods Section
- Add as introductory subsection to Methods
- **Pros:** Keeps all methodology together
- **Cons:** Methods becomes longer, framework defined after first mention

### Option D: Minimal Inline Definitions
- Add brief definitions where first used in Results
- **Pros:** Most concise
- **Cons:** Definitions scattered, no central reference

---

## Implementation Steps

### Step 1: Read and Verify Source Content
- Confirm `02_background2.tex` lines 65-97 contain all needed definitions
- Check citation keys are correct

### Step 2: Draft New Subsection
- Create condensed version of Background 3.4 content
- Ensure all style rules are followed (no em-dashes, no semicolons)
- Keep concise (target: ~40-50 lines total for all three sub-subsections)

### Step 3: Insert into Introduction
- Add to `01_introduction3.tex` after line 34 (end of Key Research Question)
- Use `\subsection{Clinical Evaluation Frameworks}` with `\subsubsection` for each part

### Step 4: Update Section Numbering (if needed)
- If using Option B, renumber subsequent sections

### Step 5: Verify Citations
- Ensure `beniczkyStandardsTestingClinical2018` and `beniczkyAutomatedSeizureDetection2021` are in bibliography
- Check all ILAE references work correctly

### Step 6: Test Compilation
- Run full LaTeX compilation to verify no errors
- Check formatting of new content

### Step 7: Cross-Check References
- Verify all instances of "ILAE Phase X" in document now have defined reference
- Verify GTCS/FBTCS mentioned earlier are now defined
- Verify prospective/retrospective terms are now clarified

---

## Content Reduction Strategy

To maintain conciseness (15-page limit), condense Background 3.4 as follows:

| Original Background 3.4 | Proposed Condensed Version |
|-------------------------|---------------------------|
| Full paragraph explanation of each phase | Bulleted list with key criteria |
| Detailed discussion of data leakage | One sentence on pseudo-prospective advantage |
| Extended tolerance discussion | Combined user-clinician comparison |
| ILAE recommendation context | Single sentence on current guidance |

**Target:** Reduce ~33 lines (Background 3.4) to ~40-50 lines spread across three focused sub-subsections

---

## Files to Modify

| File | Modification |
|------|--------------|
| `01_introduction3.tex` | Add new subsection 1.3 |
| `main.tex` | No change needed (Background stays commented) |
| `02_background2.tex` | No change (keep as reference source) |

---

## Quality Checklist

After implementation, verify:

- [ ] ILAE Phases 0-4 are clearly defined before first use
- [ ] GTCS/FBTCS seizure types are explained
- [ ] Prospective/pseudo-prospective/retrospective distinctions are clear
- [ ] FPR 0.05-0.1/h clinical significance is established
- [ ] No em-dashes used (check with grep)
- [ ] No semicolons used
- [ ] No AI-avoid words (crucial, pivotal, etc.)
- [ ] All citations work correctly
- [ ] LaTeX compiles without errors
- [ ] Content is concise (no unnecessary expansion)

---

## Estimated Effort

| Task | Estimated Effort |
|------|------------------|
| Draft new subsection content | 15-20 minutes |
| Insert and format in Introduction | 5 minutes |
| Verify citations and compile | 5 minutes |
| Quality check and style verification | 5-10 minutes |
| **Total** | **30-40 minutes** |

---

## Decision Point for User

Before proceeding, please confirm:

1. **Location preference:** Introduction subsection (Option A - recommended) vs separate section (Option B) vs Methods integration (Option C)?

2. **Level of detail:** Keep three sub-subsections (ILAE, Study Designs, Benchmarks) or combine into single shorter subsection?

3. **Seizure type definitions:** Include brief explanation of GTCS/FBTCS in this subsection or add inline where first mentioned in text?

---

**Plan created:** 2026-01-26
**Status:** COMPLETED - Implemented as Introduction subsection 1.3 with three sub-subsections
**Verified:** 2026-01-26 - All values confirmed correct, document compiles to 31 pages
**Correction made:** 2026-01-26 - Removed incorrect "0.05-0.1/h" attribution to ILAE Phase 3, correctly states "0.008-0.028/h" as ILAE Phase 3 benchmark

## Implementation Summary

**Location:** `01_introduction3.tex` lines 37-92
**Structure:**
- 1.3.1 ILAE Phased Validation Framework (lines 39-52)
- 1.3.2 Study Design Classifications (lines 54-67)
- 1.3.3 Clinical Performance Benchmarks (lines 69-92)

**Content added:**
- ILAE Phases 0-4 definitions
- GTCS/FBTCS seizure type explanations
- Prospective/pseudo-prospective/retrospective distinctions
- FPR clinical benchmarks (0.05-0.1/h)
- User vs clinician tolerance for false alarms
- ILAE recommendation context

**Quality checks passed:**
- No em-dashes
- No semicolons
- No AI-avoid words
- LaTeX compiles successfully (31 pages)
