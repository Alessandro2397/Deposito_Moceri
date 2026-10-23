import pandas as pd
import matplotlib.pyplot as plt

# Carico e leggo il file
df = pd.read_csv("C:/Users/39340/Downloads/candy-data.csv")
df_vendite = pd.read_csv("C:/Users/39340/Downloads/candy-vendite.csv")

# Stampo il file candy-data.csv e lo visiono
print(df) # Dataset con 85 righe - da 0 a 84 - e 13 colonne

# Esploro il file
print("---------- PRIMI 5 ELEMENTI ----------\n",df.head(),"\n---------- ULTIMI 5 ELEMENTI ----------\n",df.tail())
#print(df_vendite)

# Elimino i possibili duplicati, e salvo il nuovo contenuto in un altro dataframe
df_nuovo = df.drop_duplicates()
print("---------- STAMPO NUOVO DF DOPO AVERLO RIPULITO ----------\n", df_nuovo) # Visiono i risultati, ma vedo che abbiamo sempre
                                                                                # 85 righe e 13 colonne
                                                                                
# Vedo se ci sono valori NaN. df.isna().values.any() restituisce True se ne trova almeno uno: False altrimenti
print(df.isna().values.any()) # Mi è stato restituito False, quindi candy-data.csv NON contiene elementi NaN

# Vedo quanti NaN ci sono in ogni colonna
#print(df.isna().sum())

# Stampo il file candy-vendite.csv e lo visiono
print(df_vendite) # Il file candy-vendite.csv contiene, invece, 83 righe e 8 colonne

# Esploro il file
print("---------- PRIMI 5 ELEMENTI ----------\n",df_vendite.head(),"\n---------- ULTIMI 5 ELEMENTI ----------\n",df_vendite.tail())

# Elimino i possibili duplicati, e salvo il nuovo contenuto in un altro dataframe
df_vendite_nuovo = df_vendite.drop_duplicates()
print("---------- STAMPO NUOVO DF DOPO AVERLO RIPULITO ----------\n", df_vendite_nuovo) # Visiono i risultati

# In definitiva non c'erano valori mancanti, né NaN nei dataset, ma ne visiono le caratteristiche con shape e describe, :D
print(df_nuovo.shape)
print(df_vendite_nuovo.shape)
# VERIFICATO CHE HANNO ENTRAMBI LE STESSE DIMENSIONI DEI DATASET DI PARTENZA

# ADESSO SI VUOLE VERIFICARE L'ANDAMENTO, SU TERRITORIO ITALIANO, DELLE VENDITE
df_vendite_nuovo["area_vendita"].value_counts().plot.bar()
plt.plot(df_vendite_nuovo.index, df_vendite_nuovo["area_vendita"])
plt.xlim(left=0)
plt.show()
