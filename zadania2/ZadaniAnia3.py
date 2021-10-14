# zad 3

def usun(text, letter):
    new = text.translate({ord(letter): None})
    return new

napis = usun("Hej tu ania", "a")
print(napis)