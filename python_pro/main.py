import random 
import string

len_str = int(input("длинна вашего пароля"))

password = ''

for i in range(len_str):
    password += random.choice(string.printable)

print(password)