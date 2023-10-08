#A countdown timer app

#Time library
import time
import datetime

#GUI library
from tkinter import *

# Creates the GUI
window = Tk()

#Sets the Title of the GUI as well as size in Height x Width
window.title("TIMER")
window.geometry("280x250")

label1 = Label (window, text= "Hello, please enter timer in seconds: ", height= 2, width= 30).grid()
label2 = Text (window, height= 2, width= 30).grid()
label3 = Button(window, padx=20 , pady=20).grid()

#Executes Tkinder
window.mainloop()

# my_timer = int(input("Please enter the time in seconds: "))
# my_date = datetime.datetime.now()

# #range(my_timer, 0, -1) reverses the countDown, so it starts from the highest time first and counts down
# for countDown in range(my_timer, 0, -1):
#     seconds = countDown % 60
#     minutes = int(countDown / 60) % 60
#     hours = int(countDown / 3600)
#     #seconds:02 - 02 basically adds 0 as padding, every if the digit is not 2
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")

#     #Makes the countdown wait 1 second before printing
#     time.sleep(1)

#     print("CLOCK: TIME'S UP!!!"+ " - " + my_date.strftime("%c"))