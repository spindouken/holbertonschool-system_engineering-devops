#!/usr/bin/python3
"""exports an employee's tasks to a CSV file"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    """Main function to retrieve a user's tasks from JSONPlaceholder API and
    write them to a CSV file.

    This function retrieves data from the JSONPlaceholder
    API for a specific user's tasks based on the user ID
    provided as a command-line argument...
    ...then creates a list of dictionaries, where each
    dictionary corresponds to a task and contains
    information such as the user ID, username,
    task completion status, and title.
    Finally, it writes the list of dictionaries
    to a CSV file named after the user ID.
    """

    num_done, num_tasks = 0, 0
    user_id = sys.argv[1]

    # create Response object for specific user and that user's tasks
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = requests.get(url)

    url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
        .format(user_id)
    todo_response = requests.get(url)

    # create Dictionary objects from response objects
    user_info = json.loads(user_response.text)
    todo_info = json.loads(todo_response.text)

    task_list = []
    username = user_info['username']

    # create a list of dictionaries for each task
    for task in todo_info:
        task_dict = {}
        task_dict['USER_ID'] = user_id
        task_dict['USERNAME'] = username
        task_dict['TASK_COMPLETED_STATUS'] = task['completed']
        task_dict['TASK_TITLE'] = task['title']
        task_list.append(task_dict)

    # write list of dictionaries to a CSV file
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    with open('./{}.csv'.format(user_id), 'w', encoding='UTF8',
              newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL, quotechar='"')
        writer.writerows(task_list)
