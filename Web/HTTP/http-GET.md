### F1: Was hat Sie von diesem Inhalt am meisten überrascht?
Mich überraschte die große komplexität die sich seit 1990 in diesem Bereich entwickelt hat und was man alles mit HTTP mittlerweile alles machen kann.

### F2: Verstehen Sie die Eigenschaften "safe" und "idempotent" von GET. Sind diese unabhängig voneinander oder impliziert eine die andere?
Eine Methode ist 'safe' wenn es keine Änderungen am Serverzustand verursacht (read only).
Eine Methode ist 'idempotent' wenn es den selben Effekt am Server hat wie wenn man die gleiche Methode mehrmals ausführt.
Alle safe Methoden sind auch idempotent, aber nicht alle idempotent Methoden sind safe.

### F3: Zitieren Sie den entsprechenden Satz und nennen Sie den Abschnitt, wo er steht.
"A client MUST include a Host header field in all HTTP/1.1 request messages." - in Abschnitt 14.23 Host

### F4: MIME-Types
+ PDF-Datei: application/pdf
+ JPG-Bild: image/jpeg
+ MS-Word-Datei: application/msword

### F5: HTTP-Standard RFC 2616 
Der 'charset' Parameter gibt dem Empfänger an in welcher Zeichenkodierung die Textdatei vorliegt.<br>
Der Content-Encoding im Header beschreibt die Übertragungskodierung und nicht die eigentliche Textkodierung.