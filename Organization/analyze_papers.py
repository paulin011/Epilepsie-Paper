#!/usr/bin/env python3
"""
Paper Analysis Script for Epilepsy Literature Review
Analyzes markdown papers in Papers_md folder to extract key information.
"""

import os
import re
from pathlib import Path
from collections import Counter, defaultdict
import csv
import json

# Paths
PAPERS_MD_DIR = Path(__file__).parent.parent / "Papers_md"
OUTPUT_DIR = Path(__file__).parent
SCREENING_CSV = OUTPUT_DIR / "screening.csv"

# Keywords to search for in papers
MODALITY_KEYWORDS = {
    "ECG": ["ECG", "electrocardiogram", "electrocardiography"],
    "HRV": ["HRV", "heart rate variability", "heart-rate variability"],
    "PPG": ["PPG", "photoplethysmography", "photoplethysmogram"],
    "EDA": ["EDA", "electrodermal activity", "galvanic skin response", "GSR", "skin conductance"],
    "ACC": ["accelerometer", "accelerometry", "ACC", "motion sensor"],
    "EEG": ["EEG", "electroencephalogram", "electroencephalography"],
}

TASK_KEYWORDS = {
    "detection": ["seizure detection", "detect seizure", "detecting seizure", "ictal detection"],
    "prediction": ["seizure prediction", "predict seizure", "predicting seizure", "pre-ictal", "preictal"],
    "forecasting": ["seizure forecasting", "forecast seizure"],
}

STUDY_TYPES = {
    "review": ["review", "survey", "systematic review", "scoping review", "meta-analysis", "literature review"],
    "clinical_trial": ["clinical trial", "randomized", "RCT", "prospective study"],
    "retrospective": ["retrospective", "retrospectively"],
    "prospective": ["prospective", "pseudo-prospective"],
    "experimental": ["experimental", "proof-of-concept", "feasibility"],
}

EVALUATION_KEYWORDS = {
    "cross_validation": ["cross-validation", "cross validation", "k-fold", "leave-one-out", "LOOCV", "LOO"],
    "patient_independent": ["patient-independent", "subject-independent", "cross-patient", "cross-subject"],
    "patient_specific": ["patient-specific", "subject-specific", "personalized"],
}

DATASET_KEYWORDS = [
    "CHB-MIT", "CHBMIT", "Siena", "TUH", "Temple", "Physionet", 
    "Epilepsiae", "European Epilepsy Database", "Freiburg",
    "TUSZ", "SeizureIT", "wearable", "clinical", "EMU"
]

ML_KEYWORDS = {
    "deep_learning": ["CNN", "convolutional neural network", "LSTM", "RNN", "deep learning", 
                      "transformer", "autoencoder", "GAN", "neural network", "ResNet"],
    "traditional_ml": ["SVM", "support vector", "random forest", "decision tree", "XGBoost",
                       "logistic regression", "k-NN", "kNN", "naive bayes", "gradient boosting"],
    "signal_processing": ["wavelet", "FFT", "Fourier", "spectral analysis", "filtering", "bandpass"],
}


def extract_year_from_filename(filename: str) -> int | None:
    """Extract year from filename pattern 'Author - YEAR - Title.md'"""
    match = re.search(r'- (\d{4}) -', filename)
    if match:
        return int(match.group(1))
    return None


def extract_authors_from_filename(filename: str) -> str:
    """Extract authors from filename pattern 'Author - YEAR - Title.md'"""
    match = re.match(r'^(.+?) - \d{4} -', filename)
    if match:
        return match.group(1).strip()
    return ""


def extract_title_from_filename(filename: str) -> str:
    """Extract title from filename pattern 'Author - YEAR - Title.md'"""
    match = re.search(r'- \d{4} - (.+)\.md$', filename)
    if match:
        return match.group(1).strip()
    return filename.replace('.md', '')


def count_keyword_occurrences(text: str, keywords: list[str]) -> int:
    """Count how many times keywords appear in text (case-insensitive)"""
    text_lower = text.lower()
    count = 0
    for keyword in keywords:
        count += len(re.findall(r'\b' + re.escape(keyword.lower()) + r'\b', text_lower))
    return count


def detect_modalities(text: str) -> dict[str, int]:
    """Detect which modalities are mentioned in the paper"""
    results = {}
    for modality, keywords in MODALITY_KEYWORDS.items():
        count = count_keyword_occurrences(text, keywords)
        if count > 0:
            results[modality] = count
    return results


def detect_task(text: str) -> dict[str, int]:
    """Detect if paper is about detection, prediction, or both"""
    results = {}
    for task, keywords in TASK_KEYWORDS.items():
        count = count_keyword_occurrences(text, keywords)
        if count > 0:
            results[task] = count
    return results


def detect_study_type(text: str) -> list[str]:
    """Detect study type"""
    results = []
    text_lower = text.lower()
    for study_type, keywords in STUDY_TYPES.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                results.append(study_type)
                break
    return results


