#   Écrivez un script qui détermine si une chaîne contient ou non le caractère « e ».

print("ce programme détermine si une chaîne contient ou non le caractère « e »")
print("--------------------")

blabla =str(input("Entrez une phrase.")) # crée la variable à fouiller

# la fonction find() cherche la position d'un caractère dans une string.
# Lorsque le caractère est trouvé, elle renvoie l'index de la première occurrence.
# Lorsque le caractère n'est pas trouvé, elle renvoie -1.

if blabla.find("e") != -1:      # si la fonction find renvoie autre chose que -1, il y a "e" dans la chaine.
    print("La phrase contient le caractère « e ».")
else:                           # si la fonction find renvoie -1, il n'y a pas "e" dans la chaine.
    print("La phrase ne contient pas le caractère « e ».")

