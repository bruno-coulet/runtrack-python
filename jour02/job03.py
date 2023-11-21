# Créer un programme qui affiche tous les nombres de 0 à 100 compris SAUF 26, 37, 88

i=0             #   initialisation

while i <= 100:                         #   condition, tant que i plus petit que 100
    if i!=26 and i!=37 and i!=88:       #   condition, autre que 26, 37 et 88
        print(i)                        #   instructions
    i+=1                                #   incrémentation