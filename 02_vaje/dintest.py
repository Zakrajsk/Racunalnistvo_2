# Smo druga skupina sestavljali smo jo: David, Saša, Peter in Matej
from random import randint

def LIS1(A):
    '''
        s pomočjo dinamičnega programiranja "izačuna" dolžino najdaljšega naraščajočega zaporedja
        v tabeli A
    '''
    # i - vrstice
    # j - stolpci
    A  = [float("-inf")] + A
    dolzinaA = len(A)
    LISbigger = list()
    for i in range(dolzinaA):
        LISbigger.append([0] * (dolzinaA + 1)) # dodamo še en stolpec zato da se lahko potem skličemo nanj v zanki
    for j in range(dolzinaA - 1, -1, -1):
        for i in range(0, j):
            if not j + 1 > dolzinaA:
                obdrzi = 1 + LISbigger[j][j + 1]
                spusti = LISbigger[i][j + 1]
                if A[i] >= A[j]:
                    LISbigger[i][j] = spusti
                else:
                    LISbigger[i][j] = max(obdrzi, spusti)
    return LISbigger[0][1]
    

def nakl_sez():
    '''
        generira naključen seznam naključne dolžine
    '''
    kol = randint(0, 100)
    sez = [randint(0, 100) for i in range(kol)]
    return sez


if __name__ == '__main__':
    # robni primer
    print(LIS1([])) # 0
    print(LIS1([30])) # 1
    print(LIS1([20, 2, 3, 4, 5])) # 4
    print(LIS1([1, 2, 3, 4, 0])) # 4
    print(LIS1([10, 2, 3, 4, 0])) # 3
    print(LIS1([1, 2, 3, 4, 5])) # 5
    print(LIS1([10, 5, 3, 1])) # 1
    # par mix primerov
    print(LIS1([4, 1, 5, 7])) # 3
    print(LIS1([30, 40, 2, 5, 1, 7, 45, 50, 8])) # 5
    # še par naključno generiranih
    print(LIS1(nakl_sez()))
    print(LIS1(nakl_sez()))