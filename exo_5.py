def factorielle(nombre):
    fact=1
    if nombre>0:
        for i in range(1,nombre+1):
            fact*=i
        return fact
   

print(factorielle(4))
