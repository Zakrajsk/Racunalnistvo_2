# Vaje 24. 02, Dinamično programiranje 2

**Ime:** Gal Zakrajšek

**Datum:** 24.02.2021

---

Pri vajah smo obravnavali problem množenja matrik. Pogledali smo kako se problem reši rekurzivno in dinamčno z pisanjem v tabelo. Potem smo odgovarjali na par vprašanj povezanih z našim problemom. Proti koncu smo na Tomo-tu reševali naloge.


## Komentarji in opombe

Na vajah mi je bila všeč razlaga problema, saj smo si res vzeli čas in se posvetili.


## Pomemnba vprašanja, ki smo jih obravnavali na vajah
Na vajah smo obravnavali množenje matrik in pa na tomotu smo se lotili naloge postavljanja oklepajev.
Skupaj smo prišli do Bellmanove enačbe pri Matričnem množenju, ki je naslednja:\

$N(i, j) = Optimalno\ število\ operacij\ za\ izračun\ produkta$\
$N(i,j) = Min_{(k= i,...,j)}(N(i, k) + N(k+1, j) + d_{i} * d_{j+1} * d_{k+1})$\
$N(i, i) = 0$

### Kako dobiti število vseh optimalnih produktov
Privzamimo, da imamo funckijo, ki nam napolni tabelo z optimalnim številom produktov in zraven pove tudi, kje so bili tedaj postavljeni oklepaji (k, pri katerem je bilo operacij najmanj). Potem lahko začenmo iz zgornjega desnega kota, kjer je tudi končen rezultat. Pomikamo se po tabeli tako, kot nam povejo k-ji. Sproti beležimo koliko k-jev je bilo pri posameznem delu (To nam pove tudi na koliko načinov se pride do tistega rezultata katerega trenutno gledamo). Ko pridemo do konca lahko pomnožimo kolikor možnosti smo pri vsakem delčku našli in tako dobimo število vseh optimalnih produktov. 

### Kako izpisati vse te optimalne produkte
Za izpis produktov ponovno predpostavimo, da imamo funkcijo opisano pri zgornjem vprašanju. Spet začnemo iz končnega rezultata in konstruiramo toliko različnih postavitev oklepajev, kolikor je različnih k-jev pri katerih smo dobili optimalno število operacij. Če imamo naprimer dva k-ja, potem dosedanji izraz podvojimo in ekrat postavimo oklepaj pri prvem k-ju drugič pa pri drugem. Seveda moramo potem tudi naprej v tabeli iskati za obe možnosti.

### Kaj lahko poveš v primeru, ko so vse matrike kvadratne
Ko so vse matrike kvadratne je vrstni red nepomemben, saj bo vedno enaka dimenzija kakorkoli začnemo množiti. Zato bo tudi končno število operacij vedno enako.

### Kako bi algoritem poganjali na več računalnikih
Do ideje smo prišli na vajah in sicer si predstavljamo drevo, kjer imamo kot elemente operatorje(pri nas samo množenja) in matrike. Seveda to drevo konstruiramo po tem ko smo izračunali optimalno zaporedje množenj, da v naprej vemo kako razvejati drevo. Iz drevesa je razvidno katere operacije so neodvisne od ostalih (tiste, ki imajo po dva lista) in ravno te bi lahko izračunali na večih računalnikih in tako sočasno rešili več operacij in zmanjšal čas celotnega računa.

### Kaj moramo na novo izračunati ob manjši spremembi vhodnih podatkov
Spremenimo naprimer zadnjo dimenzijo matrike, seveda mora ostati tako, da je še vedno možno zmnožiti predzadnjo in zadnjo. Vse kar rabimo popraviti pri naši tabeli optimalnih operacij je zadnji stolpec. 

### Problem rezanja palice.
Režemo palice na k delov. Celotna dolžina je L.\
Cena reza je dolžina palice, ki jo trenutno režemo.\
Problem je zelo podoben kot naš problem množenja matrik. Tukaj namesto števila operacij pri množenju matrik pišemo ceno reza. Ostalo pa je enako

