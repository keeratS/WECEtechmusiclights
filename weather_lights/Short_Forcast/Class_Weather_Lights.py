# Definitions for getting information from the weather.gov API.
# We can expand this code as we begin writing more weather code.

# Should be already installed. If not:
# pip3 install requests (in terminal
import requests

# organizing in a class certainly isn't the only way to do this
# (or even necessarily the best way) but we can workshop it.

class Class_Weather_Lights:
    # constructor
    # self represents the instance of the class so we can access
    # the attributes and methods of the WeatherLights class.
    # You create the object like w = WeatherLights(latitude, longitude)
    def __init__(self, latitude, longitude):
        # By getting the grid here, we avoid having to make this call
        # everytime we want weather information.
        grid = requests.get("https://api.weather.gov/points/{},{}".format(latitude, longitude))
        grid = grid.json()
        properties = grid['properties']
        
        # we initialize instance variables inside the constructor
        self.url = properties['forecast']
        
        # just for verification
        self.city = properties['relativeLocation']['properties']['city']

    # returns current/latest wind speed in mph
    def get_wind_speed(self):
        # we will make a new API request here to ensure we are getting the
        # latest information
        
        forecast = requests.get(self.url)
        forecast = forecast.json()
        forecast = forecast['properties']['periods']
        
        # This is currently written to return the latest wind speed.
        # Notice this can easily be edited to return any requested time
        # period by adding an argument to the function.
        period = forecast[0]
        wind_speed = period['windSpeed'] # 'x mph'
        
        # get just int value and turn to num
        wind_speed = wind_speed.replace(' mph', '')
        wind_speed = float(wind_speed)
        
        return wind_speed
    
    def get_short_forecast(self):
        sforecast = requests.get(self.url)
        sforecast = sforecast.json()
        sforecast = sforecast['properties']['periods']
        period = sforecast[0]
        sforecast = period['shortForecast']
        sforecast = str(sforecast)
        return sforecast 
        