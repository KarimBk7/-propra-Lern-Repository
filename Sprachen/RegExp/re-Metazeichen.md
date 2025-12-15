### F1: Suchen Sie mittels Regex nach dem Wort "Hallo" im Text. Wie viele Treffer finden Sie?
Ich erhalte 6 Treffer für das Wort ``Hallo``

### F2: Suchen Sie nun nach un.. Wie viele Treffer ergibt dies?
Ich erhalte 6 Treffer für ``un..``

### F3: Suchen Sie nun nach ht.. Inwiefern weicht das Ergebnis von Ihrer intuitiven Erwartung darüber ab, wie die Treffer aussehen?
Ich erhalte 6 Treffer für ``ht..``

### F4: Formulieren Sie einen Regex der sowohl "Test" als auch "Text" trifft. Geben Sie reguläre Ausdrücke immer in Backticks (`) an.
``Te[xs]t``

### F5: Was beschreibt folgender Regex: e...m
Ein ``e`` gefolt von 3 belibiegen Zeichen und ein abschließendes ``m``

### F6: Neben dem Zeilenwechsel \n gibt es weitere Steuerzeichen (nicht druckbare Zeichen). Nennen Sie sechs weitere Steuerzeichen, die in regulären Ausdrücken mit einem Backslash \ gefolgt von einem Buchstaben dargestellt werden können. Nutzen Sie dafür diese Website: https://www.regular-expressions.info/nonprint.html
+ ``\t`` für tabs
+ ``\r`` für carriage return
+ ``\a``
+ ``\e``
+ ``\f``
+ ``\v`` vertikales tab

### F7: Matchen (bzw. treffen) Sie Zeichenketten, an denen ein Punkt direkt von einem Zeilenumbruch gefolgt wird. Geben Sie dafür einen Regex ab. Gebene Sie reguläre Ausdrücke immer in ` umschlossen ab.
``\.\n``

### F8: \ ist also auch ein Metazeichen, welches seine gewöhnliche Bedeutung verliert. Wie lautet der Regex, um trotzdem nach genau einem \ suchen?
``\\``

### F9: Matchen Sie Zeichenketten, die zwei Ziffern nebeneinander haben.
``\d\d``

### F10: Matchen Sie Zeichenketten, die 2 alphanumerische Zeichen enthalten, gefolgt von einem Leerraum.
``\w\w\s``

### F11: Matchen Sie zwei Ziffern gefolgt von einem Zeichen das keine Ziffer ist.
``\d\d\D``

### F12: Matchen Sie alle Uhrzeiten ("01:23", "17:49"). Ungültige Uhrzeiten wie "25:69" dürfen Sie dabei mit erwischen. Wie man das vermeidet, lernen wir später noch.
``\d\d:\d\d``

### F13: Der Text enthält zwei Telefonnummern. Überlegen Sie sich wie Sie beide Telefonnummern mit einem Regulären Ausdruck vollständig matchen können, ohne andere Textteile zu matchen. (Ihr Ausdruck kann aber nicht beliebige Telefonnummern finden. Auch dies lernen wir später.)
``\d\d\d[\s-]\d\d\d\d\d\d\d``

### F14: Matchen Sie jedes "A", das am Zeilenanfang steht.
``^A``

### F15: Matchen Sie jedes "!", das am Zeilenende steht.
``!$``