---

# Postavljanje oklepajev

## 1. Part

**Navodilo:** Sestavi rekurzivno funkcijo **oklepaji(izraz)**, ki sprejme niz **izraz**, v katerem nastopajo cela števila in računske operacije seštevanje, odštevanje, množenje in deljenje(števila in operatorji so ločeni s presledkom) ter vrne par **(najvecja, najmanjsa)**, kjer 'najvecja' predstavlja največjo vrednost, ki jo lahko dobimo, če v izrazu dodamo oklepaje, 'najmanjsa' pa najmanjšo vrednost, ki jo lahko dobimo, če v izrazu dodamo oklepaje. Primer:
```python
>>> oklepaji('1 + 5 * 6 - 3')
(33, 16)
```
Največjo vrednost dosežemo z izrazom $((1 + 5) * 6) - 3,$ najmanjšo pa z $1 + (5 * (6 - 3))$.

Spodaj je že napisan del kode. Ustrezno ga dopolni. Mesta, kjer je potrebno kaj dopisati so označena z ###.

**Rešitev:**
```python
def oklepaji(izraz):
    ''' rekurzivno poišče največjo in najmanjšo vrednost, ki ju lahko dosežemo
    z dodajanjem oklepajev izrazu izraz '''
    if not izraz:  # izraz je prazen niz
        return (0, 0)
    izraz = izraz.split()  # sestavimo seznam števil in operatorjev
    if len(izraz) == 1:  # izraz vsebuje le eno število
        return (int(izraz[0]), int(izraz[0]))
    n = len(izraz) // 2  # število operatorjev, ki nastopa v izrazu
    najvecja = -float('inf')
    najmanjsa = float('inf')
    for i in range(n):
        op = izraz[2*i+1]
        levo_max, levo_min = oklepaji(' '.join(izraz[:2*i+1]))
        desno_max, desno_min = oklepaji(' '.join(izraz[2*i+2:]))

        max_max = str(levo_max) + op + str(desno_max)
        min_min = str(levo_min) + op + str(desno_min)
        min_max = str(levo_min) + op + str(desno_max)
        max_min = str(levo_max) + op + str(desno_min)

        max_vrednost = eval(max(max_max, max_min, min_min, min_max, key=lambda x: eval(x)))
        min_vrednost = eval(min(max_max, max_min, min_min, min_max, key=lambda x: eval(x)))

        if max_vrednost > najvecja:
            najvecja = max_vrednost
        if min_vrednost < najmanjsa:
            najmanjsa = min_vrednost
    return najvecja, najmanjsa
```

**Komentar:**
Nisem imel posebnih težav. Koda je bila napol že napisana, zato sem dokaj hitro našel rešitev. Ker je rešitev rekurzivna izvajanje ni ravno najhitrejše.\
Ocenjena časovna zahtevnost: $O(2^n)$


**Testi**
Testi so bili že narejeni preko Tomota.


## 2. Part

**Navodilo:** Sestavi funkcijo **oklepaji_dinamicno(izraz)**, ki sprejme niz **izraz**, v katerem nastopajo cela števila in računske operacije seštevanje, odštevanje, množenje in deljenje(števila in operatorji so ločeni s presledkom) ter vrne par **(najvecja, najmanjsa)**, kjer 'najvecja' predstavlja največjo vrednost, ki jo lahko dobimo, če v izrazu dodamo oklepaje, 'najmanjsa' pa najmanjšo vrednost, ki jo lahko dobimo, če v izrazu dodamo oklepaje. Nalogo reši z dinamičnim programiranjem. Primer:
```python
>>> oklepaji_dinamicno('1 + 5 * 6 - 3')
(33, 16)
```
Največjo vrednost dosežemo z izrazom $((1 + 5) * 6) - 3,$ najmanjšo pa z $1 + (5 * (6 - 3))$.

Spodaj je že napisan del kode. Ustrezno ga dopolni. Mesta, kjer je potrebno kaj dopisati so označena z ###.

