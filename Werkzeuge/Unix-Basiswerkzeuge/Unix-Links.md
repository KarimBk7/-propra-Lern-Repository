### F1: Vergleichen Sie die Inodes von hardlink und harddata.



### F2: Funktioniert der Symlink ``symlink1`` noch? Wenn ja, warum? Wenn nein, warum nicht?
Ja, der Simlink funktioniert noch, weil dieser den absoluten Pfad der ``softdata`` hat. Dies bedeuted das es von egal wo zugriff auf die ``softdata`` hat. 

### F3: Funktioniert der Symlink ``symlink2`` noch? Wenn ja, warum? Wenn nein, warum nicht?
Nein, der relative Pfad ist abhängig vom Standort des Symlinks ist. Und der gespeicherte relative Pfad würde ins falsche Verzeichnis eingreifen von ``/tmp/``

### F4: Funktioniert der Hardlink hardlink noch? Wenn ja, warum? Wenn nein, warum nicht?
Ja, weil der Hardlikn den absoluten Pfad gespeichert hat und von überall aus funktioniert.

### F5: Funktioniert der Symlink ``symlink1`` noch? Wenn ja, warum? Wenn nein, warum nicht?
Nein, weil der absolute Pfad nicht mehr mit dem Pfad der ``softdata`` übereinstimmt.

### F6: Funktioniert der Hardlink hardlink noch? Wenn ja, warum? Wenn nein, warum nicht?
Ja, weil ein Hardlink auf die Inode der Datei verweist und nicht auf den Datei-Pfad selber.

### F7: Funktionieren die Symlinks unter ~/ws/tmp/links noch? Wenn ja, warum? Wenn nein, warum nicht?
Nein, weil der Symlink nur aud den Pfadnamen verweist und dieser nicht mehr vorhanden ist.

### F8: Funktioniert der Hardlink hardlink noch? Wenn ja, warum? Wenn nein, warum nicht?
Ja, weil Hardlinks auf die Inode verweisen und nicht auf den Pfad. Die Datei ist noch auf der Festplatte vorhanden.

### F9: Welche Art von Links würden Sie bei Desktopsymbolen nutzen? Begründen Sie.
Hardlinks, aufgrund der zuverlässigkeit und flexibilität. Der User kann seine Programme oder Daten beliebig verschieben und der Hardlink weis wo es ist.

### F10: Welche Art von Links würden Sie nutzen, falls Sie schneller auf einen Ordner zugreifen möchten, der tief im Ordnerbaum des Systems ist? Begründen Sie.
Hardlink.

### F11: Welche Art von Links würden Sie bei Backups nutzen? Begründen Sie.
Hardlink, weil diese dafür sorgen das etwas erst gelöscht wird, wenn auch der Hardlink selber verschwindet