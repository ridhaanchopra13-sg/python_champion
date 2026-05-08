valid = False
while not valid:
    try:
        n = int(input("Enter a number: "))
        if n % 2 == 0:
            print("bye")
        else:
            print("The number is odd")
        valid = True
    except ValueError:
        print("Invalid")