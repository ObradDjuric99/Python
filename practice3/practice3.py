name = "admin"
password = "mojaSifra"

# AKO JE IME admin I AKO JE SIFRA mojaSifra print ("Dobrodosao adminae!")
# ako je ime "toma" i ako je sifra "123456" print ("dobrodosao tomo")
# ako je ime "marija" i ako je sifra "554231" print ("dobrodosla marija")
# else print ("Niste administrator ! pogresna sifra ili ime")


if name == "admin" and password == "mojaSifra":
    print("dobrodosao admine!")
elif name == "toma" and password == "123456":
    print("Dobrodosao Tomo")
elif name == "marija" and password == "554231":
    print("Dobrodosao Tomo")
else: print("Niste administrator ! pogresna sifra ili ime")

