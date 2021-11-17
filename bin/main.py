import components.Launch as launch
#import components.utils as ut

#main application function
def main():

    while(1):
        launch.begin()
        launch.access(launch.option)

        if(launch.granted):
            ut.screen_clear()
            break

    print(f"Welcome {launch.name} !")
    print("### Application functions to be constructed ###")

if __name__ == '__main__':
    main()


