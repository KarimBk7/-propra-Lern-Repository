### F1: Wie startet man das Debugging? (VSCode)
1. Links Breakingpoints an den Zeilen erstellen (per Klick)
2. Dann links auf ``Run and Debug`` klicken oder ``f5`` drücken.

### F2: Was ist ein Breakpoint und welche Eigenschaften können Sie daran verändern?
Ein Breakpoint ist eine Markierung an einer Codezeile, bei der der Debugger die Programmausführung anhält, bevor die Zeile selbst ausgeführt wird. <br>
**Eigenschaften**:
+ Aktiv/Deaktiviert
+ Bedingung: Anhalten wenn Ausdruck war ist
+ Hit Count: Anhalten bei n-ten Erreichen
+ Logmessage: Nicht anhalten, aber beim Erreichen eine Nachricht ausgeben

### F3: Wie können Sie einen Breakpoint zu einem Conditional Breakpoint machen?
1. Rechtsklick auf den Breakpoint
2. Auf ``Edit Breakpoint`` klicken
3. Condition eintragen

### F4: Was sind Ihrer Einschätzung nach die 5 wichtigsten Funktionen des Debuggers? Erklären Sie kurz, was diese Funktionen genau machen.
1. **Breakpoints**: Die verschiedenen Eigenschaften die Breakpoints haben können scheinen, um diese unterschiedlich zu behandeln sind für mich am wichtigsten
2. **Locals und Globals**: Das Anzeigen der Werte von Variablen und Objekte, wenn man mittem im Debuggen ist (links in der Spalte ``Locals`` und ``Globals``)
3. **Call Stack**: Zeigt Verlauf der Funktionsaufrufe, die zum aktuellen Zustand geführt haben
4. **Watch**: Bewertet gewählte Ausdrücke wie ``len(arr)`` oder einfach nur einezelne Variabeln (``x``)
5. **Step-Knöpfe**: Ablauf der Funktion steuern wie bei ``pdb`` mit next, continue, step und return.

### F5: Als wie nützlich empfinden Sie den grafischen Debugger? Was gefällt Ihnen gut (insbesondere im Vergleich zu py-pdb), was schlecht?
Ich finde den grafischen Debugger auf jedenfall viel Ansprechender als ``pdb``. Es fühlt sich gleich einfacher an alles zu sehen, Breakpoints einfacher verwalten zu können, etc. <br>
Kurz gesagt: Alles ist auf einen Blicke ohne ständig hoch und runter zu scrollen oder ständig ``l`` zu drücken wie bei pdb.
Was schlecht ist fällt im Vergleich zu pdb jetzt nicht sofort ein.