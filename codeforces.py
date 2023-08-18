import requests
import time
import datetime

base_url = "https://codeforces.com/api/"

# Current ratings for a list of users.
def curr_ratings(users: str):
    users_string = ""
    for user in users:
        users_string += user + ";"

    response = requests.get(base_url + "user.info?handles=" + users_string)
    json_res = response.json()

    users_res = []
    for user in json_res["result"]:
        users_res.append({
            "handle": user["handle"],
            "rating": user["rating"]
        })
    
    users_res.sort(key=lambda x: x["rating"], reverse=True)

    return users_res

def main():
    #users = ["alexia_martinez","Andros_"]
    #res = curr_ratings(users)
    #for user in res:
    #    print(user["handle"], user["rating"])

    unix_timestamp = 1679787600

    timestamp_datetime = datetime.datetime.utcfromtimestamp(unix_timestamp)

    formatted_date = timestamp_datetime.strftime('%Y-%m-%d %H:%M:%S')

    print(formatted_date)


main()