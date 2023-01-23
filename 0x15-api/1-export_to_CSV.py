#!/usr/bin/python3
"""
this script uses REST API to return information about
his/her TODO list progress given an employee id
"""
import csv
import requests
import sys

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
            with open('{}.csv'.format(emp_id, mode='w+')) as fw:
                writer = csv.writer(fw, delimeter=', ', quoting=csv.QUOTE_ALL)
                for i in tasks_done:
                    writer.writerow([i['userId'], emp_name, i['completed'], i['title']])
