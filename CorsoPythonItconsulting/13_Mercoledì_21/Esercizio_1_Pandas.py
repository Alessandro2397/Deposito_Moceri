import pandas as pd

# 1. Carico e stampo i dati in un dataframe
df = pd.read_csv("C:/Users/39340/Documents/GitHub/10_Lunedì_19/Dataset_Esempio.csv")
print(df)

# 2. Visualizzo le prime e le ultime 5 righe del dataframe
print("PRIME 5 RIGHE\n\n",df.head(), "\n")
print("ULTIME 5 RIGHE\n\n",df.tail(), "\n")

# 3. Visualizzare il tipo di dati di ciascuna colonna
print(df.dtypes)

# 4. Calcolare le statistiche descrittive di base per le colonne numeriche (media, mediana, deviazione standard)
colonne_numeriche = df.select_dtypes(include="number")
print("---------- STATISTICHE DESCRITTIVE DI BASE ----------\n")
print("Media: ", colonne_numeriche.mean())

# NON HO FINITO DI COMPLETARE QUESTA PARTE, MIRKOOOO!!! :D
