def min_pot(pi_matrika, i, j):
    """
    Rekunstruira pot iz tabele pi, ki jo dobimo po koncu floyd washallovega algoritma.
    """
    sez = list()
    zac = i
    kon = j
    while zac != kon:
        sez.append(kon)
        kon = pi_matrika[zac][kon]
    sez.append(kon)
    return sez[::-1]