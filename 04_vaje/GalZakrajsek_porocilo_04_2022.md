# Vaje 10.3.2022 podzaporedja

**Ime:** Gal Zakrajšek

**Datum:** 13.03.2022

---

Reševanje nalog o najdaljših podzaporedjih na tomotu.


## Komentarji in opombe

Vaje so bile dobre, hitro smo ugotovili osnovno idejo in je bilo reševanje dokaj lahko.


## Pomemnba vprašanja, ki smo jih obravnavali na vajah
Pri vajah smo obravnavali problem podzaporedij. Na tomotu smo reševali različne naloge, kot so vrniti dolžino najdaljšega zaporedja (rekurzivno in dinamično), vrniti elemente, ki sestavljajo največje zaporedje. Potem pa tudi razne variacije le tega, vrniti najdaljše elemente samih lihih elementov oziroma izmenjajoče lihih in sodih elementov.

---

# Najdaljše padajoče podzaporedje

## 1. Part

**Navodilo:** Sestavi rekurzivno funkcijo **padajoce_podzaporedje_rekurzivno(zaporedje)**, ki za dano zaporedje vrne dolžino najdaljšega padajočega podzaporedja.

Kako lahko pospešimo delovanje funkcije?

**Rešitev:**
```python
def padajoce_podzaporedje_rekurzivno(zaporedje):
    """
    Za dano zaporedje vrne dolžino najdaljšega padajočega podzaporedja.
    """
    def najdaljse_padajoce(i=0, prej=float("inf")):
        if i == len(zaporedje):
            return 0

        # Izpustimo obravnavanega
        izpusti = najdaljse_padajoce(i + 1, prej)

        # Vzamemo obravnavanega
        vzami = 0
        if zaporedje[i] < prej:
            vzami = 1 + najdaljse_padajoce(i + 1, zaporedje[i])

        return max(izpusti, vzami)

    return najdaljse_padajoce()
```

**Komentar:**
Nisem imel posebnih težav, saj smo na vajah lepo razložili problem. Rešitev je seveda počasna, saj je rekurzivna.
Ocenjena časovna zahtevnost: $O(2^n)$


**Testi**
Testi so bili že narejeni preko Tomota.


## 2. Part

**Navodilo:** Sestavi funkcijo **padajoce_podzaporedje_tabela(zaporedje)**, ki za dano zaporedje vrne dolžino najdaljšega padajočega podzaporedja. Funkcija naj ne bo rekurzivna, temveč naj si delne rešitve shranjuje v tabelo.

**Rešitev:**
```python
def padajoce_podzaporedje_tabela(zaporedje):
    """
    Za dano zaporedje vrne dolžino najdaljšega padajočega podzaporedja. Brez rekurzije s shranjevanjem v tabelo.
    """
    if not zaporedje:  # Tisti en primer []
        return 0

    dolzina = len(zaporedje)
    tabela = [1 for _ in range(dolzina)]
    # Za vsakega shranimo mozno dolzino
    for i in range(dolzina):
        for j in range(i):
            if zaporedje[i] < zaporedje[j] and tabela[i] < tabela[j] + 1:
                tabela[i] = tabela[j] + 1

    return max(tabela)
```

**Komentar:**
Ni bilo posebnih težav, tukaj imamo dodatno tabelo katero sproti spreminjamo.
Ocenjena časovna zahtevnost: $O(n^2)$

**Testi**
Testi so bili že narejeni preko Tomota.


## 3. Part

**Navodilo:** Sestavi funkcijo **padajoce_podzaporedje(zaporedje)**, ki za dano zaporedje vrne najdaljše padajoče podzaporedje. Podzaporedje naj vrne kot seznam. Če je rešitev več, naj vrne tisto z najmanjšimi indeksi.

