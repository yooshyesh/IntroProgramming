class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self, name, age, grade):
        return f"Name: {name}, Alter: {age}, Note: {grade}."
    
class SchoolClass:
    pass

