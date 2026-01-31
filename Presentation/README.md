# Bachelor-Seminar Präsentation

## Ordnerstruktur

```
Presentation/
├── slides.md          # Hauptdatei für Marp-Präsentation
├── images/            # Ordner für Diagramme und Bilder
└── README.md          # Diese Datei
```

## Kompilierung

### Marp CLI installieren (falls nicht vorhanden)

```bash
npm install -g @marp-team/marp-cli
```

### PDF erzeugen

```bash
marp Presentation/slides.md --pdf
```

### PowerPoint erzeugen

```bash
marp Presentation/slides.md --pptx
```

### Live-Vorschau während des Editierens

```bash
marp -s Presentation/slides.md
```

## Präsentationsübersicht

Die Präsentation umfasst **10 Folien** für einen 15-minütigen Vortrag:

1. Titelfolie
2. Agenda
3. Forschungsfrage
4. Hintergrund & Klinischer Kontext
5. Methodik
6. Studie 1: Fine et al. (2025)
7. Studie 2: Spahr et al. (2025)
8. Studie 3: Dong et al. (2026)
9. Vergleichstabelle
10. Kernaussagen & Fazit

## Design-Richtlinien (WIM)

- Max 5 Gedanken pro Slide
- Schriftgröße: min 16pt, Überschriften 20pt
- Arial-Schriftart (keine Serifen)
- Farben: Blau/Schwarz/Grün für Text, Rot nur für Hervorhebungen
- Keine "Danke"-Folie (durch Diskussions-Einladung ersetzt)

## Inhalte

Die drei Highlight-Studien wurden basierend auf den Originalpapieren verifiziert:

- **Fine 2025:** Larsen et al. 2024 - 100% Sensitivität, 0.16 FPR/Nacht
- **Spahr 2025:** Episave - 96% Sensitivität, 1/8 Tage FPR, 384 Patienten
- **Dong 2026:** NightWatch - 71.6% Sensitivität, 0.165/h FPR, frühe HR-Detektion
