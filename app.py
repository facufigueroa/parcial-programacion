from abc import ABC, abstractmethod


#Clase abstracta
class LibraryItem(ABC) :
    def __init__(self, title : str, itemId : int):
        if type(title) != str :
            raise TypeError("Title must be a string.")
        elif type(itemId) != int :
            raise TypeError("Item id must be an int.")
        elif title == "" :
            raise ValueError("Title is required.")
        elif itemId <= 0 :
            raise ValueError("Item id must be positive.")
        else :
            self.title = title
            self.itemId = itemId
    
    @abstractmethod
    def checkout(self, user : str) -> str :
        pass


#Subclase
class Book(LibraryItem) :
    def __init__(self, title : str, itemId : int, author : str, pages : int):
        super().__init__(title, itemId)

        if type(author) != str :
            raise TypeError("Author must be a string.")
        elif type(pages) != int :
            raise TypeError("Pages must be an int.")
        elif author == "" :
            raise ValueError("Author is required.")
        elif pages <= 0 :
            raise ValueError("Pages must be positive.")
        else :
            self.author = author
            self.pages = pages
    
    def checkout(self, user : str) -> str:
        return f"Book '{self.title}' checked out by {user}."
    
    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}."


#Subclase
class Magazine(LibraryItem) :
    def __init__(self, title: str, itemId: int, issueNumber : int):
        super().__init__(title, itemId)

        if type(issueNumber) != int :
            raise TypeError("Issue number must be an int.")
        elif issueNumber <= 0 :
            raise ValueError("Issue number must be positive.")
        else :
            self.issueNumber = issueNumber
    
    def checkout(self, user : str) -> str:
        return f"Magazine '{self.title}' issue {self.issueNumber} checked out by {user}."
    
    def __str__(self) -> str:
        return f"Title: {self.title}, issue number: {self.issueNumber}."


#Función para obtener los items del archivo csv
def loadLibraryItems(path : str) -> list[LibraryItem] :
    items = []
    with open(path, "r") as file :
        for row in file :
            item = row.strip().split(",")
            if item[0] == "book" :
                items.append(Book(item[1], int(item[2]), item[3], int(item[4])))
            elif item[0] == "magazine" :
                items.append(Magazine(item[1], int(item[2]), int(item[3])))
    return items


def checkoutItems(items : list[LibraryItem], user : str) -> list[str] :
    if type(user) != str :
        raise TypeError("user must be a string")
    else :
        messages = []
        for item in items :
            messages.append(item.checkout(user))
        return messages


# Función para contar la cantidad de libros y revistas
def countItems(items : list[LibraryItem]) -> dict :
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


#Función para filtrar items
def findByTitle(items : list[LibraryItem], keyword : str) -> list[LibraryItem] :
    if type(keyword) != str :
        raise TypeError("keyword must be a string")
    else :
        libraryItems = []
        for item in items :
            if keyword.lower() in item.title.lower() :
                libraryItems.append(item)
        return libraryItems

# libraryItems = loadLibraryItems("library.csv")

# items = findByTitle(libraryItems, "harry")

# for i in items :
#     print(i)