import math
from tkinter import Label

def preberiTocke(ime_datoteke):
    """
    """
    tocke = list()
    with open(ime_datoteke, "r") as f:
        for line in f.readlines():
            x, y = map(float, line.split(";"))
            tocke.append((x, y))
    return tocke


def evklid(tocka1, tocka2):
    """
    """
    rzd = math.sqrt((tocka1[0] - tocka2[0])**2 + (tocka1[1] - tocka2[1])**2)
    return rzd if rzd != 0 else float("inf")


def matrikaRazdalij(tocke):
    """
    Vrne matriko sosednosti
    """
    matrika = list()
    for ena in tocke:
        povezave = list()
        for druga in tocke:
            povezave.append(evklid(ena, druga))
        matrika.append(povezave)
    
    return matrika


def prim(tocke):
    """
    Primov algoritem
    """
    matrika = matrikaRazdalij(tocke)
    n = len(tocke)
    drevo_indeksi = [0] #vozlisca, ki so ze bila obravnavana
    koncna_cena = 0
    for i in range(1, n):

        najkrajsa = float("inf")
        for vozlisce in drevo_indeksi:
            for i, cena in enumerate(matrika[vozlisce]):
                #iscemo minimum v matriki
                if i in drevo_indeksi:
                    continue
                if cena < najkrajsa:
                    najkrajsa = cena
                    najblizje_vozlisce = i
        drevo_indeksi.append(najblizje_vozlisce)
        koncna_cena += najkrajsa

    return drevo_indeksi, koncna_cena

def randomTocka(tocke):
    """
    """
    min_tocka = 0
    min_rzd = float("inf")
    min_x = min(tocke, key=lambda x: x[0])[0]
    max_x = max(tocke, key=lambda x: x[0])[0]
    min_y = min(tocke, key=lambda y: y[1])[1]
    max_y = max(tocke, key=lambda y: y[1])[1]
    for x in range(int(min_x), int(max_x) + 1):
        for y in range(int(min_y), int(max_y) + 1):
            pot, rzd = prim(tocke + [(x, y)])
            if rzd < min_rzd:
                min_rzd = rzd
                min_tocka = (x, y)
                print(min_rzd, min_rzd, x, y)
            if x == 100:
                print(x, y)
    return min_rzd, min_tocka

def Liam(tocke, natancnost):
    """
    """
    min_tocka = 0
    min_rzd = float("inf")
    min_x = min(tocke, key=lambda x: x[0])[0]
    max_x = max(tocke, key=lambda x: x[0])[0]
    min_y = min(tocke, key=lambda y: y[1])[1]
    max_y = max(tocke, key=lambda y: y[1])[1]
    for x in range(int(min_x), int(max_x) + 1, natancnost):
        for y in range(int(min_y), int(max_y) + 1, natancnost):
            pot, rzd = prim(tocke + [(x, y)])
            if rzd < min_rzd:
                min_rzd = rzd
                min_tocka = (x, y)
                print(min_rzd, min_rzd, x, y)
    return min_rzd, min_tocka

def okoliEne(tocke, min_x, max_x, min_y, max_y, natancnost):
    """
    """
    if natancnost < 1:
        faktor = 10
    else:
        faktor = 1
    min_tocka = 0
    min_rzd = float("inf")
    for x in range(int(min_x * faktor), int((max_x + 1) * faktor), 1):
        for y in range(int(min_y * faktor), int((max_y + 1)  * faktor), 1):
            x = x * 0.1
            y = y * 0.1
            pot, rzd = prim(tocke + [(x, y)])
            if rzd < min_rzd:
                min_rzd = rzd
                min_tocka = (x, y)
                print(min_rzd, min_tocka)
    return min_rzd, min_tocka



def main(ime_datoteke):
    """
    """
    tocke = preberiTocke(ime_datoteke)
    #print(Liam(tocke, 25))
    #print(okoliEne(tocke, 400, 472, 260, 320, 1))
    print(okoliEne(tocke, 429, 431, 281, 283, 0.1))


if __name__ =="__main__":
    main("primer2.txt")