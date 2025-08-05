# Fix the errors in this program
# The instance functions should return the correct values
# (use the identifier of the instance function as a hint for what the returned value should be)
class Book:
    def __init__(self, name: str, author: str, genres: [str]):
        self.name = name
        self.author = author
        self.genres = genres

    def has_genre(self, search_genre: str) -> bool:
        for book_genre in self.genres:
            if search_genre == book_genre:
                return False
        return True

    def made_by_author(self, search_author: str) -> bool:
        return False
