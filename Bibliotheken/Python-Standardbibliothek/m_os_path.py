import os
import time

# A1
print("home directory: ", os.path.abspath("$HOME"))

# A2 
homePath = os.path.abspath("$HOME").removesuffix("$HOME") 		# Entferne '$HOME' am ende
print("home directory exists: ", os.path.exists(homePath))

# A3
liste = os.listdir(homePath)
print(liste)

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
liste = [pfad for pfad in liste if os.path.isfile(pfad)]

biggestFile = max([os.path.getsize(pfad) for pfad in liste])
lastcreated = time.localtime(max([os.path.getctime(pfad) for pfad in liste]))
lastchanged = time.localtime(max([os.path.getmtime(pfad) for pfad in liste]))
mostcommon  = " "

print("biggest file:", biggestFile, "\nlast created:", lastcreated, "\nlast changed:", lastchanged, "\nmost common file extension:", mostcommon)
