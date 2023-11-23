# Écrire un programme qui échange les valeurs de la première et de la dernière case
# d’une liste quelconque non vide.
L = [1, 2, 3, 4, 5]


def job06(L):
    # Ajoute le 1er élément à la fin de la liste
    L.append(L[0]) 
    # supprime le premier élément
    del L[0]
    # Ajout l'avant-dernier en début de liste
    L.insert(0,L[-2])
    # supprime l'avant dernier
    del L[-2]
    # affiche la liste
    print(L)


job06(L)
