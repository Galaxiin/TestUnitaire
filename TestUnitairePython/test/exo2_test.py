# test Unit Exo 2

import sys
sys.path.append('')

from classScript import Book
from classScript import Client
from classScript import Library

import unittest

class TestBook(unittest.TestCase):

    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    book2 = Book("Pride and Prejudice", "Jane Austen")

    def test_check_out(self):
        self.assertFalse(self.book1.is_checked_out)
        self.book1.check_out()
        self.assertTrue(self.book1.is_checked_out)

        self.assertFalse(self.book2.is_checked_out)
        self.book2.check_out()
        self.assertTrue(self.book2.is_checked_out)

    def test_check_in(self):
        self.book1.check_out()
        self.assertTrue(self.book1.is_checked_out)
        self.book1.check_in()
        self.assertFalse(self.book1.is_checked_out)

        self.book2.check_out()
        self.assertTrue(self.book2.is_checked_out)
        self.book2.check_in()
        self.assertFalse(self.book2.is_checked_out)

class TestClient(unittest.TestCase):

    client1 = Client("John Doe")
    client2 = Client("Jane Doe")

    def test_check_out_book(self):
        self.client1.check_out_book(self.library, "To Kill a Mockingbird")
        self.client2.check_out_book(self.library, "To Kill a Mockingbird")

        self.assertEqual(len(self.client.checked_out_books), 1)
        self.assertIn(self.book1, self.client.checked_out_books)

    def test_check_in_book(self):
        self.client1.check_out_book(self.library, "To Kill a Mockingbird")
        self.assertEqual(len(self.client.checked_out_books), 1)
        self.client1.check_in_book(self.library, "To Kill a Mockingbird")
        self.assertEqual(len(self.client.checked_out_books), 0)

class TestLibrary(unittest.TestCase):

    library = Library()

    def setUp(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        self.assertEqual(len(self.library.books), 2)
        self.assertIn(self.book1, self.library.books)
        self.assertIn(self.book2, self.library.books)

    def test_check_out_book(self):
        self.library.check_out_book("To Kill a Mockingbird")
        self.library.check_out_book("Pride and Prejudice")
        self.assertTrue(self.book1.is_checked_out)
        self.assertTrue(self.book2.is_checked_out)

if __name__ == '__main__':
    unittest.main()