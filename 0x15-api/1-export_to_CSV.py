#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [
            writer.writerow(
                [
                    user_id,
                    user.get("username"),
                    task.get("completed"),
                    task.get("title"),
                ]
            )
            for task in todos
        ]
