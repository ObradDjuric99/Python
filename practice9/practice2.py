def calculate_delivery(city):
    if city == "Beograd" or city == "Zagreb":
        return 500
    elif city == "Subotica":
        return 100
    elif city == "Novi Sad":
        return 400                                # ovde sam odradio malo jednostavnije :D
    else:
        return 0


city_delivery = calculate_delivery("Beograd")
product_price = 200
total_cart_price = city_delivery + product_price
if city_delivery > 0:
    print(f"Porizvod iznosi {product_price} a Dostava je {city_delivery} dinarosa, ukupna vrijednost u korpi je {total_cart_price}")
else:
    print("Nema grada")