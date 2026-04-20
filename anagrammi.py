import copy


def anagrammi(parola):
    soluzioni = []
    ricorsione([], parola, soluzioni)
    return soluzioni

def ricorsione(parziale: list, rimanenti: str, soluzioni: list) -> list:
    #caso terminale
    if len(rimanenti) == 0:
        soluzioni.append(copy.deepcopy(parziale))

    #caso ricorsivo
    else:
        for i in range(len(rimanenti)):
            parziale.append(rimanenti[i])
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione(parziale, nuovi_rimanenti, soluzioni)
            parziale.pop()

#========================================================================================

#Il SET mi serve per rimuovere i doppi in casa di anagrammi di una parola con due lettere uguali.
#(oppure uso lru_cache, che una volta che sta per aggiungere una parola che ha gia stampato non la aggiunge, ma
# posso usare solo stringhe e stampare una alla volta in colonna)

#Nel set non posso mettere le liste perche non sono hashable!!!!, quindi uscira un set di stringhe
def anagrammi_str(parola):
    soluzioni = set()
    ricorsione_str("", parola, soluzioni)
    return soluzioni

def ricorsione_str(parziale: str, rimanenti: str, soluzioni: list):
    #caso terminale
    if len(rimanenti) == 0:
        soluzioni.add(copy.deepcopy(parziale))

    #caso ricorsivo
    else:
        for i in range(len(rimanenti)):
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione_str(parziale+rimanenti[i], nuovi_rimanenti, soluzioni)



if __name__ == "__main__":
    print(anagrammi("dog"))
    print(anagrammi_str("casa"))