class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    def set_age(self, age):
        self.age = age
    def set_name(self, name):
        self.name = name

Student1 = Student("John", 22)
Student1.display()
print(Student1.get_age())
print(Student1.get_name())
Student1.set_age(25)
Student1.set_name("Smith")  

    