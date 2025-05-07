# define person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: " + self.name + ", Age: " + str(self.age)
    
# example person object
person = Person("John", 36)
print(person)    

# define male class
class Male(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = "Male"

    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

    def get_gender(self):
        print(f"Gender is {self.gender}")

# define female class
class Female(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = "Female"

    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

    def get_gender(self):
        print(f"Gender is {self.gender}")

# example male and female objects
male = Male("Mike", 40)
female = Female("Anna", 30)

male.print_details()
male.get_gender()
female.print_details()
female.get_gender()
