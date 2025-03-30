# pitati korisnika da unese ime proizvoda
# Kada unese ime proizvoda  dodati proizvod u kasu
# korisnik mora uneti tri proizvoda ukupno

cart = []

while len(cart) < 3:
    product_name = input("Unesite ime proizvoda: ")
    cart.append(product_name)

print(cart)

