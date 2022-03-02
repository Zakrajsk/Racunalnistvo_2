# Vaje 24. 02, Dinamično programiranje 2

**Ime:** Gal Zakrajšek

**Datum:** 24.02.2021

---

Pri vajah smo obravnavali problem množenja matrik. Pogledali smo kako se problem reši rekurzivno in dinamčno z pisanjem v tabelo. Potem smo odgovarjali na par vprašanj povezanih z našim problemo. Proti koncu smo na Tomo-tu reševali naloge.


## Komentarji in opombe

Na vajah mi je bila všeč razlaga problema, saj smo si res vzeli čas in se posvetili problemu.


## Pomemnba vprašanja, ki smo jih obravnavali na vajah


### Kako dobiti število vseh optimalnih produktov
Privzamimo, da imamo funckijo, ki nam napolni tabelo z optimalnim številom produktov in zraven pove tudi, kje so bili tedaj postavljeni oklepaji (tisti k, pri katerem je bilo operacij najmanj). Potem lahko začenmo iz zgornjega desnega kota, kjer je tudi končen rezultat. Pomikamo se po tabeli tako, kot nam povejo tisti k-ji. Za število vseh optimalnih produktov samo pomnožimo vse k-je, ki so se pojavili pri našem pregledu. 

### Kako izpisati vse te optimalne produkte
Za izpis produktov ponovno predpostavimo, da imamo funkcijo opisano pri zgornjem vprašanju. Spet začnemo iz končnega rezultata in konstruiramo toliko različnih postavitev oklepajev, kolikor je različnih k-jev pri katerih smo dobili optimalno število operacij. Če imamo naprimer dva k-ja, potem dosedanji izraz podvojimo in ekrat postavimo oklepaj pri prvem k-ju drugič pa pri drugem. Seveda moramo potem tudi naprej v tabeli iskati za obe možnosti.

### Kaj lahko poveš v primeru, ko so vse matrike kvadratne
Ko so vse matrike kvadratne je vrstni red nepomemben, saj bo vedno enaka dimenzija kakorkoli začnemo množiti. Zato bo tudi končno število operacij vedno enako.

### Kako bi algoritem poganjali na več računalnikih
Do ideje smo prišli na vajah in sicer si predstavljamo drevo, kjer imamo kot elemente operatorje in matrike. Seveda ta drevo konstruiramo po tem ko smo izračunali optimalno zaporedje množenj. Iz drevesa je razvidno katere operacije so neodvisne od ostalih (tiste, ki imajo po dva lista) in ravno te bi lahko izračunali na večih računalnikih in tako sočasno rešili več operacij in zmanjšal čas celotnega računa.

### Kaj moramo na novo izračunati ob manjši spremembi vhodnih podatkov
Spremenimo naprimer zadnjo dimenzijo matrike, seveda mora ostati tako, da je še vedno možno zmnožiti predzadnjo in zadnjo. Vse kar rabimo popraviti pri naši tabeli opzimalnih operacij je zadnji stolpec. 

### Problem rezanja palice.
Problem je zelo podoben kot naš problem množenja matrik. Tukaj namesto števila operacij pri množenju matrik pišemo ceno reza. Ostalo pa je enako




Množenje matrik

N(i, j) = Optimalno št operacij za izračun produkta
N(i,j) = min(k= i -> j)(N(i, k) + N(k+1, j) + di * dj+1 * dk+1)
N(i, i) = 0


Postavljanje oklepajev

O(i, j) = št optimalnih produktov za zmnožitev Ai * Aj
O(i, j) = sum(k€N(i, j))(O(i, k) * O(k + 1, j))
O(i, i) = 1




Rezanje palice

Režemo palice na ik delov. Celotna dolžina je L
cena reza = dolžina palice
Problem zelo pdoobno kot matrike sam da je namesto število uporacij pač cena reza
Napiši še belmanovo enačbo