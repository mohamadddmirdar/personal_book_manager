import os
from dotenv import load_dotenv
from book import show_books,save_books,load_books
load_dotenv()
print("hi")
name = input("enter your name ? ")

admin_mode = input("Do you want to enter admin mode? (yes/no) ")

if admin_mode == "yes":
    password = input("Enter admin password: ")
    if password == os.getenv("BOOK_MANAGER_PASSWORD"):
        print("admin mode activated")
    else:
        print("wrong password")


book_num = int(input("how many book do yu want add ?  "))

books_list = load_books()

for i in range (book_num):
    book = input("please enter a name book  ")
    books_list.append(book)

show_books(books_list)
save_books(books_list)