import pytest
from src.author import Author
from src.article import Article
from src.magazine import Magazine

def test_article_initialization_adds_to_author():
    author = Author("Jane")
    magazine = Magazine("World News", "News")
    article = Article("Global Economy", magazine, author)
    
    assert article.title == "Global Economy"
    assert article.magazine == magazine
    assert article.author == author
    assert article in author.articles

def test_magazines_unique_list_from_articles():
    author = Author("Leo")
    mag1 = Magazine("Tech Today", "Technology")
    mag2 = Magazine("Nature Daily", "Science")
    
    Article("Quantum Leap", mag1, author)
    Article("AI Revolution", mag1, author)
    Article("Green Future", mag2, author)
    
    mags = author.magazines()
    
    assert len(mags) == 2
    assert mag1 in mags
    assert mag2 in mags