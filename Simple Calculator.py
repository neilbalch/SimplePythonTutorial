# output = 0
# num1 = ""
# operation = ""
# num2 = ""
# num1 = input("Hello, What is your First Number?\n")
# operation = input("Operation (+, -, *, /)?\n")
# num2 = input("Your Second Number?\n")

# floatnum1 = float(num1)
# floatnum2 = float(num2)

# if operation == "+":
#     output=floatnum1+floatnum2
# if operation == "-":
#     output=floatnum1-floatnum2
# if operation == "*":
#     output=floatnum1*floatnum2
# if operation == "/":
#     output=floatnum1/floatnum2
# if operation == "+" or operation == "-" or operation == "/" or operation == "*":
#     print("Your Answer: "+str(output))
# else:
#     print("Your operation is invalid, please try again")




# this new code is better i guess
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operator = input("Enter an operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
