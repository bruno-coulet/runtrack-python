# de 0 à 100 inclus.
# moins de 40  il échoue au test.
# S'il a plus de 40, il réussit le test.
# une note de moins de strictement 3 points de son prochain multiple de 5
# alors sa note est arrondie à ce multiple de 5. Par exemple,
# un 83 sera arrondi à 85 alors qu’un 82 restera un 82.

# Pour simplifier le travail de Luke, écrivez une fonction qui prend en paramètre une liste
# de notes et qui renvoie une liste de notes, arrondies comme il se doit, quand cela est
# nécessaire.
notes=[10,12,14,9,62,13,14,32,66,27,95]
print(notes)

def luke(notes):

    notes_arrondies=[]

    for n in notes:
        
        modulo=n%5
        if modulo<3:
            notes_arrondies.append(n)
        else:
            notes_augmente=n+(5-modulo)
            notes_arrondies.append(notes_augmente)


    print(notes_arrondies)
            
luke(notes)

