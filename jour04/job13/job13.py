#Écrivez un programme qui supprime les doublons de la liste suivante :
#SANS UTILISER DE FONCTION SYSTÈME (len, sort, round.....)

L = [10,20,30,20,10,50,60,40,80,50,40]

# fonction qui remplace la fonction système len
def my_len(lst):
    count=0
    for i in lst:
        count+=1
    return count


# Fonction pour supprimer les doublons
def doubl_cleared(lst):
    n = my_len(lst)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if lst[i] == lst[j]:
                lst.pop(j)
                n -= 1
            else:
                j += 1
        i += 1

doubl_cleared(L)
print(L)