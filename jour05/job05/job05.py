# Créer une fonction à laquelle on donne un message et un décalage, et la fonction
# renvoie alors le message décalé dans l'alphabet. Il faudra gérer le dépassement ('z'
# décalé vers la droite revient sur 'a', et 'a' décalé vers la gauche revient sur 'z').

import string
msg = "les sanglots longs des violons de l'automne bercent mon coeur d'une langueur monotone"
shift=3

def crypt(msg, shift):
    alphabet=list(string.ascii_lowercase)           # crée une liste qui contient l'alphabet
    result=""                                       # crée une liste vide pour le résultat
    
    for lettre in msg:
        if lettre in alphabet :
            index_original = alphabet.index(lettre)
            index_modifie = (index_original+shift) % 26
            lettre_chiffre = alphabet[index_modifie]
            result += lettre_chiffre
        else:
            result += lettre


    print(result)  

crypt(msg,shift)