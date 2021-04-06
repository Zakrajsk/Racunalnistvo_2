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

def Najbolj_ustvarjalno_leto(drevo_ustvarjalcev, od, do):
    """
    Poisce v katerem letu, je bilo najvec ustvarjalcev živih med letoma od in do
    """
    najbolj = 0  #koliko zivih
    katero = None  #katero leto

    for i in range(od, do + 1):
        koliko = drevo_ustvarjalcev.Vsi_prekrivajoci([i, i])
        if len(koliko) > najbolj:
            najbolj = len(koliko)
            katero = i
    
    return najbolj, katero


generirano_drevo = Preberi_datoteko("Slovenski_knjizevniki.txt")


koliko, kdaj = Najbolj_ustvarjalno_leto(generirano_drevo, 1500, 2000)
print(f"Najbolj aktivno leto je bilo: {kdaj}. Ustvarjalcev je bilo takrat: {koliko}")
