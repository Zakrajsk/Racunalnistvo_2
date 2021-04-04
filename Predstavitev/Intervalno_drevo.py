class Vozel:
    def __init__(self, interval):
        self.interval = interval
        self.max = max(interval)
        self.levo = None
        self.desno = None

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, interval):
        self._interval = interval

    @property
    def max(self):
        return self._max
    
    @max.setter
    def max(self, max):
        self._max = max

    @property
    def levo(self):
        return self._levo

    @levo.setter
    def levo(self, levo):
        self._levo = levo

    @property
    def desno(self):
        return self._desno

    @desno.setter
    def desno(self, desno):
        self._desno = desno

    def __str__(self):
        """
        Izpis posameznega vozla
        """
        return f"{self.interval}, max: {self.max}"

    def izpis(self, nivo=0):
        """
        Funkcija za izpis celotnega drevesa v stilu:
        Oce
        :    :levisin
        :    :    :levi sin levega sina
        :    :    :desni sin levega sina
        :    :desnisin
        :    :    :levi sin desnega sina
        :    :    :desni sin desnegea sina
        """
        niz = "\t:" * nivo + str(self) + "\n"
        
        if (self.levo == None and self.desno == None): #imamo list
            return niz

        if self.levo != None:
            niz += self.levo.izpis(nivo + 1)
        else:
            niz += "\t:" * (nivo + 1) + "None\n"

        if self.desno != None:
            niz += self.desno.izpis(nivo + 1)
        else:
            niz += "\t:" * (nivo + 1) + "None\n"

        return niz

