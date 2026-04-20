def quicksort(sequenza):
    #caso terminale
    if len(sequenza) <= 1:
        return sequenza
    #caso ricorsivo
    else:
        #1.scelgo il pivot
        pivot = sequenza[0] #prendo un elemento a caso, in questo caso il primo
        #2.dividere sequenza secondo il pivot
        sequenza_smaller = []
        sequenza_pivot = []
        sequenza_larger = []
        for i in sequenza:
            if i < pivot:
                sequenza_smaller.append(i)
            elif i == pivot:
                sequenza_pivot.append(i)
            else:
                sequenza_larger.append(i)
        #3.la soluzione è data da: ordinare il vettore smaller + il vettore = pivot + ordinare il vettore larger
        return (quicksort(sequenza_smaller) + sequenza_pivot + quicksort(sequenza_larger))

    #sequenza_smaller = [n for n in sequenza if n < pivot]
    #sequenza_pivot = [n for n in sequenza if n == pivot]  #ottimizzato e leggibile
    #sequenza_larger = [n for n in sequenza if n > pivot]





if __name__=="__main__":
    sequenza = [9,3,2,5,6,7,8,199]
    print(quicksort(sequenza))