**Rešitev:**
```python
def padajoce_podzaporedje(zaporedje):
    """
    Za dano zaporedje vrne elemente, ki tvorijo najdaljše padajoče podzaporedje. Brez rekurzije s shranjevanjem v tabelo.
    """
    if not zaporedje:
        return []

    dolzina = len(zaporedje)
    tabela = [[1, [zaporedje[i]]] for i in range(dolzina)]
    # Za vsakega shranimo mozno dolzino
    for i in range(dolzina):
        for j in range(i):
            if zaporedje[i] < zaporedje[j] and tabela[i][0] < tabela[j][0] + 1:
                tabela[i][0] = tabela[j][0] + 1
                tabela[i][1] = tabela[j][1][:]
                tabela[i][1].append(zaporedje[i])
    return max(tabela)[1]
```

**Komentar:**
Zelo podobna rešitev kot pri prejšni podnalogi. Tukaj imamo v tabeli na vsakem indeksu tabelo z dvema elementova [najvecja dolzina, zaporedje], kjer shranimo poleg dolžine tudi z katerimi elementi smo dosegli naše najdaljše zaporedje. Elemente dodajamo sproti takrat, ko ugotovimo, da lahko najdaljše zaporedje podaljšamo, če vstavimo element na i-tem mestu.
Ocenjena časovna zahtevnost: $O(n^2)$

**Testi**
Testi so bili že narejeni preko Tomota.

---

# Največja vsota podzaporedja

## 1. Part

**Navodilo:** Sestavi funkcijo **max_podzaporedje_vsota(zaporedje)**, ki za dano zaporedje vrne največjo možno vsoto členov naraščajočega podzaporedja.

Funkcije ne piši iz nule, ampak si pomagaj z rešitvami prve naloge.

**Rešitev:**
```python
def max_podzaporedje_vsota(zaporedje):
    """
    Za dano zaporedje vrne najvecjo vsoto najdaljšega narascajocega podzaporedja. Brez rekurzije s shranjevanjem v tabelo.
    """
    if not zaporedje:
        return 0

    dolzina = len(zaporedje)
    tabela = [zaporedje[i] for i in range(dolzina)]
    # Za vsakega shranimo mozno dolzino
    for i in range(dolzina):
        for j in range(i):
            if zaporedje[i] > zaporedje[j] and tabela[i] < tabela[j] + zaporedje[i]:
                tabela[i] = tabela[j] + zaporedje[i]

    return max(tabela)
```

**Komentar:**
Rešitev sem dobil samo z rahlo predelavo kode iz prve naloge. Tukaj namesto dolžine hranimo vsoto, zato smo samo tisti +1 zamenjali z +trenutni_element.
Ocenjena časovna zahtevnost: $O(n^2)$


**Testi**
Testi so bili že narejeni preko Tomota.

---

# Najdaljše naraščajoče podzaporedje lihi členov

## 1. Part

**Navodilo:** Sestavi funkcijo **max_podzaporedje_lihi(zaporedje)**, ki za dano zaporedje vrne najdaljše naraščajoče podzaporedje, sestavljeno iz samih lihih števil.

Funkcije ne piši iz nule, ampak si pomagaj z rešitvami prejšnjih podnalog.

**Rešitev:**
```python
def max_podzaporedje_lihi(zaporedje):
    """
    Za dano zaporedje vrne elemente, ki tvorijo najdaljše padajoče podzaporedje, elementi so lahko samo liha stevila
    """
    #izbrisemo sode elemente
    zaporedje = [el  for el in zaporedje if (el % 2 != 0)]
    if not zaporedje:
        return []

    dolzina = len(zaporedje)
    tabela = [[1, [zaporedje[i]]] for i in range(dolzina)]
    # Za vsakega shranimo mozno dolzino
    for i in range(dolzina):
        for j in range(i):
            if zaporedje[i] > zaporedje[j] and tabela[i][0] < tabela[j][0] + 1:
                tabela[i][0] = tabela[j][0] + 1
                tabela[i][1] = tabela[j][1][:]
                tabela[i][1].append(zaporedje[i])
    return max(tabela)[1]
```

