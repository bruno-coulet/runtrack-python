# Créer une fonction nommée “time_to_text” qui prend en paramètre un nombre entier de
# minutes et affiche en console une chaine de caractère sous la forme de “X heures et Y
# minutes”.

def time_to_text(number):
    if isinstance(number, int) and number>=0:
        hour=0
        if number<=59:
            print(f"0 heures et {number} minutes")
            return
        if 60<number<119:
            hour=1
            minute=number-60
        if 120<number<179:
            hour=2
            minute=number-60


    print(f"{hour} heures et {minute} minutes")

time_to_text(131)