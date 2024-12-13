class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:",self.brand,"Model:", self.model )

my_car = Car("Toyota","Corolla")
my_car.display()