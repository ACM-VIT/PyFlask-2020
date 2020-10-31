# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:41:32 2020

@author: varun
"""

# defining strings in Python
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to the world of Python"""
print(my_string)

#Accessing string characters in Python
str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#STRING OPERATIONS

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

str1 = "One"
str2 = "Two"
str3 = "Three"

# Concatenation of three strings
print(str1 + str2 + str3)

#String Repetition
str = "ABC"

# repeating the string str by 3 times
print(str*3)

#UPPER AND LOWER CASE
print(str1.upper())
print(str1.lower())