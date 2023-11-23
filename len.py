# Réécrire len
# ca compte la longueur de la string ou de la liste

def my_len(list):
    count=0
    for i in list:
        count+=1
    return count

L = [4,5,6,7,8,9,7,4,8,5,7]

print(my_len(L))