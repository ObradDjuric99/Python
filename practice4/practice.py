# pitati korisnika za godine
#ako ima 18 ili vise godina ispisati "punoljetan si"
# ako ima manje ispisati "maloljetan si"

user_age = int(input(f"Koliko imas godina? "))
# ako korisnik ima 12 ili manje godina onda ispisati "Vi ste dijete"
#ako korisnik ima od 13 do 18 godina ispisati "vi ste dinejdzer"
# ako korisnik ima od 18 do 64 godina ispisati "vi ste odrasla osoba"
# ako osoba ima 65 ili vise godina ispisati "vi ste penzioner"


if user_age < 0:
    quit("Greska program se gasi")
elif user_age <= 12:
    print("VI ste dijete")
elif 13 <= user_age < 18:  # mislio sam da se buni jer and operator nema i onda sam guglo naso da ima pa me iznerviralo :D
    print("Vi ste tinejdzer")
elif user_age >= 18 and user_age <= 64:
    print("Vi ste odrasla osoba")
elif user_age >= 65:
    print("Vi ste penzioner")
