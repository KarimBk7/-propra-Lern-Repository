import pandas as pd

erststimmen_df = pd.read_csv("Erstwahlen.csv", sep=';', encoding="latin")

# A1
erststimmen_df["SPD_pro_Waehlende"] = erststimmen_df["SPD"] / erststimmen_df["Wählende"]
print(erststimmen_df["SPD_pro_Waehlende"])


# A2
print(erststimmen_df["Bezirksname"].apply(len))


# 
def double(x):
    if x % 2 != 0:
        return 2 * x
    else: 
        return x
print(erststimmen_df["SPD"].apply(double))


# A4
print(erststimmen_df["SPD"].apply(lambda x : x*2 if x % 2 != 0 else x))


# A5
bezirke_dict = {
    "Mitte": "MI",
    "Charlottenburg-Wilmersdorf": "CW",
    "Friedrichshain-Kreuzberg": "FK",
    "Pankow": "PA",
    "Spandau": "SP",
    "Steglitz-Zehlendorf": "SZ",
    "Tempelhof-Schöneberg": "TS",
    "Neukölln": "NE",
    "Treptow-Köpenick": "TK",
    "Marzahn-Hellersdorf": "MH",
    "Lichtenberg": "LI",
    "Reinickendorf": "RE"
}

print(erststimmen_df["Bezirksname"].apply(lambda x : bezirke_dict[x]))



# A6
print(erststimmen_df["Bezirksname"].map(lambda x : bezirke_dict[x]))