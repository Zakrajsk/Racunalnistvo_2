import random
random.seed(240)

def LIS(sez):
    """
    Najde dolžino najdalšega podzaporedja.
    """
    prviEl = [float('-inf')]
    novSez = prviEl + sez # dodamo -neskončno na začeteku seznama

    def LISBIGGER(i,j):
        """
        Najde dolžino najdalšega podzaporedja od j do n, kjer je j večji i.
        """
        if j > (len(sez)): # zaustevitveni pogoj
            return 0
        elif novSez[i] >= novSez[j]:
            return LISBIGGER(i,j + 1) # pogledamo ali bomo vzeli j-ti element
        else:
            spustimo = LISBIGGER(i,j+1) # spustimo j-ti element
            vzamemo = LISBIGGER(j,j+1) + 1 # vzamemo j-ti elemnt
            return max(spustimo, vzamemo) # vzamemo optimalno vrednost
    return LISBIGGER(0,1) # kličemo LISBigger na začetku seznama