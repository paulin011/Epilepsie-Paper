

# **Maschinelles Lernen zur automatisierten Vorwarnung vor epileptischen Anfällen mittels Elektrokardiogramm (EKG): Eine dezennale Literaturübersicht über neurokardiale Dynamik und rechnerische Machbarkeit (2015–2025)**

## **I. Einleitung: Die Notwendigkeit nicht-invasiver Anfallsprognose**

### **1.1. Die Last der Unvorhersehbarkeit und das klinische Gebot**

Epilepsie ist eine chronische neurologische Störung, die durch plötzliche, wiederkehrende und vorübergehende Störungen der Wahrnehmung oder des Verhaltens gekennzeichnet ist, welche aus der übermäßigen Synchronisation kortikaler neuronaler Netzwerke resultieren.1 Die Prävalenz dieser Erkrankung liegt bei etwa 1% der Allgemeinbevölkerung.2 Einer der behinderndsten Aspekte der Störung ist die Unvorhersehbarkeit der Anfälle.1 Diese Ungewissheit führt zu erheblichen neurobiologischen, psychologischen und sozialen Folgen für die Betroffenen (People with Epilepsy, PWE), einschließlich sozialer Stigmatisierung, Angststörungen und einem erhöhten Risiko für anfallsbedingte Verletzungen oder den plötzlichen unerwarteten Tod bei Epilepsie (SUDEP).2  
Trotz verfügbarer medikamentöser Therapien und chirurgischer Behandlungen erreicht bis zu einem Drittel der PWE keine zufriedenstellende Anfallskontrolle.2 Daher besteht ein dringender Bedarf an zuverlässigen Systemen zur Anfallsprognose (Pre-Warning), die das Auftreten eines Ereignisses mehrere Minuten im Voraus vorhersagen können, um proaktive Interventionen zu ermöglichen.2

### **1.2. Das Argument für EKG in tragbaren Systemen**

Die Elektroenzephalographie (EEG) gilt zwar als Goldstandard für die Aufzeichnung der Gehirnaktivität und die rechtzeitige Vorhersage epileptischer Anfälle 3, ist jedoch für das chronische, kontinuierliche Monitoring außerhalb der klinischen Überwachungseinheit (Epilepsy Monitoring Unit, EMU) häufig unpraktikabel. Im Gegensatz dazu bietet die Analyse des Elektrokardiogramms (EKG) und der daraus abgeleiteten Herzfrequenzvariabilität (HRV) eine attraktive, nicht-invasive Alternative.
Das EKG-Signal ist im Vergleich zum EEG-Signal deutlich weniger anfällig für Bewegungsartefakte, die bei körperlicher Aktivität entstehen.4 Dies macht es zu einer ausgezeichneten Wahl für kontinuierliche Überwachungsszenarien, insbesondere im Kontext tragbarer Geräte. Durch die Nutzung von am Körper getragenen Geräten, die mit EKG-Sensoren ausgestattet sind, ergeben sich neue Möglichkeiten für die nahtlose und nicht-invasive Datenerfassung und die Entwicklung zugänglicher Vorwarnsysteme.4 Die jüngsten Fortschritte im Maschinellen Lernen (ML) und Deep Learning (DL) haben die Analyse dieser bioelektrischen Signale revolutioniert und die Entwicklung automatisierter Techniken zur Vorhersage epileptischer Anfälle ermöglicht.6

## **II. Neurokardiale Kopplung: Physiologische Grundlage und HRV-Merkmale**

### **2.1. Die autonome Grundlage präiktaler Veränderungen**

Epilepsie ist eine neurologische Störung, die bekanntermaßen Veränderungen im autonomen Nervensystem (ANS) hervorruft.1 Die Herzfrequenzvariabilität (HRV) reflektiert die Regulierung der Herzaktivität und den Tonus des ANS.1 Sie gilt als einer der genauesten Indikatoren für das sympathovagale Gleichgewicht im ANS.7  
Das Monitoring der HRV ist bei Epilepsiepatienten von wachsendem Interesse, da eine Dysregulation des kardialen ANS mit einer erhöhten Langzeitmorbidität und Mortalität, insbesondere dem Risiko von SUDEP, in Verbindung gebracht wird.7 Die Analyse der HRV kann daher genutzt werden, um diese Pathophysiologie aufzuklären und präventive Maßnahmen zu entwickeln.7

### **2.2. Das prädiktive Signal: Eigenschaften der präiktalen HRV-Dynamik**

Die Forschung der letzten zehn Jahre hat gezeigt, dass Veränderungen im EKG und den daraus abgeleiteten HRV-Parametern den eigentlichen Anfall um mehrere Minuten vorangehen können.2 Dies wird als genuine präiktale HRV-Dynamik interpretiert.2 Eine frühe Studie demonstrierte bereits, dass ein methodischer Ansatz, der Eigendekomposition von HRV-Parameter-Kovarianzmatrizen nutzt, in Verbindung mit einem Support Vector Machine (SVM)-Klassifikator, drohende Anfälle ab 5 Minuten vor dem klinischen Beginn mit einer Sensitivität von 94,1% erkennen konnte.1  
Die beobachteten Parallelen zur EEG-basierten Anfallsprognose legen einen breiteren neurokardialen Informationsfluss nahe.2 Die Dynamik der HRV-Parameter signalisiert physiologische Verschiebungen im ANS – insbesondere in der sympathischen und parasympathischen Aktivität – die in der präiktalen Phase häufig auftreten.8  
Ein zentrales, wiederkehrendes Ergebnis in der Literatur ist jedoch, dass die tatsächliche Dauer der präiktalen Phase hochgradig variabel zwischen den einzelnen Anfällen ist.2 Während frühere HRV-Studien oft eine feste präiktale Dauer von 10 Minuten verwendeten, zeigen neuere Untersuchungen, dass die Mehrheit der präiktalen Veränderungen bis zu 40 Minuten vor den Anfällen identifiziert werden können und eine hohe intra-individuelle Variabilität in ihrer Dauer aufweisen.2 Die Konsequenz dieser Erkenntnis ist fundamental: Die hohe Variabilität stellt verallgemeinbare ML-Modelle, die auf festen Fenstern trainiert wurden, vor große Herausforderungen, wodurch die Notwendigkeit adaptiver, personalisierter Modellierungsstrategien, möglicherweise unter Verwendung unüberwachter Lernmethoden, unterstrichen wird, um den tatsächlichen Beginn der autonomen Verschiebung präzise zu erfassen.

