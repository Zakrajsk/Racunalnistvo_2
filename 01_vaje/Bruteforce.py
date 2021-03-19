import itertools
import time

def ali_je_narascajoc(podatki, izbrani):
    """
    Preveri ali so podatki, ki so izbrani narascajoci
    Izbrani je tabela [0 in 1], kjer 1 predstavlja da je na tem mestu izbran element
    """
    prejsni = -1
    dolzina = 0
    for i, en in enumerate(podatki):
        if izbrani[i] == "1":
            #ce najdemo, da je en podatek manjsi pomeni da zaporedje ni narascajoce zato vrnemo dolzino 0
            if podatki[i] < prejsni:
                return 0
            prejsni = podatki[i]
            dolzina += 1
    return dolzina

def najdaljse_zaporedje_bruteforce(podatki):
    """
    Preveri vse moznosti in najde najdaljse zaporedje
    """
    #zgeneriramo vse permutacije dolzine kot podatki, ki vsebujejo 0le in 1ke
    vse_kombinacije = itertools.product("01", repeat=len(podatki))
    najdaljse = 0

    zacetni_cas = time.time()

    for kombinacija in vse_kombinacije:
        #za vsako permutacijo pogledamo ce je narascajoce
        temp_narascajoce = ali_je_narascajoc(podatki, kombinacija)

        #pogledamo ce je ta izbor daljsi od dozdaj najdaljsega
        if temp_narascajoce > najdaljse:
            najdaljse = temp_narascajoce
                
    izvajalni_cas = time.time() - zacetni_cas
    return najdaljse, izvajalni_cas


if __name__ == "__main__":
    test = [5, 2, 8, 6, 3, 6, 9, 7, 8, 10, 5, 18, 9, 25, 9, 42]
    print(najdaljse_zaporedje_bruteforce(test))