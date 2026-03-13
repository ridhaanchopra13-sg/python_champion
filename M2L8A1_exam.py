medical_cause  = input("Does students have medical problem? (Y/N)")
if medical_cause == "Y":
    print("You are allowed")
else:
    attendance = int(input("What is your attendace"))
    if attendance<75:
        print("You are not permitted for this exam")
    else:
        print("You are allowed")