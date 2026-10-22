import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Punto 1: Generazione dei dati
# Genero una serie temporale di 365 valori casuali, simulando il numero di visitatori giornalieri
# con una media di 2000 visitatori e una deviazione standard di 500.

visitatori = np.random.normal(
    loc=2000,   # numero medio visitatori giornalieri
    scale=500,                   # deviazione standard
    size=365                     # Periodo, ovvero 365 giorni 
)

date = pd.date_range(start="2026-01-01", periods=365, freq="D") # Cioè Day)

# Punto 2: Creazione del DataFrame
# Creo un DataFrame Pandas con le date come indice e il numero di visitatori come colonna.

df = pd.DataFrame(
    {"Visitatori": visitatori},
    index=date
)

# Punto 3: Calcolo delle statistiche mensili
# Raggruppo i dati per mese e calcolo la media e la deviazione standard dei visitatori giornalieri.

mensile = df.groupby(df.index.month)["Visitatori"].agg(
    ["mean", "std"]
)

# Stampo il dataframe
print(df)

# Stampo statistiche mensili, con media e deviazione standard dei visitatori giornalieri
print(mensile)

# Punto 4: Grafico a linee
# Creo un grafico a linee per visualizzare l'andamento giornaliero dei visitatori durante l'anno.
plt.figure(figsize=(12, 5))

# Creo il grafico a linee con le date sull'asse X e il numero di visitatori sull'asse Y.
plt.plot(df.index, df["Visitatori"])

# Inserisco il titolo del grafico
plt.title("Numero di visitatori giornalieri")

# Inserisco il nome "Data" sull'asse X
plt.xlabel("Data")

# Inserisco il nome "Numero di visitatori" sull'asse Y
plt.ylabel("Numero di visitatori")

# Attivo la griglia per facilitare la lettura dei valori nel grafico.
plt.grid(True)

# Visualizzo il grafico a linee.
plt.show()

