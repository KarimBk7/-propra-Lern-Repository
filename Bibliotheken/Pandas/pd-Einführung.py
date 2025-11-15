import pandas as pd

erststimmen_datensatz = pd.read_csv("Erstwahlen.csv", encoding="latin1", sep=";")
print(erststimmen_datensatz)