**Komentar:**
Rešitev sem dobil samo z rahlo predelavo kode iz prejšnih nalog. Vse kar sem naredil je, da sem na začetku v funkciji izbrisal vse sode člene v našem zaporedju, potem pa poklical enako kodo kot pri nalogi z najdaljšim zaporedjem.
Ocenjena časovna zahtevnost: $O(n^2)$


**Testi**
Testi so bili že narejeni preko Tomota.

---

# Sod - lih

## 1. Part

**Navodilo:** Sestavi funkcijo **sod_lih(zaporedje)**, ki vrne dolžino najdaljšega naraščajočega podzaporedja zaporedja 'zaporedje', sestavljenega iz izmenično lihih in sodih členov (prvi člen je lahko tako lih kot sod).

**Rešitev:**
```python
def sod_lih(zaporedje):
    """
    Za dano zaporedje vrne dolžino najdaljšega padajočega podzaporedja kjer so elementi izmenično sodi in lihi.
    """
    if not zaporedje:  # Tisti en primer []
        return 0

    dolzina = len(zaporedje)
    tabela = [1 for _ in range(dolzina)]
    # Za vsakega shranimo mozno dolzino
    for i in range(dolzina):
        for j in range(i):
            if zaporedje[i] % 2 == 0:
                #gledamo zdaj lihe
                if zaporedje[j] % 2 == 0:
                    continue
            else:
                #gledamo sode
                if zaporedje[j] % 2 != 0:
                    continue

            if zaporedje[i] > zaporedje[j] and tabela[i] < tabela[j] + 1:
                tabela[i] = tabela[j] + 1

    return max(tabela)
```

**Komentar:**
Rešitev sem dobil samo z rahlo predelavo kode iz prejšnih nalog. Pri nalogi sem dodal samo dodatni pogojni stavek, ki preveri kakšen je zadnji element v našem trenutnem najdaljšem zaporedju, v primeru da je sod potem gledamo naprej samo lihe in obratno. Če pridemo na neustrezni element ga v tej iteraciji ignoriramo in nadaljujemo z naslednjim.
Ocenjena časovna zahtevnost: $O(n^2)$


**Testi**
Testi so bili že narejeni preko Tomota.

## 2. Part

**Navodilo:** Sestavi funkcijo **sod_lih_podzap(zaporedje)**, ki vrne najdaljše naraščajoče podzaporedje zaporedja 'zaporedje', sestavljenega iz izmenično lihih in sodih členov (prvi člen je lahko tako lih kot sod).

Funkcije ne piši iz nule, ampak si pomagaj z rešitvami prejšnjih podnalog.

**Rešitev:**
```python
def sod_lih_podzap(zaporedje):
    """
    Za dano zaporedje vrne elemente, ki tvorijo najdaljše padajoče podzaporedje kjer so elementi izmenično sodi in lihi.
    """
    if not zaporedje:
        return []

    dolzina = len(zaporedje)
    tabela = [[1, [zaporedje[i]]] for i in range(dolzina)]
    # Za vsakega shranimo mozno dolzino
    for i in range(dolzina):
        for j in range(i):
            if zaporedje[i] % 2 == 0:
                #gledamo zdaj lihe
                if zaporedje[j] % 2 == 0:
                    continue
            else:
                #gledamo sode
                if zaporedje[j] % 2 != 0:
                    continue

            if zaporedje[i] > zaporedje[j] and tabela[i][0] < tabela[j][0] + 1:
                tabela[i][0] = tabela[j][0] + 1
                tabela[i][1] = tabela[j][1][:]
                tabela[i][1].append(zaporedje[i])

    return max(tabela)[1]
```

**Komentar:**
Rešitev sem dobil, ko sem združil prejšno podnalogo in pa nalogo najdaljše narascajoce zaporedje, kjer je bilo že potrebno izpisati podzaporedje, ki je najdaljše. Tako pridemo do ustrezne rešitve.
Ocenjena časovna zahtevnost: $O(n^2)$


**Testi**
Testi so bili že narejeni preko Tomota.
