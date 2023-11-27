# Écrire un programme qui affiche dans la console un triangle avec des ‘_’, des
# ‘\’ et des ‘/’ en fonction de l’input entré, qui représentera la hauteur.

height= int(input("Choisissez une hauteur : "))

def triangle(height):

    width=height*2
    print(' '*(height+1),'/\\')                         # première ligne : espace x hauteur, /\
    for i in range (1, height+1):                       
        print(' '*(height-i+1),"/",' '*2*(i-1),"\\")    # intermidiaires : espace défini, /, espace x 2(i-1), \ 

    print(" /",'_'*width,"\\")                          # dernière ligne : /, _ x 2 hauteur, \


triangle(height)