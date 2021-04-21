import math

#MATRIČNO SEŠTEVANJE IN MNOŽENJE
#Za uporabo formul v Strassenovem algoritmu je potrebno implementirati še odštevanje (easy AF ;))

def sestej(A, B):
    '''
    Sešteje dani matriki A in B, ki sta podani kot seznama seznamov.
    Seštevanje je možno le, če sta matriki enakih dimenzij.

    Časovna zahtevnost: O(N^2)
    '''
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        return C

def odstej(A, B):
    '''
    Odšteje dani matriki A in B, ki sta podani kot seznama seznamov.
    Odštevanje je možno le, če sta matriki enakih dimenzij.

    Časovna zahtevnost: O(N^2)
    '''
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        C = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        return C

def zmnozi(A, B):
    '''
    Zmnoži dani matriki A in B, ki sta podani kot seznama seznamov.
    Množenje je možno le, če ima prva matrika toliko stolpcev kolikor ima druga vrstic.

    Časovna zahtevnost: O(N^3)
    '''
    if len(A[0]) == len(B):
        C = [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]
        return C

#POMOŽNE FUNCKIJE ZA STATIČNO OBLAGANJE
    
def dopolni(A, B):
    '''
    Dani matriki dopolni do kvadratnih matrik sodih dimenzij tako,
    da matrikama doda zadostno število ničelnih vrstic in/ali stolpcev.
    Vrne četverico dveh dopolnjenih matrik ter števili vrstic in stolpcev,
    ki jih moramo končnemu produktu odstraniti, da dobimo ustrezne dimenzije
    produkta.

    Časovna zahtevnost: O(N^2)
    '''
    # Dopolnjeni matriki bosta kvadratni z dimenzijami, ki so potence števila 2
    maxDimenzija = max(len(A), len(A[0]), len(B), len(B[0]))
    potenca = math.ceil(math.log2(maxDimenzija))
    dopolnjenaDimenzija = 2 ** potenca
        
    dopolnjenaA = []
    dopolnjenaB = []

    dodaneVrsticeA = dopolnjenaDimenzija - len(A)
    dodaniStolpciA = dopolnjenaDimenzija - len(A[0])
    dodaneVrsticeB = dopolnjenaDimenzija - len(B)
    dodaniStolpciB = dopolnjenaDimenzija - len(B[0])

    # Dopolnimo A do kvadratne matrike tako,
    # da jo konstruiramo na novo
    for i in range(dopolnjenaDimenzija):
        vrstica = []
        for j in range(dopolnjenaDimenzija):
            if(i < len(A) and j < len(A[0])):
                vrstica.append(A[i][j])
            else:
                vrstica.append(0)
        dopolnjenaA.append(vrstica)
        
    # Dopolnimo B do kvadratne matrike tako,
    # da jo konstruiramo na novo
    for i in range(dopolnjenaDimenzija):
        vrstica = []
        for j in range(dopolnjenaDimenzija):
            if(i < len(B) and j < len(B[0])):
                vrstica.append(B[i][j])
            else:
                vrstica.append(0)
        dopolnjenaB.append(vrstica)

    # Koliko vrstic in stolpcev moramo odstraniti končnemu produktu? A je dimenzij m×n.
    # V primeru m >= n odstranimo minimum dodanih vrstic in minimum dodanih stolpcev,
    # sicer odstranimo maksimum dodanih vrstic in maksimum dodanih stolpcev.
    if(len(A) >= len(A[0])):
        return (dopolnjenaA, dopolnjenaB, min(dodaneVrsticeA, dodaneVrsticeB), min(dodaniStolpciA, dodaniStolpciB))
    else:
        return (dopolnjenaA, dopolnjenaB, max(dodaneVrsticeA, dodaneVrsticeB), max(dodaniStolpciA, dodaniStolpciB))

def reduciraj(trojica):
    '''
    Dano trojico dopolnjene matrike in števil
    dodanih stolpcev in/ali vrstic pretvori v
    matriko brez dodanih stolpcev in/ali vrstic.

    Časovna zahtevnost: O(N^2)
    '''
    A = []
    # Zmanjšanje dimenzij 
    m = len(trojica[0]) - trojica[1]
    n = len(trojica[0][0]) - trojica[2]
    # Matriko konstruiramo na novo
    for i in range(m):
        vrstica = []
        for j in range(n):
            vrstica.append(trojica[0][i][j])
        A.append(vrstica)
    return A

