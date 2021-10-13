#zad13
slownik = dict([("jeden", 1), ("dwa", 2), ("trzy", 3)])
slownik2 = dict([("jeden1", 11), ("dwa1", 21), ("trzy1", 31)])
lista = [slownik, slownik2]
s = '1 {0} 2 {1}'
print(s.format(*lista))