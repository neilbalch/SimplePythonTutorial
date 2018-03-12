# Advanced Calculator

I strongly reccomend you got through the tutorial for the [Simple Calculator](https://github.com/neilbalch/Python-Tutorial-Calculator/blob/master/Simple%20Calculator%20Tutorial.md) first, before you look at this, as it covers important important details of python such as whitespace and strongly typed variables.

## Goals

* This calculator is more advanced in that it includes some operations that require only one numberical input, like log and square root, as well as recalling constants, like pi and such that do not require any numerical input whatsoever. The program we build will have to deal with this, without crashing or bein vumbersome to use.
* The aim is to get this calculator to support the following functions: `+,-,*,/,/-,^,!,abs,sin,cos,tan,asin,acos,atan,log10,log,rand,randint,pi,e,tau,M+,M-,MR,degrees->radians,radians->degrees`
* The simple calculator program ended once the operation was completed, something we also want to avoid with this calculator.
* Since it has a long list of functions, we also want to be able to list out all of the things the calculator can do.
* We want to sanitize our inputs so that we will not get screwed up by malicious or otherwiwe malformed inputs

## Sanitizing numerical inputs

Because of its nature, we will not sanitize our operation input the same way as our numerical inputs; we have a list of operations that we support, and if the input doesn't match one on the list, we won't let them proceed, instead asking them to try again. Because we will be using the code for sanitizing numerical inputs multiple times, one for each of the two inputs, we will break it our into a function. Functions are used whenever code will be reused, as it speeds up bug detection and prevention as well as makes your code more readable to other people. (and you when you inevitably come back to your own code a few years later and have no idea what your code does anymore!)

Basic functions can be declared like so, `def myFunction([parameters]):`. Our function for taking input will be called "askForNumInput". Note the camel casing in the name.

> NOTE: Camel casing is the common practice of making the first letter of an object or function name lowercase and then making every subsequent first letter of a word uppercase, i.e. "askForNumInput" or "abilitiesList"

As before in the Simple Calculator, we will still use the same basic method for taking input, but instead of a constant string for the prompt, we will replace that with a variable set as a parameter in the function.

Inside this function, we will use a new statement, the `try` block. It serves the purpose of helping catch errors that would otherwise have caused the program to crash. It has three parts, `try`, `catch` and `else`. The `try` block contains the code you want to test run, the `catch` block takes a parameter, the error you are testing for and contains wat you want to do if the error ocurs, and the `else` block contains what you want to do if there is no error.

As in the Simple Calculator, we will need to have the input typecasted to `float` for our math operations, and if you put in a non numerical value, the program will crash with a `ValueError: could not convert string to float`. We want to avoid that error, so with our try block, we will catch the error `ValueError`. If we catch the ValueError, we want to tell the user that their input was invalid, and if there was no error, we want to actually typecast the input. So, our finished function should look like this:

```py
def askForNumInput(textPrompt):
    # Devine local variable
    convertedNum = math.nan

    # Wait for valid numerical input 
    while True:
        num = input(textPrompt)
        try:
            # Try to typecast the input to a float
            float(num)
        except ValueError:
            # Catch the exception if it is not a number
            print("ERROR: Syn: Invalid Num")
        else:
            # Typecasting
            convertedNum = float(num)
            break
    return convertedNum
```

## abilitiesList

Because our program will support a miryad different operations, we want the user to be able to recall a list of the operations we support. For the sake of neatness in the main block of code, we will break this out into a function. This one will be simple, it takes no parameters, as it is just a function with a bunch of print statements. The code for this should look like so:

```py
# Define Function Listing Function
def abilitiesList():
    print("+...Addition")
    print("-...Subtraction")
    print("*...Multiplication")
    print("/...Division")
    print("^...Powers")
    print("/-...Square Roots ")
    print("!...Factorials (Input Cannot Be Negetave)")
    print("Abs...Absolute Value")
    print("d/r...Degrees To Radians")
    print("r/d...Radians To Degrees")
    print("pi...Returns PI")
    print("e...Returs 'e'")
    print("tau...Returns TAU (2xPI)")
    print("M+...Save input to memory")
    print("MR...Recall Memory")
    print("M-...Clear Memory")
    print("sin...Sine")
    print("cos...Cosine")
    print("tan...Tangent")
    print("asin...Arc Sine")
    print("acos...Arc Cosine")
    print("atan...Arc Tangent")
    print("log10...Log(10) of Input")
    print("log...Returns The Apropriate Log of the Input (input1 is the log power)")
    print("rand...Returns A Random Number Between 0 and 1")
    print("randint...Returns A Random Number Between The Two Inputs")
    print("//////////////////////////////////////////////////////////////////////////")
```

## The whole shebang

Since we want this program to loop indefinetly, letting the user perform as many operations as they want before they clode the program, we will utilize an infinite loop. This can be done with a `while` loop configured as such: `while True:`. This line runs the code in the code within the loop for as long as `True` is equal to `True`, or more succinctly, while 1=1, which will always be correct, hence the name infinite loop.

At the beginning of the loop, we want to let the user know that they can request a list of the operations we can perform. We will write the code to call `abilitiesList()` later.

```py
print("//////////////////////////////////////////////////////////////////////////")
print("Type 'help' for a list of abilities")
```

Next, we will have three loops to get the operation and numerical inputs for the calculations. They are loops because we want to loop until we have a valid input for each. 

### Operation input

For the operation input loop, we will first see if the input is one of the commands that doesn't require any numerical inputs, like i.e. recalling pi or storing a value in the calculator's "memory", and if it isn't, then we will check to see if it is one of the operations we support that requires numerical input, i.e. +,-,sqrt, etc. Because we support recalling numerical constants and generating randon numbers, we need to import the libraries that allow us to use those commands. At the top of the file, add the following lines:

```py
# Import 'math' and 'random' Libraries
import math
import random
```

We will call the `abilitesList` function like so: `abilitiesList()`. The 'memory' for the calculator will be implimented using the variable `memStore` that the user can store a value into using `M+`, recall a value from using `MR` and delete the contents of using `M-`. The `memStore` variable will be defined at the top of the file so that its scope includes the entire file, following convention, below the `import` statements. If the user inputs an operation that requires numerical input(s), we will break from the loop using the command `break`, which breaks away from the current loopm in this case the `while True:`. The finished operation loop should look like this:

```py
# Loop for getting operation
    while True:
        operator = input("What operation do you want to perform? ")
        # Is operator == to any of out constants or predefines?
        if operator == "help":
            abilitiesList()
        elif operator == "pi":
            print(math.pi)
        elif operator == "e":
            print(math.e)
        elif operator == "tau":
            print(math.pi*2)
        elif operator == "MR":
            print(str(memStore))
        elif operator == "M-":
            memStore = "Empty"
            print("Memory Cleared")
        elif operator == "rand":
            print(random.random())
        # Has the user entered in a valid operator?
        elif operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "^" or operator == "/-" or operator == "!" or operator == "Abs" or operator == "d/r" or operator == "r/d" or operator == "M+" or operator == "M-" or operator == "MR" or operator == "sin" or operator == "cos" or operator == "tan" or operator == "asin" or operator == "acos" or operator == "atan" or operator == "log10" or operator == "log" or operator == "randint":
            break
        else:
            print("ERROR: Invalid Operator")
```

If the user inputs an operation that is one of the ones we can perform without taking input, we will print the corresponding answer, and loop back to asking for another operation.

### First numerical input

Luckily, because we wrote the `askForNumInput(textPrompt)` function before, the code required to take input for the next two numerical inputs is a lot easier. We still need to have loops, because we still need to sanitize our inputs. Inside the loop, instead of calling the `input()` command ourselves, we will call `askForNumInput()`, which takes care of making sure the value is numerical for us, leaving us just to making sure the value is within the range of acceptable values for each operation. 

Luckily, the only operations that require this level of finesse are `asin`, `acos` and `!` (Factorial), as the first two functions provided by the `math` library only accept balues that are between 1 and -1, and factorial inputs have to be above 0. Since we need to check two conditions, that the requested operation is `asin` or `acos` AND that the values are within -1 and 1, we will use a compound condition. We could just make two nested if statements, jone for each of the conditions, but python allows us to make better and more concise code. The same can be done with the `!` test.

Using the `and` keyword, we can combine the two conditions so that only if the first condition AND the second condition are both true we will proceed to tell the usr that there is an error. The `or` keyword works similarly, but instead of both conditions needing to be true for the entire compound condition to be true, only one needs to. Because we have four nested conditions here, between each of the sets, (around the `or`s) we need to have parentheses to tell the comiler what to evaluate first. (Very similar to how they work in PEMDAS for math!) Otherwise, if the values are kosher, we will break from the loop. The finished code for the first input should look like this:

```py
# Loop for 1st number input
while True:
    num1 = askForNumInput("First Number? ")
    # Catch asin and acos out of bounds error case
    if (operator == "asin" or operator == "acos") and (num1 > 1 or num1 < -1):
        print("ERROR: Math: 'asin' and 'acos' commands only accept inputs in range -1 to +1")
    elif operator == "!" and num1 < 0:
        print("ERROR: Math: Factorials only accept inputs > 0")
    else:
        break
```

### Second numerical input

The code for this input is extreemely simimar to the previous one. Just like the first input, we need to take input from the user using `askForumInput(textPrompt)` and check for if an error will surface with the given inputs. (this time for checking for divide by 0) But unlike the first input, where if you have gotten to to that point in the program, you automatically need a numerical input, some operations only require one numerical input, and not two, i.e. sqrt, factorial, abs, etc. So, instead of directly going to the loop, we need to check if the operation is one of the ones that only requires one numerical input. To do so, we will use another keyword, `not`. `not` inverts the boolean result from a condition, so for example, `not True` will never be true because the inverse of true is always false. Just like the condition for the first numerical input, parentheses are required around the condition to make sure that `not` modifies the correct part of the condition. The finished code for the second numerical input should look like this:

```py
# Does the operation require a 2nd input?
if not (operator=="/-" or operator=="!" or operator=="Abs" or operator=="d/r" or operator=="r/d" or operator=="M+" or operator=="sin" or operator=="cos" or operator=="tan" or operator=="asin" or operator=="acos" or operator=="atan" or operator=="log10"):
    # Loop for 2nd number input
    while True:
        num2 = askForNumInput("Second Number? ")
        # Catch x/0 error case
        if  operator == "/" and num2 == "0":
            print("ERROR: Math: Canot divide by 0!")
        else:
            break
```

### Da calculations

Now that we have all of the input we need for the selected operation, we need to actually perform the operation and print the result ot the screen. In other languages, there is a control structure called a `switch` that evaluates the condition for each `case`, each of which has its own condition that will make the code within the case run if the case condition matches the value of the switch condition. But, unfortunately, python doesn't support the `switch`, so we will need to use `if` statements instead, a more tedious and slightly less elegant solution, but it still works, and that's what matters most.

For each of the operations we listed in `abilitiesList()` that was not one that didn't need inputs, we will need to make a new `if` statements. For simple operations, i.e. +,-,* and /, this is as simple as copying the code from the Simple Calculator, (changing the input variable names to match, and making  the `print` statements for the output of course!) but for the more complex operations, like sqrt, sin,cos,tan,etc., we will need to call on the `math` and `random` libraries for help. In general, the python docs link for the [math library](https://docs.python.org/3.5/library/math.html) and the [random library](https://docs.python.org/3.5/library/random.html) will help you out with finding out what function to call for each operation we need to support and which numerical input to put where. 

> NOTE: I strongly encourage you to puzzle through this yourself, as learning how to read library documentation is an extremely valueable resource for any programmer. 

For the command `M+`, you will need to store the numerical value the user inputed to the variable `memStore`. The finished code for this section should look like this:

```py
# Calculations
if operator == "+":
    output = num1 + num2
    print("Your Answer: "+str(output))
elif operator == "-":
    output = num1 - num2
    print("Your Answer: "+str(output))
elif operator == "*":
    output = num1 * num2
    print("Your Answer: "+str(output))
elif operator == "/":
    output = num1 / num2
    print("Your Answer: "+str(output))
elif operator == "^":
    output = math.pow(num1,num2)
    print("Your Answer: "+str(output))
elif operator == "/-":
    output = math.sqrt(num1)
    print("Your Answer: "+str(output))
elif operator == "!":
    output = math.factorial(num1)
    print("Your Answer: "+str(output))
elif operator == "Abs":
    output = math.fabs(num1)
    print("Your Answer: "+str(output))
elif operator == "d/r":
    output = math.radians(num1)
    print("Your Answer: "+str(output))
elif operator == "r/d":
    output = math.degrees(num1)
    print("Your Answer: "+str(output))
elif operator == "M+":
    memStore = num1
    print("Number Stored")
elif operator == "sin":
    output = math.sin(num1)
    print("Your Answer: "+str(output))
elif operator == "cos":
    output = math.cos(num1)
    print("Your Answer: "+str(output))
elif operator == "tan":
    output = math.tan(num1)
    print("Your Answer: "+str(output))
elif operator == "asin":
    output = math.asin(num1)
    print("Your Answer: "+str(output))
elif operator == "acos":
    output = math.acos(num1)
    print("Your Answer: "+str(output))
elif operator == "atan":
    output = math.atan(num1)
    print("Your Answer: "+str(output))
elif operator == "log10":
    output = math.log10(num1)
    print("Your Answer: "+str(output))
elif operator == "log":
    output = math.log(num2, num1)
    print("Your Answer: "+str(output))
elif operator == "randint":
    output = random.randint(num1, num2)
    print("Your Answer: "+str(output))
```

# Voila!

Congratulations, you are done! Feel good about yourself if you understood this tutorial, but if you didn't, please let me know, and or read it through again and do research on your questions online. I look forward to seeing you all on the interwebs as full on programmers!
