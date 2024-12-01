coffee_size = input("Coffee_size?: ").capitalize()
Extra_shot = True

if Extra_shot:
    coffee_order = "coffee with an extra shot"
elif not Extra_shot:
    coffee_order = "coffee"

print(coffee_size + " " + coffee_order) 
