class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car_info = Car("Toyota", "Corolla")

print(car_info.brand)
print(car_info.model)