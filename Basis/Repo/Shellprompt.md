### Shellprompt
---
Ich habe das Prompt folgerndermaßen verändert:

1. Der User (user@host) ist in einem Grün, um die einzelnen Befehle voneinander zu unterscheiden.

2. Direkt danach kommt das verzeichnis (pwd) in rot, um vom grün zu unterscheiden

3. Die Befehle sind gelb, wobei die farbe hier recht egal ist solange diese nicht zu sehr dem rot des pwd ähnelt.

---

```bash
export PS1="\[\e[0;32m\]\u@\h\[\e[0;31m\]\${PWD}\[\e[1;33m\]\[\e[0;33m\] \$ "
```

