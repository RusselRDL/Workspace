import random

#Initialize scores
user_score = 0
comp_score = 0
tied_score = 0

#Create list of options user can choose from
options = ["rock", "paper", "scissors"]

while True:

    #Ask for user input
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    #If user types something not in options, reprompt msg
    if user_input not in options:
        continue

    #Use index to signify computer choice
    # rock: 0, paper: 1, scissors: 2
    random_number = random.randint(0,2)

    #Computer chooses
    comp_pick = options[random_number]
    print("Computer chose", comp_pick + ".")

    #Check win conditions and ties
    if user_input == "rock" and comp_pick == "scissors":
        print("You won!")
        user_score += 1

    elif user_input == "paper" and comp_pick == "rock":
        print("You won!")
        user_score += 1

    elif user_input == "scissors" and comp_pick == "paper":
        print("You won!")
        user_score += 1

    elif (user_input == "rock" and comp_pick == "rock") or (user_input == "scissors" and comp_pick == "scissors") or (user_input == "paper" and comp_pick == "paper"):
        print("You tied!")
        tied_score += 1

    #Losing case
    else:
        print("You lost!")
        comp_score += 1

#Print results
if user_score == 1:
    print("You won", user_score, "time.")
else:
    print("You won", user_score, "times.")

if comp_score == 1:
    print("The computer won", comp_score, "time.")
else:
    print("The computer won", comp_score, "times.")

if tied_score == 1:
    print("You tied", tied_score, "time.")
else:
    print("You tied", tied_score, "times.")

#Goodbye msg
print("Thanks for playing!")