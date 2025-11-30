### F1: Diskutieren Sie: Ist jeder Defekt auf eine falsche Programmierung zurückzuführen?
Nein, da ein Defekt eine strukturelle Eigenschaft des Produkts ist. Ursachen könnten sein das fehlerhafte oder unklare Anforderungen aufgefasst wurden, Defekte in Testfällen oder defekte im Architektur-Dokument.

### F2: Wie realistisch ist es, ein komplexes Programm zu haben, dass keine Defekte hat?
So etwas ist nahezu unrealistisch, weil eine hohe Komplexität zu vielen möglichen Zuständen führt, die nicht vollständig getesten werden können. Außerdem können sich Anforderungen im Projektverlauf ändern oder sind garnicht erst vollstädnig zu begin. Und das alles während menschliche Fehler in den Entwicklungsphasen alles erschweren.

### F3: Warum folgt aus einem Fehler nicht zwangsläufig ein Defekt? Beschreiben Sie ein Beispiel.
Ein Fehler führt nur dann zu einem Defekt, wenn sein Ergebnis in das Produkt einfließt und dort bestehen bleibt. 

### F4: Gegeben eine Anwendung, die sowohl auf Windows als auch auf Linux lauffähig ist. Sie beobachten ein wiederholbares Versagen, das nur auf einer Plattform auftritt, aber nicht auf der anderen. Recherchieren Sie einen typischen Grund, wie so etwas zustandekommt.
Ein typischer Grund sind Unterschiede im Dateisystem z.B. das Behandeln von Groß-/Kleinschreibung in Dateinamen (windows ist meist ``case-insensitive`` während Linux ``case-sensitive`` ist), unterschiedliche Pfadtrennzeichen (``/`` und ``\``) als auch unterschiedliche Zeilenenden (``CRLF`` und ``LF``).

### F5: Sind alle Akzeptanzkriterien im interaktiven manuellen Test praktikabel überprüfbar? Wenn nein, formulieren Sie das Akzeptanzkriterium inhaltlich so um, dass das möglich wird.
Alle Akzeptanzkriterien bis auf eines sind direkt in einem interaktiven Test praktikabel überprüfbar. <br>
Das Problem liegt bei der fünften Akzeptanzkriterie. Die Bedingung "für 24 Stunden" ist in einem interaktiven manuellen Test nicht praktikabel, weil man nicht real 24 Stunden wartet.<br><br>
**Umformulierung**:
„Das System sperrt das Konto nach drei aufeinanderfolgenden fehlgeschlagenen Anmeldeversuchen und zeigt die Sperrdauer an, die bis zu einem Zeitpunkt 24 Stunden nach dem dritten Fehlversuch reicht.“<br><br>
Somit kann man im Test überprüfen, ob der angezeigte Sperr-Endzeitpunkt korrekt ist, ohne 24 Stunden warten zu müssen.

### F6: Welche der folgenden Szenarios (Testszenario) beschreiben in Bezug auf obige Akzeptanzkriterien ein Versagen?
Versagen treten in S4 und S5 auf.<br>
+ S4: Valide E-Mail + gültiges Passwort → Weiterleitung auf Admin-Seite
  + Verletzung von AK6 (Weiterleitung muss auf die Nutzer-Profilseite gehen) → Versagen.
+ S5: Valide E-Mail + gültiges Passwort → Weiterleitung auf Profilseite erst eine Stunde später.
  + AK6 impliziert eine unmittelbare Weiterleitung nach erfolgreicher Anmeldung; eine Stunde Verzögerung erfüllt das Kriterium nicht → Versagen.

### F7: Ergänzen Sie mindestens ein weiteres Akzeptanzkriterium, damit es für das letzte Szenario keine Meinungsverschiedenheiten mehr geben kann.
„Nach erfolgreicher Anmeldung wird der Nutzer unmittelbar (nach paar Sekunden) auf die Nutzer-Profilseite weitergeleitet.“

### F8: Erstellen Sie zu einem der oben entdeckten Versagen einen konkreten und genauen Problembericht.
**Versagen aus S4:** Weiterleitung auf Admin-Seite statt Profilseite.

### F9: Was würden Sie tun, wenn Sie 2 Problemberichte bekommen, die wahrscheinlich vom selben Defekt handeln, aber unterschiedlich gut beschrieben sind?