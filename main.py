class Person:
    def __init__(self, name):
        self.name = name

    
p1 = Person("Saavi")
print(p1.name)

class student:
    def __init__(self,name):
        self.name = name
    print("Object created")

    def __del__(self):
          print("Object destroyed")

s1 = student("Saavi")
del s1
