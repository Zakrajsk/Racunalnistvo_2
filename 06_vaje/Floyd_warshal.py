import time

# Algorithm implementation
def floyd_warshall(G, stevilo_vozlisc):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(stevilo_vozlisc):
        for i in range(stevilo_vozlisc):
            for j in range(stevilo_vozlisc):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    #print_solution(distance, stevilo_vozlisc)


# Printing the solution
def print_solution(distance, stevilo_vozlisc):
    for i in range(stevilo_vozlisc):
        for j in range(stevilo_vozlisc):
            if(distance[i][j] == 10000):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


def sestavi_matriko(ime_datoteke):
    """
    Funkcija sestavi matriko povezav. Najprej prebere txt datoteko in s pomocjo le te nastavi vse vrednosti v matriki
    """
    branje = open(ime_datoteke)
    st_vozlisc = int(branje.readline())
    matrika_povezav = [[1000000 for i in range(st_vozlisc)] for j in range(st_vozlisc)]
    st_povezav = int(branje.readline())
    for _ in range(st_povezav):
        vrsta = branje.readline()
        prvo, drugo, teza = vrsta.strip().split(" ")
        prvo = int(prvo)
        drugo = int(drugo)
        teza = float(teza)
        matrika_povezav[prvo][drugo] = teza
    return st_vozlisc, st_povezav, matrika_povezav


def preveri_razlicne_grafe(tabela_grafov):
    """
    Funckija preveri iz izpise kako dolgo traja izvajanje posameznega dela
    pri primovem algoritmu za vsak graf iz tabele_grafov posebaj
    """
    for posamezn in tabela_grafov:
        cas = time.time()

        st_vozlisc, st_povezav, matrika = sestavi_matriko(posamezn)
        
        print(f"Pretvorba iz datoteke v graf traja: {time.time() - cas} sekund")

        cas = time.time()
        floyd_warshall(matrika, st_vozlisc)

        print(f"Delovanje Floyd-Warshallovega algoritma za {st_vozlisc} vozlišč in {st_povezav} povezav vzame: {time.time() - cas} sekund")
        print("---------------------------------------------------------------------------")

#largeEWG.txt je izpuscen, saj dela vse predolgo
vsi_grafi = ["tinyEWG.txt", "mediumEWG.txt", "1000EWG.txt", "10000EWG.txt"]
preveri_razlicne_grafe(vsi_grafi)