# Écrire une fonction qui contient une liste nommée “fruits” qui contient les strings
# “pomme”, “cerise”, “orange”. 

def verger():
    fruits = ["pomme", "cerise", "orange"]
    fruits.append("Melon")      #   Cette fonction doit à son appel ajouter à la liste “fruits” le string “Melon” à la fin de cette liste.
    return fruits


#print(verger())     # appel la function et en même temps cela équivayt à print (fruits)  donc cela affiche la liste