**Rešitev:**
```python
def oklepaji_dinamicno(izraz):
    ''' poišče največjo in najmanjšo vrednost, ki ju lahko dosežemo
    z dodajanjem oklepajev izrazu izraz '''
    if not izraz:
        return 0, 0
    izraz = izraz.split()
    n = len(izraz) - (len(izraz) // 2)  # število števil, ki nastopa v izrazu
    vrednosti = [[[0, 0] for _ in range(n)] for _ in range(n)]

    # napolnimo glavno diagonalo
    for i in range(n): 
        vrednosti[i][i] = (int(izraz[2 * i]),int(izraz[2 * i]))
    
    # polnimo po naddiagonalah
    for i in range(1, n):  # katera naddiagonala
        for k in range(n-i):  # kateri zaporedni elt v naddiagonali
            najvecja = -float('inf')
            najmanjsa = float('inf')
            for j in range(i): # pogledamo vse mozne variante v nasi tabeli
                levo_max, levo_min = vrednosti[k][k + j] 
                desno_max, desno_min = vrednosti[k + j + 1][i + k]
                #ustrezen predznak
                op = izraz[2*(j + k) + 1]
                
                max_max = str(levo_max) + op + str(desno_max)
                min_min = str(levo_min) + op + str(desno_min)
                min_max = str(levo_min) + op + str(desno_max)
                max_min = str(levo_max) + op + str(desno_min)

                max_vrednost = eval(max(max_max, max_min, min_min, min_max, key=lambda x: eval(x)))
                min_vrednost = eval(min(max_max, max_min, min_min, min_max, key=lambda x: eval(x)))

                #iscemo najvecjo in najmanjso vrednost
                if max_vrednost > najvecja:
                    najvecja = max_vrednost
                if min_vrednost < najmanjsa:
                    najmanjsa = min_vrednost
            vrednosti[k][i + k] = (najvecja, najmanjsa)  ### dopolni z ustreznimi indeksi

    return tuple(vrednosti[0][-1])
```

**Komentar:**
Težave sem imel samo z lenobo, saj sem sprva probal v glavi ustvarit tabelo in sem malo "ugibal" kako se premikamo po njej. Ko pa sem si narisal in malo bolje premislil pa nisem imel težav pri reševanju. Ideja algoritma je, da z pomočjo dinamičnega programiranja in dodatne tabele beležimo rezultate iz prejšne iteracije. Tako lahko hitreje rešimo naš problem kot pa z rekurzijo iz podnaloge 1. Ko imamo napolnjeno tabelo, lahko razberemo rezultat na spodnjem desnem mestu.\
Ocenjena časovna zahtevnost: $O(n^3)$

**Testi**
Testi so bili že narejeni preko Tomota.


## 3. Part

**Navodilo:** Sestavi funkcijo **oklepaji_izraz(izraz)**, ki sprejme niz **izraz**, v katerem nastopajo cela števila in računske operacije seštevanje, odštevanje, množenje in deljenje(števila in operatorji so ločeni s presledkom) ter vrne tisti izraz z oklepaji, kateraga vrednost je največja možna. Nalogo reši z dinamičnim programiranjem. Primer:
```python
>>> oklepaji_izraz('1 + 5 * 6 - 3')
'((1 + 5) * 6) - 3'
>>> oklepaji_izraz('1 + 3')
'1 + 3'
```
Najbolj zunanjih oklepajev ne izpisuj!

Kode ne piši na novo, ampak preuredi rešitev prejšnje podnaloge.

