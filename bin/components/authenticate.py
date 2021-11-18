import inquirer as iq
import components.utils as ut

granted = False
#application launch
def begin():
    global option
    print("""
            _________________________________________________________________________
            |                                                                       |
            |                  Welcome to OKFINANCE Management!                     |
            |_______________________________________________________________________|
    """)
    #only given two choice
    #inquirer import function
    option = iq.list_input("Login or Register?",
                              choices=['Login', 'Register', 'Exit',])

def access(option):
    global name
    if(option=="Login"):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        #function to check login credentials
        login(username,password)
    else:
        print("Enter your name and password to register")
        #TODO: Needs validation here
        username = input("Enter your name: ")
        password = input("Enter your password: ")
        register(username,password)

#function to determine application access
def appaccess():
    global granted
    granted = True

#login functon
def login(username,password):
    #login session
    success = False
    #open file to read data
    try:
        file = open("../bin/credentials.txt","r")
    except:
        print("File cannot be opened!")
        
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
        ut.screen_clear()
        print(f"\n\n\t\t\t\t{ut.bcolors.FAIL}Invalid Username or Password!{ut.bcolors.ENDC}")
        
def register(name,password):
    file = open("credentials.txt","a")
    file.write("\n"+name+","+password)
    print("\t\t\tUser registered successfully!")
