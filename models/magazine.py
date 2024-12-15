class Magazine:
    def __init__(self, id, name, category="Uncategorized"):
        self._id = id
        self._name = name
        self._category = category

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def __repr__(self):
        return f"Magazine(id={self.id}, name='{self.name}', category='{self.category}')"
