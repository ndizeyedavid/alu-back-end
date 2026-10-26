#!/usr/bin/python3
"""Export all employees' TODO lists to a single JSON file."""

import json

import requests


def main():
    """Fetch all users and todos, then write them to a JSON file."""
    users_response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )
    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    )

    users = users_response.json()
    todos = todos_response.json()

    data = {}
    for user in users:
        user_id = str(user.get("id"))
        user_todos = [
            todo for todo in todos if todo.get("userId") == user.get("id")
        ]
        data[user_id] = [
            {
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed"),
            }
            for todo in user_todos
        ]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()
