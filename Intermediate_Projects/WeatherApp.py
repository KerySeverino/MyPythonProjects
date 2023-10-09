import tkinter as tk
#(ttk) has more modern GUI looks when compare to tK
from tkinter import ttk 
#You will need to install (requests) with your terminal (Mac: pip3 install requests / Window: pip install request)
import requests
import os

def city_Input():
    CITY = entry_Str.get()

# Define the path to the API key file using a relative path
api_key_file = os.path.expanduser("~/Desktop/MyProjects/weather_api_Key.txt")

# Read the API key from the file
with open(api_key_file, "r") as file:
    api_key = file.read()

CITY = "New York, US"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid="
URL = BASE_URL + api_key + "&q=" + CITY
response = requests.get(URL).json()
#Debugging API responsed
#print(response)


#Window
window = tk.Tk()
window.title("KersevWeather")
window.geometry("300x150")

#Widgets for the app
#Title
title_Label = ttk.Label(master = window, text = "KersevWeather", font = "Arial 24 bold")
title_Label.pack()

#User instructions
instruction_Label = ttk.Label(master = window, text = "Please enter a city", font = "Arial 12 bold")
instruction_Label.pack()

#####################################################################################################
#Input field -> This allows me to combine the entry user input field and the Enter button into a single unit within the Input Frame.
input_Frame = ttk.Frame(master = window)

#Entry user input
entry_Str = ttk.Entry(master = input_Frame)
entry_Str.pack(side = "left", padx = 10)

#Enter Button for the city input
enter_Button = ttk.Button(master = input_Frame, text= "Enter", command = city_Input)
enter_Button.pack(side = "right", padx = 10)
input_Frame.pack(pady = 10)
#####################################################################################################

#Output 
output_Label = ttk.Label(master = window, text = "Output", font = "Arial 16")
output_Label.pack()

#Runner
window.mainloop()

