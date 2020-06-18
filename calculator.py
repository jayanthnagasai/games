
name = input("Enter your name:")
print("Welcome to Jay's Python Calculator Version 3.0,  " + name)

question1 = print(input("\nDo you want the legend for the calculator? \nYes or No\n"))

if question1 == "Yes":
    legend = ["+ = Add", "- = Subtract", "+ = Multiply", "/ = Division", "Inverse = Inverse of Division", "% = Mod",
              "> = To see which number is greater", "a^2 = Square of First number",
              "b^2 = Square of Second number ", "a^3 = Cube of First number", "b^3 = Cube of Second number",
              "a^b = First number times Second number ", "b^a = Second number times First number",
              "a^1/b = First root Second", "b^1/a = Second root First ", "1/a = Inverse of First number ",
              "1/b = Inverse of Second number "]
    for rule in legend:
        print(rule)
    trig_legend = ["\n Enter Sin for Sinθ", "Enter Cos for Cosθ", "Enter Tan for Tanθ", "Enter Cosec for Cosecθ",
                   "Enter Sec for Secθ", "Enter Cot for Cotθ"]
    for trig_rule in trig_legend:
        print(trig_rule)
else:
    print("Move On!")

print("\nNOTE: Remember that you can use the second operator for all calcuations except DMAS, Mod and Greater. \n Also,use the correct case while typing in the calculator")

question2 = print(input("\nDo you want to use the Regular calculator or the Trig calculator? \nRegular or Trig\n"))

if question2 == "Regular":
    print("\nStart your calculations, " + name)
    num1 = float(input("Enter first number:"))
    operator = input("Enter operator:")
    operator2 = input("Enter Second operator:")
    num2 = float(input("Enter second number:"))

    try:
        if operator == "+":
            print("\nYour Sum is = ")
            print(num1 + num2)
        elif operator == "-":
            print("\nYour Difference is = ")
            print(num1 - num2)
        elif operator == "*":
            print("\nYour Product is = ")
            print(num1 * num2)
        elif operator == "/":
            print("\nYour Qoutient is = ")
            print(num1 / num2)
        elif operator == "Inverse":
            print("\nYour Qoutient is = ")
            print(num2 / num1)
        elif operator == "%":
            print("\nYour Reminder is = ")
            print(num1 % num2)
        elif operator == ">" and num1 >= num2:
            print("\nThe Greater number between both the numbers you choose is= ")
            print(num1)
        elif operator == ">" and num2 >= num1:
            print("\nThe Greater number between both the numbers you choose is= ")
            print(num2)
        elif operator or operator2 == "a^2":
            print("\nThe Square product is = ")
            print(num1 * num1)
        elif operator or operator2 == "b^2":
            print("\nThe Square product is = ")
            print(num2 * num2)
        elif operator or operator2 == "a^3":
            print("\nThe Cube product is = ")
            print(num1 * num1 * num1)
        elif operator or operator2 == "b^3":
            print("\nThe Cube product is = ")
            print(num2 * num2 * num2)
        elif operator or operator2 == "a^b":
            print("\nYour Product is = ")
            print(pow(num1, num2))
        elif operator or operator2 == "b^a":
            print("\nYour Product is = ")
            print(pow(num2, num1))
        elif operator or operator2 == "a^1/2":
            print("\nThe Square root is = ")
            print(pow(num1, 1/2))
        elif operator or operator2 == "b^1/2":
            print("\nThe Square root is = ")
            print(pow(num2, 1/2))
        elif operator or operator2 == "a^1/3":
            print("\nThe Cube root is = ")
            print(pow(num1, 1/3))
        elif operator or operator2 == "b^1/2":
            print("\nThe Cube root is = ")
            print(pow(num1, 1/3))
        elif operator or operator2 == "a^1/b":
            print("\nYour Answer is = ")
            print(pow(num1, 1/num2))
        elif operator or operator2 == "b^1/a":
            print("\nYour Answer is = ")
            print(pow(num2, 1/num1))
        elif operator or operator2 == "1/a":
            print("\nYour Answer is = ")
            print(1/num1)
        elif operator or operator2 == "1/b":
            print("\nYour Answer is = ")
            print(1 / num2)
        else:
            print("\nInvalid Operation")
    except ZeroDivisionError:
        print("\nINVALID ANSWER - Divided by Zero")
    except ValueError:
        print("\nINVALID ANSWER - Value Error")

else:
    print("\nStart your calculations, " + name)
    opp = float(input("Enter Opposite:"))
    adj = float(input("Enter Adjacent:"))
    hyp = float(input("Enter Hypotenuse:"))
    ratio = (input("Enter Trig ratio required:"))

    try:
        if ratio == "sin" or "Sin":
            print("\nSinθ = ")
            print(opp / hyp)
        elif ratio == "cos" or "Cos":
                print("\nCosθ = ")
                print(adj / hyp)
        elif ratio == "tan" or "Tan":
                print("\nTanθ = ")
                print(opp / adj)
        elif ratio == "cosec" or "Cosec":
                print("\nCosecθ = ")
                print(hyp / opp)
        elif ratio == "sec" or "Sec":
            print("\nSecθ = ")
            print(hyp / adj)
        elif ratio == "Cot" or "cot":
            print("\nCotθ = ")
            print(adj / opp)
        else:
            print("\nInvalid Operation")
    except ZeroDivisionError:
        print("\nINVALID ANSWER - Divided by Zero")
    except ValueError:
        print("\nINVALID ANSWER - Value Error")


print("\nThanks for using the calculator," + name)


