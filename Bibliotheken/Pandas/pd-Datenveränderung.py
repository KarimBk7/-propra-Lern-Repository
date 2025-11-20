import pandas as pd

# A6
pd.options.mode.copy_on_write = True

erststimmen_df = pd.read_csv("Erstwahlen.csv", sep=';', encoding="latin")



# A1:
erststimmen_df["Stimmart"] = "Bearbeitet"
print(f"\nA1:\n{erststimmen_df}")


# A2: 
erststimmen_df.loc[0, "Bezirksname"] = "Mitte Neu"
print(f"\nA2:\n{erststimmen_df.loc[0, 'Bezirksname']}")


# A3:
mask = erststimmen_df["Bezirksname"] == "Mitte"
erststimmen_df.loc[mask, "Bezirksnummer"] = 999
print(f"\nA3:\n{erststimmen_df['Bezirksnummer']}")


# A4: 
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
subset = df.copy()


# A5 
mask = (erststimmen_df["Wählende"] > 500) & (erststimmen_df["Gültige Stimmen"] > 400)
erststimmen_df.loc[mask, "SPD"] = -999
print(f"\nA5:\n{erststimmen_df['SPD']}")
