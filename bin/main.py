import components.authenticate as auth
import components.main_menu as mm
import components.utils as ut
import components.dbconnection as db
# from components.authenticate import emailadd
import time as t

opened = True
emailadd = ""


#main running loop here.
if __name__ == '__main__':

    authenticated_status = False

    try:
        while(opened):
            #verify user first
            if authenticated_status == False:
                
                choice = auth.launchAuthenUI()

                if choice == 'Login':
                    #User Input
                    print("Enter your email and password to login")
                    emailadd = input("Enter your email address: ")
                    password = input("Enter your password: ")

                    authenticated_status = auth.verifyCredentials(emailadd, password)
                    #load profile
                    t.sleep(2)

                elif choice == 'Register':
                    #method to register user into database
                    print("Enter your credentials to register")
                    username = input("Enter your name: ")
                    password = input("Enter your password: ")
                    email = input("Enter your email: ")
                    bank = input("Enter the bank you are using: ")

                    auth.register(username, password, bank, email)

                else : 
                    break
                
                print(f"What is the status in main loop?: {authenticated_status}")

            else:

                opened = mm.mainMenu(emailadd)
                
                if opened == False:
                    print("No need to refresh")
                else:
                    print('refreshing')
                    t.sleep(3)

        print("Program Exited")

    except:
        print("Unexpected Error! ")
    

    
            


