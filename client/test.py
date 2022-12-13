import unittest
from unittest.mock import Mock
import sys

from get_book_titles import get_books
from inventory_client import InventoryClient
from book_pb2 import Book

sys.path.append('../service/')


class TestGetBookTitles(unittest.TestCase):
    def test_get_book(self):
        inventory_client_mock = InventoryClient("test", 0)
        inventory_client_mock.get_book = Mock()
        expected_books = [Book(isbn="isbn1", title="ad pariatur"),
                          Book(isbn="isbn2", title="ad pariatur")]
        inventory_client_mock.get_book.side_effect = expected_books

        books = get_books(inventory_client_mock, ["isbn1", "isbn2"])

        assert books == expected_books

    def test_get_book_live_server(self):
        inventory_client = InventoryClient("localhost", 50051)
        books = get_books(inventory_client, ["isbn1", "isbn2"])
        assert len(books) == 2


if __name__ == "__main__":
    unittest.main()