def razbijVBloke(A):
    '''
    Za dano matriko dimenzij 2n×2m, vrne četverico blokov matrike,
    dimenzij n×m.
    P predstavlja levi zgornji blok, Q predstavlja desni zgornji blok,
    R predstavlja levi spodnji blok, S predstavlja desni spodnji blok.

    Časovna zahtevnost: O(N^2)
    '''
    P = []
    Q = []
    R = []
    S = []

    # Dimenzije blokov
    n = len(A) // 2
    m = len(A[0]) // 2

    # Konstrukcija bloka P
    for i in range(n):
        vrstica = []
        for j in range(m):
            vrstica.append(A[i][j])
        P.append(vrstica)
    # Konstrukcija bloka Q
    for i in range(n):
        vrstica = []
        for j in range(m, 2 * m):
            vrstica.append(A[i][j])
        Q.append(vrstica)
    # Konstrukcija bloka R
    for i in range(n, 2 * n):
        vrstica = []
        for j in range(m):
            vrstica.append(A[i][j])
        R.append(vrstica)
    # Konstrukcija bloka S
    for i in range(n, 2 * n):
        vrstica = []
        for j in range(m, 2 * m):
            vrstica.append(A[i][j])
        S.append(vrstica)
    return (P, Q, R, S)

def sestaviBloke(cetverica):
    '''
    Za dano četverico matrik dimenzij n×m, vrne matriko dimenzij 2n×2m,
    bločno sestavljeno iz danih matrik.
    P predstavlja levi zgornji blok, Q predstavlja desni zgornji blok,
    R predstavlja levi spodnji blok, S predstavlja desni spodnji blok.

    Časovna zahtevnost: O(N^2)
    '''
    P, Q, R, S = cetverica
    A = []

    # Dimenzije blokov
    n = len(P)
    m = len(P[0])

    # V prvih n vrstic
    for i in range(n):
        vrstica = []
        # dodamo elemente bloka P v prvih n stolpcev
        for j in range(m):
            vrstica.append(P[i][j])
        # dodamo elemente bloka Q v drugih n stolpcev
        for j in range(m):
            vrstica.append(Q[i][j])
        A.append(vrstica)
    # V drugih n vrstic
    for i in range(n):
        vrstica = []
        # dodamo elemente bloka R v prvih n stolpcev
        for j in range(m):
            vrstica.append(R[i][j])
        # dodamo elemente bloka S v drugih n stolpcev
        for j in range(m):
            vrstica.append(S[i][j])
        A.append(vrstica)
    return A

#ALGORITEM OBIČAJNEGA MATRIČNEGA MNOŽENJA S STRATEGIJO DELI IN VLADAJ

