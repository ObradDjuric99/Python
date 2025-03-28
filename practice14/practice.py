import re


name = "Tomislav Nikolic"

# veliko pa malo slovo
pattern = r"[A-Z][a-z]+ [A-Z][a-z]+$"

if re.match(pattern, name):
    print("Ispisuje")

