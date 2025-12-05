### F1: Nennen Sie durchnummeriert 6 bis 8 Detailregeln, die Sie bislang nicht (oder nicht konsequent) befolgen, aber wertvoll finden und sich künftig angewöhnen wollen.
1. Ich sollte manchen Codezeilen wie das aufzählen von parametern einer Funktion oder das aufeinanderfolgen von Funktion lieber untereinander schreiben, damit man die verschiedenen Parameter und Funktionen klarer sehen kann.
2. Die maximale Zeichen-Anzahl pro Zeile sollte nicht 79 überschreiten, um Sichtbarkeit zu garantieren.
3. Man sollte Zeilenumbrüche vor Operatoren einfügen, damit es lesbarer ist und man Operatoren mit den Operanten matchen kann.
4. Das verwenden nom kleinem `L` (l), großem I oder großem O, sollte man vermeiden um Verwechslungen zu vermeiden.
5. Wenn man mehrere verschiedene Operationen in folge verwendet, sollte man die mit der stärksten Priorität ohne Leerzeichen davor und dnach schreiben während die mit weniger Priorität mit Leerzeichen davor und danach geschrieben werden.
6. Konstante in ein Modul implementieren und dessen Variablen groß schreiben mit `_`.


### F2: Nennen Sie durchnummeriert 2 bis 4 Detailregeln, die Sie nicht (oder nicht in der gegebenen Form) sinnvoll finden. Begründen Sie. Soweit im Standard diese Regeln eine Begründung haben, muss ihre Begründung darauf Bezug nehmen.
1. Das verwenden von ``''.join()`` statt `a = b + c` sehe ich nicht als sinnvoll, weil es nicht unbedingt die lesbarkeit erhöht. `a = b + c` sieht viel intuitiver aus.
2. Das benutzen von `return None`, um alle Funktionsenden zu präsentieren sehe ich ebenfalls nicht als unbedingt sinvoll, weil man dies auch über Kommentare genau so oder besser visualisierne kann. Dabei können die zusätzlichesn `returns` vielleicht sogar verwirrend wirken.
