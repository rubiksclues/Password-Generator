# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 22:33:10 2021
Password Generator
@author: Courtney
"""

#randomizer
import random

#imports characters a-z,A-Z, special characters (ascii)
import string

#possible password characters
Pass_Chars = string.ascii_letters + string.digits + string.punctuation

#password generating function using random function and characters created from string function; password can be 4-20 characters
x = random.randint(4,20)
password =''.join(random.choice(Pass_Chars) for i in range(x))
print("Password Suggestion: " + password)