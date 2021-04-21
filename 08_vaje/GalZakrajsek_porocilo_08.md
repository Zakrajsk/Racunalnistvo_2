# Vaje 14. 04, Bellman-Ford

**Ime:** Gal Zakrajšek

**Datum:** 21.04.2021

---

Na vajah smo se pogovarjali o Bellman-Fordovem algoritmu. Pogledali smo kako deluje na nekem grafu. Potem smo dobili v razmislek, kako naj bojo urejene povezave, da bi se algoritem zaključil v čim manj fazah.


## Komentarji in opombe

Vaje so bile poučne, saj smo videli, da tudi če imamo en algoritem, ki velja za dobrega, da je lahko pomembno tudi, kako podamo podatke. S tem lahko prišparamo pri časovni zahtevnosti.


## Organizacija dela

V skupinah smo naredili razmislek. Tokrat ga nismo delili z drugo skupino, saj je zmanjkalo časa.


# Bellman-Ford

**Navodilo:** Kako bi uredili povezave, da se bo algoritem zaključil v čim manj fazah.

Že pri vajah ste nam dali namig, da bi povezave uredili topološko. Sam sem nato doma malo se igral in poizkušal, če nam kaj pomaga, če tudi sekundarno uredimo (najprej topološko in nato še npr po dolžini povezav) ampak sem vedno prišel do enakega števila faz. Zato mislim, da je važno samo, da so topološko urejene. Tako lahko naš graf, ki nam je bil podan zaključimo v 3 fazah. 
1. spremenimo vse
2. spremenimo samo še okoli vozlišča 2 (morda bi tukaj lahko nekako vzeli povezavo 5 - 2 kot prvo in potem nam ni potrebno imeti te faze)
3. faza v kateri ne spremenimo nič in zato se lahko po tej fazi vse zaključi.

Pri 2. koraku bi zdaj ko vidim rešitev lahko naredil tako, da vzame najprej tisto povezavo ampak to se vedno lahko zgodi tudi obratno zato nisem prepričan, če bi lahko še kaj izboljšal.

**Navodilo** Ali izbira vrstnega reda povezav kaj vpliva na drevo najkrajših poti, ki ga najdemo.

Izbira lahko vpliva, saj včasih lahko najdemo dve poti, ki sta enako dolgi vendar v skupnem "staneta" enako. Tako lahko z drugačnim vrstim redom dobimo dve različni drevesi. Cene končnih poti pa bodo vedno optimalne.