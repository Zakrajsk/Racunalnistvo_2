from Intervalno_drevo import Vozel, Intervalno_drevo

test = Intervalno_drevo(Vozel([10, 30]))
test.vstavi([50, 60])
test.vstavi([70, 90])
test.vstavi([65, 80])
test.vstavi([5, 20])
test.vstavi([3, 50])
test.vstavi([80, 100])
test.vstavi([4, 20])
test.vstavi([20, 40])
test.vstavi([15, 20])

test.izpis()

print("-------------------Prvi prekrivajoci-------------------")

ya = test.Prekrivanje_z_intervalom([45, 46])
print(ya)

print("-------------------Vsi prekrivajoci-------------------")

vsi = test.Vsi_prekrivajoci([21, 66])

for en in vsi:
    print(en)


print("-------------------Brisanje-------------------")
#test.izbrisi([50, 60])

test.izpis()


print("-------------------Brisanje dela intervala-------------")

test.brisanje_dela_intervala([12, 42])


test.izpis()


print("-------------------Vstavljanje z zlivanjem-------------")

test_zlivanje = Intervalno_drevo(Vozel([10, 30]))
test_zlivanje.vstavi_z_zlivanjem([20, 40])
test_zlivanje.vstavi_z_zlivanjem([5, 8])
test_zlivanje.vstavi_z_zlivanjem([60, 70])
test_zlivanje.vstavi_z_zlivanjem([2, 4])
test_zlivanje.vstavi_z_zlivanjem([75, 80])

#test_zlivanje.izpis()