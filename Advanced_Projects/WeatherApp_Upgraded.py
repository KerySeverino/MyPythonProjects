import ttkbootstrap as ttk # You will need to download this, Mac: pip3 install ttkbootstrap, Window: pip install ttkbootstrap
import requests # You will need to download this, Mac: pip3 install requests, Window: pip install requests
import os
from PIL import Image, ImageTk
from io import BytesIO 

#Definitions
def fetch_weather_data(event=None):
    CITY = entry.get()
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid="
    URL = BASE_URL + api_key + "&q=" + CITY + "&units=imperial"
    response = requests.get(URL).json()
    update_display(response)

#Gets the icon image using the URL in openweathermap and displays it
def display_weather(icon_url):
    response = requests.get(icon_url)
    if response.status_code == 200:
        icon_data = response.content
        image = Image.open(BytesIO(icon_data))
        image = ImageTk.PhotoImage(image)
        icon_label.config(image = image)
        icon_label.image = image
    else: 
        icon_label.config(image = None)
        
#Updates the display every time the user enters city
def update_display(response):

    if response["cod"] == 200:
        # Update labels with weather data
        description_label.config(text="| " + response["weather"][0]["description"] + " |")
        ICON = "https://openweathermap.org/img/wn/" + response["weather"][0]["icon"] + "@2x.png"
        display_weather(ICON)

        temperature_label.config(text="| TEMPERATURE: " + str(response["main"]["temp"]) + " °F |")
        feels_like_label.config(text="FEELS LIKE: " + str(response["main"]["feels_like"]) + " °F")
        humidity_label.config(text="HUMIDITY: " + str(response["main"]["humidity"]) + " %")
        visibility_label.config(text="VISIBILITY: " + str(get_Visibility(response)) + " Miles")
        windSpeed_label.config(text="WINDSPEED: " + str(response["wind"]["speed"]) + " MPH")
        pressure_label.config(text="PRESSURE: " + str(get_Pressure(response)) + " inHg")
        tempMin_label.config(text="| MIN TEMPERATURE: " + str(response["main"]["temp_min"]) + " °F |")
        tempMax_label.config(text="| MAX TEMPERATURE: " + str(response["main"]["temp_max"]) + " °F |")

        # Clear the error message
        error_Label.config(text="")

    elif response["cod"] != 200:
        # Clear the weather data labels
        description_label.config(text="")
        temperature_label.config(text="")
        feels_like_label.config(text="")
        humidity_label.config(text="")
        visibility_label.config(text="")
        windSpeed_label.config(text="")
        pressure_label.config(text="")
        tempMin_label.config(text="")
        tempMax_label.config(text="")

        # Display the error message
        error_Label.config(text="| API Request failed. Status code [" + str(response["cod"]) + "], Please enter a valid City or Country |")

    
#Turns Visibility from Km to Miles
def get_Visibility(response):
    kilometers_visibility = response["visibility"] * 0.001
    return int(kilometers_visibility * 0.621371)

#Turns Pressure from hPA to inHg
def get_Pressure(response):
    return f'{response["main"]["pressure"] * 0.02953:.2f}'

###################################################################
#API KEY RETRIVAL

# Define the path to the API key file using a relative path
api_key_file = os.path.expanduser("~/Desktop/MyProjects/weather_api_Key.txt")

# Read the API key from the file
with open(api_key_file, "r") as file:
    api_key = file.read()

###################################################################

#Window start
window = ttk.Window(themename = "flatly")
window.title("KersevWeather")
window.geometry("900x600")

###################################################################

#Input / User frame 
input_Frame = ttk.Frame(master = window, bootstyle = "info", padding= 5)

label_instructions = ttk.Label(master = input_Frame, text = "Please enter a City or Country to retrieve Weather Information", font = "Arial 14 bold")
label_instructions.pack(side = "top", pady = 10)

entry_Str = ttk.StringVar()
entry = ttk.Entry(master = input_Frame, textvariable = entry_Str, bootstyle ="darkly")
entry.pack(side = "left", padx= 5)

enter_button = ttk.Button(master = input_Frame, text = "Enter", padding = (70,5), command = fetch_weather_data, bootstyle = "primary")
enter_button.pack(side = "right")

input_Frame.pack(side = "top", pady= 20)

###################################################################
#First Section
first_frame = ttk.Frame(master = window)

#Displays the error messages
error_Label = ttk.Label(master=first_frame, text="", font= "Arial 14 bold", bootstyle = "danger")

description_label = ttk.Label(master = first_frame, text = "", font="Arial 12 bold", bootstyle = "danger")
icon_label = ttk.Label(first_frame, text="")

#Packs all the necessary labels in the first section
error_Label.pack(side = "top")
description_label.pack(side = "top")
icon_label.pack(side="top", pady=20)

first_frame.pack(side="top")
###################################################################
#Second Section
second_frame = ttk.Frame(master = window)

temperature_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "dark")
feels_like_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "dark")
humidity_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "dark")
visibility_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "dark")
windSpeed_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "dark")
pressure_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "dark")
tempMin_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "info")
tempMax_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "danger")

temperature_label.pack(side = "top", pady = 1)
feels_like_label.pack(side = "top", pady = 1)
humidity_label.pack(side = "top", pady = 1)
visibility_label.pack(side = "top", pady = 1)
windSpeed_label.pack(side = "top", pady = 1)
pressure_label.pack(side = "top", pady = 1)

#LEFT / RIGHT
tempMin_label.pack(side = "left", pady = 1)
tempMax_label.pack(side = "right", pady = 1)

second_frame.pack(side="top")

###################################################################

####Debugging API Calls###

    #Current weather api call
    # CITY = "New York"
    # BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid="
    # URL = BASE_URL + api_key + "&q=" + CITY + "&units=imperial"
    # response = requests.get(URL).json()

    #5 day forecast api call
    # CITY = "New York"
    # BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?appid="
    # URL = BASE_URL + api_key + "&q=" + CITY + "&units=imperial"
    # response = requests.get(URL).json()

# response["main"]
#{'temp': 57.38, 'feels_like': 55.31, 'temp_min': 49.68, 'temp_max': 61.95, 'pressure': 1015, 'humidity': 53}

# response["weather"]
#[{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]

#Run
window.mainloop()


