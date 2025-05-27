
from author_dashboard.models.author import Author
from author_dashboard.models.magazine import Magazine
from author_dashboard.models.article import Article

def seed_data():
    author = Author("Jane Doe")
    mag1 = Magazine("Code Monthly", "Technology")
    mag2 = Magazine("DB Times", "Databases")

    Article("How to Code in Python", mag1, author)
    Article("Advanced SQL Tips", mag2, author)

    return author, [mag1, mag2]
