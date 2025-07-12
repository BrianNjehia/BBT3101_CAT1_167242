# Filename: 167242_q1.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{book.title} has been borrowed.")
        else:
            print(f"{book.title} is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{book.title} has been returned.")

    def list_borrowed_books(self):
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print(f"- {book.title} by {book.author}")


# Interactive part
if __name__ == '__main__':
    book1 = Book("1984", "George Orwell")
    book2 = Book("Brave New World", "Aldous Huxley")
    member = LibraryMember("Alice", "M001")

    while True:
        print("\n1. Borrow a book\n2. Return a book\n3. List borrowed books\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            if title == book1.title:
                member.borrow_book(book1)
            elif title == book2.title:
                member.borrow_book(book2)
            else:
                print("Book not found.")

        elif choice == '2':
            title = input("Enter book title to return: ")
            if title == book1.title:
                member.return_book(book1)
            elif title == book2.title:
                member.return_book(book2)
            else:
                print("Book not found.")

        elif choice == '3':
            member.list_borrowed_books()

        elif choice == '4':
            break
        else:
            print("Invalid option.")


