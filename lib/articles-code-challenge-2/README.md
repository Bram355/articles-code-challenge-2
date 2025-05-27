# articles-code-challenge-2

## Project Overview
This project is designed to manage articles, authors, and magazines. It provides a structured way to handle the relationships between these entities and includes a database layer for persistent storage.

## Project Structure
```
articles-code-challenge-2
├── src
│   ├── __init__.py
│   ├── author.py
│   ├── article.py
│   ├── magazine.py
│   └── db
│       ├── __init__.py
│       ├── connection.py
│       ├── schema.sql
│       └── seed.py
├── tests
│   ├── __init__.py
│   └── test_magazine.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd articles-code-challenge-2
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Database Setup
1. Ensure you have a compatible database server running.
2. Execute the SQL commands in `src/db/schema.sql` to create the necessary tables.
3. Run `src/db/seed.py` to populate the database with initial test data.

## Usage
- The `src` directory contains the main application logic, including classes for authors, articles, and magazines.
- The `tests` directory includes unit tests to verify the functionality of the application.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.