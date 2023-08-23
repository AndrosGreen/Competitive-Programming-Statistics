import requests
import time
import datetime

class Codeforces:

    base_url:str = "https://codeforces.com/api/"

    # Init
    def __init__(self) -> None:
        pass

    # Current ratings for a list of users.
    def curr_ratings(self, users: str):
        users_string = ""
        for user in users:
            users_string += user + ";"

        response = requests.get(self.base_url + "user.info?handles=" + users_string)
        json_res = response.json()

        users_res = []
        for user in json_res["result"]:
            users_res.append({
                "handle": user["handle"],
                "rating": user["rating"]
            })
        
        users_res.sort(key=lambda x: x["rating"], reverse=True)

        return users_res

    # Amount of solved problems for a single user.
    # A time interval can be provided.
    @classmethod
    def solved_problems(self, user, start_date = None):

        response = requests.get(self.base_url + "user.status?handle=" + user)
        if response.status_code != 200:
            print("Time Out")
            return -1
        
        response = response.json()

        result = response["result"]

        count = 0
        for submmision in result:
            if submmision["verdict"] == "OK":
                unix_timestamp = submmision["creationTimeSeconds"]
                timestamp_datetime = datetime.datetime.utcfromtimestamp(unix_timestamp)

                if start_date == None:
                    count += 1
                    continue
                if timestamp_datetime >= start_date:
                    count += 1

        return count