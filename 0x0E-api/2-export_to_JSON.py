#!/usr/bin/python3
"""exports an employee's tasks to a JSON file"""
import sys
import requests
import json


def export_employee_tasks_to_json(employee_id):
    # Retrieve employee data from the JSONPlaceholder API
    employee_data_request = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    )
    employee_data = employee_data_request.json()

    # Retrieve employee tasks from the JSONPlaceholder API
    employee_tasks_request = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )
    employee_tasks = employee_tasks_request.json()

    # Prepare data for JSON export
    tasks = []
    for task in employee_tasks:
        tasks.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_data["username"]
        })
    json_data = {str(employee_id): tasks}

    # Export JSON data to a file named after the employee ID
    with open(f'{employee_id}.json', 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == '__main__':
    # Check if the user has provided an employee ID
    if len(sys.argv) != 2:
        print("Usage: python3 employee_task_exporter.py <employee_id>")
        sys.exit(1)

    # Convert the employee ID to an integer
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Call the function to export the employee's tasks to a JSON file
    export_employee_tasks_to_json(employee_id)
