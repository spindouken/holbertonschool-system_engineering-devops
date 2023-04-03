#!/usr/bin/python3
"""exports an employee's tasks to a CSV file"""
import sys
import requests
import csv


def export_employee_tasks_to_csv(employee_id):
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

    # Prepare data for CSV export
    csv_data = []
    for task in employee_tasks:
        csv_data.append([
            employee_id,
            employee_data['username'],
            task['completed'],
            task['title']
        ])

    # Export CSV data to a file named after the employee ID
    with open(f'{employee_id}.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(csv_data)


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

    # Call the function to export the employee's tasks to a CSV file
    export_employee_tasks_to_csv(employee_id)
