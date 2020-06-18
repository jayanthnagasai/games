class Calculator:

name = input("Enter your name:")
print("Welcome to Jay's Python Calculator Version 3.0,   " + name)
print("\nHere's the legend for the calculator:")
legend = ["+ = Add", "- = Subtract", "+ = Multiply", "/ = Division", "Inverse = Inverse of Division", "% = Mod",
          "Greater = To see which number is greater", "Square of First number = a^2", "Square of First number = a^2",
          "Square of Second number = b^2", "Cube of First number = a^3", "Cube of First number = a^3",
          "First number over Second number = a^b", "Second number over First number = b^a", "First root Second = a^1/b",
          "Second root First = b^1/a", "Inverse of First number = 1/a", "Inverse of Second number = 1/b"]


for rule in legend:
    print(rule)

print("\nStart your calculations, " + name)
num1 = float(input("Enter first number:"))
operator = input("Enter operator:")
num2 = float(input("Enter second number:"))

try:
    if operator == "+":
        print("\nYour Answer is = ")
        print(num1 + num2)
    elif operator == "-":
        print("\nYour Answer is = ")
        print(num1 - num2)
    elif operator == "*":
        print("\nYour Answer is = ")
        print(num1 * num2)
    elif operator == "/":
        print("\nYour Answer is = ")
        print(num1 / num2)
    elif operator == "Inverse":
        print("\nYour Answer is = ")
        print(num2 / num1)
    elif operator == "%":
        print("\nYour Answer is = ")
        print(num1 % num2)
    elif operator == "Greater" and num1 >= num2:
        print("\nYour Answer is = ")
        print(num1)
    elif operator == "Greater" and num2 >= num1:
        print("\nYour Answer is = ")
        print(num2)
    elif operator == "Square of First number":
        print("\nYour Answer is = ")
        print(num1 * num1)
    elif operator == "Square of First number":
        print("\nYour Answer is = ")
        print(num1 * num1)
    elif operator == "Square of Second number":
        print("\nYour Answer is = ")
        print(num2 * num2)
    elif operator == "Cube of First number":
        print("\nYour Answer is = ")
        print(num1 * num1 * num1)
    elif operator == "Cube of Second number":
        print("\nYour Answer is = ")
        print(num2 * num2 * num2)
    elif operator == "First number over Second number":
        print("\nYour Answer is = ")
        print(pow(num1, num2))
    elif operator == "Second number over First number":
        print("\nYour Answer is = ")
        print(pow(num2, num1))
    elif operator == "Square root of First number":
        print("\nYour Answer is = ")
        print(pow(num1, 1/2))
    elif operator == "Square root of Second number":
        print("\nYour Answer is = ")
        print(pow(num2, 1/2))
    elif operator == "Cube root of First number":
        print("\nYour Answer is = ")
        print(pow(num1, 1/3))
    elif operator == "Cube root of Second number":
        print("\nYour Answer is = ")
        print(pow(num1, 1/3))
    elif operator == "First root Second":
        print("\nYour Answer is = ")
        print(pow(num1, 1/num2))
    elif operator == "Second root First":
        print("\nYour Answer is = ")
        print(pow(num2, 1/num1))
    elif operator == "Inverse of First number":
        print("\nYour Answer is = ")
        print(1/num1)
    elif operator == "Inverse of Second number":
        print("\nYour Answer is = ")
        print(1 / num2)
    else:
        print("\nInvalid Operation")
except ZeroDivisionError:
    print("\nINVALID ANSWER - Divided by Zero")
except ValueError:
    print("\nINVALID ANSWER - Value Error")


print("\nThanks for using the calculator," + name)

