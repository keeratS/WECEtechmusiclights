import json
import urllib.request

def gethourlytemps(wfo, gridX, gridY):
    
    #get the forecast info from the national weather service
    forecast=urllib.request.urlopen('https://api.weather.gov/gridpoints/'+wfo+"/"+str(gridX)+","+str(gridY)+"/forecast/hourly").read()
    #interpret that json
    forecast=json.loads(forecast)
    
    temps=[] #list to store the temperatures we will ask for from the api so we can return a single item
    #loop through the json and grab the 24 next hourly temperature forcasts
    
    for i in range(24):
        temps.append(forecast['properties']['periods'][i]['temperature'])
    
    #return the list
    return (temps)
