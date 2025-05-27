

import pytest


class Magazine:
    def __init__(self, name):
        self.name = name

class Article:
    def __init__(self, title, magazine):
        self.title = title
        self.magazine = magazine

class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def magazines(self):
        return list({article.magazine for article in self.articles})


def test_author_initialization():
    author = Author("Alice")
    assert author.name == "Alice"
    assert author.articles == []

def test_add_article():
    author = Author("Bob")
    mag = Magazine("Tech Today")
    article = Article("AI Advances", mag)
    author.add_article(article)
    assert len(author.articles) == 1
    assert author.articles[0].title == "AI Advances"

def test_magazines_returns_unique_list():
    author = Author("Clara")
    mag1 = Magazine("Science Weekly")
    mag2 = Magazine("Nature World")
    article1 = Article("Quantum Physics", mag1)
    article2 = Article("Climate Change", mag2)
    article3 = Article("Black Holes", mag1)
    author.add_article(article1)
    author.add_article(article2)
    author.add_article(article3)
    mags = author.magazines()
    assert len(mags) == 2
    assert mag1 in mags
    assert mag2 in mags
