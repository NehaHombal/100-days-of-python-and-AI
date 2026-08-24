import random

import string

# 1. Contains a-z and A-Z (52 characters total)
letters_collection = list(string.ascii_letters)

# 2. Contains the most common password special characters
symbols_collection = list("!@#$%^&*()_+-=[]{}|;:,.<>?~/")

# 3. Contains '0' through '9'
numbers_collection = list(string.digits)

# Quick verification checks
# print("Letters:", letters_collection[:5], "... total:", len(letters_collection))
# print("Symbols:", symbols_collection[:5], "... total:", len(symbols_collection))
# print("Numbers:", numbers_collection)

print("Welcome to random password generator!..")
letters = int(input("How many letters would you like in your password?")) # 4
symbols = int(input("How many symbols would you like in your password?"))
numbers = int(input("How many numbers would you like in your password?"))

password_possible = []
# For letters
for i in range(letters):
    randomLetter = random.choice(letters_collection)
    password_possible.append(randomLetter)

# For symbols
for i in range(symbols):
    randomSymbol = random.choice(symbols_collection)
    password_possible.append(randomSymbol)

# For numbers
for i in range(numbers):
    randomNumber = random.choice(numbers_collection)
    password_possible.append(randomNumber)

result = "".join(str(elem) for elem in password_possible)
print("Easy: " + result)
random.shuffle(password_possible)
complex = "".join(str(elem) for elem in password_possible)
print("Hard: " + complex)