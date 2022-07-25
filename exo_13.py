def triangle_pascal(nombre):
    i=[1]
    j=[0]
    for x in range(max(nombre,0)):
        print(i)
        i=[l+r for l,r in zip(i+j,j+i)]
    return nombre>=1
triangle_pascal(6)

