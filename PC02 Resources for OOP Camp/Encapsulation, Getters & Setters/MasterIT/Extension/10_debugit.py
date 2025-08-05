# Fix the errors in this program
# - Use the correct access modifier/identifier for all instance variables
class Book:
    def __init__(self, title: str, genre: str, author: str, publish_date: str):
        self.__title = title
        self.__genre = genre
        self.__author = author
        self.__publish_date = publish_date

    def get_title(self) -> str:
        return self title

    def get_genre(self) -> str:
        return self.author

    def get_author(self) -> str:
        pass

    def get_publish_date(self) -> str:
        return publish_date


book = Book("Unknown Book", "Mystery", "U. K. Nown", "01-01-1990")
print(f"{book.get_title} | {book.get_author()}, {book.get_genre()}, {book.get_publish_date()}")
