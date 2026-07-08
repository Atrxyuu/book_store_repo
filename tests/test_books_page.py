from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_books_has_page(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    h1 = page.locator("h1")

    expect(h1).to_have_text("Reading List")

def test_books_page_has_books(page: Page):
    # Ask the database to form a connection
    db_connection = DatabaseConnection()
    db_connection.connect()

    # Fetch the exact raw rows currently in the database
    db_books = db_connection.execute("SELECT title, author FROM books;")

    # Format the database rows exactly how Jinja formats them in the HTML
    expected_books = [
        f"{row['title']} by {row['author']}" for row in db_books
    ]

    # Tell Playwright to go to the page
    page.goto("http://127.0.0.1:5001/books")
    book_list = page.locator("li")

    #Assert that the page matches the database perfectly
    expect(book_list).to_have_text(expected_books)

def test_books_page_form_works(page: Page):

    page.goto("http://localhost:5001/books")
    page.get_by_placeholder("Title").fill("The Chronicles of Geronimo (the cat)")
    page.get_by_placeholder("Author").fill("Geronimo")

    page.get_by_role("button", name="Submit").click()

    # Look specifically inside an <li> tag for this text
    expect(page.locator("li").get_by_text("The Chronicles of Geronimo (the cat) by Geronimo")).to_be_visible()






