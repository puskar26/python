# Multiple Inheritance

class Battery:
    def type(self):
        return "Battery."

class Engine:
    @property  # It makes method a property
    def run(self):
        return "Engine starts"
    
class ElectricCar(Battery, Engine):
    pass

my_car = ElectricCar()

print(my_car.type())
print(my_car.run)