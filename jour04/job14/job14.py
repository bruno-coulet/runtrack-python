# Créer un programme contenant une fonction nommée “my_long_word”. Cette fonction
# doit prendre deux paramètres, un chiffre entier et une chaîne de caractère.
# Cette fonction doit retourner les mots plus long que le chiffre passé en paramètre.


a = 3
b = "Le jour pousse la nuit Et la nuit sombre Pousse le jour qui luit D'une obscure ombre"

# fonction qui remplace la fonction système len
def my_len(L):
    count=0
    for i in L:
        count+=1
    return count


def my_long_word(a, b):
    # Diviser la phrase en mots
    words = b.split()

    # Liste les mots dont la longueur est supérieure à a
    long_words = [word for word in words if my_len(word) > a]
    
    # Joindre les mots filtrés en une seule chaîne
    result = ' '.join(long_words)

    print(result)


my_long_word(4,b)

