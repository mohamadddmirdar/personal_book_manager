
from book import show_books, save_books, load_books
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Enter your name: ")
print("welcoomeee",name)

admin_mode = input("Do you want to enter admin mode? (yes/no) ")
if admin_mode == "yes":
    password = input("Enter admin password: ")
    if password == os.getenv("admin_pass"):
        print("admin mode activated")
    else:
        print("wrong password")

tasks = load_books()
count = int(input("how many tasks do you wants to add? "))

for i in range(count):
    task_name = input("Enter your task: ")
    priority = input("Enter priority(low/medium/high): ")
    task = {
        "name" : task_name,
        "priority" : priority
    }
    tasks.append(task)

<<<<<<< HEAD
show_tasks(tasks)
save_tasks(tasks)
=======

show_books(tasks)
save_books(tasks)
>>>>>>> eaeebe7969d84f72944cd4ac320ad85f4a1439e3
