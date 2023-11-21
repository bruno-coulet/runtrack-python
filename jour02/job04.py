# Créer un programme qui affiche en console les tables de multiplication de 1 à N.
# N étant un entier supérieur à zéro saisi par l’utilisateur.
# N'oubliez pas de vérifier tout ce qui est nécessaire pour assurer la fiabilité de votre programme.

n=int(input("Saississez un entier supérieur à zéro s\'il vous plait : "))


while n <= 0:                                    # vérifie que n est un entier positif
    n=int(input("Un entier supérieur à zéro s\'il vous plait, sinon ça ne marche pas : "))


table=1                                          # commence avec la table de 1

while table<=n:                                  # tant que table est inférieur à n
    
    i=1                                          # initialise i

    print(f"Table de multiplication de {table}") # annonce la table de multiplication en cours

    while i<=10:                                 # tant que i est inférieur ou égale à 10
        print(f"{table} x {i} = {table * i}")    # affiche le calcul en cours     
        i+=1                                     # incrémente i

    table+=1                                     # incrémente la table de multiplication