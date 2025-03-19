import json
import sys
from datetime import datetime
from helpers.methods import write_logs

#definisati maksimalan budzet , ako ima veci od maksimalnog
# ili manji od 0 ispisati gresku

user_data = {}
max_allowed_budget = 100000

current_date = datetime.today().strftime('%Y-%m-%d')

with open("data/users.json", "r") as file:
    user_data = json.load(file)
    user_id = user_data["id"]
    user_budget = user_data["budget"] + user_data["credit"]

budget_gap = max_allowed_budget - user_budget

if user_budget >= max_allowed_budget or user_budget <= 0:
    print("User budget is not valid, you cannot have more than maximum allowed ammount")
    sys.exit()
else:
    print(f"Your current budget is {user_budget}, and you can have ${budget_gap} more out of maximum")

expense = 0

while expense  <= 0 or expense > user_budget:
    expense = int(input("Molimo unesite iznos troska"))

budget_left = user_budget - expense

data_log = f"\nAmmount:{expense}, user:{user_id}, dateTime:{current_date}, Budget:{user_budget},budget_left:{budget_left}"


write_logs("logs/expense_log.txt", data_log)

#napraviti tekstualni file koji se zove expense_log.txt

# upisati svaki trosak u sledecem formatu
# "Ammount": cifra_expense, user : 1 , dateTime: date neki, Budget: trenutno budget, budget_gap: budget_gap