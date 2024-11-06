# Define the Person class
class Person:
    def __init__(self, name, age, gender):
        self.name = name  # Name of the person
        self.age = age    # Age of the person
        self.gender = gender  # Gender of the person

    def introduce(self):
        # Introduce the person by printing their details
        print(f"Hello! My name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

# Create an instance of the Person class
person1 = Person("John", 30, "Male")

# Call the introduce method to display the person's information
person1.introduce()
