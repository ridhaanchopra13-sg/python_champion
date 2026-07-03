class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called")
def Create_object():
    print("Making object...")
    obj = Employee()
    print("Function end...")
    return obj
print("Calling Create_object() function...")
obj = Create_object()
print("Program end...")