### F1: Matchen Sie "Soße", bei dem das "o" beliebig oft vorkommen darf. ("Soooße", "Sße")
``So*ße``

### F2: Matchen Sie jede Zeichenkette, der mit "A" beginnt, beliebig viele Zeichen dazwischen enthält und mit "n" endet.
``A.*n``

### F3: Wie können Sie trotz * dafür sorgen, dass ein Zeichen mindestens einmal vorkommt? Formulieren Sie dazu Wa*l um, sodass "a" mindestens einmal vorkommt.
``Waa*l``

### F4: Setzen Sie den vorherigen regulären Ausdruck mit + um.
``Wa+l``

### F5: Matchen Sie "Banana", wobei jedes "a" 1 oder mehrmals wiederholt werden darf. ("Baaanaanaa")
``Ba+na+na+``

### F6: Matchen Sie Zeichenketten, die "Aufgabe" oder "Aufgaben" enthalten.
``Aufgaben?``

### F7: Matchen Sie alle Zeichenketten, die mit "A" beginnen, zwischen 4 und 6 Zeichen lang sind und auf "e" enden (z. B. "Arche", "Ameise", "Alte", aber nicht "Abgründe").
``A.{2,4}e``

### F8: Matchen Sie alle 5-stelligen Zahlen.
``\d{5}``

### F9: Lesen Sie diese StackOverflow-Diskussion: https://stackoverflow.com/questions/2301285/what-do-lazy-and-greedy-mean-in-the-context-of-regular-expressions. Erklären Sie, was der Unterschied zwischen "greedy" und "lazy" Quantoren ist.
+ "Greedy"-Quantoren matchen standardmäßig so viel wie möglich, solagen das gesamte Muster noch passt.
+ "Lazy"-Quantoren matchen dagegen so wenig wie möglich und erweitern nur, wenn es nötig ist, damit das Muster ingesamt passt.

### F10: Sind unsere Quantoren bisher "greedy" oder "lazy" gewesen?
Unsere Quantoren ``*``, ``+`` und ``?`` sind "greedy".

### F11: Die Diskussion enthält außerdem eine Tabelle, die zeigt, wie man "greedy" Quantoren in "lazy" Quantoren umwandelt und umgekehrt. Formulieren Sie ihren Regex aus F2 so um, dass er die kleinstmögliche Zeichenkette trifft, die die Bedingungen erfüllt.
``A.*?n``

### F12: Testen Sie diesen Regex an dem Text "Anomalien". Wie unterscheiden sich die Treffer von F2 und F11?
Die "greedy" Version sucht das größtmögliche Ergebnis was in dem Fall ``Anomalien`` wäre während die "lazy" Version bereits beim ersten vorkommen aufhört und das Ergebnis zeigt, in dem Fall ``An``.