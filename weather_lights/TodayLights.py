
import requests

# organizing in a class certainly isn't the only way to do this
# (or even necessarily the best way) but we can workshop it.

class TempLights:
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
    def get_temperature(self):
        # we will make a new API request here to ensure we are getting the
        # latest information
        
        forecast = requests.get(self.url)
        forecast = forecast.json()
        forecast = forecast['properties']['periods']
        
        # This is currently written to return the latest wind speed.
        # Notice this can easily be edited to return any requested time
        # period by adding an argument to the function.
        period = forecast[0]
        rn_temp = period['temperature'] # 'x mph'
        
        # get just int value and turn to num
        rn_temp = rn_temp.replace(' F', '')
        rn_temp = float(rn_temp)
        
        return rn_temp