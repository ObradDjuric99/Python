import pymysql

connection = pymysql.connect(
    host = "localhost",
    user="root",
    password="brad99",
    database="python17"
)


if connection.open:
    print("connected")
else:
    print("error")


def create_user(con, name, password, years):
    cursor = con.cursor()
    query = "INSERT INTO users (username, password, age) VALUES(%s, %s, %s)"
    cursor.execute(query, (name, password, years))
    connection.commit()
    cursor.close()  # zatvaramo konekciju za ovaj api


create_user(connection, "IME test", "password", 5)