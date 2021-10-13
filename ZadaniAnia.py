# zad 1
lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
print(lorem)

#zad 2
imie = "Ania"
nazwisko = "Mikulak"
litera_1 = imie[2]
litera_2 = nazwisko[3]
liczba_liter1 = lorem.count(litera_1)
liczba_liter2 = lorem.count(litera_2)
print("W tekście jest "  + str(liczba_liter1) +  " liter " + str(litera_1) + " oraz " + str(liczba_liter2) + " liter " + str(litera_2))

#zad 5
odw_imie = imie[::-1].capitalize()
odw_nazwisko = nazwisko[::-1].capitalize()
print(odw_nazwisko + " " + odw_imie)

