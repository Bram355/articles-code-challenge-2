class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return f"Magazine(name={self.name}, category={self.category})"