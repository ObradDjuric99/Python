# napisati petlju koja ispisuje brojeve od 0 do 100

# 5 /2 = 2.5 = 2, 0.5    dvije cjeline i 2x 0.5 dakle jedna cjelina
# 9 /2 2x4.5 = 2x4 , 1 cjelina ostaje

# 444 / 2 = 2x 222
# 411 / 2 = 205x2 (410), 1 cjelina

# ako je ostakat nula, to znaci da je broj djeljiv sa 2, paran
# ako je ostatak 1, to znaci da je broj neparan


# imamo break za zaustavljanje petlje
# continue za preskakanje nekog elementa

# preskoci broj 10
# a kod treba da stane kod broja 44

numbers = range(100)

for number in numbers:
    if number == 10:
        continue
    if number == 44:
        break
    if number % 2 == 0:
        print(f"Broj je paran {number}")

# for number in numbers:   # ovu cu petlju ostaviti sebi jer je dobar primjer za nesto sto ce mi trebati sutra
#     if number % 2 ==0:    # okej shvatio sam ovo samo ostavljam ovde komentar da objasnim sebi kad budem rovio u buducnosti
#         print(f"Broj je paran {number}")  # dakle kad izvucemo procenat keya od nekog number niza dobijamo 0 i 1, 0 se moze dijelit a jedinica je neparna

#continue smo koristili kada lista korisnika koji ima aktivnu subskripciju
# mi smo koristili continue kako ne bi ispisali sve korisnike koji nemaju clanarinu duze od 3 mjeseca

# break bi koristili kada bi imali neke skripte koje bi se pokretale ->
# if test skripte nije prosao onda bi dosao break




