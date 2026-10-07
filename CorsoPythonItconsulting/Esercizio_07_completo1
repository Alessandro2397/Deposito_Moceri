lista = []
while True:
    scelta=int(input("Inserisci scelta: "))
    if(scelta==1):
        # Esercizio 1
        # Scrivere un programma che chieda all'utente di inserire numeri interi
        numero=-1
        contatore=1
        somma = 0
        while numero!=0:
            numero = int(input("Inserisci numero: "))
            lista.append(numero)
            somma = somma+numero
        print("La somma dei numeri inseriti è", somma)
    elif(scelta==2):
        # Esercizio 2
        # Scrivere un programma che chieda all'utente di inserire numeri interi
        parola = input("Inserisci una parola: ")
        for i in range(len(parola)):
            print(i+1,"° carattere: ",parola[i])
    elif(scelta==3):
        # Esercizio 3
        N = int(input("Inserisci N: "))
        passo = int(input("Inserisci passo: "))
        for dex in range(0, N, passo):
            print(dex)
    elif(scelta<0 or scelta > 3):
        pass 
    else:
        print("Salutiii, :D\n")
        break

        # Extra: Andare a creare un sistema che gestisca dinamicamente, quindi ripetibile,
        # le liste, permettendo ad un utente, di modificare, aggiungere, rimuovere e visualizzare
        # l'intera lista
        altraScelta = input(("--- EXTRA ---\n\nMODIFICA LISTA\nAGGIUNGI ALLA LISTA\nPOSIZIONE ELEMENTO DA ELIMINARE\nVISUALIZZA LISTA\nScelta -> "))
        match altraScelta:
            case "MODIFICA LISTA":
                posiz = int(input("Inserire posizione che vuoi modificare: "))
                lista[posiz] = posiz
                
            case "AGGIUNGI ALLA LISTA":
                numero = int(input("Numero da aggiungere: "))
                lista.append(numero)
                
            case "RIMUOVI ELEMENTO":
                numero = int(input("Inserisci posizione elemento da eliminare: "))
                remove(lista[numero])
            case _:
                pass
# Scusami per la piccola confusione, Mirko! Ma molto bene, oggi, :D!!
