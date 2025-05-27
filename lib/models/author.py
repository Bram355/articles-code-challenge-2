class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def magazines(self):
        return list({article.magazine for article in self.articles})
