# Encapsulation

class Car:
    def __init__(self, brand, model):
        self.__brand = brand # __ makes a variable private
        self.model = model
    def display(self):
        return (f"{self.__brand} {self.model}")
    def get_brand(self):
        return self.__brand

class ElectricVehicle(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

Tesla = ElectricVehicle("Tesla", "ModelX", "160kWH")

print(Tesla.get_brand())
print(Tesla.display())