# Écrire un programme qui affiche dans la console un rectangle avec des ‘-’ et des ‘|’ en
# fonction des paramètres d’entrées, (width, height), par exemple :
# draw_rectangle(10, 3)

def draw_rectangle (width, height):
    
    for i in range(1, height + 1):
        #   1ère et dernière ligne
        if i == 1 or i == height:
            print("|",'-'*width,"|")

        #   lignes intermédiaire
        if 1<i<height:
            print("|",' '*width,"|")



draw_rectangle(5,7)
