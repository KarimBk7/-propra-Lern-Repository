### F1: Beschreiben Sie kurz in eigenen Worten, welchen Hauptvorteil sich Bell davon verspricht, nicht das spezialisierte Werkzeug "Debugger", sondern die print()-Ausdrücke zum Finden von Defekten zu benutzen.
Bell erwartet als Hauptvorteil, dass man ohne Debugger stärker gezwungen ist  den Programm ablauf aktiv im Kopf zu verstehen, Annahmen zu formulieren und zu prüfen. Und damit sein eigenes Verständnis des Codes zu vertiefen.


### F2: Welchen anderen Vorteil hat es in Python? Wie würde sich die Erwägung in einer statisch typisierten Sprache wie Java, Scala, Rust oder Go verändern?
``print()`` lässt sich in Python mit fast alles Datenstrukturen verwenden, so das man die Variabeln in der Konsole sieht.<br>
Bei anderen Sprachen kann es etwas umständlicher sein, da man da ständig ``rebuilden`` oder ``compilieren`` muss.


### F3: Es gibt Situationen, in denen die Verwendung eines Debuggers technisch schwierig ist, etwa bei einem verteilten System. Es gibt andere, wo die Verwendung von print()-Ausdrücken erschwert ist. Unter welchen Umständen bevorzugen Sie print()?
Angenommen mir ist der Fluss des Codes unklar oder der Zustand ist zu komplex dann würde ich eher den Debugger bevorzugen.<br>
Und print() würde ich verwenden, falls ich genau weis in welchem Bereich des Program mein Fehler liegt und ich einen guten einblicke und Kenntniss über den Code habe.

### F4: Beschreiben Sie Ihre Erfahrungen mit mindestens zwei der von Johnson beschriebenen Hilfsmittel, die Sie weiter einsetzen möchten.
+ Ich habe gute Erfahrungen mit dem verwendung von ``f-strings`` und ``=`` gemacht, welche ich auch schon vorher in meinen eigenen Debugging-Sesions intuitiv verwendet habe.
+ Mit ``pprint()`` lassen sich Ausgabe lesbarer ausgeben, was bei komplexeren Datenstrukturen hilfreich ist
+ Die ``locals()``-Funktion kannte ich vorher nicht, weshalb ich die Variabeln immer einzeln in die ``print()``-Funktion abgetippt habe. Diese Funktion werde ich definitiv zukünftig nutzen wollen.


### F5: Beschreiben Sie ggf. für mindestens eines der von Johnson beschriebenen Hilfsmittel, warum Sie es voraussichtlich nicht einsetzen möchten.
Mir gefällt die ``pprint()``-Funktion mehr als die ``rprint()``, weshalb ich die ``rptint()``-Funktion nicht verwenden werde.

### F6: Sind Sie in der Lage mit private versteckte Inhalte mittels print()-Ausdrücken anzuzeigen? Welche Voraussetzungen müssen hierfür erfüllt sein?
Wenn der ``print()`` in einem Codeabschnitt steht der Zugriffsrechte auf diese private-variable hat, dann kann er diesen Ausgeben (z.B. innerhalb der selben Klasse). <br>
Man könnte auch für die Klassen eine Methode erstellen die genau diese Prints ausgeben.