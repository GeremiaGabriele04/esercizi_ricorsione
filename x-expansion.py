class XExpansion:
    def __init__(self):
        self.soluzioni = []

    def calcola(self, input):
        self.soluzioni = []  #azzero la lista, cosi ogni ciclo è pulita
        self._ricorsione("", input)

    #parziale: la soluzione parziale che aggiorno ogni volta
    #rimanenti: caratteri ancora da esaminare
    def _ricorsione(self, parziale: str, rimanenti: str):
        #caso terminale
        if len(rimanenti)==0:
            #print(parziale)
            self.soluzioni.append(parziale)

        #caso ricorsivo
        else:
            if rimanenti[0] == "X":
                self._ricorsione(parziale+"0", rimanenti[1:])
                self._ricorsione(parziale+"1", rimanenti[1:])
            else:
                self._ricorsione(parziale+rimanenti[0], rimanenti[1:])

#========================================================================00
#===========================================================================
#=============================================================================

def x_expansion2(input):
    soluzioni=[]

    def ricorsione(parziale: str, rimanenti: str):
        #caso terminale
        if len(rimanenti)==0:
            #print(parziale)
            soluzioni.append(parziale)

        #caso ricorsivo
        else:
            if rimanenti[0] == "X":
                ricorsione(parziale+"0", rimanenti[1:])
                ricorsione(parziale+"1", rimanenti[1:])
            else:
                ricorsione(parziale+rimanenti[0], rimanenti[1:])

    ricorsione("", input)
    return soluzioni


if __name__ == "__main__":
    sequenza = "01X0X"
    xexp = XExpansion()
    xexp.calcola(sequenza)
    print(xexp.soluzioni)




