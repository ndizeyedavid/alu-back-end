#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file."""

import json
import requests
import sys

def main():
    """Fetch employee todos and write them to a JSON file."""
    employee_id = int(sys.argv[1])

    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id}
    )

    user = user_response.json()
    todos = todos_response.json()

    data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username"),
            }
            for task in todos
        ]
    }

    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()
