# Écrire un programme qui trie dans l’ordre croissant une liste passée en paramètre.
# SANS UTILISER DE FONCTION SYSTÈME (len, sort, round…..)

L = [50, 60, 40, 30, 10, 70, 80, 20]

# fonction qui remplace la fonction système len
def my_len(L):
    count=0
    for i in L:
        count+=1
    return count

# Fonction pour intervertir les éléments d'indices i et j dans la liste L
def intervert(L, i, j):
    L[i], L[j] = L[j], L[i]


def crescendo(L):
    n=my_len(L)
    for _ in range(n):          # il faut repasser dans la liste pusieurs fois
        for i in range(n - 1):
        # Compare l'élément actuel avec l'élément suivant
            if L[i] > L[i+1]:
                # Échange les éléments si nécessaire
                intervert(L, i, i+1)



crescendo(L)

# Affiche la liste triée
print("Liste triée :", L)
