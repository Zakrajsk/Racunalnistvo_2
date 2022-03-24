# Vaje 17. 02, Dinamično programiranje uvod

**Ime:** Gal Zakrajšek

**Datum:** 24.03.2022

---

Pri vajah smo najprej primerjali časovno zahtevnost za osnovne operacije pri seznamu, mnozici in vezirznem seznamu. Kasneje smo reševali naloge iz Tomota o dinamičnem programiranju.


## Komentarji in opombe
Vaje so bile super, veliko je bilo govora o časovni zahtevnosti, kar pride prav tudi v resničnem svetu.


## Pomembna vprašanja, ki smo jih obravnavali na vajah
Primerjava časovnih zahtevnosti za osnovne operacije:
|                | Dodajanje na konec | Dodajanje na začetek | Brisanje | Iskanje |
|----------------|--------------------|----------------------|----------|---------|
| Seznam         | O(1) / O(n)        | O(n)                 | O(n)     | O(n)    |
| Množica        | O(1)               | O(1)                 | O(1)     | O(1)    |
| Verižni seznam | O(1)               | O(1)                 | O(n)     | O(n)    |

Kot smo ugotovili, na prvi pogled deluje množica najboljša podatkovna struktura, vendar pa se izkaže, da ni tako, saj je ta konstantna dokaj visoko število in zato takrat, ko vemo kje točno iskati oziroma brisati je bolje uporabiti seznam ali kakšno drugo podatkovno strukturo.

## Žabica
Nato smo skupaj pokomentirali nalogo žabica, ki je na tomotu. Definirali smo funckijo \
$Z(e, i) = min\ stevilo\ skokov\ za\ žabo\ na\ i-tem\ mestu\ z\ e\ energije$\

In pa $L = dolžina\ mlake$

Po pogovoru smo prišli do bellmanove enačbe:

$Z(e, i) = min_{k = 1, ..., e}(Z(e - k + m[i + k], i + k)) + 1$

Kasneje smo nalogo tudi sprogramirali in ugotovili, da je razmislek pravilen.\
Časovna zahtevnost je $O(m * l)$\

## Jajca

Kasneje smo si pogledali še nalogo jajca. Tukaj rešujemo problem, kjer skušamo z $n$ jajci ugotoviti kritično nadstropje, pri katerem se jajce razbije. Celotna zgradba pa ima pri temu $k$ nadstropij. Kritično nadstropje je prvo nadstropje, pri katerem se bo jajce razbilo, posledično se bo tudi na vseh višjih.\
Definiramo funkcijo\
$jajce(n, k) = najmanjše\ število\ metov,\ da\ v\ najslabšem\ primeru\ ugotovimo\ kritično\ nadstropje.$\
Pri tem imamo tudi dva že v naprej določena pogoja:\
$jajce(1, k) = k$ - saj če imamo samo eno jajce začnemo spodaj in se po vsakem metu premaknemo za eno nadstropje višje.\
$jajce(n, 1) = 1$ - imamo samo eno nadstropje, zato z enim metom ugotovimo, ali se tam jajce razbije ali ne.

Z pogovorom in analizo problema, smo prišli do naslednje bellmanove enačbe:\
$jajce(n, k) = min_{i = 1, ..., k}max(jajce(n - 1, i - 1), jajce(n, k - i))$

Časovna zahtevnost našega algoritma je $O(n * k^2)$



---

# Jajca

Visoka stavba ima več nadstropij. Sprehajamo se od nadstropja do nadstropja ter pri tem iz nekega nadstropja lahko spustimo jajce, ki pada do tal. Jajce se bodisi razbije bodisi ostane celo. Celo jajce lahko poberemo in ga ponovno uporabimo. Če se jajce razbije v nekem nadstropju se razbije tudi v vseh višjih nadstropjih, velja pa tudi obratno. Želimo ugotoviti, katero je najnižje nadstropje v katerem se jajce še razbije. Na voljo imamo $k$ jajc stavba pa ima $n$ nadstropij. Kolikšno je najmanjše število metov jajca, da bomo zagotovo ugotovili katero je ''kritično'' nadstropje.

## 1. Part

**Navodilo:** Sestavite funkcijo **jajce_rec(n, k)**, ki vrne najmanje število metov jajca pri $k$ nadstropjih in $n$ jajcih. Funkcija naj bo napisana rekurzivno.

