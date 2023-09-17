#Welcome to a fun number guessing game, In this game, you get to choose the range for a randomly generated number and test your luck!
import random

user_inputX = int(input("Please enter the starting number for the range: "))
user_inputY = int(input("Please enter the ending number for the range: "))

scrambledTheNumbers = random.randrange(user_inputX,user_inputY + 1)

user_inputAnswer = int(input("Enter your guess number!:"))

if(user_inputAnswer == scrambledTheNumbers):
    print("You Win! You guessed: ", user_inputAnswer)
    print("The number was: ", scrambledTheNumbers)
else:
    print("You Lose! You guessed: ", user_inputAnswer)
    print("The number was: ", scrambledTheNumbers)
