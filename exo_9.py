def premier(nombre):
    if nombre==1:
        return False
    elif nombre==2:
        return True
    else:
        for x in range (2,nombre):
            if (nombre%x==0):
                return False
        return True
print(premier(9))
print(premier(13))