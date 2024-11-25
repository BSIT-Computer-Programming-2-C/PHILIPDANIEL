# PHILIPDANIEL
# Define a class called Car
class Car:
    # The __init__ method is the constructor. It gets called when an object is created.
    def __init__(self, make, model, year):
        # These are attributes of the class
        self.make = make
        self.model = model
        self.year = year
    
    # A method that describes the car
    def describe_car(self):
        return f"{self.year} {self.make} {self.model}"
    
    # A method that simulates driving the car
    def drive(self):
        return f"The {self.model} is now driving!"

# Create an object (instance) of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes
print(my_car.make)    # Outputs: Toyota
print(my_car.year)    # Outputs: 2020

# Calling methods
print(my_car.describe_car())  # Outputs: 2020 Toyota Corolla
print(my_car.drive())         # Outputs: The Corolla is now driving!
