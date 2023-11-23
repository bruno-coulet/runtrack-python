# Créer une fonction nommée “time_to_text” qui prend en paramètre un nombre entier de
# minutes et affiche en console une chaine de caractère sous la forme de “X heures et Y
# minutes”.

def time_to_text(number):
    heure = number // 60
    minute = number %60

    print( heure,"heures", minute,"minutes")

time_to_text(131)