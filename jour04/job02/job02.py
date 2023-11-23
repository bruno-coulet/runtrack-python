# Écrire une fonction qui contient une liste nommée “fruits” qui contient les string
# “pomme”, “cerise”, “orange”.

def verger():
    fruits = ["pomme", "cerise", "orange"]
    return fruits
   

# Affichez le 2e éléments de la liste.

print(verger()[1])  #   verger()    == fruits
                    #   donc
                    #   verger()[1] == fruits[1]
                    #   fruits[1] affiche la valeir de l'index 1, soit le deuxième élément de la liste
