# create author class
class Author:
    all=[]

    def __init__( self, name ):
        self.name = name
        Author.all.append(self)
    
    #create a contracts(self) method  
    def contracts(self):
        # this will return the contract for a contract in Contract.all (this is the Contract class and we are accessing the all object) if the contract author is equal with the entire self author
        return [ contract for contract in Contract.all if contract.author == self ] 
    
    def books( self ):
        # we have to return a list of related books using the Contract class as an intermediary
        # every book for our contract in self.contracts(ie the contracts in the self that we establish) and we must call this self.contracts 
        return [ contract.book for contract in self.contracts() ]
    
    def sign_contract( self, book, date, royalties ):

        return Contract( self, book, date, royalties )
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

# create a book class
class Book:
# we will need an empty object to append all the new book info
    all=[]
# class instructor that allows us to create instances of attributes
    def __init__(self,title):
        self.title = title
        Book.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]
    
# create contract class
class Contract:
    all = []
# this will have the properties book, date, author, and royalties
    def __init__( self, author, book, date, royalties ):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # @property
    # def author(self):
        # return self.author
    # 
    # @author.setter 
    # def author( self, value ):
        # if not isinstance( value, Author ):
            # raise Exception
        # self._author = value
    # 
    # @property
    # def book(self):
        # return self.book
    # @book.setter
    # def book( self, value ):
        # if not isinstance( value, Book ):
            # raise Exception
        # self._book = value

    # @property 
    # def date(self):
        # return self._date
    # 
    # @date.setter 
    # def date(self,value):
        # if not isinstance(value, str):
            # raise Exception
        # self._date = value

    # @property 
    # def royalties(self):
        # return self._royalties
    # 
    # @royalties.setter
    # def royalties(self,value):
        # if not isinstance(value,int):
            # raise Exception
        # self._royalties = value
    @classmethod
    def contracts_by_date( cls, date ):
        return sorted(cls.all, key = lambda c:c.date)
