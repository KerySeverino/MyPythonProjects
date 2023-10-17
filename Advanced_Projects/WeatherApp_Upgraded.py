import ttkbootstrap as ttk # You will need to download this, Mac: pip3 install ttkbootstrap, Window: pip install ttkbootstrap
import requests # You will need to download this, Mac: pip3 install requests, Window: pip install requests
import os #API KEY FILE - Retrival
from PIL import Image, ImageTk #ICONS
from io import BytesIO 
from ttkbootstrap.constants import * #BOTH

### All Definitions ###

def fetch_weather_data(event=None):
    #Current weather data
    CITY = entry.get()
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid="
    URL = BASE_URL + api_key + "&q=" + CITY + "&units=imperial"
    response = requests.get(URL).json()
    update_display(response)

    #Weekly weather data
    WEEK_BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?appid="
    WEEK_URL = WEEK_BASE_URL + api_key + "&q=" + CITY + "&units=imperial"
    week_response = requests.get(WEEK_URL).json()
    update_weekly_display(week_response)
    
###################################################################       
def update_weekly_display(week_response):

    # Weekly weather data display in the window 
    if week_response["cod"] == str(200):
        #Day 1
        day1_time = week_response["list"][0]["dt_txt"]
        day1 = day1_time.split(' ')[0]
        day1_date.config(text =  str(day1))

        day1_description_label.config(text = "| " + week_response["list"][0]["weather"][0]["description"] + " |")
        day1_temp_label.config(text="TEMPERATURE: " + str(week_response["list"][0]["main"]["temp"]) + " °F")
        day1_feelslike_label.config(text="FEELS LIKE: " + str(week_response["list"][0]["main"]["feels_like"]) + " °F")
        day1_humidity_label.config(text="HUMIDITY: " + str(week_response["list"][0]["main"]["humidity"]) + " %")
        day1_mintemp_label.config(text="| MIN TEMPERATURE: " + str(week_response["list"][0]["main"]["temp_min"]) + " °F |")
        day1_maxtemp_label.config(text="| MAX TEMPERATURE: " + str(week_response["list"][0]["main"]["temp_max"]) + " °F |")

        #Day 2
        day2_time = week_response["list"][8]["dt_txt"]
        day2 = day2_time.split(' ')[0]
        day2_date.config(text =  str(day2))

        day2_description_label.config(text = "| " + week_response["list"][8]["weather"][0]["description"] + " |")
        day2_temp_label.config(text="TEMPERATURE: " + str(week_response["list"][8]["main"]["temp"]) + " °F")
        day2_feelslike_label.config(text="FEELS LIKE: " + str(week_response["list"][8]["main"]["feels_like"]) + " °F")
        day2_humidity_label.config(text="HUMIDITY: " + str(week_response["list"][8]["main"]["humidity"]) + " %")
        day2_mintemp_label.config(text="| MIN TEMPERATURE: " + str(week_response["list"][8]["main"]["temp_min"]) + " °F |")
        day2_maxtemp_label.config(text="| MAX TEMPERATURE: " + str(week_response["list"][8]["main"]["temp_max"]) + " °F |")

        #Day 3
        day3_time = week_response["list"][16]["dt_txt"]
        day3 = day3_time.split(' ')[0]
        day3_date.config(text =  str(day3))

        day3_description_label.config(text = "| " + week_response["list"][16]["weather"][0]["description"] + " |")
        day3_temp_label.config(text="TEMPERATURE: " + str(week_response["list"][16]["main"]["temp"]) + " °F")
        day3_feelslike_label.config(text="FEELS LIKE: " + str(week_response["list"][16]["main"]["feels_like"]) + " °F")
        day3_humidity_label.config(text="HUMIDITY: " + str(week_response["list"][16]["main"]["humidity"]) + " %")
        day3_mintemp_label.config(text="| MIN TEMPERATURE: " + str(week_response["list"][16]["main"]["temp_min"]) + " °F |")
        day3_maxtemp_label.config(text="| MAX TEMPERATURE: " + str(week_response["list"][16]["main"]["temp_max"]) + " °F |")

        #Day 4
        day4_time = week_response["list"][24]["dt_txt"]
        day4 = day4_time.split(' ')[0]
        day4_date.config(text =  str(day4))

        day4_description_label.config(text = "| " + week_response["list"][24]["weather"][0]["description"] + " |")
        day4_temp_label.config(text="TEMPERATURE: " + str(week_response["list"][24]["main"]["temp"]) + " °F")
        day4_feelslike_label.config(text="FEELS LIKE: " + str(week_response["list"][24]["main"]["feels_like"]) + " °F")
        day4_humidity_label.config(text="HUMIDITY: " + str(week_response["list"][24]["main"]["humidity"]) + " %")
        day4_mintemp_label.config(text="| MIN TEMPERATURE: " + str(week_response["list"][24]["main"]["temp_min"]) + " °F |")
        day4_maxtemp_label.config(text="| MAX TEMPERATURE: " + str(week_response["list"][24]["main"]["temp_max"]) + " °F |")

        #Day 5
        day5_time = week_response["list"][32]["dt_txt"]
        day5 = day5_time.split(' ')[0]
        day5_date.config(text =  str(day5))

        day5_description_label.config(text = "| " + week_response["list"][32]["weather"][0]["description"] + " |")
        day5_temp_label.config(text="TEMPERATURE: " + str(week_response["list"][32]["main"]["temp"]) + " °F")
        day5_feelslike_label.config(text="FEELS LIKE: " + str(week_response["list"][32]["main"]["feels_like"]) + " °F")
        day5_humidity_label.config(text="HUMIDITY: " + str(week_response["list"][32]["main"]["humidity"]) + " %")
        day5_mintemp_label.config(text="| MIN TEMPERATURE: " + str(week_response["list"][32]["main"]["temp_min"]) + " °F |")
        day5_maxtemp_label.config(text="| MAX TEMPERATURE: " + str(week_response["list"][32]["main"]["temp_max"]) + " °F |")

    else:
        #Clears the weather data from the window for day 1 to day 5
        #Day 1
        day1_date.config(text = "")
        day1_description_label.config(text="")
        day1_temp_label.config(text="")
        day1_feelslike_label.config(text="")
        day1_humidity_label.config(text="")
        day1_mintemp_label.config(text="")
        day1_maxtemp_label.config(text="")

        #Day 2
        day2_date.config(text = "")
        day2_description_label.config(text="")
        day2_temp_label.config(text="")
        day2_feelslike_label.config(text="")
        day2_humidity_label.config(text="")
        day2_mintemp_label.config(text="")
        day2_maxtemp_label.config(text="")

        #Day 3
        day3_date.config(text = "")
        day3_description_label.config(text="")
        day3_temp_label.config(text="")
        day3_feelslike_label.config(text="")
        day3_humidity_label.config(text="")
        day3_mintemp_label.config(text="")
        day3_maxtemp_label.config(text="")

        #Day 4
        day4_date.config(text = "")
        day4_description_label.config(text="")
        day4_temp_label.config(text="")
        day4_feelslike_label.config(text="")
        day4_humidity_label.config(text="")
        day4_mintemp_label.config(text="")
        day4_maxtemp_label.config(text="")

        #Day 5
        day5_date.config(text = "")
        day5_description_label.config(text="")
        day5_temp_label.config(text="")
        day5_feelslike_label.config(text="")
        day5_humidity_label.config(text="")
        day5_mintemp_label.config(text="")
        day5_maxtemp_label.config(text="")

