### F1: Treffen Sie "Banana" mit mindestens zwei "na". ("Banana", "Banananana" aber nicht "Ba" oder "Bana")
``Ba(na){2,}``

### F2: Treffen Sie entweder "Hund" oder "Katze".
``Hund|Katze``

### F3: Treffen Sie Dateinamen mit Endung ".png" oder ".jpeg". Der Dateiname selbst sollte nur aus alphanumerischen Zeichen bestehen und darf beliebig lang sein.
``\w*(.png|.jpeg)``

### F4: Schreiben Sie eine Zeichenklasse, die alle Kleinbuchstaben von "a" bis "z" enthält.
``[a-z]``

### F5: Treffen Sie 5 Kleinbuchstaben hintereinander.
``[a-z]{5}``

### F6: Schreiben Sie eine Zeichenklasse, die alle kleingeschriebenen deutschen Vokale (samt "ä","ö","ü") trifft.
``[aeouiäöü]``

### F7: Schreiben Sie eine Zeichenklasse, die keine Großbuchstaben des deutschen Alphabets trifft.
``[^A-Z]``

### F8: Sie haben in re-Metazeichen bereits einen regulären Ausdruck geschrieben, um eine Uhrzeit (z. B. "12:59") zu matchen. Allerdings waren in dieser Lösung ungültige Uhrzeiten wie "25:01" oder "12:69" möglich. Überlegen Sie sich, wie Sie mit Zeichenklassen und Alternation einen regulären Ausdruck schreiben können, der nur gültige Uhrzeiten in diesem Format trifft.
``(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]``

### F9:  Schreiben Sie einen regulären Ausdruck, der ein Datum im Format DD.MM.YYYY erkennt.
``(0[1-9]|1[0-9]|2[0-9]|3[0-1])\.(0[1-9]|1[0-2])\.[1-9][0-9]{3}``

### F10: Schreiben Sie einen regulären Ausdruck, der gültige E-Mail-Adressen trifft.
``[\.\w\d\-_]*@[\w\d\-]*\.[\w]{2,}``

### F11: Schreiben Sie den gesuchten Ausdruck in möglichst knapper Form. Er muss der Art nach nur für Berlin und Brandenburg funktionieren, nicht auch für z.B. Hessen oder Niedersachsen
``(Berlin|Brandenburg): Die \1``