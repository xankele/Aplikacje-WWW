# zad 8
krotka1 = (111002, "Anna", "Mikulak")
krotka2 = (111001, "Anna2", "Mikulak1")
krotka3 = (111003, "Anna3", "Mikulak2")
krotka4 = (111004, "Anna4", "Mikulak3")
lista = [krotka1, krotka2, krotka3, krotka4]

# zad 9
slownik = {}
slownik = dict({krotka1[0]:[krotka1[1], krotka1[2]],krotka2[0]:[krotka2[1], krotka2[2]],krotka3[0]:[krotka3[1], krotka3[2]],krotka4[0]:[krotka4[1], krotka4[2]], "151100": ["Anna", "Mikulak", "ann@bill.com", "1999", "Olsztyn"]})
print(slownik)
