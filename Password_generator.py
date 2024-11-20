# Password Generator.

import random
import string

letter = int(input("How many letters would you like in your password?"))
a_letter = string.ascii_letters
symbol = int(input("How many symbols would you like?"))
b_symbol = string.punctuation
number = int(input("How many numbers would you like?"))
c_number = string.digits
password = []
for char in range(0,letter):
    password += random.choice(a_letter)
for char in range(0,symbol):
    password += random.choice(b_symbol)
for char in range(0,number):
    password += random.choice(c_number)
random.shuffle(password)
print(password)
total = ""
for character in password:
    total += character
print("Password:",total)


