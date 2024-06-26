#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(">>> Welcome to Python Password Generator <<<")

num_letters = int(input("How many letters would you like in your password? \n" ))
num_numbers = int(input("How many numbers would you like in your password? \n" ))
num_symbols = int(input("How many symbols would you like in your password? \n" ))

#East level
# password = ""

# for char in range(1, num_letters + 1):
#   random_chr = random.choice(letters)
#   password += random_chr
# print(password)

# for num in range(1, num_numbers + 1):
#   random_num = random.choice(numbers)
#   password += random_num

# for sym in range(1, num_symbols + 1):
#   random_sym = random.choice(symbols)
#   password += random_sym

# print(f"Your password will be: {password}")

#Hard level
password_list = []

for char in range(1, num_letters + 1):
  random_chr = random.choice(letters)
  password_list += random_chr

for num in range(1, num_numbers + 1):
  random_num = random.choice(numbers)
  password_list += random_num

for sym in range(1, num_symbols + 1):
  random_sym = random.choice(symbols)
  password_list += random_sym

random.shuffle(password_list)

password_string = ""
for password in password_list:
  password_string += password

print(f"Your password is: {password_string}")
