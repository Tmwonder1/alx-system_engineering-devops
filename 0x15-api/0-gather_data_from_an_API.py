#!/usr/bin/python3
"""
This script gathers data from a REST API for a given employee ID
and returns information about their TODO list progress.
"""

import requests
import sys

def get_employee_data(employee_id):
    """
    Gets the employee data from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: A dictionary with employee name and their tasks.
    """
    try:
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_response.raise_for_status()
        todos_response.raise_for_status()

        user_data = user_response.json()
        todos_data = todos_response.json()

        return user_data, todos_data

    except requests.RequestException as e:
        print(f"Error: {e}")
        return None, None

def display_employee_tasks(employee_id):
    """
    Displays the employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.
    """
    user_data, todos_data = get_employee_data(employee_id)
    if user_data and todos_data:
        employee_name = user_data.get("name")
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get("completed")]
        num_done_tasks = len(done_tasks)

        print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        display_employee_tasks(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
