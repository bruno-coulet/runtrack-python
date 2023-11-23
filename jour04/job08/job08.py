# Écrire un programme qui calcule la somme de toutes les valeurs paires de la liste
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

def calcule():
    somme=0
    for i in L:
        if i%2==0:
            somme +=i
    print("la somme des éléments pair contenus dans la liste est de : ",somme)

calcule()