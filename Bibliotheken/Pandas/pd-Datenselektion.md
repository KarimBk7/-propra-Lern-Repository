### F1: Eine andere Schreibweise für dataframe["spaltenname"] ist der Syntax dataframe.spaltenname. Dieser Syntax wird jedoch beim sauberen Programmieren vermieden. Überlegen Sie, welche Probleme es mit diesem Syntax geben könnte.
+ Manche Spaltennamen können leerzeichen, sonderzeichen oder zahlen am anfang haben was zu Syntaxfehlern führt.
+ Eine Spalte könnte zufälligerweise so heißen wie eine Methode von ``Pandas``.


### F2: Enthält 0:n, auf ein DataFrame angewendet, das Element mit dem Index n oder geht es nur bis n-1? Sie können dazu das Ergebnis der vorherigen Aufgabe betrachten.
Es geht nur bis ``n-1``.


### F3: Was passiert, wenn sie versuchen, statt der Zeilenindizes Slicing auf den Spaltenindizes zu betreiben?
Pandas interpretiert diese nicht als Spaltenslicing, sondern als Slice über den Zeilenindex.

### F4: In pd-Datenstrukturen haben Sie hierzu bereits die Schreibweise dataframe[spaltenindex][zeilenindex] kennengelernt. Wieso funktioniert das nicht genauso für eine Liste an Spaltenindizes, zum Beispiel: erststimmen_df[["Wahlbezirk", "Gültige Stimmen"]][5]?
Der Rückgabetyp beim operator mit mehreren Spaltenindexen ist immernoch ein Dataframe und keine Series.<br>
Und da man mit dem Zeilenindex nur auf Series's zugreifen kann wird dies nichtfunktioniert solange es nocht ein DataFrame ist.

### F5: Welchen Bereich gibt erststimmen_df.loc[0:3] zurück?
Die zeilen 0 bis 3 (inklusive der 3) mit allen Spalten.

### F6 Welchen Bereich gibt erststimmen_df.loc[:3, "Erststimmen"] zurück?
Dies Gibt einen Fehler aus, weil es keine Spalte mit den Namen "Erststimmen" gibt. Falls mit der Aufgabe aber eher "Stimmenart" gemeint ist, dann gibt dies alle Zeilen von 0 bis 3 aus mit der Spalte "Stimmenart".

### F7: Welchen Bereich gibt erststimmen_df.loc[:] zurück?
Dies gibt den gesamtem DataFram aus ohne Einschränkungen.

### F8: Wie bereits erwähnt lassen sich per Slicing auch Schrittgrößen angeben. Was tut der folgende Ausdruck: erststimmen_df.loc[0:49:10]
Dieser Ausdruck gibt alle Zeilen von 0 bis 49, aber in 10er Schritten.

### F9: Was bedeutet erststimmen_df.loc[::10, "Adresse":"Bezirksnummer"]
Dieser Ausdruck gibt nur alle 10 Zeilen aus mit Spalten von "Adresse" bis "Bezirksnummer".
