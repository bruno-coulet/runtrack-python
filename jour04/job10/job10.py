# Écrire un programme qui calcule le produit de toutes les valeurs de la liste comprises
# dans l’intervalle [25, 90]

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def calcule():

    calcul_list=[]
    for i in L:
        if 25<i<90:
            calcul_list.append(i)
    print("le produit de toutes les valeurs de la liste comprises dans l’intervalle [25, 90] est  : ",sum(calcul_list))

calcule()



