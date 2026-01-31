---
marp: true
theme: default
paginate: true
footer: 'Cologne Institute for Information Systems (CIIS) &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; 31.01.2026'
style: |
  @import url('https://fonts.googleapis.com/css2?family=Arial:wght@400;700&display=swap');
  section {
    font-family: Arial, sans-serif;
    font-size: 18pt;
    padding-bottom: 3.5rem;
  }
  h1 {
    font-size: 28pt;
    font-weight: bold;
  }
  h2 {
    font-size: 22pt;
    font-weight: bold;
  }
  h3 {
    font-size: 20pt;
    font-weight: bold;
  }
  table {
    font-size: 16pt;
  }
  .highlight {
    color: #00496A;
  }
  .alert {
    color: #cc0000;
  }
  /* Footer with logo */
  section::before {
    content: "";
    position: absolute;
    bottom: 0.3rem;
    left: 3.5rem;
    width: 6rem;
    height: 2.5rem;
    background-image: url("images/uni-koeln-logo.png");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: left;
    z-index: 1;
  }
  /* Footer text styling */
  footer {
    position: absolute;
    left: 11rem;
    bottom: 1rem;
    font-size: 10pt;
    color: #00496A;
  }
  /* Adjust pagination position to right side */
  section::after {
    position: absolute;
    bottom: 1.7rem;
    right: 2rem;
    font-size: 10pt;
    color: #00496A;
    content: attr(data-marpit-pagination);
    font-weight: bold;
    
  }

---

<!-- _paginate: "" -->
# Deep Learning für Anfallsdetektion mittels tragbarer Sensoren (2013--2026)

## Systematische Literaturübersicht


**Referent:** Paulin Saher
**Veranstaltung:** Bachelor-Seminar
**Datum:** 31.1.2026

---

# Agenda


1. **Forschungsfrage** & Zielsetzung
2. **Hintergrund:** Klinischer Bedarf
3. **Methodik** der Literaturübersicht
4. **Drei Highlight-Studien** im Fokus
5. **Vergleich** der Studien
6. **Kernaussagen** & Fazit

---

# Forschungsfrage

**Hauptfrage:**

Wie erreichen verschiedene Deep-Learning-Architekturen und Biosignal-Modalitäten ein optimales Verhältnis zwischen Sensitivität und Falschalarmrate für die ambulante Anfallsüberwachung?

**Abgrenzung:**
- Kein EEG (nur tragbare Geräte)
- Ziel: Home-Monitoring für Patienten

---

# Hintergrund & Klinischer Kontext

**Problem:**
- Epilepsie betrifft ca. **50 Mio. Menschen** weltweit
- Aktuelle Limitation: EEG ist stationär, ungeeignet für Langzeitmonitoring

**ILAE Phasen-Modell:**
- Phase 1 (Konzept) -> Phase 2 (Klinische Validierung) -> Phase 3 (Home-Validierung)

**Klinischer Benchmark:**
- FPR < 0,05--0,1/h für akzeptable Home-Nutzung

---

# Methodik

**Systematische Literaturübersicht** (PRISMA-Richtlinien)
- Suchzeitraum: 2013--2026
- Webster & Watson Konzeptmatrix
- **13 Studien insgesamt** (9 Detektion, 4 Vorhersage)
- **Auswahlkriterien**: Hohe methodische Qualität, unterschiedliche Phasen, repräsentative Architekturen

**Heutiger Fokus:** Die Drei vielversprechensten Detektionsstudien im Detail

---

# Studie 1: Fine et al. (2025)

## Automated Tonic Seizure Detection

**Design:** Phase 1 Studie
**Gerät:** 6-Achsen-Band (ACC + Gyroskop), Handgelenk
**Algorithmus:** ANN mit 594 handcrafted Features

**Stichprobe:** n = 15, 70 tonische Anfälle

**Ergebnisse:**
- Sensitivität: <span class="highlight">100%</span> (Testset)
- FPR: 0,16/Nacht
- Latenz: 14 s (Median)

**Besonderheit:** Fokus auf tonische Anfälle, hohe Detektionsrate

---

# Studie 2: Spahr et al. (2025)

## Deep Learning Detection using Wrist Accelerometer

**Design:** Multizentrisch, prospektiv (Phase 2)
**Gerät:** Empatica E4 (nur ACC), Handgelenk
**Algorithmus:** Ensemble 1D CNN (30 Modelle, Quantil-Aggregation)

**Stichprobe:** n = 384 (8 Zentren), 49 CSs

**Ergebnisse:**
- Sensitivität: <span class="highlight">96%</span>
- FPR: 1/8 Tage (0,0054/h)
- Anpassbare Empfindlichkeit ohne Retraining

**Besonderheit:** Größte Kohorte, kommerzielle Integration (TicWatch)

---

# Studie 3: Dong et al. (2026)

## Two-Stage Nocturnal Seizure Detection

**Design:** Prospektiv, Langzeit-Home-Monitoring
**Gerät:** NightWatch Armband (ACC + PPG)
**Algorithmus:** Zweistufig (Pre-screening + CNN-LSTM + Attention)

**Stichprobe:** n = 68, 1846 Anfälle, 6304 Stunden

**Ergebnisse:**
- Sensitivität: <span class="highlight">71,6%</span>
- FPR: 0,165/h
- <span class="highlight">81% Reduktion</span> der Rechenlast durch Pre-screening

**Besonderheit:** Frühe HF-Detektion (~100 s vor Bewegung), Real-World-Daten

---

# Vergleichstabelle der 3 Studien

| Studie | Phase | Gerät | Algorithmus | Sens | FPR | Stärke |
|--------|-------|-------|-------------|------|-----|--------|
| Fine 2025 | Phase 1 | 6-Achse Band | ANN | 100% | 0,16/N | Tonische Anfälle |
| Spahr 2025 | Phase 2 | E4 (ACC) | Ensemble CNN | 96% | 1/8 Tage | Multizentrisch |
| Dong 2026 | Home | NightWatch | 2-Stufe CNN-LSTM | 72% | 0,165/h | Early HR detection |

---

# Kernaussagen & Fazit

**Hauptergebnisse:**
- Deep Learning ermöglicht klinisch relevante Detektionsraten
- Trade-off: Sensitivität vs. FPR bleibt zentrale Herausforderung
- Multimodale Sensoren (ACC + PPG) vielversprechend für frühe Detektion
- Ensemble-Ansätze bieten robuste, anpassbare Performance

**Herausforderungen:**
- Generalisierbarkeit über Patienten hinweg
- Real-World FPR oft höher als im Labor
- Energieeffizienz für ambulanten Einsatz

---

# Vielen Dank für Ihre Aufmerksamkeit!

**Noch Fragen oder Anmerkungen?**
