import datetime
import time
import pandas as pd
import openpyxl
from codeforces import Codeforces as cf

def get_report():
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

def detailed_view():
    dataframe = openpyxl.load_workbook("users.xlsx")

    dataframe1 = dataframe.active

    matrix = []

    intervals = [ 
        {
            "start": datetime.datetime(2023,8,20),
            "end":  datetime.datetime(2023,8,27)
        },
        {
            "start": datetime.datetime(2023,8,27),
            "end":  datetime.datetime(2023,9,3)
        },
    ]

    #cf.solved_problems_intervals("alexia_martinez", intervals)
    #return

    for row in range(2,dataframe1.max_row + 1):
        
        name = dataframe1["{}{}".format("B",row)].value
        last_names = dataframe1["{}{}".format("C",row)].value
        cf_user = dataframe1["{}{}".format("D",row)].value

        rating = cf.get_user_rating(cf_user)

        row = [cf_user, name, last_names, rating]

        solved_problems = cf.solved_problems_intervals(cf_user, intervals)
        
        if solved_problems == -1:
            continue

        for i in range(len(solved_problems)):
            row.append(solved_problems[i])

        matrix.append(row)

        time.sleep(3)
    
    columns = ["Usuario", "Nombre", "Apellidos", "Rating"]
    for i in range(len(intervals)):
        columns.append(f"Semana {i}")
    df = pd.DataFrame(matrix, columns=columns)

    df.to_excel("Reporte_Agosto.xlsx", sheet_name="New Sheet")

    print("Done!")

detailed_view()