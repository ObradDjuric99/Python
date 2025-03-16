from methods import load_file,saved_file,delete_file, empty_file

products = load_file("data/products.json")
users = load_file("data/user.json")

products.append({
    "name": "test",
    "price": 523,
    "quantity": 412
})

saved_file("data/products.json", products)

print(products)



empty_file("data/products.json")

