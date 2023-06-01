from cryptography.fernet import Fernet

'''
#Function to generate a key for encryption purposes
#Note: run this function once to create "key.key" then can comment out
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

#Function that returns the key in order to view passwords
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

#Encryption initialization
key = load_key()
fer = Fernet(key)

#Function to view passwords
def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():

            #rstrip removes \n from the line so it doesn't read
            data = line.rstrip()

            #split takes a string, looks for "|" and split the string into different items every time "|" is found
            user, passw = data.split("|")

            #encode: turns string into bytes | decode: takes bytes string and turns it back to normal string
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

#Function to add password
def add():
    username = input("Username: ")
    pwd = input("Password: ")

    #create file or add to already existing file
    #W: create and write file, overrides if already exists, r: read file, a: add to end of file and create if doesnt exist
    with open('passwords.txt', 'a') as file:

        #encode: turns string into bytes | decode: takes bytes string and turns it back to normal string
        file.write(username + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


#Prompt user
while True:
    mode = input("Which mode would you like to select (add/view)? Press q if you would like to quit. ").lower()
    
    #Check for inputs
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue