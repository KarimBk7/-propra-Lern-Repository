import pandas as pd

erststimmen_df = pd.read_csv("Erstwahlen.csv", sep=';', encoding="latin")


# A1
erste15 = erststimmen_df.head(15)
print(f"\nA1-head(15): \n{erste15}")


# A2:
random = erststimmen_df.sample(5)
print(f"\n\nA2-sample(5): \n{random}")


# A3
random2 = erststimmen_df.sample(frac=1/3)
print(f"\n\nA3-sample(frac=1/3): \n{random2}")


random2 = erststimmen_df.sample(random_state=42, n=1)
random2 = random2[["Wahlbezirk", "Adresse"]]
des = erststimmen_df.describe()
res = des[["CDU", "SPD", "FDP"]]
print(f"\n\nDESCRIBE: \n{res}")
