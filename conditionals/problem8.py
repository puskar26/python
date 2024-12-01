password = input("Enter your password: ")

password_size = len(password)

if password_size < 6:
    strength = "weak"
elif password_size < 11:
    strength = "medium"
else:
    strength = "strong"

print("Your password strength is",strength)
