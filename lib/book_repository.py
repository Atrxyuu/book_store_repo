from lib.book import Book

# We initialise with a database connection
class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    #Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * FROM books')
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author"])
            books.append(item)
        return books
    
    def add_book(self, book):
        self._connection.execute(
            'INSERT INTO books (title, author) VALUES (%s, %s)',
            [book.title, book.author]
            )