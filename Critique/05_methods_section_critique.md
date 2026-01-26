# Critique: Methods Section (03_Methods.tex and 3.1_Search_Strategy.tex)

**Date:** 2026-01-26
**Reviewer:** Research Methods Specialist

---

## Executive Summary

The methods section establishes a framework for a systematic review claiming to follow PRISMA 2020 guidelines and the Webster & Watson concept matrix approach. While the section demonstrates awareness of proper systematic review methodology, there are significant gaps in reproducibility, transparency, and rigor that must be addressed before the review can be considered methodologically sound. The most serious concern is the use of "gemini deep research" as an ad-hoc supplement to systematic database searching.

---

## 1. PRISMA Compliance Assessment

### 1.1 Strengths
- Explicit claim to follow PRISMA principles (citation to Tugwell 2021)
- Concept matrix framework from Webster & Watson (2002) is appropriately cited
- Inclusion/exclusion criteria are stated
- A PRISMA flow diagram is referenced and included (Figure prisma.pdf)
- PICO framework is mentioned and structured

### 1.2 Critical Gaps

**Missing PRISMA 2020 Required Elements:**

| PRISMA Item | Status | Issue |
|-------------|--------|-------|
| Protocol registration | Missing | No mention of PROSPERO registration or pre-registered protocol |
| Full search strategies | Missing | Actual query strings for IEEE Xplore, PubMed, Scopus not provided |
| Database search dates | Incomplete | No execution dates mentioned |
| Screening process details | Partial | No description of dual screening, inter-rater reliability |
| Risk of bias assessment | Missing | No quality assessment tool mentioned (e.g., QUADAS, Cochrane) |
| Data extraction procedure | Partial | No mention of dual extraction, piloting, or standardized forms |

### 1.3 PRISMA Flow Diagram
The section references `prisma.pdf` as a figure, which is good practice. However, the methods text does not describe what that diagram contains. A methods section should summarize the flow (identification, screening, eligibility, inclusion counts) even if a diagram is provided.

---

## 2. Search Strategy Rigor

### 2.1 Database Selection
**Assessment: Appropriate but incomplete**

The databases listed (IEEE Xplore, PubMed, Scopus) are reasonable for this topic. However:
- No justification for why these three were chosen
- No mention of other relevant databases (e.g., Web of Science, PsycINFO, Embase)
- Google Scholar is mentioned for "scoping" but its limitations are not discussed
- No mention of searching trial registries (e.g., ClinicalTrials.gov)

### 2.2 Search Strings - CRITICAL DEFICIENCY
**The search strings are not provided.**

The methods section states (line 12-13 of 03_Methods.tex):
> "Formal queries: IEEE Xplore, PubMed, and Scopus using controlled keyword strings..."

However, the actual search strings used are **never shown**. While PICO keywords are listed in Section 3.1, there is no indication of how these were combined into actual database queries. For reproducibility, the full search strings for each database must be provided, ideally as an appendix or supplementary material.

### 2.3 Time Frame Inconsistency
**Critical discrepancy found:**

| Document | Time Range Stated |
|----------|------------------|
| Abstract (00_Abstract.tex, line 7) | 2013-2026 |
| Methods (03_Methods.tex, line 8) | 2015-2025 |
| Exploration section (3.1_Search, line 43-44) | "expanding the time frame to 2013-2026" |

**Issue:** The methods section states searches were restricted to 2015-2025, but the abstract and exploration section reference 2013-2026. This is confusing and needs reconciliation. Did the initial search cover 2015-2025, then "exploration" extend it to 2013-2026? If so, this should be stated explicitly.

### 2.4 The "Exploration" Method - CRITICAL CONCERN
**Lines 39-44 of 3.1_Search Strategy.tex:**

> "Due to the insufficient amount of papers gathered from systematic review an exploration was done on the already existing papers. The exploration consisted of graph tools to visualize backlinks and gemini deep research feature to find relevant papers."

**Problems:**
1. **Non-systematic supplementation:** Using "gemini deep research" (an AI tool) undermines the systematic nature of the review
2. **Insufficient detail:** No description of what "graph tools" were used, what backlinks were examined
3. **Selection bias:** How were the 4 additional papers selected from AI suggestions?
4. **Undocumented methodology:** AI search behavior is opaque and non-reproducible
5. **Academic appropriateness:** Relying on proprietary AI search tools is generally not accepted in rigorous systematic reviews

