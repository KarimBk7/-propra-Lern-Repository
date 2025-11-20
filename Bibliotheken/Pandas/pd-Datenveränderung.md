### F1: Lesen Sie die Abschnitte Returning a view versus a copy und Why does assignment fail when using chained indexing? und zitieren Sie die Textstelle, in der darüber gesprochen wird, ob View oder Copy zurückgegeben werden.
+ Why does assignment fail when using chained indexing?
	 + "predict whether it will return a view or a copy"
+ Returning a view versus a copy
	+ "the result is a slice into the original object, or a copy of the slice“


### F2: Erklären Sie, was "Chained Indexing" ist.
Chaied Indexing ist das Ausführen von mehreren Indexierungen nacheinander auf ein DataFrame oder Series, statt einen einzigen Indexierausdruck zu verwenden.


### F3: Wahrscheinlich hat nur eins oder gar keins der beiden Beispiele das erststimmen_df verändert. Erklären Sie anhand des ersten Ausdrucks das Problem von "Chained Indexing".
Weil auf in der zweiten Indexierung auf ein ``Temporären`` zwischenspeicher geschrieben wird und nicht auf dass das DataFrame selbst.


### F4: Lesen Sie die Dokumentation. Wie sollte man Fälle von "Chained Indexing" sauber umformulieren?
Die Doku sagt das man diese Fälle mit ``.loc/.iloc`` umfomulieren soll mit einer extra Maske.

### F5: Erklären Sie, inwiefern dieses Beispiel eigentlich ein Exemplar des "Chained Assignment"-Problems ist.
Die indexierung passiert hier nacheinander in Zeilen und ohne ``.loc``


### F6:  Ändert sich damit was an den genannten Best Practices? Begründen Sie.
Nein, die Best Practices bleiben gleich.

### F7: Testen Sie beide Beispiele aus dem "Chained Indexing"-Abschnitt mit aktiviertem "Copy On Write". Beschreiben Sie, ob und wie sich das Verhalten ändert.
1. Ohne Copy-on-Write:
   1. In beiden Fällen wird über zwei Indexierungsoperationen auf ein Zwischenobjekt geschrieben
   2. Dieses Zwischenobjekt ist mal View, mal Copy und ist deshalb unklar ob die Änderung im Original ankommt.
2. Mit Copy-on-Write:
   1. Jede Selektion verhält sich wie eine Kopie
   2. Eine Zuweisung über Indexierungsketten verletzt die CoW-Regeln, weil dabei gleichzeitig eine abeleitetes Objekt und das Original geändert wird
   3. Fazit: Beispiel 1 und 2 ändern ``erstimme_df`` mit aktivierten Copy-on-Write überhaupt nicht mehr.