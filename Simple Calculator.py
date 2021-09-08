""" Python Simple Calculator """

# Setting all values to 0 (empty, nothing)
output = 0
num1 = ""
operation = ""
num2 = ""

# Asking What numbers you want using print command
num1 = input("Hello, What is your First Number?\n")
operation = input("Operation (+, -, *, /)?\n")
num2 = input("Your Second Number?\n")

# Setting asked numbers to float, so that it would give an exact answer
floatnum1 = float(num1)
floatnum2 = float(num2)

# If selected operation is the following then do the following
if operation == "+":
    output=floatnum1+floatnum2
if operation == "-":
    output=floatnum1-floatnum2
if operation == "*":
    output=floatnum1*floatnum2
if operation == "/":
    output=floatnum1/floatnum2
if operation == "+" or operation == "-" or operation == "/" or operation == "*":
    print("Your Answer: "+str(output))

# If none of above is the operation then give a error
else:
    print("Your operation is invalid, please try again")
