#Welcome to a fun number guessing game, In this game, you get to choose the range for a randomly generated number and test your luck!
import random

flag = True;

#Starts the game
def gameStart():
    #Storing the user input into two variables
    user_inputX = int(input("Please enter the starting number for the range: "))
    user_inputY = int(input("Please enter the ending number for the range: "))

    #Storing the random generate number in a variable
    #user_inputY + 1: includes the endind number in the range
    scrambledTheNumbers = random.randrange(user_inputX,user_inputY + 1)

#Getting the user guess answer
user_inputAnswer = int(input("Enter your guess number: "))

#Continues to check until flag is false
while flag == True:
    #Checks if the user-input is [equal] to the random number
    if(user_inputAnswer == scrambledTheNumbers):
        flag = False
        print("You Win! You guessed: ", user_inputAnswer)
        print("The number was: ", scrambledTheNumbers)

    #Checks if the user-input is [no equal] to the random number
    elif(user_inputAnswer != scrambledTheNumbers):
        print("You Lose! You guessed: ", user_inputAnswer)
        print("The number was: ", scrambledTheNumbers)
        #Ask the user if they want to try again
        user_inputRestart = str(input("Do you want to try again? Please enter [Yes] or [No]: "))

        #Checks the user respond when restarting the game, if yes the game restarts, if no the game stops 
        if(user_inputRestart == "Yes" or user_inputRestart == "[Yes]"):
            gameStart();
            user_inputAnswer = int(input("Enter your guess number!: "))
        elif(user_inputRestart == "No" or user_inputRestart == "[No]"):
            flag = False
            print("Thanks for playing!")
        else:
            #Checks if the answer is valid
            print("Please enter a valid answer")
            user_inputRestart = str(input("Do you want to try again? Please enter [Yes] or [No]"))
        
        
