### F1: Nennen Sie einen Aspekt, der Ihnen daran gut gefällt
Das Changelog nennt klar Kompatibilitätsänderungen und FIxes. Das Hilft um Risiken einzuschätzen.

### F2: und einen zweiten, der verbesserungswürdig wäre.
Es fehlen Daten und die Kategorien der verschiedenene ``change`` wie Added, Changed, Fixed, Removed, usw.

### F3: Warum benutzt Django wohl diese Form?
+ Versionierte Doku mit Permalinks zum suchen
+ Skalierbarkeit für große Frameworks mit vielen Subsystemen
+ LTS und Zwischenreleases lassen sich nebeneinander dokumentieren

### F4: Angenommen, Sie entwickeln eine Webanwendung mit Django, die derzeit mit Django Version 4.1.7 läuft und wollen jetzt ein Upgrade auf die Version 5.0.4 machen. Welche Dateien müssen Sie studieren, um die wichtigsten Dinge (nicht jede Einzelheit) zu überschauen, die bei dieser Umstellung schiefgehen könnten und vielleicht Änderungen an Ihrer Webanwendungen verlangen? Welche Abschnitte in diesen Dateien müssen Sie beachten?
+ Release notes 5.0
  + Abschnitt: "Backwards incompatible changes", "Removed features", Deprecated feautures removed in 5.0", "Python Kompatiblität"
+ Release notes 4.2
  + "Deprecations"
+ Release notes 4.1
  + "Deprecations


### F5: 5 Welche Abschnitte in welchen Dateien brauchen Sie zusätzlich, wenn Sie auch noch tolle neue Funktionalität mitbekommen möchten, die Sie vielleicht in Ihrer Webanwendung benutzen wollen?
In jeder Major/Minor-Release-Seite die Abschnitte hervorhebt die neue sein können wie "What's new?"


### F6: Inwiefern ist dieses Format bei Django gut? Wäre ein normales Changelog besser?
Es ist sehr gut für große Projekte, um alles zu versionieren, suchbar zu machen und es reich an kontext zu gestalten.<br>
Ein Nachteil ist das es nicht sofort sichtbar ist.