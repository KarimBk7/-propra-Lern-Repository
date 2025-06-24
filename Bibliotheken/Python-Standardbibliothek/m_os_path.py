import os
import time

# A1
print("home directory: ", os.path.abspath("$HOME"))

# A2 
homePath = os.path.abspath("$HOME").removesuffix("$HOME") 		# Entferne '$HOME' am ende
print("home directory exists: ", os.path.exists(homePath))

# A3
liste = os.listdir(homePath)
# print(liste)

# A4
for i in range (0,len(liste)):
	liste[i] =  os.path.join(homePath, liste[i]) #homePath + liste[i]
	
print("an entry in my home directory: ", liste[2])

# A5
filecount = 0
pathcount = 0

for i in liste:
	if os.path.isfile(i):
		filecount += 1
	elif os.path.isdir(i):
		pathcount += 1

print("# directories:", pathcount, ", # files:", filecount)

# A6
liste = [pfad for pfad in liste if os.path.isfile(pfad)]							# Alle Unterpfade entfernen. Nur Datein in Liste erlaubt

biggestFile = max([os.path.getsize(pfad) for pfad in liste])						# groesste Datei
lastcreated = time.localtime(max([os.path.getctime(pfad) for pfad in liste]))		# zuletzt erstellte Datei  (Linux: Zeitpunkt letzte Metadatenänderung)
lastchanged = time.localtime(max([os.path.getmtime(pfad) for pfad in liste]))		# zuletzt geaenderte Datei

filetype ={}
for i in liste:
	if os.path.splitext(i)[1] in filetype:
		filetype[os.path.splitext(i)[1]] += 1
	else:
		filetype[os.path.splitext(i)[1]] = 1

mostcommon = max(filetype, key=lambda ft: filetype[ft])									# am haeeufigsten vorkommende Dateiendung

print("biggest file:", biggestFile, "\nlast created:", lastcreated, "\nlast changed:", lastchanged, "\nmost common file extension:", mostcommon)


# A7
cwd = os.getcwd()
home = os.path.expanduser("~")
rel_path = os.path.relpath(cwd,home)
print("relative path from home to cwd: ",rel_path)


# A8
back_path = os.path.relpath(home,cwd)
comb = os.path.join(rel_path, back_path)
print("path home to cwd and back: ", comb)

# A9
norm = os.path.normpath(comb)
print("relative path normalized:", norm)
