import components.authenticate as auth
import components.main_menu as mm
import components.utils as ut
import components.dbconnection as db
import inquirer as iq
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
                    emailadd = iq.text(message="Enter your email")
                    password = iq.password(message='Please enter your password')

                    authenticated_status = auth.verifyCredentials(emailadd, password)
                    #load profile
                    t.sleep(1)

                elif choice == 'Register':
                    #method to register user into database
                    print("Enter your credentials to register")
                    username = iq.text(message="Enter your username")
                    password = iq.password(message='Please enter your password')
                    emailadd = iq.text(message="Enter your email")
                    bank = iq.text(message="Enter your main Bank name")

                    print(f'''
                    Please confirm your registration

                    USERNAME           : {username}
                    PASSWORD           : {password}
                    EMAIL              : {emailadd}
                    BANK ORGRANISATION : {bank}
                    ''')

                    menuoption = iq.list_input(message=f"Select an option",
                              choices=['Confirm','Cancel'
                              ])

                    if menuoption == 'Confirm':
                        authenticated_status = auth.register(username, password, bank, emailadd)
                    else:
                        print("Returning back to menu..")
                        t.sleep(1)
                        pass

                else : 
                    break
                
                #print(f"What is the status in main loop?: {authenticated_status}")

            else:

                opened = mm.mainMenu(emailadd)
                
                if opened == False:
                    print("Goodbye!")
                elif opened == 'Logout':
                    authenticated_status = False
                else:
                    print('refreshing')
                    t.sleep(1)

        print("Program Exited")

    except:
        print("Unexpected Error! ")
    

    
            