### **2.3. Merkmalsextraktion: Die Domänen der HRV-Analyse**

Die ML-basierten Ansätze zur EKG-Anfallsprognose stützen sich auf die Extraktion von HRV-Merkmalen aus verschiedenen Domänen: Zeit, Frequenz und Nichtlinearität.8

#### **2.3.1. Zeit- und Frequenzdomäne**

Konventionelle zeit- und frequenzbasierte HRV-Maße erfassen grundlegende sympathische und parasympathische Verschiebungen. Derartige Merkmale, beispielsweise die mittlere RR-Intervall-Dauer oder die Leistung im Niederfrequenz- (LF) und Hochfrequenz- (HF) Band, werden zur Analyse des sympathovagalen Gleichgewichts verwendet.9 Die kontinuierliche Morlet-Wavelet-Transformation wird beispielsweise eingesetzt, um die Zeit-Frequenz-Eigenschaften der HRV zu untersuchen, wobei die Koordination beider HRV-Komponenten (blutdruckbezogene Mayer-Wellen bei $\\approx 0.1 \\text{ Hz}$ und respiratorische Sinusarrhythmie bei $\\approx 0.3 \\text{ Hz}$) etwa 80 bis 100 Sekunden vor Anfallsbeginn beobachtet werden kann.9

#### **2.3.2. Nichtlineare Dynamik und Komplexitätsreduktion**

Die alleinige Verwendung linearer (Zeit- und Frequenz-) Metriken reicht oft nicht aus, um die subtilen kardialen autonomen Variationen und die zugrunde liegende systemische Dynamik zu erfassen.10 Aus diesem Grund ist die Einbeziehung nichtlinearer Analysemethoden, wie die Detrended Fluctuation Analysis (DFA) oder die Korrelationsdimension, entscheidend, um Komplexitätsmaße zu charakterisieren.8  
Der **Maximum Lyapunov Exponent (LLE)** ist ein besonders wichtiges nichtlineares Merkmal, das in der Kontrolltheorie die Vorhersagbarkeit eines dynamischen Systems kennzeichnet.10 Eine Reduktion des LLE – ursprünglich an iEEG-Signalen beobachtet – signalisiert eine Phasenverschiebung von chaotischer zu geordneter Gehirnaktivität, was einen kritischen vorbotenhaften Informationsgehalt darstellt.11 Dieses Konzept der Komplexitätsreduktion findet sich auch in der HRV-Analyse wieder. Es wird beobachtet, dass eine höhere Synchronisation und damit eine höhere Vorhersagbarkeit der HRV in der präiktalen Phase auftritt.9 Der Rückgang der Komplexität hin zu einem geordneteren Zustand vor dem Anfall ist ein physiologisch fundierter, nichtlinearer Biomarker, der für effektive Vorhersagemodelle unverzichtbar ist.10  
Die Notwendigkeit, nichtlineare Dynamiken zu berücksichtigen, wird dadurch begründet, dass nur diese Maße die spezifischen, präiktalen ANS-Verschiebungen vollständig ausnutzen können.  
Tabelle 1 fasst die Rolle der verschiedenen Merkmalsdomänen für die ML-Analyse zusammen.  
Tabelle 1: Vergleich der Merkmalsextraktionsdomänen für die EKG/HRV-Anfallsprognose

| Merkmalsdomäne | Beispielmerkmale | Physiologische Interpretation | Relevanz für ML-Modelle | Quelle(n) |
| :---- | :---- | :---- | :---- | :---- |
| Zeitdomäne (Linear) | Mittleres RR-Intervall, SDNN, pNN50 | Gesamte Variabilität, Interaktion von Sympathikus/Parasympathikus. | Eingabe für traditionelles ML (SVM, RF) und Baselines. | 8 |
| Frequenzdomäne (Linear) | VLF, LF, HF Leistung, LF/HF-Verhältnis | Reflektiert sympathovagales Gleichgewicht, zeigt Modulation kurz vor dem Anfall. | Klassisches Maß für den ANS-Tonus. | 8 |
| Nichtlineare Dynamik | Max Lyapunov Exponent (LLE), Korrelationsdimension, DFA | Misst Komplexität und Verschiebung von chaotisch zu geordnet, was auf eine höhere Vorhersagbarkeit hindeutet. | Entscheidend für die Erfassung spezifischer präiktaler ANS-Dynamiken. | 9 |

## **III. Datenressourcen, Vorverarbeitung und Validierungsstrategien**

### **3.1. Wichtige EKG-inklusive öffentliche Datensätze (2015–2025)**

Für die Entwicklung und Evaluation robuster ML-Modelle sind große, standardisierte Datensätze unerlässlich. Das Forschungsfeld der EKG-basierten Anfallsprognose kämpft jedoch mit einer fragmentierten Datenlandschaft, da die meisten großen, öffentlichen Korpora primär auf EEG ausgerichtet sind.14  
Dennoch enthalten einige wichtige Datensätze EKG-Signale, die für die Anfallsprognose genutzt werden:

