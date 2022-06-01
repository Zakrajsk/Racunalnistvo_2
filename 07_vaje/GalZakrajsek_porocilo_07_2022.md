# Vaje 31.3.2022 Bellman Ford, A*

**Ime:** Gal Zakrajšek

**Datum:** 07.04.2022


Na vajah smo obravnavali Bellman Fordov algoritem in pa A*. Potem smo imeli tekmovanje kdo prej pride do rešitev pri nalogah, ki so navedene v poročilu pod naslovom tekmovanje.


## Komentarji in opombe

Vaje so bile super, saj je tekmovanje naredilo vaje zabavne in so hitro minile.


## 1. naloga
**Navodilo** Ponovitev Bellman Fordovega algoritma. Kaj sprejme kot vhod, kaj izračuna, predpostavke, ideja algoritma.

Bellman Fordov algoritem računa najkrajše poti od vozlišča $s$ do vseh ostalih. Predpostaviti moramo, da graf nima negativnih ciklov dovoljujemo pa negativne uteži.\
Vhod: Graf $G$ (usmerjen in utežen) in začetno vozlišče $s$.\
Ideja:

```python
d = [inf] * n
d[s] = 0
for n in range (n - 1):
    for u, v, w in E(G):
        if d[u] + w < d[v]:
            d[v] = d[u] + w
```

Časovna zahtevnost: $O(|V| * |E|)$

## 2. naloga
**Navodilo** Kaj je A*? Kako izgleda "tipična" implementacija?

$A^*$ algoritem je podoben kot dijkstra samo, da pri dijkstri za naslednji korak vzamemo vozlišče z najmanjšo povezavo, pri $A^*$ pa imamo še hevristično funkcijo, in za nov korak izberemo vozlišče z najmanjšo dolžino + vrednost te hevristične funckije.

```python
def Dijkstra(G, s, t):
    .
    .
    .
    while Q:
        .
        .
        for v in G[n]:
            for not visited[v]:
                # Navadna dijsktra
                Q.push((d[u] + d(u, v), v))
                # A* in ta f(v) je hevristicna funkcija
                Q.push((d[u] + d(u, v) + f(v), v))
```

### 2.1. naloga
**Navodilo** Recimo, da imamo graf v obliki mreže z ovirami. Navedi primer hevristike. Kje bi še lahko uporabili tako hevristiko?

Hevristika za navedeni primer bi lahko bila Manhattanska razdalja. Odvisno, kakšno sosednost bi gledali:\
4 sosednost: Manhattamska $f(v) = abs(|t_1 - v_1| + |t_2 - v_2|)$ \
8 sosednost: Evklidska $f(v) = \sqrt{(t_1 - v_1)^2 + (t_2 - v_2)^2}$

### 2.2. naloga
**Navodilo** Recimo, da imamo graf, kjer so vozlišča mest (vasi, kraji, križišča..) in povezave ceste med njimi. Vsaka povezava e ima utež w(e), ki predstavlja razdaljo oz. pot potovanja po tej povezavi. Poleg tega ima vsaka povezava e še "ocenjen čas zastojev" w'(e, t), kjer t predstavlja trenutni čas. Ocenjen čas zastojev je tako odvisen od časa. Želimo čim hitreje dobiti odgovore na poizvedbe oblike: Kako najhitreje priti iz mesta A do mesta B.
Ideja: S predprocesiranjem skonsktuirajte ustrezno hevristiko za A* algoritem.

Ideja: predpocesiranje: Naredimo Floyw-Warshalla, če si ga lahko privoščimo. Potem imamo hevrsitično funkcijo $f(u, v) = FW(u, v)$

# Tekmovanja 31.3.2022.

## 4. naloga
**Navodilo**  Lotili se bomo neke vrste tekmovanja. Na spletni strani https://snap.stanford.edu/data/roadNet-TX.html dobite datoteko z opisom cestnega omrežja v Texasu. Vozlišča so torej križišča, ceste pa so povezave.

### 4.1. naloga
**Navodilo** Koliko vozlišč (križišč) je na najkrajši poti od vozlišča 100 do 100000?

### 4.2. naloga
**Navodilo** Recimo, da začnemo v vozlišču 0 in želimo končati v vozlišču 10000, vmes pa moramo obiskati vozlišča 1000, 3000, 5000, 8000 in 9000. Obiskujemo jih lahko v poljubnem vrstnem redu in obiščemo jih lahko tudi večkrat. Pomembno je le to, da začnemo v 0 in končamo v 10000. Poiščite čim krajšo pot, ki ustreza tem zahtevam.

Sprva je vsak reševal sam, vendar ko je prvi prišel do rešitve sva z Liamom skupaj delala in poiskušala rešiti tudi drugi del. Koda s katero sva reševala je naslednja.

```python
import time
from heapq import heappush, heappop
import itertools


def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
        cleaned = [[num for num in line.split("\t")] for line in lines]
        data_dict = {}
        for line in cleaned:
            if not line[0] in data_dict:
                data_dict[line[0]] = []
            data_dict[line[0]].append(line[1].replace("\n", ""))
        return data_dict


def get_path(data_dict, start, end):
    
    shortest_paths = {key: float("inf") for key in data_dict.keys()}
    shortest_paths[start] = 0
    visited = set()

    pq = []
    heappush(pq, (0, start))
    while len(pq) != 0:
        _, trenutno = heappop(pq)
        visited.add(trenutno)
        # Gremo skozi sosede
        for sosed in data_dict[trenutno]:
            razdalija = 1
            # Preverimo če povezava obstaja in voz. ni bilo obiskano
            if razdalija != float("inf") and sosed not in visited:
                stara_cena = shortest_paths[sosed]
                nova_cena = shortest_paths[trenutno] + 1
                if sosed == end:
                    return min(stara_cena, nova_cena)
                if nova_cena < stara_cena:  # Če bolj poceni menjamo
                    heappush(pq, (nova_cena, sosed))
                    shortest_paths[sosed] = nova_cena
    return None


def get_path_while_visiting(data_dict, start, end, visit):
    permutations = list(itertools.permutations(visit))
    
    lengths = []
    paths = []
    calculated_pairs = {}
    print("Started")
    for permutation in permutations:
        start_time = time.time()
        path = [start] + list(permutation) + [end]
        length = 0
        for i in range(len(path) - 1):
            pair = (path[i], path[i + 1])
            if pair in calculated_pairs:
                length += calculated_pairs[pair]
            else:
                leng = get_path(data_dict, path[i], path[i + 1])
                calculated_pairs[pair] = leng
                length += get_path(data_dict, path[i], path[i + 1])

        lengths.append(length)
        paths.append(paths)
        print(f"{path}: {time.time() - start_time}s, len: {length}")
    
    return min(lengths)

if __name__ == "__main__":
    start = time.time()
    graph = read_file("vaje7_31_3\data.txt")
    print(f"Time took: {time.time() - start}")
    start = time.time()
    print(get_path_while_visiting(graph, "0", "10000", ["1000", "3000", "5000", "8000", "9000"]))
    print(f"Time took: {time.time() - start}")
```