###################################################################
#Current Weather Def's
#Gets a image icon using API call, PIL, and BytesIO
def display_weather(icon_url):
    response = requests.get(icon_url)
    if response.status_code == 200:
        icon_data = response.content
        image = Image.open(BytesIO(icon_data))
        image = ImageTk.PhotoImage(image)
        icon_label.config(image = image)
        icon_label.image = image
    else: 
        icon_label.pack_forget()

#Updates the display every time the user enters city
def update_display(response):
    if response["cod"] == 200:
        # Updates labels with current weather data
        today_label.config(text= "TODAY")
        description_label.config(text="| " + response["weather"][0]["description"] + " |")
        ICON = "https://openweathermap.org/img/wn/" + response["weather"][0]["icon"] + "@2x.png"
        display_weather(ICON)

        temperature_label.config(text = "| TEMPERATURE: " + str(response["main"]["temp"]) + " °F |")
        feels_like_label.config(text = "FEELS LIKE: " + str(response["main"]["feels_like"]) + " °F")
        humidity_label.config(text = "HUMIDITY: " + str(response["main"]["humidity"]) + " %")
        visibility_label.config(text = "VISIBILITY: " + str(get_Visibility(response)) + " Miles")
        windSpeed_label.config(text = "WINDSPEED: " + str(response["wind"]["speed"]) + " MPH")
        pressure_label.config(text = "PRESSURE: " + str(get_Pressure(response)) + " inHg")
        tempMin_label.config(text = "| MIN TEMPERATURE: " + str(response["main"]["temp_min"]) + " °F |")
        tempMax_label.config(text = "| MAX TEMPERATURE: " + str(response["main"]["temp_max"]) + " °F |")

        # Clear the error message from the window
        error_Label.config(text="")

    elif response["cod"] != 200:
        # Clear the current weather data from the window
        today_label.config(text = "")
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
#Easter egg configs
current_gauge_value = 0 
def fetch_click():
    global current_gauge_value  # Use a global variable to keep track of the value
    current_gauge_value += 10  # Increment the gauge value by 10
    gauge.step(10)

    #Removes the easter egg from the weather app
    if current_gauge_value == 2200:
        gauge.pack_forget()
        click_me_Button.pack_forget()

    if current_gauge_value == 150:
        click_me_Button.config(text = "Nothing here")
    elif current_gauge_value == 400:
        click_me_Button.config(text = "Seriously?")
    elif current_gauge_value == 600:
        click_me_Button.config(text = "You for sure, are stubborn...")
        third_frame.pack(side = "left")
    elif current_gauge_value == 900:
        click_me_Button.config(text = "It's better if you stop now....", bootstyle = "warning")
        third_frame.pack(side = "top")
    elif current_gauge_value == 950:
        click_me_Button.config(text = "I'm warning you....", bootstyle = "warning")
        third_frame.pack(side = "right")
    elif current_gauge_value == 970:
        click_me_Button.config(text = "....You are breaking me....", bootstyle = "warning")
        third_frame.pack(side = "bottom")
    elif current_gauge_value == 990:
        click_me_Button.config(text = "........", bootstyle = "danger")
        third_frame.pack(side = "top")
    elif current_gauge_value == 1000:
        click_me_Button.config(text = "Idk what to said to you...")
        third_frame.pack(side = "left")
    elif current_gauge_value == 1100:
        click_me_Button.config(text = "Wouldn't it be better to just look at the weather data?", bootstyle = "warning")
        third_frame.pack(side = "top")
    elif current_gauge_value == 1710:
        click_me_Button.config(text = "I guess not...", bootstyle = "warning")
        third_frame.pack(side = "right")
    elif current_gauge_value == 1850:
        click_me_Button.config(text = "STOP!!!!", bootstyle = "danger")
        third_frame.pack(side = "left")
    elif current_gauge_value == 2050:
        click_me_Button.config(text = "YOU CAN STILL STOP THIS!!!", bootstyle = "danger")
        third_frame.pack(side = "bottom")
    elif current_gauge_value == 2100:
        click_me_Button.config(text = "Congratulations, on clicking him non-stop.. he's now in a better place.. I hope you feel better..", bootstyle = "dark")
        third_frame.pack(side = "top")
    elif current_gauge_value == 2150:
        click_me_Button.config(text = "Still clicking?...", bootstyle = "dark")
        third_frame.pack(side = "top")
    elif current_gauge_value == 2170:
        click_me_Button.config(text = "Wow..", bootstyle = "dark")
        third_frame.pack(side = "top")
    elif current_gauge_value == 2200:
        click_me_Button.config(text = "")


