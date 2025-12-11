### F1: Was ist die Beziehung zwischen Objekten und Werten von "Variablen"?
Bei Objekten herscht eine Referenzsemantik, während bei einzelnen Werten eine Wertsemantik.

### F2: was ist der Unterschied zwischen folgenden beiden Zuweisungsvarianten?
**a)** Ist ein Integer-Literal bzw. Python erstellt direk ein ``int``-Objekt mit Wert 5.<br>
**b)** Ist eine Funktion, welches ein ``int`` aus dem Argument 5 erzeugt.

### F3: Betrachten Sie wieder die Variante b) aus der vorherigen Frage. Normalerweise nutzen wir die Funktion int(), wenn wir den Datentyp eines Wertes umwandeln möchten. Gilt somit int() als Konstruktor der Klasse int oder einfach als eine eingebaute Funktion zur Typumwandlung?
``int()`` ist der Konstruktor der Klasse ``int``. Der Konstruktor ist einfach nur so implementiert, dass er unterschiedliche Eingabetypen akzeptiert.

### F4: Was ist im Video damit gemeint, dass Speicher in Python "dynamisch" verwaltet wird?
Damit ist gemeint das es verschieden Verwaltungen gibt. Diese währen ``rebind`` oder ``mutating``. Während ``rebinding`` ein neures Objekt erstellt und neu zuweist, verändert ``mutating`` das Objekt direkt.

### F5: Welcher Name zeigt auf den Wert 5, nachdem wir diesen Code ausführen?
Keiner der Namen zeigt auf den Wert 5.

### F6: Was ist mit "mutable aliasing" gemeint?
Das mehrere Variablen auf dasselbe veränderbare Objekt zeigen. Jede Änderung über einen der Variablen auf das Objekt wirkt sich aufs andere aus.

### F7: Was ist mit "mutable aliasing" gemeint?
**a)** Worauf zeigt der Name ``mylist2``, nachdem wir den Code laufen lassen? Warum?<br>
+ Der Name ``mylist2`` zeigt auf das Objekt [1, 12], weil es auf die selbe Lsite referenziert wie ``mylist`` und diese Lsite sptäer verändert wird. <br>

**b)** Welcher Name zeigt auf das ``int``-Objekt mit dem Wert 5, nachdem wir den Code laufen lassen? Warum?<br>
+ Es gibt kein Name der auf das ``int``-Objekt mit dem Wert 5 zeigt, nach der Änderung wird 5 durch 1 ersetzt.

### F8: Was sind "immutable values" ganz genau und welche Datentypen sind in Python "immutable"?
Immutable values, sind Objekte die nach deren Erstellung nciht verändert werden können. Diese können höchstens ``rebindet`` werden.<br>
Zu immutable values gehören Zahlen (wie int, float), bools und sequenzen (wie str, tuple).

### F9: Was machen wir eigentlich, wenn wir den Wert einer Variable ändern? Und was passiert mit dem ursprünglichen Wert dieser Variable nach der Änderung?
Wenn wir den Wert einer Variable ändern, dann ändern wie das ``binding`` auf eine neues erstelltes Objekt. Das alte Objekt wird weder geändert noch gelöscht außer es eine andere Variable zeigt darauf.

### F10: Wird die Definition von "Ändern" beeinflusst, wenn wir mit "mutable" Datentypen arbeiten? Wenn ja, wie genau?
Mutable Datentypen können ``mutated`` werden, welches das ändern des Objekts selber ist. Z.B. wenn ich an einer Lsite weitere Elemente ran hänge, dann ``mutate`` ich die liste und ``rebinde`` sie nicht.

### F11: Wir haben gelernt, dass das "Ändern" eines "unveränderlichen" Datentyps einfach eine neue Zuweisung bedeutet und dass dieses "Ändern" bei "veränderlichen" Datentypen wirklich den Wert "in-place" ändert. Geben Sie ein kleines Python-Beispiel für eine "Änderung" eines "veränderlichen" Datentyps, wo dabei ein neues Objekt erstellt wird.
```py
mylist = [1,2,3,4]
mylist = mylist + [5]
```

### F12: Im Video wurde die Bedeutung von "Dynamic Typing" in Python erläutert. Beschreiben Sie in eigenen Worten, was diese Eigenschaft bedeutet.
+ Ein Name selbst besitzt kein Typ. Er kann im nächsten Codeabschnitt auf ein Objekt ines anderen Typs zeigen.
+ Der Typ gehört immer zum Objekt, nicht zur Variable.


### F13: Betrachten Sie den folgenden Code:
**a)** Worauf zeigt hier der Name ``y``?<br>
+ Es zeigt auf das dritte Element der Liste ``mylsit`` (auf die ``7``)<br>

**b)** Welche namen zeigen auf das Element ``7`` in der Liste ``mylist``?<br>
+ Die Namen ``x`` und ``y`` zeigen auf das Element ``7`` in der Liste ``mylist``.


### F14: Zeigen x und y im Folgenden Code auf dasselbe Objekt mit dem Wert 10? Wieso? 
Nein, diese zeigen auf 2 verschiedene Objekte mit dem Wert ``10``. Das liegt daran, das die Objekte nicht aufeinander per Name referenziert werden und daher nicht wissen können wo die ``10`` des jeweilige anderen ist. Sie werden per Wertzuweisung erstellt und nicht Namenszuweiseung.

### F15: Fassen Sie zusammen, was Sie gelernt haben, indem Sie in eigenen Worten erklären, was gemeint ist, wenn wir sagen, "Variablen sind einfach Namen, die auf Objekte verweisen".
Variablen sind einfach nur Namen die auf Objekte verweisen. Die Namen keine Information, was für ein Typ das Objekt hat, weder was für ein Wert sich drin befindet oder sonst was. Es dient jediglich als Referenz die auf ein Objekt verweist.