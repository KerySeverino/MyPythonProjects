#A simple calculator with no GUI, it should be improved in the next project. 
#Features: Sum, Substraction, Multiplication, Division

#Storing the user input into two variables
flag = True;
user_inputX = float(input("Please enter a number: "))
user_inputY = float(input("Please enter another number: "))

#Defining the next math steps and returning it
def sum(user_inputX, user_inputY): return print("Total: ", user_inputX + user_inputY);
def subs(user_inputX, user_inputY): return print("Total: ", user_inputX - user_inputY);
def mul(user_inputX, user_inputY): return print("Total: ", user_inputX * user_inputY);
def div(user_inputX, user_inputY): return print("Total: ", user_inputX / user_inputY);

#Asking the user what he/she wants to do
user_inputAnswer = str(input("Sum, Substraction, Multiplication or Division? "))

#Checking for a valid answer, if not it will ask again 
while flag == True:
    if(user_inputAnswer == "Sum" or user_inputAnswer == "SUM"):
        flag = False
        sum(user_inputX, user_inputY)
    elif(user_inputAnswer == "Substraction" or user_inputAnswer == "SUBSTRACTION"):
        flag = False
        subs(user_inputX, user_inputY)
    elif(user_inputAnswer == "Multiplication" or user_inputAnswer == "MULTIPLICATION"):
        flag = False
        mul(user_inputX, user_inputY)
    elif(user_inputAnswer == "Division" or user_inputAnswer == "DIVISION"):
        flag = False
        div(user_inputX, user_inputY)
    else:
        print("Please enter a valid answer...Sum, Substraction, Multiplication, Division.")
        #Asking the user what he/she wants to do again
        user_inputAnswer = str(input("Sum, Substraction, Multiplication or Division? "))