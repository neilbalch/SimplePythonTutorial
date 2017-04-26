# Import 'math' Library
import math
import random
# Define Variables
output = 0
process1 = ""
processO = ""
process2 = ""
memStore = "EMPTY"
# Define Vars To Allow Program To Pass The Input Stage
operationD = False
process1D = False
process2D = False
need2 = True
skipOp = False

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

# While Loop
while(1):
    # Reset Variables
    operationD = False
    process1D = False
    process2D = False
    print("//////////////////////////////////////////////////////////////////////////")
    print("Type 'help' for a list of abilities")
    # Operation Input
    while(operationD == False):
        #print("Hello, What is your Operation (Operator)?")
        processO = input("Hello, What is your Operation (Operator)? ")
        # Is processO == to any of out constants or predefines?
        if processO == "help":
            abilitiesList()
            processO = ""
            skipOp = True
        elif processO == "pi":
            print(math.pi)
            processO = ""
            skipOp = True
        elif processO == "e":
            print(math.e)
            processO = ""
            skipOp = True
        elif processO == "tau":
            print(math.pi*2)
            processO = ""
            skipOp = True
        elif processO == "MR":
            print(str(memStore))
            processO = ""
            skipOp = True
        elif processO == "M-":
            memStore = "Empty"
            print("Memory Cleared")
            processO = ""
            skipOp = True
        elif processO == "M+":
            process2 = "0"
            operationD = True
            skipOp = True
        if processO=="rand":
            print(random.random())
            skipOp = True
        # Have We Given process1 a Valid Operator?
        elif processO == "+" or processO== "-" or processO== "*" or processO== "/" or processO== "^" or processO=="/-" or processO=="!" or processO=="Abs" or processO=="d/r" or processO=="r/d" or processO=="M+" or processO=="M-" or processO=="MR" or processO=="sin" or processO=="cos" or processO=="tan" or processO=="asin" or processO=="acos" or processO=="atan" or processO=="log10" or processO=="log" or processO=="randint":
            operationD = True    
        elif skipOp == True:
            processO = ""
        else:
            print("ERROR: Invalid Operator")
        # Do We Need A 2nd Input?
        if processO=="/-" or processO=="!" or processO=="Abs" or processO=="d/r" or processO=="r/d" or processO=="M+" or processO=="sin" or processO=="cos" or processO=="tan" or processO=="asin" or processO=="acos" or processO=="atan" or processO=="log10":
           need2 = False
        else:
            need2 = True
    # 1st Number Input
    while(process1D == False):
         #print("First Number?")
         process1 = input("First Number? ")
         try:
             float(process1)
         except ValueError:
             print("ERROR: Syn: Invalid Num")
         else:
             if processO == "asin" or processO == "acos":
                 if int(process1) > 1 or int(process1) < -1:
                     print("ERROR: Math: 'asin' and 'acos' commands only accept inputs in range -1 to +1")
                     process1D = False
                 else:
                     process1D = True
             else:
                 process1D = True
    # 2nd Number Input
    while(process2D == False):
        if need2 == False:
            process2 = "0"
            process2D = True
        else:
            #print("Second Number?")
            process2 = input("Second Number? ")
            try:
                float(process2)
            except ValueError:
                print("ERROR: Syn: Invalid Num")
            else:
                 process2D = True
    # x/0 Error
    if processO == "/" and process2 == "0":
        #Error
        print("ERROR: Math: Canot divide by 0!")
    else:
        # Typecasting
        intProcess1 = float(process1)
        # Check if to Typecast intProcess2
        if  need2 == True:
            intProcess2 = float(process2)
        # Strategic Processing
        if processO == "+":
            output=intProcess1+intProcess2
            print("Your Answer: "+str(output))
        if processO == "-":
            output=intProcess1-intProcess2
            print("Your Answer: "+str(output))
        if processO == "*":
            output=intProcess1*intProcess2
            print("Your Answer: "+str(output))
        if processO == "/":
            output=intProcess1/intProcess2
            print("Your Answer: "+str(output))
        if processO == "^":
            output=math.pow(intProcess1,intProcess2)
            print("Your Answer: "+str(output))
        if processO == "/-":
            output=math.sqrt(intProcess1)
            print("Your Answer: "+str(output))
        if processO == "!":
            output=math.factorial(intProcess1)
            print("Your Answer: "+str(output))
        if processO == "Abs":
            output=math.fabs(intProcess1)
            print("Your Answer: "+str(output))
        if processO=="d/r":
            output=math.radians(intProcess1)
            print("Your Answer: "+str(output))
        if processO=="r/d":
            output=math.degrees(intProcess1)
            print("Your Answer: "+str(output))
        if processO=="M+":
            memStore = process1
            print("Number Stored")
        if processO=="sin":
            output=math.sin(intProcess1)
            print("Your Answer: "+str(output))
        if processO=="cos":
            output=math.cos(intProcess1)
            print("Your Answer: "+str(output))
        if processO=="tan":
            output=math.tan(intProcess1)
            print("Your Answer: "+str(output))
        if processO=="asin":
            output=math.asin(intProcess1)
            print("Your Answer: "+str(output))
        if processO=="acos":
            output=math.acos(intProcess1)
            print("Your Answer: "+str(output))
        if processO=="atan":
            output=math.atan(intProcess1)
            print("Your Answer: "+str(output))
        if processO=="log10":
            output=math.log10(intProcess1)
            print("Your Answer: "+str(output))
        if processO=="log":
            output=math.log(intProcess2, intProcess1)
            print("Your Answer: "+str(output))
        if processO=="randint":
            output=random.randint(intProcess1, intProcess2)
            print("Your Answer: "+str(output))
