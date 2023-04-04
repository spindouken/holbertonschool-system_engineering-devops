#!/usr/bin/python3
"""exports an employee's tasks to a JSON file"""
import json
import requests
import sys


if __name__ == "__main__":
    """Main function to retrieve and export a
    user's tasks from JSONPlaceholder API.

    Retrieves data from the JSONPlaceholder API
    for a specific user's tasks based on the user
    ID provided as a command-line argument...
    ...then creates a dictionary where the keys
    correspond to the user ID and the values
    correspond to a list of dictionaries,
    where each dictionary corresponds to a task
    and contains information such as the task title,
    completion status, and username.
    Finally, it writes the dictionary to a JSON file
    named after the user ID.
    """

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

    tasks = {}

    tasks_list = []

    # create a dictionary for each task and add it to the list of tasks
    for task in todo_info:
        task_dict = {}
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']
        task_dict['username'] = user_info['username']
        tasks_list.append(task_dict)

    # add list of tasks to dictionary
    tasks[user_id] = tasks_list

    # write dictionary to a JSON file
    with open('./{}.json'.format(user_id), 'w', encoding='UTF8',
              newline='') as f:
        f.write(json.dumps(tasks))
