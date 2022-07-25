def inverser(chaine):
    chaine=list(chaine)
    chaine.reverse()
    str(chaine)
    return "".join(chaine)

print(inverser("relou"))