def zmnoziDAC(matrika1, matrika2):
    '''
    Zmnoži dani matriki A in B, ki sta podani kot seznama seznamov
    s strategijo deli in vladaj (divide-and-conquer).
    Množenje je možno le, če ima prva matrika toliko stolpcev kolikor ima druga vrstic.

    Časovna zahtevnost: O(N^3)
    '''
    if len(matrika1[0]) == len(matrika2):

        # Matriki dopolni do kvadratnih matrik in ugotovi, koliko vrstic in stolpcev
        # bo potrebno odstraniti, da bo končen produkt ustreznih dimenzij
        A, B, dodaniStolpci, dodaneVrstice = dopolni(matrika1, matrika2)

        # Dimenzije obeh kvadratnih matirk
        n = len(A)
        
        def DAC(matrika1, matrika2, n):
            '''
            Jedro funkcije, ki izvaja algoritem matričnega množenja s pristopom deli in vladaj.
            '''
            # Produkt dveh matrik 1×1
            if n == 1:
                return [[matrika1[0][0] * matrika2[0][0]]]
            # Produkt dveh matrik 2×2
            if n == 2:
                return [
                        [matrika1[0][0] * matrika2[0][0] + matrika1[0][1] * matrika2[1][0],
                         matrika1[0][0] * matrika2[0][1] + matrika1[0][1] * matrika2[1][1]],
                        [matrika1[1][0] * matrika2[0][0] + matrika1[1][1] * matrika2[1][0],
                         matrika1[1][0] * matrika2[0][1] + matrika1[1][1] * matrika2[1][1]]
                        ]
            else:
                # Kvadratni matriki 2^n×2^n razbijemo na bloke 2^(n-1)×2^(n-1)
                A11, A12, A21, A22 = razbijVBloke(A)
                B11, B12, B21, B22 = razbijVBloke(B)

                # in rekurzivno izvedemo na blokih 2^(n-1)×2^(n-1) ter končen rezultat sestavimo iz blokov
                P = sestej(DAC(A11, B11, n // 2), DAC(A12, B21, n // 2))
                Q = sestej(DAC(A11, B12, n // 2), DAC(A12, B22, n // 2))
                R = sestej(DAC(A21, B11, n // 2), DAC(A22, B21, n // 2))
                S = sestej(DAC(A21, B12, n // 2), DAC(A22, B22, n // 2))
            
                return sestaviBloke((P, Q, R, S))

        produkt = DAC(A, B, n)

        # Odstranimo vrstice in stolpce, ki so bili dodani pri dopolnitvi do kvadratnih matrik
        return reduciraj((produkt, dodaniStolpci, dodaneVrstice))

#STRASSENOV ALGORITEM MATRIČNEGA MNOŽENJA

def zmnoziStrassen(matrika1, matrika2):
    '''
    Zmnoži dani matriki A in B, ki sta podani kot seznama seznamov
    z uporabo Strassenovega algoritma, ki temelji na strategiji deli in vladaj.
    Množenje je možno le, če ima prva matrika toliko stolpcev kolikor ima druga vrstic.

    Časovna zahtevnost: O(N^Log2(7))
    '''
    if len(matrika1[0]) == len(matrika2):

        # Matriki dopolni do kvadratnih matrik in ugotovi, koliko vrstic in stolpcev
        # bo potrebno odstraniti, da bo končen produkt ustreznih dimenzij
        A, B, dodaniStolpci, dodaneVrstice = dopolni(matrika1, matrika2)

        # Dimenzije obeh kvadratnih matirk
        n = len(A)
        
        def Strassen(matrika1, matrika2, n):
            '''
            Jedro funkcije, ki izvaja Strassenov algoritem algoritem matričnega množenja.
            '''
            # Produkt dveh matrik 1×1
            if n == 1:
                return [[matrika1[0][0] * matrika2[0][0]]]
            # Produkt dveh matrik 2×2
            if n == 2:
                return [
                        [matrika1[0][0] * matrika2[0][0] + matrika1[0][1] * matrika2[1][0],
                         matrika1[0][0] * matrika2[0][1] + matrika1[0][1] * matrika2[1][1]],
                        [matrika1[1][0] * matrika2[0][0] + matrika1[1][1] * matrika2[1][0],
                         matrika1[1][0] * matrika2[0][1] + matrika1[1][1] * matrika2[1][1]]
                        ]
            else:
                # Kvadratni matriki 2^n×2^n razbijemo na bloke 2^(n-1)×2^(n-1)
                A11, A12, A21, A22 = razbijVBloke(A)
                B11, B12, B21, B22 = razbijVBloke(B)

                # Definiramo matrike Mi po Strassenovih formulah
                M1 = Strassen(sestej(A11, A22), sestej(B11, B22), n // 2)
                M2 = Strassen(sestej(A21, A22), B11, n // 2)
                M3 = Strassen(A11, odstej(B12, B22), n // 2)
                M4 = Strassen(A22, odstej(B21, B11), n // 2)
                M5 = Strassen(sestej(A11, A12), B22, n // 2)
                M6 = Strassen(odstej(A21, A11), sestej(B11, B12), n // 2)
                M7 = Strassen(odstej(A12, A22), sestej(B21, B22), n // 2)

                # Definiramo bloke produkta po Strassenovih formulah,
                # rekurzivno izvedemo na blokih 2^(n-1)×2^(n-1) ter končen rezultat sestavimo iz blokov
                C11 = sestej(odstej(sestej(M1, M4), M5), M7)
                C12 = sestej(M3, M5)
                C21 = sestej(M2, M4)
                C22 = sestej(sestej(odstej(M1, M2), M3), M6)
                                          
                return sestaviBloke((C11, C12, C21, C22))

        produkt = Strassen(A, B, n)

        # Odstranimo vrstice in stolpce, ki so bili dodani pri dopolnitvi do kvadratnih matrik
        return reduciraj((produkt, dodaniStolpci, dodaneVrstice))


#TESTI

A = [[-1, 3],
     [-1, 1]]
B = [[0, 2],
     [3, 1]]
C = [[1, 2, 3, 4]]
D = [[-4],
     [3],
     [-2],
     [1]
     ]

print("Matrika A:")
print(A)
print("Matrika B:")
print(B)
print()
print("Produkt A * B:")
print("Običajno množenje:", zmnozi(A, B))
print("Deli in vladaj:", zmnoziDAC(A, B))
print("Strassenov algoritem:", zmnoziStrassen(A, B))
print()
print("Produkt B * A:")
print("Običajno množenje:", zmnozi(B, A))
print("Deli in vladaj:", zmnoziDAC(B, A))
print("Strassenov algoritem:", zmnoziStrassen(B, A))
print()
print()
print("Matrika C:")
print(C)
print("Matrika D:")
print(D)
print()
print("Produkt C * D:")
print("Običajno množenje:", zmnozi(C, D))
print("Deli in vladaj:", zmnoziDAC(C, D))
print("Strassenov algoritem:", zmnoziStrassen(C, D))
print()
print("Produkt D * C: ")
print("Običajno množenje:", zmnozi(D, C))
print("Deli in vladaj:", zmnoziDAC(D, C))
print("Strassenov algoritem:", zmnoziStrassen(D, C))
