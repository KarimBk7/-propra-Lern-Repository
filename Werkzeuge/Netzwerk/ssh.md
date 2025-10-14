### F1: Was wären mögliche Gründe, wenn Ihnen das System meldet, dass sich der host_key des entfernten Rechners geändert hat? Nennen Sie zwei Beispiele.
+ Der entfernte Rechner wurde neu installiert
+ Der Host-Key wurde geändert

### F2: Beschreiben Sie kurz, was sich geändert hat.
Ich konnte nun ohne der Eingabe meines Passwort und nur mit der verwendung der SSH-Key's in die Andorra-Server gelangen.

### F3: Was hat sich geändert?
Statt den Passphrase nach jeder SSH verbindung einzugeben, tut dies der ssh-agent nachdem man einmal die Passphrase bei ssh-add eingegeben hat.