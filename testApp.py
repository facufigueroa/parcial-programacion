import unittest
from app import Book, Magazine, loadLibraryItems, checkoutItems, countItems, findByTitle

class TestApp(unittest.TestCase) :
    def testBookConstructorPositive(self) :
        book = Book("El principito", 15, "Juan Perez", 153)

        self.assertEqual(book.title, "El principito")
        self.assertEqual(book.itemId, 15)
        self.assertEqual(book.author, "Juan Perez")
        self.assertEqual(book.pages, 153)

    def testBookConstructorNegative(self) :
        with self.assertRaises(TypeError) :
            Book(1526, 15, "Juan Perez", 153)
            Book("El principito", "15", "Juan Perez", 153)
            Book("El principito", 15, 159466, 153)
            Book("El principito", 15, "Juan Perez", "153")
        
        with self.assertRaises(ValueError) :
            Book("", 15, "Juan Perez", 153)
            Book("El principito", 0, "Juan Perez", 153)
            Book("El principito", 15, "", 153)
            Book("El principito", 15, "Juan Perez", -1)
    
    def testMagazineConstructorPositive(self) :
        magazine = Magazine("Las aventuras de Juan", 15, 152)

        self.assertEqual(magazine.title, "Las aventuras de Juan")
        self.assertEqual(magazine.itemId, 15)
        self.assertEqual(magazine.issueNumber, 152)

    def testMagazineConstructorNegative(self) :
        with self.assertRaises(TypeError) :
            Magazine(1565, 15, 152)
            Magazine("Las aventuras de Juan", "15", 152)
            Magazine("Las aventuras de Juan", 15, "152")
        
        with self.assertRaises(ValueError) :
            Magazine("", 15, 152)
            Magazine("Las aventuras de Juan", 0, 152)
            Magazine("Las aventuras de Juan", 15, -1)

    def testCheckoutPositive(self) :
        book = Book("El principito", 15, "Juan Perez", 153)
        magazine = Magazine("Las aventuras de Juan", 15, 152)

        self.assertEqual(book.checkout("Facu"), "Book 'El principito' checked out by Facu.")
        self.assertEqual(magazine.checkout("Facu"), "Magazine 'Las aventuras de Juan' issue 152 checked out by Facu.")

    def testCheckoutNegative(self) :
        book = Book("El principito", 15, "Juan Perez", 153)
        magazine = Magazine("Las aventuras de Juan", 15, 152)

        self.assertNotEqual(book.checkout("Facu"), "Book 'El principito' checked out by .")
        self.assertNotEqual(magazine.checkout("Facu"), "Magazine 'Las aventuras de Juan' issue 152 checked out by .")
    
    def testCheackoutItemsPositive(self) :
        libraryItems = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]
        checkoutLibraryItems = checkoutItems(libraryItems, "Facu")

        self.assertEqual(checkoutLibraryItems, ["Book 'El principito' checked out by Facu.", "Magazine 'Las aventuras de Juan' issue 152 checked out by Facu."])

    def testCheackoutItemsNegative(self) :
        libraryItems = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]

        with self.assertRaises(TypeError) :
            checkoutItems(libraryItems, 5)
    
    def testCountItemsPositive(self) :
        libraryItems = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]
        count = {
            "books" : 1,
            "magazines" : 1
        }

        self.assertEqual(countItems(libraryItems), count)

    def testCountItemsNegative(self) :
        libraryItems = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]
        count = {
            "books" : 1,
            "magazines" : 0
        }

        self.assertNotEqual(countItems(libraryItems), count)

    def testFindByTitlePositive(self) :
        libraryItems = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]
        itemsByTitle1 = findByTitle(libraryItems, "Principito")
        itemsByTitle2 = findByTitle(libraryItems, "harry")

        self.assertEqual(itemsByTitle1[0], libraryItems[0])
        self.assertEqual(itemsByTitle2, [])

    def testFindByTitleNegative(self) :
        libraryItems = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]

        with self.assertRaises(TypeError) :
            findByTitle(libraryItems, 56)

if __name__ == "__main__" :
    unittest.main()