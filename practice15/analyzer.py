import re
from helpers.log_writer import write_logs

error_file = "logs/errors.log"
success_file = "logs/success.log"

error_pattern = r"Error \d{3}"
success_pattern = r"Success \d{3}"

with open('logs/http.log', 'r') as file:
    lines = file.readlines()

for line in lines:
    if re.search(error_pattern, line):
        write_logs(error_file, line)
    elif re.search(success_pattern,line):
         write_logs(success_file, line)

