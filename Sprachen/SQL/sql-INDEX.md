### F1: Das Befüllen der Tabelle (0, 1, 2-mit-2A, 3, 4)
Das Befüllen der Tabelle mit 1000000 Zeilen dauert länger als einfache Einzel-Queries, da für jeden Datensatz ein Insert durchgeführt wird.

### F2: Die Abfrage ohne Index (1, 2-mit-2B, 3, 4)
Ohne Index muss die Datenbank einen Fll-Table-Scan durchführen. Das bedeutet, alle 1000000 Zeilen werden nacheinander geprüft. Je größer die Tabelle desto höher die Laufzeit

### F3: Das Anlegen des Index (1, 2-mit-2C, 3, 4)
Das Anlegen des Index verursacht einmalig Kosten. Hier wird die komplette Tabelle gelesen, sortiert und die Indexstruktur aufgebaut.

### F4: Die Abfrage mit Index (1, 2-mit-2D, 3, 4)
Mit Index wird die gleiche Bedingung nicht meht per Full-Table-Scan, sondern über die Indexstruktur ausgewertet. Damit sinkt die Laufzeit.

### F5: Eine Abfrage, die die Anzahl der Datensätze mit random_number zwischen 500000 und 600000 zählt.
Der Bereich [500000, 600000] umfasst viele Werte wehslab die Selektivivtät schlechter wird als im kleinen Intervall. Auch mit Index müssen mehr Treffer gelesen werden.

### F6: Messen Sie die Ausführungszeit mit mehrspaltigem Index.
Der mehrspaltige Index erlaubt es, gleichzeitig nach random_number und category zu filtern, Die Datenbank kann im Indexbereich springen und dort nur die Einträge mit Kategory 'A' betrachten.

### F7: Messen Sie die Ausführungszeit ohne den mehrspaltigen Index.
Ohne mehrspaltigen Index muss SQLite entweder einen Full-Table-Scan durchführen oder einen weniger passenden Index verwenden. Die Laufzeit steigt im Vergleich zur Variante mit MehrspaltigenIndex.

### F8: Diskutieren Sie Ihre Messergebnisse: Wie groß war der Unterschied zwischen den Abfragezeiten mit und ohne Index? Welche Faktoren könnten die Performance-Unterschiede beeinflussen? Wie viele Anfragen müssen Sie machen, um das Anlegen des Index zu amortisieren?
**Abfragezeiten**: <br>
In den Messungen zeigt sic, dass Abfrage ohne Index deutlich langsamer sind als mit index. Bei einem Full-Table-Scan müssen alle 1000000 Zeilen gelesen werden, während der Indexzugriff nur die relevanten Bereiche durchsucsht. Je selektiber die Bedingung desto größer ist der Geschwindigkeitsvorteil.
<br>

**Einflussfaktoren**:<br>
+ Der Datenmenge
+ Der Selektivität
+ Form der Abfrage
<br>

**Amortisation des Index**:<br> 
Das Anlegen des Index verursacht einmalige Kosten in der selben Größenordnung wie ein vollständiger Durchlauf über die Tabelle. Dies amortisiert sicht, sobald genügend Leseanfrage vom Index profitieren.

