# Créer une fonction nommée “time_to_text” qui prend en paramètre un nombre entier de
# minutes et affiche en console une chaine de caractère sous la forme de “X heures et Y
# minutes”.


def time_to_text(number):
    if isinstance(number, int) and number >= 0:
        hours = number // 60
        minutes = number % 60

        if hours == 1:
            hours_text = "heure"
        else:
            hours_text = "heures"

        if minutes == 1:
            minutes_text = "minute"
        else:
            minutes_text = "minutes"

        print(f"{hours} {hours_text} et {minutes} {minutes_text}")
    else:
        print("Veuillez entrer un nombre entier positif.")

time_to_text(131)