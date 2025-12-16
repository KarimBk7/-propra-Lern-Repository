### F1: Warum muss man git bisect reset von Hand machen, statt das git bisect es automatisch tut, sobald die Suche erfolgreich war?
Weil er den Bisect-Zustand komplett aufräumt und einen zurück zum ursprünglichen HEAD leitet, obwohl man das vielleicht noch nicht tun will.

### F2: Angenommen, Sie kennen den Defekt schon und könnten ihn direkt reparieren. Warum kann es trotzdem hilfreich sein, den Commit zu finden, der den Defekt eingefügt hat? Nennen Sie zwei denkbare Gründe.
1. Womöglich möchte man die Commits trennen die nach dem Defekt commited wurden um andere Defekte aufzudecken. Denn es kann sein das es Code gibt der auf diesen Defekt aufbaut, welcher dan auch behoben werden muss.
2. Außerdem kann man somit vielleicht erkennen wieso dieser Defekt entstanden ist bzw. was hier die eigentliche Itention des Commits war.

### F3: Welches Subkommando von git bisect hilft im manuellen Modus, ggf. mit solchen nicht auswertbaren Commit-Ständen umzugehen?
Mit ``git bisect skip`` kann man den aktuellen commit als nicht auswertbar markieren, überspringt diesen und sucht mit den verbleibenden Commits weiter.

### F4: Wie lange dauert es mit bisect schlimmstenfalls, den defekten Commit zu finden?
1. Weil bisect ja mithilfe einer Binärsuche die commits sucht kann man die Laufzeit mit O(log2 n) für den Worst-Case berechnen.<br>
2- Zischen 666 (erster bad-commit) und dem letzten good-commit 800(-900) sind 134 bis 234 commits.<br>
+ **bei n=134**: log2(134) ≈ 7,07 ≈ 8
+ **bei n=234**: log2(234) ≈ 7,87 ≈ 8
3. Pro Schritt brauchen wir 2 Minuten was zu einem Endergebnis von 16 Minuten führt (8 * 2).