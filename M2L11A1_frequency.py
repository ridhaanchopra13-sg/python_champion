string = str(input("What is the string you want to enter: "))
char = str(input("Name a character you want to use: "))
i = 0
j = 0
while i < len(string):
   if (string[i] == char):
      j = j+1
   i = i+1
print("This character",char,"occured in",string, j,"times")