import os
import time


print('#'*30)
print('Calculator: Created by: Demar')
print('#'*30)


def add(x,b):
    try:
        return f'{x} + {b} = {x + b}'
    except:
        pass
    return 'error'

def sub(x,b):
    try:
        return f'{x} - {b} = {x - b}'
    except:
        pass
    return 'error'

def divide(x,b):
    try:
        return f'{x} / {b} = {x / b}'
    except:
        pass
    return 'error'

def multi(x,b):
    try:
        return f'{x} * {b} = {x * b}'
    except:
        pass
    return 'error'

def menu():
    global choice 
    choice = input('[A]dd, [S]ubtract, [D]ivide, [M]ultiply, [C]lear_Screen, [R]eturn to main menu, [Q] to exit: ').lower()
    try:
        choice = str(choice)
    except:
        print(f'you entered {choice}')
    return True


def clear_screen():
    os.system('cls')




def calculate():
    global num1, num2
    clear = input(('Clear screen? [Y] or [N]: '))

    try:
        clear = str(clear)
        if clear.lower() == 'y' or clear.lower() == 'yes':
            clear_screen()
        else:
            pass
    except:
        pass
    menu()
    while True:
    
        if choice.lower() in ['a', 'add']:
            print('#'*20)
            print('ADDITION')
            print('#'*20)

            num1 = (input('enter number: '))
            if num1.lower() == 'q':
                print('Thanks for using me')
                time.sleep(1)
                exit()

            if num1.lower() in ['r', 'return']:
                menu()
                continue
            num2 = (input('enter second number: '))
            if num2.lower() == 'q':
               print('Thanks for using me')
               time.sleep(1)
               exit()

            if num2.lower() in ['r', 'return']:
                menu()
                continue

            try:
                num1 = int(num1)
                num2 = int(num2)
            except:
                
                print('error')
                continue
            print(add(num1,num2))

        if choice.lower() in ['s','sub']:
            print('#'*20)
            print('SUBTRACT')
            print('#'*20)

            num1 = (input('enter number: '))
            if num1.lower() == 'q':
                print('Thanks for using me')
                time.sleep(1)
                exit()
            
            if num1.lower() in ['r', 'return']:
                menu()
                continue

            num2 = (input('enter second number: '))
            if num2.lower() == 'q':
                print('Thanks for using me')
                time.sleep(1)
                exit()

            if num2.lower() in ['r', 'return']:
                menu()
                continue

            try:
                num1 = int(num1)
                num2 = int(num2)
            except:
                print('error')
            print(sub(num1,num2))
        
        if choice.lower() in ['d','div', 'divide']:
            print('#'*20)
            print('DIVIDE')
            print('#'*20)

            num1 = (input('enter number: '))
            if num1.lower() == 'q':
                print('Thanks for using me')
                time.sleep(1)
                exit()

            if num1.lower() in ['r', 'return']:
                menu()
                continue

            num2 = (input('enter second number: '))

            if num2.lower() == 'q':
                print('Thanks for using me')
                time.sleep(1)
                exit()

            if num2.lower() in ['r', 'return']:
                menu()
                continue
            try:
                num1 = int(num1)
                num2 = int(num2)
            except:
                print('error')
            print(divide(num1,num2))

        
        if choice.lower() in ['m', 'mul', 'multiply']:
            print('#'*20)
            print('MULTIPLY')
            print('#'*20)

            num1 = (input('enter number: '))
            if num1.lower() == 'q':
                print('Thanks for using me')
                time.sleep(1)
                exit()
            
            if num1.lower() in ['r', 'return']:
                menu()
                continue
            
            num2 = (input('enter second number: '))
            if num2.lower() == 'q':
                print('Thanks for using me')
                time.sleep(1)
                exit()
            
            if num2.lower() in ['r', 'return']:
                menu()
                continue
            try:
                num1 = int(num1)
                num2 = int(num2)
            except:
                pass
            print(multi(num1,num2))
        
        if choice.lower() in ['q', 'exit', 'quit']:
            print('Thanks for using me')
            time.sleep(1)
            exit()
        
        if choice.lower() in ['c', 'clear']:
            clear_screen()
            menu()
            continue
        
        if (choice.lower() not in ['a', 'add'] or choice.lower() not in ['s', 'sub'] or choice.lower() not in ['d', 'divide'] or choice.lower() not in ['m','multiply'] or choice.lower() not in ['r','return'] or choice.lower() not in ['q', 'exit', 'quit']):
            menu()
        


if __name__ == "__main__":
    try:
        calculate()
    except KeyboardInterrupt:
        print('You pressed CTRL C\n')
        print('EXITING....')
        time.sleep(1)
