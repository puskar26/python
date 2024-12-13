# Polymorphism

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand # __ makes a variable private
        self.model = model
        Car.total_car += 1
    def display(self):
        return (f"{self.__brand} {self.model}")
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return "Petrol"

class ElectricVehicle(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
    
safari =  Car("Tata","Prada")

Tesla = ElectricVehicle("Tesla", "ModelX", "160kWH")
print(Tesla.fuel_type())
print(safari.fuel_type())
print(Car.total_car)