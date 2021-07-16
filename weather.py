import requests
woeid = 1132599
url = f'https://www.metaweather.com/api/location/{woeid}/'
response = requests.get(url).json()

pro = response['consolidated_weather'][2]['weather_state_name']
print(pro)