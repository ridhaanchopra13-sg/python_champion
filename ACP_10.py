n = int(input("Enter how many calculations you want to perform: "))

for i in range(n):
    base = int(input("Enter base number: "))
    exponent = int(input("Enter exponent: "))

    answer = base ** exponent
    
    print("Answer is:", answer)