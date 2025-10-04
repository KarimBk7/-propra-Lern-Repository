### F1: Jetzt klären Sie bitte durch Recherche die Bedeutung der Einträge `__pycache__` / und *.py[cod] und erklären Sie sie mit je einem Satz.

+ `__pycache__`: Ein spezieller Ordner, in dem Python die für importierte Moduule erzeugt und versionsmarkierten Bytecode-Cachedatein ablegt. Somit werden spätere Imports schneller geladen.
+ *.py[cod]: Ein Dateinamensmuster, das die drei kompilierten Python-Dateiendungen abdeckt. (.pyc, .pyo, pyd)


### F2: Recherchieren Sie, was die Einträge von vscode.gitignore bedeuten. Welche davon sollten Sie übernehmen? Erklären Sie nur deren Bedeutung in je einem Satz.
+ vscode/*: Ignoriere alle Datein und Unterordner im .vscode-Verzeichnis
+ !.vsode/settings.json: Hebt die Ignorierung für .vscode/settings.json auf
+ !.vsode/tasks.json: Hebt die Ignorierung für .vscode/tasks.json auf
+ !.vsode/launch.json: Hebt die Ignorierung für .vscode/launch.json auf
+ !.vsode/extension.json: Hebt die Ignorierung für .vscode/extension.json auf
+ !.vscode/*.code-snippets: Hebt die Ignorierung für alle .code-snippets in .vscode auf
+ !*.code-workspace: Hebt die Ignorierung für .code-workspace-Dateien im Projekt-Root auf
+ *.vsix: Ignoriere alle .vsix-Dateien, da das Binärartefakte sind