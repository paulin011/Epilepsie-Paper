# LaTeX Emphasis Standard for Epilepsie Document

## Purpose
This document defines the unified standard for text emphasis across all LaTeX section files in the Epilepsie systematic review.

## Standard

| Context | Usage | LaTeX Command | Example |
|---------|--------|---------------|---------|
| ALL emphasis | All text emphasis - narrative, labels, tables, lists | `\textbf{}` | `\textbf{algorithmic refinement alone may be insufficient}` |
| Table headers | Column and row headers in tables | `\textbf{}` | `\textbf{Study} & \textbf{Objective}` |
| Table row labels | Study names or row identifiers | `\textbf{}` | `\textbf{Spahr et al. 2025}` |
| List labels | Labels in enumerated lists (e.g., "Keywords:") | `\textbf{}` | `\textbf{Keywords:}` |
| Bullet point headings | Bold headings at start of itemized bullets | `\textbf{}` | `\item \textbf{Convulsive seizure detection:}` |
| Section headings | Section and subsection titles | LaTeX sectioning commands | `\section{Introduction}` |

## What NOT to Use

| Command | Restriction |
|---------|-------------|
| `\textit{}` | Do not use - use `\textbf{}` instead |
| `\emph{}` | Do not use - use `\textbf{}` instead |
| Manual italics (`\itshape`) | Do not use |
| Underline (`\underline{}`) | Do not use in academic text |

## Rationale

1. **Uniform bold emphasis**: Using `\textbf{}` for all emphasis creates visual consistency throughout the document. Bold upright text is more readable than italic/slanted text.

2. **Simpler standard**: One command (`\textbf{}`) for all emphasis reduces cognitive load and prevents inconsistent formatting.

## Verification Checklist

After implementation, verify:
- [x] No `\textit{}` commands remain in section files
- [x] No `\emph{}` commands remain in section files
- [x] `\textbf{}` is used consistently for ALL emphasis
- [x] No manual markup like `{\itshape }` or `\underline{}`
