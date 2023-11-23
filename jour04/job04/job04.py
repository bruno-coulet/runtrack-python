# Écrire une fonction qui contient une liste nommée “fruits” qui contient les strings
# “pomme”, “cerise”, “orange, Melon”.

def verger():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    fruits.insert(2, "Mangue")      #   Cette fonction doit à son appel ajouter la string “Mangue” à l’index 2.
    return fruits
