#zad 2
def info(data_text):
    list1 = []
    list1[:0] = data_text
    lista_liter = set(list1)
    dict = {
        "length": len(data_text),
        "letters": lista_liter,
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower()
    }
    print(dict)
st = "Hejka"
info(st)