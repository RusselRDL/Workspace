import requests

#Need to create an acc on openweathermap.org and use own your own key
API_KEY = "b0f1514bec003b24577ebd34cc6af7d1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#Prompt user to input city name
city = input("Enter a city name: ")

#f string allows you to embed variables and expressions within a string
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

#Get request to url to then give response associated with the city
response = requests.get(request_url)

#200: successful
if response.status_code == 200:

    #gives json data as python dictionary
    data = response.json()

    #Weather gives a list so access decription via accessing first element then description
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"],2)
    
    #Prints weather
    print("Weather:", weather)
    print("Temperature:", temperature, "Celsius")

#Prints error msg if unsuccessful
else:
    print("An error has occurred.")