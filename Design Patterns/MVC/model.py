import json
"""model holds business logic, interacts with db directly"""
class Person():
    def __init__(self, firstname=None, lastname= None):
        self.firstname = firstname
        self.lastname = lastname

    def name(self):
        return '{} {}'.format(self.firstname,self.lastname)

    @classmethod
    def getAll(cls):
        database = open('db.txt','r')
        result = []
        print('db contents is:',database.read())
        json_list = json.loads(database.read())
        for item in json_list:
           item = json.loads(item)
           person = Person(item['firstname'], item['lastname'])
           result.append(person)
        return result