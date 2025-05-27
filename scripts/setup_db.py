import sqlite3
from lib.db.connection import get_db_connection

def setup_database():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Read and execute the schema.sql file
    with open('lib/db/schema.sql', 'r') as schema_file:
        schema_script = schema_file.read()
        cursor.executescript(schema_script)

    # Seed the database with initial data
    from lib.db.seed import seed_database
    seed_database()

    connection.close()

if __name__ == "__main__":
    setup_database()