import requests

from pprint import pprint

API_Key = '5c57d9811b8682571466556a2fa6d908'

city = input ('Insira a cidade: ')

base_url = 'https://api.openweathermap.org/data/2.5/weather?q'+city+'appid='API_Key

weather_data = requests.get(base_url).json()

pprint(weather_data)