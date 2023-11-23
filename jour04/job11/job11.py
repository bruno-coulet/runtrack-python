# Écrire un programme qui crée la liste d’entiers L = [7, 11, 42, 39, 2]
# votre programme devra pouvoir modifier la liste en augmentant de 1 la valeur de chaque élément de la liste.
L=[7, 11, 42, 39, 2]


def increment(liste):
    newListe = [i+1 for i in liste]

    print(newListe)

increment(L)





