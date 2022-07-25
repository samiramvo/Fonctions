from re import X
from tkinter import N


def nomb_par(nombre):
    sum=0
    for i in range(1,nombre):
        if nombre%i==0:
            sum+=i
    return sum==nombre

print(nomb_par(6))