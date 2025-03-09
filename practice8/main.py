

products = {
    "bread": {
        "price": 100,
        "ammount": 50
    },
    "beer": {
        "price": 150,
        "ammount": 220
    },
    "newspappers": {
        "price": 120,
        "ammount": 80
    },
    "test": {
        "price": 800,
        "ammount": 80
    }
}

# izlistaj

# opcija: stop

# napraviti novu opciju koja ce se zvati isorijat -> sve sto se desilo
# prikazi najskuplji proizvod

options = ["dodaj", "obrisi", "izlistaj", "stop", "istorijat", "obrisi sve", "najskuplji"]

program_history = []
highest_price = 0
highest_product = None
option = None
while option not in options:
    option = input(f"Sta zelite da odradite? {", ".join(options)}:\n").lower()

    if option == "obrisi":
        product = None
        while product not in products:
            product = input("UNesite ime proizvoda za brisanje:\n").lower()
        del products[product]
        msg = f"Obrisali ste {product} iz produkata"
        print(msg)
        program_history.append(msg)
        option = None

    elif option == "dodaj":
        product = None
        while product in products or product is None:
            product = input("Unesite ime proizvoda koji ne postoji:\n")
        product_price = None
        while product_price is None or product_price <= 0:
            product_price = int(input("Unesite cijenu proizvoda:\n"))
        product_ammount = None
        while product_ammount is None or product_ammount <= 0:
            product_ammount = int(input("Unesite kolicinu za proizvod:\n"))
        products[product] = {
            "price": product_price,
            "ammount": product_ammount
        }
        msg = f"Dodali ste {product} u produkte"
        print(msg)
        program_history.append(msg)
        option = None

    elif option == "izlistaj":
        print(products)
        program_history.append("Izlistani produkti")
        option = None

    elif option == "istorijat":
        print(program_history)

    elif option == "obrisi sve":
        products = {}
        option = None
    elif option == "najskuplji":
        for product in products:
            if products[product]["price"] > highest_price:
                highest_price = products[product]["price"]
                highest_product = product
        print(f"Najskuplji proizvod je {highest_product} sa cijenom od {highest_price}")



