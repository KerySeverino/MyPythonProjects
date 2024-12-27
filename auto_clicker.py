import pyautogui # pip3 install pyautogui
import time
import threading
from pynput import keyboard # pip3 install pynput

# Variables
running = False
delay = 0.1

# DEFs
def clicker():
    while running:
        pyautogui.click()
        time.sleep(delay)

def start_clicker():
    global running
    if not running:
        running = True
        threading.Thread(target=clicker).start()
        print("Auto clicks started")

def stop_clicker():
    global running
    running = False
    print("Auto clicks stop")

def on_press(key):
    global running
    try:
        if key.char == 's':  # Start clicking
            if not running:
                running = True
                threading.Thread(target=clicker, daemon=True).start()
                print("Auto clicker started!")
        elif key.char == 'e':  # Stop clicking
            running = False
            print("Auto clicker stopped!")
        elif key.char == 'q':  # Quit program
            running = False
            print("Exiting program...")
            return False  # Stop listener
    except AttributeError:
        pass

def main():
    print("\n Auto clicker \n")
    print("Commands:")
    print("'s' to start, 'e' to stop, 'q' to quit \n")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
   
# Runner
if __name__ == "__main__":
    main()