* **EPILEPSIAE-Datenbank:** Diese umfangreiche europäische Datenbank umfasst Langzeit-EEG-, EKG- und EMG-Daten von 275 Patienten mit fokaler Epilepsie, die insgesamt 2662 Anfälle dokumentieren.15 Die Datenbank wird häufig zur Schulung von HRV-basierten Anfallsprognosemodellen herangezogen (z. B. Random Forest).16 Erste Studien, die Daten aus 1275 Anfällen von 167 Patienten analysierten, konnten konsistente Muster im Anstieg oder Abfall von Merkmalen wie dem mittleren RR-Intervall feststellen, obwohl der Effekt anderer Variablen (Anfallsart, Wachzustand) nicht immer eindeutig war.13  
* **CHB-MIT Scalp EEG Database:** Dieser weit verbreitete Datensatz ist zwar auf EEG fokussiert, enthält jedoch in einigen Aufzeichnungen, wie den letzten 36 Dateien von Fall chb04, auch EKG-Signale.17 Die begrenzte Verfügbarkeit dedizierter EKG-Daten in diesem Korpus führt jedoch zu einer Tendenz, primär EEG-Methodologien zu untersuchen.14  
* **Siena Scalp EEG:** Dieser Datensatz ist für die Forschung zur EKG-Anfallsprognose besonders geeignet, da er kontinuierliche Aufzeichnungen enthält, die präiktale, iktale und interiktale Ereignisse erfassen, und zusätzlich EKG-Signale sowie Informationen über Anfallsart und Anfallsursprung bereitstellt.17 Aktuelle ML-Studien, die diesen Datensatz verwendeten, erzielten beeindruckend niedrige Fehlalarmraten.19

### **3.2. Signalintegrität und Artefaktminderung**

Die kontinuierliche EKG-Überwachung außerhalb klinischer Einrichtungen ist anfällig für Signalverschlechterung und Artefakte. Die Vorverarbeitung ist entscheidend und umfasst die Entfernung von Artefakten (z. B. Muskelbewegungen, Netzeinstreuungen) sowie die genaue Erkennung von R-Zacken.  
Ein ernstes Problem für die praktische Anwendung ist die sogenannte „Defizitzeit“ (deficiency time).20 Bei tonisch-klonischen Bewegungen während eines Anfalls können muskelgenerierte Signale die relativ niedrigamplitudigen Herzsignale überdecken. In diesen kritischen Phasen wird das EKG nicht mehr genau aufgezeichnet, was zu einem Verlust der Signalqualität und somit zu einer Unterbrechung der Überwachung führt.20 Diese Einschränkung muss durch robuste, multimodale Ansätze oder durch Algorithmen, die diese Ausfälle erkennen und kompensieren, adressiert werden.

### **3.3. Validierungsprotokolle und der klinische Maßstab**

Zur Beschreibung der Leistung von ML-Werkzeugen werden traditionelle Metriken wie Sensitivität, Spezifität und die Fläche unter der ROC-Kurve (AUC) verwendet.20 Im Kontext der Anfallsprognose sind jedoch spezifische, realitätsnahe Metriken unerlässlich.  
Die **Sensitivität** (Anteil der korrekt vorhergesagten Anfälle an der Gesamtzahl) ist wichtig, aber die **Falsche-Vorhersage-Rate pro Stunde ($\\text{FPR/h}$)** ist der entscheidende klinische Maßstab.21 Die $\\text{FPR/h}$ quantifiziert die Häufigkeit unnötiger Alarme, da eine hohe Fehlalarmrate schnell zu Alarmmüdigkeit beim Patienten und Pflegepersonal führt. Ein typischer klinisch brauchbarer Wert liegt im Bereich von $0.01\\text{ h}^{-1}$.19 Obwohl frühe Studien $\\text{FPR}$-Raten von $0.49\\text{ h}^{-1}$ in Patientenaufzeichnungen meldeten 1, konnten jüngere Ansätze durch optimierte DL-Modelle eine $\\text{FPR}$ von bis zu $0.01\\text{ h}^{-1}$ erreichen, was die Machbarkeit unterstreicht, auch wenn die Genauigkeit dabei bei $76.05\\%$ lag.19  
Die Art der Validierung beeinflusst die gemeldete Leistung signifikant. Die Verwendung nicht-kausaler Studiendesigns, bei denen die zeitliche Abfolge der Daten ignoriert wird, führt oft zu einer Überbewertung der Algorithmusleistung.2 Aufgrund der inhärenten Nicht-Stationarität der präiktalen Dynamik 2 ignoriert eine nicht-kausale Validierung die Herausforderung, tatsächliche Signalverschiebungen in zukünftigen, ungesehenen Daten vorherzusagen. Die daraus resultierenden Sensitivitäts- und Genauigkeitswerte sind klinisch nicht interpretierbar, da sie die Realität einer Echtzeit-Bereitstellung nicht simulieren.  
Daher ist die **pseudo-prospektive Evaluierung** der Goldstandard. Dabei werden chronologisch zurückgehaltene Datensätze verwendet, um den Einsatz in Echtzeit zu simulieren.5 Studien, die diesen Ansatz verfolgten, konnten zeigen, dass tragbare Geräte patientenspezifische Anfallsvorhersagen liefern können, insbesondere wenn zirkadiane und mehrtägige Herzfrequenzzyklen als Biomarker genutzt werden.5  
Ein weiteres Problem ist der Mangel an großen, offenen EKG-spezifischen Datensätzen, die für das Benchmarking von Deep-Learning-Architekturen geeignet sind.14 Die Notwendigkeit, auf kleinere, proprietäre Datensätze zurückzugreifen (z. B. 12 Patienten, 34 Anfälle in einer frühen Studie 1), schränkt die Generalisierbarkeit und Robustheit der entwickelten ML-Modelle stark ein.14

## **IV. Architekturen des Maschinellen Lernens (2015–2025)**

Die ML-Ansätze zur EKG-basierten Anfallsprognose haben sich von klassischen Merkmals-Engineering-Methoden hin zu komplexen Deep-Learning-Architekturen entwickelt, die Merkmale automatisch aus Rohdaten ableiten.22

### **4.1. Konventionelles ML und Feature Engineering**