**Rešitev:**
```python
def oklepaji_izraz(izraz):
    ''' poišče največjo in najmanjšo vrednost, ki ju lahko dosežemo
    z dodajanjem oklepajev izrazu izraz '''
    if not izraz:
        return ''
    izraz = izraz.split()
    n = len(izraz) - (len(izraz) // 2)  # število števil, ki nastopa v izrazu
    vrednosti = [[[0, 0, "", ""] for _ in range(n)] for _ in range(n)]

    # napolnimo glavno diagonalo
    for i in range(n): 
        vrednosti[i][i] = (int(izraz[2 * i]),int(izraz[2 * i]), str(izraz[2 * i]), str(izraz[2 * i]))
    
    # polnimo po naddiagonalah
    for i in range(1, n):  # katera naddiagonala
        for k in range(n-i):  # kateri zaporedni elt v naddiagonali
            najvecja = -float('inf')
            najmanjsa = float('inf')
            for j in range(i): # pogledamo vse mozne variante v nasi tabeli
                levo_max, levo_min, levo_max_izraz, levo_min_izraz = vrednosti[k][k + j] 
                desno_max, desno_min, desno_max_izraz, desno_min_izraz = vrednosti[k + j + 1][i + k]
                #ustrezen predznak
                op = izraz[2*(j + k) + 1]
                
                max_max = str(levo_max) + " " + op +  " " + str(desno_max)
                min_min = str(levo_min) + " " + op +  " " + str(desno_min)
                min_max = str(levo_min) + " " + op +  " " + str(desno_max)
                max_min = str(levo_max) + " " + op +  " " + str(desno_min)

                #Generiramo vse mmozne izraze
                max_max_izraz = (("(" + levo_max_izraz + ") ") if len(levo_max_izraz.split(" ")) > 1 else (levo_max_izraz + " ")) + op +  ((" (" + desno_max_izraz + ")") if len(desno_max_izraz.split(" ")) > 1 else (" " + desno_max_izraz))
                min_min_izraz = (("(" + levo_min_izraz + ") ") if len(levo_min_izraz.split(" ")) > 1 else (levo_min_izraz + " ")) + op +  ((" (" + desno_min_izraz + ")") if len(desno_min_izraz.split(" ")) > 1 else (" " + desno_min_izraz))
                min_max_izraz = (("(" + levo_min_izraz + ") ") if len(levo_min_izraz.split(" ")) > 1 else (levo_min_izraz + " ")) + op +  ((" (" + desno_max_izraz + ")") if len(desno_max_izraz.split(" ")) > 1 else (" " + desno_max_izraz))
                max_min_izraz = (("(" + levo_max_izraz + ") ") if len(levo_max_izraz.split(" ")) > 1 else (levo_max_izraz + " ")) + op +  ((" (" + desno_min_izraz + ")") if len(desno_min_izraz.split(" ")) > 1 else (" " + desno_min_izraz))

                #najdemo najvecjo in najmanjso kombinacijo
                max_izraz = max(max_max_izraz, max_min_izraz, min_min_izraz, min_max_izraz, key=lambda x: eval(x))
                min_izraz = min(max_max_izraz, max_min_izraz, min_min_izraz, min_max_izraz, key=lambda x: eval(x))
                max_vrednost = eval(max(max_max, max_min, min_min, min_max, key=lambda x: eval(x)))
                min_vrednost = eval(min(max_max, max_min, min_min, min_max, key=lambda x: eval(x)))

                #iscemo najvecjo in najmanjso vrednost
                if max_vrednost > najvecja:
                    najvecja = max_vrednost
                    max_izraz_z_oklepaji = max_izraz
                if min_vrednost < najmanjsa:
                    najmanjsa = min_vrednost
                    min_izraz_z_oklepaji = min_izraz
            vrednosti[k][i + k] = (najvecja, najmanjsa, max_izraz_z_oklepaji, min_izraz_z_oklepaji)

    return vrednosti[0][-1][2]
```

**Komentar:**
Posebnih težav nisem imel. Naloge sem se lotil tako, da moja funkcija že sproti v tabelo zapisuje tudi izraz z katerim je prišel do dosedanje rešitve. Ta izraz nato po iteracijah sestavlja in na koncu imamo poleg rešitve na spodnjem desnem mestu največji rezultat in pa tudi izraz z katerim smo prišli do njega.\
Ocenjena časovna zahtevnost: $O(n^3)$

**Testi**
Testi so bili že narejeni preko Tomota.
