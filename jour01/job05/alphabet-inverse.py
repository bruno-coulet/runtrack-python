#   Afficher l'alphabet inversé

import string   # importe le module Python string

# La constante string.ascii_lowercase contient les 26 caractères minuscules de l'alphabet au format chaîne.

alphabet_inverse = ''.join(reversed(string.ascii_lowercase))

print( alphabet_inverse)