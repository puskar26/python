age = int(input("Whats your age?: "))
day = input("Is it Wednesday?:(Y/n)")

# if day == 'Y':
#     if age < 18:
#         print("Your ticket costs $6.")
#     else:
#         print("Your tivcket costs $10.") 
# else:
#     if age < 18:
#         print("Your ticket costs $8.")        
#     else:
#         print("Your ticket costs $12.")        

price  = 12 if age > 17 else 8
if day == 'Y':
    price -= 2;

print("Your ticket costs $",price)
