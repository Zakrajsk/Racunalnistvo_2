# Vaje 21.4.2022 Zgoščevalne funkcije

**Ime:** Gal Zakrajšek

**Datum:** 27.04.2022

---


Na vajah smo se pogovarjali o zgoščevalnih funkcijah.


## Komentarji in opombe

Vaje so bile malo hitre, saj nam je zmanjkovalo časa. Vendar mislim, da smo vseeno nekaj odnesli od zgoščevalnih funkcij.


## Zgoščevalne funkcije

## 1. naloga
**Navodilo** V zgoščevalno tabelo velikosti 11 (n = 11) vstavimo ključe iz seznama [23, 1, 13, 11, 24, 33, 18, 42, 31] z zgoščevalno funkcijo h(x) = x mod n

Kakšna izgleda tabela glede na različne pristope reševanja trkov. Uporabi veriženje ter linearno in kvadratično iskanje(probing). Do kakšnih problemov lahko pridemo pri teh pristopih? Kaj bi bilo, če bi uporabili kakšno drugo zgoščevalno funkcijo oblike h(x) = ax mod n za nek a različen od 0 in manjši od n? Bi lahko za poljuben a našel zaporedje ključev, ki bi ustvaril veliko trkov? Naštej še kakšne standardne zgoščevalne funkcije.


$U$, $|U| = u$\
$V$, $|V| = m$\
$S... množica\ ključev$, $|S| = n$\
$h: U -> V$

$n = 11$\
$h(x) = x$ % $n$

|    | Verizno | Linearno | Kvadratično |
|----|---------|----------|-------------|
| 0  | 11, 33  | 11       | 11          |
| 1  | 23, 1   | 23       | 23          |
| 2  | 13, 24  | 1        | 1           |
| 3  |         | 13       | 13          |
| 4  |         | 24       | 24          |
| 5  |         | 33       | 33          |
| 6  |         |          |             |
| 7  | 18      | 18       | 18          |
| 8  |         |          |             |
| 9  | 42, 31  | 42       | 42          |
| 10 |         | 31       | 31          |

Če vzamemo za primer iskanja števila $33$, bi z verižnim potrebovali $hash + 2$ primerjavi medtem, ko bi pri linearnem potrebovali $hash + 6$ primerjav. 

Razlika se pozna med linearno in kvadratično, ki nam ustvarita enako strukturo vendar potrebujemo manj primerjav pri iskanju števila $33$. Porabili bi $hash + 3$ primerjave.

Če bi uporabili $h(x) = ax$ % $n$ potem bi imeli ponovno enako težave, saj bi bili ostanki enaki.

standardne zgoščevalne:\
$g(x) = a * x + b * $ % $n$ - lahko pride še vseeno do težav, saj je pri velikih številih * in pa % vseeno malo "daljša" operacija.

$g'(x) = (ax$ % $2^w) // 2^{w - l}$ - ker imamo potence števila dva bi ta funkcija delovala hitreje.

## 2. naloga
**Navodilo** Univerzalno zgoščevanje

$U$ (univerzalna) in $V$ naj bosta množici, kjer je velikost $U$ ogromno večja kot velikost $V$. Družini preslikav $H$ iz $U$ v $V$ rečemo univerzalna, če za vsak $x != y$ iz $U$ velja $Pr[h(x) = h(y)] <= 1/n$, kjer preslikavo $h$ vzamemo naključno iz družine $H$ ter $n = |V|$.

Ideja univerzalnega zgoščevanja, da uporabimo naključen a, kar pomeni, da vzamemo naklučno zgoščevalno funkcijo. 

$H \subseteq { U -> V}$\
$H$ je univerzalna če: $ vsak\ x \ne y \in U$ tako da, $P(h(x) = h(y)) \le \frac{1}{n}$

$h_a(x) = a*x $ % $n$, $a \in Z_n$

### 2.1. naloga
**Navodilo** Pokaži, da je $H = ${$h_a | a \in Zn$} univerzalna.

$a \in Z_n$ naključen\
$a * x = a * y + k * n$\
$a(x-y) = k * n$ -> Pri tem je $a(x-y)$ enakomerno razdeljeno med $0$ in $n-1$


### 2.2. naloga
**Navodilo**Naj bo h zgoščevalna funkcija iz univerzalne družine (izbrana naključno). Recimo, da želimo v tabelo shranit m ključev. Definiramo "load factor" alpha = m/n. Koliko je povprečno število trkov? Kaj lahko poveš o dolžini najdaljše verige? Namig: Indikatorji, linearnost pričakovane vrednosti

$\alpha = \frac{n}{m} \le 1$\
$h \in H\ univerzalna $\
$L(x) = |${$y \in S | h(x)=h(y)$}$|$
$E(l(x)) = 1 + \sum_{y \in S, S \ne x } E(I_y) \le 1 + \alpha \le 2$\
$I_y = 1, h(x) = h(y)\ drugače\ 0, sicer$\
$E(I_y) = P(I_y = 1) = P(h(x) = h(y)) \le \frac{1}{m}$