**Rešitev:**
```python
from functools import lru_cache

@lru_cache(maxsize = None)
def jajce_rec(n, k):
    """
    Funkcija vrne najmanjse stevilo metov jajca pri k nadstropjih in n jajcih.
    """
    if n == 1 or k <= 1:
        return k

    return 1 + min(max(jajce_rec(n - 1, i - 1), jajce_rec(n, k - i)) for i in range(1, k + 1))
```

**Komentar:**
Nisem imel posebnih težav, saj smo že na vajah skupaj ugotovili bellmanovo enačbo.\
Ocenjena časovna zahtevnost: $O(n * k^2)$


**Testi**
Testi so bili že narejeni preko Tomota.


## 2. Part

**Navodilo:** Sestavite funkcijo **jajce_iter(n, k)**, ki vrne najmanje število metov jajca pri $k$ nadstropjih in $n$ jajcih. Tokrat naj funkcija nebo napisana rekurzivno

**Rešitev:**
```python
def jajce_iter(n, k):
    """
    Funkcija vrne najmanjse stevilo metov jajca pri k nadstropjih in n jajcih. Funkcija je iterativna brez rekurzije
    """
    tab_rezultatov = [[i if (j == 0 or i <= 1) else float('inf') for i in range(k + 1)] for j in range(n)]
    
    for i in range(1, n):
        for j in range(2, k + 1):
            
            najmanjsi = float('inf')
            for m in range(1, j + 1):
                vmesni = max(tab_rezultatov[i - 1][m - 1], tab_rezultatov[i][j - m])

                if vmesni < najmanjsi:
                    najmanjsi = vmesni
            tab_rezultatov[i][j] = 1 + najmanjsi
    return tab_rezultatov[n - 1][k]
```

**Komentar:**
Ponovno smo delali skupaj na vajah, zato ni bilo nekih težav.\
Ocenjena časovna zahtevnost: $O(n^2)$

**Testi**
Testi so bili že narejeni preko Tomota.


## 3. Part

**Navodilo:** Sestavite funkcijo **nadstropja(d, n)**, ki vam pove koliko nadstropij lahko preverite v $d$ metih in z $n$ jajci.

**Rešitev:**
```python
def nadstropja(d, n):
    '''
    Funckija nam pove koliko nastropij lahko preverimo v d metih z n jajci
    '''
    if d == 0 or n == 0:
        return 0

    return 1 + nadstropja(d - 1, n - 1) + nadstropja(d - 1, n)
```

**Komentar:**
Nalogo smo že malo predebatirali na vajah, saj jo bomo uporabili za hitrejše reševanje problema iz part2.\
Ocenjena časovna zahtevnost: $O(d^2)$

**Testi**
Testi so bili že narejeni preko Tomota.

## 4. Part

**Navodilo:** Sestavite funkcijo **jajca_hitro(n, k)** kot v prvih dveh nalogah. Tokrat mora funkcija delovati hitro tudi za večje stavbe z več nadstropji (recimo nad 1000 nadstropji). Namig: uporabite funkcijo **nadstropja(d, n)**.

**Rešitev:**
```python
def jajca_hitro(n , k):
    '''
    Funkcija vrne najmanjse stevilo metov jajca pri k nadstropjih in n jajcih. Funkcija za pomoc uporabi nadstorpja(d, n)
    '''
    d = 0
    #lahko naredimo neskoncno zanko ker bomo zagogtovo prisli do resitve
    while(True):
        koliko_lahko_preverimo = nadstropja(d, n)
        if koliko_lahko_preverimo >= k:
            return d
        d += 1
```

**Komentar:**
Tukaj je zanimivo to, da smo osnovni problem reševali tako, da smo nalogo drugače sestavili. Prvo smo naredili funckijo nadstropja(d, n), s katerimi smo dobili podatek, koliko nadstropij lahko preverimo z nekim številom jajc in metov. Tako potem na hitrejši način dobimo tudi rešitev osnovnega problema.\
Ocenjena časovna zahtevnost: $O(k^2)$

**Testi**
Testi so bili že narejeni preko Tomota.


# Poti v matriki

