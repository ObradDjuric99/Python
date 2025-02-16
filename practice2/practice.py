cars = ["Mercedes", "BMW", "Yugo"]

print(cars)

# umjesto bmw => audi

cars[1] = "Audi"

print(cars)

#dodati jos jedan auto

cars.append("Skoda")

print(cars)

#sortitati auto po a-z


cars.sort()
print(cars)

#trenutno na stanju imamo broj automobila

total_cars = len(cars)

# moje
print("trenutno na stanju imamo " + str(total_cars) + " automobila")

# tomino
print(f"trenutno na stanju imamo  {len(cars)} automobila")
