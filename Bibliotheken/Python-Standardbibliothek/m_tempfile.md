### F1: Unterschied bennanten und unbennanten Datein
Bennante Tempfiles geben Pfade zurück während unbennante Tempfiles nur Dateideskriptoren (Datei-ID) liefern. 

### F2: Wieso hat das 'SpooledTemporaryFile' nachdem erstellen kein Namen/Pfad?
Der Inhalt des SpooledTemporaryFile wird im Arbeitsspeicher geschrieben bis ein max_size erreicht wurde. Nach diesem max_size Limit wird es in den Sekundärspeicher im '/tmp'-Verzeichnis geschrieben.<br>
Deshalb kann man direkt nachdem erstellen vor dem erreichen des 1KB noch keinen Namen/Pfad erkennen.