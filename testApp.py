import unittest
from app import LibraryItem, Book, Magazine, loadLibraryItems, checkoutItems, countItems, findByTitle

class TestConstructores(unittest.TestCase) :
    def testCasoPositivo(self) :
        book = Book("El principito", 15, "Juan Perez", 153)
        self.assertEqual(book, )