from abc import ABC, abstractmethod

#Clase abstracta
class LibraryItem(ABC) :
    def __init__(self, title : str, itemId : int):
        self.title = title
        self.itemId = itemId
    
    @abstractmethod
    def checkout(self, user : str) -> str :
        pass

#Subclase
class Book(LibraryItem) :
    def __init__(self, title : str, itemId : int, author : str, pages : int):
        if type(title) != str :
            raise(TypeError, "Title must be a string.")
        elif type(author) != str :
            raise(TypeError, "Author must be a string.")
        elif type(itemId) != int :
            raise(TypeError, "ItemId must be an int.")
        elif type(pages) != int :
            raise(TypeError, "Pages must be an int.")
        elif title == "" :
            raise(ValueError, "Title is required.")
        elif author == "" :
            raise(ValueError, "Author is required.")
        elif itemId <= 0 :
            raise(ValueError, "ItemId must be positive.")
        elif pages <= 0 :
            raise(ValueError, "Pages must be positive.")
        else :
            super().__init__(title, itemId)
            self.author = author
            self.pages = pages
    
    def checkout(self, user):
        return f"Book {self.title} checked out by {user}."

#Subclase
libro = Book("Cars", "25", "Juan Cruz Perez", 123)