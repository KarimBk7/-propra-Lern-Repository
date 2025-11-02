### F1: Warum ist die Fehlermeldung trotz der Umlenkung auf dem Terminal erschienen? Zitieren Sie 1-2 Sätze (mit Quellenangabe) aus einer auf dieser Seite bereits erwähnten Referenzdokumentation als Beleg für Ihre Behauptung.
Die Meldung kam trotzdem aufs Terminal, weil ``>`` nur stdout umleitet. stderr bleibt unverändert am Terminal. Um beides umzzleiten, müsste man ``> /tmp/out 2>&1`` verwenden.

+ „Redirecting output opens the file … for writing on file descriptor n, or the standard output (file descriptor 1) if n is not specified.“
+ Von: https://man7.org/linux/man-pages/man1/bash.1.html


### F2: Wie lautet das zweite grep-Kommando, wenn man es so erweitert, dass auch die Fehlermeldung umgelenkt wird und dann in /tmp/err landet?
``grep partner_ student.yaml diesedateigibtesnicht > /tmp/out 2> /tmp/err``

### F3: Angenommen, Sie machen anschließend noch grep _name student.yaml > /tmp/out, wieviele Zeilen stehen dann in /tmp/out (BR 3.6)? Warum? Mit welcher kleinen Änderung des Kommandos kann man den gesamten Output erhalten?
in ``/tmp/out`` stehen nur die Zeilen des zweiten Greps und nichts vom vorherigen Lauf, weil ``>`` die Zieldatei vor der Ausgabe leert.

### F4: Was bedeutet das && in dem Kommando? (BR 3.2.4)
Das ``&&`` in einem SHell-Kommanod bedeutet dass das zweite Kommanod nur ausgeführt wird, wenn das erste erfolgreich war.

### F5: Warum benutzt man stattdessen nicht einfach ;?
Mit ``;`` werden beide Kommandos immer nacheinander ausgeführt. Und dies unabhängig davon ob das erste erfolgreich war oder nicht.

### F6: Was bedeuten die Klammern (BR 3.2.5)? ``(cd subdir; grep somestuff *.md)``
Die Klammern starten die enthaltene Befehlsliste in einem Subshell. Änderungen wirken nur dort und gehen nach Ende Verloren.

### F7: In welchem Verzeichnis befinden Sie sich anschließend (BR 4.1)? Unter welchen Umständen sparen Sie im obigen Fall ein ganzes Kommando ein?
Nach Ausführen befindet man sich weiterhin im ursprünglichen Verzeichnis, weil der Befehl nur im Subshell läuft. Wenn man die Klammern weglässt, dann läuft beides in der gleichen Shell, und man muss nicht erst ``cd subdir`` ausführen.

### F8: Wie können Sie jetzt eine Liste der aktuellen Hintergrundjobs anzeigen? (BR 7.2)
Mit ``jobs`` kann man alle Prozesse, die von der aktuellen Shell gestartet wurden und sich im Hintergrund oder im angehaltenene Zustand befinden anzeigen lassen. 

### F9: Wie stoppen Sie nun den ersten dieser beiden Hintergrundjobs (nur stoppen, nicht abbrechen)?
``kill -STOP %1``