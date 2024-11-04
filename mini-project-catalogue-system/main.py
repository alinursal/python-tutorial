class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"You have checked out '{self.title}'.")
        else:
            print(f"'{self.title}' is currently not available.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not checked out.")

    def display_info(self):
        availability = "Available" if self.is_available else "Checked Out"
        print(f"Title: {self.title}, Author: {self.author}, Status: {availability}")


class Catalogue:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the catalogue.")

    def display_books(self):
        if not self.books:
            print("No books in the catalogue.")
            return
        for book in self.books:
            book.display_info()


def main():
    # Creating the book catalogue
    catalogue = Catalogue()

    # Adding books to the catalogue
    catalogue.add_book("To Kill a Mockingbird", "Harper Lee")
    catalogue.add_book("1984", "George Orwell")
    catalogue.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    print("\nCurrent Book Catalogue:")
    catalogue.display_books()

    # Checking out a book
    print("\nChecking out '1984':")
    book_to_check_out = catalogue.books[1]  # Accessing the second book
    book_to_check_out.check_out()

    # Displaying updated catalogue
    print("\nUpdated Book Catalogue:")
    catalogue.display_books()

    # Returning the book
    print("\nReturning '1984':")
    book_to_check_out.return_book()

    # Final display of the catalogue
    print("\nFinal Book Catalogue:")
    catalogue.display_books()

main()