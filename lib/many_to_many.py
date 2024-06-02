
class Book:
    all = []  # Class variable to store all Book instances

    def __init__(self, title):
        self.title = title  
        Book.all.append(self)  # Add the book instance to the all list

    def contracts(self):
        # Returning a list of contracts related to the book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Returning a list of authors related to the book using the contracts
        return [contract.author for contract in self.contracts()]


class Author:
    all = [] # Storing Author instances

    def __init__(self, name):
        self.name = name  
        Author.all.append(self)  

    def contracts(self):
        # Returning a list of contracts related to the author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Returning a list of books related to the author using the contracts
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # Creating and returning a new contract between the author and the specified book
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Calculating  total royalties earned by the author from all contracts
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []  # Storing Contract instances

    def __init__(self, author, book, date, royalties):
        self.author = author 
        self.book = book  
        self.date = date  
        self.royalties = royalties  
        Contract.all.append(self)  
        
    @property
    def author(self):
        # Getter method for the author property
        return self._author

    @author.setter
    def author(self, author):
        # Setter method for the author property
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        self._author = author

    @property
    def book(self):
        # Getter method for the book property
        return self._book


    @book.setter
    def book(self, book):
        # Setter method for the book property
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        self._book = book


    @property
    def date(self):
        # Getter method for the date property
        return self._date


    @date.setter
    def date(self, date):
        # Setter method for the date property
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        self._date = date


    @property
    def royalties(self):
        # Getter method for the royalties property
        return self._royalties


    @royalties.setter
    def royalties(self, royalties):
        # Setter method for the royalties property
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        self._royalties = royalties


    @classmethod
    def contracts_by_date(cls, date):
        # Class method to return a list of contracts with the specified date
        return [contract for contract in cls.all if contract.date == date]