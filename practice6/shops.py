from collections import Counter

from Xlib.Xcursorfont import clock

shops = {
    "maxi": {
        "bread": 300,
        "newspaper": 50
    },
    "Idea":{
        "bread": 4532,
        "newspaper": 23

    },
    "shopPro": {
        "bread": 100,
        "newspaper": 23

    },
    "FreeShop": {
        "newspaper": 50
    }
}

# napisati petlju koja ce ispisati sve cijene hljeba

# # moje
# for item in shops:
#     if shops[item]["bread"] not in shops.items():
#         continue
#     else:
#         print(shops[item]["bread"])
#
#
# # tomino
#
# for shop_name, items in shops.items():
#     if items["bread"] not in shops.items():
#         continue
#     else:
#         print(items["bread"])

# uzeti srednju cijenu hljeba
# total / kolicinom

# moje

bread_count = []
for shop_name, items in shops.items():
    if not "bread" in items:
        continue                                            # ova mi je bila malo laksa za izmanipulisati jer je sve bilo u jednom arrayu
    bread_count.append(items["bread"])
    c = sum([len(bread_count)])
result = sum(bread_count) / c
# print(f"Average bread price is {result} dinaros")


# tomina logika koju sam prepravio da racuna dictionary u kojoj key nema bread
total_bread_price = 0
shops_with_bread = []
for shop_name, items in shops.items():
    if not "bread" in items:                                # ovu tvoju mi je bilo malo teze prepraviti pa sam dodao ovu listu da smjestim length od shopova
        continue
    total_bread_price += items["bread"]
    shops_with_bread.append(items["bread"])
average_bread_price = total_bread_price / len(shops_with_bread)
# print(average_bread_price)

# tomina prepravka logike da racuna dictionaryu kome nema hljeb

total_bread_price = 0
total_bread_shops = 0
for shop_name, items in shops.items():
    if "bread" in items:                                        # ja sam nekako kroz js naviko da radim sa praznim nizovima pa mi lakse bilo staviti array
        total_bread_price += items["bread"]                        # ali ovako je dosta cistije pa cu se truditi da to primjenjujem u buducnosti
        total_bread_shops += 1
average_bread_price = total_bread_price / total_bread_shops
# print(average_bread_price)


# homework ispisati prodavnicu koja ima najvecu cijenu hljeba
max_bread = 0
shop_with_most_bread = ""
for shop, items in shops.items():
    if "bread" in items and items["bread"] > max_bread:
        max_bread = items["bread"]
        shop_with_most_bread = shop                                         # nisam znao da ako prodjem kroz item i nadjem onaj koji ima najveci "bread" price da mogu izvuc i njegovo ime odma u posebnu listu
if shop_with_most_bread:
    print(f"{shop_with_most_bread} has the highest bread count: {max_bread}")
else:
    print("No shop has bread.")

