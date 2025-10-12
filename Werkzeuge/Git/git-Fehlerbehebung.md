### F1: Wird hier wirklich ein bestehender Commit modifiziert? Wenn nein, was passiert stattdessen?
Nein der bestehende Commit wird nicht modifiziert. <br>
Git erstellt einene neuen Commit, der beide Momentaufnahmen enthält. Der Branch-zeiger wird vom alten Commit auf den neuen Commit verschoben.


### F2: Wir setzen mit unseren Befehlen die Datei im Arbeitsverzeichnis auf einen vorherigen Zustand zurück. Was passiert dabei mit dem zweiten Commit?
Der zweite falsche Commit bleibt erhalten, weil man mit ```git restore``` ändert man nur das Arbeitsverzeichnis. Der Commit ist weiterhin Teil der History.