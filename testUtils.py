import unittest
import csv
import tempfile
from classes import Book, Magazine
from utils import loadLibraryItems, checkoutItems, countItems, findByTitle

class TestUtils(unittest.TestCase) :

    # Test positivo de la función loadLibraryItems.
    def testLoadLibraryItemsPositive(self) :
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".csv", delete=False, newline="") as tempCsvFile :
            csvWriter = csv.writer(tempCsvFile)
            data = [["book", "El principito", 15, "Juan Perez", 153], ["magazine", "Las aventuras de Juan", 15, 152]]
            csvWriter.writerows(data)
        
        items = loadLibraryItems(tempCsvFile.name)
        expected = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]

        self.assertEqual(items, expected)

    # Test negativo de la función loadLibraryItems.
    def testLoadLibraryItemsNegative(self) :
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".csv", delete=False) as tempCsvFile :
            csvWriter = csv.writer(tempCsvFile)
            
            csvWriter.writerow(["book", 15, "Juan Perez", 153])
            csvWriter.writerow(["magazine", "Las aventuras de Juan", 152])

        # La función recibe menos datos de los que necesita.
        with self.assertRaises(ValueError) :
            loadLibraryItems(tempCsvFile.name)         
    
    # Test positivo de la función checkoutItems.
    def testCheackoutItemsPositive(self) :
        libraryItems = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]
        checkoutLibraryItems = checkoutItems(libraryItems, "Facu")

        expected = ["Book 'El principito' checked out by Facu.", "Magazine 'Las aventuras de Juan' issue 152 checked out by Facu."]

        self.assertEqual(checkoutLibraryItems, expected)

    # Test negativo de la función checkoutItems.
    def testCheackoutItemsNegative(self) :
        libraryItems = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]

        # El parámetro user de la función es de tipo str y recibe int.
        with self.assertRaises(TypeError) :
            checkoutItems(libraryItems, 5)
    
    # Test positivo de la función countItems.
    def testCountItemsPositive(self) :
        libraryItems = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]
        count = {
            "books" : 1,
            "magazines" : 1
        }

        self.assertEqual(countItems(libraryItems), count)

    # Test negativo de la función countItems.
    def testCountItemsNegative(self) :
        libraryItems = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]
        count = {
            "books" : 1,
            "magazines" : 0
        }

        self.assertNotEqual(countItems(libraryItems), count)

    # Test positivo de la función findByTitle.
    def testFindByTitlePositive(self) :
        libraryItems = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]
        itemsByTitle1 = findByTitle(libraryItems, "Principito")
        itemsByTitle2 = findByTitle(libraryItems, "harry")

        self.assertEqual(itemsByTitle1[0], libraryItems[0])
        self.assertEqual(itemsByTitle2, [])

    # Test negativo de la función findByTitle.
    def testFindByTitleNegative(self) :
        libraryItems = [Book("El principito", 15, "Juan Perez", 153), Magazine("Las aventuras de Juan", 15, 152)]

        # El parámetro keyword de la función es de tipo str y recibe int.
        with self.assertRaises(TypeError) :
            findByTitle(libraryItems, 56)

if __name__ == "__main__" :
    unittest.main()