In der früheren Phase (2015–2018) dominierten Modelle wie Support Vector Machines (SVM) und Random Forests. Diese stützten sich auf manuell extrahierte HRV-Merkmale. Wie in Abschnitt 2.2 dargelegt, konnte ein früher methodischer Ansatz unter Verwendung einer SVM bereits eine Sensitivität von $94.1\\%$ erreichen.1 Der Erfolg dieser Methoden war direkt an die Qualität der vorab berechneten Merkmale, insbesondere der nicht-linearen Maße, gekoppelt. Beispielsweise wurde ein Random Forest-Klassifikator erfolgreich zur Verarbeitung von HRV- und Lorenz-Merkmalen aus der EPILEPSIAE-Datenbank eingesetzt.16

### **4.2. Deep Learning (DL) Architekturen**

Deep Learning ermöglicht die Verarbeitung des EKG-Signals in Rohform oder mit minimaler Vorverarbeitung, wodurch die Notwendigkeit des zeitaufwändigen, manuellen Feature Engineering entfällt.

#### **4.2.1. Convolutional Neural Networks (CNNs)**

CNNs haben sich als vielversprechend für die Erfassung von impliziten Mustern in zeitlichen Sequenzen erwiesen.22 Sie werden eingesetzt, um Merkmale direkt aus den EKG-Signalen zu extrahieren. Ein 39-schichtiges CNN, das für die Anfallsvorhersage trainiert wurde, konnte eine Vorhersagegenauigkeit von $94.29\\%$ erreichen. Solche DL-Ansätze demonstrieren das Potenzial des EKG-Signals für den Aufbau tragbarer Überwachungssysteme.23 Auch komplexere CNN-Architekturen wie ResNet50 mit Transfer Learning wurden vorgeschlagen, um Anfälle aus (primär iEEG-Daten, aber mit dem Potenzial für EKG-Fusion) mit Genauigkeiten von bis zu $95.5\\%$ zu klassifizieren.24

#### **4.2.2. Recurrent Neural Networks (RNNs) und LSTMs**

Da EKG- und HRV-Signale Zeitreihendaten sind, sind rekurrente Architekturen wie Long Short-Term Memory (LSTM) Modelle ideal, um sequenzielle Abhängigkeiten zu modellieren. LSTMs sind in der Lage, die zeitliche Dynamik des Herzrhythmus über lange präiktale Perioden hinweg zu erfassen.

### **4.3. Überlegenheit von Hybrid- und Optimierten Modellen**

Die leistungsstärksten ML-Ansätze im aktuellen Forschungsstand kombinieren Architekturen, um sowohl räumliche (CNN-erfasste) als auch zeitliche (LSTM-erfasste) Muster zu nutzen.  
**CNN-LSTM-Hybride** haben eine signifikant bessere Leistung gezeigt als ihre einzelnen Komponenten oder traditionelle ML-Methoden. Eine Studie, die ein 1D CNN-LSTM-Modell validierte, zeigte im Vergleich zu k-Nearest Neighbors (k-NN), SVM und Decision Trees eine Steigerung der Genauigkeit von bis zu $7.09\\%$. Im Vergleich zu einem reinen Standard-CNN konnte das Hybridmodell eine Genauigkeitsverbesserung von $2.26\\%$ erzielen.25 Darüber hinaus bieten diese Hybridmodelle Vorteile bei der Reduzierung von Fehlalarmen. Bei einem Vergleich verschiedener Modelle erreichte ein CNN-LSTM-Hybrid die niedrigste Falsche-Positive-Rate ($\\text{FPR}$) von $6.8\\%$, verglichen mit $8.2\\%$ für ein reines CNN und $9.5\\%$ für ein reines LSTM.26

### **4.4. Neue Trends: Transformer-Modelle und Interpretierbarkeit**

Aktuelle Forschungstrends erweitern den Einsatz von DL über CNNs und LSTMs hinaus. Dazu gehören selbstüberwachtes Lernen, Graph Neural Networks (GNNs) und insbesondere Transformer-basierte Modelle.14 Transformer-Netzwerke nutzen breite Aufmerksamkeitsmechanismen, um komplexe, weitreichende Abhängigkeiten in den bioelektrischen Zeitreihen zu erfassen.26 Dies ist besonders relevant für die EKG-Analyse, um der Herausforderung der Nicht-Stationarität der physiologischen Signale besser begegnen zu können.  
Parallel dazu gewinnt die **Interpretierbarkeit** von DL-Modellen an Bedeutung.22 Um die klinische Akzeptanz zu fördern, müssen Forscher nicht nur die Leistung, sondern auch die physiologische Begründung hinter den Vorhersagen liefern können. Ansätze wie die Verwendung von temporalen Logik-Neuronalen Netzen oder personalisierten Anfallssignaturen sollen die Erklärbarkeit verbessern.27

## **V. Vergleichende Leistungsbewertung und Benchmarking**

Die Evaluierung der ML-Modelle zur Anfallsprognose erfordert eine kritische Analyse der erzielten Leistungskennzahlen, insbesondere im Hinblick auf die klinische Umsetzbarkeit.

### **5.1. Analyse der Leistungskennzahlen**

Die Ergebnisse der Anfallsprognosemodelle variieren stark, abhängig vom gewählten Vorhersagehorizont (Seizure Prediction Horizon, SPH), der Validierungsstrategie und der Patientenkohorte. Die nachfolgende Tabelle 2 präsentiert eine Auswahl von Leistungs-Benchmarks für EKG-basierte ML-Ansätze aus dem relevanten Zeitraum.  
Tabelle 2: Benchmark von Machine Learning Modellen für die EKG-basierte Anfallsprognose (Illustrative Beispiele 2015–2025)

