"""OOPS in Python"""
class Book():

    # class variable
    __booklist = []

    #staticmethod
    @staticmethod
    def getbooklist():
         if len(Book.__booklist) == 0: # if no books, create a list, else return existing list
             Book.__booklist = []
         else:
            return Book.__booklist

    def __init__(self, book_name):
        self.book_name = book_name
        Book._Book__booklist.append(book_name)
        print("Book named {} added.".format(self.book_name))
        
    # instance method
    def set_price(self, price):
        # price is private variable
        self.__price = price
        print("Book price set to be ",self.__price)

    # instance method
    def author(self,author):
        # author is protected variable
        self._author = author
        print("Book author set to be ",self._author)

a = Book('Introduction to algorithms by Santosh Vagga')
a.set_price(1200)
a.author('Mr. Santoshkumar Vagga')

# to access private variable directly without use of function, use object._classname__privatevariable
print("The set price is ",a._Book__price)
print(a.getbooklist())

b = Book('Data structures by Sahani')
b.set_price(450)
b.author('Mrs. Sahani')
print(a.getbooklist())