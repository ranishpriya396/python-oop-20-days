# 🐍 Day 2 — __init__() & Instance Attributes
# ans -> __init__() is a special method that runs automatically when an object is created.
# self -> self is a reference to the current instance of the class. It allows access to the attributes and methods of the class in Python.
# self.name -> The name belonging to this particular object.
# self refers to different objects:
# student1 → self → student1
# student2 → self → student2
# self refers to the object currently being worked on.
# instance attributes are unique to each instance of a class. They are defined within the __init__() method and are prefixed with self. This allows each object to have its own set of attributes, which can be accessed and modified independently of other instances.
# 2. self = current object ⭐⭐⭐
# Right side = incoming value
# Left side (self.x) = stored in the object
# 4. Parameter vs attribute
# Create an Employee class with:

# name
# age
# salary
# -> create oject for the class and print the attributes of the object.
class Employee:
    def __init__(self, name, age,salary): # parameters
        self.name =name   # instance attribute
        self.age =age 
        self.salary = salary
    def display(self):
        print(f"name : { self.name} , age : {self.age},salary : {self.salary}")

emp1 = Employee("ranish", 25, 50000)
emp2 = Employee("Kari",34,34004)
emp1.display()
emp2.display()

# 4. emp1.display() → calls method for emp1

