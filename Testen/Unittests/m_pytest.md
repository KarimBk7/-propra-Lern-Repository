### F1: Aha, offenbar kann pytest als direkter Ersatz von unittest agieren. Welcher Output gefällt Ihnen besser? Warum?
Ich denke das der Output von pytest mir besser gefällt, weil man zusätzliche Information wie ``Platform`` und ``rootdir`` sehen kann, welche bei der Dokumentation oder Debuggen praktisch sein können. <br>
Außerdem sieht man fehgeschlagene Tests viel ausführlicher als bei ``unittest``.

### F2: Vergleichen Sie die Ausgaben der beiden Kommandos. Was ist Ihr Eindruck? Fallen Ihnen noch wichtige Gründe ein, unittest zu benutzen?
**Unittest**: 
+ gibt die print-Ausgaben während der Ausführung aus
+ Jeder Fehlschlag bietet ein Traceback inklusive Klassenname, Methodenname und Zeilennummer
+ Am Ende gibt eseine Übersicht der Anzahl Tests und Laufzeit
<br>

**Pytest**:
+ Zeigt Umgebung (siehe F1)
+ Listet Tests einmal kompakt 
+ Danach kommt eine detaillierte Sektion ``ERRORS`` mit Erklärung, warum es nicht läuft
+ Am Ende eine Zusammenfassung wie viele passed, error und Gesamtzeit
<br>

**Gründe Unittest zu benutzen**:
+ Benutzt Testklassen, was für manche Test-Designs praktisch sein kann
+ Kein zusätzliches Paket notwendig (Für ältere Systeme gut)
