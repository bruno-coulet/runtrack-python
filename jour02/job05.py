# Écrire un programme qui itère les nombres entiers de 1 à 100. Pour les
# multiples de trois, afficher "Fizz" au lieu du nombre et pour les multiples
# de cinq afficher "Buzz". Pour les nombres qui sont des multiples de trois
# et cinq, afficher "FizzBuzz".

i=1

while i<=100:
    if i%3 == 0:            #   le modulo retourne le reste de la division euclidienne
        print("Fizz")       #   si on divise par 3 et qu'il reste 0 on affiche fizz
    elif i%5 == 0:
        print("Buzz")
    else:
        print (i)
    i+=1

