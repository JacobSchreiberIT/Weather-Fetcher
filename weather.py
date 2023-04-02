from dotenv import load_dotenv
import requests
import os

#load enviroment variables, these variables are used to store sensitive data
load_dotenv()

#URL we want to reach and out API Key
Endpoint_url = "https://api.openweathermap.org/data/2.5/weather"
API_Key = os.getenv("API_KEY")

#Get user input
user_input = input("Enter a city name: ").lower()

#Create request url and send a get response
Request_url = f"{Endpoint_url}?q={user_input}&appid={API_Key}"
response = requests.get(Request_url)

#Check if response was successful and set variable data to data received
if response.status_code == 200:
    data = response.json()
    #(Kelvin − 273.15) × 9/5 + 32 = 80.33°F
    temp = round((data['main']['temp'] - 273.15) * 9/5 + 32)
    print(temp, "degrees fahrenheit")
else:
    print("An error occured")

