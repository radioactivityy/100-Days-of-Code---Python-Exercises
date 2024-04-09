import random
import string

letter_lenght = int(input("How many letters would you like in your password?"))
letter_password = ''.join(random.choice(string.ascii_letters) for _ in range (letter_lenght))
    
symbols_lenght = int(input("How many symbols would you like?"))
symbols_password = ''.join(random.choice(string.punctuation) for _ in range(symbols_lenght))

numbers_lenght  = int(input("How many numbers would you like?"))
numbers_password= ''.join(random.choice(string.digits) for _ in range (numbers_lenght))

password = letter_password + symbols_password + numbers_password

print(f"Your random password: {password}")