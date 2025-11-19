### F1: Obwohl eine Series mehrere Elemente enthält, kann man auch genau so logische Ausdrücke auf eine Series anwenden (series < value). Tun Sie dies für die Spalte "Die Linke" im erststimmen_df und beschreiben Sie, was zurückgegeben wird.
Dieser Ausdruck vergleicht paarweise alle Werte mit dem ``Value`` und schreibt dementprechend daneben ``False`` oder ``True``.


### F2: Wie Sie merken, ist es eher eine Stilfrage, ob man query() verwendet oder beim herkömmlichen Boolean-Indexing bleibt. Lesen Sie diesen Blog-Artikel zu den Vor- und Nachteilen von query(). Zu welcher Variante neigen Sie und warum? Begründen Sie.
Ich Neige eher zur ``query()``-Variante, daman sich so das erstllen von Variabeln spart. Man kann den namen der Spalte direkt in die Query rein schreiben, statt wie bei Boolean-Indexing erstmal ne Reihe von Series's zu erstellen.