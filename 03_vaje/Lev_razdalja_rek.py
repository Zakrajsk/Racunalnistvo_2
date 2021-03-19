def levenshteinovaRazdalja(a, b):
    '''Vrne levenshteinovo razdaljo med nizoma a in b'''
    if a == "":
        return len(b)
    if b == "":
        return len(a)
    if a[-1] == b[-1]:
        razdalja = 0
    else:
        razdalja = 1
    koncna_razdalja = min(levenshteinovaRazdalja(a[:-1], b) + 1,
                          levenshteinovaRazdalja(a,b[:-1]) + 1,
                          levenshteinovaRazdalja(a[:-1],b[:-1]) + razdalja)
    return koncna_razdalja


print(levenshteinovaRazdalja("borba", "torba"))
print(levenshteinovaRazdalja("abc", "a"))
print(levenshteinovaRazdalja("ornitologija", "otoralingolog"))