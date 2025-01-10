from database.connection import get_db_connection
from models.article import Article  # No circular import here

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) <= 0:
            raise ValueError("Name must be a non-empty string.")
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed.")
        self._name = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer.")
        self._id = value

    @staticmethod
    def create(name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()
        author_id = cursor.lastrowid
        conn.close()
        return Author(author_id, name)

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]) for article in articles]

    def magazines(self):
        from models.magazine import Magazine  # Lazy import to avoid circular import
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON a.magazine_id = m.id
            WHERE a.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return [Magazine(mag["id"], mag["name"], mag["category"]) for mag in magazines]
