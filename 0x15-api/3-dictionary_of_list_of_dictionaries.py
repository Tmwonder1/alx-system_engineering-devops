#!/usr/bin/python3
"""
This script gathers data from a REST API for all employees
and exports their TODO list progress to a JSON file.
"""

import json
import requests

def get_all_employees_data():
    """
    Gets data for all employees from the API.

    Returns:
        list: A list of dictionaries containing user data and their tasks.
    """
    try:
        users_url = "https://jsonplaceholder.typicode.com/users"
        todos_url = "https://jsonplaceholder.typicode.com/todos"

        users_response = requests.get(users_url)
        todos_response = requests.get(todos_url)

        users_response.raise_for_status()
        todos_response.raise_for_status()

        users_data = users_response.json()
        todos_data = todos_response.json()

        return users_data, todos_data

    except requests.RequestException as e:
        print(f"Error: {e}")
        return None, None

def export_all_to_json():
    """
    Exports all employees' tasks to a JSON file.
    """
    users_data, todos_data = get_all_employees_data()
    if users_data and todos_data:
        all_tasks = {}
        for user in users_data:
            user_id = user.get("id")
            username = user.get("username")
            tasks = [task for task in todos_data if task.get("userId") == user_id]
            all_tasks[user_id] = [{"username": username,
                                   "task": task.get("title"),
                                   "completed": task.get("completed")} for task in tasks]

        json_filename = "todo_all_employees.json"
        with open(json_filename, mode='w') as json_file:
            json.dump(all_tasks, json_file)

if __name__ == "__main__":
    export_all_to_json()
