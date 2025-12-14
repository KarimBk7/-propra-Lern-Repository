### F1: Mit welchen Werten werden benannte Rückgabewerte initialisiert?
Diese werden bei Funktionsbegin mit dem Nullwert ihres Typs initialisiert.

### F2: Wann ist es Ihrer Meinung nach sinnvoll, benannte Rückgabewerte zu benutzen? (Dies ist keine technische Frage, sondern eine Stilfrage.)
+ Wenn die Namen sinn ergeben
+ Mehrere Rückgabewerte existieren

### F3: Was ist der Unterschied zwischen einer variadischen Funktion und einer Funktion, die einen Slice (Golang) von Parametern bekommt?
**Variadische Funktion**: <br>
+ Wird aufgerufen mit mehreren Elementen getrennt mit ``,``
**Funktion mit Slice**: <br>
Wird mit Slice aufgerufen ``[]string{"a", "b"})``

### F4: Welche Vor- oder Nachteile einer Schreibweise gegenüber der anderen fallen Ihnen ein?
**Nachteil Slice**: Wenn der Nutzer nur einen einzigen Wert übergeben will, aber die Funktion einen Slice als Parameter will, dann muss der Nutzer einen unnötogen Extraschritt tun, und diesen in ein Slice tun.


