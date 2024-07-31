#!/usr/bin/python3
"""
    Python script returning TODO list progress 
    information for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    user = requests.get(user_url).json()
    todo = requests.get(todo_url).json()

    nb_completed = 0
    nb_total = 0
    tasks_completed = []

    for task in todo:
        nb_total += 1
        if task.get("completed") is True:
            nb_completed += 1
            tasks_completed.append(task.get("title"))

    statement = "Employee {} is done with tasks({}/{}):"
    print(statement.format(user.get("name"), nb_completed, nb_total))
    for task in tasks_completed:
        print("\t {}".format(task))
