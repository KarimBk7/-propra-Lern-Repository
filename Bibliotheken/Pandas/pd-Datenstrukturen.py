import pandas as pd


buecher_namen_array = ["Harry Potter und der Stein der Weisen", "Der kleine Prinz", "Die unendliche Geschichte"]
buecher_namen_series = pd.Series(buecher_namen_array)

# A1
dritte = buecher_namen_series[2]
print(f"Das dritte Buch ist {dritte}")


# A2 
buecher_namen_series = pd.Series(buecher_namen_array, 
    index=["3-551-32011-X", "3-7920-0024-5", "3-522-20202-3"] # ISBN der Bücher
)

dritte = buecher_namen_series[2]
print(buecher_namen_series["3-522-20202-3"])


# A3
buecher_preis_dict = {
    "3-522-20202-3": 12.99,
    "3-551-32011-X": 5.99,
    "3-7920-0024-5": 5.90
}
buecher_preis_series = pd.Series(buecher_preis_dict)
print(buecher_preis_series)

buecher_bewertung_series = {
    "3-522-20202-3": 10,
    "3-551-32011-X": 6,
    "3-7920-0024-5": 8
}

isbn = "3-522-20202-3"
print(buecher_namen_series[isbn])
print(buecher_preis_series[isbn])
print(buecher_bewertung_series[isbn])


# A4
buecher_dict = {
    "Buchname": buecher_namen_series,
    "Preis in €": buecher_preis_series,
    "Bewertung": buecher_bewertung_series
}

buecher_df = pd.DataFrame(buecher_dict)
print(buecher_df)

print("\n\n", buecher_df["Preis in €"])


# A5
print("\n\n", buecher_df["Buchname"]["3-522-20202-3"])
