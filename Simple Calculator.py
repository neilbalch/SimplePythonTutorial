output = 0
process1 = ""
processO = ""
process2 = ""
print("Hello, What is your First Number?")
process1 = input()
print("Operation?")
processO = input()
print("Your Second Number?")
process2 = input()
print("Processing...")

intProcess1 = int(process1)
intProcess2 = int(process2)

if processO == "+":
    output=intProcess1+intProcess2
if processO == "-":
    output=intProcess1-intProcess2
if processO == "*":
    output=intProcess1*intProcess2
if processO == "/":
    output=intProcess1/intProcess2

print("Your Answer: "+str(output))
