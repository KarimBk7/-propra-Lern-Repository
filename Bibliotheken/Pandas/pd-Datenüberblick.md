### F1: Beschreiben Sie, was die Methoden head(n) und tail(n) machen.
+ head(n):
	+ Gibt die ersten n Zeilen des DataFrames zurück.
+ tail(n):
	+ Gibt die letzten n Zeilen des DataFrames zurück

### F2: Was würde example_df.tail(-3) zurückgeben?
Gibt alle Zeilen bis auf die ersten 3 zurück.


### F3:  Was passiert bei example_df.head(n), wenn n größer ist als die Anzahl an Zeilen in example_df?
Es Werden einfach alle Zeilen zurück gegeben.


### F4: Beschäftigen Sie sich mit dem Parameter random_state von sample(). Welcher Wahlbezirk kommt hinaus, wenn Sie den random_state=42 und n=1 verwenden? Nennen Sie die Adresse.
Die Adresse lautet ``03W823``.


### F5: Wieso kann man mit sample() eventuell informativere Einblicke in die Datensätze kriegen als mit head() und tail()?
Es könnte sein das viele Datensätze am Anfang oder am Ende des DataFrames sehr ähnliche Werte haben.

### F6: Wie viele Spalten hat erststimmen_df?
Es hat 41 Spalten.

### F7: Wie viele Spalten speichern Integer-Daten?
Genau 33 Spalten speichern Integer-Daten.

### F8: Was ist der Rückgabewert von info()?
Die Funktion ``info()`` hat keinen Rückgabewert sondern printed direkt alles in die Konsole.

### F9: Welche Spalte hat die wenigsten Einträge?
Sie Spalte mit dem Namen ``aufn`` hat die wenigsten Einträge.


### F10: Schauen Sie in die Dokumentation zu DataFrame-Attributen und finden Sie heraus, in welchem Attribut die Zeileneinträge gespeichert werden.
Das Aittribut ``values``(``DataFrame.values``) hat die Zeileneinträge gespeichert.


### F11: Schauen Sie sich die Dokumentation zu describe() an und benutzen Sie describe() auf dem erststimmen_df. Zu welcher Art von Spalten werden hier Daten aufgeführt? Und wieso nicht zu den anderen Spalten?
Gibt standardmäßig nur Statistiken für numerische Spalten aus, weil bei z.B. Strings die Statistiken wie ``mean``, ``std`` und ``min`` schwer anwendbar sind.

### F12: Was ist die maximale Anzahl an Stimmen, die die SPD in einem Wahlbezirk bekommen hat?
Die maximale Anzahl an Stimmen, die die SPD in einem Wahlbezirk bekommen hat ist 318.

### F13: Was ist die minimale Anzahl an Stimmen, die die CDU in einem Wahlbezirk bekommen hat?
Die minimale Anzahl an Stimmen, die die CDU in einem Wahlbezirk bekommen hat ist 8.

### F14: Wie viele Stimmen hat die FDP im Durchschnitt bekommen?
Die FDP bekam im Durchschnitt 14.612285