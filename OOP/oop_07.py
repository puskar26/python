# Static Methods
# Methods that only belongs to the class not it's instances

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
    @staticmethod
    def static_method():
        return "Only Car can access it."

class ElectricVehicle(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
    
safari =  Car("Tata","Prada")

Tesla = ElectricVehicle("Tesla", "ModelX", "160kWH")
# print(Tesla.fuel_type())
# print(safari.fuel_type())
# print(Car.total_car)

# print(Tesla.static_method())

# isinstance() -> shows whether a object is an instance of a class or not

print(isinstance(Tesla , ElectricVehicle))
print(isinstance(Tesla , Car))