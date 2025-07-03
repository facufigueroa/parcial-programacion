from abc import ABC, abstractmethod



class LibraryItem(ABC) :
    def __init__(self, title : str, itemId : int):
        if not isinstance(title, str) :
            raise TypeError("Title must be a string.")
        elif not isinstance(itemId, int) :
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

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        pass



class Book(LibraryItem) :
    def __init__(self, title : str, itemId : int, author : str, pages : int):
        super().__init__(title, itemId)

        if not isinstance(author, str) :
            raise TypeError("Author must be a string.")
        elif not isinstance(pages, int) :
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
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Book) and self.title == other.title and self.itemId == other.itemId and self.author == other.author and self.pages == other.pages
    
    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}."



class Magazine(LibraryItem) :
    def __init__(self, title: str, itemId: int, issueNumber : int):
        super().__init__(title, itemId)

        if not isinstance(issueNumber, int) :
            raise TypeError("Issue number must be an int.")
        elif issueNumber <= 0 :
            raise ValueError("Issue number must be positive.")
        else :
            self.issueNumber = issueNumber
    
    def checkout(self, user : str) -> str:
        return f"Magazine '{self.title}' issue {self.issueNumber} checked out by {user}."
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Magazine) and self.title == other.title and self.itemId == other.itemId and self.issueNumber == other.issueNumber
    
    def __str__(self) -> str:
        return f"Title: {self.title}, issue number: {self.issueNumber}."