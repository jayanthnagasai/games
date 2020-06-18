name = input("Enter your name:")
print("Welcome to Jay's Python Calculator Version 3.0" + name)
print("Here's the legend for the calculator")
legend = ["+ = Add", "- = Subtract", "+ = Multiply", "+ = Division", "Inverse = Inverse of Division", "% = Mod",
          "Greater = To see which number is greater", "Square of First number = a^2", "Square of First number = a^2", ]

num1 = float(input("Enter first number:"))
operator = input("Enter operator:")
num2 = float(input("Enter second number:"))


if operator == "+":
    print("Your Answer is = ")
    print(num1 + num2)
elif operator == "-":
    print("Your Answer is = ")
    print(num1 - num2)
elif operator == "*":
    print("Your Answer is = ")
    print(num1 * num2)
elif operator == "/":
    print("Your Answer is = ")
    print(num1 / num2)
elif operator == "Inverse":
    print("Your Answer is = ")
    print(num2 / num1)
elif operator == "%":
    print("Your Answer is = ")
    print(num1 % num2)
elif operator == "Greater" and num1 >= num2:
    print("Your Answer is = ")
    print(num1)
elif operator == "Greater" and num2 >= num1:
    print("Your Answer is = ")
    print(num2)
elif operator == "Square of First number":
    print("Your Answer is = ")
    print(num1 * num1)
elif operator == "Square of First number":
    print("Your Answer is = ")
    print(num1 * num1)
elif operator == "Square of Second number":
    print("Your Answer is = ")
    print(num2 * num2)
elif operator == "Cube of First number":
    print("Your Answer is = ")
    print(num1 * num1 * num1)
elif operator == "Cube of Second number":
    print("Your Answer is = ")
    print(num2 * num2 * num2)
elif operator == "First number over Second number":
    print("Your Answer is = ")
    print(pow(num1, num2))
elif operator == "Second number over First number":
    print("Your Answer is = ")
    print(pow(num2, num1))
elif operator == "Square root of First number":
    print("Your Answer is = ")
    print(pow(num1, 1/2))
elif operator == "Square root of Second number":
    print("Your Answer is = ")
    print(pow(num2, 1/2))
elif operator == "Cube root of First number":
    print("Your Answer is = ")
    print(pow(num1, 1/3))
elif operator == "Cube root of Second number":
    print("Your Answer is = ")
    print(pow(num1, 1/3))
elif operator == "First root Second":
    print("Your Answer is = ")
    print(pow(num1, 1/num2))
elif operator == "Inverse of First number":
    print("Your Answer is = ")
    print(1/num1)
elif operator == "Inverse of Second number":
    print("Your Answer is = ")
    print(1 / num2)
else:
    print("Invalid Operation")

