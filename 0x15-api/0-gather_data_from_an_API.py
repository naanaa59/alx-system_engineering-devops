#!/usr/bin/python3
"""
    This script gather data from a REST API
"""

import requests
import sys


if __name__ == "__main__":

    EMPLOYEE_NAME = ""
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    titles_of_done_tasks = []
    user_id = int(sys.argv[1])

    response_users = requests.get("https://jsonplaceholder.typicode.com/users")
    response_todo = requests.get("https://jsonplaceholder.typicode.com/todos")

    json_users = response_users.json()
    json_todo = response_todo.json()

    for user in json_users:
        if user["id"] == user_id:
            EMPLOYEE_NAME = user["name"]

    for task in json_todo:
        if task["userId"] == user_id:
            TOTAL_NUMBER_OF_TASKS += 1

            if task["completed"] is True:
                NUMBER_OF_DONE_TASKS += 1
                titles_of_done_tasks.append(task["title"])

    print(f"Employee {EMPLOYEE_NAME} is done with tasks\
({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    for title in titles_of_done_tasks:
        print(f"\t {title}")
