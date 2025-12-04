### F1: Welchen Nachteil hätte es, wenn man nicht pytest.mark.parametrize benutzen würde, sondern in der Testfunktion eine Schleife macht, um deren Einträge zu durchlaufen?
Man würde nicht genau sehen welcher der Tests genau fehlgeschlagen ist. Außerdem hat es eine schlechtere Integration mit pytest-Features die man aus Task ``pytest_call`` gelernt hat.


### F2: Kann man eine solche pytest.mark.parametrize-Tabelle aus einer Datei einlesen? Wie würde so ein Konstrukt gebaut?
Man könnte dies entweder mit einer ``CSV-Datei`` machen oder mit einer ``JSON-Datei``, um Tests einzulesen. 
