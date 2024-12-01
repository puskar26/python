dict1 = {
    "name":"pushkar",
    "age" : 20 ,
    "level" : "Bachelors",
}
# print(dict1)

# To print values
# print(dict1["name"])
# print(dict1["age"])
# print(dict1.get("level"))

# Change values of the keys in dictionary
dict1["name"] = "Eakraj"
# print(dict1)

# Iterating via dictionaries
# for info in dict1:
#     print(info, dict1[info])

# Another method
# for key, value in dict1.items():
#     print(key, value) 

# Conditionals in dictionaries
# if "name" in dict1:
#     print("Valid") 

# Length  
# print(len(dict1))

# Adding new value pairs
# dict1["field"] = "Computer Engineering"
# print(dict1)

# Remove element
# dict1.pop("level")
# print(dict1)

# To remove lasy item
# dict1.popitem()
# print(dict1)

# del -> Removes reference from the memory
# del dict1["field"]
# print(dict1)

# To copy
# dict2 = dict1.copy()
# print(dict2)

# Multiple Dictionaries
drinks = {
    "Tea" : {
        "Black" : "bold",
        "Green" : "grassy",
        "White" : "delicate",
        "Oolong" : "floral",
        "Herbal" : "fruity",
    },
    "Coffee" : {
        "Espresso" : "rich",
        "Americano" : "bold",
        "Latte" : "creamy",
        "Cappuccino" : "frothy",
        "Mocha" : "chocolatey",
    },
}
# print(drinks)
# print(drinks["Tea"])
# print(drinks["Coffee"])
# print(drinks["Coffee"]["Cappuccino"])
# print(drinks["Tea"]["Black"])

# Interesting

# set1  = {x : x ** 2 for x  in range (10)}
# print(set1)
# set1.clear()
# print(set1)

# Make dictionaries from keys
keys = ["Black", "Green", "Herbal"]
default_value = "delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)