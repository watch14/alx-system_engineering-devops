#!/usr/bin/env python3
""" API TODOS """
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]

    todo_link = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    user_link = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    user_resp = requests.get(user_link)
    todo_resp = requests.get(todo_link)

    user_data = user_resp.json()
    todo_data = todo_resp.json()

    tasks = 0
    done = 0
    completed = []
    for todo_item in todo_data:
        tasks += 1

        if todo_item["completed"]:
            completed.append(todo_item["title"])
            done += 1

    print("Employee {} is done with tasks ({}/{})".format(
        user_data['name'], done, tasks))
    for i in completed:
        print(f"\t {i}")
