number = int(input("Enter number: "))

if number == 0:
    print("1")
else:
    digits = 0
    while number != 0:
        digits = digits + 1
        number = number // 10

    print(digits)