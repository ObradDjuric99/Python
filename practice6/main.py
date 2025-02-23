#lista studenata
# svaki student ce imati name: "Obrad"
# skor od 0 do 100
# active true ili false

students = [
    {
        "name": "Obrad",
        "score": 90,
        "active": False
    },
    {
        "name": "Ognjen",
        "score": 70,
        "active": True
    },
    {
        "name": "Stefan",
        "score": 50,
        "active": False
    },
    {
        "name": "Toma",
        "score": 30,
        "active": True
    },
    {
        "name": "Milan",
        "score": 18,
        "active": False
    },
]
# petlja koja ispisuje aktivne studente
# ako je skor aktivnog studenta od 80-100 onda upisujemo -> "grade" : "A"
#od 60-80 onda upisujemo -> "grade" : "B"
#od 40-60 onda upisujemo -> "grade" : "C"
#od 20-60 onda upisujemo -> "grade" : "D"
# od <20 onda upisujemo -> "grade" : "F"

active_students = []

for student in students:
    if student["active"]:
        active_students.append(student)
        for active in active_students:
            if 80 < active["score"] < 100:
                active["grade"] = "A"
            if 60 < active["score"] < 80:
                active["grade"] = "B"
            if 40 < active["score"] < 60:
                active["grade"] = "C"
            if 20 < active["score"] < 40:
                active["grade"] = "D"
            else: active["grade"] = "F"
    else:
        print("Student " + student["name"] + " is not active")
print(active_students)

# tolko vec radim nikad mi ove petlje nisu isle, dobro mi je doso ovaj python haha
# inace nisam znao da treba ispisati sve studente pa sam ovako ubacivo samo aktivne u active_students

# e sad ti si me zajebo sa ovom metodom
for student in students:
    if not student["active"]:
        continue

    if student["score"] >= 80:
        student["grade"] = "A"
    if 60 < student["score"] < 80:
        student["grade"] = "B"
    if 40 < student["score"] < 60:
        student["grade"] = "C"
    if 20 < student["score"] < 40:
        student["grade"] = "D"
    if student["score"] < 20:
        student["grade"] = "F"
    print(student)



