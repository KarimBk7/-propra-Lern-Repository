### F1: Lesen Sie die Einleitung von diesem Artikel über funktionale Programmierung in Python. Nennen und beschreiben Sie kurz die zwei aus Ihrer Sicht wichtigsten Vorteile von funktionaler Programmierung, die im Artikel genannt werden.
+ Fuktionen nehmen nur einen Input und einen Output und haben keinen internen Zustand der das Ergebnis irgendwie beinflussen kann.
+ Einfacheres debugging und testen


### F2: Vergleichen Sie die beiden Lösungen. Welche Variante empfinden Sie als besser lesbar? Stellen Sie sich vor (oder probieren Sie es aus), sie übergeben an die beiden Funktion mehrere Millionen Produkte. Denken Sie, dass die Funktionen sich unterschiedlich verhalten und wenn ja, inwiefern? Wie schätzen Sie die beiden Funktionen hinsichtlich ihrer Laufzeit und Speichernutzung ein und wie lässt sich ggf. dadurch der Unterschied erklären?
Für die spezifische Aufgabe hätte auch eine simple for-Schleife gerreicht, wenn man die länge, komplexität und lesbarkeit des Codes betrachtet. Wenn man dieses Problem jedoch öfters im Laufe des Projekts behandeln muss dann ist die funktionale Methode eher doch besser.<br>
Die imperative Version erstellt keine neue Liste und ist Speicherpaltz sparender, weil es eine ``in-place`` Operation durchführt.
Intuitiv gesehen würde ich sagen das beide Varianten Laufzeittechnisch gleich sind.