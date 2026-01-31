---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Arial:wght@400;700&display=swap');
  section {
    font-family: Arial, sans-serif;
    font-size: 18pt;
  }
  h1, h2, h3 {
    font-size: 20pt;
    font-weight: bold;
  }
  table {
    font-size: 16pt;
  }
  .highlight {
    color: #0066cc;
  }
  .alert {
    color: #cc0000;
  }
---

<!-- _paginate: "" -->
# Deep Learning fur Anfallsdetektion mittels tragbarer Sensoren (2013-2026)

## Systematische Literaturubersicht

**Referent:** [Name]
**Veranstaltung:** Bachelor-Seminar
**Datum:** [Datum]

---

# Agenda

1. **Forschungsfrage** & Zielsetzung
2. **Hintergrund:** Klinischer Bedarf
3. **Methodik** der Literaturubersicht
4. **Drei Highlight-Studien** im Fokus
5. **Kernaussagen** & Fazit

---

# Forschungsfrage

**Hauptfrage:**

Wie erreichen verschiedene Deep-Learning-Architekturen und Biosignal-Modalitaten ein optimales Verhaltnis zwischen Sensitivitat und Falschalarmrate fur die ambulante Anfallsuberwachung?

**Abgrenzung:**
- Kein EEG (nur tragbare Gerate)
- Ziel: Home-Monitoring fur Patienten

---

# Hintergrund & Klinischer Kontext

**Problem:**
- Epilepsie betrifft ca. **50 Mio. Menschen** weltweit
- Aktuelle Limitation: EEG ist stationar, ungeeignet fur Langzeitmonitoring

**ILAE Phasen-Modell:**
- Phase 1 (Konzept) -> Phase 2 (Klinische Validierung) -> Phase 3 (Home-Validierung)

**Klinischer Benchmark:**
- FPR < 0,05-0,1/h fur akzeptable Home-Nutzung

---

# Methodik

**Systematische Literaturubersicht** (PRISMA-Richtlinien)
- Suchzeitraum: 2013-2026
- Webster & Watson Konzeptmatrix
- **13 Studien insgesamt** (9 Detektion, 4 Vorhersage)

**Heutiger Fokus:** Drei Detektionsstudien im Detail

---


# Vergleichstabelle der 3 Studien

| Studie | Phase | Gerat | Algorithmus | Sens | FPR | Starke |
|--------|-------|-------|-------------|------|-----|--------|
| Fine 2025 | Phase 1 | 6-Achse Band | ANN | 100% | 0,16/N | Tonische Anfalle |
| Spahr 2025 | Phase 2 | E4 (ACC) | Ensemble CNN | 96% | 1/8T | Multizentrisch |
| Dong 2026 | Home | NightWatch | 2-Stufe CNN-LSTM | 72% | 0,165/h | Early HR detection |

---

# Studie 1: Fine et al. (2025)

## Automated Tonic Seizure Detection

**Design:** Phase 1 Studie
**Gerat:** 6-Achsen-Band (ACC + Gyroskop), Handgelenk
**Algorithmus:** ANN mit 594 handcrafted Features

**Stichprobe:** n = 15, 70 tonische Anfalle

**Ergebnisse:**
- Sensitivitat: <span class="highlight">100%</span> (Testset)
- FPR: 0,16/Nacht
- Latenz: 14 s (Median)

**Besonderheit:** Fokus auf tonische Anfalle, hohe Detektionsrate

---

# Studie 2: Spahr et al. (2025)

## Deep Learning Detection using Wrist Accelerometer

**Design:** Multizentrisch, prospektiv (Phase 2)
**Gerat:** Empatica E4 (nur ACC), Handgelenk
**Algorithmus:** Ensemble 1D CNN (30 Modelle, Quantil-Aggregation)

**Stichprobe:** n = 384 (8 Zentren), 49 CSs

**Ergebnisse:**
- Sensitivitat: <span class="highlight">96%</span>
- FPR: 1/8 Tage (0,0054/h)
- Anpassbare Empfindlichkeit ohne Retraining

**Besonderheit:** Grosste Kohorte, kommerzielle Integration (TicWatch)

---

# Studie 3: Dong et al. (2026)

## Two-Stage Nocturnal Seizure Detection

**Design:** Prospektiv, Langzeit-Home-Monitoring
**Gerat:** NightWatch Armband (ACC + PPG)
**Algorithmus:** Zweistufig (Pre-screening + CNN-LSTM + Attention)

**Stichprobe:** n = 68, 1846 Anfalle, 6304 Stunden

**Ergebnisse:**
- Sensitivitat: <span class="highlight">71,6%</span>
- FPR: 0,165/h
- <span class="highlight">81% Reduktion</span> der Rechenlast durch Pre-screening

**Besonderheit:** Frihe HF-Detektion (~100 s vor Bewegung), Real-World-Daten

---

# Kernaussagen & Fazit

**Hauptergebnisse:**
- Deep Learning ermglicht klinisch relevante Detektionsraten
- Trade-off: Sensitivitat vs. FPR bleibt zentrale Herausforderung
- Multimodale Sensoren (ACC + PPG) vielversprechend fur frhe Detektion
- Ensemble-Ansatze bieten robuste, anpassbare Performance

**Herausforderungen:**
- Generalisierbarkeit ber Patienten hinweg
- Real-World FPR oft hher als im Labor
- Energieeffizienz fur ambulanten Einsatz

---

# Vielen Dank fur Ihre Aufmerksamkeit!

**Fragen und Kommentare erwunscht**

<span class="highlight">Bachelor-Seminar 2026</span>