class Intervalno_drevo:
    def __init__(self, koren=None):
        self.koren = koren

    @property
    def koren(self):
        return self._koren
    
    @koren.setter
    def koren(self, koren):
        self._koren = koren


    def get_koren(self):
        return self.koren

    def ali_je_prazno(self):
        """
        Vrne true ce je drevo prazno
        """
        return self.koren == None

    def izpis(self):
        """
        Funkcija za izpis
        """
        if self.koren == None:
            print("PRAZNO")
        else:
            print(self.koren.izpis())

    @staticmethod
    def osvezi_max(kje):
        """
        Funckija se sprehodi po drevesu in spremeni vse max vrednost pri vozliscih, ki so napacni
        """
        if kje == None: #ni kaj za urejati
            return

        if kje.levo == None and kje.desno == None:
            kje.max = max(kje.interval)

        elif kje.levo == None:
            kje.max = max(max(kje.interval), Intervalno_drevo.osvezi_max(kje.desno))

        elif kje.desno == None:
            kje.max = max(max(kje.interval), Intervalno_drevo.osvezi_max(kje.levo))
        else:
            kje.max = max([max(kje.interval), Intervalno_drevo.osvezi_max(kje.levo), Intervalno_drevo.osvezi_max(kje.desno)])
        return kje.max
        


    def vstavi(self, interval):
        """
        Vstavi nov vozel z intervalom na pravilno mesto,
        Ob tem tudi spreminja max vrednost pri tistih, ki imajo max vrednost manjso od novega intervala
        """

        nov_vozel = Vozel(interval)
        if self.koren == None:
            self.koren = nov_vozel
            return
        
        poz = self.koren
        while True: #dokler ga ne vstavimo

            if poz.max < nov_vozel.max:
                poz.max = nov_vozel.max

            if nov_vozel.interval[0] < poz.interval[0]: #pogledamo ali moramo levo ali desno
                if poz.levo == None: #Ce je prazen ga lahko dodamo
                    poz.levo = nov_vozel
                    break
                poz = poz.levo
            else:
                if poz.desno == None:
                    poz.desno = nov_vozel
                    break
                poz = poz.desno

    def izbrisi(self, za_izbris):
        """
        V drevesu poisce interval, in ga izbrise, pri tem ohrani vsa pravila
        """

        #iskanje intervala
        poz = self.koren
        prejsni = None #zaenkrat koren nima starsa

        while True:
            if poz == None: #nismo nasli intervala in zato zakljucimo
                return 
            if poz.interval == za_izbris: #nasli interval in ga zapisali v poz
                break
            if poz.interval[0] < za_izbris[0]: #preverimo ali moramo levo ali desno
                prejsni = poz #za hranjenje prejsnega da lahko izbrisemo samo list
                gremo_desno = True #ali gremo levo ali desno (da vemo ker list potrebno izbrisati)
                poz = poz.desno
            else:
                prejsni = poz
                gremo_desno = False
                poz = poz.levo

        #menjava najdenega intervala z najmanjsim listom v poddrevesu tega intervala
        #nima sinov 
        if poz.levo == None and poz.desno == None:
            if prejsni == None: #brisemo koren brez sinov, zato samo nastavimo koren na None
                self.koren = None
                return

            if gremo_desno:
                prejsni.desno = None
            else:
                prejsni.levo = None

        #ima samo sina na levi
        elif poz.levo != None and poz.desno == None:
            poz.interval = poz.levo.interval
            poz.desno = poz.levo.desno
            poz.levo = poz.levo.levo

        #ima samo sina na desni
        elif poz.desno != None and poz.levo == None:
            poz.interval = poz.desno.interval
            poz.levo = poz.desno.levo
            poz.desno = poz.desno.desno

        #ima oba sina gremo v desno poddrevo in potem samo v levo dokler se da
        else:
            #najdemo najmanjsega
            menjalni = poz.desno
            prejsni = menjalni
            gremo_levo = False
            while menjalni.levo != None:# dokler imam leve sinove gremo levo
                prejsni = menjalni
                gremo_levo = True
                menjalni = menjalni.levo
            poz.interval = menjalni.interval
            if gremo_levo:
                prejsni.levo = None
            else:
                poz.desno = menjalni.desno
                prejsni.desno = None
        
        #osvezimo max pri drevesih
        Intervalno_drevo.osvezi_max(self.koren)


    def brisanje_dela_intervala(self, del_intervala):
        """
        Iz vseh intervalov, ki se prekrivajo z podanim delom izbrisemo tako, da noben interval vec ne bo vseboval tega intervala
        """
        #poiscemo vse ki se prekrivajo

        prekrivajoci = Vsi_prekrivajoci(self.koren, del_intervala)

        #vse 4 razlicne moznosti  (zaobjame, iz desne, iz leve, je vsebovan)

        for posamezen in prekrivajoci:
            #ali del intervala, ki ga brisemo vsebuje celoten interval [del_intervala[osnovni]del_intervala]
            #izbrisemo celotni
            if del_intervala[0] <= posamezen.interval[0] and del_intervala[1] >= posamezen.interval[1]:
                self.izbrisi(posamezen.interval)
                self.izpis()
            
            #ali se prekrivata na desni [del_intervala][osnovni]
            if del_intervala[0] <= posamezen.interval[0] and del_intervala[1] <= posamezen.interval[1]:
                posamezen.interval = [del_intervala[1] + 1, posamezen.interval[1]]

            #ali se prekrivata na levi [osnovni][del_intervala]
            if del_intervala[0] >= posamezen.interval[0] and del_intervala[1] >= posamezen.interval[1]:
                posamezen.interval = [posamezen.interval[0], del_intervala[0] - 1]

            #ali vsebuje interval vsebuje celoten del intervala, ki ga brisemo  [osnivni [del_intervala] osnovni]
            #enega spremenimo na [osnovni[0], del_intevala[0]] in vstavimo se [del_intervala[1], osnovni[1]]
            if del_intervala[0] > posamezen.interval[0] and del_intervala[1] < posamezen.interval[1]:
                self.vstavi([del_intervala[1] + 1, posamezen.interval[1]])
                posamezen.interval = [posamezen.interval[0], del_intervala[0] - 1]


    def vstavi_z_zlivanjem(self, nov_interval):
        """
        Vstavi nov interval tako, da v drevesu kjer nimamo prekrivajočih se intervalov najprej izbriše tiste katere bi prekrival in nato
        vstavi enega samega, ki zajema vse izbrisane intervale in tudi novega [min_vseh_izbrisanih, max_vseh_izbrisanih]
        """
        #Najdemo vse ki se prekrivajo
        tabela_prekrivajocih = Vsi_prekrivajoci(self.koren, nov_interval)

        #najdemo min pa max vseh vozlisc
        najmanjsi = min(nov_interval)
        najvecji = max(nov_interval)

        for posamezni in tabela_prekrivajocih:
            kan_min, kan_max = posamezni.interval
            #zamenjamo ce smo nasli vecjega ali manjsega
            najmanjsi = min(kan_min, najmanjsi)
            najvecji = max(kan_max, najvecji)
            #izbrisemo prekrivajoce
            self.izbrisi(posamezni.interval)

        #vstavimo novemga [min, max]
        self.vstavi([najmanjsi, najvecji])

            
            

