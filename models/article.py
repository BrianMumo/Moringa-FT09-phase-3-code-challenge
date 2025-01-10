from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed.")
        self._title = value

    @staticmethod
    def create(author, magazine, title, content):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO articles (title, content, author_id, magazine_id) 
            VALUES (?, ?, ?, ?)
        """, (title, content, author.id, magazine.id))
        conn.commit()
        article_id = cursor.lastrowid
        conn.close()
        return Article(article_id, title, content, author.id, magazine.id)
