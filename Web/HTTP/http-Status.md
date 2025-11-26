### F1: In welchen Situationen würde ein Server den Statuscode 100 Continue senden? Beschreiben Sie ein typisches Szenario und erklären Sie, warum dieser Code nützlich ist.
**Szenario**: Der Client will ein großen Request-Body senden (z.B. Post). Als nächstes sendet der Client nur die Request-Header inklusive ``Except: 100-continue``. Der Server prüft in den Headers, ob die Anfrage Akzeptabel ist und antwortet mit ``100-continue``. Damit signalisiert der Server das alles gut ist und bittet  um den ``Body``. Erst dann sendet der Client den eigentlichen Body.<br>
**Nutzen**: Vermeidet Übertragung großer Bodies, wenn Anfrage wegen Header-Problemen sowieso abgelehnt würde und reduziert unnötige Last auf Client und Server.

### F2: Welcher Unterschied besteht zwischen den Statuscodes 200 OK und 204 No Content? Wann würde man jeden der beiden verwenden? Geben Sie konkrete Beispiele.
+ ``200 OK``: Erfolgreiche Anfrage + es wird eine Antwort mit Inhalt zurückgegeben.
  + Bsp.: Server antortet mit JSON-Daten des Profils und dem Status 200
+ ``204 No Content``: Erfolgreiche Anfrage, aber kein Inhalt im Response-Body
  + Bsp.: Ressource gelöscht, Server braucht nichts zurücksenden.

### F3: Erklären Sie die subtilen Unterschiede zwischen 301 Moved Permanently, 302 Found und 303 See Other. Warum ist diese Unterscheidung in der Praxis wichtig?
+ ``301 Moved Permanently``: Die Ressource ist dauerhaft verschoben. Die neue URL sollte künftig verwendet werden. Suchmaschinen aktualisieren Ihren Index (Ersetzen alte URLs)
+ ``302 Found``: Ressource liegt vorrübergehend unter anderer URL, aber die ursprüngliche URL bleibt gültig. 
+ ``303 See Other``: Wird meist nach einer POST-Request verwendet. Der Client soll eine GET-Anfrage an die neue URL senden, damit der POST bei Reload nicht erneut abgeshickt wird.
+ ``Wichtigkeit``: Untershied beinflusst Caching, Linkpersistenz, Suchmaschinenindexierung und wie Clients weiter verfahren.

### F4: Erklären Sie den Unterschied zwischen 301 Moved Permanently und 308 Permanent Redirect. Warum wurden die neuen 307/308-Codes eingeführt?
+ ``301 Moved Permanently`` erlaubt dem CLient, die HTTP-Methode zu ändern (z.B. von POST zu GET).
+ ``308 Permanent Redirect``: bedeutet ebenfalls permanente Umleitung, aber HTTP-Methode und Body bleiben erhalten.
+ ``Warum 307/308-Codes ausgeführt``: Um sich Umleitungen zu ermöglichen, bei denen POST-Requests oder andere Methoden nicht in GET umgewandelt werden.

### F5: Sie entwickeln eine Web-API und ein Client sendet einen POST-Request an einen Endpunkt, der nur GET-Requests akzeptiert. Welchen Statuscode sollten Sie zurückgeben?
Passend wäre ``405 Method Not Allowed`` . Die HTTP-Methode (POST) ist für die Ressource nicht erlaubt.<br>
Man könnte auch ``501 Not Implemented``, wenn der Server die Methode gar nicht unterstützt, aber 405 ist präziser, da der Endpunkt existiert.

### F6: Ein Client überschreitet das Rate Limit (erlaubte Anzahl von Anfragen pro Zeiteinheit, z.B. 20 Requests pro Minute) Ihrer API. Welcher Statuscode ist angemessen?
Angemessen wäre ``429 Too Many Requests`` für Rate-Limiting bzw. zu viele Anfragen in kurzer Zeit.


### F7: Ein Webserver ist aufgrund eines Festplattendefekts nicht verfügbar. Welchen Statuscode sollte er zurückgeben?
**Passend**: ``503 Service Unavailable``. Server kann aktuell nicht liefern, wegen Wartung, Überlastung oder technischer Probleme.<br>

### F8: Stellen Sie sich vor, Sie betreiben einen Online-Video-Streaming-Dienst. Ordnen Sie die folgenden Situationen den passenden HTTP-Statuscode zu und begründen Sie Ihre Entscheidung.nb

|Situation| HTTP-Statuscode| Begründung|
|---------|----------------|-----------|
|Startseite erfolgreich abgerufen|``200 OK``| Anfrage erfolgreich, Seite ausgeliefert|
|Upstream-Streaming-Server antwortet nicht rechtzeitig|``502 Bad Gateway``| Dienst agirt asl Proxy/Gateway; 502 wenn ungültige Antwort|
|Fehler bei Videotranscodierung auf Server|``500 Internal Server Error``| Unerwarteter Serverfehler, Bearbeitung der Anfrage nicht möglich|
|Serie existiert nicht mehr| ``404 Not Found``| Ressource existiert nicht|
|Trailer vorübergehend auf andere URL verschoben|``302 Found`` oder ``307 ``Temporary Redirect``| Temporäre Umleitung; bei 307 bleibt Methode erhalten|
|Serie dauerhaft auf neue URL verschoben| ``301 Moved Permanently`` oder ``308 Permanent Redirect``| Dauerhafte Umleitung; 308, falls man HTTP-Methode und Body erhalten will|