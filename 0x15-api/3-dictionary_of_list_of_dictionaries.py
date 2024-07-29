#!/usr/bin/python3
"""Record and export all employees todos in json"""
import json
import requests


def get_user_todos(user_id, username):
    """
    This method fetch all todos from specific user
    Args: user_id (number)
    Return: Json with todos
    """
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    return [
        {
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed"),
        }
        for task in todos
    ]


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as f:
        json.dump(
            {
                u.get("id"): get_user_todos(u.get("id"), u.get("username"))
                for u in users
            },
            f,
        )
