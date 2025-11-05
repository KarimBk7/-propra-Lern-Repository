### F1: Was ist der wichtigste Unterschied zwischen Copyleft-Lizenzen und freizügigen ("permissive") Lizenzen?
Copyleft erlaubt Nutzung nur, wenn abgeleite Werke unter derselben Lizenz veröffentlicht werden.<br>
Permissive Lizenzen erlauben fast alles, auch proprietäre Weitergabe.

### F2: Warum sind manche Creative Commons-Lizenzen keine Open-Source-Lizenzen?
Weil sie die Open-Source-Definition verletzen wie NC oder ND

### F3: Was ist der wichtigste Unterschied zwischen der MIT-Lizenz und Public Domain?
MIT ist eine Lizenz die Nutzung, Änderung, Weitergabe mit Copyright-Hinweisen enthält.<br>
Public Domain ist eine Rechtsfreigabe die keine Auflagen oder Pflicht zur Namensnennung hat.

### F4: Wie findet man (üblicherweise) heraus, welche Lizenz eine Open-Source-Bibliothek hat?
Im Repo nach LICENSE oder COPYING im root schauen.

### F5: Welche Open-Source-Lizenz wählen Sie? Warum?
Meine Wahl würde unter Apache-2.0 fallen, das es weit verbreitet ist, Patentsicher und Kompatibel ist mit GPLv3 und anderen gägngigen OSS-Stacks.

### F6: Beschreiben Sie, was Sie bei der Benutzung von XY beachten müssen, wenn Sie die nachfolgenden Fälle vorfinden. Besprechen Sie dabei insbesondere, wann Sie für die Verwendung von XY ihre Lizenz für B ändern müssten. Können Sie sie dann auch tatsächlich ändern? Wollen Sie?
+ XY referenziert keine Lizenz.
  + Ohne Lizenz darf man es nicht kopieren oder verbreiten
  + B darf XY nicht verwenden/ bündeln
  + Lizenzänderung für B? Nicht möglich/sinnvoll. Brauchen erst eine Lizenz für XY.
+ XY unterliegt der MIT-Lizenz.
  + Kompatibel mit Apache-2.0. Sie können XY als Abhängigkeit nutzen oder „vendorn“.
  + Lizenzänderung für B? Nein. B kann Apache-2.0 bleiben.
+ XY unterliegt der GNU GPLv3-Lizenz.
  + Wenn B XY erfordert und ich B zusammen mit XY oder als untrennbar verknüpftes Werk verbreite, muss ich B unter GPLv3 lizensieren
  + Lizenzänderung für B? Ja, falls enge Kopplung/Distribution mit XY; sonst vermeiden.
+ XY unterliegt der Apache Lizenz 2.0.
  + Voll kompatibel mit B (Apache-2.0)
  + Lizenzänderung für B? Nein. B kann Apache-2.0 bleiben.