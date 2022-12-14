import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the LukCnt Password Generator!")

quantity_of_letters = int(input("How many letters would you like in your password?\n"))
quantity_of_numbers = int(input("How many numbers would you like?\n"))
quantity_of_symbols = int(input("How many symbols would you like?\n"))

temporary_password = []

for counter in range(quantity_of_letters):
    random_letter = random.choice(LETTERS)
    temporary_password.append(random_letter)

for counter in range(quantity_of_numbers):
    random_number = random.choice(NUMBERS)
    temporary_password.append(random_number)

for counter in range(quantity_of_symbols):
    random_symbol = random.choice(SYMBOLS)
    temporary_password.append(random_symbol)

random.shuffle(temporary_password)

final_password = "".join(temporary_password)
print(f"Here is your password: {final_password}")