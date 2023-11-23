# Écrire un programme qui créer la liste d’entiers L = [7, 11, 42, 39, 2], votre programme
# devra pouvoir modifier la liste en augmentant de 1 la valeur de chaque élément de la liste.

L=[7, 11, 42, 39, 2]


def addition(liste):
    newListe = [i+1 for i in liste]

    print(newListe)

addition(L)

# def list():
#     L = [7, 11, 42, 39, 2]
#     for i in range (len(L)):
#         L[i] +=1
# .....

L = [7, 11, 42, 39, 2]
M = []

for i in L:
    i = i+1
    M.append(i+1)

print(M)



