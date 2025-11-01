### F1: Was bedeutet es, wenn eine Shell nicht interaktiv ist (BR 1.2)?
Führt Befehle aus einer Datei oder einem String aus und har keine direkte Interaktion.

### F2: Was bedeutet es, wenn Kommandos asynchron ausgeführt werden (BR 1.2)?
Asynchrone Ausführung bedeutet, dass eine Kommando im Hintergrund läuft und die Shell nicht drauf wartet, bevor sie mit dem nächsten Befehl weitermacht.

### F3: Was vermuten Sie, welche zwei dieser Kommandos Sie am häufigsten verwenden werden? Warum glauben Sie das?
+ grep 
	+ weil es praktisch ist relevante Information aus langen Ausgaben oder sonstigen zu erhalten
+ less
	+ für systeme ohne IDE bzw. Texteditor ist das lesen damit einfacher

### F4: Beschreiben Sie sprachlich welche Dateien das Argument ```~/*/process_*.{py,txt}``` erfasst (BR 3.5.1, BR 3.5.2, BR 3.5.8).
Das Argument erfasst alle Dateien in direkten Unterverzeichnissen des Home-Verzeichnisses, dessen Name mit "process_" beginnt und auf .py pder .txt endet.

### F5: Wie lautet das aus drei Kommandos zusammengesetzte Kommando, mit dem man sich erst für die zwei obigen Pfade je eine Variable definiert und dann mit deren Hilfe das cp-Kommando verkürzt ausdrückt? (BR 3.2.4, BR 3.4)
```SRC="<PFAD_ZUR_QUELLE>"; DST="<PFAD_ZUM_ZIEL>"; cp -- "$SRC" "$DST"```

### F6: Wenn es um das Wechseln zwischen Verzeichnissen geht, geht es manchmal sogar noch bequemer: Wie setzt man die Shellvariable CDPATH so, dass man anschließend anstelle von cd /my/other/also/not/exactly/short/path2/subdir schreiben kann cd subdir (BR 5.1)?
```export CDPATH=.:~:/my/other/also/not/exactly/short/path2``` <br>
```cd subdir```

### F7: Schreiben Sie eine einzeilige Shellfunktion pyimports, die das obige grep|wc-Kommando so umsetzt, dass das erste Argument an die Stelle von "re" tritt.
```pyimports() { grep -r -P --include '*.py' "^import $1" . | wc -l; }```

### F8: Definieren Sie für Ihre eigenen Zwecke (z.B. des ProPra) praktische Shellvariablen, Aliase und ggf. Shellfunktionen und legen Sie sie in ~/.bash_profile und/oder ~/.bashrc ab; mindestens eine Pfad-Shellvariable und die pyimports-Shellfunktion. Nehmen Sie sich vor, diese Hilfen ständig zu ergänzen und zu verbessern (und irgendwann veraltete auch wieder rauszuwerfen).
``pyimports() { grep -r -P --include '*.py' "^import $1" . | wc -l; }``<br>

### F9: Geben Sie ihren PATH an, wie er mit echo $PATH ausgegeben wird. Nein, besser: Wie er mit echo $PATH | perl -pe "s/:/\n/g" | sort ausgegeben wird. (Oh, vielleicht sollte der hintere Teil ein Alias werden?)
``alias showpath='printf "%s\n" "${PATH//:/$'\''\n'\''}"'``

### F10: Schauen Sie sich die Einzelteile ihres PATH an. Welcher davon ist am ehesten verzichtbar?

### F11: Probieren Sie which aus für die Kommandos grep, man, cd, which, command und pyimports. Dann das Gleiche mit command -v. Dann das Gleiche mit command -V. Welche Variante wollen Sie sich angewöhnen? Warum?
Ich gewöhne mir ``command -v`` an ,weil es standardisiert ist und auch Aliase, Shell-Builtins und Funktionen korrekt erkennt, während ``which`` nur ausführbare Datein im ``PATH`` erkennt.