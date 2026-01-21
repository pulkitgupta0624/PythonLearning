'''
Write a library class  with no. of books and two instance variables.
Write a program ti creatr a library from this library class and show how you can print all books,
add a booka and get the number of books using different methods.
Show that your program diesn't persist the books after the program is stopped.

'''

class Library:
    no_of_books = 0

    def __init__(self, lib_name, location):
        self.lib_name = lib_name
        self.location = location
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        Library.no_of_books += 1

    def show_books(self):
        if len(self.books) == 0:
            print("No books available in library.")
        else:
            print("\n Books in Library:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    def get_books_count_class(self):
        return Library.no_of_books
    
    def get_books_count_list(self):
        return len(self.books)
    

lib = Library("Pulkit library", "Jaipur")

lib.add_book("Python Basics")
lib.add_book("OOPS in Python")
lib.add_book("DSA with Python")

print(f"🏛️ Library Name: {lib.lib_name}")
print(f"📍 Location: {lib.location}")

lib.show_books()
            
print("\n✅ Number of Books (using class variable):", lib.get_books_count_class())
print("✅ Number of Books (using len of list):", lib.get_books_count_list())

print("\n⚠️ Note: This program does NOT save books permanently.")
print("If you stop the program and run again, the books list becomes empty.")
