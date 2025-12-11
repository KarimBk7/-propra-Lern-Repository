### F1: Welche for-Schleifen kann man nicht durch eine gleichwertige List-Comprehension ersetzen? Warum?
Schleifen mit komplexerem Inhalt wie ``break``. ``continue``, ``return`` oder ``yield``, weil eine List.Comprehension über alle Elemente der Iterablen läuft und könnte keine dieser behandeln.


### F2: Welche for-Schleifen könnte man zwar, aber sollte man nicht durch eine gleichwertige List-Comprehension ersetzen? Warum?
Eine List-Comprehension, die keine Elemente speichert sondern nur funktionen aufruft. Beispiel wäre had aufrufen von ``print()``. man würde die gesamte Liste mit ``None`` füllen.


### F3: Im Artikel wurden "Zen of Python"-Prinzipien erwähnt, anders bekannt auch als "PEP 20". Beschreiben Sie für jedes der folgenden Prinzipien einen Fall, in dem der Einsatz von List-Comprehensions das jeweilige Prinzip verletzt:
1. **"Flat is better than nested"**:
Stark verschachtelte List-Compreehensions mit mehreren ``for``- und ``if``-Teilen.<br>
Das verletzt es, weil die Lesbarkeit stark abnimmt. Der geschriebene Code sollte für andere Entwickler ebenso gut lesbar sein. mehrere ``for``- oder ``if``-Teile in einer List Comprehension erschweren die lesbarkeit enorm.<br>
2. **"Readability counts."**:
Auch wenn eine List-Comprehension ein richtiges Ergebnis liefert, ist es womöglich für zukünftige Änderungen er unpraktisch, da man leicht den überblick verliert. Lieber ausgeprägter bauen und es dafür übersichtlicher machen.