import requests
import math

api_key = 'cb7ec436183bf5b8086a9a43753cac12'

city = input('Enter your city name')

url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def round_to_2_sig(number):
    if number == 0:
        return 0
    else:
        order_of_magnitiude = math.floor(math.log10(abs(number)))
        scale = 10 ** (2 - order_of_magnitiude - 1) 
        return round(number * scale) / scale

if response.status_code == (200):
    data = response.json()
    temp = data['main']['temp']
    celsius_temp = kelvin_to_celsius(temp)
    rounded_temp = round_to_2_sig(celsius_temp)
    desc = data['weather'][0]['description']

    print(f'Temperature: {rounded_temp} Degree celsius')
    print(f'Description {desc}')

else:
    print('Error Fetching Weather data') 