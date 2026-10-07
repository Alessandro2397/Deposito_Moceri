# Punto 1

numero=-1
while(numero!=0):
    numero = int(input("Inserisci un numero (0 per uscire): "))
    if(numero%2==0 and numero != 0):
        print("Il numero inserito (", numero,") è pari\n")
    elif(numero==0):
        print("Saluti, :D!\n")
        break
    else:
        print("Il numero inserito (", numero,") è dispari\n")
        
# Punto 2

controllore = True
while controllore:
    numero = int(input("Inserisci un numero: "))
    for x in range(numero, -1, -1):
        print(x)
        numero-=1
    richiesta=input("Vuoi ripetere?")
    if richiesta.upper()=="NO":
        controllore = False
        print("Saluti, :D!\n")
    else:
        controllore = True
        
# Punto 3

lista = []
n = int(input("Da quanti numeri è composta la tua lista? "))
for i in range(n):
    numero = int(input("Inserisci numero: "))
    lista.append(numero)
    print("Il quadrato di",lista[i],"è ",lista[i]*lista[i])
    
# Utilizzo di if while e for
massimo=0
for j in range(len(lista)):
    if(lista[j]>massimo):
        massimo = lista[j]
print("Il numero massimo è",massimo)

flag=True
k=0
contaElem=0
while(flag):
    if(k==len(lista)-1):
        print("Il numero di elementi della lista è", contaElem)
    else:
        contaElem+=1
    
