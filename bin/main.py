import components.authenticate as auth
import components.main_menu as mm
import components.utils as ut
import components.dbconnection as db
import time as t

opened = True
#main application function
def authenticate():

    auth.begin()

    if auth.option == 'Exit':
        return 'exit'

    else:
        auth.access(auth.option)
        if(auth.granted):
            print(f"Welcome {auth.name} !") 
            t.sleep(1)
            return True

    return False

if __name__ == '__main__':
    authenticated_status = False

    try:
        while(opened):
            if authenticated_status == False:
                authenticated_status = authenticate()
                print(authenticated_status)
                if authenticated_status == 'exit':
                    break
            else:
                #print("Im here")
                opened = mm.mainMenu()

                if opened == False:
                    print("No need to refresh")
                else:
                    t.sleep(3)
                    print("In main loop")
                    print('refreshing')
                    t.sleep(3)

            print("Program Exited")

    except:
        print("Unexpected Error! ")
    

    
            


