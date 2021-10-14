# zad 4
def temperature(degrees, temperature_type):
    if(temperature_type == 'fah'):
        print((degrees*9/5) +32)
    elif(temperature_type == 'ran'):
        print((degrees*1.8) + 491.67)
    elif(temperature_type == 'kel'):
        print(degrees + 273.15)
    else:
        print("Wrong type")
temperature(20, 'kel')
