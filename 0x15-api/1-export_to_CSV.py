#!/usr/bin/python3
"""
    This script gather data from a REST API and create a CSV file
"""


import csv
import requests
import sys


if __name__ == "__main__":

    user_id = int(sys.argv[1])
    EMPLOYEE_NAME = ""
    TOTAL_NUMBER_OF_TASKS = 0
    row_data = []
    all_data = []

    response_users = requests.get("https://jsonplaceholder.typicode.com/users")
    response_todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    json_users = response_users.json()
    json_todos = response_todos.json()

    for user in json_users:
        if user.get("id") == user_id:
            EMPLOYEE_NAME = user.get("username")

    for task in json_todos:
        if task.get("userId") == user_id:
            USER_ID = f'{user_id}'
            USERNAME = f'{EMPLOYEE_NAME}'
            TASK_COMPLETED_STATUS = f'{task.get("completed")}'
            TASK_TITLE = f'{task.get("title")}'
            row_data = [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE]
            all_data.append(row_data)

    with open(f'{user_id}.csv', mode='w', newline="") as file:
        csv_writer = csv.writer(file, quoting=csv.
                                QUOTE_ALL, lineterminator='\n')

        for row in all_data:
            csv_writer.writerow(row)
