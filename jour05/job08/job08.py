#   Compare les éléments d'une liste
#   échange de place uniquement avec l'élément adjacent
#   jusqu'a ce que la liste soit triée dans l'ordre croissant

L = [5, 6, 4, 3, 1, 7, 8, 2]

# Fonction pour intervertir les éléments d'indices i et j dans la liste L
def intervert(L, i, j):
    L[i], L[j] = L[j], L[i]


def sortedList(L):
    operations=0
    n=len(L)
    for _ in range(n):          # il faut repasser dans la liste pusieurs fois
        for i in range(n - 1):
        # Compare l'élément actuel avec l'élément suivant
            if L[i] > L[i+1]:
                # Échange les éléments si nécessaire
                intervert(L, i, i+1)
                operations += 1

    print(f"Nombre de coups nécessaires pour trier la liste : {operations}")
    print(f"Liste triée : {L}")

sortedList(L)