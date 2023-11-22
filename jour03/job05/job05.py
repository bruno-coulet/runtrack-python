# Créer une fonction nommée “calcule” qui prend 3 paramètres :
#  “num1”, est un nombre,
# "operator", est un caractère (string) contenant le type d’opération(+, -, *, /, %),
# “num2”, est un nombre.

# La fonction doit retourner le résultat de l’opération.

def calcule(num1, operator, num2):      #   initialise la fonction

    num1=int(num1)                      #   num1 doit être un entier
    operator=str(operator)              #   opérator doit être une chaine
    num2=int(num2)                      #   num2 doit être un entier

    if operator == '+' :                #   Suivant l'operator
        resultat=num1+num2              #   le resultat sera différent
    elif operator == '-':
        resultat=num1-num2
    elif operator == '*':
        resultat=num1*num2
    elif operator == '%':
         resultat=num1%num2
    elif operator == '/':
          if num2 != 0:                 #   vérifie qu'on ne divise pas par zéro
            resultat=num1/num2
          else:                         #   si division par zéro : message d'erreur
            resultat="Cela ne se fait pas de diviser par zéro"  # il faut créer la variable resultat
                                        #   si l'opérateur est inepte
    else :
        resultat="Désolé, il est impossible de calculer ça"     # il faut créer la variable resultat


    return resultat                     #   la fonction retourne la variable resultat


#print(calcule(1, "+", 2))               #   appel la fonction poour vérifier



