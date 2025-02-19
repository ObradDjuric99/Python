products = ["iphone 14", "iphone 15", "samsung s23"]

# prije hinta

if products.__contains__( "iphone4"):
    print("ima")
else:
    print("nema")

# nakon hinta za in operator

phone_name = input("Insert name of phone: ")


if phone_name in products:
    print("ima")
else:
    print("nema")