| Forschungsfokus (Jahr) | Signal/Merkmalstyp | Modellarchitektur | Verwendeter Datensatz | Schlüsselmetrik (FPR/h) | Sensitivität (oder ACC) | Quelle(n) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Frühe ML-Machbarkeit (2017) | HRV-Parameter | SVM (Eigendekomposition) | 12 Patienten, 34 Anfälle (Klinische Daten) | $0.49\\text{ h}^{-1}$ (Patient) | $94.1\\%$ (Sensitivität) | 1 |
| Deep Learning (2024) | EKG-Signale (roh) | 39-Schicht-CNN | Proprietär/unbestimmt | N/A (Fokus auf ACC) | $94.29\\%$ (Vorhersage-ACC) | 23 |
| Advanced DL (2025) | HRV-Merkmale | Unbestimmt DL/ML | Siena-Datenbank | $0.01\\text{ h}^{-1}$ | $76.05\\%$ (Genauigkeit) | 19 |
| Hybrid-Vergleich (Jüngst) | Zeitreihen (generisch) | Hybrid CNN-LSTM | N/A (Vergleichende Analyse) | $6.8\\%$ (niedrigste $\\text{FPR}$ im Vergleich) | N/A ($\\text{FPR}$-Fokus) | 26 |

Ein kritischer Befund ist der inhärente Zielkonflikt zwischen Sensitivität und der Falsche-Vorhersage-Rate. Modelle, die hohe Genauigkeitswerte (z. B. über $94\\%$) melden, verwenden oft enge, binäre Klassifikationsaufgaben (Anfall vs. Nicht-Anfall) oder stützen sich stark auf retrospektive Daten.23 Im Gegensatz dazu zeigen pseudo-prospektive Studien, die für die klinische Übertragung relevanter sind, realistischere Leistungswerte. Beispielsweise konnte bei einer sehr niedrigen $\\text{FPR}$ von $0.01\\text{ h}^{-1}$ die Genauigkeit des Modells auf $76.05\\%$ fallen.19 Das Erreichen einer klinisch akzeptablen $\\text{FPR}$ bei gleichzeitig hoher Sensitivität bleibt die zentrale technische Herausforderung.

### **5.2. Die Lücke zur klinischen Übertragung**

Die Forschung zeigt, dass die **Ergebnisse auf Gruppenebene die klinische Anwendung noch nicht unterstützen**.2 Dies liegt an der Notwendigkeit einer strengen Individualisierung. Die physiologischen Parameter, einschließlich der präiktalen Dauer und der HRV-Dynamik, variieren stark von Patient zu Patient und sogar von Anfall zu Anfall beim selben Patienten.2 Die Übertragung der Ergebnisse auf die klinische Praxis erfordert daher eine Abkehr von verallgemeinerten Modellen hin zu patientenspezifischen, adaptiven Trainingsprotokollen.  
Die Validierung und Bereitstellung ist momentan stark fragmentiert.14 Es fehlt an einheitlichen Evaluierungsprotokollen, standardisierten Wartehorizonten und klaren klinischen Metriken. Diese Fragmentierung behindert die Vergleichbarkeit von Forschungsergebnissen und erschwert die Erreichung der erforderlichen Sicherheits- und Zuverlässigkeitsstandards für eine klinische Implementierung in der realen Welt.

## **VI. Synthese: Einschränkungen, Forschungslücken und zukünftige Richtungen**

### **6.1. Die Herausforderung der Nicht-Stationarität und Individualisierung**

Die größte Hürde für die zuverlässige EKG-basierte Anfallsprognose ist die Nicht-Stationarität und die erhebliche Variabilität der präiktalen Dynamik.2 Die prädiktiven Veränderungen sind hochgradig individualisiert und können in der Dauer stark schwanken – von wenigen Minuten bis zu 40 Minuten vor Anfallsbeginn.2  
Die Verwendung einer festen präiktalen Dauer (z. B. 10 Minuten), wie sie in älteren Studien üblich war, erfasst die tatsächlichen biologischen Dynamiken nicht adäquat. Dies führt dazu, dass Studien, die starre Fenster verwenden, oft kritische, frühe ANS-Verschiebungen verpassen.2  
**Forschungslücke 1: Adaptive und evolutionäre Modelle.** Zukünftige Forschung muss sich auf die Entwicklung personalisierter Algorithmen konzentrieren. Dies schließt unüberwachtes Lernen oder evolutionäre Algorithmen ein, die in der Lage sind, das optimale präiktale Fenster dynamisch für jeden einzelnen Patienten zu identifizieren und sich an Verschiebungen im physiologischen Normalzustand anzupassen.2

### **6.2. Datenbeschränkungen und Benchmarking-Fragmentierung**

Die Verfügbarkeit von qualitativ hochwertigen, EKG-spezifischen Langzeitdatensätzen ist begrenzt. Viele Forscher verwenden primär EEG-fokussierte Korpora, in denen EKG-Daten nur marginal oder für eine Teilmenge der Patienten enthalten sind (z. B. CHB-MIT).14 Dies führt zu einer inkonsistenten Datenbasis und erschwert die direkte Vergleichbarkeit der Modelle.  
**Forschungslücke 2: Standardisierte EKG-Benchmarks und Modellvielfalt.** Es besteht ein dringender Bedarf an der Schaffung **vereinheitlichter Benchmarking-Strategien**. Diese Strategien sollten es ermöglichen, die Leistung unterschiedlicher DL-Architekturen – CNNs, Transformer und GNNs – anhand klinisch relevanter Metriken und dynamischer Risikoschwellen objektiv zu vergleichen.14 Derzeit fehlt es an der notwendigen Modellvielfalt; die meisten Studien konzentrieren sich auf CNNs, während neuere Architekturen wie Transformer oder GNNs seltener untersucht werden.14 Die Bereitstellung von ML-bereiten Benchmarks mit variablen Vorhersage- und Auftretenshorizonten (SPH/SOP) ist entscheidend, um Rechengruppen weltweit zu befähigen, ihre Modelle unter standardisierten Bedingungen zu validieren.29

### **6.3. Multimodalität und Sensorfusion: Der Weg zur Robustheit**

