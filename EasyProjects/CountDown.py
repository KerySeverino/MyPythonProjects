#A countdown timer 

#time library
import time
import datetime

#GUI library
from tkinter import *

# Creates the GUI
root = Tk()

#Sets the Title of the GUI as well as size in Height x Width
root.title("TIMER")
root.geometry("350x200")
lbl = Label (root, text = "You there?")
lbl.grid()

#Executes Tkinder
root.mainloop()

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