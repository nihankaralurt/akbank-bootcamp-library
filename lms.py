"""
Library Management System

In this project I implemented basic string/list/file operations,
created a Library class with constructor and destructor methods
and created a simple terminal menu to manage the library system.

Akbank Python Bootcamp Assignment

Nihan Karalürt
16.02.2024
"""

class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
    
    def __del__(self):
        self.file.close()
    
    def list_books(self):
        # Read the contents of the file
        self.file.seek(0) #move cursor to the top of the file
        content = self.file.read()
        # Add each line to a list using splitlines() method of the string object
        content = content.splitlines()
        #Now each element of the list holds information about a single book. Print book names and authors using this information.
        for info in content: 
            book = info.split(", ")
            print(f"Name:\t{book[0]}\nAuthor:\t{book[1]}\n")

    def add_books(self):
        #Ask user input for book title, book author, first release year and number of pages
        book_title = input('book_title:')
        book_author = input('book_author:')
        first_release_year = input('first_release_year:')
        number_of_pages = input('number_of_pages:')
        #Create a string with this information. Add book title then comma(virgül) then author then comma etc.
        new_book = book_title + ", "+ book_author + ", "+ first_release_year + ", "+ number_of_pages + "\n"
        #Append this line to the file. 
        self.file.write(new_book)
        
    def remove_books(self):
        #Ask the user input for book title.
        book_title = input("book title= ")
        #Read the file contents and add books to a list (just like you did while creating a list books method).
        #Find the index of the book to be deleted in the list.Remove the book from the list. 
        self.file.seek(0)
        content = self.file.read()
        content = content.splitlines()
        i = 0
        for title in content: 
            title = title.split(",")
            if title[0] == book_title:
                del content[i]
                break
            else:
                i += 1
        
        #Remove the contents of the books.txt
        self.file.truncate(0)
        #Add all elements of the list to the books.txt.
        for c in content:
            self.file.write(c + "\n")
       
lib = Library()

print("""
      *** MENU ***
      1) List Books
      2) Add Book
      3) Remove Book
      q) Exit
      """)
i = input("choose: ")
while i != "q":
    if i == "1":
        lib.list_books() 
    elif i == "2":
        lib.add_books()
    elif i == "3":
        lib.remove_books()
    else:
        print("Faulty Input")
    print("""
      *** MENU ***
      1) List Books
      2) Add Book
      3) Remove Book
      q) Exit
      """)
    i = input("choose: ")    
del lib