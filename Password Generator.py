#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string

def generate_password(length=12, uppercase=True, digits=True, symbols=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if length < 1:
        return "Password length must be at least 1."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")
    length = int(input("Enter password length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_uppercase, include_digits, include_symbols)

    print(f"Generated Password: {password}")

if __name__ == "__main__":
    password_generator()


# In[ ]:




