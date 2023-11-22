#   Créer une fonction qui prend en paramètre un nombre nommé “nombre”.
#   Afficher “positif” si le nombre est supérieur à 0
#   Afficher “negatif” si le nombre est inférieur à 0
#   Appeler cette fonction plusieurs fois en y passant des paramètres différents pour
#   afficher ces résultats.  

def bingo(nombre):                      #   initialise la fonction

              
    try:                                #   vérifie que :
        nombre = int(nombre)            #   le paramètre est un nombre
    except ValueError:                  #   sinon : message d'erreur
        print("Seul les nombres peuvent être positif ou négatif, pas les chaînes de caractères")
        return                          #   et arret de la fonction


    if nombre>0:                        #   si nombre est positif
        print("positif")
    elif nombre<0:                      #   si nombre est negatif
        print("negatif")
    else :                              #   autre
        print("mi-figue mi-raisin")



bingo(5)                                #   appel la fonction pour voir
bingo(-1)
bingo(0)
bingo("a")

