# Créer une fonction qui prend en paramètre une String nommée “langage”.

def bidule(langage):
    # autre=str(langage)                           # initialise une variable avec le paramètre en chaîne de caractère
    if langage.lower() == "javascript":          # Si la valeur de “langage” est égale à “JavaScript” affichez “tu es un développeur web”
        print("tu es un développeur web")
    elif langage.lower() == "python":            # Sinon si la valeur de “langage” est égale à “python” affichez “tu es un développeur IA”
        print("tu es un développeur IA")
    elif langage.lower() == "java":              # Sinon si la valeur de “langage” est égale à “java” affichez “tu es un développeur logiciel”
        print("tu es un développeur logiciel")
    elif langage.lower() == "reactjs":           # Sinon si la valeur de “langage” est égale à “reactjs” affichez “tu es un developpeur mobile”
        print("tu es un développeur mobile")
    else :                                  # Sinon, affichez “un jour, je serai le meilleur développeur... ”
        print(f"un jour, je serai le meilleur développeur ")
        #{autre}

bidule("javascriPT")                       # appel la fonction pour tester