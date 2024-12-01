# List but immutable

tea_types = ("Black", "Milk", "Oolong")
# print(tea_types)

more_types = ("Earl", "Green")

new_tea = more_types + tea_types
# print(new_tea)

# To assign variables to tuple data
(Black, Milk, Oolong ) = tea_types
print(Black)
print(Milk)
print(Oolong)

# Types 
print(type(tea_types))