### F1: Benutzen Sie den Abschnitt "Two Categories of Go Types" im Artikel go101: Value Parts um die Frage zu beantworten, was Einblocktypen und Mehrblocktypen sind.
**Einblocktypen** sind Datentypen die nur von einem ``memory block`` (kontinuierliches Speichersegment) im Speicher gehosted werden, während **Mehrblocktypen** Datentypen sind die von mehr als einem ``memory block`` gehosted werden.

### F2: Wie wird ein int-Array der Länge 5 deklariert?
Mit schreiben der Zahl 5 in die Eckigen Klammern <br>
``array := [5]int``.

### F3: Wie wird ein int-Array der Länge 5 definiert (also mit Werten befüllt)?
Mit schreiben der Zahl 5 in die Eckigen Klammern und einem darauf folgende geschweifte Klammer mit den Werten. <br>
``array := [5]int{1,2,3,4,5}``.

### F4: Wie greift man per Index auf ein bestimmtes Element eines Arrays zu?
Mit dem reinschreiben des Indexes in die Eckigeklammer nach dem Namen der Variable<br>
``array[2]``

### F5: Kann man in einer Variable vom Typ [5]int ein Array wie {7, 8, 9, 10} speichern? Begründen Sie Ihre Antwort.
Ja, dies geht, da die zugewiesene Liste nur 4 Elemente Enthält, während die Variable ja Platz für 5 Elemente hat.

### F6: Was ist der Nullwert eines Arrays?
Der Nullwert eines Arrays mit fester Länge ist die Liste gefüllt mit 0en. ``[3]int --> [0,0,0]``<br>
Der Nullwert eines Arrays ohne fester Länge ist ein leeres Array. ``[]int --> []``

### F7: Was passiert, wenn man ein bestehendes Array einer anderen Variable zuweist? Entstehen dadurch zwei eigenständige Arrays oder eine gemeinsame Referenz?
Es entstehen dadurch zwei eigenständige Arrays und keine Referenz zueinander.

### F8: Was passiert mit dem Array evenNumbers, wenn Sie ein Element in evenNumbersSlice auf 42 setzen?
Das geänderte Element wird ebenfalls im Array ``evenNumbers`` auf 42 gesetzt, wei ``evenNumbersSlice`` nur eine View vom eigentlichen Array ist.

### F9: Ändern Sie die Zeile 14 im A-Tour-Of-Go-Beispiel zu ``s = s[:14]`` Führen Sie das Programm aus. Was ist passiert? Warum? Worauf muss man bei einer solchen Größenänderung achten?
Es entsteht ein runtime-error mit ``slice bounds out of range``, weil wir auf Position 14 greifen, obwohl das Arrays nur 6 belegte Plätze hat.

### F10: Was ist die Kapazität des Slice s?
Die Kapazität von ``s`` beträgt 3.

### F11: Was ist die Kapazität des Slice s? Was ist seine Länge?
Die Kapazität ist 8 und die Länge ist 4.

### F12: Was ist die Kapazität des Slice s2? Was ist seine Länge?
Die Kapazität ist 8 und die Länge ist 0.

### F13: Was geben die zwei fmt.Println()-Anweisungen jeweils aus?
[42 9 8]<br>
[42 9 11 13 14]

### F14: Was befindet sich am Ende in Variablen arr, sl1 und sl2? Was ist das zugrundeliegende Array von sl1 und sl2?
arr = [10 20 30 40 99 60]<br>
sl1 = [20 30 40] <br>
sl2 = [20 30 40 99 60]<br>
Beide Slices referenzieren das Array ``arr``.