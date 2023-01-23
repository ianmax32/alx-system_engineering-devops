#!/usr/bin/python3
"""
this script uses REST API to return information about
his/her TODO list progress given an employee id
"""
import sys
import requests

if __name__ == "__main__":
    emp_id = sys.argv[1]
    link1 = 'https://jsonplaceholder.typicode.com/users/'
    link2 = 'https://jsonplaceholder.typicode.com/todos'
    resp_todo = requests.get(link2.format(emp_id))
    resp_user = requests.get(link1 + emp_id)

    emp_name = resp_user.json().get('name')
    tasks = resp_todo.json()
    tasks_done = []
    num_tasks = 0

    for a in tasks:
        if a.get('userId') == int(emp_id):
            num_tasks += 1
            if a.get('completed') is True:
                tasks_done.append(a.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(emp_name,
                                                          len(tasks_done),
                                                          num_tasks))

    for a in tasks_done:
        print('\t {}'.format(a))
