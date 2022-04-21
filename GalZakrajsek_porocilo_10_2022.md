# Vaje 14. 04, Bellman-Ford

**Ime:** Gal Zakrajšek

**Datum:** 21.04.2022

---


Na vajah smo se pogovarjali o Bellman-Fordovem algoritmu. Pogledali smo kako deluje na nekem grafu. Potem smo dobili v razmislek, kako naj bojo urejene povezave, da bi se algoritem zaključil v čim manj fazah.


## Komentarji in opombe

Vaje so bile poučne, saj smo videli, da tudi če imamo en algoritem, ki velja za dobrega, da je lahko pomembno tudi, kako podamo podatke. S tem lahko prišparamo pri časovni zahtevnosti.


## Organizacija dela

V skupinah smo naredili razmislek. Tokrat ga nismo delili z drugo skupino, saj je zmanjkalo časa.





## Zgoščevalne funkcije


1. 
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

če vzamemo za primer iskanja števila 33. 
Bi z verižnem potrebovali hash + 2 primerjavi medtem ko bi pri linearnem potrebovali hash + 6 primerjav. 

Razlika se pozna med linearno in kvadratično, ki nam ustvarita enako strukturo vendar potrebujemo manj primerjav pri iskanju števila 33. hast + 3 primerjave.

Če bi uporabili $h(x) = ax$ % $n$ potem bi imeli ponovno enako težave, saj bi bili ostanki enaki.

standardne zgoščevalne:\
$g(x) = a * x + b * $ % $n$ - lahko pride še vseeno do težav, saj je pri velikih številih * in pa % vseeno malo "daljša" operacija.

$g'(x) = (ax$ % $2^w) // 2^{w - l}$ - ker imamo potence števila dva to dela hitreje


2. Ideja univerzalnega zgoščevanja, da uporabimo naključen a, kar pomeni, da vzamemo naklučno zgoščevalno funkcijo. 

$H \subseteq { U -> V}$\
$H$ je univerzalna če: $ vsak\ x \ne y \in U$ tako da, $P(h(x) = h(y)) \le \frac{1}{n}$

$h_a(x) = a*x $ % $n$, $a \in Z_n$\
Pokaži, da je $H = ${$h_a | a \in Zn$} univerzalna.

$a \in Z_n$ naključen\
$a * x = a * y + k * n$\
$a(x-y) = k * n$ -> Pri tem je $a(x-y)$ enakomerno razdeljeno med $0$ in $n-1$

##### 2.2
$\alpha = \frac{n}{m} \le 1$\
$h \in H\ univerzalna $\
$L(x) = |${$y \in S | h(x)=h(y)$}$|$
$E(l(x)) = 1 + \sum_{y \in S, S \ne x } E(I_y) \le 1 + \alpha \le 2$\
$I_y = 1, h(x) = h(y)\ drugače\ 0, sicer$\
$E(I_y) = P(I_y = 1) = P(h(x) = h(y)) \le \frac{1}{m}$














