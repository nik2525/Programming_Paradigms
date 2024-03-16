class Book:
    def __init__(self, title, author, genre):
        """
        Initialize a new book object with a title, author, and genre.

        :param title: The title of the book
        :param author: The author of the book
        :param genre: The genre of the book
        """
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        """
        Return a string representation of the book object.

        :return: A string representation of the book object
        """
        return f"{self.title} by {self.author} ({self.genre})"


class Library:
    def __init__(self):
        """
        Initialize a new library object with an empty list of books.

        """
        self.books = []

    def add_book(self, book):
        """
        Add a book object to the library's list of books.

        :param book: The book object to add to the library
        """
        self.books.append(book)

    def list_books(self):
        """
        Print a list of all the books in the library.

        """
        for book in self.books:
            print(book)

    def search_books(self, search_term):
        """
         #Search the library's list of books for a book with a title or author that matches the search term.

        :param search_term: The search term to look for in the library's list of books
        :return: A list of books that match the search term
        """
        results = []
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower():
                results.append(book)
        return results


def main():
   
     #The main function that runs the library management system.
    library = Library()

    # Add books to the library
    library.add_book(Book("The Catcher inthe Rye", "J.D. Salinger", "Fiction"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "Fiction"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"))
    library.add_book(Book("The Odyssey", "Homer", "Classic"))
    library.add_book(Book("SpaceJam", "Ben Tennyson", "Comedy"))

    # Display menu to user
    while True:
        print("\n1. List all books")
        print("2. Search for a book")
        print("3. Add a book")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            # List all books
            print("\nAll books:")
            library.list_books()
        elif choice == 2:
            # Search for books
            search_term = input("Enter a search term (title or author): ")
            results = library.search_books(search_term)
            if results:
                print("\nSearch results:")
                for book in results:
                    print(book)
            else:
                print("\nNo books found.")
        elif choice == 3:
            # Add a book
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")
            library.add_book(Book(title, author, genre))
            print("\nBook added successfully!")
        elif choice == 4:
            # Exit
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()