# Écrire un programme qui crée une liste nommée “L” d’au moins 5 entiers
def job05():
    L = [1, 2, 3, 4, 5]

    # puis successivement :Afficher la deuxième valeur de la liste
    print(L[1])       

    # Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
    def modif():
        L[3] = L[2] + L[4]
    modif()

    # puis afficher le tableau.
    print(L)
    # puis afficher la dernière valeur de la liste.
    print(L[4])

job05()