Die Einschränkungen der EKG-Einzelmodalität, insbesondere die Anfälligkeit für Artefakte und die „Defizitzeit“ während konvulsiver Anfälle 20, erfordern einen Übergang zur multimodalen Datenfusion.  
Die physiologische Kopplung von Hirn- und Herzaktivität während des präiktalen Zustands legt nahe, dass eine Kombination der Modalitäten die Robustheit signifikant erhöhen kann. Multimodale Algorithmen, die beispielsweise EKG, EEG und elektrodermale Aktivität integrieren, übertreffen EEG-basierte Algorithmen deutlich.30 Studien zeigten, dass die Sensitivität durch die Fusion um $8\\%$ bis $11\\%$ erhöht werden konnte, bei gleicher Fehlalarmrate.30  
Dieser Synergieeffekt ist für die Minimierung der $\\text{FPR/h}$ von entscheidender Bedeutung. Durch die Integration verschiedener physiologischer Signale kann die Zuverlässigkeit einer Vorhersage maximiert und gleichzeitig die Wahrscheinlichkeit reduziert werden, dass Artefakte in einer einzelnen Modalität zu einem Fehlalarm führen.24 Zukünftige Arbeiten sollten sich auf fortgeschrittene Fusionsstrategien konzentrieren, wie kohärenz- und korrelationsbasierte Ansätze, um EKG- und EEG-Signale effektiv zu verknüpfen und das volle Potenzial der multimodalen Datenanalyse auszuschöpfen.31

### **6.4. Klinische Machbarkeit und regulatorische Herausforderungen**

Nicht-invasive tragbare Sensoren haben ihre Machbarkeit bei der Vorhersage des Anfallsrisikos im pseudo-prospektiven Setting unter Beweis gestellt. Die Einbeziehung zirkadianer und mehrtägiger Herzfrequenzzyklen liefert dabei einen signifikanten prädiktiven Mehrwert.5 Für die Anwendung im Alltag müssen diese Prototypen kontinuierlich betriebsbereit sein und sich durch Patienten-Updates verfeinern lassen, um sich an Verschiebungen im Normalzustand anzupassen.28  
**Forschungslücke 3: Regulatorische und Interpretierbarkeitshürden.** Trotz technischer Fortschritte bestehen erhebliche Hürden bei der klinischen Bereitstellung. Regulatorische Herausforderungen und ethische Bedenken (Datenschutz, Sicherheit) verzögern die Markteinführung automatisierter Anfallsprognosesysteme.33 Die Technologie erfordert einen einheitlichen Rahmen für die regulierungskonforme klinische Übertragung, der die Kluft zwischen akademischer Innovation und realer Anwendung überbrückt.34  
Schließlich müssen die Forscher die Zieldefinition des Systems überdenken. Da die Vorhersage des genauen Zeitpunkts eines einzelnen Anfalls mit sehr niedriger $\\text{FPR/h}$ technisch anspruchsvoll bleibt 2, könnte ein klinisch transformierender Schritt darin bestehen, sich auf die zuverlässige Erkennung von **Änderungen in der Anfallsfrequenz** zu konzentrieren, anstatt nur einzelne Anfälle in Echtzeit zu erkennen.35 Die Nutzung der in den Langzeitdaten erfassten zirkadianen und multitägigen Zyklen zur Risikoeinschätzung 5 stellt ein möglicherweise leichter erreichbares technisches Ziel mit großem klinischen Nutzen dar.35  
Tabelle 3 fasst die kritischen Herausforderungen für die klinische Übertragung zusammen.  
Tabelle 3: Kritische Herausforderungen bei der klinischen Übertragung der EKG-basierten Prognose

| Herausforderungskategorie | Beschreibung und Hauptproblem | Auswirkungen auf die Modellleistung und den klinischen Nutzen | Quelle(n) |
| :---- | :---- | :---- | :---- |
| Präiktale Variabilität | Nicht-Stationarität und hochgradig individualisierte/variable präiktale Dauer (bis zu 40 Minuten). | Modelle mit festem Vorhersagehorizont versagen; erfordert personalisierte, adaptive Methoden. | 2 |
| Datenqualität/Artefakte | Hohe Artefaktbelastung durch Bewegung und Muskelkontraktionen ("Defizitzeit"). | Verringerte Sensitivität und Präzision; Datenverlust während kritischer Phasen, besonders bei tragbaren Geräten. | 20 |
| Klinische Validierung | Unzureichend niedrige $\\text{FPR/h}$ und Abhängigkeit von Gruppenergebnissen anstelle individueller Risikobewertung. | Führt zu Alarmmüdigkeit; aktuelle Gruppenergebnisse unterstützen die klinische Anwendung nicht. | 2 |
| Regulatorische Hürden | Mangel an standardisierten Validierungs-Benchmarks und regulatorischen Rahmenwerken für medizinische KI-Geräte. | Hindernis für die Überführung von Forschungsinnovationen in die reale Patientenversorgung. | 33 |

## **VII. Schlussfolgerung und Zukünftige Forschungsprioritäten**

Die Literaturübersicht der letzten zehn Jahre bestätigt die Existenz eines robusten neurokardialen Zusammenhangs, der eine tragfähige, nicht-invasive Grundlage für die automatisierte Anfallsprognose mittels EKG bietet. Die Analyse der Herzfrequenzvariabilität, insbesondere durch die Einbeziehung nichtlinearer Merkmale wie dem Maximum Lyapunov Exponent, liefert kritische Informationen über die präiktale Komplexitätsreduktion des autonomen Systems.  
Auf rechnerischer Ebene haben Deep-Learning-Methoden, insbesondere hybride Architekturen wie CNN-LSTM, deutliche Leistungsvorteile gegenüber traditionellen ML-Ansätzen gezeigt, insbesondere bei der Reduzierung der Fehlalarmrate. Jüngste Studien demonstrieren, dass klinisch vielversprechende $\\text{FPR}$-Werte von bis zu $0.01\\text{ h}^{-1}$ erreichbar sind.  
Dennoch verhindern die erhebliche intra-individuelle Variabilität der präiktalen Dynamik und die Nicht-Stationarität des Signals eine breite klinische Anwendung auf Gruppenebene. Die größten Forschungslücken konzentrieren sich auf die Notwendigkeit adaptiver, patientenspezifischer Modelle und die Etablierung standardisierter, pseudo-prospektiver Validierungsprotokolle.

