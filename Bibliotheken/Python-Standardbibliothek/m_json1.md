### F1 Wie werden Schlüssel-Wert-Paare in JSON dargestellt?
Sie werden mit einem Namen und einem Wert dargestellt, welche mit einem Doppelpunkt getrennt sind. Der Name ist hierbei immer innerhalb Anführungszeichen ("name": wert).

### F2 Welche Datentypen werden im JSON-Objekt verwendet?
Es werden Strings, Nummern, Objekte, Arrays, Bools und null verwendet.

### F3 Wie werden Zeichenketten in JSON notiert?
Zeichenketten werden innerhalb Anführungszeichen notiert ("Zeichenkette").

### F4 Wie werden Zahlen in JSON dargestellt?
Zahlen werden einfach ohne weiteres rechts vom Doppelpunkt eingetragen.

### F5 Wie werden boolesche Werte in JSON ausgedrückt?
Boolesche Werte werden einfach ohne weiteres rechts vom Doppelpunkt eingetragen.

### F6 Wie werden Arrays in JSON notiert?
Arrays werden mit eckigen Klammern notiert und deren einzelnen Elemente werden mit Kommas getrennt. Elemente werden wie sie üblicherweise eingetragen werden einfach an den belibigen stellen eingetragen.

### F7 Welche Regeln gelten für das Formatieren von JSON?
Daten sind in Name und Wert Paaren, Daten werden mit Kommas getrennt, geschweifte Klammern halten Objekte und eckige Klammern halten Arrays.

### F8: Warum wird JSON als 'leichtgewichtig' bezeichnet?
JSON wird als 'leichtgewichtig' bezeichnet, weil es nicht wie XML tags oder weitere Elemente benötigt. Dies verbessert die Leistungssteigerung in Datentransger und Datenverbrauch.

### F9 Was sind die wichtigsten Stärken und Schwächen im Vergleich der drei Notationen JSON, YAML und XML?
|JSON|YAML|XML|
|----|----|---|
|+ Einfach zu lesen|+ Einfach zu lesen|- Komplexer zu lesen|
|+ Schnell|+ Schnell|- Langsamer|
|- keine Namespaces|- keine Namespaces|+ hat Namespaces|

### F10 Wie kann man bei JSON Kommentare einbinden?
In JSON gibts es standardgemäß keine Kommentare die man einbinden kann. Manche erstellen Objekte, um Kommentare drin zu schreiben, aber diese werden bei der Datenverwaltung mitgelesen.