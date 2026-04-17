def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
def exponent(p,q):
    return p**q
def floordiv(p,q):
    return p//q
print("a = add\nb = subtract\nc = multiply\nd = divide\ne = exponent\nf = floordiv")
Y = str(input("This is a calculator, please select option: "))
num1 = int(input("Choose a number 1: "))
num2 = int(input("Choose a number 2: "))
if Y == "a":
    print(num1, "+" ,num2, "=" ,add(num1,num2))
elif Y == "b":
    print(num1, "-" ,num2, "=" ,subtract(num1,num2))
elif Y == "c":
    print(num1, "*" ,num2, "=" ,multiply(num1,num2))
elif Y == "d":
    print(num1, "/" ,num2, "=" ,divide(num1,num2))
elif Y == "e":
    print(num1, "**" ,num2, "=" ,exponent(num1,num2))
elif Y == "f":
    print(num1, "//" ,num2, "=" ,floordiv(num1,num2))
else:
    print("This is an invalid input")


