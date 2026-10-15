# Gestione della produzione di una fabbrica
# Lista che conterrà tutti i prodotti della fabbrica
produzione = []

# Ciclo infinito while True
while True:
    print("\n===== GESTIONE PRODUZIONE FABBRICA =====")
    print("1. Aggiungi prodotto") # Opzione per aggiungere prodotto
    print("2. Visualizza produzione") # Opzione per visualizzare tutti i prodotti
    print("3. Cerca prodotto") # Opzione per cercare prodotto
    print("4. Modifica quantità")
    print("5. Rimuovi prodotto")
    print("6. Calcola totale pezzi prodotti")
    print("7. Esci")

    scelta = input("Scegli un'opzione: ")
    
    # 1. Aggiungi prodotto
    if(scelta=="Aggiungi prodotto"):
        nome = input("Inserisci il nome del prodotto: ").strip() 
        
        # Gestisco eventuale errore nome vuoto
        if(nome==""):
            print("Il nome del prodotto non può essere vuoto")
            # continue serve a saltare il resto del ciclo, e tornare al menu iniziale
            continue
        
        # Inserisci quantità
        quantita = int(input("Inserisci la quantità prodotto: "))
        # Gestisco errore quantità < 0
        if(quantita < 0):
            print("La quantità non può essere negativa. ")
            
        else:
            # Uso dizionario prodotto
            prodotto = {
                "Nome": nome,
                "Quantità: ": quantita
            }
            
            # Aggiungi prodotto alla lista produzione
            produzione.append(prodotto)
            print("Prodotto aggiunto correttamente! ")
            
    # 2. Visualizza produzione
    elif(scelta=="Visualizza produzione"):
        if len(produzione) == 0:
            print("Nessun prodotto registrato. ")
            
        else:
            print("\n--- PRODUZIONE GIORNALIERA ---")
            for prodotto in produzione:
                print("- Prodotto:",prodotto["nome"],"\n- Quantità:",prodotto["quantita"])
                
    # 3. Cerca prodotto
    elif(scelta=="Cerca prodotto"):
        # Inserisco nome prodotto da cercare
        nome = input("Inserisci il nome del prodotto da cercare:").strip()
        # Inizializzo booleano "trovato" a False
        trovato=False
        
        # Scorro la lista produzione[]
        for prodotto in produzione:
            if prodotto["nome"].lower() == nome.lower():
                print("Prodotto trovato!!\n",prodotto["nome"],"\nQuantità:",prodotto["quantita"])
                trovato=True
                
        if not trovato:
            print("Prodotto non trovato, :(\n")
    
    # 4. Modifica quantità
    elif(scelta=="Modifica quantità"):
        nome = input("Inserisci il nome del prodotto di cui modificare la quantità: ").strip()
        trovato=False
        for prodotto in produzione:
            if prodotto["nome"].lower() == nome.lower():
                nuova_quantita = int(input("Inserisci nuova quantità: "))
                if(nuova_quantita < 0):
                    print("Attenzione: la nuova quantità non può essere negativa! ")
                    
                else:
                    prodotto["quantita"] = nuova_quantita
                    print("La quantità è stata modificata correttamente, :D!!\n")
                    
    elif(scelta == "Rimuovi prodotto"):
        print("")
        
    # 7. Esci
    elif(scelta=="Esci"):
        print("E' stato un piacere, cordiali salutiii, :D!!\n")
        break
