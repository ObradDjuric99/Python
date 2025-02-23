# pitaj korisnika koliko godina ima
# ako nije unjeo godine pitaj opet

#ako korisnik unese godine manje od 18 i dalje ga pitamo

age = input("Unesite svoje godine")

while not age.isdigit() or int(age) < 18:
        age = input("Unesite svoje godine")
