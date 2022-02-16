import json

data_file = open('weather_data.json')

data = json.load(data_file)

location = data ['Location']
condition = data ['Weather Condition']
temp = ['Temperature']
wind_speed = ['Wind']
wind_dir = ['Wind']['Wind Direction']
pressure = ['Pressure']
humidity = ['Humidity']
timestamp = ['Timestamp']

print(location, condition, temp, wind_speed, wind_dir, pressure, humidity, timestamp)