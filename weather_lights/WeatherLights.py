# Definitions for getting information from the weather.gov API.
# We can expand this code as we begin writing more weather code.

# Should be already installed. If not:
# pip3 install requests (in terminal)
import requests

# returns coordinates from ip address as (lat, long)
def get_lat_long():
    url = "http://ipinfo.io/json"
    response = requests.get(url)
    data = response.json()
    
    coord = data["loc"]
    coord = coord.split(",")
    return coord[0], coord[1]
    
# organizing in a class certainly isn't the only way to do this
# (or even necessarily the best way) but we can workshop it.

class WeatherLights:
    # constructor
    # self represents the instance of the class so we can access
    # the attributes and methods of the WeatherLights class.
    # You create the object like WeatherLights(latitude, longitude)
    # or WeatherLights() to get location from ip
    def __init__(self, latitude = None, longitude = None):
        if(latitude is None or longitude is None):
            latitude, longitude = get_lat_long()
        
        # By getting the grid here, we avoid having to make this call
        # everytime we want weather information.
        grid = requests.get("https://api.weather.gov/points/{},{}".format(latitude, longitude))
        grid = grid.json()
        properties = grid['properties']
        
        self.grid_x = properties['gridX']
        self.grid_y = properties['gridY']
        
        # initializing instance variables
        self.url = properties['forecast'] # basic forecast url
        
        self.latitude = latitude
        self.longitude = longitude
        
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
        # if contains range, get avg
        ran = wind_speed.find(" to ")
        if(ran != -1):
            a = float(wind_speed[0:ran])
            b = float(wind_speed[5:])
            wind_speed = (a+b) / 2
        else:
            wind_speed = float(wind_speed)
        
        return wind_speed
    
    def get_short_forecast(self):
        #Short Forecast
        sforecast = requests.get(self.url)
        sforecast = sforecast.json()
        sforecast = sforecast['properties']['periods']
        period = sforecast[0]
        sforecast = period['shortForecast']
        sforecast = str(sforecast)
        return sforecast 

if __name__ == "__main__":
    # tests
    lat = 38.9072
    long = -77.0369
    weather1 = WeatherLights(lat, long)
    print("Given coordinates", lat, long)
    print(weather1.latitude, weather1.longitude)
    
    print()
    weather2 = WeatherLights()
    print("From ip address")
    print(weather2.latitude, weather2.longitude)
    
    