def detect_datasets(text: str) -> list[str]:
    """Detect which datasets are mentioned"""
    results = []
    text_lower = text.lower()
    for dataset in DATASET_KEYWORDS:
        if dataset.lower() in text_lower:
            results.append(dataset)
    return list(set(results))


def detect_ml_methods(text: str) -> dict[str, list[str]]:
    """Detect ML methods mentioned"""
    results = defaultdict(list)
    text_lower = text.lower()
    for category, keywords in ML_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                results[category].append(keyword)
    return dict(results)


def detect_evaluation(text: str) -> list[str]:
    """Detect evaluation methodology"""
    results = []
    for eval_type, keywords in EVALUATION_KEYWORDS.items():
        if count_keyword_occurrences(text, keywords) > 0:
            results.append(eval_type)
    return results


def extract_metrics(text: str) -> dict[str, bool]:
    """Detect which metrics are reported"""
    metrics = {
        "sensitivity": ["sensitivity", "recall", "true positive rate", "TPR"],
        "specificity": ["specificity", "true negative rate", "TNR"],
        "accuracy": ["accuracy"],
        "AUC": ["AUC", "area under curve", "ROC"],
        "F1": ["F1", "F-score", "F1-score"],
        "precision": ["precision", "positive predictive value", "PPV"],
        "FAR": ["false alarm rate", "FAR", "FPR", "false positive rate", "FA/h"],
    }
    results = {}
    for metric, keywords in metrics.items():
        results[metric] = count_keyword_occurrences(text, keywords) > 0
    return results


def analyze_paper(filepath: Path) -> dict:
    """Analyze a single paper and extract relevant information"""
    filename = filepath.name
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None
    
    # Extract basic info from filename
    year = extract_year_from_filename(filename)
    authors = extract_authors_from_filename(filename)
    title = extract_title_from_filename(filename)
    
    # Analyze content
    modalities = detect_modalities(content)
    tasks = detect_task(content)
    study_types = detect_study_type(content)
    datasets = detect_datasets(content)
    ml_methods = detect_ml_methods(content)
    evaluation = detect_evaluation(content)
    metrics = extract_metrics(content)
    
    # Word count
    word_count = len(content.split())
    
    return {
        "filename": filename,
        "title": title,
        "authors": authors,
        "year": year,
        "word_count": word_count,
        "modalities": modalities,
        "primary_modality": max(modalities, key=modalities.get) if modalities else None,
        "tasks": tasks,
        "primary_task": max(tasks, key=tasks.get) if tasks else None,
        "study_types": study_types,
        "datasets": datasets,
        "ml_methods": ml_methods,
        "evaluation": evaluation,
        "metrics": metrics,
        "uses_deep_learning": "deep_learning" in ml_methods,
        "uses_traditional_ml": "traditional_ml" in ml_methods,
        "is_ecg_based": "ECG" in modalities or "HRV" in modalities,
        "is_wearable": "wearable" in content.lower(),
    }


def generate_statistics(papers: list[dict]) -> dict:
    """Generate aggregate statistics from all papers"""
    stats = {
        "total_papers": len(papers),
        "years": Counter(),
        "modalities": Counter(),
        "tasks": Counter(),
        "study_types": Counter(),
        "datasets": Counter(),
        "ml_categories": Counter(),
        "evaluation_methods": Counter(),
        "metrics_reported": Counter(),
    }
    
    for paper in papers:
        if paper["year"]:
            stats["years"][paper["year"]] += 1
        
        for mod in paper["modalities"]:
            stats["modalities"][mod] += 1
        
        for task in paper["tasks"]:
            stats["tasks"][task] += 1
        
        for st in paper["study_types"]:
            stats["study_types"][st] += 1
        
        for ds in paper["datasets"]:
            stats["datasets"][ds] += 1
        
        for cat in paper["ml_methods"]:
            stats["ml_categories"][cat] += 1
        
        for ev in paper["evaluation"]:
            stats["evaluation_methods"][ev] += 1
        
        for metric, present in paper["metrics"].items():
            if present:
                stats["metrics_reported"][metric] += 1
    
    # Count specific categories
    stats["ecg_based_papers"] = sum(1 for p in papers if p["is_ecg_based"])
    stats["wearable_papers"] = sum(1 for p in papers if p["is_wearable"])
    stats["deep_learning_papers"] = sum(1 for p in papers if p["uses_deep_learning"])
    stats["traditional_ml_papers"] = sum(1 for p in papers if p["uses_traditional_ml"])
    
    return stats


