import requests
"""
Orirignal code provided by MicroSoft via Coursera as part of the Python Web Development coursework.

Running the app with a valid API Key and city, will return the current temperature in Kelvin (with F/C conversions) and simple text
description of the weather type (Clear/Sunny/Partial Clouds/etc...)

The original script and API only provided the Kelvin and weather description,
I've added the conversions for both (F)ahrenheit and (C)elcius
"""
# Assumed to be using Open Weather Map

api_key = 'API_Key' #placeholder
city = 'City Name' #placeholder

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code ==200:
    data = response.json()
    temperature_k = data['main']['temp']
    temperature_f = round(((data['main']['temp'])-273.15)*9/5+32, 2)
    temperature_c = round((temperature_f-32)*5/9, 2)
    description = data['weather'][0]['description']

    print(f'The temprature in {city} is {temperature_k} Kelvin ({temperature_f}F/{temperature_c}C) with {description}.')
else:
    print('An error occurred while retrieving weather data for your city.')