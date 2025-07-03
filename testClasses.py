import unittest
from classes import Book, Magazine

class TestClasses(unittest.TestCase) :

    # Test positivo del constructor de la clase Book.
    def testBookConstructorPositive(self) :
        book = Book("El principito", 15, "Juan Perez", 153)

        self.assertEqual(book.title, "El principito")
        self.assertEqual(book.itemId, 15)
        self.assertEqual(book.author, "Juan Perez")
        self.assertEqual(book.pages, 153)
    
    # Test negativo del constructor de la clase Book.
    def testBookConstructorNegative(self) :

        # Title recibe int en lugar de str.
        with self.assertRaises(TypeError) :
            Book(1526, 15, "Juan Perez", 153)
        
        # ItemId recibe str en lugar de int.
        with self.assertRaises(TypeError) :
            Book("El principito", "15", "Juan Perez", 153)
        
        # Author recibe int en lugar de str.
        with self.assertRaises(TypeError) :
            Book("El principito", 15, 159466, 153)
        
        # Pages recibe str en lugar de int.
        with self.assertRaises(TypeError) :
            Book("El principito", 15, "Juan Perez", "153")
        
        # Title recibe una cadena vacía.
        with self.assertRaises(ValueError) :
            Book("", 15, "Juan Perez", 153)
        
        # ItemId recibe un número menor o igual a cero.
        with self.assertRaises(ValueError) :
            Book("El principito", 0, "Juan Perez", 153)
        
        # Author recibe una cadena vacía.
        with self.assertRaises(ValueError) :
            Book("El principito", 15, "", 153)
        
        # Pages recibe un número menor o igual a cero.
        with self.assertRaises(ValueError) :
            Book("El principito", 15, "Juan Perez", -1)
    
    # Test positivo del constructor de la clase Magazine.
    def testMagazineConstructorPositive(self) :
        magazine = Magazine("Las aventuras de Juan", 15, 152)

        self.assertEqual(magazine.title, "Las aventuras de Juan")
        self.assertEqual(magazine.itemId, 15)
        self.assertEqual(magazine.issueNumber, 152)
    
    # Test negativo del constructor de la clase Magazine.
    def testMagazineConstructorNegative(self) :

        # Title recibe int en lugar de str.
        with self.assertRaises(TypeError) :
            Magazine(1565, 15, 152)
        
        # ItemId recibe str en lugar de int.
        with self.assertRaises(TypeError) :
            Magazine("Las aventuras de Juan", "15", 152)
        
        # IssueNumber recibe str en lugar de int.
        with self.assertRaises(TypeError) :
            Magazine("Las aventuras de Juan", 15, "152")
        
        # Title recibe una cadena vacía.
        with self.assertRaises(ValueError) :
            Magazine("", 15, 152)
        
        # ItemId recibe un número menor o igual a cero.
        with self.assertRaises(ValueError) :
            Magazine("Las aventuras de Juan", 0, 152)
        
        # IssueNumber recibe un número menor o igual a cero.
        with self.assertRaises(ValueError) :
            Magazine("Las aventuras de Juan", 15, -1)
    
    # Test positivo del método checkout de las clases Book y Magazine.
    def testCheckoutPositive(self) :
        book = Book("El principito", 15, "Juan Perez", 153)
        magazine = Magazine("Las aventuras de Juan", 15, 152)

        bookExpected = "Book 'El principito' checked out by Facu."
        magazineExpected = "Magazine 'Las aventuras de Juan' issue 152 checked out by Facu."

        self.assertEqual(book.checkout("Facu"), bookExpected)
        self.assertEqual(magazine.checkout("Facu"), magazineExpected)
    
    # Test negativo del método checkout de las clases Book y Magazine.
    def testCheckoutNegative(self) :
        book = Book("El principito", 15, "Juan Perez", 153)
        magazine = Magazine("Las aventuras de Juan", 15, 152)

        bookNotExpected = "Book 'El principito' checked out by ."
        magazineNotExpected = "Magazine 'Las aventuras de Juan' issue 152 checked out by ."

        self.assertNotEqual(book.checkout("Facu"), bookNotExpected)
        self.assertNotEqual(magazine.checkout("Facu"), magazineNotExpected)

if __name__ == "__main__" :
    unittest.main()