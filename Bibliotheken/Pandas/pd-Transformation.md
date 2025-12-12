### F1: Können Sie max() auf eine Spalte mittels apply() anwenden, um das Maximum der Spalte zu bestimmen? Begründen Sie.
Nein, weil die Funktion die über ``apply()`` übergeben wird, bei jedem Element in der Spalte verwendet werden. Das heißt das jedes Element alleine in der ``max()`` sein wird.


### F2: Wenden Sie max() mittels apply() auf das ganze erststimmen_df an. Was passiert, wenn Sie apply() auf ein DataFrame statt auf eine Series anwenden? Beschreiben Sie die Rückgabe.
Es wird von jeder Spalte das jeweils größte Element ausgegeben.w



### F3: Was berechnet max() im folgenden Beispiel? Wie ist x in dem Fall aufgebaut?
Es berechnet den maximalen Wert jeder Zeile mit den jeweiligen Elementen in Spalte SPD, CDU und AFD. ``x`` ist in dem Fall eine Zeile.



### F4: Für die hier besprochenen Beispiele von apply() könnte man apply() ohne sonstige Änderungen durch map() ersetzen. Das ist aber erstens weniger klar (und deshalb nicht zu empfehlen) und funktioniert zweitens in komplizierteren Fällen nicht mehr. Erklären Sie den Unterschied zwischen map() und apply() in Bezug auf ihre typische Verwendung. Wann ist map() ausreichend, wann braucht man apply()?
Die Funktion ``map()`` ist eine Methode von Series, nicht von DataFrames. Wird verwendet, um einzelne Spalten zu verwalten.<br>
Die Funktion ``appply()`` funktioniert für Series und DataFrame, wobei es bei Series wie die Funktion ``map()`` funktioniert und bei DataFrames auf ganze Zeilen oder Spalten.