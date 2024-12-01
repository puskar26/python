import math
import random
# print(2 ** 100)
# print(10>20)
# print(True and False)
# print(True or False)

# Floor -> Gives closest smaller value
# print(math.floor(3.6))
# print(math.floor(-3.6))

# Trunc -> Takes to the number towards zero

# print(math.trunc(2.7))
# print(math.trunc(-2.7))

# Complex Numbers
# comp1 = 2 + 3j
# comp2 = 3 + 8j
# print(comp1 + comp2)

# Other bases
# Octal -> 0onumber
# print(0o20)

# Hexadecimal -> 0xnumber
# print(0xFF)

# Binary -> 0bnumber
# print(0b111)

# Another way
# int('number', base)
# print(int('A' , 16))

# Randoms
# print(random.random()) # Gives Random value between 0 and 1

# Random integer 
# random.randint(start, end)
# print(random.randint(2,4))

# Random Choices
# random.choice(list)

l1 = ['Puskar','Pushkar']
# print(random.choice(l1))

# Shuffle -> random.shuffle(list)

random.shuffle(l1)
print(l1)