from bs4 import BeautifulSoup
import re

# Aufgabe A2:
datei = open("seite.html",'r')
soup = BeautifulSoup(datei,'html.parser')

# Aufgabe A4:
iv = soup.find('nav',id='sidebar')										# Inhaltsverzeichnis. Gekenzeichnet durch das nav-tag mit id='sidebar'

# Aufgabe A3:
diff = iv.find_all(attrs={'class': re.compile(r'difficulty[12]')})		# alle span tag mit cllass mit 'difficulty1' oder 'difficulty2'

#Aufgabe A5:
print(f"number of <span> tags declaring difficulty 1 or 2:", len(diff))
print("\nThose are the found tags:")
for i in diff:
	print(i)


# Aufgabe A6:
timevalues_total = 0

for i in diff:
	tmp = i.parent														# gehe in eltern tag
	tmp = tmp.find(attrs={'class': 'timevalue-decoration'})				# suche nach <span>-tag mit class='timevalue-decoration'
	
	timevalues_total += float(tmp.get_text())							# exportiere als float und addiere

print("\nTheir total timevalue: %.1f" % timevalues_total)
