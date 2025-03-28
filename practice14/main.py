import re
from sys import prefix

our_numbers = "12345"  # da li se nalaze samo brojevi ovde

# malo slovo r predstavlja da trazimo dio stringa kao obican tekst
#tekst sadrzi \ (escape character)

# r - je sve sto provjeravam tretiraj kao obican tekst
# ^ - trazimo od pocetka stringa
# \d - trazi samo brojeve od 0 do 9 - matches any numbers from 0 to 9
# + - nastavlja sa trazenjem brojeva
# $ - kraj stringa


#patern za provjeravanje da li su brojevi unutar necega

# pattern = r"^\d+$"
#
#
# if re.match(pattern, our_numbers):
#     print("Mecuje se")
# else:
#     print("Ne mecuje se")

# regex koji ce provjeravati da li imamo samo slova unutar stringa

# sentence = "i love python"
#
# pattern = r"^[a-zA-Z ]+$"
#
# if re.match(pattern, sentence):
#     print("Mecuje se")
# else:
#     print("Ne mecuje se")

#
# sentence = "Today will rain"
#
# pattern = r"^[A-Z]"
#
# if re.match(pattern, sentence):
#     print("Mecuje se")
# else:
#     print("Ne mecuje se")


# 381 = srbija, 382 = bosnia , 385 = croatia, 389 = montenegro

# country_codes = {
#     "serbia":{
#         "phone": "381"
#     },
#     "bosnia":{
#         "phone": "382"
#     },
#     "croatia":{
#         "phone": "385"
#     },
#    "montenegro": {
#         "phone": "389"
#     }
# }
#
# phoneNumber = "389555333"
#
# pattern = r"^38(1|2|5|9)"
#
# phone_match = re.match(pattern, phoneNumber)
# .group(1) vadi prvi prefiks koji je nasao recimo ako je 38 i pocinje sa 5 nacice 385

# for country, items in country_codes.items():
#     if phone_match:
#         prefix = "38"+phone_match.group(1)
#         if prefix == items["phone"]:
#             print(f"Starting number is {prefix} and country is {country}")



country_codes = {
    "381": "serbia",
    "382": "montenegro",
    "385": "bosnia",
    "389": "croatia"
}

phoneNumber = "389555333"

pattern = r"^38(1|2|5|9)"

phone_match = re.match(pattern, phoneNumber)

if phone_match:
    prefix = "38"+phone_match.group(1)
    country = country_codes[prefix]
    print(f"Prefix number is {prefix} and country is {country}")