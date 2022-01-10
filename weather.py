import requests
import os
from datetime import datetime

user_api = os.environ["current_weather_data"]
location = input("Enter City Name:")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+ location + "&appid="+ user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print ("Invalid City: {}, Please Check the City Name ".format(location))
else: 

    temp_city = ((api_data['main']['temp']) - 273.15)
    temp_feel = ((api_data['main']['feels_like']) - 273.15)
    min_temp = ((api_data['main']['temp_min']) - 273.15)
    max_temp = ((api_data['main']['temp_max']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    wind_sp = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print()
    print('**************** CURRENT WEATHER CONDITION ****************')
    print()
    print('-----------------------------------------------------------')
    print('City : {} || {}'.format(location.upper(), date_time))
    print('-----------------------------------------------------------')

    print("Current Temperature: {:.2f}C".format(temp_city))
    print("Feels Like:          {:.2f}C".format(temp_feel))
    print("Maximum Temperature: {:.2f}C".format(max_temp))
    print("Minimum Temperature: {:.2f}C".format(min_temp))
    print("Current Weather:    ", weather_desc)
    print("Current Humidity:   ", humidity,"%")
    print("Current Wind Speed: ", wind_sp,'kmph')