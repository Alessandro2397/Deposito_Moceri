import numpy as np

# 1° punto - Crea un array di 20 interi casuali compresi tra 10 e 50
print("---------- primo punto ----------")
array = np.random.randint(10, 51, size=20)

print(array)

# 2° punto - Stampa i primi 10 elementi dell'array
print("---------- secondo punto ----------")
primi_10 = array[:10]

print(primi_10)

# 3° punto - Stampa gli ultimi 5 elementi dell'array (dal 16° al 20°)
print("---------- terzo punto ----------")
ultimi_5 = array[16:21]
                 
print(ultimi_5)

# 4° punto - Stampa gli elementi che vanno dal 5° indice al 14°
print("---------- quarto punto ----------")
da_5_a_14 = array[5:15]

print(da_5_a_14)

# 5° punto - Stampa ogni terzo elemento dell'array
print("---------- quinto punto ----------")
ogni_terzo = array[::3]

print(ogni_terzo)

# 6° punto - Sostituisci gli elementi che vanno dall'indice 5 all'indice 10 (escluso) con il numero 99
print("---------- sesto punto ----------")
array[5:10] = [99]

print(array)

# 7° punto
print("---------- settimo punto ----------")
# E' rimasto quest'ultimo punto da fare, domani recupererò, :D
