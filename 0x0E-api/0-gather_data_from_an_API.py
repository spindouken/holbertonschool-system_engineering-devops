#!/usr/bin/python3
"""This script gathers data from the JSONPlaceholder API to track the progress
of an employee's tasks"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    # Make a GET request to retrieve the employee data
    employee_data_request = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    )
    employee_data = employee_data_request.json()

    # Make a GET request to retrieve the employee's tasks
    employee_tasks_request = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )
    employee_tasks = employee_tasks_request.json()

    # Count the number of completed tasks
    completed_tasks = [task for task in employee_tasks if task['completed']]

    # Display the results
    employee_name = employee_data['name']
    num_completed_tasks = len(completed_tasks)
    num_total_tasks = len(employee_tasks)

    print(
        f"Employee {employee_name} has completed {num_completed_tasks} out of "
        f"{num_total_tasks} tasks:"
    )

    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == '__main__':
    # Check if the user has provided an employee ID
    if len(sys.argv) != 2:
        print("Usage: python3 employee_task_tracker.py <employee_id>")
        sys.exit(1)

    # Convert the employee ID to an integer
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Call the function to track the employee's task progress
    get_employee_todo_progress(employee_id)
