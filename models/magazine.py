from database.connection import get_db_connection
from models.article import Article  # No circular import here

class Magazine:
    def __init__(self, id, name, category=None):  # Default value for 'category'
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value is not None and (not isinstance(value, str) or len(value) <= 0):
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    @staticmethod
    def create(name, category):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        conn.commit()
        magazine_id = cursor.lastrowid
        conn.close()
        return Magazine(magazine_id, name, category)

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]) for article in articles]

    def contributors(self):
        from models.author import Author  # Lazy import to avoid circular import
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT a.* FROM authors a
            JOIN articles ar ON ar.author_id = a.id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return [Author(author["id"], author["name"]) for author in authors]
