from flask import Flask, render_template, request, redirect # Add 'render_template' to your listed imports from Flask
from lib.database_connection import DatabaseConnection
from lib.book import Book
from lib.book_repository import BookRepository
from lib.user import User
from lib.user_repository import UserRepository

# instantiate a Flask app object
app = Flask(__name__)

# Route to render our home page / index page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Routes for seeing the book list

@app.route('/books', methods=['GET'])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books=books)

# Route for adding a new book, redirects back top book list

@app.route('/books', methods=['POST'])
def create_book():
  connection = DatabaseConnection()
  connection.connect()
  book_repository = BookRepository(connection)
  book_details = request.form
  new_book = Book(None, book_details['title'], book_details['author'])
  book_repository.add_book(new_book)
  return redirect("/books")

# Routes for seeing the sign up page

@app.route('/users/new', methods=['GET'])
def new_user():
    return render_template("signup_form.html")

# Route for adding user details at sign up page and rerouting to book list

@app.route('/users/new', methods=['POST'])
def create_user():
  print("FORM DATA RECEIVED:", request.form)
  connection = DatabaseConnection()
  connection.connect()
  user_repository = UserRepository(connection)
  user_details = request.form
  new_user = User(None, user_details['username'], user_details['password'])
  user_repository.save_user_details(new_user)
  return redirect("/books")

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)


