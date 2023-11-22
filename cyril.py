chaine = [chr(k) for k in range(97, 123)] * 10

print(chaine[0])
for i in range(1, len(chaine), 2):
    for j in range(0, i+2):
        if j < len(chaine):
            print(chaine[j], end="")
    print()