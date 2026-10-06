scelta = int(input("Inserisci numero > 10: "))
if(scelta>10):
    scelta = int(input("Inserisci numero > 50"))
    nome = input("Inserisci nome: ")
    password = input("Inserisci password: ")
    id = nome + " _ " + "000"
    
    print(id)
else:
    print("La scelta non era 1")