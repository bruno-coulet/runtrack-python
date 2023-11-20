# Create product variables.
product_name='cocotte'
product_price=int(20)
product_quantity=int(10)


# Display product_info
def product_info(product_name, product_price, product_quantity):    #  create product_info function

    print("INVENTAIRE :")
    print(f"Nom du produit: {product_name}")
    print(f"Prix: {product_price} kopec")
    print(f"Quantité disponible: {product_quantity}")



product_info(product_name, product_price, product_quantity)         #  call product_info function



# Ajouter des produits en stock.
delivery=int(30)
product_quantity_update = product_quantity + delivery
print(f"Quantité disponible après nouvel arrivage: {product_quantity_update}")


# Demander à l’utilisateur de saisir la quantité de produits qu’il souhaite acheter
wanted=input ("Combien de cocottes voulez-vous acheter ?")

# vérifie que l'utilisateur demande un chiffre entier de cocotte
try:
    wanted = int(wanted)
except ValueError:
    print("Merci d'entrer un nombre entier, nous ne vendons pas de demi cocotte.")

# mettre le stock à jour.
product_quantity = product_quantity_update - wanted
print(f"Quantité disponible après nouvelle commande: {product_quantity}")


# 10 % Inflation, price update
inflation = 1.1                                                     # inflation rate
product_price_update = product_price * inflation                    # new variable for the new price
print(f"Nouveau prix après inflation: {product_price_update}")      # display new price




# Update and display product_info
def product_info_update(product_name, product_price, product_price_update, product_quantity):    #  create product_info_update function

    print("INVENTAIRE MIS A JOUR:")
    print(f"Nom du produit: {product_name}")
    print(f"Prix initial: {product_price} kopec")
    print(f"Quantité disponible: {product_quantity}")
    print(f"Prix après inflation: {product_price_update} kopec")



product_info_update(product_name, product_price, product_price_update, product_quantity)         #  call product_info_update function