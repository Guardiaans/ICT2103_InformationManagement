import components.launch as launch
import components.main_menu as mm
import components.utils as ut
import time as t

opened = True
#main application function
def authenticate():

    launch.begin()
    launch.access(launch.option)

    if(launch.granted):
        authenticated = True
        print(f"Welcome {launch.name} !") 
        t.sleep(1)
        return 


if __name__ == '__main__':
    authenticated = False
    print(authenticated)
    while(opened):
        if authenticated == False:
            authenticated = authenticate()
            print(authenticated)
        else:
            print("Im here") 
            #mm.mainMenu()


