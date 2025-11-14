### F1: Aber warum funktioniert das? Der Unterprozess unterliegt doch derselben Speicherbeschränkung auf 512 MB, in der unsere Daten nicht genug Platz finden! <br> Recherchieren Sie, wie GNU sort das anstellt, und geben Sie für die Antwort eine möglichst vertrauenswürdige Quelle an.

Der Unterprozess ``sort`` unterliegt eigentlich derselben Speicherbeschränkung, aber GNU sort versucht gar nicht die Daten vollständig im RAM zu halten.
GNU sort nutzt einen externen Sortieralgorithmus welcher nur einen begrenzten Datenblock in den Speicher einliest, Daten temporär auf die Festplatte schreibt und alles am ende wieder zusammenführt mit ``Merge``.
<br>
<br>
Quelle: https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html