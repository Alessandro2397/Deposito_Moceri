sommaPari=0
sommaDispari=0
cont=0
primo=0
nonPrimo=0
prova=0
flagg=True
import random
# Chiedi all'utente quale intero positivo n vuole inserire, e quale
# esercizio vuole fare - da 1 a 6 -:
# punto 1: inserimento intero positivo n
n=-1
lista = []
while n<=0 or n>6:
    n=int(input("Inserisci un intero positivo n: "))
    if(n<=0 or n>6):
        print("Errore di immissione!")

# punto 2: genera una lista di numeri interi casuali tra 1 ed n (incluso). Lunghezza lista = n
for i in range(0,n,1):
    lista.append(random.randint(1, n))
    print(lista[i])

# punto 3: utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista
for cont in range(len(lista)):
    if(lista[cont]%2==0):
        sommaPari=sommaPari+lista[cont]
print("La somma dei numeri pari nella lista è ",sommaPari)

# punto 4: utilizza un ciclo for per calcolare e stampare la somma dei numeri dispari nella lista
for cont in range(len(lista)):
    if(lista[cont]%2!=0):
        sommaDispari=sommaDispari+lista[cont]
print("La somma dei numeri dispari nella lista è ",sommaDispari)

# punto 5: utilizza un ciclo per determinare se un numero è primo. La funzione deve restituire True
# se il numero è primo, altrimenti False
while flagg:
    prova=int(input("Inserisci numero a tua scelta per verificare se è primo: "))
    for q in range(2,prova,1):
        if(prova%q==0):
            nonPrimo=prova
            print("Il numero",nonPrimo,"non è primo, :D!")
            flagg=False
        elif(prova%q!=0 and q==(prova-1)):
            primo=prova
            print("Il numero da te scelto", primo, "è primooo, :D!!")
