from Intervalno_drevo_resitev import Vozel, Intervalno_drevo

def Preberi_datoteko(ime_datoteke):
    """
    Prebere datoteko knjizevnikov in sestavi intervalno drevo
    Podatki morajo biti navedeni tako:   ime priimek (rojstvo-smrt)
    """
    inter_drevo = Intervalno_drevo()
    
    for posamezni in open(ime_datoteke, encoding="utf-8"):
        ime, pribl_interval = posamezni.split("(")
        interval = list(map(int, pribl_interval.strip()[:-1].split("-"))) #strip za whitespace in potem se -1 da odmaknemo oklepaj
        inter_drevo.vstavi(interval, ime)
    
    return inter_drevo

def Izbrisi_dopuste(drevo_delavcev, od, do):
    """
    Vsem delavcev v drevesu izbrise dopuste za datume [od do].
    Osebam, ki se prekrivajo z tem datumom samo iz ene strani samo skrajša dopust
    Osebam, ki pa imajo dopust tako, da zaobjame podan datum pa naredi dva krajša dopusta
    Osebam, ki imajo dopust med tema datuma, pa jim celotni dopust zbriše
    """
    drevo_delavcev.brisanje_dela_intervala([od, do])


def St_ljudi_na_dopustu(drevo_delavcev):
    """
    Vrne tabelo za vse dni, ki nam pove koliko ljudi je tisti dan na dopustu
    """
    tabela_dopustov = list()
    for i in range(1, 32):
        koliko = drevo_delavcev.Vsi_prekrivajoci([i, i])
        tabela_dopustov.append(len(koliko))

    return tabela_dopustov

generirano_drevo = Preberi_datoteko("Delavci.txt")
generirano_drevo.izpis()

Izbrisi_dopuste(generirano_drevo, 10, 15)

generirano_drevo.izpis()
print(St_ljudi_na_dopustu(generirano_drevo))