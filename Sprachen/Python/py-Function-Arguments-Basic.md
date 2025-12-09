### F1: Was ist der Unterschied zwischen einem Parameter und einem Argument in Python?

**Parameter**: Sind Namen/Platzhalter in einer Funktionsdefinition<br>
**Argument**: Sind konkrete Werte/Objekte beim Funktionsaufruf.


### F2: "Ein Argument kann entweder die Rolle eines Positions- oder eines Schlüsselwortarguments einnehmen." Stimmt diese Aussage? Erklären Sie, indem Sie beide Arten von Argumenten kurz definieren und dies durch geeignete Beispiele in Python veranschaulichen.
Ja die Aussage stimmt, da ein Positionsargument nur an seine Position an den Parameter gebunden wird und ein Schlüsselwortargument **NUR** über den Namen an einen bennanten Parameter gebunden wird, außerdem spielt die Poition dabei keine Rolle.
<br>
Im folgendem sieht man die kombination aus Positions- und SChlüsselwortargument.
Die Position von Wert ``1`` wird mit Parameter ``a`` gebunden, da diese an selber Position stehen, während die Werte ``c=3`` und ``b=2`` per Schlüsselwort an die Parameter gebunden werden, was die Position irrelevant macht.

```py
def foo (x, y, z):
	print(x, y, z)

>>> foo(1, z=3, y=2)
1 2 3
```

### F3: Was sind Parameter mit Standardwerten? Gelten Argumente, die beim Funktionsaufruf an solche Parameter gebunden werden, eher als Positions- oder Schlüsselwortargumente? Überlegen Sie.
Standardwerte sind Werte die innerhalb der Funktion bereits an einem Parameter gebunden sind ohne das der User diesen Wert definieren muss. Dieser Wert wird verwendet wenn der User keinen Wert im Funktionsaufruf definiert.<br>
Ob Argumente eher as Positions- oder Schlüsselwortargumente an Parameter gebunden werden hängt vom Funktionsaufruf ab.<br>
Man kann beides verwenden und das was weder mit Position noch mit Schlüsselwort gerufen wird, wird einfach mit Standardwert gebunden.

### F4: Finden Sie die Defekte in den folgenden Funktionsaufrufen. Geben Sie jeweils einen reparierten Aufruf an:
1. Positionsargumente dürfen nicht nach Schlüsselwortargumenten folgen.
```py 
Korektur: print(foo(1, b=2, c=3)) 
```

2. Der Parameter ``b`` erhält zwei Argumente per Schlüsselwort- als auch per Positionsargument.
```py
Korektur: print(foo(1, c=2, b=3))
```

3. Positionsargumente dürfen nicht nach Schlüsselwortargumenten folgen.
```py 
Korektur: print(foo(a=1, b=2, c=3)) 
```

### F5: Überlegen Sie: Warum sollen überhaupt Positionsargumente vor Schüsselwortargumenten kommen?
Wenn man Schlüsselwortargumente vor Positionsargumenten verwenden würde, dann wäre es sehr unklar wann man welches Argument übergibt wenn die Schlüsselwortargumente selber die Position der Positionsargumente beinflussen.<br>
Angenommen man möchte per Positionsargumente den ersten Parameter definieren, aber im Funktionsaufruf steht bereits in Schlüsselwortargument an erster Stelle. Würde ich jetzt den ersten oder zweiten Parameter binden?
```py
def foo(a,b,c):
	print(a,b,c)

foo(c=3,1,2)
```

### F6: Geben Sie für jede der folgenden Spezifikationen die jeweilige Signatur der Funktion taschenrechner() für einen einfachen Taschenrechner in Python an. Die Funktion soll einen mathematischen Operator (+, -, *, /) als String sowie zwei Eingabezahlen entgegennehmen.

1. Die Funktion verwendet nur Positionsargumente.
```py
def taschenrechner(x, y, op, /):
```

2. Die Funktion verwendet nur Schlüsselwortargumente
```py
def taschenrechner( x, y, /, *, op):
```

3. Der mathematische Operator ist zwangsweise ein Schlüsselwortargument, während die beiden Eingabezahlen zwangsweise Positionsargumente sind.

### F7: Würden Sie für folgenden Funktionen irgendwelche Beschränkungen der Argumentübergabe einführen? Begründen Sie. Bedenken Sie, wie gut oder schlecht man einem Argument seine Rolle ansehen kann.
1. Ich würe alle Parameter die mit `neu..` beginnen einem Schlüsselwortargument-only zuweisen, um beim ändern von Daten nicht die falsche Spalte oder Variable zu ändern. Matrikelnummer als ersten parameter klingt intuitiv genug und kann bleiben.
2. Alle parameter nach text sollten Schlüsselwortargument only sein, da dessen Reihenfolge nicht sofort eindeutig identifizierbar ist. Parameter ``text`` bei einer Funktion namens ``formattiere_text`` als erste Position zu wählen kling selbstverständlich und muss nicht angepasst werden.
3. Hier muss man keine Regeln einbauen, da die Reihenfolge der Argumente keinen Unterschied im Ergebnis macht und alle 3 Parameter einfach nur Seitenlängen sind und es da nichts zu unterscheiden gibt. Man könnte aus Lesbarkeit die Parameter zu Position-only machen, da es eindeutig ist was die Parameter sein sollen.