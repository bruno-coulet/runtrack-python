
def moyenne(note_1, note_2, note_3):            # Créez une fonction nommée "moyenne" qui prend en paramètre trois notes.
    return (note_1 + note_2 + note_3)/3         # et retourne la moyenne de ces notes.


n1=float(input("Entrez la note n°1 : "))         # stocke les notes dans 3 variables n1, n2 et n3
n2=float(input("Entrez la note n°2 : "))   
n3=float(input("Entrez la note n°3 : "))


    # enregistrez le résultat de la fonction"moyenne" dans une variable appelée "moyenne_etudiant".
moyenne_etudiant = moyenne(n1, n2, n3)


    # Afficher ensuite une phrase en fonction de la moyenne de l’étudiant :

if moyenne_etudiant < 8 :           # Élève devant faire des efforts si la moyenne est comprise entre 0 et 7. 
    print("Élève devant faire des efforts")
elif moyenne_etudiant < 11 :        # Élève moyen si la moyenne est comprise entre 10 et 8. 
    print("Élève moyen")
elif moyenne_etudiant < 15 :        # Bon élève si la moyenne est comprise entre 14 et 11. 
    print("Bon élève")
else:                               # Très bon élève si la moyenne est comprise entre 20 et 15.
    print("Très bon élève")