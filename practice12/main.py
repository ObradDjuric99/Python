import platform
from platform import python_version_tuple

version = python_version_tuple()

version_first_of = int(version[0])

if version_first_of != 3:
    print("Ne valja ti ovo")
else:
    print(f"Tvoja verzija je: {version_first_of} i odlicna je")

