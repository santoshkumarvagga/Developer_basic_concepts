"""OOPS in Python"""
class Book():
    def __init__(self, book_name):
        self.book_name = book_name
        print("Book named {} added.".format(self.book_name))
        
    def set_price(self, price):
        # price is private variable
        self.__price = price
        print("Book price set to be ",self.__price)

    def author(self,author):
        # author is protected variable
        self._author = author
        print("Book author set to be ",self._author)

a = Book('Introduction to algorithms by Santosh Vagga')
a.set_price(1200)
a.author('Mr. Santoshkumar Vagga')

# to access private variable directly without use of function, use object._classname__privatevariable
print("The set price is ",a._Book__price)