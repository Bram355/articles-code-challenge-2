import sqlite3
from src.db.connection import get_db_connection

def seed_database():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Insert authors
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Jane",))
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Leo",))

    # Insert magazines
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("World News", "News"))
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Today", "Technology"))
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Nature Daily", "Science"))

    # Insert articles
    cursor.execute("INSERT INTO articles (title, magazine_id, author_id) VALUES (?, ?, ?)", ("Global Economy", 1, 1))
    cursor.execute("INSERT INTO articles (title, magazine_id, author_id) VALUES (?, ?, ?)", ("Quantum Leap", 2, 2))
    cursor.execute("INSERT INTO articles (title, magazine_id, author_id) VALUES (?, ?, ?)", ("AI Revolution", 2, 2))
    cursor.execute("INSERT INTO articles (title, magazine_id, author_id) VALUES (?, ?, ?)", ("Green Future", 3, 2))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    seed_database()