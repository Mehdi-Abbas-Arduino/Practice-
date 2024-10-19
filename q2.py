# OOPS 
class Vehicle:
    def __init__(self,make,model,year) -> None:
        self.make = make
        self.model = model
        self.year = year 
    def intro(self):
        print(f"This Vehicle is made by {self.make} in year {self.year} and the model is {self.model}")
        
class Truck(Vehicle):
    def __init__(self, make, model, year,cargo_capacity) -> None:
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity
        
    def start_engine(self):
        print("Start the Engine.")
        
class Car(Vehicle):
    def __init__(self, make, model, year,drive) -> None:
        super().__init__(make, model, year)
        self.drive = drive
        
    