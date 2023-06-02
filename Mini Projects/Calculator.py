#Quit function
def quit():
    return

#Invalid input function
def invalid():
    print()
    print("--------------------------------------")
    print("Please input a valid option next time!")
    print("--------------------------------------")
    print()

#Main Calculator Function
def calc():
    while True:
        #Prompt user for options
        print("Which option would you like to select (A,B,C,D)? or press Q to quit. ")
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiplication")
        print("D. Division")
        user_input = input().upper()

        #Selecting choices
        if user_input == "A":
            print("Note: Numbers will be added in the order you type them!")

            #Prompt user and convert string into integer: if not valid input, prompt invalid msg and prompt again
            try:
                num1 = int(input("Please enter the first number: "))
            except:
                invalid()
                continue
            try:
                num2 = int(input("Please enter the second number: "))
            except:
                invalid()
                continue

            #Call Addition Function
            add(num1, num2)

        elif user_input == "B":
            print("Note: Both options will be displayed!")
            
            #Prompt user and convert string into integer: if not valid input, prompt invalid msg and prompt again
            try:
                num1 = int(input("Please enter the first number: "))
            except:
                invalid()
                continue
            try:
                num2 = int(input("Please enter the second number: "))
            except:
                invalid()
                continue

            #Call Subtract Function
            sub(num1, num2)

        elif user_input == "C":
            
            #Prompt user and convert string into integer: if not valid input, prompt invalid msg and prompt again
            try:
                num1 = int(input("Please enter the first number: "))
            except:
                invalid()
                continue
            try:
                num2 = int(input("Please enter the second number: "))
            except:
                invalid()
                continue

            #Call Multiplication Function
            mult(num1, num2)

        elif user_input == "D":
            print("Note: Both options will be displayed!")
            
            #Prompt user and convert string into integer: if not valid input, prompt invalid msg and prompt again
            try:
                num1 = int(input("Please enter the first number: "))
            except:
                invalid()
                continue
            try:
                num2 = int(input("Please enter the second number: "))
            except:
                invalid()
                continue
            
            #Call Division Function
            div(num1, num2)
            
        elif user_input == "Q":
            break
        else:
            invalid()
            continue

#Function to ask if user wants to input another calculation
def again():
    user_input = input("Would you like to perform another calculation? (y/n) ").lower()
    if user_input == "y":
        print()
        calc()
    elif user_input == "n":
        return
    else:
        print("Invalid input")
        again()

#Function for addition
def add(x, y):
    ans = x + y
    print(x, "+", y, "=", ans)
    again()

#Function for subtraction
def sub(x,y):
    ans1 = x - y
    ans2 = y - x
    print("A. ", x, "-", y, "=", ans1)
    print("B. ", y, "-", x, "=", ans2)
    again()

#Function for multiplication
def mult(x,y):
    #Prompt user for option
    print("Which option would you like to select? (A/B)")
    print("A. Normal (x*y)")
    print("B. Powers (x^y)")
    user_input = input().upper()

    #Check options
    if user_input == "A":
        ans = x * y
        print(x, "*", y, "=", ans)
        again() 
    elif user_input == "B":
        pow(x,y)
    elif user_input == "Q":
        quit()
    else:
        print("Invalid option")
        mult(x,y)

#Function for division
def div(x,y):
    if y != 0 and x != 0:
        ans1 = x/y
        ans2 = y/x
        print("A.", x, "/", y, "=", ans1)
        print("B.", y, "/", x, "=", ans2)
        again()
    
    elif x == 0:
        ans1 = x/y
        print("A.", x, "/", y, "=", ans1)
        print("B. Cannot divide by 0!")
        again()
    
    else:
        ans1 = y/x
        print("A.", y, "/", x, "=", ans1)
        print("B. Cannot divide by 0!")
        again()

#Function for powers
def pow(x,y):
    ans1 = x**y
    ans2 = y**x
    print("A.", x, "^", y, "=", ans1)
    print("B.", y, "^", x, "=", ans2)
    again()

#Welcome user
name = input("Please enter your name: ").upper()
print()
print("--------------------------------------------")
print("| HELLO, WELCOME", name, "TO YOUR CALCULATOR |")
print("--------------------------------------------")
print()

#Call calculator
calc()

#Goodbye Message
print()
print("-----------------------")
print("|       GOODBYE!      |")
print("-----------------------")
print()