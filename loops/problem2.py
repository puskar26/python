n = int(input("Enter n: "))
count = 0

for i in range(1, n+1):
    if i % 2 == 0:
        count += i
print(count)