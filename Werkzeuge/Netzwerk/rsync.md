### F1: Was ist der Unterschied im Verhalten der beiden Kommandos?
Das erste Kommando kopiert das Verzeichnis und den Inhalt in das Zielverzeichnis und das zweite Kommande kopiert nur den Inhalt des Ordners in das Zielverzeichnis.

### F2: Wie stellt rsync sicher, dass nur geänderte Dateien erneut kopiert werden?
``rsync`` vergleicht Dateigröße und mtime und nur wenn eine Datei sich darin unterschediet, wird sie erneut übertragen.

### F3: Welche zwei wichtigsten Unterschiede gibt es zwischen der Verwendung von rsync und anderen Kopierbefehlen wie cp?
1. ``rsync`` überträgt nur Änderungen (nur geänderte Teile/Dateien)
2. ``rsync`` unterstützt Netzwerksynchronisation über SSH.

### F4: Wie könnten Sie (theoretisch; praktisch ist das nicht relevant) mit rsync überprüfen, ob die Synchronisation tatsächlich alle Änderungen übernommen hat, ohne das Kopieren zu wiederholen?
Durch einen ``Dry-Run``, der nur vergleicht und nichts überträgt.