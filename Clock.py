from tkinter import *
from time import *

#Updates the time, day and date every 1 second
def update():
    
    """
    %I will display the time in the 12 hour-clock
    %M will display the Minute as a decimal
    %S will display the seconds as a decimal
    %p will display the local equivalent of either AM or PM
    """
    timeStr = strftime("%I:%M:%S %p")
    timeLabel.config(text=timeStr)

    #Displays Locale's full week name
    dayStr = strftime("%A")
    dayLabel.config(text=dayStr)

    """
     %B will display Locale's full month name
     %d will display Day of the month as a decimal
     %Y will display Year with century as a decimal
    """
    dateStr = strftime("%B %d, %Y")
    dateLabel.config(text=dateStr)

    window.after(1000,update)

#Initializes the window
window = Tk()
window.title("CLOCK")

#Creates the clock title label which displays Digital Clock
clock_Title = Label (window, text= "Digital Clock", font=("Arial",25,"bold"), fg="#c7732a", height= 2)
clock_Title.pack()

#Creates the time label which displays the current time
timeLabel = Label(window,font=("Arial",60),fg="white",bg="black")
timeLabel.pack()

#Creates the day label which displays the current day
dayLabel = Label(window,font=("Arial",25,"bold"),fg="#c7732a")
dayLabel.pack()

#Creates the date label which displays the current date
dateLabel = Label(window,font=("Arial",30))
dateLabel.pack()

update()

window.mainloop()
