### F1: Recherchieren Sie und erklären Sie für folgende Anwendungsfälle, wie die Zustandslosigkeit von HTTP entscheidend für die Skalierbarkeit ist: Content Delivery Networks (CDNs); Lastverteilung (load balancing) bei eCommerce-Anbietern. (Je ein Aspekt genügt, aber Ihre Antworten müssen richtig sein.)
##### CDNs
HTTP ist zustandslos. Ein Request an eine Ressource enthält alle zu gebrauchten Informationen, damit ein Server ihn beantworten kann.<br>
Dadurch kann CDN jeden einzelnen Request an beliebige Edge-Server weiterleiten, die dieses Objekt veretis gecacht haben.

##### Load Balancing bei eCommerce-Anbietern
E-Commerce-Systeme müssen sehr viele parallele Nutzer bedienen. Durch die Zustandslosigkeit von HTTP sind Requests nicht an einene bestimmten Server gebunden. <br>
Ein Load Balancer kann deshalb jede HTTP-Anfrage an beliebige freie Server weiterleiten, weil der Server keinen vorherigen Zustant benötigt, um die Anfrage korrekt zu verarbeiten, weil der Server keinen vorherigen Zustand benötigt, um die Anfrage korrekt zu verarbeiiten.


### F2: Erklären Sie den Unterschied zwischen Cookies und Sessions. Warum werden beide Mechanismen oft zusammen verwendet?
+ Cookies werden im Broswer gespeichert. Ein Cookies kann eine Session-ID oder Einstellungen enthalten.
+ Sessions werden auf dem Server gepspeichert. Der Server hält dabei die eigentlichen Benutzerdaten. Wird über Session-ID identifiziert.


### F3: Ein Online-Shop möchte folgende Funktionen implementieren:

+ Benutzer soll angemeldet bleiben
  + Umsetzung über ein Cookie mit Session-ID. Der Server hält die Session, das Cookie identifiziert nur den Benutzer.
+ Warenkorbinhalte sollen gespeichert werden
  + Umsetzung über eine Server-Session. Der Warenkorb gehört in den Server-Speicher, nicht in den Client.
+ Bevorzugte Sprache soll gesetzt werden
  + Umsetzung über ein persistentes Cookie, da es nur eine einfache Einstellung ist und ohne Serverzustand funktioniert.
+ Besuchstatistiken sollen erfasst werden
  + Umsetzung über ein Cookie mit pseudonymer ID. Der Server ordnet die Requests dieser ID zu.


### F4: Eine Website möchte sowohl Login-Informationen für 30 Tage speichern als auch temporäre Daten zur Sortier-Ordnung einer Tabelle table1 nur für die aktuelle Browsersitzung. Wie würden die entsprechenden Set-Cookie Header aussehen, wenn das Cookie vor Ausspionieren geschützt sein soll?
``Set-Cookie: table1=value123; Max-Age=2592000; HttpOnly; Secure; SameSite=Lax``