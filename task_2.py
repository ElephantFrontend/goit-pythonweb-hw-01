from abc import ABC, abstractmethod
from typing import List
from logger import logger


class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title: str = title
        self.author: str = author
        self.year: str = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info(f"Книга додана: {book}")

    def remove_book(self, title: str) -> None:
        initial_count: int = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        if len(self.books) < initial_count:
            logger.info(f"Книга з назвою '{title}' видалена.")
        else:
            logger.info(f"Книга з назвою '{title}' не знайдена.")

    def get_books(self) -> List[Book]:
        return self.books


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book: Book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books: List[Book] = self.library.get_books()
        if not books:
            logger.info("Бібліотека порожня.")
        else:
            logger.info("Список книг у бібліотеці:")
            for book in books:
                logger.info(str(book))


def main() -> None:
    library: Library = Library()
    manager: LibraryManager = LibraryManager(library)

    while True:
        command: str = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title: str = input("Enter book title: ").strip()
                author: str = input("Enter book author: ").strip()
                year: str = input("Enter book year: ").strip()
                manager.add_book(title, author, year)

            case "remove":
                title: str = input("Enter book title to remove: ").strip()
                manager.remove_book(title)

            case "show":
                manager.show_books()

            case "exit":
                logger.info("Вихід із програми.")
                break

            case _:
                logger.info("Невідома команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
