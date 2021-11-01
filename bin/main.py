import inquirer
import os
from time import sleep

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

granted = False
#application launch
def begin():
    global option
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

def access(option):
    global name
    if(option=="Login"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        #function to check login credentials
        login(name,password)
    else:
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
        print(f"\n\n\t\t\t\t{bcolors.FAIL}Invalid Username or Password!{bcolors.ENDC}")
        
def register(name,password):
    file = open("credentials.txt","a")
    file.write("\n"+name+","+password)
    print("\t\t\tUser registered successfully!")


#main application function
def main():

    while(1):
        begin()
        access(option)

        if(granted):
            screen_clear()
            break

    print(f"Welcome {name} !")
    print("### Application functions to be constructed ###")

if __name__ == '__main__':
    main()


