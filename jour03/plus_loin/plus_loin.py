# Créer une fonction qui prend en paramètre un string et qui la retourne inversée.
# Par exemple, « nikana » deviendra « anakin ».

def envers(endroit):

    chaine=str(endroit)
    if isinstance(endroit, str): 
        print("".join(reversed(f"{chaine}")) )
    else:
        print("il faut une chaîne de caractères en paramètre, sinon ça ne marche pas")

envers ("a rebrousse poil")
envers("tiordne'l à ,à l'envers")
envers(24)
envers("snes xued sel snad ehcram aç ,radar")


#   Il y a ausis la méthode du slicing [::-1]  