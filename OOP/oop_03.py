# Inheritance

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        print(f"{self.model}{self.brand}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model V", "100 kWH")

print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)
print(my_tesla.display())

