# Créer un programme qui demande à l’utilisateur trois longueurs a, b, c. À l'aide de ces
# trois longueurs, déterminer s'il est possible de construire un triangle.
# Déterminer ensuite si ce triangle est rectangle, isocèle, équilatéral ou quelconque.
# Attention : un triangle rectangle peut être isocèle.

print("-----------------------------------")
print("On va essayer de faire un triangle")
print("Il nous les longueur des 3 côtés")
print("-----------------------------------")
a=int(input("Entrez la Longueur du côté a : "))


try:
    if a == int(a) and a > 0:
        print(f"Merci, {a} est une valeur acceptable")
    else:
        print(f"Merci de donnre une valeur positive")
except ValueError:      # Message d'erreur !!!!!!!
    print("Merci d'entrer un nombre entier positif, on essaie de faire un triangle qui tiens la route.")



b=int(input("Entrez la Longueur du côté b : "))
c=int(input("Entrez la Longueur du côté c : "))