### **Priorisierte Forschungsagenda**

Um die Anfallsprognose mittels EKG von der akademischen Forschung in die klinische Realität zu überführen, sind folgende Bereiche als prioritär zu behandeln:

1. **Personalisierung und Adaptation:** Entwicklung von evolutionären Algorithmen, die die physiologische Basislinie des Patienten dynamisch verfolgen und den optimalen präiktalen Vorhersagehorizont (SPH) individuell bestimmen.2  
2. **Multimodale Integration:** Konsequente Nutzung robuster Sensorfusionsstrategien (ECG, EEG, etc.), um die Robustheit der Vorhersage zu maximieren und die $\\text{FPR/h}$ auf ein klinisch akzeptables Niveau zu senken, wodurch die Anfälligkeit für Einzelmoden-Artefakte kompensiert wird.30  
3. **Standardisierung und Benchmarking:** Schaffung eines Konsenses über die Definition klinisch relevanter Metriken und die Erstellung großer, offener, EKG-spezifischer Benchmarks, um die Entwicklung und den objektiven Vergleich von DL-Architekturen (einschließlich Transformer-Modellen) zu fördern.14  
4. **Klinische Ausrichtung:** Fokussierung auf die Entwicklung interpretierbarer ML-Modelle zur Förderung der klinischen Akzeptanz und die Zusammenarbeit mit Regulierungsorganisationen, um Rahmenwerke für die regulierungskonforme Bereitstellung dieser fortschrittlichen tragbaren Warnsysteme zu schaffen.22

#### **Referenzen**

