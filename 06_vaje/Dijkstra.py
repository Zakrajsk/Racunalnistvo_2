# Dijkstra's Algorithm in Python
import sys
import time

def sestavi_matriko(ime_datoteke):
    """
    Funkcija sestavi matriko povezav. Najprej prebere txt datoteko in s pomocjo le te nastavi vse vrednosti v matriki
    """
    branje = open(ime_datoteke)
    st_vozlisc = int(branje.readline())
    matrika_povezav = [[0 for i in range(st_vozlisc)] for j in range(st_vozlisc)]
    matrika_sosescine = [[0 for i in range(st_vozlisc)] for j in range(st_vozlisc)]
    st_povezav = int(branje.readline())
    for _ in range(st_povezav):
        vrsta = branje.readline()
        prvo, drugo, teza = vrsta.strip().split(" ")
        prvo = int(prvo)
        drugo = int(drugo)
        teza = float(teza)
        matrika_povezav[prvo][drugo] = teza
        matrika_povezav[drugo][prvo] = teza
        matrika_sosescine[prvo][drugo] = 1
        matrika_sosescine[drugo][prvo] = 1

    return matrika_sosescine, matrika_povezav, st_vozlisc, st_povezav

for ena_datoteka in ["tinyEWG.txt", "mediumEWG.txt", "1000EWG.txt", "10000EWG.txt"]:

    cas = time.time()
    vertices, edges, st_vozlisc, st_povezav = sestavi_matriko(ena_datoteka)
    print(f"Pretvorba iz datoteke v graf traja: {time.time() - cas} sekund")

    cas = time.time()

    # Find which vertex is to be visited next
    def to_be_visited():
        global visited_and_distance
        v = -10
        for index in range(num_of_vertices):
            if visited_and_distance[index][0] == 0 \
                and (v < 0 or visited_and_distance[index][1] <=
                    visited_and_distance[v][1]):
                v = index
        return v


    num_of_vertices = len(vertices[0])

    visited_and_distance = [[0, 0]]
    for i in range(num_of_vertices-1):
        visited_and_distance.append([0, sys.maxsize])

    for vertex in range(num_of_vertices):

        # Find next vertex to be visited
        to_visit = to_be_visited()
        for neighbor_index in range(num_of_vertices):

            # Updating new distances
            if vertices[to_visit][neighbor_index] == 1 and \
                    visited_and_distance[neighbor_index][0] == 0:
                new_distance = visited_and_distance[to_visit][1] \
                    + edges[to_visit][neighbor_index]
                if visited_and_distance[neighbor_index][1] > new_distance:
                    visited_and_distance[neighbor_index][1] = new_distance
            
            visited_and_distance[to_visit][0] = 1

    i = 0

    # Printing the distance
    for distance in visited_and_distance:
        #print("Distance of ", chr(ord('a') + i),
        #    " from source vertex: ", distance[1])
        i = i + 1
    
    print(f"Delovanje Dijkstrinega algoritma za {st_vozlisc} vozlišč in {st_povezav} povezav vzame: {time.time() - cas} sekund")
    print("---------------------------------------------------------------------------")