Dano imamo matriko, ki vsebuje števila $1$, $0$ in $-1$, kjer $-1$ predstavlja nevarno celico. Iz prve celice (levo zgoraj) potujemo po matriki in nabiramo točke ($1$ točka, če obiskana celica vsebuje število $1$, $0$ točk, če vsebuje število $0$), pri tem pa ne smemo obiskati nevarnih celic. Poleg tega nam je dovoljeno potovati samo navzdol ali na levo, če smo v lihi vrstici oz. navzdol in na desno, če smo v sodi vrstici.

Pri reševanju si lahko pomagaš z napisano rešitvijo v C++ ali v Javi, ki jo najdeš na tej spletni strani. Na isti strani je tudi primer matrike s prikazano rešitvijo.

## 1. Part

**Navodilo:** Sestavi rekurzivno funkcijo **najvrednejsa_pot(matrika)**, ki vrne največje število točk, ki jih lahko naberemo pri potovanju po matriki po zgoraj napisanih pravilih.

**Rešitev:**
```python
#V testnih primerih je vračalo napako, zato sem tukaj skopiral testno matriko
matrika1 = [[1, 1, -1, 1, 1],
            [1, 0, 0, -1, 1],
            [1, 1, 1, 1, -1],
            [-1, -1, 1, 1, 1],
            [1, 1, -1, -1, 1]]

def najvrednejsa_pot(matrika):
    """
    Funkcija rekurzivno najde tako pot v matriki, da izberemo najvec tock (1 ena tocka, 0 nic tock, -1 prepovedano)
    """
    def premikanje(vrsta, stolpec):
        """
        Pomozna funkcija za premikanje po matriki, da ne potrebujemo matrike posiljat kot parametr
        """
        if vrsta == len(matrika) or stolpec == len(matrika) or stolpec < 0 or matrika[vrsta][stolpec] == -1:
            return 0
        
        #pogledamo kam lahko gremo
        if vrsta % 2 != 0:
            #levo pa dol
            return matrika[vrsta][stolpec] + max(premikanje(vrsta + 1, stolpec), premikanje(vrsta, stolpec - 1))
        else:
            #desno pa dol
            return matrika[vrsta][stolpec] + max(premikanje(vrsta + 1, stolpec), premikanje(vrsta, stolpec + 1))

    return premikanje(0, 0)
```

**Komentar:**
Načeloma težav nisem imel. Opazil sem, da se je testni program sesuval, ker nekako ni imel definirane matrike1, zato sem jo iz spodnje kode skopiral pred mojo funkcijo in je test delal.
Ocenjena časovna zahtevnost: $O(n^3)$

**Testi**
Testi so bili že narejeni preko Tomota.


## 2. Part

**Navodilo:** Sestavi funkcijo najvrednejsa_pot_dinamicno(matrika), ki vrne največje število točk, ki jih lahko naberemo pri potovanju po matriki po zgoraj napisanih pravilih. Nalogo reši z dinamičnim programiranjem.

**Rešitev:**
```python
def najvrednejsa_pot_dinamicno(matrika):
    ''' poišče največje število točk, 
    ki jih lahko naberemo pri potovanju po matriki '''

    n = len(matrika)

    naj_poti = [[0] * n for _ in range(n)]

    for vrsta in range(len(matrika)):
        for stolpec in (range(n) if vrsta % 2 == 0 else range(n-1, -1, -1)):
            #Ce smo na -1 lahko takoj prenehamo saj sem nesmemo
            if matrika[vrsta][stolpec] != -1:
                #pogledamo obe smeri iz katere lahko pridedmo
                if vrsta % 2 == 0:
                    zgoraj = naj_poti[vrsta - 1][stolpec] if vrsta != 0 else 0
                    levo = naj_poti[vrsta][stolpec - 1] if stolpec != 0 else 0
                    naj_poti[vrsta][stolpec] = max(zgoraj, levo) + matrika[vrsta][stolpec]
                else:
                    zgoraj = naj_poti[vrsta - 1][stolpec] if vrsta != 0 else 0
                    desno = naj_poti[vrsta][stolpec + 1] if stolpec != n - 1 else 0
                    naj_poti[vrsta][stolpec] = max(zgoraj, desno) + matrika[vrsta][stolpec]
    
    return max(map(max, naj_poti))
```

**Komentar:**
Ni bilo nobenih posebnih težav.
Ocenjena časovna zahtevnost: $O(n^2)$

**Testi**
Testi so bili že narejeni preko Tomota.
