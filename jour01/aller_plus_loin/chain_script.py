#   Écrivez un script qui détermine si une chaîne contient ou non le caractère « e ».
print(" ")
print(" ")
print("-----------------------------------------------------------------------")
print(" ")
print("ce programme détermine si une chaîne contient ou non le caractère « e »")
print(" ")
print("-----------------------------------------------------------------------")
print(" ")
print(" ")

blabla =str(input("Entrez une phrase et validez!")) # crée la variable à fouiller

# la fonction find() cherche la position d'un caractère dans une string.
# Lorsque le caractère est trouvé, elle renvoie l'index de la première occurrence.
# Lorsque le caractère n'est pas trouvé, elle renvoie -1.
print(" ")
print(" ")
print(" ")
if blabla.find("e") != -1:      # si la fonction find renvoie autre chose que -1, il y a "e" dans la chaine.
    print("Oui oui oui, cette phrase contient bien le caractère « e ».")
else:                           # si la fonction find renvoie -1, il n'y a pas "e" dans la chaine.
    print("J'ai bien fouillé, cette phrase ne contient pas le caractère « e ».")
print(" ")
print("------------------------------------------------------------------------")
print("---------------------------    A bientôt  ------------------------------")
print("------------------------------------------------------------------------")
print(" ")
print(" ")

