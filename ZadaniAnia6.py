# zad 6
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = []
for x in range (5):
    lista2.append(lista[5+x])

for x in range(5):
    lista.pop(9 - x)

print(lista)
print(lista2)

# zad 7

lista3 = [0] + lista + lista2
lista3.sort(reverse=True)
print(lista3)

