# Conditional statement / if-else

name = "Obrad"
# if name Obrad => "pozdrav obrade"
# if name someone else => "pozdrav {someone else}"

if name == "Obrad":
    print("Pozdrav " + name)
else:
    print("Pozdrav neko drugi")

age = 31

if age >= 18:
    print("Punoljetni ste")
else:
    print("Niste punoljetni")