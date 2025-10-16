### F1: Unter welchen Umständen kann man einen korrekt funktionierenden Server, der ssh anbietet, mit ```ping``` erreichen, aber nicht mit ```ssh```?
Das liegt daran das Ping und SSH verschieden behandelt werden.
Ping nutzt ICMP und SSH nutzt TCP/22. Daher kann der Kernel auf ICMP-Echos antworten, obwohl ssh nicht lauscht oder der falsche Port konfiguriert ist.<br>
Außerdem lassen Firewalls ICMP durch, aber filtern TCP/22 oder leiten sie falsch. Das bewirkt das der Server per Ping und nicht per SSH erreichbar ist.

### F2: Charakterisieren Sie grob den wichtigsten Unterschied zwischen dig und host aus Aufrufersicht.
Host ist ein einfaches Werkzeug mit knapper Ausgabe für Abfragen. Es ist schnekk, aber bietet wenige Optionen.<br>
Dig ist ein Diagnose- und Debug-Tool, welches detaillierte Ausgaben liefert und Kontrolle über Query-Typen, Flags, EDNS, usw. anzeigt.