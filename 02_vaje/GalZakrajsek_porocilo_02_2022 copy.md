# Vaje 24. 02, Dinamično programiranje, 2.del

**Ime:** Gal Zakrajšek

**Datum:** 24.02.2021

---

Množenje matrik

N(i, j) = Optimalno št operacij za izračun produkta
N(i,j) = min(k= i -> j)(N(i, k) + N(k+1, j) + di * dj+1 * dk+1)
N(i, i) = 0


Postavljanje oklepajev

O(i, j) = št optimalnih produktov za zmnožitev Ai * Aj
O(i, j) = sum(k€N(i, j))(O(i, k) * O(k + 1, j))
O(i, i) = 1


Algoritem na več računalnikih

Ideja: naredimo drevo operatorji in matrike. Katere dele drevesa lahko neodvisno naredimo. Tiste, ki imajo po dva lista.

Kvadratne matrike za največ različnih možnosti. Ideja če pišemo algoritem če so zaporedne kvadratne matrike jih kar takoj zračunaš, saj je čist vseeno kako jih vzameš.

Kaj spreminjamo, če se podatki spremenijo (zadnjo št stolpci): Časovna vel stolpca ^2 ker se celoten zadnji stolpec spremeni.



Rezanje palice

Režemo palice na ik delov. Celotna dolžina je L
cena reza = dolžina palice
Problem zelo pdoobno kot matrike sam da je namesto število uporacij pač cena reza
Napiši še belmanovo enačbo