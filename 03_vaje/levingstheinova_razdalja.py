import time
from functools import lru_cache

def levingsteinova_razdalja(niz_1, niz_2):
    
    @lru_cache(maxsize=None)
    def primerjaj(i, j):
        '''
            primerja i-ti in j-ti elt
        '''
        # zaustavitveni pogoj
        if i >= len(niz_1) and j >= len(niz_2):
            return 0

        # konec enega izmed nizov
        if i >= len(niz_1) and j < len(niz_2):
            # niz_1 je prazen, niz_2 ni prazen
            return len(niz_2) - j
        if i < len(niz_1) and j >= len(niz_2):
            # niz_2 je prazen, niz_1 ni prazen
            return len(niz_1) - i

        # znaka sta enaka => primerjamo naslednja
        if niz_1[i] == niz_2[j]:
            return primerjaj(i + 1, j + 1)

        # vemo, da sta znaka različmna

        # (1.) ohranimo samo niz_1[i]
        ohranimo_i = 1 + primerjaj(i, j + 1)

        # (2.) ohranimo samo niz_2[j]
        ohranimo_j = 1 + primerjaj(i + 1, j)

        # (3.) zamenjamo znaka
        zamenjamo = 1 + primerjaj(i + 1, j + 1)

        return min(ohranimo_i, ohranimo_j, zamenjamo)

    return primerjaj(0, 0)


if __name__ == '__main__':

    zac = time.time()
    for _ in range(100):
        levingsteinova_razdalja("ab" * 100, "cd" * 100)


    konc = time.time() - zac
    print(konc / 100)


    #print(f'ornitologija : otorinolaringolog = {levingsteinova_razdalja("ornitologija" * 420, "otorinolaringolog" * 60)}')
    #print(f'borba : torba = {levingsteinova_razdalja("borba", "torba")}')
    #print(f'abc : a = {levingsteinova_razdalja("abc", "a")}')
    #print(f'ornitologija : otorinolaringologija = {print(levingsteinova_razdalja("Donaudampfschiffahrtselektrizitätenhauptbetriebswerkbauunterbeamtengesellschaft", "Donaudampfschifffahrtsgesellschaftskapitän"))}')
    