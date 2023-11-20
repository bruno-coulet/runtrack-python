# Première ébauche
#  for i in(alphabet déjà stocké quelque part)
#     print(i)
#     i=i+1

# Chat GPT
# for i in range(ord('A'), ord('Z')+1):
#     print(chr(i), end=' ')
# print("\n")



# Recherche gogol : pyhton module alphabet > https://www.delftstack.com/

import string                    # importe le module Python string

# La constante string.ascii_lowercase contient les 26 caractères minuscules de l'alphabet au format chaîne.

print(string.ascii_lowercase)   # affiche le contenu de la constante sous forme de chaîne.