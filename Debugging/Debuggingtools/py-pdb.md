### F1: Was sind die beiden verschiedenen Methoden des Tutorials, wie Sie das Debugging mit pdb starten?
Entweder mit ``import pdb; pdb.set_trace()`` oder seut version 3.7 mit ``breakpoint()``.

### F2: Welche wichtigsten Kommandos stehen Ihnen zur Steuerung von pdb zur Verfügung?
+ **l**: Umliegende Codezeilen anzeigen
+ **b**: breakpoints erstellen
+ **s**: in Funktionen eindringen
+ **n**: fährt mit laufzeit fort bis zur nächten Zeile
+ **r**: um direkt zur return Zeile der akutellen Funktion zu springen

### F3: Welche Voraussetzung sollte bei einem größeren Programm erfüllt sein, um mittels "pdb" einen Defekt gut finden zu können?
Der Fehler sollte gut reproduzierbar sein mithilfe eines spezifischen Testfalls.


### F4: Wie nützlich finden Sie das Debugging mit "pdb"? Was gefällt Ihnen gut, was nicht?
Die Visualisieung innerhalb der Konsole ist etwas unüberschaubar. Ein etwas besseres UI welches mehr Informationen bereitstellt w#re nicht schlecht.<br>
Ich mag das schnelle navigieren mit abkürzungen der Befehle.