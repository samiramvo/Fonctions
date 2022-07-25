import string,sys
def ispangram(str1,stralphabet=string.ascii_lowercase):
    stralphabet=set(stralphabet)
    return stralphabet<=set(str1.lower())

print(ispangram("La vie est belle"))
