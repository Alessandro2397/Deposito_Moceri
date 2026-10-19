import numpy as np
# Creo matrice Numpy 2D di dimensioni 6x6 contenente numeri interi casuali da 1 a 100

matrice = np.random.randint(1, 101, size=(6, 6))
# 1° punto - Stampo matrice
print("\n---------- primo punto ----------\n",matrice,"\n")

# 2° punto - Estrai la sotto-matrice centrale 4x4 dalla matrice originale
sotto_matrice = matrice[1:5, 1:5]

print("\n---------- secondo punto ----------\n",sotto_matrice,"\n")

# 3° punto - Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via)
matrice_invertita = sotto_matrice[::-1]

print("\n---------- terzo punto ----------\n",matrice_invertita,"\n")

# 4° punto - Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi
diagonale = np.diag(matrice_invertita)

print("\n---------- quarto punto ----------\n",diagonale)

# 5° punto - Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1
matrice_invertita[matrice_invertita % 3 == 0] = -1

print("\n---------- quinto punto ----------\n",matrice_invertita)

