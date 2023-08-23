import datetime
import time
import pandas as pd
from codeforces import Codeforces as cf

cf_usernames_file_path = "users.txt"

usernames = []
with open(cf_usernames_file_path, 'r') as file:
    for line in file:
        username = line.strip()
        usernames.append(username)

# Start date
start_date = datetime.datetime(2023,8,20,0,0,0)

matrix = []

for user in usernames:
    problems_solved = cf.solved_problems(user,start_date)
    new_user = [user, problems_solved]
    print(user, problems_solved)
    matrix.append(new_user)
    time.sleep(1)

df = pd.DataFrame(matrix, columns=["user", "problems solved"])

df.to_excel("pandas_to_excel.xlsx", sheet_name="New Sheet")
print("Done!")