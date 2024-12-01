distance = int(input("Enter the distance: "))

if distance < 3:
    transportation = "Walk"
elif distance < 16:
    transportation = "Bike"
else:
    transportation = "Car"

print(transportation)
