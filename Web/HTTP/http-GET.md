#### F1: Was hat Sie von diesem Inhalt am meisten überrascht?
Mich überraschte die große komplexität die sich seit 1990 in diesem Bereich entwickelt hat und was man alles mit HTTP mittlerweile alles machen kann.

#### F2: Verstehen Sie die Eigenschaften "safe" und "idempotent" von GET. Sind diese unabhängig voneinander oder impliziert eine die andere?
Eine Methode ist 'safe' wenn es keine Änderungen am Serverzustand verursacht (read only).
Eine Methode ist 'idempotent' wenn es den selben Effekt am Server hat wie wenn man die gleiche Methode mehrmals ausführt.
Alle safe Methoden sind auch idempotent, aber nicht alle idempotent Methoden sind safe.