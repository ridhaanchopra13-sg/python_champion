
answer = str(input("Are you sure you want to shutdown? Yes or No: "))   
if answer == "Yes":
    exit()
elif answer == "No":
    print("Abort shutdown")
else:
    print("Sorry.")