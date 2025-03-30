import re
# Quantifiers  -- prepoznavanje vise puta neko slovo ili rijec
# *: Matches 0 or more occurences. ->   a* (ili nula ili vise ponavljanja slova a)
# +: Matches 1 or more occurences.
# ?: Matches 0 or 1 occurence (makes it optional).
# {n}: Matches exactly n occurrence. a{3} -> "aaa"
# {n,}: Matches n or more occurences. a{2,}  "aa", "aaa"
# {n,m}: Matches between n and m occurences. {2,4} "aa", "aaa", "aaaa"


# bonus kodovi su oni koji imaju ispred tri slova i posle tri broja -> QWD123
# \b \b gleda na limitranu rijec od pocetka do kraja rijeci

bonus_codes = "ABC123, bonus455, bonus22, qwd123"

code_pattern = r"\b[A-Za-z]{3}\d{3}\b"

product_codes = re.findall(code_pattern, bonus_codes)

# print(product_codes)


# rijec od 5 slova pracena sa 2 broja
word_codes = "g12, td234, td12, tdg12, tdg123, tdgt12, tdgt123, tdgtd12, tdgtd1234123123, testrdas1323"

word_pattern = r"\b[A-Za-z]{1,5}\d{2,}\b"

search_words = re.findall(word_pattern, word_codes)
print(search_words)