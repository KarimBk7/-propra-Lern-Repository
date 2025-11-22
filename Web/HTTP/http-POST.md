### F1: Welche weiteren HTTP-Methoden gibt es neben GET und POST, und wofür werden sie typischerweise verwendet?
+ DELETE: Löscht Daten vom Server
+ PUT: Ändert alle Daten aus
+ PATCH: Ändert ein Teil der Daten

### F2: Erklären Sie den semantischen Unterschied zwischen GET und POST anhand eines konkreten Szenarios aus dem Alltag, das sowohl GET als auch POST enthält. Beschreiben Sie, warum die HTTP-Methode für den jeweiligen Zweck semantisch korrekt ist und was passieren würde, wenn man die falsche Methode verwendete.
+ GET: "Nur lesen" ohne Daten zu ändern
  + Szenario: Online-Produkt ansehen
+ POST: ist für Anfragen mit Datenänderungen auf dem Server
  + Bestellung im Onlineshop absenden


### F3: Recherchieren Sie, wann man die verschiedenen Content-Type-Varianten verwendet. Welche Vor- und Nachteile hat jede Variante? Wann würden Sie application/json statt application/x-www-form-urlencoded verwenden?
+ application/x-www-form-urlencoded:
  + Wann verwenden?:
    + Klassisches HTML-Formulare ohne JavaScript
    + Schlüsselpaar Daten
  + Vorteile: 
    + Von Browsern und Serverframeworks unterstützt
    + Geeignet für kleine Formulardaten
  + Nachteile
    + Nur Text, keine echten Binärdaten
    + Verschachtelte Datenstrukturen (umständlich)
+ application/json:
  + Wann verwenden?:
    + Kommunikation zwischen Frontend
    + Wenn Objekte (wie Arrays usw.) übertragen werden müssen
  + Vorteile: 
    + Unterstützt komplexe, verschahctelte Datenstrukturen
    + Gut lesbar
  + Nachteile:
    + Schicken nicht automatisch JSON
    + Server muss JSON explizit parsen
+ multipart/form-data:
  + Wann verwendet?:
    + Formular mit Datei-Uploads
    + Wenn Textfelder und eine oder mehrere Dateien gemeinsam übertagen werden sollen
  + Vorteile:
    + Unterstützt Binärdaten (Bilder, PDFs, usw.)
    + Mehrere Daten in einem Request möglich
  + Nachteile:
    + Deutlich mehr Protokoll-Overhead
    + Parsing auf Serverseite komplexer
    + Schwer lesbar

##### Wann application/json statt application/x-www-form-urlencoded?
+ Wenn die Daten komplex sind wie z.B. Objekte, Arrays, Listen, usw.
+ Wenn Frontend und Backend mit JSON arbeiten
+ Wenn man die Struktur klar versionieren und testen möchte