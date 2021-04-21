def Page_rank(matrika_povezav, damping_faktor, st_iteracij):
    """
    Izvede page rank na grafu ki je opisan z matriko povezav 0 - ni 1 - je povezava
    """
    st_strani = len(matrika_povezav)
    page_ranki = [1 / st_strani for _ in range(st_strani)]

    for _ in range(st_iteracij):
        temp_ranki = [0] * st_strani

        for i in range(st_strani):
            vsota_suma = 0

            #racunanje vsota zadnjega dela enacbe
            for j in range(st_strani):
                if matrika_povezav[j][i] == 0: #spustimo ce stran ne kaze na stran na katero racunamo
                    continue
                vsota_suma += page_ranki[j] / sum(matrika_povezav[j])

            temp_ranki[i] = (1 - damping_faktor) / st_strani + damping_faktor * vsota_suma
        
        page_ranki = temp_ranki
        print(page_ranki)
    return page_ranki


matrika_povezav = [[0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [1, 1, 1, 0, 0], [1, 1, 0, 1, 0]]

Page_rank(matrika_povezav, 0.85, 2)