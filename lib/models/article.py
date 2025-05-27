class Article:
    def __init__(self, title, magazine, author):
        self.title = title
        self.magazine = magazine
        self.author = author
        author.add_article(self)
