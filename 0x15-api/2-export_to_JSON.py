#!/usr/bin/python3
"""
    This script gather data from a REST API and create a CSV file
"""


import csv
import json
import requests
import sys


if __name__ == "__main__":

    user_id = int(sys.argv[1])
    EMPLOYEE_NAME = ""
    tasks_list = []
    json_exp = {}

    response_users = requests.get("https://jsonplaceholder.typicode.com/users")
    response_todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    json_users = response_users.json()
    json_todos = response_todos.json()

    for user in json_users:
        if user.get("id") == user_id:
            EMPLOYEE_NAME = user.get("username")

    for task in json_todos:
        if task.get("userId") == user_id:
            tasks_dict = {}

            USER_ID = f'{user_id}'

            TASK_TITLE = f'{task.get("title")}'
            tasks_dict["task"] = TASK_TITLE

            TASK_COMPLETED_STATUS = f'{task.get("completed")}'
            tasks_dict["completed"] = task.get("completed")

            USERNAME = f'{EMPLOYEE_NAME}'
            tasks_dict["username"] = USERNAME

            tasks_list.append(tasks_dict)

            json_exp[f"{USER_ID}"] = tasks_list

    with open(f"{USER_ID}.json", "w") as json_file:
        json.dump(json_exp, json_file)
