### F1: Unterschiede der Copy-Funktionen von Shutil
1. shutil.copyfile(src, dst)
	+ Kopiert nur den Dateiinhalt von 'src' nach 'dst'
	+ Metadaten werden nicht kopiert
2. shutil.copy(src, dst)
	+ kopiert den inhalt wie 'copyfile'
	+ Dateiberechtigungen werden übernommen
3. shutil.copy2(src, dst)
	+ wie 'copy' 
	+ Zusätzlich werden viele Metadaten übernommen
4. shutil.copyfileobj(fsrc, fdst)
	+ Kopiert den Inhalt zweier offener File-Objekte
	+ Anders als 'copyfile', weil mit Sockets und Pipes gearbeitet werden kann
5. shutil.copytree(src, dst)
	+ Kopiert ein komplettes Verzeichnis inkl. Unterverzeichnissen rekursiv