def print_statistics(stats: dict):
    """Print statistics in a readable format"""
    print("\n" + "="*60)
    print("📊 PAPER ANALYSIS SUMMARY")
    print("="*60)
    
    print(f"\n📚 Total Papers Analyzed: {stats['total_papers']}")
    
    print("\n📅 Papers by Year:")
    for year in sorted(stats["years"].keys()):
        count = stats["years"][year]
        bar = "█" * count
        print(f"  {year}: {bar} ({count})")
    
    print("\n🔬 Modalities Mentioned:")
    for mod, count in stats["modalities"].most_common():
        pct = count / stats["total_papers"] * 100
        print(f"  {mod}: {count} papers ({pct:.1f}%)")
    
    print("\n🎯 Tasks:")
    for task, count in stats["tasks"].most_common():
        pct = count / stats["total_papers"] * 100
        print(f"  {task}: {count} papers ({pct:.1f}%)")
    
    print("\n📖 Study Types:")
    for st, count in stats["study_types"].most_common():
        print(f"  {st}: {count} papers")
    
    print("\n💾 Datasets Mentioned:")
    for ds, count in stats["datasets"].most_common(10):
        print(f"  {ds}: {count} papers")
    
    print("\n🤖 ML Methods:")
    for cat, count in stats["ml_categories"].most_common():
        pct = count / stats["total_papers"] * 100
        print(f"  {cat}: {count} papers ({pct:.1f}%)")
    
    print("\n✅ Evaluation Methods:")
    for ev, count in stats["evaluation_methods"].most_common():
        print(f"  {ev}: {count} papers")
    
    print("\n📏 Metrics Reported:")
    for metric, count in stats["metrics_reported"].most_common():
        pct = count / stats["total_papers"] * 100
        print(f"  {metric}: {count} papers ({pct:.1f}%)")
    
    print("\n📌 Key Insights:")
    print(f"  • ECG/HRV-based papers: {stats['ecg_based_papers']} ({stats['ecg_based_papers']/stats['total_papers']*100:.1f}%)")
    print(f"  • Wearable-focused papers: {stats['wearable_papers']} ({stats['wearable_papers']/stats['total_papers']*100:.1f}%)")
    print(f"  • Deep Learning papers: {stats['deep_learning_papers']} ({stats['deep_learning_papers']/stats['total_papers']*100:.1f}%)")
    print(f"  • Traditional ML papers: {stats['traditional_ml_papers']} ({stats['traditional_ml_papers']/stats['total_papers']*100:.1f}%)")


def export_to_csv(papers: list[dict], output_path: Path):
    """Export paper analysis to CSV"""
    fieldnames = [
        "filename", "title", "authors", "year", "word_count",
        "primary_modality", "primary_task", "is_ecg_based", "is_wearable",
        "uses_deep_learning", "uses_traditional_ml",
        "modalities", "tasks", "study_types", "datasets", "ml_methods", "evaluation"
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for paper in papers:
            row = {
                "filename": paper["filename"],
                "title": paper["title"],
                "authors": paper["authors"],
                "year": paper["year"],
                "word_count": paper["word_count"],
                "primary_modality": paper["primary_modality"],
                "primary_task": paper["primary_task"],
                "is_ecg_based": paper["is_ecg_based"],
                "is_wearable": paper["is_wearable"],
                "uses_deep_learning": paper["uses_deep_learning"],
                "uses_traditional_ml": paper["uses_traditional_ml"],
                "modalities": "; ".join(paper["modalities"].keys()),
                "tasks": "; ".join(paper["tasks"].keys()),
                "study_types": "; ".join(paper["study_types"]),
                "datasets": "; ".join(paper["datasets"]),
                "ml_methods": "; ".join(f"{k}: {', '.join(v)}" for k, v in paper["ml_methods"].items()),
                "evaluation": "; ".join(paper["evaluation"]),
            }
            writer.writerow(row)
    
    print(f"\n💾 Exported analysis to: {output_path}")


def main():
    print("🔍 Analyzing papers in Papers_md folder...")
    print(f"   Looking in: {PAPERS_MD_DIR}")
    
    if not PAPERS_MD_DIR.exists():
        print(f"❌ Error: Directory not found: {PAPERS_MD_DIR}")
        return
    
    # Get all markdown files
    md_files = list(PAPERS_MD_DIR.glob("*.md"))
    print(f"   Found {len(md_files)} markdown files")
    
    # Analyze each paper
    papers = []
    for filepath in md_files:
        result = analyze_paper(filepath)
        if result:
            papers.append(result)
    
    print(f"   Successfully analyzed {len(papers)} papers")
    
    # Generate and print statistics
    stats = generate_statistics(papers)
    print_statistics(stats)
    
    # Export to CSV
    output_csv = OUTPUT_DIR / "paper_analysis_results.csv"
    export_to_csv(papers, output_csv)
    
    # Also save detailed JSON
    output_json = OUTPUT_DIR / "paper_analysis_detailed.json"
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump({"papers": papers, "statistics": {
            k: dict(v) if isinstance(v, Counter) else v 
            for k, v in stats.items()
        }}, f, indent=2, default=str)
    print(f"💾 Exported detailed analysis to: {output_json}")
    
    # Print papers that might need manual review (missing key info)
    print("\n⚠️  Papers potentially needing review (no clear modality/task):")
    for paper in papers:
        if not paper["modalities"] or not paper["tasks"]:
            print(f"   - {paper['filename'][:60]}...")


if __name__ == "__main__":
    main()
