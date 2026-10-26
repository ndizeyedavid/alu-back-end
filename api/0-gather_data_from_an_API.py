#!/usr/bin/python3
"""Gather TODO list progress for a single employee."""

import requests

import sys


def main():
    """ Display an employee's completed TODO tasks."""
    employee_id = int(sys.argv[1])

    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )

    if response.status_code == 200:
        user_data = response.json()
        todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos",
            params={"userId": employee_id}
        )

        if todos_response.status_code == 200:
            todos = todos_response.json()
            completed_tasks = [
                task for task in todos if task.get("completed")
            ]

            print(
                "Employee {} is done with tasks({}/{}):".format(
                    user_data.get("name"),
                    len(completed_tasks),
                    len(todos)
                )
            )

            for task in completed_tasks:
                print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
