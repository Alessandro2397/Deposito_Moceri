class Teatro:
    def __init__(self, n):
        self.posti = [n]

        for i in range(n):
            p = Posto()
            self.posti.append(p)
            


class Posto(Teatro):
    _numero = 0 # Numero del posto
    _fila = "" # Fila in cui si trova il posto
    _occupato = True
    
    # Inizializza il posto impostando _occupato a False
    def __init__(self,_occupato):
        self._occupato = False
       
    # Prenota il posto se non è già occupato 
    def prenota(self): 
        if(self._occupato is True):
            return "Il posto è già occupato!\n"
        
        elif(not self._occupato):
            return "Hai prenotato il posto correttamente!\n"
            
     
    # Libera il posto se è occupato, altrimenti segnala che il posto non era prenotato   
    def libera(self):
        if self.occupato == True:
            self.occupato = False
            print("Posto liberato")
            
        else:
            print("Il posto è già libero")
            

""" Come ti dicevo oggi, Mirko, in questo esercizio sono stato
molto rallentato da quel dubbio STRUTTURALE che mi era sorto, 
ovvero 'POSTO è giusto che sia superclasse? O forse sarebbe meglio fare TEATRO, superclasse,
quindi invertire la gerarchia??? Domani continuerò comunqueeee, :D!! """
