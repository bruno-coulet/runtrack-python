# Écrire un programme qui compte le nombre de multiples de 3 présents dans la liste
L = [8, 24, 48 ,2 ,16]


def multiple_de_3():
    x3=0                        # Initialise x3  
    for i in L:
        if i%3==0:              # si l'élément en cours se divise par 3
            x3+=1               # ça incrémente la variable x3              
    print(x3)                   # affiche x3


multiple_de_3()