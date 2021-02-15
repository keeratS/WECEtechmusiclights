# WECE Technical Smart String Lights

This repo contains the code for the UIUC WECE Technical project for 2020-2021.  

These smart string lights provide on command weather data in a fun, visual format (on a string of 50 leds). It also provides music visualizations based on the mic input, as well as some fun themed lighting.  

## Functionality

There are currently three different categories of functionalities. Here's how to call them and what the light output means. 

#### Weather Lights  

*Short Forcast*  
The short_forecast displays the current weather based off your location.

Snow: if there is snow in the forecast it will display white lights that turn on individually and turn off, and then move to the next light. The code tries to imitate snow falling.  
Rain: if there is rain in the forecast, the program will start with white LEDs and blue lights will move through the white lights to imitate rain falling from clouds.  
Sunny: if there is sun in the forecast, the code will move yellow lights through the leds to symbolize the sun rays moving.  
Cloudy: if there is clouds in the forecast, the code will move white lights through the leds to symbolize large clouds moving.   
Foggy: if there is fog in the forecast, the program is similar to the cloudy code, but the lights are much duller.  

If there is a combination of the above weather, it will do weather animations that are listed in the forecast. (For example, if it is sunny and cloudy today, the lights will display sunny and cloudy one after the other)

*Wind Speed*  
The wind_speed_lights function gets the current wind speed. The speed of the lights across directly correspond to the wind speed, assuming a two inch distance between adjacent LEDs.

*Precipitation*
Visualizes the probabilities of rain and snow by filling a proportional number of lights. 

#### Music Lights    

*Pitch Reaction*  
The pitch_react function taken the input from the microphone and displays a hue for the lights based on the current pitch. This animation moves across the string of lights as subsequent input comes in. 

#### Themed Lights   

*Galaxy Lights*  
Makes the lights blue and shifts through slightly different colors, creating a twinkling effect.

*Fireworks*  
Lights up random sections of the lights in primary colors which slowly spread and fade, like fireworks.

*Rainbow Shift*
Creates traveling lights across the string in rainbow order. 

*Fire Flicker*
Produces subtly shifting fire-colored lights. 
