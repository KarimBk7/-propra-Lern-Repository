### F1: Schauen Sie sich die Dokumentation von Pandas zu Series an. Welche von den Parametern aus der Dokumentation haben wir bei der Erstellung der Series übergeben? Was für einen Effekt hatten die übergebenen Parameter?
Wie haben nur die Daten übergeben (bzw. die Liste).<br>
+ index: Beschriftung der Elemente.
+ dtype: Datentyp der Series
+ name: Name der Series
+ copy: steuert ob ``data`` kopiert werden soll (Referenz- oder Wertsemantik)

### F2: Welchen Vorteil kann der benutzerdefinierte Index bei der Erstellung eines DataFrame bieten?
Um verschiedene Datenattribute intuitiver zu benennen.

### F3: Wenn dataframe[spalten_index_wert] eine Series ist und series[zeilen_index_wert] ein Element einer Series zurückgibt: Wie können Sie dann mithilfe des spalten_index_wert und zeilen_index_wert ein einzelnes Element aus einem dataframe zurückgeben? Erstellen Sie keine Hilfsvariablen.
Wie bei einem Array/Liste einfach ``dataframe[Spalten_index_wert][zeilen_index_wert]``