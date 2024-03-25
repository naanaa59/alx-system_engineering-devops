#!/usr/bin/python3
"""
    This script gather data from a REST API and create a CSV file
"""


import csv
import json
import requests
import sys


if __name__ == "__main__":

    EMPLOYEE_NAME = ""
    tasks_list = []
    json_exp_user = {}
    json_exp_all_users = {}

    response_users = requests.get("https://jsonplaceholder.typicode.com/users")
    response_todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    json_users = response_users.json()
    json_todos = response_todos.json()

    for id in range(1, 11):
        for user in json_users:

            if user.get("id") == id:
                EMPLOYEE_NAME = user.get("username")

            for task in json_todos:
                if task.get("userId") == id:
                    tasks_dict = {}

                    USER_ID = f'{id}'

                    USERNAME = f'{EMPLOYEE_NAME}'
                    tasks_dict["username"] = USERNAME

                    TASK_TITLE = f'{task.get("title")}'
                    tasks_dict["task"] = TASK_TITLE

                    TASK_COMPLETED_STATUS = f'{task.get("completed")}'
                    tasks_dict["completed"] = task.get("completed")

                    tasks_list.append(tasks_dict)
                    json_exp_user[f"{USER_ID}"] = tasks_list
    json_exp_all_users.update(json_exp_user)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(json_exp_all_users, json_file)
