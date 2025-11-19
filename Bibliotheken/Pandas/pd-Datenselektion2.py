import pandas as pd

erststimmen_datensatz = pd.read_csv("Erstwahlen.csv", encoding="latin1", sep=";")


# A1
linke = erststimmen_datensatz["Die Linke"]
print(f"\nA1:\n{(linke > 20).sum()}") # trifft 3565 Zeilen


# A2
linke = erststimmen_datensatz["Die Linke"]
print(f"\nA2:\n{(linke == 20).sum()}") # trifft 7 Zeilen


# A3
cdu = erststimmen_datensatz["CDU"]
print(f"\nA3:\n{(linke > cdu).sum()}") # trifft 1787 Zeilen


# A4
print(f"\nA4:\n{(linke > 9).sum()}") # trifft 3597 Zeilen


# A5
gueltig = erststimmen_datensatz["Gültige Stimmen"]
print(f"\nA5:\n{((linke > 50) & (gueltig < 250)).sum()}") # trifft 5 Zeilen


# A6
bezirkname = erststimmen_datensatz["Bezirksname"]
print(f"\nA6:\n{(erststimmen_datensatz[(bezirkname != "Mitte")])}") # trifft 3295 Zeilen


# A7
spd = erststimmen_datensatz["SPD"]
print(f"\nA7:\n{erststimmen_datensatz[((linke > cdu) & (linke < spd))]}")  # trifft 130 Zeilen


# A8
print(f"\nA8:\n{erststimmen_datensatz.loc[(linke > cdu) & (linke < spd)]}") # trifft 130 Zeilen


# A9
print(f"\nA9:\n{erststimmen_datensatz.query("Bezirksname != 'Mitte'")}") # trifft 3295 Zeilen


# A10
print(f"\nA10:\n{erststimmen_datensatz.query("(`Die Linke` > CDU) & (`Die Linke` < SPD)")}") # trifft 130 Zeilen


# A11
print(f"\nA11:\n{erststimmen_datensatz.filter(like='1', axis=0)}") # trifft 1737 Zeilen


# A12
print(f"\nA12:\n{erststimmen_datensatz.filter(regex='(?i)bezirk', axis=1)}") # trifft 3598 Zeilen


# A13
print(f"\nA13:\n{erststimmen_datensatz.sort_values("Bezirksname", ascending=False)}") 


# A14
print(f"\nA14:\n{erststimmen_datensatz.sort_values("SPD", ascending=False).query("SPD < CDU")}") 
