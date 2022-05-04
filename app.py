command = ""
started = False
while command.lower() !='quit':
    command = input("> ").lower()
    if command=='start':
        if started:
            print("Your engine begins to skip as you attempt to start while the engine is running")
        else:
            started = True
            print("Car started.....")

    elif command=="stop" :
        if not started:
            print("You press on the breaks harder in vain, for the vehicle is already stopped")
        else:
            started = False
            print("Car Stopped")

    elif command == "help":
        print('''
        start- to start the car
        stop- to stop the car
        quit- to quit the game''')
    elif command == "quit":
        break
    else:
        print("Sorry I dont quite understand")

