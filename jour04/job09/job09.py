# Écrire un programme qui récupère la valeur, maximum et le minimum des éléments de
# la liste.

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]


def min_max():

    minimum=L[0]
    for i in L:
        if i < minimum:
            minimum = i
    print("La valeur minimale est : ",minimum)

    maximum=L[0]
    for i in L:
        if i > maximum:
            maximum=i
    print("La valeur maximale est : ",maximum)

min_max()


