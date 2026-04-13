#UTILE UTILIZZARE DEBUG PER VEDERE RECURSION
def countdown_recursive(n):
    #condizione terminale
    if n==0:
        print("Stop")
    #condizione non terminale
    else:
        print(n)
        countdown_recursive(n-1)

if __name__ == "__main__":
    N=4
    countdown_recursive(N)
