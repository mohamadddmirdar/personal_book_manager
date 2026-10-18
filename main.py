print("hi")
name = input("enter your name ? ")


book_num = int(input("how many book do yu want add ?  "))

books_list = []

for i in range (book_num):
    book = input("please enter a name book  ")
    books_list.append(book)