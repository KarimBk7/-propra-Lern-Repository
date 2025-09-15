### F1: Geben Sie in eigenen Worten an, welche Berechtigungen die Datei hat: Wer darf was?.
+ Der Besitzer 'karim' darf lesen und schreiben
+ Die Gruppe 'karim' darf nur lesen
+ Alle anderen Benutzer dürfen nur lesen

### F2: Beschreiben Sie in Ihren Worten, was dieses Kommando macht: 'chmod -R 0754 dateiberechtigungsordner/ && sudo chown -R rechtenutzer:rechtenutzer dateiberechtigungsordner/'
1. Die Rechte werden rekursiv im Ordner 'dateiberechtigungsordner' geändert. Der Besitzer kann lesen, schreiben und ausführen. Die Gruppe kann lesen und ausführen. Andere nur lesen.
2. Und zusätzlich wird der Besitzer und die Gruppe rekursiv im gesamten Ordner auf 'rechtenutzer'geändert.