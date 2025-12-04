### F1: Welchen Nachteil kann es (je nach Testsuite) haben, nur das erste Versagen zu sehen?
+ Weniger Überblick, weil man denkt das weniger betroffen ist, obwohl vielleicht viel mehr betroffen ist
+ Man sieht Relationen in den Versagen schlechter.

### F2: Arbeiten Sie zum Debugging direkt mit dem Output des Komplett-Laufs oder beschaffen Sie sich mit einem zweiten Lauf zuvor einen kürzeren Output? Warum? Falls zweiter Lauf: Welches Kommando setzen Sie ein?
Ich würde einen zweiten Lauf machen und mir damit einen kürzeren, fokussierten Output holen. Der Komplett-Lauf ist zum Überblick, aber zum Debuggen unübersichtlich.

### F3: Welche Option von pytest finden Sie allgemein besonders clever? Warum?
+ Ich finde das makieren von Testfällen zum gruppieren sehr nützlich. 
+ Pytest merkt sich, welche Tests im letzten Lauf fehlschlagen, damit er nur diese durchläuft wenn man das will
+ Viele Möglichkeiten zeit zu sparen in den man die Ausgabe anpasst