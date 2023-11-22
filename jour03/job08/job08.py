
def miam(type, saison):                       # Créer une fonction qui prend 2 paramètres
    # type=str(type)
    # saison=str(saison)

    if type=="fruits" and saison=="hiver":    # Si la valeur de “type” est égale à “fruits” et celle de saison est égale à “hiver”,
        print("orange, mandarine et kiwi")    # affichez “orange, mandarine et kiwi”
    elif type=="fruits" and saison=="été":    # Si la valeur de “type” est égale à “fruits” et que celle de saison est égale à “ete”
        print("Poire, fraise, cassis")        # affichez “Poire, fraise, cassis”
    elif type=="legume" and saison=="hiver":  # Si la valeur de “type” est égale à “legume” et que celle de saison est égale à “hiver”
        print("carotte, topinambour, endive") # affichez “carotte, topinambour, endive”
    elif type=="legume" and saison=="été":    # Si la valeur de “type” est égale à “legume” et que celle de saison est égale à “ete”
        print("artichaut, aubergine,navet")   # affichez “artichaut, aubergine,navet”

    else :
        print("mangez de la viande !")

miam("fruits", "été")                         # appel de la fonction pour voir
miam("fruits", "hiver")
miam("legume", "été")
miam("legume", "hiver")
miam ("a", "b")
miam(5, 6)
