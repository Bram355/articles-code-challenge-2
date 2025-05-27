import sqlite3
from lib.db.connection import get_db_connection

def run_example_queries():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Example query: Retrieve all authors
    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()
    print("Authors:")
    for author in authors:
        print(author)

    # Example query: Retrieve all magazines
    cursor.execute("SELECT * FROM magazines")
    magazines = cursor.fetchall()
    print("\nMagazines:")
    for magazine in magazines:
        print(magazine)

    # Example query: Retrieve all articles
    cursor.execute("SELECT * FROM articles")
    articles = cursor.fetchall()
    print("\nArticles:")
    for article in articles:
        print(article)

    connection.close()

if __name__ == "__main__":
    run_example_queries()