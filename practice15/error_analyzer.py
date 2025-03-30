import re


pattern = r"\d{2}:\d{2}:\d{2}"

with open('logs/errors.log') as error_log:
    for error in error_log.readlines():
        match = re.search(pattern, error)
        print(match)

