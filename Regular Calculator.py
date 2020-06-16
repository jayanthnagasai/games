
print("Welcome to Jay's Python Calculator Version 1.0")

from math import *

name= input("What is your name:")
num1= input("Enter the first number:")
num2= input("Enter the second number:")

sum= float(num1) + float(num2)
difference= float(num1) - float(num2)
product= float(num1) * float(num2)
qoutient= float(num1) / float(num2)
mod= float(num1) % float(num2)
squ1= float(num1) * float(num1)
cub1= float(num1) * float(num1) * float(num1)
squ2= float(num2) * float(num2)
cub2= float(num2) * float(num2) * float(num2)
sqro1= sqrt(float(num1))
sqro2= sqrt(float(num2))
power_12= pow(float(num1), float(num2))
power_21= pow(float(num2), float(num1))

print("\nBASIC CALCULATIONS")
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

print("\nMAXIMUM/MINIMUM")
print("The maximum number you chose is:")
print(max(num1, num2))
print("The minimum number you chose is:")
print(min(num1, num2))

print("\nSQUARES, CUBES AND ROOTS")
print("The square of your first number is:")
print(squ1)
print("The cube of your first number is:")
print(cub1)
print("The square of your second number is:")
print(squ2)
print("The cube of your second number is:")
print(cub2)
print("The square root of your first number is:")
print(sqro1)
print("The square root of your second number is:")
print(sqro2)

print("\nPOWERS")
print("The power of your first number over your second power is:")
print(power_12)
print("The power of your second number over your first power is:")
print(power_21)


print("\nThank you for using the calculator," + name)

