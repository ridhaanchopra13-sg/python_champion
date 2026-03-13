print("Select your ride: ")
print("1. Bike")
print("2. Car")
choice = int(input("Enter your choice: "))
if(choice == 1): 
    print("what type of bike?")
    print("1.BMX\n")
    print("2.Scooter\n")
    choice2=int(input("Enter you choice2: "))
    if choice2 == 1: 
        print("you have selected BMX")
    else:
        print("you have selected scooter")
elif (choice == 2):
        print("what type of car?")
        print("1.Lamborghini\n")
        print("2.Sidan\n")
        choice3=int(input("Enter yout choice3: "))
        if choice3 == 1:
             print("You have selected lamborghini")
        else:
             print("You have selceted sudan")
else:
    print("Wrong choice")