###################################################################
#API KEY RETRIVAL
# Define the path to the API key file using a relative path
api_key_file = os.path.expanduser("~/Desktop/MyProjects/weather_api_Key.txt")

# Read the API key from the file
with open(api_key_file, "r") as file:
    api_key = file.read()


###################################################################
#Window start
window = ttk.Window(themename = "superhero")
window.title("KersevWeather")
window.geometry("1000x640")

###################################################################
#Input / User Section
input_Frame = ttk.Frame(master = window, bootstyle = "dark", padding= 5)

label_instructions = ttk.Label(master = input_Frame, text = "Please enter a City or Country to retrieve Weather Information", font = "Arial 14 bold")
label_instructions.pack(side = "top", pady = 10)

entry_Str = ttk.StringVar()
entry = ttk.Entry(master = input_Frame, textvariable = entry_Str, bootstyle ="primary")
entry.pack(side = "left", padx= 5)

enter_button = ttk.Button(master = input_Frame, text = "Enter", padding = (70,5), command = fetch_weather_data, bootstyle = "primary")
enter_button.pack(side = "right")

input_Frame.pack(side = "top", pady= 20)

###################################################################
#First Section
first_frame = ttk.Frame(master = window)

today_label = ttk.Label(master = first_frame, text = "", font="Arial 12 bold", bootstyle = "success")
description_label = ttk.Label(master = first_frame, text = "", font="Arial 12 bold", bootstyle = "danger")
icon_label = ttk.Label(first_frame, text="")

