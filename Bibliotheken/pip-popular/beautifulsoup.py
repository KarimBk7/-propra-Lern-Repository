from bs4 import BeautifulSoup

datei = open("seite.html",'r')
soup = BeautifulSoup(datei,'html.parser')

print(soup.find_all('span'))