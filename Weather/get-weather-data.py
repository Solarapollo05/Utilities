#----- Imports -----
import json, datetime
import requests as req

# ----- Globals -----
global api_key
global city_id
global url
global weather
global data
global data_updated

# ----- Main -----
with open ('config.json','r')as config_file:
    config_data = json.load(config_file)
    api_key = config_data['api_key']
    city_id= config_data['city_id']
    url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}'
data_updated = bool()

# ---------- Weather Data ----------

def get_current():
    print('Connecting to API to update data...')
    try:
        weather = req.get(url).json()

        condition = weather ['weather'][0]['main']
        temp = weather ['main']['temp']
        pressure = weather ['main']['pressure']
        humidity = weather ['main']['humidity']
        wind_speed = weather ['wind']['speed']
        wind_dir = weather ['wind']['deg']
        location_name = weather ['name']
        
        # ---------- Data Processing ----------
        temp = temp - float(273.15) # Convert temp from Kelvin to Celcius
        raw_data = [location_name, condition, temp, wind_speed, wind_dir, pressure, humidity]
        # TODO - Convert wind_dir from angle to Direction (North, South ect
        
        data ={
            'Name': location_name,
            'Weather Condition': condition,
            'Temperature': round (temp, 1),
            'Wind Speed': round(wind_speed, 2),
            'Wind Direction': wind_dir,
            'Pressure': round(pressure,1),
            'Humidity': humidity
        }
        global data_updated
        data_updated = True
        return data
        
    except:
        print('Failed to update weather data. Falling back to old data.')
        data_updated = False

def save_data_json(data):
    current_date = datetime.datetime.now()
    weather_dict = {"Location": data["Name"], 
    "Weather Condition": data["Weather Condition"],
    "Temperature": data["Temperature"],
    "Wind": {'Wind Speed': data["Wind Speed"], 'Wind Direction': data['Wind Direction']},
    "Pressure": data["Pressure"],
    "Humidity": data["Humidity"],
    "Timestamp": current_date.strftime("%H:%M:%H - %d/%m/%y")
    }
    print (current_date.strftime("%H:%M:%H - %d/%m/%y"))

    with open ('weather_data.json', 'w') as json_file:
        json.dump(weather_dict, json_file, indent=4)
        print('Saved weather data to file. ')

#def read_old_data():
    #with open ('weather_data.json', 'r') as json_file:
        #loaded_data = json.load(json_file)
        #timestamp = loaded_data ['Timestamp']

        #print('Warning - Using data from', timestamp, ', data may be inaccurate.')
        #print(f'\n The temperature is {loaded_data["Temperature"]}, and the condition is {loaded_data["Weather Condition"]}. ')
        
data = get_current()

# save_data_txt(data)
if data_updated == True:
    save_data_json(data)
#else:
    #data = read_old_data()