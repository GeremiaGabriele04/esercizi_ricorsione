from time import time

from anyio.functools import lru_cache


class Fibonacci:
    def __init__(self):
        self.cache = {0: 0, 1: 1} #inserisco gia le due soluzioni che gia so, poi aggiornero il dict

    def calcola_elemento_cache(self,n):
        #se ho gia la soluzione per questo n
        #la prendo dalla cache
        if self.cache.get(n) is not None:
            return self.cache[n]

        #else, vado avanti con la ricorsione
        else:
            self.cache[n] = (self.calcola_elemento_cache(n-1) +
                             self.calcola_elemento_cache(n-2))
            return self.cache[n]


    def calcola_elemento(self, n):
        #terminale
        if n==0:
            return 0
        elif n==1:
            return 1
        #non terminale
        else:
            return (self.calcola_elemento(n-1) + self.calcola_elemento(n-2))

    @lru_cache
    def calcola_elemento_lru(self, n):
        #terminale
        if n==0:
            return 0
        elif n==1:
            return 1
        #non terminale
        else:
            return (self.calcola_elemento_lru(n-1) + self.calcola_elemento_lru(n-2))



if __name__=="__main__":

    # il primo 1min, il secondo e il terzo praticamente uguali vicini allo 0

    N=40
    fib = Fibonacci()
    start_time = time()
    print(fib.calcola_elemento(N))
    end_time = time()
    print(f"Elapsed time - recursion: {end_time - start_time}")

    start_time = time()
    print(fib.calcola_elemento_cache(N))
    end_time = time()
    print(f"Elapsed time - recursion: {end_time - start_time}")

    start_time = time()
    print(fib.calcola_elemento_lru(N))
    end_time = time()
    print(f"Elapsed time - recursion: {end_time - start_time}")