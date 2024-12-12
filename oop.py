# Define the Car class
class Car:
    # Constructor method to initialize the car's attributes
    def __init__(self, make, model, year):
        self.make = make  # Brand of the car (e.g., Ford, Toyota)
        self.model = model  # Model of the car (e.g., Mustang, Corolla)
        self.year = year  # Year of manufacture

    # Method to display car information
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    # Method to start the car
    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is now running.")

    # Method to stop the car
    def stop_engine(self):
        print(f"The {self.make} {self.model}'s engine is now off.")

# Create an instance (object) of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(my_car)
# # Call the methods on the object
my_car.display_info()  # Display the car's information
my_car.start_engine()  # Start the engine
my_car.stop_engine()  # Stop the engine

