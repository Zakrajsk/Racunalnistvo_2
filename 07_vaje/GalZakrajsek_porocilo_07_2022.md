## 1. naloga
Bellman Ford računa najkrajše poti od vozlišča $s$ do vseh ostalih.\
Vhod: Graf $G$ (usmerjen in utežen) in začetno vozlišče $s$.\
Predpostavke: Ni negativnih ciklov dovolimo pa negativne uteži.\
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
$A^*$ Podobno kot dikstra samo, da pri dikstri za naslednji korak vzamemo vozlisce z najmanjso povezavo samo da pri $A^*$ imamo se hevristično funkcijo, in za nov korak izberemo vozlišče z najmanjšo dolžino + hevristično funckijo.

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
                Q.push((d[u] + d(u, v), v))
                #pri A* in ta f(v) je hevristika
                Q.push((d[u] + d(u, v) + f(v), v))
```

### 2.1

4 sosednost: Manhattam $f(v) = abs(|t_1 - v_1| + |t_2 - v_2|)$ \
8 sosednost: Evklidska $f(v) = \sqrt{(t_1 - v_1)^2 + (t_2 - v_2)^2}$

### 2.2
Ideja: predpocesiranje: Naredimo FW (recimo da si to lahko privoščimo)
potem imamo hevrsitično funkcijo $f(u, v) = FW(u, v)$
