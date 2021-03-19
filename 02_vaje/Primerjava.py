from merilnik import *
from LIS import *
from dintest import *
from usmerjeniGraf import *
from matplotlib import pyplot as plt


def izrisi_tri(fun1,  fun2, fun3, gen_primerov, sez_n, k=10):
    '''
        Funkcija nariše grafa porabljenih časov za izračun `fun1` in `fun2`
        na primerih generiranih z `gen_primerov`, glede na velikosti primerov
        v `sez_n`. Za oceno uporabi `k` ponovitev. Izriše 2 grafa na eni
        sliki, kar omogoča lažje primerjanje.
    '''
    casi1 = [oceni_potreben_cas(fun1, gen_primerov, n, k) for n in sez_n]
    casi2 = [oceni_potreben_cas(fun2, gen_primerov, n, k) for n in sez_n]
    casi3 = [oceni_potreben_cas(fun3, gen_primerov, n, k) for n in sez_n]

    # plt.plot(sez_n, casi1, 'r', sez_n, casi2, 'y')
    plt.plot(sez_n, casi1, 'r')
    plt.plot(sez_n, casi2, 'y')
    plt.plot(sez_n, casi3, 'b')
    
    plt.show()

def izpisi_case_treh_funkcij(fun1, fun2, fun3, gen_primerov, sez_n, k = 10):
    """ Funkcija izpiše tabelo časov za izračun `fun1` in `fun2`, na primerih generiranih z
    `gen_primerov`, glede na velikosti primerov v `sez_n`. Za oceno uporabi `k`
    ponovitev. """

    # Seznam časov, ki jih želimo tabelirati
    casi1 = []  
    for i in sez_n:
        primer = gen_primerov(k)
        casi1.append(oceni_potreben_cas(fun1, gen_primerov, i, k))
    pad = 0  
    for i in sez_n:
        if len(str(i)) > pad:
            pad = len(str(i))
    casi2 = []  
    for i in sez_n:
        primer = gen_primerov(k)
        casi2.append(oceni_potreben_cas(fun2, gen_primerov, i, k))
    casi3 = []  
    for i in sez_n:
        primer = gen_primerov(k)
        casi3.append(oceni_potreben_cas(fun3, gen_primerov, i, k))
    for i in sez_n:
        if len(str(i)) > pad:
            pad = len(str(i))
    # izpiši glavo tabele
    print("{:{pad}} | Čas izvedbe funkcije 1 | Čas izvedbe funkcije 2 | Čas izvedbe funkcije 3".format("n", pad = pad))

    # horizontalni separator
    sep_len = pad + max(len(" | Čas izvedbe funkcije 1 | Čas izvedbe funkcije 2 | Čas izvedbe funkcije 3"), 3 + max(len(str(t)) for t in casi1) + max(len(str(t)) for t in casi2))   
    print("-" * sep_len)
    sep_len1 = max(len(" | Čas izvedbe funkcije 1"),  max(len(str(t)) for t in casi1)) - 3 
    # ta -3 zato ker mi ni uspelo in sem potem "numerično razrešil"

    # izpiši vrstice
    for n, t, s, m in zip(sez_n, casi1, casi2, casi3):
        print("{:{pad}} | {:{sep_len1}} | {:{sep_len1}} | {:{sep_len1}}".format(str(n), t, s, m, pad = pad, sep_len1 = sep_len1 ))
    

sez_n = [k for k in range(50)]
izpisi_case_treh_funkcij(LIS1, LIS, najdaljse_zaporedje_graf, test_gen_sez, sez_n, k = 30)
# izrisi_tri(LIS1, LIS, najdaljse_zaporedje_graf, test_gen_sez, sez_n, k = 10)