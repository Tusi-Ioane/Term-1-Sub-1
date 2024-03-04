#example PARENT CLASS
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

#parent class
class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def printname(self):
        print(self.name, self.color)

x = fruit ("banana", "yellow")
x.printname()

#child class
class field(fruit):
    pass

x = field("pear", "green")
x.printname()

#__init__ function + super function
class field(fruit):
    def __init__(self, name, color):
        super().__init__(name, color)
        fruit.__init__(self, name, color)

#properties
class field(fruit):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.expireyear = 2009
    def printname(self):
        print(self.name, self.color, self.expireyear)

# class field(fruit):
#     def __init__(self, name, color):
#         super().__init__(name, color)
#         self.expireyear = 