1. Early Seizure Detection Based on Cardiac Autonomic Regulation Dynamics \- Frontiers, Zugriff am November 20, 2025, [https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2017.00765/full](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2017.00765/full)  
2. ECG‐based epileptic seizure prediction: Challenges of current data‐driven models \- PMC, Zugriff am November 20, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11803288/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11803288/)  
3. Accuracy of Machine Learning in Detecting Pediatric Epileptic Seizures: Systematic Review and Meta-Analysis, Zugriff am November 20, 2025, [https://www.jmir.org/2024/1/e55986/](https://www.jmir.org/2024/1/e55986/)  
4. Advances in Machine Learning for Epileptic Seizure Prediction: A Review of ECG-Based Approaches \- Preprints.org, Zugriff am November 20, 2025, [https://www.preprints.org/manuscript/202504.0942/v1](https://www.preprints.org/manuscript/202504.0942/v1)  
5. Forecasting Seizure Likelihood With Wearable Technology \- Frontiers, Zugriff am November 20, 2025, [https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.704060/full](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.704060/full)  
6. Artificial Intelligence-Based Epileptic Seizure Prediction Strategies: A Review \- MDPI, Zugriff am November 20, 2025, [https://www.mdpi.com/2673-2688/6/10/274](https://www.mdpi.com/2673-2688/6/10/274)  
7. Exploring Autonomic Alterations during Seizures in Temporal Lobe Epilepsy: Insights from a Heart-Rate Variability Analysis \- MDPI, Zugriff am November 20, 2025, [https://www.mdpi.com/2077-0383/12/13/4284](https://www.mdpi.com/2077-0383/12/13/4284)  
8. Unsupervised Clustering of HRV Features Reveals Preictal Changes in Human Epilepsy, Zugriff am November 20, 2025, [https://www.researchgate.net/publication/343942952\_Unsupervised\_Clustering\_of\_HRV\_Features\_Reveals\_Preictal\_Changes\_in\_Human\_Epilepsy](https://www.researchgate.net/publication/343942952_Unsupervised_Clustering_of_HRV_Features_Reveals_Preictal_Changes_in_Human_Epilepsy)  
9. Time-variant, frequency-selective, linear and nonlinear analysis of heart rate variability in children with temporal lobe epilepsy \- PubMed, Zugriff am November 20, 2025, [https://pubmed.ncbi.nlm.nih.gov/24845290/](https://pubmed.ncbi.nlm.nih.gov/24845290/)  
10. Heart Rate Variability as a Tool for Seizure Prediction: A Scoping Review \- PMC, Zugriff am November 20, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10856437/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10856437/)  
11. Phase space topography and the Lyapunov exponent of electrocorticograms in partial seizures \- ResearchGate, Zugriff am November 20, 2025, [https://www.researchgate.net/publication/21038851\_Phase\_space\_topography\_and\_the\_Lyapunov\_exponent\_of\_electrocorticograms\_in\_partial\_seizures](https://www.researchgate.net/publication/21038851_Phase_space_topography_and_the_Lyapunov_exponent_of_electrocorticograms_in_partial_seizures)  
12. Non-linear Classification of Heart Rate Parameters as a Biomarker for Epileptogenesis \- PMC \- PubMed Central, Zugriff am November 20, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3361514/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3361514/)  
13. On the viability of ECG features for seizure anticipation on long-term data \- IEEE Xplore, Zugriff am November 20, 2025, [http://ieeexplore.ieee.org/document/8065951/](http://ieeexplore.ieee.org/document/8065951/)  
14. A Review of Machine Learning and Deep Learning Trends in EEG-Based Epileptic Seizure Prediction \- IEEE Xplore, Zugriff am November 20, 2025, [https://ieeexplore.ieee.org/iel8/6287639/10820123/11153423.pdf](https://ieeexplore.ieee.org/iel8/6287639/10820123/11153423.pdf)  
15. AN-EXTENSIVE-EUROPEAN-EEG-DATABASE-FOR-ANALYSES-OF-LONG-TERM-RECORDINGS \- American Epilepsy Society, Zugriff am November 20, 2025, [https://aesnet.org/abstractslisting/an-extensive-european-eeg-database-for-analyses-of-long-term-recordings](https://aesnet.org/abstractslisting/an-extensive-european-eeg-database-for-analyses-of-long-term-recordings)  
16. Identification of Relevant ECG Features for Epileptic Seizure Prediction Using Interpretable Machine Learning \- Malmö University, Zugriff am November 20, 2025, [https://mau.diva-portal.org/smash/get/diva2:1988179/FULLTEXT01.pdf](https://mau.diva-portal.org/smash/get/diva2:1988179/FULLTEXT01.pdf)  
17. EEG datasets for seizure detection and prediction— A review \- PMC \- PubMed Central, Zugriff am November 20, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10235576/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10235576/)  
18. CHB-MIT Scalp EEG Database v1.0.0 \- PhysioNet, Zugriff am November 20, 2025, [https://physionet.org/content/chbmit/1.0.0/](https://physionet.org/content/chbmit/1.0.0/)  
19. \[2504.08381\] An Empirical Investigation of Reconstruction-Based Models for Seizure Prediction from ECG Signals \- arXiv, Zugriff am November 20, 2025, [https://arxiv.org/abs/2504.08381](https://arxiv.org/abs/2504.08381)  
20. The present and future of seizure detection, prediction, and forecasting with machine learning, including the future impact on clinical trials \- PubMed Central, Zugriff am November 20, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11269262/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11269262/)  
21. On the performance of seizure prediction machine learning methods across different databases: the sample and alarm-based perspectives \- Frontiers, Zugriff am November 20, 2025, [https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1417748/full](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1417748/full)  
22. Machine and Deep Learning-Based Seizure Prediction: A Scoping Review on the Use of Temporal and Spectral Features \- MDPI, Zugriff am November 20, 2025, [https://www.mdpi.com/2076-3417/15/11/6279](https://www.mdpi.com/2076-3417/15/11/6279)  
23. An approach to detect and predict epileptic seizures with high accuracy using convolutional neural networks and single-lead-ECG signal \- PubMed, Zugriff am November 20, 2025, [https://pubmed.ncbi.nlm.nih.gov/38359446/](https://pubmed.ncbi.nlm.nih.gov/38359446/)  
24. Deep Learning Models for Predicting Epileptic Seizures Using iEEG Signals \- MDPI, Zugriff am November 20, 2025, [https://www.mdpi.com/2079-9292/11/4/605](https://www.mdpi.com/2079-9292/11/4/605)  
25. A One-Dimensional CNN-LSTM Model for Epileptic Seizure Recognition Using EEG Signal Analysis \- Frontiers, Zugriff am November 20, 2025, [https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.578126/full](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.578126/full)  
26. (PDF) An Optimized Hybrid CNN-LSTM Model for Epileptic Seizure Detection and Prediction, Zugriff am November 20, 2025, [https://www.researchgate.net/publication/394265373\_An\_Optimized\_Hybrid\_CNN-LSTM\_Model\_for\_Epileptic\_Seizure\_Detection\_and\_Prediction](https://www.researchgate.net/publication/394265373_An_Optimized_Hybrid_CNN-LSTM_Model_for_Epileptic_Seizure_Detection_and_Prediction)  
27. A comprehensive evaluation of interpretable artificial intelligence for epileptic seizure diagnosis using an electroencephalogram: A systematic review \- PubMed Central, Zugriff am November 20, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11907617/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11907617/)  
28. Wearable Epileptic Seizure Prediction System with Machine-Learning-Based Anomaly Detection of Heart Rate Variability \- MDPI, Zugriff am November 20, 2025, [https://www.mdpi.com/1424-8220/20/14/3987](https://www.mdpi.com/1424-8220/20/14/3987)  
29. MLSPred-bench: Transforming electroencephalography (EEG) datasets into machine learning-ready epileptic seizure prediction benchmarks \- PubMed, Zugriff am November 20, 2025, [https://pubmed.ncbi.nlm.nih.gov/40949826/](https://pubmed.ncbi.nlm.nih.gov/40949826/)  
30. The power of ECG in multimodal patient‐specific seizure monitoring: Added value to an EEG‐based detector using limited channels \- NIH, Zugriff am November 20, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8518059/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8518059/)  
31. (PDF) Multimodal Coherence-Correlation Fusion of EEG and ECoG Signals for Enhanced Epileptic Seizure Detection Using Discrete Lyapunov Wavelet Transform \- ResearchGate, Zugriff am November 20, 2025, [https://www.researchgate.net/publication/395435689\_Multimodal\_Coherence-Correlation\_Fusion\_of\_EEG\_and\_ECoG\_Signals\_for\_Enhanced\_Epileptic\_Seizure\_Detection\_Using\_Discrete\_Lyapunov\_Wavelet\_Transform](https://www.researchgate.net/publication/395435689_Multimodal_Coherence-Correlation_Fusion_of_EEG_and_ECoG_Signals_for_Enhanced_Epileptic_Seizure_Detection_Using_Discrete_Lyapunov_Wavelet_Transform)  
32. Artificial intelligence in electroencephalography analysis for epilepsy diagnosis and management \- PMC \- PubMed Central, Zugriff am November 20, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12400865/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12400865/)  
33. EasyChair Preprint Challenges in Automating Seizure Prediction with Deep Learning's Crucial Role, Zugriff am November 20, 2025, [https://easychair.org/publications/preprint/cH9V/open](https://easychair.org/publications/preprint/cH9V/open)  
34. Automatic detection and prediction of epileptic EEG signals based on nonlinear dynamics and deep learning: a review \- Frontiers, Zugriff am November 20, 2025, [https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1630664/full](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1630664/full)  
35. Proposed clinical practice guideline for automated seizure detection using wearable devices, Zugriff am November 20, 2025, [https://www.ilae.org/guidelines/guidelines-and-reports/proposed-clinical-practice-guideline-for-automated-seizure-detection-using-wearable-devices](https://www.ilae.org/guidelines/guidelines-and-reports/proposed-clinical-practice-guideline-for-automated-seizure-detection-using-wearable-devices)