#Packs all the necessary labels in the first section
today_label.pack(side = "top")
description_label.pack(side = "top")
icon_label.pack(side="top")

#Displays the error messages
error_Label = ttk.Label(master=first_frame, text="", font= "Arial 14 bold", bootstyle = "danger")
error_Label.pack(side = "top")

first_frame.pack(side="top")


###################################################################

#Second Section
second_frame = ttk.Frame(master = window)

temperature_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "light")
feels_like_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "light")
humidity_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "light")
visibility_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "light")
windSpeed_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "light")
pressure_label = ttk.Label(master = second_frame, text = "", font="Arial 12 bold", bootstyle = "light")
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

second_frame.pack(side="top", pady= 40)


###################################################################
#Weekly Section
#Day 1 Labels
day1_frame = ttk.Frame(master = window)

day1_date = ttk.Label(master = day1_frame, text = "", font = "Arial 12 bold", bootstyle = "success", padding = 5)
day1_description_label = ttk.Label(master = day1_frame, text = "", font="Arial 12 bold", bootstyle = "danger")
day1_temp_label = ttk.Label(master = day1_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day1_feelslike_label = ttk.Label(master = day1_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day1_humidity_label = ttk.Label(master = day1_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day1_mintemp_label = ttk.Label(master = day1_frame, text = "", font="Arial 12 bold", bootstyle = "info")
day1_maxtemp_label = ttk.Label(master = day1_frame, text = "", font="Arial 12 bold", bootstyle = "danger")

day1_date.pack(side = "left")
day1_description_label.pack(side = "left")
day1_temp_label.pack(side = "left")
day1_feelslike_label.pack(side = "left")
day1_humidity_label.pack(side = "left")
day1_mintemp_label.pack(side = "left") 
day1_maxtemp_label.pack(side = "left")
day1_frame.pack(side = "top")

day2_frame = ttk.Frame(master = window)

#Day 2 Labels
day2_date = ttk.Label(master = day2_frame, text = "", font = "Arial 12 bold", bootstyle = "success", padding = 5)
day2_description_label = ttk.Label(master = day2_frame, text = "", font="Arial 12 bold", bootstyle = "danger")

day2_temp_label = ttk.Label(master = day2_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day2_feelslike_label = ttk.Label(master = day2_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day2_humidity_label = ttk.Label(master = day2_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day2_mintemp_label = ttk.Label(master = day2_frame, text = "", font="Arial 12 bold", bootstyle = "info")
day2_maxtemp_label = ttk.Label(master = day2_frame, text = "", font="Arial 12 bold", bootstyle = "danger")

day2_date.pack(side = "left")
day2_description_label.pack(side = "left")
day2_temp_label.pack(side = "left")
day2_feelslike_label.pack(side = "left")
day2_humidity_label.pack(side = "left")
day2_mintemp_label.pack(side = "left") 
day2_maxtemp_label.pack(side = "left")

day2_frame.pack(side = "top")

#Day 3 Labels
day3_frame = ttk.Frame(master = window)

day3_date = ttk.Label(master = day3_frame, text = "", font = "Arial 12 bold", bootstyle = "success", padding = 5)
day3_description_label = ttk.Label(master = day3_frame, text = "", font="Arial 12 bold", bootstyle = "danger")

day3_temp_label = ttk.Label(master = day3_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day3_feelslike_label = ttk.Label(master = day3_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day3_humidity_label = ttk.Label(master = day3_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day3_mintemp_label = ttk.Label(master = day3_frame, text = "", font="Arial 12 bold", bootstyle = "info")
day3_maxtemp_label = ttk.Label(master = day3_frame, text = "", font="Arial 12 bold", bootstyle = "danger")

day3_date.pack(side = "left")
day3_description_label.pack(side = "left")
day3_temp_label.pack(side = "left")
day3_feelslike_label.pack(side = "left")
day3_humidity_label.pack(side = "left")
day3_mintemp_label.pack(side = "left") 
day3_maxtemp_label.pack(side = "left")

day3_frame.pack(side = "top")

#Day 4 Labels
day4_frame = ttk.Frame(master = window)

day4_date = ttk.Label(master = day4_frame, text = "", font = "Arial 12 bold", bootstyle = "success", padding = 5)
day4_description_label = ttk.Label(master = day4_frame, text = "", font="Arial 12 bold", bootstyle = "danger")

day4_temp_label = ttk.Label(master = day4_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day4_feelslike_label = ttk.Label(master = day4_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day4_humidity_label = ttk.Label(master = day4_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day4_mintemp_label = ttk.Label(master = day4_frame, text = "", font="Arial 12 bold", bootstyle = "info")
day4_maxtemp_label = ttk.Label(master = day4_frame, text = "", font="Arial 12 bold", bootstyle = "danger")

day4_date.pack(side = "left")
day4_description_label.pack(side = "left")
day4_temp_label.pack(side = "left")
day4_feelslike_label.pack(side = "left")
day4_humidity_label.pack(side = "left")
day4_mintemp_label.pack(side = "left") 
day4_maxtemp_label.pack(side = "left")

day4_frame.pack(side = "top")

#Day 5 Labels
day5_frame = ttk.Frame(master = window)

day5_date = ttk.Label(master = day5_frame, text = "", font = "Arial 12 bold", bootstyle = "success",  padding = 5)
day5_description_label = ttk.Label(master = day5_frame, text = "", font="Arial 12 bold", bootstyle = "danger")

day5_temp_label = ttk.Label(master = day5_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day5_feelslike_label = ttk.Label(master = day5_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day5_humidity_label = ttk.Label(master = day5_frame, text = "", font="Arial 12 bold", bootstyle = "light")
day5_mintemp_label = ttk.Label(master = day5_frame, text = "", font="Arial 12 bold", bootstyle = "info")
day5_maxtemp_label = ttk.Label(master = day5_frame, text = "", font="Arial 12 bold", bootstyle = "danger")

day5_date.pack(side = "left")
day5_description_label.pack(side = "left")
day5_temp_label.pack(side = "left")
day5_feelslike_label.pack(side = "left")
day5_humidity_label.pack(side = "left")
day5_mintemp_label.pack(side = "left") 
day5_maxtemp_label.pack(side = "left")

day5_frame.pack(side = "top")

###################################################################
#Four section - Easter egg
third_frame = ttk.Frame(master = window)

gauge = ttk.Floodgauge(
    master=third_frame,
    font=(None, 12),
    mask='???',
    bootstyle="primary"
)

gauge.pack(fill=BOTH, expand=YES, padx=10, pady=10)

click_me_Button = ttk.Button(master = third_frame, text = "Don't Click Me!", padding = (50,50), command = fetch_click, bootstyle = "primary")
click_me_Button.pack(side = "bottom")

third_frame.pack(side = "top")
###################################################################

#Run
window.mainloop()