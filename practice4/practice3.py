

# korisnik treba da unece cijenu korpe
# ako je cijena preko 1000 ispisati koliko popust su ostvarili (10%) - 1000, "Ostavrili ste 10% popusta sto iznosi 100 eura"
# ako je cijena ispod 1000 ispisati "Vasa korpa iznosi 1000"


max_cart_price = 1000
cart_price = int(input("Unesite cijenu korpe"))
if cart_price > max_cart_price:
    tax_amount = cart_price*0.10
    print(f"Ostvarili ste 10% popusta sto ukupno iznosi {tax_amount}e")
else:
    print("Vasa korpa iznosi 1000")