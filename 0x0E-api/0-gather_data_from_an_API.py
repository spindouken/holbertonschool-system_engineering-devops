#!/usr/bin/python3
"""This script gathers data from the JSONPlaceholder API to track the progress
of an employee's tasks"""

import json
import requests
import sys

if __name__ == "__main__":
    """Main function to gather data from the
    JSONPlaceholder API for an employee's tasks.
    ...retrieves data from the API for a specific employee based on the
    user ID provided as a command-line argument.
    ...then extracts the employee's name and the number
    of tasks the employee has completed out of the total number of tasks.
    Finally, it prints the employee's name along with
    the number of completed tasks and their titles.
    """
    num_done, num_tasks = 0, 0
    userId = sys.argv[1]

    # create Response object for specific user and that user's tasks
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
    user_response = requests.get(url)

    url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
        .format(userId)
    todo_response = requests.get(url)

    # create Dictionary objects from response objects
    user_info = json.loads(user_response.text)
    todo_info = json.loads(todo_response.text)

    employee_name = user_info['name']

    for task in todo_info:
        num_tasks += 1
        if task['completed']:
            num_done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_done, num_tasks))

    for task in todo_info:
        if task['completed']:
            print("\t {}".format(task['title']))
