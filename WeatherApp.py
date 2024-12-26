import ttkbootstrap as ttk # You will need to download this, Mac: pip3 install ttkbootstrap, Window: pip install ttkbootstrap
import requests # You will need to download this, Mac: pip3 install requests, Window: pip install requests
import os

#API from OpenWeatherMap: Gets the weather data to display it
def fetch_weather_data(event=None):
    CITY = entry.get()
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid="
    URL = BASE_URL + api_key + "&q=" + CITY
    response = requests.get(URL).json()
    update_display(response)

#Updates the display every time the user enters city 
def update_display(response):
    temperature_label.config(text="TEMPERATURE: " + str(get_Fahrenheit(response)) + "°F")
    feels_like_label.config(text="FEELS LIKE: " + str(get_Feels_Like(response)) + "°F")
    humidity_label.config(text="HUMIDITY: " + str(get_Humidity(response)) + "%")
    visibility_label.config(text="VISIBILITY: " + str(get_Visibility(response)) + " mi")
    windSpeed_label.config(text="WINDSPEED: " + str(get_windSpeed(response)) + " MPH")

#Turns kelvin to Fahrenheit, and gets the temp
def get_Fahrenheit(response):
    kelvin_Temp = response["main"]["temp"]
    fahrenheit_Temp = (kelvin_Temp - 273.15) * 9/5 + 32
    return int(fahrenheit_Temp)

#Turns kelvin to Fahrenheit, and gets the feels like
def get_Feels_Like(response):
    kelvin_Temp = response["main"]["feels_like"]
    fahrenheit_Temp = (kelvin_Temp - 273.15) * 9/5 + 32
    return int(fahrenheit_Temp)

#Gets the humitity
def get_Humidity(response):
    humidity = response["main"]["humidity"]
    return int(humidity)

#Gets the visibility, by calculating meters, kilometers and miles
def get_Visibility(response):
    meters_visibility = response["visibility"]
    kilometers_visibility = meters_visibility * 0.001
    miles = kilometers_visibility * 0.621371
    return int(miles)

def get_windSpeed(response):
    windSpeed = response["wind"]["speed"]
    return int(windSpeed)

# Define the path to the API key file using a relative path
api_key_file = os.path.expanduser("~/Desktop/MyProjects/weather_api_Key.txt")

# Read the API key from the file
with open(api_key_file, "r") as file:
    api_key = file.read()

#Creates the window and sets the theme using ttKBootstrap 
window = ttk.Window(themename = "darkly")

window.title("KersevWeather")
window.geometry("400x300")


# Title
title_Label = ttk.Label(master = window, text = "KersevWeather", font = "Arial 24 bold")
title_Label.pack()

# User instructions
instruction_Label = ttk.Label(master = window, text = "Please enter a city", font = "Arial 12 bold")
instruction_Label.pack(pady = 10)

#####################################################################################################
# Input field
input_Frame = ttk.Frame(master = window)

entry_Str = ttk.StringVar()
entry = ttk.Entry(master = input_Frame, textvariable = entry_Str)
entry.pack(side ="left", pady = 10)

# Fetch Weather button
enter_button = ttk.Button(master=input_Frame, text="Enter", padding = (20,10),command = fetch_weather_data)
enter_button.pack(side = "right", padx = 10)

input_Frame.pack()
#####################################################################################################


#####################################################################################################
# Output field
output_Label = ttk.Label(master = window)
temperature_label = ttk.Label(master = output_Label, text = "", font="Arial 12 bold")
feels_like_label = ttk.Label(master = output_Label, text = "", font="Arial 12 bold")
humidity_label = ttk.Label(master = output_Label, text = "", font="Arial 12 bold")
visibility_label = ttk.Label(master = output_Label, text = "", font="Arial 12 bold")
windSpeed_label = ttk.Label(master = output_Label, text = "", font="Arial 12 bold")

temperature_label.pack(side = "top")
feels_like_label.pack(side = "top")
humidity_label.pack(side = "top")
visibility_label.pack(side = "top")
windSpeed_label.pack(side = "top")

output_Label.pack()
#####################################################################################################

# Starts the Tkinter main loop

#Debugging API calls
# CITY = "New York"
# BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid="
# URL = BASE_URL + api_key + "&q=" + CITY
# response = requests.get(URL).json()
# print(response)

window.mainloop()

