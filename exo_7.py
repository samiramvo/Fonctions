def comp(chaine):
    maj=[]
    min=[]
    for c in chaine:
        if c.isupper():
            maj+=1
       
        if c.islower():
            min+=1
        
        else:
            pass

print(comp("La vie est beLLe"))