### F1: Um wie viel Prozent hat sich die Laufzeit erhöht?
Die Laufzeit im Vergleich zum Skript daavor hat sich um 2 % erhöht.

### F2: Studieren Sie mithilfe der Dokumentation die Profiling-Ausgabe. Welche drei Programmzeilen (bitte deren Text angeben) verbrauchen den Bärenanteil der Laufzeit?
+ Zeile 10 und 48: ``conn = sqlite3.connect(dbfile)``
+ Zeile 51: ``c.execute('INSERT INTO profile VALUES (?, ?)', (name, age))``
+ Zeile 52: ``conn.commit()``

### F3: Um welchen Faktor hat sich die Laufzeit reduziert? (Cool, oder?)
Das Program ist nun ungefähr 36-Mal so schnell.