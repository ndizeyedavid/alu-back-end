#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file."""

import csv
import requests
import sys


def main():
    """Fetch employee todos and write them to a CSV file."""
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

    with open(f"{employee_id}.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                user.get("username"),
                task.get("completed"),
                task.get("title"),
            ])


if __name__ == "__main__":
    main()
