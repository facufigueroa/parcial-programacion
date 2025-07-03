import csv
from classes import LibraryItem, Book, Magazine



# Función para obtener los items del archivo csv
def loadLibraryItems(path : str) -> list[LibraryItem] :   # Latest python versions
# def loadLibraryItems(path : str) -> list :   # Older python versions
    items = []
    with open(path, "r") as file :
        reader = csv.reader(file)
        for row in reader :
            if row == [] :
                return items
            elif row[0] == "book" :
                if len(row) != 5 :
                    raise ValueError("Book row must have 5 items.")
                else :
                    items.append(Book(row[1], int(row[2]), row[3], int(row[4])))
            elif row[0] == "magazine" :
                if len(row) != 4 :
                    raise ValueError("Magazine row must have 4 items.")
                else :
                    items.append(Magazine(row[1], int(row[2]), int(row[3])))
    return items



def checkoutItems(items : list[LibraryItem], user : str) -> list[str] :   # Latest python versions
# def checkoutItems(items : list, user : str) -> list :   # Older python versions
    if type(user) != str :
        raise TypeError("user must be a string")
    else :
        messages = []
        for item in items :
            messages.append(item.checkout(user))
        return messages



# Función para contar la cantidad de libros y revistas
def countItems(items : list[LibraryItem]) -> dict :   # Latest python versions
# def countItems(items : list) -> dict :   # Older python versions
    count = {
        "books" : 0,
        "magazines" : 0
    }
    for item in items :
        if item.__class__.__name__ == "Book" :
            count["books"] += 1
        else :
            count["magazines"] += 1
    return count



# Función para filtrar items
def findByTitle(items : list[LibraryItem], keyword : str) -> list[LibraryItem] :   # Latest python versions
# def findByTitle(items : list, keyword : str) -> list :   # Older python versions
    if type(keyword) != str :
        raise TypeError("keyword must be a string")
    else :
        libraryItems = []
        for item in items :
            if keyword.lower() in item.title.lower() :
                libraryItems.append(item)
        return libraryItems