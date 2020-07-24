"""view holds presentation logic"""
from model import Person
def showAllView(list):
   print("In our db we have {} users. Here they are:".format(len(list)))
   for item in list:
      print(item.name())
def startView():
   print('MVC - the simplest example')
   print('Do you want to see everyone in my db?[y/n]')
def endView():
   print('Goodbye!')