print("Welcome to my Quiz!")

play = input("Would you like to play? ")

#Use .lower() in order to convert answers to lowercase --> dont have to check for casing
if play.lower() != "yes":
    quit()

#Set score to 0
score = 0

#Ask question, check if answer is correct, print result and increment score if correct
answer = input("What is my age? ")
if answer == "19":
    print("Correct!")
    score +=1
else:
    print("incorrect!")

answer = input("What is my favorite color? ")
if answer.lower() == "blue":
    print("Correct!")
    score +=1
else:
    print("incorrect!")

answer = input("What is my favorite hobby? ")
if answer.lower() == "video games":
    print("Correct!")
    score +=1
else:
    print("incorrect!")

answer = input("what is my favorite game? ")
if answer.lower() == "osu!":
    print("Correct!")
    score +=1
else:
    print("incorrect!")

print("You got", str((score/4) * 100) + "%.")
#Convert score to string to print to screen
print("You got", score, "questions correct!")