#============================================
# Title:  mailloux_caculator.py
# Author: Richard Krasso
# Modified by: Laurie Mailloux
# Date:  June 17, 2020
# Description: Exercise 8.3
#===========================================


first_name = 'Laurie'
last_name = 'Mailloux'
print(first_name + ' ' + last_name)


def add(number1, number2): #function to add two numbers then return total
    return number1 + number2

def subtract (number1, number2): #function to subtract two numbers then return total
    return number1 - number2

def divide (number1, number2): #function to divide two numbers they return total
    return number1 / number2

#print the result of each call
print (add(4,2))
print(subtract(8,5))
print(divide(16,2))