import random

#Invalid Input
def invalid():
    deaths = ["A knife appears from the dark and zips through your heart. You have died!", "You have stepped on a pressure plate and have blown up. You have died!", "A stalagmite has fallen and pierced your skull. You have died!", 
              "A stepped on a trapdoor and have been spiked. You have died!", "You got lost and ran out of water as well as food. You have died"]
    random_number = random.randint(0,4)
    death = deaths[random_number]
    print(death)
    quitGame()

#Room 1: User chose "open (no key)"
def gameRoom1():
    user_input = input("You walk up to the door and try to open it but it is locked. Do you wish to explore further down the cave or go back? (further/back) ").lower()
    if user_input == "back":
        gameRoom3()
    elif user_input == "further":
        gameRoom4()
    else:
        invalid()

#Room 2: User chose "further (from cross)"
def gameRoom2():
    user_input = input("You make your way further and further into the cave but you are running low on resources. Luckily you found an alternate exit. Do you wish to continue or exit? (continue/exit) ").lower()
    if user_input == "continue":
        print("You start to walk amongst the edge but slip and fall to your death!")
        quitGame()
    elif user_input == "exit":
        print("You safely exit the cave!")
        quitGame()
    else:
        invalid()

#Room 3: User chose "left"
def gameRoom3():
    user_input = input("You traverse deeper into the darkness and stumble upon a waterfall and a wobbly bridge. Do you want to cross or go back? (cross/back) ").lower()
    if user_input == "cross":
        gameRoom5()
    elif user_input == "back":
        gameRoom8()
    else:
        invalid()

#Room 4: User chose "further (after door)"
def gameRoom4():
    user_input = input("You have found a sacred sword and an exit! While running low on resources, do you wish to continue or exit? (continue/exit) ").lower()
    if user_input == "continue":
        print("You stumble upon an open area and are swarmed by monsters. You died trying to fight them off.")
        quitGame()
    elif user_input == "exit":
        print("As you take the sword monsters begin to spawn but you manage to escape with your life.")
        quitGame()
    else:
        invalid()

#Room 5: User chose "cross"
def gameRoom5():
    user_input = input("You steadily make your way across the bridge! Do you wish to go further down the path or go back? (further/back) ").lower()
    if user_input == "further":
        gameRoom2()
    elif user_input == "back":
        gameRoom3()
    else:
        invalid()

#Room 6: User chose "open (with key)"
def gameRoom6():
    user_input = input("You open the door and are met with a huge treasure. Do you dare steal some or go back? (steal/back) ").lower()
    if user_input == "steal":
        print("The statue in front of you looks down upon you. Its eyes glow red and lasers obliterate you into pieces.")
        quitGame()
    elif user_input == "back":
        gameRoom7()
    else:
        invalid()

#Room 7: User chose "right (start)"/ "right (from 8)"/"back"
def gameRoom7():
    key = random.randint(0,1)
    user_input = input("You make your way down further into the darkness and you are greeted with a large door. Do you wish to open the door or go further? (open/further) ").lower()
    if user_input == "open" and key == 0:
        gameRoom1()
    elif user_input == "open" and key == 1:
        print("You have found the key as you were walking towards the door!")
        gameRoom6()
    elif user_input == "further":
        gameRoom4()
    else:
        invalid()

#Room 8: User chose "right"/"back"
def gameRoom8():
    user_input = input("You return to the cavern. Do you wish to traverse the right or exit? (right/exit) ").lower()
    if user_input == "right":
        gameRoom7()
    elif user_input == "exit":
        quitGame()
    else:
        invalid()

#Starting room
def gameStartRoom():
    user_input = input("You enter a dark cavern and find two paths, which do you decide to take? (left/right) ").lower()
    if user_input == "left":
        gameRoom3()
    elif user_input == "right":
        gameRoom7()
    else:
        invalid()

#Start Game
def game():
    name = input("Type your name: ")
    print("Welcome", name, "to this adventure!")
    gameStartRoom()

#QuitGame 
def quitGame():
    print("Thanks for playing!")
    user_input = input("Would you like to play again? (y/n) ")
    if user_input == "y":
        game()
    if user_input == "n":
        quit()

#Start game
game()