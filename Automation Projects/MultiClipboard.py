import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

#Function that saves data to json file
def save_data(filepath, data):

    #Create or override existing file
    with open(filepath, "w") as file:

        #Write python dictionary as json object to the file
        json.dump(data, file)

#Function that reads json file
def load_data(filepath):
    try:
        #open file for read
        with open(filepath, "r") as file:

            #load json file 
            data = json.load(file)

            #returned as python dictionary
            return data
    except:
        return {}

#Checking if command is exactly length one
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        
        #Prompt user for key
        key = input("Enter a key: ")

        #Store key into data dictionary with its associated value
        data[key] = clipboard.paste()

        #rewrite and save data into file
        save_data(SAVED_DATA,data)
        print("Data has been saved!")

    elif command == "load":
                
        #Prompt user for key
        key = input("Enter a key: ")

        #Checks if key is in data dictionary, if it is, copy to clipboard
        if key in data:
            clipboard.copy(data[key])
            print("Data has been copied to clipboard.")

        #If not in dictionary, print doesn't exist
        else:
            print("Key does not exist.")
    
    elif command == "list":
        print(data)
    else:
        print("Unknown Command")
else:
    print("Pass exactly one command")
