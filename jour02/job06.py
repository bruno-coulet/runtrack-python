# Écrire un programme qui affiche les nombres premiers jusqu’à 1000.


#   initialise i
i=1                                        
#   La variable a stocke i divisé par 1         -   doit retourner un entier
a = i/1
#   variable b stocke i divisé par lui même     -   doit retourner 1
b = i/i



#i%2!=0                                     #   les nombre entiers sont tous impairs sauf 2
#while a.is_integer():  
 #  tant que la division par 1 retourne un entier     
    
while  i <= 1000:   #  tant que i=2 ou que i est impair et i <= 1000
    i+=1             
    while i == 2 or i % 2 != 0:
        print(i)                                 #   affiche i
                                       #   incremente i
    



