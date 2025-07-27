import glob
import os

# A1
txtFiles = glob.glob("m_glob/*.txt")
print("all txt files:", txtFiles)


# A2
nmbNames = glob.glob("m_glob/*[1234567890]*")
nmbFiles = [n for n in nmbNames if os.path.isfile(n)]
print("all iles with a number:", nmbFiles)


# A3
allNames = glob.glob("m_glob/*")
allDir = [n for n in allNames if os.path.isdir(n)]
print("all directories", allDir)


# A4
nqn = glob.glob("m_glob/9NQn/*[1234567890][1234567890]*")
print("all files in '9NQn' with two numbers:", nqn)


# A5
hidden = glob.glob("m_glob/.*")
print("all hidden files:", hidden)


# A6
klammer = glob.glob("m_glob/*[*")
print("all files with '[':", klammer)


# A7
json = glob.glob("m_glob/**/*m*.json", recursive=True)
print("recursive: all json files with 'm':", json)


# A8
res = glob.glob("m_glob/*/**/[!ABCDEFGHIJKLMNOPQRSTUVWXYZ]*.txt", recursive=True, include_hidden=True)
print("recursive: all txt files in subdirs without uppercase first letter:", res)


# A9
txtList = []
for i in glob.iglob("m_glob/**/*.txt", recursive=True):
	txtList.append(i)
	if len(txtList) >= 3:			# Annahme aus Augabenstellung: "Gebe die ersten 3 Ergebnisse aus"
		break

print("recursive: all txt files, first 3 results:", txtList)