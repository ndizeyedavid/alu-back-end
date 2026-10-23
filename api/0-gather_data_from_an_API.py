#!/usr/bin/python3
import sys
import requests

#if len(sys.argv) < 1:
#    print("Please provide atleast 1 argument")

employeeId = int(sys.argv[1])

response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employeeId}")

if response.status_code == 200:
    userData = response.json()
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employeeId}")

    if todos_response.status_code == 200:
        todos = todos_response.json()
        completedTasks = []
        for task in todos:
            if task["completed"]: completedTasks.append(task)
                
        print(f"Employee {userData['name']} is done with tasks({len(completedTasks)}/{len(todos)}):")

        for completedTask in completedTasks:
            print(f"\t{completedTask['title']}")
