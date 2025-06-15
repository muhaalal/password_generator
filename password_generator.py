#Password Generator
import random

strings_special_characters=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", ":", ";", "'", "<", ">", ",", ".", "?"]
strings_uppercase_letters= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "j", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
strings_numbers= ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
strings_lowercase_letters= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print("Hello, I will help you create a strong password which keeps you safe by protecting you from data breaches and hackers.")

while True:
    length=int(input("How many characters do you want your password to be: "))
    if length >=8:
        break
    else:
        print("🔴Your passwords length should be atleast 8 characters long")

special_characters=input("Would you like to include special characters (yes/no): ").lower()
numbers=input("Would you like to include numbers (yes/no): ").lower()

char_pool=strings_uppercase_letters+strings_lowercase_letters
if special_characters==("yes"):
    char_pool+=strings_special_characters
if numbers == ("yes"):
    char_pool+=strings_numbers

user_password=""
for i in range(length):
    user_password += random.choice(char_pool)

print(f"Your password is {user_password}")


