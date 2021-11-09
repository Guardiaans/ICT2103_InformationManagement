import inquirer
import os
from time import sleep
# import sys
# sys.path.insert(1, 'C:/Users/angyi/Documents/GitHub/ICT2103_InformationManagement/bin')

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

granted = False
#application launch
def view(value):
    global option
    if value == 0:
        print("""
            _________________________________________________________________________
            |                                                                       |
            |   Welcome to OKFINANCE Management! Please read me before proceeding   |
            |_______________________________________________________________________|
    """)
    #only given two choice
    #inquirer import function
        option = inquirer.list_input("Login or Register?",
                              choices=['Login', 'Register'])
    elif value == 2:
        option = inquirer.list_input("Manage Budget:",
                                     choices=['View Budget', 'Create Budget'])
    elif value == 1:
        option = inquirer.list_input("Main Menu:",
                                     choices=['Manage Budget'])
    elif value == 3:
        print("All your budget are here!")
        option = inquirer.list_input("Exit?",
                                     choices=['Exit'])
    elif value == 4:
        print("Create your budget are here!")
        option = inquirer.list_input("Exit?",
                                     choices=['Exit'])

# def managebudgetbegin():
#     option = inquirer.list_input("View or Create?",
#                                  choices=['View Budget', 'Create Budget'])


# def mainmenubegin():
#     option = inquirer.list_input("Manage Budget?",
#                                  choices=['Manage Budget'])
# def index(number):
#     global indexed
#     if number == 0:
#         indexed = 0
#     elif number == 1:
#         indexed == 1
#     elif number == 2:
#         indexed == 2

def access(option1):
    global name
    if(option1=="Login"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        #function to check login credentials
        login(name,password)
    elif(option=="View Budget"):
        screen_clear()
        while (1):
            view(3)
            access(option)
            break
    elif(option1 == "Manage Budget"):
        screen_clear()
        while(1):
            view(2)
            access(option)
            break
    elif(option1 == "Create Budget"):
        screen_clear()
        budget = input("Enter the values: ")
        createbudget(budget)
        while(1):
            view(4)
            access(option)
            break
    elif(option1=="Register"):
        print("Enter your name and password to register")
        #TODO: Needs validation here
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        register(name,password)


#function to determine application access
def appaccess():
    global granted
    granted = True


#login functon
def login(username,password):
    #login session
    success = False
    #open file to read data
    file = open("credentials.txt","r")
    for data in file:
         usr,pw = data.split(",")
         #strip to remove quotation from password
         pw = pw.strip()
         if(usr==username and pw==password):
             success = True
             break
    file.close()
    if(success):
        print("\t\t\tLogin Successfully")
        appaccess()
    else:
        screen_clear()
        print("Invalid Username or Password!")
        
def register(name,password):
    file = open("credentials.txt","a")
    file.write("\n"+name+","+password)
    print("\t\t\tUser registered successfully!")

def createbudget():
    sql = "Sql start"
    if sql:
        sql_stuff = "Insert into db"
    else:
        print("An error has occured")


def dashboard(sql_object):
    sql = sql_object
    if sql:
        balance_sql = "Enter sql statement here"
    else:
        print("An error has occured")

#main application function
def main():
    while(1):
        view(0)
        access(option)
        if granted:
            screen_clear()
            break
    # print(f"Welcome {name} !")
    # print("### Application functions to be constructed ###")
    while(1): # main menu
        view(1)
        access(option)
        break
    # while(2):
    #     view(2)
    #     access(option)
    #     break


if __name__ == '__main__':
    main()


