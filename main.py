class Person:
    def __init__(self, name):
        self.name = name

    
p1 = Person("Saavi")
print(p1.name)

class student:
    def __init__(self,name):
        self.name = name
    print("Object created")

    def __del__(self):
          print("Object destroyed")

s1 = student("Saavi")
del s1


class Library:
    def __init__(self):
        self.books = ["Python", "HTML", "C++", "CSS"]

    def display_books(self):
        if self.books:
            print("\nAvailable Books:")
            for book in self.books:
                print("-", book)
        else:
            print("\nNo books available.")

    def lend_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"\nYou have claimed the book '{book_name}'.")
        else:
            print("\nSorry, Book not avalable")

    def return_book(elf,book_name):
        self.books.append(book_name)
        print(f"\n'{book_name}' has been returned")

    def add_book(self, book_name):
        self.book.append(book_name)
        print(f"\n'{book_name}' has been added to the library.")

library = Library()

while True:
    print("\n--- Library Manaagement System")
    print("1. Dispplay Books")
    print("2. Lend Book")
    print("3. Retuen Book")
    print("4. Add Book")
    print("5. Exit")
