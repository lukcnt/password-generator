import string

print("Welcome to the LukCnt Password Generator!")

quantity_of_letters = int(input("How many letters would you like in your password?\n"))
quantity_of_numbers = int(input("How many numbers would you like?\n"))
quantity_of_symbols = int(input("How many symbols would you like?\n"))

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)