## F1: Erklären Sie die einzelnen Spalten dieses Eintrags. (user1:x:1002:1002::/home/user1:/bin/sh)
1. Benutzername: user1
2. Passwort: x
3. User-ID: 1002
4. Group-ID: 1002
5. GECOS-Feld: leer
6. Home-Verzeichnis: /home/user1
7. Login-Shell: /bin/sh

## F2 Charakterisieren Sie den Unterschied der Befehle useradd und adduser.
+ useradd:
	+ Low-Leve-Befehl aus 'passwd'
	+ Erstellt benutzer ohne viel Komfort
	+ Standard: kein Home-Verzeichnis
+ adduser:
	+ High-Level-Befehl in Ubuntu
	+ Fragt nach Passwort, Namen, Telefonnummer, etc.
	+ Legt automatisch Home-Verzeichnis an
	