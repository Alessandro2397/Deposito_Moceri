import pandas as pd
import matplotlib.pyplot as plt

dati = {
    "Temperatura": [
        18.5, 19.2, 17.8, 20.1, 21.3,
        22.0, 19.8, 18.9, 20.5, 23.1,
        24.0, 22.7, 21.5, 20.8, 19.6,
        18.2, 17.5, 19.0, 21.0, 22.4,
        23.5, 25.1, 24.3, 22.8, 21.7,
        20.2, 19.4, 18.7, 21.2, 23.0
    ]
}

df = pd.DataFrame(dati)

print(df)

# Calcolo delle statistiche
temperatura_max = df["Temperatura"].max()
temperatura_min = df["Temperatura"].min()
temperatura_media = df["Temperatura"].mean()
temperatura_mediana = df["Temperatura"].median()

# Stampo le statistiche
print("Temperatura massima: ", temperatura_max)
print("Temperatura minima: ", temperatura_min)
print("Temperatura media: ", temperatura_media)
print("Temperatura mediana: ", temperatura_mediana)

# Passo a creazione grafico
plt.plot(df.index, df["Temperatura"])

plt.title("Temperature giornaliere")
plt.xlabel("Giorno del mese")
plt.ylabel("Temperatura (°C)")
plt.xlim(left=0)

plt.grid(True)
plt.show()
