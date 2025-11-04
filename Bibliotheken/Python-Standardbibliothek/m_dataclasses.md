### F1: Welche Methoden werden automatisch erzeugt, wenn eine Klasse mit ``@dataclass(order=True)`` dekoriert wird?
Die Methoden  ``__eq()__``, ``__repr()__``, ``__init()__``, ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` werden erstellt.

### F2: Beschreiben Sie einen konkreten Zweck und Fall, für den Sie künftig ``dataclass`` anstatt ``dict`` einsetzen werden und warum.
Wenn ich komplexere Datentypen brauche, um Algorithmen im Zussamenhang mit diesen zu erstellen die womöglich mit ``dict`` schwerer wären zu implementieren.