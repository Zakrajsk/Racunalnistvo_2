# Vaje 14.4.2022 Minimalna vpeta drevesa 2

**Ime:** Gal Zakrajšek

**Datum:** 21.04.2022

---


Na vajah smo se razdelili v skupine in med sabo tekmovali kdo bo rešil določene naloge iz teme minimalnih vpetih dreves. Vsaka skupina si je izbrala en algoritem za reševanje problema.


## Komentarji in opombe

Vaje so bile zabavne, saj je bilo tekmovanje zelo napoto, saj so obe skupine dobile rezultate v zelo podobnih časih. 


## Minimalna vpeta drevesa

Za reševanje problemov, smo si v skupini izrabli Primov algoritem. Ki smo ga implementirali tako.

```python
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
```

Kasneje smo tekmovali v naslednjih vprašanjih:

1. Najti ceno minimalnega vpetega drevesa (drevo, ki povezuje vse točke).\
    Ceno smo našli brez problema, saj smo samo pognali naš algoritem.

2. Dovolimo dodatek ene točke. Poiščite točko s katero čim bolj znižate ceno MVD.\
    Najprej smo poskušali čisto naključno dodajati točko v graf, potem pa smo se lotili tega bolj postopoma. Naredili smo mrežo točk in za vsako preverili novo ceno MVD. Na koncu smo dobili ceno najmanjšega in pa točko z katero smo to dosegli. Potem smo okoli te točke spet naredili mrežo točk, ki so bile zdaj bolj gosto skupaj in tako spet izboljšali MVD. Postopek smo en čas ponavljali, dokler nismo prišli do željene natančnosti.

3. Dovolimo dodatek 5 točk. Poiščite take točke, ki čim bolj znižajo ceno MVD.
4. Dodajte do največ n točk, ki čim bolj znižajo ceno.

3 in 4 točko smo samo malo pokomentirali, saj ni bilo časa.