**Recommendation:** This approach is methodologically problematic. If additional papers were needed, the proper approach would be to:
- Re-examine and broaden the systematic search strategy
- Consult with a librarian or information specialist
- Search additional databases
- Expand time parameters prospectively (not post-hoc)

---

## 3. PICO Framework Evaluation

### 3.1 Implementation Quality
**Overall: Good structure, poor execution**

The PICO framework is explicitly addressed (lines 4-36 of 3.1_Search Strategy.tex), which is a strength. Each component is defined:

- **P (Patient/Problem):** Well-defined with appropriate keywords
- **I (Intervention):** Comprehensive lists of biosignals and technologies
- **C (Comparison):** Uses exclusion logic for EEG studies
- **O (Outcome):** Lists relevant performance metrics

### 3.2 Issues with PICO Implementation

1. **MeSH term typo:** Line 15 shows `Se54izures` - appears to be a corruption of "Seizures"

2. **Boolean logic not specified:** The keywords are listed but not combined. How were they actually used in searches? For example:
   - Was it `(epilepsy OR seizure) AND (wearable) AND (deep learning)`?
   - How were exclusion terms applied?

3. **Database-specific adaptations:** The same keywords don't work identically across PubMed (uses MeSH), IEEE Xplore (controlled vocabulary differs), and Scopus. No mention of how queries were adapted per database.

---

## 4. Study Selection Process

### 4.1 What is Described
- Inclusion criteria: wearable/non-EEG signals, detection or prediction
- Exclusion criteria: EEG-only, invasive, simulation-only
- Deduplication mentioned (line 50 of 3.1_Search)

### 4.2 What is Missing

**Critical gaps in selection description:**

1. **Screening procedure:** No description of:
   - How many reviewers performed screening
   - Whether title/abstract screening was distinct from full-text review
   - How disagreements were resolved
   - Any pilot testing of screening criteria

2. **Eligibility assessment:** No details on:
   - How full texts were obtained
   - How many texts were reviewed
   - Reasons for exclusion at full-text stage

3. **Conference proceedings handling:** Line 48 mentions "few exceptions made regarding conference proceedings" but doesn't explain:
   - What criteria justified exceptions
   - Which conference proceedings were included
   - Why this deviation from the "journal articles" rule

---

## 5. Data Extraction

### 5.1 Extraction Fields
**Strength:** Comprehensive list of extracted dimensions (lines 29-66 of 03_Methods.tex)

The extraction fields are well-defined and align well with the research question. The division into two concept matrix tables (study-level and detailed metrics) follows the Webster & Watson approach appropriately.

### 5.2 Extraction Procedure - NOT DESCRIBED

**Missing information:**
- Who performed data extraction?
- Was there dual extraction with reconciliation?
- Were extraction forms piloted?
- How were discrepancies resolved?
- What was done when studies reported multiple metrics or multiple experiments?

The current section only describes *what* was extracted, not *how* it was extracted.

---

## 6. Quality Assessment and Risk of Bias

### 6.1 Current Status: ABSENT

**There is no mention of quality assessment or risk of bias evaluation.**

This is a major omission for a systematic review. Without quality assessment, readers cannot distinguish between high-quality and low-quality studies or understand potential biases.

### 6.2 What Should Be Included

For studies of diagnostic accuracy (which seizure detection studies essentially are), appropriate tools include:
- **QUADAS-2** (Quality Assessment of Diagnostic Accuracy Studies)
- **PROBAST** (Prediction model Risk Of Bias ASsessment Tool) for forecasting studies
- Custom quality criteria appropriate for wearable device validation

At minimum, the review should assess:
- Study design (prospective vs retrospective)
- Sample size adequacy
- Validation approach (LOSO vs temporal split vs internal)
- Risk of overfitting
- Clinical setting representativeness
- Reporting completeness

---

## 7. Clarity and Reproducibility

### 7.1 Reproducibility Assessment: POOR

**Another researcher could NOT reproduce this review based on the methods description alone.**

