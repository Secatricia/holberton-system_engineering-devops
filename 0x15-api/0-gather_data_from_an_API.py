#!/usr/bin/python3
""" using this REST API, for a given employee ID"""
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    user = requests.get(user_url).json()
    TODO = requests.get(todo_url).json()

    cpt_nb = 0
    total_nb = 0
    cpt_task = []

    for task in TODO:
        total_nb += 1
        if task.get("completed") is True:
            cpt_nb += 1
            cpt_task.append(task.get("title"))

    sentence = "Employee {} is done with tasks({}/{}):"

    print(sentence.format(user.get("name"), cpt_nb, total_nb))

    for task in cpt_task:
        print("\t {}".format(task))
