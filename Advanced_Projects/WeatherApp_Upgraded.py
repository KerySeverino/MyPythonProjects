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

    #Hands the (url) to the display_weather DEF
    ICON = "https://openweathermap.org/img/wn/" + response["weather"][0]["icon"] + "@2x.png"
    display_weather(ICON)

#Gets the icon image using the URL in openweathermap and displays it
def display_weather(icon_url):
    response = requests.get(icon_url)
    if response.status_code == 200:
        icon_data = response.content
        image = Image.open(BytesIO(icon_data))
        image = ImageTk.PhotoImage(image)
        icon_label.config(image = image)
        icon_label.image = image  

#Updates the display every time the user enters city
def update_display(response):
    description_label.config(text = "" + response["weather"][0]["description"])
    temperature_label.config(text = "TEMPERATURE: " + str(response["main"]["temp"]) + " °F")
    feels_like_label.config(text = "FEELS LIKE: " + str(response["main"]["feels_like"]) + " °F")
    humidity_label.config(text = "HUMIDITY: " + str(response["main"]["humidity"]) + " %")
    visibility_label.config(text = "VISIBILITY: " + str(get_Visibility(response)) + " Miles")
    windSpeed_label.config(text = "WINDSPEED: " + str(response["wind"]["speed"]) + " MPH")
    pressure_label.config(text = "PRESSURE: " + str(get_Pressure(response)) + " inHg")
    tempMin_label.config(text = "MIN TEMPERATURE: " + str(response["main"]["temp_min"]) + " °F -")
    tempMax_label.config(text = "MAX TEMPERATURE: " + str(response["main"]["temp_max"]) + " °F")
    
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


window = ttk.Window(themename = "darkly")
window.title("KersevWeather")
window.geometry("900x600")

#Visual Layout#
# lb0 = ttk.Label(master = input_Frame, text = "Entry", font = "Arial 14", background= "blue")
# lb0.pack(side="left")
# lb1 = ttk.Label(master = input_Frame, text = "Enter", font = "Arial 14", background= "blue")
# lb1.pack(side="right")
# lb2 = ttk.Label(master = first_frame, text = "Temp", font = "Arial 14", background= "blue")
# lb2.pack(side="top")
# lb3 = ttk.Label(master = first_frame, text = "Weather Description", font = "Arial 14", background= "blue")
# lb3.pack(side="top")
# lb4 = ttk.Label(master = first_frame, text = "Feels like", font = "Arial 14", background= "blue")
# lb4.pack(side="top")

# lb5 = ttk.Label(master = first_frame, text = "Humidity", font = "Arial 14", background= "blue")
# lb5.pack(side="top")
# lb6 = ttk.Label(master = first_frame, text = "Visibility", font = "Arial 14", background= "blue")
# lb6.pack(side="top")
# lb7 = ttk.Label(master = first_frame, text = "Windspeed", font = "Arial 14", background= "blue")
# lb7.pack(side="top")
# lb8 = ttk.Label(master = first_frame, text = "Pressure", font = "Arial 14", background= "blue")
# lb8.pack(side="top")

# lb9 = ttk.Label(master = first_frame, text = "Tempmin", font = "Arial 14", background= "red")
# lb9.pack(side="left")
# lb10 = ttk.Label(master = first_frame, text = "Tempmax", font = "Arial 14", background= "blue")
# lb10.pack(side="left", padx = 5)

# lb11 = ttk.Label(master = first_frame, text = "Sunset", font = "Arial 14", background= "red")
# lb11.pack(side="right", padx = 5)
# lb12 = ttk.Label(master = first_frame, text = "sunrise", font = "Arial 14", background= "blue")
# lb12.pack(side="right")


###################################################################

input_Frame = ttk.Frame(master = window)

label_instructions = ttk.Label(master = input_Frame, text = "Please enter a City or Country to retrieve Weather Information", font = "Arial 14")
label_instructions.pack(side = "top", pady = 10)

entry_Str = ttk.StringVar()
entry = ttk.Entry(master = input_Frame, textvariable = entry_Str, bootstyle ="info")
entry.pack(side = "left", padx= 5)

enter_button = ttk.Button(master = input_Frame, text = "Enter", padding = (70,5), command = fetch_weather_data, bootstyle = "info")
enter_button.pack(side = "right")

input_Frame.pack(side = "top", pady= 20)

###################################################################
#First Section
first_frame = ttk.Frame(master = window)

description_label= ttk.Label(master = first_frame, text = "", font="Arial 12 bold", bootstyle = "danger")
icon_label = ttk.Label(first_frame, text="")

temperature_label = ttk.Label(master = first_frame, text = "", font="Arial 12 bold")
feels_like_label = ttk.Label(master = first_frame, text = "", font="Arial 12 bold")
humidity_label = ttk.Label(master = first_frame, text = "", font="Arial 12 bold")
visibility_label = ttk.Label(master = first_frame, text = "", font="Arial 12 bold")
windSpeed_label = ttk.Label(master = first_frame, text = "", font="Arial 12 bold")
pressure_label = ttk.Label(master = first_frame, text = "", font="Arial 12 bold")
tempMin_label = ttk.Label(master = first_frame, text = "", font="Arial 12 bold")
tempMax_label = ttk.Label(master = first_frame, text = "", font="Arial 12 bold")

#Packs all the necessary labels in the first section
description_label.pack(side = "top")
icon_label.pack(side="top", pady=20)

temperature_label.pack(side = "top", pady = 1)
feels_like_label.pack(side = "top", pady = 1)
humidity_label.pack(side = "top", pady = 1)
visibility_label.pack(side = "top", pady = 1)
windSpeed_label.pack(side = "top", pady = 1)
pressure_label.pack(side = "top", pady = 1)

#LEFT / RIGHT
tempMin_label.pack(side = "left", pady = 1)
tempMax_label.pack(side = "right", pady = 1)

first_frame.pack(side="top")
###################################################################
#Second Section
second_frame = ttk.Frame(master = window)

# 5 day forecast / maybe?

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


