class IOString:
    def __init__(self):
        self.str1 = ""
    def get_String(self):
        self.str1 = str(input("Enter a string: "))
    def print_String(self):
        print("The string is: ",self.str1.capitalize())
object = IOString()
object.get_String()
object.print_String()