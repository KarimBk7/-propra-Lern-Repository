root@DESKTOP-J4GQQ0C/mnt/c/Users/abdil/ws/propra/Bibliotheken/Python-Standardbibliothek $ python argparsetest.py -b Banane enanaB
Das ist eine Test-Config-Datei fuer die Aufgabe 'argparsetest.py'-Aufgabe.

Maxdepth ist 1

Batch-Files:
Banane
enanaB

root@DESKTOP-J4GQQ0C/mnt/c/Users/abdil/ws/propra/Bibliotheken/Python-Standardbibliothek $ python argparsetest.py -m 42 -c imaginaeresFile.txt
Inhalt einer temprären Datein um '-c' zu veranschaulichen.

Maxdepth ist 42

root@DESKTOP-J4GQQ0C/mnt/c/Users/abdil/ws/propra/Bibliotheken/Python-Standardbibliothek $ python argparsetest.py -m
usage: argparsetest.py [-h] [-c CONFIG] [-m MAXDEPTH] [-b BATCH [BATCH ...]]
argparsetest.py: error: argument -m/--maxdepth/--depth: expected one argument

root@DESKTOP-J4GQQ0C/mnt/c/Users/abdil/ws/propra/Bibliotheken/Python-Standardbibliothek $ python argparsetest.py -b -c
usage: argparsetest.py [-h] [-c CONFIG] [-m MAXDEPTH] [-b BATCH [BATCH ...]]
argparsetest.py: error: argument -b/--batch: expected at least one argument




