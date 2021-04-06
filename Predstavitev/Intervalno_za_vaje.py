#Rahlo spremenjena oziroma implementacija brez vstavljanja in pa brisanja dela intervala
class Vozel:
    def __init__(self, interval, ime="Neki ni vredu"):
        self.interval = interval
        self.max = max(interval) #najvecja vrednost v intervalu v podrevesih ali v sebi 
        self.levo = None
        self.desno = None
        self.ime = ime 

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
        return f"{self.interval}, max: {self.max}, {self.ime}"

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


    def ali_se_prekrivata(self, interval):
        """
        Vrne true, ce se vozla po intervalih prekrivata
        """
        return min(self.interval[1], interval[1]) - max(self.interval[0], interval[0]) >= 0


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

        if kje.levo == None and kje.desno == None: #ali imamo se kasnega sina na katergea moremo it
            kje.max = max(kje.interval)

        elif kje.levo == None: #pogledamo ce je desno vecji element, da ga spremenimo
            kje.max = max(max(kje.interval), Intervalno_drevo.osvezi_max(kje.desno))

        elif kje.desno == None: #pogledamo ce je leo kaksen vecji element
            kje.max = max(max(kje.interval), Intervalno_drevo.osvezi_max(kje.levo))
        else: #pogledamo v obe smeri ce imamo se kaksnega vecjega in ga ustrezno spremenimo
            kje.max = max([max(kje.interval), Intervalno_drevo.osvezi_max(kje.levo), Intervalno_drevo.osvezi_max(kje.desno)])
        return kje.max #vrnemo zaradi rekurzije


    def izbrisi(self, za_izbris):
        """
        V drevesu poisce interval, in ga izbrise, pri tem ohrani vsa pravila
        """

        #iskanje intervala
        poz = self.koren
        prejsni = None #zaenkrat koren nima starsa

        while True: #delamo dokler ne najdemo intervala
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

        #v poz imamo sedaj interval ki ga brisemo, v prejsni imamo njegovega oceta in
        #ce je gremo_desno true pomeni da iz oceta.desno pridemo do poz

        #menjava najdenega intervala z najmanjsim listom v poddrevesu tega intervala
        #nima sinov zato samo izbrisemo, ker je list
        if poz.levo == None and poz.desno == None:
            if prejsni == None: #brisemo koren brez sinov, zato samo nastavimo koren na None
                self.koren = None
                return

            if gremo_desno:
                prejsni.desno = None
            else:
                prejsni.levo = None

        #ima samo sina na levi zato samo sina premaknemo gor
        elif poz.levo != None and poz.desno == None:
            poz.interval = poz.levo.interval
            #prestavimo se povezave na sinove 
            poz.desno = poz.levo.desno
            poz.levo = poz.levo.levo

        #ima samo sina na desni zato samo sina premaknemo gor
        elif poz.desno != None and poz.levo == None:
            poz.interval = poz.desno.interval
            #prestavimo se povezave na sinove
            poz.levo = poz.desno.levo
            poz.desno = poz.desno.desno

        #ima oba sina gremo v desno poddrevo in potem samo v levo dokler se da
        else:
            #najdemo najmanjsega
            menjalni = poz.desno #se premaknemo v desno poddrevo 
            prejsni = menjalni
            gremo_levo = False
            #sedaj moramo skrajno levo, da najdemo najmanjsi interval, ki pa bo ker je v desnem poddrevesu vecji od tistega ki ga brisemo
            while menjalni.levo != None:# dokler imam leve sinove gremo levo
                prejsni = menjalni
                gremo_levo = True
                menjalni = menjalni.levo
            poz.interval = menjalni.interval

            if gremo_levo: #izbrisemo se tega, ki smo ga zamenjali z brisanim
                prejsni.levo = None
            else:
                poz.desno = menjalni.desno
                prejsni.desno = None
        
        #osvezimo max pri drevesih
        Intervalno_drevo.osvezi_max(self.koren)


    def vstavi_z_zlivanjem(self, nov_interval):
        """
        Vstavi nov interval tako, da v drevesu kjer nimamo prekrivajočih se intervalov najprej izbriše tiste katere bi prekrival in nato
        vstavi enega samega, ki zajema vse izbrisane intervale in tudi novega [min_vseh_izbrisanih, max_vseh_izbrisanih]
        """
        #Najdemo vse ki se prekrivajo
        tabela_prekrivajocih = Intervalno_drevo._Vsi_prekrivajoci(self.koren, nov_interval)

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
        self.vstavi([najmanjsi, najvecji], "ime")


    @staticmethod      
    def _Prekrivanje_z_intervalom(poz, iskan_interval):
        """
        Fukcija poisce interval, ki se prekriva z podanim
        Vrne prvega (najvisjega), ki se pojavi v drevesu
        """
        if poz == None or min(iskan_interval) > poz.max: #intervala nismo nasli
            return None

        if poz.ali_se_prekrivata(iskan_interval):
            return poz
        
        if max(iskan_interval) <= poz.levo.max:
            return Intervalno_drevo._Prekrivanje_z_intervalom(poz.levo, iskan_interval)
        else:
            return Intervalno_drevo._Prekrivanje_z_intervalom(poz.desno, iskan_interval)


    def Prekrivanje_z_intervalom(self, iskan_interval):
        """
        Metoda, ki poklice staticno funkcijo za iskanje prvega prekrivanja z danim iskanim intervalom
        """
        return Intervalno_drevo._Prekrivanje_z_intervalom(self.koren, iskan_interval)


    @staticmethod
    def _Vsi_prekrivajoci(poz, iskan_interval):
        """
        Funkcija poisce in vrne tabelo vseh intervalov, ki se prekrivajo z podanim
        """
        if poz == None: # ce imamo slucajno prazno drevo
            return []
        
        levo_pod = []
        desno_pod = []
        #levo poddrevo
        if poz.levo != None and poz.levo.max >= min(iskan_interval): #ali je moznost, da je v levem poddrevesu se kaksen prekrivajoc
            levo_pod = Intervalno_drevo._Vsi_prekrivajoci(poz.levo, iskan_interval)
        
        if poz.desno != None and poz.desno.max >= min(iskan_interval): #ali je moznost, da je v desnem poddrevesu se kaksen prekrivajoc
            desno_pod = Intervalno_drevo._Vsi_prekrivajoci(poz.desno, iskan_interval)

        #desno poddrevo
        if poz.ali_se_prekrivata(iskan_interval): #se prekrivata in ga dodamo
            return [poz] + levo_pod + desno_pod
        return levo_pod + desno_pod

    def Vsi_prekrivajoci(self, iskan_interval):
        """
        Metoda, ki poklice staticno metodo in vrne tabelo vseh vozlov, kateri intervali se prekrivajo z iskanim
        """
        return Intervalno_drevo._Vsi_prekrivajoci(self.koren, iskan_interval)

