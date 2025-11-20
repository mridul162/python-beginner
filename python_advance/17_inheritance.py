# Inheritance Exercise

class Vehicle:
    def general_usage(self):        # Method to print general usage
        print("general use: transportation")

class Car(Vehicle):                 # Car class inherits from Vehicle
    def __init__(self):             # Constructor
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):       # Method to print specific usage
        print("specific use: commute to work, vacation with family")

class MotorCycle(Vehicle):          # MotorCycle class inherits from Vehicle
    def __init__(self):             # Constructor
        print("I'm motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):       # Method to print specific usage
        self.general_usage()
        print("specific use: road trip, racing")

c = Car()
m = MotorCycle()

print(isinstance(c,MotorCycle))
print(issubclass(Car,Vehicle))
print(issubclass(Car,MotorCycle))


