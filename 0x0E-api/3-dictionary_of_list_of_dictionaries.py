#!/usr/bin/python3
import json
import requests


def get_all_employees_tasks():
    # Get all employee data
    all_employee_data = requests.get('https://jsonplaceholder.typicode.com/users')
    all_employee_data = all_employee_data.json()

    # Prepare JSON data
    json_data = {}
    for employee_data in all_employee_data:
        employee_id = employee_data['id']
        
        # Get employee TODOs
        employee_todos = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
        employee_todos = employee_todos.json()

        tasks = []
        for task in employee_todos:
            tasks.append(
                {
                    "username": employee_data["username"],
                    "task": task["title"],
                    "completed": task["completed"]
                }
            )

        json_data[str(employee_id)] = tasks

    return json_data

def export_all_employee_tasks_to_json(json_data):
    # Export JSON data
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(json_data, json_file)

if __name__ == '__main__':
    json_data = get_all_employees_tasks()
    export_all_employee_tasks_to_json(json_data)
