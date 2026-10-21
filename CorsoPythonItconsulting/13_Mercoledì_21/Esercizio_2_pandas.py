import pandas as pd

# Carico il dataset
df = pd.read_csv("C:/Users/39340/Downloads/customers-100.csv")

# Visualizzo il dataset
print(df)

# Esploro il dataframe
print("PRIMI 5 CAMPI\n",df.head())
print("ULTIMI 5 CAMPI\n",df.tail())

# Pulisco il dataframe, cioè elimino, innanzitutto, gli spazi dai nomi, ed elimino i duplicati
df.columns = df.columns.str.strip()
df.drop_duplicates()
print("ESPLORIAMO IL DATASET RIPULITO","\n")
print(df)

