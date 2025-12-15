### F1: Was passiert, wenn die Funktion nil als Parameter bekommt?
Es entsteht ein ``panic: runtime error`` mit invalid memory adress or nil pointer dereference.

### F2: Beschreiben Sie mit eigenen Worten, warum a im folgenden Beispiel nicht verändert wird, b aber sehr wohl.
Die Funktion ``change()`` bekommt den Wert übergeben und nicht die Adresse, weshalb das ändern der Variable innerhlab der Funktion nicht die Variable in der Urpsrungsfunbktion verändert. <br>
Die Funktion ``changePointer`` erhält jedoch die Speicheradresse der Variable, was dazu führt das es den neuen Wert in den selben Speicherort der Urpsrungsvariable rein schreibt.

### F3: Was wird im folgenden Beispiel auf die Kommandozeile ausgegeben? Warum?
In der Konsole wird die Adresse der Variable ``x`` ausgegeben.