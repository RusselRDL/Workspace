import random

#Ask for user input (for top of range)
top = input("Type a number: ")

#Check if digit is inputed and convert string to integer
if top.isdigit():
    top = int (top)

    #If not valid, quit
    if top <= 0:
        print("Please enter a number greater than 0")
        quit()

#If input isnt a digit, quit
else:
    print("Please enter a number next time")
    quit()

#Generate random number from 0 to inputed number by user
random_number = random.randint(0, top)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Make a guess: ")

    #Check if digit is inputed and convert string to integer
    if user_guess.isdigit():
        user_guess = int (user_guess)
    else:
        print("Please enter a number")
        continue
    
    #If user guesses right, print correct
    if user_guess == random_number:
        print("You are correct!")
        break

    #If guess is above number, print above, if below, print below
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

#Print results
print("You got it in", guesses, "guesses")
