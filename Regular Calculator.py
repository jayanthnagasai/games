
print("Welcome to Jay's Python Calculator Version 1.0")

from math import*

name= input("What is your name:")
num1= input("Enter the first number:")
num2= input("Enter the second number:")

sum= float(num1) + float(num2)
difference= float(num1) - float(num2)
product= float(num1) * float(num2)
qoutient= float(num1) / float(num2)
mod= float(num1) % float(num2)

print("Your sum is:")
print(sum)
print("Your difference is:")
print(difference)
print("Your product is:")
print(product)
print("Your qoutient is:")
print(qoutient)
print("Your mod is:")
print(mod)

print("Thank you for using the calculator," + name)

