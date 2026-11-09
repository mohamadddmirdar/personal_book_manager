
from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Enter your name: ")
print("welcome",name)

admin_mode = input("Do you want to enter admin mode? (yes/no) ")
if admin_mode == "yes":
    password = input("Enter admin password: ")
    if password == os.getenv("admin_pass"):
        print("admin mode activated")
    else:
        print("wrong password")

tasks = load_tasks()
count = int(input("how many tasks do you wants to add? "))

for i in range(count):
    task_name = input("Enter your task: ")
    priority = input("Enter priority(low/medium/high): ")
    task = {
        "name" : task_name,
        "priority" : priority
    }
    tasks.append(task)

show_tasks(tasks)
save_tasks(tasks)