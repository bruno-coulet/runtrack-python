#   Affiche l'alphabet :
# import string
# print(string.ascii_lowercase)

import string

# def alphabet():
#     alphabet=(string.ascii_lowercase)
#     return alphabet


alphabet_inverse = ''.join(reversed(string.ascii_lowercase))

print( alphabet_inverse)