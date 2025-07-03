import unittest
from classes import Book, Magazine

class TestClasses(unittest.TestCase) :
    def testBookConstructorPositive(self) :
        book = Book("El principito", 15, "Juan Perez", 153)

        self.assertEqual(book.title, "El principito")
        self.assertEqual(book.itemId, 15)
        self.assertEqual(book.author, "Juan Perez")
        self.assertEqual(book.pages, 153)
    
    def testBookConstructorNegative(self) :
        with self.assertRaises(TypeError) :
            Book(1526, 15, "Juan Perez", 153)
        
        with self.assertRaises(TypeError) :
            Book("El principito", "15", "Juan Perez", 153)
        
        with self.assertRaises(TypeError) :
            Book("El principito", 15, 159466, 153)
        
        with self.assertRaises(TypeError) :
            Book("El principito", 15, "Juan Perez", "153")
        
        with self.assertRaises(ValueError) :
            Book("", 15, "Juan Perez", 153)
        
        with self.assertRaises(ValueError) :
            Book("El principito", 0, "Juan Perez", 153)
        
        with self.assertRaises(ValueError) :
            Book("El principito", 15, "", 153)
        
        with self.assertRaises(ValueError) :
            Book("El principito", 15, "Juan Perez", -1)
    
    def testMagazineConstructorPositive(self) :
        magazine = Magazine("Las aventuras de Juan", 15, 152)

        self.assertEqual(magazine.title, "Las aventuras de Juan")
        self.assertEqual(magazine.itemId, 15)
        self.assertEqual(magazine.issueNumber, 152)
    
    def testMagazineConstructorNegative(self) :
        with self.assertRaises(TypeError) :
            Magazine(1565, 15, 152)
        
        with self.assertRaises(TypeError) :
            Magazine("Las aventuras de Juan", "15", 152)
        
        with self.assertRaises(TypeError) :
            Magazine("Las aventuras de Juan", 15, "152")
        
        with self.assertRaises(ValueError) :
            Magazine("", 15, 152)
        
        with self.assertRaises(ValueError) :
            Magazine("Las aventuras de Juan", 0, 152)
        
        with self.assertRaises(ValueError) :
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

if __name__ == "__main__" :
    unittest.main()