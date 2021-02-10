# WECE Technical Smart String Lights

This repo contains the code for the UIUC WECE Technical project for 2020-2021.  

These smart string lights provide on command weather data in a fun, visual format (on a string of 50 leds). It also provides music visualizations based on the mic input, as well as some fun themed lighting.  

## Functionality

There are currently three different categories of functionalities. Here's how to call them and what the light output means. 

#### Weather Lights
The short_forecast displays the current weather based off your location

Snow: if there is snow in the forecast it will display white lights that turn on individually and turn off, and then move to the next light. The code tries to imitate snow falling.
Rain: if there is rain in the forecast, the program will start with white LEDs and blue lights will move through the white lights to imitate rain falling from clouds.
Sunny: if there is sun in the forecast, the code will move yellow lights through the leds to symbolize the sun rays moving.
Cloudy: if there is clouds in the forecast, the code will move white lights through the leds to symbolize large clouds moving. 
Foggy: if there is fog in the forecast, the program is similar to the cloudy code, but the lights are much duller.
The program is done running when the rainbow lights display at the end. 

If there is a combination of the above weather, it will do weather animations that are listed in the forecast. (For example, if it is sunny and cloudy today, the lights will display sunny and cloudy one after the other)



#### Music Lights

#### Themed Lights
