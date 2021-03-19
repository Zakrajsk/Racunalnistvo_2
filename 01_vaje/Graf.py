import time
import random
import Bruteforce
from matplotlib import pyplot as plt

class Node:
    def __init__(self, vrednost):
        self._vrednost = vrednost
        self._naslednji = set()

    def dodaj(self, node):
        """
        Doda povezavo do vozlisca
        """
        self._naslednji.add(node)

    def najdaljsa_pot(self):
        """
        Rekurzivna funckija za iskanje najdaljse poti by martin ogrin
        """
        if not self._naslednji:
            return 1
        
        naslednji = [izbran.najdaljsa_pot() for izbran in self._naslednji]
        return 1 + max(naslednji)


def naredi_graf(podatki):
    """
    Glede na podatke naredi graf, kjer ima vsako vozlisce povezavo do vseh ostalih, ki so vecji od izhodiscnega
    """
    n = len(podatki)
    tabela_kazalcev = [Node(i) for i in podatki]
    for i in range(n):
        for j in range(i + 1, n):
            if podatki[j] > podatki[i]:
                tabela_kazalcev[i].dodaj(tabela_kazalcev[j])

    return tabela_kazalcev


def najdaljse_zaporedje_graf(podatki):
    """
    S pomocjo grafa najde najdaljse zaporedje s podatki
    """
    kaz = naredi_graf(podatki)
    zacetni_cas = time.time()
    najvecja = 0
    #iz vsakega vozlisca poiscemo najdaljso pot
    for en in kaz:
        najvecja = max(najvecja, en.najdaljsa_pot())

    izvajalni_cas =time.time() - zacetni_cas
    return najvecja, izvajalni_cas


test = [5, 2, 8, 6, 3, 6, 9, 7]
test2 = [5, 2, 8, 6, 3, 6, 9, 7, 8, 10, 5, 18, 9, 25, 9, 42]
test3 = []


#risanje grafa

for i in range(1, 82):
    #generiramo teste
    test4 = [random.randint(1, 1000) for i in range(i)]

    najvecja, izvajalni_cas = najdaljse_zaporedje_graf(test4)

    plt.plot(i, izvajalni_cas, "ro")

    #od 22 naprej se bruteforce metoda predolgo izvaja
    if i < 22:
        najvecja, izvajalni = Bruteforce.najdaljse_zaporedje_bruteforce(test4)
        plt.plot(i, izvajalni, "bo")


plt.show()


