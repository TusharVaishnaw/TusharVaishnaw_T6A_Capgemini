class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, branch):
        super().__init__(name)   # call parent constructor
        self.branch = branch

s = Student("Tushar", "IT")

print(s.name, s.branch)
