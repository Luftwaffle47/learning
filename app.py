command = ""
started = False
crash  = False
while command.lower() !='quit':
    command = input("> ").lower()
    if command=='start':
        if crash:
            print("Well, your engine block is busted")
        started = False

        if started:
            print("Your engine begins to skip as you attempt to start while the engine is running")
        else:
            started = True
            print("Car started.....")

    elif command=="stop" :
        if crash:
            started = False
            print("I don't know what to tell you, but you're stopped already but not by choice")

        if not started:
            print("You press on the breaks harder in vain, for the vehicle is already stopped")
        else:
            started = False
            print("Car Stopped")
    elif command == "crash":
        if crash == True:
            print("Wow another vehicle hit you somehow.... ")
        else:
            crash = True
            print("You somehow hit the only tree in the parking lot.....")


    elif command == "help":
        print('''
        start- to start the car
        stop- to stop the car
        quit- to quit the game
        crash- ded''')
    elif command == "quit":
        break
    else:
        print("Sorry I dont quite understand")

