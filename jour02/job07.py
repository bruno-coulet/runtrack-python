# À partir de la chaîne "abcdefghijklmnopqrstuvwxyz" *
# 10, écrivez un programme qui récupère et affiche autant
# de caractères que possible de cette chaîne sous forme
# de suite pyramidale.



# for i in range(len(alphabet)):
#     print(alphabet[i])
#     j=i+1
#     for j in range(len(alphabet)):
#         print(alphabet[i,j])

alphabet="abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabet)):  # tant que i est entre 0 et 25 (26 lettres de l'alphabet)
    print(alphabet[:i+1])       # affiche du début jusqu'à i et incrémente i
    