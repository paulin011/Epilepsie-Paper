#!/usr/bin/env python3
"""
Simple automated extractor for study metadata from PDFs in Papers/.
Outputs CSV with extracted_n_subjects, n_seizures, sensors, datasets, validation_protocol and confidence + excerpt.
"""
import os
import re
import csv
import fitz

PDF_DIR = '/home/paulin/Documents/Epilepsie/Papers'
OUT_CSV = '/home/paulin/Documents/Epilepsie/Organization/auto_extracted_full.csv'

SENSORS = ['ecg','ppg','photoplethysmograph','photoplethysmography','photopleth','accelerometer','accelerometry','eda','electrodermal','respir','respiration','spo2','oximetry','gyroscope','emg']
DATASETS = ['EPILEPSIAE','CHB-MIT','Siena','PHYSIONET','AES','Epilepsy Ecosystem']
VALIDATION_KEYS = ['pseudo-prospective','pseudo prospective','leave-one-seizure-out','leave one seizure out','leave-one-subject-out','cross-validation','cross validation','rolling','real-time','patient-specific','patient specific']

# regex patterns
RE_N_EQ = re.compile(r'\b[nN]\s*=\s*(\d{1,4})')
RE_N_PAT = re.compile(r'(\d{1,4})\s+(?:patients|subjects|participants|children|adults)', re.I)
RE_N_SEIZ = re.compile(r'(?:seizures|events|episodes)\s*(?:[:=\-]?)\s*(\d{1,4})', re.I)
RE_NUM_SEIZ_2 = re.compile(r'(\d{1,4})\s+(?:seizures|events|episodes)', re.I)


def extract_text(pdf_path):
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        return ''
    parts = []
    for page in doc:
        try:
            parts.append(page.get_text())
        except Exception:
            pass
    return "\n".join(parts)


def find_n_subjects(text):
    m = RE_N_EQ.search(text)
    if m:
        start = max(0, m.start()-120)
        return m.group(1), 'high', text[start:m.end()+120]
    m2 = RE_N_PAT.search(text)
    if m2:
        start = max(0, m2.start()-80)
        return m2.group(1), 'medium', text[start:m2.end()+80]
    return '', 'low', ''


def find_n_seizures(text):
    m = RE_N_SEIZ.search(text)
    if m:
        start = max(0, m.start()-120)
        return m.group(1), 'high', text[start:m.end()+120]
    m2 = RE_NUM_SEIZ_2.search(text)
    if m2:
        start = max(0, m2.start()-80)
        return m2.group(1), 'medium', text[start:m2.end()+80]
    # sometimes authors report "X seizures in Y patients" - try that
    m3 = re.search(r'(\d{1,4})\s+seizures\s+in\s+(\d{1,4})', text, re.I)
    if m3:
        start = max(0, m3.start()-80)
        return m3.group(1), 'medium', text[start:m3.end()+80]
    return '', 'low', ''


def find_sensors(text):
    found = set()
    for s in SENSORS:
        if re.search(r'\b' + re.escape(s) + r'\b', text, re.I):
            found.add(s)
    if found:
        return ",".join(sorted(found)), 'high', ''
    return '', 'low', ''


def find_datasets(text):
    found = set()
    for d in DATASETS:
        if re.search(re.escape(d), text, re.I):
            found.add(d)
    if found:
        return ",".join(sorted(found)), 'high', ''
    # look for generic word "dataset" with a nearby capitalized name
    m = re.search(r'dataset[s]?\s+(?:named|called|from)\s+([A-Z][A-Za-z0-9\-]+)', text)
    if m:
        return m.group(1), 'medium', ''
    return '', 'low', ''


def find_validation(text):
    found = set()
    for k in VALIDATION_KEYS:
        if re.search(re.escape(k), text, re.I):
            found.add(k)
    if found:
        return ",".join(sorted(found)), 'high', ''
    return '', 'low', ''


def main():
    rows = []
    files = sorted([f for f in os.listdir(PDF_DIR) if f.lower().endswith('.pdf')])
    for fname in files:
        path = os.path.join(PDF_DIR, fname)
        print('Processing', fname)
        text = extract_text(path)
        if not text or len(text) < 50:
            print('  -> empty or failed extract')
        n_subj, n_subj_conf, excerpt_subj = find_n_subjects(text)
        n_seiz, n_seiz_conf, excerpt_seiz = find_n_seizures(text)
        sensors, sensors_conf, _ = find_sensors(text)
        datasets, datasets_conf, _ = find_datasets(text)
        val, val_conf, _ = find_validation(text)
        excerpt = (excerpt_subj or excerpt_seiz)[:600]
        rows.append([fname, n_subj, n_subj_conf, n_seiz, n_seiz_conf, sensors, sensors_conf, datasets, datasets_conf, val, val_conf, excerpt])

    hdr = ['filename','extracted_n_subjects','n_subjects_confidence','extracted_n_seizures','n_seizures_confidence','extracted_sensors','sensors_confidence','extracted_datasets','datasets_confidence','extracted_validation_protocol','validation_confidence','excerpt_for_QC']
    with open(OUT_CSV, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(hdr)
        w.writerows(rows)
    print('Wrote', OUT_CSV)


if __name__ == '__main__':
    main()
