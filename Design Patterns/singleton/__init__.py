import selenium
class A:
    __instance = 1
    def __init__(self):
        if A.__instance == 1:
            print("Instance created first time.")
            A.__instance +=1
        else:
            return self
a = A()
b = A()
c = A()

print(a)
print(b)
print(c)