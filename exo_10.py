def pairs(liste):
    new_liste=[]
    for i in liste:
        if i%2==0:
            new_liste.append(i)
    return new_liste

print(pairs([1,2,3,4,5,6,7,8,9]))        