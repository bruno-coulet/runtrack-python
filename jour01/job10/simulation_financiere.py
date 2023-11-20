# Initialiser deux variables

invest = int(input("Investissement initial :")) #   variable : montant initial de l’investissement
rate = float(input("Taux de rendement annuel :")) #   variable : taux de rendement annuel en pourcentage.



# Afficher en console le gain annuel en fonction du taux de rendement.

gain = invest * (rate / 100)            #   variable : investissement * taux

gain_round = round(gain, 2)   #   Arrondir le résultat à deux décimales

print(f"gain annuel: {gain_round} kopecks")           #   affiche le résultat de la variable




#   L’investisseur augmente son capital de 5 000 euros.

invest_update=invest+5000
print("L'investisseur ajoute 5000 kopeck")
#   le taux augmente de 2%.
rate_update=rate+2
print("Le taux augmente de 2%")




# Calculer à nouveau le gain de l’investisseur et afficher en console le résultat.

gain_update = invest_update * (rate_update / 100)
gain_round = round(gain_update, 2)   #   Arrondir le résultat à deux décimales
print(f"Suite aux derniers évènements, voici le nouveau gain annuel prévu : {gain_round} kopecks")



# L'investisseur retire 10% du montant total, suite à ce retrait, le rendement diminue de 1%.

invest=invest*0.9
rate=rate_update-1

# Calculer le montant final de l’investissement et afficher le nouveau gain.

gain=invest*(rate/100)
gain_round = round(gain, 2)   #   Arrondir le résultat à deux décimales
print(f"nouveau gain annuel après baisse du capital et du taux: {gain_round} kopecks")