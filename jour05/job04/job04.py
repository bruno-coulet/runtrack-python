# Écrire une fonction qui, recevant une taille n en paramètre, affiche un tapis de n+1
# ligne/n+1 colonne traversé par une diagonale.


def tapis(n):

    print(f"+{'-' * (n-1)}+")           # première ligne

    for i in range(2,n+1):                # lignes intermédiaires
        

        # if i==2:
        #     print(f"|{'#' * (n-i)} |")
        # else:
        print(f"|{'#' * (n-i)} {'#'*(i-2)}|")


    print(f"+{'-' * (n-1)}+")           # dernière ligne

tapis(10)