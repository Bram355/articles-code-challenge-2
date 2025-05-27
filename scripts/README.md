

This project is designed to manage a simple database of articles, authors, and magazines using SQLite. It includes scripts for setting up the database schema, seeding it with initial data, and running example queries.




articles-code challenge
├── lib
│   └── db
│       ├── connection.py
│       ├── seed.py
│       └── schema.sql
├── scripts
│   ├── setup_db.py
│   └── run_queries.py
├── requirements.txt
└── README.md

Tests
```


2. **Install dependencies**:
   Make sure you have Python installed, then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   Run the following command to create the database schema and seed it with initial data:
   ```
   python scripts/setup_db.py
   ```

## Usage

- To run example queries against the database, use:
  ```
  python scripts/run_queries.py
  ```


- **lib/db/connection.py**: Contains the `get_db_connection()` function to establish a connection to the SQLite database.
- **lib/db/seed.py**: Defines the `seed_database()` function to populate the database with initial data.
- **lib/db/schema.sql**: Contains SQL commands for creating the necessary tables in the database.
- **scripts/setup_db.py**: Executes the SQL commands in `schema.sql` and calls `seed_database()` to populate the database.
- **scripts/run_queries.py**: Intended for running example queries and demo scripts against the database.
- **requirements.txt**: Lists the dependencies required for the project.



