import time

class Graf():

    def __init__(self, vozlisca):
        self.V = vozlisca
        self.graf = [[0 for _ in range(vozlisca)] for __ in range(vozlisca)]

    def Izpis(self, oce):
        """
        Izpis drevesa
        """
        print("Povezava \tCena")
        for i in range(1, self.V):
            print(oce[i], "-", i, "\t", self.graf[i][oce[i]])


    def minKey(self, vozlisca, ze_obiskani):
        """
        Poisce vozlisce, ki se ni v minimalnem drevesu in je najmanj oddaljena od drevesa
        """
        min = float("inf")

        for v in range(self.V):
            if vozlisca[v] < min and ze_obiskani[v] == False:
                min = vozlisca[v]
                min_index = v

        return min_index


    def prim(self):
        """
        S primovim algoritmom sestavi najmanjse vpeto drevo
        """
        trenutno_dolzine = [float("inf")] * self.V #tabela trenutnih rezultatov, da vemo katero vozlisce prvo izberemo
        parent = [None] * self.V # Tabela za resitve
        ze_izbrani = [False] * self.V #si bomo shranili kdaj smo ze obiskali neko vozlisce

        trenutno_dolzine[0] = 0 #nastavimo na nic, da prvo izberemo to vozlisce
        parent[0] = -1 #to je vedno -1 ker smo tega izbrali za izhodisce

        for _ in range(self.V):

            obravnavan = self.minKey(trenutno_dolzine, ze_izbrani) #izberemo tistega z minimalno vrednostjo, ki pa se ni bil izbran

            ze_izbrani[obravnavan] = True #sedaj ga oznacimo ze za izbranega

            for posamezno in range(self.V): #gremo cez vozlisca

                #ce povezava obstaja in se nismo izbrali tega vozlisca ter ima trenutno dolzine se vedno vecjo kot nova povezava med izbranim
                #takrat zamenjamo ker smo nasli boljso
                if self.graf[obravnavan][posamezno] > 0 and ze_izbrani[posamezno] == False and trenutno_dolzine[posamezno] > self.graf[obravnavan][posamezno]:
                    trenutno_dolzine[posamezno] = self.graf[obravnavan][posamezno]
                    parent[posamezno] = obravnavan

        #self.Izpis(parent) #izpisemo resitev, zakomentirana, ker sem racunal casovne zahtevnosti

def sestavi_matriko(ime_datoteke):
    """
    Funkcija sestavi matriko povezav. Najprej prebere txt datoteko in s pomocjo le te nastavi vse vrednosti v matriki
    """
    branje = open(ime_datoteke)
    st_vozlisc = int(branje.readline())
    matrika_povezav = [[0 for i in range(st_vozlisc)] for j in range(st_vozlisc)]
    st_povezav = int(branje.readline())
    for _ in range(st_povezav):
        vrsta = branje.readline()
        prvo, drugo, teza = vrsta.strip().split(" ")
        prvo = int(prvo)
        drugo = int(drugo)
        teza = float(teza)
        matrika_povezav[prvo][drugo] = teza
        matrika_povezav[drugo][prvo] = teza
    return st_vozlisc, st_povezav, matrika_povezav

def preveri_razlicne_grafe(tabela_grafov):
    """
    Funckija preveri iz izpise kako dolgo traja izvajanje posameznega dela
    pri primovem algoritmu za vsak graf iz tabele_grafov posebaj
    """
    for posamezn in tabela_grafov:
        cas = time.time()

        st_vozlisc, st_povezav, matrika = sestavi_matriko(posamezn)
        testni = Graf(st_vozlisc)
        testni.graf = matrika

        print(f"Pretvorba iz datoteke v graf traja: {time.time() - cas} sekund")


        cas = time.time()
        testni.prim()

        print(f"Delovanje Primovega algoritma za {st_vozlisc} vozlišč in {st_povezav} povezav vzame: {time.time() - cas} sekund")
        print("---------------------------------------------------------------------------")

#largeEWG.txt je izpuscen, saj dela vse predolgo
vsi_grafi = ["tinyEWG.txt", "mediumEWG.txt", "1000EWG.txt", "10000EWG.txt"]
preveri_razlicne_grafe(vsi_grafi)