Critical missing elements for reproducibility:
1. Exact search strings for each database
2. Date ranges for each search execution
3. Complete inclusion/exclusion criteria with examples
4. Details on the AI-based "exploration" process
5. Specific handling of conference proceedings
6. Quality assessment methodology

### 7.2 Clarity Issues

1. **Terminology inconsistency:** The review uses both "detection" and "prediction" - are these being treated as distinct or is "prediction" inclusive of "forecasting"?

2. **Table structure confusion:** Lines 32-52 describe tables labeled "detection-matrix," "forecasting-matrix," etc., but it's unclear how many tables total and what their exact structure is.

3. **Vague language:** Phrases like "few exceptions made" (line 48) and "additional 4 papers were acquired" (line 42) lack precision.

---

## 8. Specific Recommendations for Revision

### Priority 1 (Essential for Methodological Soundness)

1. **Remove or justify the AI-based exploration**
   - Option A: Remove the 4 AI-sourced papers and rely only on systematic search
   - Option B: Provide detailed justification and describe a systematic approach to supplementing the search (e.g., hand-searching specific journals, expert consultation)
   - If retaining: fully describe the process and acknowledge as a limitation

2. **Provide full search strings**
   - Add an appendix with exact search strings for each database
   - Include search dates and result counts

3. **Add quality assessment**
   - Select an appropriate tool (QUADAS-2, PROBAST, or custom criteria)
   - Describe how quality assessment will be used in the synthesis

4. **Clarify time frame**
   - Reconcile the 2015-2025 vs 2013-2026 discrepancy
   - Clearly state when and why time parameters were expanded

5. **Describe selection process**
   - Who screened, how many stages, how conflicts resolved
   - Provide counts for each PRISMA stage (identify, screen, eligible, included)

### Priority 2 (Important for Transparency)

6. **Fix the MeSH term typo** (Se54izures)

7. **Justify database selection**
   - Explain why IEEE Xplore, PubMed, and Scopus were chosen
   - Acknowledge any relevant databases not searched

8. **Clarify conference proceeding handling**
   - Specify which conferences and why exceptions were made

9. **Describe data extraction procedure**
   - Single vs dual extraction
   - Pilot testing, standardization

10. **Register a protocol** (if not already done)
    - Consider PROSPERO or OSF registration
    - Even post-hoc registration with caveats is better than none

### Priority 3 (Helpful for Readers)

11. **Add a limitations subsection to Methods**
    - Acknowledge the AI supplementation upfront
    - Note language restrictions (if any)
    - Describe publication bias considerations

12. **Improve concept matrix description**
    - Provide a schematic or clearer description of the tables
    - Explain how the two-table approach enables synthesis

---

## 9. Summary Assessment

| Criterion | Rating | Comments |
|-----------|--------|----------|
| PRISMA compliance | Poor | Framework acknowledged but key elements missing |
| Search strategy rigor | Poor | No actual search strings provided; AI supplementation problematic |
| PICO implementation | Fair | Good structure, execution gaps, typo present |
| Study selection clarity | Poor | Process not described, counts missing |
| Data extraction | Fair | Fields well-defined, procedure not described |
| Quality assessment | Absent | Major omission |
| Reproducibility | Poor | Could not be reproduced from description |
| Overall clarity | Fair | Understandable but incomplete |

**Overall Verdict:** The methods section requires substantial revision to meet basic standards for a systematic review. The current state is more consistent with a narrative review that attempts to use systematic review language and structure, rather than a true systematic review.

---

## References

- Page MJ, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71.
- Rethlefsen ML, et al. PRISMA-S: an extension to the PRISMA statement for reporting literature searches in systematic reviews. Syst Rev. 2021.
- Webster J, Watson RT. Analyzing the past to prepare for the future: Writing a literature review. MIS Quarterly. 2002.

**Sources:**
- [The PRISMA 2020 statement: an updated guideline for ...](https://www.bmj.com/content/372/bmj.n71)
- [PRISMA statement](https://www.prisma-statement.org/)
- [An updated guideline for reporting systematic reviews - PubMed](https://pubmed.ncbi.nlm.nih.gov/33782057/)
- [2.4.8 Reporting the Search Strategy: PRISMA-S - JBI Global Wiki](https://jbi-global-wiki.refined.site/space/MANUAL/653000709)
