# zad 1
def funkcja(a_list, b_list):
    c_list = []
    for x in range(0, len(a_list) or len(b_list), 2):
        c_list.append(a_list[x])
        c_list.append(b_list[x+1])
    return c_list

a = [1, 2, 7, 8]
b = [3, 4, 8 ,8]

print(funkcja(a,b))



