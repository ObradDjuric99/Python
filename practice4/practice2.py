# napisite program koji trazi od korisnika da unese ime proizvoda, a zatim ispisuje cijenu tog proizvoda
# ako proizvod ne postoji, ispisite poruku "Proizvod nije pronadjen"
from PyQt5.QtCore import lowercasebase

products = {"iPhone 14": 199, "iphone 15": 1200, "samsuings23": 1200}

product_name = input("Upisite ime proizvoda: ").lower()

if product_name in products:
    print(f"Cijena ovog proizovda je: {products[product_name]}")
else:
    print(f"Produk ne postoji: test")