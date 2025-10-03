### F1: Fassen Sie die fünf Hauptpunkte in eigenen Worten in je einem Satz zusammen.

1. Git speichert bei jedem Commit einen Schnappschuss des Projekt-Dateisystems
2. Weil man die gesamte Historie lokal hat, brauchen viele Befehle keine Netzwerkverbindung, welches git offline nutzbar macht.
3. Alles was Git speichert, wird vor dem Ablegen gehasht, damit Git veränderungen in Datein erkennt
4. Die meisten Aktionen in Git fügen dem Datenbank-Verlauf neue Objekte hinzu. Gelöschte Datein bleiben oft noch rekonstruierbar.
5. Die drei Zustände 'modified', 'staged' und 'commited' helfen einen den Überblick im Projekt zu behbalten.

### F2: Wenn man eine Datei so ändert, dass ihre Größe und ihr Zeitstempel gleich bleiben, woran kann git trotzdem feststellen, dass sie geändert wurde?
Git erkennt Änderungen nicht nur über Größe und Zeitstempel der Datei sondern auch über dessen Inhalt.

### F3: Warum kann man git auch unterwegs oder ohne Internet gut benutzen?
Man hat die ganze Historie lokal, viele Operationen sind lokal ausfühbar, man lann Änderung commiten und später pushen.

### F4: Warum gehen viele Operationen in git so schnell?
Keine Netzwerk-Latenz durch viele lokale Git-Operationen. Git führt Datei-Statistiken und Hashes als Cache. Git muss Inhalt jeder Datei nicht vergleichen, sondern vergleicht Hashes, um festzustellen ob diese verändert wurden. 

### F5: In welchen drei Punkten lässt sich der Git workflow einfach zusammenfassen?
1. Im Projekt Arbeiten: Datein erstellen, ändern, etc.
2. Vorbereiten: Welche Änderungen werden hinzugefügt und commited
3. Synchronisieren: Online hochladen