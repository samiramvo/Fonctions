from audioop import mul


def mul_num(liste):
    numb=1
    for x in liste:
     numb*=x
    return numb
liste=(8,2,3,0,7)
print(mul_num(liste))