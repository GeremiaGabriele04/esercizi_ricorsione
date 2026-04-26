from contextlib import nullcontext
from time import time


class NRegine():

    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0

    #=============================APPROCCIO 2===========================
    #Rappresento soluzione come un vettore di N regine,
    #ognuno rappresentante una regina come coppia riga e colonna

    def solve2(self, N):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self._ricorsione2([], N)

    #parziale: un vettore di coppie (riga, colonna)

    def _ricorsione2(self, parziale, N):
        self.n_chiamate += 1

        #caso terminale: ho messo N regine
        if len(parziale) == N:
            #if self._is_soluzione(parziale):    SUPERFLUO
            #    self.n_soluzioni += 1
            #    print(parziale)
            self.n_soluzioni += 1
            print(parziale)

        #caso ricorsivo: ho messo < N regine
        else:
            for riga in range(N):
                for col in range(N):
                    #verifico se la nuova regina sia ammissibile
                    nuova_regina = [riga, col]
                    if self._step_is_valid(nuova_regina, parziale):  #riduco le chiamate
                        #aggiungi questo pezzetto in parziale
                        parziale.append(nuova_regina)
                        #andare avanti con la ricorsione
                        self._ricorsione2(parziale, N)
                        #backtracking
                        parziale.pop()


    def _step_is_valid(self, nuova_regina, parziale) -> bool:
        for regina in parziale:
            if not self._is_pair_admissible(nuova_regina, regina):
                return False
        return True


    def _is_pair_admissible(self, regina1, regina2) -> bool:
        #1. verifico la riga
        if regina1[0] == regina2[0]:
            return False
        #2. verifico la colonna
        if regina1[1] == regina2[1]:
            return False
        #3. verifico la diagonale1
        if regina1[0] - regina1[1] == regina2[0] - regina2[1]:  #TRUCCO DIAG
            return False
        #4. verifico la diagonale2
        if regina1[0] + regina1[1] == regina2[0] + regina2[1]:  #TRUCCO DIAG
            return False
        #5. tutto passato --> TRUE
        return True

    def _is_soluzione(self, soluzione_possibile) -> bool:
        for i in range(len(soluzione_possibile)):
            for j in range(i+1, len(soluzione_possibile)):
                if not self._is_pair_admissible(soluzione_possibile[i], soluzione_possibile[j]):
                    return False
        return True



if __name__ == '__main__':
    nreg = NRegine()
    start_time = time()
    nreg.solve2(4)
    end_time = time()

    print(f"Elapsed time: {end_time - start_time}")
    print(f"Ho trovato {nreg.n_soluzioni} soluzioni possibili")
    print(f"Chiamate effettuate: {nreg.n_chiamate}")