def ali_se_prekrivata(prvi_interval, drugi_interval):
    """
    Vrne true, ce se intervala prekrivata
    """
    return min(prvi_interval[1], drugi_interval[1]) - max(prvi_interval[0], drugi_interval[0]) >= 0


def Prekrivanje_z_intervalom(poz, iskan_interval):
    """
    Fukcija poisce interval, ki se prekriva z podanim
    Vrne prvega (najvisjega), ki se pojavi v drevesu
    """
    if poz == None or min(iskan_interval) > poz.max: #intervala nismo nasli
        return None

    if ali_se_prekrivata(poz.interval, iskan_interval):
        return poz
    
    if max(iskan_interval) <= poz.levo.max:
        return Prekrivanje_z_intervalom(poz.levo, iskan_interval)
    else:
        return Prekrivanje_z_intervalom(poz.desno, iskan_interval)

        
def Vsi_prekrivajoci(poz, iskan_interval):
    """
    Funkcija poisce in vrne tabelo vseh intervalov, ki se prekrivajo z podanim
    """
    if poz == None: # ce imamo slucajno prazno drevo
        return []
    
    levo_pod = []
    desno_pod = []
    #levo poddrevo
    if poz.levo != None and poz.levo.max >= min(iskan_interval): #ali je moznost, da je v levem poddrevesu se kaksen prekrivajoc
        levo_pod = Vsi_prekrivajoci(poz.levo, iskan_interval)
    
    if poz.desno != None and poz.desno.max >= min(iskan_interval): #ali je moznost, da je v desnem poddrevesu se kaksen prekrivajoc
        desno_pod = Vsi_prekrivajoci(poz.desno, iskan_interval)

    #desno poddrevo
    if ali_se_prekrivata(poz.interval, iskan_interval): #se prekrivata in ga dodamo
        return [poz] + levo_pod + desno_pod
    return levo_pod + desno_pod






test = Intervalno_drevo(Vozel([10, 30]))
test.vstavi([50, 60])
test.vstavi([70, 90])
test.vstavi([65, 80])
test.vstavi([5, 20])
test.vstavi([3, 50])
test.vstavi([80, 100])
test.vstavi([4, 20])
test.vstavi([20, 40])
test.vstavi([15, 20])

test.izpis()

print("-------------------Prvi prekrivajoci-------------------")

ye = Prekrivanje_z_intervalom(test.get_koren(), [45, 46])
print(ye)

print("-------------------Vsi prekrivajoci-------------------")

vsi = Vsi_prekrivajoci(test.get_koren(), [21, 66])
for en in vsi:
    print(en)


print("-------------------Brisanje-------------------")
#test.izbrisi([50, 60])

test.izpis()


print("-------------------Brisanje dela intervala-------------")

test.brisanje_dela_intervala([12, 42])


test.izpis()


print("-------------------Vstavljanje z zlivanjem-------------")

test_zlivanje = Intervalno_drevo(Vozel([10, 30]))
test_zlivanje.vstavi_z_zlivanjem([20, 40])
test_zlivanje.vstavi_z_zlivanjem([5, 8])
test_zlivanje.vstavi_z_zlivanjem([60, 70])
test_zlivanje.vstavi_z_zlivanjem([2, 4])
test_zlivanje.vstavi_z_zlivanjem([75, 80])

#test_zlivanje.izpis()

