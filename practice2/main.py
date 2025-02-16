# 3 varijable "name", "last_name" i "age" i postavite neke vrijednosti

name = "Obrad"
last_name = "Djuric"
age = 25

# moje
print("Ja se zovem " + name + " prezivam se " + last_name + " i imam " + age.__str__() + " godina")
# tomino :D
print("Ja se zovem " + name + " prezivam se " + last_name + " i imam " + str(age) + " godina")

print(f"Ja se zovem {name} prezivam se {last_name} i imam {str(age)} godina")   #novi python nacin

price = 2000
tax = 0.22
product_tax = price * tax

full_name = name +" "+ last_name
print(product_tax, full_name)

