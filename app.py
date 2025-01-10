from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine


def main():
    # Initialize the database and create tables
    create_tables()

    # Create sample authors
    print("\nCreating authors...")
    author1 = Author.create("John Doe")
    author2 = Author.create("Jane Smith")
    print(f"Created authors: {author1}, {author2}")

    # Create sample magazines
    print("\nCreating magazines...")
    magazine1 = Magazine.create("Tech Weekly", "Technology")
    magazine2 = Magazine.create("Fashion Forward", "Lifestyle")
    print(f"Created magazines: {magazine1}, {magazine2}")

    # Create sample articles
    print("\nCreating articles...")
    article1 = Article.create(author1, magazine1, "AI Innovations", "Content about AI.")
    article2 = Article.create(author1, magazine2, "Tech in Fashion", "Content on tech influencing fashion.")
    article3 = Article.create(author2, magazine1, "The Future of Robotics", "Robotics advancements.")
    print(f"Created articles: {article1}, {article2}, {article3}")

    # Test author methods
    print("\nTesting author methods...")
    print(f"{author1.name}'s Articles: {author1.articles()}")
    print(f"{author1.name}'s Magazines: {author1.magazines()}")

    # Test magazine methods
    print("\nTesting magazine methods...")
    print(f"{magazine1.name}'s Articles: {magazine1.articles()}")
    print(f"{magazine1.name}'s Contributors: {magazine1.contributors()}")

    # Test article methods
    print("\nTesting article methods...")
    print(f"Article '{article1.title}' Author: {author1.name}")
    print(f"Article '{article1.title}' Magazine: {magazine1.name}")

    # Additional aggregate and association methods
    print("\nTesting additional magazine methods...")
    print(f"{magazine1.name} Article Titles: {[article.title for article in magazine1.articles()]}")
    contributing_authors = [
        author for author in magazine1.contributors() if len(author.articles()) > 2
    ]
    print(f"{magazine1.name} Contributing Authors: {contributing_authors if contributing_authors else 'None'}")


if __name__ == "__main__":
    main()
