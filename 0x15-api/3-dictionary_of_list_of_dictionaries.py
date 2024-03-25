#!/usr/bin/python3
"""
    This script gather data from a REST API and create a CSV file
"""


import csv
import json
import requests
import sys


if __name__ == "__main__":

    json_exp_user = {}
    json_exp_all_users = {}

    response_users = requests.get("https://jsonplaceholder.typicode.com/users")
    response_todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    json_users = response_users.json()
    json_todos = response_todos.json()

    for id in range(1, 11):
        tasks_list = []
        employee_name = ""

        for user in json_users:
            if user.get("id") == id:
                employee_name = user.get("username")
                break

        for task in json_todos:
            if task.get("userId") == id:
                tasks_dict = {
                        "username": employee_name,
                        "task": task.get("title"),
                        "completed": task.get("completed")
                }
                tasks_list.append(tasks_dict)
        json_exp_all_users[str(id)] = tasks_list

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(json_exp_all_users, json_file)
