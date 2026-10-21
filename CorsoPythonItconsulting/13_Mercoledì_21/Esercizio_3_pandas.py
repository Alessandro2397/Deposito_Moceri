import pandas as pd

dati = {
    "Città": ["Roma", "Milano", "Napoli", "Roma", "Milano",
              "Napoli", "Roma", "Milano", "Napoli"],
    "Prodotto": ["Laptop", "Smartphone", "Tablet", "Smartphone",
                 "Laptop", "Laptop", "Tablet", "Tablet", "Smartphone"],
    "Quantità": [10, 15, 8, 20, 12, 5, 14, 9, 18],
    "Prezzo": [800, 500, 300, 500, 800, 800, 300, 300, 500]
}

# 1. Caricare i dati in un dataframe
print("1. ---------- CARICO I DATI IN UN DATAFRAME ----------")
df = pd.DataFrame(dati)
print(df)

# 2. Aggiungere una colonnta totale_vendite che sia il risultato del prodotto tra quantità e prezzo
print("2. ---------- AGGIUNGO COLONNA Totale vendite ----------")
df["Totale vendite"] = df["Quantità"] * df["Prezzo"]

# Ristampo il dataset aggiornato
print("\nDATASET AGGIORNATO\n",df,"\n")

# 3. Raggruppare i dati per prodotto e calcolare il totale vendite per ciascun prodotto
print("3. ---------- RAGGRUPPO I DATI PER PRODOTTO E CALCOLO IL TOTALE DELLE VENDITE PER CIASCUNO ----------")
vendite_per_prodotto = df.groupby("Prodotto")["Totale vendite"].sum()
print(vendite_per_prodotto)

# 4. Trovare il prodotto più venduto in termini di quantità
#prodotto_piu_venduto = df.groupby("Prodotto")["Quantità"].max()
print("4. ---------- TROVARE IL PRODOTTO PIU' VENDUTO IN TERMINI DI QUANTITA' ----------")
prodotto_piu_venduto = vendite_per_prodotto.idxmax()
print("Prodotto più venduto: ", prodotto_piu_venduto,"\n")

# 5. # Calcolare il totale delle vendite per ogni città
vendite_per_citta = df.groupby("Città")["Totale vendite"].sum()
print("Città con il maggior numero di vendite: ",vendite_per_citta.max())
