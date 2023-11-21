# Créer un programme qui parcourt les nombres de 0 à 20, affichez 1
# nombre sur 2 dans le terminal.



i=0             #   initialisation

while i < 20:   #   condition modifié par rapport à l'exercice précédent pour ne pas afficher 20
    print(i)    #   instructions
    i+=2        #   incrémentation


print("deuxième option")

for i in range(0,21,2):
    print(i)