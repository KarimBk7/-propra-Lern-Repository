import pandas as pd

erststimmen_df = pd.read_csv("Erstwahlen.csv", sep=';', encoding="latin1")

# A1
cdu = erststimmen_df[["Wahlbezirk", "Gültige Stimmen", "CDU"]]
print(cdu)

# A2
slicing = erststimmen_df[0:10]
print(slicing)

# A3
slicing2 = erststimmen_df[0:50:3]
print(slicing2)

# A4
slicing3 = erststimmen_df[["Wahlbezirk", "Gültige Stimmen"]][5:6]
print(slicing3)

# A5
slicing4 = erststimmen_df[5:6][["Wahlbezirk", "Gültige Stimmen"]]
print(slicing4)

# A6
cdu2 = erststimmen_df.at[0,"CDU"]
print(cdu2)

# A7 
loc = erststimmen_df.loc[0, "CDU"]
print(loc)

# A8
loc2 = erststimmen_df.loc[[0, 2], ["CDU", "Gültige Stimmen"]]
print(loc2)

# A9
loc3 = erststimmen_df.loc[:5, "Adresse":"Wahlbezirk"]
print(loc3)

iat = erststimmen_df.iat[0,0]
print(iat)

iloc = erststimmen_df.iloc[10:50, 1:5]
print(iloc)