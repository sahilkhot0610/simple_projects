class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.total_quantity = quantity

class Library:
    def __init__(self): 
        self.books = []

    def add_books(self, title, author, quantity):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.total_quantity += quantity
                print(f"The Book{title} is updated ! Total Quantity is : {book.total_quantity}")
                return

        new_book = Book(title, author, quantity)
        self.books.append(new_book)
        print(f"The Book {title} is added successfully in Library")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"The Book {book.title} founded with quantity of {book.total_quantity}")
                return 
            
        print(f"The Book {title} is not found in library")
        return 

    def display_books(self):
        print(f"\n {'Title' :<20} | {'Author' :<20} | {'Quantity' :<20}")
        print("-" * 55)
        for book in self.books:
            print(f"{book.title :<20} | {book.author :<20} | {book.total_quantity :<10}\n")

        return
    
    def lend_off(self, title, quantity):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.total_quantity < quantity:
                    print("That Much books is not available ! come later !")
                    break
                book.total_quantity -= quantity
                print(f"The book {title} is lend off with {quantity} quantity")
                return
        
        print(f"The Book with title {title} is not found in library")

    def return_book(self, title, quantity):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.total_quantity += quantity
                print(f"The Book{title} is updated ! Total Quantity is : {book.total_quantity}")
                return

        else:
            print(f"This book {title} is not available in library to return it press 1 to dd it as a new book")    
        
        
My_Library = Library()

while(True):
    print("\n-----Welcome to Library-----")
    print("1 : Add Books")
    print("2 : Search Books")
    print("3 : Borrow Books")
    print("4 : Return Books")
    print("5 : Display Books")
    print("6 : Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        print("Enter the Book details : ")
        title = input("Title : ")
        author = input("Author : ")
        try:
            quantity = int(input("Quantity : ")) 
        except ValueError:
            print("Please Enter the qunatity as an integer ")
            continue
            
        My_Library.add_books(title, author, quantity)
    
    elif choice == 2:
        search_title = input("Enter The title of book to search : ")
        My_Library.search_book(search_title)

    elif choice == 3:
        title = input("Enter Book title which is to borror : ")
        try:
            quantity = int(input("Quantity : ")) 
        except ValueError:
            print("Please Enter the qunatity as an integer ")
            continue
            
        My_Library.lend_off(title, quantity)

    elif choice == 4:
        title = input("Enter Book title to return  : ")
        try:
            quantity = int(input("Quantity : ")) 
        except ValueError:
            print("Please Enter the qunatity as an integer ")
            continue
            
        My_Library.return_book(title, quantity)

    elif choice == 5:
        My_Library.display_books()

    elif choice == 6:
        break

    else:
        print("Invalid Choice ! Please Try Again")
        