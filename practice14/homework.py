import re

# da li je email

email = "toma@gmail.com"
# da li postoje slova (\w)
# \w provjeravamo da li postoje slova
# \.- provjeravamo . ili crticu

# da li sadrzi @
# \. da li postoji "." tacka
# \w

email_pattern = r"^[\w\.-]+@[\w\.-]+\."

if re.match(email_pattern,email):
    print("mecuje se")