from tkinter import N


def DijkstraSez(G, S):
    """
    Naredi dikstro na danem grafu in zacetnem vozliscu S s pomočjo navadnih seznamov
    G - seznam sosednosti
    S - indeks v seznamu sosednosti
    O(|V|^2)
    """
    n = len(G)
    razd = [float("inf")] * n
    obisk = [False] * n
    razd[S] = 0
    q = set() #notri damo vsa vozlisca
    while q:
        minVoz = 2 #dobimo vozel po zadnjem obisku z najmanjso ceno #se iz q uzamemo
        doMin = razd[minVoz]
        for i, w in G[minVoz]:
            if  doMin + w < razd[i]:
                razd[i] = doMin + w
            obisk[minVoz] = True 
            q.remove(minVoz)
        return razd

def DijkstraQ(G, S):
    """
    Naredi dikstro na danem grafu in zacetnem vozliscu S s pomočjo vrste z prioriteto
    G - seznam sosednosti
    S - indeks v seznamu sosednosti
    O((|E| + |V|) * log(|E|))
    """
    n = len(G)
    razd = [float("inf")] * n
    obisk = [False] * n
    razd[S] = 0
    PQ = [(0, S)] #Prioritetna vrsta (tukaj samo prikazana in ni pravilna implementacija)
    while len(PQ) != 0:
        doMin, minVoz = PQ.pop()
        if obisk[minVoz]:
            continue
        obisk[minVoz] = True
        razd[minVoz] = doMin
        for i, w in G[minVoz]:
            if not obisk[i]:
                PQ.push((doMin + w), i)
    return razd


def Hamiltonova_pot(G):
    """
    Ce obstaja vrne True, utezi v G so 1 ali je neutezen
    """
    pot = "naj_pot(G)"
    if len(pot) == "|VG|":
        return True
    return False
