from numpy.ma.core import append, repeat

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
    }
}

deletion = "Obrisi"
add = "Dodaj"

product = None

key = ["ammount:", "price:"]


while product not in products:
    user_question = input("Sta zelite da odradite?: ").lower()
    if user_question == deletion.lower():
        product = input("Unesite ime proizvoda koji zelite da obrisete: ").lower()
        while product not in products:
            product = input("Unesite ime proizvoda koji zelite da obrisete: ").lower()
        del products[product]
        continue
    elif user_question == add.lower():
        name_product_question = input("Unesite ime proizvoda: ").lower()
        while name_product_question in products or name_product_question == "" or len(name_product_question) < 3:
            name_product_question = input("Proizvod vec postoji unesite drugi: ").lower()
        price_product_question = None
        ammount_product_question = None
        while price_product_question is None or price_product_question <= 0:
            price_product_question = int(input("Unesite cijenu proizvoda: "))
        while ammount_product_question is None or ammount_product_question <= 0:
            ammount_product_question = int(input("Unesite kolicinu proizvoda: "))
        products[name_product_question] = {key[1]:price_product_question, key[0]: ammount_product_question}
        break


print(products)

# ja sam ubacio ovde kada se delete odradi da opet pita sta hocemo da uradimo nisam ubacio u dodavanje da ne bi beskonacno ovo vrtili :D








