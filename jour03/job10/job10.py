# Créer une fonction qui vérifie que le nombre est bien un chiffre entier et positif
# puis qu'il est pair ou impair.
def pair_impair(number):
    if isinstance(number, int) and number>=0:
        if number%2==0:
            print(f"{number} est un chiffre pair")
        else:
            print(f"{number} est un chiffre impair")


#   Appeler cette fonction plusieurs fois avec des valeurs différentes
pair_impair(1)
pair_impair(2)
pair_impair(3)
pair_impair(4)
print("Et ce n'est pas vraiment négociable")
