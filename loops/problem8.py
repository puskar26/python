number = 19
is_prime = True

for i in range(2, number):
    if (number % i) == 0:
        is_prime = False
        break

if(is_prime):
    print("Prime.")
else:
    print("Not Prime.")