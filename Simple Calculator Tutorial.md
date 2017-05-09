# Simple Calculator

## Printing to the screen

In python, printing to the command line can be done using the `print()` statement. The only required argument is a string to be printed. For example, in Python 3, `print("Hello World")` will print `Hello World` to the command line.

## Intro to Input

In python, user input on the command line can be taken by using the command `input()`. Putting in a string (optional) as a paramter will give the user a prompt after which they can input text. This statement returns a string with the text the user typed, so it needs to be assigneed to a variable. This can be done in python like so, `myvar = input("Feed me data! ")`. Python is not a language with strongly typed variables, which means that you do not have to define a type when you create a variable. The interpreter will automatically assign the variable a type the first time it is instantiated with data.

## Getting input from the user for a calculation

Querying input from the user for a calculation can be done like so, 
```py
num1 = input("Hello, What is your First Number?\n")
operation = input("Operation?\n")
num2 = input("Your Second Number?\n")
```
This code will print a prompt asking for a first number to the screen, ask for input, print a prompt asking for an operation to the screen, ask for input, etc. The `\n` at the end of the strings is an escape character that tells python to add a newline to the end of the prompt. I did this so that the user would start typing on the line below the prompt. (personal asthetic taste)

## Typecasting the inputs

In order for us to do math on the numbers that the user typed, we need to convert them to numerical values, as you cannot do math on strings, for obvious reasons. (After all, what is "abc" / "def" anyways?) The method for doing so  is called Typecasting. and in Python, you can convert to float (decimal numbers less than 7 digits) by using the float() statement. This can be done for our purposes like so,
```py
floatnum1 = float(num1)
floatnum2 = float(num2)
```
> NOTE: We are not sanitizing our inputs, and entering in a non-numerical value here will break the code, and sanitizing inputs is really important, but a topic for a later time. For now, we will just hope that no one comes across this code with malicious intentions.

At this point, the code should look like this:
```py
num1 = input("Hello, What is your First Number?\n")
operation = input("Operation?\n")
num2 = input("Your Second Number?\n")

floatnum1 = float(num1)
floatnum2 = float(num2)
```

## Performing the math

Now that we have the numbers converted to float types, we are ready to do the math. For simplicity's sake in this lesson, we will use `if()` statements to tell what the user wants to do. In this program, we will support four operations, +,-,* and /, so we will need to have 4 if statements. One if statement for this program will look like, 
```py
if operation == "+":
  output=floatnum1+floatnum2
```
This checks to see if the user wanted to add the two numbers, and if they did, it adds them together.
> NOTE: Python is whitespace sensitive, so make sure you indent the second line with two spaces, or the if statement will not compile.

> NOTE: This code also does not sanitize the input for the operation, and if the user did not enter +,-,*, or /, the program will break at the next step, when we print the answer to the screen. Again, for the same reason, we will just hope that no one comes across this code with malicious intentions.

Repeat the following for the following three operations.


At this point, the code should look like this:
```py
num1 = input("Hello, What is your First Number?\n")
operation = input("Operation?\n")
num2 = input("Your Second Number?\n")

floatnum1 = float(num1)
floatnum2 = float(num2)

if operation == "+":
    output=floatnum1+floatnum2
if operation == "-":
    output=floatnum1-floatnum2
if operation == "*":
    output=floatnum1*floatnum2
if operation == "/":
    output=floatnum1/floatnum2

```

## Printing the result

Using the `print()` statement, we can print the result out to the screen. In Python, strings can be concatenated by "adding" them together, as if they were numbers. The code for this step looks like this: `print("Your Answer: "+str(output))`. This code prints the text "Your answer: " concatenated with the output, after it has been typecasted to a string. (You can't concatenate it while it is still formatted as a float)

At this point, the code should look like this:
```py
num1 = input("Hello, What is your First Number?\n")
operation = input("Operation?\n")
num2 = input("Your Second Number?\n")

floatnum1 = float(num1)
floatnum2 = float(num2)

if operation == "+":
    output=floatnum1+floatnum2
if operation == "-":
    output=floatnum1-floatnum2
if operation == "*":
    output=floatnum1*floatnum2
if operation == "/":
    output=floatnum1/floatnum2

print("Your Answer: "+str(output))
```


# Running the code

Running the code is as simple as opening `IDLE`, the official Python editor for Windows, Mac and Linux, opening your code file, and pressing `F5` on your keyboard, or going to the `Run\Run Module` menu item at the top of the window (Windows), or the top of the screen (Mac)

# Done!

Amazing! You have made a simple command line based calculator! If you understood all of the code in this lesson, and you have gotten the code to compile, please continue onto the advanced tutorial.
