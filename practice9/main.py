from Xlib.Xcursorfont import clock

# calculate_delivery -> izracunaj dostavu
# Beograd - 500, Subotica - 1200, Novi Sad - 700, Zagreb - 900
# ako grad ne postoji ispisati "grad ne postoji"

cities = {
    "beograd": 500,
    "subotica": 1200,
    "novi sad": 700,
    "zagreb": 900
}


city_name = input("Unesite ime grada: ").lower()

def calculate_delivery(city):
    while city_name not in cities:
        print("Grad ne postoji")
        break
    for item, value in cities.items():                       # mozda sam pretjero malo ovu prvu vjezbu nisam znao da bi samo pisali ifove
        if item == city:
            print(f"Dostava u {city} iznosi {value} Dinarosa")


calculate_delivery(city_name)



def calculate(number1,number2):
    return number1 + number2


result = calculate(8,15)
print(result)