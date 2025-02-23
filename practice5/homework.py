# pitati korisnika da unese ime proizvoda
# kada unese ime proizvoda dodai proizvod u kasu
#korisnik mora unjeti 3 proizvoda ukupno

# moje
item_list = []

while len(item_list) < 3:
    product_name = input("Unesite proizvod u kasu: ")
    item_list.append(product_name)
print(item_list)




# tomino

register = list()   # ovo si me zezno nisam znao da se lista moze ovako pravit :D

while len(register) < 3:
    item = input("Unesite ime proizvoda: ")
    register.append(item)
    print(register)
