# **kwagrs
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name="Pushkar")       
print_kwargs(name="Pushkar", age = 20)       
print_kwargs(name="Pushkar", age =20 , level = "Bachelors")       