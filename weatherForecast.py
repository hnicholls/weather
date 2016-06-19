
#!/usr/bin/env python3
# weatherForecast.py - prints the 5 day/3hr weather forecast for a location supplied via the command line
# uses openWeatherMap API - see http://openweathermap.org/current for API details
# run as: weatherForecast.py Christchurch, NZ

import json, requests, sys, pprint, os

# extract location from the command line arguments
if len(sys.argv) <2:
    print('Location missing. Usage: weatherForecast.py location  E.g. weatherForecast.py Christchurch, NZ')
    sys.exit(1)
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org via API
# The response from the URL is held in member variable response.text
# API parameter cnt=n restricts results to n forecasts; n <= 40
API_KEY =  os.environ['OPEN_WEATHER_MAP_API_KEY']
url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&units=metric&cnt=40&APPID=%s' % (location, API_KEY)

response = requests.get(url)
response.raise_for_status()
# Load JSON string data into a Python dictionary named weatherData
weatherData = json.loads(response.text)
# print('Here is the raw data returned from openweathermap.org for ' + location + ':')
# pprint.pprint(weatherData)

for threeHourForecast in range(len(weatherData['list'])):
    forecast = weatherData['list'][threeHourForecast]
    simpleForecast = {'dateRaw':       forecast['dt'], \
                      'dateText':      forecast['dt_txt'], \
                      'cloudCover':    forecast['clouds']['all'], \
                      'humidity':      forecast['main']['humidity'], \
                      'pressure':      forecast['main']['pressure'], \
                      'temperature':   forecast['main']['temp'], \
# TODO Fix if no rain, the key "3h" is missing i.e. "rain":{}, requires some code to fix so commented out for now
#                      'rainfall':      forecast['rain']['3h'], \
                      'windDirection': forecast['wind']['deg'], \
                      'windSpeed':     forecast['wind']['speed']}
    # pprint.pprint(simpleForecast)
    print('\nIteration ' + str(threeHourForecast))
    # print('Raw Date:       ' + str(simpleForecast['dateRaw']))
    print('Textual date:   ' + simpleForecast['dateText'] + ' GMT')
    print('Cloud cover:    ' + str(simpleForecast['cloudCover']) + '%')
    print('Humidity:       ' + str(simpleForecast['humidity']) + '%')
    print('Pressure:       ' + str(simpleForecast['pressure']) + 'hPa')
    print('Temperature:    ' + str(simpleForecast['temperature']) + 'degreesC')
#TODO Fix    print('Rainfall:       ' + str(simpleForecast['rainfall']) + 'mm')
    print('Wind direction: ' + str(simpleForecast['windDirection']) + 'degrees')
    print('Wind speed:     ' + str(simpleForecast['windSpeed']) + 'm/s')


# end of file








