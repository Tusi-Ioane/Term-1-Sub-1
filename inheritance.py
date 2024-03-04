#single inheritance
# class animal:
#     def __init__(self, sound):
#         self.sound = sound
#     def printname(self):
#         print(self.sound)

# x = animal ("roar")
# x.printname()

# class dog(animal):
#     def __init__ (self, sound):
#         super().__init__(sound)
#         animal.__init__(self, sound)

# x = dog ("bark")
# x.printname()

#multiple inheritance
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age= age
    def printname(self):
        print(self.name, self.age)

x = Person ("Andy", "19")
x.printname()

class skills:
    def __init__(self, com, pro):
        self.communication = com
        self.program = pro
    def printname(self):
        print(self.communication, self.program)

x = skills("Speech", "Python")
x.printname()

class Employee(Person, skills):
    def __init__(self, name, age, communication, program):
        super().__init__(self, name, age, communication	, program)
        Person.__init__(self, name, age)
        skills.__init__(self, communication, program)
    def printname(self):
        return super().printname(self.name, self.age, self.communication, self.program)

#multilevel inheritance
# class vehicle:
#     def __init__(start_engine, )